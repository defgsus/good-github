## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-23](docs/good-messages/2022/2022-01-23.md)


1,458,768 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,458,768 were push events containing 2,042,962 commit messages that amount to 124,766,534 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[eb384bd2d7...](https://github.com/jjpark-kb/Skyrat-tg/commit/eb384bd2d72a5b23dd9785cc06815049d507d3d5)
#### Sunday 2022-01-23 00:34:27 by Useroth

Telemetry 'n shit (#10810)

* Refactors dbcore and limits the maximum amount of concurrent async queries to a variable amount (#59676)

Refactors dbcore to work off a subsystem if executed async and limits the maximum amount of concurrent async queries to 25.

This has been tested locally on a mysql docker image and there were no crashes (as long as you didn't run it with debug extools) + data was getting recorded fine.
Why It's Good For The Game

May or may not resolve terry crashes, however, each query creates a new thread which takes up 2mb, preventing the game from using that 2mb. This can lead to ooms if they stack up, e.g. due to poor connectivity. This solves that issue.

maintainer note: this did not actually resolve the crashes, but has value anyway. Crashes were sidestepped fixed by finding out Large Address Awareness works

cl
refactor: Refactors dbcore.dm to possibly resolve the crashes that happen on Terry.
/cl

* Fixes an oversight in database code and cleans up telemetry (#64177)

As it is right now, we never actually clear the temporary list processing_queries
So if the subsystem is for some reason unable to complete a run, we will just whip right back around to it again
If it's been long enough, this could even cause horrific log spam. There was just now a manuel round with roughly 30k undeleted query errors. not good.

But what was actually not deleting you may ask?
Well

When you create a db request, a 5 minute timer starts. after those 5 minutes are up, the request is qdeleted by the db subsystem
This is to prevent the creation of unused requests, and to handle requests that are never cleaned up

Telemetry code was creating all of its db requests inside a for loop that could check tick, and then later
attempting to call them in series

Since requests by default sleep, this almost always lead to undeleted queries, which harddel'd given long enough periods

I've fixed this by moving the data gathering away from the query creation
Why is it good for the game

I was working on atmos code, happy, safe in my delusion, when suddenly I got a ping from tattle freaking out over 200 undeleted queries a second
This resolves that issue, so I can once again live in peace
Changelog

cl
admin: Telemetry code will spam you with undeleted query logs much less often now!
server: Improved how the db subsystem handles undeleted queries, should never have an incident like that again
/cl

* Fixes an error in telemetry queries (#64205)

* Hardsynced time_track.dm with upstream

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [pixelcmtd/CXClient](https://github.com/pixelcmtd/CXClient)@[6b90a95848...](https://github.com/pixelcmtd/CXClient/commit/6b90a95848d3559a92c22e1792f5eb0d86e3156e)
#### Sunday 2022-01-23 00:47:30 by chris

stripped the dependencies from the jar

they weren't needed.

i just spent hours FUCKING around with ivy and i hate my life a lot more
now. i think we might never have a proper build system fml

---
## [saem/nimskull](https://github.com/saem/nimskull)@[f35b5bf2d4...](https://github.com/saem/nimskull/commit/f35b5bf2d447c10b6a104ef0649115a266e8dea6)
#### Sunday 2022-01-23 00:48:36 by haxscramper

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
## [gys619/JDD3](https://github.com/gys619/JDD3)@[91af94f0d0...](https://github.com/gys619/JDD3/commit/91af94f0d05e0082d8b7f80401a60997e5d62266)
#### Sunday 2022-01-23 00:53:57 by gys619

新增：[ .DS_Store, .editorconfig, .gitattributes, .gitignore, CK_WxPusherUid.json, JDJRValidator_Aaron.js, JDJRValidator_Pure.js, JDJRValidator_Smiek.js, JDSignValidator.js, JD_extra_cookie.js, JS1_USER_AGENTS.js, JS_USER_AGENTS.js, LICENSE, QuantumultX/gallery.json, QuantumultX/lxk0301_gallery.json, Surge/Task.sgmodule, Surge/lxk0301_Task.sgmodule.sgmodule, TS_USER_AGENTS.ts, USER_AGENTS.js, ZooFaker_Necklace.js, activity/jdCookie.js, activity/jd_0yuankanjia.js, activity/jd_5g.js, activity/jd_818.js, activity/jd_UnknownTask4.js, activity/jd_angryBean.js, activity/jd_apple_live.js, activity/jd_appliances.js, activity/jd_beauty_ex.js, activity/jd_big_winner.js, activity/jd_blueCoin.py, activity/jd_bookshop.js, activity/jd_bzlshdgt.js, activity/jd_car_exchange.js, activity/jd_carnivalcity.js, activity/jd_cfd_fresh.js, activity/jd_cfd_fresh_exchange.js, activity/jd_cfdtx.js, activity/jd_city.js, activity/jd_city_exchange.js, activity/jd_city_lottery.js, activity/jd_citytx.js, activity/jd_coupon.js, activity/jd_crazy_joy.js, activity/jd_crazy_joy_bonus.js, activity/jd_crazy_joy_coin.js, activity/jd_daily_egg.js, activity/jd_daily_lottery.js, activity/jd_ddwj.js, activity/jd_ddworld_exchange.js, activity/jd_decompression.js, activity/jd_desire.js, activity/jd_digital_floor.js, activity/jd_djyyj.js, activity/jd_dlpj.js, activity/jd_ds.js, activity/jd_family.js, activity/jd_fcdyj_help_wx.js, activity/jd_fcwb.js, activity/jd_festival.js, activity/jd_film_museum.js, activity/jd_firecrackers.js, activity/jd_firecrackers2.js, activity/jd_fission.js, activity/jd_focus.js, activity/jd_ftzy_help.js, activity/jd_global.js, activity/jd_global_mh.js, activity/jd_golden_machine.js, activity/jd_gouwuche.js, activity/jd_gyp.js, activity/jd_haier.js, activity/jd_half_redrain.js, activity/jd_hb.js, activity/jd_health.js, activity/jd_honour.js, activity/jd_hotNeight.js, activity/jd_hotnight.js, activity/jd_hyj.js, activity/jd_hyj_help.py, activity/jd_immortal.js, activity/jd_immortal_answer.js, activity/jd_industrial_task.js, activity/jd_industryLottery.js, activity/jd_jchsign.js, activity/jd_jdh.js, activity/jd_jika.js, activity/jd_jingsubang.js, activity/jd_joy.js, activity/jd_joy_feedPets.js, activity/jd_joy_park_newtask.js, activity/jd_joy_reward.js, activity/jd_joy_run.js, activity/jd_joy_steal.js, activity/jd_jr_draw.js, activity/jd_jump.js, activity/jd_jxd.js, activity/jd_jxdzz.js, activity/jd_jxg.js, activity/jd_jxhlk.js, activity/jd_jxhlk.py, activity/jd_jxnc.js, activity/jd_jxstory.js, activity/jd_koi_Help.js, activity/jd_kxcdz.js, activity/jd_ldhwj.js, activity/jd_live_redrain.js, activity/jd_live_redrain2.js, activity/jd_ljd.js, activity/jd_lol.js, activity/jd_lotteryMachine.js, activity/jd_lottery_drew.js, activity/jd_lsj.js, activity/jd_lxLottery.js, activity/jd_lzclient.js, activity/jd_market_lottery.js, activity/jd_mcxhd.js, activity/jd_medal.js, activity/jd_medal_exchange.py, activity/jd_mh.js, activity/jd_mhyyl_sendCard.js, activity/jd_mofang.js, activity/jd_mofang_ex.js, activity/jd_moneyTree_help.js, activity/jd_ms.js, activity/jd_ms_redrain.js, activity/jd_mx_shop.js, activity/jd_neight1.js, activity/jd_neight2.js, activity/jd_newTreasure.py, activity/jd_newYearMoney.js, activity/jd_newYearMoney_lottery.js, activity/jd_nian.js, activity/jd_nian_ar.js, activity/jd_nian_sign.js, activity/jd_nian_wechat.js, activity/jd_party_night.js, activity/jd_petTreasureBox.js, activity/jd_pubg.js, activity/jd_qcshj.js, activity/jd_qjd.py, activity/jd_qqxing.js, activity/jd_qycl.js, activity/jd_redPacket.js, activity/jd_redPacket_help.js, activity/jd_refreshInvokeKey.js, activity/jd_ryhxj.js, activity/jd_selectionOffice.js, activity/jd_sevenDay.js, activity/jd_sign_graphics.js, activity/jd_sjjc.js, activity/jd_small_home.js, activity/jd_speed.js, activity/jd_summer_movement.js, activity/jd_superMarket.js, activity/jd_super_box.js, activity/jd_super_mh.js, activity/jd_super_redrain.js, activity/jd_sxLottery.js, activity/jd_syj.js, activity/jd_tcl.js, activity/jd_teamFLP.js, activity/jd_tewu.js, activity/jd_tiger.js, activity/jd_travel.js, activity/jd_travel_help.js, activity/jd_travel_shop.js, activity/jd_ttpt.js, activity/jd_unbind.js, activity/jd_unknownTask1.js, activity/jd_watch.js, activity/jd_xg.js, activity/jd_xgyl.js, activity/jd_xiaomi.js, activity/jd_xinxiangyin.js, activity/jd_xqscjd.js, activity/jd_xtg.js, activity/jd_xtg_help.js, activity/jd_year.js, activity/jd_yijia.js, activity/jd_yijiajiu.js, activity/jd_ylyn.js, activity/jd_ys.js, activity/jd_zbjmh.js, activity/jd_zoo.js, activity/jd_zooCollect.js, activity/jd_zooElecsport.js, activity/jd_zzt.js, activity/jx_mc_coin.js, activity/jx_sign.js, activity/jx_sign_xd.js, backUp/AlipayManor.js, backUp/GetJdCookie.md, backUp/GetJdCookie2.md, backUp/GetJdCookie3.md, backUp/JDJRValidator_Smiek.js, backUp/JD_extra_cookie.js, backUp/TG_PUSH.md, backUp/ZooFaker_Necklace.js, backUp/elecV2P.md, backUp/getJDCookie.js, backUp/gitSync.md, backUp/gua_MMdou.js, backUp/gua_UnknownTask1.js, backUp/gua_UnknownTask3.js, backUp/gua_UnknownTask4.js, backUp/gua_UnknownTask5.js, backUp/gua_carnivalcity.js, backUp/gua_ddgame.js, backUp/gua_doge.js, backUp/gua_olympic_opencard.js, backUp/gua_olympic_opencard2.js, backUp/gua_opencard10.js, backUp/gua_opencard12.js, backUp/gua_opencard13.js, backUp/gua_opencard14.js, backUp/gua_opencard17.js, backUp/gua_opencard21.js, backUp/gua_opencard22.js, backUp/gua_opencard23.js, backUp/gua_opencard24.js, backUp/gua_opencard25.js, backUp/gua_opencard26.js, backUp/gua_opencard27.js, backUp/gua_opencard28.js, backUp/gua_opencard30.js, backUp/gua_opencard31.js, backUp/gua_opencard38.js, backUp/gua_opencard4.js, backUp/gua_opencard43.js, backUp/gua_opencard5.js, backUp/gua_opencard6.js, backUp/gua_opencard7.js, backUp/gua_opencard8.js, backUp/gua_opencard9.js, backUp/gua_wealth_island.js, backUp/gua_wealth_island_help.js, backUp/gua_xiaolong.js, backUp/iCloud.md, backUp/iOS_Weather_AQI_Standard.js, backUp/jdJxncShareCodes.js, backUp/jdJxncTokens.js, backUp/jdUA.py, backUp/jd_15.py, backUp/jd_DrawEntrance.js, backUp/jd_HongBao.js, backUp/jd_OpenCard.py, backUp/jd_all_bean_change.js, backUp/jd_angryBean.js, backUp/jd_angryCash.js, backUp/jd_angryKoi.js, backUp/jd_appliances.js, backUp/jd_bean_change.js, backUp/jd_beauty_ex.js, backUp/jd_beauty_twelfth.js, backUp/jd_big_winner.js, backUp/jd_blueCoin.py, backUp/jd_bookshop.js, backUp/jd_bs.py, backUp/jd_bzlshdgt.js, backUp/jd_car.js, backUp/jd_car_exchange.js, backUp/jd_car_exchange_xh.js, backUp/jd_carnivalcity.js, backUp/jd_cart_remove.js, backUp/jd_cashHelp.py, backUp/jd_cash_exchange.js, backUp/jd_cfd.js, backUp/jd_cfd_SlotMachine.js, backUp/jd_cfd_fresh.js, backUp/jd_cfd_fresh_exchange.js, backUp/jd_cfd_loop.js, backUp/jd_cfd_mooncake.js, backUp/jd_cfd_mooncake_help.js, backUp/jd_cfdtx.js, backUp/jd_city.js, backUp/jd_city_exchange.js, backUp/jd_citytx.js, backUp/jd_crazy_joy.js, backUp/jd_crazy_joy_bonus.js, backUp/jd_crazy_joy_coin.js, backUp/jd_daily_egg.js, backUp/jd_ddPlayer.js, backUp/jd_ddo_pk.js, backUp/jd_ddwj.js, backUp/jd_ddworld_exchange.js, backUp/jd_decompression.js, backUp/jd_delCoupon.js, backUp/jd_delete.py, backUp/jd_deletenotify.py, backUp/jd_djjl.js, backUp/jd_djyyj.js, backUp/jd_dpqd.js, backUp/jd_dreamFactory.js, backUp/jd_dt.js, backUp/jd_dyj_help.js, backUp/jd_earn30.js, backUp/jd_enen.js.bak, backUp/jd_evaluation.js, backUp/jd_exchangejxbeans.js, backUp/jd_family.js, backUp/jd_fan.js, backUp/jd_fansa.js, backUp/jd_fc.js, backUp/jd_fcdyj.js, backUp/jd_fcffl.js, backUp/jd_film_museum.js, backUp/jd_finance.js, backUp/jd_flpa.js, backUp/jd_foodRunning.js, backUp/jd_fruit.js, backUp/jd_getFollowGift.py, backUp/jd_goddess.js, backUp/jd_goldPhone.js, backUp/jd_golden_machine.js, backUp/jd_gq.js, backUp/jd_gyp.js, backUp/jd_half_redrain.js, backUp/jd_hb_a.js, backUp/jd_health.js, backUp/jd_hyj.js, backUp/jd_hyj_help.py, backUp/jd_industrial_task.js, backUp/jd_industryLottery.js, backUp/jd_iqoo_run.js, backUp/jd_jchsign.js, backUp/jd_jika.js, backUp/jd_jingsubang.js, backUp/jd_joy.js, backUp/jd_joy_help.js, backUp/jd_joy_park_newtask.js, backUp/jd_joy_reward.js, backUp/jd_joy_reward_Mod.js, backUp/jd_joy_run.js, backUp/jd_joy_score.js, backUp/jd_joy_steal.js, backUp/jd_joy_tx.js, backUp/jd_joyjd_open.js, backUp/jd_joyjd_open_list.js, backUp/jd_jr_draw.js, backUp/jd_jump.js, backUp/jd_jxcfd_cash100.py, backUp/jd_jxd.js, backUp/jd_jxg.js, backUp/jd_jxgc.js, backUp/jd_jxgc_tuan.py, backUp/jd_jxmc_mkmb.js, backUp/jd_jxnc.js, backUp/jd_jxnnfls.py, backUp/jd_kanjia.js, backUp/jd_kanjia2.js, backUp/jd_kanjia3.js, backUp/jd_kj.js, backUp/jd_kxcdz.js, backUp/jd_kyd.js, backUp/jd_ldhwj.js, backUp/jd_live_redrain.js, backUp/jd_lol.js, backUp/jd_lotteryMachine.js, backUp/jd_lottery_drew.js, backUp/jd_lsj.js, backUp/jd_lxLottery.js, backUp/jd_lzclient.js, backUp/jd_lzdz2_fashion.js, backUp/jd_lzdz2_fashion1.js, backUp/jd_mall_active.js, backUp/jd_market_lottery.js, backUp/jd_mb.js, backUp/jd_mhtask.js, backUp/jd_mid.js, backUp/jd_mid2.js, backUp/jd_mofang.js, backUp/jd_mofang_ex.js, backUp/jd_mohe.js, backUp/jd_ms.js, backUp/jd_necklace_new.js, backUp/jd_newTreasure.py, backUp/jd_nzmh.js, backUp/jd_olympicgames.js, backUp/jd_openCard.py, backUp/jd_pet.js, backUp/jd_phone.js, backUp/jd_plantBean.js, backUp/jd_ppdz.js, backUp/jd_price.js, backUp/jd_priceProtect_Mod.js, backUp/jd_qcshj.js, backUp/jd_qixi.js, backUp/jd_qjd.js, backUp/jd_qjd.py, backUp/jd_qqxing.js, backUp/jd_rankingList.js, backUp/jd_redPacket.js, backUp/jd_redPacket_help.js, backUp/jd_ryhxj.js, backUp/jd_sevenDay.js, backUp/jd_sign_graphics1.js, backUp/jd_small_home.js, backUp/jd_speed.js, backUp/jd_spider_requests.py, backUp/jd_summer_exchange.js, backUp/jd_summer_movement.js, backUp/jd_summer_movement_bet.js, backUp/jd_summer_movement_card.js, backUp/jd_summer_movement_help.js, backUp/jd_summer_movement_map.js, backUp/jd_superBrand2.js, backUp/jd_superMarket.js, backUp/jd_superMarket_xh.js, backUp/jd_super_redrain.js, backUp/jd_syj.js, backUp/jd_task.json, backUp/jd_teamAnJia.js, backUp/jd_teamFLP.js, backUp/jd_tiger.js, backUp/jd_travel.js, backUp/jd_travel_shop.js, backUp/jd_try.js, backUp/jd_ttpt.js, backUp/jd_twlove.js, backUp/jd_unbind.js, backUp/jd_unsubscriLive.js, backUp/jd_unsubscribe.js, backUp/jd_utils.js, backUp/jd_vivo_add.js, backUp/jd_wish.js, backUp/jd_wxCollectionActivity.js, backUp/jd_wxShopFollowActivity.js, backUp/jd_wxj.js, backUp/jd_xiaomi.js, backUp/jd_xqscjd.js, backUp/jd_xsqjd.js, backUp/jd_xtg.js, backUp/jd_xxy.js, backUp/jd_year.js, backUp/jd_yijia.js, backUp/jd_young.js, backUp/jd_yqyl.js, backUp/jd_ys.js, backUp/jd_zd.js, backUp/jd_zdjr.js, backUp/jd_zjd.py, backUp/jd_zy_ddwj_help.js, backUp/jddj_fruit.js, backUp/jx_sign_xd.js, backUp/mengniu.js, backUp/mySelf.boxjs.json, backUp/redrian_user.py, backUp/reposync.md, backUp/rush_anjia.js, backUp/tencentscf.md, backUp/webhook.js, backUp/xmSports.js, boxjs.json, cleancart_activity.js, code.sh, config.json, desktop.ini, docker/Dockerfile, docker/Readme.md, docker/auto_help.sh, docker/bot/jd.png, docker/bot/jd_bot, docker/bot/requirements.txt, docker/bot/setup.py, docker/crontab_list.sh, docker/default_task.sh, docker/docker_entrypoint.sh, docker/example/custom-append.yml, docker/example/custom-overwrite.yml, docker/example/default.yml, docker/example/docker\345\244\232\350\264\246\346\210\267\344\275\277\347\224\250\347\213\254\347\253\213\345\256\271\345\231\250\344\275\277\347\224\250\350\257\264\346\230\216.md, docker/example/jd_scripts.custom-append.syno.json, docker/example/jd_scripts.custom-overwrite.syno.json, docker/example/jd_scripts.syno.json, docker/example/multi.yml, docker/notify_docker_user.js, docker/proc_file.sh, fanli.js, function/common.js, function/config.js, function/eval.js, function/jdValidate.js, function/jdcookie.js, function/jxAlgo.js, function/ql.js, function/sendNotify.js, getJDCookie.js, githubAction.md, gua_MMdou.js, gua_UnknownTask7.js, gua_UnknownTask9.js, gua_opencard101.js, gua_opencard108.js, gua_opencard109.js, gua_opencard110.js, gua_opencard111.js, gua_opencard112.js, gua_opencard93.js, gua_opencard94.js, gua_opencard95.js, gua_opencard96.js, gua_opencard97.js, gua_opencard98.js, gua_wealth_island.js, gua_wealth_island_help.js, index.js, jdCookie.js, jdDreamFactoryShareCodes.js, jdEnv.py, jdFactoryShareCodes.js, jdFruitShareCodes.js, jdJxncShareCodes.js, jdJxncTokens.js, jdPetShareCodes.js, jdPlantBeanShareCodes.js, jd_CheckCK.js, jd_CkSeq.js, jd_DailyBonus_Mod.js, jd_DrawEntrance.js, jd_EsportsManager.js, jd_Evaluation.py, jd_QLOneKeyDependency.sh, jd_UpdateUIDtoRemark.js, jd_aid_factory.js, jd_aid_fortune.js, jd_angryBean.js, jd_angryKoi.js, jd_babel_sign.js, jd_bean_change.js, jd_bean_change_new.js, jd_bean_home.js, jd_bean_info.js, jd_bean_sign.js, jd_beauty.js, jd_beauty_ex.js, jd_big_winner.js, jd_blueCoin.js, jd_blueCoin.py, jd_bookshop.js, jd_bt_sign.js, jd_car.js, jd_car_exchange.js, jd_cash.js, jd_cash_exchange.js, jd_ccSign.js, jd_cfd.js, jd_cfd_fresh.js, jd_cfd_loop.js, jd_cfd_mooncake.js, jd_cfd_mooncake_help.js, jd_cfd_pearl.js, jd_cfd_pearl_ex.js, jd_cfdhb100.py, jd_cfdhb111.py, jd_checkcookie.sh, jd_city.js, jd_club_lottery.js, jd_config.sample.sh, jd_connoisseur.js, jd_daily_egg.js, jd_daily_lottery.js, jd_ddnc_farmpark.js, jd_ddworld_exchange.js, jd_delCoupon.js, jd_delete_coupon.js, jd_dongxiang_benefits.py, jd_dpqd.js, jd_dpqd_diy.js, jd_dreamFactory.js, jd_dreamFactory_help.js, jd_dreamFactory_tuan.js, jd_duobao.js, jd_dwapp.js, jd_evaluation.js, jd_exchangejxbeans.js, jd_family.js, jd_fanli.js, jd_fcdyj.js, jd_fcwb.js, jd_festival.js, jd_foodRunning.js, jd_fruit.js, jd_fruit_everydayRed.py, jd_fruit_friend.js, jd_fruit_medalExchange.py, jd_fruit_task.js, jd_getFollowGift.py, jd_gold_creator.js, jd_gold_sign.js, jd_goodMorning.js, jd_half_redrain.js, jd_hbCount.py, jd_health.js, jd_health_collect.js, jd_health_help.js, jd_identical.py, jd_jd2xd.js, jd_jdfactory.js, jd_jdtj_winner.js, jd_jdzz.js, jd_jfcz.js, jd_jieMo.js, jd_jin_tie.js, jd_joy.js, jd_joy_feedPets.js, jd_joy_park.js, jd_joy_park_help.js, jd_joy_park_task.js, jd_joy_reward.js, jd_joy_reward_Mod.js, jd_joy_run.js, jd_joy_steal.js, jd_joy_tx.js, jd_joyjd_open.js, jd_joypark_open.js, jd_jr_draw.js, jd_jump.js, jd_jxg.js, jd_jxgckc.js, jd_jxhlk.py, jd_jxmc.js, jd_jxmc_hb.js, jd_jxnc.js, jd_jxnn.js, jd_kanjia.js, jd_kanjia2.js, jd_kd.js, jd_live.js, jd_live_redrain.js, jd_lotteryMachine.js, jd_lottery_drew.js, jd_lxLottery.js, jd_lzdz1_jx.json, jd_m_sign.js, jd_mall.js, jd_mall_active.js, jd_market_lottery.js, jd_medal.js, jd_mhtask.js, jd_mhyyl.js, jd_mofang_ex.js, jd_mohe.js, jd_mohe_help.js, jd_moneyTree.js, jd_moneyTree_help.js, jd_morningSc.js, jd_mpdzcar.js, jd_mpdzcar_game.js, jd_mpdzcar_help.js, jd_ms.js, jd_nh_sign.js, jd_nzmh.js, jd_openCard.py, jd_pet.js, jd_pigPet.js, jd_plantBean.js, jd_plantBean_help.js, jd_price.js, jd_priceProtect_Mod.js, jd_qjd.py, jd_qqxing.js, jd_rankingList.js, jd_redPacket.js, jd_redPacket_help.js, jd_redrain.js, jd_redrain_half.js, jd_refreshInvokeKey.js, jd_reward.ts, jd_scripts_check_dependence.py, jd_sendBeans.js, jd_sevenDay.js, jd_sgmh.js, jd_shop.js, jd_shop_sign.js, jd_shopsign.js, jd_sign.js, jd_signFree.js, jd_sign_graphics.js, jd_sign_graphics1.js, jd_sjnhj.js, jd_small_home.js, jd_speed.js, jd_speed_sign.js, jd_speed_sign_Part1.js, jd_speed_sign_Part2.js, jd_speed_sign_Part3.js, jd_speed_sign_Part4.js, jd_speed_sign_Part5.js, jd_superMarket.js, jd_super_mh.js, jd_super_redrain.js, jd_superbox.js, jd_sxLottery.js, jd_syj.js, jd_tiger.js, jd_tiger_help.js, jd_travel.js, jd_try.js, jd_try_notify.py, jd_ttysq.js, jd_tw.js, jd_unbind.js, jd_unsubscriLive.js, jd_unsubscribe.js, jd_upgrade.js, jd_userAwardExpandinfo.py, jd_week.js, jd_wish.js, jd_work_invokeKey.js, jd_work_validate.js, jd_wsdlb.js, jd_wxCollectionActivity.js, jd_wxShopFollowActivity.js, jd_wxgame.js, jd_wyw.js, jd_xdz.py, jd_xmf_exchange.js, jd_xyhy.js, jd_year.js, jd_yfcoupon.js, jd_ylyn.js, jd_yqyl.js, jd_zdjr.js, jd_zjb.js, jd_zjb_help.js, jd_zqfl.py, jddjCookie.js, jddj_bean.js, jddj_fruit.js, jddj_fruit_collectWater.js, jddj_getPoints.js, jddj_getck.js, jddj_plantBeans.js, joy_run_token.json, jx_aid_cashback.js, jx_cfd_card.js, jx_factory_automation.js, jx_factory_commodity.js, jx_sign.js, jx_sign_xd.js, jx_ttysq.js, lxk0301.boxjs.json, magic.js, package-lock.json, package.json, ql.js, sendNotify.js, sendNotify.py, serverless.yml, shell_script_mod.sh, sign_graphics_validate.js, task_before.sh, test.js, tools/a.py, tools/empty.json, tools/jd_dreamFactory_product.js, utils/JDCookie.py, utils/JDJRValidator.js, utils/JDJRValidator_Pure.js, utils/JDJRValidator_Pure1.js, utils/JDSignValidator.js, utils/JD_DailyBonus.js, utils/MoveMentFaker.js, utils/MovementFaker.js, utils/USER_AGENTS.js, utils/ZooFaker_Necklace.js, utils/common.js, utils/config.js, utils/eval.js, utils/jdCookie.js, utils/jdShareCodes.js, utils/jdValidate.js, utils/jd_jxmcToken.js, utils/jd_sign_validate.js, utils/jdcookie.js, utils/jxAlgo.js, utils/magic.js, utils/ql.js, utils/sendNotify.js, utils/sign_graphics_validate.js, utils/sign_graphics_validate1.js, wskey.py]
修改内容：[ README.md]

---
## [WorshipMeOrElse/find-the-gorts](https://github.com/WorshipMeOrElse/find-the-gorts)@[ae28a67c1a...](https://github.com/WorshipMeOrElse/find-the-gorts/commit/ae28a67c1a8656b93d3e8a0fc779a6b3dbcf0a92)
#### Sunday 2022-01-23 00:55:46 by WorshipMeOrElse

removed addchildren function due to unnecessary amount of connections

like holy shit a childadded connection on every fucking thing like ur kidding right

RIGHT

---
## [DuoIncure/PocketMine-MP](https://github.com/DuoIncure/PocketMine-MP)@[d9c70cb176...](https://github.com/DuoIncure/PocketMine-MP/commit/d9c70cb176c25bd67f7cab384428d6a9165f4539)
#### Sunday 2022-01-23 00:56:56 by Dylan K. Taylor

start.cmd: prevent idiotic behaviour when paths contain characters such as brackets
god I hate this shit so much

---
## [vr-voyage/SharpLogix](https://github.com/vr-voyage/SharpLogix)@[7f1507d821...](https://github.com/vr-voyage/SharpLogix/commit/7f1507d8216db726fb6654db9d1e04b665fe7a0f)
#### Sunday 2022-01-23 01:43:29 by Voyage

Midway commit

Turns out that adding support for "local checkpoints"
require a LOT of modifications to make it run correctly.

And event with those, I'm starting to think that I
might need to merge RemoteLogix and SharpLogix somehow.
The reason being that I need an internal nodes
representation when trying, for example, to generate a
register to store the output of a generic node
(ReadDynamicVariable).

Unless I find a way to weasel out by abusing the auto
casting system within the Neos graphical side, but this
might require some very ugly Reflection use from the
plugin side...

So, yeah, in the end RemoteLogix HAS a representation
of the nodes. With this I can ping a node and get the
current outputs types, and all...
So combining both might not be a bad idea... However,
the issue is that I'm using CSharpSyntaxWalker here,
and I don't think there are similar C/C++ libraries
doing the same.
While Godot support C#, its support is less versatile
than GodotScript. For example, generating HTML5 apps
from Godot C# can quickly be a pain.

The only solution to use any language, would be to
create another SharpLogix clone that would focus on
IL parsing, instead of code parsing, which was still an
idea in the first place... It has a lot of upsides
(precompiled stuff, you're almost sure that the code is
valid unless the user REALLY want to mess with you, ...).

Still, now that I'm starting with C#, I'd still like
to provide basic support, and internal node representation
isn't the hardest thing to implement.
However, it's just that "I already done it", so I'd like
to avoid remaking it again.

Signed-off-by: Voyage <voyage@miouyouyou.fr>

---
## [dMajoIT/terminal](https://github.com/dMajoIT/terminal)@[ccc74686a2...](https://github.com/dMajoIT/terminal/commit/ccc74686a28f4231355696d90a2e1f4b3be44a49)
#### Sunday 2022-01-23 01:56:50 by Mike Griese

Add snap-layouts support to the Terminal (#11680)

Adds snap layout support to the Terminal's maximize button. This PR is
full of BODGY, so brace yourselves.

Big thanks to Chris Swan in #11134 for building the prototype.
I don't believe this solves #8795, because XAML islands can't get
nchittest messages

- The window procedure for the drag bar forwards clicks on its client
  area to its parent as non-client clicks.
- BODGY: It also _manually_ handles the caption buttons. They exist in
  the titlebar, and work reasonably well with just XAML, if the drag bar
  isn't covering them.
- However, to get snap layout support, we need to actually return
  `HTMAXBUTTON` where the maximize button is. If the drag bar doesn't
  cover the caption buttons, then the core input site (which takes up
  the entirety of the XAML island) will steal the `WM_NCHITTEST` before
  we get a chance to handle it.
- So, the drag bar covers the caption buttons, and manually handles
  hovering and pressing them when needed. This gives the impression that
  they're getting input as they normally would, even if they're not
  _really_ getting input via XAML.
- We also need to manually display the button tooltips now, because XAML
  doesn't know when they've been hovered for long enough. Hence, the
  `_displayToolTip` `ThrottledFuncTrailing`

## Validation
Minimized, maximized, restored down, hovered the buttons slowly, moved
the mouse over them quickly, they feel the same as before. But now with
snap layouts appearing.

## TODO!
* [x] I'm working on getting the ToolTips on the caption buttons back. Alas, I needed a demo of this _today_, so I'll fix that tomorrow morning.
* [x] mild concern: I should probably test Win 10 to make sure there wasn't weird changes to the message loop in win11 that means this is broken on win10.
* [x] I think I used the wrong issue number for tons of my comments throughout this PR. Double check that. Should be #9443, not #9447.

Closes #9443
I thought this took care of #8587 ~as a bonus, because I was here, and the fix is _now_ trivial~, but looking at the latest commit that regressed.

Co-authored-by: Chris Swan <chswan@microsoft.com>
(cherry picked from commit f2ebb21bd13b20db38305136d34fa0778baf7920)

---
## [dMajoIT/terminal](https://github.com/dMajoIT/terminal)@[5198c8e2e4...](https://github.com/dMajoIT/terminal/commit/5198c8e2e4e4b62b04c971246ee114968090aab1)
#### Sunday 2022-01-23 01:56:50 by Mike Griese

Make sure the infobar is inserted before the tab content, not on top of (#11609)

Fixes #11606

This is weird, but the infobars would appear totally on top of the
TerminalPage when `showTabsInTitlebar:false`. This would result in the infobar
obscuring the tabs.

Now, the infobars are strictly inserted after the tabs, before the content. So
when they appear, they will reduce the amount of space usable for the control.
That is a little annoying, but preferable to the tabs totally not existing.

Relevant conversation notes from #10798:

> > If the info bar is not local to the tab, then its location between the tab
> > bar (when the title bar is hidden) and the terminal panes feels
> > misleading. Should it instead be above the tab bar or below the terminal
> > panes?
>
> You're... not wrong here. It's maybe not the best place for it, but _on top_
> of the tabs would look insane, and probably wouldn't even work easily, given
> the way we reparent the tab row into the titlebar.
>
> In the pane itself would make more sense, but that runs abreast of all sorts
> of things like #9024, #4998, which might make more sense.

I'm just gonna go with this now, because it's _better_ than before, while we
work out what's _best_.

![gh-11606-fix](https://user-images.githubusercontent.com/18356694/138729178-b96b7003-0dd2-4521-8fff-0fd2a5989f22.gif)

(cherry picked from commit a916a5d9de450bc6a008d257d3c5c5cfd27e07ec)

---
## [ebbit1q/Cockatrice](https://github.com/ebbit1q/Cockatrice)@[ebe2c494aa...](https://github.com/ebbit1q/Cockatrice/commit/ebe2c494aa4c92f2ed64f94c1ef6df05e63deafd)
#### Sunday 2022-01-23 02:07:16 by ebbit1q

remove the stop dump zone command from the protocol (#4326)

the stop dump zone command was implemented as a courtesy to other
players in order to take into account when they would stop looking at
unknown information

however, this can be abused, a malicious client can send this command
whenever they would like

cockatrice is not a physical tabletop nor does it aim to be, if you can
take a screenshot of your deck and then close the view, you are not
cheating as you have been given this information

in order to prevent anyone from abusing this we should remove the
command from the protocol, this means servers will ignore this message
and clients will get a little invalid command reply in their debug log

the extension id will remain reserved

shuffling your deck will always invalidate any card view looking at
those cards

if players wish to signal that they stopped looking at their deck for
whatever reason they should just use the chat instead, optionally using
one of the chat macros

---
## [Kylerace/tgstation](https://github.com/Kylerace/tgstation)@[a2fa7799f3...](https://github.com/Kylerace/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Sunday 2022-01-23 03:19:23 by Jeremiah

Removes swarmers from the game (#63989)

What the title says. But why?
I generally have a rule when making a contribution, that is "don't make the game less fun"
I'm not salting, I didn't die to a swarmer.
... Yet that's the problem. Swarmers are the griefiest antag in the game, but when you complain that they're annoying or unfun, you're doomed to hear "lol they can't even hurt you though."

WELL THAT ACTUALLY MAKES THEM WORSE. I would rather die to a hundred xenos and space dragons than be forced to untie myself in maintenance for 45 seconds while the shuttle leaves.
Why It's Good For The Game

Unfun game modes should be removed from the game.

    Being griefed by swarmers is annoying
    Playing as a swarmer is not very exciting either. Click on iron.

lastly, because oranges authorized it
Changelog

cl
del: Removes swarmers! The griefiest, lowest fun value antagonist is removed from the game.
/cl

---
## [MetalfOxXer/Naruto_Ninpou](https://github.com/MetalfOxXer/Naruto_Ninpou)@[32f854d563...](https://github.com/MetalfOxXer/Naruto_Ninpou/commit/32f854d563dd24bb8044f996059e59e49cc5e2c3)
#### Sunday 2022-01-23 03:25:40 by MetalfOxXer

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
## [987123879113/mame](https://github.com/987123879113/mame)@[a49e215466...](https://github.com/987123879113/mame/commit/a49e2154666b0ee7423e2d859c21b7592a4c61b8)
#### Sunday 2022-01-23 03:51:59 by Firehawke

Apple II updates for January 2022 (#9189)

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Earth Science: Interplanetary Travel (cleanly cracked) [4am, Firehawke]
Isaac Newton and F.I.G. Newton (cleanly cracked) [4am, Firehawke]
Return to Reading: The Call of the Wild (cleanly cracked) [4am, Firehawke]
The German Hangman (cleanly cracked) [4am, Firehawke]
Legionnaire (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Bridge Tutor with Precision and Scientific Bidding (cleanly cracked) [4am, san inc, Firehawke]
The French Hangman (cleanly cracked) [4am, Firehawke]
The Russian Hangman (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Mickey's Space Adventure [4am, Firehawke]
The Environment Life Dynamic [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Stellar Power [4am, Firehawke]

New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Ken Uston's Professional Blackjack (Version 1.12) (cleanly cracked) [4am, Firehawke]
Dinosaur's Lunch (cleanly cracked) [4am, Firehawke]
Race Car Keys (cleanly cracked) [4am, Firehawke]
Functional Harmony: Basic Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Diatonic Seventh Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Borrowed and Altered Chords (cleanly cracked) [4am, Firehawke]
Building Reading Skills: The Letter-Sound Farm (cleanly cracked) [4am, Firehawke]
Follow Me (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

The German Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Russian Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Spanish Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Exploring Library Land (cleanly cracked) [4am, Firehawke]
Library Treasure Hunt (cleanly cracked) [4am, Firehawke]
Expedition U.S.A.! (cleanly cracked) [4am, Firehawke]
Codes and Cyphers (cleanly cracked) [4am, san inc, Firehawke]
Ripley's Believe It Or Not: Beginning Library Research Skills (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Glutton [4am, Firehawke]

---
## [Tkpointz/android_kernel_aresin](https://github.com/Tkpointz/android_kernel_aresin)@[e69e497f5a...](https://github.com/Tkpointz/android_kernel_aresin/commit/e69e497f5a278fa283c57d88fcbf9e65a8aaa3c7)
#### Sunday 2022-01-23 07:33:26 by Peter Zijlstra

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
Signed-off-by: Tkpointz <pointzztk@gmail.com>

---
## [Nowaaru/suwariyomi](https://github.com/Nowaaru/suwariyomi)@[deb78f9be0...](https://github.com/Nowaaru/suwariyomi/commit/deb78f9be00ca3cfbb5e605ba3bc6053077b03b4)
#### Sunday 2022-01-23 08:36:31 by Nowaaru

genuinely fuck programming i dont care about this npm test bullshit anymore FUCK you

---
## [Utumno/wrye-bash](https://github.com/Utumno/wrye-bash)@[6c0fc771bb...](https://github.com/Utumno/wrye-bash/commit/6c0fc771bb222c37b53ef99dd9a2d07c4c484f5b)
#### Sunday 2022-01-23 08:44:43 by MrD

FName: EEE tests for FNDict

EEE test immutability - copies
EEE add del self.__dict__ to ci_body?

An initial version of this branch had Paths replaced with CIstr's. That
turned out to be highly unsatisfactory:

- CIstr I created to use internally in LowerDict - LD is the API, not
CIstr.
- body_ and ext_ wrappers are too slow - the code looked more ugly and
os.path.splitext (an expensive operation) kept proliferating
- those DataStore keys are really a beast of its own kind (corresponding
to filenames) and by the lesson this very branch teaches us better have
a specialized type for them
- turns out I wanted to keep Path's ability to compare with strings -
but I wanted this as efficient as possible - can't have slots
unfortunately but other than that given that FName *can only be
instantiated with unicodre strings* I was able to drop the
`if type is str` checks in FNDict dunder methods
- FName(CIstr) would be too much nesting and probably performance (lookups
of methods traverse the mro -TODO: time) - anyway FName is-not a CIstr

Check if FName should be the usual case in comparisons (try: except AE)
once I have scanned the code

SSS:

return None if None is passed (duh)

Backwards compat TTT  EEE move forward_compat_path_to_fn below FNDict

Well I kept adding backwards compat and even with dedicated functions:

@@ -428,6 +431,2 @@ def __repr__(self):
 # backwards and forward compat functions
-def backwards_compat_fn_to_path(di, value_type=lambda x: x):##: [backwards compat] drop in 312+
-    return {GPath_no_norm('%s' % k): value_type(v) for k, v in di.items()}
-def backwards_compat_fn_to_path_list(li, ret_type=list):
-    return ret_type(map(GPath_no_norm, map(str, li)))
 def forward_compat_path_to_fn(di, value_type=lambda x: x):##: [forward compat] drop 313+

this was getting out of hand  -  so:

@@ -378,2 +378,5 @@ def ci_body(self):

+    def __reduce__(self):##: [backwards compat] drop in 312+ (but still store strs)
+        return GPath_no_norm, (str(self),)

@@ -553,2 +552,5 @@ def __repr__(self):

+    def __reduce__(self): #[backwards compat]we 'd rather not save custom types
+        return dict, (dict(self),)

I think now I got them all :)
Note I pickle the cache factory (GPath_no_norm) - so when I load
settings I already cache the filenames - can't think of anything bad
(apart that this won't carry to pre GPath_no_norm  versions of bash -
that is pre 307 as 662423530ff1ba4219ed0b2cc91effd5306a5ca2 on 307, but
I don't think many people will update to 310 and then go back to 306)

Edit: was bitten bitterly by my smart idea (stays a smart idea, but).
So I was testing a bashed patch and some form ids had Paths instead of
FNames and this drove me nuts, had put breakpoints everywhere and still
couldn't find where these Paths were from - turns out we use deepcopy
(yes I used to know) and deepcopy will use __reduce__ if it's there.
This incidentally gave me an idea for optimizing the Path copies
currently.

squash! FN

@@ -394,5 +388,4 @@ def __eq__(self, other):
         except AttributeError:
-            if isinstance(other, str):
-                return self._lower == other.lower()
-            return NotImplemented
+            # this will blow if other is not a str even if it defines lower
+            return self._lower == str.lower(other)
     def __ne__(self, other):

eee test  deepcopy

squash! fe24d5da24b5a8694835e81cee307ddad94bde2a

Yey:

self = FName('path.txt'), other = bolt.Path('path.txt')

    def __eq__(self, other):
        try:
            return self._lower == other._lower # (self is other) or self...
        except AttributeError:
            # this will blow if other is not a str even if it defines lower
>           return self._lower == str.lower(other)
E           TypeError: descriptor 'lower' for 'str' objects doesn't apply to a 'Path' object

@@ -459,3 +459,3 @@ def test__eq__(self):
         # fname and paths
-        assert fn == GPath('path.txt') ##: Oops do we want this?
+        with pytest.raises(TypeError): assert fn != GPath('path.txt')
         # paths and None
@@ -470,3 +470,3 @@ def test__eq__(self):
         assert empty == ''
-        assert empty == GPath('') ##: Oops do we want this?
+        with pytest.raises(TypeError):assert empty != GPath('')
         for other in (b'', None, [], [1], True, False, 55):
@@ -505,4 +505,4 @@ def test_dict_keys(self):
         assert FN in fn_keys_dict # yey
-        assert GPath(file_str) in fn_keys_dict ##: Oops do we want this?
-        assert GPath(FILE_STR) in fn_keys_dict ##: Oops do we want this?
+        with pytest.raises(TypeError): assert GPath(file_str) in fn_keys_dict
+        with pytest.raises(TypeError): assert GPath(FILE_STR) in fn_keys_dict
         string_keys_dict = {file_str: 1}
@@ -527,4 +527,4 @@ def test_sets_lists(self):
             assert FN in fn_set # yey
-            assert GPath(file_str) in fn_set ##: Oops do we want this?
-            assert GPath(FILE_STR) in fn_set ##: Oops do we want this?
+            with pytest.raises(TypeError): assert GPath(file_str) in fn_set
+            with pytest.raises(TypeError): assert GPath(FILE_STR) in fn_set
             string_set = cont_type([file_str])

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[10ba80973b...](https://github.com/tgstation/tgstation/commit/10ba80973bfc977b17aa116f3b630862e9e70a7c)
#### Sunday 2022-01-23 08:46:53 by Kylerace

makes most statpanel tabs update a tenth or so as often (>= 4 seconds instead of 4 deciseconds) because theyre wastful of cpu (#63991)

makes most updating stat panel tabs update once every 4 seconds instead of 4 deciseconds, but switching tabs instantly updates statpanel data for you. also makes examining a turf make flat icons for a maximum of 10 contents instead of 30 because its ridiculous to call getFuckingFlatIcon() wrappers that many times. also makes SSfluids not have SS_TICKER and updates its wait accordingly because theres no reason for it to be a ticker subsystem

the mc tab updates every 2 seconds unless someone has the pref enabled to refresh it quickly because SOME UNILLUMINATED LEMONS absolutely must watch overtime spikes in real time

statpanels can take between 1-3% of masters total processing time at very high pop, which is silly considering theres no need for someone to know any of the data updated accurate to less than half of a second. The only reason it needed to update so fast was because it looked awful when switching tabs, which will only be updated on the next fire. now switching tabs updates data instantly so theres no need to update the rest of the data quickly.

also makes each stat tab update into its own proc so we can tell how much each tab update costs

---
## [percent20/hubris](https://github.com/percent20/hubris)@[8e0b13b865...](https://github.com/percent20/hubris/commit/8e0b13b86564fc7316428943dfe5fde88bb60ef4)
#### Sunday 2022-01-23 08:52:31 by Cliff L. Biffle

Remove "standalone" build.

I introduced the standalone build early on as a way of quickly iterating
on a single task, without waiting for an entire image to build -- an
equivalent to `cargo check`. It has proven somewhat useful but also
breaks things.

- The standalone build does not build the actual code you'd ship, it
  instead configures the code in "standalone mode" where a bunch of
  stuff is arbitrarily stubbed out. This means that getting a successful
  standalone build tells you little about the real build.

- You can also _forget_ to put in the standalone magic, in which case
  your actual firmware builds, but then someone else doing a
  "standalone" build later faces a cryptic failure. This is why the
  standalone builds are run in CI -- to avoid this.

- As we introduce increasing levels of configurability in tasks,
  stubbing that configuration out in arbitrary ways is getting harder.
  When it was a matter of conditional compilation driven by board name,
  we could sprinkle in some `feature = "standalone"` hacks to guide it.
  As we move toward task slots and general configuration data in the
  app.toml, the main distinguishing feature of the standalone build --
  that it does not _have_ an app.toml -- starts to become a real pain.

My iteration workflow is currently served by `cargo xtask build`. I am
not aware of any reliable way of getting RLS/rust-analyzer to work on
Hubris, even _with_ the standalone build, so this shouldn't regress
editor support.

---
## [newstools/2022-punch-nigeria](https://github.com/newstools/2022-punch-nigeria)@[196037cb85...](https://github.com/newstools/2022-punch-nigeria/commit/196037cb85f86f747c124dc26869feac92139b30)
#### Sunday 2022-01-23 11:08:59 by Billy Einkamerer

Created Text For URL [punchng.com/i-thought-policeman-who-shot-me-was-joking-when-he-cocked-his-gun-hospitalised-bauchi-truck-driver/]

---
## [yadij/squid](https://github.com/yadij/squid)@[2b6b1bcb86...](https://github.com/yadij/squid/commit/2b6b1bcb8650095c99a1916f5964305484af7ef0)
#### Sunday 2022-01-23 11:11:42 by Alex Rousskov

Bug 5055: FATAL FwdState::noteDestinationsEnd exception: opening (#877)

The bug was caused by commit 25b0ce4. Other known symptoms are:

    assertion failed: store.cc:1793: "isEmpty()"
    assertion failed: FwdState.cc:501: "serverConnection() == conn"
    assertion failed: FwdState.cc:1037: "!opening()"

This change has several overlapping parts. Unfortunately, merging
individual parts is both difficult and likely to cause crashes.

## Part 1: Bug 5055.

FwdState used to check serverConn to decide whether to open a connection
to forward the request. Since commit 25b0ce4, a nil serverConn pointer
no longer implies that a new connection should be opened: FwdState
helper jobs may already be working on preparing an existing open
connection (e.g., sending a CONNECT request or negotiating encryption).

Bad serverConn checks in both FwdState::noteDestination() and
FwdState::noteDestinationsEnd() methods led to extra connectStart()
calls creating two conflicting concurrent helper jobs.

To fix this, we replaced direct serverConn inspection with a
usingDestination() call which also checks whether we are waiting for a
helper job. Testing that fix exposed another set of bugs: The helper job
pointers or in-job connections were left stale/set after forwarding
failures. The changes described below addressed most of those problems.


## Part 2: Connection establishing helper jobs and their callbacks

A proper fix for Bug 5055 required answering a difficult question: When
should a dying job call its callbacks? We only found one answer which
required cooperation from the job creator and led to the following
rules:

* AsyncJob destructors must not call any callbacks.

* AsyncJob::swanSong() is responsible for async-calling any remaining
  (i.e. set, uncalled, and uncancelled) callbacks.

* AsyncJob::swanSong() is called (only) for started jobs.

* AsyncJob destructing sequence should validate that no callbacks remain
  uncalled for started jobs.

... where an AsyncJob x is considered "started" if AsyncJob::Start(x)
has returned without throwing.

A new JobWait class helps job creators follow these rules while keeping
track on in-progress helper jobs and killing no-longer-needed helpers.

Also fixed very similar bugs in tunnel.cc code.


## Part 3: ConnOpener fixes

1. Many ConnOpener users are written to keep a ConnectionPointer to the
   destination given to ConnOpener. This means that their connection
   magically opens when ConnOpener successfully connects, before
   ConnOpener has a chance to notify the user about the changes. Having
   multiple concurrent connection owners is always dangerous, and the
   user cannot even have a close handler registered for its now-open
   connection. When something happens to ConnOpener or its answer, the
   user job may be in trouble. Now, ConnOpener callers no longer pass
   Connection objects they own, cloning them as needed. That adjustment
   required adjustment 2:

2. Refactored ConnOpener users to stop assuming that the answer contains
   a pointer to their connection object. After adjustment 1 above, it
   does not. HappyConnOpener relied on that assumption quite a bit so we
   had to refactor to use two custom callback methods instead of one
   with a complicated if-statement distinguishing prime from spare
   attempts. This refactoring is an overall improvement because it
   simplifies the code. Other ConnOpener users just needed to remove a
   few no longer valid paranoid assertions/Musts.

3. ConnOpener users were forced to remember to close params.conn when
   processing negative answers. Some, naturally, forgot, triggering
   warnings about orphaned connections (e.g., Ident and TcpLogger).
   ConnOpener now closes its open connection before sending a negative
   answer.

4. ConnOpener would trigger orphan connection warnings if the job ended
   after opening the connection but without supplying the connection to
   the requestor (e.g., because the requestor has gone away). Now,
   ConnOpener explicitly closes its open connection if it has not been
   sent to the requestor.

Also fixed Comm::ConnOpener::cleanFd() debugging that was incorrectly
saying that the method closes the temporary descriptor.

Also fixed ConnOpener callback's syncWithComm(): The stale
CommConnectCbParams override was testing unused (i.e. always negative)
CommConnectCbParams::fd and was trying to cancel the callback that most
(possibly all) recipients rely on: ConnOpener users expect a negative
answer rather than no answer at all.

Also, after comparing the needs of two old/existing and a temporary
added ("clone everything") Connection cloning method callers, we decided
there is no need to maintain three different methods. All existing
callers should be fine with a single method because none of them suffers
from "extra" copying of members that others need. Right now, the new
cloneProfile() method copies everything except FD and a few
special-purpose members (with documented reasons for not copying).

Also added Comm::Connection::cloneDestinationDetails() debugging to
simplify tracking dependencies between half-baked Connection objects
carrying destination/flags/other metadata and open Connection objects
created by ConnOpener using that metadata (which are later delivered to
ConnOpener users and, in some cases, replace those half-baked
connections mentioned earlier. Long-term, we need to find a better way
to express these and other Connection states/stages than comments and
debugging messages.


## Part 4: Comm::Connection closure callbacks

We improved many closure callbacks to make sure (to the extent possible)
that Connection and other objects are in sync with Comm. There are lots
of small bugs, inconsistencies, and other problems in Connection closure
handlers. It is not clear whether any of those problems could result in
serious runtime errors or leaks. In theory, the rest of the code could
neutralize their negative side effects. However, even in that case, it
would only be a matter of time before the next bug bites us due to stale
Connection::fd and such. These changes themselves carry elevated risk,
but they get us closer to reliable code as far as Connection maintenance
is concerned. Without them, we will keep chasing deadly side effects of
poorly implemented closure callbacks.

Long-term, all these manual efforts to keep things in sync should become
unnecessary with the introduction of appropriate Connection ownership
APIs that automatically maintain the corresponding environments (TODO).


## Part 5: Other notable improvements in the adjusted code

Improved Security::PeerConnector::serverConn and
Http::Tunneler::connection management, especially when sending negative
answers. When sending a negative answer, we would set answer().conn to
an open connection, async-send that answer, and then hurry to close the
connection using our pointer to the shared Connection object. If
everything went according to the plan, the recipient would get a non-nil
but closed Connection object. Now, a negative answer simply means no
connection at all. Same for a tunneled answer.

Refactored ICAP connection-establishing code to to delay Connection
ownership until the ICAP connection is fully ready. This change
addresses primary Connection ownership concerns (as they apply to this
ICAP code) except orphaning of the temporary Connection object by helper
job start exceptions (now an explicit XXX). For example, the transaction
no longer shares a Connection object with ConnOpener and
IcapPeerConnector jobs.

Probably fixed a bug where PeerConnector::negotiate() assumed that
sslFinalized() does not return true after callBack(). It may (e.g., when
CertValidationHelper::Submit() throws). Same for
PeekingPeerConnector::checkForPeekAndSpliceMatched().
 
Fixed FwdState::advanceDestination() bug that did not save
ERR_GATEWAY_FAILURE details and "lost" the address of that failed
destination, making it unavailable to future retries (if any).

Polished PeerPoolMgr, Ident, and Gopher code to be able to fix similar
job callback and connection management issues.

Polished AsyncJob::Start() API. Start() used to return a job pointer,
but that was a bad idea:
    
* It implies that a failed Start() will return a nil pointer, and that
  the caller should check the result. Neither is true.

* It encourages callers to dereference the returned pointer to further
  adjust the job. That technically works (today) but violates the rules
  of communicating with an async job. The Start() method is the boundary
  after which the job is deemed asynchronous.
    
Also removed old "and wait for..." post-Start() comments because the
code itself became clear enough, and those comments were becoming
increasingly stale (because they duplicated the callback names above
them).

Fix Tunneler and PeerConnector handling of last-resort callback
requirements. Events like handleStopRequest() and callException() stop
the job but should not be reported as a BUG (e.g., it would be up to the
callException() to decide how to report the caught exception). There
might (or there will) be other, similar cases where the job is stopped
prematurely for some non-BUG reason beyond swanSong() knowledge. The
existence of non-bug cases does not mean there could be no bugs worth
reporting here, but until they can be identified more reliably than all
these benign/irrelevant cases, reporting no BUGs is a (much) lesser
evil.

TODO: Revise AsyncJob::doneAll(). Many of its overrides are written to
check for both positive (i.e. mission accomplished) and negative (i.e.
mission cancelled or cannot be accomplished) conditions, but the latter
is usually unnecessary, especially after we added handleStopRequest()
API to properly support external job cancellation events. Many doneAll()
overrides can probably be greatly simplified.

---
## [Vishalcj17/android_kernel_qcom_sm8350](https://github.com/Vishalcj17/android_kernel_qcom_sm8350)@[82b44b7207...](https://github.com/Vishalcj17/android_kernel_qcom_sm8350/commit/82b44b7207434d4f860bc63efb50468afc97afda)
#### Sunday 2022-01-23 12:31:23 by alk3pInjection

techpack: display: Handle dim for udfps

Apparently, los fod impl is better than udfps cuz it
has onShow/HideFodView hook, which allows us to toggle
dimlayer seamlessly.

Since udfps only partially supports the former one,
we'd better kill dim in kernel. This is kinda a hack
but it works well, bringing perfect fod experience
back to us.

Also implement a panel status check to ensure that
the dim layer dies when display is off.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Change-Id: I14d028a821e4a776bc62feb5836b3fe012bc808e

---
## [njprov/mazes](https://github.com/njprov/mazes)@[48bae08c3a...](https://github.com/njprov/mazes/commit/48bae08c3ac0756e2a05f9cad8800df1dab33b1a)
#### Sunday 2022-01-23 14:42:40 by Jack Provance

Create LICENSE.txt

do what the fuck you want to public license

---
## [TheGamingTime/Agronomy-Crisis-Sauce-code](https://github.com/TheGamingTime/Agronomy-Crisis-Sauce-code)@[c9ab7e8851...](https://github.com/TheGamingTime/Agronomy-Crisis-Sauce-code/commit/c9ab7e88511ba0376daa38cdaed36d372b7ebd9c)
#### Sunday 2022-01-23 15:53:40 by TheGamingTime

new among us in real life

i hate myself kill me pls

---
## [chyzman/ctft](https://github.com/chyzman/ctft)@[b4bb2cb0ae...](https://github.com/chyzman/ctft/commit/b4bb2cb0aebc4d8448a7060bea5450538eac7589)
#### Sunday 2022-01-23 17:05:22 by chyzman

OMEGA REG
THE REGISTRY TO END ALL OTHER REGISTRIES
ITS SO FUCKING EFFICIENT LIKE HOLY SHIT THE CODE IS LIKE 1/10 THE SIZE IT USED TO BE

---
## [Dimensions-Softwares/project-destiny](https://github.com/Dimensions-Softwares/project-destiny)@[0e5aab0325...](https://github.com/Dimensions-Softwares/project-destiny/commit/0e5aab0325677a8570dbbc17a6d0f6c3cd9c2c22)
#### Sunday 2022-01-23 18:03:29 by Only Void

Tried to deleted reusable workflows to see if it's the problem

God i hate my life

---
## [Tomcat-42/dwm](https://github.com/Tomcat-42/dwm)@[67d76bdc68...](https://github.com/Tomcat-42/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2022-01-23 18:24:42 by Chris Down

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f1dc6f1250...](https://github.com/mrakgr/The-Spiral-Language/commit/f1dc6f1250eb733f36ea90012d29c78d00fcb412)
#### Sunday 2022-01-23 18:57:42 by Marko Grdinić

"11:05am. Let me chill a bit more and I will start.

11:35am. Let me start. I've had my bit of fun. Lately, I've started reading Infinite Dendogram again. It is as fun as it was before.

11:45am. Ok, I see. Exporting as obj, exports everything in that file as an object. I'd have to separate it by hand.

12:05pm. Ok, I've separated the leaf and the petal into separate Blender files, exported them in obj files, and imported them in Houdini. First order of business is to figure out how to emulate the solidify modifier in it. I guess in Houdini that should just be extrude. Let me give it a try. After that I'll try emulating the bulb.

12:10pm. The bulb that I did came out really well, so it is a shame to have to do it again, but I must. This will be good practcie.

12:20pm. Extrusion works, but the normals are inverted. How do I fix that?

https://youtu.be/ICZv_u65hH8
Reversing & Correcting Normals in Houdini Pt. 4/4 – Correcting Primitive Normals

Let me watch this, it is only 2.5m.

https://youtu.be/ICZv_u65hH8?t=86

No way would I have been able to figure this out on my own. But this solution is really a lot more complex than I thought.

https://youtu.be/ICZv_u65hH8?t=114

Exploded view. so that is how they do that assembly effect.

12:40pm. The petals have been aranged. Let me do the leaves.

1pm. Let me go have breakfast.

1:45pm. Let me do the chores and I will resume. I am making slow progress, but I am really into it.

2:10pm. I am back. Let me resume.

2:40pm. I really do adore the procedural workflow. Putting the leaves in places was great. Now I have a slight problem, let me ask about it in the Houdini thread. Though, before that, let me try fixing it in Blender. I'll try a different export mode. It seems it has two different types of `.obj` exports.

Nope, that did not help any.

2:50pm. Ah whatever, let me ask in /3/ thread. The imported leaves have a weird checkerboard texture on their stem faces for some reason.

3:20pm. I worked a bit more on it. Now the bulb is complete. I did a wonderful work.

Hmmm, this is so strange.

3:50pm. No I do not have any idea why I need both a reverse and a normal node for this to work given that normals are there. Perhaps polyextrude does not calculate the normals properly. Even so I don't understand why simply fliping them does not work. At any rate, it does not matter. The bulb I create is just as good as the one in Blender. I have every reason to feel proud. And unlike the Blender one, for this one I have the entire node network right there and I can easily come in and change some of the transforms.

I can use this for example to implement a rotator for the sake of opening and closing the bulb. This would be hell to do in Blender.

Right now, I do not really understand how to parameterize the node network just yet. I also do not know how to cleanly factor the node tree.

3:55pm. Still the potential is there. I am thinking whether I should resume the tutorial from yesterday. I got some of my art urge satisfied, and am starting to hunger for knowledge.

But let me leave that aide for now. Let me see how far I can go with doing the stalk on my own.

4:05pm. Ah, let me take a break. I feel really satisfied right now even though I honestly haven't done much.

4:30pm. Let me resume. I'll read the Ayakashi, and come to think of it the Mahoako thread from yesterday, later. Right now, let me focus on the stalk. This is a great time to figure out how curves work in Houdini. If I can't figure it out, I'll go back to tutorials. I think that those network tutorials that I've decided to skip yesterday should teach me how to use the nets properly.

5pm. How did I spend 30m just fiddling around. At any rate, I am not making progress. I just about drew a curve, but I do not know how to use it. it is not like in Blender where I just have the curve to mesh node and things are self explanatory.

Let me watch tutorials. I guess I'll start with the network ones. I'll want to figure out how to factor some of the things that I've done. After that I'll move to curve tutorials. Focus me, I can do this thing. Bit by bit, I'll learn Houdini.

5:05pm. Focus me. Where was I yesterday. I should still have time in the day for one more module.

5:50pm. Had to leave for lunch.

https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273890/posts/4431828

The stuff in the previous lesson I already knew, but I should pay attention to this one.

Hmmmm...let me try something. Something just occurred to me.

Ah, no it is fine. Thankfully the geometry is ignoring the object level transforms for the specific objects it is importing.

6:10pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273890/posts/4431920

I should have gone for the curve tutorials. This is so boring.

https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273890/posts/5150144

I had no idea you could just extrude a curve in Houdini, that is not the case in Blender. So that is how he created the studio background. In Blender I'd just extrude an edge of a plane upwards and then bevel it.

Ah, this chapter also covers parenting. I was wondering what wiring at the object level does. Nice. I really like how Houdini organizes its collections more than Blender.

6:30pm. Let me pause just a bit to make an unrelated remark because I have been thinking about it for a while now. Just how are normal maps related to the height maps? I think that you could go from height -> normal, but what if for example you had both, but normals were wrong? I've been wondering about that. I'll have to dig up an tutorial that explains that.

Let me go back to the task at hand for now.

7:20pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273890/posts/4432000

There is interesting stuff here. Let me try the move centroid to origin. Yeah, this is a really useful button. It has allowed me to get the XY coords for the final tranform just right.

7:25pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273891/posts/4432018

Let me stop here. Only a single module of this course is left. It is too bad I do not have have the paid stuff. Maybe I could put in a request in the piracy thread? I doubt it. Forget it.

What I am going to do tomorrow is finish this course, and then move on to the author's modeling tutorials. He has a bunch of stuff on curves. I'd be very surprised if he does nto cover how to turn it into a mesh. But come to think of it, maybe the way to do that is to just put a bunch of meshes on the scattered point and then bridge them.

The way he extruded a curve to get that curved studio surface background was a hint to me.

Or rather than bridge, maybe loft is what I need. I've only been introduced to those two operations in the loop tools plugin video, so they are not at the forefront of my mind. I bet this is how Blender turns the curve into a mesh internally anyway. I'll leave it for later.

Even if I have this idea, that still leaves figuring out how to set the radius at a particular point. For that I'd need the spline factors. Right now I do not know how to get them, and I'll really need somebody to show it to me. After I exhaust the tutorials, I'll have to start reading the docs and checking out the examples there.

7:40pm. Let me not worry about that now. Right now let me rest. Ayakashi, Mahoako, Dendrogram along with the bath are waiting for me. Let me take off for the day here.

Even though I was just moving objects around today, I was decently into it. I did pretty much the same thing as in Blender, but right now I have the entire history and will be able to change things at a moment's notice should I want to. In Blender I'd have to change everything from scratch.

7:45pm. Hmmm, in fact it would be worth it to change the way bulb leaves are placed.

7:50pm. Well, I'll leave them the way they are. They way I am handling the pivot points in this object was awkward for the leaves and I see a better way of doing it now."

---
## [ungeskriptet/linux](https://github.com/ungeskriptet/linux)@[d7ee81ad09...](https://github.com/ungeskriptet/linux/commit/d7ee81ad09f072eab1681877fc71ec05f9c1ae92)
#### Sunday 2022-01-23 19:32:00 by Dan Carpenter

NFC: nci: Add some bounds checking in nci_hci_cmd_received()

This is similar to commit 674d9de02aa7 ("NFC: Fix possible memory
corruption when handling SHDLC I-Frame commands").

I'm not totally sure, but I think that commit description may have
overstated the danger.  I was under the impression that this data came
from the firmware?  If you can't trust your networking firmware, then
you're already in trouble.

Anyway, these days we add bounds checking where ever we can and we call
it kernel hardening.  Better safe than sorry.

Fixes: 11f54f228643 ("NFC: nci: Add HCI over NCI protocol support")
Signed-off-by: Dan Carpenter <dan.carpenter@oracle.com>
Signed-off-by: David S. Miller <davem@davemloft.net>

---
## [TwistedTom/mame](https://github.com/TwistedTom/mame)@[137649ccec...](https://github.com/TwistedTom/mame/commit/137649ccec8159929e68212470b41eeed136b252)
#### Sunday 2022-01-23 19:34:20 by Firehawke

New working software list additions (apple2gs_flop_clcracked.xml) (#8712)

* New working software list additions (apple2gs_flop_clcracked.xml)
-----------------------------------------------------------------

Aesop's Fables (cleanly cracked) [Brian Troha]
All About America (cleanly cracked) [Brian Troha]
Ancient Land of Ys (cleanly cracked) [Brian Troha]
Arkanoid (Version 12-Jan-89) (cleanly cracked) [Brian Troha]
Arkanoid II: Revenge of Doh (Version 29-Aug-89) (cleanly cracked) [Brian Troha]
Arkanoid II: Revenge of Doh (Version 18-Jul-89) (cleanly cracked) [Brian Troha]
Battle Chess (cleanly cracked) [Brian Troha]
Block Out (Version 1.0) (cleanly cracked) [Brian Troha]
Bubble Ghost (cleanly cracked) [Brian Troha]
Bubble Ghost - Hard Drive compatible (cleanly cracked) [Brian Troha]
Calendar Crafter (Version 1.2) (cleanly cracked) [Brian Troha]
California Games (cleanly cracked) [Brian Troha]
Captain Blood (cleanly cracked) [Brian Troha]
Cavern Cobra (cleanly cracked) [Brian Troha]
Club Backgammon (Version 2.0) (cleanly cracked) [Brian Troha]
Club Backgammon (Version 1.0) (cleanly cracked) [Brian Troha]
Cribbage King / Gin King (Version 1.01) (cleanly cracked) [Brian Troha]
Defender of the Crown (cleanly cracked) [Brian Troha]
Déjà Vu (cleanly cracked) [Brian Troha]
Déjà Vu II: Lost in Las Vegas (cleanly cracked) [Brian Troha]
Designer Prints (Version 1.0) (cleanly cracked) [Brian Troha]
Designer Puzzles (Version 1.0) (cleanly cracked) [Brian Troha]
Destroyer (cleanly cracked) [Brian Troha]
Downhill Challenge (cleanly cracked) [Brian Troha]
Fantavision (Version 2.1) (cleanly cracked) [Brian Troha]
Fantavision (Version 1.0) (cleanly cracked) [Brian Troha]
Fast Break (cleanly cracked) [Brian Troha]
Final Assault (cleanly cracked) [Brian Troha]
Gauntlet (cleanly cracked) [Brian Troha]
Geometry (Version 1.0) (cleanly cracked) [Brian Troha]
Gnarly Golf (cleanly cracked) [Brian Troha]
Grand Prix Circuit (cleanly cracked) [Brian Troha]
Great Western Shootout (cleanly cracked) [Brian Troha]
Hacker II: The Doomsday Papers (cleanly cracked) [Brian Troha]
Hardball! (cleanly cracked) [Brian Troha]
Hostage: Rescue Mission (cleanly cracked) [Brian Troha]
Impossible Mission II (cleanly cracked) [Brian Troha]
Jack Nicklaus' Greatest 18 Holes of Major Championship Golf (cleanly cracked) [Brian Troha]
Jigsaw (Version 1.4 - 022988) (cleanly cracked) [Brian Troha]
King's Quest - Quest for the Crown (cleanly cracked) [Brian Troha]
King's Quest II - Romancing The Throne (cleanly cracked) [Brian Troha]
King's Quest III - To Hier is Human (cleanly cracked) [Brian Troha]
LaserForce (cleanly cracked) [Brian Troha]
Leisure Suit Larry in the Land of the Lounge Lizards (cleanly cracked) [Brian Troha]
Magical Myths (cleanly cracked) [Brian Troha]
Mancala (Version 1.0) (cleanly cracked) [Brian Troha]
Marble Madness (cleanly cracked) [Brian Troha]
Math Blaster Plus! (Version 1.1) (cleanly cracked) [Brian Troha]
Math Blaster Plus! (Version 1.0) (cleanly cracked) [Brian Troha]
Math Wizard (cleanly cracked) [Brian Troha]
Mavis Beacon Teaches Typing (Version 1.8 21-Dec-88) (cleanly cracked) [Brian Troha]
Mavis Beacon Teaches Typing (Version 1.2 16-Nov-87) (cleanly cracked) [Brian Troha]
Mean 18 (cleanly cracked) [Brian Troha]
Mercury (Version 1.0) (cleanly cracked) [Brian Troha]
Music Construction Set (Version 1.0) (cleanly cracked) [Brian Troha]
Neuromancer (cleanly cracked) [Brian Troha]
Paperboy (cleanly cracked) [Brian Troha]
Pipe Dream (cleanly cracked) [Brian Troha]
Qix (Version 1.4? 16-Jan-90) (cleanly cracked) [Brian Troha]
Read and Rhyme (cleanly cracked) [Brian Troha]
Read-a-Rama (cleanly cracked) [Brian Troha]
Reader Rabbit (Version 2.3) (cleanly cracked) [Brian Troha]
Reader Rabbit (Version 2.2) (cleanly cracked) [Brian Troha]
Reading and Me (Version 1.0) (cleanly cracked) [Brian Troha]
Sea Strike (Version 1.0) (cleanly cracked) [Brian Troha]
Serve and Volley (cleanly cracked) [Brian Troha]
Shanghai (Version 15-Sep-87) (cleanly cracked) [Brian Troha]
Shanghai (Version 20-Jan-87) (cleanly cracked) [Brian Troha]
ShowOff (Version 1.1) (cleanly cracked) [Brian Troha]
Silent Service (Version 925.01) (cleanly cracked) [Brian Troha]
Silpheed - Super Dogfighter (cleanly cracked) [Brian Troha]
Skate or Die (Version 1.1 07-Oct-88) (cleanly cracked) [Brian Troha]
Skate or Die (Version 1.0 12-Aug-88) (cleanly cracked) [Brian Troha]
Space Quest - The Sarien Encounter (cleanly cracked) [Brian Troha]
Space Quest II - Vohual's Revenge (cleanly cracked) [Brian Troha]
Spirit of Excalibur (cleanly cracked) [Brian Troha]
Storybook Weaver (Version 1.0) (cleanly cracked) [Brian Troha]
Storybook Weaver - World of Adventure (Version 1.0) (cleanly cracked) [Brian Troha]
Storybook Weaver - World of Make-Believe (Version 1.0) (cleanly cracked) [Brian Troha]
Street Sports Soccer (cleanly cracked) [Brian Troha]
Superstar Ice Hockey (cleanly cracked) [Brian Troha]
Tales From The Arabian Nights (cleanly cracked) [Brian Troha]
Task Force (cleanly cracked) [Brian Troha]
Tetris (cleanly cracked) [Brian Troha]
The Adventures of Sinbad (cleanly cracked) [Brian Troha]
The Duel: Test Drive II (cleanly cracked) [Brian Troha]
The Fidelity Chessmaster 2100 (Version 1.1 17-Nov-88) (cleanly cracked) [Brian Troha]
The Fidelity Chessmaster 2100 (Version 1.01 28-Sep-88) (cleanly cracked) [Brian Troha]
The Graphics Studio (cleanly cracked) [Brian Troha]
The Immortal (cleanly cracked) [Brian Troha]
The King of Chicago (cleanly cracked) [Brian Troha]
The Last Ninja (cleanly cracked) [Brian Troha]
The Logic Master (Version 1.5) (cleanly cracked) [Brian Troha]
The Print Shop (Version 1.0) (cleanly cracked) [Brian Troha]
The Third Courier (cleanly cracked) [Brian Troha]
The Tower of Myraglen (Version 1.0) (cleanly cracked) [Brian Troha]
The Wonders of the Animal Kingdom (cleanly cracked) [Brian Troha]
The Word Master (cleanly cracked) [Brian Troha]
Thexder (Version 2.7) (cleanly cracked) [Brian Troha]
Topdraw (Version 1.00A) (cleanly cracked) [Brian Troha]
TrianGo (Version 1.0) (cleanly cracked) [Brian Troha]
Uninvited (cleanly cracked) [Brian Troha]
Vegas Craps (Version 1.0) (cleanly cracked) [Brian Troha]
Vegas Gambler (Version 1.1 25-Jul-88) (cleanly cracked) [Brian Troha]
Vegas Gambler (Version 1.0 07-Jun-88) (cleanly cracked) [Brian Troha]
War in Middle Earth (cleanly cracked) [Brian Troha]
Where in the U.S.A. is Carmen Sandiego? (cleanly cracked) [Brian Troha]
Where in the World is Carmen Sandiego? (cleanly cracked) [Brian Troha]
Winter Games (cleanly cracked) [Brian Troha]
World Games (cleanly cracked) [Brian Troha]
World Tour Golf (cleanly cracked) [Brian Troha]
Writer's Choice Elite (cleanly cracked) [Brian Troha]
Xenocide (Version 25-Sep-89) (unprotected) [Brian Troha]
Xenocide (Version 11-Aug-89) (cleanly cracked) [Brian Troha]
Zany Golf (cleanly cracked) [Brian Troha]

---
## [fasmga/frontend](https://github.com/fasmga/frontend)@[10f06615d1...](https://github.com/fasmga/frontend/commit/10f06615d1c8815d1491b9b4d9f92bc94fed8c67)
#### Sunday 2022-01-23 20:32:39 by StuckDuck

D-D-Daytrip took it to ten (hey)  Baby back, ayy, couple racks, ayy Couple Grammys on him Couple plaques, ayy That's a fact, ayy Throw it back, ayy, throw it back, ayy  And this one is for the champions I ain't lost since I began, yeah Funny how you said it was the end, yeah Then I went did it again, yeah  I told you long ago on the road I got what they waiting for I don't run from nothing, dog Get your soldiers, tell 'em I ain't layin' low You was never really rooting for me anyway When I'm back up at the top, I wanna hear you say "He don't run from nothin', dog Get your soldiers, tell 'em that the break is over" (uh)  Need to, uh, need to get this album done Need a couple number onеs Need a plaque on every song Need mе like one with Nicki now Tell a rap nigga I don't see ya (hah) I'm a pop nigga like Bieber (hah) I don't fuck bitches, I'm queer (hah) But these niggas bitches like Madea, yeah, yeah, yeah, ayy (yeah)  Oh, let's do it I ain't fall off, I just ain't release my new shit I blew up, now everybody tryna sue me You call me Nas, but the hood call me Doobie  And this one is for the champions I ain't lost since I began, yeah Funny how you said it was the end, yeah Then I went did it again, yeah  I told you long ago on the road I got what they waiting for (I got what they're waiting for) I don't run from nothing, dog Get your soldiers, tell 'em I ain't layin' low (bitch, I ain't runnin' from nowhere) You was never really rooting for me anyway (ooh, ooh) When I'm back up at the top, I wanna hear you say (ooh, ooh) "He don't run from nothin', dog Get your soldiers, tell 'em that the break is over" (yeah)  My track record so clean, they couldn't wait to just bash me I must be gettin' too flashy, y'all shouldn't have let the world gas me (woo) It's too late 'cause I'm here to stay and these girls know that I'm nasty (mmm) I sent her back to her boyfriend with my handprint on her ass cheek City talkin', we takin' notes Tell 'em all to keep makin' posts Wish he could, but he can't get close OG so proud of me that he chokin' up while he makin' toasts I'm the type that you can't control, said I would, then I made it so  I don't clear up rumors (ayy), where's y'all sense of humor? (Ayy) I'm done makin' jokes 'cause they got old like baby boomers Turned my haters to consumers, I make vets feel like they juniors (juniors) Say your time is comin' soon, but just like Oklahoma (mmm) Mine is comin' sooner (mmm), I'm just a late bloomer (mmm) I didn't peak in high school, I'm still out here gettin' cuter (woo) All these social networks and computers Got these pussies walkin' 'round like they ain't losers  I told you long ago on the road I got what they waiting for (I got what they waiting for) I don't run from nothing, dog Get your soldiers, tell 'em I ain't layin' low (bitch, I ain't runnin' from nowhere) You was never really rooting for me anyway When I'm back up at the top, I wanna hear you say "He don't run from nothin', dog Get your soldiers, tell 'em that the break is over" (yeah)  I'm the industry baby, mmm (yeah) I'm the industry baby (yeah)

---
## [KDE/kirigami](https://github.com/KDE/kirigami)@[2a143511ce...](https://github.com/KDE/kirigami/commit/2a143511ce1d24a21bb8f29b10e3c29f9b28b201)
#### Sunday 2022-01-23 20:44:44 by Noah Davis

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

- `gridUnit` is `QFontMetricsF::height()`. It is 18px with Noto Sans 10
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

- smallSpacing is `std::floor(gridUnit / 4)`. With Noto Sans 10, this is
4px. With Noto Sans 11, this is 5px; a 1.25x increase.
- If it rounded instead, it would be 5px with Noto Sans 10 and 6px
with Noto Sans 11; a 1.2x increase.

- largeSpacing is `smallSpacing * 2`.

Do not assume that `smallSpacing * 4` or `largeSpacing * 2` will be
equal to gridUnit.

Alternative font based solutions for spacing units that I have pondered
-----------------------------------------------------------------------

- What about pixelSize? Could we use that instead of font height? It
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
- Noto Sans 10 has a pixelSize of 13.33 (10/0.75) and Noto Sans 11 has
a pixelSize of 14.67 (11/0.75). Making consistent/good integer based
spacing units from those might be a little tricky.

- What about measuring the real height of some characters and basing
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
## [alba-tr0ss/DH](https://github.com/alba-tr0ss/DH)@[695a833518...](https://github.com/alba-tr0ss/DH/commit/695a833518d8225c73fab390acbc81a9deb091a6)
#### Sunday 2022-01-23 20:52:14 by Albatross

swarm attack #1.5

god i fucking hate the team validator

---
## [KDE/kirigami](https://github.com/KDE/kirigami)@[eabe91d986...](https://github.com/KDE/kirigami/commit/eabe91d986f59b07bea26b513951b782d375e5b2)
#### Sunday 2022-01-23 21:24:02 by Noah Davis

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
## [ngadss/friday-night-fever](https://github.com/ngadss/friday-night-fever)@[4b8a2dc67f...](https://github.com/ngadss/friday-night-fever/commit/4b8a2dc67fd6f15ade122d660a58fb4e8d6a75fb)
#### Sunday 2022-01-23 21:32:12 by AlyssaTheCoder

tony monero i just contracted feveritis

go fuck yourself

---
## [newstools/2022-daily-post-nigeria](https://github.com/newstools/2022-daily-post-nigeria)@[6f5e3cf798...](https://github.com/newstools/2022-daily-post-nigeria/commit/6f5e3cf79812fdda1fd796d61ccff219c225b350)
#### Sunday 2022-01-23 21:43:08 by Billy Einkamerer

Created Text For URL [dailypost.ng/2022/01/23/2023-god-can-pick-female-president-from-living-faith-church-bishop-oyedepo/]

---
## [DigitalCharlie/a-day-at-the-fair](https://github.com/DigitalCharlie/a-day-at-the-fair)@[d2910303c7...](https://github.com/DigitalCharlie/a-day-at-the-fair/commit/d2910303c70359ba730e32414a13ca55ad6e95db)
#### Sunday 2022-01-23 21:53:29 by Digital Charlie

Holy shit the event loop actually works now. The solution feels really silly but at least it works.

---
## [Canohaaaaaaa/TerraGov-Marine-Corps](https://github.com/Canohaaaaaaa/TerraGov-Marine-Corps)@[4529479889...](https://github.com/Canohaaaaaaa/TerraGov-Marine-Corps/commit/4529479889ccc617b1aee8519755e6ab5aa49b08)
#### Sunday 2022-01-23 23:11:40 by hyper2snyper

Lasgun fixes (#9183)

* FUCK YOU SO MUCH EGUNS

* Update guns_codex.dm

---
## [blessedmulligan/tgstation](https://github.com/blessedmulligan/tgstation)@[4610f700eb...](https://github.com/blessedmulligan/tgstation/commit/4610f700eb74a3a41555e69c4904ad897caf2d99)
#### Sunday 2022-01-23 23:39:03 by LemonInTheDark

Fixes up multiz atmos connection, cleans some things up in general (#63270)

About The Pull Request

ALLLRIGHT so
Multiz atmos was letting gas flow down into things that should be well, not flowable into
Like say doors, or windows.

This is weird.

Let's get into some context on why yeah?

First, how do things work currently?

atoms have a can_atmos_pass var defined on them. This points to a define that describes how they interact with
flow.
ATMOS_PASS_NO means well, if we're asked, block any attempts at flow. This is what walls use.
ATMOS_PASS_YES means the inverse
ATMOS_PASS_DENSITY means check our current density
ATMOS_PASS_PROC means call can_atmos_pass, we need some more details about this attempt

These are effectively optimizations.

That var, can_atmos_pass is accessed by CANATMOSPASS() the macro
It's used for 3 things.

1: Can this turf share at all?
2: Can this turf share with another turf
3: Does this atom block a share to another turf

All of this logic is bundled together to weed out the weak.

Anyway, so when we added multiz atmos, we effectively made a second version of this system, but for vertical
checks.

Issue here, we don't actually need to.
The only time we care if a check is vertical or not is if we're talking to another turf, it's not like you'll
have an object that only wants to block vertical atmos.
And even if you did, that's what ATMOS_PASS_PROC is for.

As it stands we need to either ignore any object behavior, or just duplicate can_atmos_pass but again.
Silly.

So I've merged the two, and added an arg to mark if this is a verical attempt.
This'll fix things that really should block up/down but don't, like windows and doors and such.

Past that, I've cleaned can_atmos_pass up a bit so it's easier for people to understand in future.
Oh and I removed the second CANATMOSPASS from immediate_calculate_adjacent_turfs.
It isn't a huge optimization, and it's just not functional.

It ties into zAirOut and zAirIn, both of which expect to be called with a valid direction.
So if say, you open a door that's currently blocking space from leaking in from above, you end up with the door
just not asking the space above if it wants to share, since the door can't zAirOut with itself.

Let's just wipe it out.

This makes the other code much cleaner too, heals the soul.

Anyway yadeyada old as ass bug, peace is restored to the kingdom, none noticed this somehow you'd think people
would notice window plasma, etc etc.
Why It's Good For The Game

MUH SIMULATION
Also fuck window gas
Changelog

cl
fix: Fixed gas flowing into windows from above, I am.... so tired
fix: Fixes gas sometimes not moving up from below after a structure change, see above
/cl

---
## [flintforge/gqlgen](https://github.com/flintforge/gqlgen)@[43b56cbaf3...](https://github.com/flintforge/gqlgen/commit/43b56cbaf3f1de1d1ad379055ab1de157592cf38)
#### Sunday 2022-01-23 23:51:57 by Ben Kraft

Forward `go mod tidy` stdout/stderr

This is a command that can fail (in my case I think for stupid reasons
in a hell of my own construction, but nonetheless).  Right now we just
get
```
$ go run github.com/Khan/webapp/dev/cmd/gqlgen
tidy failed: go mod tidy failed: exit status 1
exit status 3
```
which is not the most informative.  Now, instead, we'll forward its
output to our own stdout/stderr rather than devnull.

---

