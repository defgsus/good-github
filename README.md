## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-14](docs/good-messages/2023/2023-03-14.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,521,157 were push events containing 3,747,629 commit messages that amount to 289,250,000 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 47 messages:


## [jianyuyanyu/sapling](https://github.com/jianyuyanyu/sapling)@[c2ffc8fedf...](https://github.com/jianyuyanyu/sapling/commit/c2ffc8fedf2e68823af411fa5f7ca1760c7c31ef)
#### Tuesday 2023-03-14 00:24:31 by Muir Manders

workingcopy: make FileChangeDetectorTrait parallel friendly

Summary:
I want to parallelize the work this object does, but the trait interface is serial (and synchronous):

```
pub trait FileChangeDetectorTrait {
    // Check if file size and mtime are unchanged (otherwise queue "maybe changed" result).
    fn has_changed(&mut self, ts: &mut TreeState, path: &RepoPath) -> Result<FileChangeResult>;

    // Resolve "maybe changed" files by checking contents.
    fn resolve_maybes(&self) -> Box<dyn Iterator<Item = Result<ResolvedFileChangeResult>> + Send>;
}
```

It also was a bit annoying to use because it reported results w/ two different types, so the client needed duplicate handling. The new trait allows for asynchronous processing and only returns a single kind of result:

```
// Converting to an iterator signals you are done submitting paths.
pub trait FileChangeDetectorTrait: IntoIterator<Item = Result<ResolvedFileChangeResult>> {
    fn submit(&mut self, ts: &mut TreeState, path: &RepoPath);
}
```

I converted the existing concrete implementation to the new trait. It requires the object to buffer more results, but not any file data, so it shouldn't have much of an impact memory wise.

Reviewed By: quark-zju

Differential Revision: D43626597

