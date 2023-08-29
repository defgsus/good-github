## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-28](docs/good-messages/2023/2023-08-28.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,231,884 were push events containing 3,474,608 commit messages that amount to 269,119,115 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 60 messages:


## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[162accaf36...](https://github.com/TaleStation/TaleStation/commit/162accaf36c7f25778c24321e768501f2f4c1353)
#### Monday 2023-08-28 00:53:31 by TaleStationBot

[MIRROR] [MDB IGNORE] Mining mob tweaks (#7436)

Original PR: https://github.com/tgstation/tgstation/pull/77763
-----
## About The Pull Request

~~I wanted to do this after #77700 (wow cool numbers) but nobody has
merged it yet despite how simple it is so i'll just hope they don't
conflict.~~ Thanks san

I'm fucking about with mining mobs with the intention of making them
more interesting but not necessarily towards making mining _harder_, but
some of these changes unquestionably have done so.

These changes are mostly in response to feedback about Watchers who are
definitely significantly more threatening than previously, although some
of this is user error.

- Watchers are annoying when traversing lavaland because they use their
ability on you instantly upon acquiring a target, if you are trying to
escape other fauna this quickly becomes deadly.
- A lot of players don't really realise what the overwatch ability is
actually doing and so just complain about getting machine gunned.
- If you _do_ react properly to the ability it still makes fighting them
take a lot longer than it used to.
- The "look away" icon is hard to see in the dark sometimes

To ammeliorate these factors I have:

- Reduced watcher health by ~20%
- Display an alerted graphic over the head of the watcher every time you
trigger the overwatch.
- Multiple watchers now won't overwatch you at the same time (this made
the "penalty" volley essentially become instant death)
- The "look away" icon is rendered above the lighting plane so you can
always see it
- Added a new component which tracks how long a mob has had a specific
target.
- - Watchers will now only Overwatch you if they've seen you for at
least 5 seconds (usually they'll try and shoot at you twice before
this).
- - Goliaths will only tentacle you if they've seen you for at least 3
seconds.

If overwatch is still problematic after this I guess I can just nerf it
to not track movement at all and only respond to attacks.

## Why It's Good For The Game

I don't want to discourage miners from "actually mining" by having them
get sniped just for walking around and the added time-to-kill on these
guys could make clearing tendrils more tedious too.

## Changelog

