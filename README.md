## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-25](docs/good-messages/2022/2022-01-25.md)


1,744,410 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,744,410 were push events containing 2,763,594 commit messages that amount to 223,271,683 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [lozzoc/kitty-kmk-nodejs-swift-uikit-widgets](https://github.com/lozzoc/kitty-kmk-nodejs-swift-uikit-widgets)@[a94a795836...](https://github.com/lozzoc/kitty-kmk-nodejs-swift-uikit-widgets/commit/a94a79583686a91d1704df761598bff7c486d909)
#### Tuesday 2022-01-25 00:04:25 by Conner Maddalozzo

finished coredata overall also life improvements

core data... easier? idk, it seems like abunch of nil coalescing to unwrap optionals, also i ahve no idea how to inspect core data objecsts

push notification deep linking works

life cycle improvements, persisted store updates as needed i belive
holy shit.

---
## [RandomTales/Naruto_Ninpou](https://github.com/RandomTales/Naruto_Ninpou)@[32f854d563...](https://github.com/RandomTales/Naruto_Ninpou/commit/32f854d563dd24bb8044f996059e59e49cc5e2c3)
#### Tuesday 2022-01-25 00:05:34 by MetalfOxXer

changes

nerf shisuis E bonus dmg to 2% per lvl instead of 3%
reduce the time the hero disappears by using bunshins by half, so it atleast takes some skill to dodge
increase the damage of Madara's tengai shinsei in his Perfect Susano form to 15xgen magic damage instead of 10xgen magic damage.
reduce explosive tag dmg to 1000 instead of 1500
increase Anko's D cooldown
reduce Flash bomb silence to 2secs
reduce Zabuza's Q range by 100
remove the category from itens like uchiha sword, uchiha shield, akatsuki ring. Just makes combining itens a bit less annoying
reduce Gaaras pause duration on his Q by atleast 0.5 secs
decrease Hinata's Hakkesho Kuuten T area of effect from 800 to 600, 800 is a bit too much for such a strong ability that also gives her invulnerability
slow down the fire ball from Yugito's T a bit instead of decreasing the range
Ichigos stat gain seems to be incorrect. At lvl 50 he should have more nin and gen but all his stats have the same amount (137)
add a 0.1x tai scaling to the shark in mugensame, they currently deal 146 normal dmg, at 500 tai they would deal 196.
add aoe indicators to Borutos spells
add a audio clue to mifunes d for his allies to hear
temari's Evasion from W is sometimes permanent, making temari or her allies immune to Auto attacks
Make Neji immune to crowd control spells like roots and stuns and wire string during his R so he doesnt get bugged.

---
## [fulpstation/fulpstation](https://github.com/fulpstation/fulpstation)@[c449fbb56c...](https://github.com/fulpstation/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Tuesday 2022-01-25 00:22:38 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[57ea2d4dcb...](https://github.com/cockroachdb/cockroach/commit/57ea2d4dcbaf6cbca7f2761b9776dac0f5975fb2)
#### Tuesday 2022-01-25 00:28:13 by craig[bot]

Merge #68488 #75271 #75293 #75303 #75304 #75436 #75443 #75447 #75462

68488: server: add verbose logging when graceful drain range lease transfer stalls r=knz a=cameronnunez

Informs #65659.

Debugging graceful drain is challenging due to limited information. It is not clear what
is going wrong from the logs. This patch adds more detailed logging when graceful drain
range lease transfer encounters issues. Specifically, range lease transfer attempt
information (when an attempt occurs, duration blocked on transfer attempt, and the lease
that is being transferred) is logged.

The reason behind the failure of the transfer attempt may not be logged on the
draining node. This is because this information lies on the node that serves the draining
request. Currently, we do not have logging that aggregates all of this information
in one place. See #74158.

Release note (cli change): If graceful drain range lease transfer encounters issues,
verbose logging is automatically set to help with troubleshooting.

75271: sql,server: create toString to role option r=maryliag a=maryliag

Previously, the code was using roleOption.String() to
create a string to be used on queries. This was causing
an issue with roles that contained spaces within it,
e.g. role option `VALIDUNTIL` was being translate to
`VALIDUNTIL` instead of the correct way `VALID UNTIL`.
This commit updates the String() function to correctly
add the space on the `VALID UNTIL` case.

Release note (bug fix): Update the String() function of
roleOption to add a space on the role `VALID UNTIL`.

75293: backupccl: reuse allocated tenant prefix in rekey r=dt a=dt

Release note: none.

75303: migrations: make sure public role gets privs on public schema r=ajwerner a=rafiss

This matches up with how the public schema gets created in a
non-migration scenario.

Release note: None

75304: execbuilder: deflake TestExecBuild r=irfansharif a=irfansharif

Fixes #74933. This test asserts on physical plans of statements after
moving ranges around, i.e. whether distsql execution is "local" or
"distributed". This is determined by:
- where the distsql planner places processor cores,
- which in turn is a function of the span resolver,
- which delegates to the embedded distsender,
- which operates off of a range cache.

The range cache, like the name suggests, can hold stale data. This test
moved replicas of indexes around to induce distributed execution, but
was not accounting for the caches holding onto stale data. In my test
runs every so often I was seeing stale range descriptors from before the
relocate trip up the planner to generate a local execution, flaking the
test. Fortunately for us, all we need to do is slap on a retry. To
repro:

    # Took under a minute on my gceworker. Helped to trim down the test
    # file slightly.
    dev test pkg/sql/opt/exec/execbuilder \
      -f 'TestExecBuild/5node' -v --show-logs \
      --stress --stress-args '-p 4'

Release note: None

75436: kvserver: de-flake TestProtectedTimestamps r=irfansharif a=irfansharif

Fixed #75020. This test makes use of an "upsert-until-backpressure"
primitive, where it continually writes blobs to a scratch table
configured with a lower max range size (1<<18 from the default of
512<<20) until it experiences replica backpressure. Before #73876 (when
using the system config span), the splitting off of the scratch table's
ranges happened near instantly after the creation of the table itself.
This changed slightly with the span configs infrastructure, where
there's more of asynchrony built in and ranges may appear after a while
longer.

