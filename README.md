## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-12](docs/good-messages/2022/2022-03-12.md)


1,448,574 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,448,574 were push events containing 2,127,593 commit messages that amount to 123,392,115 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 28 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[745426eff2...](https://github.com/tgstation/tgstation/commit/745426eff227ff556105147a4802540617decd7b)
#### Saturday 2022-03-12 00:02:20 by LemonInTheDark

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
## [laminas/laminas-servicemanager](https://github.com/laminas/laminas-servicemanager)@[1fb805d456...](https://github.com/laminas/laminas-servicemanager/commit/1fb805d456f4e916e5fbddad4d2349adfd2f05ba)
#### Saturday 2022-03-12 00:26:59 by Michał Bundyra

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
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[9223af86c1...](https://github.com/Buildstarted/linksfordevs/commit/9223af86c1820a593c0370bfe6e09c27b098b5a7)
#### Saturday 2022-03-12 01:06:01 by Ben Dornis

Updating: 3/12/2022 1:00:00 AM

 1. Added: Why Common Sense Is Not THAT Common
    (https://jovica.org/posts/common_sense/)
 2. Added: Job Search 2022 Update: Week 1
    (https://blog.urth.org/2022/03/11/job-search-2022-update-week-1/)
 3. Added: Cooking with credentials - pepper - Eric Mann's Blog
    (https://eric.mann.blog/cooking-with-credentials-pepper/)
 4. Added: I can probably hack your password in MINUTES!
    (https://docs.aista.com/blog/i-can-probably-hack-your-password-in-minutes)
 5. Added: Substack’s app: building the VC moat
    (https://onemanandhisblog.com/2022/03/substacks-app-building-the-vc-moat/)
 6. Added: My experience as a first-time contributor to open source.
    (https://ciahkarimi.hashnode.dev/my-experience-as-a-first-time-contributor-to-open-source)
 7. Added: How To Do Less
    (https://alexturek.com/2022-03-07-How-to-do-less/)
 8. Added: My favorite FFmpeg cookbook.
    (https://sergiotapia.com/my-favorite-ffmpeg-cookbook)
 9. Added: Giving Better Code Review Feedback — Laura Tacho
    (https://lauratacho.com/blog/better-code-review-feedback)
10. Added: Ethereum Is The Newsfeed We Deserve
    (https://timdaub.github.io/2022/03/11/ethereum-is-the-newsfeed-we-deserve/)
11. Added: Why I Left the Intelligence Community
    (https://dangilmore.com/2022/03/10/why-i-left-the-intelligence-community/)
12. Added: Creating a Compiler with Raku – Andrew Shitov
    (https://andrewshitov.com/creating-a-compiler-with-raku/)
13. Added: Sending Prometheus Alerts to Telegram with Telepush
    (https://muetsch.io/sending-prometheus-alerts-to-telegram-with-telepush.html)
14. Added: Collections: Nuclear Deterrence 101
    (https://acoup.blog/2022/03/11/collections-nuclear-deterrence-101/)
15. Added: MarketRank: The Anti-SEO Ranking Algorithm
    (https://dkb.io/post/market-rank)
16. Added: Guess the Startup by ttunguz

    (https://tomtunguz.com/tale-of-two-databases/)
17. Added: Why Neutrality
    (https://larrysanger.org/2022/03/why-neutrality/)

Generation took: 00:05:51.0265498
 Maintenance update - cleaning up homepage and feed

---
## [vascorsd/archlinux-packages](https://github.com/vascorsd/archlinux-packages)@[d569b338ae...](https://github.com/vascorsd/archlinux-packages/commit/d569b338aee0dc21cdc5903570e266b921b485b8)
#### Saturday 2022-03-12 01:36:51 by Vasco Dias

updated scalfix. still fucking weirdo and sucking not having a native binary and super totally focused on sbt only world. grrr

---
## [niftynei/lightning](https://github.com/niftynei/lightning)@[1f364f9ae8...](https://github.com/niftynei/lightning/commit/1f364f9ae8937e95abed39b48b1f9e8c013f06af)
#### Saturday 2022-03-12 01:50:55 by niftynei

bkpr: add journal entry for offset account balances; report listbalances

When the node starts up, it records missing/updated account balances
to the 'channel' events... which is kinda fucked for wallet + external
events now that i think about it but these are all treated the same
anyway so it's fine.

This is the magic piece that lets your bookkeeping data startup ok on an
already running/established node.

---
## [forking-repos/elasticsearch](https://github.com/forking-repos/elasticsearch)@[37ea6a8255...](https://github.com/forking-repos/elasticsearch/commit/37ea6a8255623d41be7df11440610ffa958ce50e)
#### Saturday 2022-03-12 02:19:41 by Nik Everett

TSDB: Support GET and DELETE and doc versioning (#82633)

This adds support for GET and DELETE and the ids query and
Elasticsearch's standard document versioning to TSDB. So you can do
things like:
```
POST /tsdb_idx/_doc?filter_path=_id
{
  "@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2
}
```

That'll return `{"_id" : "BsYQJjqS3TnsUlF3aDKnB34BAAA"}` which you can turn
around and fetch with
```
GET /tsdb_idx/_doc/BsYQJjqS3TnsUlF3aDKnB34BAAA
```
just like any other document in any other index. You can delete it too!
Or fetch it.

The ID comes from the dimensions and the `@timestamp`. So you can
overwrite the document:
```
POST /tsdb_idx/_bulk
{"index": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

Or you can write only if it doesn't already exist:
```
POST /tsdb_idx/_bulk
{"create": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

This works by generating an id from the dimensions and the `@timestamp`
when parsing the document. The id looks like:
* 4 bytes of hash from the routing calculated from routing_path fields
* 8 bytes of hash from the dimensions
* 8 bytes of timestamp
All that's base 64 encoded so that `Uid` can chew on it fairly
efficiently.

When it comes time to fetch or delete documents we base 64 decode the id
and grab the routing from the first four bytes. We use that hash to pick
the shard. Then we use the entire ID to perform the fetch or delete.

We don't implement update actions because we haven't written the
infrastructure to make sure the dimensions don't change. It's possible
to do, but feels like more than we need now.

There *ton* of compromises with this. The long term sad thing is that it
locks us into *indexing* the id of the sample. It'll index fairly
efficiently because the each time series will have the same first eight
bytes. It's also possible we'd share many of the first few bytes in the
timestamp as well. In our tsdb rally track this costs 8.75 bytes per
document. It's substantial, but not overwhelming.

In the short term there are lots of problems that I'd like to save for a
follow up change:
1. ~~We still generate the automatic `_id` for the document but we don't use
   it. We should stop generating it.~~ Included in this PR based on review comments.
2. We generated the time series `_id` on each shard and when replaying
   the translog. It'd be the good kind of paranoid to generate it once
   on the primary and then keep it forever.
3. We have to encode the `_id` as a string to pass it around
   Elasticsearch internally. And Elasticsearch assumes that when an id
   is loaded we always store as bytes encoded the `Uid` - which *does*
   have nice encoding for base 64 bytes. But this whole thing requires
   us to make the bytes, base 64 encode them, and then hand them back to
   `Uid` to base 64 decode them into bytes. It's a bit hacky. And, it's
   a small thing, but if the first byte of the routing hash encodes to
   254 or 255 we `Uid` spends an extra byte to encode it. One that'll
   always be a common prefix for tsdb indices, but still, it hurts my
   heart. It's just hard to fix.
4. We store the `_id` in Lucene stored fields for tsdb indices. Now
   that we're building it from the dimensions and the `@timestamp` we
   really don't *need* to store it. We could recalculate it when fetching
   documents. In the tsdb rall ytrick this'd save us 6 bytes per document
   at the cost of marginally slower fetches. Which is *fine*.
5. There are several error messages that try to use `_id` right now
   during parsing but the `_id` isn't available until after the parsing
   is complete. And, if parsing fails, it may not be possible to know
   the id at all. All of these error messages will have to change,
   at least in tsdb mode.
6. ~~If you specify an `_id` on the request right now we just overwrite
   it. We should send you an error.~~ Included in this PR after review comments.
7. We have to entirely disable the append-only optimization that allows
   Elasticsearch to skip looking up the ids in lucene. This *halves*
   indexing speed. It's substantial. We have to claw that optimization
   back *somehow*. Something like sliding bloom filters or relying on
   the increasing timestamps.
8. We parse the source from json when building the routing hash when
   parsing fields. We should just build it from to parsed field values.
   It looks like that'd improve indexing speed by about 20%.
9. Right now we write the `@timestamp` little endian. This is likely bad
   the prefix encoded inverted index. It'll prefer big endian. Might shrink it.
10. Improve error message on version conflict to include tsid and timestamp.
11. Improve error message when modifying dimensions or timestamp in update_by_query
12. Make it possible to modify dimension or timestamp in reindex.
13. Test TSDB's `_id` in `RecoverySourceHandlerTests.java` and `EngineTests.java`.

I've had to make some changes as part of this that don't feel super
expected. The biggest one is changing `Engine.Result` to include the
`id`. When the `id` comes from the dimensions it is calculated by the
document parsing infrastructure which is happens in
`IndexShard#pepareIndex`. Which returns an `Engine.IndexResult`. To make
everything clean I made it so `id` is available on all `Engine.Result`s
and I made all of the "outer results classes" read from
`Engine.Results#id`. I'm not excited by it. But it works and it's what
we're going with.

I've opted to create two subclasses of `IdFieldMapper`, one for standard
indices and one for tsdb indices. This feels like the right way to
introduce the distinction, especially if we don't want tsdb to cary
around it's old fielddata support. Honestly if we *need* to aggregate on
`_id` in tsdb mode we have doc values for the `tsdb` and the
`@timestamp` - we could build doc values for `_id` on the fly. But I'm
not expecting folks will need to do this. Also! I'd like to stop storing
tsdb'd `_id` field (see number 4 above) and the new subclass feels like
a good place to put that too.

---
## [Cupax3/BoH-Bay](https://github.com/Cupax3/BoH-Bay)@[e949b98d60...](https://github.com/Cupax3/BoH-Bay/commit/e949b98d60d0cf6f2bfceac3c6453b3fbf61e309)
#### Saturday 2022-03-12 02:45:35 by Pariah919

Ports gun attachments (#1250)

* i hate technobug

* Update gun.dm

* ok

* attachments work again

* yeah, I never added these sounds, and?

ping mjp#4043 on discord if these sounds are still not added when i wake up in 4 hours and are avaliabel

* ye

* attachments moment

* howdoesthisnotruntime

* comment less agressive, sorry

* attachies

Co-authored-by: Carl? <Stats-and-tracks@hotmail.com>

---
## [classified/android_kernel_oneplus_sm8150](https://github.com/classified/android_kernel_oneplus_sm8150)@[c43d7ae3c6...](https://github.com/classified/android_kernel_oneplus_sm8150/commit/c43d7ae3c6b686876b152043fe007cbd103de74c)
#### Saturday 2022-03-12 04:43:23 by alk3pInjection

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
## [Twaticus/tgstation](https://github.com/Twaticus/tgstation)@[906fb0682b...](https://github.com/Twaticus/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Saturday 2022-03-12 04:58:42 by necromanceranne

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
## [xja/CyberCodeOnline](https://github.com/xja/CyberCodeOnline)@[6d5cb134f2...](https://github.com/xja/CyberCodeOnline/commit/6d5cb134f217d2cfa2a14edfd3a81d4748a74fdc)
#### Saturday 2022-03-12 08:14:28 by S0M3_DUD3

Updated german commen used curse words

Translations
		"Arschfresse" - Analface
		"Arschlecker" - Anallicker
		"Arschficker" - Analfucker
		"Pimmel" - other word for dick
		"Schwanzlutscher" - dicksucker
		"Kanacke" - curse word for imigrants
		"Fettsack" - "Fat guy"
		"Schlampe" - "Bitch"
		"Mutterficker" - "Motherfucker"
		"Assi" - curse word for jobless
		"Aushilfsnazi" - nazi thing

---
## [zach1502/Ren](https://github.com/zach1502/Ren)@[84ddbd0bf0...](https://github.com/zach1502/Ren/commit/84ddbd0bf041172e5f66e2c2ed18b92b097d9f1e)
#### Saturday 2022-03-12 09:43:24 by zach1502

Stockmarket Cog

Integrates the Real life stock market into Ren!
Thought adding new ways to gain/lose credits might be fun. Also, has the added benefit of teaching people how to invest and gaining experience losing money.

Unlike Squid.py, effort was put in.

Oh, and comments... yea kinda forgot about those midway so, you got this! Its fairly simple code so should be alright without it.

Couple of issues are still present in no particular order:
- Its slow, that needs to be worked on, especially for the buy and sell functions
- The output could be prettier. 
- Buy & Sell functions are kinda messy. Needs to be cleaned up.
- For the charts, the time stamps are weird if you view a stock when its currently being traded on the market

WIP/To-Do:
- Dividends (think of it as adult allowance for the financial illiterate)
- buy/sell with the full company name instead of tickers

---
## [CoryParsnipson/invert-the-pyramid-dev](https://github.com/CoryParsnipson/invert-the-pyramid-dev)@[2e09bc11ee...](https://github.com/CoryParsnipson/invert-the-pyramid-dev/commit/2e09bc11ee1978de52ffa882f9bac3359406772c)
#### Saturday 2022-03-12 10:30:06 by Cory Parsnipson

Use request.headers.get()

You're not supposed to use request.headers['key'], the person from the
sveltekit discord said. You can't access keys using square
brackets, you need to use a getter for "security reasons. Okay. Cool.
That's fucking stupid.

---
## [KrishnakantShedge/kernel_realme_RMX1851](https://github.com/KrishnakantShedge/kernel_realme_RMX1851)@[8e8583709c...](https://github.com/KrishnakantShedge/kernel_realme_RMX1851/commit/8e8583709c0d2cd98c80e5e13e51bc93b26fb658)
#### Saturday 2022-03-12 11:21:39 by Cyber Knight

kramel.sh: Switch to LLVM Binutils for {AR, OBJDUMP, STRIP}

- GNU Binutils seem to break compilation hence let's switch to LLVM Binutils.
- Fuck you GNU.

Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[ac21ef9078...](https://github.com/Salex08/tgstation/commit/ac21ef9078d88f51a4e198e394ed56e3cc731b45)
#### Saturday 2022-03-12 11:23:43 by Pickle-Coding

No, we don't want radiation getting released in large pipenets fuck you fuckr uyu! (#65212)

* Make it harder to release radiation in large pipenets. Squares the volume / 2,500 thingy, and adds the requirements to the proto-nitrate bz response and proto-nitrate tritium response gas reactions to release radiation. This will make it significantly harder to release radiation in large pipenets, because releasing radiation in large pipenets makes it harder for people to identify the cause on why they are getting irradiated, which is bad and goes against the modern radiation goals.

Squaring is not enough for deranged people that know we don't want radiation released in large pipenets. Cubes the requirement instead. If someone could get enough gases reacting at once after this, then there is a bigger problem with atmos.

Who had fun seeing everything green, then getting irradiated and not even knowing why? I don't know, because I don't know who put the gases in waste and why we must suffer.

---
## [ShadeAware/BoH-Bay-1](https://github.com/ShadeAware/BoH-Bay-1)@[fe6e9e9f05...](https://github.com/ShadeAware/BoH-Bay-1/commit/fe6e9e9f05778ededd5f354206899b74c12ffc44)
#### Saturday 2022-03-12 12:56:57 by ShadeAware

Makeshift Weaponry expansion (#1400)

* early work, still doesn't compile, kill me

* changing some notes

* Big updato

* fhghfgdgfd

* fuck

* fuck you

* piece of shit

* Revert "piece of shit"

This reverts commit 207cb44e914315e6cbfcd45c9a801f19c945432a.

* WORK

* ereersgRRG

---
## [pikapower9080/pikapower9080.github.io](https://github.com/pikapower9080/pikapower9080.github.io)@[c2405b8fdd...](https://github.com/pikapower9080/pikapower9080.github.io/commit/c2405b8fddd6ab282446d721a6ff944204033081)
#### Saturday 2022-03-12 13:41:09 by pikapower9080

an important update with an important story
ok so basically you don't even want to know but like i accidentally made
the silly sentence generator go bye bye by mistake and yeah i fixed it
finally and also transformed my old ugly code
also i have no idea how to write a commit message without github desktop
am i doing this right?? i hope so

---
## [team-eoanb/EoaNB](https://github.com/team-eoanb/EoaNB)@[72f8e41bed...](https://github.com/team-eoanb/EoaNB/commit/72f8e41bed14568ca13fec96bbf780ba3e5c65de)
#### Saturday 2022-03-12 14:28:51 by Kenhel

Serbia Economy and extended Military skeleotn

The economy one was a pure pain anyways ima go do the final serbian tree, the political one didnt check for errors because this was a skeleton shouldnt be any errors if there is one oh my fucking god fuck me lmk and ill fix it anyways ima go shoot myself after this this was painful

---
## [Qortal/Brooklyn](https://github.com/Qortal/Brooklyn)@[9f6f847f86...](https://github.com/Qortal/Brooklyn/commit/9f6f847f8639c41bb6392fad7d836076d71f392c)
#### Saturday 2022-03-12 14:30:58 by Raziel K. Crowe

Titan's ARM Boost clock in action

Happy weekend everyone except you T3Q, fuck you!

---
## [nevimer/Skyrat-tg](https://github.com/nevimer/Skyrat-tg)@[d96e7b7e27...](https://github.com/nevimer/Skyrat-tg/commit/d96e7b7e278dd0226a4de8d9463edda37af709f9)
#### Saturday 2022-03-12 16:28:17 by SkyratBot

[MIRROR] Makes Ants glow, puts a min on ant screaming & shoe permeability, & other ant-related things. [MDB IGNORE] (#11821)

* Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

* Makes Ants glow, puts a min on ant screaming & shoe permeability, & other ant-related things.

Co-authored-by: Wallem <66052067+Wallemations@users.noreply.github.com>

---
## [CyanideTheJuggla/book-search-refactor](https://github.com/CyanideTheJuggla/book-search-refactor)@[334e3e6134...](https://github.com/CyanideTheJuggla/book-search-refactor/commit/334e3e6134373caa9e2c354cfc4529bd28f9bb5e)
#### Saturday 2022-03-12 17:50:42 by Scott Howell

fuck this stupid shit

did a bunch of work, going to fuck it out 0of here now so whats the point of committing or mentioning what the fuck I actually did, fuck this stupid assignment

---
## [freesewing/freesewing](https://github.com/freesewing/freesewing)@[67da7dd595...](https://github.com/freesewing/freesewing/commit/67da7dd5950f3e3ed39a190c23f3cd8b095cd93f)
#### Saturday 2022-03-12 17:55:37 by Joost De Cock

feat(lab): First stab at custom layout

This adds a React component to handle custom layouts.
This React component is a long way from perfect, but it's a start.

There are two reasons that (at least in my opinion) implementing this is non-trivial:

1) React re-render vs DOM updates

   For performance reasons, we can't re-render with React when the user drags a
   pattern part (or rotates it). It would kill performance.
   So, we don't re-render with React upon dragging/rotating, but instead manipulate
   the DOM directly.

   So far so good, but of course we don't want a pattern that's only correctly laid
   out in the DOM. We want to updat the pattern gist so that the new layout is stored.
   For this, we re-render with React on the end of the drag (or rotate).

   Handling this balance between DOM updates and React re-renders is a first contributing
   factor to why this component is non-trivial

2) SVG vs DOM coordinates

   When we drag or rotate with the mouse, all the events are giving us coordinates of
   where the mouse is in the DOM.

   The layout uses coordinates from the embedded SVG which are completely different.
   So we need to make this translation and that adds complexity.

3) Part-level transforms

   It's not just that the DOM coordinates and SVG coordinate system is different, each
   part also has it's own transforms applied and because of this behaves as if they have
   their own coordinate system.

   In other words, a point (0,0) in the part is not the top-left corner of the page.
   In the best-case scenario, it's the top-left corner of the part. But even this is
   often not the case as parts will have transforms applied to them.

4) Flip along X or Y axis

   Parts can be flipped along the X or Y axis to facilitate a custom layout.
   This is handled in a transform, so the part's coordinate's don't actually change. They
   are flipped late into the rendering process (by the browser displaying the SVG).

   Handling this adds yet more mental overhead

5) Bounding box

   While moving and rotating parts around is one thing. Recalculating the bounding box
   (think auto-cropping the pattern) gets kinda complicated because of the reasons
   outlined above.

   We are currently handling a lot in the frontend code. It might be more elegant to move
   some of this to core. For example, core expects the custom layout to set the widht and height
   rather than figuring it out on its own as it does for auto-generated layouts.

 Known issues

 - Rotating gets a little weird sometimes as the part rotates around it's center in the
   SVG coordinate system, but the mouse uses it's own coordinates as the center point that's
   used to calculate the angle of the rotation

 - Moving parts into the negative space (minus X or Y coordinated) does not extend the bounding box.

 - Rotation gets weird when a part is mirrored

 - The bounding box update when a part is rotated is not entirely accurate

I've sort of left it at this because I'm starting to wonder if we should perhaps re-think
how custom layouts are supported in the core. And I would like to discuss this with the core team.

---
## [fsociety-tribute/sunfish](https://github.com/fsociety-tribute/sunfish)@[e7b610a136...](https://github.com/fsociety-tribute/sunfish/commit/e7b610a136517b202bbe9b7e4ef2c6be72038f7a)
#### Saturday 2022-03-12 18:22:06 by Peter Zijlstra

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
## [newstools/2022-express](https://github.com/newstools/2022-express)@[4249a3ae35...](https://github.com/newstools/2022-express/commit/4249a3ae352dc2106ba671c61f5882714278ec86)
#### Saturday 2022-03-12 18:53:12 by Billy Einkamerer

Created Text For URL [www.express.co.uk/celebrity-news/1578615/love-island-amy-hart-trolls-instagram-shocked-ugly-boyfriend-age-news-latest-update]

---
## [Bradenbertrand/WordleLeaderboards](https://github.com/Bradenbertrand/WordleLeaderboards)@[7d72802679...](https://github.com/Bradenbertrand/WordleLeaderboards/commit/7d72802679f537457a40fe743ee03afdce1b1752)
#### Saturday 2022-03-12 20:32:18 by Bradenbertrand

Update getSolution.js

more frustrating attempts at figuring this out before I leave for work in 30 min (sorry to employers looking at this ik its not a journal but fuck it mcnugget)

---
## [Omicron166/LNS](https://github.com/Omicron166/LNS)@[9bed171a9d...](https://github.com/Omicron166/LNS/commit/9bed171a9d7085bb5a25a4c8d9c206a98bec67ad)
#### Saturday 2022-03-12 20:46:04 by Omicron166

new url parser

go fuck yourself urllib, no more problems with url ports

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[2ea74a33fa...](https://github.com/mrakgr/The-Spiral-Language/commit/2ea74a33fa33f2894aaa41c6847627ef761b3faa)
#### Saturday 2022-03-12 20:50:44 by Marko Grdinić

"9:10am. Let me chill a bit and then I will start. Killing Bites is out.

9:25am. Let me start. Yesterday the image finished. I was afraid it would take a lot longer, but it took exactly 4x as long as the 0.01 version.

Focus me, close down the twitter. Let me make that post. After that...I should try placing it underwater. That just means uptting it behind a refractive surface in this case.

///

Here is V-Ray when it works well. I had to render it for an hour to get rid of the noise, and this image should make for a decent wallpaper. It is half complete at this stage, I still need to add the girl and make the camera below the surface of the pool. There are about 300 branches with flowers on them and 5000 flowers in the scene. Not all of them were captured in this particular shot. Not something I've want to attempt painting by hand. Houdini attracted me due to its ability to scatter points and instantiate the objects. Blender has started to get the capability to do this with its geometry nodes, but it nowhere near Houdini's level. After I do the above as well as finish the rest of the scene, I will have completed my first mastery challenge. I hope I can get faster at making these kinds of illustrations.

///

9:50am. Focus me, let me post it on Twitter as well.

10:15am. https://twitter.com/Ghostlike/status/1502573403605291015

Here it is.

It was almost 4 months since the last tweet. I did a long thread.

Let me try putting it underneath the surface water.

10:25am. I do not understand water. Is it reflective or refractive or what? It is definitely refractive.

Come to think of it, V-Ray has a preset for water. Let me just use that.

10:25am. High reflection and high translucency. They are not all the way maxed out and but it is close. It also has a bit to fog as expected - this explains why the sea gets darker as the depth increases, the light gets trapped. The diffuse color is pure black. I am going to have to make a collection of materials if I want to create interesting scenes. This will be a part of being an artist. Right now, I am very rough in my conception of materials.

10:30am. Houdini literally has an oceanic waves node. Let me read the docs for it.

https://www.sidefx.com/docs/houdini/nodes/sop/oceanwaves.html

I do not know how to use this. Let me look up some tutorials.

https://youtu.be/ZpGjSfYi5vo
Houdini Breakdown/Tutorial - Wave in a box Part 01

10:40am. https://www.sidefx.com/docs/houdini/dyno/ripples.html

There are tools specifically for ripples.

> The Ripple surface node deforms a grid to add concentric ripples. You can animate this node’s parameters to “fake” simple ripples, or use it to set up the initial conditions for a true dynamics ripple simulation.

This might be what I need.

> Waves can rebound against edges. You can paint attributes to create areas of fast, slow, or no wave propagation.

This sure beats having a paint brush.

10:45am. Ah, let me just watch the video. I might as well explore this aspect of Houdini a little.

https://youtu.be/ZpGjSfYi5vo?t=1161

This is so complicated. For things like giant waves and such I'd honestly consider just sculpting them.

11:10am. https://cgpersia.com/2022/02/isotropix-clarisse-ifx-v5-0-sp7-win-x64-182421.html

I had a hunch to check out whether Clarisse is on CGPersia. It is. Let me download it. I'll consider giving it a try.

...Ah, it is actually way smaller than I thought. Since it is split into 3 pieces I thought it would be 3gb, but each of the pieces are 250mb. Piece of cake.

Houdini really can't handle very heavy geometry, so if Clarisse could do that, it would be worth considering. It is not like I can't use both tools.

Now let me finish the ocean tutorial.

11:25am. Let me watch more water stuff in Houdini.

https://www.youtube.com/results?search_query=houdini+ocean

Even though my prefered approach to this would be sculpting, it is worth spending some time on this. Riples do not need to be fancy.

https://youtu.be/vi0WIWHLBqY?t=9

This is a good globe. I'll want to be able to build something like this.

https://youtu.be/vi0WIWHLBqY?t=16

This was a great animation. 5/5.

https://youtu.be/vi0WIWHLBqY?t=35

It seems a decent amount of these tools are not simulation based. These are those that I should use.

https://youtu.be/vi0WIWHLBqY?t=107

This is definitely of interest to me. That small box tutorial was useless to me. I should not have wasted my time on it.

https://youtu.be/vi0WIWHLBqY?t=187

Titanic was the first time CG generated oceans were used in a film.

https://youtu.be/vi0WIWHLBqY?t=984

He says he will not be doing the ocean foam. A pity, I'll have to look at it separately. Ocean Spectra is great. While Flip seems are complicated, this node is one I'll be able to dive into. I'll have to look into the ripple tools as well.

12pm. Let me just make a remark that it really a pity how much interesting shader stuff is CPU based. Maybe AI chips will end up being be more suitable for this kind of work than GPUs. To make proper use of GPUs I will have to dive into doing my own textures. I can always convert painted attributes to images and then use those on a low poly mesh.

https://www.sidefx.com/forum/topic/49823/?page=1#post-225552

Interesting stuff here on this subject.

///

Guys, I think the question is good. I don't see why you need to recommend other softwares instead of answering the question.
I often need to paint a quick mask to use outside of Houdini in a game engine. Painting directly on 3D model into texture would be a nice option.
Right now I have to paint on subdivided mesh and then bake it into texture which take a lot of unnecessary time.

///

Painting on a subdiv'd mesh and baking it is the idea I had. I myself would just remesh while keeping old edges intact. Though I haven't yet made sure that this keeps UVs. I think it should given that I've seen some UV preserving considerations in that node.

> second is to scatter huge amount of points onto your geometry, paint with paint node on points and then transfer color in shader back to mesh

I haven't considered this.

Texture Painting | Quick start | Blender | 3min

Let me watch this.

https://youtu.be/LcCQKuWPhXk?t=200

This is actually quite nice. I could do flavors a lot more easily than with attributes. Yeah, just what was I thinking trying to stick to attribute painting. I should study texture painting properly.

12:10pm. But then again it is not like I tried the proper thing of putting a lot of geometry on attributes either and then painting that.

Let me go back to watching the ocean tools.

https://youtu.be/Z81I1sX6izI
HOUDINI POLYPAINT TOOL | PAINTING, ANIMATING AND DRAWING

This caught my attention. Houdini does not have this built in though.

12:35pm. Oh, Clarisse finished. The third file is actually the MACOS version so I don't need to bother downloading it.

12:45pm. It loads very fast. Ok, nevermind it for now. I'll leave it sitting there until later.

12:50pm. https://youtu.be/vi0WIWHLBqY?t=1829

Let me stop this video here.

Let me move on. This simulation stuff is not of interest to me.

12:55pm. https://youtu.be/c_GsYJfV-rM
Using The Ripple Solver

Let me watch this for a bit and then I will stop for breakfast. I'll play around with this after that.

https://youtu.be/c_GsYJfV-rM?t=420

Hmmm, do the Hexpressions not have operator precedence?

https://youtu.be/c_GsYJfV-rM?t=494

Let me stop here. Time for a break.

I've been distracted all morning, but I'll finish this soon and start getting things done. I want to get the pool out of the way so I can deal with the rest of scene. I don't want to linger too much on this.  Ideally I'd finish this today, so I can move to sculpting Luna. After all this is done I'll put the scenes together, shade them and finish the mastery challenge.

2:45pm. Done with breakfast and chores.

2:50pm. Let me resume the tutorial. I should forget everything else and go for it.

https://youtu.be/c_GsYJfV-rM?t=537

Is he just doing Distance From Geometry using VOPs?

https://youtu.be/c_GsYJfV-rM?t=711

Couldn't he have used the transfer attribute for this? I bet that could have worked as well.

https://www.sidefx.com/docs/houdini/nodes/sop/ripple.html

No, this does not have enough functionality to satisfy me. I won't be able to deflect the ripples around the body. Nor will I be able to set it so that the ripples propagate outwards from it. Since it is a pool I am imagining the ripples coming from Luna herself, so it makes sense that they would spread outward.

In fact that should come directly from the edges. I'll have to think about this. I'll probably have to boolean out the grid and then just displace the edges.

Ok, but that is for the future when I've actually sculpted and rigged Luna. Right now I just want to see the visual effect of the ripple so the Ripple node should do nicely.

3:25pm. An alternative would just be to apply multiple ripple nodes. But that could lead to them overlapping. Let's not do that.

I looks like shit. I need to fiddle with the settings. Let me first get rid of the fog for the water.

Ah, no wait, I forgot that I turned off the light dome.

3:30pm. I just figured out how to use quickmarks. This will improve my navigation ability 500%. I just have to press Ctrl+number to set them and then I can use the number keys to move around. Previously I've been using two windows or doing it manually.

3:40pm. Houdini objects take an enormous amount of memory for whatever reason. In this particular case, I'd be much better off if I could make the surface a displacement map.

Let me lightly shade the pool itself.

For the ladder...I'll go with the blurry silver preset.

I do not what the perfect mix of green and blue is called, but I'll go with it for the pool color. Won't bother messing with roughness at the moment. Since the camera won't be on them anyway, I can leave the wet spots for later. I'll also make the fog depth pure white so the light just passes through. It will make it easier on the renderer.

3:50pm. Let me take a look at how it looks with the vines. I'll let it render in progressive mode for a few minutes. I'll also try the denoiser.

I should be forgiving of V-Ray's mismatch between the GPU and CPU capabilities. GPUs can't compete with CPUs in versatility so this much is only to be expected.

4pm. Good enough. I'll have to decide what I want in the final shot. Riples are nice, but not if they detract from the image quality too much. I could have the best of both worls by simply making the waves short.

4:05pm. Let me think, do I just finish the rest of the scene here? Yeah, let me do it. It has been a long time coming. Let just do it today. I'll conquer this and move on with my plans. First let me make the roughness patches around the pool.

4:25pm. Houdini crashed. It was starting to do strange things before that. And I was not prompt enough in saving. I wonder how much did I lose.

4:40pm. What the hell. I was wondering why scatter was not working properly. Now I've looked underneat and I see that the radius works way differently there for some reason.

...And the reason for that is because I am not just looking at the tiles, but the big box inbetween them! Ahhhh, right.

4:50pm. I am thinking what I shold do about this and the decision is to just remove the box. Alternatively, I could lay down some points.

4:55pm. No, the answer is - put it in a group! A primitive group is something that boolean won't remove. Now when it comes to doing the scatter I can just select the other group. More specifically the faces on the top.

5:20pm. I finally managed to figure out how to scatter the points properly. I should have just spray painted it to be honest. I have a fetish for trying to do thing programatically.

My workflow is quite inefficient because I am wasting time generalizing where I should not.

Now let me texture the tiles.

This will take some work to separate out.

5:25pm. Well, as far as my inefficiency is concerned, I will be able to improve upon that by simply planning things through better once I have the necessary experience. Right now I am still in the experimentation stage.

5:50pm. I just love it when V-Ray ignores the output node and I have to waste time going in there and switch to it by hand.

6:30pm. It is not like this when I apply noise at the geo level, but moving the noise scale at a decent level literally does nothing. It is unfuriating.

6:35pm. Ok, it is time to note this down.

Apart from ridged fractal, trying to modify any of the other settings gives me absolutely negligible difference in noise patterns. If there are, they sure aren't visible in color intesities.

It isn't like this when I use Houdini's native noises and try changing lacunarity or roughness. Maybe the problem is with the renderer, and I am simply not letting it run long enough to see a noticeable difference.

Lunch time.

7:05pm. Let me resume. I've been thinking and no matter how I look at it, my texturing workflow is a failure. I am going to give Clarisse a try for my next challenge. When I ran it earlier, it had a way faster startup than Houdini which is a good sign. Houdini is very slow, much like Clip Studio. I always dread trying to open either of these.

But for now let me finish what I have. I need those exp points.

7:10pm. I am done with the water splashes on the tiles. Now..

7:20pm. Got the splashes on the pool itself.

Now what is next? The props.

7:25pm. No, let me stop here. Not for the day, just with Houdini. The way the texturing is coming out does not fill me with pride. The flower shot that I did come out decently well, but the scene as a whole is extremely underwhelming.

It lacks the oomph that shading was supposed to give me. I thought that things would get better once I dove into V-Ray, but applying it to this scene ends up with a very plastic look. The way to get better results is to apply noise patterns and refine them, but I can't get that plan going.

That rusty metal hinge I posted in the Houdini thread was very good despite its simplicity.

But V-Ray is simply not good for real time rendering development that I am trying to get out of it. Maybe I'd have gotten better results by simply going back to Blender.

7:35pm. Let me study Clarisse here. I'll go through the tutorial for it. It is not like I am getting paid for finishing this. I got one good thing out of it.

Since Clarisse does not have a GPU renderer I might be able to import the stuff there and render it in V-Ray in Houdini.

For noise, instead of trying to mess with shaders, I should have done it on the CPU and mapped it onto a texture that the GPU can consume.

Given's V-Ray buginess and GPU restrictions I am honestly not sure if the different noise patterns not working is a consequence of that. It would absolutely be plausible that it would silently fail. V-Ray doing the right thing design wise is more exception than the rule. V-Ray is basically only good for rendering the whole thing once it has been set up and absolutely nothing else.

Right now even if I wanted to do lookdev with the native renderer, nothing shows up when mapped to the V-Ray shaders.

7:40pm. Let me give it a shot. If I can't do anything art wise by the end of the year, I'll give up and get a programming job like the rest of the losers.

https://www.youtube.com/c/isotropix
> Clarisse streamlines 3D content creation for CG artists, letting you work interactively and iteratively on final images thanks to its powerful, artist-friendly look development, lighting and rendering capabilities.

Since Clarisse is selling itself on this, I might as well go for it.

https://www.youtube.com/playlist?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf
A Beginner's Journey with Clarisse

https://youtu.be/bQugIY3QGu4?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=18

Hmmm, really? This looks very nice.

https://youtu.be/bQugIY3QGu4?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=160

I don't like this. This is more similar to Blender than Houdini.

https://www.youtube.com/watch?v=SMz9HDLm4AM
Clarisse iFX: Fantasy City Making-of

I want Clarisse to sell me on it a bit more before I dive in. This looks really great, but just imagine trying to do the lookdev for this in Houdini. One thing which perked up my attention yesterday was reading about Clarisse's scatter capabilities. And procedural texturing really got me going.

https://youtu.be/4n0ZVxb-xqA
Monsoon - Large Scale Environment Creation Using Clarisse and Photoshop

This looks really great. I'll watch this later.

For now, let me skip ahead in the tutorial. I want to see what procedural layouting has. I had this hunch that this was a really important subject ever since I saw how to do it in Blender, in fact, scattering objects is why I picked up Houdini. The rest is just a bonus. But if I can get better results using a different program, I will ditch Houdini.

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=500

The nodes are in the material editor. And it seems they have special scattering objects.

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=624

It renders very quickly.

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=750

These are a lot of pebbles. By the time I reached 5k flowers in Houdini, it started grinding noticeably. A peble should not be that much more difficult than a flower, but it depends on how much geometry the pebble has.

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=982

This is kind of selling me on it. I messed with gradient textures a lot so I can appreciate how much easier this looks here than it was for me in Houdini.

...Come to think of just how many trees did he put in that scene? It looked to be a couple of thousand. And indeed I did no notice any noticeable slowdown.

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=1164

Here he will make the stars by using a huge sphere and applying a point cloud. This is how I made the .exr in Blender.

8:55pm. Ok, I'll give Clarisse a serious try. It does not matter if I finish the scene in Houdini if it looks like it will end up looking bad.

9pm. I created a box. I am looking to the right and I see there is a volume tab. It caught my eye because it was open initially. It has dimensions there. I can change the dimenion of the box respective to a particular axis like in Blender, but what I also see is that box has density options, including falloff. There is a ramp there. This is pretty remarkable.

9:10pm. Based on the previous video, I suspect that unlike Blender, Clarisse does have a sensible browser. It is a massive pain in the ass in Blender to move objects from and to different collections. Remember how I'd erase a collection and it would spill into the outside one? Super annoying.

And parenting would put the children inside the parent in the browser. Try to move the parent to a different collection and the children remain where they are, they get spilled outside.

This was ultra annoying while working with objects in Blender for me.

9:10pm. Maybe I should watch Magic Rock tutorial in Houdini, just so I can see how he goes about texturing it if nothing else. Probably not in the shaders themselves.

In theory, what I had in mind in Houdini was a good idea. Rather than bake infinite procedural textures into a bitmap, it makes more sense to work with them at shader time. But none of that matters if the tool you are using is too slow to be practical at that stage.

https://youtu.be/bQugIY3QGu4?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=327

Actually, locking a context to a 3d view is a great idea. In Houdini I am contantly forced to jump around toggling visibilities by hand.

https://youtu.be/bQugIY3QGu4?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=475

I am having trouble following this. 9:25pm is not a time to start a new learning session. Let me finish watching this and I will stop for the day.

https://youtu.be/bQugIY3QGu4?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=545
> It has raytracing occlusion. It makes placing object close together and checking for object penetration very convenient.

This was actually one of the issue for me in both Houdini and Blender. Even though this is the most basic of tutorials, it has things new to me.

https://youtu.be/bQugIY3QGu4?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf
Beginner's Journey with Clarisse - Part1 - Fundamentals

Let me leave this link here for tomorrow. In order to get it I am going to have to play with it. Now that I have experience in both Houdini and Blender, learning Clarisse should be a lot easier than if I was starting from scratch, so I have that going for me.

9:35pm. I am going to get that Houdini and Clarisse course from CGPersia. Clarisse is such an unknown program and does not have much a community compared to anything else that I've seen. I only heard about it due to that procedural texturing tutorial on Youtube.

https://cgpersia.com/2021/04/the-gnomon-workshop-3d-landscapes-with-houdini-and-clarisse-176661.html

4.5gb. I'll leave downloading it for the next few days, starting tomorrow.

Some of the other courses in Clarisse are also on environment building. Exactly what I want to get good at. That I can find courses covering this is an indication of what the program itself is good at.

9:45pm. Let me close here early for once. Tomorrow I'll go through the beginner tutorial. It might be worth it to try recreating that intro scene. It actually looks better than the one I spent month making.

9:50pm. As a stress test, I should take those flowers and see how many of them Clarisse can fit onto the screen. Will it start grinding like Houdini and Blender? It will have to be something to find out."

---
## [xclaesse/wrapdb](https://github.com/xclaesse/wrapdb)@[7e69bfce97...](https://github.com/xclaesse/wrapdb/commit/7e69bfce97df6ef5d70e556ca4059e8f5f38af3f)
#### Saturday 2022-03-12 21:50:15 by Eli Schwartz

openjp2: Use wrap fallbacks instead of thirdparty

The thirdparty directory provided by upstream contains (old) versions of
projects we already have in the wrapdb. There is zero value in
permitting or encouraging this usage.

Also, the actual dependency lookups suck. e.g. the zlib logic, even when
probing for system versions, tries to find a pkg-config dependency, then
probes for 3 different library names, falls back to subproject() on a
subproject that doesn't exist in the wrap itself, with incorrect usage
of found(), and finally subdirs into the custom copy.

Half of this doesn't work, and all of it is redundant since meson
includes its own robust finder logic that does library probing correctly
in a cross-platform manner under the name... "zlib", just like the
pkg-config dependency.

Furthermore, ***upstream agrees with us***. To quote their own README:

```
This directory contains 3rd party libs (PNG, ZLIB)...

They are convinient copy of code from people outside of the OpenJPEG community.
They are solely provided for ease of build of OpenJPEG on system where those
3rd party libs are not easily accessible (typically non-UNIX).

The OpenJPEG does not recommend using those 3rd party libs over your system
installed libs. The OpenJPEG does not even guarantee that those libraries will
work for you.
```

This is so un-recommended by literally everyone everywhere, that
continuing to provide broken versions here is an intolerable thing.

What upstream wanted, really, was a build system that supported meson wraps.
Then they could have never included a thirdparty directory, but provided
subprojects/*.wrap "solely for ease of build on systems where those libs
are not easily accessible". It's a match made in heaven!

...

Also while we are at it, ditch the commented out copy of astyle, which
was built as an executable because a manually run maintainer shellscript
would execute the forked "openjpstyle" for you. It's totally unneeded by
the wrap, and even if it was considered interesting, it must go through
the standard wrap review && release process.

Move the remaining simple dependency() calls to the subdir that needs
them, which is already guarded by a project option.

Co-authored-by: Xavier Claessens <xavier.claessens@collabora.com>

---
## [m4cey/remote-spotify](https://github.com/m4cey/remote-spotify)@[08ef448c45...](https://github.com/m4cey/remote-spotify/commit/08ef448c45ae918bdd08b35db505da59962fe24a)
#### Saturday 2022-03-12 21:53:31 by m4cey

reset those nifty fucking tokens omg I fucking hate this bug it drove me mad

---