fbshipit-source-id: 4ffcd9b870ee8a4fba94aa3972cc4e1a299ebec5

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9d5b4907e8...](https://github.com/tgstation/tgstation/commit/9d5b4907e8d8aaecf24bfd8f6755822b494a4b55)
#### Tuesday 2023-03-14 01:29:43 by Rhials

Post-Revolutionary Fervor station trait, revolutionary bedsheets, and a megaphone (#73799)

## About The Pull Request

Upon revolution success, the chosen headrev will now also receive a
megaphone, and a "revolutionary bedsheet" repurposed from a stolen CC
bedsheet to commemorate their success. The post-revs confusion and lack
of command/security usually leads to an instantaneous, total breakdown
in cohesion. It's every man for himself -- that's no way to run a
commune! Just because the revolution has succeeded and nobody can see
your big blue "R" anymore doesn't mean you can't be a leader!


![image](https://user-images.githubusercontent.com/28870487/222981576-e62e457b-1b2d-4756-8c87-7a9093c92c2d.png)

This also adds a new revolution-themed negative station trait --
Post-Revolutionary Fervor. When present, this trait trashes the command
areas at the start of the round. This means cracked windows, broken
consoles, vendors getting knocked over, and the occasional dead
greytider.


![image](https://user-images.githubusercontent.com/28870487/222981095-14ce9336-2320-406e-b0a6-dc91cb8f9479.png)

If you start cleaning at the start of the round, you might finish right
as the next batch of revs decides to crop up.
## Why It's Good For The Game

Giving one of the headrevs a bigger voice and a cool cape (or uncool,
depending on how you view the sprite) means that there's a chance for
them to step up and try to keep the wheels on. Just remember -- Nobody
is obligated to actually listen to this person, it's just a bedsheet.

Adds a neato station trait, which probably counts as command gameplay
content.

## Changelog
:cl: Rhials
add: The headrev who receives the revolutionary banner after a win will
also receive a commemorative bedsheet and megaphone.
add: Post-Revolutionary Fervor station trait. I hope you enjoy fixing
broken computer screens.
spriteadd: A revolutionary bedsheet.
/:cl:

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[b66af64718...](https://github.com/re621/dnpcache/commit/b66af64718f3071b2cdd16fe54f0a0fcb7aa109b)
#### Tuesday 2023-03-14 01:39:24 by bitWolfy

Add 1054 artists to the DNP list.

Added: doxhun, cupsofjade, nicesweater, bluecat_friend, peshky, masuku, lunarfloral, kugi, sagejwood, sqrlyjack, maiteik, leozedi, popdroppy, mikakater, 413k_zzzz, puppyemonade, xanthewolf, joooji, nasusbot, shredded_wheat, dogsdontwipe, wonderwaffle93, gogoandyrobo, jezzlen, dourdoofus, vksuika, klotzzilla, cooperdooper, shadnaotomi, nudegote, sexygoatgod, humgeronimo, ladysophia, mrwhiskerz, cocicka, d-wop, charmerpie, yourdigimongirl, elvche, booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, einin, freaks, angellsview3, arwenscoots, royalzbed, hellfurred, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, tren, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [Segrain/cmss13](https://github.com/Segrain/cmss13)@[34daca112c...](https://github.com/Segrain/cmss13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Tuesday 2023-03-14 01:48:02 by Segrain

Fix for varediting bitflags. (#2735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

I am honestly at a loss as to what is happening here. I do not speak
HTML all too well, and at cursory reading buttons _should_ be returning
their value, which is `1`, `2` and so on. But on debugging, they
actually return their text (`Save`, `Cancel`), which does not proceed to
work with the code receiving it. Changed that code accordingly, and then
edited the values for good measure in case somebody better versed in
HTML would get a heart attack from my folly.

Also, this looks ugly to me. Which button is which flag here?

![image](https://user-images.githubusercontent.com/4447185/221438285-cdb380c2-a871-4620-be04-0b3c5027501f.png)

This, in my humble opinion, is easier to read (would actually look
better outside of local server messing fancy windows as is its wont):

![image](https://user-images.githubusercontent.com/4447185/221438302-660c5976-d0e2-44fa-a18a-9f73a229f2c4.png)
In the process, I confess, my HTML illiteracy broke a little something
again. But we are not actually _using_ `slidecolor`, so hopefully it is
not actually important.

# Explain why it's good for the game

Is fix.


# Testing Photographs and Procedure
See above.

# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
admin: Editing bitflag variables actually works now.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [rust-adventure/2048](https://github.com/rust-adventure/2048)@[a89d834ec1...](https://github.com/rust-adventure/2048/commit/a89d834ec1891f4c14bf0fc946a3ea152d59b373)
#### Tuesday 2023-03-14 02:23:50 by Christopher Biscardi

Sorting tiles with Ord

Most implementations of 2048 use a matrix to represent the locations and values of different cells. To implement board shifts they rotate the matrix and apply the same function, then rotate it back.

With the way we're using Bevy's ECS we are going to take a different approach and we'll be using simpler math.

The algorithm we'll be using will order all of the tiles from the bottom left to the top right. So if every grid location is filled with a tile, we'd get the tile at `0,0`, then `1,0`, then `2,0`, then `3,0`. After reaching the end we go up one level and the fifth tile is `1,0`, and so on.

With this arrangement of tiles, we can check the current tile and the next tile and see if they should be merged. If they're on different rows, or if their points values are different we skip forward to the next tile, otherwise we merge them.

We'll add a query for all the tile entities to the `board_shift` system. We are going to potentially mutate the `Position` and `Points` components on the tile entity depending so they need to be mutable references.

```rust
fn board_shift(
    input: Res<Input<KeyCode>>,
    mut tiles: Query<(Entity, &mut Position, &mut Points)>,
)
```

The first direction we're going to implement is `BoardShift::Left`. To start off, we'll make sure the tiles are sorted into the order we talked about earlier.

The `tiles` query is mutable, so we need to use `[iter_mut](https://docs.rs/bevy/0.10.0/bevy/ecs/prelude/struct.Query.html#method.iter_mut)` to get an iterator. After getting an iterator, we can use `[.sorted_by](https://docs.rs/itertools/0.10.5/itertools/trait.Itertools.html#method.sorted_by)` to first sort by row and then column of the grid. `.sorted_by` is from the Itertools crate.

`.sorted_by` expects an `[Ordering](https://doc.rust-lang.org/std/cmp/enum.Ordering.html)` value as the return type. `[Ordering](https://doc.rust-lang.org/std/cmp/enum.Ordering.html)` is an enum that has `Less`, `Equal`, and `Greater` variants.

`[Ord](https://doc.rust-lang.org/std/cmp/trait.Ord.html)` is a trait that can be implemented for any type. It requires implementing the `cmp` method, which compares two values of the given type. In our case, `u8` already has an `Ord` implementation, so we can use `Ord::cmp` to determine if any two `y` values in a tile's `Position` component are equal or different.

If they're equal, that means the two tiles are in the same row and we need to do the same for the `x` value. If they're not equal, we can pass the return value back to `sorted_by` because it will be an `Ordering` variant.

```rust
Some(BoardShift::Left) => {
    dbg!("left");
    let mut it =
        tiles.iter_mut().sorted_by(|a, b| {
            match Ord::cmp(&a.1.y, &b.1.y) {
                Ordering::Equal => {
                    Ord::cmp(&a.1.x, &b.1.x)
                }
                ordering => ordering,
            }
        });
}
```

While the `Ord` trait is part of Rust's prelude and is already in scope for use to use: We need to bring `Ordering` ourselves, which we can add next to the `convert::TryFrom`. You can think of this as being like destructured imports in JavaScript.

```rust
use std::{cmp::Ordering, convert::TryFrom};
```

\## Aside: Debugging

If this is confusing, you can do something to help. Add the following line after the sorting code. This will collect the iterator into a `Vec` and debug it to the console for you to look at when you hit the left arrow key. The `_` in the type signature tells Rust to "figure out what the type should be here", which it will be able to grab from our query.

```rust
dbg!(it.collect::<Vec<_>>());
```

If you have not done so already, you will also need to add a `Debug` representation to the `Points` and `Position` structs to use the above `dbg!` code.

```rust
\#[derive(Debug, Component)]
struct Points {
    value: u32,
}

\#[derive(Debug, Component)]
struct Position {
    x: u8,
    y: u8,
}
```

This prints out a tuple for each tile that matches what we asked for in the query type signature: `(Entity, &mut Position, &mut Points)`. If you run this a few times you will be able to see the tiles on the screen and compare them to the output we're getting from the sorting.

```rust
[src/main.rs:247] "left" = "left"
[src/main.rs:257] it.collect::<Vec<_>>() = [
    (
        21v0,
        Mut(
            Position {
                x: 1,
                y: 0,
            },
        ),
        Mut(
            Points {
                value: 2,
            },
        ),
    ),
    (
        19v0,
        Mut(
            Position {
                x: 0,
                y: 2,
            },
        ),
        Mut(
            Points {
                value: 2,
            },
        ),
    ),
]
```

After you're done debugging, remember to remove that `dbg!` line of code or you'll start seeing some "borrow of moved value: `it`" warnings as we continue. The derive lines can stay.

---
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[74144f2bc9...](https://github.com/Xander3359/tgstation/commit/74144f2bc9e69c9829339a1bd7ffa962e37c0cd0)
#### Tuesday 2023-03-14 02:44:19 by LemonInTheDark

Fixes some runtime spam from lazyloading/map templates (#73037)

## About The Pull Request

Ensures we don't try and rebuild loading turfs midload

Turf refs persist through destroy, so when we changeturf earlier to get
our turf reservation, we insert our space turfs into the rebuild queue,
and then end up here where we can be rebuilt randomly, midload, with
uninit'd turfs

Avoids starting atmos machine processing until init

This avoids some runtimes with null gasmixtures

There's still trouble with atmos and template loading, pipes start
processing before their pipelines exist, so we just kinda get fucked.
Need to look into this more deeply, it involves pulling this stuff off
`on_construct` and `setup_template_machinery` and throwing it in maybe
late init, which I don't really relish but will just have to do
eventually.

## Why It's Good For The Game

Reduces runtime spam

---
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[a47afd9051...](https://github.com/Xander3359/tgstation/commit/a47afd905156bcc9a070db015cec7b1d1a07c578)
#### Tuesday 2023-03-14 02:44:19 by Sol N

2 New Positive Quirks! (#72912)

## About The Pull Request

I added a few quirks to a downstream that I feel fit well with tg so
here they are.

First up is Poster Boy, a quirk that gives you three mood altering
posters, similar to the traitor objective to hang up demoralizing
posters. You spawn with a box that has one poster that will uplift the
entire crews spirits and 2 that are unique to your department. Captain
counts for security and assistants get only neutral posters. Finally,
with a crayon or spraycan, if you are any antagonist you can make your
poster into one of the ones from the traitor objective.

![dreamseeker_nRy44SL9Jb](https://user-images.githubusercontent.com/116288367/214109008-6f1b4b7c-e800-4142-be6d-926a8e975973.png)
example of quirk posters
Costs 4.


Finally, the characterful Throwing Arm quirk, which lets you throw
objects further (but not harder) and means you will never miss shots
into the disposals bin.
Costs 7.

previously i had a food subscription quirk here as well but i pulled it
out and plan to re-add it as a separate PR in march, where it will now
give you ingredients to cook a meal with occasionally.

## Why It's Good For The Game

Positive quirk variety is good and fun, I think that these positive
quirks are reasonable ones that offer unique things that the current
positive quirks do not.
Poster boy gives people a reason to run around and claim wall real
estate for their department and hopefully can build more solidarity in
departments, the hidden antag feature probably has uses but is just for
styling on people.
Throwing arm offers a fun character trait that probably can have some
slight uses and encourages the use of throwing weapons and tools more.
Also it is good to have a way to never miss the disposals bin. It's so
embarrassing.

## Changelog
:cl:
add: Poster boy and Throwing arm positive quirks.
imageadd: added posters for poster boy quirk
/:cl:

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[1cdc327a8f...](https://github.com/GoldenAlpharex/tgstation/commit/1cdc327a8f98c1592fc970a4ef1c39d685c81554)
#### Tuesday 2023-03-14 02:51:16 by Jacquerel

Station Trait: Spider Infestation (#73893)

## About The Pull Request

Hate having your cables eaten by mice? Nanotrasen have heard your
complaints and settled on a natural, _organic_, and eco-friendly
solution.

When this station trait is active, roundstart and event mouse spawns
have a chance to instead be replaced with duct spiders (both will exist,
it doesn't remove mice).
Duct spiders are largely harmless to humans, actively hunt other
maintenance creatures (such as mice), and have only one _tiny_ downside.

![image](https://user-images.githubusercontent.com/7483112/224345781-2627be98-67f2-4cab-ac40-c6c9b35ea909.png)

These mobs can also sometimes be spawned by a minor scrubber clog event.

As a side note, all spider basic mobs with AI (except Araneus) will now
try to automatically fill a small area around them with webs.

Also I made it so that mobs will ignore their random_walking behaviour
if they're engaged in a `do_after`, just in case.

## Why It's Good For The Game

Adds a little bit of variety to things which can slightly annoy you in
maintenance.
Spiders will automatically make places they live in look like spiders
live there.

## Changelog

:cl:
add: A station trait which sometimes populates maintenance with small
spiders. You can wear them as a hat if you wanted to have a spider on
your head for some reason.
add: Spider mobs will automatically start webbing up their environment.
/:cl:

---
## [hokaze/Orcus-Compendium](https://github.com/hokaze/Orcus-Compendium)@[2f5969bb01...](https://github.com/hokaze/Orcus-Compendium/commit/2f5969bb0168c66efa27023374f2658489221544)
#### Tuesday 2023-03-14 03:24:20 by hokaze

- version bump to v0.05!
- ...and I actually remembered to update the visible version number on the webpage for once <_<;

- fixed issue where the reminder about Priests getting an extra class discipline from their "Worships the [X]" Kit also appeared as a dropdown suggestion for the Class Discipline search

- fixed some Kits showing empty Requirements instead of "None" (Bind Familiar, Brews Poisons, Channels Godmind, Charms Animals and Conjures Fiends)

- added support for search dropdowns to Arts (was formerly only on Classes) and refactored how the datalists are populated to make implementing on other tables (or adding new search fields) slightly faster/easer

- changed variable and function names in the js to be more consistent (now using snake_case for most vars and camelCase for methods, which I don't think is the standard for js, but it's still better than the previous mess of using both for both x_x)

- fixed regression where the prev/next buttons on class show info were broken (because they weren't using the new enable_navigation flag that had been added to prevent the buttons showing on Tradition.html and Role.html)

- moved some vars to misc.js rather than repeatedly declaring vars with the same name to refer to the same document elements over and over (yes global variables are bad practice, but I cba to make this project follow OO principles right now or constantly rewrite them in functions and a lot of vars were global due to being outside function scope anyway)

- minor refactor of showing + removing modal show info navigation buttons and moved to misc.js as in theory nothing there is specific to Classes and shouldn't need more than some minor changes to work on other tables...or at least the ones that just open a html file, the ones that do display via json instead can't use this as a drop-in quite yet
(main change is you have to pass in the equivalent of class_name_list, the key, the "class_" prefix used as the tr id, the table and the name of the "show[X]Info" method to use...but in time I'm hoping the showinfo method can also be made generic rather than tailored per table?)

- added the modal nav to kits to prove that worked for more than just classes
(and in the process spotted + fixed a bug with it that would have been a major headache otherwise - the class version had be written with a special case that decremented the prev/next keys by 1, as the class keys start at 1 instead of 0, and thus had to -1 to be used as the class_name_list index, but the other json files usually start at key = 0. This itself is due to how csv_to_json uses the index of the csv as the key, starting after the header, but classes.csv starts with a dummy "aaaaaa" entry from the xslx. So the actual long-term fix was to just remove the special case -1 to the key to grab the index, and modify csv_to_json.py so it uses the number of lines actually saved to the json as the key, instead of the csv index. But then we still run into the issue of using a key on the index, as we skip some classes like warrior in the class.json parsing that'd potentially induce an offset, so we ALSO change it to access the class/item name of the next html file by referencing the actual json data with the prev_key and next_key instead of using it as an array index! Phew!)
(note 2 on this: this still needs further refactoring as I think the way it checks for next/prev table row can be optimised? and I think we might be able to just use item_data instead of needing name_list? TODO in future I guess, will likely be needed to make lookup when in the middle of the powers table usable without hanging the browser? Or not, seems to be usable so far, even when picking powers near the end of the table or with search terms that muddle about the key jumps, no noticable lag yet, unlike searching)

- actually, scratch what past me said about needing some work to make nav buttons work on all the tabs, I can make showModalNavigation work for the non-html showInfo tables, just needed a slight rewrite to how the html-using showInfo methods work so they grab the name.html from the key, which now means all showInfo methods use the same key + enable_navigation args instead of some needing name (for name.html) + key + enable_navigation
- confirmed working on both html and json based showInfo methods...
- ...thus, I have added prev/next buttons to ALL current tabs/tables EXCEPT Species: Classes, Powers, Cruxes, Heritages, Kits and Arts
(species is excluded just because it doesn't actually have a html showInfo display yet)

- heckin' chonker of a commit

- TODO next, probably: finish setting up datalist dropdowns, currently only Classes and Arts have them

---
## [OpenViva/OpenViva-UE5](https://github.com/OpenViva/OpenViva-UE5)@[297bf8d0c9...](https://github.com/OpenViva/OpenViva-UE5/commit/297bf8d0c9d5bc787b2f12e3b8ad1249b491bf0c)
#### Tuesday 2023-03-14 04:11:34 by SolidStonee

lamp system that hurts my fucking head

god unreal is so annoying sometimes

---
## [khevy/fulpnation](https://github.com/khevy/fulpnation)@[fc5620aa13...](https://github.com/khevy/fulpnation/commit/fc5620aa13b120224a0b353c455d14d240ab2c24)
#### Tuesday 2023-03-14 04:16:02 by John Willard

Removes punch holopara type (#918)

* Removes punch holopara type

The punch holoparasite was repathed to standard, it was there the whole time what the HELL

* Update bloodsucker_guardian.dm

* fix to guardians

* Update bloodsucker_guardian.dm

* fuck you

* Update bloodsucker_guardian.dm

---
## [dibarbet/omnisharp-roslyn](https://github.com/dibarbet/omnisharp-roslyn)@[efeafeca33...](https://github.com/dibarbet/omnisharp-roslyn/commit/efeafeca33abe1d19659ed8c7ebab1d7c3481188)
#### Tuesday 2023-03-14 05:59:56 by Fredric Silberberg

Host dependency cleanup

Today, we delete a a few dlls in the cake packaging scripts, to remove DLLs that should come from the runtime we're loaded with, rather than the dlls we built with. This is fine for packaging, but is annoying when doing local tests by just rebuilding the relevant driver, because you have to remember to go into the output directly and delete them every time. I addressed this by removing the dlls in msbuild itself:

* System.Configuration.ConfigurationManager: this was a transitive dependency through Microsoft.CodeAnalysis.Features -> Microsoft.CodeAnalysis.Elfie. We don't need Elfie or its dependencies, so I made all references to these layers explicit and turned off flowing of transitive dependencies. This does cause a slight issue: one of those transitive dependencies is System.Text.Json 6.0, while OmniSharp.MSBuild transitively references 5.0. To ensure the appropriate binding redirects are still generated, I added an explicit reference to System.Text.Json, but we are not using that reference for anything else.
* Nuget.*.dll: these are real dependencies that we should not ship in .NET 6+. I added a target to remove that version from the list of files to be copied.

---
## [sailfishos/docs.sailfishos.org](https://github.com/sailfishos/docs.sailfishos.org)@[8ce5a53a3d...](https://github.com/sailfishos/docs.sailfishos.org/commit/8ce5a53a3d6d7bd9de98da6a22e5a0f7d672d163)
#### Tuesday 2023-03-14 07:13:28 by Matt Wang

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

I've introduced several new disabled rules. Let me quickly explain what's going on; there are two categories of rules I've disabled:

1. rules that were temporary disables; they were frequent enough that I couldn't manually resolve them, but should be simple. **I plan on opening issues to re-enable each of these rules**, just after this PR
    - `declaration-block-no-redundant-longhand-properties`: this is just tedious and error-prone
    - `no-descending-specificity`: this one is tricky since it could have impacts on the cascade (though that seems unlikely)
    - `scss/no-global-function-names`: I think we need to [import map and then use `map.get`](https://stackoverflow.com/questions/64210390/sass-map-get-doesnt-work-map-get-does-what-gives), but I'll leave this as out of scope for now
2. rules that are long-term disables; due to the SASS-based nature of our theme, I think we'll keep these in limbo
    - `alpha-value-notation` causes problems with SASS using the `modern` syntax - literals like `50%` are not properly interpolated, and they cause formatting issues on the site
    - `color-function-notation` also causes problems with SASS, but in this case the `modern` syntax breaks SASS compilation; we're not alone (see this [SO post](https://stackoverflow.com/questions/71805735/error-function-rgb-is-missing-argument-green-in-sass)).

In addition, we have many inline `stylelint-disable` comments. I'd open a separate issue to audit them, especially since I think some disables are unnecessary.

**note: there hasn't been much other discussion, so I'm going to remove primer's stylelint config.**

If I do add `@primer/stylelint-config`, I get *a ton* of errors about now using `@primer`'s in-built SCSS variables. I imagine that we probably won't want to use these presets (though I could be wrong). In that case, I think we could either:

1. disable all of those rules
4. not use `@primer/stylelint-config`, since we're not actually using primer, and shift back to the standard SCSS config provided by Stylelint

~~Any thoughts here? I also don't have the original context as to why we do use the primer rules, perhaps @pmarsceill can chime in?~~

---
## [brisvag/napari](https://github.com/brisvag/napari)@[3ec4be1ae8...](https://github.com/brisvag/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Tuesday 2023-03-14 08:29:26 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [adam8157/gpdb](https://github.com/adam8157/gpdb)@[1f5ef5ae08...](https://github.com/adam8157/gpdb/commit/1f5ef5ae0806cb75bb0297e46e41765ffa426252)
#### Tuesday 2023-03-14 08:55:51 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [code-af/Python_beginner_projects](https://github.com/code-af/Python_beginner_projects)@[612c248c64...](https://github.com/code-af/Python_beginner_projects/commit/612c248c649f1a73f389adaae0dc8545f4c51974)
#### Tuesday 2023-03-14 09:10:43 by code-af

Add files via upload

this is a simple beginner friendly project for rock paper scissors game in short 'rps', which I have created in my GitHub code space so I thought about sharing it here, though I have created it from scratch I can't say I haven't took any inspirations at all , of course I did and which in turn has helped me create my own version in an efficient way as per my capabilities being a beginner in python, Hope you enjoy and please pardon me if you find the #comments are annoying its just something I made for helping others to understand the code, Thank you.

---
## [initinll-forks/nushell](https://github.com/initinll-forks/nushell)@[2e01bf9cba...](https://github.com/initinll-forks/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Tuesday 2023-03-14 09:15:11 by Bob Hyman

add `dirs` command to std lib (#8368)

# Description

Prototype replacement for `enter`, `n`, `p`, `exit` built-ins
implemented as scripts in standard library.
MVP-level capabilities (rough hack), for feedback please. Not intended
to merge and ship as is.

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes
New command in standard library

```nushell
〉use ~/src/rust/nushell/crates/nu-utils/standard_library/dirs.nu
---------------------------------------------- /home/bobhy ----------------------------------------------
〉help dirs
module dirs.nu -- maintain list of remembered directories + navigate them

todo:
* expand relative to absolute paths (or relative to some prefix?)
* what if user does `cd` by hand?

Module: dirs

Exported commands:
  add (dirs add), drop, next (dirs next), prev (dirs prev), show (dirs show)

This module exports environment.
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs add ~/src/rust/nushell /etc ~/.cargo
-------------------------------------- /home/bobhy/src/rust/nushell --------------------------------------
〉dirs next 2
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │         │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
│ 3 │ ==>     │ ~/.cargo           │
╰───┴─────────┴────────────────────╯
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs drop
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │ ==>     │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
╰───┴─────────┴────────────────────╯
---------------------------------------------- /home/bobhy ----------------------------------------------
〉
```
# Tests + Formatting

Haven't even looked at stdlib `tests.nu` yet.

Other todos:
* address module todos.
* integrate into std lib, rather than as standalone module. Somehow
arrange for `use .../standard_library/std.nu` to load this module
without having to put all the source in `std.nu`?
*  Maybe command should be `std dirs ...`?   
* what else do `enter` and `exit` do that this should do? Then deprecate
those commands.

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[f124a5d354...](https://github.com/git-for-windows/git/commit/f124a5d354cc1422f2ed150ec38fc29ea95d300d)
#### Tuesday 2023-03-14 09:28:43 by Johannes Schindelin

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

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[fc1e2e5e26...](https://github.com/harryob/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Tuesday 2023-03-14 10:00:35 by riot

L42A replacement with M4RA, less balance edition (#2674)

<!-- Write BELOW The Headers and ABOVE The comments else it may not be
viewable. -->

# IMPORTANT NOTES PLEASE READ
THIS DOES NOT CONTAIN THE NEW AMMO AND REBALANCED L42/M4RA THAT #1485
HAD
THIS DOES CONTAIN SOME BALANCE THINGS, BUT IT IS NOT ANYWHERE CLOSE TO
THE ABOVE

Also lore team wanted this, plz no gbp close maintainers 🙏 🙏 🧎‍♂️ 🕋 

# About the pull request

Replaces L42A in all marine available sources with the M4RA, the
canonical DMR of the USCM, you may notice this is currently the scout
rifle, well the scout rifle is now the M4RA Custom, a version that can
chamber the HV rounds that are spec ammo, but it can also chamber
standard m4ra rounds, albeit doing less damage with them than a normal
M4RA.

M4RA has current L42A stats fully, with the three exceptions being
having no stock to attach or remove(stock was not integrated it sucked),
being able to fit a/vgrip like scout m4RA, which may seem like a huge
thing but L42 stats were already insane, so it doesn't effect much.

M4RA Custom(scout gun), gets L42 stats as well, with the exception of
having less of a damage mult, meaning when not using the spec ammo, it
is out-preformed by the standard m4RA.

Adds new M4RA sprites, both standard and custom, by triiodine 

Adds sprites for all M4RA mag variants, by myself.

This was requested by lore team, previous PR of this with way more
balance stuff was #1485
Ok thats about all 🙂 

# Explain why it's good for the game

Lore accuracy is good, and this mostly doesn't effect the actual game
outside of the scout rifle changes.
Also scout rifle underpreformed if you weren't omega hell sliming with
inc-impact stunlocking while on fire, still will be omega hell slime
central but that isn't the thing being solved in this pr , it'll do fine
when NOT sliming at least now.


# Testing Photographs and Procedure
It works.


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->
 
:cl:
add: Adds the M4RA as the standard marine DMR, identical stats to L42
with the exception of fitting a v or agrip and no removable stock, stats
still the same as l42 without stock.
del: L42 from all marine accessible sources with the exception of black
market
balance: Scout M4RA is now the M4RA Custom, it can use standard M4RA
magazines but standard M4RA cannot use custom magazines.
balance: Scout M4RA now has L42/M4RA standard stats with the exception
of lower damage.
balance: Scout M4RA now can fit magnetic harness, laser sight, however
it can no longer fit recoil compensator
fix: R4T sling now has the correct color scheme on LV522
spellcheck: New desc for M4RA and L42 by misty
imageadd: New M4RA icons by triio, both scout and normal
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[877d6ce3d2...](https://github.com/treckstar/yolo-octo-hipster/commit/877d6ce3d2a77342fabd187279f9eb08f7a23090)
#### Tuesday 2023-03-14 10:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [parasme123/gravid](https://github.com/parasme123/gravid)@[a7623f5671...](https://github.com/parasme123/gravid/commit/a7623f5671a0eab0d9fdecf0242f35decc0d02f7)
#### Tuesday 2023-03-14 10:38:57 by jitendra

Solve Feedback points

1.) Terms and Condition and Privacy policy should be clickable.
2.) I agree with the Terms & Conditions and Privacy Policy
3.) Email or WhatsApp message not received on registration
4.) Remove the user Doctor option. We will build the doctors app post MVP
5.) Error Message should be corrected to- Click the checkbox to proceed
6.) Name must be between 2 to 100 characters
7.) Remove male pic and use nuetral gender default pic
8.) Remove marked statement
9.) link all the social icons : Share popup added
10.) Also change the text below the pic to “Refer a friend”
11.) Also change website to new website URL
12.) Currency should be specified
13.) Pic of the expert should be in circle with same background
14.) Pic and text should be centrally aligned
15.) Specify “No bookmarks added”
16.) Correct the icon of the installed app and the name should start with capital “G”
17.) Parenting TV - video does not stop if the user goes to some other link on the app The audio is on in the background
18.) We need a “Next” button on the bottom right side along with Skip options. Do the user to go to the next page. This page doesn’t go to the next page until you click on skip

---
## [gsax/doftiles](https://github.com/gsax/doftiles)@[d92496b938...](https://github.com/gsax/doftiles/commit/d92496b9387c59786d917ebe084c26dc6fea8d6c)
#### Tuesday 2023-03-14 11:37:04 by Georg Sachs

Add defaults.list

You need not only a mimeapps.list, but also an defaults.list to define
your preferred default applications.
God I hate all this mime shit.

---
## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[582f5b38cb...](https://github.com/dsmith328/LC13Master/commit/582f5b38cb9ad5d051cbea48af501089ba3f0206)
#### Tuesday 2023-03-14 11:49:59 by Lance

Holy FUCK temporary commit

Mixed between previous abno based spawning and new subsystem

Cleanup Commit

Removes a lot of previous code and paves the way for the subsystem method.

Major Commit

Apocalypse Bird drops it's loot and only spawns once. It'll not try to happen if there aren't enough birds, and if two are breached before the third arrives it'll take the third breaching to start the event, until the others are suppressed. Birds do not target people and are immortal while moving to the portal. If unable to reach it after 3 minutes they'll be forced in manually.

Tweaked Proc

Redundant Code Removal

Remembered I didn't need this

Enhanced Code

Moved an if-statement to a better place to more adequately solve the issue.

Test Commit

Does this solution work?

Global Abnormality Mob List

Patrol Changes and Bird Grab changes

Gaming Test?

Temp Commit

Second Commit

Another Commit!

Fourth Commit

Subsystem changes. Dead abno cleansing. Lower speak cooldown. Debug text removal.

P-bird fix

Fixes P-bird able to die before reaching the portal

---
## [EbolaNerd/S3](https://github.com/EbolaNerd/S3)@[d65224884d...](https://github.com/EbolaNerd/S3/commit/d65224884dfd7e73995e927a50b34de903ec827e)
#### Tuesday 2023-03-14 15:00:46 by Ebolanerd

´Begun the shitshow of calling pam for player creation. It's complete ass and I hate it.

---
## [SDP-GeoHunt/geo-hunt](https://github.com/SDP-GeoHunt/geo-hunt)@[f9251b69f7...](https://github.com/SDP-GeoHunt/geo-hunt/commit/f9251b69f7619f194275af5f78673368a1de171b)
#### Tuesday 2023-03-14 15:46:58 by Marwan

Compose migration (#26)

* Modify configuration files to support Kotlin & Jetpack Compose

As discussed this morning, we plan on moving to Kotlin and Jetpack compose. This commit marks the beginning of the modification to make it.

* Update minSdk to comply with firebase requirement

Changes:
* Change from minSdk:24 to minSdk:28 to comply with the firebase
  realtime database requirements

* Delete old java activity file and write basic test

Changes:
* Remove `GreetingActivity.java` and `MainActivity.java` and
  dependencies
* Write simple `ComposeActvitityTest.kt`

* fix: Support for coverage with Kotlin

* Added Mockito

* Fixed the build.gradle with proper versions

* :fire: :100: :triump: base :rage:

---------

Co-authored-by: BoyeGuillaume <guillaume.boye@epfl.ch>

---
## [facebook/hhvm](https://github.com/facebook/hhvm)@[0cd7ddd10c...](https://github.com/facebook/hhvm/commit/0cd7ddd10ce74f5d10a62ba9abe91904a33959b7)
#### Tuesday 2023-03-14 15:47:46 by Lucian Wischik

progress 4/4 user-experience tweaks

Summary:
## Fanout calculation, and sooner typecheck

During large fanout calculations we see these:
```
waiting for hh_server [determining changes]
~7s
waiting for hh_server [getting members 1/10000 (5%) 15 elements]
~2s
waiting for hh_server [getting members 10000/10000 (100%) 10000 elements]
server log "finished recomputing type declarations"
~50s
server log "type declarations for 1 file: 173"
~3s
waiting for hh_server [typechecking 500/20000 files] - when it completes its first batch
```
* https://fburl.com/hack/jh0b0ucz - "determining changes" for 7s, "getting members" finished in 1s, but then it gave no updates for the 37s between "finished recomputing type declarations" and "type declarations for 1 files: 46.1", then a further 6s evaluating prechecked changes.
* https://fburl.com/hack/nn7kyl5b - "determining changes" sometimes takes a long time, but "getting members" just about never does. And again, there's a 50s gap between "finished recomputing type declarations" end of `redo_type_decl` and "type declarations for 1 files: 173" `ServerTypeCheck.type_check_core`

This diff adds some extra progress messages:
```
waiting for hh_server [determining files] -- resolving Dep.t into filenames via naming-sqlite lookup
waiting for hh_server [determining trunk changes] - doing the prechecked algorithm
waiting for hh_server [getting members 1/1000 (5%)] - I removed the "15 elements" extra stuff
waiting for hh_server [typechecking] - right at the very first moment of typechecking
waiting for hh_server [typechecking 20000 files] - when it knows how many files but hasn't yet started
```

1. It's wrong to be stuck at "getting members 100%" for such a long time. It should only ever get stuck on things that indicate work in progress! I hope that "determining files" and "determining trunk files" will (1) mean we don't get stuck on 100% for so long, (2) shed more light on what's happening during those long fanout calculations.
2. We used to only ever display "[typechecking 500/20000 files]" after the first batch had completed, some 2-4s after typechecking began. I hope that "[typechecking]" will show up super early, and "[typechecking 20000 files]" will show up as soon as possible, so we know when typechecking has started.

## Sooner typecheck for HackIDE

Sometimes we'd see "[HackIDE:ide_idle done]" for 2-3s.
* https://fburl.com/hack/buvh5hgh - "ide_idle done" we failed to report progress at start of typecheck.
* https://fburl.com/hack/6k6xf1i0 - the same "ide_idle done"

The reason is that hh_server had handled IDE_IDLE from clientLsp, and so displayed "ide_idle done", and then started typechecking almost immediately, but took 2-3s before the first batch had been displayed. I hope that the new "[typechecking]" message will avoid this.

Another case, I believe, is when typechecking was interrupted, and we were left looking at the message "HackIDE:change write" relating to the interruption, and then typechecking resumed very soon after, but we didn't see the first typechecking message until it had finished its first batch in 2-3s. I hope this will be improved as well.
* https://fburl.com/hack/jtlf369s - "HackIDE:change write" because I think it resumed a typecheck after an interrupt, but didn't display status for that typecheck

## Typechecking 10/10 files

Sometimes it shows "Typechecking 10/10 files" for several seconds. The reason is that it has indeed finished typechecking the last final, but then there are 2-3s of further work before it finishes handling the request and responds to the user. I'm not sure what it's doing in this time.
* https://fburl.com/hack/6z6cirle - "typechecking 10/10 files" but there were a further 2-3 seconds before RECHECK_END and, shortly after it, Server_end_handle

I added a new message to clarify
```
waiting for hh_server [typecheck ending]
```

## Typechecking 9990/10000 files (100.0%)
It's displeasing to see 100.0% when it hasn't yet finished typechecking the final file. I therefore made it round down to 99.9% until it really has finished every single last file.

## Why is this all so ad-hoc? isn't there something better?

I think that good progress-reporting is just hard! I can't think of any architecture design that would make good reporting just fall out for free.

(well, the only one would be "add a progress report on every single line of code" but that would be intolerable).

It's hard for us code authors to anticipate which lines or functions will take a long time. And when we break a function up into multiple sub-functions, then sometimes progress reporting should happen inside one of the sub-function because that's where the slow bit was, and sometimes at the higher-level function because that's where we want to indicate that the slow stuff has finished. Maybe progress reporting would be easier in a simpler thing like "fetch url" which has fewer phases. But for us, fanout calculation and interruptible typechecking have so many phases.

One overarching difficulty is that a user never wants to see "[subpart1 done]". They only ever want to see "[subpart2]", i.e. they want to see what it's working on, not what it finished working on. So I think progress reporting isn't compositional in any useful way... every time we report "[subpart1]" then we're at the mercy of whether we correctly also reported "[subpart2]".

Reviewed By: nt591

Differential Revision: D44008749

fbshipit-source-id: 5011da481fb5c2dffd9856482e5b201dda85f13c

---
## [facebook/hhvm](https://github.com/facebook/hhvm)@[cc6c2a5591...](https://github.com/facebook/hhvm/commit/cc6c2a5591caf964f27cc8157125d3cf54816e8e)
#### Tuesday 2023-03-14 15:47:46 by Lucian Wischik

progress 2/4 no more warning

Summary:
This diff makes only one change. In the ServerInit.ml snippet below, it removes the call to `ServerProgress.send_warning`. This is the only call to `send_warning` in the entire codebase.
```
let lazy_saved_state_init () =
  match ServerLazyInit.saved_state_init ... with
  | Ok _ -> ...
  | Error err ->
    let message = load_state_error_to_verbose_string err in
    let (next_step_descr, next_step) =
      if not genv.local_config.SLC.require_saved_state then
        ("fallback", Exit_status.No_error)
      else if auto_retry then
        ("retry", Exit_status.Failed_to_load_should_retry)
      else
        ( "fatal", Exit_status.Failed_to_load_should_abort)
    in
    (match next_step with
    | Exit_status.No_error ->
      ServerProgress.send_warning user_message
```
The warning was for the scenario where hh_server attempts a native saved-state-load, but it fails, and hh.conf "require_saved_state=false", so it falls back to a full init. The user experience in this case was to display a warning message:
```
$ ... tweak .hhconfig
$ hh --config require_saved_state=false
hh_server is busy: [waiting on db...] /
Could not load saved-state from DevX infrastructure. The underlying error message was: Hack can't start because .hhconfig isn't recognized.
If you are editing .hhconfig, sorry, Hack does not support starting up while there is an edited .hhconfig.
Otherwise, are you in the middle of a rebase? Can you `arc pull`?
Once done, restart Hack by clicking on it in the status bar or running hh restart on the command line.
If that fails, post in Hack Language Feedback/Support.

hh_server is busy: [indexing - this can take a long time, see warning above]
```

In other words, the text that is usually an error would now be displayed as a warning, in addition to the usual progress message `hh_server is busy: [indexing]`.

But our hh.conf.erb makes require_saved_state=true in all cases, so we never go down this path. Therefore, I deleted last remaining call to `ServerProgress.send_warning`, and I deleted this API entirely. There were a whole load of knock-on cleanups that I could therefore do throughout the rest of the codebase.
* ServerProgress used to support calling "send_warning" at one time, and "send_progress" at another, so it had to maintain a state of what the most recent warning and most recent progress messages where, so they could be combined together when it writes the progress.json file
* clientConnect used to support reading the warning and progress, and appending "this can take a long time", and checking whether the warning has changed
* If you look at ServerProgress.mli, the API has been simplified. I also renamed "ServerProgress.send_progress" to just ServerProgress.write, because that's what it does.

Reviewed By: nt591

Differential Revision: D43969343

fbshipit-source-id: 7d41880a57f214a94fa737ca42c444650bc449c8

---
## [NopemanMcHalt/S.P.L.U.R.T-Station-13](https://github.com/NopemanMcHalt/S.P.L.U.R.T-Station-13)@[bc48a6eafc...](https://github.com/NopemanMcHalt/S.P.L.U.R.T-Station-13/commit/bc48a6eafcf9afedfc419afaa982dd15339a94aa)
#### Tuesday 2023-03-14 15:56:37 by Darius

Add vampire ability permission check

Adds a new mob proc that allows checking if vampiric abilities should function. Allows easily checking anti-magic, trait holy, garlic necklace, garlic blood, and staked status.

Bloodfledge actions and coffin healing will now use this check. Flight potions will warn bloodfledge quirk users before allowing consumption.

---
## [matjaeck/crawlee](https://github.com/matjaeck/crawlee)@[a95e6676b2...](https://github.com/matjaeck/crawlee/commit/a95e6676b2e3574c8db3083c661dc09a5405751e)
#### Tuesday 2023-03-14 16:52:08 by Martin Adámek

chore: switch to yarn v3 (#1752)

NPM got somehow [broken more than
usual](https://github.com/apify/crawlee/actions/runs/3997285915/jobs/6873858419)
and its no longer possible to install the dependencies in CI. We were
struggling with NPM for quite some time (especially after we moved to
turborepo). I’ve been advocating for yarn since my first days here, been
using it for last ~5 years on a daily basis and it never did anything
wrong to me, so I hope this will be the right step and a smooth
transition for all the collaborators.

What to expect? Since we require node 16, we can leverage `corepack`, a
new tool shipped with newer node versions (btw developed by yarn
maintainers). This means you just need to run `corepack enable` and yarn
should be available in your workspace. In case of some problems, you can
try running `corepack prepare yarn@stable --activate`, but it shouldn’t
be needed. Note that we use `corepack` instead of commiting yarn binary
to the git repo - that is the reason why `.yarn` folder is gitignored.

Initially we will start with a conservative setup, using a node linker,
so there will be the good `node_modules` folder we are all used to. I’d
like to experiment with the advanced features as well, mainly in the
project templates, as it could greatly improve the build times (we could
even skip the install step completely).

With that said, we will be still using NPM inside our E2E tests, to be
sure the project can be safely installed with NPM. This change should
affect only the collaborators, not our users. Ideally we should test
other package managers via CI too, so we are sure `pnpm` works as well,
or maybe even `bun`.

Few API differences and quality of life improvements yarn brings:
* `npm install` -> `yarn`
* `npm install xxx` -> `yarn add xxx`
* `npm run ...` -> `yarn …`
* `npx …` -> `yarn …`
* no need to deal with the `--` issue from `npm run` (propagating CLI
params to the script)
* powerful caching and _sane_ lockfile format

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[a59f8a0d61...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/a59f8a0d61ceda8dbd046de812d01f0f53dee392)
#### Tuesday 2023-03-14 17:13:01 by chris

Monster casting changes (mostly goatmom's casters)

(Big picture: There is a potential pet goatmom priestess in the madman quest that I've wanted to be special in this way for a while now. Also tweaked the Blessed while I was at it).

1) Introduce Red Word spell: Single target version of the red word of knowledge.
--Vs. the player it causes sanity loss (based on clothing worn), possibly a random minor madness effect, and Panic based on clothing worn.
---Knowing the red word grants immunity to this effect
--Vs. monsters it causes the crazed/flee/disrobe effect of the red word, plus an immediate proc of disrobing.
-Not cast vs. imune targets, only cast in melee range (flavored as "whispering")

2) Introduce Hypnotic Colors spell: Wide-gaze paralysis effect that causes targets to move slightly towards the caster.
--Possible stunlock vs. the PC if the PC lacks resistance and the spell is cast too frequently. The only monster capable of casting it currently casts it at less that 1/7 (and is typically friendly anyway).
---Does not friendly-fire
--Hypnotic Colors is considered AoE so may be cast without a true target.

3) Goatmom spell lists:
--Mistweaver priestesses favor red word and hypnotic colors as well as their standard spell list.
--The Blessed cast red word, god ray, and sometimes (1/100) disintegration (7 damage) in addition to previous spells

4) Psi bolt diversity:
--Priests of Ib use the nausia psi bolt
--The good neighbor uses doubt bolt
--The Blessed use sanity bolt

5) Tweaks:
--Tame priests don't use earthquake (it's more of a pain than a benefit I think).
--Mother's gaze doesn't print the "casts a spell" message (it has a different flavor)

---
## [NetworkManager/NetworkManager](https://github.com/NetworkManager/NetworkManager)@[f20d5a2e4f...](https://github.com/NetworkManager/NetworkManager/commit/f20d5a2e4fe274a1697a1337b79a70aa1e9fc80e)
#### Tuesday 2023-03-14 17:13:31 by Thomas Haller

platform: always reconfigure IP routes even if removed externally

NML3Cfg is stateful, that means it remembers which address/route it
configured earlier. That is important because the API users of NML3Cfg
only say what the want to configure now, and NML3Cfg needs to remove
addresses/routes that it configured earlier but are no longer to be
present. Also, NetworkManager wants to allow the user to add
addresses/routes externally with `ip addr|route add` and NetworkManager
not removing it. This is a common use case for dispatcher scripts, but
in general, we want to allow other components to add addresses/routes.

We try something similar with the removal of routes/addresses managed by
NetworkManager. When NetworkManager adds a route/address, which later
disappears, then we assume that the user intentionally removed the
address/route and take the hint to not re-add it.

However, it doesn't work. It is problematic for two reasons:

- kernel can automatically remove routes. For example, deleting an IPv4
  address that is the prefsrc of a route, will cause kernel to delete
  that route. Sure, we may be unable to re-configure the route at this
  moment, but we shouldn't remember indefinitely that the route is
  supposed to be absent. Rather, we should re-add it when possible.

- kernel is a pain with validating consistencies of routes. For example,
  when a route has a nexthop gateway, then the gateway must be onlink
  (directly reachable), or kernel refuses to add it with "Nexthop has
  invalid gateway". Of course, when removing the onlink route kernel is
  fine leaving the gateway route behind, which it would otherwise refuse
  to add.
  Anyway. Such interdependencies for when kernel rejects adding a route
  with "Nexthop has invalid gateway" are non-trivial. We try to work
  around that by always adding the necessary onlink routes. See
  nm_l3_config_data_add_dependent_onlink_routes(). But if the user
  externally removed the dependent onlink route, and NetworkManager
  remembers to not re-adding it, then the efforts from
  nm_l3_config_data_add_dependent_onlink_routes() are ignored. This
  causes ripple effects and NetworkManager will also be unable to add the
  nexthop route.

Trying to preserve absence of routes that NetworkManager would like to
configure is not tenable. Don't do it anymore. There was anyway no
guarantee that on the next update NetworkManager wouldn't try to re-add
the route in question. For example, if the route came from DHCP, and the
lease temporarily went away and came back, then NetworkManager probably
would have (correctly) forgotten that the user wished that the route be
absent. This did not work reliably and it just causes problems.

---
## [themotte/rDrama](https://github.com/themotte/rDrama)@[9895fa1bba...](https://github.com/themotte/rDrama/commit/9895fa1bbabc9213391e380753ca72404f80aa18)
#### Tuesday 2023-03-14 18:28:49 by justcool393

comments.html: refactor so that something can be sanely
changed in it

the comments.html template (along with submission.html) has numerous
undesirable properties which i will describe now. unless you are very
familiar with the codebase, it can be extremely difficult to grok.

this is pretty insane as there is nothing fundamentally complex about
the goal of comments.html: return a component that shows a username
and info, reports if any, comment content, and actions a user can
take.

this behemeoth was initially 886 lines in the old version of this
codebase, and this is with awards and a lot of other cruft removed.
anyway, the maintainability of this file is about on par with some
legacy application that keels over and dies if you sneeze vaguely
in its direction.

the nicest thing i can say about it is that it isn't currently
crashing.

anyway some of the problems include:

* large, splittable components, are not split into separate files.

this makes it incredibly difficult to find or make changes across
the template and makes it nearly impossible to find or change a
specific thing.

this is most easily exemplified in the modals, which should by all
accounts be separate templates, just inlined into comments.html.

* the nesting is oftentimes incorrect.

inexplicably, probably out of laziness from when the code was first
written, things will end up fully left aligned, while multiple layers
deep into a nesting context.

if an if statement or an endif is changed, it is *incredibly*
difficult to figure out where the error was. you can't trust the
nesting.

* multiple repeated checks for things that are always true.

this is probably a symptom of the above two problems but it's very
noticeable once you fix the nesting. for example there is a block
near the very top of the actions bar which checks for
parent_submission which effectively checks "is this in a post" (this
commit won't complain about parent_submission checks but i do have
opinions on those).

all of the action buttons further down the chain also check for
parent_submission, or even check inconsistently (by using if c.post)
within this context this is a completely unnecessary check in this
context.

while it is potentially useful (and in fact because #251 requires we
dismantle the assumption a little bit) to have these checks now, the
fact that they were initially added shows that when the code was all
initial written, there was little care into thinking about comment
state.

* mobile actions are duplicated and duplicated inline.

i actually do find it probably pretty hard to support this normally
given the codebase's DOM so whatever, duplicate the things, *but* if
we're going to do that, inlining it into the middle of an incredibly
long template is really difficult to comprehend as a design decision.

...anyway yeah this PR intends to fix these problems and enable work
to be done on #251. this is a "perfect is the enemy of good" commit.
it doesn't change much fundamental and is not intended to erase the
sins of the original file, but at least make it maintainable.

this also fixes a minor bug with #473 where the GIF modal was left
in by accident.

---
## [Aphast/T.E.-station](https://github.com/Aphast/T.E.-station)@[ba77b0daae...](https://github.com/Aphast/T.E.-station/commit/ba77b0daae961bb0274e6856a0f1f87934f8c4f4)
#### Tuesday 2023-03-14 18:46:31 by JasmineRickards

Merge pull request #35 from IFuckedUpMerging/actually-fix-that-dumb-stupid

[REQ] Fixes Dreamchecker Error + Modsuit Icons

---
## [TheParasiteProject/frameworks_base](https://github.com/TheParasiteProject/frameworks_base)@[fb2175aeca...](https://github.com/TheParasiteProject/frameworks_base/commit/fb2175aecae355b05b72eaba99ae1211762fd623)
#### Tuesday 2023-03-14 19:45:43 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [BeBulinda/alx-low_level_programming](https://github.com/BeBulinda/alx-low_level_programming)@[362b818b29...](https://github.com/BeBulinda/alx-low_level_programming/commit/362b818b293494e6fcb3ec7bb7d8f57cc420d23b)
#### Tuesday 2023-03-14 19:56:09 by Be Bulinda

0x0B. C - malloc, free

# 0x0B. C - malloc, free

# 0. Float like a butterfly, sting like a bee
Write a function that creates an array of chars, and initializes it with a specific char.
    Prototype: char *create_array(unsigned int size, char c);
    Returns NULL if size = 0
    Returns a pointer to the array, or NULL if it fails

# 1. The woman who has no imagination has no wings
Write a function that returns a pointer to a newly allocated space in memory, which contains a copy of the string given as a parameter.
    Prototype: char *_strdup(char *str);
    The _strdup() function returns a pointer to a new string which is a duplicate of the string str. Memory for the new string is obtained with malloc, and can be freed with free.
    Returns NULL if str = NULL
    On success, the _strdup function returns a pointer to the duplicated string. It returns NULL if insufficient memory was available
FYI: The standard library provides a similar function: strdup. Run man strdup to learn more.

# 2. He who is not courageous enough to take risks will accomplish nothing in life
Write a function that concatenates two strings.
    Prototype: char *str_concat(char *s1, char *s2);
    The returned pointer should point to a newly allocated space in memory which contains the contents of s1, followed by the contents of s2, and null terminated
    if NULL is passed, treat it as an empty string
    The function should return NULL on failure

# 3. If you even dream of beating me you'd better wake up and apologize
Write a function that returns a pointer to a 2 dimensional array of integers.
    Prototype: int **alloc_grid(int width, int height);
    Each element of the grid should be initialized to 0
    The function should return NULL on failure
    If width or height is 0 or negative, return NULL

# 4. It's not bragging if you can back it up
Write a function that frees a 2 dimensional grid previously created by your alloc_grid function.
    Prototype: void free_grid(int **grid, int height);
    Note that we will compile with your alloc_grid.c file. Make sure it compiles.

# 5. It isn't the mountains ahead to climb that wear you out; it's the pebble in your shoe
Write a function that concatenates all the arguments of your program.
    Prototype: char *argstostr(int ac, char **av);
    Returns NULL if ac == 0 or av == NULL
    Returns a pointer to a new string, or NULL if it fails
    Each argument should be followed by a \n in the new string

# 6. I will show you how great I am
Write a function that splits a string into words.
    Prototype: char **strtow(char *str);
    The function returns a pointer to an array of strings (words)
    Each element of this array should contain a single word, null-terminated
    The last element of the returned array should be NULL
    Words are separated by spaces
    Returns NULL if str == NULL or str == ""
    If your function fails, it should return NULL

---
## [kubouch/nushell](https://github.com/kubouch/nushell)@[378a3ae05f...](https://github.com/kubouch/nushell/commit/378a3ae05f5459a64f97af3781d4336c35652db4)
#### Tuesday 2023-03-14 20:42:13 by Kovacsics Robert

Use `with-env` to avoid calling external command on invalid command (#8209)

# Description

My terminal emulator happens to be called `st`
(https://st.suckless.org/) which breaks these tests for me

_(Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.)_

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes

_(List of all changes that impact the user experience here. This helps
us keep track of breaking changes.)_

# Tests + Formatting

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[c795a3e0da...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/c795a3e0da86765cd29eabdc66546cd706ce0e5c)
#### Tuesday 2023-03-14 20:47:15 by Nickay

FOR THE LOVE OF GOD TEST YOUR FUCKING SHIT IN DEBUG MODE AND ERROR LOG BEFORE PUSHING

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a1e5591d51...](https://github.com/mrakgr/The-Spiral-Language/commit/a1e5591d51b1f8837da6e4659d25c9bd7b4a7b45)
#### Tuesday 2023-03-14 21:16:17 by Marko Grdinić

"8:05am. I am up. Let me chill for a bit.

8:25am. Let me slowly get started. Every day, playing Limbus pushes me to the bring of exhaustion and I sleep like a baby. It is a pretty good sleeping pill.

https://youtu.be/lFKEp4FrnV8
LunchBytes - Build Cloud Native High-Scale Apps with Microsoft Orleans

Let me watch this for a bit. I meant to study Orleans lightly for a while, but didn't have the time. After this I'll do some refactoring and then figure out how to do those lists in React.

https://youtu.be/hiosjTVUPP4?t=528
Introduction to Microsoft Orleans

Let me watch this instead.

8:45am. Forget it. Let me start. Doing this lightly is just wasting my time. I already knew that this kind of studying is no better than onanism. Orleans is kind of ugly, but C# code is usually like that.

https://reactjs.org/docs/lists-and-keys.html

https://react-select.com/home
> A flexible and beautiful Select Input control for ReactJS with multiselect, autocomplete, async and creatable support.

Doesn't it have something native. I do not want to import a library.

https://reactjs.org/docs/forms.html

https://beta.reactjs.org/reference/react-dom/components/input

...

https://beta.reactjs.org/reference/react-dom/components/select

Wait,  I need this.

8:55am. Yeah, this is what I'll be doing. Things like distributed computing are best picked up when I need them. I should be able to find a job that does not require me to know Orleans right off the bat. I'll figure out how to scale to large apps once I encounter that problem. For now, let me just aim for the common.

10:20am. Done. Right now I am just in a daze, but maybe I should get started on the video? Ah right...

```fs
type ILeducChance =
    abstract member chance : id: int option * mask: Mask * cont: (Card * Mask -> unit) -> unit
type ILeducAction =
    abstract member action : model: LeducModel * msgs: string list * allowed_actions: AllowedActions * cont: (Action -> unit) -> unit
type ILeducTerminal =
    abstract member terminal : model: LeducModel * msgs: string list -> unit
type ILeducPlayer =
    inherit ILeducChance
    inherit ILeducAction
    inherit ILeducTerminal
```

Let me organize this like so.

```fs
type Leduc2P(chance : ILeducChance,terminal : ILeducTerminal,p0 : ILeducAction,p1 : ILeducAction) =
    interface ILeducPlayer with
        member this.chance(id, mask, cont) = chance.chance(id,mask,cont)
        member this.action(model, msgs, allowed_actions, cont) =
            if model.p1_id = 0 then p0.action(model, msgs, allowed_actions, cont)
            else p1.action(model, msgs, allowed_actions, cont)
        member this.terminal(model, msgs) = terminal.terminal(model,msgs)
```

Last night, I thought that I might need to implement the separate interaces for this, `ILeducChance`, `ILeducAction` and `ILeducTerminal` each, but it is no problem.

Ok, enough messing around. With this I have everything I need for tutorial4.

12:05pm. https://pixabay.com/music/acoustic-group-acoustic-folk-music-guitar-141345/

12:50pm. https://youtu.be/J1ogFprtZ_U
Introducing The Random Player For Leduc

Here it is. Done with this video. Next I'll introduce tabular CFR. I guess I better get to work on it.

It is too bad nobody will ever watch these videos. In contrast, the Paperspace ones are much more popular.

12:55pm. It is time for a break. I got Eiyuuou yesterday and I might as well watch it now.

Today's voice acting session felt rather smooth.

1:55pm. Done with breakfast. Let me chill for a bit and then I will do the chores and get started on the next part. First will be the tabular CFR algorithm.

2:55pm. Done with chores. Let me start with the next step. Today I was so caught up in what I was doing in the morning that I forgot to take a bath. I'll have to make sure to take one tomorrow. But now...

I've done this so many times that the CFR algorithm is etched into my soul.

The first step is to get into it.

```fs
module CFR

type IAction<'model,'action> =
    abstract member action : 'model * 'action [] * ('action -> float) -> float
```

I'll focus on just implementing it like this. There is no need to make it more complicated.

3:35pm.

```fs
module CFR

open System.Collections.Generic

type PathProb = float * float
type IAction<'model,'action> =
    abstract member action : model: 'model * actions: 'action [] * prob: PathProb * cont: ('action * PathProb -> float) -> float

let ( *.) (a : PathProb) (b : float) = fst a * b, snd a

type CFR<'model,'action when 'model: equality>() =
    let d : Dictionary<'model, float[]> = Dictionary()
    let get_policy model len = failwith "todo: get the model from the dictionary"

    interface IAction<'model,'action> with
        member this.action(model, actions, prob, cont) =
            let current_policy : float [] = get_policy model actions.Length
            let rewards = Array.map2 (fun act policy_prob -> cont (act, prob *. policy_prob)) actions current_policy
            0
```

I am thinking about it. I've written this little bit, and what I feel the urge to do would be to explain this part.

Let write code a bit, and then explain a bit. I'll iterate it like that.

https://www.youtube.com/results?search_query=counterfactual+regret

There is a bunch of stuff on CFR on Youtube, but I'll do it the best way.

Let me fire up the mic.

...Dick, I accidentally erased the Camtasia project I posted previously. By accident I created the CFR under the same number as the old one, and then instead of erasing the CFR one, I erased the real one. Anyway, I'll just back up the file from Youtube. It is not like I am going to be going back and editing it.

Focus me, let me start the new project.

4:15pm. Damn it. Remember what that Creator Village guy said about his nasal passage doing a click when he stops speaking and recommended that I let the air out past the sentence end? That was such good advice. I was wondering where those clicks are coming from, and it turns out from inside my nose somewhere.

4:30pm. Damn. Right now I am fatigued and I am definitely finding it harder to speak eloquently.

4:50pm. It is like I am trying to pry the words out of my mouth with a plyer. I feel so low of energy, and my nasal passage is making clicks.

6:45pm. I've managed to dub 3m of video.

3h for 3m of video. If I had to do this for a living, I'd rather kill myself. Seriously. I am basically going to practice this for two more weeks or so, and then I'll switch to the synth voice if it is possible.

That Matt guy who suggested voiceless vids as a way of making money on Youtube is seriously underestimating how hard making such videos is. It is very hard!

If I can't get a good paying job because I am too stupid to string two sentences together without stuttering, mumbling or backtracking, and miss my chance to compete in the race for the Singularity, then that would be comedic justice at its finest.

6:55pm. But anyway, I did well today. Now it is time to rest. No point in working past this point.

https://news.ycombinator.com/item?id=35154275
https://interviewing.io/blog/why-you-shouldnt-list-certifications-on-linkedIn

> Engineers use interviewing.io for anonymous mock interviews. If things go well, they skip right to the technical interview at real companies (which is also fully anonymous). We started interviewing.io because resumes suck and because we believe that anyone, regardless of how they look on paper, should have the opportunity to prove their mettle.

Interesting site.

I should be using this for interviewing practice."

---
## [jedjoud10/cflake-engine](https://github.com/jedjoud10/cflake-engine)@[b0145e956e...](https://github.com/jedjoud10/cflake-engine/commit/b0145e956e71409a9b1c023813b4b50eefa0915d)
#### Tuesday 2023-03-14 21:45:03 by jedjoud10

Holy shit it truly is asynchronous that's insane bro

---
## [idoblenderstuffs/idoblenderstuffs.github.io](https://github.com/idoblenderstuffs/idoblenderstuffs.github.io)@[a0ca09713c...](https://github.com/idoblenderstuffs/idoblenderstuffs.github.io/commit/a0ca09713c839b4bd72d25d8375677ab9d70b1ca)
#### Tuesday 2023-03-14 22:23:44 by idoblenderstuffs

using github to make sites on an ipad is so slow

i fucking hate this i want my damn pc back

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e47c47a081...](https://github.com/tgstation/tgstation/commit/e47c47a081f5919eea2b43453be7ac011ee2a492)
#### Tuesday 2023-03-14 22:23:51 by MrMelbert

You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed (#73983)

## About The Pull Request

If you are restrained, and placed into an unlocked labor camp
teleporter, you cannot instantly resist out of it. However the resist
timer is cut in half while unlocked.

## Why It's Good For The Game

Getting someone into the gulag teleporter is an incredibly un-necessary
pain in the rear because simply *spamming resist* turns it into a game
where you have to shove them in, then really quick go over to the
computer and slam the lock button. This is... kinda lame. A lot of new
player security officers get got by this, and I think it's sad. Inb4
"Skill issue"

## Changelog

:cl: Melbert
balance: If you are handcuffed, you can't instantly resist out of an
unlocked labor camp teleporter (however, resist time is halved).
/:cl:

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[7f8874df29...](https://github.com/MarkSuckerberg/Shiptest/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Tuesday 2023-03-14 22:28:15 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[60e85fa947...](https://github.com/tgstation/tgstation/commit/60e85fa947799e20419dc867a238afb27b840e59)
#### Tuesday 2023-03-14 22:34:54 by LemonInTheDark

Polishes some side sources of light and color (#73936)

## About The Pull Request

[Circuit Floor
Polish](https://github.com/tgstation/tgstation/commit/6b0ee9813271f693ceb44ad42277c36ef2e71268)

Circuit floors glow! but it looks like crap cause it's dim and the
colors are washed out.
I'd like to make them look nicer. Let's make them more intense and
longer range, and change the colors over to more vivid replacements.

While I'm here, these should really use power and turn on and off based
off that.
Simple enough to do, just need to hook into a signal (and add a setter
for turf area, which cleans up other code too).

[Desklamp
Upgrade](https://github.com/tgstation/tgstation/commit/8506b13b9c97bf740c3e97db04450555387dd126)

Desklamps look bad. They're fullwhite, have a way too large
range.Crummy.
Let's lower their lightrange from 5 to 3.5, and make the ornate ones
warmer, and the more utilitarian ones cooler. The clown one can be
yellow because it's funny

I'm renaming a color define here so I'm touching more files then you'd
expect

[Brightens
Niknacks](https://github.com/tgstation/tgstation/pull/73936/commits/835bae28e9eb9946be53c9f5dac0a0a39f15ef21)

Increases the light range of request consoles, status displays,
newscasters, and air alarms (keycard machines too, when they're awaiting
input at least)
Increases the brightness of air alarms, I think they should be on par
with apcs, should be able to tell when they're good/bad.
Increases the brightness of vending machines (I want them to light up
the tiles around them very lightly, I think it's a vibe)

Fixes a bug with ai status displays where they'd display an emissive
even if they didn't have anything on their screen, looking stupid.
This was decently easy but required a define. Looked really bad tho

## Why It's Good For The Game

Pretty

<details>
<summary>
Circuit Floors
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534470-c6eac5f5-5de6-40e9-897d-3212b8796d81.png)

![image](https://user-images.githubusercontent.com/58055496/224534477-ad412ad9-f7c4-44ae-ad75-a1a2c9bd17be.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534486-b7b408a3-546c-4f90-aa9f-0e58bf8128ad.png)

![image](https://user-images.githubusercontent.com/58055496/224534496-626458f7-ab63-429c-a5db-eae9c784d06a.png)
</details>

<details>
<summary>
Desk Lights
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534513-9868b0b8-bc73-4b45-b986-8445078a8653.png)

![image](https://user-images.githubusercontent.com/58055496/224534518-bbbc8c6d-b59e-4f28-a31c-6c6a7e2c2885.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534529-7988f440-03be-42ef-894c-b9e77f577ae5.png)

![image](https://user-images.githubusercontent.com/58055496/224534532-c3f2c6bf-c925-4a59-a8f9-10bb955a9942.png)
</details>

The niknack changes are more minor so I'm not gonna grab photos for
them. I can if you'd like but I don't think it's necessary. Mostly a
vibes in dark spaces sorta thing
 
## Changelog

:cl:
add: I made circuit floors brighter and more vivid.
add: Made air alarms, vending machines, newscasters, request consoles,
status displays and keycard machines slightly "brighter" (larger light
range, tho I did make air alarms a bit brighter too)
add: Tweaked desklamps. Lower range, and each type gets its own coloring
instead of just fullwhite.
fix: AI displays are no longer always emissive, they'll stop doing it if
they aren't displaying anything. Hopefully this'll look nicer
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1dad66101d...](https://github.com/tgstation/tgstation/commit/1dad66101d498eeed8aad73d17f142b631cc0f0e)
#### Tuesday 2023-03-14 22:36:49 by TheSmallBlue

All hail The Pickle Jar, harbringer of better crafting (#73939)

## About The Pull Request
Fixes #73841 

---

_It is the 12th of March, 2023. Around 3am. I have published a Pull
Request which involves circuits, and got reminded of my low GBP. I go
into the issues tab to see if there's anything someone of my low skill
caliber could tackle. I see it; Pickles.
"How hard could I be?" I ask myself, foolishly unaware of the dangers
that would soon overcome me.
Surely it must've been a mistype, I thought. Surely someone accidentally
confused pickles and cucumbers.
"Wait, the pickles are supposed to be created on the jar when the jar is
created", I say foolishly.
"Wait, its putting the ingredients used for the jar in the jar, that
doesn't explain why the pickles aren't there though", I say foolishly
"Wait, whoever tried fixing this earlier fucking qdel'd the beaker and
called it a day????", I say, foolishly._

---

Anyways I changed how the crafting menu distincts between categories,
instead of checking whether or not the path is for food, it checks the
actual categories themselves (why didn't it do this already), meaning
that you can have non-food items on the food tab if it has a food
category. Did this by adding a list that includes all crafting
categories, so in the future when adding new categories you'll have to
add them twice, which sucks, but oh well.

Also added a new variable to craftable items, which makes it so that you
can not delete a container's contents if you so wish (why was this the
default).

All this so that when you craft pickles, it actually crafts pickles
instead of cucumbers.

I spent hours on this, its 6:30am as I'm typing this. I'm tired. Fucking
pickles.

Super duper ultra thanks to FinalPotato for guiding me and suffering
with me through this and teaching me so much about DM and BYOND. I
cannot emphasize just how helpful and awesome they were thank you thank
you thank you <3
## Why It's Good For The Game

Bug fixing be good
## Changelog
:cl:
fix: The jar of pickles, after millenia, finally actually contains
pickles. All hail the jar of pickles.
/:cl:

---
## [mikeb127/pytorch](https://github.com/mikeb127/pytorch)@[d09cd15216...](https://github.com/mikeb127/pytorch/commit/d09cd152161626381cae7780bbd2c44eedeb33d7)
#### Tuesday 2023-03-14 22:38:01 by Taylor Robie

[Profiler] Defer recording startup python events (take 2) (#91684)

This is my commandeer of https://github.com/pytorch/pytorch/pull/82154 with a couple extra fixes.

The high level idea is that when we start profiling we see python frames which are currently executing, but we don't know what system TID created them. So instead we defer the TID assignment, and then during post processing we peer into the future and use the system TID *of the next* call on that Python TID.

As an aside, it turns out that CPython does some bookkeeping (https://github.com/python/cpython/blob/ee821dcd3961efc47262322848267fe398faa4e4/Include/cpython/pystate.h#L159-L165, thanks @dzhulgakov for the pointer), but you'd have to do some extra work at runtime to know how to map their TID to ours so for now I'm going to stick to what I can glean from post processing alone.

As we start observing more threads it becomes more important to be principled about how we start up and shut down. (Since threads may die while the profiler is running.) #82154 had various troubles with segfaults that wound up being related to accessing Python thread pointers which were no longer alive. I've tweaked the startup and shutdown interaction with the CPython interpreter and it should be safer now.

Differential Revision: [D42336292](https://our.internmc.facebook.com/intern/diff/D42336292/)
Pull Request resolved: https://github.com/pytorch/pytorch/pull/91684
Approved by: https://github.com/chaekit

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[33d9a0338f...](https://github.com/tgstation/tgstation/commit/33d9a0338f1d6811162479e337dbd0945463a8e8)
#### Tuesday 2023-03-14 22:39:26 by LemonInTheDark

Reworks trashbags slightly (#73761)

## About The Pull Request

I'm a bit sad about the state of trashbags. 
They're very clunky to use, so they almost never get touched. S
depressing. Let's try and fix that.

Let's make em fit in the belt slot (again), but as a tradeoff we'll make
it harder to pull one thing from your bag.
We'll give it a say, 1.5 second delay, so you can't quickdraw from em.
If you try and dump them out into something else, we'll throw any
spillover on the ground below you

I'm also doing some general code cleanup here. Making procs more
readable, vars more direct, removing some old legacy stuff.
I've added a remove_single proc to hook into via subtype, which takes a
mob as input. this has required placing extra requirement on some helper
procs, but fortunately it's not something they're unable to meet.

My hope is this will make garbage bags usable without being stupid.

## Why It's Good For The Game

I don't see these get used at all, cause they're a pain to carry around.
They got gimped because people were using them as infinite storage for
shotgun shells and other small items.
I've made using them for this sort of thing hard and slow, so I think we
oughta be fine. If not I'll do some more touching, maybe give the
autodrop a delay.

## Changelog
:cl:
balance: The janitor's trashbag now fits on his belt. In exchange,
taking something out of it sends a visible message, and has a delay.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [vbe-odoo/odoo](https://github.com/vbe-odoo/odoo)@[c68a159884...](https://github.com/vbe-odoo/odoo/commit/c68a15988432b201ae3786eb54bac3110c4242f4)
#### Tuesday 2023-03-14 23:58:32 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

X-original-commit: 97f52bd40d97109a7983549d252476959ddceada
Part-of: odoo/odoo#112325

---