The test previously started upserting as soon as it created the table,
being able to implicitly rely on the tight synchrony of already having
the table's ranges carved out. This comes when deciding to record a
replica's largest previous max range size -- something we only do if the
replica's current size is larger than the new limit (see
(*Replica).SetSpanCnfig). When we weren't upserting until the range
applied the latest config, this was not possible. With span configs and
its additional asynchrony, this assumption no longer held. It was
possible then for the range to accept writes larger than the newest max
range size, which unintentionally (for this test at least) triggers an
escape hatch where we avoid backpressure when lowering a range's max
size below its current size (#46863).

The failure is easy to repro. This test runs in ~8s, and with the
following we were reliably seeing timeouts where the test was waiting
for backpressure to kick in (but it never did because of the escape
hatch).

    dev test pkg/kv/kvserver \
      -f TestProtectedTimestamps -v --show-logs \
      --timeout 300s --ignore-cache --count 10

De-flaking this test is simple -- we just wait for the table's replicas
to apply the latest config before issuing writes to it.

Release note: None

75443: ui: removed formatting to statements on the details pages r=THardy98 a=THardy98

**ui: removed formatting to statements on the details pages**

Previously, statements displayed on the statement/transaction/index
details pages were formatted (formatting was added to allow for better
readability of statements on these detail pages). However, statements
queries from the frontend were noticeably slower due to this
implementation. This change reverts the changes to statement formatting
(updates the fixtures to show the non-formatted statements), but keeps
the change that uses statement ID as an identifier in the URL instead of
the raw statement.

**Release note (ui change)**: removed formatting to statements on the
statement, transaction and index details pages, change to replace raw
statement with statement ID in the URL remained.

75447: storage: fix `EngineComparer` ordering of bare suffixes r=jbowens a=erikgrinaker

For generalized range key support, Pebble now requires bare key suffixes
to be comparable with the same ordering as if they had a common user key
prefix (see [cockroachdb/pebble#08c5d46c75722b9527c360ca1e7069c0d2286e59](https://github.com/cockroachdb/pebble/commit/08c5d46c75722b9527c360ca1e7069c0d2286e59)).

This patch modifies `EngineComparer` to satisfy that requirement.
Previously, such suffixes would sort in ascending timestamp order
rather than the correct descending order.

Release note: None

75462: pgwire: fix a flake in TestAuthenticationAndHBARules r=cameronnunez a=knz

Fixes #75286.

The regexp was sometimes capturing the conn_end event from the
previous test directive.

Release note: None

Co-authored-by: Cameron Nunez <cameron@cockroachlabs.com>
Co-authored-by: Marylia Gutierrez <marylia@cockroachlabs.com>
Co-authored-by: David Taylor <tinystatemachine@gmail.com>
Co-authored-by: Rafi Shamim <rafi@cockroachlabs.com>
Co-authored-by: irfan sharif <irfanmahmoudsharif@gmail.com>
Co-authored-by: Thomas Hardy <thardy@cockroachlabs.com>
Co-authored-by: Erik Grinaker <grinaker@cockroachlabs.com>
Co-authored-by: Raphael 'kena' Poss <knz@thaumogen.net>

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[61de6ff6cd...](https://github.com/i3roly/glibc_ddwrt/commit/61de6ff6cdd0932f4e0e51c859b3f3107cbbb131)
#### Tuesday 2022-01-25 00:29:46 by gagan sidhu

48194/4.14.262 MWDS+update @vschagen's hw crypto. "autotune is autopoon" - randy marsh

sort of a notable update

- softether is now the latest version (both in the lootbag and bigger versions)
- updated smbd
- added the dynamic/mixed WDS feature, but it won't dump the number of connected clients in site survey.
	- maybe the RALINK guys haven't updated the site survey to do that. not sure.
		-either way, it's there
- updated @vschagen's mtk-eip93 hardware crypto driver to the latest/final version
- updated the kernel too
- ripped a small bit of @hanwckf's changes to the raeth code, particularly something to do with resetting the PPE
	- it's on his 4.4 repo.
		-seems like he's silently ninjaing off to 4.4 instead of the padavan 3.x lol.
	- I SEE YOU, FRIEND!!

this took a bit more time than i expected it to, especially the MWDS feature.
	- but now i'm probably the only guy (sorry @paldier u know i wub you) with it on a the mt_wifi 5.x.x.x series driver

nothing to report on the "marsh signing front". the man is clever, what can the redskins say? it seems with each passing day he grows more clever with how he deploy his literary weapon of choice.

nonetheless, we don't fuckin care.

go you-know-what yourself,

the mf redskins

* Shelly's room, evening. Randy knocks on her door *

Randy
        Shelly, that's enough time on your phone.

Shelly
        Leave me alone, Dad! Stop nagging me all the time!

Randy
        You know we're all cutting down on phone time.

Shelly
        [sits up]

        Don't limit me! You don't even understand me!

Randy
        [sees a poster of himself as <'famous' "musician">,
        his secret identity]

        Yeah. I don't understand you at all. A lot you know.

        [walks away saddened]

        *   The Marsh garage    *

*  Randy is adding more stacks of cash to those already  *
*    hidden behind the poster. A door opens and Randy    *
*            quickly seals it up.                        *

* He gets to his workbench just as Stan closes the door. *

Stan
        Uh hey Dad. I need to talk to you.

Randy
        Oh really? A-About... about what?

Stan
        Dad, is it possible for someone to be one way on
        the outside but totally different on the inside?

        [Randy sighs deeply and stands up to walk]

        I mean, can someone identify as one sex but be
        something else but still have it be nothing about sex?

Randy
        Yes. Yes, Stan. I am <'famous' "musician">.

Stan
        ...What?

Randy
        It started off so simple. There's a guy at work. Hanson.
        He would use the bathroom and just blow the thing up, you know?
        Not only that, but he was in there all the time! I finally got
        fed up and pretended to be a woman.
        I called myself <'famous' "musician">. Have you ever been in a
        woman's bathroom, Stan? It's all clean and there's enough stalls
        for everyone. It was so freeing. I started singing while I was
        in there, and then I- started writing things down.

Stan
        Well you said you knew a guy at work who was
        <'famous' "musician">'s uncle.

Randy
        Yah, that's my cover.

Stan
        The chick that wrote the theme song to the new
        <shitty recession stimulus-funded book and movie series>, is you?

Randy
        Yeah.

        [turns around and faces Stan]

        The record company messed it all up. It was supposed to go:

            "<shitty recession stimulus-funded book and movie series>,
            yah yah yah, yah yah yah! <shitty recession stimulus-funded
            book and movie series>."

        But they just- do what they want with my songs.

Stan
        Wha-wait, <'famous' "musician"> sounds like a girl.

Randy
        Autotune. Wanna see how I do it?

        [moments later, a music program pops up.
        Twelve tracks are shown at lower left]

        I come up with all my best stuff in the bathroom at work.

        I use this program to import the recordings I make on my phone.

        [plays the highlighted track]

            "Yeah yeah, feeling good on a Wednesday. Sparklinnnnn'
            thoughts. Givin' me the hope to go ohhhn"

            [farts and poop noises]

            "Oh! Whoa. What I need now is a little bit of shelter."

Stan
        Dad, <'famous' "musician">'s music is actually really good.

Randy
        Thanks.

        But it gets even better when I add the drum loops.

        [replays the same track with drum loops added]

        Then with the computer I can actually quantize everything.

        [brings up the quantizer and chooses his settings]

        Backup instruments.

        [scale, beats, bass, tambourine, guitars, strings]

        And then finally I use the Autotune.

        ["Auto-Tuner v10." He chooses his settings there, and
        the song is transformed. The same track is now enhanced
        with <no name shitty "musician">'s voice and no trace of Randy]

            "Sparklin' thoughts, feelin' good on a Wednesday.
            Givine me the hope, givin' givin' me the hope to go ohhhn.
            What I need is a little bit of shelter."

        [this is all too much for Stan to take in, and he passes out.]

        [Randy notices]

        Stan?

---
## [KDE/kirigami](https://github.com/KDE/kirigami)@[edd13e294e...](https://github.com/KDE/kirigami/commit/edd13e294ea6d71839308d916b8faba87c21b37e)
#### Tuesday 2022-01-25 01:10:34 by Noah Davis

Units: make smallSpacing 4px and largeSpacing 8px

TL;DR
-----

Convert spacings to static amounts of pixels because when designing UIs,
this is how we tend to think of them in practice and our theming systems
also use static amounts of pixels (QStyles, plasma themes).

In theory, making spacing dynamic based on the font height allows the
spacings to scale with the size of content directly and in many cases it
does. Unfortunately, since our theming systems don't really do this, we
sometimes end up with inconsistent looking spacing and padding.

How fonts and units currently work
----------------------------------

`gridUnit` is `QFontMetricsF::height()`. It is 18px with Noto Sans 10
and 22px with Noto Sans 11. This is a huge jump in font height (1.22x)
even though characters have only increased in size by 1.1x. Perhaps this
is a problem with Noto Sans 11, but there simply aren't enough rules in
place to keep this kind of problem from happening. It also might not be
a problem with the font, just a part of Noto Sans' goal to support every
character, including large characters like  ꙲. Maybe the problem is in
QFontMetricsF or even deeper in FreeType (QFontMetricsF gets its info
from FreeType), but I doubt any of us are going to fix it (if it even is
a bug) and I doubt a fix will come from someone outside of our group.
Fonts are an extremely complex subject and fonts have to deal with
extremely touchy and complex real world subjects, like how to faithfully
represent a wide variety of scripts that maybe have inconsistent rules
which must be respected.

smallSpacing is `std::floor(gridUnit / 4)`. With Noto Sans 10, this is
4px. With Noto Sans 11, this is 5px; a 1.25x increase.
- If it rounded instead, it would be 5px with Noto Sans 10 and 6px with
Noto Sans 11; a 1.2x increase.

largeSpacing is `smallSpacing * 2`.

Do not assume that `smallSpacing * 4` or `largeSpacing * 2` will be
equal to gridUnit.

Alternative font based solutions for spacing units that I have pondered
-----------------------------------------------------------------------

What about pixelSize? Could we use that instead of font height? It
might be better in some ways, but worse in others. pixelSize is a pixel
based way to measure fonts that is actually arbitrary in practice. Noto
Sans' Latin and CJK characters happen to take up roughly the same amount
of vertical space as their pixelSize, so maybe we could base the spacing
on the pixelSize instead. However, not all fonts use a pixelSize the
same as the height of their tallest and lowest reaching Latin
characters. I use `kpAJE|` as a basic Latin string and `pixeltool` for
comparing pixelSize to real size. GNOME's Cantarell font shoud be 16px
from the top of k to the bottom of p if the pixelSize is 16px, but it is
actually 15px. Hack's Latin text is 17px high with a pixelSize of 16
(some poeple like monospace for everything). These two aren't large
differences, but the differences could still affect the values of
spacing units if based on pixelSize and other fonts have larger
differences. pixelSize is less variable (it's basically just `pointSize
* 1.33` or `pointSize / 0.75`), but doesn't necessarily represent what
is actually in the font. QFontMetricsF::height() represents what is
actually in the font and is the default height of all text elements, but
can vary a lot. Tradeoffs have to be made.
- Noto Sans 10 has a pixelSize of 13.33 (10/0.75) and Noto Sans 11 has a
pixelSize of 14.67 (11/0.75). Making consistent/good integer based
spacing units from those might be a little tricky.

What about measuring the real height of some characters and basing
spacings off of that? That could work. Maybe not for highly stylized
fonts, but it could work for common sans serif fonts. We still have to
make a lot of assumptions about how fonts should be though and fonts can
still behave differently at different sizes. Making good/consistent
spacing units from these will also be a little tricky.

Why switch to raw pixels?
-------------------------

6px is the standard amount of margin/spacing that the Breeze QStyle and
many parts of the Breeze Plasma style use. It doesn't change with font
size, so basing spacing units on font size makes us less likely to get
the right size. Could we make the QStyle use font based units instead?
Probably, but maybe we shouldn't. We can't make Plasma theme margins
based on font size. You can't embed dynamic system font size into an SVG
in a way that works for our theming system. However, these are
technicalities.

It's just difficult to control all the variables when dealing with font
sizes. Switching to pixels would make things less dynamic, but it would
also make it easier to design a good looking UI. We can finally make
assumptions about whether or not a unit will be divisible by 2, 3 or 4
without having to round. Rounding isn't a big deal on its own, but it's
another place for inconsistency to occur. In one place, something rounds
down and you get less padding than average. In another place, something
rounds up and you get more padding than average. Some people floor, some
people round and some people ceil in various situations, leading to more
opporunities for inconsistencies.

Most people don't increase or decrease font sizes so much that scaling
spacings to font size matters much. Most people who increase font size a
lot have difficulty seeing text. We should probably do some research
into whether or not they need more spacing too, but the problem with
increasing text size is you also have less space for text. If you
increase spacing on top of that, you have even less space for text.
Maybe they don't need their spacings to scale?

The lack of a 6px unit will not be solved by this patch. I intend to add
a 6px `mediumSpacing` property in a different patch.

History of our spacing units
----------------------------

As far as I can tell, smallSpacing and largeSpacing originally came from
Plasma, which doesn't support Qt UI scaling on X11. In Plasma, we
normally use `Math.round(value * PlasmaCore.Units.devicePixelRatio)` if
we want to scale some raw pixels with the system scale because
PlasmaCore.Units.devicePixelRatio is based on the font and the font size
scales with the system. smallSpacing in Kirigami is pretty much
unchanged from how it was in Plasma, but largeSpacing in Plasma is
identical to the font height/gridUnit.

---
## [Texera/texera](https://github.com/Texera/texera)@[c3af4463f4...](https://github.com/Texera/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Tuesday 2022-01-25 01:32:25 by Albert Liu

Add PresetService (User Presets Step 3) (#1164)

Final feature demo:

![Kapture 2022-01-13 at 23 36 00](https://user-images.githubusercontent.com/12578068/149469927-b62bfa43-4701-4498-a489-565aea36da2c.gif)

---------------------------

This PR is extracted from #1041 as step 2 of the User Preset feature.

rebase of picked commits pertaining to PresetServiceService onto Albert-UserDictionaryService

PresetService provides the ability to save and "apply" collections of settings (represented by objects) that a user might find convenient to save and apply as a group. These groups are called Presets.

PresetService uses DictionaryService to store presets (it creates kind of a *view* in the database sense, of the user dictionary, that only includes Presets)

Changes from last review (for Yicong)
 - Code comments
 - fixed subscription memory leak by using takeUntil(observable), where said observable completes on NgOndestroy
 - DictionaryService now attempts to init whenever client logs in (sorry, you'll have to re-review my changes to DictionaryService)
 - PresetService now has public ready promise/value member 
   - This indicates that its init isn't complete until DictionaryService's init is complete (which is async, and cant be awaited in the constructor)
 - DeletePreset now built into PresetService (don't know why I ever didn't have that)
 - Revert Changes to Styles.scss to fix Karma test runner interface (I originally changed them as a workaround for an ng-zorro component that's no longer used)

 Note: for this step, I had less time and more complex code to test. I'm not sure I caught all the bugs, but it passes unit tests.
The quality of the code in this pr is lesser, in my opinion, so You'll have to be a little more careful on my behalf.



Co-authored-by: Zuozhi Wang <zuozhiw@gmail.com>
Co-authored-by: Yicong Huang <17627829+Yicong-Huang@users.noreply.github.com>

---
## [tl566/jd-4](https://github.com/tl566/jd-4)@[f4deb86968...](https://github.com/tl566/jd-4/commit/f4deb869685db7ddd40484ad16f79064babbea5c)
#### Tuesday 2022-01-25 01:42:44 by gys619

新增：[ CK_WxPusherUid.json, JDJRValidator_Pure.js, JD_extra_cookie.js, JS1_USER_AGENTS.js, Loon/LoonTask.conf, Loon/lxk0301_LoonTask.conf, ModScript/jd_dreamFactory_Mod.js, ModScript/jd_fanli_Mod.js, ModScript/jd_fruit_Mod.js, ModScript/jd_health_Mod.js, ModScript/jd_jdfactory_Mod.js, ModScript/jd_joy_reward_Mod.js, ModScript/jd_medal_Mod.js, ModScript/jd_pet_Mod.js, ModScript/jd_plantBean_Mod.js, ModScript/jd_sgmh_Mod.js, ModScript/jd_speed_sign_Mod.js, NoUsed/NoUsed_jd_priceProtect_Mod.js, NoUsed/NoUsed_jd_speed_sign_Part1.js, NoUsed/NoUsed_jd_speed_sign_Part2.js, NoUsed/NoUsed_jd_speed_sign_Part3.js, NoUsed/NoUsed_jd_syj_Mod.js, Orz-3.conf, QuantumultX/cookies.conf, QuantumultX/gallery.json, QuantumultX/lxk0301_cookies.conf, QuantumultX/lxk0301_gallery.json, QuantumultX_Profiles.conf, Surge/Task.sgmodule, Surge/lxk0301_Task.sgmodule.sgmodule, TS_USER_AGENTS.ts, ZooFaker_Necklace.js, activity/desktop.ini, activity/jdCookie.js, activity/jd_5g.js, activity/jd_818.js, activity/jd_FLP.js, activity/jd_UnknownTask4.js, activity/jd_angryBean.js, activity/jd_angryKoi.js, activity/jd_apple_live.js, activity/jd_appliances.js, activity/jd_blueCoin.py, activity/jd_bookshop.js, activity/jd_car_exchange.js, activity/jd_carnivalcity.js, activity/jd_carnivalcity_help.js, activity/jd_cfd_fresh_exchange.js, activity/jd_cfdtx.js, activity/jd_city_exchange.js, activity/jd_city_lottery.js, activity/jd_coupon.js, activity/jd_crazy_joy.js, activity/jd_crazy_joy_bonus.js, activity/jd_crazy_joy_coin.js, activity/jd_daily_egg.js, activity/jd_ddwj.js, activity/jd_ddwj_help.js, activity/jd_decompression.js, activity/jd_digital_floor.js, activity/jd_dlpj.js, activity/jd_dqmh.js, activity/jd_ds.js, activity/jd_family.js, activity/jd_fanli.py, activity/jd_fcwb.js, activity/jd_fcwb_auto.js, activity/jd_festival.js, activity/jd_film_museum.js, activity/jd_finance.js, activity/jd_firecrackers.js, activity/jd_firecrackers2.js, activity/jd_focus.js, activity/jd_ftzy_help.js, activity/jd_global.js, activity/jd_global_mh.js, activity/jd_golden_machine.js, activity/jd_haier.js, activity/jd_health.js, activity/jd_honour.js, activity/jd_hotNeight.js, activity/jd_hotnight.js, activity/jd_hyj.js, activity/jd_immortal.js, activity/jd_immortal_answer.js, activity/jd_industrial_task.js, activity/jd_industryLottery.js, activity/jd_jddt.js, activity/jd_jdh.js, activity/jd_jika.js, activity/jd_jingsubang.js, activity/jd_joy_park_newtask.js, activity/jd_joy_tx.js, activity/jd_jr_draw.js, activity/jd_jxd.js, activity/jd_jxhlk.js, activity/jd_jxhlk.py, activity/jd_jxlhb.js, activity/jd_jxnc.js, activity/jd_jxstory.js, activity/jd_kxcdz.js, activity/jd_ldhwj.js, activity/jd_live_redrain.js, activity/jd_live_redrain2.js, activity/jd_ljd.js, activity/jd_lol.js, activity/jd_lotteryMachine.js, activity/jd_lsj.js, activity/jd_lxLottery.js, activity/jd_market_lottery.js, activity/jd_mcxhd.js, activity/jd_mh.js, activity/jd_mofang_exchange.js, activity/jd_ms_redrain.js, activity/jd_mx_shop.js, activity/jd_newTreasure.py, activity/jd_newYearMoney.js, activity/jd_newYearMoney_lottery.js, activity/jd_nh.js, activity/jd_nian.js, activity/jd_nian_ar.js, activity/jd_nian_sign.js, activity/jd_nian_wechat.js, activity/jd_party_night.js, activity/jd_petTreasureBox.js, activity/jd_price.js, activity/jd_pubg.js, activity/jd_qcshj.js, activity/jd_qjd.py, activity/jd_qqxing.js, activity/jd_qycl.js, activity/jd_redPacket.js, activity/jd_ryhxj.js, activity/jd_selectionOffice.js, activity/jd_sjjc.js, activity/jd_small_home.js, activity/jd_speed.js, activity/jd_split.js, activity/jd_summer_movement.js, activity/jd_superBrand.js, activity/jd_super_box.js, activity/jd_superbox.js, activity/jd_sxLottery.js, activity/jd_syj.js, activity/jd_tcl.js, activity/jd_teamFLP.js, activity/jd_tewu.js, activity/jd_travel_shop.js, activity/jd_tyt_w.js, activity/jd_unbind.js, activity/jd_unknownTask1.js, activity/jd_vivo.js, activity/jd_watch.js, activity/jd_wxFans.js, activity/jd_xg.js, activity/jd_xgyl.js, activity/jd_xiaolong.js, activity/jd_xiaomi.js, activity/jd_xinxiangyin.js, activity/jd_xtg.js, activity/jd_xtg_help.js, activity/jd_yijiajiu.js, activity/jd_ylyn.js, activity/jd_ys.js, activity/jd_zoo.js, activity/jd_zooCollect.js, activity/jd_zooElecsport.js, activity/jd_zzt.js, activity/jr_sign.js, activity/jx_mc_coin.js, activity/jx_sign.js, aiqicha.js, backUp/AlipayManor.js, backUp/ZooFaker_Necklace.js, backUp/gitSync.md, backUp/gua_MMdou.js, backUp/gua_UnknownTask1.js, backUp/gua_UnknownTask3.js, backUp/gua_UnknownTask4.js, backUp/gua_UnknownTask5.js, backUp/gua_carnivalcity.js, backUp/gua_ddgame.js, backUp/gua_doge.js, backUp/gua_olympic_opencard.js, backUp/gua_olympic_opencard2.js, backUp/gua_opencard10.js, backUp/gua_opencard12.js, backUp/gua_opencard13.js, backUp/gua_opencard14.js, backUp/gua_opencard17.js, backUp/gua_opencard21.js, backUp/gua_opencard22.js, backUp/gua_opencard23.js, backUp/gua_opencard24.js, backUp/gua_opencard25.js, backUp/gua_opencard26.js, backUp/gua_opencard27.js, backUp/gua_opencard28.js, backUp/gua_opencard30.js, backUp/gua_opencard31.js, backUp/gua_opencard38.js, backUp/gua_opencard4.js, backUp/gua_opencard43.js, backUp/gua_opencard5.js, backUp/gua_opencard6.js, backUp/gua_opencard7.js, backUp/gua_opencard8.js, backUp/gua_opencard9.js, backUp/gua_wealth_island.js, backUp/gua_wealth_island_help.js, backUp/gua_xiaolong.js, backUp/iCloud.md, backUp/iOS_Weather_AQI_Standard.js, backUp/jd_15.py, backUp/jd_HongBao.js, backUp/jd_OpenCard.py, backUp/jd_all_bean_change.js, backUp/jd_angryBean.js, backUp/jd_angryCash.js, backUp/jd_angryKoi.js, backUp/jd_appliances.js, backUp/jd_beauty_twelfth.js, backUp/jd_big_winner.js, backUp/jd_blueCoin.py, backUp/jd_bs.py, backUp/jd_car.js, backUp/jd_car_exchange_xh.js, backUp/jd_cart_remove.js, backUp/jd_cashHelp.py, backUp/jd_cfd.js, backUp/jd_cfd_SlotMachine.js, backUp/jd_cfd_loop.js, backUp/jd_cfd_mooncake.js, backUp/jd_cfdtx.js, backUp/jd_ddPlayer.js, backUp/jd_ddwj.js, backUp/jd_decompression.js, backUp/jd_delete.py, backUp/jd_deletenotify.py, backUp/jd_djyyj.js, backUp/jd_dyj_help.js, backUp/jd_fansa.js, backUp/jd_fc.js, backUp/jd_fcdyj.js, backUp/jd_fcffl.js, backUp/jd_film_museum.js, backUp/jd_flpa.js, backUp/jd_foodRunning.js, backUp/jd_goddess.js, backUp/jd_golden_machine.js, backUp/jd_gq.js, backUp/jd_hyj.js, backUp/jd_hyj_help.py, backUp/jd_industryLottery.js, backUp/jd_iqoo_run.js, backUp/jd_jika.js, backUp/jd_joy_help.js, backUp/jd_joy_reward_Mod.js, backUp/jd_joy_score.js, backUp/jd_jx_sign.js, backUp/jd_jxgc.js, backUp/jd_jxgc_tuan.py, backUp/jd_kanjia.js, backUp/jd_kanjia2.js, backUp/jd_kanjia3.js, backUp/jd_ldhwj.js, backUp/jd_lol.js, backUp/jd_lzdz2_fashion.js, backUp/jd_lzdz2_fashion1.js, backUp/jd_mb.js, backUp/jd_mid.js, backUp/jd_mid2.js, backUp/jd_mofang.js, backUp/jd_necklace_new.js, backUp/jd_olympicgames.js, backUp/jd_phone.js, backUp/jd_ppdz.js, backUp/jd_price.js, backUp/jd_priceProtect_Mod.js, backUp/jd_productZ4Brand.js, backUp/jd_qjd.py, backUp/jd_qqxing.js, backUp/jd_redPacket.js, backUp/jd_redPacket_help.js, backUp/jd_ryhxj.js, backUp/jd_speed_signfaker.js, backUp/jd_summer_movement.js, backUp/jd_summer_movement_bet.js, backUp/jd_summer_movement_card.js, backUp/jd_summer_movement_help.js, backUp/jd_summer_movement_map.js, backUp/jd_superBrand.js, backUp/jd_superBrand2.js, backUp/jd_superMarket_xh.js, backUp/jd_teamAnJia.js, backUp/jd_teamFLP.js, backUp/jd_travel_shop.js, backUp/jd_try.js, backUp/jd_twlove.js, backUp/jd_vivo_add.js, backUp/jd_wxFans.js, backUp/jd_xiaomi.js, backUp/jd_xxy.js, backUp/jd_young.js, backUp/jd_yqyl.js, backUp/jd_ys.js, backUp/jd_zjd.py, backUp/jd_zy_ddwj_help.js, backUp/jddj_fruit.js, backUp/mySelf.boxjs.json, backUp/webhook.js, backUp/xmSports.js, boxjs.json, cleancart_activity.js, creat.sh, docker/Dockerfile, docker/Readme.md, docker/auto_help.sh, docker/bot/jd.png, docker/bot/jd_bot, docker/bot/requirements.txt, docker/bot/setup.py, docker/crontab_list.sh, docker/default_task.sh, docker/docker_entrypoint.sh, docker/example/custom-append.yml, docker/example/custom-overwrite.yml, docker/example/default.yml, docker/example/docker\345\244\232\350\264\246\346\210\267\344\275\277\347\224\250\347\213\254\347\253\213\345\256\271\345\231\250\344\275\277\347\224\250\350\257\264\346\230\216.md, docker/example/jd_scripts.custom-append.syno.json, docker/example/jd_scripts.custom-overwrite.syno.json, docker/example/jd_scripts.syno.json, docker/example/multi.yml, docker/notify_docker_user.js, docker/proc_file.sh, function/.DS_Store, function/common.js, function/config.js, function/eval.js, function/jdValidate.js, function/jdcookie.js, function/jxAlgo.js, function/ql.js, function/sendNotify.js, gdbhapp.js, getJDCookie.js, gua_MMdou.js, gua_UnknownTask7.js, gua_UnknownTask9.js, gua_ddworld.js, gua_opencard81.js, gua_opencard82.js, gua_opencard83.js, gua_opencard84.js, gua_opencard85.js, gua_opencard86.js, gua_wealth_island.js, gua_wealth_island_help.js, jdEnv.py, jdJxncShareCodes.js, jdJxncTokens.js, jd_7dayClockin.py, jd_CkSeq.js, jd_DailyBonus_Mod.js, jd_DrawEntrance.js, jd_EsportsManager.js, jd_Evaluation.py, jd_aid_factory.js, jd_angryBean.js, jd_angryKoi.js, jd_bean_change_new.js, jd_beauty_ex.js, jd_blueCoin.py, jd_bookshop.js, jd_card_collecting_common_enc.js, jd_cart_remove.js, jd_cash_exchange.js, jd_cfd_fresh.js, jd_cfd_mooncake_help.js, jd_cfd_pearl.js, jd_daily_lottery.js, jd_ddnc_farmpark.js, jd_delCoupon.js, jd_dlpj.js, jd_dqmh.js, jd_dreamFactory_tuan.js, jd_duobao.js, jd_dyj_help.js, jd_evaluation.js, jd_exchangejxbeans.js, jd_exjxbeans.js, jd_family.js, jd_fan.js, jd_fanli.py, jd_fc.js, jd_fcwb.js, jd_fission.js, jd_flp.js, jd_foodRunning.js, jd_fruit_friend.js, jd_fruit_help.js, jd_fruit_task.js, jd_fxhh.js, jd_game_common_enc.js, jd_getFollowGift.py, jd_goodMorning.js, jd_gyp.js, jd_half_redrain.js, jd_hbCount.py, jd_health_collect.js, jd_health_exchange.py, jd_help_sendBean.js, jd_jchsign.js, jd_jddt.js, jd_jieMo.js, jd_joy-park.js, jd_joy_feedPets.js, jd_joy_park_help.js, jd_joy_reward_Mod.js, jd_joy_tx.js, jd_joyjd_open.js, jd_joypark_open.js, jd_jx_factory_automation.js, jd_jxg.js, jd_jxlhb.js, jd_jxmc_hb.js, jd_jxnc.js, jd_jxnn.js, jd_jxqd_new.js, jd_kanjia.js, jd_koiHelp.js, jd_koi_Help.js, jd_live_redrain.js, jd_look_video_common_enc.js, jd_lotteryMachine.js, jd_lucky_egg.js, jd_lzdz_unify.js, jd_mall.js, jd_mall_active.js, jd_market_lottery.js, jd_medal.js, jd_mofang.js, jd_mofang_exchange.js, jd_morningSc.js, jd_mx_jddt.js, jd_nnfl.js, jd_openCard.py, jd_prodev_dailyTask.js, jd_productZ4Brand.js, jd_qjd.js, jd_qjd.py, jd_rankingList.js, jd_redPacket.js, jd_refreshInvokeKey.js, jd_reward.ts, jd_rush_lzclient.js, jd_sendBeans.js, jd_share_common_enc.js, jd_shop_sign.js, jd_sign_graphics1.js, jd_sign_graphics_validate.js, jd_small_home.js, jd_speed.js, jd_speed_sign_Mod.js, jd_speed_sign_Part1.js, jd_speed_sign_Part2.js, jd_speed_sign_Part3.js, jd_speed_sign_Part4.js, jd_speed_sign_Part5.js, jd_speed_signfaker.js, jd_speed_signfree.js, jd_split.js, jd_star_wind_zzt.js, jd_super_mh.js, jd_super_redrain.js, jd_sxLottery.js, jd_syj.js, jd_task_checkCookie.js, jd_task_farm.js, jd_task_hby.js, jd_task_invokeKey.js, jd_task_jd2xd.js, jd_task_lottery.js, jd_task_noahHaveFunLottery.js, jd_task_price.js, jd_task_shopBean.js, jd_task_unfollowShop.js, jd_task_validate.js, jd_try_MyTrials.js, jd_unsubscriLive.js, jd_update.js, jd_upgrade.js, jd_vivo.js, jd_week.js, jd_wish2.js, jd_wish3.js, jd_work_price.js, jd_work_validate.js, jd_wxCollectionActivity.js, jd_wxFans.js, jd_wyw.js, jd_xiaolong.js, jd_xmf.js, jd_xmf_exchange.js, jd_xqscjd.js, jd_ylyn.js, jd_yqyl.js, jd_ys.js, jd_zbjmh.js, jd_zdjr.js, jd_zqfl.py, jddjCookie.js, jddj_bean.js, jddj_bean.json, jddj_fruit.js, jddj_fruit.json, jddj_fruit_collectWater.js, jddj_fruit_collectWater.json, jddj_getPoints.js, jddj_getPoints.json, jddj_getck.js, jddj_plantBeans.js, jddj_plantBeans.json, jkdapp.js, joy_run_token.json, jr_task_pig.js, jw_task_jdzz.js, jw_task_signRedpacket.js, jx_aid_cashback.js, jx_help_cashback.js, lxk0301.boxjs.json, lzdz1_jx.json, m_fanli.js, m_jd_car_sign.js, m_jd_delete_coupon.js, m_jd_duobao.js, m_jd_jd2xd.js, m_jd_sign.js, m_jd_yfcoupon.js, m_jx_cfd_card.js, m_jx_cfd_pearl_exchange.js, m_jx_factory_automation.js, m_jx_factory_commodity.js, m_jx_mc_zn_exchange.js, magic.js, package-lock.json, productZ4Brand11.js, ql.js, rush_jinggengjcq_dapainew.js, rush_lzclient.js, rush_lzdz1_dapai.js, rush_wxCollectionActivity.js, sendNotify.py, shell_script_mod.sh, starShop.json, tools/a.py, tools/empty.json, tools/jd_dreamFactory_product.js, utils/JDCookie.py, utils/JDJRValidator.js, utils/JDJRValidator_Pure.js, utils/JDJRValidator_Pure1.js, utils/JDSignValidator.js, utils/JD_DailyBonus.js, utils/MoveMentFaker.js, utils/MovementFaker.js, utils/USER_AGENTS.js, utils/ZooFaker_Necklace.js, utils/common.js, utils/config.js, utils/eval.js, utils/jdCookie.js, utils/jdShareCodes.js, utils/jdValidate.js, utils/jd_jxmcToken.js, utils/jd_sign_validate.js, utils/jdcookie.js, utils/jxAlgo.js, utils/magic.js, utils/ql.js, utils/sendNotify.js, utils/share_code.js, utils/sign_graphics_validate.js, utils/sign_graphics_validate1.js, zcodes.json]
修改内容：[ LICENSE, README.md, backUp/getJDCookie.js, backUp/jd_bean_change.js, backUp/jd_carnivalcity.js, backUp/jd_carnivalcity_help.js, backUp/jd_cfd_fresh_exchange.js, backUp/jd_crazy_joy.js, backUp/jd_crazy_joy_bonus.js, backUp/jd_crazy_joy_coin.js, backUp/jd_fan.js, backUp/jd_industrial_task.js, backUp/jd_jxlhb.js, backUp/jd_jxnc.js, backUp/jd_kxcdz.js, backUp/jd_kyd.js, backUp/jd_live_redrain.js, backUp/jd_lotteryMachine.js, backUp/jd_lsj.js, backUp/jd_qcshj.js, backUp/jd_qixi.js, backUp/jd_small_home.js, backUp/jd_vivo.js, backUp/jd_xtg.js, backUp/tencentscf.md, githubAction.md, index.js, jdCookie.js, jdDreamFactoryShareCodes.js, jdFactoryShareCodes.js, jdFruitShareCodes.js, jdPetShareCodes.js, jdPlantBeanShareCodes.js, jd_bean_change.js, jd_bean_home.js, jd_bean_sign.js, jd_big_winner.js, jd_car.js, jd_car_exchange.js, jd_cash.js, jd_cfd.js, jd_cfd_mooncake.js, jd_cfd_pearl_ex.js, jd_club_lottery.js, jd_daily_egg.js, jd_ddly.js, jd_ddworld.js, jd_dreamFactory.js, jd_dwapp.js, jd_fanli.js, jd_fcdyj.js, jd_fruit.js, jd_genz.js, jd_health.js, jd_jdfactory.js, jd_jdzz.js, jd_jfcz.js, jd_jin_tie.js, jd_joy.js, jd_joy_park.js, jd_joy_park_task.js, jd_joy_reward.js, jd_joy_run.js, jd_joy_steal.js, jd_jump.js, jd_jxgckc.js, jd_jxmc.js, jd_kd.js, jd_lxLottery.js, jd_mofang_ex.js, jd_mohe.js, jd_moneyTree.js, jd_moneyTree_help.js, jd_ms.js, jd_nnfls.js, jd_nzmh.js, jd_pet.js, jd_pigPet.js, jd_plantBean.js, jd_price.js, jd_qqxing.js, jd_redrain.js, jd_redrain_half.js, jd_sgmh.js, jd_shop.js, jd_signFree.js, jd_sign_graphics.js, jd_speed_sign.js, jd_superBrand.js, jd_superMarket.js, jd_try.js, jd_wish.js, jd_wsdlb.js, jd_zjb.js, jx_sign.js, jx_sign_xd.js, package.json, sendNotify.js, serverless.yml]

---
## [double-a-stories/life-of-the-party](https://github.com/double-a-stories/life-of-the-party)@[a0338e74e1...](https://github.com/double-a-stories/life-of-the-party/commit/a0338e74e1a050692d68d45dbbcf445ebca863a4)
#### Tuesday 2022-01-25 01:52:03 by double-a-stories

Changed most instances of "God" to other stuff

-Most characters reflexively use "oh my gosh" instead.
-Nikki/Nox are polytheists, and say "gods"
-Ana uses "G-d" instead. She's Jewish.
-Hollis's commands still use "oh god oh fuck"
-The "pantheon of animal gods" are no longer forgotten.

---
## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[8f32cbe38d...](https://github.com/Shadow-Quill/tgstation/commit/8f32cbe38d956e06c919be36386da76befb0555b)
#### Tuesday 2022-01-25 03:04:14 by LemonInTheDark

Reworks janitor cyborg cleaning, focus on the slipping (#64131)

Alt of #64105 and #64126 (I'm sorry Novva, I should have said something earlier)
I main janitor. As a janitor main, my greatest joy in life is slipping people who ignore my signs

I've seen some people complain about janitor borgs, so I decided to look into em

Unfortunately, not only is the janitor borg just a straight upgrade to janitors, it has absolutely no reason to use most of its kit
We give it standard cleaning supplies, and hell even bespoke tools to deal with leaving slippery tiles everywhere, but we also just let them clean anything they can walk over

This seems a bit too much to me, even for borgs. Also it's like, really boring

So what if we made their movement based cleaning cost something? How about we make it suck water from their bucket. Use the same pattern as mop code, make it twice as expensive though. Give it a slowdown, some sound cues, and an action button to trigger it all

---
## [k21971/UnNetHack](https://github.com/k21971/UnNetHack)@[275272a84a...](https://github.com/k21971/UnNetHack/commit/275272a84a6f3f1405c4a02c6f3b34cdecaafbb2)
#### Tuesday 2022-01-25 03:52:24 by copperwater

Scroll of remove curse becomes learned when items' curses are removed

The scroll of remove curse is trivially identified by checking inventory
after reading it to see whether anything became uncursed. This leads to
annoying tactics like remembering which scroll you just read so you can
go call it "remove curse" on the discoveries list.

This simply autoidentifies it when an item that was known to be cursed
has its curse removed.

Cherry picked from nethack/nethack@e13b1833cc

---
## [SteliosPapoutsakis/dwm](https://github.com/SteliosPapoutsakis/dwm)@[67d76bdc68...](https://github.com/SteliosPapoutsakis/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Tuesday 2022-01-25 04:22:54 by Chris Down

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
## [kalentang/incubator-doris](https://github.com/kalentang/incubator-doris)@[ef2ea1806e...](https://github.com/kalentang/incubator-doris/commit/ef2ea1806e4fb77369ab17a02d20fc8a286be43e)
#### Tuesday 2022-01-25 06:51:16 by HB

[docs] Improve the chapter on debugging FE in doc.  (#7309)

At present, there are defects in the chapter on debugging FE in doc. My colleagues and I stepped on the pit when 
building the debugging environment, so I want to improve this chapter in combination with my own stepping on the pit 
experience.

The following is my explanation of the changes: 

1. mkdir -p ./thirdparty/installed/bin
explain: When I downloaded versions 0.14 and 0.15, there were no files under thirdparty, so I didn't know whether to 
create it myself or what to do. Finally, I decided to create it myself. I think it's necessary to add instructions here.

2. Add installation thrift@0.13.0 Failed handling method. 
explain: My colleagues and I failed to find the installation package when executing the installation command, and finally 
found a solution on GitHub. Therefore, I added the handling method of the problem to avoid other Mac users from 
getting stuck in this place.

3. Fixed an error in the generated code description.
explain: Before I finished building the code, I debugged FE, and I failed all the time. Idea hints that no files can be found. 
Later, after consulting with morningman in wechat group, it was understood that `mvn install -DskipTests` does not 
need to execute `mvn generate-sources` after execution. This is inconsistent with the description in the document and 
needs to be corrected.

---
## [Iamgoofball/-tg-station](https://github.com/Iamgoofball/-tg-station)@[bc4dfa7a0e...](https://github.com/Iamgoofball/-tg-station/commit/bc4dfa7a0eb0baf1fff5f0d6785e2bdb61661c69)
#### Tuesday 2022-01-25 07:35:10 by Iamgoofball

REMOVES THE FUCKING 20 SECOND STUNLOCK RNG FROM TOURETTES FROM TOURETTES BECAUSE IT'S FUCKING STUPID AND I JUST HAD THE MOST AGONIZING THIRTY FUCKING MINUTES OF MY GODDAMN LIFE

---
## [krux02/nimskull](https://github.com/krux02/nimskull)@[f35b5bf2d4...](https://github.com/krux02/nimskull/commit/f35b5bf2d447c10b6a104ef0649115a266e8dea6)
#### Tuesday 2022-01-25 10:38:16 by haxscramper

Make compiler report structured

Full rework of the compiler message handling pipeline. Remove old-style message generation that was
based purely on strings that were formatted in-place, and instead implement structured logging where
main compiler code only instantiates objects with required information.

Explanation of changes for this commit will be split into several sections, matching number of edit
iterations I had to make in order for this to work properly.

* File reorganization

In addition to the architectural changes this PR requires some type definition movements.

- PNode, PSym and PType definitions (and all associated types and enums) were moved to the
  ast_types.nim file which is then reexported in the ast.nim
- Enum defininitions for the nilability checking were moved to nilcheck_enums.nim and then
  reexported
- Enum definitions for the VM were moved to to vm_enums.nim

* New files

- Main definition of the report types is provided in the reports.nim file, together with minor
  helper procedures and definition of the ReportList type. This file is imported by options, msgs
  and other parts of the compiler.
- Implementation of the default error reporting is provided in the cli_reporter.nim - all
  disguisting hardcoded string hacks were moved to this single file. Now you can really witness the
  "error messages are good enough for me" thinking that prevailed in the compiler UX since it's
  inception.

* Changed files

Most of the changes follow very simple pattern - old-style hardcoded hacks are replaced with
structural report that is constructed in-place and then converted to string /when necessary/. I'm
pretty sure this change already puts me close to getting CS PHD - it was *unimaginably hard* to
figure out that hardcoding text formatting in place is not the best architecture. Damn, I can
probably apply to the nobel prize right now after I figure that out.

** Changes in message reporting pipeline

Old error messages where reportined via random combinations of the following:

- Direct calls to `msgs.liMessage` proc - it was mostly used in the helper templates like
  `lintReport`
- `message`
- `rawMessage`
- `fatal`
- `globalError` - template for reporting global errors. Misused to the point where name completely
  lost it's meaning and documentation does not make any sense whatsoever. [fn:global-err]
- `localError` - template for reporting necessary error location, wrapper around `liMessage`
- `warningDeprecated` - used two times in the whole compiler in order to print out error message
  about deprecated command switches.

Full pipeline of the error processing was:

- Message was generated in-place, without any colored formatting (was added in `liMessage`)
  - There were several ways message could be generated - all of them were used interchangeably,
    without any clear system.
    1. Some file had a collection of constant strings, such as `errCannotInferStaticParam = "cannot
       infer the value of the static param '$1'"` that were used in the `localReport` message
       formatting immediately. Some constants were used pretty often, some were used only once.
    2. Warning and hint messages were categorized to some extent, so and the enum was used to
       provide message formatting via `array[TMsgKind, string]` where `string` was a `std/strutils`
       formatting string.
    3. In a lot of cases error message was generated using hardcoded (and repeatedly copy-pasted)
       string
- It was passed down to the `liMessage` (removed now) procedure, that dispatched based on the global
  configuration state (whether `ignoreMsgBecauseOfIdeTools` holds for example)
- Then message, together with necessary bits of formatting (such as `Hint` prefix with coloring) was
  passed down to the `styledMsgWriteln(args: varargs[typed])` template, whcih did the final dispatch
  into
- One of the two different /macros/ for writing text out - `callStyledWriteLineStderr` and
  `callIgnoringStyle`.
  - Dispatch could happen into stdout/stderr or message writer hook if it was non-nil
- When message was written out it went into `writeLnHook` callback (misused for
  `{.explain.}` [fn:writeln-explain]) (hacked for `compiles()` [fn:writeln-compiles]) and was
  written out to the stdout/stderr.

It is now replaced with:

- `Report` object is instantiated at some point of a compilation process (it might be an immediate
  report via `localError` or delayed via `nkError` and written out later)
- `structuredReportHook` converts it to string internally. All decitions for formatting, coloring
  etc. happen inside of the structured report hook. Where to write message, which format and so on.
- `writeLnHook` /can/ be used by the `structuredReportHook` if needed - right now it is turned into
  simple convenience callback. In future this could even be replaced with simple helper proc, for
  now I left it as it is now because I'm not 100% sure that I can safely remove this.

** Changes in the warning and hint filtering

Report filtering is done in the particular *implementation* of the error hook -
`options.isEnabled()` provides a default predicate to check whether specific report can be written
out, but it must still be called manually. This allows to still see all the reports if needed. For
example, `cli_reporter.reportHook()` uses additional checks to force write some reports (such as
debug trace in `compiles()` context).

Most of the hint and warning were already categorized, altough some reports had to be split into
several (such as `--hint=Performance` that actually controlled reports for `CopiesToSink` and
`CannotMakeSink`, `--hint=Name` that controlled three reports).

None of the errors were categorized (reports from the `nkError` progress was incorporated, but in
I'm mostly describing changes wrt. to old reporting system) and all were generated in-place

** Minor related changes

- List of allowed reports is now stored in the `noteSets: array[ConfNoteSet, ReportKinds]` field of
  the `ConfigRef`, instead of *seven* separate feilds. Access is now done via getter/setter procs,
  which allows to track changes in the current configuration state.
- Renamed list of local options to `localOptions` - added accessors to track changes in the state.
- Move all default report filter configuration to `lineinfos.computeNotesVerbosity()` - previously
  it was scattered in two different places: `NotesVerbosity` for `--verbosity:N` was calculated in
  `lineinfos`, foreignPackageNotesDefault was constructed in `options`
- Changed formatting of the `internalAssert` and `internalError` messages
- Removed lots of string formatting procs from the various `sem*` modules - ideally they should
  *all* be moved to the `cli_reporter` and related.

-------

Additional notes

[fn:global-err] As I said earlier, `globalError` was misused - it is still not possible to fully get
rid of this sickening hack, since it is used for /control flow/ (you read this correct - it is an
error reporting template, and it is used for control flow. Wonderful design right?).

So, in short - `globalError` can raise `ERecoverableError` that can be caught in some other layer
(for example `sem.tryConstExpr` abuses that in order to bail out (pretty sure it was done as an
'optimization' of some sort, just like 'compiles') when expression fails to evaluate at
compile-time [fn:except])

[fn:except] https://github.com/nim-works/nimskull/pull/94#issuecomment-1006927599

[fn:writeln-explain] Of course you can't have a proper error reporting in the nim compiler, so this
hook was also misused to the point of complete nonsense. Most notable clusterfuck where you could
spot this little shit is implementation of `{.explain.}` pragma for concepts. It was implemented via
really 'smart' (aka welcome to hell) solution in

https://github.com/nim-works/nimskull/commit/74a80988d9289e8147a791c4b0939d4287baaff3 (sigmatch
~704) and then further "improved" in
https://github.com/nim-lang/Nim/commit/fe48dd1cbec500298f7edeb75f1d6fef8490346c by slicing out parts
of the error message with `let msg = s.replace("Error:", errorPrefix)`

For now I had to reuse similar hack - I *do* override error reporting hook in order to collect all
the missing report information. In the future it would be unnecessary - when concept is matched it's
body will be evaluated to `nkError` with reports that are written out later.

[fn:writeln-compiles] when `compiles()` check is executed, all error output is temporarily disabled
(both stderr and stdout) via setting allowed output flags to `{}` (by default it is set to

---
## [jvdlem/PGD-GAMEJAM-2](https://github.com/jvdlem/PGD-GAMEJAM-2)@[8cb099aa19...](https://github.com/jvdlem/PGD-GAMEJAM-2/commit/8cb099aa19bce32be81dbcd72d30078efcbd5730)
#### Tuesday 2022-01-25 10:38:46 by Terdirk12

2nd big fix lets goo

-fixed elevator not opening in a build
-made coins go to the player faster (why were they so gosh darn slow)
-enemies now come at you from across the room (no more cheaky sniping)
-fixed some nullreferences in the pistol
-currently the roof of the cave system is gone but that be cuz some rooms need to be fixed (jordi knows which ones)
-added some light in the boss room so that you can actually see which eye is opened
-made the scope material less metallic for a more clear picture
-scaled back a previous fix for button presses from 10 units to 2 units
-made the builds development builds for now just so we can see where what goes wrong.
-dm me "i have read ur long ass shit" if you have actually read my long ass shit. -Dirk :D

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[7ae22f873c...](https://github.com/LemonInTheDark/tgstation/commit/7ae22f873c16f8f270e80c84adbc8e5fa38a2172)
#### Tuesday 2022-01-25 11:42:40 by LemonInTheDark

Removes the sleep from singularity code

Rather then using sleep to store the state of our iteration, we instead queue the iteration in a list.
We then use fastprocess to call our "digest" proc several times per full eat, with the hope of staying on top of
our queue
This rarely happens because the queue is too large, god why is a sm powered singulo 24x24 tiles.

I'm a bit unsure on this, but I think it might be worth just making a singulo subsystem. Feels a bit silly, but it allows much more control

I've also A: cached our dist checks, and B: Added dist checks to prevent attempting to pull things out of range
This might look a bit worse, but it saves a lot of work

Oh right and I made the singulo unable to eat while it still has tiles to digest. The hope is to prevent
overwork and list explosion.

Hopefully this will prevent singulo server stoppage, though I've seen some other worrying things in testing.
This is good regardless

---
## [dotnet/maui](https://github.com/dotnet/maui)@[ac6befcbee...](https://github.com/dotnet/maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Tuesday 2022-01-25 12:43:51 by Jonathan Peppers

[controls] Brush.Foo should return immutable instances (#3824)

When profiling a `dotnet new maui` app, with this package:

https://github.com/jonathanpeppers/Mono.Profiler.Android

The `alloc` report shows:

    Allocation summary
    Bytes      Count  Average Type name
    39984        147 2 72     Microsoft.Maui.Controls.SolidColorBrush

Stack trace:

    38352 bytes from:
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.VisualElement:.cctor ()
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.Brush:.cctor ()

Reviewing the `Brush` class, there are indeed 147 `SolidColorBrush`
created on startup that are stored in fields.

But what is weird about this, is that `SolidColorBrush` is mutable!

    public Color Color
    {
        get => (Color)GetValue(ColorProperty);
        set => SetValue(ColorProperty, value);
    }

So I could literally write code like:

    Brush.Blue.Color = Colors.Red;

Blue is red! (insert evil laughter?)

I think the appropriate fix here is that all of these `static
readonly` fields should just be properties that return a new
`ImmutableBrush`. We can cache the values in fields on demand. Then
someone can't do something evil like change `Blue` to `Red`?

I reviewed WPF source code to check what they do, and they took a
similar approach:

https://github.com/dotnet/wpf/blob/5e8187344b2b561ef08b9ca2735cd89cbdd3c11e/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/brushes.cs#L33-L1586

We should make this API change now before MAUI is stable, and we have
the side benefit to save 39984 bytes of memory on startup?

I added tests for these scenarios, and discovered 3 typos for `Brush`
colors that listed the wrong color.

---
## [hiper25-OpenSource/android_kernel_oneplus_sm8250](https://github.com/hiper25-OpenSource/android_kernel_oneplus_sm8250)@[0a52362bfc...](https://github.com/hiper25-OpenSource/android_kernel_oneplus_sm8250/commit/0a52362bfc8fcd59c48d47e0b44090a7924d84f9)
#### Tuesday 2022-01-25 13:50:47 by alk3pInjection

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
## [avar/git](https://github.com/avar/git)@[82a35504c9...](https://github.com/avar/git/commit/82a35504c99604fa219c83434489000a07673c99)
#### Tuesday 2022-01-25 14:05:07 by Ævar Arnfjörð Bjarmason

CI: run "make" and "make test" at the top-level

Continue the work started in my 25715419bf4 (CI: don't run "make test"
twice in one job, 2021-11-23) and unroll the running of "make" and
"make test" to the top-level of .github/workflows/main.yml.

In a parallel series of proposed updates to the CI[1] it's argued that
the current method of running ci/run-build-and-tests.sh will elide
whether we have a failure on the build or test step.

That's true, and a problem that's worth solving, but I think that the
proposed approach of emitting GitHub-specific markup in tests is the
wrong approach for this particular problem.

We should instead "unroll" the running of "make" and "make test" to
main.yml, so that we can simply run "make" and "make test". This would
have been painful before my 25715419bf4 (CI: don't run "make test"
twice in one job, 2021-11-23), as we'd run "make test" more than once
in some cases. But as this change shows it's now easy to do this.

We might still need CI-specific markup for some other cases, but for
this case we're better off by running "make" or "make test" directly
at the top-level.

It'll be immediately understood that e.g. "make" failed, and easier to
locally test the failure, as we'll have fever special CI entry points
to worry about. Adding another non-GitHub CI target will also be
easier, as we won't rely as heavily on its specific CI features.

See [2] and [3] for the GitHub-specific CI syntax being used here. In
particular we'd like to emulate the previous behavior of "make all
test" and not re-run "make test" if "make all" failed.

1. https://lore.kernel.org/git/pull.1117.git.1643050574.gitgitgadget@gmail.com/
2. https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idif
3. https://docs.github.com/en/actions/learn-github-actions/contexts#job-status-check-functions

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [newstools/2022-daily-post-nigeria](https://github.com/newstools/2022-daily-post-nigeria)@[2322da4b6b...](https://github.com/newstools/2022-daily-post-nigeria/commit/2322da4b6b924db6f941adb954769d7bf94915fb)
#### Tuesday 2022-01-25 15:03:43 by Billy Einkamerer

Created Text For URL [dailypost.ng/2022/01/25/sammie-okposo-apologises-for-cheating-on-his-wife-begs-god-for-forgiveness/]

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[c41ae43158...](https://github.com/repinger/exynos9611_m21_kernel/commit/c41ae431582ad98840dc7ca4f9fe5ff8251e5ea6)
#### Tuesday 2022-01-25 15:22:35 by Peter Zijlstra

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
## [Dudemanguy/mpv](https://github.com/Dudemanguy/mpv)@[4555f61651...](https://github.com/Dudemanguy/mpv/commit/4555f616510812a17255859ab1a9bc543559db1e)
#### Tuesday 2022-01-25 15:47:44 by Dudemanguy

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

Instead, just use Lua 5.1. This works fine lets us get rid of a terrible
hack in the meson build. People really shouldn't be using 2.0 LuaJIT
anyway, so the build failing is for their own good.

---
## [Dudemanguy/mpv](https://github.com/Dudemanguy/mpv)@[69274ff8c9...](https://github.com/Dudemanguy/mpv/commit/69274ff8c932c994e27eacd9f6a0732e63e0ec1f)
#### Tuesday 2022-01-25 15:47:44 by Dudemanguy

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
## [malaterre/GDCM](https://github.com/malaterre/GDCM)@[ff550ec21a...](https://github.com/malaterre/GDCM/commit/ff550ec21a0a57f307c0743b240e335504a21eb4)
#### Tuesday 2022-01-25 16:22:38 by Blair Conrad

Comment out MITRA MARKUP 1.0 references

There is no real sense in keeping those fake private attributes around.
Original discussion copy/pasted here:

I did see those in privatedicts.xml and did a quick scan in my source to
see if I had information at hand to augment. I didn't.
Since you asked, I looked a little more deeply this morning and learned
a bit more, but it's not great news.

I found some DICOM conformance statements that match the data currently
in privatedicts.xml, with no additional information.

I also found one other internal document that suggested a different use
(well, maybe consistent up to xx11 but not for xx12, xx13, and xx14;
then again maybe x12 and onward were errors in the first conformance
statements I mentioned). The document describes a long-defunct product.
But here's what I get from it.

Each element from xx00 to xxFF describes a piece of markup. The values
consist of different components. In each case, the first component is an
indicator of the type of markup (e.g. caliper, freeform caption, angle,
…) and there are 15 subsequent components which will vary depending on
the type of markup. As far as I can tell, each component is a string,
although some will be essentially an enumeration, some are integer
strings, some are double strings, and so on.

We could in theory replace xx12, xx13, and xx14's value multiplicity
with 1-n, and extend up to xxFF, but I'm not incredibly comfortable with
it, and I'm not sure there's great value, unless you're aware of people
having problems with these tags. I'm leery of changing the dictionary to
be both new and erroneous. 😁

---
## [xionghul/gcc](https://github.com/xionghul/gcc)@[aeac414923...](https://github.com/xionghul/gcc/commit/aeac414923aa1e87986c7fc6f9b921d89a9b86cf)
#### Tuesday 2022-01-25 17:58:06 by Thomas Schwinge

Revert "Fix PR 67102: Add libstdc++ dependancy to libffi" [PR67102]

This reverts commit db1a65d9364fe72c2fff65fb2dec051728b6f3fa.

On 2021-09-17T01:01:39-0700, Andrew Pinski via Gcc-patches <gcc-patches@gcc.gnu.org> wrote:
> On Fri, Sep 17, 2021 at 12:46 AM Thomas Schwinge <thomas@codesourcery.com> wrote:
>> On 2021-09-15T13:56:37-0700, apinski--- via Gcc-patches <gcc-patches@gcc.gnu.org> wrote:
>> > The error message is obvious -funconfigured-libstdc++-v3 is used
>> > on the g++ command line.  So we just add the dependancy.
>>
>> > --- a/Makefile.def
>> > +++ b/Makefile.def
>> > @@ -592,6 +592,7 @@ dependencies = { module=configure-target-fastjar; on=configure-target-zlib; };
>> >  dependencies = { module=all-target-fastjar; on=all-target-zlib; };
>> >  dependencies = { module=configure-target-libgo; on=configure-target-libffi; };
>> >  dependencies = { module=configure-target-libgo; on=all-target-libstdc++-v3; };
>> > +dependencies = { module=configure-target-libffi; on=all-target-libstdc++-v3; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libbacktrace; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libffi; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libatomic; };
>>
>> I'm confused, because given that this 'Makefile.def' change only has the
>> following effect:
>>
>> > --- a/Makefile.in
>> > +++ b/Makefile.in
>> > @@ -61261,6 +61261,7 @@ all-bison: maybe-all-intl
>> >  all-flex: maybe-all-intl
>> >  all-m4: maybe-all-intl
>> >  configure-target-libgo: maybe-all-target-libstdc++-v3
>> > +configure-target-libffi: maybe-all-target-libstdc++-v3
>> >  configure-target-liboffloadmic: maybe-configure-target-libgomp
>> >  all-target-liboffloadmic: maybe-all-target-libgomp
>> >  configure-target-newlib: maybe-all-binutils
>>
>> ... isn't that actually a no-op, because we already had such a dependency
>> listed?  Now twice:
>>
>>     $ grep -n -F 'configure-target-libffi: maybe-all-target-libstdc++-v3' -- Makefile.in
>>     61264:configure-target-libffi: maybe-all-target-libstdc++-v3
>>     61372:configure-target-libffi: maybe-all-target-libstdc++-v3
>>
>> Compared to the existing one, the one you've added is additionally
>> restricted by '@unless gcc-bootstrap'.
>>
>> I noticed this as I remembered that on our og[...] development branches
>> we have a patch in the opposite direction: get rid of this dependency via
>> removing 'lang_env_dependencies = { module=libffi; cxx=true; };' from
>> 'Makefile.def'.  See
>> <http://mid.mail-archive.com/alpine.DEB.2.21.9999.1812201344250.99920@build7-trusty-cs.sje.mentorg.com>
>> "Disable libstdc++ dependency for libffi".  (Maciej CCed in case you have
>> any further thoughts on that.)
>
> Oh, I see what happened now, the old bug was actually fixed by r6-5415
> which added cxx=true.
> So yes my patch is actually not needed and can be reverted.
> I tried to look to see if there was a dependency was there but for
> some reason I did not see it.

---
## [apache/couchdb](https://github.com/apache/couchdb)@[2e2e3805f7...](https://github.com/apache/couchdb/commit/2e2e3805f71849febc67e68e24cc1e2686a287c9)
#### Tuesday 2022-01-25 18:07:11 by Adam Kocoloski

Refactor Jenkins to dynamically generate stages

This is one of those situations where you go in to make a small change,
see an opportunity for some refactoring, and get sucked into a rabbit
hole that leaves you wondering if you have any idea how computers
actually work. My initial goal was simply to update the Erlang version
used in our binary packages to a modern supported release. Along the
way I decided I wanted to figure out how to eliminate all the copypasta
we generate for making any change to this file, and after a few days of
hacking here we are. This rewrite has the following features:

* Updates to use Debian 11 (current stable) as the base image for
  building releases and packaging repos.

* Defaults to Erlang 23 as the embedded Erlang version in packages. We
  avoid Erlang 24 for now because Clouseau is not currently compatible.

* Dynamically generates the parallel build stages used to test and
  package CouchDB on various OSes. This is accomplished through a bit
  of scripted pipeline code that relies on two new methods defined at
  the beginning of the Jenkinsfile, one for "native" builds on macOS
  and FreeBSD and one for container-based builds. See comments in the
  Jenkinsfile for additional details.

* Expands commands like `make check` into a series of steps to improve
  visibility. The Jenkins UI will now show the time spent in each step
  of the build process, and if a step (e.g. `make eunit`) fails it will
  only expand the logs for that step by default instead of showing the
  logs for the entire build stage. The downside is that if we do make
  changes to the series of targets underneath `check` we need to
  remember to update the Jenkinsfile as well.

* Starts per-stage timer _after_ agent is acquired. Previously builds could
  fail with a 15m timeout when all they did was sit in the build queue.

This is a cherry-pick of 9b6454b with the following modifications:

- Drop the MINIMUM_ERLANG_VERSION to 20
- Drop the packaging ERLANG_VERSION to 23
- Add the weatherreport-test as a build step
- Add ARM and POWER back into the matrix using a new buildx-based
  multi-architecture container image.

---
## [neurodebian/Psychtoolbox-3](https://github.com/neurodebian/Psychtoolbox-3)@[4b90b29dda...](https://github.com/neurodebian/Psychtoolbox-3/commit/4b90b29dda9d30aa9b89b2cb1077e85dddd61ecc)
#### Tuesday 2022-01-25 18:21:14 by Mario Kleiner

Screen/Linux: Support Wayland compositors without wl_shell, but xdg_shell.

libWaffle as of its latest release now also supports the basic stable
xdg shell protocol for window creation and management:

In the past, only wl_shell was supported. Now it will try to use
xdg_shell and fall back to wl_shell if xdg_shell is not supported.
As most production compositors do support xdg_shell in at least a
basic variant by now, this means most of the time xdg_shell will
be used.

Adapt our window setup code to make use of this new Waffle feature.
Also some cosmetic changes to status messages etc.

This now allows testing on wlroots-based compositors like Sway WM,
which do not support old wl_shell, but only xdg_shell. Also a bit
more robust on KDE's kwin wayland and GNOME's Mutter wayland.

Restrictions:

- We do not use xdg_shell calls ourselves yet, but rely on Waffle,
  so we are restricted: Can't select which output to display a
  fullscreen window on. That's supported on wl_shell only so far.

- Also no assignment of window titles in windowed mode.

- Oh and we need a bug-fixed libWaffle, as upstream release has a
  bug in its fullscreen xdg support! I'll need to upstream my fix.

- Sway does support the presentation timing feedback protocol, so
  now we have n=2 compositors with not totally broken timing, yay!
  However: Scheduling on Sway is as much of a s***-show as expected,
  as each Wayland compositor seems to reinvent the wheel in terms
  of composition scheduling. This will stay awful until a proper
  presentation timing extension is released and supported by most
  compositors. On Sway one needs these tweaks to get not totally
  awful timing and performance on a 144 Hz display:

  In Octave: setenv('PSYCH_WAYLAND_SWAPDELAY', '-0.002')
  In Sway's config file (see man sway-output):

  output DP-3 max_render_time 2

  Why these magic numbers? I wouldn't know, but endless tinkering
  made it work best for these settings. Any other refresh rate
  would probably need different numbers.

-> So this is an improvement, but far from anything one would want
   to expose ones's users to. X-Server still rules...

---
## [Moah700/Competiting-2022-Testing](https://github.com/Moah700/Competiting-2022-Testing)@[137c86fef1...](https://github.com/Moah700/Competiting-2022-Testing/commit/137c86fef1c233793d9ac8c4cc30474f16b7222e)
#### Tuesday 2022-01-25 19:11:03 by Moah700

new autocommand new subsystem

tried to get rid of colorsensing stuff in robot.java
moved colorsensing to subsystem ColorSensing.java
auto is in autocommand FollowTheYellowBrickRoad.java (sorry for the weird name but its kinda funny so actually not sorry)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a950223cc5...](https://github.com/mrakgr/The-Spiral-Language/commit/a950223cc56dff34243b6d65955a92d530f87a69)
#### Tuesday 2022-01-25 19:41:45 by Marko Grdinić

"11:45am. I slept pretty poorly tonight. Let me finish the thread, and then I will start. I want to begin with the tutorial.

12:10pm. Let me watch the tutorial for a bit. It is time to start.

12:20pm. https://www.sidefx.com/tutorials/attributes-and-copy/?collection=66
> (At 5:15) If you want to give a line a thickness, you have a very simple option called PolyWire.

So that is how I can give the curve a profile. Houdini works a bit differently than Blender, so this would probably work curves as well, rather than just meshes. Still...I doubt this node will have allowances for radius, but you can't underestimate Houdini. Not only does it have more nodes, but each of them are a lot bigger than the ones in Blender so for all I know it just might have allowances for what I want.

...Hmmm, I see the wire radius option.

Actually, let me follow along.

12:30pm. Ohhh, putting something like @P.y into the radius actually works! Houdini is so great.

1:15pm. The comibnation of shift to proximity to point is worth keeping in mind.

Let me pause at 32:43. I need to have breakfast and do the chores. I'll leave the other half for after I am done with that.

2:45pm. Let me read the Baki thread and I will start.

2:55pm. Let me resume. No, the PolyWire is not good enough. It does not allow a profile.

3pm. I'll have to put in some overtime today. Let me do it till 8pm today. These tutorials are not as dry as the ones from yesterday.

3:20pm. 54m. Orientation along curve is something I need to keep in mind.

3:30pm. 57m. Coloring the plans like this is interesting. It is one thing to slap a texture on some surface, but if I had something like a pile of hair or a carpet, it would not be easy to color it.

Well, maybe based on the coordinates it would be doable.

https://www.sidefx.com/tutorials/vops-vex-and-ramps/?collection=66

Done with the tutorial, let me move on to this.

Actually, now that I know how to orient along a curve, maybe I could connect the mesh using bridge or loft?

Let me give it a try.

3:55pm. Sigh, no I can't figure it out. These nodes are so mistifying. I'll need a tutorial to show me how they work first.

Let me start the tutorial.

4:05pm. Nevermind this tutorial. I am not interested in VOPS and LOPS. I'll skip these two vids and move to the next thing.

https://www.sidefx.com/tutorials/games-quickstart/

Let me take a look at this. I'll start with part 8. I do not have the patience for either the advanced stuff or, the very basic stuff anymore. How do I make good use of curves?

Hmmm, there is a specific centering node. Yeah, it occured to me to think that the transform is not suited for this for the reason that the button I used in fact wouldn't be reactive to upstream changes.

I'll have to remember to replace the center tranform for the bulb with the match size node.

Let me get back into the tutorial.

4:25pm. No this is not it.

https://youtu.be/hjYYh8cr3dg
Model a bridge in Houdini || Beginner Tutorial

Let me just watch this bridge tutorial.

https://youtu.be/hjYYh8cr3dg?t=31

Here he is using distance along geometry. I am guessing this is for the curve factor.

Or maybe not. He will be using this to heigten the curve based on the mask. Remarkable.

https://youtu.be/hjYYh8cr3dg?t=72

He is using the sweep node to make a profile. So that is how it works.

https://youtu.be/hjYYh8cr3dg?t=231

I had no idea you could just merge the connection back.

https://www.youtube.com/results?search_query=houdini+sweep

I am not done yet, but this really gave me an interest in the sweep node. Based on these vids, definitely, what I need is the sweep node.

https://youtu.be/hjYYh8cr3dg?t=494

Oh wow, you can set the pivots like this.

4:45pm. This was an informative tutorial. Let me study the sweep node tutorials. I am also curious about add.

5:10pm. Now I am studying the add node. What I've done is turned off all the nodes that I do not want to see, and am checking it out.

5:25pm. Ok...now that I spent some time thinking and factoring out its functionality, I understand the add node completely. It has some functionality for adding points and connecting them to make poligons. It also has some functionality for removing primitives and unused points as well. It can be controlled via groups or via patterns directly. No problem.

It seems a lot more complicated at first glance than it is. Let me take a look at the sweep node tutorials. If I can cross this hurdle, I could get through the plant tutorial.

https://youtu.be/RCux_9B6ua8
Houdini 18 - Basics - Using the New Sweep Node

Let me study this.

https://youtu.be/RCux_9B6ua8?t=124

Yeah, this is exactly what I need. Still, didn't Simon use this for a flat surface in the bridge video. That is how the plant thing was used as well.

https://youtu.be/RCux_9B6ua8?t=165

Ah, the probably used the ribbon...

No wait. That still does not make sense for the leaf. I'll have to study this in depth.

Let me take a short break here.

6:35pm. Done with lunch. So much for it being a short break. I am nowhere near done.

Brrrr, it is so damn cold today.

Let me resume the tutorial.

5:35pm. Hmmm, I see. The plant thing inserted the leaf as the cross section. That is the thing that is supposed to be the curve profile. I definitely would not have thought of using it like that. Still why does it have such behavior? Let me watch the tutorial and then I will think about it.

https://youtu.be/RCux_9B6ua8?t=336

It is possible to apply the scale along the curve too. Now if only I knew how to get the factor and I'd be all set.

...Actually, since there is a ramp, it does not seem like I have to do that explicitly. It should be a lot easier to get the effect that I want in Houdini without having to do math.

https://youtu.be/RCux_9B6ua8?t=361

It is really great of him to show me how to get the `u`s.

https://youtu.be/RCux_9B6ua8?t=640

This is really nice.

https://youtu.be/RCux_9B6ua8?t=838
> Pretty awesome stuff.

Yeah, I agree. I now definitely have enough to do the stalk. Still, does Houdini have some kind of weight painting functionality?

7pm.

///

This node can handle multiple spines, and/or multiple cross-sections.

* If there are multiple curves in the first (spine) input, the cross-section(s) is/are swept along each spine curve separately.

* If there are multiple curves in the second (cross-section) input, the cross-sections are distributed along the curve length according to the Cross section order parameter on the Construction tab.

///

So it is possible to have multiple cross sections in this. Remarkable.

> You can also use a pscale or scale point attribute on the spine curve to scale the cross sections (when Transform Using Curve Point Attributes is on).

Good, good.

7:30pm. Houdini crashed on me when editing an add node. I guess even it is not 100% bug free.

7:50pm. Wow it is really easy to crash Houdini. I just try to connect the node past the end of the array and it crashes.

7:55pm. '0 $N'

It is easy to connect the first and the last point using this.

I've been experimenting with replacing the add node with a single curve, but it matters greatly to the sweep node whether I connect the first to last or last to first. The later is no good.

8:15pm. Maybe I am going sick. My father has had a fever for the last few days, and I am feeling lightheaded myself right now. It is not that unpleasant, but I might end up being laid up in bed tomorrow or the day after.

At any rate, I thought that connecting the first and the last point of a curve might cause it to crash, but it turns out it works just fine. The add node itself is just a little iffy, but `0 $N` works just fine.

8:30pm. Rather than have it as a poligon, I think I'll leave it as a curve.

Right, so I get the way the add and the sweep nodes work now. I have everything I need to resume work on the flower. I also have everything I need for the plant tutorial. Let me watch it just for a bit.

https://youtu.be/GxKfKvYu7VU
Plant Growing animation | Houdini Full Tutorial

8:35pm. https://youtu.be/GxKfKvYu7VU?t=419

So far I actually get everything. This is good progress.

8:35pm. Let me stop here. I am too tired to continue. I really am feeling lightheaded. I am not sure what I'll do. Maybe just finish vol 15 of Dendro and head to bed."

---
## [thesadru/hikari](https://github.com/thesadru/hikari)@[58922627c3...](https://github.com/thesadru/hikari/commit/58922627c381bc5fc908de39a152ab7863cdf1dc)
#### Tuesday 2022-01-25 19:55:48 by sadru

Piss of flake8

don't care + didn't ask + you're white + cry about it + stay mad + get real + L + mald seethe cope harder + hoes mad + basic + skill issue + ratio + you fell off + the audacity + triggered + any askers + redpilled + get a life + ok and? + cringe + touch grass + donowalled + not based + your're a (insert stereotype) + not funny didn't laugh + you're* + grammar issue + go outside + get good + reported + ad hominem + GG! + ask deez + ez clap + straight cash + ratio again + final ratio + stay mad + stay pressed + pedophile + cancelled + done for + mad free + freer than air + rip bozo + slight_smile + cringe again + mad cuz bad + lol + irrelevant + cope + jealous + go ahead whine about it + your problem + don't care even more + sex offender + sex defender + not okay + glhf + problematic

---
## [thoughtbot/hotwire-example-template](https://github.com/thoughtbot/hotwire-example-template)@[c105f127f2...](https://github.com/thoughtbot/hotwire-example-template/commit/c105f127f220696326a9b434ec3b097347422e2a)
#### Tuesday 2022-01-25 22:29:33 by Sean Doyle

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
## [thoughtbot/hotwire-example-template](https://github.com/thoughtbot/hotwire-example-template)@[5224dedf32...](https://github.com/thoughtbot/hotwire-example-template/commit/5224dedf32888e96c557ce887b27e1fbb9948577)
#### Tuesday 2022-01-25 22:29:42 by Sean Doyle

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

