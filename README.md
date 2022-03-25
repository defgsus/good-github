## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-24](docs/good-messages/2022/2022-03-24.md)


1,842,943 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,842,943 were push events containing 2,912,542 commit messages that amount to 203,827,897 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [TheFakeElon/tgstation](https://github.com/TheFakeElon/tgstation)@[dd747fcc5a...](https://github.com/TheFakeElon/tgstation/commit/dd747fcc5a46df051a5fe0e42950c46c72269244)
#### Thursday 2022-03-24 00:39:16 by MrMelbert

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
## [JuliaLang/julia](https://github.com/JuliaLang/julia)@[62e0729dbc...](https://github.com/JuliaLang/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Thursday 2022-03-24 00:55:41 by Mirek Kratochvil

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
## [macdice/postgres](https://github.com/macdice/postgres)@[ec62cb0aac...](https://github.com/macdice/postgres/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Thursday 2022-03-24 02:22:33 by Tom Lane

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
## [zinc-collective/convene](https://github.com/zinc-collective/convene)@[8fd6ea7922...](https://github.com/zinc-collective/convene/commit/8fd6ea7922adf82f949b018b89cda31a2a0c77b8)
#### Thursday 2022-03-24 02:42:10 by Zee Spencer

Sprout EmbeddedForm independent of Space Registration

EmbeddedForms allow AirTable forms to be embedded directly into a Room.

Things like opinion polls, newsletter signups, comment boxes, etc.

If you can make an AirTable form for it, you can put it on your landing
page!

Squashed commit of the following:

commit 6054b87ce21f8a07084d9ccd00f3d0c0c1fedcf6
Author: Zee Spencer <zspencer@users.noreply.github.com>
Date:   Wed Mar 9 20:05:15 2022 -0800

    Add some todos for cleanup

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

commit 76b59e4b47b033882882ab93a24e778df14f2851
Author: Zee Spencer <zspencer@users.noreply.github.com>
Date:   Wed Mar 9 19:23:08 2022 -0800

    Reframe acquiring a space to include the Waitlist

    We took some time to sketch out a little bit about what the "onboarding"
    experience looks like for Convene (and theoretically, "Products" built
    on Convene that want to use a "waitlist" for letting people into their
    product.)

    Next step: Sprout the furniture?

    See: https://github.com/zinc-collective/convene/issues/8

    Co-authored-by: Ana Ulin <ana@ulin.org>

---
## [zinc-collective/convene](https://github.com/zinc-collective/convene)@[add90291f1...](https://github.com/zinc-collective/convene/commit/add90291f1e5462c6e27db0bb624bd148e470c93)
#### Thursday 2022-03-24 02:50:02 by Zee

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
## [feifeibear/pytorch](https://github.com/feifeibear/pytorch)@[65329f4fac...](https://github.com/feifeibear/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Thursday 2022-03-24 03:34:24 by Edward Z. Yang

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
## [WifiRouterYT/wifirouteryt.github.io](https://github.com/WifiRouterYT/wifirouteryt.github.io)@[6fa8eb3cda...](https://github.com/WifiRouterYT/wifirouteryt.github.io/commit/6fa8eb3cda277e7b3f5f63e743dd092a31dfacbd)
#### Thursday 2022-03-24 05:05:22 by WifiRouter

remade background + title

this took so long holy fucking shit

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[f697fd9bca...](https://github.com/k21971/EvilHack/commit/f697fd9bca00ae89618f71d84912947525d39e5f)
#### Thursday 2022-03-24 05:09:57 by k21971

The Hand of Vecna.

Previously, upon destroying Vecna, he would maybe drop the Eye of Vecna,
or sometimes he wouldn't. Now when he's destroyed, he'll either drop the
Eye or the Hand of Vecna (50/50 chance). One or the other, but never
both (or neither). This artifact is a special case - in other variants
that have the Hand of Vecna, it's just another food object, much like
the Eye. For EvilHack, it's much more. The Hand of Vecna is technically
a pair of flesh gloves that the player can 'wear'. In inventory it won't
show as a pair of gloves, but as a single mummified hand. When putting
it on, the player receives some rather scary feedback about how their
left hand withers away and dies, and the Hand replaces their original
hand, fusing with their arm. It even shows that way when viewing it in
inventory. Because of this, once the Hand of Vecna is 'worn', it can
never be removed. And because it's technically gloves, the player can't
wear another pair of gloves over it, which is in keeping with how it was
handled via many ad&d sessions, as the Hand of Vecna would not allow
itself to be covered or confined by such simple things.

The breakdown of its abilities and behavior:
* The Hand of Vecna appears as a 'mummified hand', and takes up the
glove slot for worn armor
* Once worn, it cannot be removed, ever. Even if the player polymorphs
into a monster that would normally cause it to drop their gloves
* Because of this, it is immune to erosion, disintegration, destroy
armor monster spell, and destroy armor scroll. It also cannot be stolen
when worn
* It can be enchanted up to +7, but because it can't be destroyed, it
will never evaporate if attempting to enchant it higher than +7 (nothing
happens)
* Special abilities - hungerless regeneration, half physical damage,
disease resistance. It can be invoked for its death magic, killing or
hurting any monster within line of sight that isn't resistant to death
magic. Just as with the Eye of Vecna, invoking its death magic has
consequences
* The Hand of Vecna also confers giant strength like gauntlets of
power, and will cause an additional 1d5 + 7 (8-12) hit points of cold
damage via melee attack to monsters affected by cold, regardless of
whether a weapon is wielded or are fighting bare-handed
* The Hand must be worn for any of the above-listed special abilities to
work
* Worn rings can be removed without issue without needing to remove the
Hand of Vecna, even if it's cursed - it's not treated as a pair of
gloves, even though it techincally is
* Because the Hand is technically dead, players can pick up objects such
as a cockatrice corpse without penalty (another case of 'it's not a pair
of gloves, but technically it is')
* Monsters are scared of the power of the Hand of Vecna, and will not
attempt to 'merge' with it

I may have missed some cases where the player could actually remove the
Hand once worn. If so, should be fun hunting those cases down. This is
another one of those artifacts that was a lot of fun to make, and should
give the player that much more incentive to try and defeat Vecna.

There's a couple small bugs I've noticed and corrected while working on
this, the most important one being that hungerless regeneration was not
working when wielding artifacts like Trollsbane or the Staff of
Aesculapius. Not entirely sure that innate giant race hungerless
regeneration was working either. They do now though.

Enjoy :)

---
## [mikesmiffy128/sst](https://github.com/mikesmiffy128/sst)@[00ad7cdd3d...](https://github.com/mikesmiffy128/sst/commit/00ad7cdd3d05d09a43bda972c823fdc440feabb9)
#### Thursday 2022-03-24 05:18:05 by Michael Smith

Clean up gameinfo_init() and other random stuff

- Just ask the engine for the game directory instead of doing the stupid
  argv sniffing hacks from the early days of trying to get the damn
  thing working.

- Also add some other path variables, functions and whatnot, and do some
  other minor tidying up.

- Also also, another damn copyright year, somebody please help me.

Unfortunate negative effect off this change: con_init() no longer
reports the game name, because it has to happen before gameinfo_init().
I've decided I don't really care, though.

---
## [madhubkk/gate](https://github.com/madhubkk/gate)@[e2a108db75...](https://github.com/madhubkk/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Thursday 2022-03-24 05:58:31 by Chris Phillips

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
## [kangalioo/poise](https://github.com/kangalioo/poise)@[f5aff9a625...](https://github.com/kangalioo/poise/commit/f5aff9a62558966ad8b91036371f1d228f474ca6)
#### Thursday 2022-03-24 06:08:42 by kangalioo

Don't apply reuse_response for slash

Why? It all begins with modals. When you send a modal as the initial response (it has to be), and the command is marked reuse_response, poise was trying to edit the modal as if it were a message and crash. This didin't ever fail before because pre-modals, all initial interaction response possibilities were editable into text. Anyways, there's a bunch of ugly solutions, like keeping track in ApplicationContext not only whether a response was sent, but also whether it was a modal, in which case the reuse_response editing would be directed at a followup response instead, so you'd also keep track of the followup response message ID and it's all a big mess. And then I remembered why reuse_response exists in the first place and it's for prefix commands, for edit tracking. And using reuse_response for slash doesn't even really make sense, like, think about it, you're sending multiple messages in the code (`ctx.send(1); ctx.send(2);`) but it all goes in a single message. Makes no sense. If people wanna edit their initial response, they should do _that_: `ctx.send(1).edit(2);`. And this now also works absolutely fine with modals. You can do `Modal::execute(ctx); ctx.send(1).edit(2);` and the edit will not try to edit the modal, but it will edit the send(1) which is already a followup message because Modal::execute set the has_sent_initial_response atomic flag, and everything was fine. I hope. We will see

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[a6e923df06...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/a6e923df06c138578a4434ef04727a3db5087d67)
#### Thursday 2022-03-24 06:49:59 by Angelo G. Del Regno

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
## [Nireru/PF_UE4_Catch](https://github.com/Nireru/PF_UE4_Catch)@[1e73dce423...](https://github.com/Nireru/PF_UE4_Catch/commit/1e73dce4239bafed0557e4975b27dcd548cfe893)
#### Thursday 2022-03-24 06:52:21 by Nireru

Final? I think

+ pause now works

But idk what to add else. In my opinion adding more features is just polishing complete game and does'nt give any progress/experience for me.
Random shape of collectables? Nah.
Losing? Why?
Saving top score? Probably, but unnecesarry. Game may become more competitive than chill at certain moments.
Main menu? Nah.
Adding music? Idk about copyright.

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[759d24ab14...](https://github.com/JohnFulpWillard/tgstation/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Thursday 2022-03-24 07:10:00 by san7890

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
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[884c1eeb62...](https://github.com/JohnFulpWillard/tgstation/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Thursday 2022-03-24 07:10:00 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[55336d1e53...](https://github.com/tgstation/tgstation/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Thursday 2022-03-24 09:12:29 by vincentiusvin

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
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[745426eff2...](https://github.com/vincentiusvin/tgstation/commit/745426eff227ff556105147a4802540617decd7b)
#### Thursday 2022-03-24 09:19:32 by LemonInTheDark

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
## [mcgrof/kdevops](https://github.com/mcgrof/kdevops)@[99b78db71e...](https://github.com/mcgrof/kdevops/commit/99b78db71edbb01048f375030ff464e7f8faa024)
#### Thursday 2022-03-24 09:52:32 by Luis Chamberlain

install_vagrant: enhance the redhat install

Make it clear our goal on redhat distros that our goal
is to force install the zip file directly. Force the fact
force_install_zip=true.

Likewise the manual installer does not verify and ensure
that you have a few packages to actually use vagrant properly,
so provide those packages as well.

Lastly, ensure we nuke the existing version of vagrant if
force_install_zip=true to ensure we actually upgrade in case
a user is stuck with an ancient release.

Note: for fedora we should strive to avoid this holy hell,
actually any sensible distribution will learn fast that this
path of manually installing vagrant-libvirt lies complete
madness and so the only thing sensible to do is to package
them.

I'll expand a bit more on this to help distributions when
evaluating if they should package vagrant or vagrant-libvirt:

If you are an enterprise release you probably don't because
of the entire holy hell dependency chain and the amount of work
you are then implying to support for many years all that ruby
crap. However you probably have some sort of "public" distro
oulet, so use that and package vagrant and vagrant-libvirt
crap there. The vagrant-libvirt stuff needs tons of work that
someone should just do to make vagrant libvirt provider a proper
first class citizen as the virtualbox one is, and so we don't have
to depend on two stupid packages. I think kdevops illustrates well
with manual commands what needs to get done to get this to happen.

Holy hell and can we simply have a rewrite of vagrant to some
sensible programming language other than this ruby crap? </rant>

Signed-off-by: Luis Chamberlain <mcgrof@kernel.org>

---
## [mcgrof/kdevops](https://github.com/mcgrof/kdevops)@[c4019b9448...](https://github.com/mcgrof/kdevops/commit/c4019b9448f53ae0a9223759dc3841b126be1c1c)
#### Thursday 2022-03-24 09:52:32 by Luis Chamberlain

Vagrantfile: add support for a custom libvirt storage pool path

Prior to this change we always override the default for the
vagrant-libvirt plugin for the libvirt.storage_pool_path with:

libvirt.storage_pool_path = File.dirname(__FILE__)

__FILE__ in this case is kdevops Vagrantfile, so if you git cloned
kdevops in $HOME/kdevops this pool path is set to $HOME/kdevops/vagrant.
This is broken for a few reasons, the latest discovered reason being
is stated below which forces us to now change the default mechanism to
something more sensible:

1) If using libvirt vagrant tries to chown this directory to root,
   and for obvious reasons this is stupid. This means a user hacking
   on kdevops under $HOME/kdevops/ now sees $HOME/kdevops/vagrant owned
   as root. This presents all sorts of stupid issues requiring manual
   changes by the user.

2) If you git cloned kdevops under a directory under $HOME and if the
   $HOME directory has the permissions o-rw it means even if qemu runs
   as a user qemu, it won't be able to access the nvme drives or the
   images downloaded / created for the guest through kdevops.

Let's change the default to use something outside of the $HOME, and let
users manually select the old behavior. Since some Linux distributions
(SUSE) might have been relying on the prior behaviour so we enable the old
behaviour only for those distributions. We leave it up to those
distributions to revise and ensure that migrating to the new behaviour
is fine and folks using kdevops in production are ready for this change.

Since the pool path is also used on Virtualbox we refer to this as the
kdevops pool path. Virtualbox uses the pool path to create the additional
nvme drives only, so we create kconfig symbols for both libvirt and virtualbox
and provide descriptions of what this pool path means for each of them.

The last step is to ensure the pool path has the correct expected
permissions as otherwise we won't be able to get a user to read
or write to that directory. We take the liberty to change permissions
on the pool path as the user is aware of this during configuration,
however it would be stupid and wild to assume we can or should go
beyond that directory or files already on that directory. And this
is precisely why using anything based on $HOME was stupid to begin
with, although at first it probably it seemed like a nice idea.

This should fix the first 'make bringup' issues faced on a few
distributions which have o-rx on $HOME if a user git cloned kdevops
inside their $HOME somewhere, as our default for the kdevops pool
path is now is outside $HOME. If the user insists to use the pool
path within the $HOME directory at least there is enough documentation
to enable the to do what they need (chmod o+rw $HOME), but we're not
going to do that for them.

This lets us also simplfy out all the crazy ruby chown / mkdir / chgrp
stuff with just 2 nice ansible tasks delegated to the install_vagrant
ansible role. This is also another demonstration as to *why* the lease
vagrant does the better.

Signed-off-by: Luis Chamberlain <mcgrof@kernel.org>

---
## [LuciferHorst/HFU-3.0](https://github.com/LuciferHorst/HFU-3.0)@[806d4580bb...](https://github.com/LuciferHorst/HFU-3.0/commit/806d4580bb509650765863418bf4294c5bbc27f8)
#### Thursday 2022-03-24 11:14:51 by Jokertard

Some slight inf/tank changes

-INF/Special forces got a bit more breakthrough and soft attack through gun techs
- Tank hull breakthrough  got slightly lowered
- Main gun of tanks got its IC upped a bit while some modules lost IC, mainly radio
- Heavy tank Guns buffed slightly (Will look into armor later fuck you lucifer)
- Defense module is now 5 defense instead of 3 but doesnt give 10% BRK, and u can only put 1 on tanks (u can still put multiple on mech)
- Stabilizers are back
- Mech 2/3 lost base defense and mech in general is slightly cheaper

---
## [ThirteenAG/pcsx2](https://github.com/ThirteenAG/pcsx2)@[d6684efd26...](https://github.com/ThirteenAG/pcsx2/commit/d6684efd262ef1c83d37c50b48edc478952dddf9)
#### Thursday 2022-03-24 12:27:24 by RedDevilus

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
## [ArrowOS-Devices/android_kernel_xiaomi_sdm660](https://github.com/ArrowOS-Devices/android_kernel_xiaomi_sdm660)@[a938b43afa...](https://github.com/ArrowOS-Devices/android_kernel_xiaomi_sdm660/commit/a938b43afab7eca662afd122b4677a76e246ba75)
#### Thursday 2022-03-24 13:05:49 by Maciej Żenczykowski

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
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [ABJ4403/Payback2_CHEATus](https://github.com/ABJ4403/Payback2_CHEATus)@[7d5c35e30c...](https://github.com/ABJ4403/Payback2_CHEATus/commit/7d5c35e30caa479270e993f66d015417ae0d98d5)
#### Thursday 2022-03-24 13:47:42 by MDP43140

Update Payback2_CHEATus to v2.1.2

from @ABJ4403 (lol he's too lazy to do it):
+ changing some tables-related functions (Thanks to "Rabia Alhaffar" for some Lua Polyfill functions).
+ New god mode cheats: No car steal (if it doesnt work, you need to reduce the freeze duration in GG settings).
+ New god mode cheats: Change veichle color (this includes RAINBOW, haha AlphaGG so u thought only you have it? i also have it lmao XD).
+ Changed | to + for better compatibility (with standard Lua interpreter) and debugging.
+ Deprecate useFuzzyDecrease on loopSearch (its useless now, replaced by searchEntityAnchor, loopSearch now used for whole different stuff).
+ PredefinedLangLists now located outside of the function for better performance, and RAM management, and to prevent extra CPU cycle wasted.
+ formatting function improved.
+ and more...

---
## [FTPam/ICPC-Practice](https://github.com/FTPam/ICPC-Practice)@[37a386226d...](https://github.com/FTPam/ICPC-Practice/commit/37a386226da73d5caed9897107fb449a2be049d1)
#### Thursday 2022-03-24 13:48:25 by TPam

Create 暴力.cpp

Description

N (2 <= N <= 8,000) cows have unique brands in the range 1..N. In a spectacular display of poor judgment, they visited the neighborhood 'watering hole' and drank a few too many beers before dinner. When it was time to line up for their evening meal, they did not line up in the required ascending numerical order of their brands.

Regrettably, FJ does not have a way to sort them. Furthermore, he's not very good at observing problems. Instead of writing down each cow's brand, he determined a rather silly statistic: For each cow in line, he knows the number of cows that precede that cow in line that do, in fact, have smaller brands than that cow.

Given this data, tell FJ the exact ordering of the cows.
Input

* Line 1: A single integer, N

* Lines 2..N: These N-1 lines describe the number of cows that precede a given cow in line and have brands smaller than that cow. Of course, no cows precede the first cow in line, so she is not listed. Line 2 of the input describes the number of preceding cows whose brands are smaller than the cow in slot #2; line 3 describes the number of preceding cows whose brands are smaller than the cow in slot #3; and so on.
Output

* Lines 1..N: Each of the N lines of output tells the brand of a cow in line. Line #1 of the output tells the brand of the first cow in line; line 2 tells the brand of the second cow; and so on.
Sample Input

5
1
2
1
0
Sample Output

2
4
5
3
1
Source

USACO 2003 U S Open Orange

---
## [leeonon/react](https://github.com/leeonon/react)@[c7b4497988...](https://github.com/leeonon/react/commit/c7b4497988e81606f1c7686434f55a49342c9efc)
#### Thursday 2022-03-24 14:44:48 by Andrew Clark

[Experiment] Lazily propagate context changes (#20890)

* Move context comparison to consumer

In the lazy context implementation, not all context changes are
propagated from the provider, so we can't rely on the propagation alone
to mark the consumer as dirty. The consumer needs to compare to the
previous value, like we do for state and context.

I added a `memoizedValue` field to the context dependency type. Then in
the consumer, we iterate over the current dependencies to see if
something changed. We only do this iteration after props and state has
already bailed out, so it's a relatively uncommon path, except at the
root of a changed subtree. Alternatively, we could move these
comparisons into `readContext`, but that's a much hotter path, so I
think this is an appropriate trade off.

* [Experiment] Lazily propagate context changes

When a context provider changes, we scan the tree for matching consumers
and mark them as dirty so that we know they have pending work. This
prevents us from bailing out if, say, an intermediate wrapper is
memoized.

Currently, we propagate these changes eagerly, at the provider.

However, in many cases, we would have ended up visiting the consumer
nodes anyway, as part of the normal render traversal, because there's no
memoized node in between that bails out.

We can save CPU cycles by propagating changes only when we hit a
memoized component — so, instead of propagating eagerly at the provider,
we propagate lazily if or when something bails out.

Most of our bailout logic is centralized in
`bailoutOnAlreadyFinishedWork`, so this ended up being not that
difficult to implement correctly.

There are some exceptions: Suspense and Offscreen. Those are special
because they sometimes defer the rendering of their children to a
completely separate render cycle. In those cases, we must take extra
care to propagate *all* the context changes, not just the first one.

I'm pleasantly surprised at how little I needed to change in this
initial implementation. I was worried I'd have to use the reconciler
fork, but I ended up being able to wrap all my changes in a regular
feature flag. So, we could run an experiment in parallel to our other
ones.

I do consider this a risky rollout overall because of the potential for
subtle semantic deviations. However, the model is simple enough that I
don't expect us to have trouble fixing regressions if or when they arise
during internal dogfooding.

---

This is largely based on [RFC#118](https://github.com/reactjs/rfcs/pull/118),
by @gnoff. I did deviate in some of the implementation details, though.

The main one is how I chose to track context changes. Instead of storing
a dirty flag on the stack, I added a `memoizedValue` field to the
context dependency object. Then, to check if something has changed, the
consumer compares the new context value to the old (memoized) one.

This is necessary because of Suspense and Offscreen — those components
defer work from one render into a later one. When the subtree continues
rendering, the stack from the previous render is no longer available.
But the memoized values on the dependencies list are. This requires a
bit more work when a consumer bails out, but nothing considerable, and
there are ways we could optimize it even further. Conceptually, this
model is really appealing, since it matches how our other features
"reactively" detect changes — `useMemo`, `useEffect`,
`getDerivedStateFromProps`, the built-in cache, and so on.

I also intentionally dropped support for
`unstable_calculateChangedBits`. We're planning to remove this API
anyway before the next major release, in favor of context selectors.
It's an unstable feature that we never advertised; I don't think it's
seen much adoption.

Co-Authored-By: Josh Story <jcs.gnoff@gmail.com>

* Propagate all contexts in single pass

Instead of propagating the tree once per changed context, we can check
all the contexts in a single propagation. This inverts the two loops so
that the faster loop (O(numberOfContexts)) is inside the more expensive
loop (O(numberOfFibers * avgContextDepsPerFiber)).

This adds a bit of overhead to the case where only a single context
changes because you have to unwrap the context from the array. I'm also
unsure if this will hurt cache locality.

Co-Authored-By: Josh Story <jcs.gnoff@gmail.com>

* Stop propagating at nearest dependency match

Because we now propagate all context providers in a single traversal, we
can defer context propagation to a subtree without losing information
about which context providers we're deferring — it's all of them.

Theoretically, this is a big optimization because it means we'll never
propagate to any tree that has work scheduled on it, nor will we ever
propagate the same tree twice.

There's an awkward case related to bailing out of the siblings of a
context consumer. Because those siblings don't bail out until after
they've already entered the begin phase, we have to do extra work to
make sure they don't unecessarily propagate context again. We could
avoid this by adding an earlier bailout for sibling nodes, something
we've discussed in the past. We should consider this during the next
refactor of the fiber tree structure.

Co-Authored-By: Josh Story <jcs.gnoff@gmail.com>

* Mark trees that need propagation in readContext

Instead of storing matched context consumers in a Set, we can mark
when a consumer receives an update inside `readContext`.

I hesistated to put anything in this function because it's such a hot
path, but so are bail outs. Fortunately, we only need to set this flag
once, the first time a context is read. So I think it's a reasonable
trade off.

In exchange, propagation is faster because we no longer need to
accumulate a Set of matched consumers, and fiber bailouts are faster
because we don't need to consult that Set. And the code is simpler.

Co-authored-by: Josh Story <jcs.gnoff@gmail.com>

---
## [HermitDreams/FFR-Spellcrafting](https://github.com/HermitDreams/FFR-Spellcrafting)@[e7407a16b8...](https://github.com/HermitDreams/FFR-Spellcrafting/commit/e7407a16b8edec59df2ffe2b6b548aee4f936e68)
#### Thursday 2022-03-24 17:03:16 by Linkshot

March 24th spell list uploaded (click for details)

(this is the raw unmodified output bc im tired)

CURE: Power: 16- Shape: Merging Stars, Colour: 10 (Bright Green), Message: 1 (HP up!)
OHM- Shape: Bar of Light, Colour: 3 (Dark Blue), Message: Defend lightning
INVS: Power: 30- Shape: Twinkling Bar, Colour: 3 (Dark Blue), Message: 3 (Easy to dodge)
SNAR: Acc Bonus: 48- Shape: Palm Blast, Colour: 10 (Bright Green), Message: 13 (Attack halted)
-
TRIK: Acc Bonus: 64- Shape: Palm Blast, Colour: 6 (Magenta), Message: 0; None
VEIL: Acc Bonus: 24- Shape: Palm Blast, Colour: 9 (Yellow), Message: 0; None
LIT: Power: 10, Acc Bonus: 16- Shape: Flaring Bolt, Colour: 3 (Dark Blue), Message: 0; None
SNOW: Power: 10, Acc Bonus: 24- Shape: Fizzling Flare, Colour: 13 (Bright Cyan), Message: 0; None
=
AICE- Shape: Twinkling Bar, Colour: 13 (Bright Cyan), Message: Defend cold
RUSE: Power: 60- Shape: Bar of Light, Colour: 3 (Dark Blue), Message: 3 (Easy to dodge)
HARM: Power: 30, Acc Bonus: 32- Shape: Flaring Bolt, Colour: 7 (Red), Message: 0; None
BEAM: Power: 16, Acc Bonus: 32- Shape: Flaring Bolt, Colour: 1 (White), Message: 0; None
-
BSRK- Shape: Bar of Light, Colour: 6 (Magenta), Message:18 (Quick Shot)
BANE: Acc Bonus: 24- Shape: Bursting Ball, Colour: 4 (Purple), Message: 77 (Poison smoke)
CRYO: Acc Bonus: 24- Shape: Energy Bolt, Colour: 13 (Bright Cyan), Message: 76 (Frozen)
SWAL: Acc Bonus: 32- Shape: Glowing Ball, Colour: 8 (Orange), Message: 22 (Fell into crack)
=
CUR2: Power: 33- Shape: Merging Stars, Colour: 12 (Pale Cyan), Message: 1 (HP up!)
JUG2: Power: 40, Acc Bonus: 40- Shape: Energy Bolt, Colour: 12 (Pale Cyan), Message: 0; None
HRM2: Power: 40, Acc Bonus: 32- Shape: Flaring Bolt, Colour: 12 (Pale Cyan), Message: 0; None[Light Axe]
HEAL: Power: 12- Shape: Stars, Colour: 10 (Bright Green), Message: 1 (HP up!)[Heal Helm/Staff]
-
CHOK: Acc Bonus: 32- Shape: Glowing Ball, Colour: 4 (Purple), Message: 77 (Poison smoke)
ICE2: Power: 30, Acc Bonus: 24- Shape: Energy Flare, Colour: 13 (Bright Cyan), Message: 0; None[Mage Staff]
LIT2: Power: 30, Acc Bonus: 24- Shape: Flaring Bolt, Colour: 3 (Dark Blue), Message: 0; None[Thor/Zeus]
LOK2: Power: 60, Acc Bonus: 107- Shape: Twinkles, Colour: 9 (Yellow), Message: 5 (Easy to hit)
=
PURE- Shape: Directed Burst, Colour: 10 (Bright Green), Message: 0; None
RUS2: Power: 80- Shape: Bar of Light, Colour: 3 (Dark Blue), Message: 3 (Easy to dodge)[Defense]
ANEC- Shape: Twinkling Bar, Colour: 14 (Grey), Message: Defend evil[White Shirt]
ABAN- Shape: Twinkling Bar, Colour: 4 (Purple), Message: Defend smoke
-
FAST- Shape: Bar of Light, Colour: 11 (Dark Green), Message: 18 (Quick shot)[Power Glove]
HOLD: Acc Bonus: 64- Shape: Palm Blast, Colour: 6 (Magenta), Message: 13 (Attack halted)
SPIN: Acc Bonus: 48- Shape: Palm Blast, Colour: 11 (Dark Green), Message: 0; None
FUM2: Power: 40, Acc Bonus: 40- Shape: Energy Flare, Colour: 4 (Purple), Message: 0; None
=
CUR3: Power: 66- Shape: Merging Stars, Colour: 13 (Bright Cyan), Message: 1 (HP up!)
LIFE- Shape: Directed Burst, Colour: 12 (Pale Cyan), Message: 74 (Ineffective now)
ATOX- Shape: Twinkling Bar, Colour: 4 (Purple), Message: Defend aging
HEL2: Power: 24- Shape: Stars, Colour: 12 (Pale Cyan), Message: 1 (HP up!)
-
MIST: Acc Bonus: 175- Shape: Twinkles, Colour: 1 (White), Message: 11 (Lost intelligence)[Bane Sword]
HID3: Power: 60- Shape: Bar of Light, Colour: 4 (Purple), Message: 3 (Easy to dodge)
WARP
MUFF: Acc Bonus: 107- Shape: Palm Blast, Colour: 6 (Magenta), Message: 0; None
=
SOFT- Shape: Directed Burst, Colour: 1 (White), Message: 74 (Ineffective now)
EXIT
JUG3: Power: 70, Acc Bonus: 64- Shape: Energy Bolt, Colour: 7 (Red), Message: 0; None
GRV3: Power: 120, Acc Bonus: 48- Shape: Twinkles, Colour: 11 (Dark Green), Message: 5 (Easy to hit)
-
HOWL: Acc Bonus: 64- Shape: Palm Blast, Colour: 13 (Bright Cyan), Message: 76 (Frozen)[Wizard Staff]
ICE3: Power: 60, Acc Bonus: 40- Shape: Energy Flare, Colour: 13 (Bright Cyan), Message: 0; None[Black Shirt]
POD3: Power: 75, Acc Bonus: 40- Shape: Energy Flare, Colour: 2 (Light Blue), Message: 0; None
RUB: Acc Bonus: 24- Shape: Glowing Ball, Colour: 14 (Grey), Message: 21 (Erased)
=
CUR4- Shape: Merging Stars, Colour: 3 (Dark Blue), Message: 24 (HP max!)
JUG4: Power: 80, Acc Bonus: 64- Shape: Energy Bolt, Colour: 12 (Pale Cyan), Message: 0; None
CLRa- Shape: Magic Burst, Colour: 5 (Pink), Message: 0; None
HEL3: Power: 48- Shape: Stars, Colour: 13 (Bright Cyan), Message: 1 (HP up!)
-
DIM: Acc Bonus: 48- Shape: Palm Blast, Colour: 6 (Magenta), Message: 0; None
FIR3: Power: 70, Acc Bonus: 40- Shape: Energy Flare, Colour: 7 (Red), Message: 0; None
LIT3: Power: 70, Acc Bonus: 40- Shape: Flaring Bolt, Colour: 3 (Dark Blue), Message: 0; None
GYS3: Power: 70, Acc Bonus: Auto-Hit- Shape: Fizzling Flare, Colour: 9 (Yellow), Message: 43 (Critical hit!!)
=
LIF2- Shape: Merging Stars, Colour: 5 (Pink), Message: 74 (Ineffective now)
VANQ: Power: 100, Acc Bonus: 107- Shape: Flaring Bolt, Colour: 7 (Red), Message: 0; None
GRO4: Power: 56, Acc Bonus: 48- Shape: Twinkles, Colour: 11 (Dark Green), Message: 15 (Became terrified)
FOG4: Power: 24- Shape: Twinkling Bar, Colour: 10 (Bright Green), Message: 2 (Armor up)
-
VOLT: Power: 100, Acc Bonus: 64- Shape: Flaring Bolt, Colour: 3 (Dark Blue), Message: 0; None
COVR: Acc Bonus: 64- Shape: Palm Blast, Colour: 9 (Yellow), Message: 0; None
WEAK: Power Word (Element: Status)- Shape: Sparkling Bolt, Colour: 6 (Magenta), Message: 0; None
NEG: Acc Bonus: 64- Shape: Twinkles, Colour: 3 (Dark Blue), Message: 29 (Defenseless)
=
Battle Messages
#01: HP up! [Assigned]
#02: Armor up [Assigned]
#03: Easy to dodge [Assigned]
#05: Easy to hit [Assigned]
#08: Defend lightning [Spaces to add: -2]
#10: Weapons stronger [Unassigned]
#11: Lost intelligence [Assigned]
#12: Defend cold
#13: Attack halted [Assigned]
#15: Became terrified [Assigned]
#16: Defend evil
#18: Quick shot [Assigned]
#21: Erased [Assigned]
#22: Fell into crack [Assigned]
#24: HP max! [Assigned]
#25: Defend bane
#27: Weapon became enchanted [Unassigned]
#28: Defend rot
#29: Defenseless [Assigned]
#30: Time stopped [Unassigned]
#31: Exile to 4th dimension [Unassigned]
#43: Critical hit!! [Assigned]
#47: Stopped [Unassigned]
#74: Ineffective now [Assigned]
#76: Frozen
#77: Poison smoke [Assigned]

---
## [cyberknight777/dragonheart_kernel_oneplus_sm8150](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150)@[c3767e4740...](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150/commit/c3767e47406c01e6efc932195e3a236d6a7c8171)
#### Thursday 2022-03-24 17:47:36 by Daniel Borkmann

bpf: fix subprog verifier bypass by div/mod by 0 exception

One of the ugly leftovers from the early eBPF days is that div/mod
operations based on registers have a hard-coded src_reg == 0 test
in the interpreter as well as in JIT code generators that would
return from the BPF program with exit code 0. This was basically
adopted from cBPF interpreter for historical reasons.

There are multiple reasons why this is very suboptimal and prone
to bugs. To name one: the return code mapping for such abnormal
program exit of 0 does not always match with a suitable program
type's exit code mapping. For example, '0' in tc means action 'ok'
where the packet gets passed further up the stack, which is just
undesirable for such cases (e.g. when implementing policy) and
also does not match with other program types.

While trying to work out an exception handling scheme, I also
noticed that programs crafted like the following will currently
pass the verifier:

  0: (bf) r6 = r1
  1: (85) call pc+8
  caller:
   R6=ctx(id=0,off=0,imm=0) R10=fp0,call_-1
  callee:
   frame1: R1=ctx(id=0,off=0,imm=0) R10=fp0,call_1
  10: (b4) (u32) r2 = (u32) 0
  11: (b4) (u32) r3 = (u32) 1
  12: (3c) (u32) r3 /= (u32) r2
  13: (61) r0 = *(u32 *)(r1 +76)
  14: (95) exit
  returning from callee:
   frame1: R0_w=pkt(id=0,off=0,r=0,imm=0)
           R1=ctx(id=0,off=0,imm=0) R2_w=inv0
           R3_w=inv(id=0,umax_value=4294967295,var_off=(0x0; 0xffffffff))
           R10=fp0,call_1
  to caller at 2:
   R0_w=pkt(id=0,off=0,r=0,imm=0) R6=ctx(id=0,off=0,imm=0)
   R10=fp0,call_-1

  from 14 to 2: R0=pkt(id=0,off=0,r=0,imm=0)
                R6=ctx(id=0,off=0,imm=0) R10=fp0,call_-1
  2: (bf) r1 = r6
  3: (61) r1 = *(u32 *)(r1 +80)
  4: (bf) r2 = r0
  5: (07) r2 += 8
  6: (2d) if r2 > r1 goto pc+1
   R0=pkt(id=0,off=0,r=8,imm=0) R1=pkt_end(id=0,off=0,imm=0)
   R2=pkt(id=0,off=8,r=8,imm=0) R6=ctx(id=0,off=0,imm=0)
   R10=fp0,call_-1
  7: (71) r0 = *(u8 *)(r0 +0)
  8: (b7) r0 = 1
  9: (95) exit

  from 6 to 8: safe
  processed 16 insns (limit 131072), stack depth 0+0

Basically what happens is that in the subprog we make use of a
div/mod by 0 exception and in the 'normal' subprog's exit path
we just return skb->data back to the main prog. This has the
implication that the verifier thinks we always get a pkt pointer
in R0 while we still have the implicit 'return 0' from the div
as an alternative unconditional return path earlier. Thus, R0
then contains 0, meaning back in the parent prog we get the
address range of [0x0, skb->data_end] as read and writeable.
Similar can be crafted with other pointer register types.

Since i) BPF_ABS/IND is not allowed in programs that contain
BPF to BPF calls (and generally it's also disadvised to use in
native eBPF context), ii) unknown opcodes don't return zero
anymore, iii) we don't return an exception code in dead branches,
the only last missing case affected and to fix is the div/mod
handling.

What we would really need is some infrastructure to propagate
exceptions all the way to the original prog unwinding the
current stack and returning that code to the caller of the
BPF program. In user space such exception handling for similar
runtimes is typically implemented with setjmp(3) and longjmp(3)
as one possibility which is not available in the kernel,
though (kgdb used to implement it in kernel long time ago). I
implemented a PoC exception handling mechanism into the BPF
interpreter with porting setjmp()/longjmp() into x86_64 and
adding a new internal BPF_ABRT opcode that can use a program
specific exception code for all exception cases we have (e.g.
div/mod by 0, unknown opcodes, etc). While this seems to work
in the constrained BPF environment (meaning, here, we don't
need to deal with state e.g. from memory allocations that we
would need to undo before going into exception state), it still
has various drawbacks: i) we would need to implement the
setjmp()/longjmp() for every arch supported in the kernel and
for x86_64, arm64, sparc64 JITs currently supporting calls,
ii) it has unconditional additional cost on main program
entry to store CPU register state in initial setjmp() call,
and we would need some way to pass the jmp_buf down into
___bpf_prog_run() for main prog and all subprogs, but also
storing on stack is not really nice (other option would be
per-cpu storage for this, but it also has the drawback that
we need to disable preemption for every BPF program types).
All in all this approach would add a lot of complexity.

Another poor-man's solution would be to have some sort of
additional shared register or scratch buffer to hold state
for exceptions, and test that after every call return to
chain returns and pass R0 all the way down to BPF prog caller.
This is also problematic in various ways: i) an additional
register doesn't map well into JITs, and some other scratch
space could only be on per-cpu storage, which, again has the
side-effect that this only works when we disable preemption,
or somewhere in the input context which is not available
everywhere either, and ii) this adds significant runtime
overhead by putting conditionals after each and every call,
as well as implementation complexity.

