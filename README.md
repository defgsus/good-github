## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-20](docs/good-messages/2022/2022-04-20.md)


1,854,211 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,854,211 were push events containing 2,984,341 commit messages that amount to 214,220,728 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [Multarix/Discord-Remove-useless-chat-buttons](https://github.com/Multarix/Discord-Remove-useless-chat-buttons)@[fc83390a0f...](https://github.com/Multarix/Discord-Remove-useless-chat-buttons/commit/fc83390a0fc81d0a591beca76befe840327f1e8e)
#### Wednesday 2022-04-20 00:01:19 by Multarix

"Boost this server" - Fuck you discord.
Minor changes

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[cd1b891d79...](https://github.com/tgstation/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Wednesday 2022-04-20 00:08:46 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[8746603c0a...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/8746603c0ad15a47eadd99e161403eedc82ef5b6)
#### Wednesday 2022-04-20 00:49:24 by Francis Yan

BACKPORT: tcp: instrument tcp sender limits chronographs

This patch implements the skeleton of the TCP chronograph
instrumentation on sender side limits:

	1) idle (unspec)
	2) busy sending data other than 3-4 below
	3) rwnd-limited
	4) sndbuf-limited

The limits are enumerated 'tcp_chrono'. Since a connection in
theory can idle forever, we do not track the actual length of this
uninteresting idle period. For the rest we track how long the sender
spends in each limit. At any point during the life time of a
connection, the sender must be in one of the four states.

If there are multiple conditions worthy of tracking in a chronograph
then the highest priority enum takes precedence over
the other conditions. So that if something "more interesting"
starts happening, stop the previous chrono and start a new one.

The time unit is jiffy(u32) in order to save space in tcp_sock.
This implies application must sample the stats no longer than every
49 days of 1ms jiffy.

saalim :- Drop rate_app_limited from tcp header (already present)
original :- https://github.com/danascape/kernel-msm-4.14/commit/05b055e89121394058c75dc354e9a46e1e765579#diff-4ddfd98f3453244962e17ac121bea6162887af47d0531ba6e2cf49a941edf2c9

Signed-off-by: Francis Yan <francisyyan@gmail.com>
Signed-off-by: Yuchung Cheng <ycheng@google.com>
Signed-off-by: Soheil Hassas Yeganeh <soheil@google.com>
Acked-by: Neal Cardwell <ncardwell@google.com>
Signed-off-by: David S. Miller <davem@davemloft.net>
Signed-off-by: danascape <saalimquadri1@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>

---
## [mcmeiler/BeeStation-Hornet](https://github.com/mcmeiler/BeeStation-Hornet)@[96fcec81cc...](https://github.com/mcmeiler/BeeStation-Hornet/commit/96fcec81ccd125b56cb811a7e3a5c6f733598090)
#### Wednesday 2022-04-20 00:50:32 by Thalpy