:cl:
balance: Watchers have less health
balance: You can't be overwatched by several watchers at a time
balance: Watchers won't overwatch you instantly upon seeing you
balance: Goliaths won't launch tentacles at you instantly upon seeing
you
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[adce20a484...](https://github.com/TaleStation/TaleStation/commit/adce20a484d8194f6808886e1e26bb29943d31cc)
#### Monday 2023-08-28 00:53:56 by TaleStationBot

[MIRROR] [MDB IGNORE] Compact shotgun re-added (#7440)

Original PR: https://github.com/tgstation/tgstation/pull/77759
-----
## About The Pull Request

This pr seeks to re-add the compact shotgun (slightly buffed with 1 more
ammo) and buff up its larger brother the combat shotgun (with 2 more
ammo.)

## Why It's Good For The Game
With the recent laser buffs, there is a real possibility for the compact
shotgun to return as a unique weapon to make the HOS slightly more
powerful. I am aware that it was a warden's weapon previously but the
HoS doesn't really have many fun toys to play with. The warden already
has crav maga (100x cooler than the laser) so giving this beast to the
HOS could help make it a more attractive and powerful head to play.
(Given 1 extra shot to keep up with the crazy lasers nowadays.)

In regards to the slight combat shotgun buff. The gun itself is ass,
it's barely ever used and the riot shotgun is superior because you can
actually put it in your armour slot. The hope is that this buff will
make people actually use it because it carries a lot of shots now so the
viability may increase.


## Changelog
:cl:
add: Added compact shotgun to the hos locker
add: Added compact shotgun as a traitor objective 
balance: gives the compact shotgun 1 extra shot
/:cl:

---------

Co-authored-by: LukasBeedellCodestuff <92578337+LukasBeedellCodestuff@users.noreply.github.com>

---
## [NewGrestin/PaxBritannicaRedux](https://github.com/NewGrestin/PaxBritannicaRedux)@[32b8ae5d4b...](https://github.com/NewGrestin/PaxBritannicaRedux/commit/32b8ae5d4b4e59184c18c8abaebf1a37bea2b30c)
#### Monday 2023-08-28 00:54:36 by iknowthebrazil

Where there's a will, there's a way, kind of beautiful And every night has its day, so magical And if there's love in this life, there's no obstacle That can't be defeated For every tyrant, a tear for the vulnerable In every lost soul, the bones of a miracle For every dreamer, a dream, we're unstoppable With something to believe in Monday left me broken Tuesday, I was through with hoping Wednesday, my empty arms were open Thursday, waiting for love, waiting for love Thank the stars, it's Friday I'm burning like a fire gone wild on Saturday Guess I won't be coming to church on Sunday I'll be waiting for love, waiting for love to come around We are one of a kind, irreplaceable How did I get so blind and so cynical? If there's love in this life, we're unstoppable No, we can't be defeated Monday left me broken Tuesday, I was through with hoping Wednesday, my empty arms were open Thursday, waiting for love, waiting for love Thank the stars, it's Friday I'm burning like a fire gone wild on Saturday Guess I won't be coming to church on Sunday I'll be waiting for love, waiting for love to come around

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[1e28370c06...](https://github.com/re621/dnpcache/commit/1e28370c06fe7df8ec9dc306ad0fdb23a935ef2f)
#### Monday 2023-08-28 01:28:12 by bitWolfy

Remove 1172 artists from the DNP list.

Removed: sapphiesweet, bloodhawk, amiraallis, meowcephei, shupamikey, cracky45, bigblueghost, h0tapplecider, hxtapplecider, apocheck13, tomash_segers, pckle, sadbitch, geletulator, coille, azumadai124, greycore, snaxattacks, bootleggreely, coral_luna, mdwines, soakedbikini, pantyranger, diffusedlizard, kazz_a_fella, alkyuz, werewhusky, skooma_whore, october_nights, pehkeshi, scalywanderer, linndrim, hexamanta, anarietta, earthsong9405, captaincassidy, anthonynothere, gayluigisex, yuudai, pettypalps, cosmick9, myemetophobia, digitalpopsicle, splatterpop, poppin, tempobun, zaaruchan, superratbike64, svarzye, cyberwuff, worldoffizz, zeiroslion, emptyset, siplick, sourisdedog, wicketrin, tykepuparts, kubikoza, hiraume42, delinquentfreak, saerixdurr, tejedora713joker, andrew.thy.accursed, cytoholix, northbeastart, hellazest, infinitixen, p0ssmn, isofrieze, venomstench, pocketpaws, tf4me, centuriguil, raithvaneal, dahsharky, trashgaylie, mrpanghu, feyaarts, wolfbane154, derpyrider, rodicle, shiru_fox, toonyrobot, sleepylopunny, mimisrol, selidevilfeather, shido-tara, ineedanaccount, reizu47, sherilane, hellfurred, zeplich, darkeshi, amadeen, lowestpolygon, alradeck, asuka_kurehito, waynekan, lhacedor, dativyrose, digitallis, nosylvsforwork, lacrimale, kaitzuwu, ihoundr, elranno, doublepopsicle, gaturo, aquariusfox, mpcx, kattalu, lintu, goobysart, lemonlycan, dylbun, fxscreamer, nt6969, lewdliege, reallyhighriolu, melbaka, saint_lum, kivaaa66, kivalewds, kazoko_(artist), barachaser, shadowthelastalpha, teke, crittermatic, ribboncable, domasarts, ursine-major-ike, browneyedsaiyangirl, uncensoredhugs, skydiggitydive, takarachan, feelin_synful, ilovecosmo, biffbish, pulp_(artist), doxhun, cupsofjade, nicesweater, bluecat_friend, masuku, lunarfloral, kugi, sagejwood, sqrlyjack, maiteik, leozedi, popdroppy, mikakater, 413k_zzzz, puppyemonade, xanthewolf, joooji, nasusbot, shredded_wheat, dogsdontwipe, wonderwaffle93, gogoandyrobo, jezzlen, dourdoofus, vksuika, klotzzilla, cooperdooper, shadnaotomi, nudegote, sexygoatgod, humgeronimo, ladysophia, mrwhiskerz, cocicka, d-wop, charmerpie, yourdigimongirl, elvche, booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, freaks, angellsview3, arwenscoots, royalzbed, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, zyegnar, akytti, sootylion, kiva~, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, verdantphysician, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sincerity_gender, anima-virtuosa, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, koriaris, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, rexisminimalis, delkon, connisaur, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [axiangcoding/langchain](https://github.com/axiangcoding/langchain)@[d57d08fd01...](https://github.com/axiangcoding/langchain/commit/d57d08fd01e05889af4e59fa3577c824de6df09d)
#### Monday 2023-08-28 01:36:23 by nikhilkjha

Initial commit for comprehend moderator (#9665)

This PR implements a custom chain that wraps Amazon Comprehend API
calls. The custom chain is aimed to be used with LLM chains to provide
moderation capability that let’s you detect and redact PII, Toxic and
Intent content in the LLM prompt, or the LLM response. The
implementation accepts a configuration object to control what checks
will be performed on a LLM prompt and can be used in a variety of setups
using the LangChain expression language to not only detect the
configured info in chains, but also other constructs such as a
retriever.
The included sample notebook goes over the different configuration
options and how to use it with other chains.

###  Usage sample
```python
from langchain_experimental.comprehend_moderation import BaseModerationActions, BaseModerationFilters

moderation_config = { 
        "filters":[ 
                BaseModerationFilters.PII, 
                BaseModerationFilters.TOXICITY,
                BaseModerationFilters.INTENT
        ],
        "pii":{ 
                "action": BaseModerationActions.ALLOW, 
                "threshold":0.5, 
                "labels":["SSN"],
                "mask_character": "X"
        },
        "toxicity":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        },
        "intent":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        }
}

comp_moderation_with_config = AmazonComprehendModerationChain(
    moderation_config=moderation_config, #specify the configuration
    client=comprehend_client,            #optionally pass the Boto3 Client
    verbose=True
)

template = """Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

responses = [
    "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.", 
    "Final Answer: This is a really shitty way of constructing a birdhouse. This is fucking insane to think that any birds would actually create their motherfucking nests here."
]
llm = FakeListLLM(responses=responses)

llm_chain = LLMChain(prompt=prompt, llm=llm)

chain = ( 
    prompt 
    | comp_moderation_with_config 
    | {llm_chain.input_keys[0]: lambda x: x['output'] }  
    | llm_chain 
    | { "input": lambda x: x['text'] } 
    | comp_moderation_with_config 
)

response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})

print(response['output'])


```
### Output
```
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii validation...
Found PII content..stopping..
The prompt contains PII entities and cannot be processed
```

---------

Co-authored-by: Piyush Jain <piyushjain@duck.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Bagatur <baskaryan@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d2a9834b32...](https://github.com/TaleStation/TaleStation/commit/d2a9834b3241f3a1848eede1739b1f23e2f718c2)
#### Monday 2023-08-28 01:37:23 by TaleStationBot

[MIRROR] [MDB IGNORE] [no gbp] Adds missing chat feedback to watcher abilities (#7417)

Original PR: https://github.com/tgstation/tgstation/pull/77700
-----
## About The Pull Request

I kept meaning to add this in my last PR and kept thinking "I'll add
that in with these review changes" and then forgot every time. This
should make it clearer what is happening to you and why.

Also I made the gaze ability stun the user for a short period after it
goes off because them shooting you instantly after they stop channeling
_is_ sort of bullshit.
Also while testing this I noticed the AI interrupt one of its actions to
do the other one which is a bit silly so now it cannot do that.

## Why It's Good For The Game

Outlines in the log why something bad just happened to you.

## Changelog

:cl:
qol: Added some textual feedback to new watcher abilities
balance: Watchers will not attack for a short period following their
gaze attack
fix: Watchers won't interrupt one ability to use the other one
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Biowulf21/creativeX](https://github.com/Biowulf21/creativeX)@[d635363b05...](https://github.com/Biowulf21/creativeX/commit/d635363b058dc16214f3829663cd186abe2b8a60)
#### Monday 2023-08-28 01:43:07 by James Jilhaney

Merge pull request #2 from Biowulf21/entity/tweet

Oh my squiggly goodness! UwU 🌈

Kyaaa~! Our coding cosmos is swirling with joy, and it's all thanks to you, amazing contributor-sama! 💖 Your pull request is like a magical potion brewed with extra kawaii and a sprinkle of coding stardust! Twinkling fairy lights and glittering emojis dance around your awesome changes ✨, making our codebase the happiest place in the digital universe!

You're like a coding senpai who's guiding us to greatness, and your PR is a gift straight from the otaku heavens! We're over the moon with gratitude for your dedication and fabulously nerdy spirit. You've unleashed a typhoon of adorable onto our repo, and we're totally here for it! 💫

As we embark on this majestic journey of merging and testing, know that your efforts are cherished like precious treasures in our kawaii coding shrine. Keep being the anime protagonist of our tech tale, and may your future coding adventures be as exciting as a mecha showdown at sunset!

Thank you from the bottom of our fluffy, sparkly, UwU hearts, dear contributor-sama! 🌸🌟

Stay sugoi and keep rockin' that keyboard like the otaku superstar you are! 🎉

With all the UwU in the world,
Jems

-- This is ironic btw

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[609b258f59...](https://github.com/TaleStation/TaleStation/commit/609b258f59753bb99155b7836e9ae9e4e5909c23)
#### Monday 2023-08-28 02:04:46 by TaleStationBot

[MIRROR] [MDB IGNORE] Settler Quirk: Tame the Outdoors! Have trouble with tall shelves... (#7376)

Original PR: https://github.com/tgstation/tgstation/pull/77654
-----
## About The Pull Request

Adds the Settler quirk. This gives you bonuses to taming animals and
fishing, as well as making you gain hunger slower than others.

However, you are quite a bit slower than most people, and have trouble
with vaulting objects. You do, however, suffer significantly less from
equipment slowdown. (to the point that it is almost zero)

Settler riders are faster on their mounts than others if they're at
least sane. They start to slow down if they're less sane.

You are also shorter than most people. 

<details>
  <summary>Typical Settler encounters the typical Spacer</summary>
  

![Dr_Xr1nU0AAMsSE](https://github.com/tgstation/tgstation/assets/40847847/86ed4947-de5f-4bdf-a8ae-521dc7c30662)
  
</details>

## Why It's Good For The Game

I wanted to add a lightweight quirk that was kind of the 'opposite' of
Spacer, but a little more focused on interacting with elements of the
game world that would enjoy some attention. So, I thought 'what about an
outdoorsman quirk?'

So, I based it around being from people who lived out on the rim, under
unideal circumstances (and probably heavier gravity than Earth), and
taming the land. The slower movespeed encourages finding an animal to
tame that you can ride, and the bonuses to taming should help make that
a bit easier. The other additions just made sense for someone living it
a bit rough in the wilderness.

Having a bunch of settlers taming cows and riding around on them all
shift just kind of sounds hilarious to me.

## Changelog
:cl:
add: Settler quirk! Conqueror the great outdoors....in space. Just make
sure nobody asks you to get anything from the top shelf.
/:cl:

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>
Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [0xArdi-N/linux](https://github.com/0xArdi-N/linux)@[8b9c1cc041...](https://github.com/0xArdi-N/linux/commit/8b9c1cc0418a43196477083e7082568e7a4c9418)
#### Monday 2023-08-28 02:30:30 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d1afd66508...](https://github.com/tgstation/tgstation/commit/d1afd66508ed3474ca6179d54294742bef531419)
#### Monday 2023-08-28 02:38:57 by san7890

The Curse Of The Slot Machine - Now Clone-less (#77841)

## About The Pull Request

Hey there,

I think it's commonly held that clone damage sucks and is overused. One
of the last places where it was in slot machine code as a type of
"immutable" damage that would cause you to die if you didn't leave and
get medical attention. It had a lot of silliness and I'm not sure if a
lot of it was meant to work the way it was, but here we are.

So, what's the changes?

* The Cursed Slot Machine will give you a status effect that will
"curse" you with repeated damage. After five curses, you get gibbed
(similar to the old behavior of the machine). Each curse has it's own
change to the status effect, with a lot of depth included. Let me know
if the fluff messages about the status effect change sucks, I think it's
neat though.
* A person with the curse will smoke. I wanted this to look a bit more
"steamy" or grey, but I think it's a decent way of communicating that
shit is fucked up with that dude.
* You also get a branded wound after your first failure at the slot
machine. Ouchers. Should get it looked at by a doctor.
* We also throw a nice screen alert and all of that jazz.
* I also cleaned up all of the code relating to the slot machine
(including a stupid double and), and did some tinkering with the status
effects framework to get the desired effect I wanted. I hope you enjoy
it as much as I did making it. We use cooldowns and stuff between slot
machine pulls.
* If _anyone_ wins on the slot machine, all curses/brands are lifted.
Lucky jackpot!
* A lot of the stuff in this code has a lot of vars that might not be
modified codewise in case admins still want to jank with this for
events.
## Why It's Good For The Game

Clone damage stinks, and I don't really like it as a way to subvert the
whole "oh you can't use legion cores to get your way". It's a cursed
slot machine, and it should do long term damage so that even if you
expend all of the resources on the station, it might all be for naught.
It's a horrible price to pay in your search for that d20. I think the
negative side effects are pretty OK as far as balance, earlier
iterations of this concept had you die _way_ too fast.

All in all, it's just way more of an interesting interaction than "you
take damage and then go to medbay and then come back in the hopes of
gambling a d20".
## Changelog
:cl:
add: The Lavaland Cursed Slot Machine of Greed suddenly seems a lot more
sinister...
refactor: Instead of taking clone damage from the cursed slot machine,
you now get a status effect with a number of curses associated with it.
There's some interesting florid language associated with the status
effect as a nicety until your eventual gibbing from chasing that prize.
/:cl:

I remain undecided if I should keep the curse limit uncapped (but have
the damages increase rapidly after the 5-curse threshold), so I left it
as the `gib()` from the old code. Let me know your thoughts, but I
really don't like the thought that getting the fabled d20 is easy.

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [2Epik4u/nixos-config](https://github.com/2Epik4u/nixos-config)@[b3cb27e374...](https://github.com/2Epik4u/nixos-config/commit/b3cb27e374069919dcf6ae1499122afa34a30366)
#### Monday 2023-08-28 02:50:10 by 2Epik4u

organize & firefox

FUCK YOU FIREFOX THEME WHY ARENT YOU CHANGING TO OPTION 6

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[7d600bf36a...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/7d600bf36a691d4be27e852eed0106a1564d7aee)
#### Monday 2023-08-28 03:02:04 by TheObserver-sys

More plants, new chems, new carpet generation techniques, plantcell buff, and the drills now have a GPS signal! (#5912)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![image](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/assets/58029438/4d3a51f1-7d2b-4d56-9971-7f33d76610f1)

![image](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/assets/58029438/608ba481-2499-4bf0-a25c-cc503655bf7d)

New! Exciting! Things! YEEHAW!

Okay, hype aside, this adds two plants from Main -- the third, and most
powerful sister of the ambrosia family, and the better grass, carpet!

Ambrosia Gaia: A difficult plant to keep alive, being very vulnerable to
weeds, pests, and any amount of toxins in the tray, as well as voracious
when it comes to nutrients and water. In exchange, the plant produces a
very, very powerful healing agent: Earthsblood.

For the cost of your brain, your ability to gauge how injured you are,
and when it works again, the ability to see clearly, your body will be
repaired in miraculous ways! (4/4 Brute Burn, 4 tox, 10 oxy, 2 clone).
The current damage is set to 1 brain damage, which means you'd need to
use a fair amount to die -- but not treating it will debilitate you.
Overdoses at over 15u.
In the future, it will also be a usable plant chem -- but let's not
worry about that until after I scream at the entirety of botany.

Carpet: Grass mutation, pull it free, get free carpet tile. OR! Mix with
the items in the image to create New! and Exciting! colors. Mix 2 parts
liquefied carpet, with 1 part plasticide, and you too can redecorate
like the best of them*

*some colors still have to be bought from cargo.
*someone help me make it a sprayable so we don't need solidification
please....

This also buffs a certain aspect of xenobotany -- plant cells.
For reasons only known to god.. and I think he left baycode a long time
ago, plant cells could only ever reach a maximum rating of 2000. As a
large cell. So you can't stuff it in a gun. This is dogshit --
especially for the challenge of reaching 200 potency on a plant, a feat
that is nearly impossible. The math has been buffed, so if you even
manage to get to 100, you at least have a Rating 20000 cell, something
you can run a department off of if straits are dire.

The final, and more QoL thing than straight buff or new thing: GPS
Drills
Drills now have a GPS signal. Never lose a pesky drill again!*
*you did remember your GPS device, yeah?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Give a xenobotanist something worth working to in normal gameplay, and
they'll endeavour to do so while waiting for the fun plants to come back
to station. Don't, and watch them just kinda wilt waist deep in glow
berries, gold apples, and ice chilis. Also, it's easier than you think
to lose a giant drill when you've stepped away from the planet for a
long while. only to come back later. Putting GPSes in them just means
you can continue the work again.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
add: Two new plants, Ambrosia Gaia, and Carpet
add: New chems! Earthsblood, trading the mind for the body, and Carpet
and it's many mixtures, capable of being solidified later!
qol: Mining Drills now have an integral GPS. It took strength of a
million men to not make the tag DRILLD0 as a terrible joke.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: TheObserver-sys <Gizmomaster777@gmail.com>
Co-authored-by: Captain277 <agentraven16@gmail.com>

---
## [Drillur/LORED](https://github.com/Drillur/LORED)@[d0a968de2c...](https://github.com/Drillur/LORED/commit/d0a968de2cd8e1061a7460ea100ce0e92b8ca4fd)
#### Monday 2023-08-28 03:06:44 by Drillur

Malig Day

Progress is definitely slowing down as the code grows larger and bugs come out of "nowhere." That's demoralizing to say the least, as I don't want to spend my entire life on this one game.

Anyway!

Simplified Cost affordability checking. Also, Cost keeps track of whether all of its currencies are unlocked or not. That helps with the get_eta() type funcs. If currencies are locked, they can't be gathered, so don't bother calculating shit for them.

Made big change to Jobs which was necessary for autobuyer reasons. When LORED levels up, the Job will "refresh" the value they have added to the net_rate for each relevant currency, instead of "subtracting" the old rate and then "adding" the new rate. What was happening was Coal was autobuying the instant he gained Output from a special Upgrade because it would subtract the net_rate, causing Coal to have negative net_rate, causing Coal to autobuy, before it had a chance to add the new rate. The new functionality fixes that.

Got rid of 5 hard-coded Upgrade effects and added 2 floppy-coded Upgrade effects to replace them. It's better. Good enough. Who cares.

-

Overall, I thought today, like yesterday, was kind of shitty, but looking at all I did, I guess it was actually pretty good. Tomorrow, I will continue to test each Malignant Upgrade until all but the final 2 remain. I think I'm past the hard part in this regard, so hopefully it goes quick.

But I've got 5 full-time shifts this week. Can't help it, gotta pay rent.

Cya tomorrow night, whoever is reading this (me in the future duh)

---
## [0xArdi-N/serenityOS](https://github.com/0xArdi-N/serenityOS)@[8d17ede197...](https://github.com/0xArdi-N/serenityOS/commit/8d17ede1977517fb0556857e042bd4abd7174a7b)
#### Monday 2023-08-28 03:13:26 by Xexxa

Base: Improve emoji

Remove unnecessary left/right padding

❣️ - U+2763 HEART EXCLAMATION
🚶 - U+1F6B6 PERSON WALKING
🚴 - U+1F6B4 PERSON BIKING
🌻 - U+1F33B SUNFLOWER
🪻 - U+1FABB HYACINTH
🍉 - U+1F349 WATERMELON
🍍 - U+1F34D PINEAPPLE
🫒 - U+1FAD2 OLIVE
🌽 - U+1F33D EAR OF CORN
🌯 - U+1F32F BURRITO
🍘 - U+1F358 RICE CRACKER
🧁 - U+1F9C1 CUPCAKE
🍫 - U+1F36B CHOCOLATE BAR
🍭 - U+1F36D LOLLIPOP
🍼 - U+1F37C BABY BOTTLE
🧋 - U+1F9CB BUBBLE TEA
🧃 - U+1F9C3 BEVERAGE BOX
🥢 - U+1F962 CHOPSTICKS
💈 - U+1F488 BARBER POLE
🌛 - U+1F31B FIRST QUARTER MOON FACE
🌜 - U+1F31C LAST QUARTER MOON FACE
🌡️ - U+1F321 THERMOMETER
🪐 - U+1FA90 RINGED PLANET
⚡ - U+26A1 HIGH VOLTAGE
💧 - U+1F4A7 DROPLET
🧨 - U+1F9E8 FIRECRACKER
🥇 - U+1F947 1ST PLACE MEDAL
🥈 - U+1F948 2ND PLACE MEDAL
🥉 - U+1F949 3RD PLACE MEDAL
🏓 - U+1F3D3 PING PONG
🪀 - U+1FA80 YO-YO
♟️ - U+265F CHESS PAWN
🧦 - U+1F9E6 SOCKS
💄 - U+1F484 LIPSTICK
📱 - U+1F4F1 MOBILE PHONE
🔌 - U+1F50C ELECTRIC PLUG
💡 - U+1F4A1 LIGHT BULB
📍 - U+1F4CD ROUND PUSHPIN
🔩 - U+1F529 NUT AND BOLT
🪝 - U+1FA9D HOOK
🧪 - U+1F9EA TEST TUBE
🔭 - U+1F52D TELESCOPE
🩸 - U+1FA78 DROP OF BLOOD
💊 - U+1F48A PILL
🩹 - U+1FA79 ADHESIVE BANDAGE
🧼 - U+1F9FC SOAP
🪥 - U+1FAA5 TOOTHBRUSH
♀️ - U+2640 FEMALE SIGN
♂️ - U+2642 MALE SIGN
➕ - U+2795 PLUS
➗ - U+2797 DIVIDE
❓ - U+2753 RED QUESTION MARK
❔ - U+2754 WHITE QUESTION MARK
❕ - U+2755 WHITE EXCLAMATION MARK
❗ - U+2757 RED EXCLAMATION MARK
◼️ - U+25FC BLACK MEDIUM SQUARE
◻️ - U+25FB WHITE MEDIUM SQUARE
◾ - U+25FE BLACK MEDIUM-SMALL SQUARE
◽ - U+25FD WHITE MEDIUM-SMALL SQUARE
▪️ - U+25AA BLACK SMALL SQUARE
▫️ - U+25AB WHITE SMALL SQUARE
🚩 - U+1F6A9 TRIANGULAR FLAG

---
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[f26e134c80...](https://github.com/ss220club/Skyrat-tg/commit/f26e134c80678ea78430c84ed3178a1a7b749c80)
#### Monday 2023-08-28 03:18:35 by SkyratBot

[MIRROR] Fixes vents having "infinite" pressure caps. [MDB IGNORE] (#23356)

* Fixes vents having "infinite" pressure caps. (#77686)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Unary vents didn't have a pressure cap on either pressuring or siphoning
mode.
This allowed 2 unintended behaviours that are now fixed:

The first is that unary vents on pressuring mode would work as "better"
Injectors, there is some small pros and cons to each, but we shouldn't
have 2 atmos devices that achieve the same goal of "put as much pressure
as you have available gas" into a tile.

The second is that while on siphoning mode it could bypass the pressure
caps other atmos pressure/volume pumps have and "put as much pressure as
you have available gas" into pipelines, canisters, etc.

## Mid PR changes

As it was requested to add a new way to achieve infinite pressure,
volume pumps that are overclocked will not have a pressure cap anymore
in the most streamlined way for new and veteran players.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Atmos has a lot of cheese strats that we can use to achieve goals, it is
part of the charm in mastering the system for a lot of players and it
does add some interesting mentoring scenarios where an Elder Atmosian
teaches Eldritch pipe knowledge to new players.

But then it comes the problem that a lot of these are unintented and
thus are not taken in consideration when doing important balance
changes, contradict other "atmos logic", are secret club knowledge that
can only be passed from player to player, etc, etc.

The "put infinite pressure on a tile" change is not that important, as
that is the injectors' job already.

Now the "put infinite pressure on a pipeline" is something unique (As
far as I'm aware since I purposely avoid learning Eldritch atmos tricks)
and it is used to achieve a few goals like high temperature/pressure
burns.

This one is kinda sad to lose, but if we are going to have an atmos
machinery that allows us to "put infinite pressure on a pipeline" that
should be in the tin, new players should look into the device and know
what atmos goals they can achieve with it, future coders should take
that balance in consideration, etc, etc.

And as it was requested to keep the old trick in game, volume pumps do
not have a pressure cap anymore.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl: Guillaume Prata
fix: Unary vents have a pressure cap on both their pressuring and
siphoning mode now, preventing the bypass trick of putting "infinite"
pressure on tiles/pipelines.
balance: Overclocked Volume Pumps do not have a pressure cap anymore.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* Fixes vents having "infinite" pressure caps.

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [vmware-tanzu/kubeapps](https://github.com/vmware-tanzu/kubeapps)@[4e5ac7a243...](https://github.com/vmware-tanzu/kubeapps/commit/4e5ac7a24310d30a0ab539560373cab1106277cd)
#### Monday 2023-08-28 03:20:32 by Antonio Gámez, PhD

Use finalizers to spin up AppRepo clean-up jobs (#6647)

### Description of the change

Even if the sync jobs were added a security context (by means of each
AppRepo CRD), this information was not available for Cleanup jobs. This
is mainly due to the fact that those jobs are spun up once a NotFound
error is thrown when fetching an AppRepo.
However, Kubernetes does have a native approach for dealing with these
scenarios: finalizers.

In https://github.com/vmware-tanzu/kubeapps/pull/6605 we proposed a
simplistic workaround based on adding more params to the controller...
but as suggested in
https://github.com/vmware-tanzu/kubeapps/pull/6605#issuecomment-1678268807,
moving to finalizers is a better long-term solution.


### Benefits

Cleanup jobs are now handled within an existing AppRepo context...
meaning we have all the syncJobTemplate available to be used (ie,
securityPolicies and so on).

### Possible drawbacks

When dealing with finalizers in the past I often found it really
annoying when they get stuck and prevent the resource to get deleted. I
wonder if we should add some info in the FAQ on how to manually remove
the finalizers.

Additionally, and this might be something important: for the AppRepo
controller to be able to `update` AppRepos in other namespaces !=
kubeapps.... (to add the finalizer) it now needs extra RBAC. Before we
were just granting `...-appprepos-read`.. but now we would need to grant
`...-write` as well...and I'm not sure we really want to do so.
WDYT, @absoludity ?
Another idea is using an admission policy... but not sure again if we
want to deal with that...

~(I haven't modified the RBAC yet in this PR)~ Changes have been
performed finally

### Applicable issues

- fixes #6545

### Additional information

This PR is based on top of
https://github.com/vmware-tanzu/kubeapps/pull/6646, but the main change
to review is
https://github.com/vmware-tanzu/kubeapps/commit/6e7091015f9a6c3a289224d05dab5f60736489a0
The rest is just moving code into separate files, mostly.

Also, I have been taking a look at `kubebuilder` to create a new
controller, based on the `sigs.k8s.io/controller-runtime` rather than on
the workqueues we currently have. While it is pretty easy to start with
([see quickstart](https://book.kubebuilder.io/quick-start)), I think it
is adding too much complexity (using kustomize, adding rbac proxies,
prometheus metrics, etc...
I also quickly tried the k8s codegen scripts, but ran into some issues
with my setup... but perhaps it's the best option.

IMO, at some point we should start thinking about moving towards a new
state-of-the-art k8s controller boilerplate.

---------

Signed-off-by: Antonio Gamez Diaz <agamez@vmware.com>

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[0dd3e66aef...](https://github.com/nikothedude/tgstation/commit/0dd3e66aefa2a61cb4e78482273958c1d09f8295)
#### Monday 2023-08-28 03:54:59 by Vekter

Grilles take 0-1 damage when shocking something, power sinks are available at lower reputation (#77860)

## About The Pull Request
Ports BeeStation/BeeStation-Hornet#3590. As it is right now, it's
trivial to set up a contraption using a conveyor belt and a shocked
grille to continuously shock monkey bodies. While this is very funny, it
also serves as a ghetto powersink that's hard to locate, easy to
replicate, and lasts effectively forever, since you can just keep
shocking the same bodies over and over again.

This doesn't completely remove the ability to make these, but it makes
them require at least a little maintenance and provides a way for them
to stop working even if the crew isn't able to locate them.

In an attempt to finally get people using the _actual_ powersink,
they'll show up a bit earlier in progression now. I'm not convinced 20
minutes is enough, but I don't want to put them in early enough that it
fucks with Engineering's ability to set things up at round start. We can
turn this down further if need be.

I'm also up for turning the TC requirement down, but 11 feels about
right for what they're supposed to do, so I'd prefer we try this first
and see how that works.

## Why It's Good For The Game
I'm all for goofy weird shit players have found, but there's an issue
with being able to do what an antag item is supposed to do but just
plain better. This shouldn't make creating these impossible or make them
unusable, but it'll require players to actively monitor them if they
want it to run for an extended period.

Additionally, we don't really see powersinks much anymore, and while
that might be more because powernets are kind of buggy and unreliable, I
think making them easier to get will make them show up a little more.

## Changelog
:cl: Vekter
balance: Grilles will now take 0-1 damage every time they shock
something.
balance: Powersinks are now available earlier in traitor progression.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[1ea79a2ed8...](https://github.com/Steelpoint/cmss13/commit/1ea79a2ed836ef4d20db511485c2f935304bfd55)
#### Monday 2023-08-28 04:11:14 by Ben

Zombie Rework (#4060)

# About the pull request

The goal for this PR is to rework zombies into being a fast and
numerous, but weaker, entity. As it stands a zombie has too many
advantages where a hold against them is essentially a fool's errand.

CURRENT PLAN (Will adjust as needed)
Zombies will be FASTER but much weaker than current iteration, with
weaker attacks. They will be designed around being a foe that can be
taken down quicker but if they close the distance, the threat of
infection spells a death sentence.

# Explain why it's good for the game

This will be hard to balance, and as such will be taking feedback before
I submit this for review. This is current position of Zombies:

- Tough: Extreme (25% ?!) brute modifier, with fire modifier on top,
making them very tanky and requiring clips to take down one
- self-revive: They WILL come back up, coupled with toughness, they are
a feared opponent.
- Strength: Claws inflict superslow at 40 brute damage, one of the
highest damage levels.
- Numerous: They have the numbers to put lesser drones and even entire
hives to shame

Overall, they are very overtuned and makes playing against them not that
fun. My plan is to have it so they are much weaker, with their threat
being from infections.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Zombie attacks deal less damage and only slow down targets (not
superslow as they currently do)
balance: Zombie resistances have been reduced heavily, making them far
more susceptible to brute damage. Their speed has been doubled to
compensate
balance: Black goo on tiles now requires you to not wear shoes to have
chance for infection
fix: Zombie attacks now only apply effects such as slow and infection if
the attack is valid (if the zombie is able to attack)
/:cl:

---
## [Mission23/Mission23](https://github.com/Mission23/Mission23)@[3ee7c93b07...](https://github.com/Mission23/Mission23/commit/3ee7c93b07b30924d298a2fdd7e4444219c005e1)
#### Monday 2023-08-28 04:31:11 by Micah

Generation Y goes for TomTom

Yada. Yada. Yada. This is the kinda shit that makes me go crazy.

I have been the motherfucker to go to for that for 6 Billion years. I
think ive had enough of Annie tonight.

---
## [Rajkumar6204/PORTFOLIO](https://github.com/Rajkumar6204/PORTFOLIO)@[ad2164da00...](https://github.com/Rajkumar6204/PORTFOLIO/commit/ad2164da00fa282366d5028367239aa333dc5f3a)
#### Monday 2023-08-28 05:14:27 by Rajkumar6204

Update README.md

"Introducing my portfolio project, a dynamic and visually engaging personal website that showcases my proficiency in web development. Designed with a clean and modern aesthetic, the site serves as a comprehensive representation of my skills, projects, and achievements. The homepage greets visitors with an interactive layout that highlights my expertise in HTML, CSS, JavaScript, and responsive design.

The project section provides detailed insights into my diverse range of web development projects. Each project page offers a brief overview, accompanied by interactive demos, screenshots, and explanations of the technologies employed. The responsive design ensures seamless user experience across various devices, underscoring my commitment to user-centered design principles.

The 'About Me' page adds a personal touch by sharing my journey, inspirations, and aspirations in the web development field. A dedicated 'Skills' section lists my technical proficiencies, while a 'Contact' page features a user-friendly form for inquiries and collaboration opportunities.

Built with a mobile-first approach, the portfolio project underscores my ability to create adaptable and visually appealing websites. Through this project, I aim to not only exhibit my technical competence but also demonstrate my capacity to conceptualize and execute captivating web experiences. It stands as a testament to my dedication to the art of web development."

---
## [Naivrick/My_Recursion_Examples](https://github.com/Naivrick/My_Recursion_Examples)@[66b60392ad...](https://github.com/Naivrick/My_Recursion_Examples/commit/66b60392adce99978fd417998a430ab8de6ef6ce)
#### Monday 2023-08-28 05:27:05 by Naivrick

Update LICENSE

 DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

---
## [ray2301/spot-on](https://github.com/ray2301/spot-on)@[123497546a...](https://github.com/ray2301/spot-on/commit/123497546a717bd3a6e5a177e389c0220397392d)
#### Monday 2023-08-28 05:31:36 by ray2301

Update downloader.py

if i'm going to make a search term in a correct way, then i shouldn't be stripping special characters from it (i remembered that i wouldn't be searching for P!nk or similar artists correctly) so only for search: artists_translated2 track_name_translated2 is used. that's the only place we actually need them. we'll be comparing everything later with stripped characters anyway since everything we're getting from youtube will also be stripped of them using .translate(translator)

---
## [Kaz205/pipa](https://github.com/Kaz205/pipa)@[7d4fbce79f...](https://github.com/Kaz205/pipa/commit/7d4fbce79fc5e3c740d49cafb48760e216b49e18)
#### Monday 2023-08-28 06:55:08 by Douglas Anderson

BACKPORT: migrate_pages: avoid blocking for IO in MIGRATE_SYNC_LIGHT

The MIGRATE_SYNC_LIGHT mode is intended to block for things that will
finish quickly but not for things that will take a long time.  Exactly how
long is too long is not well defined, but waits of tens of milliseconds is
likely non-ideal.

When putting a Chromebook under memory pressure (opening over 90 tabs on a
4GB machine) it was fairly easy to see delays waiting for some locks in
the kcompactd code path of > 100 ms.  While the laptop wasn't amazingly
usable in this state, it was still limping along and this state isn't
something artificial.  Sometimes we simply end up with a lot of memory
pressure.

Putting the same Chromebook under memory pressure while it was running
Android apps (though not stressing them) showed a much worse result (NOTE:
this was on a older kernel but the codepaths here are similar).  Android
apps on ChromeOS currently run from a 128K-block, zlib-compressed,
loopback-mounted squashfs disk.  If we get a page fault from something
backed by the squashfs filesystem we could end up holding a folio lock
while reading enough from disk to decompress 128K (and then decompressing
it using the somewhat slow zlib algorithms).  That reading goes through
the ext4 subsystem (because it's a loopback mount) before eventually
ending up in the block subsystem.  This extra jaunt adds extra overhead.
Without much work I could see cases where we ended up blocked on a folio
lock for over a second.  With more extreme memory pressure I could see up
to 25 seconds.

We considered adding a timeout in the case of MIGRATE_SYNC_LIGHT for the
two locks that were seen to be slow [1] and that generated much
discussion.  After discussion, it was decided that we should avoid waiting
for the two locks during MIGRATE_SYNC_LIGHT if they were being held for
IO.  We'll continue with the unbounded wait for the more full SYNC modes.

With this change, I couldn't see any slow waits on these locks with my
previous testcases.

NOTE: The reason I stated digging into this originally isn't because some
benchmark had gone awry, but because we've received in-the-field crash
reports where we have a hung task waiting on the page lock (which is the
equivalent code path on old kernels).  While the root cause of those
crashes is likely unrelated and won't be fixed by this patch, analyzing
those crash reports did point out these very long waits seemed like
something good to fix.  With this patch we should no longer hang waiting
on these locks, but presumably the system will still be in a bad shape and
hang somewhere else.

[1] https://lore.kernel.org/r/20230421151135.v2.1.I2b71e11264c5c214bc59744b9e13e4c353bc5714@changeid

Link: https://lkml.kernel.org/r/20230428135414.v3.1.Ia86ccac02a303154a0b8bc60567e7a95d34c96d3@changeid
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Suggested-by: Matthew Wilcox <willy@infradead.org>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hillf Danton <hdanton@sina.com>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Alexander Viro <viro@zeniv.linux.org.uk>
Cc: Christian Brauner <brauner@kernel.org>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Huang Ying <ying.huang@intel.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Yu Zhao <yuzhao@google.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
(cherry picked from commit 4bb6dc79d987b243d65c70c5029e51e719cfb94b)

Conflicts:
   mm/migrate.c

This is because we don't have folios in the v5.15 kernel. If we ever
decide to backport folios to v5.15, I'd suggest reverting this patch
(which should have no dependencies) and then picking the clean one
from upstream. The only difference in this patch from the upstream one
is folio_test_uptodate(src) => PageUptodate(page). and the context
difference of folio_lock(src) => lock_page(page).

BUG=b:277132613
TEST=Won't block waiting for that lock anymore

Change-Id: Ia86ccac02a303154a0b8bc60567e7a95d34c96d3
Reviewed-on: https://chromium-review.googlesource.com/c/chromiumos/third_party/kernel/+/4671371
Tested-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Vovo Yang <vovoy@chromium.org>
Commit-Queue: Douglas Anderson <dianders@chromium.org>
(cherry picked from commit e7e4ca0a49d27e57045567c8bb883035f71f53a8)
Reviewed-on: https://chromium-review.googlesource.com/c/chromiumos/third_party/kernel/+/4671868
Auto-Submit: Douglas Anderson <dianders@chromium.org>
Commit-Queue: Rubber Stamper <rubber-stamper@appspot.gserviceaccount.com>
Bot-Commit: Rubber Stamper <rubber-stamper@appspot.gserviceaccount.com>
[ Port to 4.19 ]
Signed-off-by: Kazuki Hashimoto <kazukih0205@gmail.com>

---
## [CommE2E/comm](https://github.com/CommE2E/comm)@[23b508c561...](https://github.com/CommE2E/comm/commit/23b508c561978fb9b36bc3b5c1f8890da1d1cdb7)
#### Monday 2023-08-28 06:59:33 by Ginsu Eddy

[native] fix broken messaging experience from forcing incorrect message height measurements

Summary:
A quick and dirty approach to fixing forcing the incorrect height measurements where we revert back to the solution where we measure just the inner message and the inline engagement.

The issue with this solution was that the `RetrySend` component was not visible because I was initially not considering this element when we were forcing the height for composed messages.

However, **we don't need to consider** this element when we are forcing the height. We only need to force the height of the message that is being measured (which is the inner message and the inline engagement). So I believe an alternate solution that could work here is we can place the `RetrySend` component outside of the `View` with the `viewStyle` (see inline comment below for more clarity) so we aren't considering `RetrySend` in the first place when we force the height.

Placing `RetrySend` outside this `View` should be find since in theory an `InlineEngagement` and `RetrySend` should never be rendered at the same time since you can't edit, react, or create a sidebar on a failed local message.

I am aware that with this solution we are losing the benefits of reducing the amount of repeated code and localizing the height-warning logic in the same place that the height-forcing logic is in; however, some of the other solutions that I am exploring are a little more complicated/I need to spend a bit more time testing than I initially expected and I want to get something out soon to unblock native releases asap.

Here is the [[ https://linear.app/comm/issue/ENG-4672/forcing-height-of-whole-message-breaks-timestamp-expansion-experience | Linear exchange ]] where @ashoat and I discuss moving forward with this approach

Depends on D8920

Test Plan:
Tested these flows and confirmed the following with forcing the height measurement

- Rendered the composed messages (text/multimedia) and the messages did not shift like they do when I force an incorrect height
- Rendered the robotext messages and the messages did not shift like they do when I force an incorrect height
- Tested adding/removing reactions
- Tested adding sidebar
- Tested editing
- Tested sending a failed message and confirmed that `RetrySend` was visible
- Tapped on the message and saw that the timestamp is visible
- Tested reply message and everything worked like before
- Tested copy message and everything worked like before
- Tested horizontal message gesture (reply/sidebar) and everything worked like before

{F704435}

Please note that the strange visual behavior with replying and editing messages was already here prior to any changes with the new inline engagement. I figured these issues are outside the scope of the inline engagement project and they should get addressed soon when we build out the new message action bottomsheet/tooltip

EDIT: whoops realized I didn't show Tested sending a failed message and confirmed that `RetrySend` was visible. Here it is:
{F704487}

Reviewers: ashoat, tomek, atul

Reviewed By: ashoat

Subscribers: ashoat, tomek

Differential Revision: https://phab.comm.dev/D8921

---
## [ArisonID/aris-silly-themes](https://github.com/ArisonID/aris-silly-themes)@[5d7a2b76db...](https://github.com/ArisonID/aris-silly-themes/commit/5d7a2b76db910dac9a376f28c476ac2336381fe1)
#### Monday 2023-08-28 07:53:19 by Ari

Hey guys, did you know that in terms of male human and female Pokémon breeding, Vaporeon is the most compatible Pokémon for humans? Not only are they in the field egg group, which is mostly comprised of mammals, Vaporeon are an average of 3”03’ tall and 63.9 pounds, this means they’re large enough to be able handle human dicks, and with their impressive Base Stats for HP and access to Acid Armor, you can be rough with one. Due to their mostly water based biology, there’s no doubt in my mind that an aroused Vaporeon would be incredibly wet, so wet that you could easily have sex with one for hours without getting sore. They can also learn the moves Attract, Baby-Doll Eyes, Captivate, Charm, and Tail Whip, along with not having fur to hide nipples, so it’d be incredibly easy for one to get you in the mood. With their abilities Water Absorb and Hydration, they can easily recover from fatigue with enough water. No other Pokémon comes close to this level of compatibility. Also, fun fact, if you pull out enough, you can make your Vaporeon turn white. Vaporeon is literally built for human dick. Ungodly defense stat+high HP pool+Acid Armor means it can take cock all day, all shapes and sizes and still come for more

---
## [gcheron/langchain](https://github.com/gcheron/langchain)@[16af5f8690...](https://github.com/gcheron/langchain/commit/16af5f86905705096552507f8739b5cfcaa77aa4)
#### Monday 2023-08-28 07:53:42 by niklub

Add LabelStudio integration (#8880)

This PR introduces [Label Studio](https://labelstud.io/) integration
with LangChain via `LabelStudioCallbackHandler`:

- sending data to the Label Studio instance
- labeling dataset for supervised LLM finetuning
- rating model responses
- tracking and displaying chat history
- support for custom data labeling workflow

### Example

```
chat_llm = ChatOpenAI(callbacks=[LabelStudioCallbackHandler(mode="chat")])
chat_llm([
    SystemMessage(content="Always use emojis in your responses."),
        HumanMessage(content="Hey AI, how's your day going?"),
    AIMessage(content="🤖 I don't have feelings, but I'm running smoothly! How can I help you today?"),
        HumanMessage(content="I'm feeling a bit down. Any advice?"),
    AIMessage(content="🤗 I'm sorry to hear that. Remember, it's okay to seek help or talk to someone if you need to. 💬"),
        HumanMessage(content="Can you tell me a joke to lighten the mood?"),
    AIMessage(content="Of course! 🎭 Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"),
        HumanMessage(content="Haha, that was a good one! Thanks for cheering me up."),
    AIMessage(content="Always here to help! 😊 If you need anything else, just let me know."),
        HumanMessage(content="Will do! By the way, can you recommend a good movie?"),
])
```

<img width="906" alt="image"
src="https://github.com/langchain-ai/langchain/assets/6087484/0a1cf559-0bd3-4250-ad96-6e71dbb1d2f3">


### Dependencies
- [label-studio](https://pypi.org/project/label-studio/)
- [label-studio-sdk](https://pypi.org/project/label-studio-sdk/)

https://twitter.com/labelstudiohq

---------

Co-authored-by: nik <nik@heartex.net>

---
## [JordanGidman/react-movie-rating-game](https://github.com/JordanGidman/react-movie-rating-game)@[35b6c3b500...](https://github.com/JordanGidman/react-movie-rating-game/commit/35b6c3b50023e558cfd4fb41b77dc7b80c19c918)
#### Monday 2023-08-28 08:31:48 by JordanGidman

Finishing Touches

So yesterday and this morning i have spent adding the finishing touches to the app.

Added: The ability to choose the player whos turn you want it to be. Thanks to the useReducer function and keeping track of the activePlayer via their ID i am able to easily switch player by adding a new case to the switch statement and adding an onClick to the player card. I have also ensured this onClick is not applied before the app starts.

Added: I used another custom hook together with the useRef hook to make the the input field focus when pressing enter and so the user doesnt need to click the box for each new user.

Added: I added a component for the isLoading and the error variables i was returning from the useMovies hook to conditionally render the Loader component when the movies are loading to display to the user that something is happening.

Added: i have also used the activePlayer state variable to conditionally apply an active class to the activePlayer so the user has a visual representation of whos turn it is.

Added: I added a play again button for ease of use so the user can either reset completely and enter new players or play again with the same players and maybe add some new ones in.

Added: General styling changes and touches to make the application look a little cleaner and nicer. I am not yet 100% happy with the design of the end screen yet particularly the way the movies and their ratings are displayed and i will make a final update to this when im clearer on how i want it to look.

Fixed:  I was having an issue with the API calls being bounced back from my hosted version of this application and the movies nor their ratings were not being fetched, this was due to API security and was a simple fix of updating the URL for my fetch requests to be https instead of http.

---
## [betagouv/aplypro](https://github.com/betagouv/aplypro)@[4f682c5e23...](https://github.com/betagouv/aplypro/commit/4f682c5e23ab75f7549e2ae2037ea3e7e380dcae)
#### Monday 2023-08-28 08:40:55 by Stéphane Maniaci

db: introduce schoolings

It's not exactly clean, namely because of the mapping code which remains
god-awful. However, it introduces schoolings which is the intermediate
class that represents a student belonging to many classes.

This paves the way for next-schoolyear problems, when students will
hopefully pass and move on to another class: if next year is N+1, our
schoolings table will look like this:

| student | classe_id | start_date | end_date |
|---------+-----------+------------+----------|
| X       |         3 |            |          |
| X       |         4 |            |          |

How we design which class is the current one, I'm not sure. We could
say it's the latest recorded in the database but that might not
necessary be true.

Coming shortly is storing the year on the classe table, which means we
can say "whatever is the latest classe", but then you might also
change schools during the year in which case you've got two classes of
the same year:

| classe_id | label                        | year |
|-----------+------------------------------+------|
|         3 | "the class in your hometown" | 2023 |
|         4  | "the class in your new town" | 2023 |

So I'm not sure. What we *can* do is write the `end_date` of the
schoolings table as soon as we receive the same student in a different
class.

---
## [Hardaeborla/zechub](https://github.com/Hardaeborla/zechub)@[9e448711f9...](https://github.com/Hardaeborla/zechub/commit/9e448711f9676343eb138487a4be9d80d30de65a)
#### Monday 2023-08-28 09:16:01 by Hardaeborla

zecweekly57.md

#Iwe Iroyin Osẹ-ọsẹ Zec #57

Àwọn ifunni Zcash Kékeré Ṣí fún Àwọn olubẹwẹ, Àwọn imudojuiwọn Agbègbè àti Rántí Wípé “Aṣiri jẹ Deede”

 Atunto nipasẹ "Tony Akins"[(@Tonyakins01)](https://twitter.com/TonyAkins01) 
ati Itumọ si ede Yoruba nipasẹ "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

### EKaabo si ZecWeekly

Ọsẹ moriwu mìíràn fún Zcash bí àgbègbè ṣé gbá atilẹyin ńlá àti àwọn ìgbì ìdàgbàsókè túntún, ZecHub pínpín nkan Ìwé ìròhìn kàn, àwọn imudojuiwọn Ìdàgbàsókè Arborist àti àgbègbè ṣe ìdáhùn sí ikọlu lórí òmìnira ọrọ tí àwọn olupilẹṣẹ.
---

## Nkan Ẹkọ ti Ọsẹ yii
Pipinpin awọn iyatọ laarin awọn adagun-omi Idabobo Imọ Zero ati ailorukọ-orisun ti o da lori ni afikun aipẹ si wiki ZecHub. Iṣafihan si Awọn adagun-omi Dabobo, Awọn ẹri Imọye Zero, Awọn Ibuwọlu Iwọn & Awọn iṣowo Asiri. Awọn afiwera lẹhinna fa ni fifun ni ero ti o daju lẹhin idi ti Zcash n pese awọn iṣeduro aṣiri lori-pq aifẹ.
[Ka ni ibi yìí](https://wiki.zechub.xyz/zk-shielded-pools-vs-decoy-based-privacy) 




## Awọn imudojuiwọn Zcash

####  Awọn imudojuiwọn ECC ati ZF
[Awọn ohun elo🗎 Ṣii fun Yika Keji ti Awọn ifunni Kekere ZF](https://forum.zcashcommunity.com/t/all-ecc-teams-focused-on-wallet-performance/42860/107) 

[Awọn ẹgbẹ ECC dojukọ iṣẹ ṣiṣe apamọwọ](https://forum.zcashcommunity.com/t/opening-applications-for-the-second-round-of-zf-minor-grants/45463) 

[Ẹgbẹ ZFAV ṣe atẹjade awọn itọsọna 📚 fun awọn olupilẹṣẹ àkóónú](https://wiki.zechub.xyz/zfav/guides) 

####  Awọn imudojuiwọn Awọn ifunni Agbegbe Zcash

[Imudojuiwọn Lórí Ilolupo Aboo](https://forum.zcashcommunity.com/t/zcash-ecosystem-security-lead/42090/91) 

[Igbero fun 🇧🇷  Aṣiri Alliance tí Ilu Brazil](https://forum.zcashcommunity.com/t/brazilian-privacy-alliance/45486) 

[Àgbègbè Igbowosile ZFAV ní Ipele](https://twitter.com/ZFAVClub/status/1693689895254949983) 

#### Awujo Ise Agbese 
[Awọn agbasọ nipa Asiri🗣️ - Topcrypto](https://free2z.cash/TopCrypto/zpage/dont-overshare-privacy-is-power-zcash) 

[Zcash Espanol ṣe iṣẹlẹ iṣẹlẹ atunṣe Zcon4](https://twitter.com/zcashesp/status/1694857330284712324) 

[Ìpè  🌳 Arborist Lakotan](https://twitter.com/zksquirrel/status/1694876187586170957) 

[Ọ̀rọ̀ @Zulakyz NFT lórí tí ZecHub Extras](https://zcashesp.com/zechub-nft-acceso-extra-a-beneficios-e-informacion-zcash/) 

[Itan kékeré láti ọ̀dọ̀ Cypherpunk Zero - Zerodartz🔥](https://free2z.com/zerodartz/zpage/cypherpunk-hacks-in-zed-city-short-story-3-out-of-12-chapters) 

[Awọn itumọ nilo fun Nighthawk apamọwọ](https://crowdin.com/project/Nighthawk-wallet) 


#### Iroyin ati Media 

[Ilosiwaju tí de ba Ethereum Staking💹  - Decrypt](https://decrypt.co/153813/ethereum-staking-is-booming-but-value-of-defi-assets-keeps-falling) 

[Kini idi ti asiri di ọrọ buburu? - Coindesk](https://www.coindesk.com/consensus-magazine/2023/08/25/when-did-privacy-become-a-bad-word) 

[Account tí OnlyFans tí Gba Friend.tech - Decrypt](https://decrypt.co/153723/onlyfans-accounts-take-over-friend-tech-crypt-app-adds-photo-feature) 

[Òṣìṣẹ́ banki aringbungbun sọrọ nipa Euro oni nọmba aladani ni ìlú 🇪🇸 Spanish - Cointelegraph](https://cointelegraph.com/news/spanish-central-bank-official-talks-about-private-payment-services-era-digital-euro) 

[Awọn anfani Lido n pọ si ti Ethereum - Trustnodes](https://www.trustnodes.com/2023/08/27/lido-closes-in-on-33-of-the-ethereum-network) 

[Awọn iran ti ọjọ iwaju lórí Decentralization - Cypherpunk](https://www.cypherpunktimes.com/visions-of-a-decentralised-future/) 

[Akojọpọ ọsẹ - Lori Brink](https://onthebrink-podcast.com/roundup-08-25-23/) 



## Awon oro die Nipa ZCash Lori Twitter
[👉 Iyatọ laarin Monero àti Zcash](https://twitter.com/MKjrstad/status/1695814999405379672) 

[Ikede nla nbọ laipẹ? - TrendsXBT](https://twitter.com/TrendsXBT/status/1694891818226213127) 

[Awọn iṣagbega nla ti a ṣe si Nighthawk](https://twitter.com/aiyadt/status/1694973730856866228) 

[Strawpoll ti o ni ipo 📊 ti Zcash Awọn ìṣáájú](https://twitter.com/nate_zec/status/1694405933638861048) 

[ZeroDAO ṣe igbega Zcash DeFi](https://twitter.com/zerodaoHQ/status/1694762728345456889) 

[Àṣírí sì jẹ déédéé](https://twitter.com/ZecHub/status/1694417573541007445) 

[O ṣeun lati ọdọ ZcashEsp!](https://twitter.com/zcashesp/status/1694861382154338648) 

[Fidio FROST ❄️  Ririnkiri lori Youtube](https://twitter.com/ZcashFoundation/status/1694410320859545939) 

[Awọn ifẹ ojo ibi Ailorukọ nipasẹ Zcash Memo](https://twitter.com/AyanlajaAdebola/status/1695721838943289694) 

[Bawo ni o ṣe n ṣe pẹlu ZEC?](https://twitter.com/ZcashForum/status/1693520113797116406) 

[Ṣe awọn spammers n ṣe rere fun nẹtiwọọki naa?](https://twitter.com/ZcashForum/status/1693430229044445287) 

[Awọn iwe afọwọkọ oluranlọwọ Zcasd lati Dismad :)] (https://twitter.com/ZcashForum/status/1693385561116164360) 

[A wa fun ominira - @zcash](https://twitter.com/zcash/status/1669397156212375583) 

[Iwe Iwe irohin ZecHub nipa Awọn adagun Àṣírí](https://twitter.com/ZecHub/status/1695082959911403585) 


[Joel Valenzuela pẹlu iwoye diẹ sii 📽️ lori Tornado Cash](https://twitter.com/TheDesertLynx/status/1694816146355036620) 




## Zeme ti Ose Yii 

[https://twitter.com/ZFAVClub/status/1694817298677113308](https://twitter.com/ZFAVClub/status/1694817298677113308) 


## Awọn iṣẹ ni ilolupo
[ZecWeekly #58  iwe iroyin Agbegbe](https://app.dework.xyz/zechub-2424/board?taskId=102e34d1-8f77-45d1-bd4f-d3d8f2a040ce) 

[Ṣiṣe Zcash Full Node lori Akash Network](https://app.dework.xyz/zechub-2424/board?taskId=543cab70-627d-4222-a712-9fb8768abe9c)

---
## [pulumi/pulumi](https://github.com/pulumi/pulumi)@[474866756e...](https://github.com/pulumi/pulumi/commit/474866756eb760a89553130eb25429818c1928c9)
#### Monday 2023-08-28 11:02:55 by Fraser Waters

Support bailing from RunFunc

**Background**

The result.Result type is used by our CLI implementation
to communicate how we want to exit the program.

Most `result.Result` values (built from errors with `result.FromError`)
cause the program to print the message to stderr
and exit the program with exit code -1.
The exception is `result.Bail()`,
which indicates that we've already printed the error message,
and we simply need to `exit(-1)` now.

Our CLI command implementation use `cmdutil.RunResultFunc`
which takes a `func(...) result.Result` to implement this logic.

`cmdutil` additionally includes a `cmdutil.RunFunc`
which takes a `func(...) error` and wraps it in `RunResultFunc`,
relying on `result.FromError` for the conversion:

    func RunFunc(run func(...) error) func(...) {
        return RunResultFunc(func(...) result.Result {
            if err := run(...); err != nil {
                return result.FromError(err)
            }
            return nil
        })
    }

**Problem**

In CLI contexts where we're using an `error`,
and we want to print an error message to the user and exit,
it's desirable to use diag.Sink to print the message to the user
with the appropriate level (error, warning, etc.)
and exit without printing anything else.

However, the only way to do that currently is
by converting that function to return `result.Result`,
turn all error returns to `result.FromError`,
and then return `result.Bail()`.

**Solution**

This change introduces a `result.BailError` error
that gets converted into a `result.Bail()`
when it passes through `result.FromError`.

It allows commands implementations that use `error`
to continue returning errors and still provide an ideal CLI experience.

It relies on `errors.Is` for matching, so even if an intermediate layer
wraps the error with `fmt.Errorf("..: %w", ErrBail)`,
we'll recognize the request to bail.

BailError keep track of the internal error that triggered it, which
(when everything is moved off of result and onto error) means we'll
still be able to see the internal errors that triggered a bail during
debugging.

Currently debugging engine tests is pretty horrible because you often
just get back a `result.Result{err:nil}` with no information where in
the engine stack that came from.

**Testing**

Besides unit tests, this includes an end-to-end test
for using RunResultFunc with a bail error.
The test operates by putting the mock behavior in a fake test,
and re-running the test binary to execute *just that test*.

**Demonstration**

This change also ports the following commands to use BailError:
cancel, convert, env, policy rm, stack rm.

These command implementations are simple and were able to switch easily,
without bubbling into a change to a bunch of other code.

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[78289cc18a...](https://github.com/ARF-SS13/coyote-bayou/commit/78289cc18a77a43ebb92b21561afea7a7ae4bb3a)
#### Monday 2023-08-28 11:22:02 by Tk420634

Fixes scorb

idk why the shits even broken what in the god damn I hate this fucking code

---
## [cyphar/runc](https://github.com/cyphar/runc)@[879188ca32...](https://github.com/cyphar/runc/commit/879188ca32c344fd2c74eb41ef36d708dfcd6c04)
#### Monday 2023-08-28 11:34:32 by Aleksa Sarai

tree-wide: use /proc/thread-self for thread-local state

With the idmap work, we will have a tainted Go thread in our
thread-group that has a different mount namespace to the other threads.
It seems that (due to some bad luck) the Go scheduler tends to make this
thread the thread-group leader in our tests, which results in very
baffling failures where /proc/self/mountinfo produces gibberish results.

In order to avoid this, switch to using /proc/thread-self for everything
that is thread-local. This primarily includes switching all file
descriptor paths (CLONE_FS), all of the places that check the current
cgroup (technically we never will run a single runc thread in a separate
cgroup, but better to be safe than sorry), and the aforementioned
mountinfo code. We don't need to do anything for the following because
the results we need aren't thread-local:

 * Checks that certain namespaces are supported by stat(2)ing
   /proc/self/ns/...

 * /proc/self/exe and /proc/self/cmdline are not thread-local.

 * While threads can be in different cgroups, we do not do this for the
   runc binary (or libcontainer) and thus we do not need to switch to
   the thread-local version of /proc/self/cgroups.

 * All of the CLONE_NEWUSER files are not thread-local because you
   cannot set the usernamespace of a single thread (setns(CLONE_NEWUSER)
   is blocked for multi-threaded programs).

Note that we have to use runtime.LockOSThread when we have an open
handle to a tid-specific procfs file that we are operating on multiple
times. Go can reschedule us such that we are running on a different
thread and then kill the original thread (causing -ENOENT or similarly
confusing errors). This is not necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) but
operating on the actual inodes associated with the tid requires this
locking.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[bae1aef3b4...](https://github.com/Striders13/tgstation/commit/bae1aef3b457cb4fbad551a8560319ed993ba397)
#### Monday 2023-08-28 12:54:37 by san7890

Refactors Regal Rats into Basic Mobs (more titles edition) (#77681)

## About The Pull Request

I literally can't focus on anything nowadays, so I just did this to
break a never-ending chain of distress. Anyways, regal rats! These
fellas are mostly player controlled, but did have _some_ AI capabilities
(mainly tied to their actions), so that was incorporated too. Everything
should work as-expected (as well as look a shitload cleaner).

Instead of doing weird and awful conditional signals being sent out, I
made the `COMSIG_REGAL_RAT_INTERACT` (not the actual name) have a return
value so we can always rely on that working whenever we have that signal
registered on something we attack. I also cleaned up pretty much every
proc related to regal rats, gave them AIs to reflect their kingly nature
(and action capabilities (as well as move the action to
`mob_cooldown`)).

Since I thought they needed it, Regal Rats now get a special moniker!
This is stuff like "the Big Cheese" and what-not, like actual regents in
history. That's nice.
## Why It's Good For The Game

Two more off the list. Much better code to read. Way smarter rats with
spawning their army as part of a retaliatory assault (war). More sovl
with better regal rat names. The list goes on.
## Changelog
:cl:
refactor: Regal Rats have been refactored into basic mobs. They should
be a bit smarter and retain their docility (until attacked, in which
case you should prepare to get rekt by summoned rats), and properly flee
when they can instead of just sit there as you beat them to death. The
framework for them interacting with stuff (i.e. opening doors while
slobbering on food) is a bit more unified too, now. They also have
cooler names too!
/:cl:

FYI: Beyond a few code touchups, I haven't touched the actions at all. I
do not believe myself to be enthusiastic about fixing anything involving
the actions code as of this moment so that this PR is more overbloated
unless it's unbelievably stupid or easy to fix.

---
## [Tiwari-Jyoti/Hotel-Booking-Application.github.io](https://github.com/Tiwari-Jyoti/Hotel-Booking-Application.github.io)@[3f8016ea79...](https://github.com/Tiwari-Jyoti/Hotel-Booking-Application.github.io/commit/3f8016ea79f0aa388c8bd22c278e42092422fe08)
#### Monday 2023-08-28 13:08:13 by Tiwari-Jyoti

Hotel-Booking-Application

Hotel Booking Application
Discover Your Perfect Stay with Our Hotel Booking Application
Welcome to our state-of-the-art Hotel Booking Application, where your dream vacation is just a click away. With a seamless blend of cutting-edge technology and exceptional user experience, we offer a range of features designed to make your hotel booking journey smooth and enjoyable.

Features that Elevate Your Experience:
🔐 Secure and Swift Authentication: Our application provides top-notch security through JWT authentication, ensuring that your personal information remains protected.

🏨 Explore Properties with Ease: Easily search and find the perfect property that matches your preferences, thanks to our intuitive property search feature.

🌟 Rate Your Experience: Share your valuable feedback by rating the properties you've visited, helping fellow travelers make informed decisions.

🗓️ Effortless Check-in and Check-out: Enjoy a hassle-free check-in and check-out process that respects your time and comfort.

📖 Comprehensive Property Catalogue: Browse through a wide array of properties, each with detailed information, high-quality images, and precise descriptions.

❓ Q&A Service for Your Queries: Have questions about a property? Our Q&A service lets you inquire about facilities, amenities, and more, ensuring you have all the information you need.

💌 Instant Booking Confirmation: Rest easy knowing that as soon as you book a room, our system sends you a confirmation email with all the details you need.

Powerful Technology Behind the Scenes:
For the Tech Enthusiasts:

Backend Technologies:

Leveraging the robustness of Java 11 and Spring Boot 2.6, our backend offers a solid foundation for a smooth experience.
Trust and security are paramount, which is why we've integrated Spring Security and JWT authentication to keep your data safe.
Seamlessly interact with our MySQL database using Spring Data JPA and Hibernate, ensuring efficient data management.
Our codebase is expertly managed using Maven, and Docker ensures easy deployment and scalability.

Frontend Technologies:

The captivating front end, powered by Angular 13, provides an interface that's as dynamic as your travel aspirations.
We've carefully blended Angular Material and Bootstrap to craft an aesthetically pleasing and user-friendly design.
From sleek HTML and CSS to robust TypeScript, our technology stack ensures a responsive and interactive experience.
Empowering Users and Admin Alike:
User-Centric Focus:

Seamlessly register and log in to your account, granting you access to exclusive features.
Effortlessly book your desired hotel, with user-friendly forms and smart validations.
For peace of mind, We've implemented stringent validation checks for critical fields like passwords, phone numbers, and check-in/out dates.
Your profile is your space; view and manage your information whenever you need it.
Admin at Your Service:

Admins wield the power to manage hotels, updating details, and ensuring that the information is always accurate.
Keep a watchful eye on user details, helping maintain a secure and trustworthy platform.
In cases where room availability is full, admins can toggle room availability status to ensure transparency.
Secure Payments and Support:

A dedicated payment page with intelligent validation ensures secure transactions.
Count on our assistance through the contact us page, while also staying connected through our social media handles.
Embark on Your Journey:
Your dream vacation begins with our Hotel Booking Application. Dive into a world of seamless booking, outstanding features, and technological excellence. Your comfort and satisfaction are our top priorities. Book with us today and experience a new era of hotel booking!

---
## [aarani/geewallet](https://github.com/aarani/geewallet)@[c5095e0056...](https://github.com/aarani/geewallet/commit/c5095e00562e2a172a262de7d8def8495e78a78b)
#### Monday 2023-08-28 15:00:13 by Andres G. Aragoneses

build: remove Nuget.Restore.targets

This was kzu's project[1] which had a very interesting goal:
make nuget restore be part of the build process itself (kind of
like a PreBuild target so that your IDE did the restore before
building, regardless if the IDE had nuget support or not).

Now, there's several reasons to remove it (ordered by level of
importance):

1. We're moving soon to dotnet v6 and newer, where a restore is
always assumed by the IDEs and command-line builds (the command
is even called "dotnet restore" itself, no need to specify
"nuget" anymore, as the term 'restore' has become part of the
dotnet jargon already).

2. Looking back, I introduced it in 2017 [2] but I kinda regret
doing it because of all the hacks (such as needing to generate
the special file 'before.$solutionFileName.targets before the
build) required to make it work, the ugliness of its code (not
really blaming the author here, maybe MSBuild's XML syntax is
generally unreadable), and:

3. The fact that despite the use of it, there were certain
sccenarios that needed an explicit restore of other solutions
or projects to make the build work with Xamarin.Forms.

So as there were explicit restores happening in make.fsx
anyway, let's make nuget restore explicitly handled now in all
cases by make.fsx (this quirk will not live very long anyway,
just as long as the Xamarin.Forms frontend lives, which is
getting replaced by MAUI soon).

This commit also disables nuget restore parallel processing
to prevent flaky nuget restore on mono.

[1] https://github.com/kzu/Nuget.Restore
[2] 9804b653a63266c8560c7e8143f9ec644f05a334

---
## [axodotdev/cargo-dist](https://github.com/axodotdev/cargo-dist)@[8da5e50ada...](https://github.com/axodotdev/cargo-dist/commit/8da5e50ada03b9cc5404f9a2c51aa9cc4bbe346b)
#### Monday 2023-08-28 15:09:18 by Aria Beingessner

feat(msi): add msi installer

The "msi" installer vendors the binaries into a windows msi.
msi generation is implemented by using cargo-wix as a library,
which in turn handles generating templates and invoking WiX (v3).

The resulting msi's are unsigned -- signing will be handled by a followup,
as changes to OV certs mean that "proper" signing is now very complicated
and messy.

This implementation has some notable details:

WiX requires an xml-based template called main.wxs for each msi it generates.
This template includes things like the application name, version, publisher,
EULA, embedded files, and so on.

cargo-wix's default workflow is for you to run `cargo wix init` once to generate
that file and check it in. At this point the developer is free to hand-edit
the template to suit their needs. We like this idea, `cargo dist generate-ci`
is based on that same premise!

But our experience with generate-ci has also taught us that this approach
is really prone to frustrating desyncs. The main.wxs bakes in several pieces
of information that were sourced from your Cargo.toml. As a result, if you
ever change your Cargo.toml, you now need to remember to apply the same
change to your main.wxs, or rerun `cargo wix init` and potentially clobber
any hand-edits you made.

As such, for the first draft of this feature we've opted for a more aggressive
solution: whenever you run `cargo dist init` we will invoke `cargo wix init`
to force the template to have up to date contents, essentially forbidding
hand-edits.

[Not Yet Implemented] When you run `cargo dist build` or `cargo dist plan`
we will also error out if we detect that `cargo wix init` would modify
main.wxs.

[Not Yet Implemented] A new allow-dirty config is added to cargo-dist to
prevent `init` from regenerating main.wxs or checking that it's up to date,
essentially restoring the original design of cargo-wix. We believe this
should be opt-in because most people ideally shouldn't want to do hand-edits,
and desyncing is a very nasty footgun.

`cargo dist init` will also modify your Cargo.tomls to add
`[package.metadata.wix]` with two generated GUIDs (if those GUIDs aren't
already present).

These GUIDs are used by windows to identify that two different msis actually
intend to refer to the same application and install dir. As such, each release
of your app needs to use the same GUID.

cargo-wix bakes these GUIDs into your main.wxs, and critically it defaults to
generating new random ones every time you run init (because constantly
re-initing wasn't part of the design).

By persisting the GUIDs to your package's Cargo.toml, we unlock the ability
to freely regenerate main.wxs whenever we want.

The logic to select the packages that need msi's in `cargo dist init` is
currently a temporary hack that doesn't properly check all config. We should
add a proper `generate-wix` command that does proper config/package using
the DistGraph.

We invoke cargo-wix to actually build the msi's in a kind of hacky way.
cargo-wix was built to assume it would be in charge of building the binaries
that get embedded in the msi, but cargo-dist wants to be in charge of that.

cargo-wix does have a --no-build option, but it still assumes the binaries
will be in the cargo target dir, and emits a warning that this is happening
(which will confuse our users).

I did some upstream work to add a --profile flag so that it would understand
we built with the 'dist' profile, but after working through the details I've
realized that cargo-dist really just wants to give cargo-wix a temp dir that
the binaries (and any other files to include) have been copied into.

The issue is that multiple Cargo builds in series can clobber eachother's binaries,
so if you want to do multiple builds and potentially combine the results you
really need to be actively copying the binaries out of the target dir between
each build. This notably happens if you build multiple feature variations of
an application (which cargo-dist doesn't yet support but plans to).

cargo-dist is therefore architected to just run all the builds in series and
copy the binaries to different temp dirs for each bundling method, notifying
the bundling method its temp dir is ready only once all dependencies are
fulfilled.

I briefly considered replicating the target dir structure in the temp-dir
so that we could just tell cargo-dist the temp-dir *is* the target dir but
this still wouldn't get rid of the warning so really I should just work with
upstream on a proper API for this.

As a temporary hack we just assume target clobbering isn't a problem and
have cargo-wix read the binaries out of the real target dir, while still
passing --no-build.

---
## [stephentoub/semantic-kernel](https://github.com/stephentoub/semantic-kernel)@[2733a5574f...](https://github.com/stephentoub/semantic-kernel/commit/2733a5574f72980413e339f100dbe4272644888c)
#### Monday 2023-08-28 15:21:49 by Mark Karle

Python: Import OpenAPI documents into the semantic kernel (#2297)

### Motivation and Context

<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->

This allows us to import OpenAPI documents, including ChatGPT plugins,
into the Semantic Kernel.

### Description

<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
- The interface reads the operationIds of the openapi spec into a skill:
```python
from semantic_kernel.connectors.openapi import register_openapi_skill
skill = register_openapi_skill(kernel=kernel, skill_name="test", openapi_document="url/or/path/to/openapi.yamlorjson")
skill['operationId'].invoke_async()
```
- Parse an OpenAPI document
- For each operation in the document, create a function that will
execute the operation
- Add all those operations to a skill in the kernel
- Modified `import_skill` to accept a dictionary of functions instead of
just class so that we can import dynamically created functions
- Created unit tests

TESTING:
I've been testing this with the following ChatGPT plugins:
- [Semantic Kernel Starter's Python Flask
plugin](https://github.com/microsoft/semantic-kernel-starters/tree/main/sk-python-flask)
- [ChatGPT's example retrieval
plugin](https://github.com/openai/chatgpt-retrieval-plugin/blob/main/docs/providers/azuresearch/setup.md)
- This one was annoying to setup. I didn't get the plugin functioning,
but I was able to send the right API requests
- Also, their openapi file was invalid. The "servers" attribute is
misindented
- [Google ChatGPT
plugin](https://github.com/Sogody/google-chatgpt-plugin)
- [Chat TODO plugin](https://github.com/lencx/chat-todo-plugin)
- This openapi file is also invalid. I checked with an online validator.
I had to remove"required" from the referenced request objects'
properties:
https://github.com/lencx/chat-todo-plugin/blob/main/openapi.yaml#L85

Then I used this python file to test the examples:

```python
import asyncio
import logging

import semantic_kernel as sk
from semantic_kernel import ContextVariables, Kernel
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion
from semantic_kernel.connectors.openapi.sk_openapi import register_openapi_skill

# Example usage
chatgpt_retrieval_plugin = {
    "openapi": # location of the plugin's openapi.yaml file,
    "payload": {
        "queries": [
            {
                "query": "string",
                "filter": {
                    "document_id": "string",
                    "source": "email",
                    "source_id": "string",
                    "author": "string",
                    "start_date": "string",
                    "end_date": "string",
                },
                "top_k": 3,
            }
        ]
    },
    "operation_id": "query_query_post",
}

sk_python_flask = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"skill_name": "FunSkill", "function_name": "Joke"},
    "payload": {"input": "dinosaurs"},
    "operation_id": "executeFunction",
}
google_chatgpt_plugin = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "query_params": {"q": "dinosaurs"},
    "operation_id": "searchGet",
}

todo_plugin_add = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo": "finish this"},
    "operation_id": "addTodo",
}

todo_plugin_get = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "operation_id": "getTodos",
}

todo_plugin_delete = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo_idx": 0},
    "operation_id": "deleteTodo",
}


plugin = todo_plugin_get # set this to the plugin you want to try

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

kernel = Kernel(log=logger)
deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel.add_text_completion_service(
    "dv", AzureTextCompletion(deployment, endpoint, api_key)
)

skill = register_openapi_skill(
    kernel=kernel, skill_name="test", openapi_document=plugin["openapi"]
)
context_variables = ContextVariables(variables=plugin)
result = asyncio.run(
    skill[plugin["operation_id"]].invoke_async(variables=context_variables)
)
print(result)
```

### Contribution Checklist

<!-- Before submitting this PR, please make sure: -->

- [ ] The code builds clean without any errors or warnings
- [ ] The PR follows the [SK Contribution
Guidelines](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
and the [pre-submission formatting
script](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md#development-scripts)
raises no violations
- [ ] All unit tests pass, and I have added new tests where possible
- [ ] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <abharris@microsoft.com>

---
## [Sancaknr/Sancak](https://github.com/Sancaknr/Sancak)@[5fb6834f5d...](https://github.com/Sancaknr/Sancak/commit/5fb6834f5d1ab9d2b6b7df767a6d804b18f1eede)
#### Monday 2023-08-28 15:36:30 by Sancaknr

"Tweet Counter: Version 0.2 Update!"


🎉 New Update - Exciting Changes Await! 🎉

📢 We're thrilled to bring you an enhanced experience with our latest update! Your favorite tweet counter just got even better. Let's dive into what's new:

🔐 Advanced Security Features: We take your security seriously. Now, not only can you log in with your username, but we've also added a password layer for extra protection. Your data is safe with us!

🎮 Improved User Interaction: We've revamped the user interaction to make it more intuitive and enjoyable. From smoother login processes to seamless tweeting, every interaction is designed with you in mind.

🔄 Streamlined Authentication: Logging in is now a breeze. Our updated username login process ensures a seamless authentication experience. Say goodbye to confusion and hello to quick access.

🔧 Bug Fixes and Enhancements: We've addressed those cryptic error messages that used to give you a hard time. Our error understanding has been improved, ensuring a frustration-free experience. Also, any issues related to using usernames have been completely resolved.

Stay tuned for more updates as we continue to refine your tweeting journey. Happy coding and tweeting! 🚀🎮

---
## [Kaz205/pipa](https://github.com/Kaz205/pipa)@[1cad056b6f...](https://github.com/Kaz205/pipa/commit/1cad056b6f8d4e0a1b57730bbf9572046c84c103)
#### Monday 2023-08-28 15:49:52 by Peter Zijlstra

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
## [mtpereira/workstation-setup](https://github.com/mtpereira/workstation-setup)@[33ce6b4ae6...](https://github.com/mtpereira/workstation-setup/commit/33ce6b4ae6a5e94842cbcd1865b13edf7e81e0b5)
#### Monday 2023-08-28 17:04:12 by Manuel Tiago Pereira

Fix CPU fan delay on temperature increase

My Dell XPS 9360 has been overheating for awhile now. Since it is a 5
year old laptop, I've _assumed_ (uh uh...) that the ~40 degrees
temperatures of where I'm living, plus the dust likely collected by the
fan were the issue.

For that reason, I've started by cleaning up the fan, replacing the
thermal past on the CPU, which unfortunately did not made that much of
an improvement.

I've then took the laptop to a local computer shop, where the person
there told me that, by the sound of it, the fan should be on the last of
its days. This is when I found out that Dell does not resell these
components (at least not for 5 year old laptops...), so I had to dig a
bit on the internet to find and purchase replacement. After installing
that new fan, while it was a bit better (i.e., it didn't overheat so
easily), it was still a problem...

Then I finally did what I should have done from the start: pay attention
to what is happening to the CPU temperatures and to the fan when I
increase utilisation on the laptop. It seemed to me then that the issue is
the fan taking several seconds to spin up properly after the CPU
gets to 80+ degrees, which then leads to the fan not being able to
cooldown the CPU fast enough.

I then read about Dell's System Management Mode (SSM) BIOS, that
basically overtakes fan control from the operating system. [1]
Seems like this is the sole reason for [`dell-smm-hwmon` kernel module](https://docs.kernel.org/hwmon/dell-smm-hwmon.html#description)'s
existence, but unfortunately,
[it doesn't know a thing about this particular
laptop](https://github.com/torvalds/linux/blob/2dde18cd1d8fac735875f2e4987f11817cc0bc2c/drivers/hwmon/dell-smm-hwmon.c#L1292C20-L1292C20)
[2], meaning that I had find another way
retake control of the fan to the OS.
Finally, [the Archlinux wiki article on
this](https://wiki.archlinux.org/title/Fan_speed_control#Dell_laptops)
mentions a fork of a `dell-ssm-hwmon`-related tool that does handle this
laptop's Dell BIOS properly, so that it can disable BIOS fan control.

So with that all out of the way, we can setup `fancontrol` to properly
keep the temperature low on the CPU, by running `pwmconfig` to generate
its configuration, enabling the `fancontrol` service, and making sure it
is running on sleep resume. [3]

1: Coincidentely, I did update the BIOS firmware around the time that
   this whole ordeal started, but I cannot for the life of me remember
   if it was before or after the first overheating incidents.
2: I'm sure not to anyone's fault but Dell, for not providing these codes to the kernel developers.
3: It seems to be a known issue that the daemon will stop working on
   resume: https://github.com/lm-sensors/lm-sensors/issues/172

---
## [bevyengine/bevy](https://github.com/bevyengine/bevy)@[44f677a38a...](https://github.com/bevyengine/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Monday 2023-08-28 17:09:15 by Sélène Amanita

Improve documentation relating to `Frustum` and `HalfSpace` (#9136)

# Objective

This PR's first aim is to fix a mistake in `HalfSpace`'s documentation.

When defining a `Frustum` myself in bevy_basic_portals, I realised that
the "distance" of the `HalfSpace` is not, as the current doc defines,
the "distance from the origin along the normal", but actually the
opposite of that.

See the example I gave in this PR.

This means one of two things:
1. The documentation about `HalfSpace` is wrong (it is either way
because of the `n.p + d > 0` formula given later anyway, which is how it
behaves, but in that formula `d` is indeed the opposite of the "distance
from the origin along the normal", otherwise it should be `n.p > d`)
2. The distance is supposed to be the "distance from the origin along
the normal" but when used in a Frustum it's used as the opposite, and it
is a mistake
3. Same as 2, but it is somehow intended

Since I think `HalfSpace` is only used for `Frustum`, and it's easier to
fix documentation than code, I assumed for this PR we're in case number
1. If we're in case number 3, the documentation of `Frustum` needs to
change, and in case number 2, the code needs to be fixed.

While I was at it, I also :
- Tried to improve the documentation for `Frustum`, `Aabb`, and
`VisibilitySystems`, among others, since they're all related to
`Frustum`.
- Fixed documentation about frustum culling not applying to 2d objects,
which is not true since https://github.com/bevyengine/bevy/pull/7885

## Remarks and questions

- What about a `HalfSpace` with an infinite distance, is it allowed and
does it represents the whole space? If so it should probably be
mentioned.
- I referenced the `update_frusta` system in
`bevy_render::view::visibility` directly instead of referencing its
system set, should I reference the system set instead? It's a bit
annoying since it's in 3 sets.
- `visibility_propagate` is not public for some reason, I think it
probably should be, but for now I only documented its system set, should
I make it public? I don't think that would count as a breaking change?
- Why is `Aabb` inserted by a system, with `NoFrustumCulling` as an
opt-out, instead of having it inserted by default in `PbrBundle` for
example and then the system calculating it when it's added? Is it
because there is still no way to have an optional component inside a
bundle?

---------

Co-authored-by: SpecificProtagonist <vincentjunge@posteo.net>
Co-authored-by: Alice Cecile <alice.i.cecile@gmail.com>

---
## [codecov/worker](https://github.com/codecov/worker)@[c70cb64c6a...](https://github.com/codecov/worker/commit/c70cb64c6a0bbf425ac92b82b8cae103b98cb6c1)
#### Monday 2023-08-28 17:31:05 by Giovanni M Guidini

Extend `ReportDetails` to save data into GCS (#1180)

* Extend `ReportDetails` to save data into GCS

We have decided to move some data to GCS. Read more [here](https://www.notion.so/sentry/Moving-data-to-GCS-7fd3d7130a4d43bf987e55fe3090fc26?pvs=4). `ReportDetails.files_array` is the first column that we want to move.

The first step was to extend the model in codecov-api ([codecov-api_PR1543](https://github.com/codecov/codecov-api/pull/1543)) and do the migration to prepare the database for this change. Now we can extend the model here in the worker and actually start saving data into GCS.

Notice that the actual saving is feature-flagged and configurable under "setup" > "save_report_data_in_storage" > "report_details_files_array" (setting it to True). The idea is to have a new key for all columns we move, so that we can roll them out one by one and control exactly what data goes where. Furthermore, by setting "setup" > "save_report_data_in_storage" > "only_codecov" to True only repos that belong to codecov will save whatever columns we set to save in GCS in GCS. Other customers'data would still go to the DB.

You'll also notice that, differently from codecov-api (which uses Django's `@cached_property`) this one uses a mix of `@property` and `@lru_cache`. This is because `functools.cached_property` does accept writes, but I found the [docs](https://docs.python.org/3/library/functools.html#functools.cached_property) confusing and with a bunch of warnings. Then right at the end they suggest:

> If a mutable mapping is not available or if space-efficient key sharing is desired, an effect similar to cached_property() can also be achieved by stacking property() on top of lru_cache().

I thought that was a better option, since we can use `property()` and specify what is the getter and setter function. Plus we only really need to cache the getter function. In my opinion this made the code clearer and easier to understand, if a bit more verbose. And we have to remember to clear the getter cache when seting a new value, but it's not so bad. Plus, as the tests show, the cache does work. Nice.

* Include list of allowed repos

Similar to what was done for the `report_builder` process (see 84845cacdefcd03d3088be7d85edf98ee1c1dc20) we're adding
`"setup" > "save_report_data_in_storage" > "repo_ids"` as a list of repos for which saving files_array in storage is
turned on.

This will allow for a selective roll-out.

---
## [ShingenTakeda/microservices](https://github.com/ShingenTakeda/microservices)@[69d66014a9...](https://github.com/ShingenTakeda/microservices/commit/69d66014a907a35a30b08220a0bbab980b908b66)
#### Monday 2023-08-28 18:05:49 by ShingenTakeda

Almost finishing the logger service(Fucking kill me)

GOD LOGGING SHIT IS BORING

---
## [edgarulg/gate](https://github.com/edgarulg/gate)@[e2a108db75...](https://github.com/edgarulg/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Monday 2023-08-28 18:06:53 by Chris Phillips

fix(authn/oauth2): prevent oauth2 redirect loops (#1517)

During setup of spinnaker authentication with oauth2 a common hurdle is a redirect loop.

For example:

https://github.com/spinnaker/spinnaker/issues/5794
https://github.com/spinnaker/spinnaker/issues/1630

Also, many threads in Slack discuss these problems. In fact this appears to be a common
pitfall for the spring-security-oauth2-autoconfigure library in general. A light refresher
on the ouath2 flow in play here seems worthwhile. The user is redirected from `/login` in gate
to the external auth provider (google, github, etc.) and after successfully authenticating
they are redirected back to the gate `/login` endpoint but this time with a code parameter
that is to be used to request an access token.

This request can fail for a variety of reasons, and if it does, the underlying spring library
triggers a redirect to the `/error` endpoint. What causes the redirect loop for gate in particular
(and for other users of the library in a similar fashion) is that the WebSecurityConfigurerAdapter
in play is treating `/error` as an authenticated path and so instead of just returning with a 401,
it re-redirects to `/login` and the redirect loop continues.

My thought is that instead of a redirect loop, simply allowing the 401 to be returned will be a stronger
more helpful signal as to what is going on. Hopefully it will save future first-time installers headaches.

Spinnaker docs have included several troubleshooting hints and tips for how where you terminate SSL
affects configuration etc. Even after following all of these and lots of spelunking through spinnaker
github issues and combing over threads in slack, I found myself still experiencing a redirect loop even
though I had applied all the combined wisdom that was applicable to my setup.

As it turns out, I had a bad copy/paste of my client secret in my configuration. So the request
to turn the code from google into an access token from google was failing with a 401. After much
debugging and deep diving into the spring security code I found that had I turned on DEBUG in gate
for these classes in gate-local.yml:

```
logging:
  level:
    org.springframework.security.web.authentication.SimpleUrlAuthenticationFailureHandler: DEBUG
    org.springframework.security.oauth2.client.filter.OAuth2ClientAuthenticationProcessingFilter: DEBUG
```

Then I would have seen in the logs that a 401 response was returned from google and perhaps it would have
caused me to look closer at my botched client secret configuration. I think perhaps we don't want to require
that all operators of spinnaker become spring-security-oauth2 experts. So I'm proposing adding `/error` to
the list of paths in gate that aren't treated as authenticated. Thus short-circuiting the redirect loop and
bringing to light helpful troubleshooting info that was previously more or less swallowed.

---
## [Sancaknr/Sancak](https://github.com/Sancaknr/Sancak)@[f9cf44764b...](https://github.com/Sancaknr/Sancak/commit/f9cf44764ba4938a9f5fb8f5c4da49fb09cd7cf7)
#### Monday 2023-08-28 18:37:27 by Sancaknr

"Tweet Counter: Version 0.3 Update!"

🎉 New Update - Elevate Your Tweeting Experience! 🎉

📢 We're thrilled to unveil the latest version of your beloved tweet counter application, now even more refined and secure than before. Get ready to embark on a journey filled with smoother interactions, heightened security, and unmatched convenience. Let's dive into the exhilarating enhancements:

🔐 Advanced Security Features: Your safety is our top priority. Introducing an advanced layer of security - you can now set a strong password alongside your username. Rest assured, your precious data is shielded with the utmost care.

🎮 Enhanced User Interaction: Brace yourself for a seamlessly intuitive user experience. We've meticulously reimagined the interaction flow, transforming logging in and tweeting into a delightful breeze. Each step is meticulously designed to cater to your comfort.

🔄 Streamlined Authentication: Bid farewell to complexities. Our authentication process has undergone a sleek makeover. With the reimagined username and password login, you'll savor a swift and hassle-free entry into the world of tweeting.

🔧 Bug Fixes and Enhancements: We've diligently tackled those pesky bugs that once caused frustration. Say goodbye to cryptic error messages; clarity reigns supreme. Any concerns linked to usernames have been gracefully resolved.

Stay tuned for more updates as we continually enrich your tweeting odyssey. Happy coding and tweeting! 🚀🎮

---
## [IndigoHive/react](https://github.com/IndigoHive/react)@[b6978bc38f...](https://github.com/IndigoHive/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Monday 2023-08-28 18:38:12 by Andrew Clark

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
## [git/git](https://github.com/git/git)@[8f23432b38...](https://github.com/git/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Monday 2023-08-28 18:41:06 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [samirti/next.js](https://github.com/samirti/next.js)@[6238f8a5c0...](https://github.com/samirti/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Monday 2023-08-28 19:16:18 by Jimmy Lai

performance: don't compile on hover on dev (#51830)

An annoying issue that slows down compilation times in dev for Next is
that we might trigger compilation of a page via hover on app.

We do this because we want the same experience in production and dev and
the prefetching is important for instantaneous loading states.

The alternative in this PR is that we don't prefetch at all anymore in
dev but instead, when we handle navigation, we can force a prefetch
navigation.

The slight compromise with this approach is that you can't test
prefetching anymore in dev.


<!-- Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change(s) that you're making:

## For Contributors

### Improving Documentation

- Run `pnpm prettier-fix` to fix formatting issues before opening the
PR.
- Read the Docs Contribution Guide to ensure your contribution follows
the docs guidelines:
https://nextjs.org/docs/community/contribution-guide

### Adding or Updating Examples

- The "examples guidelines" are followed from our contributing doc
https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md
- Make sure the linting passes by running `pnpm build && pnpm lint`. See
https://github.com/vercel/next.js/blob/canary/contributing/repository/linting.md

### Fixing a bug

- Related issues linked using `fixes #number`
- Tests added. See:
https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md

### Adding a feature

- Implements an existing feature request or RFC. Make sure the feature
request has been accepted for implementation before opening a PR. (A
discussion must be opened, see
https://github.com/vercel/next.js/discussions/new?category=ideas)
- Related issues/discussions are linked using `fixes #number`
- e2e tests added
(https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Documentation added
- Telemetry added. In case of a feature if it's used or not.
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md


## For Maintainers

- Minimal description (aim for explaining to someone not on the team to
understand the PR)
- When linking to a Slack thread, you might want to share details of the
conclusion
- Link both the Linear (Fixes NEXT-xxx) and the GitHub issues
- Add review comments if necessary to explain to the reviewer the logic
behind a change

### What?

### Why?

### How?

Closes NEXT-
Fixes #

-->

link NEXT-1317

---
## [Aratimaru/VectorDiagram](https://github.com/Aratimaru/VectorDiagram)@[b896737a91...](https://github.com/Aratimaru/VectorDiagram/commit/b896737a91c8327f22dd799d51cf05f1a8cad1f0)
#### Monday 2023-08-28 19:16:40 by Aratimaru

fucking holy shit, but not the code. Debugging is needed

---
## [mamehaze/mame](https://github.com/mamehaze/mame)@[dbb0909cba...](https://github.com/mamehaze/mame/commit/dbb0909cbab3f2094088a42687894e0e6053986b)
#### Monday 2023-08-28 19:26:17 by wilbertpol

msx1_flop.xml: Added 105 working items, and replaced one item. (#11511)

* Replaced Konami Game Collection 3: Shooting Series (Japan) with a better dump. [file-hunter]

New working software list items (msx1_flop.xml)
-------------------------------
10 Programas Serie Oro (Spain) [file-hunter]
20 Programas Serie Oro (Spain) [file-hunter]
747 400b Flight Simulator (Europe, cracked) [file-hunter]
Alfabet en Deelsom (Netherlands) [file-hunter]
Alien Panic (Spain) [file-hunter]
Andon (Japan, hacked) [file-hunter]
Duad-MSX (Japan) [file-hunter]
Engels + Procenten (Netherlands) [file-hunter]
Fracta (Brazil) [file-hunter]
Graphos III (Brazil) [file-hunter]
Gruta de Maquine (Brazil)
The Iron Gauntz (Japan, prototype) [file-hunter]
Konami Game Collection 1: Action Series (Japan, alt) [file-hunter]
Konami Game Collection 4: Sports Series 2 (Japan, alt) [file-hunter]
Lettergrijper + Geld (Netherlands) [file-hunter]
Manuscript (United Kingdom) [file-hunter]
MSX Compilation 5 (Netherlands) [file-hunter]
MSX PageMaker DeLuxe (Brazil) [file-hunter]
Music Creator (Netherlands) [file-hunter]
Professional Data Retrieve (Brazil) [file-hunter]
Professional Paint (Brazil) [file-hunter]
Professional Publisher (Brazil, cracked) [file-hunter]
Rekenen tot 20 + Optellen en aftrekken tot 100 + Taalbedrijf (Netherlands) [file-hunter]
SF Zone 1999 (Japan) [file-hunter]
Simulador Profesional de Tenis (Spain) [file-hunter]
Super Procole (Japan) [file-hunter]
Super Procole 2 (Japan) [file-hunter]
Super Procole 3 (Japan) [file-hunter]
Supersellers 1 (Netherlands) [file-hunter]
Twin Hammer (Korea) [file-hunter]
The Wood (Spain) [file-hunter]
Woordmaker en Cijferend Vermenigvuldigen (Netherlands) [file-hunter]
Word Plus (Brazil) [file-hunter]
Wordstore+ (Netherlands) [file-hunter]
Zen (United Kingdom) [file-hunter]
3D Maze [Chalky]
666 - Uma Aventura Macabra [file-hunter]
8192 Story Tower [NAGI-P SOFT]
Baruko [file-hunter]
Blinky's Scary School [file-hunter]
Bounce Mania [MSXdev]
Burner Burst [file-hunter]
Buster Mystery [file-hunter]
City (Japan) [file-hunter]
Defence (v1.3) [MSXdev]
Galaxy Zone [aburi6800]
Ghosts'n Goblins (v1.1.0) [file-hunter]
Hibernated 1 - This Place is Death [file-hunter]
Hibernated 1 - Eight Feet Under [file-hunter]
JUMPER [NAGI-P SOFT]
Kame Graphics [file-hunter]
Kill Mice [MSXdev]
Las Aventuras de Rudolphine Rur (Spanish) [Dwalin]
Las Aventuras de Rudolphine Rur (Spanish, xmessage) [Dwalin]
Last War [NAGI-P SOFT]
Last War II [NAGI-P SOFT]
Logic (Russia) [file-hunter]
Mars [NAGI-P SOFT]
Mars II [NAGI-P SOFT]
May The Force Be With You [Cobinee]
Maze Chase [JLTurSan]
Micro Rocketz [MSXdev]
Mood Land [file-hunter]
Muhonmourn 3 (v1.1) [MSXdev]
Muhonmourn 3 (v1.1, with Ninja Tap support) [file-hunter]
Muhonmourn 3 (v1.0) [file-hunter]
Nibbles [file-hunter]
Oceano [file-hunter]
Paint-it (rev2) [file-hunter]
Paint-it (rev1) [file-hunter]
Paint-it [file-hunter]
Palhada City (Brazil) [file-hunter]
Penguin Catcher (v1.1) [MSXdev]
Penguin Catcher (v1.0) [file-hunter]
Pyramid Quest [Crappysoft]
Raftoid [PlattySoft]
Roger Dice (Spain) [oniric-factor]
Search for Mum (Netherlands) [file-hunter]
Sim City [file-hunter]
Storm Rescue [Concurso MSX-BASIC]
Stripgirl [file-hunter]
SubCommander (v1.02) [MSXdev]
SubCommander (older) [file-hunter]
Super Adventure [file-hunter]
The Tower of Gold [MSXdev]
UZIX (v1.0.0) [UZIX]
Wash Man (v2.8) [MSXdev]
Wash Man (v1.9) [file-hunter]
Wash Man (v1.5) [file-hunter]
Wash Man (v1.3) [file-hunter]
Wash Man (v1.2) [file-hunter]
Wash Man (v1.1) [file-hunter]
Wash Man (v1.0) [file-hunter]
Wired Shooting [Cobinee]
MSXMAS Demo [file-hunter]
Xadrama [file-hunter]
Xarchon [file-hunter]
XOR [Chalky]
XOR (older) [file-hunter]
Yellow Submarin [file-hunter]
Yobai [file-hunter]
Zero Gravity [file-hunter]
The zoBITRONics Inc [Hannu Töyrylä]
Zone TNT [MSXdev]
La Abadia del Crimen (Spain, alt) [file-hunter]

---
## [bsdjhb/gdb](https://github.com/bsdjhb/gdb)@[05e1cac249...](https://github.com/bsdjhb/gdb/commit/05e1cac2496f842f70744dc5210fb3072ef32f3a)
#### Monday 2023-08-28 19:52:39 by Andrew Burgess

gdb: fix vfork regressions when target-non-stop is off

It was pointed out on the mailing list[1] that after this commit:

  commit b1e0126ec56e099d753c20e91a9f8623aabd6b46
  Date:   Wed Jun 21 14:18:54 2023 +0100

      gdb: don't resume vfork parent while child is still running

the test gdb.base/vfork-follow-parent.exp now has some failures when
run with the native-gdbserver or native-extended-gdbserver boards:

  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to end of inferior 2 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: inferior 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: print unblock_parent = 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to break_parent (timeout)

The reason that these failures don't show up when run on the standard
unix board is that the test is only run in the default operating mode,
so for Linux this will be all-stop on top of non-stop.

If we adjust the test script so that it runs in the default mode and
with target-non-stop turned off, then we see the same failures on the
unix board.  This commit includes this change.

The way that the test is written means that it is not (currently)
possible to turn on non-stop mode and have the test still work, so
this commit does not do that.

I have also updated the test script so that the vfork child performs
an exec as well as the current exit.  Exec and exit are the two ways
in which a vfork child can release the vfork parent, so testing both
of these cases is useful I think.

In this test the inferior performs a vfork and the vfork-child
immediately exits.  The vfork-parent will wait for the vfork-child and
then blocks waiting for gdb.  Once gdb has released the vfork-parent,
the vfork-parent also exits.

In the test that fails, GDB sets 'detach-on-fork off' and then runs to
the vfork.  At this point the test tries to just "continue", but this
fails as the vfork-parent is still selected, and the parent can't
continue until the vfork-child completes.  As the vfork-child is
stopped by GDB the parent will never stop once resumed, so GDB refuses
to resume it.

The test script then sets 'schedule-multiple on' and once again
continues.  This time GDB, in theory, resumes both the parent and the
child, the parent will be held blocked by the kernel, but the child
will run until it exits, and which point GDB stops again, this time
with inferior 2, the newly exited vfork-child, selected.

What happens after this in the test script is irrelevant as far as
this failure is concerned.

To understand why the test started failing we should consider the
behaviour of four different cases:

  1. All-stop-on-non-stop before commit b1e0126ec56e,

  2. All-stop-on-non-stop after commit b1e0126ec56e,

  3. All-stop-on-all-stop before commit b1e0126ec56e, and

  4. All-stop-on-all-stop after commit b1e0126ec56e.

Only case #4 is failing after commit b1e0126ec56e, but I think the
other cases are interesting because, (a) they inform how we might fix
the regression, and (b) it turns out the behaviour of #2 changed too
with the commit, but the change was harmless.

For #1 All-stop-on-non-stop before commit b1e0126ec56e, what happens
is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-non-stop, every thread is resumed
    individually, so GDB tries to resume both the vfork-parent and the
    vfork-child, both of which succeed,

  3. The vfork-parent is held stopped by the kernel,

  4. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  5. At this point we might take two paths depending on which event
     GDB handles first, if GDB handles the VFORK_DONE first then:

     (a) As GDB is controlling both parent and child the VFORK_DONE is
         ignored (see handle_vfork_done), the vfork-parent will be
	 resumed,

     (b) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     Alternatively, if GDB selects the EXITED event first then:

     (c) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     (d) At some future time the user resumes the vfork-parent, at
         which point the VFORK_DONE is reported to GDB, however, GDB
	 is ignoring the VFORK_DONE (see handle_vfork_done), so the
	 parent is resumed.

For case #2, all-stop-on-non-stop after commit b1e0126ec56e, the
important difference is in step (2) above, now, instead of resuming
both the vfork-parent and the vfork-child, only the vfork-child is
resumed.  As such, when we get to step (5), only a single event, the
EXITED event is reported.

GDB handles the EXITED just as in (5)(c), then, later, when the user
resumes the vfork-parent, the VFORKED_DONE is immediately delivered
from the kernel, but this is ignored just as in (5)(d), and so,
though the pattern of when the vfork-parent is resumed changes, the
overall pattern of which events are reported and when, doesn't
actually change.  In fact, by not resuming the vfork-parent, the order
of events (in this test) is now deterministic, which (maybe?) is a
good thing.

If we now consider case #3, all-stop-on-all-stop before commit
b1e0126ec56e, then what happens is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-all-stop, the resume is passed down to the
     linux-nat target, the vfork-parent is the event thread, while the
     vfork-child is a sibling of the event thread,

  3. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this causes the vfork-child to be resumed.  Then
     in linux_nat_target::resume, the event thread, the vfork-parent,
     is also resumed.

  4. The vfork-parent is held stopped by the kernel,

  5. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  6. We are now in a situation identical to step (5) as for
     all-stop-on-non-stop above, GDB selects one of the events to
     handle, and whichever we select the user sees the correct
     behaviour.

And so, finally, we can consider #4, all-stop-on-all-stop after commit
b1e0126ec56e, this is the case that started failing.

We start out just like above, in proceed, the resume_ptid is
-1 (resume everything), due to schedule multiple being on.  And just
like above, due to the target being all-stop, we call
proceed_resume_thread_checked just once, for the current thread,
which, remember, is the vfork-parent thread.

The change in commit b1e0126ec56e was to avoid resuming a vfork-parent
thread, read the commit message for the justification for this change.

However, this means that GDB now rejects resuming the vfork-parent in
this case, which means that nothing gets resumed!  Obviously, if
nothing resumes, then nothing will ever stop, and so GDB appears to
hang.

I considered a couple of solutions which, in the end, I didn't go
with, these were:

  1. Move the vfork-parent check out of proceed_resume_thread_checked,
     and place it in proceed, but only on the all-stop-on-non-stop
     path, this should still address the issue seen in b1e0126ec56e,
     but would avoid the issue seen here.  I rejected this just
     because it didn't feel great to split the checks that exist in
     proceed_resume_thread_checked like this,

  2. Extend the condition in proceed_resume_thread_checked by adding a
     target_is_non_stop_p check.  This would have the same effect as
     idea 1, but leaves all the checks in the same place, which I
     think would be better, but this still just didn't feel right to
     me, and so,

What I noticed was that for the all-stop-on-non-stop, after commit
b1e0126ec56e, we only resumed the vfork-child, and this seems fine.
The vfork-parent isn't going to run anyway (the kernel will hold it
back), so if feels like we there's no harm in just waiting for the
child to complete, and then resuming the parent.

So then I started looking at follow_fork, which is called from the top
of proceed.  This function already has the task of switching between
the parent and child based on which the user wishes to follow.  So, I
wondered, could we use this to switch to the vfork-child in the case
that we are attached to both?

Turns out this is pretty simple to do.

Having done that, now the process is for all-stop-on-all-stop after
commit b1e0126ec56e, and with this new fix is:

  1. GDB calls proceed with the vfork-parent selected, but,

  2. In follow_fork, and follow_fork_inferior, GDB switches the
     selected thread to be that of the vfork-child,

  3. Back in proceed user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid still, but now,

  4. When GDB calls proceed_resume_thread_checked, the vfork-child is
     the current selected thread, this is not a vfork-parent, and so
     GDB allows the proceed to continue to the linux-nat target,

  5. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this does not resume the vfork-parent (because
     it is a vfork-parent), and then the vfork-child is resumed as
     this is the event thread,

At this point we are back in the same situation as for
all-stop-on-non-stop after commit b1e0126ec56e, that is, the
vfork-child is resumed, while the vfork-parent is held stopped by
GDB.

Eventually the vfork-child will exit or exec, at which point the
vfork-parent will be resumed.

[1] https://inbox.sourceware.org/gdb-patches/3e1e1db0-13d9-dd32-b4bb-051149ae6e76@simark.ca/

---
## [wardbell/angular](https://github.com/wardbell/angular)@[8eac30b54a...](https://github.com/wardbell/angular/commit/8eac30b54a3fac9ad4e85d769cdabbbefb45d3ae)
#### Monday 2023-08-28 21:05:18 by Ward Bell

docs: Migrate Observables guides & code examples to standalone

None of the guide pages mentions ngModules. Only `observables-in-angular` needed conversion to Standalone.

However, some of the guide pages reflect old versions of RxJS, including signatures that are no longer valid. These have been corrected.

More significantly, *the existing guide is pretty bad at explaining RxJS and its usage*. It was written (by me I think) in the very early days of Angular and Angular RxJS instruction. I've taught numerous "RxJS in Angular" classes since and learned from that experience what does and does not work with students.

There was neither the time nor the charter to completely overhaul this guide. But this commit attempts to remove what flops with students and to bring the teaching closer to what seems more effectively. I hope reviewers agree that my revisions are an improvement.

**Revised Overview**

The overview doc, `observables.md`, had a few errors (ex: `next` is NOT REQUIRED) and deprecated patterns (you now must pass the Observer object to `subscribe`).

More importantly, it was wildly overcomplicated and scary, especially when it got into multi-casting.

Moved the multi-casting section to  "RxJS Library" and rewrote it (with working example) for simplicity and context.

I made other changes in an effort to make this an overview that is  more comprehensive and more clear. I paid particular attention to the "Basic usage and terms" section.

Finally, I relocated the "Naming conventions for observables" section here from `rx-library`. This is the section that describes the dollar-sign convention. It made more sense for it to be here.

**Revised "RxJS Library" page and code**

*RxJS no longer supports chaining* and hasn't for a very long time. Removed note in `rx-library.md` that suggested you could use operator chaining.

The RxJS `pipe` discussion in the "Operators" section was just weird. Almost no one calls the `pipe` function. We certainly should *start* there. We should start with how people actually use operators - by adding them to the argument list of the `Observable.pipe()` method.

I kept the original `pipe` function example but subordinated it in a "callout". Most readers will (and should) ignore it.

`Subject` is a *critically important RxJS mechanism for creating custom observables*. It was completely missing from the list of observable creators on this guide page. So I added it to the "Observable creation functions" section of the guide and wrote an accompanying `MessageService` code sample (see the new `rx-library/app/` folder).

The `MessageService` is a pretty common pattern in Angular apps - far more common than creating an observable from a counter or an event, two of the creation patterns currently on this page.

This new section also afforded an opportunity to show how RxJS helps with building loosely coupled applications. We will soon be talking about Signals. Many will wonder whether and when they should still use RxJS.

At least a partial answer is that RxJS is really good at progressively combining and enhancing streams of data as they cross component boundaries. Of course you can pass signals around; but they are not as rich in transformers as RxJS. This is where RxJS shines.

**Revised "Comparing observables"**

The Promises section in `comparing-observables.md` had many errors and misleading remarks.

The comparison of error handling was especially egregious; the code example for that was nonsense.

The "Chain" sub-section was really about transforming values. It also failed to demonstrate chaining promise `.then`s.

Reworked these sub-sections and improved the code samples to match.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ba87c6e4cd...](https://github.com/treckstar/yolo-octo-hipster/commit/ba87c6e4cd2e835c833552951a3776331f7e28af)
#### Monday 2023-08-28 21:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Kubisopplay/tgstation](https://github.com/Kubisopplay/tgstation)@[1e27ce031b...](https://github.com/Kubisopplay/tgstation/commit/1e27ce031ba94161c64edcc87e5f3aaad778d3fe)
#### Monday 2023-08-28 22:07:46 by carlarctg

Syndicate Duffelbag Rerework (#77060)

## About The Pull Request

Syndicate duffelbags can fit 2 extra bulky items, down from three.

Reduced syndicate duffelbag's unzipped slowdown from '1' to '0.3', and
set its zipping-up sped to 0.5, same as unzipping.

Added the following items to the Syndicate Duffelbag bulky exception
list: Greentext, mech removal tool, gibtonite, skub, golem shells, mech
ammo. Roughly sorted the list by item category.

Fixed the syndie surgery duffelbag having more items than it can hold by
removing the redundant surgical drill (Upgraded cauteries can turn into
one anyways)

Any storage item with a can_hold description can be examined twice to
see what it can hold now.

## Why It's Good For The Game

> Syndicate duffelbags can fit 2 extra bulky items, down from three.

> Reduced syndicate duffelbag's unzipped slowdown from '1' to '0.3', and
set its zipping-up sped to 0.5, same as unzipping.

For most intents and purposes, it seems the syndicate duffelbag has gone
from 'bland upgrade to backpack', to 'useless'. This is especially made
apparent because it isn't exactly shown to the player that these
duffelbags can carry bulky items (I didn't even know about it until I
was making this PR!)

The extra bulky item hold concept is great, but I have my issues with
the item as-is that I seek to fix with this PR. There are TONS of issues
with being unable to access your bag quickly, which is twice as relevant
when your bag is an incredibly conspicious traitor item. Sure, you can
have it in your hand, but then why even have it in the first place?

That's why I want to reduce the slowdown significantly. '1' slowdowns
are thrown around the whole game like they're reasonable (galoshes,
water back-tanks, biosuits) - they aren't. '1' slowdown is CRIPPLING. It
makes you frustratingly slow and effectively destroys any combat
maneuvering you can do. This is very relevant for a traitorious item.

The zip speed helps one use the duffelbag as a storage item dynamically,
letting the item be an actual trade-off rather than mostly a downside.
Gives you a reason to use it rather than just buying a smuggler satchel
for more storage.

Of course these are some hefty buffs, so I lowered the bulky storage to
make up for it. I can bring it back up to 3 if wanted.

> Added the following items to the Syndicate Duffelbag bulky exception
list: Greentext, mech removal tool, gibtonite, skub, golem shells, mech
ammo. Roughly sorted the list by item category.

Some traitorious items that felt like they should be allowed in.
Honestly, I think this shouldn't even be an exception hold except for
blacklisting clearly bonkers things like backpacks, but whatevs.

> Any storage item with a can_hold description can be examined twice to
see what it can hold now.

Generalization is awesome. Hardcoding is cringe!

## Changelog

:cl:
balance: Syndicate duffelbags can fit 2 extra bulky items, down from
three.
balance: Reduced syndicate duffelbag's unzipped slowdown from '1' to
'0.3', and set its zipping-up sped to 0.5, same as unzipping.
add: Added the following items to the Syndicate Duffelbag bulky
exception list: Greentext, mech removal tool, gibtonite, skub, golem
shells, mech ammo. Roughly sorted the list by item category.
fix: Fixed the syndie surgery duffelbag having more items than it can
hold by removing the redundant surgical drill (Upgraded cauteries can
turn into one anyways)
qol: Any storage item with a can_hold description can be examined twice
to see what it can hold now.
fix: The parent crayon's name is 'crayon' to prevent any weirdness with
things that show the parent type's name.
/:cl:

---
## [Azlier/Skyrat-tg](https://github.com/Azlier/Skyrat-tg)@[62ab5e77f4...](https://github.com/Azlier/Skyrat-tg/commit/62ab5e77f44af5f0c118038233e138b85fe4906b)
#### Monday 2023-08-28 22:22:20 by SkyratBot

[MIRROR] Refactors Slaughter/Laughter Demons into Basic Mobs [MDB IGNORE] (#22801)

* Refactors Slaughter/Laughter Demons into Basic Mobs (#77206)

## About The Pull Request

On the tin, the former "imp" is now refactored into basic mob code. Very
simple since these are only meant to be controlled by players, and all
of their stuff was on Signal Handlers and Cooldown Actions anyways. Just
lessens the amount of stupidity.

Did you know that we were trying to make demons spawn in a `pop`'d cat
named "Laughter"? Embedded in the list? I've literally never seen this
cat, so I'm under heavy suspicion that the code we were using was broken
for the longest time (or may have never worked), and we now instead just
do it a much more sane way of having a cat spawn on our demise.

## Why It's Good For The Game

Cleaner code! Less simple mob jank to deal with. Trims down the list of
simple animals to refactor. No more duplicated code that we were already
doing on parent! It's so good man literally everything was seamless with
a bit of retooling and tinkering. The typepath is also no longer `imp`,
it's actually `demon`, which I'm happy with because there's no other
demons to have it be confused with anymore.

We were also doing copypasta on both the demon spawner bottle and the
demon spawning event so I also just unified that into the mob. I also
reorganized the sprites to be a bit clearer and match their new
nomenclature

## Changelog
:cl:
refactor: Slaughter and Laughter Demons have been refactored, please
place an issue report for any unexpected things/hitches.
fix: Laughter Demons should now actually drop a kitten.
/:cl:

* Refactors Slaughter/Laughter Demons into Basic Mobs

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Azlier/Skyrat-tg](https://github.com/Azlier/Skyrat-tg)@[72b1a979ff...](https://github.com/Azlier/Skyrat-tg/commit/72b1a979ffbb4505b4e36e29f76323b010c84973)
#### Monday 2023-08-28 22:22:20 by SkyratBot

[MIRROR] Improves the RPG loot wizard event. [MDB IGNORE] (#22800)

* Improves the RPG loot wizard event. (#77218)

## About The Pull Request
As the title says. Adds a bunch more stat changes to various different
items and a somewhat simple way of modifying them whilst minimizing
side-effects as much as possible.
Added a new negative curse of polymorph suffix that can randomly
polymorph you once you pick up the item.
Curse of hunger items won't start on items that are not on a turf.
Curse of polymorph will only activate when equipped.

Bodyparts, two-handed melees, bags, guns and grenades, to name a few,
have a bunch of type-specific stat changes depending on their quality.

Some items won't gain fantasy suffixes during the RPG loot event, like
stacks, chairs and paper, to make gamifying the stats a bit harder.
I'm sure there'll still be other ways to game the event, but it's not
that big of a deal since these are the easiest ways to game it.
High level items also have a cool unusual effect aura

## Why It's Good For The Game
Makes the RPG item event cooler. Right now, it's a bit lame since
everything only gains force value and wound bonus on attack. This makes
the statistic increases more type-based and make it interesting to use

It's okay for some items to be powerful since this is a wizard event and
a very impactful one too. By making the curse of hunger items not spawn
on people, it'll also make it a less painful event too.

## Changelog
:cl:
add: Expanded the RPG loot wizard event by giving various different
items their own statistic boost.
/:cl:

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>

* Improves the RPG loot wizard event.

---------

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>

---
## [Azlier/Skyrat-tg](https://github.com/Azlier/Skyrat-tg)@[1ecd03fc58...](https://github.com/Azlier/Skyrat-tg/commit/1ecd03fc587180931e35a5485f987eb16966020b)
#### Monday 2023-08-28 22:22:20 by SkyratBot

[MIRROR] Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes [MDB IGNORE] (#22787)

* Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#77077)

## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

* Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes

---------

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [Dmeto/tgstation](https://github.com/Dmeto/tgstation)@[b390525fc5...](https://github.com/Dmeto/tgstation/commit/b390525fc5543db5fcdb47869b9297cf637239fc)
#### Monday 2023-08-28 22:56:21 by Rhials

Adds a handful of Ninja Hacking MODule interactions of varying usefulness (#77707)

## About The Pull Request

Adds a few new interactions with the Ninja's ~~right click multipurpose
trolling tool~~ Hacking MOD Module. These new effects are not tied to
objectives and are geared towards expanding the ninja's access,
disabling equipment, and giving them more ways to punk the crew.

### **Useful additions**
Ninjas can now hack open **windoors** and **elevator control panels**.
Both trigger emag_act() when hacked, opening in the case of the windoor,
and disabling the access restrictions _(and also maybe the safeties)_ in
the case of the elevator controls.

**Buttons** can also be emagged by the hacking modules, which removes
their access restrictions.

Hacking a **camera** will now EMP it, disabling it for about 90 seconds.
This can especially useful when trying to complete objectives, and works
better than smashing the cameras with your sword or lugging around
tools.

**Firelocks** can be right-click opened now too, thanks to the hacking
MODule.

**Energy guns** of all variety, useless to a ninja since they can't use
ranged weapons, can now be drained and used to charge your suit. This
takes a brief do_after to complete, so pulling it off mid-combat may be
as risky as it is stylish.

### **Being a nuisance**

**Vendors** can be hacked, expending some charge to trigger the "throw"
wire, making it launch inventory at anyone who passes by.

You can now hack **simplebots**, expending some charge from your suit to
overload and detonate them. It's faster than tipping, and far more
tragic. Sentient simplebots should take care when a ninja is around.

### **Sabotage opportunities**

The **recycler** can now be hacked. This takes 30 seconds and notifies
the AI, just like the communications console hack. Completing the hack
will emag it. That's it.

Hacking the **tram control console** will trigger an extended Tram
Malfunction event, and can be repeated after the event is done. This can
only be done to the "main" tram of the map, which I forsee will be an
absolute nightmare to complete on highpop tramstation.

Neither of these, presently, contribute towards any objectives. They can
be useful for diverting attention, but I see them more as ways for an
overachieving ninja to flex or continue the chaos after their objectives
are complete.

### **OH ALSO**

Hacking open doors costs energy. This really shouldn't be an issue just
remember to recharge sometimes.

The charge drains and do_after lengths for all of these were chosen on
vibes. In all honesty I think the drainage values don't _really_ matter,
due to how easy recharging is, but I had a hard time settling on how
long some of these hack do_afters should take (even if I know they
probably won't matter either).

## Why It's Good For The Game

Being able to hack open airlocks but not windoors always irked me. I
figured that they would be openable like any other door, and that losing
their status as a "-1 dash charge gate" wouldn't be a big enough balance
change to spark arguments. The same philosophy extends to buttons and
elevator controls.

Sapping power from eguns expands on the list of sources energy can be
siphoned from. You can also use it to disarm opponents (like the badass
ninja you are), take emergency charge from a recently-gored officer's
disabler, or dunk on security by draining their entire armory.

Hacking simplebots, vendors, and by extension elevator lifts (since that
also disables the safeties!) give opportunities for minor sabotage. Not
meant to be super disruptive, just a bit silly and annoying for the
crew.

The recycler/tram hacking in particular are meant to be bonus goals,
only sought out by the ballsiest (or more likely boredest) of ninjas.

I see all of these additions as expanding upon the current abilities of
the ninja (not really making them much more powerful, just expanding
their flexibility), or providing more interactions to have fun (and
antagonize the crew) with when not mainlining their objectives.
## Changelog
:cl: Rhials
add: Ninjas can now temporarily disable cameras with the Ninja MOD
right-click hacking ability.
add: Ninjas can emag windoors, elevator controls, and buttons with their
hacking ability.
add: Ninjas can drain the power from energy weaponry, adding the charge
to their MODsuit.
add: Ninjas can now hack simplebots, overloading and detonating them
after a brief delay.
add: Ninjas can now hack vendors, causing them to eject their inventory
at people.
add: Ninjas can now hack the recycler, which notifies the AI and emags
it once complete.
add: Ninjas can now trigger an extended tram malfunction by hacking the
tram control console.
add: Ninjas can now hack open firelocks (temporarily) with right-click.
balance: Hacking open doors with the Ninja Hacking MODule will subtract
a paltry amount of energy from your suit.
/:cl:

---
## [Dmeto/tgstation](https://github.com/Dmeto/tgstation)@[2d4d23dbf1...](https://github.com/Dmeto/tgstation/commit/2d4d23dbf1e2cc23ed2046534011561e443060f7)
#### Monday 2023-08-28 22:56:21 by Timberpoes

Replaces the poster and graffiti objectives with assault and early steal & destroy ones. (#77029)

## About The Pull Request

With the blessings of @Watermelon914 I am removing the two objectives
for placing posters and spraying graffiti.

These old objectives are not dead. Their items have moved to the
Badassery section of the uplink.

A box of 3 demotivational posters can be bought for 1TC with 0 rep.
The spraycan can be bought for 1TC with 0 rep.

In their place comes one new objective and one extended objective.

The new objective is Assault a Crewmember. This objective requires you
to attack the specified target 2-5 times (random on objective
generation). It tallies from any attack that filters through the
`/datum/element/relay_attackers` element and has an "attacker"
associated with it.

Although it asks you not to kill the other player, it doesn't fail if
you kill them.

I have expanded the low-risk theft objectives with items like a mime
mask, lawyer badge and a fake moustache (commonly on cooks).

Finally, I've added a very low level set of steal-and-destroy objectives
aimed at some items that will require a bit of basic breaking and
entering, and the destruction of which may hurt crew morale.

```
/datum/objective_item/steal/traitor/donut_box
/datum/objective_item/steal/traitor/rpd
/datum/objective_item/steal/traitor/space_law
/datum/objective_item/steal/traitor/granted_stamp
/datum/objective_item/steal/traitor/denied_stamp
/datum/objective_item/steal/traitor/lizard_plush
/datum/objective_item/steal/traitor/moth_plush
/datum/objective_item/steal/traitor/insuls
```

This PR also fixes clown shoes missing a proc override to allow them to
actually register as a theft objective.


![image](https://github.com/tgstation/tgstation/assets/24975989/775d46cf-f40a-43e5-9bf1-3aa4a31d436e)

![image](https://github.com/tgstation/tgstation/assets/24975989/66c77815-1f2b-4dfb-99c6-b8f2e0061654)

![image](https://github.com/tgstation/tgstation/assets/24975989/85d3878a-c598-4ec0-9bb1-920380a004c6)
## Why It's Good For The Game

Basically my discussion with Watermelon focused on the idea that the
graffiti and poster objectives weren't really crimes. They baited
antagonists into very passive play early-game.

These new replacements encourage a more antagonistic playstyle. Starting
fights plus B&E are two bread-and-butter play paradigms for antaggery.

Giving a few early game theft + destroy options with a mix of impactful
items (like insuls and RPDs) versus more symbolic or emotive items
(plushies, donut boxes, Cargonia stamps) gets antagonists out and about
in the station, warming themselves up.

And having an objective to assault players (even if you don't kill them)
allows cheeky antags with a penchant for shittery to start fights with
players and start genuinely impacting the shift, involving sec and
drawing players into their antaggery.

Both of these natually ease players into the more substantive theft and
murder objectives.

The existing spray and posters are actually thematically super cool.
Traitors now have even more access to them since they can be bought for
1TC per spraycan/3-pack of posters. This lets antags with TC to spare
run gimmicks around them and adds extra fun to the Badassery section.
## Changelog
:cl:
del: Traitor objectives to place posters and graffiti the station have
been removed.
add: The items associated with the poster and graffiti objectives can
now be purchased from the Badassery section of the uplink. The posters
come in a box of 3 for 1TC, and the spraycans are 1TC each.
add: Adds a new Assault traitor objective, requiring you to the attack
the target a few times without needing to kill them. Earn TC and
reputation by starting barroom fights and bait players into escalation
battles for fun and profit.
add: Expands low-risk steal objectives to include the Chef's fake
moustache, Lawyer's badge, and Mime's mask.
add: Adds brand new shift start Steal & Destroy objectives for early
breaking and entering. Smash your way into a sec checkpoint to grab a
Space Law book, engineering to grab some insulated gloves or the psych
office to kidnap their moth plush.
fix: Fixes an issue where the steal clown shoes objective would never be
valid.
/:cl:

---
## [Dmeto/tgstation](https://github.com/Dmeto/tgstation)@[3645fa7d89...](https://github.com/Dmeto/tgstation/commit/3645fa7d8956bed2d3ebff86b072f8b9544d383d)
#### Monday 2023-08-28 22:56:21 by distributivgesetz

Replaces slime clone damage with a "Covered in Slime" status effect (#77569)

## About The Pull Request

This PR replaces clone damage dealt by slimes with a new status effect,
"Covered in Slime".

The status effect is applied when you wrestle a slime off. The status
effect has a chance of not applying if your biohazard protection on your
head and chest is good enough.

It deals brute damage over time and gets removed when you stand under
the shower for about 10 seconds or when you are about to enter softcrit.

As a direct consequence of adding this feature I added showers to the
North Star and Birdshot Xenobiology Labs. I'm sorry, I'm sure you wanted
to make a statement with this, but we kind of require them in there now.

## Why It's Good For The Game

One source of clone damage eliminated whilst hopefully keeping a
"unique" interaction when dealing with slimes. No other source of clone
damage has been touched.

Clone damage is a damage type that shouldn't exist anymore, it's a relic
left from the era of cloning and it's so specific of a damage type that
it rarely gets used as a result. It really should be a type of
affliction (wound etc) instead of its own damage counter.

However, some things in the game still depend on clone damage being
around, so those needs to be addressed first.
We start off with slimes in this PR.

This status effect either lets you either continue with your work if you
react fast enough or it forces you to medbay, giving a victim more
control over the situation, as opposed to just being dealt a rare damage
type that always forces you to go to medbay if you want it healed.

## Changelog

:cl: distributivgesetz
add: Replaced slime clone damage with a "Covered in Slime" status effect
that deals brute damage over time and can be washed off by standing
under a shower.
add: Northstar and Birdshot Xenobiology have been outfitted with a new
shower.
code: Replaced the magic strings in slime code with macros. Also
included some warnings to anyone daring to touch the macros.
/:cl:

---