Yet another option is to teach verifier that div/mod can
return an integer, which however is also complex to implement
as verifier would need to walk such fake 'mov r0,<code>; exit;'
sequeuence and there would still be no guarantee for having
propagation of this further down to the BPF caller as proper
exception code. For parent prog, it is also is not distinguishable
from a normal return of a constant scalar value.

The approach taken here is a completely different one with
little complexity and no additional overhead involved in
that we make use of the fact that a div/mod by 0 is undefined
behavior. Instead of bailing out, we adapt the same behavior
as on some major archs like ARMv8 [0] into eBPF as well:
X div 0 results in 0, and X mod 0 results in X. aarch64 and
aarch32 ISA do not generate any traps or otherwise aborts
of program execution for unsigned divides. I verified this
also with a test program compiled by gcc and clang, and the
behavior matches with the spec. Going forward we adapt the
eBPF verifier to emit such rewrites once div/mod by register
was seen. cBPF is not touched and will keep existing 'return 0'
semantics. Given the options, it seems the most suitable from
all of them, also since major archs have similar schemes in
place. Given this is all in the realm of undefined behavior,
we still have the option to adapt if deemed necessary and
this way we would also have the option of more flexibility
from LLVM code generation side (which is then fully visible
to verifier). Thus, this patch i) fixes the panic seen in
above program and ii) doesn't bypass the verifier observations.

  [0] ARM Architecture Reference Manual, ARMv8 [ARM DDI 0487B.b]
      http://infocenter.arm.com/help/topic/com.arm.doc.ddi0487b.b/DDI0487B_b_armv8_arm.pdf
      1) aarch64 instruction set: section C3.4.7 and C6.2.279 (UDIV)
         "A division by zero results in a zero being written to
          the destination register, without any indication that
          the division by zero occurred."
      2) aarch32 instruction set: section F1.4.8 and F5.1.263 (UDIV)
         "For the SDIV and UDIV instructions, division by zero
          always returns a zero result."