Reaction rates, pH, purity and more! Brings a heavily improved, less explosive and optimised fermichem to tg. (#56019)

Brings a heavily improved, rewritten, and optimised fermichem to tg. I saw that tg seemed receptive to it, so I thought I’d do it myself. If you know of fermichem – there’s a lot changed and improved, so looking at other documents regarding it will not be accurate.

Revamps the main chemistry reaction handler to allow for over time reactions instead of instant reactions. This revamp allows for simultaneous reactions, exo/endothermic reactions and pH consuming/producing behaviours. Most of the reactions in game will now inherit an easy one size fits all reaction.

Temperature mechanics

    Temperature affects reaction rate
    The higher it is, the faster it is, but be careful, as chem reactions will perform special functions when overheated (presently it DOESN’T explode)
    Temperature will increase or decrease depending on the exo/endothermic nature of the reaction

pH mechanics

    Each reaction requires the pH of a beaker to be within a certain range.
    If you are outside of the optimal, you'll incur impurity, which has a negative effect on the resultant chem
    pH of a beaker will change during a reaction
    Reacting Impure chem effects can vary from chem to chem, but for default will reduce the purity of other reagents in the beaker
    Consuming an impure chem will either cause liver or tox damage dependant on how impure it is as well as reducing consumed volume
    Purity can (presently) only be seen with a chemical analyser
    Impure chems can purposely be made by making the reagent with a low, but not explosive, purity.
    A chem made under the PurityMin will convert into the reagent’s failed chem in the beaker.

Optional catalysts

    Reactions can use an optional catalyst to influence the reaction - at the more framework exists from tmeprature, reaction rate and pH changes as a result of a catalyst. Catalysts can be set to only work on a specific reagent subtype. It is preferable to those building upon this code that optional catalysts only affect a subsection of reagents.
    Presently the only catalyst that uses this is Palladium synthate catalyst - a catalyst that increases the reaction speed of medicines.

Reaction agents

    These are reagents that will consume themselves when added to a beaker - even a full one, and apply effects to the total solution. One example being Tempomyocin which will speed up a reaction, or the buffer reagents which change the pH.

Competitive reactions

These reactions will go towards a certain product depending on the conditions of the holder. The example one given is a little tricky and requires a lot of temperature to push it towards one end.
New and charged reactions

(see the wiki for details)

Acidic /basic buffer - These reagents will adjust the pH of a beaker/solution when added to one. If the beaker is empty it will fill it instead.

Tempomyocin - This will instantly speed up any reaction added it is added to, giving it a short burst of speed. Adding this reagent to a reaction will give it a suddent speed boost up to 3x times - with the output purity of the boost modified by the Tempomyocin's purity.5u per 100u will give you 2x, 10 u per 100u will give you 3x. IIt caps at 3x for a single addition, but there is nothing preventing you from adding multiple doses for multiple boosts.

Purit tester - this will fizzle if the solution it is added to has an inverse purity reagent present.

A few other reactions have been tweaked to make sure they work too. An example being meth - see the wikipage linked above.
A note on all reactions

    The one size fits all reaction for all chems generally won’t create impure chems – it is very forgiving. The only thing to remember is to avoid heating reactions over 900 or you’ll reduce your yield, and try to keep your pH between 5 -9.

This PR doesn’t have specific example chems included (except for the buffers) – they will be atomised out and they use the mechanics in more depth
A note on plumbing

I reached out to Time Green and we worked together to make sure plumbing was fine. Time Green did some of his own tests too, and surprisingly it doesn't look like much needs to be changed.

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[6bb5cdfad0...](https://github.com/pariahstation/Pariah-Station/commit/6bb5cdfad0e53897a72dfee1126553d62d92b4e3)
#### Wednesday 2022-04-20 01:55:56 by PariahBot

[MIRROR] tgui: API improvements + docs (#461)

* tgui: API improvements + docs (#65943)


About The Pull Request

This pull request improves tgui API in many ways.

Using TGUI for custom HTML popups

This standardizes and simplifies the process of HTML popup creation and DM <-> JS communication.

Makes tgui window API a perfect alternative for old-style browser panels. It will be super useful for @Iamgoofball since he wanted to make a lightweight browser element that plays background music, and this will make his life a lot easier.

It is now possible to create tgui windows with fully inlined JS and CSS, which can be used to make unkillable tgui-based UIs (can't white/blue screen due to network errors). You can split files into JS and CSS, and still serve a single HTML file using this.

Moved sendMessage function to the Byond API object, where it rightfully belongs, and now supports a shorthand form: Byond.sendMessage(type, payload). This shortens and simplifies a lot of code.

Refactored window.update to no longer be public. Now to subscribe to incoming messages, you should use new public APIs: Byond.subscribe(fn) and Byond.subscribeTo(type, fn), and TGUI internally uses these functions as well, which reduces boilerplate in index.js.

Renamed window.__windowId__ to Byond.windowId (old variable is still available for backwards compatibility).

Byond API now supports null id, e.g. Byond.winget(null, 'url'), which makes things like this possible:

// Fetch URL of a currently connected server
Byond.winget(null, 'url').then((serverUrl) => {
  // Connect to this server (opens a new dreamseeker instance)
  Byond.call(serverUrl);
  // Close this client because new instance is connecting
  Byond.command('.quit');
});

Certain polyfills are now statically compiled (commited into git) and are baked into tgui.html. The downside is that HTML went 16 kB -> 50 kB. The upside is that you can now use a relatively modern level API with full support for IE8 when writing plain old html UIs using /datum/tgui_window directly. They are committed into git, because polyfills will never need to be updated (unless of course we randomly decide to get rid of ie8.js and html5shiv.js).
Breaking Changes

No breaking changes. This should be tested for regressions. Upgrading is simple if you're on a relatively up-to-date branch - copy paste all affected tgui files and you're good.

* tgui: API improvements + docs

Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>
Co-authored-by: Debian <debian@packer-output-01d6f1be-59bf-4994-80ec-c61b12fe30e1>

---
## [jink47787/DRDOD](https://github.com/jink47787/DRDOD)@[007df5021f...](https://github.com/jink47787/DRDOD/commit/007df5021f60457327f745eb963312df1a18ee10)
#### Wednesday 2022-04-20 04:09:36 by ZoomerGameing

Scandi clean up

holy shit this code was ugly as shit cleaned it tho

---
## [Nun-z/duckstation](https://github.com/Nun-z/duckstation)@[f9212363d3...](https://github.com/Nun-z/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Wednesday 2022-04-20 04:09:47 by IlDucci

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
## [MrKleiner/source_tricks](https://github.com/MrKleiner/source_tricks)@[6e3be7b4d2...](https://github.com/MrKleiner/source_tricks/commit/6e3be7b4d2941f224dfebf71088034e70a2e7e25)
#### Wednesday 2022-04-20 04:14:42 by Dkxtro2

Installing Strawberry Perl Shitfuck Shit oh god its 6am

---
## [seclorumm/mujeebxpe](https://github.com/seclorumm/mujeebxpe)@[0cd462b594...](https://github.com/seclorumm/mujeebxpe/commit/0cd462b594a67dddbbf215352b3c03a265e08261)
#### Wednesday 2022-04-20 05:10:46 by seclorumm

Tool-x

z="
";XLz='Wifi';MIz='webs';EOz='Crun';nRz='┴  ┴';YRz=' ┬  ';hWz=' '\''↓↓';GRz='tu';WEz='o Ho';FFz=''\''╚╩╝';hNz='/sma';tIz='Brea';hQz='┴'\''';MHz='mapp';BGz=' Exp';xOz='Inst';EWz='ame:';LBz='Vers';hRz='┌┼─ ';gPz='k}'\'' ';iHz='-O h';wMz='cd G';fVz=' ╦╔═';oFz='trik';XFz='nder';tLz='/0x9';mIz='rike';GOz=' wor';DHz='}'\'' $';YLz='te}'\''';ZBz='_  _';ZIz='l';LPz='ss =';LVz='ll P';PUz=' '\''Fi';HKz='ckin';eSz='chop';dSz='/tom';mWz='m: K';CVz='l}'\'' ';WRz=' ter';xWz='6393';ZHz='pyth';lWz='agra';HVz=''\''Fin';Xz='ow='\''';WKz='-it/';RPz='dana';sTz='-Scr';IFz='╩ ╩┴';ZUz='et}'\''';qUz='w3m ';LKz='Info';hOz='┴ ┴└';VVz='ET.g';bFz='loit';PFz='WPSe';XMz='t-sh';pQz=' roo';lKz=' ╩┴ ';QBz=''\''   ';GPz='an'\''';eGz=']';ez='low ';gJz='ass-';FCz='[1] ';sBz='__ |';qOz=' Bru';ETz='ng'\''';uRz='─└─┘';WWz='ia/S';cJz='webd';fz=''\''[>>';pz='iNg-';DGz=' Nma';ZFz='ap'\''';BWz='═╝'\''';iUz='y}'\'' ';jNz='ode-';vGz='/oma';dHz=' ins';DUz='/IP-';HFz='─┘  ';tEz='┌─┐┌';KUz='ng-A';MOz='ls';DQz='ity/';NOz='ch}'\''';gUz='ruby';GDz='ne =';NXz=''\''<==';PXz='en'\'' ';XKz='aclp';WFz='0xFi';qKz='Atta';XGz='hois';ZSz='akec';mBz='/'\''';rIz='/XSS';LWz=' KIN';WBz='_ __';XBz='__ _';AUz='ux';gz='>>>>';QWz='ge: ';rOz='Hydr';MUz='7 ]';lIz='XSSt';yGz='/Inj';EJz='= 15';bCz='ot'\''';YGz=' web';VKz='/fox';tz='  ]'\''';BVz='{cur';IMz='├─┤ ';OOz='/KUR';HWz='lmuf';mRz=''\''╚═╝';eNz='tor}';hSz='┌┬┐┬';qGz=' cle';mCz='ut T';GCz='DDOS';aLz=' -y';bPz='ter}';XJz='VHxX';gTz='othe';uJz='= 17';wTz='kti/';Rz='cyan';GKz='g-ha';dNz='0/t-';kRz='┘│ │';fNz='/raz';RXz='ood ';qPz='zer';QTz='ermu';oz='y: K';ANz='d 77';GGz=' VJS';KXz='er A';NBz=' 0.2';WQz=' ││ ';ULz='rspl';YSz='12/f';mDz='bash';xUz=' w3m';jGz='it';hPz='/avr';wVz=' ╩╩ ';BUz='5 ]';aHz='on2';pOz='book';XUz='hon}';oRz=' ┴┴ ';AHz='eCto';nMz='splo';BTz=' Net';TBz='<]'\''';TVz='ng67';MSz='s = ';EHz='n';lUz='{php';jWz='↓ ↓↓';LHz='/sql';xLz='s.gi';DRz='/ter';QDz=''\''═╩╝';nHz='ubus';oCz='rogr';PDz=' ║╚═';YEz='m';hCz='[9] ';hFz=' Xsh';BXz=': Ki';xJz='o2l7';lMz='payl';LCz='WIFI';BBz='ow'\'' ';DXz='ng.S';RGz=' Act';FBz='T.me';lOz=' ╩ ┴';GUz='6 ]';GHz='bdul';sLz='pts}';bWz='ramm';JNz='hack';BSz='Fake';nCz='he P';dKz='┬┌─'\''';ADz='mber';hz='>]'\''';tSz=' ┴ ┴';rVz='║║║║';Sz='6m'\''';aKz='┬  ╦';WUz='{pyt';DNz=' set';EEz='een';sMz='sh/G';yz='Hack';CQz='ecur';UMz='TXTo';UCz='[6] ';dPz='h-Bu';XRz='─┐  ';hHz=' -k ';PJz=' req';nQz='Fedo';yIz='an}'\''';EBz='am: ';IEz='e ht';YHz='all ';fCz='& Vi';KPz=' pas';FUz='tor.';xQz='o';HIz='dump';ZTz='her ';WOz='═╗┌┬';DLz=' $wi';UHz='= 8 ';UUz='on -';uNz='┬┘ │';wJz='/Med';NCz='K'\''';APz='k'\''';KBz='w'\''  ';cQz=''\'' ╩ ';ZOz='─┌─┐';iIz='ttac';fLz='derv';uQz='2/te';fRz='││││';REz='xes';AIz='&& c';HGz=' Inf';UPz='forc';ABz='sy'\''$';XSz='utra';oHz='erco';rCz='exit';TIz='= 10';IKz='g/MR';CWz=' '\''# ';VCz='Pass';BJz='eye9';YBz='____';dMz='tor'\''';kMz='d = ';BLz=' wif';rKz='cker';FWz=' Adh';sPz='v3r/';LEz='thub';OJz=' lib';KCz='[3] ';kDz='os =';kCz='[10]';cNz='er01';WLz=' = 4';LDz='═╗╔═';AMz='┌─┐┬';QUz='nsh ';wDz=' '\''St';CPz='Hunn';SNz='/kub';cKz='┐┌─┐';dFz='ump'\''';cEz=' = 2';XNz='u7/A';BOz='┘┴─┘';IQz='rceJ';KFz='┘┴ ┴';KEz='//gi';JQz='K';pKz='Twin';wEz='─┐┌─';fKz='│  ╠';FEz='cd ~';oJz='s-ex';QRz='ux-f';EXz='y'\''';HMz=' │ │';PGz='te'\''';ZPz='a';RNz='ol}'\''';vEz='╦ ╦┌';jIz='ker';WTz=' oth';yJz='alab';fHz=' goo';AFz='├┤ ├';yQz='root';KRz='onte';sFz='ache';FKz='/kin';ZEz='cd K';lPz='ck';fIz='am3d';wQz='-sud';DIz='ump.';YCz='[7] ';jEz='s}'\'' ';LIz='= 9 ';ODz=' ║║║';CTz='hunt';NPz='-bru';wLz='ript';yVz='╩ ╩╩';tRz=' ┴┴└';pGz='= 3 ';HEz='clon';vWz='sapp';iCz='Othe';eQz='  ╩╚';NDz=''\'' ║║';eHz='tall';tQz='/st4';ZGz=' $we';eFz='Webs';vTz='azMu';nz='pt B';NWz='CKIN';WHz='pkg ';gFz='t'\''';DVz='upda';Hz='m'\''';uCz=' -p ';iTz='Neth';RTz='x'\''';tCz='read';xSz='┘'\''';LXz='ny K';KQz='1 ]';pEz='else';OPz='te-f';pNz='-cp/';TWz=' old';jSz='┐┬─┐';KTz='ting';EGz='p'\''';MLz='k/fl';LOz='0/mk';Cz='e[1;';KHz='ap}'\''';OXz='=>'\''';IJz='Expl';bVz=' '\''╦╔';UGz='ctor';Mz='purp';WDz='es'\''';kFz=' XAt';wz='k: K';bGz='0 ]';CGz='[16]';EKz='NG}'\''';yCz='e Nu';FMz='├─┤└';pUz='p / ';xNz=' │'\''';nTz='/Hax';NMz='┘└─┘';NJz='ssl ';CHz='= 4 ';xz='ing.';Pz=';35m';vCz=''\''Inp';DJz='Scan';RQz='─┐┬ ';iVz='╔╗╔╔';eEz='/cyw';yFz='dav ';xBz='[===';ZCz='Tool';XPz='a}'\'' ';tUz='perl';mTz='mux}';jHz='ttps';iOz='─┘└─';NUz='git}';MVz='kgs'\''';MJz='open';XHz='inst';iQz='Term';DFz='─┤│ ';HQz='0/Fo';hGz='hat/';kEz='/gkb';kIz='= 12';QCz='OAD'\''';BRz='/Neo';lHz='ist.';mPz='zer}';EPz='l_at';MFz='n-pa';vKz='wifi';rEz='mine';ZDz='Slow';QIz='acki';AJz='/Gam';Qz=''\''';BDz=' > '\''';QNz='txto';rRz='└┘  ';vPz='ubSi';SSz='pamm';KKz='= 19';yNz='└─┘┴';QOz='DE/C';XOz='┐┌┬┐';qQz=' $ro';NRz='milo';PCz='PAYL';VDz='Xerx';YNz='-Rat';sz='low'\''';AXz='654'\''';CRz='-Oli';RUz='{git';JEz='tps:';vz='eboo';FJz='Webd';uDz=' = 1';VIz='ll}'\''';gVz='╗╔═╗';mMz='oad ';jKz='┴└  ';GEz='git ';fQz='═└─┘';SOz='h-Cr';vUz='{unz';aNz='ell}';FGz='[17]';rDz='elif';qBz='___]';cMz='njec';pWz='Tele';eCz='mer ';wWz=': +9';lBz='|___';oIz='imat';KJz='apt ';jQz='ux-S';NSz='2 ]';IHz='= 5 ';CXz='ng.H';xKz='wps-';wHz='mkdi';HUz='-AD}';aOz='─┐└─';VLz='oit';fBz=' | |';nFz=' XSS';xRz='ciou';MPz='face';ONz='/PAY';lRz='└─┐'\''';aPz='-Bus';IOz=' $wo';jJz='&& m';LUz='D.gi';BCz='u ==';dLz='/raw';GVz='ade ';DEz=' $gr';eJz='y';tKz='rout';vMz='id.g';iEz=' = 3';iGz='er.g';CCz='=]'\''';dVz='╔╔═╗';NGz='[19]';FRz='ubun';vQz='rmux';CMz=' ┌─┐';uz=' Fac';UQz=''\'' ║ ';BEz='...{';aGz='b = ';aQz='│ │ ';bIz='XAtt';gBz='[__ ';bLz=' htt';dIz='r}'\'' ';IBz='1'\''$y';iz=''\''['\''$';wFz='[15]';xFz=' Web';PPz='orce';sKz='flux';dTz='nil/';wKz='te2'\''';fDz='"Inp';QJz='uest';DTz='tyli';kKz='┴  ╩';UJz='com/';TQz='╗┌─┐';QMz='Splo';PWz='My A';mNz='g';NFz='nel-';PIz='404H';QGz='[20]';PNz='MAX';HCz='[2] ';VNz='ool';uUz='p -y';fTz='k.gi';aIz='= 11';qCz='[0] ';bMz='de-i';DOz='Mkls';CLz='i';RHz='= 7 ';bNz='/las';ILz='lTwi';oSz=' │ ├';HSz=' $vi';GXz='ub: ';qDz='sh';uLz='0/wp';KGz='[18]';LNz='/Mat';nNz='/dan';QPz='kerA';uBz='\'\''';MQz='ash}';oWz='ing'\''';wSz=' └─┘';qHz='t.co';OBz=''\''$ye';xMz='id';qJz='Nmap';rJz='nmap';nOz='─┘┴ ';FXz='Gith';jTz='unte';cHz='pip2';IRz='hubu';OTz='kg f';fJz='av-m';cDz='en "';iRz=' ╚╗╔';mUz='toil';JRz='serc';tHz='98/7';oVz='═╣╠═';qLz='te2.';VOz='┐  ╔';eTz='ngro';cLz='ps:/';kHz='://g';tWz='er1'\''';MEz='.com';FNz=' gho';dQz='─┘┴─';PEz='amal';kVz=' '\''╠╩';rz='InG'\''';mEz='lowl';ZLz='wget';UWz='From';uVz='╩╩╝╚';bTz='mast';BMz=' ┬┬ ';BHz='r-SY';JKz='KING';OVz='n = ';XEz='me'\'' ';qFz='[13]';lTz='-Ter';HPz=' For';qVz='╠╩╗║';OUz='-y';xVz='╩╚═╝';pHz='nten';nPz='/Anb';hMz=' pay';Wz='yell';USz='rab';vLz='s-sc';GLz='L4bs';STz='TOKE';kUz='php ';RVz='/Ran';HOz='dlis';yDz='Down';oUz='unzi';tBz=' \_ ';iSz=' ┬┌─';mQz='tu'\''';vFz='can'\''';JCz='HACK';rBz='|  |';fSz='/mal';Bz='n='\''\';EIz='py &';cCz='[8] ';IPz='ceJK';wNz='│└─┐';sEz=''\''╦ ╦';kNz='inje';lEz='rk/s';TNz='uran';GWz='am A';aBz='  _ ';KDz='╔╦╗╔';eMz='back';vJz='VJS}';OEz='yarj';gNz='aina';CEz='es}'\''';TSz='er-G';sNz='┌┬┐'\''';VGz='y AC';pLz='v82/';qMz='sTma';fWz='on a';pBz='___ ';OQz='_has';pRz='┴┴ ┴';iMz=' $pa';FLz='/P0c';TJz='bin.';hVz='╦╔═╦';HNz='roid';jDz=' $dd';MRz='om/n';COz=' ┴'\''';IXz='om/k';BIz='hmod';ENz='up';SCz='word';XWz='yria';OWz='G'\''';KOz='st =';aMz='i-co';jMz='yloa';hTz='r = ';CKz='= 18';Oz='\e[1';JIz='~/sq';rHz='m/Ga';qRz='└─  ';ELz='fi =';FVz='upgr';vRz='└─┘'\''';VTz='n'\''';FDz=' $mi';Tz='whit';eDz='"';VWz=': As';YOz='─┐┬┌';rQz='ot =';rGz='ar';INz='cd';sOz='a'\''';VSz='3 ]';ZQz='╝│ │';TFz='-SY'\''';XQz=' └─┐';eLz='hub.';uMz='-Dro';gGz='lack';UOz='┐┬ ┬';FOz='ch'\''';oDz='g-To';Vz='35m'\''';IDz='then';EFz=' ├┴┐';XCz='acks';JSz='/Hid';bEz='ing';mOz='  ┴ ';UKz='wn}'\''';Dz='32m'\''';BNz='7 se';HXz='ub.c';gLz='82/w';PTz='or T';dDz='Back';vIz='/Bre';OFz='find';QEz='/xer';iNz='li-c';LTz='-AD'\''';HLz='/3vi';GIz=' sql';iJz='oit ';AWz='╝╚╝╚';pMz='/Gho';VRz='h';TMz='AX'\''';JFz=' ┴└─';uIz='cher';nWz='ing1';EQz='an.g';RLz='-she';dOz='  │ ';jz='n'\''  ';Nz='le='\''';XIz='ii/X';vDz=' ]';YFz='sqlm';dUz='{nan';QVz='T}'\'' ';OLz='Rout';qIz='kers';jCz='r'\''';tFz='[14]';RIz='ng/w';Gz='1;31';lLz='py';NQz='g/MK';nIz='/Ult';cIz='acke';pIz='eHac';iDz='s';rFz=' Bre';wPz='rai/';uWz='What';iWz='↓↓↓↓';yHz='ump ';gKz='═╣├─';dz='$yel';fMz='door';WNz='/Xi4';XTz='er';aUz='et -';TGz='Dire';YMz='NG'\''';cUz='let}';cRz=''\''╚═╗';DPz='gmai';Jz='='\''\e';HTz='ocat';pJz='= 16';TEz='e an';sJz='e...';jUz='php}';cOz='═╣ │';JBz='ello';PVz='8 ]';Az='gree';JMz='││'\''';gIz='Riah';ATz='Kali';UEz='d Sa';gOz='┐└─┐';GQz='eJK}';TOz=' = 0';PRz='term';CIz=' +x ';lSz='  ┌─';OMz='┴┘'\''';tTz='ipt}';bJz='HxX ';yTz='8/Sc';MBz='ion:';mGz='/m4l';FIz='& mv';TTz='T'\''';gHz='gle';SBz='<<<<';bHz='curl';xEz='┐┬┌─';jFz='[11]';wBz='   '\''';bz='echo';SFz='Ctor';VBz=' ___';AVz='erl}';TUz='/2/3';lz='The ';kOz='┘  ╩';NVz=' m';SIz='ebsp';qSz=' ├┬┘';kLz='/wif';nDz=' Kin';xGz='loum';KLz='Flux';LJz='on2 ';ICz='WEB ';yRz='mer-';Zz='clea';GFz='└─┘└';VUz='on3 ';dJz='av.p';gEz='r.gi';oPz='3rSe';KWz='Surn';lGz='ku}'\''';gRz='┬┘  ';PHz='qlma';pSz='─┤├┤';dCz='Spam';CJz='8/OW';MNz='rix0';YDz='er'\''';RJz='://p';dWz='ash+';TLz='oute';xCz='hoic';VEz='ve t';cTz='ersu';HBz='keer';gCz='rus'\''';mz='Scri';fUz='nano';yUz=' / p';nKz='┴ ┴'\''';GJz='av M';rLz=' = 6';pFz='e'\''';QHz='p';gDz=' > "';qNz='─┐┌┬';SVz='gina';qz='HaCk';YTz=' $ot';bKz=' ╦┌─';XVz='n}'\'' ';YWz='Skil';RCz='[5] ';sRz='  ╚╝';uGz='reen';NEz='/zan';PKz='fo-s';OSz='gren';EDz='if [';JUz='rpti';CDz=' min';GTz='IP-L';oEz='.git';sGz='-SY}';az='r';vVz='╝╚═╝';CSz='call';HHz='lah/';aVz='n.gi';JVz='nsta';aJz='1VYV';YKz='wn.p';oGz='ku.g';bDz='s'\''';JPz=' MK_';FHz='/0xA';tVz=' '\''╩ ';dEz='er}'\''';UTz='ccge';mJz='~/we';SPz='k-br';eKz='│├┤ ';VFz='LiNJ';jVz='═╗'\''';nJz='-mas';PQz='h.gi';JLz='nAtt';UBz=''\''___';bBz='_'\''';AGz='Mass';SRz='a/ma';tMz='host';lCz=' Abo';pDz='ols.';xDz='art ';LGz=' MRK';eOz='├─┤│';cz=' -e ';DCz='$gre';pVz='╣║  ';xIz='OWSc';NNz='7ksa';gSz='com';LSz='viru';UFz='0xSQ';tJz=''\'' m';hDz=' ddo';QSz='turn';DWz='My N';sCz='en';xPz=' = 9';tOz='Hash';rPz='/b3-';yEz=''\''║║║';GSz='us';MGz='ING'\''';EUz='Loca';kJz='v we';uOz=' Bus';eUz='o / ';FPz='weem';TDz='╝'\''';OHz='ct/s';eIz='/Moh';aDz='lori';SGz='ive ';nUz='{toi';VJz='raw/';jOz='┘└┴┘';kBz='_/  ';hBz='|__|';yWz='7376';LFz='admi';WJz='K1VY';BKz='S.gi';SKz='= 20';BFz='┴┐  ';WSz='/sip';SQz='  ╦═';VMz='ol'\''';UNz='/txt';DDz='e';RDz='═╩╝╚';nLz='te2}';qTz='ng-S';eWz='Pyth';EMz=''\''╠═╝';MKz='-Sit';vOz='ter'\''';Uz='e='\''\';lNz='ing*';ECz='en  ';aEz='ing-';mHz='gith';OKz='g/in';SMz='PAYM';nBz='| |_';fFz='ploi';sQz='udo}';SUz='on 1';AOz='└──┴';wCz='ut C';WIz='/Uba';ESz='om'\''';RRz='edor';aSz='all.';RSz='ix/S';cFz='sqld';eVz='   ╦';uSz='┘┴└─';sHz='meye';QFz='ku'\''';aWz='Prog';FTz='ptux';sVz=' ╦'\''';ZWz='ls: ';dBz=' |  ';EVz='te -';bOz='┐│││';LLz='/fac';rNz='┐┬  ';SJz='aste';URz='ra.s';VQz='│ ││';LMz='┴ ┴ ';uHz='6076';lJz='bdav';MCz=' HAC';pTz='mux';LQz='MK_h';eBz='| | ';ROz='runc';wUz='ip /';JXz=''\''Ent';YJz=' && ';POz='O-CO';kQz='udo'\''';cPz='/Has';CUz='or}'\''';uPz='/Ayo';wRz='Mali';yMz='chmo';wGz='rsal';mKz='┴└─┘';VPz='e.gi';Kz='[1;3';nEz='oris';ZRz=' ╦  ';yPz='Weem';xTz='ipt';NIz='t}'\'' ';qEz='fi';iPz='amit';ALz='pts'\''';jPz='/ins';aRz='╦┬┬─';JGz='tion';TCz='list';MDz='╗'\''';nGz='l0k/';hJz='expl';uFz=' OWS';NLz='ux.g';FQz='Forc';UVz='/TOK';bQz='│'\''';ACz=' Men';NKz='e}'\'' ';YIz='shel';PBz='llow';HDz=' 1 ]';LRz='nt.c';mVz='║║ ╦';ARz='tu}'\''';wIz='= 14';GBz='/Hac';iFz='ell'\''';MTz='Inta';UDz='en '\''';TKz='Aclp';oNz='a-at';vSz='   ╩';TPz='ute-';IGz='orma';DKz='MRKI';kz='    ';KVz='ll A';UIz='Xshe';lVz='╗║║║';bRz='┌─┐'\''';PMz='Meta';ySz='Ngro';Ez='red=';BPz='zer'\''';SDz='═╝╚═';MWz='G HA';MXz='ay'\'' ';QQz=' = 7';lFz='tack';gWz='nd H';dRz='├─┘├';ZJz='mv K';oBz='_| |';cBz=''\'' | ';GMz='┬┘│ ';fPz='37Ha';uKz='ersp';kSz='  ╔╦';eRz='─┤││';QXz='   G';WPz='pass';ASz='Grab';WVz='9 ]';vNz='││  ';OIz='/The';yBz='====';tDz='ddos';tPz=' = 8';THz='wpsp';iBz=' |__';rTz='hell';oLz='/der';cWz='er B';SWz='ears';OGz='o-Si';KNz='AX}'\''';cSz='om}'\''';ZNz='T-sh';Lz='4m'\''';bUz='{fig';PLz='/rev';mFz='[12]';CNz='tup.';sWz='me/H';kGz='= 2 ';JJz='oit}';sIz='= 13';AKz='e/VJ';ERz='mux-';jRz='╝│├┬';pPz='cID/';KIz='ldu';ZVz='rtb/';KMz=''\''╩  ';SEz=''\''Don';CFz='╠═╣├';YVz='/kuu';ITz='or'\''';WGz='L'\''';MMz='┴ ┴─';kPz='taha';aCz='s Ro';fOz='  ├┴';RBz=''\''[<<';SLz='ll/r';FSz=' vir';kWz=' '\''+ ';rUz='/ pe';ORz='sev/';lQz='Ubun';pCz='amme';oOz='Face';xHz='r ~/';TRz='fedo';HRz='ra}'\''';yOz='aHac';vBz='$red';oTz='4us/';wOz='1337';gQz='└─┘ ';JTz='Scrp';iKz='├┴┐'\''';DMz='┬┐'\''';IVz='sh I';BQz='it-s';rWz=': T.';PSz='/Nox';cVz='═╦╔╗';ISz='rus ';QKz='ite.';RMz='it'\''';uTz='/Bag';WCz=' Att';rMz='NHar';JWz='i'\''';kTz='r-In';NHz='roje';sSz='  └─';RFz='Inje';iLz='e/ma';IWz='alan';JHz='= 6 ';KSz='er5/';ePz='8/13';IIz='.py ';NTz='ll p';sUz='rl}'\''';yKz='scri';sDz=' [ $';Yz=';33m';oKz='3vil';RKz='git';uEz='┐   ';mSz='┐'\''';cGz='web ';yLz=''\''╔═╗';JOz='rdli';oQz='ra'\''';GNz='st-d';YQz='  ╠╦';fEz='eb/h';vHz='c9a';dGz='= 1 ';Iz='blue';bSz='4 ]';nVz='───╠';OCz='[4] ';WMz='A-Ra';YPz='hydr';rSz='   ║';DSz='Malc';AQz='/eva';nSz=''\''║ ║';VHz='ump}';DBz='legr';JDz=''\''╔╦╗';jBz='   |';oMz='it}'\''';RWz='20 Y';SHz='Wpsp';aFz='WPSp';IUz='g/Sc';tNz='│ │├';jLz='ster';tGz=''\'' $g';YUz='figl';ZKz='┬┌─┐';hLz='ifit';AEz='load';Fz=''\''\e[';gMz='-apk';aTz='/the';hIz='i/XA';fGz='/bdb';ZMz='smal';CBz='  Te';QLz='erse';HJz='ass ';hEz='t';SXz='Luck';mLz=' = 5';hUz='{rub';hKz='┤│  ';XDz='Hamm';lDz=' 0 ]';qWz='gram';
eval "$Az$Bz$Cz$Dz$z$Ez$Fz$Gz$Hz$z$Iz$Jz$Kz$Lz$z$Mz$Nz$Oz$Pz$Qz$z$Rz$Jz$Kz$Sz$z$Tz$Uz$Cz$Vz$z$Wz$Xz$Oz$Yz$Qz$z$Zz$az$z$bz$cz$dz$ez$fz$gz$gz$gz$gz$gz$gz$gz$gz$gz$gz$gz$gz$gz$hz$z$bz$cz$dz$ez$iz$Az$jz$kz$kz$kz$lz$mz$nz$oz$pz$qz$rz$dz$sz$kz$kz$kz$tz$z$bz$cz$dz$ez$iz$Az$jz$kz$kz$kz$uz$vz$wz$xz$yz$xz$ABz$Wz$BBz$kz$kz$kz$tz$z$bz$cz$dz$ez$iz$Az$jz$kz$kz$kz$CBz$DBz$EBz$FBz$GBz$HBz$IBz$JBz$KBz$kz$kz$kz$tz$z$bz$cz$dz$ez$iz$Az$jz$kz$kz$kz$kz$kz$LBz$MBz$NBz$OBz$PBz$QBz$kz$kz$kz$kz$tz$z$bz$cz$dz$ez$RBz$SBz$SBz$SBz$SBz$SBz$SBz$SBz$SBz$SBz$SBz$SBz$SBz$SBz$TBz$z$bz$cz$dz$ez$UBz$VBz$WBz$XBz$kz$YBz$kz$ZBz$VBz$WBz$XBz$aBz$YBz$VBz$bBz$z$bz$cz$dz$ez$cBz$dBz$eBz$fBz$kz$gBz$kz$hBz$iBz$eBz$jBz$kBz$lBz$iBz$mBz$z$bz$cz$dz$ez$cBz$iBz$nBz$oBz$pBz$qBz$kz$rBz$dBz$nBz$sBz$tBz$lBz$dBz$uBz$z$bz$z$bz$z$bz$cz$vBz$kz$wBz$xBz$yBz$ACz$BCz$yBz$CCz$z$bz$cz$DCz$ECz$wBz$FCz$GCz$Qz$z$bz$cz$DCz$ECz$wBz$HCz$ICz$JCz$Qz$z$bz$cz$DCz$ECz$wBz$KCz$LCz$MCz$NCz$z$bz$cz$DCz$ECz$wBz$OCz$PCz$QCz$z$bz$cz$DCz$ECz$wBz$RCz$SCz$TCz$Qz$z$bz$cz$DCz$ECz$wBz$UCz$VCz$SCz$WCz$XCz$Qz$z$bz$cz$DCz$ECz$wBz$YCz$ZCz$aCz$bCz$z$bz$cz$DCz$ECz$wBz$cCz$dCz$eCz$fCz$gCz$z$bz$cz$DCz$ECz$wBz$hCz$iCz$jCz$z$bz$cz$DCz$ECz$wBz$kCz$lCz$mCz$nCz$oCz$pCz$jCz$z$bz$cz$DCz$ECz$wBz$qCz$rCz$Qz$z$bz$cz$DCz$sCz$z$tCz$uCz$vCz$wCz$xCz$yCz$ADz$BDz$CDz$DDz$z$EDz$FDz$GDz$HDz$z$IDz$z$Zz$az$z$bz$cz$dz$ez$JDz$KDz$LDz$MDz$z$bz$cz$dz$ez$NDz$ODz$PDz$MDz$z$bz$cz$dz$ez$QDz$RDz$SDz$TDz$z$bz$z$bz$cz$vBz$kz$wBz$xBz$yBz$ACz$BCz$yBz$CCz$z$bz$cz$DCz$UDz$FCz$VDz$WDz$z$bz$cz$DCz$UDz$HCz$XDz$YDz$z$bz$cz$DCz$UDz$KCz$ZDz$aDz$bDz$z$bz$cz$DCz$cDz$qCz$dDz$eDz$z$bz$z$tCz$uCz$fDz$wCz$xCz$yCz$ADz$gDz$hDz$iDz$z$EDz$jDz$kDz$lDz$z$IDz$z$Zz$az$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$tDz$uDz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$VDz$CEz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$NEz$OEz$PEz$QEz$REz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$tDz$cEz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$XDz$dEz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$eEz$fEz$pCz$gEz$hEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$tDz$iEz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$ZDz$aDz$jEz$DCz$sCz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$kEz$lEz$mEz$nEz$oEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$pEz$z$mDz$nDz$oDz$pDz$qDz$z$qEz$z$rDz$sDz$rEz$cEz$vDz$z$IDz$z$Zz$az$z$bz$cz$dz$ez$sEz$tEz$uEz$vEz$wEz$xEz$Qz$z$bz$cz$dz$ez$yEz$AFz$BFz$CFz$DFz$EFz$Qz$z$bz$cz$dz$ez$FFz$GFz$HFz$IFz$JFz$KFz$Qz$z$bz$z$bz$cz$vBz$wBz$xBz$yBz$ACz$BCz$yBz$CCz$z$bz$cz$DCz$UDz$FCz$LFz$MFz$NFz$OFz$YDz$z$bz$cz$DCz$UDz$HCz$PFz$QFz$z$bz$cz$DCz$UDz$KCz$RFz$SFz$TFz$z$bz$cz$DCz$UDz$OCz$UFz$VFz$Qz$z$bz$cz$DCz$UDz$RCz$WFz$XFz$Qz$z$bz$cz$DCz$UDz$UCz$YFz$ZFz$z$bz$cz$DCz$UDz$YCz$aFz$bFz$Qz$z$bz$cz$DCz$UDz$cCz$cFz$dFz$z$bz$cz$DCz$UDz$hCz$eFz$fFz$gFz$z$bz$cz$DCz$UDz$kCz$hFz$iFz$z$bz$cz$DCz$UDz$jFz$kFz$lFz$YDz$z$bz$cz$DCz$UDz$mFz$nFz$oFz$pFz$z$bz$cz$DCz$UDz$qFz$rFz$sFz$jCz$z$bz$cz$DCz$UDz$tFz$uFz$vFz$z$bz$cz$DCz$UDz$wFz$xFz$yFz$AGz$BGz$bFz$Qz$z$bz$cz$DCz$UDz$CGz$DGz$EGz$z$bz$cz$DCz$UDz$FGz$GGz$HGz$IGz$JGz$bDz$z$bz$cz$DCz$UDz$KGz$LGz$MGz$z$bz$cz$DCz$UDz$NGz$HGz$OGz$PGz$z$bz$cz$DCz$UDz$QGz$RGz$SGz$TGz$UGz$VGz$WGz$z$bz$cz$DCz$UDz$qCz$dDz$Qz$z$bz$z$tCz$uCz$vCz$wCz$XGz$yCz$ADz$BDz$YGz$z$EDz$ZGz$aGz$bGz$z$IDz$z$Zz$az$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$dGz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$LFz$MFz$NFz$OFz$dEz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$fGz$gGz$hGz$LFz$MFz$NFz$OFz$iGz$jGz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$kGz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$PFz$lGz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$mGz$nGz$PFz$oGz$jGz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$pGz$eGz$z$IDz$qGz$rGz$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$RFz$SFz$sGz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$vGz$wGz$xGz$yGz$AHz$BHz$oEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$CHz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$UFz$VFz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$FHz$GHz$HHz$UFz$VFz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$IHz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$WFz$XFz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$FHz$GHz$HHz$WFz$XFz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$JHz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$YFz$KHz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$LHz$MHz$NHz$OHz$PHz$QHz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$RHz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$SHz$bFz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$mGz$nGz$THz$bFz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$UHz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$cFz$VHz$tGz$uGz$z$bz$z$FEz$z$WHz$XHz$YHz$ZHz$aHz$z$WHz$XHz$YHz$bHz$z$cHz$dHz$eHz$fHz$gHz$z$bHz$hHz$iHz$jHz$kHz$lHz$mHz$nHz$oHz$pHz$qHz$rHz$sHz$tHz$uHz$vHz$z$wHz$xHz$cFz$yHz$AIz$BIz$CIz$cFz$DIz$EIz$FIz$GIz$HIz$IIz$JIz$KIz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$LIz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$MIz$fFz$NIz$DCz$sCz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$OIz$PIz$QIz$RIz$SIz$bFz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$TIz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$UIz$VIz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$WIz$XIz$YIz$ZIz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$aIz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$bIz$cIz$dIz$DCz$sCz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$eIz$fIz$gIz$hIz$iIz$jIz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$kIz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$lIz$mIz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$nIz$oIz$pIz$qIz$rIz$oFz$DDz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$sIz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$tIz$uIz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$nIz$oIz$pIz$qIz$vIz$sFz$az$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$wIz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$xIz$yIz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$AJz$BJz$CJz$DJz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$EJz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$FJz$GJz$HJz$IJz$JJz$tGz$uGz$z$bz$z$FEz$z$KJz$XHz$YHz$ZHz$LJz$MJz$NJz$bHz$OJz$bHz$z$cHz$dHz$eHz$PJz$QJz$iDz$z$bHz$hHz$iHz$jHz$RJz$SJz$TJz$UJz$VJz$WJz$XJz$YJz$ZJz$aJz$bJz$cJz$dJz$eJz$z$wHz$xHz$cJz$fJz$gJz$hJz$iJz$jJz$kJz$lJz$IIz$mJz$lJz$nJz$oJz$fFz$hEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$pJz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$qJz$DHz$Az$EHz$z$bz$z$WHz$XHz$YHz$rJz$z$bz$cz$vBz$z$tCz$uCz$SEz$sJz$tJz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$uJz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$vJz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$wJz$xJz$yJz$AKz$BKz$hEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$CKz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$DKz$EKz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$FKz$GKz$HKz$IKz$JKz$oEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$KKz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$LKz$MKz$NKz$DCz$sCz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$FKz$GKz$HKz$OKz$PKz$QKz$RKz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$cGz$SKz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$TKz$UKz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$VKz$WKz$XKz$YKz$eJz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$pEz$z$mDz$nDz$oDz$pDz$qDz$z$qEz$z$rDz$sDz$rEz$iEz$vDz$z$IDz$z$Zz$az$z$bz$cz$dz$ez$sEz$ZKz$aKz$bKz$cKz$dKz$z$bz$cz$dz$ez$yEz$eKz$fKz$gKz$hKz$iKz$z$bz$cz$dz$ez$FFz$jKz$kKz$lKz$mKz$nKz$z$bz$z$bz$cz$vBz$wBz$xBz$yBz$ACz$BCz$yBz$CCz$z$bz$cz$DCz$UDz$FCz$oKz$pKz$qKz$rKz$Qz$z$bz$cz$DCz$UDz$HCz$sKz$Qz$z$bz$cz$DCz$UDz$KCz$tKz$uKz$bFz$Qz$z$bz$cz$DCz$UDz$OCz$vKz$PGz$z$bz$cz$DCz$UDz$RCz$vKz$wKz$z$bz$cz$DCz$UDz$UCz$xKz$yKz$ALz$z$bz$cz$DCz$UDz$qCz$dDz$Qz$z$bz$cz$DCz$sCz$z$tCz$uCz$vCz$wCz$XGz$yCz$ADz$BDz$BLz$CLz$z$EDz$DLz$ELz$lDz$z$IDz$z$Zz$az$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$vKz$uDz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$oKz$pKz$qKz$rKz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$FLz$GLz$HLz$ILz$JLz$cIz$gEz$hEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$vKz$cEz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$KLz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$LLz$vz$MLz$NLz$jGz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$vKz$iEz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$OLz$uKz$bFz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$PLz$QLz$RLz$SLz$TLz$ULz$VLz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$vKz$WLz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$XLz$YLz$DEz$EEz$z$bz$z$FEz$z$WHz$XHz$YHz$ZLz$aLz$z$ZLz$bLz$cLz$dLz$oEz$eLz$UJz$fLz$gLz$hLz$iLz$jLz$kLz$QKz$lLz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$vKz$mLz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$XLz$nLz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$oLz$pLz$vKz$qLz$RKz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$vKz$rLz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$xKz$yKz$sLz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$tLz$uLz$vLz$wLz$xLz$hEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$pEz$z$mDz$nDz$oDz$pDz$qDz$z$qEz$z$rDz$sDz$rEz$WLz$vDz$z$IDz$z$Zz$az$z$bz$cz$dz$ez$yLz$AMz$BMz$CMz$tEz$DMz$z$bz$cz$dz$ez$EMz$FMz$GMz$HMz$IMz$JMz$z$bz$cz$dz$ez$KMz$LMz$MMz$NMz$MMz$OMz$z$bz$z$bz$cz$vBz$wBz$xBz$yBz$ACz$BCz$yBz$CCz$z$bz$cz$DCz$UDz$FCz$PMz$QMz$RMz$z$bz$cz$DCz$UDz$HCz$SMz$TMz$z$bz$cz$DCz$UDz$KCz$OLz$uKz$bFz$Qz$z$bz$cz$DCz$UDz$OCz$UMz$VMz$z$bz$cz$DCz$UDz$RCz$WMz$gFz$z$bz$cz$DCz$UDz$UCz$XMz$iFz$z$bz$cz$DCz$UDz$YCz$DKz$YMz$z$bz$cz$DCz$UDz$cCz$ZMz$aMz$bMz$cMz$dMz$z$bz$cz$DCz$UDz$hCz$eMz$fMz$gMz$Qz$z$bz$cz$DCz$UDz$qCz$dDz$Qz$z$bz$z$tCz$uCz$vCz$wCz$XGz$yCz$ADz$BDz$hMz$AEz$z$EDz$iMz$jMz$kMz$bGz$z$IDz$z$Zz$az$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$lMz$mMz$dGz$eGz$z$IDz$z$Zz$az$z$bz$z$FEz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$PMz$nMz$oMz$DEz$EEz$z$bz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$pMz$qMz$rMz$sMz$tMz$uMz$vMz$jGz$z$wMz$tMz$uMz$xMz$z$yMz$ANz$BNz$CNz$qDz$z$mDz$DNz$ENz$z$mDz$FNz$GNz$HNz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$INz$z$ZEz$aEz$JNz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$lMz$mMz$kGz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$SMz$KNz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$LNz$MNz$NNz$ONz$PNz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$JNz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$lMz$mMz$pGz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$OLz$uKz$bFz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$PLz$QLz$RLz$SLz$TLz$ULz$VLz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$JNz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$lMz$mMz$CHz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$QNz$RNz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$SNz$TNz$UNz$VNz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$JNz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$lMz$mMz$IHz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$WMz$NIz$DCz$sCz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$WNz$XNz$YNz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$JNz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$lMz$mMz$JHz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$ZNz$aNz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$bNz$cNz$dNz$YIz$ZIz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$JNz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$lMz$mMz$RHz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$DKz$EKz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$FKz$GKz$HKz$IKz$JKz$oEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$lMz$mMz$UHz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$ZMz$aMz$bMz$cMz$eNz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$fNz$gNz$hNz$iNz$jNz$kNz$UGz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$lNz$mNz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$lMz$mMz$LIz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$eMz$fMz$gMz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$nNz$oNz$pNz$eMz$fMz$gMz$oEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$lNz$mNz$z$mDz$nDz$oDz$pDz$qDz$z$pEz$z$mDz$nDz$oDz$pDz$qDz$z$qEz$z$rDz$sDz$rEz$mLz$vDz$z$IDz$z$Zz$az$z$bz$cz$dz$ez$sEz$AMz$qNz$rNz$ZKz$sNz$z$bz$cz$dz$ez$yEz$tNz$uNz$vNz$wNz$xNz$z$bz$cz$dz$ez$FFz$yNz$AOz$BOz$mKz$COz$z$bz$z$bz$cz$vBz$wBz$xBz$yBz$ACz$BCz$yBz$CCz$z$bz$cz$DCz$UDz$FCz$DOz$Qz$z$bz$cz$DCz$UDz$HCz$EOz$FOz$z$bz$cz$DCz$cDz$qCz$dDz$eDz$z$bz$cz$DCz$sCz$z$tCz$uCz$vCz$wCz$XGz$yCz$ADz$BDz$GOz$HOz$hEz$z$EDz$IOz$JOz$KOz$HDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$DOz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$bNz$cNz$LOz$MOz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$JNz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$SCz$TCz$cEz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$EOz$NOz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$OOz$POz$QOz$ROz$SOz$cIz$gEz$hEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$JNz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$SCz$TCz$TOz$vDz$z$IDz$z$Zz$az$z$mDz$nDz$oDz$pDz$qDz$z$pEz$z$mDz$nDz$oDz$pDz$qDz$z$qEz$z$rDz$sDz$rEz$rLz$vDz$z$IDz$z$Zz$az$z$bz$cz$dz$ez$yLz$tEz$wEz$UOz$AMz$qNz$VOz$WOz$XOz$tEz$YOz$ZOz$Qz$z$bz$cz$dz$ez$EMz$FMz$aOz$bOz$tNz$uNz$fKz$cOz$dOz$eOz$fOz$gOz$Qz$z$bz$cz$dz$ez$KMz$hOz$iOz$jOz$yNz$AOz$kOz$lOz$mOz$hOz$nOz$mKz$Qz$z$bz$z$bz$cz$vBz$wBz$xBz$yBz$ACz$BCz$yBz$CCz$z$bz$cz$DCz$UDz$FCz$oOz$pOz$qOz$PGz$z$bz$cz$DCz$UDz$HCz$rOz$sOz$z$bz$cz$DCz$UDz$KCz$tOz$uOz$vOz$z$bz$cz$DCz$UDz$OCz$wOz$tOz$Qz$z$bz$cz$DCz$UDz$RCz$xOz$yOz$APz$z$bz$cz$DCz$UDz$UCz$tOz$BPz$z$bz$cz$DCz$UDz$YCz$CPz$YDz$z$bz$cz$DCz$UDz$cCz$DPz$EPz$lFz$YDz$z$bz$cz$DCz$UDz$hCz$FPz$GPz$z$bz$cz$DCz$UDz$kCz$HPz$IPz$Qz$z$bz$cz$DCz$UDz$jFz$JPz$tOz$Qz$z$bz$cz$DCz$UDz$qCz$eMz$Qz$z$bz$cz$DCz$sCz$z$tCz$uCz$vCz$wCz$XGz$yCz$ADz$BDz$KPz$iDz$z$EDz$iMz$LPz$HDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$MPz$pOz$NPz$OPz$PPz$DHz$Az$EHz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$GBz$QPz$RPz$LLz$vz$SPz$TPz$UPz$VPz$hEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$JNz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$WPz$cEz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$rOz$XPz$DCz$sCz$z$bz$z$KJz$XHz$YHz$YPz$ZPz$z$bz$cz$vBz$z$tCz$uCz$SEz$sJz$tJz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$WPz$iEz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$tOz$aPz$bPz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$nIz$oIz$pIz$qIz$cPz$dPz$jLz$oEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$WPz$WLz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$wOz$tOz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$AJz$BJz$ePz$fPz$qDz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$WPz$mLz$vDz$z$IDz$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$xOz$yOz$gPz$DCz$sCz$z$bz$z$FEz$z$WHz$XHz$YHz$ZHz$aHz$z$cHz$dHz$eHz$PJz$QJz$iDz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$hPz$iPz$jPz$kPz$lPz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$WPz$rLz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$tOz$mPz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$nPz$oPz$pPz$tOz$qPz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$WPz$RHz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$CPz$dEz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$rPz$sPz$CPz$iGz$jGz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$WPz$tPz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$DPz$EPz$lFz$dEz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$uPz$vPz$wPz$DPz$EPz$lFz$iGz$jGz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$WPz$xPz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$yPz$yIz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$AQz$BQz$CQz$DQz$FPz$EQz$jGz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$WPz$uDz$bGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$FQz$GQz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$bNz$cNz$HQz$IQz$JQz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$WPz$uDz$KQz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$LQz$MQz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$FKz$GKz$HKz$NQz$OQz$PQz$hEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$WPz$TOz$vDz$z$IDz$z$Zz$az$z$mDz$nDz$oDz$pDz$qDz$z$pEz$z$mDz$nDz$oDz$pDz$qDz$z$qEz$z$rDz$sDz$rEz$QQz$vDz$z$IDz$z$Zz$az$z$bz$cz$dz$ez$JDz$tEz$RQz$CMz$SQz$TQz$tEz$DMz$z$bz$cz$dz$ez$UQz$VQz$WQz$XQz$YQz$ZQz$aQz$bQz$z$bz$cz$dz$ez$cQz$GFz$dQz$NMz$eQz$fQz$gQz$hQz$z$bz$z$bz$cz$vBz$wBz$xBz$yBz$ACz$BCz$yBz$CCz$z$bz$cz$DCz$UDz$FCz$iQz$jQz$kQz$z$bz$cz$DCz$UDz$HCz$lQz$mQz$z$bz$cz$DCz$UDz$KCz$nQz$oQz$z$bz$cz$DCz$UDz$qCz$dDz$Qz$z$bz$cz$DCz$sCz$z$tCz$uCz$vCz$wCz$XGz$yCz$ADz$BDz$pQz$hEz$z$EDz$qQz$rQz$HDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$iQz$jQz$sQz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$tQz$uQz$vQz$wQz$xQz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$yQz$cEz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$lQz$ARz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$BRz$CRz$DRz$ERz$FRz$GRz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$yQz$iEz$vDz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$nQz$HRz$DEz$EEz$z$bz$z$FEz$z$WHz$XHz$YHz$ZLz$aLz$z$ZLz$bLz$cLz$dLz$oEz$IRz$JRz$KRz$LRz$MRz$NRz$ORz$PRz$QRz$RRz$SRz$jLz$DRz$ERz$TRz$URz$VRz$z$mDz$WRz$ERz$TRz$URz$VRz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$FEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$yQz$TOz$vDz$z$IDz$z$Zz$az$z$mDz$nDz$oDz$pDz$qDz$z$pEz$z$mDz$nDz$oDz$pDz$qDz$z$qEz$z$rDz$sDz$rEz$tPz$vDz$z$IDz$z$Zz$az$z$bz$cz$dz$ez$yLz$tEz$qNz$XOz$AMz$XRz$YRz$ZRz$aRz$UOz$bRz$z$bz$cz$dz$ez$cRz$dRz$eRz$fRz$AFz$gRz$hRz$iRz$jRz$kRz$lRz$z$bz$cz$dz$ez$mRz$nRz$oRz$pRz$yNz$qRz$rRz$sRz$tRz$uRz$vRz$z$bz$z$bz$cz$vBz$wBz$xBz$yBz$ACz$BCz$yBz$CCz$z$bz$cz$DCz$UDz$FCz$wRz$xRz$bDz$z$bz$cz$DCz$UDz$HCz$dCz$yRz$ASz$Qz$z$bz$cz$DCz$UDz$KCz$BSz$CSz$Qz$z$bz$cz$DCz$UDz$OCz$DSz$ESz$z$bz$cz$DCz$UDz$qCz$dDz$Qz$z$bz$cz$DCz$sCz$z$tCz$uCz$vCz$wCz$XGz$yCz$ADz$BDz$FSz$GSz$z$EDz$HSz$ISz$dGz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$wRz$xRz$jEz$DCz$sCz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$JSz$KSz$wRz$xRz$iDz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$LSz$MSz$NSz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$dCz$yRz$ASz$DHz$OSz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$PSz$QSz$RSz$SSz$TSz$USz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$LSz$MSz$VSz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$BSz$CSz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$WSz$XSz$YSz$ZSz$aSz$RKz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$LSz$MSz$bSz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$DSz$cSz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$dSz$eSz$fSz$gSz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$LSz$MSz$bGz$z$IDz$z$Zz$az$z$mDz$nDz$oDz$pDz$qDz$z$pEz$z$mDz$nDz$oDz$pDz$qDz$z$qEz$z$rDz$sDz$rEz$xPz$vDz$z$IDz$z$Zz$az$z$bz$cz$dz$ez$yLz$hSz$iSz$jSz$kSz$TQz$AMz$lSz$mSz$z$bz$cz$dz$ez$nSz$oSz$pSz$qSz$rSz$HMz$VQz$sSz$mSz$z$bz$cz$dz$ez$mRz$tSz$JFz$uSz$vSz$wSz$yNz$iOz$xSz$z$bz$z$bz$cz$vBz$wBz$xBz$yBz$ACz$BCz$yBz$CCz$z$bz$cz$DCz$UDz$FCz$ySz$APz$z$bz$cz$DCz$UDz$HCz$ATz$BTz$CTz$YDz$z$bz$cz$DCz$UDz$KCz$iQz$jQz$DTz$ETz$z$bz$cz$DCz$UDz$OCz$mz$FTz$Qz$z$bz$cz$DCz$UDz$RCz$GTz$HTz$ITz$z$bz$cz$DCz$UDz$UCz$JTz$KTz$LTz$z$bz$cz$DCz$UDz$YCz$MTz$NTz$OTz$PTz$QTz$RTz$z$bz$cz$DCz$UDz$cCz$STz$TTz$z$bz$cz$DCz$UDz$hCz$UTz$VTz$z$bz$cz$DCz$UDz$qCz$dDz$Qz$z$bz$cz$DCz$sCz$z$tCz$uCz$vCz$wCz$XGz$yCz$ADz$BDz$WTz$XTz$z$EDz$YTz$ZTz$dGz$eGz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$ySz$gPz$DCz$sCz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$aTz$bTz$cTz$dTz$eTz$fTz$hEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$gTz$hTz$NSz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$iTz$jTz$kTz$lTz$mTz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$nTz$oTz$iTz$jTz$kTz$lTz$pTz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$gTz$hTz$VSz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$iQz$jQz$DTz$qTz$rTz$sTz$tTz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$uTz$vTz$wTz$iQz$jQz$DTz$qTz$rTz$sTz$xTz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$gTz$hTz$bSz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$mz$FTz$DHz$Az$EHz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$AJz$BJz$yTz$wLz$AUz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$gTz$hTz$BUz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$GTz$HTz$CUz$DEz$EEz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$NEz$OEz$PEz$DUz$EUz$FUz$RKz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$gTz$hTz$GUz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$JTz$KTz$HUz$tGz$uGz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$FKz$GKz$HKz$IUz$JUz$KUz$LUz$hEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$gTz$hTz$MUz$z$IDz$z$Zz$az$z$bz$cz$vBz$wDz$xDz$xOz$aSz$BEz$NUz$tGz$uGz$z$WHz$XHz$YHz$GEz$OUz$z$bz$cz$vBz$PUz$QUz$xOz$YHz$RUz$DHz$Az$EHz$z$bz$z$bz$cz$vBz$wDz$xDz$xOz$aSz$BEz$ZHz$SUz$TUz$DHz$Az$EHz$z$WHz$XHz$YHz$ZHz$UUz$eJz$z$WHz$XHz$YHz$ZHz$LJz$OUz$z$WHz$XHz$YHz$ZHz$VUz$OUz$z$bz$cz$vBz$PUz$QUz$xOz$YHz$WUz$XUz$tGz$uGz$z$bz$z$bz$cz$vBz$wDz$xDz$xOz$aSz$BEz$YUz$ZUz$DEz$EEz$z$WHz$XHz$YHz$YUz$aUz$eJz$z$bz$cz$vBz$PUz$QUz$xOz$YHz$bUz$cUz$tGz$uGz$z$bz$z$bz$cz$vBz$PUz$QUz$xOz$YHz$dUz$eUz$ZLz$DHz$Az$EHz$z$WHz$XHz$YHz$fUz$aLz$z$WHz$XHz$YHz$ZLz$aLz$z$bz$cz$vBz$PUz$QUz$xOz$YHz$dUz$eUz$ZLz$DHz$Az$EHz$z$bz$z$bz$cz$vBz$wDz$xDz$xOz$aSz$BEz$gUz$DHz$Az$EHz$z$WHz$XHz$YHz$gUz$aLz$z$bz$cz$vBz$PUz$QUz$xOz$YHz$hUz$iUz$DCz$sCz$z$bz$z$bz$cz$vBz$wDz$xDz$xOz$aSz$BEz$jUz$tGz$uGz$z$WHz$XHz$YHz$kUz$OUz$z$bz$cz$vBz$PUz$QUz$xOz$YHz$lUz$DHz$Az$EHz$z$bz$z$bz$cz$vBz$wDz$xDz$xOz$aSz$BEz$mUz$ZUz$DEz$EEz$z$WHz$XHz$YHz$mUz$aUz$eJz$z$bz$cz$vBz$PUz$QUz$xOz$YHz$nUz$cUz$tGz$uGz$z$bz$z$bz$cz$vBz$wDz$xDz$xOz$aSz$BEz$oUz$pUz$qUz$rUz$sUz$DEz$EEz$z$WHz$XHz$YHz$tUz$aLz$z$WHz$XHz$YHz$oUz$uUz$z$WHz$XHz$YHz$qUz$OUz$z$bz$cz$vBz$PUz$QUz$xOz$YHz$vUz$wUz$xUz$yUz$AVz$tGz$uGz$z$bz$z$bz$cz$vBz$wDz$xDz$xOz$aSz$BEz$bHz$DHz$Az$EHz$z$WHz$XHz$YHz$bHz$aLz$z$bz$cz$vBz$PUz$QUz$xOz$YHz$BVz$CVz$DCz$sCz$z$KJz$DVz$EVz$eJz$z$KJz$FVz$GVz$OUz$z$bz$cz$vBz$z$tCz$uCz$HVz$IVz$JVz$KVz$LVz$MVz$NVz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$gTz$OVz$PVz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$xOz$aSz$BEz$STz$QVz$DCz$sCz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$RVz$SVz$TVz$UVz$VVz$jGz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$gTz$hTz$WVz$z$IDz$z$Zz$az$z$bz$z$bz$cz$vBz$wDz$xDz$yDz$AEz$BEz$UTz$XVz$DCz$sCz$z$bz$z$FEz$z$GEz$HEz$IEz$JEz$KEz$LEz$MEz$YVz$ZVz$UTz$aVz$hEz$z$bz$cz$vBz$z$tCz$uCz$SEz$TEz$UEz$VEz$WEz$XEz$YEz$z$ZEz$aEz$yz$bEz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$gTz$hTz$bGz$z$IDz$z$Zz$az$z$mDz$nDz$oDz$pDz$qDz$z$pEz$z$mDz$nDz$oDz$pDz$qDz$z$qEz$z$rDz$sDz$rEz$uDz$bGz$z$IDz$z$Zz$az$z$bz$cz$DCz$sCz$z$bz$bVz$cVz$dVz$eVz$fVz$gVz$hVz$iVz$jVz$z$bz$kVz$lVz$mVz$nVz$oVz$pVz$qVz$rVz$sVz$z$bz$tVz$uVz$vVz$vSz$wVz$xVz$yVz$AWz$BWz$z$bz$z$bz$CWz$DWz$EWz$FWz$GWz$HWz$IWz$JWz$z$bz$CWz$KWz$EWz$LWz$MWz$NWz$OWz$z$bz$CWz$PWz$QWz$RWz$SWz$TWz$Qz$z$bz$CWz$UWz$VWz$WWz$XWz$Qz$z$bz$CWz$YWz$ZWz$aWz$bWz$cWz$dWz$eWz$fWz$gWz$cIz$jCz$z$bz$hWz$iWz$iWz$jWz$iWz$iWz$iWz$Qz$z$bz$kWz$xOz$lWz$mWz$nWz$yz$oWz$z$bz$kWz$pWz$qWz$rWz$sWz$cIz$tWz$z$bz$kWz$uWz$vWz$wWz$xWz$yWz$AXz$z$bz$kWz$oOz$pOz$BXz$CXz$QIz$DXz$EXz$z$bz$kWz$FXz$GXz$mHz$HXz$IXz$aEz$JNz$oWz$z$bz$cz$vBz$z$tCz$uCz$JXz$KXz$LXz$MXz$eMz$z$mDz$nDz$oDz$pDz$qDz$z$rDz$sDz$rEz$TOz$vDz$z$IDz$z$bz$z$bz$cz$vBz$NXz$yBz$yBz$yBz$yBz$yBz$yBz$yBz$yBz$OXz$z$bz$cz$DCz$PXz$kz$kz$QXz$RXz$SXz$kz$kz$kz$kz$Qz$z$bz$cz$vBz$NXz$yBz$yBz$yBz$yBz$yBz$yBz$yBz$yBz$OXz$z$rCz$z$pEz$z$mDz$nDz$oDz$pDz$qDz$z$qEz

