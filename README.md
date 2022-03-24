## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-23](docs/good-messages/2022/2022-03-23.md)


1,774,734 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,774,734 were push events containing 2,855,696 commit messages that amount to 205,744,442 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [KDr2/pytorch](https://github.com/KDr2/pytorch)@[65329f4fac...](https://github.com/KDr2/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Wednesday 2022-03-23 00:03:04 by Edward Z. Yang

Disable meta device tests.

After discussion with Can Balioglu, we have concluded that
https://github.com/pytorch/pytorch/pull/53682 , while clever, is more
trouble than it is worth.  The main problem is that whenever someone
adds support for new meta tensors, they then get dozens of new test case
failures, because tests that were previously halted by lack of support
for an operator on meta tensors, now have gotten further and hit some
logic which expects to be able to, e.g., pull out a real value from a
tensor (which clearly doesn't work).  This is very annoying and time
consuming!  Most of these tests aren't written with meta device in
mind, and it's not a good use of time to try to make them more generic.

The plan on record is to switch meta testing to OpInfo, but that patch
will take some time to prepare for now I want to stem the bleeding.  I
don't think we're at high risk for regressions here because meta tensors
mostly share logic with their regular brethren.

Signed-off-by: Edward Z. Yang <ezyangfb.com>

Pull Request resolved: https://github.com/pytorch/pytorch/pull/74468

Approved by: https://github.com/mruberry

---
## [pj1312/tgstation](https://github.com/pj1312/tgstation)@[dd747fcc5a...](https://github.com/pj1312/tgstation/commit/dd747fcc5a46df051a5fe0e42950c46c72269244)
#### Wednesday 2022-03-23 00:43:17 by MrMelbert

BIDDLE HERETICS: Heretic revamp! (Shadow Realm, UI Overhaul, Refactoring, and Murderhoboing Tweaks)  (#64658)

About The Pull Request

This PR seeks to revamp heretic in it's almost entirety.

Closes #58435
Closes #62114
Closes #63605

image
Gameplay changes:

    The heretic no longer starts with a Codex Cicatrix or a Living Heart.
        Heretics now draw transmutation runes by using any writing tool while having Mansus Grasp active.
            The Mansus Grasp can be used to remove heretic runes.
        Draining influences can be done with "right click".
            While draining, people who examine you may get a message hinting that you're interacting with an influence.
            Drained influences can also be dispersed with anomaly neutralizers!
        The Codex Cicatrix is now a researchable item that lets you gain additional knowledge from influences.
            The Codex can still draw and remove runes, and does it faster.
        The Living Heart is now the heretic's heart. Literally. It's the heart in their chest. Their heart takes on the appearance of a living heart, and they can pulse it on demand to track their targets. This makes an audible noise.
            If your heart is lost (you're disemboweled or whatever), you need to do a ritual to regain it!

    Casting any heretic spell (besides Grasp) requires a Focus.
        A Heretic Focus is a neck item they can transmute.
        Heretic robes also function as a focus when toggled up.
        Ascending also disables the need for a focus, because of course.

    Heretics now gain 1 knowledge point passively every 20 minutes.

    Sacrificing has been revamped entirely.
        A heretic now gains four sacrifice targets on spawn.
            One random crewmember
            One member of their department
            One member of security
            One member of command (a "high value" sacrifice)
        You can sacrifice people who are in in soft-crit, hard-crit, or dead.
        Sacrificing someone will cuff them (if they are not), HEAL them, revive them, and set them unconscious. After a short time. they will be sent to a shadow realm. This shadow realm is themed to your heretic type.
            The shadow realm is a 2 minute long survival challenge where the sacrificee is subject to a constant barrage of shadowy hands.
            If they survive, they are teleported back to a random turf with no memory of how they got there. They'll also slur a TON to get the point across.
            If they die, their corpse is teleported back to a random turf on the station.

    No more multi-hearting! Your targets are your own.
        BUT adds a knowledge that allows heretics to reroll their sacrifice targets with a ritual.

    Each path now has a "Rituals of Knowledge". These are randomly generated rituals that may be difficult to complete but awards knowledge points in return.

    Ascending now has some requirements.
        To learn the ascension ritual, you need to complete all of the objective you are assigned.
        The ascension ritual now each have a varied requirement, instead of "needing 3 bodies" only.

    Other minor gameplay changes:
        Lots of balance tweaking.
            Buffed some summons.
            Buffed the Lord of the Night very slightly.
            Nerfed the Madness Mask.
        Put a limit on the amount of blade transmutations possible at once. 3 for flesh, 2 for other paths.
        Logs of BUG fixing.
        Rust Grasp is now based on right click for surfaces instead of combat mode.
        General grammar and flavor tweaks a ll around.

Admin / code changes:

    Revamped the way heretics appear within the traitor panel.
        You can now easily see who they're targeting for sacrifice and what they have researched
        Also adds some helpful buttons to heretics, like giving them points!
    Refactored much, much of heretic code
        LIKE ALL OF HERETIC CODE WAS IN 4 FILES.
            Split up all the knowledge, spells, and items that belong to the heretic into their own files and folders.
        Not only that, but everything internally was still named "Eldritch Cultist" and similar.
            Almost every mention of "Eldritch Cultist" has been properly replaced by "Heretic".
    Much better reference handling all around.
    General code improvements over heretic stuff.
    Unit tests, because of course.

Todo

Sprites for the focus

    Look at adding 1-2 other objectives prior to ascension. Theft? Special rituals? ("Rust [x] tiles to be able to ascend")

Why It's Good For The Game
Okay but why?

Heretics are not in a good place at the moment, this much is clear. They've been completely disabled on MRP for this reason.

The reasoning is simple: A lot of murder.
There's nothing inherently wrong with an antagonist heavy with murder, but the Heretic really missed the mark.
Gib, gib, gib, then ascend so you can keep killing.

In the background, the Heretic was FULL of flavorful spells, rituals, and "lore" stolen from Cultist Simulator that was unfortunate enough to be shackled to the heretic's gameplay loop.

So, this revamp aims to amend that:

Dial back the heretic's focus on mass murder and put more focus on the heretic's interesting flavor.
Spooky maintenance rituals, knowledge seeking maniac.

    Sacrifice no longer outright kills / requires murder, meaning a heretic can progress without racking up a bodycount.
    Influence is gained passively over time, so they can spend influence on more interesting side paths.
    Side paths are required to progress to ascension, so they're encouraged to explore new things.

Ultimately, while there still may be a little way to go, this PR seeks to take a good leap in starting it.
Changelog

cl Melbert
add: Large scale heretic revamp!
expansion: The Codex Cicatrix is no longer a roundstart heretic item. Research is handled through their antag info UI. Rune drawing is done by using a writing tool with Mansus Grasp active in your offhand. The actual Codex is an unlockable ritual item now.
expansion: The Living Heart is no longer a roundstart heretic item - their actual heart now becomes their Living Heart, and it makes a sound when triggered. Losing your heart (being disemboweled) will require you to do a ritual to regain it.
expansion: The Hereic Antag UI has been overhauled, and now hosts much of their mechanics as well as providing some helpful tips for newer players.
expansion: Most heretic spells now require a focus to cast. All heretics can make a basic focus necklace, and some heretic equipment also functions as a focus. (Credit to Imaginos for the focus sprite!)
expansion: Heretics now passively gain +1 influence every 20 minutes.
expansion: Heretic sacrificing has been reworked. You can now sacrifice people who are in soft crit or weaker. Sacrificing someone heals them, cuffs them, and teleports them to the SHADOW REALM, where they must dodge a barrage of hands to survive. Survive long enough and you return without memory - die, and your body will be thrown back.
expansion: Heretics now have a few new rituals, including the Ritual of Knowledge, a randomly generated ritual that awards knowledge points.
expansion: Heretic ascension now has a few requirements - you must complete your objectives assigned to you prior to learning the final ritual, and all the final rituals have been changed a bit!
qol: Using the Heretic's Mansus Grasp on surfaces (EX: Rust Grasp) now works on right-click, instead of combat mode.
qol: Used heretic influences can now be removed with a Anomaly Neutralizers.
balance: Some heretic rituals are now limited in the amount they can make. You can only have up to 2 heretic blades crafted at once (3 if you are Path of Flesh).
balance: The Lord of the Night has been buffed to be a little scarier. Did you know the Lord of the Night can eat arms to regain body parts and heal?
balance: Buffed some heretic summons - mostly their health pools.
balance: Nerfed the heretic's Mask of Madness. It can no longer infinite stam-crit you.
balance: Nerfed the heretic's ash mark.
balance: Nerfed a bunch of on-hit-heretic-blade effects. Many effects only apply on mark detonation now: Void blade silence, flesh blade wounds, ash blade gasp cooldown refund.
fix: Fixed quite a few bugs and unintended behaviors with heretic code.
refactor: Refactored and improved much of Heretic code. Improved the file structure dramatically.
admin: The heretic's traitor panel has been beefed up a bit.
/cl

---
## [pindograma/pesqEle](https://github.com/pindograma/pesqEle)@[223aa8e0ec...](https://github.com/pindograma/pesqEle/commit/223aa8e0ec03dcb78e351796d967356b49235796)
#### Wednesday 2022-03-23 02:50:07 by Daniel Ferreira

add 2022 functions for scraper

Add functions to parse the 2022 website. Honestly, given that the
previous years' functions simply don't work anymore (and are useless,
given the availability of the CSV files on the TSE's website), we should
probably just remove them.

Another problem is that the new TSE website only shows 10 results per
page, and dealing with pagination is a big pain. For now, we're able to
deal with it since there are only a couple polls available. But in the
future, we'll want to address that, or get a guarantee from the TSE that
the CSVs will be available, making this scraper unnecessary.

---
## [ThePrimeagen/tyrone-biggums](https://github.com/ThePrimeagen/tyrone-biggums)@[0db00ec750...](https://github.com/ThePrimeagen/tyrone-biggums/commit/0db00ec750be5f5e31a77b63e7d39287c5649a69)
#### Wednesday 2022-03-23 03:19:15 by mpaulson

feat: a completely worthless commit message fuck you haters

---
## [MetaMask/controllers](https://github.com/MetaMask/controllers)@[10be35a414...](https://github.com/MetaMask/controllers/commit/10be35a4142e777f94846106874d0674cdbf3a57)
#### Wednesday 2022-03-23 04:40:23 by Elliot Winkler

WIP: Use Polly to mock HTTP requests in tests

**tl;dr:** I've introduced [Polly][1] as a replacement for Nock as I
believe it will lead to more readable and authentic tests. A few things:

* This is a proof of concept – I've only added it to
  CollectiblesController to start out with.
* All I've done is replace Nock requests with Polly requests. Ideally,
  we wouldn't need to mock anything manually at all and let Polly do its
  thing. Unfortunately, some HTTP requests that we are mocking no longer
  work.
* In the future, we should investigate using Ganache instead of hitting
  mainnet and exposing our Infura project id in tests.

---

Currently there are a couple of problems with our tests as it relates to
network requests:

1. We do not prevent network requests from being made. There are
   some tests which use Nock to mock requests, but not all requests are
   being mocked, and we are unaware which ones are actually going
   through.
2. Nock, although a popular package, is rather cumbersome to use, and
   makes tests difficult to understand and follow.

To address these problems, this commit replaces Nock with Polly. Polly
is a package developed by Netflix that intercepts all HTTP requests and
automatically captures snapshots (recordings) of these requests as they
are being made. These recordings are then used in successive test runs.
You can also manually mock requests if you want more manual control.

## Why introduce another package? Why is Nock not sufficient?

There are a few problems with Nock that make it difficult to work with:

1. Mocks take up space in your test, so you will probably find yourself
   extending a collection of mocks you've assembled at the top of the
   file. Once you have enough, who knows which mocks serve which tests?
2. Once you've added a mock to your test, that mock stays forever. If
   the API changes in the future, or stops working altogether, you will
   never know until you remove that mock.
3. If you turn `nock.disableNetConnect()` on, and you haven't mocked a
   request, [it will throw a NetConnectNotAllowedError][2]. This works
   in most cases, but what happens if you have a `try`/`catch` block
   around the request you're making and you are swallowing the error?
   Then your test may fail for no apparent reason. And how do you know
   which request you need to mock? Nock has a way to peek behind the
   curtain and log the requests that are being made by running
   `DEBUG=nock.* yarn jest ...`, but this output is seriously difficult
   to read:

   ```
   2022-03-23T03:50:09.033Z nock.scope:api.opensea.io query matching skipped
   2022-03-23T03:50:09.033Z nock.scope:api.opensea.io matching https://api.opensea.io:443/api/v1/asset/0x495f947276749Ce646f68AC8c248420045cb7b5e/40815311521795738946686668571398122012172359753720345430028676522525371400193 to GET
   https://api.opensea.io:443/api/v1/asset_contract/0x2aEa4Add166EBf38b63d09a75dE1a7b94Aa24163: false
   2022-03-23T03:50:09.033Z nock.scope:api.opensea.io attempting match {"protocol":"https:","slashes":true,"auth":null,"host":"api.opensea.io:443","port":443,"hostname":"api.opensea.io","hash":null,"search":null,"query":null,"pathname":"/api/v1/asset/0x495f947276749Ce646f68AC8c248420045cb7b5e/40815311521795738946686668571398122012172359753720345430028676522525371400193","path":"/api/v1/asset/0x495f947276749Ce646f68AC8c248420045cb7b5e/40815311521795738946686668571398122012172359753720345430028676522525371400193","href":"https://api.opensea.io/api/v1/asset/0x495f947276749Ce646f68AC8c248420045cb7b5e/40815311521795738946686668571398122012172359753720345430028676522525371400193","method":"GET","headers":{"accept":["*/*"],"user-agent":["node-fetch/1.0 (+https://github.com/bitinn/node-fetch)"],"accept-encoding":["gzip,deflate"],"connection":["close"]},"proto":"https"}, body = ""
   ```

Polly removes all of these problems:

1. Because Polly records request snapshots, you don't usually have to
   worry about mocking requests manually. These recordings are kept in
   files which are categorized by the tests which made the requests.
2. Because Polly actually hits the API you're mocking, you can work with
   real data. You can instruct Polly to expire these recordings after a
   designated timeframe to guarantee that your code doesn't break if
   the API ceases to work in the way you expect.
3. Polly will also print a message when a request is made that it
   doesn't recognize without needing to run an extra command:

    ```
    Errored ➞ POST https://mainnet.infura.io/v3/ad3a368836ff4596becc3be8e2f137ac PollyError: [Polly] [adapter:node-http] Recording for the following request is not found and `recordIfMissing` is `false`.
        {
          "url": "https://mainnet.infura.io/v3/ad3a368836ff4596becc3be8e2f137ac",
          "method": "POST",
          "headers": {
            "content-type": "application/json",
            "connection": "keep-alive",
            "host": "mainnet.infura.io",
            "user-agent": "Mozilla/5.0 (Darwin x64) node.js/12.22.6 v8/7.8.279.23-node.56",
            "content-length": "201"
          },
          "body": "{\"jsonrpc\":\"2.0\",\"id\":30,\"method\":\"eth_call\",\"params\":[{\"to\":\"0x18E8E76aeB9E2d9FA2A2b88DD9CF3C8ED45c3660\",\"data\":\"0x0e89341c0000000000000000000000000000000000000000000000000000000000000024\"},\"latest\"]}",
          "recordingName": "CollectiblesController/updateCollectibleFavoriteStatus/should keep the favorite status as false after updating metadata",
          "id": "53192eab94ddedfb300b625b1cb79843",
    ...
    ```

## What about Nock Back? Doesn't this do the same thing?

It's true that Nock contains a feature to capture requests called [Nock
Back][3]. However, this is cumbersome, too:

1. You have to wrap your test in a `nockBack` call.
2. You have to name your recording files.
3. You have to call `nockDone()` in your test.

There is a package called `jest-nock-back` that fixes these issues and
makes using Nock Back very easy. However, it isn't maintained (last
release was 3 years ago) and there isn't a way to automatically expire
your recordings (which I believe is a key feature).

Some requests make irreversible changes to resources, such as
transferring a token from one account to another.

To handle these types of requests, Polly still lets you manually mock
requests just like Nock. We've configured Polly to not record a request
it doesn't recognize by default, so in this case you'll get a message
when running the test that makes such a request. From there you can make
a decision about how you'd like to mock this request — whether you want
Polly to record the request or whether you'd like to manually mock it.

That said, if the request in question involves a blockchain network,
instead of mocking the request, we might investigate whether it's
possible to use Ganache to perform the irreversible action rather than
actually hitting mainnet or some other network.

* Because Polly automatically creates request mocks and these mocks are
  no longer contained in tests, developers will need to be educated
  about Polly (Polly is not as popular as Nock) and remember that it
  exists whenever updating tests.
* If a recording is no longer needed or needs to be updated, the
  associated file holding the recorded information about the request
  needs to be deleted. Finding this file is not a great experience.
* Nock has virtually zero initialization code. Polly's initialization
  code is surprisingly complicated (although that is largely hidden, so
  no one should have to mess with it).

[1]: https://netflix.github.io/pollyjs/#/README
[2]: https://github.com/nock/nock#enabledisable-real-http-requests
[3]: https://github.com/nock/nock#nock-back

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[1ea49c7896...](https://github.com/treckstar/yolo-octo-hipster/commit/1ea49c78962ce87d9ee66cf8e2266e4300a1a8ee)
#### Wednesday 2022-03-23 05:00:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [michaelpq/postgres](https://github.com/michaelpq/postgres)@[ec62cb0aac...](https://github.com/michaelpq/postgres/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Wednesday 2022-03-23 05:33:17 by Tom Lane

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
## [svitalis123/alx-low_level_programming](https://github.com/svitalis123/alx-low_level_programming)@[0c6948a8af...](https://github.com/svitalis123/alx-low_level_programming/commit/0c6948a8af1c2842a6968fcc0e47787b73ba97fb)
#### Wednesday 2022-03-23 05:50:40 by svitalis123

strcat
strncat
strncpy
strcmp
I am a kind of paranoid in reverse. I suspect people of plotting to make me happy
Always look up
Expect the best. Prepare for the worst. Capitalize on what comes
Mozart composed his music not for the elite, but for everybody
rot13
Numbers have life; they're not just symbols on paper
A dream doesn't become reality through magic; it takes sweat, determination and hard work
It is the addition of strangeness to beauty that constitutes the romantic character in art
Noise is a buffer, more effective than cubicles or booth walls

---
## [sunamo/sunamo](https://github.com/sunamo/sunamo)@[a7dad265de...](https://github.com/sunamo/sunamo/commit/a7dad265de6fe7a628668a8d23a296d6a3666f4a)
#### Wednesday 2022-03-23 06:43:23 by Radek Jancik

I share the belief of many of my contemporaries that the spiritual crisis pervading all spheres of Western industrial society can be remedied only by a change in our world view. We shall have to shift from the materialistic, dualistic belief that people and their environment are separate, toward a new consciousness of an all reality, which embraces the experiencing ego, a reality in which people feel their oneness with animate nature and all of creation. - Hofmann, Dr. Albert

---
## [robin0336/Liubin](https://github.com/robin0336/Liubin)@[d1eb993f78...](https://github.com/robin0336/Liubin/commit/d1eb993f78bcdb09b0aa0fbbfafad900087b49b5)
#### Wednesday 2022-03-23 08:22:31 by robin0336

Create README.md

Database of ECGs and CAGs
Introduction
Background: Electrical storm (ES) is a heterogeneous clinical emergency that can present with malignant ventricular arrhythmias such as ventricular fibrillation (VF),
ventricular tachycardia (VT), requiring the need for cardiac defibrillation. ES is a life-threatening condition with a high mortality rate. Successfully managing ES
in the setting of acute myocardial infarction（MI）is expected to be known by physicians on call to reduce in-hospital mortality.

Case presentation: A 57-year-old man presenting with acute onset chest pain was found to have an infero-posterior ST-segment elevation myocardial infarction (STEMI) 
complicated by acute right ventricular MI secondary to total occlusion of the proximal right coronary artery (RCA). The patient developed ES in the form of recurrent
VF that was managed successfully with electrical defibrillation, antiarrhythmic therapy with amiodarone and esmolol, endotracheal intubation, sedation, electrolyte 
replacement, volume resuscitation, comfort care, psychological intervention, and percutaneous coronary intervention (PCI) of the occluded epicardial artery. With 
these interventions used in quick succession and with the aspiration of a massive RCA thrombus, the patient was reversed to hemodynamic stability, did not have 
further episodes of VF, and survived the index hospitalization.

Conclusion: ES is a rare but fatal complication of acute MI. Residents on night shifts should be better prepared and equipped to deal with this rare condition. We 
hope our successful experience can benefit physicians on call who take care of acute MI patients that deteriorate with ES.
Data Sharing
This is the data repository of the case report sharing the ECGs and CAGs. Browse and download the data by clicking the folder links above.

---
## [WordPress/gutenberg](https://github.com/WordPress/gutenberg)@[3ea2d42b0a...](https://github.com/WordPress/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Wednesday 2022-03-23 09:05:28 by Dennis Snell

Blocks: Remember raw source block for invalid blocks. (#38923)

Part of #38922

When the editor is unable to validate a block it should preserve the
broken content in the post and show an accurate representation of that
underlying markup in the absence of being able to interact with it.

Currently when showing a preview of an invalid block in the editor we
attempt to re-generate the save output for a block given the attributes
we originally parsed. This is a flawed approach, however, because by
the nature of being invalid we know that there is a problem with those
attributes as they are.

In this patch we're introducing the `__unstableBlockSource` attribute on 
a block which only exists for invalid blocks at the time of this patch. That 
`__unstableBlockSource` carries the original un-processed data for a block
node and can be used to reconstruct the original markup without using
garbage data and without inadvertently changing it through the series
of autofixes, deprecations, and the like that happen during normal block loading.

The noticable change is in `block-list/block` where we will be showing
that reconstruction rather than the re-generated block content. Previously
it was the case that the preview might represent a corrupted version of the
block or show the block as if emptied of all its content. Now, however,
the preview sould accurately reflect the HTML in the source post even
when it's invalid or unrecognized according to the editor.

Further work should take advantage of the `__unstableBlockSource`
property to provide a more consistent and trusting experience for
working with unrecognized content.

---
## [atriwidada/Top10](https://github.com/atriwidada/Top10)@[7400eb7a80...](https://github.com/atriwidada/Top10/commit/7400eb7a8068179812f6ef96ee67bb492bed15e4)
#### Wednesday 2022-03-23 09:28:25 by Henry Hu

Create index.zh-tw.md

# OWASP Top 10 2021 介紹

歡迎來到最新版本的 OWASP Top 10! OWASP Top 10 2021 最新版本不只是設計
上不同，我們也提供了一頁式的圖形化說明讓你可以印出來，你可以從我們的網頁
上面直接下載。
Welcome to the latest installment of the OWASP Top 10! The OWASP Top 10
2021 is all-new, with a new graphic design and an available one-page
infographic you can print or obtain from our home page.

A huge thank you to everyone that contributed their time and data for
this iteration. Without you, this installment would not happen. **THANK
YOU**.

## What's changed in the Top 10 for 2021

There are three new categories, four categories with naming and scoping
changes, and some consolidation in the Top 10 for 2021.

<img src="./assets/image1.png" style="width:6.5in;height:1.78889in" alt="Mapping of the relationship between the Top 10 2017 and the new Top 10 2021" />

**A01:2021-Broken Access Control** moves up from the fifth position; 94%
of applications were tested for some form of broken access control. The
34 CWEs mapped to Broken Access Control had more occurrences in
applications than any other category.

**A02:2021-Cryptographic Failures** shifts up one position to #2,
previously known as *Sensitive Data Exposure,* which was broad symptom
rather than a root cause. The renewed focus here is on failures related
to cryptography which often leads to sensitive data exposure or system
compromise.

**A03:2021-Injection** slides down to the third position. 94% of the
applications were tested for some form of injection, and the 33 CWEs
mapped into this category have the second most occurrences in
applications. Cross-site Scripting is now part of this category in this
edition.

**A04:2021-Insecure Design** is a new category for 2021, with a focus on
risks related to design flaws. If we genuinely want to "move left" as an
industry, it calls for more use of threat modeling, secure design
patterns and principles, and reference architectures.

**A05:2021-Security Misconfiguration** moves up from #6 in the previous
edition; 90% of applications were tested for some form of
misconfiguration. With more shifts into highly configurable software,
it's not surprising to see this category move up. The former category
for XML External Entities (XXE) is now part of this category.

**A06:2021-Vulnerable and Outdated Components** was previously titled
*Using Components with Known Vulnerabilities* and is #2 in the industry
survey, but also had enough data to make the Top 10 via data analysis.
This category moves up from #9 in 2017 and is a known issue that we
struggle to test and assess risk. It is the only category not to have
any CVEs mapped to the included CWEs, so a default exploit and impact
weights of 5.0 are factored into their scores.

**A07:2021-Identification and Authentication Failures** was previously
*Broken Authentication* and is sliding down from the second position,
and now includes CWEs that are more related to identification failures.
This category is still an integral part of the Top 10, but the increased
availability of standardized frameworks seems to be helping.

**A08:2021-Software and Data Integrity Failures** is a new category for
2021, focusing on making assumptions related to software updates,
critical data, and CI/CD pipelines without verifying integrity. One of
the highest weighted impacts from CVE/CVSS data mapped to the 10 CWEs in
this category. Insecure Deserialization from 2017 is now a part of this
larger category.

**A09:2021-Security Logging and Monitoring Failures** was previously
*Insufficient Logging &* Monitoring and is added from the industry
survey (#3), moving up from #10 previously. This category is expanded to
include more types of failures, is challenging to test for, and isn't
well represented in the CVE/CVSS data. However, failures in this
category can directly impact visibility, incident alerting, and
forensics.

**A10:2021-Server-Side Request Forgery** is added from the industry
survey (#1). The data shows a relatively low incidence rate with above
average testing coverage, along with above-average ratings for Exploit
and Impact potential. This category represents the scenario where the
industry professionals are telling us this is important, even though
it's not illustrated in the data at this time.

## Methodology

This installment of the Top 10 is more data-driven than ever but not
blindly data-driven. We selected eight of the ten categories from
contributed data and two categories from an industry survey at a high
level. We do this for a fundamental reason, looking at the contributed
data is looking into the past. AppSec researchers take time to find new
vulnerabilities and new ways to test for them. It takes time to
integrate these tests into tools and processes. By the time we can
reliably test a weakness at scale, years have likely passed. To balance
that view, we use an industry survey to ask people on the front lines
what they see as essential weaknesses that the data may not show yet.

There are a few critical changes that we adopted to continue to mature
the Top 10.

### How the categories are structured

A few categories have changed from the previous installment of the OWASP
Top Ten. Here is a high-level summary of the category changes.

Previous data collection efforts were focused on a prescribed subset of
approximately 30 CWEs with a field asking for additional findings. We
learned that organizations would primarily focus on just those 30 CWEs
and rarely add additional CWEs that they saw. In this iteration, we
opened it up and just asked for data, with no restriction on CWEs. We
asked for the number of applications tested for a given year (starting
in 2017), and the number of applications with at least one instance of a
CWE found in testing. This format allows us to track how prevalent each
CWE is within the population of applications. We ignore frequency for
our purposes; while it may be necessary for other situations, it only
hides the actual prevalence in the application population. Whether an
application has four instances of a CWE or 4,000 instances is not part
of the calculation for the Top 10. We went from approximately 30 CWEs to
almost 400 CWEs to analyze in the dataset. We plan to do additional data
analysis as a supplement in the future. This significant increase in the
number of CWEs necessitates changes to how the categories are
structured.

We spent several months grouping and categorizing CWEs and could have
continued for additional months. We had to stop at some point. There are
both *root cause* and *symptom* types of CWEs, where *root cause* types
are like "Cryptographic Failure" and "Misconfiguration" contrasted to
*symptom* types like "Sensitive Data Exposure" and "Denial of Service."
We decided to focus on the root cause whenever possible as it's more
logical for providing identification and remediation guidance. Focusing
on the root cause over the symptom isn't a new concept; the Top Ten has
been a mix of *symptom* and *root cause*. CWEs are also a mix of
*symptom* and *root cause*; we are simply being more deliberate about it
and calling it out. There is an average of 19.6 CWEs per category in
this installment, with the lower bounds at 1 CWE for
*A10:2021-Server-Side Request Forgery (SSRF)* to 40 CWEs in
*A04:2021-Insecure Design*. This updated category structure offers
additional training benefits as companies can focus on CWEs that make
sense for a language/framework.

### How the data is used for selecting categories

In 2017, we selected categories by incidence rate to determine
likelihood, then ranked them by team discussion based on decades of
experience for Exploitability, Detectability (also likelihood), and
Technical Impact. For 2021, we want to use data for Exploitability and
Impact if possible.

We downloaded OWASP Dependency Check and extracted the CVSS Exploit, and
Impact scores grouped by related CWEs. It took a fair bit of research
and effort as all the CVEs have CVSSv2 scores, but there are flaws in
CVSSv2 that CVSSv3 should address. After a certain point in time, all
CVEs are assigned a CVSSv3 score as well. Additionally, the scoring
ranges and formulas were updated between CVSSv2 and CVSSv3.

In CVSSv2, both Exploit and Impact could be up to 10.0, but the formula
would knock them down to 60% for Exploit and 40% for Impact. In CVSSv3,
the theoretical max was limited to 6.0 for Exploit and 4.0 for Impact.
With the weighting considered, the Impact scoring shifted higher, almost
a point and a half on average in CVSSv3, and exploitability moved nearly
half a point lower on average.

There are 125k records of a CVE mapped to a CWE in the NVD data
extracted from OWASP Dependency Check, and there are 241 unique CWEs
mapped to a CVE. 62k CWE maps have a CVSSv3 score, which is
approximately half of the population in the data set.

For the Top Ten, we calculated average exploit and impact scores in the
following manner. We grouped all the CVEs with CVSS scores by CWE and
weighted both exploit and impact scored by the percentage of the
population that had CVSSv3 + the remaining population of CVSSv2 scores
to get an overall average. We mapped these averages to the CWEs in the
dataset to use as Exploit and Impact scoring for the other half of the
risk equation.

## Why not just pure statistical data?

The results in the data are primarily limited to what we can test for in
an automated fashion. Talk to a seasoned AppSec professional, and they
will tell you about stuff they find and trends they see that aren't yet
in the data. It takes time for people to develop testing methodologies
for certain vulnerability types and then more time for those tests to be
automated and run against a large population of applications. Everything
we find is looking back in the past and might be missing trends from the
last year, which are not present in the data.

Therefore, we only pick eight of ten categories from the data because
it's incomplete. The other two categories are from the industry survey.
It allows the practitioners on the front lines to vote for what they see
as the highest risks that might not be in the data (and may never be
expressed in data).

## Why incidence rate instead of frequency?

There are three primary sources of data. We identify them as
Human-assisted Tooling (HaT), Tool-assisted Human (TaH), and raw
Tooling.

Tooling and HaT are high-frequency finding generators. Tools will look
for specific vulnerabilities and tirelessly attempt to find every
instance of that vulnerability and will generate high finding counts for
some vulnerability types. Look at Cross-Site Scripting, which is
typically one of two flavors: it's either a more minor, isolated mistake
or a systemic issue. When it's a systemic issue, the finding counts can
be in the thousands for an application. This high frequency drowns out
most other vulnerabilities found in reports or data.

TaH, on the other hand, will find a broader range of vulnerability types
but at a much lower frequency due to time constraints. When humans test
an application and see something like Cross-Site Scripting, they will
typically find three or four instances and stop. They can determine a
systemic finding and write it up with a recommendation to fix on an
application-wide scale. There is no need (or time) to find every
instance.

Suppose we take these two distinct data sets and try to merge them on
frequency. In that case, the Tooling and HaT data will drown the more
accurate (but broad) TaH data and is a good part of why something like
Cross-Site Scripting has been so highly ranked in many lists when the
impact is generally low to moderate. It's because of the sheer volume of
findings. (Cross-Site Scripting is also reasonably easy to test for, so
there are many more tests for it as well).

In 2017, we introduced using incidence rate instead to take a fresh look
at the data and cleanly merge Tooling and HaT data with TaH data. The
incidence rate asks what percentage of the application population had at
least one instance of a vulnerability type. We don't care if it was
one-off or systemic. That's irrelevant for our purposes; we just need to
know how many applications had at least one instance, which helps
provide a clearer view of the testing is findings across multiple
testing types without drowning the data in high-frequency results.

## What is your data collection and analysis process?

We formalized the OWASP Top 10 data collection process at the Open
Security Summit in 2017. OWASP Top 10 leaders and the community spent
two days working out formalizing a transparent data collection process.
The 2021 edition is the second time we have used this methodology.

We publish a call for data through social media channels available to
us, both project and OWASP. On the [OWASP Project
page](https://owasp.org/www-project-top-ten/#div-data_2020), we list the
data elements and structure we are looking for and how to submit them.
In the [GitHub
project](https://github.com/OWASP/Top10/tree/master/2020/Data), we have
example files that serve as templates. We work with organizations as
needed to help figure out the structure and mapping to CWEs.

We get data from organizations that are testing vendors by trade, bug
bounty vendors, and organizations that contribute internal testing data.
Once we have the data, we load it together and run a fundamental
analysis of what CWEs map to risk categories. There is overlap between
some CWEs, and others are very closely related (ex. Cryptographic
vulnerabilities). Any decisions related to the raw data submitted are
documented and published to be open and transparent with how we
normalized the data.

We look at the eight categories with the highest incidence rates for
inclusion in the Top 10. We also look at the industry survey results to
see which ones may already be present in the data. The top two votes
that aren't already present in the data will be selected for the other
two places in the Top 10. Once all ten were selected, we applied
generalized factors for exploitability and impact; to help rank the Top
10 in order.

## Data Factors

There are data factors that are listed for each of the Top 10
Categories, here is what they mean:

-   *CWEs Mapped*: The number of CWEs mapped to a category by the Top 10
    team.

-   *Incidence Rate*: Incidence rate is the percentage of applications
    vulnerable to that CWE from the population tested by that org for
    that year.

-   (Testing) *Coverage*: The percentage of applications tested by all
    organizations for a given CWE.

-   *Weighted Exploit*: The Exploit sub-score from CVSSv2 and CVSSv3
    scores assigned to CVEs mapped to CWEs, normalized, and placed on a
    10pt scale.

-   *Weighted Impact*: The Impact sub-score from CVSSv2 and CVSSv3
    scores assigned to CVEs mapped to CWEs, normalized, and placed on a
    10pt scale.

-   *Total Occurrences*: Total number of applications found to have the
    CWEs mapped to a category.

-   *Total CVEs*: Total number of CVEs in the NVD DB that were mapped to
    the CWEs mapped to a category.

## Category Relationships from 2017

There has been a lot of talk about the overlap between the Top Ten
risks. By the definition of each (list of CWEs included), there really
isn't any overlap. However, conceptually, there can be overlap or
interactions based on the higher-level naming. Venn diagrams are many
times used to show overlap like this.

<img src="./assets/image2.png" style="width:4.31736in;height:3.71339in" alt="Diagram Description automatically generated" />

The Venn diagram above represents the interactions between the Top Ten
2017 risk categories. While doing so, a couple of essential points
became obvious:

1.  One could argue that Cross-Site Scripting ultimately belongs within
    Injection as it's essentially Content Injection. Looking at the 2021
    data, it became even more evident that XSS needed to move into
    Injection.

2.  The overlap is only in one direction. We will often classify a
    vulnerability by the end manifestation or "symptom," not the
    (potentially deep) root cause. For instance, "Sensitive Data
    Exposure" may have been the result of a "Security Misconfiguration";
    however, you won't see it in the other direction. As a result,
    arrows are drawn in the interaction zones to indicate which
    direction it occurs.

3.  Sometimes these diagrams are drawn with everything in *A06:2021
    Using Components with Known Vulnerabilities*. While some of these
    risk categories may be the root cause of third-party
    vulnerabilities, they are generally managed differently and with
    different responsibilities. The other types are typically
    representing first-party risks.

# Thank you to our data contributors

The following organizations (along with some anonymous donors) kindly
donated data for over 500,000 applications to make this the largest and
most comprehensive application security data set. Without you, this
would not be possible.

| | | | |
| :---: | :---: | :---: | :---: |
| AppSec Labs | GitLab | Micro Focus | Sqreen |
| Cobalt.io | HackerOne | PenTest-Tools | Veracode |
| Contrast Security | HCL Technologies | Probely | WhiteHat (NTT) |

---
## [abhishek1994-ux/-MyCloudDiary](https://github.com/abhishek1994-ux/-MyCloudDiary)@[27761892d9...](https://github.com/abhishek1994-ux/-MyCloudDiary/commit/27761892d931f10e8d0598a6914381361b38163d)
#### Wednesday 2022-03-23 09:34:18 by Abhishek Shrivastava

What is Microsoft Azure? 

**Executive summary**
Microsoft Azure is Microsoft's comprehensive collection of cloud-based alternatives to physical hardware and services. Azure virtual machines run all of Microsoft's server products as well as a wide range of third-party products including Linux distributions and third-party software; the Azure product line also includes a comprehensive collection of more than 200 services that developers can use to build cloud-based apps. This guide offers an executive-level overview of Microsoft Azure services, including product offerings and prices.

**What is Microsoft Azure?**
Microsoft Azure is a broad, ever-expanding set of cloud-based computing services that are available to businesses, developers, government agencies, and anyone who wants to build an app or run an enterprise on the internet without having to install and manage hardware or server software. It has been the fastest-growing business segment for Microsoft in recent years and in recent years has surpassed both Windows and Office in terms of revenue.

Cynics love to dismiss the entire concept of cloud computing with a scoff: "The cloud is just someone else's computer." But that oversimplification describes only one small part of the Azure business: Infrastructure as a Service (IaaS), in which cloud-based services replace physical hardware.

The full range of Microsoft Azure services covers much more ground than simply relocating on-premises servers to the cloud. In addition to IaaS resources, you have a full range of Platform as a Service (PaaS) and Software as a Service (SaaS) options, giving your organization access to cloud-based services without the necessity of managing a server. For example, you can stand up a website based on WordPress or build a basic Node JS site without having to configure (or patch) the underlying Windows or Linux server.

In addition, developers of apps and web-based sites and services can use Azure storage and services as building blocks, without having to worry about the security or reliability of the underlying infrastructure.

Microsoft announced Azure in 2008. Two years later, in January 2010, Windows Azure debuted to the public. Microsoft rebranded its cloud platform as Microsoft Azure in 2014. The name change wasn't just cosmetic but was instead an acknowledgment that the scope of Azure cloud services had gone far beyond just Windows-based offerings. By late 2017, in fact, Microsoft reported that 40% of all virtual machines in Azure were running Linux, up from less than one-third just a year earlier.

The Azure Global Infrastructure includes data centers in 60 datacenter regions, spanning 140 countries. Microsoft also maintains two Azure Government Secret regions that are in undisclosed locations.

Also: Microsoft says 40 percent of all VMs in Azure now are running Linux

**MUST READ**
What is cloud computing? Everything you need to know from public and private cloud to software as a service
What is cloud computing? Everything you need to know from public and private cloud to software as a service

An introduction to cloud computing from IaaS and PaaS to hybrid, public and private cloud.

**Read More**
**
What are the benefits of Microsoft Azure?**
The most obvious benefit of Azure's IaaS offerings is that your organization doesn't have to buy, configure, maintain, and repair hardware to run cloud-based workloads. Savings start with the cost of the hardware but encompass a far greater number of indirect costs, including the physical space required to house those servers as well as the electricity to keep them running.

Because Azure-based resources are virtual, they're not vulnerable to unexpected hardware failures that can result in downtime while you wait for repairs or a replacement. Virtual hardware resources can scale up or down in a way that physical hardware can't, making it possible to deal with sudden surges in traffic to an Azure-based website. Large organizations that have to meet global privacy requirements for data storage and transfer can easily move data and services to a region of their choosing.

For developers, Azure offers instant access to services for developing mobile apps, designing IoT devices, connecting to online storage and database resources, and deploying container technology. In addition, Microsoft has invested heavily in machine learning and AI tools for developers.

What is Azure infrastructure as a service?
One of the most basic Azure IaaS usage scenarios is replacing a physical server with a virtual server running in Azure's datacenter, thus eliminating the need to maintain hardware.

**Also: Walmart bets on Microsoft Azure**

That server can run any supported desktop or server version of Windows, up to and including Windows Server 2022. Or you can choose from a long list of Linux distros, also in a wide range of supported versions, including Ubuntu Server, Red Hat Enterprise Linux, CentOS, and even Oracle Linux. In the enormous Azure Marketplace, you can find ready-run virtual servers for just about any task, including SQL Server, Docker, SAP Hana, and even (to go with that Oracle Linux server) Oracle Database.

You could, in fact, build an entire virtual desktop infrastructure (VDI) in Azure's cloud and manage it all with third-party tools. You can sign up for Citrix Virtual Desktops Essentials directly from the Azure Portal, for example, enabling a traditional VDI option from a service provider already well known in corporate circles. For a completely different approach, look at Nerdio for Microsoft Azure, which allows managed service providers to create an entire business network and manage it from a third-party web portal, which the company bills as "IT as a service."

Microsoft's own Azure-based VDI service is called Azure Virtual Desktop. It supports Windows 10 and Windows 11 in multi-user configurations available on any device, replacing on-premises server-based virtualization. It's also available running Windows 7 virtual desktops, with an irresistible perk for enterprises that are struggling with Windows 10 migration plans: three years of free extended security updates, extending from the official Windows 7 end of support on January 14, 2020. A hybrid Windows desktop service called Windows 365 is also available.

**MUST READ**
Windows Virtual Desktop service on Azure TechRepublic
Three smart cloud services that can help keep your business more secure
Windows 365: Hands on with Microsoft's pricey new Cloud PC subscriptions
A cloud-based computing infrastructure is capable of tricks you can't easily accomplish in your own server room, including built-in load balancing and on-the-fly hardware upgrades at the flip of a virtual switch. It also includes some impressive security features such as just-in-time VM access, which locks down VMs at the network level, blocking inbound traffic except when specific requests for access are approved.

Also: SaaS, PaaS, and IaaS: Understand the differences

**What services compete with Azure?**
Azure is a clear second among cloud providers -- well behind Amazon Web Services, but well ahead of any other competition. Among the other competitors, Google Cloud Platform offers a similar set of cloud-based infrastructure and app services using the search giant's global infrastructure. Other companies, including Salesforce and Oracle, offer a subset of cloud-based services that are aimed primarily at those firms' existing customers.

**What else can you do on Azure?**
We could probably write an entire book covering the full range of services available on Azure, and it would be out of date the next day, because that universe is continually expanding. Here's a broad summary of other services available, organized by category.
**
STORAGE AND DATABASES**
Storing huge amounts of data, structured or unstructured, is what Azure was built for. The native Azure Storage services include: Azure Blobs (for unstructured data, including serving images, documents, and video streams directly to a browser); Azure Files, which are cloud-based file shares accessible using Standard Message Block (SMB) protocols; Azure Queues, for messaging between application components; and Azure Tables, a NoSQL store for structured data.

For migrating databases built on SQL Server, there's Azure SQL Database, a fully managed service that can be used as Managed Instances to migrate on-premises workloads or deployed from scratch to supply SQL database as a service.

And then there's Azure Cosmos DB, Microsoft's really big bet on big data. Microsoft calls it a "fully managed, globally-distributed, horizontally scalable in storage and throughput, multi-model database service backed up by comprehensive SLAs [service level agreements]."

**MUST READ**
Inside Microsoft's Cosmos DB
Azure Cosmos DB gets cheaper, Azure Machine Learning gets smarter
Microsoft Ignite postmortem: The underlying hybrid convergence
APP DEVELOPMENT TOOLS AND SERVICES
Developers of desktop and mobile apps have a full set of tools for building and deploying those apps, starting with the Visual Studio development environment, which is available in multiple versions (including preview releases) on Windows Server and Windows 10 Enterprise N virtual machines.

In addition to offering Visual Studio Team Services and Azure DevOps, Azure includes a broad selection of third-party devops tools for sharing code, managing workflows, deploying software, and monitoring performance and usage. You can use Jenkins, for example, to build apps in the cloud and deploy them directly to Azure. Use Terraform or Ansible to provision and configure infrastructure, and then manage it all with Chef Automate.

**MUST READ**
Microsoft rebrands, repositions Visual Studio Team Services as Azure DevOps
What is DevOps? An executive guide to agile development and IT operations
CONTAINERS AND CONTAINER SERVICES
Containers are standardized, encapsulated environments that run applications securely, with high availability and the capability to scale quickly. Azure's marketplace makes it particularly easy to deploy and scale container images. The standard for managing containerized workloads is the Kubernetes container orchestration service, which is available on Azure as Azure Kubernetes Service (AKS).

How important is containerization to the future of cloud-based workloads? As ZDNet's Scott Fulton has noted, "Microsoft has completely retooled its entire server system philosophy around Kubernetes, and hired several of its principal creators."

Azure offers well over 100 container images in its marketplace, along with tools from Docker and others for managing those images.

**MUST READ**
Five business benefits of containers
What Kubernetes really is, and how orchestration redefines the data center
MACHINE LEARNING
Among the most recent additions to Azure are a set of tools for performing predictive analytics and identifying useful algorithms. The Azure Machine Learning service makes it possible to build, train, and deploy machine learning in hybrid environments or directly in the cloud, using the same frameworks and tools you use on-premises.

**MICROSOFT**
An employee quit. Then Microsoft completely broke the rules
The best Windows laptops
Cloud computing: Azure ups the pressure on AWS
Surface Laptop Studio review: A true convertible, with designer appeal
How do you manage Azure services?
The primary interface for managing Azure subscriptions and resources is the Microsoft Azure Portal. That destination includes a customizable dashboard that offers at-a-glance information about running services, as well as a point-and-click interface for adding, configuring, and deploying new Azure resources.

From the Azure Portal, you can deploy, manage, and monitor resources in groups, using the Azure Resource Manager. For repetitive tasks, you can use Azure PowerShell and the Azure Command Line Interface (Azure CLI).

Using a custom dashboard, you can monitor the operation and performance of Azure-based applications and infrastructure, including the ability to query and analyze logs. To avoid surprises, you can set up alerts to receive notifications of critical conditions and assign automated actions based on user-defined triggers.

The Azure Security Center provides a numeric score that analyzes how well your cloud-based resources stack up against security best practices. Based on that score, the AI-based service provides recommendations to help remediate vulnerabilities and harden those resources against threats.

Finally, a separate Cost Management center allows you to analyze usage-based costs, configure alerts to avoid unpleasant budget surprises, and review recommendations for reducing waste.

**What is Azure Active Directory?**
Even if you've never opened the Microsoft Azure Portal or worked directly with any Azure services, there's a strong possibility that your organization already has a presence in Azure Active Directory (Azure AD).

Microsoft's cloud services are interconnected at fundamental levels, a fact that simplifies administration and license management. If you have a Microsoft 365 (formerly Office 365) Business or Enterprise subscription, for example, all of your user management goes through Azure AD. The same is true of Dynamics CRM and Microsoft Intune. You can manage users and associated devices through the Azure AD portal.

Those basic accounts are free. Additional features are available in Premium P1 and Premium P2 tiers, for an additional per-user fee of $6 and $9 per month, respectively.

**What does Microsoft Azure cost?**
Most Azure services are billed on a pay-as-you-go model, with no upfront costs. You can receive a discount on Azure services by purchasing one-year or three-year reservations that substantially reduce costs. The Azure Portal provides cost estimates when you add a new resource; you can also use the Azure Pricing Calculator to quickly estimate costs for a new resource on a pay-as-you-go or reserved-instance basis.

Most Visual Studio subscriptions provide free monthly Azure credit as a benefit; the exact amount depends on the subscription level. Likewise, anyone who's a BizSpark or Microsoft Partner Network member receives a monthly allotment of Azure credits, as well.

And if you just want to try your hand at Azure services, you can sign up for a free account that includes $200 worth of credit for the first month as well as access to a handful of popular services that are free for the first year.

---
## [JuliaLang/julia](https://github.com/JuliaLang/julia)@[62e0729dbc...](https://github.com/JuliaLang/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Wednesday 2022-03-23 10:14:32 by Mirek Kratochvil

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

---
## [jmark99/error-prone](https://github.com/jmark99/error-prone)@[fa6b82c77d...](https://github.com/jmark99/error-prone/commit/fa6b82c77deb00cdf7b34561232f116c7bbdf8b4)
#### Wednesday 2022-03-23 13:16:55 by ghm

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
## [TiviPlus/tgstation](https://github.com/TiviPlus/tgstation)@[759d24ab14...](https://github.com/TiviPlus/tgstation/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Wednesday 2022-03-23 13:20:04 by san7890

Four Corners, Red Rover: An Exploration in Decal Trends [MDB IGNORE] (#65290)

* Four Corners, Red Rover: An Exploration in Decaled Trends

You there! What exactly is wrong with this photograph?!

You don't need to tell me, I've boxed it out. There's four individual corners for the decalling. This is weird. You may be asking: Why don't they use the "full tile" turf decals? Let me demonstrate.

Look at the difference between the one at left and the one in the middle. The turf decal totally smothers the nice contrast lines afforded to use by the base turf, causing it to have smooth, clammy exterior. This is probably why no mapper ever uses the full turf decal, much to the chagrin of people who stare at how big the size of this repo is.

Now, what's that on the right? Why, it's the new sprite (and pathing I made) to help counter-act this issue! This perfectly lines up with the contrast lines of the base turf, allowing us to have a non-flattened visualization, while not having four fucking turf decals a turf load upon initialization. How epic!

I've also added "contrasted" variants of the "half" and "anticorner" turf decals for future use. I probably won't go through and update this in this PR, but the opportunity remains available.

I may or not map this change across all the maps. We shall see.

* neutral corners

we love vsc

* no wait

i forgot a bunch of potential edgecases so we'll have to go back. yellow should be fine but neutral, dark, blue, and green should get a second look over

* recheck

found some stuff, probably missed out on others. let us commence forth

* MISTAKE

nearly a fucko bwoingo

* final pass

it compiles and i've had enough, someone else can probably figure it out from this point onwards

* #65230 goated my timbs

now we wait for linters to fail

* YOU DIDN'T SAY THAT THE FIRST TIME

LINTERS AAFAFAFF

---
## [TiviPlus/tgstation](https://github.com/TiviPlus/tgstation)@[884c1eeb62...](https://github.com/TiviPlus/tgstation/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Wednesday 2022-03-23 13:20:04 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [influxdata/influxdb_iox](https://github.com/influxdata/influxdb_iox)@[55643945a1...](https://github.com/influxdata/influxdb_iox/commit/55643945a1a654d0db0bcc5eb0a42d7c3185efa9)
#### Wednesday 2022-03-23 13:56:33 by Marco Neumann

refactor: `querier` w/o `db` (#4063)

* feat: `TombstoneRepo::list_by_table`

* feat: `ParquetFileRepo::list_by_table_not_to_delete`

* refactor: `querier` w/o `db`

Get the `querier` to work w/o relying on `db`. A few notes:

- Testing is kinda shallow, we really need to get `query_tests` working
  w/ `querier` (see #3934).
- We still run a sync loop for namespaces, tables and schemas. This will
  be a replaced by "update namespace incl. tables and schemas on demand".
  Note however that we cannot fetch single tables and schemas on demand
  at the moment, because DataFusion doesn't implement async schema
  inspection (only `scan` / "give me all the chunks" is async). I think
  that's OK for now and we can address this later.
- There is NO cache for parquet files and tombstones at the moment. For
  correctness, they need to be fetched in a single transaction (or we
  need a kinda tricky sequence number / logical clock tracking) and I am
  not sure yet how this makes sense when we have the ingester data wired
  up and predicates pushed down to the catalog (see next point). So
  let's measure first and then decide on a caching strategy for this.
- Predicates are currently NOT pushed down to the catalog. I'll need to
  figure out how to extract time range from generic DataFusion
  expressions to make that work (it's easier for InfluxRPC queries, but
  they are not tested at the moment, see first point).

Sorry that this commit is kinda huge. I initially planned to only
migrate the chunks away from `db` and leave the tables and schemas for a
follow-up PR, but the DataFusion trait structure (chunks are bound to
their tables) makes this kinda pointless.

Closes #3974.

* docs: explain what we're doing

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

* docs: mention tracking issues

* docs: explain what we're doing

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

---
## [gsteel/laminas-view](https://github.com/gsteel/laminas-view)@[6e623ccabf...](https://github.com/gsteel/laminas-view/commit/6e623ccabfcd26999ce836990e5157125b58aede)
#### Wednesday 2022-03-23 14:15:26 by Michał Bundyra

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0aadc677a4...](https://github.com/treckstar/yolo-octo-hipster/commit/0aadc677a49a559f940cd0cbb9d689b96bd87c0a)
#### Wednesday 2022-03-23 15:00:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [save196/dwm](https://github.com/save196/dwm)@[67d76bdc68...](https://github.com/save196/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-03-23 16:04:24 by Chris Down

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
## [NOOBDY/c-homework](https://github.com/NOOBDY/c-homework)@[3bef5d61d8...](https://github.com/NOOBDY/c-homework/commit/3bef5d61d8e6aaa2ab64fb73839ec2271abc9a6f)
#### Wednesday 2022-03-23 17:38:01 by noobdy

13 jesus fucking christ this code is so god fucking awful please send help

---
## [spinnakerbot/gate](https://github.com/spinnakerbot/gate)@[e2a108db75...](https://github.com/spinnakerbot/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Wednesday 2022-03-23 18:39:15 by Chris Phillips

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
## [KrossX/pcsx2](https://github.com/KrossX/pcsx2)@[d6684efd26...](https://github.com/KrossX/pcsx2/commit/d6684efd262ef1c83d37c50b48edc478952dddf9)
#### Wednesday 2022-03-23 18:43:36 by RedDevilus

GameDB: GS HW Batch X

Relevant:
Bully
Colosseum - Road to Freedom
Dark Chronicle (Dark Cloud 2)
Killzone
God of War
Gun
Midnight Club 3
Mortal Kombat - Deadly Alliance
Need for Speed Carbon / Most Wanted / Undercover
Prince of Persia - Sand of Time / The Two Thrones / Warrior Within
Resident Evil 4 (BioHazard 4)
Thrillville / Off the Rails

---
## [kaolincash/khaos](https://github.com/kaolincash/khaos)@[99cf8411f4...](https://github.com/kaolincash/khaos/commit/99cf8411f4388bbae906610af8b0eb70d60f5114)
#### Wednesday 2022-03-23 19:52:44 by noted bones haver kaolin maia cash

iaso

iaso (named for the ancient Greek goddess of restoration, and all lowercase) is an Elden Ring Save File Backup & Restore tool which can be easily customised for a multitude of applications but, by default, keeps backups of your save files in case of errors.

Contents:
i. A Personal Note
ii. Tested Scenarios
iii. Usage Instructions
iv. How It Works 
v. How To Customise


i. A Personal Note (A.K.A. Don't be a cheater, cheater.)
Using iaso on your main save to restore lost runes and items is, in my opinion, contrary to the spirit of the game and constitutes cheating.
While I understand iaso can and probably will be used to make cheating more convenient, I feel the benefits outweigh the potential harm, given the undeniably shaky (see: understatement) PC release of Elden Ring.
I don't want my 300+ hours going down the drain due to the bugs that remain in the (otherwise reasonably playable, at this point) game, and I know you don't either.

p.s. you cannot restore saves to a new steam user id and the scope of the iaso project will never extend to that; she's purely a backup tool for a specified directory, geared toward adding a rudimentary quicksave feature to games where save files are particularly precious. I recommend also utilising this for other FromSoftware games by customising it as described below.




====================================================
ii. Tested Scenarios (like a few times to prove they worked, YMMV.)
Note: Fully Offline is the only intended usage of iaso. Does this break TOS? Probably. Do you care? Probably not.
I cannot account for all of FromSoftware's current or future shenanigan-detection tools, use at your own risk, don't call me if Miyazaki-san burns your house down with Flame of the Redmanes, you know the drill.
        - Fully Offline: Works as intended.
        - Logged into FromSoftware servers: Seems to work as expected. Cannot account for bans from prolonged use, idk, ymmv, etc.
        - Using Steam Cloud + Logged into FromSoftware servers: Will not work, as Steam will restore your save.




====================================================
iii. Usage Instructions (Part 1: What do I do with these files?)
FIRST OF ALL: DISABLE STEAM CLOUD OR THIS WILL NOT WORK
So how do I use this?
        You download the batch files provided and run them as necessary.
        You may need to fiddle with permissions/run as administrator, depending on your setup, but theoretically you can copy and paste the code into notepad, save it as "backup.bat" and so the same for "restore.bat" if you really wanted to.


Wait, I have to run these manually, every time?
        Not necessarily! In my case, I'm using Corsair iCUE to map F5 and F6 to backup and restore within the eldenring.exe program when it runs.


So I can just map the .bat files to F5 and F6 and save/restore my state every time I lose my runes?
        NO! DO NOT USE IASO FOR THAT PURPOSE, SUCH AN ACTION COULD PERMANENTLY RUIN YOUR SAVE FILE.

        This is not an undo-redo key that will teleport your character back in time, and if the restore tool is used while the game is running it could easily damage your save because I can't account for how eldenring.exe uses those files while they're loaded. Restoring with iaso while in the Main Menu *should* be fine, as the save files are not loaded, but I cannot account for what eldenring.exe might be doing behind the scenes and I haven't tested it extensively so, please let me know of any cases of this happening should you deign to risk it.

        Remember: iaso is a tool for backing up and restoring save files THAT ARE NOT IN USE for the EXPLICIT PURPOSE of PREVENTING loss of your entire save by the game crashing and rendering your only copy of the game's save file unusable. Do, however, keep in mind that it is ONLY the restore function that has any potential downside. Spam F5 to your heart's content.

        Seriously, though, don't abuse the restore function.


Wait- what? Isn't it extremely risky to restore the save files at all, then?
        Yes. Of course it is. IF and ONLY if the game is running and the files are in use. Similar to when the game generates stormy weather and crashes and threatens you for not closing it properly is a risk to the integrity of your save data, so, too, is overwriting live save files in a running game. 
        I also recognise that FromSoftware have, themselves, claimed that this specific issue has been addressed (regarding the save file corruptions, not the crashes..). 
        Just be patient whenever you want to restore a backup and close the game first.


Okay, I see your point, but I'm not sure the risk is justified nonetheless...
        That's entirely reasonable.


...try to convince me?
        If you insist, I will go into explicit detail of how iaso does her thing (it's actually very simple, if a little wordy by virtue of it being written by... me). For the benefit of any laypersons who struggle to parse code and want to know what's happening, though, I'll do my best to make it easy enough to follow.


Ok, thanks. Also, while I still have you here, I really hate that when you named it "iaso", you spelled it in all lowercase.
        It's actually "her".




====================================================
iii. Usage Instructions (Part 2: So... What Am I Even Using, Then?)
        The broad strokes of how the backup process works are as follows:
                1) iaso creates two backups.
                        1a) The first backup is your quicksave slot, and is called "EldenRingQuicksave"
                        1b) The second backup is an archive that stores every backup made with iaso unless you personally remove them
                 2) There is no number 2)


Ok so how is that dangerous?
        It's not, when you're restoring the files manually.
        The danger arises when you restore the files, which is what happens next.


There is a number 2)!
        There is a number 2) in that there is a second file to worry about, yes.
        The second program, restore.bat, indiscriminately overwrites everything within "EldenRing" (your actual real live save folder with every single save slot you have  inside it) with the contents of "EldenRingQuicksave" with no confirmation prompt for accidental executions. This is for the benefit of those, myself included, mapping this to a key like F6. 
        You see, I play with an Xbox controller, and my keyboard is physically disabled with a custom profile that makes all but the "switch profile" and "printscreen" keys functionless, to prevent accidental interactions. I even spliced a push button into my mouse's cable so that I can toggle it on the fly without unplugging it.
        I won't be pressing this thing by accident. 
        You, however, might. 
        Don't.


That's supposed to convince me?
        Think about it: I had to idiot-proof my own keyboard and mouse because I'm clumsy, not stupid, and I suspect you, also, are not stupid. This tool is idiot proof in that even if you fuck up your save, it by design has a separate archive of manually restorable backups. In fact, there is no way to auto-restore these, you *have* to do it manually if you're restoring anything other than the quicksave slot. iaso, when used as intended, should be completely safe to use. If your computer is struck by lightning halfway through a restoration, it might go weird, but you have an archive, including the exact quicksave you were just attempting to restore, which also exists within the quicksave slot until overwitten. Just don't be stupid, stupid.


Alright, I'm convinced. I feel like I should be a little offended by some of that, but I'm reasonably convinced that having two separate backups is probably overkill put in for the sole reason that you, yourself, are an idiot.
        Exactly! I'm glad you agree that I am an idiot.


Anything else?
        Read on if you want to learn in detail how this works, otherwise just use the files as directed above.
        While the game isn't running.
        Please.



====================================================
iv. How It Works (A.K.A. The Viewer Retention Drop-Off Point)
A very simple explanation of how it works, for the layperson who wants to customise this easily, here's the excerpt that does the backup itself:
Here we establish what the variable "slot" is, which we later append to the path we're interested in as its unique name.
A sensible way to generate a consistently unique name for each slot is to take the current time, which will never be the same twice.
This has the added benefit of allowing us to find the most recent save, or to restore to an older backup from a time we know was good!
        set slot=%year%-%month%-%day%@%hour%%minute%Hrs%second%s


Next, we establish our paths. In this case, it's Elden Ring, which doesn't have its own quicksave feature.
        set source=%APPDATA%\EldenRing
        set backup=%APPDATA%\EldenRingQuicksave
        set archive="%APPDATA%\EldenRingArchive\%slot% - TO MANUALLY RESTORE simply rename me 'EldenRing' and overwrite the current 'AppData-Roaming-EldenRing' folder."
We have three folders here:
        source = the actual place Elden Ring stores the save files for your game
        quicksave = the quicksave folder that will contain your most recent quicksave, ready to redeploy later
        archive = every quicksave that you've made, which could get large if you use this a lot. I haven't implemented an auto purge, so you will have to be cognisant of this.
All of these are stored within C:\Users\[Your Username]\AppData\Roaming.
Using the %APPDATA% shorthand (which, incidentally, also works in the Windows Explorer address bar, to get you there quicker if you want to go digging) we can avoid having to alter this for every single user as the [Your Username] is, of course, variable. Overall, this makes the path easier to type for me if I need to use it again, and easier to read, understand, and edit for the end user (that's you!) <3


Finally, we run the logic of the program!
All this does is copy the source directory we defined earlier into two places, in two slightly different ways:
Remember in the previous step, we defined the "archive" variable to have an appendix? This is where our "slot" variable from earlier comes back into play.
First, we robocopy source -> quicksave, which makes a copy of the "EldenRing" folder, which is of course in the ideal state already, and makes a 1:1 copy of it right next to it, named "EldenRingQuicksave". This cloned directory will be at C:\Users\[VARIABLE STRING]\AppData\Roaming, right alongside the original EldenRing directory.
Note: the /E option tells robocopy we want *everything* inside the source folder. This means we want its subdirectories, and not just the files inside the folder you asked for, as robocopy by default will only copy files and not directories.


        robocopy %source% %quicksave% /E


The next line, we robocopy source -> archive copies "EldenRing" to a second sister directory named "EldenRingArchive", but because we added the "\Elden Ring - %slot%" appendix, the \ tells robocopy to make a new directory inside EldenRingArchive named "Elden Ring - %slot%", which uses the variable from our very first step that we've already defined as the current time.


        robocopy %source% %archive% /E


        Which is the same as saying: 
                | robocopy |   +   | %APPDATA%\EldenRing |   +   | "%APPDATA%\EldenRingArchive\EldenRing - |   +   | %slot% |   +   | - TO MANUALLY RESTORE simply rename me 'EldenRing' and overwrite the current 'AppData-Roaming-EldenRing' folder." |   +   | /E /is /it |
                Which, itself, is the same as saying to your computer:
                       | Make a copy of |   +   | the folder called C:\Users\[Your Username]\AppData\Roaming\EldenRing and paste it at |   +   | C:\Users\YourUsername\AppData\Roaming\EldenRingArchive\EldenRing\ |   +   | [whatever the current date & time is in YYYY/MM/DD] |   +   | and include every subdirectory when you do it, overwriting them if they already exist, irrespective of their attributes |


The result of the second line of code is that we are left with an archive directory of timestamped directories which, themselves, are clones of "EldenRing", and can be restored manually by following the instructions provided in the name of the directory itself. Simple!


A lot to read, but simple.
And now we can begin to talk about how the restoration works. This is also simple, and requires much less explanation:

        robocopy %quicksave% %source%

It does the same as robocopy %source% %quicksave% from earlier. But in reverse. Simple.




====================================================
v. How to Customise (or How I Learned To Stop Worrying And Modify The Code)
Hopefully, you read how it all works above, so I shouldn't actually need to explain this if you've been able to infer it already.
Of course, I would personally have skipped to this section first upon seeing the customisation section in the contents and thinking "ooh!" because I'm a terrible groblin, and in case that's exactly what you've just done too (hi, I see you), then here's explicit instructions:


There are three variables you need to be concerned with:
        set source="Your source path, i.e. your Dark Souls or BloodBorne save locations (which I don't know offhand so you'll have to Google it, I'm not your mom)."
        set quicksave="Your backup location, which can be anywhere. This is where your quicksave slot will exist, and will be an exact copy of the path you specified in %source% in the line above this one."
        set archive="your archive location, which can also be anywhere. This is the reference library of all the quicksaves you've ever made, and you should keep it somewhere safe in case anything happens to your main save. Assuming all variables are correct, this one is easily your most important one. Keep it secret, keep it safe."


IMPORTANT TIP: If your path has spaces in it, you must enclose the entire path with quotes. For example, in the following example, only one of these will work:
                                    set source="%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED" will work (fine, I did look it up myself, get off my back)
                    however; set source=%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED will not work fine, because the space following "DARK" in "DARK SOULS" is parsed as the end of the path.


So, an example of this altered for Dark Souls (y'know what, fuck it, have this one on me, too) would be the following, for the entire batch file:
echo off
set year=%date:~6,4%
set month=%date:~3,2%
set day=%date:~0,2%
set hour=%time:~0,2%
if %hour% lss 10 (set hour=0%time:~1,1%)
set minute=%time:~3,2%
set second=%time:~6,5%
set slot=%year%-%month%-%day%@%hour%%minute%Hrs%second%s

set source="%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED"
set quicksave="%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED QUICKSAVE"
set archive="%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED ARCHIVE\%slot% - To manually restore, simply rename me 'DARK SOULS REMASTERED' and overwrite the current '%USERPROFILE%-Documents-FromSoftware-DARK SOULS REMASTERED' folder."

robocopy %source% %quicksave% /E /is /it
robocopy %source% %archive% /E /is /it


and the restore.bat, which you should save as a separate file:
echo off
robocopy "%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED QUICKSAVE" "%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED" /E /is /it


Now don't say I never did anything for you, kid.
- maia

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ed54bcec65...](https://github.com/mrakgr/The-Spiral-Language/commit/ed54bcec65ce2c9d47ea2b8c21b7c0e335b58dda)
#### Wednesday 2022-03-23 20:30:12 by Marko Grdinić

"11:15am. I am losing both sleep and bath time to read Otome Survival, but I would not have it any other way. I read one of the author's previous works and it was good, but I was put off by the descriptions for some of his other stuff. It seems that was a mistake.

11:20am. Let me skip the morning session. I've almost caught up with Otome Survival and I am going to exercise discipline and leave the chapters for later. Let me chill a bit, have breakfast, do the chores and then I will go back to studying.

1:10pm. Done with breakfast and chores. I've also caught up with Otome Survival. With this maybe I'll be able to go to bed earlier today.

Let me clear those thoughts away. Any mail, any replies? No. Well, I do not need it, I'll just bake the scratches as planned.

https://forum.isotropix.com/viewtopic.php?f=5&t=6948
Random Shader/Texture On multiple objects

This is something I'll have to study in the future, but not now. What I'll start things off is by looking up AOVs.

///

There are 2 types of AOVs in Clarisse:

* Built-in AOVs which are automatically declared by the renderer, materials or subpixel filters such as the Cryptomatte.
* Custom AOVs that are AOVs created by the user using AOV Store or Light Path Expressions. The AOV Store node allows you to output the result of a texture network at the material level or at the 3D Layer. The Light Path Expression node on the other hand allows you to extract rendering information directly from the path tracer.

///

So the built ins are declared by the renderer.

1:25pm. Ok, that is about it for AOVs. There is a huge number of them and I do not know what any of them do, but that does not matter for me. I'll leave the compositing stuff for much later if ever.

Let me open the UV baking project.

1:40pm. Had to take a short break. Right now I am trying to figure out...ah.

1:55pm. Ok, I understand the blue scratches completely. It is not doing UV baking like I expected. Rather, it spreads out the scratches and uses an orthographic camera to make the render.

If you have a curve, then depending on the rotation it can be straight or slanted. This is a good way to get variation.

...And since the camera is orthographic, that is an easy way to get a tileable texture since it will loop natural on any side. I see.

Let me check out the other materials.

2:20pm. I am studying the blue metal. It has a proceduraly generated texture which I've just internalized. It seems that I've neglected the difference bwteen the dot and scale pattern and this gave me some insight into the celular noise. Let me dive deeper into the blue metal material.

2:40pm. An informative project. It seems it is possible to import an image in an material.

Clarisse is very crash prone.

2:45pm. Just where do the diffuse_front_k and reflection_k variables comes from. They aren't custom made in the image buffer. And they are grayed out despite being on the right side in the AOV editor.

3:05pm. Yeah, the baked material does not work currently. But since these are stored variables, to make them work, all I'd have to do is add them to the buffer. Let me try it.

3:30pm. I copied the object and the blue metal and I am going through it step by step. Right now, I can only ask, is there something wrong with the weight3 variable? What it was supposed to show is curvature blended with the noise texture. For some reason, the AOV output ends up being pure black. I want to understand why that is happening.

3:50pm. Huh, I don't know. When I copied the material and set up the rendering image myself, the AOVs come out correctly. The way the image is set up for this project is weird. It says to use the current context for everything, but the light and the camera are in a different one.

I think that the reason it is not working is some kind of bug, but I haven't figure out what kind of bug exactly yet.

Let me try setting up an image in the original project. I know that I do not have much to gain from this, but I might as well complete the investigation since I started it.

4pm. Sigh, I am a moron. The reason weight3 is black because it is pointing to a different material than the one I thought. It happens to output all black into weight3. That solves that mystery.

4:05pm. It is freezing all of a sudden.

The Ctrl + Alt + click to zoom function seems to be buggy for some reason. It crashed Clarisse twice, and sometime it outright fails to do anything.

4:15pm. The baked textures lose a lot of detail when zoomed in. It is really a pity. But I wouldn't bake the complete system anyway.

At any rate, with this I am done with the UV baking project. I now understand every single aspect of it. Do I want to study any of the other examples, or should I just move on to the floor? Let me check out the TOC for the examples.

///

Bracelet
In this project you will find a setup of a bracelet with hundreds of gems made with scatterers. This is interesting to learn how refractive and reflective materials interact with lights and caustics.

Camera
This project shows you a setup of a shading layer that reconnects shaders to objects with simple rules.

City
This project is focused on layout. Learn how point clouds, scatterers, combiners and instances are used to set dress a gigantic futuristic city.

Clouds
A simple landscape project with volumes clouds using a free sample of the VDB Clouds Kit available to purchase at: http://tiny.cc/VDBclouds.

Collision detection
A simple project that shows you the scatterer collision detection feature.

Desert city
Another project that shows how to build a desert city from scratch.

Falling computers
This project shows you how to extract points attributes from an alembic file to place instances based on point id and how to drive rotation of scattered objects using point cloud properties.

Forest
This project uses simple point clouds and scatterers to generate a dense forest.

Light pass expression (LPE)
Little setup that shows how to configure light pass expression and how to use them to recompose the beauty.

Metro
A simple project that shows how to control rotation of scattered objects with a locator.

Miniride
This project is a small ride of spaceships flying in a desert.

Particle paint
In this project you will find a layout with objects scattered on a point cloud made with the particle and property paint tools.

Per instance time offset
This simple project shows how to set the scatterer in order to offset animation on instances.

Ray switch
In this project you will learn how to use ray switch texture node.

Razor
This project uses the render to texture feature to generate an HDR probe in real time.

Shader ball
This project provides you some basics PBR materials.

UV baking
The setup in this project lets you make a tileable scratch texture from a render. This project also shows how to bake a material using the UV bake feature.

Watch
Another example of look dev using layered materials and adaptive anti aliasing.

///

Let me take a short break here.

4:40pm. Let me resume.

The Razor project seems interesting, but I'll leave studying these for later. Let me finally take care of the floor.

5:10pm. Why is the panormaic camera so crappy here. It gets stretched massively near the top and bottom edges.

No, this thing is probably only for HDRIs. I do want the orthogonal camera after all.

5:20pm. I am dead. I give up on making this in Clarisse. Let me make a proper tileable texture in Houdini.

5:25pm. It had those labs node specifically for this job, but I forgot what it was named.

https://www.sidefx.com/tutorials/game-tools-mesh-tiler/

Oh this is it.

Got the scratches tiled. Now how do I UV bake the texture?

///

Baking to Texture
Once you have a tiling mesh you like, plug the result into the simple baker tool. (and your planar surface) Then select which texture maps you want to extract, such as Normal Map, Height Map, Roughness, AO, etc. Set your baking resolution and hit render. For more information on how to set up the Simple Baker, follow its tutorial here.

///

https://www.sidefx.com/docs/houdini/nodes/sop/labs--simple_baker-2.0.html

I've set it up, but when I click render what I get is it trying to open Redshift and failing. WTF?

5:55pm. Goddamit. I have no idea how to fix this. What the hell? Why is it looking for Redshift?

https://forums.odforce.net/topic/50627-how-to-set-the-renderer-for-labs-simple-baker/

Let me take a look at the environment.

6:10pm. I managed to resolve it. Simply removing the Redshift settings from the `houdini.env` file was enough.

But the resulting texture does not look right. What is going on?

6:25pm. It seems I did not set up the plane right. I need to have the ground plane be above the points. Let me finally load up the texture in Clarisse.

Ah, damn, there is some heavy blurring in the edges. It completely ruins the texture. How do I turn that off?

7pm. Had to leave for lunch.

https://www.sidefx.com/docs/houdini/nodes/sop/labs--maps_baker-3.0.html
> The map baker can transfer texture and data maps from high resolution to low resolution geometry. Unlike the games baker which relies on a mantra render, the maps baker uses a COPS network that is orders of magnitude faster than the mantra equivalent.

Hmmm, really? No, it does not matter. Seriously, why the hell is it messing with the edges and how do I stop it from doing that?

https://www.youtube.com/watch?v=B8HqBuH9xew
Baking Texture & Masking Maps at Lightspeed! | Paul Ambrosiussen | LAHUG

7:15pm. This is driving me insane. I am playing with different options and just running in circles. Let me watch some of the above.

https://youtu.be/B8HqBuH9xew?t=193

This isn't that uninteresting, but I just want to get through this issue at this point. I can't believe how much trouble the floor scratches are giving me.

8pm. I figured it out. I noticed in the talk he kept talking about UVs so I tried putting them on the grid and it started working. Maybe previously it was using parametric UVs which gave weird results. But it was 98% ok, which made me suspect UVs late.

8:10pm. Using surface normals as a tracing mode does not work that well. For some reason it is more likely to miss the target than hit it. I am guessing it does a grid search under the hood.

Ok, I get the texture running in Clarisse. Let me finish the video. I am not really happy with this. Maybe I should have exported the tiled objects as USD and point array'd them across the floor.

8:35pm. Yeah, the surface normals do not work well when the intersecting objects are almost flat as I suspected. Ok. At this point I think I understand the maps baker well enough. I've mastered the art of making scratch textures.

8:45pm. Let me lower the density, there are too many of them right now. And maybe it would be better if they were even thinner.

9:15pm. Let me close here. I have the floor scratches done to perfection.

9:20pm. I've really learned a lot about UV baking in the last two days.

Tomorrow, I should be able to get started with the props. A bed, desk, monitor, my PC case, stool, shelves, matresses, cushions, blankets...there is a lot of stuff to go through."

---
## [aslenofarid/kernel_asus_sdm660](https://github.com/aslenofarid/kernel_asus_sdm660)@[e50b21bed7...](https://github.com/aslenofarid/kernel_asus_sdm660/commit/e50b21bed7a439ab31c224d4ff18aec77bd8637d)
#### Wednesday 2022-03-23 21:10:18 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[20d3361f6b...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/20d3361f6b9e81e83b1fe2b69a57713f5a81cc2e)
#### Wednesday 2022-03-23 21:10:59 by SkyratBot

[MIRROR] makes podpeople spec_life call parent [MDB IGNORE] (#12106)

* makes podpeople call parent (#65362)

About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

* makes podpeople spec_life call parent

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [kaolincash/khaos](https://github.com/kaolincash/khaos)@[a9cca2ab8e...](https://github.com/kaolincash/khaos/commit/a9cca2ab8edfbe0adfc3768458eccb3ccf08a6c8)
#### Wednesday 2022-03-23 21:50:33 by noted bones haver kaolin maia cash

Add files via upload

iaso (named for the ancient Greek goddess of restoration, and all lowercase) is an Elden Ring Save File Backup & Restore tool which can be easily customised for a multitude of applications but, by default, keeps backups of your save files in case of errors.

**Contents**:
**i. A Personal Note**
**ii. Tested Scenarios**
**iii. Usage Instructions**
**iv. How It Works** 
**v. How To Customise**

**i. A Personal Note** (A.K.A. Don't be a cheater, cheater.)
Using iaso on your main save to restore lost runes and items is, in my opinion, contrary to the spirit of the game and constitutes cheating.
While I understand iaso can and probably will be used to make cheating more convenient, I feel the benefits outweigh the potential harm, given the undeniably shaky (see: understatement) PC release of Elden Ring.
I don't want my 300+ hours going down the drain due to the bugs that remain in the (otherwise reasonably playable, at this point) game, and I know you don't either.

p.s. you cannot restore saves to a new steam user id and the scope of the iaso project will never extend to that; she's purely a backup tool for a specified directory, geared toward adding a rudimentary quicksave feature to games where save files are particularly precious. I recommend also utilising this for other FromSoftware games by customising it as described below.

====================================================

**ii. Tested Scenarios** (like a few times to prove they worked, YMMV.)
Note: Fully Offline is the only intended usage of iaso. Does this break TOS? Probably. Do you care? Probably not.
I cannot account for all of FromSoftware's current or future shenanigan-detection tools, use at your own risk, don't call me if Miyazaki-san burns your house down with Flame of the Redmanes, you know the drill.
- Fully Offline: Works as intended.
- Logged into FromSoftware servers: Seems to work as expected. Cannot account for bans from prolonged use, idk, ymmv, etc.
- Using Steam Cloud + Logged into FromSoftware servers: Will not work, as Steam will restore your save.

====================================================

**iii. Usage Instructions** (Part 1: What do I do with these files?)
FIRST OF ALL: DISABLE STEAM CLOUD OR THIS WILL NOT WORK

> **So how do I use this?**

You download the batch files provided and run them as necessary.
You may need to fiddle with permissions/run as administrator, depending on your setup, but theoretically you can copy and paste the code into notepad, save it as "backup.bat" and so the same for "restore.bat" if you really wanted to.

> **Wait, I have to run these manually, every time?**

Not necessarily! In my case, I'm using Corsair iCUE to map F5 and F6 to backup and restore within the eldenring.exe program when it runs.

> **So I can just map the .bat files to F5 and F6 and save/restore my state every time I lose my runes?**

NO! DO NOT USE IASO FOR THAT PURPOSE, SUCH AN ACTION COULD PERMANENTLY RUIN YOUR SAVE FILE.
This is not an undo-redo key that will teleport your character back in time. 
If the restore tool is used while the game is running it could easily damage your save because I can't account for how eldenring.exe uses those files while they're loaded.
Restoring with iaso while in the Main Menu _should_ be fine, as the save files are not loaded, but I cannot account for what eldenring.exe might be doing behind the scenes. 
I haven't tested it extensively so, please let me know of any cases of this happening should you deign to risk it.

Remember: iaso is a tool for backing up and restoring save files THAT ARE NOT IN USE for the EXPLICIT PURPOSE of PREVENTING loss of your entire save by the game crashing and rendering your only copy of the game's save file unusable. Do, however, keep in mind that it is ONLY the restore function that has any potential downside. Spam F5 to your heart's content.

Seriously, though, don't abuse the restore function.

> **Wait- what? Isn't it extremely risky to restore the save files at all, then?**

Yes. Of course it is. IF and ONLY if the game is running and the files are in use. Similar to when the game generates stormy weather and crashes and threatens you for not closing it properly is a risk to the integrity of your save data, so, too, is overwriting live save files in a running game. 
I also recognise that FromSoftware have, themselves, claimed that this specific issue has been addressed (regarding the save file corruptions, not the crashes..). 
Just be patient whenever you want to restore a backup and close the game first.

> **Okay, I see your point, but I'm not sure the risk is justified nonetheless...**

That's entirely reasonable.

> **...try to convince me?**

If you insist, I will go into explicit detail of how iaso does her thing (it's actually very simple, if a little wordy by virtue of it being written by... me). For the benefit of any laypersons who struggle to parse code and want to know what's happening, though, I'll do my best to make it easy enough to follow.

> **Ok, thanks. Also, while I still have you here, I really hate that when you named it "iaso", you spelled it in all lowercase.**

It's actually "her".

====================================================

**iii. Usage Instructions** (Part 2: So... What Am I Even Using, Then?)
The broad strokes of how the backup process works are as follows:
1) iaso creates two backups.
        1a) The first backup is your quicksave slot, and is called "EldenRingQuicksave"
        1b) The second backup is an archive that stores every backup made with iaso unless you personally remove them
2) There is no number 2)

> **Ok so how is that dangerous?**

It's not, when you're restoring the files manually.
The danger arises when you restore the files, which is what happens next.

> **There _is_ a number 2)!**

There is a _number 2)_ in that there is a second file to worry about, yes.
The second program, restore.bat, indiscriminately overwrites everything within "EldenRing" (your actual real live save folder with every single save slot you have  inside it) with the contents of "EldenRingQuicksave" with no confirmation prompt for accidental executions. This is for the benefit of those, myself included, mapping this to a key like F6. 
You see, I play with an Xbox controller, and my keyboard is physically disabled with a custom profile that makes all but the "switch profile" and "printscreen" keys functionless, to prevent accidental interactions. I even spliced a push button into my mouse's cable so that I can toggle it on the fly without unplugging it.
I won't be pressing this thing by accident. 
You, however, might. 
Don't.

> **That's supposed to convince me?**

Think about it: I had to idiot-proof my own keyboard and mouse because I'm clumsy, not stupid, and I suspect you, also, are not stupid. This tool is idiot proof in that even if you fuck up your save, it by design has a separate archive of manually restorable backups. In fact, there is no way to auto-restore these, you *have* to do it manually if you're restoring anything other than the quicksave slot. iaso, when used as intended, should be completely safe to use. If your computer is struck by lightning halfway through a restoration, it might go weird, but you have an archive, including the exact quicksave you were just attempting to restore, which also exists within the quicksave slot until overwitten. Just don't be stupid, stupid.

> **Alright, I'm convinced. I feel like I should be a little offended by some of that, but I'm reasonably convinced that having two separate backups is probably overkill put in for the sole reason that you, yourself, are an idiot.**

Exactly! I'm glad you agree that I am an idiot.

> **Anything else?**

Read on if you want to learn in detail how this works, otherwise just use the files as directed above.
While the game isn't running.
Please.

====================================================

**iv. How It Works** (A.K.A. The Viewer Retention Drop-Off Point)
A very simple explanation of how it works, for the layperson who wants to customise this easily, here's the excerpt that does the backup itself:
Here we establish what the variable "slot" is, which we later append to the path we're interested in as its unique name.
A sensible way to generate a consistently unique name for each slot is to take the current time, which will never be the same twice.

`set slot="%year%-%month%-%day%@%hour%%minute%Hrs%second%s - TO MANUALLY RESTORE simply rename me 'EldenRing' and overwrite the current 'AppData-Roaming-EldenRing' folder."`

This has the added benefit of allowing us to find the most recent save, or to restore to an older backup from a time we know was good!

Next, we establish our paths. In this case, it's Elden Ring, which doesn't have its own quicksave feature.

`set source=%APPDATA%\EldenRing`

`set backup=%APPDATA%\EldenRingQuicksave`

`set archive="%APPDATA%\EldenRingArchive\%slot%"`

We have three folders here:

`source = the actual place Elden Ring stores the save files for your game`

`quicksave = the quicksave folder that will contain your most recent quicksave, ready to redeploy later`

`archive = every quicksave that you've made, which could get large if you use this a lot. I haven't implemented an auto purge, so you will have to be cognisant of this.`

All of these are stored within `C:\Users\[Your Username]\AppData\Roaming`.

Using the %APPDATA% shorthand (which, incidentally, also works in the Windows Explorer address bar, to get you there quicker if you want to go digging) we can avoid having to alter this for every single user as the [Your Username] is, of course, variable. Overall, this makes the path easier to type for me if I need to use it again, and easier to read, understand, and edit for the end user (that's you!) <3

Finally, we run the logic of the program!
All this does is copy the source directory we defined earlier into two places, in two slightly different ways:
Remember in the previous step, we defined the "archive" variable to have an appendix? This is where our "slot" variable from earlier comes back into play.

First, we `robocopy` from `source` to `quicksave`, which makes a copy of the "EldenRing" folder, which is of course in the ideal state already, and makes a 1:1 copy of it right next to it, named "EldenRingQuicksave". This cloned directory will be at C:\Users\[VARIABLE STRING]\AppData\Roaming, right alongside the original EldenRing directory.
Note: the /E option tells robocopy we want *everything* inside the source folder. This means we want its subdirectories, and not just the files inside the folder you asked for, as robocopy by default will only copy files and not directories.

`robocopy %source% %quicksave% /E`

The next line is similar, but it uses `robocopy` from the `source` folder to the `archive`, which means it copies "EldenRing" to a second sister directory named "EldenRingArchive", but because we added the `"\%slot%"` appendix, the `\` tells robocopy to make a new directory inside EldenRingArchive named "%slot%", which uses the variable from our very first step that we've already defined as the current time.

So, that next line:

`robocopy %source% %archive%`

Let's break that down a bit into exactly what we're saying to the computer here. What we're doing here is trying to give instructions the computer can understand, one at a time, in as efficient a way as possible (it's simply faster if there's less data to parse). Here we have a total of 5 major things occurring that we've asked the computer to do:
1) Do the thing. Here, the thing we want it to do is to copy, so we use the tool "robocopy" (there are other choices, I like robocopy) that performs this task because it was built in much the same way as I'm building this to perform this specific function.
2) Tell robocopy what to copy
3) Tell robocopy where to copy it & what to name it
4) Which in our case is made up of two parts; the root path, and also the %slot%, bundled together as the %archive% variable
5) How robocopy should handle contingencies such as already existing files

<sup>[1]</sup>`robocopy` <sup>[2]</sup>`%source%` <sup>[3][4]</sup>`%archive%` <sup>[5]</sup>`/E /is /it`

Which is the same as saying: 

<sup>[1]</sup>`robocopy`   +   <sup>[2]</sup>`%APPDATA%\EldenRing`   +   <sup>[3]</sup>`"%APPDATA%\EldenRingArchive\EldenRing -`   +   <sup>[4]</sup>`%slot%`   +   <sup>[5]</sup>`/E /is /it `

Which, itself, is the same as telling your computer to

<sup>[1]</sup>`make a copy of `   +   <sup>[2]</sup>`the folder called C:\Users\[Your Username]\AppData\Roaming\EldenRing and paste it at`   +   <sup>[3]</sup>`C:\Users\YourUsername\AppData\Roaming\EldenRingArchive\`   +   <sup>[4]</sup>`whatever the current date & time is in YYYY/MM/DD] and the instructional suffix`   +   <sup>[5]</sup>`and include every subdirectory when you do it, overwriting them if they already exist, irrespective of their attributes`

The result of the second line of code is that we are left with an archive directory of timestamped directories which, themselves, are clones of "EldenRing", and can be restored manually by following the instructions provided in the name of the directory itself. Simple!

A lot to read, but simple in principle.

And now we can begin to talk about how the restoration works. This is also simple, and requires much less explanation:

`robocopy %quicksave% %source%`

It does the same as 

`robocopy %source% %quicksave%`

from earlier. But in reverse. Simple.

====================================================

**v. How to Customise** (or How I Learned To Stop Worrying And Modify The Code)
Hopefully, you read how it all works above, so I shouldn't actually need to explain this if you've been able to infer it already.
Of course, I would personally have skipped to this section first upon seeing the customisation section in the contents and thinking "ooh!" because I'm a terrible groblin, and in case that's exactly what you've just done too (hi, I see you), then here's explicit instructions:

There are three variables you need to be concerned with:

`set source="Your source path, i.e. your Dark Souls or BloodBorne save locations (which I don't know offhand so you'll have to Google it, I'm not your mom)."`

`set quicksave="Your backup location, which can be anywhere. This is where your quicksave slot will exist, and will be an exact copy of the path you specified in %source% in the line above this one."`

`set archive="your archive location, which can also be anywhere. This is the reference library of all the quicksaves you've ever made. Assuming all variables are correct, this one is easily your most important one. Keep it secret, keep it safe."`

IMPORTANT TIP: If your path has spaces in it, you must enclose the entire path with quotes. For example, in the following example, only one of these will work:

`set source="%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED"`

will work (fine, I did look it up myself, get off my back)
however; 

`set source=%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED`

will not work fine, because the space following "DARK" in "DARK SOULS" is parsed as the end of the path.

So (y'know what, fuck it, have this one on me, too), an example of this altered for Dark Souls would be the following, for the entire batch file:

```
echo off
set year=%date:~6,4%
set month=%date:~3,2%
set day=%date:~0,2%
set hour=%time:~0,2%
if %hour% lss 10 (set hour=0%time:~1,1%)
set minute=%time:~3,2%
set second=%time:~6,5%
set slot="%year%-%month%-%day%@%hour%%minute%Hrs%second%s - TO MANUALLY RESTORE simply rename me and overwrite the existing save folder."

set source="%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED"
set quicksave="%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED QUICKSAVE"
set archive="%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED ARCHIVE\%slot%"

robocopy %source% %quicksave% /E /is /it
robocopy %source% %archive% /E /is /it
```

and the restore.bat, which you should save as a separate file:

```
echo off
robocopy "%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED QUICKSAVE" "%USERPROFILE%\Documents\FromSoftware\DARK SOULS REMASTERED" /E /is /it
```
Now don't say I never did anything for you, kid.

maia

---
## [sirhunkzalot/Harpaesis](https://github.com/sirhunkzalot/Harpaesis)@[851412704e...](https://github.com/sirhunkzalot/Harpaesis/commit/851412704ec5c76cbb89450361ab7b44e7d27665)
#### Wednesday 2022-03-23 23:06:08 by Matthew Sommer

I did it I did the thing its fixed i'm so god damn tired i usually get annoyed when people do bad commit titles/descriptions but holy shit man.

---
## [gunmantheh/mpv](https://github.com/gunmantheh/mpv)@[27e5416c12...](https://github.com/gunmantheh/mpv/commit/27e5416c124884758bb206bb5948221a5f00f87d)
#### Wednesday 2022-03-23 23:22:59 by wm4

video: add pixel component location metadata

I thought I'd probably want something like this, so the hardcoded stuff
in repack.c can be removed eventually. Of course this has no purpose at
all, and will not have any. (For now, this provides only metadata, and
nothing uses it, apart from the "test" that dumps it as text.)

This adds full support for AV_PIX_FMT_UYYVYY411 (probably out of spite,
because the format is 100% useless). Support for some mpv-only formats
is missing, ironically.

The code goes through _lengths_ to try to make sense out of the FFmpeg
AVPixFmtDescriptor data. Which is even more amazing that the new
metadata basically mirrors pixdesc, and just adds to it. Considering
code complexity and speed issues (it takes time to crunch through all
this shit all the time), and especially the fact that pixdesc is very
_incomplete_, it would probably better to have our own table to all
formats. But then we'd not scramble every time FFmpeg adds a new format,
which would be annoying. On the other hand, by using pixdesc, we get the
excitement to see whether this code will work, or break everything in
catastrophic ways.

The data structure still sucks a lot. Maybe I'll redo it again. The text
dump is weirdly differently formatted than the C struct - because I'm
not happy with the representation. Maybe I'll redo it all over again.

In summary: this commit does nothing.

---
## [gunmantheh/mpv](https://github.com/gunmantheh/mpv)@[5309497727...](https://github.com/gunmantheh/mpv/commit/5309497727debfe1b268f915c5a41bdbe93ad9de)
#### Wednesday 2022-03-23 23:22:59 by wm4

subprocess: replace posix_spawnp() with fork()

This code runs posix_spawnp() within a fork() in some cases, in order to
"disown" processes which are meant as being started detached. But
posix_spawnp() is not marked as async-signal-safe, so what we do is not
allowed. It could for example cause deadlocks, depending on
implementation and luck at runtime. Turns out posix_spawnp() is useless
crap.

Replace it with "classic" fork() to ensure correctness.

We could probably use another mechanism to start a process "disowned"
than doing a double-fork(). The only problem with "disowning" a process
is calling setsid() (which posix_spawnp() didn't support, but maybe will
in newer revisions), and removing as as parent from the child process
(the double-fork() will make PID 1 the parent). But there is no good way
to either remove us as parent, or to "reap" the PID in a way that is
safe and less of a mess than the current code. This is because
POSIX/UNIX is a miserable heap of shit. (Less shit than "alternatives"
like win32, no doubt.)

Because POSIX/UNIX is a miserable heap of shit, execvp() is also not
specified as async-signal-safe. It's funny how you can run a full
fledged HTTP server in an async-signal-safe context, but not start a
shitty damn process. Unix is really, really, really extremely bad at
this process management stuff. So we reimplement execvp() in an
async-signal-safe way.

The new code assumes that CLOEXEC is a thing. Since POSIX/UNIX is such a
heap of shit, O_CLOEXEC and FD_CLOEXEC were (probably) added at
different times, but both must be present. io.h defines them to 0 if
they don't exist, and in this case the code will error out at runtime.
Surely we could do without CLOEXEC via fallback, but I'll do that only
if at least 1 bug is reported wrt. this issue.

The idea how to report exec() failure or success is from musl. The way
as_execvpe() is also inspired by musl (for example, the list of error
codes that should make it fail is the same as in musl's code).

---
## [gunmantheh/mpv](https://github.com/gunmantheh/mpv)@[c6369933f1...](https://github.com/gunmantheh/mpv/commit/c6369933f1d9cd204b09be95ef7d4ed1351610e2)
#### Wednesday 2022-03-23 23:22:59 by wm4

command: add property to return text subtitles in ASS

See manpage additions. This was requested, sort of. Although what has
been requested might be something completely different. So this is
speculative.

This also changes sub_get_text() to return an allocated copy, because
the buffer shit was too damn messy.

---