Fixes: f4d7e40a5b71 ("bpf: introduce function calls (verification)")
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Acked-by: Alexei Starovoitov <ast@kernel.org>
Signed-off-by: Alexei Starovoitov <ast@kernel.org>
Signed-off-by: Danny Lin <danny@kdrag0n.dev>
Signed-off-by: utsavbalar1231 <utsavbalar1231@gmail.com>
Signed-off-by: UtsavBalar1231 <utsavbalar1231@gmail.com>
Signed-off-by: atndko <z1281552865@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[78af48a556...](https://github.com/mrakgr/The-Spiral-Language/commit/78af48a5567671663f9b14a5786f67a44fed7990)
#### Thursday 2022-03-24 18:46:59 by Marko Grdinić

"10:10am. I am up. Let me chill a bit and I will start.

10:30am. Let me start. If I start reading Yurushia's story I'll waste the whole morning. I slept well tonight, and am feeling rested right now. This is the opposite of yesterday. So I should do some modeling. Oh yeah, let me set the course to download.

10:35am. Let me drop the clipping mask. What I did with the floor was good. Even if the tiles themselves are repetitive, by slapping a non-repetitive pattern of scratches on top, you can get something better.

10:45am. Let me try a gradient ramp. I just can't the overall colors to match my own laminate. I tried reducing the contrast and increasing the saturation, but that still just makes it look bleached out.

Should there be something like the curves too for rgb. Blender had a thing where I could change the contrast directly using curves. I neeed something like that here.

> Error. Captcha expired. Try again in 1 hour.

Forgot to press download on RapidGator and got this. They are just messing with mehere here. No, I won't buy your shitty account.

10:55am. There is the remap node, but I can't figure out how to add extra points on the curve. Sloppy work by Isotropix.

Let me try the gradient ramp.

https://en.wikipedia.org/wiki/Shades_of_brown

I really need once and for all figure out what the standard brown is.

11:15am. I give up. I can't the floor to have the right feel no matter how much I mess with the contrast, saturation or ramps, The overall texture itself is not right, so messing with the globals just gives me the same pattern in the end.

Just forget about it.

I need to move on to the props.

Focus me, just load up Houdini and make the thing.

11:30am. Mhhhh, I knew this would be hard. Let me restart.

Also it seems that mirroing while doing the booleans is a bad idea. When I try to boolean an open mesh, I get outright cutting.

12:55pm. This sucks so bad. Trying to model this in Houdini is sucking the life out of me. For an object of this complexity it is not like I can afford to make it generic either.

I thought it would be easier in Houdini, but I should try to make in Blender as well for comparison.

1pm. The UI matters a great deal here. It is just so awkward to do this in Houdini

Let me stop here. Since this is my first time doing serious independent modeling, of course I am not going to be taking off like a rocket. Something like this is the best possible exercise I could make to level up my 3d skills at my current level of development.

I watched a lot of things, but I am severely lacking in practice. I need to do this smartly and refine my workflow. It won't take me too long to break into 3/5 if I can clear these hurdles.

2:40pm. Done with breakfast and chores. I really don't feel like it, a part of me just wants to drop all of this laze around around for the rest of my days. At this point, thanks to my accumulated programming ability, the easy route for me is definitely to take up programming for money. No need to learn new things or struggle that way.

But the reason why I got good at programming in the first place is due to endless struggle. It was not by taking the easy way.

Something like making a desk is not something that should be causing me consternation. A challenge like this should be done in under an hour easy for a skilled artist.

Obviously, Houdini is not what I should be using here. I can't be both quick and generic. I'd be much better served of being able to make quick prototypes. For texturing I should learn how to draw masks on which to later slap noise on.

Now focus me. Let me give it a try from start.

4:20pm. That was engrossing. I only have that cylinder at the bottom which acts as a leg placer.

I am looking at the objects and I see that in 3.1 Blender has Nurbs surfaces like Houdini. I haven't tried them out, but I am impressed by its pace of development. It really feels nice to work in a program that is as stable and snappy as it.

4:35pm. The bisect tool is really nice.

Now I'll be able to mirror the whole mesh cleanly. But...wasn't there an explicit symmetrize option?

4:50pm. Yeah, it works great. I should not have done that bisect as it left a cut in the middle. But it was easy to remove. Let me do the finishing touches.

Let me make the vertex groups for the bevels.

Ah, right. I can just use weights. For those which I want less bevel, I can just lower the strength.

5:55pm. Had to take a lunch break. The creases are giving me trouble. What is happening that other creases influence the maximum offset and there is a gap in one of the boards that is really close to the outer edge.

Right now I am exploring the ways to fine tune it properly. Maybe if I give the edges low weights it will work.

Honestly, it is cool that Blender has actual edge attributes. Houdini has points, primitives and vertices, but no edges which is annoying.

6pm. Focus me. I need to keep going forward. I am going to deal with this desk today. The modeling part is almost done, I just need to figure the beeveling and then texture it.

This last part is admittedly not easy as the top has some very unique wear patterns. I am not sure if it is worth to try to replicate it, if I do, it will probably take me a day or two of experimenting. But it could be worth it. I am studying texturing at this point in time. Now that I've established my basic modeling workflow, this pattern is probably the hardest part of the entire room.

Yeah, I really should replicate it. I mean, I myself am 12h a day in front of the computer, so it fairly important part of it as it is directly between me and the monitor.

6:50pm. I should have been more wary of ngons. Next time I'll avoid using them. I decided to redo the piece I was working on. I got quite into it.

Now let me finish beveling the rest of the piece.

7:15pm. Trying to remove the middle seam that happens due to symmetrizing can be troublesome. Just now disolve edges left vertices behind and ended up deleting faces for one object. Next time I'll just leave the seam there, it is not worth bothering with.

What I am looking at is pretty much my own desk. It is a really convincing 3d model. I do not know whether I messed it up somewhere, but it feels right when I look at it, so that if fine. Even if I got something wrong compared to the real life one, it is not like anybody will be raiding my room to check so who cares.

Yeah, this is the way to do it. I am going to have to assign a few shading groups to different parts and then export it as obj. Or maybe USD would be better, let me go with that. I have no reason to favor obj.

7:25pm. Right now I am thinking how I could make the texture. At first glance it reminded me of polynomials, but instead of that, why not make my reasoning's starting point a topological chart instead.

What I could do is make some fine anti aliased noise, quantize, edge detect. That will give me the eshes that I want. I could thicken the edges a bit, multiply that with some rougher noise and voila, I have my mask.

Alternatively, I do not even need quantization and edge detection. I could just use a ramp and whipsaw it between black and white to get the edges. I did the same thing for the ceiling patterns. I just need to push the idea further this time.

Yeah, that would be really good. I should use constant interpolations this time. The best part of this is that I could do it in Clarisse as well. No need to mess with CHOPs.

7:40pm. Let me close here. I'll put the plan into action tomorrow. Right now I don't feel like it anymore. A day's work is a day's work.

Tomorrow I am going to do the UV unwrapping and then texturing in Clarisse. After that I'll deal with the rest of the props.

When I've completed the room, I'll have achieved something significant."

---
## [Tomsod/elemental](https://github.com/Tomsod/elemental)@[f94c56dabf...](https://github.com/Tomsod/elemental/commit/f94c56dabf363ce134f76498bbea9f771a5b37be)
#### Thursday 2022-03-24 19:28:35 by Tomsod M

Rearrange some potions

Most of this commit's ideas are shamelessly stolen from BTB's mod
description, because, well, they're very good ideas.

First, swap green and blue potion effects.  This makes yellow reagents
more relevant in the early game, and makes SP harder to restore than HP,
which is justified by the Heal spell alone.  Also, for the same reason,
magic potions (now green) have lost their 10 SP bonus.

Second, make Stone to Flesh white, replacing Cure Paralysis, and the
latter is now an alternative effect of Recharge Item.  Reason: Divine
Restoration made a white-tier paralysis cure redundant, and an expert
spell equivalent is too weak for a black potion.

Instead, the new black potion (replacing StF) is Raise Dead, something
which alchemy really missed; this will hopefully make GM more enticing.

Lastly, I axed all stoning/paralysis cure spells from Red Dwarf Mines,
because this was bloody stupid game design, and players can now buy
their own StF potions in the nearby shop, anyway.  Instead there's ore.

---
## [influxdata/influxdb_iox](https://github.com/influxdata/influxdb_iox)@[55643945a1...](https://github.com/influxdata/influxdb_iox/commit/55643945a1a654d0db0bcc5eb0a42d7c3185efa9)
#### Thursday 2022-03-24 19:35:43 by Marco Neumann

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
## [gsteel/mezzio-laminasviewrenderer](https://github.com/gsteel/mezzio-laminasviewrenderer)@[601bc921b6...](https://github.com/gsteel/mezzio-laminasviewrenderer/commit/601bc921b64e54ab0d60f136d1df4935d5398383)
#### Thursday 2022-03-24 20:53:27 by Michał Bundyra

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
## [Cenrus/tgstation](https://github.com/Cenrus/tgstation)@[3bd5a2d8df...](https://github.com/Cenrus/tgstation/commit/3bd5a2d8df49213708540f1c0ffe0873b5d2e233)
#### Thursday 2022-03-24 21:34:09 by Wallem

Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

---
## [chrisboyle/sgtpuzzles](https://github.com/chrisboyle/sgtpuzzles)@[c0da615a93...](https://github.com/chrisboyle/sgtpuzzles/commit/c0da615a933a6676e2c6b957368067ca1bc10abd)
#### Thursday 2022-03-24 22:40:28 by Simon Tatham

Centralise initial clearing of the puzzle window.

I don't know how I've never thought of this before! Pretty much every
game in this collection has to have a mechanism for noticing when
game_redraw is called for the first time on a new drawstate, and if
so, start by covering the whole window with a filled rectangle of the
background colour. This is a pain for implementers, and also awkward
because the drawstate often has to _work out_ its own pixel size (or
else remember it from when its size method was called).

The backends all do that so that the frontends don't have to guarantee
anything about the initial window contents. But that's a silly
tradeoff to begin with (there are way more backends than frontends, so
this _adds_ work rather than saving it), and also, in this code base
there's a standard way to handle things you don't want to have to do
in every backend _or_ every frontend: do them just once in the midend!

So now that rectangle-drawing operation happens in midend_redraw, and
I've been able to remove it from almost every puzzle. (A couple of
puzzles have other approaches: Slant didn't have a rectangle-draw
because it handles even the game borders using its per-tile redraw
function, and Untangle clears the whole window on every redraw
_anyway_ because it would just be too confusing not to.)

In some cases I've also been able to remove the 'started' flag from
the drawstate. But in many cases that has to stay because it also
triggers drawing of static display furniture other than the
background.

---