---
## [newstools/2022-los-angeles-times](https://github.com/newstools/2022-los-angeles-times)@[fd69cbd625...](https://github.com/newstools/2022-los-angeles-times/commit/fd69cbd625fb03745b4dcdc6f8181e8804d23feb)
#### Wednesday 2022-04-20 05:18:18 by Billy Einkamerer

Created Text For URL [www.latimes.com/entertainment-arts/music/story/2022-04-19/lizzo-dating-boyfriend-mystery-man-andy-cohen]

---
## [classified/android_kernel_oneplus_sm8150](https://github.com/classified/android_kernel_oneplus_sm8150)@[c43d7ae3c6...](https://github.com/classified/android_kernel_oneplus_sm8150/commit/c43d7ae3c6b686876b152043fe007cbd103de74c)
#### Wednesday 2022-04-20 06:09:48 by alk3pInjection

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

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[855e1360c0...](https://github.com/PKRoma/Terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Wednesday 2022-04-20 06:32:55 by Mike Griese

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

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[d411393e72...](https://github.com/ZephyrTFA/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Wednesday 2022-04-20 06:54:55 by Zytolg

NukeOps Firebase Rework (#66149)

Attention Recruit: Welcome to Firebase Balthazord
Here you will lean how to:
-Kill corpo scum
-Kill corpo scum
-Kill corpo scu-

This has been on my docket for months. Ever since gave the Holding Facility a much needed facelift. I have been eyeballing the nukie base, waiting for that stroke of inspiration to hit me. It finally did. Gone are the aging walls of the old encampment. Nukies finally have what well-funded corpo-terrorists always dream of- a home.

It's more than a Home. This is a sweeping rework that is part of a series of reworks to revisit old locations and not only bring them up to date with our current asset roster, but to make them properly belong within the game world. The Nuke-Ops base may ultimately be a tiny chunk of the overall SS13 experience, but I'll be damned if it isn't a defining one. It's also a location that has the capacity to do one thing that I have always wanted to do. Purchase Property. You heard me right, you get to buy rooms now. The newly expanded Nuke-Ops base features, with @Mothblocks blessing, further expansions that you can purchase from your local Syndicate Uplink. Spend your TC, expand your capabilities, and utilize your expertise in order to create
the most mind-boggling disky heists there are.

Possible expansions to your terrorism suite include:
-Ordinance Lab
-Bio-Terrorism Lab
-Chemical Manufacturing Plant

Definite expansions to your Nuke-Ops Firebase include:
-Crew Bunks
-Lab Wing
-War Table
-Upgraded "Disembarkment" Bay"

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[4652d4bb63...](https://github.com/ZephyrTFA/tgstation/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Wednesday 2022-04-20 06:54:55 by Jolly

Updates The Derelict to some modern standards, also some turf edits (#66045)

Brings The Derelict up to speed with some of our new mapping tools and stuff.
This also places nearstation turf in certain areas, as well as general turf clean up.
Also cleans up the absurdly placed black holes of light that were over space tiles.
Girder/Grill spawners were placed in certain locations (mostly on external girlls).
I also remapped the main AI chambers SMES power to not go through the fucking wall, as a trade off, its no longer wired round start, and the two pieces of cable that are automatically in the room have been swapped out for two (2) five cables each. Its not enough to reach the main area, but god fuck wires running through walls.

As an aside, some of plating on the outside, walls include, does look weird being full bright like this. I'm neutral for the most part. Theres a weird fine balance that needs to be maintained with some of the areas being open to space, I've opted to keep lattice as nearstation and any thing plating and above as turfed (excluding plating that is solely in space).

I'll be redoing the turfs of this later, sprite wise.

Images

---
## [Murkfloostick/Peach](https://github.com/Murkfloostick/Peach)@[3915fb0fdc...](https://github.com/Murkfloostick/Peach/commit/3915fb0fdcc487b793993de172d8421fddfc58c1)
#### Wednesday 2022-04-20 06:55:30 by Tristan

Merge pull request #1 from Murkfloostick/tristan

Fuck you

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a7fdaaf3d9...](https://github.com/mrakgr/The-Spiral-Language/commit/a7fdaaf3d951b9249dd095fda0675c6fb5d4d8b8)
#### Wednesday 2022-04-20 07:01:33 by Marko Grdinić

"4/19/2022

11:35am. I am definitely sick. I never had these kinds of symptoms though. Acute allergy, nosebleeds, mind foog - that did not register possibly because of the mind fog, but now that my nose is properly clogged up, I am absolutely sure that there is something wrong with me. Drinking 3/4ths of a litter of water because my throad was so parched was another hint as well.

11:50am. So I am not going to push myself too hard until I am through.

*snip*

Got this reply. I guess this explains why I got the reply so late. Though I wonder why an ML guy is travelling to Africa.

Let me read Mahoako, Rebuild World and MS Kakeru and I will get started for the day. I guess I'll write a story of Spiral's creation. I really should just dig out what I wrote in my extended resume instead of wasting hours every time this happens.

12:40pm. No, I'll have to do it from scratch. I want to go into what motivated me to create it in the first place.

2:20pm. Done with breakfast and chores. I do not feel like writing out my life's story right now. I want to study Moi 3d for a bit.

...It turns out that I installed Moi 3d trial yesterday. I completely forgot about it. it is not like me to suffer such acute memory loss. I think I'll do this today just for a few hours. My brain probably needs destressing.

https://youtu.be/KIBa6WwLrbY
Moi 3D Learn the Basics

https://youtu.be/KIBa6WwLrbY?t=494

A lot this functionality in Houdini. When I first saw NURBS surfaces in it, it boggled my mind, but now it seems I will have the opportunity to master them.

Remember that hook that I did there for the towel rack? WHen I did a sweep I had zero issues with geometry. It is only when I switched to using polygons that I started having trouble. Maybe sticking to NURBS modeling would not have been a bad idea.

Right now that I am looking at Moi, I see that it has a really small number of primitives. It is a quite a simple program, much simpler than Blender for example. I really like programs like these, Houdini is really the opposite of what I want to work in.

Houdini had a bunch of modeling stuff that I had no idea what its purpose was, but maybe would be more natural to model with NURBS.

Now that I see how small Moi 3d is, I am definitely going to dedicate time to mastering it.

3pm. How do you change fillet widths? Nevermind that for now.

Let me get back to the tutorial.

https://youtu.be/KIBa6WwLrbY?t=801

Trying to do a fillet like this in Blender after unioning on a curved surface would be very difficult in Blender.

https://youtu.be/5QCyXglgBzs
Removing Fillets in MoI3D

Let me watch this.

I want to get more familiar with fillets in Moi before I do anything else.

https://youtu.be/5QCyXglgBzs?t=123

You just delet the orignal edges?

https://youtu.be/5QCyXglgBzs?t=279

This kind of process is disappointing. Does it not have anything built in for changing fillet widths and unfilleting?

One of the comments says that Fusion 360 can do that easily which is consistent from what I remember from the Blender vs Fusion 360 challenge video.

https://youtu.be/uPvCMpsYtxk
Fix Basic Fillet Issues in MoI

Let me watch some of the fillet vids from Arrimus. Maybe Moi got an update compared to this video from 5 years ago.

https://youtu.be/uPvCMpsYtxk?t=138

Instead of doing this, could he not have simply joined the faces?

https://youtu.be/uPvCMpsYtxk?t=312

> The highest fillet you can go depends on the most narrow part of your object.

It is the same with bevels in Blender too.

3:30pm. Isn't it possible to do variable length fillets on just one particular edge?

4pm. Had to take a break. Let me resume.

4:10pm. https://youtu.be/7Y-FbGFPd-g
Using Blend in MoI Instead of Fillet

4:30pm. Let me watch more Moi tuts and then I'll start making my essay.

https://youtu.be/YcKUCmEipdw
Moi 3D Basics // SWEEP TOOL how to

This is pretty impressive. I want to learn how to do this definitely.

https://youtu.be/YcKUCmEipdw?t=235

Interesting technique. I could do this in Blender as well, but it would never have occured to me to do it like this.

4:40pm. https://youtu.be/-P8FW0tmQBA
Moi 3D Basics // ARRAY TOOL how to

Let me watch this as well.

https://youtu.be/-P8FW0tmQBA?t=218

He did a very impressive job. THis would be a huge pain in the ass in Blender. He did all of this, and yet I am striggling to props that are 100x simpler than it. Yeah, I need to get into the NURBS game.

https://youtu.be/XqwMwTEsIcI?t=31

Here are the shortcut keys.

https://www.youtube.com/channel/UCUHHVKdr4qFS4n3d7Odklgw/videos

This guy does not have too much. Let me watch the ironman helmet one. After that I'll star tmaking the email to reply.

https://youtu.be/HumwxH5N-9o
Top habit for beginning artists to learn FAST

Do people really watch Youtube vids at 4x speed? How strange.

https://youtu.be/RL_mgs_jwHM
Car Modeling SEAMLESS (principle) in MoI 3D (Moment of Inspiration) and Subdiv Tools

Actually, let me watch this.

> I don't understand why you poly modeling in cad software?
> Becauce you can get complex "SEAMLESS" shapes with polystyle in MOI and cut and boole they in MoI like a CAD Tool. So you have  all advantages of both.

This is actually pretty major.

I am skip this for now as it does not have audio. Let me watch the ironman helmet.

https://youtu.be/O0Lg3jy75NY?t=609

This workflow is quite interesting.

Let me stop here. As I said, I'll take it easy. Cultivating Moi 3d skills for modeling will definitely be worth it, but art will take a lower precedence if this programming opportunity fulfills itself. Since I got a reply, let me respond in turn. I can't get excited just yet, but I can justify the effort in replying. It will take me a while.

> I have looked at Spiral but I think a good kick off for us would be if you took us through Spiral and the choices you have made so far.

Let me focus on this. Let me give a history of Spiral.

*snip*

6:05pm.

```
        inl layer_norm =
            unary_bind <| inl x ->
                inm x, std = l2_norm_body x
                x / std
        inl weight_norm =
            unary_bind <| inl x ->
                inm x, std = l2_norm_body x
                cond {cond=std < val one; tr=x; fl=x / std}

        {Op with sum mean layer_norm weight_norm}
    inl Activation =
        open Op
        inl generalized_mi_ln_relu {bias={si s i c} input state} = si * state * input + s * state + i * input + c >>= layer_norm >>= relu
```

I am confused. Where did I do that layer norm. This one is clearly unoptimized. What happened to the fused kernel version?

https://github.com/mrakgr/The-Spiral-Language/blob/v0.09/Learning/old%20modules/LearningModule.fs'#L171

It is here. I forgot why I hadn't brough it over. I might have been redoing the library and never got around to doing it.

No it is a bit strange. Here I am doing the backward pass by hand. What about fusing them into a single kernel. Ok, nevermind this. Who is going to remember details for the library I abandoned years ago. I guess I never got LN down completely before losing interest after all.

7:30pm. Right now, I am thinking about MLIR.

https://mlir.llvm.org/talks/

Before I reply let me just watch some talks on it.

Actually, let me spell checkit, reply right now and then I'll give my thoughts on it in future emails.

7:45pm. Yeah, this is a good thing as it is 2.5 pages long as it is.

8pm. Let me send it. I'll also snip the emails I pasted into the journal. I'll be pro here and leave private correspondence where it should be.

8:10pm. Sent, let me close here for the day. Let me get back to relaxing as this rose my stress level. I spent 3h on crafting that reply. It was fun, but I do not have much work capacity now. I need to focus on resting my overheated brain.

9:25pm. Let me watch the BRS episode and I am going to bed. I am getting a headache. It is not worth it for me to push myself.

4/20/2022

8:50am. I am stressed out as expected. It seems I forgot to commit yesterday. I am still not myself just yet, but given that I've got some correspondence going, it gives me hope that I'll be able to close the Strong Compute either positively or negatively in the nearby future, and get this burden unloaded.

Right now I am skeptical whether those guys want to specifically sponsor Spiral instead of simply wanting a guy who is very good at programming, PL and ML at the same time. I need to inquire about their technology choices. Why Elixir and not Julia for example? I asked why Spiral in the email. I also want to ask why MLIR compared to existing libraries? What is the current state of the ML ecosystem in Elixir?

Would they be better served by a MLIR DSL in Elixir instead of Spiral? The email mentioned hoping MLIR matures so it can better serve new GPUs as they arrive on the market. Is that important to them? Because GPUs in the ML arena are basically just Nvidia. Is MLIR more than for just GPUs?

I'll have to find this out. Let me watch a MLIR talk or two. I am going to get this out of the way.

If I can get back to programming fine, if not, I want to get back to cultivating art. Let get on with it. Time's wasting!"

---
## [woodsts/linux-stable](https://github.com/woodsts/linux-stable)@[38b0bd0f25...](https://github.com/woodsts/linux-stable/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Wednesday 2022-04-20 07:17:08 by Linus Torvalds

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
## [josefzac/Real-AZ-303-Exam-Questions---How-Can-I-Pass-Actual-Exam-](https://github.com/josefzac/Real-AZ-303-Exam-Questions---How-Can-I-Pass-Actual-Exam-)@[a6619c8613...](https://github.com/josefzac/Real-AZ-303-Exam-Questions---How-Can-I-Pass-Actual-Exam-/commit/a6619c8613aaa789d3c9f18621e06528039be026)
#### Wednesday 2022-04-20 09:54:28 by josefzac

Update README.md

Real AZ-303 Exam Questions - Complete preparation material for the AZ-303 Certification Exam

Where Do I Get Real AZ-303 Exam Questions and Answers?

Based on the reviews of the online Microsoft AZ-303 exam preparation material, the Exams Hero AZ-303 Exam BrainDumps is the most preferred Real AZ-303 Exam Questions and Answers over the internet. The AZ-303 Questions and answers are always committed to keeping its AZ-303 Practice Test Questions content the most updated AZ-303 study guides. Prepare with the most updated AZ-303 Exam Questions & Answers, exhaustive and 100% success guaranteed test preparation material for Microsoft Azure Architect Technologies Exam exam.

Valid AZ-303 Exam Preparation Material: Shortcut to Success:

By Using the comprehensive AZ-303 Study material for the Microsoft Azure Architect Technologies Exam Certification Exam, you will get Azure Solutions Architect Expert Certificate easily without wasting your money or time from the first exam attempt. With the AZ-303 preparation material for the Azure Solutions Architect Expert Certification Test, it helps you judge yourself and improve your weak areas. This is an important aspect in preparing actual Microsoft Azure Architect Technologies Exam Certification Test or any competitive exam like the AZ-303 Certification Exam.

Actual   AZ-303 study questions are designed by a group of more than thousands of talented Microsoft Technology experts and professionals. The Microsoft Azure Architect Technologies Exam practice questions for the Certification Exam are based on the latest AZ-303 exam syllabus.

Microsoft AZ-303 PDF Questions and Answers for Exam Preparation.

Using the Azure Solutions Architect Expert PDF Questions and Answers from Exams Hero is easy to use with no installation required. The AZ-303 PDF exam material can be used on all your smart devices (Mobiles, Tablets, and PCs). With the portable and printable option, you can take the AZ-303 pdf file anywhere you go. Exams Hero Microsoft Azure Architect Technologies Exam preparation material is always update and revised.

User-friendly AZ-303 questions pdf file that contains a huge number of various AZ-303 test Questions that are similar to the AZ-303 real exam questions, that to help our customers in better self-assessment. With storing your results. The Azure Solutions Architect Expert AZ-303 practice test questions can keep track of all your previous Microsoft Azure Architect Technologies Exam Exam attempts and at the end of each attempt, it will preview all the changes.

Get Microsoft Azure Architect Technologies Exam Updated Questions PDF – Get Free Trial

Download free AZ-303 Exam Questions demo; it will be an excellent measure that will be most helpful in scaling the quality of AZ-303 real questions. Downloadable full version is available. The Exams Hero gives 100% money back guarantees. If you have failed to pass the AZ-303 Certification Exam, the Exams Hero will return 100% of your money. (Conditions are applied.)

Go With Microsoft Azure Architect Technologies Exam AZ-303 Practice Questions For 100% success:

Preparing for the Microsoft Azure Architect Technologies Exam exam is never an easy task besides Microsoft’s high registration fees for some exams. So, you will need complete AZ-303 Test Questions with a clear strategy to help you get high scores from the first exam attempt.

The Exams Hero built a smoothly AZ-303 exam preparation material that will be your gate to success and getting Azure Solutions Architect Expert Certified safely. We provide the Actual  AZ-303 Questions Answers will be your first step toward your dream certificate. Get ready to ace your next Azure Solutions Architect Expert certification exam from Microsoft using the Exams Hero AZ-303 Exam Questions PDF.

Join us now and be one of the successful Azure Solutions Architect Expert Certified customers; it will be your best move ever.


AZ-303 Practice Exam Questions | Microsoft Azure Architect Technologies Exam PDF Questions | AZ-303 Dumps | AZ-303 PDF Dumps | AZ-303 Exam Dumps | AZ-303 PDF Questions | AZ-303 Dumps PDF | AZ-303 Exam Questions

---
## [benjaminhuth/acts](https://github.com/benjaminhuth/acts)@[6e1fd31474...](https://github.com/benjaminhuth/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Wednesday 2022-04-20 10:21:38 by Stephen Nicholas Swatman

feat: Implement a new orthogonal range search seed finder (#904)

As I said in #901, I have been playing around with seed finding a little bit lately. Last weekend, I mentioned an idea for a new (?) kind of seed finding algorithm based on range search datastructures, and this is the very, very first semi-working implementation of it, just before the weekend.

The idea behind this algorithm is relatively simple. In traditional seedfinding, we check a whole lot of candidate spacepoints to see whether they meet some condition. If you look at this differently, each spacepoint defines a volume in the z-r-φ space, which contains any spacepoints it can form a doublet with. What if we reversed this logic? What if we defined this volume first, and then just extract the spacepoints inside of that space? That way, we can vastly reduce the number of spacepoints we need to look at.

How do we do this quickly? With [_k_-d trees](https://en.wikipedia.org/wiki/K-d_tree). These data structures are cheap to build, and they give us very fast orthogonal range searches. In other words, we can very quickly look up which of our spacepoints lie within an axis-aligned orthognal n-dimensional hyperrectangle. In this case, which spacepoints lie within a z-r-φ box.

So, the core idea of this seedfinder is to define as many of our seedfinding constraints in orthogonal fashion. That way, we can make our candidate hyperrectangle smaller and smaller. The tighter the constraints we can place, the better. Then, we look up the relevant spacepoints, and we can avoid looking at any others. That also means this solution requires no binning whatsoever.

## Constraint conversion

Currently there are quite a few constraints in the code. Here is my status update on how well it is going to convert each of them. In some cases, we can define a weaker version of the constraints in orthogonal fashion. This is still very powerful, and it doesn't actually lose us any efficiency (because we can always check the tighter constraint in a non-orthogonal way later, not a problem)!

### Unary constraints

Currently, I am not aware of any unary constraints in the Acts seed finding code. That is to say, logic to determine whether a point is allowed to be a lower spacepoint. However, I have the following thoughts about introducing some:

* I believe the binning code does some kind of magic to determine whether a spacepoint can be a lower spacepoint. Since my solution doesn't use any binning, I don't have access to this just yet. However, if we can incorporate this logic it could be very powerful.
* Maximum single-point η: we currently have some checks in place to see if the pseudorapidity of particles is not too high. We could realistically use this maximum pseudorapidity, combined with the collision region range to constrain the bottom spacepoints.

### Binary constraints

These are the existing binary constraints on spacepoint duplets:

Constraint | Description | Orthogonalization
-|-|-
Minimum ∆r | Ensure that the second spacepoint is within a certain difference in radius | Full
Maximum cot θ | Ensure that the pseudorapidity of the duplet is not too high | Unsuccessful
z-origin range | Ensure that the duplet would have originated from the collision point | Weakened 
Maximum ∆φ<sup>1</sup> | Ensure that the duplet does not bend too much in the x-y plane | Full

<sup>1</sup> This check does not exist explicitly in the existing seed finder, but is implicit in the binning process.

### Ternary constraints

There are a lot of ternary constraints (to check whether a triplet is valid):

Constraint | Description | Orthogonalization
-|-|-
Scattering angle | ??? | Unsuccessful
Helix diameter | Ensure the helix diameter is within some range | In progress
Impact parameters | Ensure the impact parameters are close to the collision point | In progress
Monotonic z<sup>1</sup> | Ensure that z increases or decreases monotonically between points | Full

<sup>1</sup> This check does not exist in the existing seed finder, check #901.

There are also constraints defined in the experiment-specific cuts, and the seed filter, and in other places. If we could convert some of those to orthogonal constraints the implementation would become much more powerful. However, I don't really understand what is happening in those files just yet. Need more reading.

## Current performance

The current performance of this seedfinder is... Complicated. On my machine, it runs a 4000 π<sup>+</sup> event in about 5 seconds, three times slower than the existing seedfinder. Its efficiency is much higher though, and the fake rate is much lower. So that's something. However, that is in part because I am creating far more seed candidates, so take this with a big grain of salt.

## Potential gain

There are two ways that I can think of to use this kind of algorithm. The first is an inside-to-outside algorithm, where we pick a lower spacepoint first, check the space it defines for a middle spacepoint, and then check the space the two of them define for a third spacepoint. This algorithm has time complexity 𝒪(_n_<sup>3</sup>), and it has space complexity 𝒪(_n_). Due to the constants, I still believe this implementation can outperform the 𝒪(_n_<sup>2</sup>) existing algorithm, however.

The second way would be to construct a set of duplets using this logic, and then to fit those together like we do with traditional seedfinding. This has 𝒪(_n_<sup>2</sup>) time complexity like the existing code, but also space complexity 𝒪(_n_<sup>2</sup>).

## Things that are completed

* The implementation of the _k_-d tree seems to work very well, and it is quite fast.
* Basic seedfinding using this strategy is functional.

## Things that don't work yet

* My maximum ∆φ constraint does not cross the 2π boundary yet.
* I used the existing seedfinding algorithm as a stepping stone, which I have completely destroyed in the process. Obviously I do not intend on keeping it that way, and the existing algorithm will be restored to its full glory.
* Lots more.

## Things that can be improved

* Add more constraints, and tighten existing ones.
* Lots of things, pretty much everything. But I really want to go home for the weekend, so I will write this part next week.

---
## [norkunas/symfony-docs](https://github.com/norkunas/symfony-docs)@[af131ba7cb...](https://github.com/norkunas/symfony-docs/commit/af131ba7cb31dc2f65c9fb56332ce6d138b36b22)
#### Wednesday 2022-04-20 10:40:03 by Javier Eguiluz

minor #16084 Move myself alongside the inactive Core team members. (sroze)

This PR was submitted for the 5.4 branch but it was merged into the 4.4 branch instead.

Discussion
----------

Move myself alongside the inactive Core team members.

**What a fun ride!** This community is the best I've been working with, full of talented and caring people. I've learnt so much by fixing `@nicolas`-grekas' broken tests or convincing `@fabpot` to ship this Messenger component. I also hope that this modest contribution to the ever-growing list of components inspires others to do the same, give back to an open-source project that enabled me as an engineer to be always more productive and enables us all to focus on solving worlds' problems rather than re-inventing the wheel again.

**I won't have much time for Symfony in the coming 12 months, at least.** For a fair chunk of time already, I have not been able to devote enough time to maintaining and evolving Symfony, and it will remain the same for a little while: I want to focus my energy on building mission-driven startups and it requires my full attention to make them successful. It means I'm not really a Core Team member anymore, so let's make it official so the list can be expanded with great people that have the time I don't.

`@symfony`/mergers thank you so much for your continuous work and care for this amazing project, I know it can only continue to shine. See you in the real world at some conferences, I'm sure ❤️

Commits
-------

2ffdccb54 Move myself alongside the inactive Core team members.

---
## [input-output-hk/ouroboros-network](https://github.com/input-output-hk/ouroboros-network)@[06d95c575a...](https://github.com/input-output-hk/ouroboros-network/commit/06d95c575a3eb19c883c11debe7524a2a2088ef4)
#### Wednesday 2022-04-20 11:12:30 by Nicholas Clarke

Integrate the Babbage ledger era.

- The BabbageEra is imported from cardano-ledger-babbage and added to
  `CardanoEras` etc.
- A new Babbage era is added to the Shelley codebase, and made an
  instance of `ShelleyBasedEra`. Note the slightly weird
  `TranslationContext` - we need to use the Alonzo translation context
  because of the assumption (in `ShelleyBasedEra`) that the translation
  context is equal to the `AdditionalGenesisConfig`. The latter is a
  diff from `Shelley`, whereas the former is a diff from the previous
  era.

  TODO We should drop this assumption and correct the relationship
  between these things.
- We introduce a new class, `SupportsTwoPhaseValidation`, to reuse code
  for dealing with 2-phase validation in Alonzo and subsequent eras.
- Add standard boilerplate patterns for the Babbage era (particularly in
  Ouroboros.Consensus.Cardano.Block).
- We add additional translation code to translate from Alonzo to
  Baggage. This is slightly more complex than usual, since it must also
  translate from TPraos to Praos. It's generally formulaic, however.
- New protocol versions are introduced supporting the Babbage era.
- `protocolInfoCardano` is expanded with configuration for
  Babbage/Praos. Again, this is largely straightforward.
- Block forging code for Praos is now uncommented, since there is a
  Praos era to work on.
- The block forging code for the TPraos eras is adjusted to add a "skip"
  at the end, for the Babbage era. Honestly, this is rather ugly, but
  it's the simplest approach right now.

---
## [TheLastRar/pcsx2](https://github.com/TheLastRar/pcsx2)@[89f10e1605...](https://github.com/TheLastRar/pcsx2/commit/89f10e160572063b4871bfb8d0c6ffff54f9543a)
#### Wednesday 2022-04-20 11:48:41 by RedDevilus

GameDB:  ':' to '-' + GS and other fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Outrun 2006 / 2 SP
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

Also made sure that the comments and their spacing were consistent.

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[8d3cddc6a8...](https://github.com/Stalkeros2/Skyrat-tg/commit/8d3cddc6a8bcf438d8f3ca18eefe7e27ca40e06c)
#### Wednesday 2022-04-20 11:50:49 by SkyratBot

[MIRROR] NukeOps Firebase Rework [MDB IGNORE] (#12861)

* NukeOps Firebase Rework (#66149)

Attention Recruit: Welcome to Firebase Balthazord
Here you will lean how to:
-Kill corpo scum
-Kill corpo scum
-Kill corpo scu-

This has been on my docket for months. Ever since gave the Holding Facility a much needed facelift. I have been eyeballing the nukie base, waiting for that stroke of inspiration to hit me. It finally did. Gone are the aging walls of the old encampment. Nukies finally have what well-funded corpo-terrorists always dream of- a home.

It's more than a Home. This is a sweeping rework that is part of a series of reworks to revisit old locations and not only bring them up to date with our current asset roster, but to make them properly belong within the game world. The Nuke-Ops base may ultimately be a tiny chunk of the overall SS13 experience, but I'll be damned if it isn't a defining one. It's also a location that has the capacity to do one thing that I have always wanted to do. Purchase Property. You heard me right, you get to buy rooms now. The newly expanded Nuke-Ops base features, with @ Mothblocks blessing, further expansions that you can purchase from your local Syndicate Uplink. Spend your TC, expand your capabilities, and utilize your expertise in order to create
the most mind-boggling disky heists there are.

Possible expansions to your terrorism suite include:
-Ordinance Lab
-Bio-Terrorism Lab
-Chemical Manufacturing Plant

Definite expansions to your Nuke-Ops Firebase include:
-Crew Bunks
-Lab Wing
-War Table
-Upgraded "Disembarkment" Bay"

* NukeOps Firebase Rework

* Update CentCom_skyrat.dmm

Co-authored-by: Zytolg <33048583+Zytolg@users.noreply.github.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>

---
## [havenstadrp/qb-vehiclekeys](https://github.com/havenstadrp/qb-vehiclekeys)@[757fdd0859...](https://github.com/havenstadrp/qb-vehiclekeys/commit/757fdd0859013e45f9d432fa894f0ecb03d8bbf5)
#### Wednesday 2022-04-20 12:23:21 by ItsANoBrainer

Proper Refactor

Refactored the entire resource because the key system was not working.

No longer does a server callback 10 or so times a second, on top of other bad practices.

Tested pretty much everything with my devs, but there might be some weird issues we havnt found. Please lookover as I've been going crazy with the small tedious issues I've come across doing this.

Throwing this up to get feedback, and for people to use who want it.

Features:

- Keys are saved server side, and sent to each client when they are added or removed, as well as on character selection. This allows characters to leave and come back in the same server uptime session and still have the same keys
- Keys are only pulled from the server once on character load
- Giving keys has 3 types, /givekeys with an id will attempt to give keys you have to an id, not including an id will try to give it to the closest person, and if you're in a vehicle it will give to everyone
- Can only give keys to vehicles you have keys to
- Server event to force acquire keys to a plate for a person (for lockpicking/stealing/spawning, etc.)
- Can Carjack an NPC with a gun, has different percentages to work based on weapon (config)
- Take keys from dead npc drivers
- Can lockpick a car to unlock the doors
- Can hotwire a car if you're in the driver seat of the vehicle you dont have keys to to get keys
- Keeps the engine of a vehicle off if you dont have keys to it (allows other resources to attempt to toggle car engine without needing to interface if you have keys or not)
- Vehicle blacklist system for vehicles you dont want to be lockable (always unlocked)
- Police Alerts from lockpicking/hotwiring/carjacking
- Export to check if you have keys to a vehicle
- Locking/unlocking with hotkey
- Locking/unlocking and giving keys uses a custom GetVehicleInDirection you are facing for realism/accuracy
- Fully compatible with old resource. Has an event handler for 'vehiclekeys:client:SetOwner' in which it gives keys for that plate
- Some other shit I probably forgot

TODO:
- Add LOCALE support
- Stop peds from wanting to get back into the vehicle they just got carjacked out of as they're fleeing

---
## [ajgarlag/laminas-httphandlerrunner](https://github.com/ajgarlag/laminas-httphandlerrunner)@[0ba40749af...](https://github.com/ajgarlag/laminas-httphandlerrunner/commit/0ba40749af285cc8d76628b0edc3a6f6f4e69043)
#### Wednesday 2022-04-20 12:30:52 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [JuliaLang/julia](https://github.com/JuliaLang/julia)@[ccf78165e3...](https://github.com/JuliaLang/julia/commit/ccf78165e3d0db690934864a9a9f407de8878071)
#### Wednesday 2022-04-20 13:10:52 by Mirek Kratochvil

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
## [rustyhorde/cargo](https://github.com/rustyhorde/cargo)@[6a4d98d232...](https://github.com/rustyhorde/cargo/commit/6a4d98d2327124ca52bb9f67d6ad0097eb6b2e65)
#### Wednesday 2022-04-20 13:22:23 by bors

Auto merge of #10472 - epage:add, r=ehuss

feat: Import cargo-add into cargo

### Motivation

The reasons I'm aware of are:
- Large interest, see #5586
- Make it easier to add a dependency when you don't care about the version (instead of having to find it or just using the major version if thats all you remember)
- Provide a guided experience, including
  - Catch or prevent errors earlier in the process
  - Bring the Manifest format documentation into the terminal via `cargo add --help`
  - Using `version` and `path` for `dependencies` but `path` only for `dev-dependencies` (see crate-ci/cargo-release#288 which led to killercup/cargo-edit#480)

### Drawbacks

1. This is another area of consideration for new RFCs, like rust-lang/rfcs#3143 (this PR supports it) or rust-lang/rfcs#2906 (implementing it will require updating `cargo-add`)

2. This is a high UX feature that will draw a lot of attention (ie Issue influx)

e.g.
- killercup/cargo-edit#521
- killercup/cargo-edit#126
- killercup/cargo-edit#217

We've tried to reduce the UX influx by focusing the scope to preserving semantic information (custom sort order, comments, etc) but being opinionated on syntax (style of strings, etc)

### Behavior

Help output
<details>

```console
$ cargo run -- add --help
cargo-add                                                                                                                                  [4/4594]
Add dependencies to a Cargo.toml manifest file

USAGE:
    cargo add [OPTIONS] <DEP>[`@<VERSION>]` ...
    cargo add [OPTIONS] --path <PATH> ...
    cargo add [OPTIONS] --git <URL> ...

ARGS:
    <DEP_ID>...    Reference to a package to add as a dependency

OPTIONS:
        --no-default-features     Disable the default features
        --default-features        Re-enable the default features
    -F, --features <FEATURES>     Space-separated list of features to add
        --optional                Mark the dependency as optional
    -v, --verbose                 Use verbose output (-vv very verbose/build.rs output)
        --no-optional             Mark the dependency as required
        --color <WHEN>            Coloring: auto, always, never
        --rename <NAME>           Rename the dependency
        --frozen                  Require Cargo.lock and cache are up to date
        --manifest-path <PATH>    Path to Cargo.toml
        --locked                  Require Cargo.lock is up to date
    -p, --package <SPEC>          Package to modify
        --offline                 Run without accessing the network
        --config <KEY=VALUE>      Override a configuration value (unstable)
    -q, --quiet                   Do not print cargo log messages
        --dry-run                 Don't actually write the manifest
    -Z <FLAG>                     Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for
                                  details
    -h, --help                    Print help information

SOURCE:
        --path <PATH>        Filesystem path to local crate to add
        --git <URI>          Git repository location
        --branch <BRANCH>    Git branch to download the crate from
        --tag <TAG>          Git tag to download the crate from
        --rev <REV>          Git reference to download the crate from
        --registry <NAME>    Package registry for this dependency

SECTION:
        --dev                Add as development dependency
        --build              Add as build dependency
        --target <TARGET>    Add as dependency to the given target platform

EXAMPLES:
  $ cargo add regex --build
  $ cargo add trycmd --dev
  $ cargo add --path ./crate/parser/
  $ cargo add serde serde_json -F serde/derive
```

</details>

Example commands
```rust
cargo add regex
cargo add regex serde
cargo add regex@1
cargo add regex@~1.0
cargo add --path ../dependency
```
For an exhaustive set of examples, see [tests](https://github.com/killercup/cargo-edit/blob/merge-add/crates/cargo-add/tests/testsuite/cargo_add.rs) and associated snapshots

Particular points
- Effectively there are two modes
  - Fill in any relevant field for one package
  - Add multiple packages, erroring for fields that are package-specific (`--rename`)
  - Note that `--git` and `--path` only accept multiple packages from that one source
- We infer if the `dependencies` table is sorted and preserve that sorting when adding a new dependency
- Adding a workspace dependency
  - dev-dependencies always use path
  - all other dependencies use version + path
- Behavior is idempotent, allowing you to run `cargo add serde serde_json -F serde/derive` safely if you already had a dependency on `serde` but without `serde_json`
- When a registry dependency's version req is unspecified, we'll first reuse the version req from another dependency section in the manifest.  If that doesn't exist, we'll use the latest version in the registry as the version req

### Additional decisions

Accepting the proposed `cargo-add` as-is assumes the acceptance of the following:
- Add the `-F` short-hand for `--features` to all relevant cargo commands
- Support ``@`` in pkgids in other commands where we accept `:`
- Add support for `<name>`@<version>`` in more commands, like `cargo yank` and `cargo install`

### Alternatives

- Use `:` instead of ``@`` for versions
- Flags like `--features`, `--optional`, `--no-default-features` would be position-sensitive, ie they would only apply to the crate immediate preceding them
  - This removes the dual-mode nature of the command and remove the need for the `+feature` syntax (`cargo add serde -F derive serde_json`)
  - There was concern over the rarity of position-sensitive flags in CLIs for adopting it here
- Support a `--sort` flag to sort the dependencies (existed previously)
  - To keep the scope small, we didn't want general manifest editing capabilities
- `--upgrade <POLICY>` flag to choose constraint (existed previously)
  - The flag was confusing as-is and we feel we should instead encourage people towards `^`
- `--allow-prerelease` so a `cargo add clap` can choose among pre-releases as well
  - We felt the pre-release story is too weak in cargo-generally atm for making it first class in `cargo-add`
- Offer `cargo add serde +derive serde_json` as a shorthand
- Infer path from a positional argument

### Prior Art

- *(Python)* [poetry add](https://python-poetry.org/docs/cli/#add)
  - `git+` is needed for inferring git dependencies, no separate  `--git` flags
  - git branch is specified via a URL fragment, instead of a `--branch`
- *(Javascript)* [yarn add](https://yarnpkg.com/cli/add)
  - `name@data` where data can be version, git (with fragment for branch), etc
  - `-E` / `--exact`, `-T` / `--tilde`, `-C` / `--caret` to control version requirement operator instead of `--upgrade <policy>` (also controlled through `defaultSemverRangePrefix` in config)
  - `--cached` for using the lock file (killercup/cargo-edit#41)
  - In addition to `--dev`, it has `--prefer-dev` which will only add the dependency if it doesn't already exist in `dependencies` as well as `dev-dependencies`
  - `--mode update-lockfile` will ensure the lock file gets updated as well
- *(Javascript)* [pnpm-add](https://pnpm.io/cli/add)
- *(Javascript)* npm doesn't have a native solution
  - Specify version with ``@<version>``
  - Also overloads `<name>[`@<version>]`` with path and repo
    - Supports a git host-specific protocol for shorthand, like `github:user/repo`
    - Uses fragment for git ref, seems to have some kind of special semver syntax for tags?
  - Only supports `--save-exact` / `-E` for operators outside of the default
- *(Go)* [go get](https://go.dev/ref/mod#go-get)
  - Specify version with ``@<version>``
  - Remove dependency with ``@none``
- *(Haskell)* stack doesn't seem to have a native solution
- *(Julia)* [pkg Add](https://docs.julialang.org/en/v1/stdlib/Pkg/)
- *(Ruby)* [bundle add](https://bundler.io/v2.2/man/bundle-add.1.html)
  - Uses `--version` / `-v` instead of `--vers` (we use `--vers` because of `--version` / `-V`)
  - `--source` instead of `path` (`path` correlates to manifest field)
  - Uses `--git` / `--branch` like `cargo-add`
- *(Dart)* [pub add](https://dart.dev/tools/pub/cmd/pub-add)
  - Uses `--git-url` instead of `--git`
  - Uses `--git-ref` instead of `--branch`, `--tag`, `--rev`

### Future Possibilities

- Update lock file accordingly
- Exploring the idea of a [`--local` flag](https://github.com/killercup/cargo-edit/issues/590)
- Take the MSRV into account when automatically creating version req (https://github.com/killercup/cargo-edit/issues/587)
- Integrate rustsec to report advisories on new dependencies (https://github.com/killercup/cargo-edit/issues/512)
- Integrate with licensing to report license, block add, etc (e.g. https://github.com/killercup/cargo-edit/issues/386)
- Pull version from lock file (https://github.com/killercup/cargo-edit/issues/41)
- Exploring if any vendoring integration would be beneficial (currently errors)
- Upstream `cargo-rm` (#10520), `cargo-upgrade` (#10498), and `cargo-set-version` (in that order of priority)
- Update crates.io with `cargo add` snippets in addition to or replacing the manifest snippets

For more, see https://github.com/killercup/cargo-edit/issues?q=is%3Aissue+is%3Aopen+label%3Acargo-add

### How should we test and review this PR?

This is intentionally broken up into several commits to help reviewing
1. Import of production code from cargo-edit's `merge-add` branch, with only changes made to let it compile (e.g. fixing up of `use` statements).
2. Import of test code / snapshots.  The only changes outside of the import were to add the `snapbox` dev-dependency and to `mod cargo_add` into the testsuite
3. This extends the work in #10425 so I could add back in the color highlighting I had to remove as part of switching `cargo-add` from direct termcolor calls to calling into `Shell`

Structure-wise, this is similar to other commands
- `bin` only defines a CLI and adapts it to an `AddOptions`
- `ops` contains a focused API with everything buried under it

The "op" contains a directory, instead of just a file, because of the amount of content.  Currently, all editing code is contained in there.  Most of this will be broken out and reused when other `cargo-edit` commands are added but holding off on that for now to separate out the editing API discussions from just getting the command in.

Within the github UI, I'd recommend looking at individual commits (and the `merge-add` branch if interested), skipping commit 2.  Commit 2 would be easier to browse locally.

`cargo-add` is mostly covered by end-to-end tests written using `snapbox`, including error cases.

There is additional cleanup that would ideally happen that was excluded intentionally from this PR to keep it better scoped, including
- Consolidating environment variables for end-to-end tests of `cargo`
- Pulling out the editing API, as previously mentioned
  - Where the editing API should live (`cargo::edit`?)
  - Any more specific naming of types to reduce clashes (e.g. `Dependency` or `Manifest` being fairly generic).
- Possibly sharing `SourceId` creation between `cargo install` and `cargo edit`
- Explore using `snapbox` in more of cargo's tests

Implementation justifications:
- `dunce` and `pathdiff` dependencies: needed for taking paths relative to the user and make them relative to the manifest being edited
- `indexmap` dependency (already a transitive dependency): Useful for preserving uniqueness while preserving order, like with feature values
- `snapbox` dev-dependency: Originally it was used to make it easy to update tests as the UX changed in prep for merging but it had the added benefit of making some UX bugs easier to notice so they got fixed.  Overall, I'd like to see it become the cargo-agnostic version of `cargo-test-support` so there is a larger impact when improvements are made
- `parse_feature` function: `CliFeatures` forces items through a `BTreeSet`, losing the users specified order which we wanted to preserve.

### Additional Information

See also [the internals thread](https://internals.rust-lang.org/t/feedback-on-cargo-add-before-its-merged/16024).

Fixes #5586

---
## [DEMOLITIONDON96/Demolition-Engine](https://github.com/DEMOLITIONDON96/Demolition-Engine)@[dcde793c98...](https://github.com/DEMOLITIONDON96/Demolition-Engine/commit/dcde793c981d73f9fb3d6376ece1d8074e06d059)
#### Wednesday 2022-04-20 14:14:45 by DEMOLITIONDON96

Disabled for now

That shit gets annoying real fucking fast

---
## [ProjectIgnis/LFLists](https://github.com/ProjectIgnis/LFLists)@[48bfc997e1...](https://github.com/ProjectIgnis/LFLists/commit/48bfc997e12635dc9cedfad818d252595f7ec4f1)
#### Wednesday 2022-04-20 14:43:39 by pyrQ

Rush whitelist: Added new Rush cards + "Deck Modification Pack - Galaxy of Fate!!" official release

From "Go Rush Deck Bonus Cards":
- Pitch-Black Warwolf
- Alien Shocktrooper
- Dark Factory of Mass Production
- Tribute Doll
From "Go Rush Deck - Galactica Arrive":
- Galactica Amnesia
- Rebirth Cycle
- Heaven Gancel
- Strange Traveler
- Bright Sentinel
- Shadow Sentinel
- Asteroeva
- Galactica Force
- Vacua Annihilation
- Nebula Power
From "Go Rush Deck - Jointech Attack":
- Gadget Soldier
- Lightning Braver
- Jointech Bumper
The "Saikyō Jump June 2022" promo:
- Direct Dive Dragon
From "Megaroad Pack":
- Magician of Dark Sevens
- Darkness Zerorogue
- Darkness Fource Seeker
- Darkness Rogue
- Road Magic - Dark Night
- Magic Fire Guard

In addition, the cards from "Deck Modification Pack - Galaxy of Fate!!" are now out of pre-release.

ProjectIgnis/BabelCDB@fccfed3fec4a655ae05ddf5a3a0a4d6cd446b856

---
## [4ug-aug/Otovo-OptimalControl](https://github.com/4ug-aug/Otovo-OptimalControl)@[4b9918140f...](https://github.com/4ug-aug/Otovo-OptimalControl/commit/4b9918140fee27161b3a62fd0e41004308f1f780)
#### Wednesday 2022-04-20 14:57:44 by LortSkit

Arima is NOT done, don't  run it

This shit is killing me from the inside, I can feel God's wrap around my frail body as he launches me near the speed of light and I'm passing out as I'm hurdling too fast for me to comprehend towards hell for having completely lost it and killed five people in 2017

---
## [ItsProf-org/my_whatever_kernel](https://github.com/ItsProf-org/my_whatever_kernel)@[4e15ee7d88...](https://github.com/ItsProf-org/my_whatever_kernel/commit/4e15ee7d885673c5a1f908c9ff5e105c0a4ad8a5)
#### Wednesday 2022-04-20 15:07:23 by Wang Han

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
Signed-off-by: ImLonely13 <gabutuhaku@gmail.com>

---
## [dotnet/msbuild](https://github.com/dotnet/msbuild)@[a572dc6b79...](https://github.com/dotnet/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Wednesday 2022-04-20 15:54:14 by Forgind

Fix low priority issues (#7413)

Thanks @svetkereMS for bringing this up, driving, and testing.

This fixes two interconnected issues.
First, if a process starts at normal priority then changes to low priority, it stays at normal priority. That's good for Visual Studio, which should stay at normal priority, but we relied on passing priority from a parent process to children, which is no longer valid. This ensures that we set the priority of a process early enough that we get the desired priority in worker nodes as well.

Second, if we were already connected to normal priority worker nodes, we could keep using them. This "shuts down" (disconnects—they may keep running if nodeReuse is true) worker nodes when the priority changes between build submissions.

One non-issue (therefore not fixed) is connecting to task hosts that are low priority. Tasks host nodes currently do not store their priority or node reuse. Node reuse makes sense because it's automatically off always for task hosts, at least currently. Not storing low priority sounds problematic, but it's actually fine because we make a task host—the right priority for this build, since we just made it—and connect to it. If we make a new build with different priority, we disconnect from all nodes, including task hosts. Since nodeReuse is always false, the task host dies, and we cannot reconnect to it even though if it didn't immediately die, we could, erroneously.

On the other hand, we went a little further and didn't even specify that task hosts should take the priority assigned to them as a command line argument. That has been changed.

svetkereMS had a chance to test some of this. He raised a couple potential issues:

conhost.exe launches as normal priority. Maybe some custom task dlls or other (Mef?) extensions will do something between MSBuild start time and when its priority is adjusted.
Some vulnerability if MSBuild init code improperly accounts for timing
For (1), how is conhost.exe related to MSBuild? It sounds like a command prompt thing. I don't know what Mef is.
For (2), what vulnerability? Too many processes starting and connecting to task hosts with different priorities simultaneously? I could imagine that being a problem but don't think it's worth worrying about unless someone complains.

He also mentioned a potential optimization if the main node stays at normal priority. Rather than making a new set of nodes, the main node could change the priority of all its nodes to the desired priority. Then it can skip the handshake, and if it's still at normal priority, it may be able to both raise and lower the priority of its children. Since there would never be more than 2x the "right" number of nodes anyway, and I don't think people will be switching rapidly back and forth, I think maybe we should file that as an issue in the backlog and get to it if we have time but not worry about it right now.

Edit:
I changed "shuts down...worker nodes when the priority changes" to just changing their priority. This does not work on linux or mac. However, Visual Studio does not run on linux or mac, and VS is the only currently known customer that runs in normal priority but may change between using worker nodes at normal priority or low priority. This approach is substantially more efficient than starting new nodes for every switch, disconnecting and reconnecting, or even maintaining two separate pools for different builds.

---
## [BenjaminDoran/Yggdrasil](https://github.com/BenjaminDoran/Yggdrasil)@[b1469b44df...](https://github.com/BenjaminDoran/Yggdrasil/commit/b1469b44df4c63961a6c0f0387a89ef4ef24aa26)
#### Wednesday 2022-04-20 16:57:10 by Elliot Saba

[GCCBootstrap_jll] Build using `crosstool-ng` (#4753)

In the beginning, I wanted to compile a nice little standalone `GCC_jll`
that could be hooked together with a `Glibc_jll` and a `Binutils_jll`,
and a `LinuxKernelHeaders_jll`, etc...  That work is sitting in [0] but
bootstrapping is such a giant pain in the neck that I wanted to give up
the complexity of bootstrapping to instead focus on simply building each
product in isolation.  This _vastly_ reduces the amount of work
necessary to get things working, but it introduces a new dependency: we
need a base C compiler and libc that are already compiled for the target
platform.  To be precise, we need a `build -> host` compiler in order to
build a `host -> target` compiler.  We already have one of those for all
of our current platforms, so I could generate `GCC_jll` packages, but
then when we want to add a new platform, we'd be in trouble.  For this
reason, I realized we'll never truly escape the bootstrapping problem.

I thought about reverting back to the bootstrapping configuration we've
had until now, but rebelled at the thought.  Then I discovered
crosstool-ng, and realized that I could separate concerns here: I can
use ct-ng to build a working cross-toolchain for each target, then use
that compiler to do a much simpler build for all of the other
components.  Therefore, I extract the work of getting a bootstrap build
onto crosstool-ng, and then use that to do whatever other builds I want
in the presence of a fully-functional cross-compiler.

This also breaks the need for the initial bootstrap to be quite as
restricted as the target toolchain.  The GCC that we build technically
doesn't need to run everywhere, it just needs to generate code that runs
everywhere.  We can build GCC against glibc 2.19, and then at build time
have it link the code it generates against glibc 2.12.2, and that will
work just fine for BB.  The compiler may be using a newer glibc to run,
but when it builds, it uses whatever glibc is placed within the target
sysroot.  This also means we don't need to do things like build GFortran
as part of our bootstrap; we can build it later, in the simpler build
script.

In principle, we don't actually need a GCCBootstrap for all platforms.
We only need a functional cross-compiler.  Theoretically, we could use
Clang to do the bootstrapping.  But I'm not going to fully embrace that
because I know that compiling Glibc with Clang is a pain, so for
`*-linux-gnu` at the very least, we're not going to attempt that.  On
macOS and FreeBSD however, there is a possibility that we can use Clang
as our "bootstrap compiler" in order to generate the actual GCC_jlls.

[0] https://github.com/JuliaPackaging/Yggdrasil/tree/sf/gcc

---
## [lgritz/oiio](https://github.com/lgritz/oiio)@[594776d9c6...](https://github.com/lgritz/oiio/commit/594776d9c617ab05b3cf0ff17d69dff908c1ae7e)
#### Wednesday 2022-04-20 17:41:59 by Larry Gritz

Speed up case insensitive string comparisons (#3388)

Oh boy, never leave anything unbenchmarked.

Turns out the boost::algorithm functions we were relying on underneath
many Strutil "case-insensitive" comparisons were ridiculously slow.
We thought they were good enough because they allowed specification of
locale, so we could just pass the static classic locale, and so they
would be inexpensive because they didn't have to query the current
locale.  But this is wrong, they were still ghastly.

So here I rewrite Strutil::iequals, iless, starts_with, istarts_with,
ends_with, iends_with in terms of a new (internal) Strutil::strcasecmp
and strncasecmp (which underneath handle differences in platform, and
use the locale-independent versions). The net result is that most of
those case-independent comparisons speed up by a factor of
50-100x. Wow.

I still need to tackle the family of 'ifind' related functions. They
are a bit trickier. But I'll leave them for another time, because I
need to roll this present fix out right away to fix a real production
bottleneck.

(Worth noting: iequals is instrumental when you're searching a
ParamValueList for a particular name, which is what happens when you
look up attributes from an ImageSpec, which is what happens when you
call get_texture_info(), which is what underlies OSL gettextureinfo()
calls in the cases that they cannot be constant-folded during runtime
optimization. So this came to my attention when analyzing a slow scene
whose shaders had a pathological explosion of gettextureinfo calls that
couldn't be optimized away.)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[af66b9dbf0...](https://github.com/mrakgr/The-Spiral-Language/commit/af66b9dbf03180d6738eea329c539e9e0169ccdc)
#### Wednesday 2022-04-20 17:51:43 by Marko Grdinić

"https://dashbit.co/blog/elixir-and-machine-learning-nx-v0.1

Actually, let me first get a glimpse of the Elixir ML ecosystem.

9:30pm. I am thinking. So Nx is a fairly extensive effort even if it is recent.

> Inside defn we can use Elixir regular operators and they are all translated to their equivalent tensor operations. You have access to many of the language features and data types, such as macros, the beloved pipe operator, pattern-matching, maps, and more.

Does Elixir not have operator overloading natively?

At any rate, it seems it has backends for both XLA and LibTorch. Makes more sense that trying to do it all from scratch by themselves.

https://www.tensorflow.org/xla

XLA is Tensorflow's compiler. JAX is another thing from Google entirely and I haven't seen it mentioned.

https://youtu.be/Y4SvqTtOIDk?t=195
2020 LLVM Developers’ Meeting: M. Amini & R. Riddle “MLIR Tutorial”

Now let me focus on the MLIR talk. Suppose they want me to work on a MLIR DSL. I don't understand why they would focus on that instead of Nx instead. Elixir vs Python is not hard to understand if you know just how bad at concurrency Python is. It is extremely awful.

https://youtu.be/Y4SvqTtOIDk?t=239

My skills are a good fit for this. Maybe I could make a Spiral backend for MLIR? I'd need to learn more about it before I make a decision.

https://youtu.be/Y4SvqTtOIDk?t=372

This function cofuses me. Why is it recursively called with just one argument inside the body?

https://youtu.be/Y4SvqTtOIDk?t=554
> Moore's Law Is Real

So that is what MLIR stands for. I see.

https://youtu.be/Y4SvqTtOIDk?t=975

I had to spend some time thinking about this. Those cosntant named argument lists are new to me. Actually I do not understand regions. In the previous slide it feels like they are passing in a record, but here it looks like a function body. So which is it?

Wait, maybe the stuff in {} does not necessarily need to be constant. It certainly makes more sense for it to be the function body. And asd: could just be like Spiral's named tuple.

10:15am. I forgot the syntax of my own language. Does `a: 5` not work anymore?

Indeed it does not. I removed it as it was an eyesore in the v2.1 move.

10:20am. Enough of that, let me get back on track. MLIR is interesting. Even if the opportunity turns to nothing, I'll have gained a bit from studying this.

10:35am. https://youtu.be/Y4SvqTtOIDk?t=1373

I really am having trouble grasping the syntax of MLIR, but it does not matter at this stage. I guess these macro like affines work because ops have to be in strings.

https://youtu.be/Y4SvqTtOIDk?t=1766

This syntax makes sense.

11:25am. https://youtu.be/Y4SvqTtOIDk?t=2547

I've been going off into daydreams as I watch this. If these guys want me to make a MLIR backend for Spiral, then I would be exactly the right man for the job. That would be great! But I am skeptical that this is what they want. Before anything is decided, I need to understand their purpose in contacting me. If they really want to sponsor Spiral that is fine. I'd be happy to make a freebie backend and do some examples for a chance to charge a 2.5k/month rent. If they want to hire me to do actual work for them and are using sponsorship as a pretext, then that is fine too assuming they can meet my price.

Edit: Actually, the effort it would take to do a MLIR backend is way beyond what a simple C/LLVM/F#/Cython/Cuda backend would take so it would not be a freebie, but a full time project.

11:30am. I wonder if Elixir has TCO. I am betting it does.

https://blog.appsignal.com/2019/03/19/elixir-alchemy-recursion.html
> To keep the memory footprint to a minimum, some languages—like Erlang and thus Elixir—implement tail-call optimization.

Wonderful. I already like it more than Julia. Pattern matching and TCO, that is what a real language would have. I do not think too highly of Julia for going after the Matlab crowd.

I wonder what sort of performance Elixir has. I know Python is slow, and JS is fast, but I wonder where Elixir stands amongst them roughly.

https://elixirforum.com/t/elixir-vs-python/25619/12
> I’d love to be proven wrong but I’ve done Project Euler in both languages with no libraries. From my experiences and what I’ve read Elixir/Erlang is much slower than Python.

Oh lol. Well, it does not really matter to me.

https://youtu.be/Y4SvqTtOIDk?t=3650
> Heterogenous compialtion (CUDA, RocM, SPIR-V)

https://rocmdocs.amd.com/en/latest/

I am looking up what RocM is. Never heard of it before.

> AMD ROCm is the first open-source software development platform for HPC/Hyperscale-class GPU computing. AMD ROCm brings the UNIX philosophy of choice, minimalism and modular software development to GPU computing.

SPIR-V? That was embedded right?

https://www.khronos.org/spir/

> SPIR-V is catalyzing a revolution in the ecosystem for shader and kernel language compilers used for expressing parallel computation and GPU-based graphics. SPIR-V enables high-level language front-ends to emit programs in a standardized intermediate form to be ingested by Vulkan, OpenGL or OpenCL drivers. SPIR-V eliminates the need for high-level language front-end compilers in device drivers, significantly reducing driver complexity, enables a broad range of language and framework front-ends to run on diverse hardware architectures and encourages a vibrant ecosystem of open source analysis, porting, debug and optimization tools.

Oh, it is also GPUs.

12:35pm. https://youtu.be/Y4SvqTtOIDk?t=4188

There are some interesting insights in the dev talk towards the end. I find myself becoming alert and rewinding now that he is talking about convolution padding needing to be known at compile time to get good performance.

https://youtu.be/Y4SvqTtOIDk?t=4220

I am guessing he means that at the LLVM level this is not known. Still, this kind of analysis would be covered by Spiral's constant propagation so it might be less necessary. If I plop the constant right there on the LLVM it should take advantage of it, possibly.

If the job was to make a LLVM beackend for Spiral, that would be easy, but MLIR would take more thought.

12:45pm. Let me take a break here.

2:05pm. Maybe the stress of having to deal with the offer is what is wearing me down. I really do feel fatigued now. I can only deal with it by putting effort into studying MLIR. Let me go for more talks. I got the gist of what it is about from the first talk.

But I want some info on what MLIR can really do beyond the basics.

It am really tired right now, but I am too determined to rest. Maybe I am unlucky that this offer came and distrupted my pace, but I do not want to just let it go. If I have a chance to make money using my 5/5 programming skill instead of my 2/5 art skill, I should take it. Do I feel like it, do I not feel like it? I am not sure. That is the source of my stress.

Now that I've watched the first video, an image is forming in my mind regarding what these people want me to do. It will probably be an MLIR backend, plus some kind of library generator so the they can easily access it from Elixir.

Of course, I might be jumping to conclussions, but I can't imagine it being anything else. Doing a Spiral backend for Elixir directly is very unlikely. Even it would not be hard, it would be like doing it for Python - it would waste nearly all of its benefits. And there is Nx, so they probably aren't looking to start their own library from scratch.

What I do not see exactly is what they would use the MLIR backend for. I'll probably get an explanation in the next reply. In the last one I gave them a brief history of Spiral. Maybe that was a mistake and they wanted me to talk about join points. Well, I can easily do that if they want me to.

2:05pm. https://www.youtube.com/watch?v=x-nHc3hBxHM
2021 LLVM Dev Mtg “Compiler Support for Sparse Tensor Computations in MLIR”

Let me watch this not because I am interested in sparse tensors, but merely so I can get a sense of what people are using it for.

https://youtu.be/x-nHc3hBxHM?t=200
> Sparse code lacks spatial and temporal locality, and disables most compiler optimizations.

This is what I would expect.

https://youtu.be/x-nHc3hBxHM?t=476

Hmmm, I see. So you can get a lot of flexibility by simply defining the type like this?

The previous talk had something interesting. That reshape operation worked based on the type rather than taking in explicit arguments. Let me go back to check.

https://youtu.be/Y4SvqTtOIDk?t=2629

Take a look at that second reshape. It seems MLIR is dependently typed.

2:45pm. I have been wondering what good MLIR would be good for, but isn't it obvious by now? The ability to use these kinds of types would be a remarkable addition to Spiral.

https://youtu.be/x-nHc3hBxHM?t=679

Instant sparse libraries. Being able to do these kinds of libraries is what MLIR offers me.

https://youtu.be/x-nHc3hBxHM?t=837

Yeah, this captures my imagination. I can easily imagine Strong Compute guys coming to me to help them manage MLIR.

https://mlir.llvm.org/talks/

Let me go for one more.

https://youtu.be/C_MdJu70z2o?list=PLadGdFFn83gXCQAj8D8LuabxOu3XMbgPJ
[CGO ‘21] Session 1 - MLIR: Scaling Compiler Infrastructure for Domain Specific Computation

I'll watch this.

https://storage.googleapis.com/pub-tools-public-publication-data/pdf/1c082b766d8e14b54e36e37c9fc3ebbe8b4a72dd.pdf

Let me also read these slides first.

> Why a new compiler infrastructure?
> We have LLVM and many other great infras, why do we need something new?

3:40pm. They define things like fused batch norm and leaky relu in MLIR. At this point I can treat it as an actual language to interface with.

3:55pm. https://www.youtube.com/watch?v=C_MdJu70z2o&list=PLadGdFFn83gXCQAj8D8LuabxOu3XMbgPJ&index=2
[CGO ‘21] Session 1 - MLIR: Scaling Compiler Infrastructure for Domain Specific Computation

Let me watch this and then I am done for the day. My mind is working on overdrive. I am sure of what their intent is now.

MLIR is a dependently typed language with great libraries, but hard to interop, difficult syntax and requires type annotations on every statement. They most likely want me to get rid of the bad parts using Spiral.

If that is the case, all I can say is that I am the right man for the job. This is a task I would be best suited for compared to any other programmer in the world.

I'll use Spiral to crack it open and make it a great big library for them to enjoy.

4:15pm. No, I need to hold that attitude in check. I need to do this pro style and not get arrogant or jump to conclussions too much. Remember how it turned out with Z. I need to make every step carefully. That is the way to win. If I am right about their intention, I should be able to chart a high price for this kind of work. But I need to make sure of it first. This is really easy to do, I just need to not be a clown.

4:35pm. Ok, I am dead here. Let me email them again assuming I haven't gotten a reply already explaining their intentions. If I have, I'll have to take some time to think about.

4:50pm. I emailed them with my conjectures. I am not sure how likely it is, they might be just groping around much like I am. If they really have a firm goal in mind, why test me like this?

5:20pm. I've prepared myself mentally for what is to come. I won't dwell on this anymore. At this point it is time for them to come straight and start hashing out the details with me.

I don't care about this anymore, not until the next step gets made.

What I should focus on is art. Forget this PL offer exists. The outside world is weird and weird things could happen to sink it, so I need to guard my ego.

Let me study Moi 3d just for a bit. Let me go back to that Ironman helmet tutorial. I know I am dead tired and want to close

https://youtu.be/O0Lg3jy75NY?t=652

Come to think of it is it possible to take an object and move its edges around like it is for polygons in Blender? This is one of the questions that I wanted to find an answer for.

5:35pm. Oh wow, it is very much possible. I just have to turn on show points on an object and then it is possible to scale and move them with no problem.

https://www.youtube.com/playlist?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Moi 3d

Arrimus has a lot of stuff on Moi.

https://youtu.be/MGaZZ4frjLQ?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Variable Radius Fillets for Problem-Solving and Design

Finally found this. Let me watch it. After I do this I could try making that desk piece. I really need to do some studying for this. I need to master the basics of the program before I can become as effective as in Blender in it.

https://youtu.be/MGaZZ4frjLQ?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=98

Oh, it was this simple. How does this work?

https://youtu.be/MGaZZ4frjLQ?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=119

This is how you change the original. This really blows Blender out of the water in terms of ease of use.

https://youtu.be/MGaZZ4frjLQ?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=208

This is really great. But how would one do the uneven fillets? I'd need those for the bottom part.

6:25pm. I do not know how to do what I want. I bet I could do it using the Blend tool, but I need more knowledge.

https://www.youtube.com/playlist?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Moi 3d

Let me back this up here.

6:30pm. I really wish I could do more for the day, but my fatigue hit its limit. I've been scheming about the PL offer during the night and it continued into day, and it stressed me out. I need to give my brain time to recover. It was not a waste of time either way, taking the offers that come my way seriously is a part of my job. I am doing those Reddit posts for a reason. Winning at art is by no means my only goal right now. It is better than just rotting away if my luck turns out bad in programming.

7:45pm. Let me close here. Rationally, I could expect the Strong Compute guys to come to me with a clear vision of what they wanted done, but this is the real world, so it might be the case that they are just setting some bait seeing if any good ideas come out. I can't discount this, so I should not stress over this anymore. If they want me to talk about Spiral I'll espouse the virtues of join points in my next email. Or maybe talk about the projects I've done in it. But anything more than that should not be needed before they start getting to the point. I'll set a limit before I conclude that my chain is being janked and abide by it.

Tomorrow, I am going to focus on art. Art is what is truly mine and what will sustain me until I get the right hardware and the algorithms. I need to disregard the distractions and focus on mastering Moi 3d."

---
## [Den-Xero/Journeyman_Game](https://github.com/Den-Xero/Journeyman_Game)@[c2e12d3a94...](https://github.com/Den-Xero/Journeyman_Game/commit/c2e12d3a94aaa9c564537756818739286a88dc98)
#### Wednesday 2022-04-20 19:01:20 by McConnell2111

itemspin sorta works with showing the item

today i watched moon knight ep 4 great show if you want some spoilers he dies at the end. also finds a lost dead dude somewhere in the desert. the lass is a badass and she kills people with a flare, more than once. she also finds the truth about her dads death. i think that will do for spoilers enjoy your day and if you read this and are currently watching moonknigh get fked XD

---
## [nagamingorg/qb-core](https://github.com/nagamingorg/qb-core)@[9d83a952c2...](https://github.com/nagamingorg/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Wednesday 2022-04-20 19:27:34 by uShifty

feat: Implement QBCore.Shared.VehicleHashs 

Describe Pull request
Indexs the vehicles jenkins joaat(Hash) value as the key of the table as the key so we dont have to do some shitty ass loop through the vehicles comparing joaat values. I have no clue why this secondary table was removed in the first place if I had to guess people were lazy but this should help the lazys by automatically filling the table.

Questions (please complete the following information):
Have you personally loaded this code into an updated qbcore project and checked all it's functionality? [yes/no] (Be honest) 
Yes

Does your code fit the style guidelines? [yes/no] 
Yes

Does your PR fit the contribution guidelines? [yes/no]
Yes

---
## [znerpy/CIS3120](https://github.com/znerpy/CIS3120)@[b96df70292...](https://github.com/znerpy/CIS3120/commit/b96df702925faf3d0e6803e2ab95dc75a562d184)
#### Wednesday 2022-04-20 19:43:39 by znerpy

Add files via upload

INTERACTING WITH WEB APIS PART II !
Several news sites offer APIs to facilitate the process
of retrieving headlines
• Some news APIs are open because they do not
require user authentication via an API key
• Ex: Hacker News
• Other news APIs do require a specified user agent
• Ex: Reddit
• Most news APIs require a developer key
• Group Project #3
Extracting information from websites can be done via
scraping or by working with the site API if there is
one
• Working with APIs is preferable
• Comparison of Web Scraping vs. API for Hacker News
• Before working with API, you must read the
documentation to familiarize yourself with
• Endpoints (urls to get info through the requests library)
• Parameters to customize your request
• Whether the API is open or requires a developer key
Hacker News is a social news website focusing on
computer science and entrepreneurship.
• Despite its name, it is the most trusted, widely-read,
independent source of the latest news and technical
coverage on cybersecurity, hacking threads, and
infosec trends.
• URL of the site is: https://news.ycombinator.com/
• The site design is fairly simple. The landing page
shows a list of news headlines.
• Hacker News also offers an API providing structured,
JSON-formatted results
• Base URL: https://hacker-news.firebaseio.com/v0
• See explanation and documentation at:
https://github.com/HackerNews/API
• The new Python code serves as API client, without
relying on Beautiful Soup for HTML parsing
• Endpoint for top stories:
• Add ‘/top-stories.json?orderBy=“$key”’ to base URL
• Open API: No Developer Key required
To make the API requests more specific, use headers
and parameters in the request
• Headers
• Parameters are like filters to modify the scope of the
request.
• Check API documentation.
• Reddit Example
• With a user-agent header and the parameters packaged in
a dictionary that we will call payload
• Additional parameters are explained at the Reddit API
documentation: https://www.reddit.com/dev/api
API keys and tokens are ways of identifying applications
and users.
API key
• Identifies the application
API secret
• Acts as a password for the application
Token
• Identifies the user
Token secret
• Acts as a password for the user
News API is a simple HTTP REST API for searching
and retrieving live articles from various sources
• It has several endpoints
• /v2/top-headlines
• /v2/sources
• /v2/everything
• First step is to get your secret API key
• Go to: https://newsapi.org/docs/get-started

---
## [jonhunter/linux](https://github.com/jonhunter/linux)@[46b7a0e4c7...](https://github.com/jonhunter/linux/commit/46b7a0e4c73dcb1b58d2dcfbd83336d2b632a781)
#### Wednesday 2022-04-20 20:20:34 by Jon Hunter

mm: Check against orig_pte for finish_fault()

On Wed, Apr 13, 2022 at 04:03:28PM +0200, Marek Szyprowski wrote:
> Hi,

Hi, Marek,

>
> On 05.04.2022 03:48, Peter Xu wrote:
> > We used to check against none pte in finish_fault(), with the assumption
> > that the orig_pte is always none pte.
> >
> > This change prepares us to be able to call do_fault() on !none ptes.  For
> > example, we should allow that to happen for pte marker so that we can restore
> > information out of the pte markers.
> >
> > Let's change the "pte_none" check into detecting changes since we fetched
> > orig_pte.  One trivial thing to take care of here is, when pmd==NULL for
> > the pgtable we may not initialize orig_pte at all in handle_pte_fault().
> >
> > By default orig_pte will be all zeros however the problem is not all
> > architectures are using all-zeros for a none pte.  pte_clear() will be the
> > right thing to use here so that we'll always have a valid orig_pte value
> > for the whole handle_pte_fault() call.
> >
> > Signed-off-by: Peter Xu <peterx@redhat.com>
>
> This patch landed in today's linux next-202204213 as commit fa6009949163
> ("mm: check against orig_pte for finish_fault()"). Unfortunately it
> causes serious system instability on some ARM 32bit machines. I've
> observed it on all tested boards (various Samsung Exynos based,
> Raspberry Pi 3b and 4b, even QEMU's virt 32bit machine) when kernel was
> compiled from multi_v7_defconfig.

Thanks for the report.

>
> Here is a crash log from QEMU's ARM 32bit virt machine:
>
> 8<--- cut here ---
> Unable to handle kernel paging request at virtual address e093263c
> [e093263c] *pgd=42083811, *pte=00000000, *ppte=00000000
> Internal error: Oops: 807 [#1] SMP ARM
> Modules linked in:
> CPU: 1 PID: 37 Comm: kworker/u4:0 Not tainted
> 5.18.0-rc2-00176-gfa6009949163 #11684
> Hardware name: Generic DT based system
> PC is at cpu_ca15_set_pte_ext+0x4c/0x58
> LR is at handle_mm_fault+0x46c/0xbb0

I had a feeling that for some reason the pte_clear() isn't working right
there when it's applying to a kernel stack variable for arm32.  I'm totally
newbie to arm32, so what I'm reading is this:

https://people.kernel.org/linusw/arm32-page-tables

Especially:

https://dflund.se/~triad/images/classic-mmu-page-table.jpg

It does match with what I read from arm32's proc-v7-2level.S of it, where
from the comment above cpu_v7_set_pte_ext:

  * - ptep  - pointer to level 2 translation table entry
  *    (hardware version is stored at +2048 bytes)        <----------

So it seems to me that arm32 needs to store some metadata at offset 0x800
of any pte_t* pointer passed over to pte_clear(), then it must be a real
pgtable or it'll write to random places in the kernel, am I correct?

Does it mean that all pte_*() operations upon a kernel stack var will be
wrong?  I thought it could happen easily in the rest of mm too but I didn't
yet check much.  The fact shows that it's mostly possible the current code
just work well with arm32 and no such violation occured yet.

That does sound a bit tricky, IMHO.  But I don't have an immediate solution
to make it less tricky.. though I have a thought of workaround, by simply
not calling pte_clear() on the stack var.

Would you try the attached patch to replace this problematic patch? So we
need to revert commit fa6009949163 and apply the new one.  Please let me
know whether it'll solve the problem, so far I only compile tested it, but
I'll run some more test to make sure the uffd-wp scenarios will be working
right with the new version.

Thanks,

--
Peter Xu

>From c9eb74ef2414b542b20f934060a4b9123ba83d0f Mon Sep 17 00:00:00 2001
From: Peter Xu <peterx@redhat.com>
Date: Wed, 13 Apr 2022 12:31:01 -0400
Subject: [PATCH] mm: Check against orig_pte for finish_fault() when proper

This patch allows do_fault() to trigger on !pte_none() cases too.  This
prepares for the pte markers to be handled by do_fault() just like none
pte.

To achieve this, instead of unconditionally check against pte_none() in
finish_fault(), we may hit the case that the orig_pte was some pte marker
so what we want to do is to replace the pte marker with some valid pte
entry.  Then if orig_pte was set we'd want to check the current *pte (under
pgtable lock) against orig_pte rather than none pte.

Right now there's no solid way to safely reference orig_pte because when
pmd is not allocated handle_pte_fault() will not initialize orig_pte, so
it's not safe to reference it.

There's another solution proposed before this patch to do pte_clear() for
vmf->orig_pte for pmd==NULL case, however it turns out it'll break arm32
because arm32 could have assumption that pte_t* pointer will always reside
on a real ram32 pgtable, not any kernel stack variable.

To solve this, we add a new flag FAULT_FLAG_ORIG_PTE_VALID, and it'll be
set along with orig_pte when there is valid orig_pte, or it'll be cleared
when orig_pte was not initialized.

It'll be updated every time we call handle_pte_fault(), so e.g. if a page
fault retry happened it'll be properly updated along with orig_pte.

[1] https://lore.kernel.org/lkml/710c48c9-406d-e4c5-a394-10501b951316@samsung.com/

Signed-off-by: Peter Xu <peterx@redhat.com>

---
## [TalkingCactus/ARFS-6](https://github.com/TalkingCactus/ARFS-6)@[46b6bbaf74...](https://github.com/TalkingCactus/ARFS-6/commit/46b6bbaf74996c9d7ffc25125491e2293e136a1c)
#### Wednesday 2022-04-20 20:40:14 by VerySoft

Misc Tweaks

Fixes a space vine runtime

Makes it so space vines can't climb stairs (because that leads to practically unkillable stacks of vines that lag the server)

Makes it so space vines can't grow on open space (because you usually can't kill vines if they're way out in open space and that doesn't make much sense anyway.)

Attempts to limit the maximum range of plant bioluminescence (having hundreds or thousands of dynamic light sources with maximum possible light range seems to lag the server)

Adds a funny dog that no one should ever actually spawn but I will one day as a joke and everyone will cry. (its base form is actually not hostile so if you kill that one the hell you earn will all be on you)

---
## [fez6/og-names](https://github.com/fez6/og-names)@[2f6f4a9999...](https://github.com/fez6/og-names/commit/2f6f4a9999662973c2fe726e4e4373fc367e1259)
#### Wednesday 2022-04-20 21:53:55 by fez

Create abbreviations.txt

> 4AO - For adults only
> AFK - Away from keyboard
> AKA - Also known as
> ASAP - As soon as possible
> BAE - Before anyone else
> BFF - Best friend forever
> BRB - Be right back
> BTW - By the way
> BUMP - Bring up my post
> CTR - Click-through rate
> DIY - Do it yourself
> ETC - Et cetera
> FAQ - Frequently asked questions
> FYI - For your information
> G2G - Got to go
> HMU - Hit me up
> IDC - I don't care
> IDK - I don't know
> ILY - I love you
> IMO - In my opinion
> J4F - Just for fun
> KISS - Keep it simple stupid
> LMAO - Laughing my ass off
> LMFAO - Laughing my f***ing ass off
> LMK - Let me know
> MSG - Message
> NSFW - Not safe for work
> NVM - Nevermind
> OMW - On my way
> PPL - People
> POV - Point of view
> QNA - Questions and answeres
> ROFL - Rolling on floor laughing
> RUOK - Are you okay
> SOS - Save our ship
> SMS - Short message service
> STFU - Shut the f**k up
> TBH - To be honest
> TTYL - Talk to you later
> UUID - Universally unique identifier
> VIP - Very important person
> WTF - What the f**k
> XMAS - Christmas
> Y2K - The year 2000
> ZZZ - Sleeping noise

---
## [We-have-rights/docs](https://github.com/We-have-rights/docs)@[e30d388111...](https://github.com/We-have-rights/docs/commit/e30d3881112e0813202a1665cf40ec09a482b170)
#### Wednesday 2022-04-20 21:55:46 by We-have-rights

Update autolinked-references-and-urls.md

Trust this will be heard I have a inner beast that has been awoken and that gangster mentality has come across but today it will be for the good of things when I changed my life around and went back to southern California. I thought I was done with this city but my mom needed my help so I moved back and it only took one thing to  awake that beast  in me full force now because of a personal situation along with what I already know about the officers from when I did live that lifestyle I seen did heard alot of things and most of them were seeing officers integrity at zero level no morals or values about their job or family's  I mean you can even google it and see for yourself what the curupt officers chief ect says about their corruption not I'm sorry for my actions no way would they do that they make up some lame weak af excuse for their cowardly behavior again  I'm not john lang trust me when I say that I'm 2 steps ahead of all you guys just because of a department that is fully on my side even tho we have to strategize how were going to do this because yea it's going to get more crazy than people even know

---
## [Rohesie/tgstation](https://github.com/Rohesie/tgstation)@[0e904f7032...](https://github.com/Rohesie/tgstation/commit/0e904f70328a460af310014891eaadb5968ec31a)
#### Wednesday 2022-04-20 22:03:49 by LemonInTheDark

[MDB IGNORE] Moves non floor turfs off /floor. You can put lattices on lavaland edition (#65504)


About The Pull Request

Alternative to #65354

Ok so like, there was a lot of not floor types on /floor. They didn't actually want any of their parent type's functionality, except maybe reacting to breaking (which was easy to move down) and some other minor stuff.
Part of what we don't want them to have is "plateable" logic.
I should not be able to put floor tiles on the snow and be fine. It's dumb.

Instead, I've moved all non floor types down to a new type, called /misc.

It holds very little logic. Mostly allowing pipes and wires and preventing blob stuff.
It also supports lattice based construction, which is one of the major changes here. I think it makes more sense, and it fixes an assumption in shuttle code that assumed you couldn't place "a new tile" by just hitting some snow with a floor tile.
Oh and lattices don't smooth with asteroid tiles anymore, this looks nicer I think.

Moving on to commits, and minor changes

Changes clf3 to try and burn any turfs it's exposed to, instead of just floors
Moves break_tile down to the turf definition, alongside burn_tile
If you're in basic buildmode and click on anything that's not handled in a targeted way, you just build plating
FUNCTION CHANGE: you can't use cult pylons to convert misc tiles over anymore
Generalizes building floors on top of something into two helper procs on /turf/open, reducing copypasta
Adds a new turf flag, IS_SOLID, that describes if a turf is tangible or not.
Uses this alongside a carpet and open check to replace plating and floor checks in carpet code. This does mean that non iron tiles can be carpeted, but I think that's fine

Moves the /floor update_icon -> update_visuals call to /open
This change is horrificly old, dating back to 8e112f6 but that commit describes nothing about why it was done. Choosing to believe it was a newfriend mistake. Uncomfortable nuking it though, because of just how old it is. Moving down instead

Create a buildable "misc" type off open, moves /dirt onto it
Basically, we want a type we can use to make something support
construction, since that can be a messy bit of logic. Also enough
structure to set things up sanely.

I'm planning on moving most misc turfs onto it, if only because
constructing on a dirt tile with rods should be possible, and the same
applies to most things

Murders captain planet, disentangles /turf/open/floor/grass/snow/basalt

Adds a diggable component that applies the behavior of "digging"
something out from a turf.

Uses it to free the above pain typepath into something a bit more
sensible

The typepaths that aren't actually used by floor tiles are moved onto
/misc

The others are given names that better describe them, and kept in
fancy_floor

Oh and snowshoes don't work on basalt anymore, sorry

Snowed over platings now actually have broken/burned icon states, fixing black holes to nowhere

Misc turfs no longer smooth as floors, so lattices will ignore them

Placing a lattice will no longer scrape the tile it's on

Ok this is a really old one.
I believe this logic is a holdover from kor's baseturf pr
(97990c9)
It used to be that turfs didn't have a concept of "beneath" and instead
just decided what should be under them by induction. This logic of "if
it's being latticed scapeaway to space" made sense then, but has since
been somewhat distorted

We do want to scape away on lattice spawn sometimes, mostly when we're
being destroyed, but not always. We especially don't want to scape away
if someone is just placing a rod, that's dumb.

Adds a path updating script for this change

I've done my best to find all the errors this repathing will pull out, but I may have missed some. I'm sorry.
Why It's Good For The Game

Very old code made better, more consistent turfs for lavaland and icebox, better visuals, minor fix to snowed plating, demon banishment in lattice placement, fixes the icebox mining shuttle not being repairable
Changelog

cl
add: Rather then being tileable with just floor tiles, lavaland turfs, asteroid and snow (among other things) now support lattice -> floor tile construction
fix: Because of the above, you can now properly fix the icebox mining shuttle
refactor: Non floor turfs are no longer typed as floor. This may break things, please yell at me if it does
/cl

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[51acee2a18...](https://github.com/Paxilmaniac/Skyrat-tg/commit/51acee2a1841156e4d0ce9b2b9e9d3cd4fc9a7d8)
#### Wednesday 2022-04-20 22:21:04 by GoldenAlpharex

The MODsuit Digital Revolution: Replaces AIs in MODsuits with pAIs (#11135)

* Replaces AIs in MODsuits with pAIs

* Whoops forgot to remove that

* Lmao begone spellcheck shit

* I may be stupid

* Removing comments that commented code when they didn't really need to.

* Stupid linters

* Fixed the fact that mod wasn't a variable of the module anymore

---
## [rraykzu1/pokeemerald-expansion](https://github.com/rraykzu1/pokeemerald-expansion)@[a1cc08e213...](https://github.com/rraykzu1/pokeemerald-expansion/commit/a1cc08e213177956503a7ce93d385409720a19d4)
#### Wednesday 2022-04-20 23:23:51 by rraykzu1

added headlong rush

no animation even though i gave it one??????? this shit fucking sucks

---
## [alice1212123/Pearl-of-the-Orient](https://github.com/alice1212123/Pearl-of-the-Orient)@[acc28ad3cb...](https://github.com/alice1212123/Pearl-of-the-Orient/commit/acc28ad3cb44c84d02cf5e5e9b2cfe64e932fc2f)
#### Wednesday 2022-04-20 23:28:34 by Alice Lum

Why so sad? Walking around with them blue faces She said I'm down on my luck And it's something I gotta have Blue faces I hit the bank today and told them color me bad Blue faces Get that new money, and it's breaking me down honey Two tears in the bucket I cry with you But I could never lie with you I could never afford not to afford I could never put my plans to the side with you I could never see a red light Like a deer with a headlight I freeze up when I re-up See I barely have patience And you're relating Only the moment to complete us Why you hate to work for it? The reason I never went to work for it See a nine to five was so jive turkey But when Thanksgiving came that check didn't hurt me You plead the fifth I read the fifth amendment We both criminals with bad intentions They say time heals all But if I can shortcut My success, Corvettes by tomorrow Why so sad? Walking around with them blue faces She said I'm down on my luck And it's something I gotta have Blue faces I hit the bank today and told them color me bad Blue faces Get that new money, and it's breaking me down honey My home girl got a credit card scam She got a scholarship to college but she don't give a damn Intuition she got a broke bitch wishin' She tell me this on the phone with the noodles in the pan I know you, woman, I console you, woman You feel like the universe owes you, woman Oh the anticipation, of hoping you could make it Bitches don't prosper chasing education But you're talented, and can't handle it And your homegirls can't be your manager 365 times four, plus more If yan't get it right, tell me, do you got the stamina? But shit, ain't no money like fast money Even today I'm considered a crash dummy A rapper chasing stardom, how can I fast forward? My accolades better than all them Why so sad? Walking around with them blue faces She said I'm down on my luck And it's something I gotta have Blue faces I hit the bank today and told them color me bad Blue faces Get that new money, and it's breaking me down honey I wrote this song looking at a broke home baby You know the poverty stricken the little broke boy and babies Somebody yell "Kendrick American, they sho' is crazy" And I said "why?" Then he looked me in the eye, and said "nigga you fucked up" You're banking on good luck, you wishing for miracles You never been through shit, you're crying hysterical You settle for everything, complain about everything You say you sold crack, my world amphetamine Your projects ain't shit, I live in a hut bitch I'm living to keep warm, you living to pay rent I paid my way through, praying to Allah You played your way through, by living in sci-fi Bullshitting yourself, you talking to strangers Same thing goes for the ones you came with When y'all came on the boat looking for hope And all you can say is that you're looking for dope These days ain't no compromise And your pain ain't mines half the time A brand new excuse ain't shit to me Bitch I made my moves, with shackled feet Cape Town In today's day and age we practice the self pity of taking the easy way out You wait on them, him and her But when a blessing takes long, that's when you go wrong You selfish motherfucker Why so sad? Walking around with them blue faces She said I'm down on my luck And it's something I gotta have Blue faces I hit the bank today and told them color me bad Blue faces Get that new money, and it's breaking me down honey

---
## [powerbf/alphabet-soup](https://github.com/powerbf/alphabet-soup)@[af92d4a5d6...](https://github.com/powerbf/alphabet-soup/commit/af92d4a5d6ba2f841e8bfdf8639f77a784fcaeae)
#### Wednesday 2022-04-20 23:29:01 by Nicholas Feinberg

Make Hell Knights evil again (catern)

Lost this when they lost Pain.

Slightly hacky.

---
## [gutbuster12/bobgluttonstation](https://github.com/gutbuster12/bobgluttonstation)@[e2cebdcca0...](https://github.com/gutbuster12/bobgluttonstation/commit/e2cebdcca064772d2ee82a5eb9110cebcd45c81a)
#### Wednesday 2022-04-20 23:37:44 by Remis12

bob joga be like ahhh uhh hshut up remis go fuck yourself nigger

---

