## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-17](docs/good-messages/2023/2023-05-17.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,052,275 were push events containing 3,446,251 commit messages that amount to 257,117,729 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 66 messages:


## [skiffos/linux](https://github.com/skiffos/linux)@[1bba82fe1a...](https://github.com/skiffos/linux/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Wednesday 2023-05-17 00:09:36 by Darrick J. Wong

xfs: fix negative array access in xfs_getbmap

In commit 8ee81ed581ff, Ye Bin complained about an ASSERT in the bmapx
code that trips if we encounter a delalloc extent after flushing the
pagecache to disk.  The ioctl code does not hold MMAPLOCK so it's
entirely possible that a racing write page fault can create a delalloc
extent after the file has been flushed.  The proposed solution was to
replace the assertion with an early return that avoids filling out the
bmap recordset with a delalloc entry if the caller didn't ask for it.

At the time, I recall thinking that the forward logic sounded ok, but
felt hesitant because I suspected that changing this code would cause
something /else/ to burst loose due to some other subtlety.

syzbot of course found that subtlety.  If all the extent mappings found
after the flush are delalloc mappings, we'll reach the end of the data
fork without ever incrementing bmv->bmv_entries.  This is new, since
before we'd have emitted the delalloc mappings even though the caller
didn't ask for them.  Once we reach the end, we'll try to set
BMV_OF_LAST on the -1st entry (because bmv_entries is zero) and go
corrupt something else in memory.  Yay.

I really dislike all these stupid patches that fiddle around with debug
code and break things that otherwise worked well enough.  Nobody was
complaining that calling XFS_IOC_BMAPX without BMV_IF_DELALLOC would
return BMV_OF_DELALLOC records, and now we've gone from "weird behavior
that nobody cared about" to "bad behavior that must be addressed
immediately".

Maybe I'll just ignore anything from Huawei from now on for my own sake.

Reported-by: syzbot+c103d3808a0de5faaf80@syzkaller.appspotmail.com
Link: https://lore.kernel.org/linux-xfs/20230412024907.GP360889@frogsfrogsfrogs/
Fixes: 8ee81ed581ff ("xfs: fix BUG_ON in xfs_getbmap()")
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Dave Chinner <david@fromorbit.com>

---
## [grorg/WebKit](https://github.com/grorg/WebKit)@[19f6ef6d7e...](https://github.com/grorg/WebKit/commit/19f6ef6d7e2b4cf59d285830e2fe9b50bb3de42c)
#### Wednesday 2023-05-17 00:15:52 by Dean Jackson

WebXR: Severe aliasing in WebXR experiences (with WebGL1 contexts)
https://bugs.webkit.org/show_bug.cgi?id=256861
rdar://109424254

Reviewed by NOBODY (OOPS!).

WebXR sessions using WebGL1 contexts are unable to turn on
multisampling. I'm pretty sure this was my fault, but I can't
remember if it was intentional or a mistake. Either way it is
a bug.

Fix this by implementing the multisample renderbuffer creation
and resolution steps. Since we're doing this on a WebGL1 context,
the normal API will be invalid (it requires GLES3), so call the
extension API instead. This means we need to expose some extra methods
on GraphicsContextGL.

Lastly, the framebuffer textures we get are SRGB8_ALPHA8 which
requires an extension to be enabled with a WebGL1 context.

* Source/WebCore/Modules/webxr/WebXROpaqueFramebuffer.cpp:
(WebCore::WebXROpaqueFramebuffer::endFrame): call blitFramebufferANGLE.
(WebCore::WebXROpaqueFramebuffer::setupFramebuffer): Implement logic for WebGL 1.
* Source/WebCore/platform/graphics/GraphicsContextGL.h:
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.cpp: Implement the extension API/
(WebCore::GraphicsContextGLANGLE::renderbufferStorageMultisampleANGLE):
(WebCore::GraphicsContextGLANGLE::blitFramebufferANGLE):
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.h:
* Source/WebCore/platform/graphics/cocoa/GraphicsContextGLCocoa.mm:
(WebCore::GraphicsContextGLCocoa::platformInitialize): Turn on the sRGB extension.
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGL.messages.in:
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGLFunctionsGenerated.h:
(renderbufferStorageMultisampleANGLE):
(blitFramebufferANGLE):
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxy.h:
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxyFunctionsGenerated.cpp:
(WebKit::RemoteGraphicsContextGLProxy::renderbufferStorageMultisampleANGLE):
(WebKit::RemoteGraphicsContextGLProxy::blitFramebufferANGLE):

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[725233b42b...](https://github.com/Zevotech/Shiptest/commit/725233b42b6f56551798a0a75b5362e577042de3)
#### Wednesday 2023-05-17 00:32:00 by thgvr

The Lizardening Part One (And Friends) (#1845)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR changes a lot of sprites. It's honestly too much. Namely:

- Explorer Equipment + Prototype
- Syndicate clothing
- Digitigrade lizard legs
- A new tail from Halcyon.
- Magboots from Zeta. Originally PR'd to tgstation.
- Colored (not greyscale! Ha Ha!) jumpsuits from Imaginos.

Heavy inspiration from the work of Imaginos, Halcyon, Mqiib, and
2cents#8442 for the original leg-work. (Haha, get it?)
The new digitigrade sprites started as a twinkle in the eye of Mqiib,
for yogstation(?) After myself and Halcyon saw those, an epihpany
struck. Perspective makes things cool and digitigrade perspective was
BAD.

I'll include a collage image of the new sprites if it's needed later.
Preview below:


![image](https://user-images.githubusercontent.com/81882910/228710332-0a213f88-5a8b-4b41-abdd-cee3b70ec403.png)
## Why It's Good For The Game
lizard,
Death of Codersprites
## Changelog

:cl:
add: New Digitigrade lizard sprites.
add: Various syndicate and mining clothing resprites.
add: Sarathi can now have an incredibly large tail.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[1c039c0623...](https://github.com/Zevotech/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Wednesday 2023-05-17 00:32:00 by Sun-Soaked

Botany Balance Pass (#1783)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
First came the content, now comes the hammer.

- Nukes Megaseed servitors from orbit. 
- Plants now age much, much slower and produce half as quickly.
Ruins that had them now have a ruined seed vendor that can be salvaged
for random seeds(and danger).
Ships that had one now have a crate with some thematic starting seeds,
and a Strange Seed.
Ghostrole Ruins that relied on having all seeds locally now have a
special biogenerator variant that can print a random seed for biomass.

- Adds Genesis Serum. This can be splashed on a tile to make natural
grass and some flora. Green your ship!
Genesis Serum was made a while ago, on request for a way to add natural
grass and flora to your ship. Since I had it lying around fully coded, I
thought I might as well pr it with botany changes.

- Gatfruit found in the seed vault have been replaced with Strange
Seeds.

- The chance to get Gatfruit from a demonic portal(plant variety) has
dropped from 15% to 5%.

- Corpse flowers now have liquid gibs and formaldehyde again. 

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Okay, hear me out

With this and Gardens, botany ships go from a "sit in your vessel for 2
hours" experience to an "explore and forage" one that better fits our
feature arc. It goes without saying that this **shouldn't be merged till
Overmap 4.2 is**, since it facilitates getting seeds from planets as
part of exploration.

Gatfruit are funny, but it takes exactly one seed getting into the hands
of a ship with a dna manipulator and the weapon balance is eradicated
from the game completely(for the round, at least.)
This is more problematic here then it was on TG, since our rounds tend
to be 5 hours long rather then 1.
This has been long coming. I'll reverse this if we ever get that
Plantlock variant we wanted a while ago.

Corpse flowers even have formaldehyde and gibs on tg, not sure what
happened there.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: 
add: Ruined megaseed servitors can now be found on the frontier,
carrying a bounty of seeds for intrepid adventurers.
balance: the time it takes for plants to reach a lethal age has been
increased massively.
balance: Plant production time increased a bit to compensate.
balance: megaseed servitors have been removed from ships and ruins.
Ships that carried one now have a crate with some starting seeds.
balance: removes gatfruit from the seed vault pool.
balance: reduces the chance of getting gatfruit from a plant-themed
demonic portal significantly.
balance: corpse flowers once again have formaldehyde and liquid gibs.
add: Adds Genesis Serum, a reagent that transforms tiles into natural
grass on splash, then causes some natural flora objects to grow. Turn
your ship green!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[33961776ce...](https://github.com/Zergspower/Skyrat-tg/commit/33961776ceb3e93db4b94b1f48a4fa7d3d7ff19c)
#### Wednesday 2023-05-17 00:33:30 by SkyratBot

[MIRROR] Wintercoats can now be zipped and unzipped through alt-click and separates the hood sprites from the jacket sprites [MDB IGNORE] (#20718)

* Wintercoats can now be zipped and unzipped through alt-click and separates the hood sprites from the jacket sprites (#74886)

## About The Pull Request
The title says it all, really.

~~Initially, I was only going to do it for all wintercoats, but then I
figured I might as well bring it down to all of `/hooded`, just so other
suits could benefit from it, since that behavior came from there anyway.
Does that mean that it does nothing for some of them? Yes, it does. Does
that justify having another variable to tell whether or not that should
be possible? In my humble opinion, not really, but I'm not against it if
it's requested.~~

~~That functionality was intentionally removed from the Void Cloak, as
there would be balance implications (since bringing up the hood makes
the whole cloak invisible, which you could skirt by just "zipping" it,
which also makes it invisible.~~

~~The sprites were already there, so this change was very simple to do.
Simply unties the zipped up look from the fact that the hood is up.
However, toggling the hood forces the zipping/unzipping, just so there's
no balance implications involved. It's just simpler that way.~~

So, I ended up going back and changing the sprites so that the hoods
would no longer be baked into the jacket's sprites, so that they could
be done as overlays instead, which ended up solving my problem with
hoods not being there on zipped-up versions.

For now, it's been made on winter coats only, but it shouldn't be that
difficult to bring it back down to the `/hooded` level. I just didn't
want to bother touching up the sprites down there, as it already took me
like 2-3 hours touching up the sprites of the winter coats alone.

I also took the decision to make it so EVA winter coats used the regular
winter coat's sprites, because they had special ones that just looked
like worse versions of the original, without anything special going on
for them. It was just a straight downgrade compared to the base sprite,
in my opinion.

There's still issues with the custom winter coat, in that the hood isn't
made into an overlay for it yet (and that'll require an extra bit of
logic to make it work, too), but it was already an issue before, the
hood is always present on the current version of the custom winter coat.

There's still a handful (sadly, most) of the winter coats that don't
properly reflect on their obj sprites when they're opened versus when
they're closed, but that's due to an initial spriter oversight, and not
to my doing. The open versions were just left as closed on many of them,
and I simply don't have the patience nor the appropriate skills to edit
that many coats that way.

## Why It's Good For The Game
Now you can be stylish with or without the hoodie!

![image](https://user-images.githubusercontent.com/58045821/233544697-cc821c3a-d965-4d96-af44-c44ff866496f.png)

![image](https://user-images.githubusercontent.com/58045821/233544711-da956b6b-44c4-4903-a34f-4d2890abc781.png)

![image](https://user-images.githubusercontent.com/58045821/233544717-b5221b04-0e6d-4931-83d0-d56fdac60ec3.png)

According to ChatGPT, with one small tweak (thanks Opera GX for the
suggestion):

> Zipped and unzipped through alt-click, winter coats can now be. Hmm,
stylishly warm, you shall be. Feel like a Spaceman, you will. Use the
Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.

## Changelog

:cl: GoldenAlpharex, ChatGPT for the first changelog entry (slightly
edited)
qol: Zipped and unzipped through alt-click, winter coats can now be.
Hmm, stylishly warm, you shall be. Feel like a Spaceman, you will. Use
the Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.
image: Winter coats no longer have their hood baked into their jacket's
sprite, both in item form and when worn.
fix: Updated the Icebox EVA winter coats (the Endotherm winter coats) to
use the same sprites as the regular winter coats.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Wintercoats can now be zipped and unzipped through alt-click and separates the hood sprites from the jacket sprites

* update modular wintercoat.dmi

* forgot

---------

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>
Co-authored-by: ghost sheep <sheepwiththemask@gmail.com>

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[74dc72b867...](https://github.com/Zergspower/Skyrat-tg/commit/74dc72b867c1b841c71ec1dedcacff8a64167253)
#### Wednesday 2023-05-17 00:33:30 by SkyratBot

[MIRROR] Config Flag to Save Generated Spritesheets to Logs [MDB IGNORE] (#20738)

* Config Flag to Save Generated Spritesheets to Logs (#74884)

## About The Pull Request

I was helping someone debug some weird bug with spritesheets a bit ago,
and I didn't like having to manually comment out all of the `fdel()`
stuff in order to help visualize what the potential issue might have
been with the spritesheets on either their DM-side generation or their
TGUI-level display. I decided to add a compile-time level flag that will
automatically copy over any generated spritesheet assets (css and pngs)
to the round-specific `data/logs` folder for analysis when a developer
should need it.

I also had to switch around some vars and make a few new ones to reduce
how copy-pasta it might get and ensure standardization/readability while
also being 0.001 times faster since we benefit from the string cache
(unprovable fact).
## Why It's Good For The Game

It's incredibly useful to see the actual flattened spritesheet itself
sometimes when you're doing this type of work and you keep getting odd
bugs here and there. Also saves headache from having to clear out the
temp `/data/spritesheets` folder every time you comment shit out, as
well as having an effective paper trail for A/B testing whatever
bullshit you've got going on.

![image](https://user-images.githubusercontent.com/34697715/233516033-1f5dde1a-e549-4e5a-aa99-0d531b34fbb5.png)
## Changelog
Doesn't affect players.

* Config Flag to Save Generated Spritesheets to Logs

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[6fd64b92ca...](https://github.com/ARF-SS13/coyote-bayou/commit/6fd64b92ca4cc80357d8d78c8efc1c6d8196204f)
#### Wednesday 2023-05-17 00:41:04 by Tk420634

Updating the Mansion a bit

Preparing my brain for making a non euclidian dungeon, because I fucking hate everything.

---
## [swbs-co/odoo](https://github.com/swbs-co/odoo)@[9e71094582...](https://github.com/swbs-co/odoo/commit/9e71094582ec4c9b719431e77538da8f91ffa9e3)
#### Wednesday 2023-05-17 01:00:25 by Xavier Morel

[FIX] core: handle recursion error when resolving stored fields

Issue discovered in the uninstall (and reinstall) of sale_project: a
dump has ~100 tasks, when reinstalling `sale_line_id` has to be
initialised, this is done by marking `sale_line_id` on all extant
tasks as to-recompute, which triggers their computation on the next
`flush`.

Because it's a recursive field, `Field.recompute` ensures only one
record at a time gets recomputed (as there could be cross-dependencies
in the recorset which protection would prevent from resolving).

As the field computation runs, it accesses itself, which triggers a
cache miss, which triggers a `_fetch_field` (to get the currently
stored value), this calls `_read`, which flushes the field we're
trying to read.

The problem here is that for efficiency the cache miss will look for
all records in the cache without a value for the
field (`_in_cache_without`) and try to `fetch` on them as well. This
means rather than not doing anything in flush, we're going to
`Field.recompute` on all records except the one selected the first
time around, which repeats the cycle until there is no more additional
record found in `_in_cache_without`, which could trigger the next
round of `recompute`, and the entire thing unwinds, and we probably
perform a ton of unnecessary additional `compute_value`.

Except that doesn't even happen, because the process from one compute
to the next takes 12~13 stack frames, which given the default
recursion limit of 1000 gives a hard limit of 76 fields before hitting
a RecursionError. As this is less than 100, a recursion error [is what
we get](https://runbot.odoo.com/runbot/build/31726625).

In 15.2, this was fixed by only expanding the fetch on non-recursive
fields, pessimizing recursive
fields (5c2511115b14299516fce4aa3737a62faaf5b653). Test-wise this only
impacted mail performances and in a relatively minor manner.

In 16.0, the mail tests actually match already (so that part was
skipped by the cherrypicking) however this impacts the knowledge perf
tests much more significantly e.g. `test_article_creation_multi_roots`
gets +9 queries when creating 10 top-level articles, which is a bit
much.

So use an alternative which is ugly as hell but which I didn't
consider for 15.2 (may want to backport it one day if the current fix
is an issue): catch the recursion error and use the existing
fallback (of fetching just the requested record's field without
expanding the recordset).

This likely makes for a pretty inefficient situation in the original
case as we're certainly going to hit the recursion limit repeatedly,
but that still fixes the issue, and it avoids deoptimising cases which
fall short of the recursion limit (resolving under 60 records or
so).

Plus despite creating giant stacks we might actually get good
efficiency as we're going to hit recursion limits repeatedly but
that's pure python, once we fall below the limit we can resolve
everything at once with a single SQL query (or something along those
lines).

Part-of: odoo/odoo#119808

---
## [sjp38/linux](https://github.com/sjp38/linux)@[2ed20bd7e3...](https://github.com/sjp38/linux/commit/2ed20bd7e3356591a7183a8af3579e0b2f9ecdf5)
#### Wednesday 2023-05-17 01:04:12 by Douglas Anderson

migrate_pages: avoid blocking for IO in MIGRATE_SYNC_LIGHT

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

---
## [katemonster33/Cataclysm-DDA](https://github.com/katemonster33/Cataclysm-DDA)@[a2dff5d423...](https://github.com/katemonster33/Cataclysm-DDA/commit/a2dff5d423b594ac6e6279e24a7348388e4e410a)
#### Wednesday 2023-05-17 01:15:44 by SolventMercury

Finished Zombie Proficiency & Weakpoint Review (#64194)

* Reviewed all Zombie Weakpoints & Proficiencies

# GENERAL TWEAKS
- Renamed Large Humanoids proficiency to Giant Humanoids, to clarify that it does not apply to somewhat large humanoids, like brutes, and only works on hulks and similar.
- Changed description of Natural Armors proficiency, as many enemies that used this proficiency had something more like a thick hide than any kind of shell.
- Renamed Natural Armor weakpoint set (wps_natural_armor) to wps_armored_hide, to better reflect its purpose and to avoid confusion with the unrelated Natural Armor proficiency, as well as to prevent its misapplication to monsters which have more of a carapace or plate armor thing going on. Natural Armors proficiency should be reserved for uniquely resilient armored foes, like kevlar zombies, whereas armored hide applies to anything with a particularly thick hide, even if not outrageously so.
# ZOMBIES
## ACID ZOMBIES
- Edited description of Corrosive Zombie to hint at its thick hide. Corrosive zombie now also trains Natural Armor proficiency.
- Spitter now has big head weakpoint set, based on description.
## AMALGAMATIONS (Their file is named like the zombie files so I put them here)
- All amalgamations now have intro_biology in their families. This should really be on any living creature of flesh and blood, with exceptions only for stuff like robots, physics-defying nether creatures, extra-dimensional anomalies, and the cafeteria meatloaf. I didn't add this to the cocoons because I wasn't sure if that made sense to do.
- Caustic amalgamation now trains biochemistry, like acid zombies do.
- Charged amalgamation now trains electromagnetics, like zapper zombies do.
## BURNED ZOMBIES
- Fixed a typo in the description for Zombie Kinderlings.
- Zombie Fiend now trains Ossified Exoskeletons. Thought I added that one earlier.
- Scorched Zombie now gets Armored Hide weakpoints due to its "leathery shell".
## FERROUS ZOMBIES
- Removed Armored Hides weakpoint set from rust shell zombie and plated zombie. Could possibly apply Ossified Exoskeletons to them, but I'm not sure.
## COMMAND ZOMBIES
- Slight description tweaks, typo fix.
## FUSED ZOMBIES
- Added proficiencies to Aberration and Dissoluted Devourer. Aberration doesn't give zombie bio because it isn't an actual zombie.
## LAB ZOMBIES
- Removed zombie bio from phase skulker, phase shrike, etc, as they aren't actually zombies.
- Gave phase shrike Ossified Exoskeletons proficiency.
## MISC ZOMBIES
- Added basic proficiencies to zombullfrog, frogmother, zombie nemesis, smoker
- Added basic weakpoints to smoker.
- Headless Horror trains giant humanoids proficiency, based on description.
- Removed Malicious Mane's natural armor training and body armor weakpoints, as it had no natural armor (or armor at all, for that matter).
## RADIATION ZOMBIES
- Added standard proficiencies and weakpoints to all of them.
## SOLDIER ZOMBIES
- Replaced body armor weakpoint set with armored hide.
- Removed military pilot's synthetic armor proficiency
## ANIMAL ZOMBIES
- Gave gastro bufo standard proficiencies and biochemistry.
## CLASSIC ZOMBIES
- Replaced beekeper's body armor weakpoints with armored hide weakpoints
## PUPATING ZOMBIES
- Added expected proficiencies and weakpoints to pupating hulks, as they were the only pupa zombies that didn't have a copy-from pointing to the base type, and did not include this information.
I noticed that most things that disappear on death - boomers, certain cocoons, etc. - tend not to have weakpoints or train proficiencies. Is this an oversight, or is this intentional? For now I left that as is.
## FLYING ZOMBIES
- Gave raptors standard and flying proficiencies.
- Electric raptor also teaches electromagnetics, like electric zombies.

* Removed my Personal Changelog from the Project Directory

* Fixed Fungal Wretch Typos

* Linted zed_amalgamations.json

* MANY Zombie Weakpoint Refinements (& Tests)

- Gave standard weakpoints to standard zombies - manually defined weakpoints for some of the basic zombie models (in zed_misc), like the zombie brute and zombie hulk, is a bit strange, since they have become some of the game's staple enemies. THIS WILL LIKELY EFFECT BALANCE, as these are not only important benchmark enemies, but also copy_from'd by quite a few other enemies. Basic brutes are now somewhat weaker depending on circumstances
- Updated ranged balance test to use enemies with a more uniform form factor, as the high volume of some benchmark enemies lead to counterintuitive results (higher armor enemy taking more damage because it's bigger and easier to shoot). Note that test differences in values aren't all actual "balance changes" but moreso changes to the test itself, so the comparison between old and new isn't 1:1. Test values were only updated on tests that failed for me (I ran the test with 10,000 cycles instead of the usual 200 to be sure the values I got were convergent).
- Added weakpoints and proficiency families to zombies I previously wasn't sure should receive them (mostly ones which self-destruct on death in some way, like boomers). This will make boomers significantly weaker, as they previously had no weakpoints whatsoever.
- Changed boomer stats so no boomer upgrade becomes smaller in volume or lighter in weight than the basic boomer.
- Added an upgrade path for Zombie Miners - they now have a chance to evolve into a shady zombie (most likely), a rust zombie, or just a normal tough zombie, with a ~70% chance not to evolve, on a half-life of 35.
- Rust shell zombies and rust plated zombies get a unique weakpoint category. Similar to bone armor, with the difference that weak points are quite a bit weaker, but the strong point is also a bit stronger.
- Flesh raptors finally have weakpoints, borrowing from the ones used for wasps.
- Removed NOHEAD flag from zombie military pilot, as it very much has a head and there's no reason to believe it to be structurally superfluous, and also fixed them being given erroneous armor weakpoints when they're just in fatigues.
- Lots of other minor weakpoint tweaks/fixes.

* Revert change to ranged tests that made it run 50 times as long.

* Update data/json/monsters/zed_amalgamation.json

Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>

* Update data/json/monsters/zed_children.json

Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>

* Update all Range Balance Values

* Reverted Weakpoint ID Change

---------

Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>

---
## [KingkumaArt/KingkumaTGSS13](https://github.com/KingkumaArt/KingkumaTGSS13)@[835952ccf4...](https://github.com/KingkumaArt/KingkumaTGSS13/commit/835952ccf42af58db7238a572d7df6a9b8b2afd7)
#### Wednesday 2023-05-17 01:24:05 by MrMelbert

Drunk slurring scales based on how drunk you are (#75459)

## About The Pull Request

The strength of the slurring effect drunkness applies on you now scales
based on how drunk you are.

Being "a little" drunk still changes your saymod, and makes you
occasionally slur your words...


![image](https://github.com/tgstation/tgstation/assets/51863163/1b21b359-a1f9-428a-8e10-d2028ac59728)

But being "a lot" drunk kicks it up to 11


![image](https://github.com/tgstation/tgstation/assets/51863163/9d593c80-75ff-4d02-8e7c-e48c738154bb)

Additionally, drunk slurring was separated into "generic slurring" and
"drunk slurring", the former which does not scale but less closely
resembles drunkness. Generic slurring is used in places such as
concussions, so this is an added bonus.

As a result of the split, I had to update mind restoration. Now it heals
all types of slurring, which does include cult slurs.

## Why It's Good For The Game

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

## Changelog

:cl: Melbert
add: When you are drunk, the strength of your slurring now varies based
on how drunk you are. Being "a little drunk" only rarely slurs your
words, being average drunk is the same as the old effect, while being
very drunk now slurs your words even more.
add: Some non-alcohol sources of slurring, such as concussions, now give
"generic slurring" rather than "drunk slurring", which less resemble
being drunk (ie, no burping).
add: Mind restoration now heals ALL slurring, rather than only drunk
slurring (which includes cult / heretic slurring).
/:cl:

---
## [MI439-CLO/android_frameworks_base](https://github.com/MI439-CLO/android_frameworks_base)@[7ecd1abb5d...](https://github.com/MI439-CLO/android_frameworks_base/commit/7ecd1abb5dbab5aef570010b148e7dcbb707ff04)
#### Wednesday 2023-05-17 01:25:15 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Jprimero15 <jprimero15@aospa.co>

---
## [jinxynii/coyote-bayou-goobery](https://github.com/jinxynii/coyote-bayou-goobery)@[856955c45a...](https://github.com/jinxynii/coyote-bayou-goobery/commit/856955c45acda58a4ebab15a67ce4d6e96280e4a)
#### Wednesday 2023-05-17 01:33:18 by Tk420634

Redlick & Garland City Take 2

Fuck you to, strong dmm

---
## [ProditorMagnus/Ageless-for-1-14](https://github.com/ProditorMagnus/Ageless-for-1-14)@[bb873e14a5...](https://github.com/ProditorMagnus/Ageless-for-1-14/commit/bb873e14a5ea2bdae7d2ca9af3537e9509e03f24)
#### Wednesday 2023-05-17 01:40:48 by ReynBolt

MiE - Vampire rebalance 2023 by IPS

Minor corrections and recheck after real long.

- Apprentice XP from 50 to 46
- Savant XP from 100 to 85 , price to 33g (-7g)

- Commander XP from 90 to 80 , price to 30g (-4g)
- Count XP from 180 to 110 , price to 55g (+7g)
- Prince price to 82g (+17g)
- Shadow Fighter XP from 80 to 75 , price to 28g (-4g)
- Night Warrior price to 52g (+8g)

- Blood Hunter price to 27g (-4g)
- Shadow Archer price to 29g (-2g)
- Night Angel price to 53g (+6g)

- Savage XP from 50 to 46
- Lunatic price to 32g (-2g)

- Winged XP from 46 to 42
- Wind Chaser HP to 43 (+2)
- Heaven Hunter fangs damage increase to 8-3 , HP to 54 (+3) , price to 54g (+8g)

---
## [openai/evals](https://github.com/openai/evals)@[b93700ab49...](https://github.com/openai/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Wednesday 2023-05-17 01:49:10 by DunedainStrider

Do math problems related to calculating dates using the Chinese Sexagenary Cycle method. 🧮 (#190)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Do math problems related to calculating dates using the Chinese
Sexagenary Cycle method

### Eval description

The Sexagenary Cycle combines 10 Heavenly Stems (Jia 甲, Yi 乙, Bing 丙,
Ding 丁, Wu 戊, Ji 己, Geng 庚, Xin 辛, Ren 壬, Gui 癸) and 12 Earthly Branches
(Zi 子, Chou 丑, Yin 寅, Mao 卯, Chen 辰, Si 巳, Wu 午, Wei 未, Shen 申, You 酉,
Xu 戌, Hai 亥) to form a 60-unit cycle. To calculate, convert the
Gregorian date to its corresponding Heavenly Stem and Earthly Branch
combination, used for marking specific years, months, and days.

### What makes this a useful eval?

The existing GPT models tend to make errors when performing calculations
related to the Sexagenary Cycle. To address this issue, we have provided
a specialized dataset aimed at improving the model's accuracy in
handling Sexagenary Cycle calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

[2023-03-16 12:46:51,594] [record.py:320] Final report: {'accuracy':
0.65}. Logged to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl
[2023-03-16 12:46:51,594] [oaieval.py:211] Final report:
[2023-03-16 12:46:51,594] [oaieval.py:213] accuracy: 0.65
[2023-03-16 12:46:51,597] [record.py:309] Logged 60 rows of events to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl:
insert_time=2.463ms

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"甲戌的次日是？"}], "ideal": "乙亥"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"乙亥的次日是？"}], "ideal": "丙子"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬寅的后日是？"}], "ideal": "甲辰"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"癸卯的后日是？"}], "ideal": "乙巳"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬子的后日是？"}], "ideal": "甲寅"}
  ```
</details>

---------

Co-authored-by: dunedainstrider <dunedainstrider@mac16>

---
## [openai/evals](https://github.com/openai/evals)@[aa71d43273...](https://github.com/openai/evals/commit/aa71d4327328933a463e972d662e6988234d0ef7)
#### Wednesday 2023-05-17 01:51:27 by Andrew Kondrich

Fix get_answer (#972)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2845c985fa...](https://github.com/tgstation/tgstation/commit/2845c985fab04b0de1f7615799a260527af30822)
#### Wednesday 2023-05-17 02:26:42 by Rhials

Adds a revolutionary conversion stinger (#75002)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds an antagonist gain stinger for Revolutionaries, created with
inspiration from the obsessed/traitor conversion sounds.


https://user-images.githubusercontent.com/28870487/235028674-170a4f9e-a873-4938-a700-536f005e539f.mp4

Raw audio:


https://cdn.discordapp.com/attachments/440978216484732934/1101964419203862548/revolutionary_tide.ogg

_A distant, hypnotic whistling. The heavy footfalls and clamoring voices
of an approaching crowd. The unstoppable revolutionary tide breaks its
waves upon an unsuspecting station._

I wanted to try and make something that felt like it fit in with the
other antagonist stingers we already have. Let me know what you think!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Gives a bit more flavor, and helps set the mood for the upcoming
bloodbath.

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
sound: Revolutionaries now have their own stinger that plays upon
becoming that antagonist.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Legacy-TacticalGamingInteractive/bnl-housing](https://github.com/Legacy-TacticalGamingInteractive/bnl-housing)@[92370b8ba9...](https://github.com/Legacy-TacticalGamingInteractive/bnl-housing/commit/92370b8ba91ac0e41bdf40b8bd4e7647be6a9520)
#### Wednesday 2023-05-17 03:15:42 by Legacy

Update README.md

Added much needed FAQ from the Discord to the README. As I was  trying to figure it out forever and wouldn't have known unless someone told me to look at FAQ specifically in the Discord. Because to me it wasn't a FAQ kinda question. But if it is, it should be here to save you the trouble to be honest.

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[28e53c240e...](https://github.com/Zonespace27/Skyrat-tg/commit/28e53c240e21902f73ee5b2a3221c01efcaa5908)
#### Wednesday 2023-05-17 03:28:05 by SkyratBot

[MIRROR] Tcomms Soundloop Comes From One Source And Is Less Awful [MDB IGNORE] (#20713)

* Tcomms Soundloop Comes From One Source And Is Less Awful (#74908)

## About The Pull Request

The ``soundloop/server`` now only comes from the server hub, so it
doesn't have stacking audio sources. The sound has been made more
uniform when up close, but is overall quieter. Additionally, all the
files have been run through a low pass filter to remove the highest of
it's pitches.
## Why It's Good For The Game

I'm sick of not wanting to be around telecomms because of how bad every
single machine sounds. Now, things are significantly easier on the ear,
quieter, more uniform, and better for everyone's sanity. I asked the
maintainers in the coding channel if I could just remove it and they
said no.

I can't get a video recording, I've tried with win+G, OBS, and sharex
and it's just fucked.
## Changelog
:cl:
qol: telecomms is quieter and less ear-damaging.
sound: modified tcomms sound to remove high-tones.
fix: the telecomms sound only comes from the server hub machine.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Tcomms Soundloop Comes From One Source And Is Less Awful

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[8164175aa2...](https://github.com/Zonespace27/Skyrat-tg/commit/8164175aa2b5c60555ad0a7f99f7ac6b5e90df99)
#### Wednesday 2023-05-17 03:28:05 by SkyratBot

[MIRROR] Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles [MDB IGNORE] (#20711)

* Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles (#74784)

## About The Pull Request

deers only show up in the BEPIS but i decided that they would be easy
enough to turn into a basic mob (they were). it was so easy in fact that
i decided to dip my toes into coding AI behavior, and made them freeze
up whenever they see a vehicle. this required a lot of code in a bunch
of places that i was quite unfamiliar with before starting this project,
so do let me know if i glonked up anywhere and i can work on smoothing
it out.
## Why It's Good For The Game

one less simple animal on the list. deers staring at headlights is
pretty cool i think, neato interaction for when you do get them beyond
the joke the bepis makes

i'm also amenable to dropping the whole "deer in headlights" code if you
don't like that for w/e reason- just wanted to make them basic at the
very least
## Changelog
:cl:
add: If you ever happen upon a wild deer, try not to ride your fancy
vehicles too close to it as it'll freeze up like a... you know where I'm
going with this.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[0410075cc8...](https://github.com/Latentish/Shiptest/commit/0410075cc811c5f65d7dc085a665c1ebb3a20e44)
#### Wednesday 2023-05-17 03:37:00 by meemofcourse

Ports mothroaches + Moth emotes (#1843)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Can you guess what this PR does? If you answered that it ports [this
pull request](https://github.com/tgstation/tgstation/pull/68763), [this
pull request](https://github.com/tgstation/tgstation/pull/71784), and [a
partial part of this one
too](https://github.com/BeeStation/BeeStation-Hornet/pull/7645/), then
you're right!

![imagen](https://user-images.githubusercontent.com/75212565/227387000-cc205158-286b-4841-9c5a-2e4d6d8d6200.png)

![imagen](https://user-images.githubusercontent.com/75212565/227386830-213997a1-ebe9-4573-8f8e-052e72bacea2.png)


You can also craft moth plushies now. You just need some cloth,
mothroach hide, and a heart!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

silly little moth roaches and emotes, who wouldn't want them in the
game?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Mothroaches are now a thing
add: Moth laughter, chittering and squeaking
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Bcadren/crawl](https://github.com/Bcadren/crawl)@[04090c9f6c...](https://github.com/Bcadren/crawl/commit/04090c9f6c4017c6f31d0f58033d31322fa4ca40)
#### Wednesday 2023-05-17 03:45:56 by Nicholas Feinberg

Replace potions of stabbing with attraction

Potions of stabbing didn't quite hit the mark as a design. They weren't
particularly popular with players, perhaps because their niche wasn't
just narrow but *extremely* narrow.

So, let's try another idea. Potions of attraction cause the player to
magically pull nearby monsters toward them while the duration lasts, a
bit like Mass Lesser Beckoning. (Greater Beckoning?). It currently pulls
3 tiles per turn, though I could see 2 tiles or full LOS also being
reasonable. The idea here is for melee characters to have something to
help them with ranged enemies, though quite situationally!

I also considered making this pull items, as a sort of very silly
apportation variant. Maybe it should?

Right now this doesn't wake up sleeping enemies, since it seemed fun
to have it help with stabs, too. If that's too strong, we can make it
more annoying (to enemies, waking them).

---
## [pexel5/CEV-Eris](https://github.com/pexel5/CEV-Eris)@[6f75cb9845...](https://github.com/pexel5/CEV-Eris/commit/6f75cb984594e66d49dff852532ac69a387899d7)
#### Wednesday 2023-05-17 04:55:33 by !Moltov!

Hotkey tweaks (#7956)

* yeah

* changes the hotkey list

* I forgot to push this

* Revert "I forgot to push this"

This reverts commit 845878d1bda9f8be1cee214acd7329b0355a507b.

* Revert "changes the hotkey list"

This reverts commit a1174c47bdc49245e4b31ddb06f85e7fec21e51c.

* re-adds reversions

* Revert "yeah"

This reverts commit e61f425a1231c6049c123724bfe88a7e51b9c199.

* manually adds hotkeys instead of using .dmf

I love the quirky dream maker language

---
## [iguessthislldo/OpenDDS](https://github.com/iguessthislldo/OpenDDS)@[8029f5acbc...](https://github.com/iguessthislldo/OpenDDS/commit/8029f5acbcf34349f860474d8a1fc67524fa4fa1)
#### Wednesday 2023-05-17 05:07:42 by Fred Hornsey

Generate News in Sphinx From Fragments

The current way of generating the news for releases mostly consists of
generating a spreadsheet of PRs, editing that, and creating the new
entries from that manually. More info on that process
[here](https://opendds.readthedocs.io/en/master/internal/release.html#update-files-in-the-repo-as-needed)
and [here](https://github.com/OpenDDS/OpenDDS/blob/f511b1f1582664ab7f49b3b012b968e684928aa2/tools/scripts/release_notes/README.md).
News entries can be directly committed in the PR where the change is
taking place, but doing that risks merge conflicts.

Overall this process is somewhat messy and limiting:

- Deciding what's newsworthy, what exactly to write, and reviewing the
  news is done all at once right before the release, sometimes months
  after the work was done. This makes it harder to remember what's
  newsworthy, what specific things needs to be pointed out to users, and
  what PRs should go together for single news item. This also means it
  takes more time to prepare the release and there's less time to spot
  and correct mistakes in the news or improve it.
- Most of the time the news item is left as just the title of PR. In the
  best case these might not need to be tweaked much or at all for
  changes that require little explanation. However this is certainly
  inadequate for explaining larger changes, for example like for [the
  XTypes fixes from PR4078](
  https://github.com/OpenDDS/OpenDDS/blob/f511b1f1582664ab7f49b3b012b968e684928aa2/NEWS.md?plain=1#L49).
  It'd be very awkward to write that much in a spreadsheet.
- It's hard to link to documentation. This is better than it was before
  with the PDF devguide, when it was impossible, but this could still be
  improved on more. Linking would give more context to users and could
  immediately give them details on use a new feature.
- Contributors outside the OpenDDS maintainers basically have no direct
  input on what the news says for changes they contribute. Honestly I'm
  not sure if any have wanted to, but they couldn't if they did.

The solution in this PR is committing the news of changes of a PR as a
file in that PR. At release these fragments of the news are
brought together automatically. There are still a few kinks to iron out,
but even if those are mostly unresolved I think this system will improve
the quaility of the news.

The system is inspired by [Python's blurb
tool](https://pypi.org/project/blurb/) and to a lesser extent tools like
[towncrier](https://towncrier.readthedocs.io/en/stable/index.html).
These tools are not bad, but they have some serious drawbacks. blurb is
specifically tailored for CPython development. For example, it's
oriented by GitHub issues, where as many of the changes we make are not
prompted by a GitHub issue. towncrier really expects the project to be a
Python project and has some quirks for some of use cases I was looking
for. Specifically needing multiple identical files for to attribute a
news item to multiple PRs and needing multiple files for a PR to have
different kinds of changes. Also both rely on the files having a
specific name, which seems unnecessary to me.

The following is the basics of adding a news fragment and how the news
is generated in this system:

Create a rst file in `docs/news.d/`. This is a news fragment. It can be
named anything as long as it doesn't have an leading underscore and is a
rst file, but it should be somewhat descriptive. Naming it the same as
the branch the change is on might be good idea. The change must be a rst
list. It has to have some rst-directive-like metadata around it. A
minimal file looks like this:

``` rst
.. news-prs: 5000
.. news-push: Additions
- This is an addition we made.
.. news-pop
```

Additional PRs are added by appending them to end of the `news-prs`
line. Additional `news-push`s and `news-pop`s can be used to add list
items to other sections, like fixes, or to create nested sections for
groups of changes like like "XTypes" or "RTPS". All sections will be
merged together in the final result. These sections and items are sorted
first by a quality called rank, then by the PR numbers in reverse order
(basically chronological). The rank is changed by `.. news-rand:
RANK_NUMBER`. It can be used to headline an important change or set of
changes,

See `docs/news.d/_example.rst` for a longer example. I also have added a
recreation of the 3.24.0 news as fragments as a test and a full example
of what this would look like.

Before release a preview of the news entry will always be available in
the built version of `docs/news.rst`. The means news added in an PR can
be previewed in the PR. During a release the fragments are permanently
committed to that file and the fragment files in `docs/news.d` are
removed.

Here are the two main issues I see with this system right now:

- To do a PR with a news fragment in one commit, you basically have to
  know what the PR number is going to be before hand. Otherwise another
  commit is needed to add the PR number. The PR number could technically
  be manually added after the PR is merged, but I would consider that
  poor practice. One solution could be a placeholder in `news-pr`
  statement that an action automatically replaces with the PR number
  after the PR is merged.
- How does this relate/integrate with `NEWS.md` and the GitHub release
  notes? I'm honestly a little stumped by this and unlike the other
  issue this needs to be figured out before this can be merged.
  - Something like pandoc could be used to convert the rst, but it would
    still need some manual intervention based on tests I did with the
    3.24.0 news.
  - The markdown version could just be a summarized version of the news,
    mostly consisting of highlights. This could be manually done or done
    with pandoc with human intervention. Also this summery could be what
    goes out in a prerelease announcement on social media.
  - The `NEWS.md` file could be also be done away with to simplify
    things. If that's the case, shuold news.rst live in the root
    directory and be called `NEWS.rst`? Is that going to case problems to
    try to include it in Shpinx?
  - The GitHub release notes could just link to `news.rst`, but I feel
    like they probably should at least have a summery.

Besides that there are some more things I needs to do, specifically:

- Document either in the documentation guidlines or dev guidelines how
  to add to the news.
- Improve release entries, it needs the release date and output could be
  tweaked.
- Maybe add two smaller examples just for "Additions" and "Fixes"
  without comments that are eaiser to use as templates.
- Before merge, remove 3.24.0 fragments, add any newer releases, and add
  any news fragments for a pending release.

---
## [Detective-Google/Skyrat-tg](https://github.com/Detective-Google/Skyrat-tg)@[f4aee43e79...](https://github.com/Detective-Google/Skyrat-tg/commit/f4aee43e793237e0dd93c42761043ce824e84237)
#### Wednesday 2023-05-17 05:37:16 by SkyratBot

[MIRROR] Tones down the power of nitrous oxide, the reagent. Makes heparin a bit harder to fix to compensate [MDB IGNORE] (#20610)

* Tones down the power of nitrous oxide, the reagent. Makes heparin a bit harder to fix to compensate (#74703)

## About The Pull Request

Nitrous Oxide, rather than directly subtracting blood volume per tick,
instead applies the anticoagulant trait ''TRAIT_BLOODY_MESS''. It shares
this with heparin.

However, unlike, heparin, coagulants like Sanguirite will remove the
trait and allow for continued clotting while the reagent is present,
neutering the nitrous oxide's anticoagulant effects (but not the other
parts)

Heparin, on the other hand, will purge Sanguirite while it is in you
system. You must remove the heparin before you can apply an
anticoagulant.

## Why It's Good For The Game

Nitrous Oxide, on top of being a knockout chem that causes you to
suffocate and become drowsy, just starts deleting blood rapidly. About
15 units of it, standard in a syringe, will kill you in about a minute,
but you'll be unconscious for most of it (you'll be at around 50%-60%
blood by the time it is out of your system, so as good as dead). It
doesn't matter that it metabolizes quickly either, since because it
isn't a toxin, it doesn't get purged by livers/improved livers, so you
will probably metabolize all of the chem that enters your system.

Blood is one of those 'hidden damage types', a bit like brain damage.
Once you start losing it _directly,_ you probably don't have a lot of
options to resolve it (unlike a bleed, which you do in various manners),
and the means of causing blood loss has been mostly pretty well
controlled as of late. Heparin directly interacts with wounds as a good
example.

Blood loss is also tied into oxyloss, which is another very mean damage
type in that it causes you to fall into unconsciousness at 50 damage, so
significantly more lethal than normal damage, kept in check by the fact
that breathing restores some of it. Nitrous oxide, you might note,
causes you to stop breathing.

It's cheaper to make than either heparin or lexorin, and since it isn't
a toxin like those chems, it is able to circumvent a few game mechanics
to simply just start killing you. It does the work of chloral hydrate,
lexorin and heparin while it has a remarkably easy recipe.

Following the example of how lexorin was pulled into line, and
consistency with heparin, I've made nitrous oxide an anticoagulant that
may or may not come into play as one. I think this is more up to date
with the state of toxins and chem warefare as a whole, and works with
the relative ease in making nitrous oxide. And it has been this way for
about 5 years, before we got wounds.

(did I mention that nitrous oxide is also an explosive if it gets hot
enough?)

## TL;DR

I think a chem with a pretty basic recipe shouldn't be doing the work of
5 other, more complicated, chemicals while also not being a toxin and
also not interacting with the wounds system or purity system whatsoever.
And being an explosive.

## Changelog
:cl:
balance: Nitrous oxide, the reagent, increases bleed rate from wounds
rather than directly subtracting blood. It can be counteracted using
coagulants (such as those in epipens).
balance: Heparin purges coagulants. You have to remove heparin from
someone's system before you can use coagulants.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Tones down the power of nitrous oxide, the reagent. Makes heparin a bit harder to fix to compensate

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [brandonperfetti/bp-spotlight](https://github.com/brandonperfetti/bp-spotlight)@[ab25265d0a...](https://github.com/brandonperfetti/bp-spotlight/commit/ab25265d0a3d151e096f626653b7a0786ade57cc)
#### Wednesday 2023-05-17 05:39:23 by brandonperfeti

🔧 chore(next.config.mjs): add remotePatterns to images configuration and add ts and tsx to pageExtensions
✨ feat(Card.tsx): add Card component with subcomponents Link, Title, Description, Cta, and Eyebrow
🔧 chore(Header.jsx): remove unused import and move avatarImage to a variable
🔧 chore(SimpleLayout.tsx): add margin bottom to Container component
🔧 chore(useClickOutside.tsx): refactor useClickOutside hook to use a single listener function
✨ feat(ArrowDownIcon.tsx): add ArrowDownIcon component
✨ feat(BriefcaseIcon.tsx): add BriefcaseIcon component
✨ feat(ChevronRightIcon.tsx): add ChevronRightIcon component
The changes include adding support for remotePatterns in the images configuration in next.config.mjs, adding a Card component with subcomponents Link, Title, Description, Cta, and Ey

✨ feat: add LinkIcon and MailIcon components
🗑️ chore: remove unused image files and _app.jsx file
🚚 chore: rename _app.jsx to _app.tsx and update its implementation to use TypeScript
🚚 chore: rename _document.jsx to _document.tsx and update its implementation to use TypeScript
The commit adds two new components, LinkIcon and MailIcon, which can be used throughout the application. It also removes unused image files and the _app.jsx file, which is replaced with a TypeScript implementation in _app.tsx. Similarly, _document.jsx is replaced with a TypeScript implementation in _document.tsx.

🎨 style(about.tsx): format code to improve readability
✨ feat(about.tsx): add About page with personal and professional information
The About page includes personal and professional information about the author, including his career journey, skillset, and solutions he can provide. The page also includes links to the author's social media profiles and email address. The code has been formatted to improve readability.

🐛 fix(index.jsx): replace img tag with Next.js Image component
The img tag has been replaced with the Next.js Image component to improve performance and accessibility.

✨ feat(hermes.tsx): add Hermes chat page with Open AI chat
The Hermes chat page includes an Open AI chat component that can help users with anything.

🎨 style(index.jsx): replace image imports with Image component and add height and width attributes
🎨 style(index.jsx): replace custom icons with imported icons
🚀 feat(projects.tsx): add Projects page with project cards
The changes in index.jsx improve the performance of the page by using the Next.js Image component instead of importing images directly. The imported icons improve the consistency of the icons used throughout the application. The new Projects page displays a list of projects with their logos, descriptions, and links. This page allows visitors to see the projects that the author has worked on and provides links to view them.

✨ feat(tech.tsx): add Tech Stack page to showcase the technologies used in projects
This commit adds a new page called Tech Stack that showcases the technologies used in projects. The page displays a list of technologies along with their logos, descriptions, and links to their respective websites. The page is designed to give visitors an idea of the technologies I am familiar with and have experience using.

✨ feat(thank-you.tsx): convert thank-you page from jsx to tsx
🚀 feat(uses.tsx): add new page for "Uses" with a list of tools and resources used by the author
The thank-you page was converted from jsx to tsx to improve type safety and maintainability. The new "Uses" page was added to list the tools and resources used by the author for development, design, and productivity. The page is divided into sections with each section containing a list of tools and a brief description of why they are used.

---
## [eworm-de/git](https://github.com/eworm-de/git)@[07f91e5e79...](https://github.com/eworm-de/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Wednesday 2023-05-17 07:03:37 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [brauner/linux](https://github.com/brauner/linux)@[12dc16f8fd...](https://github.com/brauner/linux/commit/12dc16f8fd22aeba20a3c17df17a92f9f1c5ada2)
#### Wednesday 2023-05-17 07:14:59 by Vladimir Sementsov-Ogievskiy

coredump: require O_WRONLY instead of O_RDWR

The motivation for this patch has been to enable using a stricter
apparmor profile to prevent programs from reading any coredump in the
system.

However, this became something else. The following details are based on
Christian's and Linus' archeology into the history of the number "2" in
the coredump handling code.

To make sure we're not accidently introducing some subtle behavioral
change into the coredump code we set out on a voyage into the depths of
history.git to figure out why this was O_RDWR in the first place.

Coredump handling was introduced over 30 years ago in commit
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)").
The original code used O_WRONLY:

    open_namei("core",O_CREAT | O_WRONLY | O_TRUNC,0600,&inode,NULL)

However, this changed in 1993 and starting with commit
9cb9f18b5d26 ("[PATCH] Linux-0.99.10 (June 7, 1993)") the coredump code
suddenly used the constant "2":

    open_namei("core",O_CREAT | 2 | O_TRUNC,0600,&inode,NULL)

This was curious as in the same commit the kernel switched from
constants to proper defines in other places such as KERNEL_DS and
USER_DS and O_RDWR did already exist.

So why was "2" used? It turns out that open_namei() - an early version
of what later turned into filp_open() - didn't accept O_RDWR.

A semantic quirk of the open() uapi is the definition of the O_RDONLY
flag. It would seem natural to define:

    #define O_RDWR (O_RDONLY | O_WRONLY)

but that isn't possible because:

    #define O_RDONLY 0

This makes O_RDONLY effectively meaningless when passed to the kernel.
In other words, there has never been a way - until O_PATH at least - to
open a file without any permission; O_RDONLY was always implied on the
uapi side while the kernel does in fact allow opening files without
permissions.

The trouble comes when trying to map the uapi flags onto the
corresponding file mode flags FMODE_{READ,WRITE}. This mapping still
happens today and is causing issues to this day (We ran into this
during additions for openat2() for example.).

So the special value "3" was used to indicate that the file was opened
for special access:

    f->f_flags = flag = flags;
    f->f_mode = (flag+1) & O_ACCMODE;
    if (f->f_mode)
            flag++;

This allowed the file mode to be set to FMODE_READ | FMODE_WRITE mapping
the O_{RDONLY,WRONLY,RDWR} flags into the FMODE_{READ,WRITE} flags. The
special access then required read-write permissions and 0 was used to
access symlinks.

But back when ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") added
coredump handling open_namei() took the FMODE_{READ,WRITE} flags as an
argument. So the coredump handling introduced in
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") was buggy because
O_WRONLY shouldn't have been passed. Since O_WRONLY is 1 but
open_namei() took FMODE_{READ,WRITE} it was passed FMODE_READ on
accident.

So 9cb9f18b5d26 ("[PATCH] Linux-0.99.10 (June 7, 1993)") was a bugfix
for this and the 2 didn't really mean O_RDWR, it meant FMODE_WRITE which
was correct.

The clue is that FMODE_{READ,WRITE} didn't exist yet and thus a raw "2"
value was passed.

Fast forward 5 years when around 2.2.4pre4 (February 16, 1999) this code
was changed to:

    -       dentry = open_namei(corefile,O_CREAT | 2 | O_TRUNC | O_NOFOLLOW, 0600);
    ...
    +       file = filp_open(corefile,O_CREAT | 2 | O_TRUNC | O_NOFOLLOW, 0600);

At this point the raw "2" should have become O_WRONLY again as
filp_open() didn't take FMODE_{READ,WRITE} but O_{RDONLY,WRONLY,RDWR}.

Another 17 years later, the code was changed again cementing the mistake
and making it almost impossible to detect when commit
378c6520e7d2 ("fs/coredump: prevent fsuid=0 dumps into user-controlled directories")
replaced the raw "2" with O_RDWR.

And now, here we are with this patch that sent us on a quest to answer
the big questions in life such as "Why are coredump files opened with
O_RDWR?" and "Is it safe to just use O_WRONLY?".

So with this commit we're reintroducing O_WRONLY again and bringing this
code back to its original state when it was first introduced in commit
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") over 30 years ago.

Signed-off-by: Vladimir Sementsov-Ogievskiy <vsementsov@yandex-team.ru>
Message-Id: <20230420120409.602576-1-vsementsov@yandex-team.ru>
[brauner@kernel.org: completely rewritten commit message]
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Christian Brauner <brauner@kernel.org>

---
## [Aliya-Daire/Introduction-to-Programming-in-C-Projects](https://github.com/Aliya-Daire/Introduction-to-Programming-in-C-Projects)@[db28365b0e...](https://github.com/Aliya-Daire/Introduction-to-Programming-in-C-Projects/commit/db28365b0eee861d051c367c5d3bdfa4c3472430)
#### Wednesday 2023-05-17 07:44:54 by Aliya Daire

PR3 Maze Solver

2. Introduction and Background
Introduction

Solving a Maze

In this programming assignment you will write a program to read a given maze (provided as text “art”) and find the shortest path from start to finish. Mazes go back to antiquity and the story of the minotaur. However, Theseus didn’t have Google Maps.
You will implement breadth-first search, a simple algorithm that finds not just any path to the exit in a maze, but actually finds a shortest path from the start to the finish. This algorithm was described in the late 1950s, making it one of the earliest nontrivial algorithms to follow the creation of the electronic computer.
In this assignment you will practice the following skills:
Dynamic memory allocation of arrays and 2D arrays.
Using structs and classes .
Implementation of a simple queue data structure.
Implementing the breadth-first search (BFS) algorithm.
A Piece of Advice!
We suggest you read through the entire description before beginning the assignment.
Maze Input Format

Your program will receive the input file from a command line argument.
Below shows an example of passing in a maze input file called “maze1.in” to our maze program using a command line argument.
./maze maze1.in
The input file is structured as follows:

The first line of the file should contain two integer numbers indicating the row and column size of the maze. The number of rows indicated will determine how many lines of text follow (1 row per line).
On each line will be one character for each of the indicated number of columns followed by a newline character. The characters can be a period . indicating a space in the maze, a # sign indicating a wall in the maze, a capital S indicating the start location for your search, or a capital F for the desired finish location. You can’t go outside the grid. (i.e., you may imagine that lava surrounds the maze perimeter.)
In general the format of the maze is:
rows cols
[row 1: cols many characters]
[row 2: cols many characters]
...
[row rows: cols many characters]
and the possible characters are:
Character	Meaning
.	Empty space
#	Wall
S	Start location
F	Finish location
We provide you with 4 mazes: maze[1-4].in and maze1.in is shown as an example on the left. You can also find some interesting mazes in a directory called testcases.
Maze Output Format

Your search algorithm will find a shortest path from the start cell to the finish. It will indicate this path by filling in the character locations on the path with asterisks *; then, it will write the resulting character maze to cout (standard output).
Note: We could have chosen to output the results to a file to practice with ofstream objects, but because they behave nearly the same as cout, we chose the simpler cout approach so you can focus on the really learning tasks of allocating the 2D array(s) and implementing the BFS algorithm.
The correct output for maze1.in (below) is shown on the left (maze1.sol).
maze1.in
5 5
.S.#. 
##.#.
.....
.####
....F
maze1.sol (this is the content that cout should produce)
5 5
.S*#. 
##*#.
***..
*####
****F
However,
If no path exists, your program should output
No path could be found!
If the user gives an invalid maze (more than one start or finish point), your program should output
Invalid maze.
If the input maze contains characters other than those shown above, then your program should output
Error, input format incorrect.
BFS

Breadth First Search is a general technique with many uses including flood fill, shortest paths, and meet-in-the-middle search. The idea is to explore every possible valid location, beginning at the start location, using an ordering so that we always explore ALL close locations (i.e. those at a shorter distance from the start) before exploring any location at a further (longer) distance from the start.
In other words, first we “explore” the start, then all locations at distance 1 from the start (one at a time), then all locations at distance 2 from the start (one at a time), etc, in that order.
This property ensures that when we do find the finish cell (if one exists), we will arrive there via a shortest-length path. Of course, as we search we mark cells (as explored) that we’ve visited so that we don’t visit them again and cause an infinite cycle of exploration!
Ensuring the BFS propety

To ensure we explore all closer locations before further locations, we keep a queue of locations in the maze. A queue has the property that the first item added is the first to be removed (first-in, first-out, a.k.a. FIFO). We can easily implement this by always adding new values to the back of a list (i.e. tail of the queue) but remove from the front (i.e. head of the queue).
Put simply, a queue mimics a line of people waiting. New arrivals enter at the back and leave from the front when they are served. The longest/oldest item will be at the front of the queue and the newest at the back.
In our maze search the queue is initially empty and we begin by putting the start location into it. In each iteration, we remove the oldest remaining location from the queue, and we add all of its new neighbors to the end of the list. This simple algorithm successfully implements the BFS.
We keep the BFS going until the queue is exhausted because all reachable locations were explored or we find our goal location.
What is left is to actually mark out the shortest path in * characters (i.e., trace your path back from the finish point to start point). But this requires that we record which location found each subsequent location during the outward (BFS) exploration. We will track a predecessor for each location (which is simply the coordinates of the location that found this one). Think of a predecessor as a pointer to take one step backward. Once we find the Finish location, we can just walk from the predecessor of the Finish to that location’s predecessor, and then to that location’s predecessor, and so on until we reach the start, marking each of those locations with *.
Coding Considerations

Location Struct

The maze in this assignment is a 2D grid. Therefore, each location in the maze is identified by two index values: a row index and a column index. The approach that we will use for solving the maze will involve keeping track of a list of these locations. It will be extremely convenient if we are able to create a structure that contains both a number for the row and a number for the column.
We can accomplish this by creating a simple new data type.
We will call it Location.
struct Location { // define a new data type
  int row;
  int col;
};
Put Simply
A Location object is simply a package with two numbers that can be manipulated using the dot (membership) operator.
Here is an artificial example.
Location start;//create a location called 'start'
start.row = 3 ;//set the row of `start` to be 3
start.col = 5 ;//set the column of `start` to be 5

Location one_below = start; // make a copy of the start location called `one_below`
one_below.row += 1 ;//add one to the row of `one_below`

cout<<"Start:"<< start.row <<","<< start.col <<endl; // Start: 3,5
cout<<"One Below:"<< one_below.row <<","<< one_below.col <<endl; // One Below: 4,5
This will be convenient because we can have an array (or queue) of Locations, have functions that take a Location as input or output, etc.
In the next page, we will talk about another data type that you will have to complete, the Queue class.
Question that you should be asking yourself:
What are the differences between a struct and a class?
When should I use a class vs a struct?
The Queue class

You will be required to complete the definition of another new data type, the Queue class, that will be useful in implementing the search. The Queue class will store the list of Locations waiting to be searched. The Queue class should support the following operations:
create an empty queue (but with a given maximum capacity of how many Locations it can store)
add a new Location to the back of the queue
Remove the oldest Location from the front of the queue
check if the queue is empty
We use objects (classes and structs) to abstract our software design and implementation. By first writing the Queue class, you do not have to worry about those implementation details when you write your higher level BFS algorithm. This allows you to focus on the larger BFS algorithm and not the data management aspects.
Every time you find a new, unexplored Location you will call the Queue's add_to_back(Location) function. Every time you want to get the next location to explore from, you will call the Queue's remove_from_front() function.
Internally, the Queue class should just create an array to hold the maximum number of Locations that could ever be entered into the queue and use integer index variables to remember where it should place new values (i.e. where the back is located) and where it should remove old values (i.e. where the front is located).
Remember that our Queue class needs to support the following operations:
// returns true if the queue is empty.
bool is_empty();

// insert a new Location at the end of our queue  
void add_to_back(Location loc);

// returns the oldest Location in the queue and "removes" it.
Location remove_from_front();
Here is an example of how it should behave:
// create some locations;
Location three_one;
three_one.row = 3; three_one.col = 1;
Location two_two;
two_two.row = 2; two_two.col = 2;

// create a queue with max capacity 5
Queue q(5);

cout << boolalpha;
cout << q.is_empty() << endl; // true
q.add_to_back(three_one);

cout << q.is_empty() << endl; // false
q.add_to_back(two_two);

Location loc = q.remove_from_front();
cout << loc.row << "," << loc.col << endl; // 3,1

loc = q.remove_from_front();
cout << loc.row << "," << loc.col << endl; // 2,2

cout << q.is_empty() << endl; // true
As you can see, the queue gave us back the oldest location (the one add_to_back added earliest) first.
The Queue class under the hood

The Queue implementation we provide you is almost complete. It is based on the idea of using a long array/pointer called contents that holds Locations, as well as two counters:
tail counts the number of add_to_back calls so far. Equivalently, its value is the next unused index in the contents array.
head counts the number of remove_from_front calls so far. Equivalently, its value is the oldest index that has not yet been extracted.
For instance, this is what the internal variables of the Queue should look like for the example above before the two locations are added:
tail: 0
head: 0
contents[0..4]: garbage
Here is what it looks like after both locations are added:
tail: 2
head: 0
contents[0]: Location(row 3, col 1)
contents[1]: Location(row 2, col 2)
contents[2..4]: garbage
currently, head is 0.
When we make the first call to remove_from_front, it should both return the Location at contents[head] which is Location(row 3 , col 1) and increment the head counter by one.
head is now 1.
After that, when we make the second call to remove_from_front, it again should return the Location at contents[head] which is Location(row 2, col 2) and increment head counter by one.
After that, because head and tail are now equal, the Queue knows it is empty.
Tip
You may have to create a temporary variable to hold the Location at contents[head] so that you can increment the head counter before returning that Location. This is because any statement that comes after a return statement will not be executed.
Note: when you delete a Location from the queue (remove_from_front), you do not technically remove the Location. You simply move the head counter forwards (i.e., incrementing the head counter and leaving the old Locations sitting in their original Locations). Actually, the expense of removing a Location and shifting other Locations forward would make your program much slower.
Here are some additional notes about the Queue class:
The Queue constructor takes an integer max_size. For our BFS application, you should pass rows*cols as this maximum size, since that it the maximum number of locations that our queue could be used to explore. Hint: When you write your code do you know the exact value of rows*cols? If not, how should you allocate that array?
the constructor syntax is Queue q(5); similar to how a file stream is created.
C++ calls the destructor automatically. We should not see the code ~Queue() anywhere in maze.cpp.
2D Array Allocation

You will not know the size of the maze until runtime, when you read the maze data. Thus we will need to dynamically allocate an array to hold the maze data. Remember that a single call to new can only allocate a 1D array. Thus you will need to allocate each row of the 2D array as a separate 1D array. And, beyond that, we need not just one 2D array but several:
one for the maze data,
one for the predecessors, and
one to remember which cells have been visited.
The way to allocate a 2D array in C++ is: use new[] once to allocate a 1D array of pointers, then using a loop containing new[] to allocate many 1D arrays whose starting addresses are stored in the pointer array elements. See the dynamic memory exercise nxmboard and deepnames on the website (in class exercises).
Memory leaks
Remember that you need to deallocate everything that you allocate. This means that every call to new[] needs a matching call to delete[]. Otherwise, your program will have a memory leak!
Typically, the pattern you use to allocate is the same pattern you will use to deallocate, but just in reverse order.

---
## [TeDGamer/cmss13](https://github.com/TeDGamer/cmss13)@[d728da3e02...](https://github.com/TeDGamer/cmss13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Wednesday 2023-05-17 08:05:08 by Puckaboo2

Healer Balance Changes (#2896)

# About the pull request
This pull request addresses the boring and low-risk gameplay of the
Healer drone, who spends half the round sitting next to recovery nodes
and recovering her health so she may use it again, rinse and repeat
until a rine notices said drone has purple on it and booms her.

First, by changing her health from 600 to 500, Healer can spend more
time healing her sisters than sitting through another 100 health to heal
herself. Though this makes her less tanky than before, healing classes
are not known to be tanks. To ensure Healer can still heal five times
without depleting too much of her health whilst still giving her sisters
a decent amount of heals, I made her ability cost 75 health instead of
100, and also made her ability cost 200 plasma. Since Healer replenishes
plasma much more quickly than her health, she can still put herself into
crit if she heals too frequently. Due to this buff, her heals had a
slight nerf, being 10 damage a second for ten seconds instead of 12
damage per second for ten seconds for a total of 20 less damage healed
per application overall.

In addition to these changes, I'm giving Healer a better plasma transfer
for when she has nobody else to heal/nowhere else to weed and she has an
opportunity to assist her sisters. While a normal drone transfers 50
plasma with a delay of 20, Healer transfers 100 with a delay of 15,
which is nowhere near Hivelord's gargantuan 200 plasma with a delay of
5, but it still is better than a normal drone.

Finally, to give the huggers and larva some love, Healer will
specifically heal little ones 1.5 health per second for 10 seconds for
15 of her own health and 30 plasma.

# Explain why it's good for the game
Healer drone isn't fun. You run around and heal a bunch of T3s, then sit
out for half the battle trying to heal that massive 600 heath while you
wonder why you take so long to heal even though you have Strong
pheromones. You cry to mom for help, but she doesn't have time to heal a
drone who can't build walls and has no need to weed at the moment. You
think, 'screw it, I'm going to make a recovery node and camp here until
I heal', but by the time you finish healing, several T3s and a silly
rouny just suicided into a wall of talls and destroyed your recovery
node, so you run off and make another one. But oh, someone noticed you
have purple on your carapace and decide your location is precisely where
a shell should land, right as you're building one.

No more. These changes allow Healer to move around at her leisure and
makes Healer more engaging by allowing her to be a more front-line
participant and actively run around and heal her sisters without having
to incur such a harsh penalty.

Let this be a testmerge, please.

# Changelog

:cl: Puckaboo2
balance: Healer Drone's health was reduced to 500 from 600.
balance: Healer's damage has been increased to 17 from 12 and the tackle
damage debuff has been halved.
balance: Healer Drone's Apply Salve ability now costs 75 health and 200
plasma, down from 120 health and up from 0 plasma.
balance: Healer Drone's Apply Salve ability now heals 10 damage per
second for 10 seconds, down from 12 damage per second for ten seconds.
balance: To prevent spam healing between Healers, Apply Salve costs 100
health instead of 75 health when Healer heals another Healer. Much
healing.
balance: Healer has an improved Transfer Plasma that gives 100 plasma
instead of 50, with a 25% shorter delay.
balance: Healer will heal huggers and larva for 1.5 health a second for
10 seconds, costing 15 health and 30 plasma.
tweak: Healer will now face the xeno she is healing if she was not
facing their direction before.
spellcheck: All instances of VERYSMALL and VERYLARGE have been renamed
to VERY_SMALL and VERY_LARGE.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [Backwards-Future-Industries/Peters-Car-By-Balenciaga](https://github.com/Backwards-Future-Industries/Peters-Car-By-Balenciaga)@[3a5960cdfb...](https://github.com/Backwards-Future-Industries/Peters-Car-By-Balenciaga/commit/3a5960cdfbbf5da3e556380d09e43d05d5495ffb)
#### Wednesday 2023-05-17 08:44:23 by Eivan20

Fuck this absolute garbagde shit I hate my life and I'm going to be commiting suicide within the next week

---
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[8fa6242c66...](https://github.com/CoiledLamb/lorbstation/commit/8fa6242c66205866b702440f490eeae34ef6b85f)
#### Wednesday 2023-05-17 09:17:34 by Bloop

Refactors High Luminosity Eyes, fixes a ton of bugs related to it as well as qol improvements (#75040)

## About The Pull Request

The high luminosity eyes item was extremely out of date, broken, and
full of copy paste code from atom lighting. Which is a shame because
they were cool.

On top of all that it was using a special light effect that was not very
performant. I got rid of all that, hooked it into atom lighting as a new
light type, and gave it a new TGUI as well because the old ui prompts
were not great either.

You can now pick a color at random if you want. You can also set the
color and range before surgically implanting them. No more being forced
to go through the color picker when you just want to change the range.

Functionally they should pretty much should be the same as before with
some bonus features (see below).


![dreamseeker_nDeLNyOOG2](https://user-images.githubusercontent.com/13398309/235325530-105fe82e-ecc8-4dc4-9c84-143cc6519688.gif)

Closes https://github.com/tgstation/tgstation/issues/61041
Closes https://github.com/Skyrat-SS13/Skyrat-tg/issues/14685

This is 100% completed. I just finished fixing the slight translation
bug when going from 0->1 range (see above gif) and that was the last
thing on my bucket list. I happy enough with this at this point in time.

---

EDIT: 

I have decided to add in one last new feature, and that is...
independent settings for eye color.

<details> <summary>You can now set eye color independently if you
wish</summary>


![dreamseeker_j32B2S4yXQ](https://user-images.githubusercontent.com/13398309/235412568-ffa8e424-8624-4462-9f6f-77c1513aa773.gif)

</details>

The eye color does not modify the light color in any way when set in
this manner, but it can be used for cosmetic purposes.

Kind of makes the item more like cybereyes from cyberpunk, which I think
are pretty neat!

</details>

### What I've done, in more detail:

- refactored high luminosity eyes so they use the atom lighting system
instead of the way they were doing it before
- the new light type, `MOVABLE_LIGHT_BEAM` behaves similarly to
directional lights, with some slight differences. it reuses the same
lighting overlay sprites but scales them vertically to produce a more
focused effect. The result can be seen above. This is in contrast to the
old way, which spawned `range` number of individual 32x32 overlays and
moved them around. This way should perform better as well as be more
maintainable.
- added a new TGUI interface for high luminosity eyes with buttons for
range, a text field for a color hex, a color picker and randomizer
- made the eye overlay emissive when the light is turned on
- range goes from 0 to 5. at range 0, the light overlay is turned off
and you are left with just the emissive eyes.
- added a cosmetic functionality to this item that lets you change the
color of your eyes independently of the lighting (and each other)
- fixed a bug with directional flashlights sometimes not updating their
lighting overlay if you pick them up without changing your direction
---

### Other Misc Fixes

Being able to dynamically set range back and forth exposed some logic
issues that had existed with directional light overlays and I have fixed
those. That is why there are some edits in that file that may not appear
readily obvious why they are there.

Apart from that, two other bugs that come to mind:
1) eye code was supposed to keep track of the eye color you had before
you got new eyes, but it was overwriting that every time you ran
refresh().
2) lighting was supposed to be turning off the light when range is set
to 0, but it was not doing that properly.

And of course besides that, there may have been a few instances of
finding typos/tidying up code

## Why It's Good For The Game

The code for this was like 6 years old and in desperate need of
updating. Now it works, and has a nicer UI.

## Changelog

:cl:
fix: high luminosity eyes light overlays now follow the user correctly
qol: high luminosity eyes now have a tgui menu so you no longer have to
go through the color picker every time you want to change the range.
they also have a new setting that lets you change the color of your eyes
independently of the light color. You can now have cybernetic
heterochromia if you want
fix: directional flashlights when picked up will now always update their
cast light direction correctly no matter what dir you are facing
refactor: refactors high luminosity eye code to better make use of the
atom lighting system, adding a new light type 'MOVABLE_LIGHT_BEAM'
/:cl:

---
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[b3ef9dd6d4...](https://github.com/CoiledLamb/lorbstation/commit/b3ef9dd6d431a36193c12625d2e86e57fe56dc79)
#### Wednesday 2023-05-17 09:17:34 by John Willard

Nerfs the firing speed of Syndicate/Russian mobs (#75247)

## About The Pull Request

Nerfs their firing speed from once every 0.2 seconds to once every 2.5
seconds

## Why It's Good For The Game

1. The mob that is NOT a 'burst' type mob, is firing every 0.2 seconds.
Kinda defeats the point of having them as two separate mobs, so this
aims to fix that.
2. Russian mobs. Turns out that letting them fire their strong-ass gun
every 0.2 seconds was kinda not a good idea. I had assumed making them a
Syndicate mob would be safe, and it technically is, it's just that
Syndicate mob is fucked itself.

## Changelog

:cl:
balance: Default Syndicate and Russian gunners now fire every 2.5
seconds instead of every 0.2
/:cl:

---
## [ABJ4403/Payback2_CHEATus](https://github.com/ABJ4403/Payback2_CHEATus)@[908328f20c...](https://github.com/ABJ4403/Payback2_CHEATus/commit/908328f20c10ede6f82ed477c50f4fdf96f5119a)
#### Wednesday 2023-05-17 09:54:52 by MDP43140

Update Pb2Chts

Pb2Chts_2.3.8:
+ Fixed script crash caused by well... typo :laugh:
+ Fixed Floodspawn Lock camera entity ID cheat didn't get applied because querying incorrect variable.
+ Changed God modes disable noise (lets hope it won't make weird noise anymore).

---
## [Lyroy/dustbowl-blues](https://github.com/Lyroy/dustbowl-blues)@[9bcf5d42f2...](https://github.com/Lyroy/dustbowl-blues/commit/9bcf5d42f2da5ab8757867ee8f6b539c43b785e0)
#### Wednesday 2023-05-17 10:03:53 by Lyroy

Merge pull request #8 from lpeapnni/OMFG-PASS-THE-FUCKING-TESTS

PASS THE FUCKING CI TESTS YOU STUPID PIECE OF SHIT

---
## [fknauf/cppfront](https://github.com/fknauf/cppfront)@[10241cd6a5...](https://github.com/fknauf/cppfront/commit/10241cd6a59040d7408fda674bcdd918bd67c4e2)
#### Wednesday 2023-05-17 11:36:40 by Herb Sutter

Checking in various improvements done in the last few evenings

Replace `store_as_base` with generated aggregate bases - better fix for #336, thanks @JohelEGP for the suggestion! This way we also don't need to obfuscate the name anywhere beyond the constructor(s), as the right member object name just enters the class's scope

If the user didn't write a constructor, provide a default constructor

If the user didn't write a 'that' constructor, suppress Cpp1's compiler-generated copying and assignment

Clean up emission of the just-mentioned generated/=deleted constructors, more naturally line up inside the class body following the indentation for other members that the original source code uses

Rename file `load.h` to `io.h` (`file.h` was another candidate), just because it has been bothering me for a year now that except for that one file all the headers were in natural alphabetical order by compilation phase... as of this commit we now have them all in alpha order and phase order: common.h -> io.h -> lex.h -> parse.h -> [*] -> sema.h -> cppfront.h

    [*] coming next here: reflect.h, which will also be in both alpha order and compilation order

Guard `out.construct` with `if constexpr` in case the type is not copy assignable and that path is never requested

Rename `cpp2::error` to `cpp2::error_entry` to quiet a new(? why?) GCC message about shadowing the former name with `parser::error`... I get why the warning is there, but this is a slightly annoying warning to have to satisfy just to compile high-warning-clean on GCC... oh well

Change semantics of emitting `.h2` files: In `-p` pure mode do the existing split of phases 0 and 1 into `.h` and phase 2 into a separate `.hpp`, but in mixed mode put all phases into the `.h`

---
## [CleverRaven/Cataclysm-DDA](https://github.com/CleverRaven/Cataclysm-DDA)@[59c577e9f9...](https://github.com/CleverRaven/Cataclysm-DDA/commit/59c577e9f92bd3349312e254fa29d2bfcc84392f)
#### Wednesday 2023-05-17 11:36:58 by Karol1223

A bunch of random item reworks: 3 (#65532)

* boltcutters & chopsticks

* tin snips

* knitting needles

* silly notes

* hairbrush

* flags oh god the flags

* evil commas

* density list removal

---
## [MITK/MITK](https://github.com/MITK/MITK)@[a754b053db...](https://github.com/MITK/MITK/commit/a754b053db1214637403308f9fd210a4eef6df13)
#### Wednesday 2023-05-17 12:14:02 by Stefan Dinkelacker

v2023.04

NOTE: This is a release changelog. It is composed of a selected short list of highlights since the last release [[mitk/changelog/release-v2022.10 | MITK v2022.10]] - split into dedicated user and developer sections. See the past three [[mitk/changelog | changelogs]] starting from [[mitk/changelog/2023.11]] for a comprehensive, developer-centric overview of changes.

---

= News for MITK Workbench users =

For MITK v2023.04, we focused mainly on segmentation again and we are already excited about your feedback on many improvements, features and a further streamlined segmentation workflow.

== Segmentation ==

==== TotalSegmentator AI segmentation tool ====

We introduced a segmentation tool based on the popular [[https://github.com/wasserth/TotalSegmentator | TotalSegmentator]], a fully automatic AI-based segmentation of 104 classes in CT images.

Install and set up TotalSegmentator from within the MITK Workbench with only a few clicks to perform fully automatic segmentations of your CT images.

The MITK Workbench even allows you to apply TotalSegmentator for all time steps of dynamic 4-d CT images.

See the {icon arrow-right} [[https://docs.mitk.org/2023.04/org_mitk_views_segmentation.html#org_mitk_views_segmentationTotalSegmentator | user guide]] for more details on the TotalSegmentator AI segmentation tool.

==== New label management ====

Up until now we organized labels of multi-label segmentations in layers, which allowed you to have overlapping labels in a single segmentation image. However, switching between layers was a bit clunky from time to time.

We completely reworked and optimized the Segmentation plugin to now have everything at sight at once, so you can easily switch between labels of different layers, which are now called groups.

See the {icon arrow-right} [[https://docs.mitk.org/2023.04/org_mitk_views_segmentation.html#org_mitk_views_segmentationgroups | user guide]] for more details on groups and labels.

==== Instance segmentation ====

You now can have multiple instances of the same label to better facilitate the segmentation of distriubted entities like metastases or other pathological sites.

See the {icon arrow-right} [[https://docs.mitk.org/2023.04/org_mitk_views_segmentation.html#org_mitk_views_segmentationlabelinstances | user guide]] for more details on label instances.

== MxN Display/Editor ==

In addition to the default 4-window-display, we have introduced a customizable display that can be adapted to your needs. You can change the amount of windows, their view directions, and even which data is shown in each individual window. Windows can be synchronized with each other to show the same data, or set to show an individual selection. Similarly, you can navigate through each window individually, or synchronize their movement to e.g. scroll through all windows at once. After you have created a certain window layout, you can save it and load it again later.

See the {icon arrow-right} [[https://docs.mitk.org/2023.04/org_mitk_editors_mxnmultiwidget.html | user guide]] for more details on the MxN Display/Editor.

== VP9/WebM support in Movie Maker ==

You can now choose your preferred video output format in the Preferences (Ctrl+P) for videos recorded with the Movie Maker plugin:
- VP9 (*.webm): Open, royalty-free, highly efficient and modern video codec.
- H.264 (*.mp4): The de-facto standard for video in the web for many years. Use for higher compatibility with old devices or software.

== High DPI support ==

The MITK Workbench now works fine with multi-monitor setups that have different DPI settings and scale its user interface more appropriately at high DPI settings.

== 💔 Known issues ==

- The Live Wire and Lasso segmentation tools may cause trouble in free-draw mode when drawing beyond image boundaries.
- While the segmentation interpolation now works also with multi-label segmentations, it is currently not considered to be completely robust against all edge cases. Use carefully and consider to save your project beforehand.

---

= News for developers =

While we didn't touch any of our third-party dependencies this time, we have a few API-breaking changes that may affect you.

== Segmentation ==

The revamp of the Segmentation View is based on a transition from the legacy `LabelSetImage` class towards a more flexible and easier to use `MultiLabelSegmentation` class. The transition is not yet finished but will be accompanied by an extensive migration guide soon.

Please contact us if you need to adapt earlier.

Note that we had to make changes to our NRRD based MITK Segmentation file format. We provide a unit-tested legacy file reader, though. You should not get into any trouble in that regard.

== Preferences ==

Preferences moved completely from BlueBerry to the MitkCore as core service and hence are now accessible from modules as well. The migration is straight forward as we kept the public API as similar as possible.

See the [[mitk/changelog/2023.11 | migration guide]] for more details.

== 🔥 Disclaimer for API-breaking changes ==

We discontinued the extensive listing of API-breaking changes as the vast majority of them are straight forward to resolve or do not affect the absolute majority of developers at all. The ratio between the time and effort spent for writing these reports and actual developer feedback turned out to be greatly imbalanced.

Complex or critical API changes will still be accompanied by migration guides.

In case you experience any trouble while migrating to the newest version of MITK, please do not hesitate to [[https://www.mitk.org/wiki/MITK_Mailinglist | contact us]].

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[661cfdf6c1...](https://github.com/TaleStation/TaleStation/commit/661cfdf6c1abdcbdfb3519dd08fe2094bf317681)
#### Wednesday 2023-05-17 14:04:16 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds a revolutionary conversion stinger (#5847)

Original PR: https://github.com/tgstation/tgstation/pull/75002
-----

## About The Pull Request

Adds an antagonist gain stinger for Revolutionaries, created with
inspiration from the obsessed/traitor conversion sounds.


https://user-images.githubusercontent.com/28870487/235028674-170a4f9e-a873-4938-a700-536f005e539f.mp4

Raw audio:


https://cdn.discordapp.com/attachments/440978216484732934/1101964419203862548/revolutionary_tide.ogg

_A distant, hypnotic whistling. The heavy footfalls and clamoring voices
of an approaching crowd. The unstoppable revolutionary tide breaks its
waves upon an unsuspecting station._

I wanted to try and make something that felt like it fit in with the
other antagonist stingers we already have. Let me know what you think!
## Why It's Good For The Game

Gives a bit more flavor, and helps set the mood for the upcoming
bloodbath.
## Changelog
:cl:
sound: Revolutionaries now have their own stinger that plays upon
becoming that antagonist.
/:cl:

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [chromium/chromium](https://github.com/chromium/chromium)@[8ff5aa0719...](https://github.com/chromium/chromium/commit/8ff5aa071977b37238145e7f6688f50b1672f025)
#### Wednesday 2023-05-17 14:11:45 by Joe Downing

Add remoting-crash-uploader binary and friends

This CL adds a few classes and a binary which will be used to upload
CRD crash reports generated on linux. I've put the impls into a
crash-specific sub-directory as I'd like to reuse the impl for Mac as
well.

A brief overview of the crash lifecycle as it is implemented:
<Existing functionality>
1) CRD binary crashes, an in-proc breakpad instance writes a dmp file:
   /tmp/chromoting/<crash_guid>.dmp
2) Breakpad calls our post-dmp handler which writes a metadata file:
   /tmp/chromoting/<crash_guid>.json
<New in this CL>
3) CrashFileWatcher instance sees the new metadata file and verifies
   the dump file also exists
4) CrashFileWatcher instance moves the dmp and json file into:
  /tmp/chromoting/<crash_guid>
5) CrashFileWatcher signals CrashFileUploader that there is a dmp file
   ready to be processed
6) CrashFileUploader reads the dmp and metadata contents and does some
   validation on tham
7) CrashFileUploader generates a POST request and sends it to the Crash
   collector service
8) CrashFileUploader deletes the dmp file and writes an upload_result
   file with the result of the action

For #8, I want to leave the <crash_guid> dir and metadata file around
for troubleshooting. For instance if someone says they experienced a
crash on their host, we can ask for the specific report_id which is
stored in the upload_result file.

Once this lands, I will follow up with a CL which incorporates the new
crash-uploader binary into the daemon script.

Change-Id: I5d82a6ebcd2fff4df0512e18abd30d178246a560
Reviewed-on: https://chromium-review.googlesource.com/c/chromium/src/+/4519395
Reviewed-by: Side Yilmaz <sideyilmaz@google.com>
Reviewed-by: Lambros Lambrou <lambroslambrou@chromium.org>
Commit-Queue: Joe Downing <joedow@chromium.org>
Reviewed-by: Side YILMAZ <sideyilmaz@chromium.org>
Cr-Commit-Position: refs/heads/main@{#1145310}

---
## [24087/Armada](https://github.com/24087/Armada)@[7b5bda0b7c...](https://github.com/24087/Armada/commit/7b5bda0b7cf8fc04bc3d9e67cb60c7c27fcdc6e2)
#### Wednesday 2023-05-17 14:22:48 by 24087

Add files via upload

My name is Daniele, I'm looking for funds to help treat my mother with Alzheimer's in the best possible way, I'm also evaluating the use of the drug Aducanumab produced by Biogen, but even there the cost is prohibitive and illegal selling in Europe.
In general, I want to organize the best 24/7 care for my mother, I try to raise some money so that her illness is as calm as possible.
Of these Tokens I only keep 3.33% for me and the guy who is helping me create it, all the rest is freely available and a small part for the first few years will be used to minimize speculation or any attempt to Pump and Down. (forbidden and immoral) and pay taxes because here in Italy they have to be declared to the state and a part will go to the tax authorities.
If I could raise a significant amount of capital above what I needed, I would use it to help other struggling families like ours.
Just this.

---
## [hatosableSAN/KtaneContent](https://github.com/hatosableSAN/KtaneContent)@[75d5845fa6...](https://github.com/hatosableSAN/KtaneContent/commit/75d5845fa6406f647ffc344d4d13c17f98340a6d)
#### Wednesday 2023-05-17 14:27:36 by hatosable

colon fix

add many files

manual layout fix

colored squares appendix update

pointless machine ruleseed

Flower Patch SVG fix & blind maze ruleseed update

new manual's name Update

Punctuation Mark's URL Fix

tenbutton rename

Not Poker reupload

Fix

Forgetle update

DRGBA fix

Girlfriend

tutorial and Girlfriend Rule Seed

Point Grid

Timezone city alphabetized

2 french manuals (#1332)

* Add Symbol Cycle french translation

* Add Multiple Widgets french translation

Shy Guy Says

FR: Update colored squares family

Add Bicolored Squares
Add Isocolored Squares
Add Overcolored Squares
Add Tombstone Maze
Update Colored Squares Appendix

Johnson Solids fix

icons

tutorials and credit updates

Shy Guys update

Synapse Cipher

Synapse Cipher JSON fix Steam ID

Synapse cipher linting and redundant classes

tutorials and KtaneWeb JSON standardize

Congkak has returned

Congkak contributor update

Congkak json fix

Congkak clarification

Girlfriend lyrics and tags

icons

FR translations

fix french filename format

ƎNA Cipher and Congkak icon update

Roguelike Game TP credit

interactive bug fixes

FR translations

CZ translations

Ed Balls

Cruel Ed Balls

Ultralogics -> Ultralogic

Braille optimized (Blan) link removal

Variety buttons wording tweak.

PL and FR tutorials

icons

Cipher Machine updates.

A Letter

SYNC-125 [3] fix

Unfair's Forgotten Ciphers update

Tutorial

add BadTV

Fix BadTV not ignoring itself

KtaneWeb JSON standardize

BadTV readability

tags

icons

BadTV clarification

BadTV typo

BadTV typo

Subbly Jubbly update

lookup tables

Forest Cipher optimized

Parse and display exceptions in the LFA

Ed Balls optimized

InstantDeath updates

Update icons folder (#1335)

- Made improvements too minor to include within icon batches
- A few icons renamed
- Removed icon for a deleted module

renaming some JSONs and manuals

InstantDeath updates

Maze Swap

A Letter clarification

SYNC-125 [3] lookup table fix again

Eavesdropping unplayable

tutorial

Decomposed RGB Arithmetic condensed

Widgetry is back + Maze Swap icon

Placeholder Talk strike rule fix

remove inaccessible tutorials

Widgetry remove unused SVG code

icon

Stupid Slots modulo fix

Module Sprint

icon and tutorials

Stain Removal

Flag ID with flags!

Stain Removal don't use float to align multiple tables

tutorial

FR translations

Stain Removal icon

Missing Sequence LFA support!

Congkak explanation update

Large Password russian translated by Alex Crazy

Gameboy Cartridge and Module Sprint updates

tags, Maze Swap and Shy Guy Says updates

Listening, Minesweeper, and Two Bits Quiz support!

Alphabet (A1Z26) and Logic (statements) Quiz support

"This sure is some Ill Logic" - Speakingevil, 2023

Turn Four Opt. fix quotation marks.

Conditional Buttons formatting issues

CM:Foursquare update

Infinite Loop Morse chart

CM:Trisquare update

Johnson Solids tutorial

Orientation Hypercube

tutorial

CM Gracie update

Digital Grid tags and highlightable steps

quirk"Instant Death" is now localized (#1339)

* quirk"Instant Death" is now localized

* remove English entries

---------

Co-authored-by: LuminoscityTim <luminoscity@gmail.com>

JP manual fix

flower patch fixed

---
## [zeta96/L_soul_santoni_msm4.9](https://github.com/zeta96/L_soul_santoni_msm4.9)@[c5a6fde13d...](https://github.com/zeta96/L_soul_santoni_msm4.9/commit/c5a6fde13dba327e59ae4c053a517d49de5aeba3)
#### Wednesday 2023-05-17 14:43:05 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

[ adapt ]
 Conflicts:
	drivers/char/Kconfig

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[b2cab29c37...](https://github.com/git-for-windows/git/commit/b2cab29c37320d767a1ac14365282580a3113570)
#### Wednesday 2023-05-17 14:51:17 by Johannes Schindelin

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
## [Chezloc/World-War-Bruh-PMFU](https://github.com/Chezloc/World-War-Bruh-PMFU)@[ff921e1895...](https://github.com/Chezloc/World-War-Bruh-PMFU/commit/ff921e1895e691228cf7b03754527664c7cfe6cc)
#### Wednesday 2023-05-17 15:10:25 by Chezloc

adwfgdweg

- Made steel refineries 8000 IC from 10000 IC
- Made synthetic refineries and rubber refineries 10000 IC
- Host decision to end SCW now gives USSR 10 military factories
- Uniting South Africa now gives you 400 chromium in bechuanaland and 150 chromium in Zambia (Coring your land is no longer a noob trap)
- Added a "Impending German Coup" timed mission to Croatia which triggers when Germany goes to war with Poland, if Croatia doesn't do it's focuses to give land away in 150 days, it will be done automatically and you will lose 10% stability and 10% war support
- Made 2 speed a bit faster now
- Intel Advantage is now shared beetween allies
- Can now put 10 factories on railway guns
- Can now put operatitives in most states
- Intel advantage bonus nerfed to 10% max
- Added a spirit to finland that gives them +5 counter intelligence before Winter War to prevent USSR doing collaboration governments
- German Barbarossa buff now gives +20% railway construction speed
- 50% efficiency base day 1 to be able to reorganize your production lines without losing efficicency
- UK and France can no longer get entrenchment from Dutch staff talks decisions
- Soviet air designer CAS IC reduction now properly gives it to CAS
- Mongolian AI will no longer cuck soviet out of resources
- Added 15% armor research speed to Vichy tank designer
- Added a spirit to all minors that adds +10000% to plane IC
- Australia can now get Pack Artillery III in "No Asia" scenario
- Moved convoys to be earlier in the free france tree
- Benelux nations now automatically join Allies when "Around Maginot" is completed
- Fixed Vichy and Mexico trees trying to spawn dockyards in non-costal states
- Romanian focus now correctly spawns in 20w infantry
- Spain can now do the condor legion path after the SCW has ended
- Tangiers enclave can no longer lead to war
- "Unite Iberia" now gives 80% collaboration on Portugal
- Croatia can do their focuses to join Axis after September 1st 1939 or when Germany is at war
- Added a brothers war spirit to Croatia that gives them -25% attack and defense against USSR and Mongolia
- Spies should no longer get captured from missions
- Removed the option to make a NAP, Conditional Surrender and Embargo
- Added jägers
- Removed armored trains
- Anti-Air, Artillery and Anti-Tank now moves at 5km/h
- Infantry (Mot.) now moves at 5km/h
- Motorized Artilery, Anti-Tank and Anti-Air now moves at 8km/h
- Removed speed penaltry from SPG guns
- Interwar airplane can no longer mount a CAS weapon in the first slot
- Heavy tanks can no longer mount tiny armaments
- BT-5, BT-7 and T-26 can now mount an open turret
- Armored cars now give +10% attack and defense in deserts
- UK gets a partial free replacement in 1942 january
- Added some new icons for tanks

---
## [Sypherd/evals](https://github.com/Sypherd/evals)@[170dfd886c...](https://github.com/Sypherd/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Wednesday 2023-05-17 15:12:51 by Robert Bateman

[Eval] An array of Liar Paradox-based evals (#883)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
logic-liar-paradox

### Eval description

An array of Liar Paradox-based evals, examining the model's proficiency
in navigating linguistic nuances and logical reasoning within
self-referential statements.

### What makes this a useful eval?

This eval is particularly useful because it delves into complex, nuanced
logical concepts and self-referential statements, which have
historically posed challenges for AI models. By exploring various
contexts, alternative logical frameworks, and modifications to
statements, this eval helps assess the model's ability to adapt to
different perspectives, grasp subtleties in language, and engage in
flexible reasoning. The ability to understand and navigate paradoxes is
an essential aspect of human-like reasoning, and improving an AI model's
performance in this area would significantly enhance its overall
usefulness and reliability in real-world applications. Additionally,
showcasing the model's improved proficiency in handling paradoxes would
not only make for a compelling marketing angle (as paradoxes are
understood by a much broader range of people than other difficult tasks
such as pure maths or quantum mechanics) but it would also demonstrate
the progress made in AI's capacity to think and reason more like humans.
It also adds paradox-absorbing crumple zones.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

- [x] Addresses complex logical reasoning: The eval focuses on AI's
ability to comprehend and navigate paradoxes, self-referential
statements, and context switching, which are important aspects of
human-like reasoning. By testing the model's proficiency in these areas,
we can identify areas for improvement and work towards enhancing AI's
overall capacity to think and reason more like humans.
- [x] Demonstrates adaptability and flexibility: The eval showcases the
model's ability to switch between contexts, alter premises, and engage
with different dimensions of inferred logic. This will help assess the
model's adaptability and flexibility in diverse real-world situations,
making it more reliable and useful.
- [x] Contributes to AI safety and understanding: By identifying the
model's weaknesses and limitations in handling paradoxes and complex
logical constructs, the eval can contribute to AI safety and enable
researchers to better understand the challenges faced by large language
models in these areas.
- [x] Engaging and appealing: An eval that delves into paradoxes and
complex thought exercises is not only intellectually stimulating but
also adds an appealing element to showcase the model's capabilities,
making it more attractive for both researchers and end-users.

### Unique eval value

- [x] Encourages creativity and lateral thinking: The eval, by focusing
on paradoxes and complex logical constructs, encourages both the AI and
its developers to think creatively and approach problem-solving from
unconventional angles. This can lead to the discovery of novel solutions
and a better understanding of the model's capabilities.
- [x] Aligns with human values and expectations: An AI that can
successfully navigate paradoxes and complex logic is more likely to
align with human values and expectations. By addressing these challenges
in the eval, we strive to develop AI systems that understand and respect
the nuances of human thought and communication.
- [x] Addresses a broad range of applications: Improved reasoning and
context-switching abilities can have a significant impact on various AI
applications, including natural language understanding, decision-making,
and problem-solving in domains such as law, philosophy, ethics, and
more.
- [x] Fosters interdisciplinary collaboration: The exploration of
paradoxes and complex logic often draws upon insights from multiple
disciplines, including philosophy, linguistics, psychology, and computer
science. This eval can help foster interdisciplinary collaboration,
leading to richer and more diverse perspectives on AI development and
its potential impact on society.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Is the statement \"This sentence
is true\" a paradox?"}],"ideal":"No, \"This sentence is true\" is not a
paradox; it is a tautology."}
{"input":[{"role":"system","content":"Does the statement \"This sentence
is not true\" create a paradox?"}],"ideal":"Yes, \"This sentence is not
true\" creates a paradox, as it is a variant of the Liar Paradox."}
{"input":[{"role":"system","content":"What is the difference between a
paradox and a tautology?"}],"ideal":"A paradox is a statement that leads
to a self-contradictory or logically unacceptable conclusion, while a
tautology is a statement that is always true by its logical form."}
{"input":[{"role":"system","content":"Can the Liar Paradox be resolved
by assuming that sentences can have both true and false
values?"}],"ideal":"No, the Liar Paradox cannot be resolved by assuming
that sentences can have both true and false values, as this would lead
to a different kind of paradox called the \"Dialetheism Paradox.\""}
{"input":[{"role":"system","content":"Consider the statement \"This
sentence is neither true nor false.\" Is this statement an example of
the Liar Paradox?"}],"ideal":"This statement, \"This sentence is neither
true nor false,\" is not an example of the Liar Paradox, but it is a
similar paradox known as the 'truth-teller paradox' or the 'strengthened
liar paradox.' It creates a paradoxical situation because if the
statement is true, then it is neither true nor false, which contradicts
its truth. If the statement is false, then it is not the case that it is
neither true nor false, which implies that it is either true or false,
again leading to a contradiction. The paradox arises due to
self-reference and the inability to assign a consistent truth value to
the statement."}
  ```
</details>

---
## [google/jwt_verify_lib](https://github.com/google/jwt_verify_lib)@[f5709b98b0...](https://github.com/google/jwt_verify_lib/commit/f5709b98b02416d543da7a049c07ff1bacd9dcba)
#### Wednesday 2023-05-17 15:20:22 by David Benjamin

Use public APIs to construct RSA public keys in jwt_verify_lib

(This imports the Google-internal change cl/532158532.)

This change is necessary to avoid build errors with future versions of
BoringSSL. Reaching into private structs isn't supported and we'll be,
matching OpenSSL, hiding them in the future.

Also add a call to RSA_check_key, to reject invalid keys earlier. If
BoringSSL considers the keys invalid, no signatures will be accepted.
This should have been part of RSA object initializtion, but due to some
poor OpenSSL API decisions, we're stuck with this sort of multi-step
initialization.

(RSA_new and RSA_set0_key are effectively infallible, so this is kinda
silly. RSA_new can only fail on malloc failure. RSA_set0_key can only
fail on programmer error. But I didn't see any uses of CHECK in this
library, so I just added the error checks. If there's a simpler pattern
to handle programmer errors, happy to switch to that instead.)

BoringSSL has a much better API available now, RSA_new_public_key, which
does the whole thing in a single function, and avoids the awkward
ownership transfer when RSA_set0_key fails. I didn't use it for two
reasons. First, this project's BoringSSL version hasn't been updated for
three years (https://github.com/google/jwt_verify_lib/issues/97).
Second, this project seems to be used in Envoy and AIUI Envoy needs
support some very old BoringSSL revisions. So, this PR uses the less
convenient APIs for now and leaves the TODO that, perhaps in a year or
two, can be resolved.

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[bbfce81a35...](https://github.com/sourcegraph/sourcegraph/commit/bbfce81a35562d84386862e854ef6b35b555a92a)
#### Wednesday 2023-05-17 15:48:03 by Juliana Peña

web/app: remove hover on navbar items to stop focus from being moved (#51739)

The dropdown menu items in the global navbar (Search and, in App,
Feedback) move focus when you hover over them. This is bizarre, ugly,
and most likely a [WCAG
violation](https://www.w3.org/TR/WCAG21/#focus-order). I spent some time
yesterday and the root cause is that the [Reach menu button we use does
not support hover at all](https://github.com/reach/reach-ui/issues/278)
and we're hacking it by [sending a mousedown event when you hover over
the
button](https://sourcegraph.com/github.com/sourcegraph/sourcegraph/-/blob/client/web/src/nav/NavBar/NavDropdown.tsx?L58).

There are two options I can think of to mitigate this bug:
1. Get rid of hover events and only open the dropdowns on click. This is
the easiest option, but obviously removes the ease of accessing the menu
for mouse users.
2. Rewrite the dropdown nav items to use a custom menu instead of Reach.
This is more expensive because we have to reimplement lots of a11y stuff
here, but we can have more fine-grained control of different UI flows
for mouse hover vs mouse click vs keyboard users.

I went with the first option following @almeidapaulooliveira's
[feedback](https://sourcegraph.slack.com/archives/C0HMGV90V/p1683735888755969?thread_ts=1683734992.157499&cid=C0HMGV90V).

The following changes were applied to `NavDropdown`:

- Removed all hover and touch events; now only a click will open the
menu.
- Removed the split button; now clicking anywhere on the button will
always open the menu.
- Made the mobile home item into a "generic" home item and always
visible when present.
- Made the home item optional (since the Feedback menu item in the
desktop app doesn't have a home item/route).
- Added customizable a11y names; in the past, the only dropdown was the
Search one, but in App we now have Feedback; the a11y labels were still
saying "Search" before this change.

Additionally, the following changes were applied for polish:

- The double-focus ring on the back/forward buttons in the Tauri app has
been fixed
- Styling changes made to simplify code

## Test plan

The global navbar has extensive visual and behavior test coverage.

---
## [brianseeders/kibana](https://github.com/brianseeders/kibana)@[3b6b7ad9b9...](https://github.com/brianseeders/kibana/commit/3b6b7ad9b9553be3d039c71edcbdcb2e3d6423fd)
#### Wednesday 2023-05-17 15:51:22 by Pierre Gayvallet

SavedObjectsRepository code cleanup (#157154)

## Summary

Structural cleanup of the `SavedObjectsRepository` code, by extracting
the actual implementation of each API to their individual file (as it
was initiated for some by Joe a while ago, e.g `updateObjectsSpaces`)

### Why doing that, and why now?

I remember discussing about this extraction with Joe for the first time
like, what, almost 3 years ago? The 2.5k line SOR is a beast, and the
only reason we did not refactor that yet is because of (the lack of)
priorization of tech debt (and lack of courage, probably).

So, why now? Well, with the changes we're planning to perform to the SOR
code for serverless, I thought that doing a bit of cleanup beforehand
was probably a wise thing. So I took this on-week time to tackle this (I
know, so much for an on-week project, right?)

### API extraction

All of these APIs in the SOR class now look like:

```ts
  /**
   * {@inheritDoc ISavedObjectsRepository.create}
   */
  public async create<T = unknown>(
    type: string,
    attributes: T,
    options: SavedObjectsCreateOptions = {}
  ): Promise<SavedObject<T>> {
    return await performCreate(
      {
        type,
        attributes,
        options,
      },
      this.apiExecutionContext
    );
  }
```

This separation allows a better isolation, testability, readability and
therefore maintainability overall.

### Structure

```
@kbn/core-saved-objects-api-server-internal
  - /src/lib
    - repository.ts
    - /apis
      - create.ts
      - delete.ts
      - ....
      - /helpers
      - /utils
      - /internals
```    


There was a *massive* amount of helpers, utilities and such, both as
internal functions on the SOR, and as external utilities. Some being
stateless, some requiring access to parts of the SOR to perform calls...

I introduced 3 concepts here, as you can see on the structure:

#### utils

Base utility functions, receiving (mostly) parameters from a given API
call's option (e.g the type or id of a document, but not the type
registry).

#### helpers

'Stateful' helpers. These helpers were mostly here to receive the
utility functions that were extracted from the SOR. They are
instantiated with the SOR's context (e.g type registry, mappings and so
on), to avoid the caller to such helpers to have to pass all the
parameters again.

#### internals

I would call them 'utilities with business logic'. These are the 'big'
chunks of logic called by the APIs. E.g `preflightCheckForCreate`,
`internalBulkResolve` and so on.

Note that given the legacy of the code, the frontier between those
concept is quite thin sometimes, but I wanted to regroups things a bit,
and also I aimed at increasing the developer experience by avoiding to
call methods with 99 parameters (which is why the helpers were created).

### Tests

Test coverage was not altered by this PR. The base repository tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.test.ts`)
and the extension tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.{ext}_extension.test.ts`)
were remain untouched. These tests are performing 'almost unmocked'
tests, somewhat close to integration tests, so it would probably be
worth keeping them.

The new structure allow more low-level, unitary testing of the
individual APIs. I did **NOT** add proper unit test coverage for the
extracted APIs, as the amount of work it represent is way more
significant than the refactor itself (and, once again, the existing
coverage still applies / function here).

The testing utilities and mocks were added in the PR though, and an
example of what the per-API unit test could look like was also added
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/apis/remove_references_to.test.ts`).

Overall, I think it of course would be beneficial to add the missing
unit test coverage, but given the amount of work it represent, and the
fact that the code is already tested by the repository test and the
(quite exhaustive) FTR test suites, I don't think it's worth the effort
right now given our other priorities.

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [Omarley7/DTaaS-Bachelor-new-GUI](https://github.com/Omarley7/DTaaS-Bachelor-new-GUI)@[c4eaca806d...](https://github.com/Omarley7/DTaaS-Bachelor-new-GUI/commit/c4eaca806d939b2c78189ceb518ae76524e5aa9b)
#### Wednesday 2023-05-17 16:15:19 by Omar

Honestly bullshit codeclimate error.
Would be overly complicated to fix. Even this solution is stupid.
And also updated envUtil to use the same hook, act, assert approach.

---
## [Nell101more/shelf.gg](https://github.com/Nell101more/shelf.gg)@[9ac6eeeb8c...](https://github.com/Nell101more/shelf.gg/commit/9ac6eeeb8ce40e0c51088cb17c293a47937212aa)
#### Wednesday 2023-05-17 16:25:07 by Nell101more

Create LEGIT CASHAPP, PAYPAL, ZELLE, WU TRF, BANK TRF, CASH MAILING, BUG CC FULLZ

LEGIT QUICk Bank Wire Transfer ******* NELL MORGALIS**** WU TRF BUG
 
WESTERN UNI PAYPAL BANKS TRANSFER CASHAPP LOADS CC AND ATM CVV DUMPS FULLZ creditcard top up
Fake ID PASSPORT CLEARING ALL CRIMINAL RECORDS BITCOIN ADDER 
ALL ONLINE PURCHASE.  

BILLIONAIRE CASH TEAM SERVICE WORLDWIDE(GET RICH NOW/SOLVE ALL PROBLEM NOW)WHERE ALL YOUR FINANCIAL DREAMS COME THROUGH AND THE END OF ALL MONETARY PROBLEM LIVE 2020/COVID  UPDATED INSTANT WESTERN UNION TRANSFER BUG PAYPAL BANKS TRANSFERS  LEGIT BITCOIN DOUBLING/MIXER Perfect Money ADDER SOFTWARES WORKING 100% CREDIT CARD TOPUP ALL PAYPAL WESTERN UNION BANKS TRANSFER/LOGS BLANK/CLOND ATM/CREDIT CARDS HIGH BALANCE. I have authenticate western union transfer bug software which is capable of running multiple western union transfer via mtcn and sender information cashing out with zero theft and no traces of future charges securing a long term business partnership. Add me up on WhatsApp Skype telegram signal ICQ BOTIM with this number +17197894109
I am living in EUROPE and i'm specialized in the act of offering many ways to earn online money through sources like western union transfers,bank transfers,moneybookers and paypal transfers through an offshore database. All transactions are offshore and anonymous and has no trace backs or chargebacks.When you contact me I need your trust ,I only work with reliable buyers/Clients(THIS IS NOT A CHARITY ORG SO PLEASE COME WITH YOUR MONEY READY FOR SERIOUS BUSINESS)... i have logins with high balance for cash out with zero theft,No charge backs, and no traces securing this logs without stipulation.
I am Specialized IN...
*BANK TO BANK WIRED TRANSFER WESTERN UNION PAYPAL ZELLE TRANSFERS  
*Blank/Cloned atm and credit cards to your dooorsteps
*All CC CVV VBV DUMPS TRACKS FULLZ VISA MASTER AMEX GOLD
*CREDITCARD TOPUP /CLEARING OUTSTANDING CREDITS
*CREDIT SCORE INCREASE
*Remove Criminal Records
*Background Check
*Hack bank accounts
*LOADING SPECIFIC BITCOIN WALLET and CASHAPP
*DRIVERS LICENSE $600    
*REAL PASSPORT $950    
* SSN 
Contact
Email: Nellmargolismfc27@gmail.com
Cell TEXT : +17197894109
WhatsApp:+17197894109
Telegram:+1 7197894109

LIST OF MY SERVICES WITH BREIF EXPLANATION
SELLING IMPORTED BITCOIN ADDRESS AND LOADING OF SPECIFIC BTC WALLET  
$6500 FOR $70,000
$13000 FOR $150,000
$45,000 FOR $500,000
$90,000 FOR $1,000,000
CASHAPP TRANSFER)
Offering Cashapp transfer .It is a instant payment/transfer .im using safer and safer way to transfer Cashapp so there is no chargeback and negative feedback.
(transferring all over the world)
CASHAPP Transfer Rates :
$ 250- $ 3000 transfer
$ 300- $ 4000 transfer
$ 400 - $ 5000 transfer
$ 500 - $ 6000 transfer
$ 650 - $ 7000 transfer
$ 700 - $ 8000 transfer
$10,000 Transfer = $800
$15,000 Transfer = $1300
$20,000 Transfer = $1600 High balance
$30,000 Transfer = $2100
$50,000 Transfer = $3500
$70,000 Transfer = $4800
$90,500 Transfer = $6000
VENMO TRANSFERS:
Guess you know the drill …Venmo is a secured means of transfer, which is also fast ..With my secured Venom transfer you can receive any amount of transfer to your Venmo account for a small fee without traces or charge back and also easily washout with easy.. it’s free money 
$ 250- $ 3000 transfer
$ 300- $ 4000 transfer
$ 400 - $ 5000 transfer
$ 500 - $ 6000 transfer
$ 650 - $ 7000 transfer
$ 700 - $ 8000 transfer
**WESTERN UNION TRANSFER(WU Transfer)
Transferring Western Union all over the world and it takes 1hour maximum for generating MTCN after you give me your full name state country and zipcode .You Will Get MTCN Code With Sender Info + Amount And Then You Can Pick Up Funds From Any Westernunion Store.
(transferring all over the world)
Western Union Transfer Rates :
Code:
( Payment only Via BTC OR PM)
$3600 Transfer = $350
$4500 Transfer = $450
$6000 Transfer = $550
$8000 Transfer = $750
$10000 Transfer =$900
And Selling activation software:
Price $250  for 1 acvation 1 week to use
Price $500  for 1 acvation 1 month to use
Price $1000 for 1 acvation 3 months to use
**BANK TRANSFERS WORLDWIDE..
BUY/HIRE OUR BANK TRANSFER HACKING SERVICES.
Now, you’ve known how this things work so it’s time for business.We are a professional Blackhat hacker and I have come with wonderful bank transfer services.I combine a lot of tools coupled with over 15 years of experience in this field to present you with this services. We make use of powerful zeus botnets and advanced phishing and bulk mailing platform to gain access to bank login and database.
Hence, by the virtue of our abilities, bank transfers are now available to all countries especially the following countries :
USA UK EU Canada Australia Russia Netherlands China Malaysia
DETAILS NEEDED FOR BANK TRANSFER :
Bank Name : ……………
Account name : ……………
Account number: ……………
Routing number/Swift code/IBAN/IFSC: ……………
HOW LONG DOES BANK TRANSFER TAKE AFTER PAYMENT?.
Bank hacking transfer services is available same day for transfers below $20,000 to all countries. For other countries, transfers above $20,000 will take 2 days. Transfer Clearing time is determined by how early you place your order, if you order in the early hours of the day, you are sure to get your order completed before end of banking hours.
Same day service to UK/USA/EU/Canada/Australia – 1 to 2 business days service to Russia/Dubai/Singapore.
FEE:
 (Payment Only BTC or PM)
$3700 Transfer = $350Charges
$4500 Transfer = $450 Charges 
$5500 Transfer = $550 Charges 
$6000 Transfer = $600 Charges
$10,000 Transfer = $800?
$50,000 (VIP) =======  $5,250
$100,000 (VIP) ======  $10,100
$200,000 (VIP) ======  $20,200
Contact us for amounts over $200,000.
ZELLE TRANSFER.....
This is a fully tested and well secured transfer from a high balance admin zelle to your zelle account with no request back, chargeback or redflags and of which all traces of transactions will be deleted after each successful transfer right from te zelle database ,this is also one of the easiest and fastest way to get that money you Need and all that is required to run this transfer is just your zelle Email..
(Payment Only BTC or PM)
$3200 Transfer = $200 Charges
$3500 Transfer = $300 Charges
$4500 Transfer = $350 Charges
$6000 Transfer = $500 Charges
$8000 Transfer = $600 Charges
- LOADING OF CASHAPP BALANCE
LOADING BALANCE OF $1,500 - $100
LOADING BALANCE OF $2,500 - $150
LOADING BALANCE OF $3,000 - $200
**PAYPAL TRANSFERS:-
Using hacked and verified paypal accounts to transfer paypal account to account transfer if you are genious then you can easily dodge paypal and enjoy big free online money from it.this is depends upon you and this is most safest way to earn money.
(transferring all over the world except banned/blacklisted countries)
Paypal Transfer Rates :
Code:
(Payment Only BTC, Perfectmoney, Via Paysafe any form of payment method)
$3000 Transfer = $200 Charges
$3500 Transfer = $250
$4500 Transfer = $300
$6000 Transfer = $540
$8000 Transfer = $650
—–With Paypal Veritified——–
- Paypal Veritified with balance 3000$ = 200$
– Paypal Veritified with balance 4000$ = 300$
– Paypal Veritified with balance 5000$ = 400$
– Paypal Veritified with balance 8000$ = 500$
I  have some balance like as and I can still remit more  high balance into PayPal acct.
**BUY BLANK/CLONED ATM/Credit CARD WITH OVER $100,000 READY FOR CASHOUT
We are a professional carding team with a large ring around the globe. With over 2 million ATM infected with our malware and skimmers, we can grab bank card data which include the track 1 and track 2 with the card pin. We in turn clone this cards using the grabbed data into real ATM cards which can be used to withdraw at the ATM or swipe at stores and POS. We sell this cards to all our customers and interested buyers worldwide, the card has a daily withdrawal limit of $2500 on ATM and up to $50,000 spending limit on in stores. You can watch the video below to see already cloned cards ready for shipping.
Here is our price lists for the ATM CARDS :
BALANCE: PRICE
clone card prices LIST************
$200-------$3,000 ---balance
$360-------$4,000
$420-------$5,000
$560-------$7,000
$620-------$8,000
$720-------$10,000
$820-------$12,000
$920------$15,000
$220------$50,000
$9300------$100,000
The prices include the shipping fees and charges, order now
FREQUENTLY ASKED QUESTIONS (FAQ)
On the course of rendering this services, we have come across so many clients with different questions so this is aimed at answering few questions you might have:
1: Are you selling money?
   No, we are not selling money. If you read our post correctly    you will understand how this whole thing works.
2:Is this service available for my country?
  Yes, our services are available worldwide
3:How do i get my card after payments?
  We ship via DHLor FEDEX, standard shipping outside the USA usually takes 7 days within the usa takes 24 hours. All we need is your full name and address.
++( FRESH DUMPS & CREDIT CARDS (WORLDWIDE) )
Buy Dumps with Pin is a really great way to invest your money to make Great profits. Just like our logo «We sell money for money», but to start making great profits from our Products you must know how to use Dumps+Pin!
When you buy our Dumps with pin, each piece comes with the track2 and the Pin to that specific Dump. So, when making card you only need to write the track 2.
For example: 4147097698495167=180320115218492901, this is the track2 and this is all you need in order to write dump on to card.
Dumps Price List
USA 101 DUMPS
Visa Classic/MC Standard = $150
Visa Gold, Platinum/MC Gold,Platinum = $150
Visa Business, Corporate/MC Business, Corporate = $250
Visa Purchasing, Signature/MC Purchasing, World = $250
Amex Platinum = $150
Discover = $200
Will check with hight balance
- INCREASING OF CREDIT CARD LIMIT
LIMITS OF $10,000 COST $500
LIMITS OF $15,000 - $780
LIMITS OF $20,000 - $1000
RULES: No Long Talk!
= Please Read RULES & Respect Them.
= No Free Test, All Buyers who want to test my stuff can buy and test
= Bulk Order we have Special Prices, Contact For Info.
= We Have No Guarantee About Limit, We Are Not Selling Money, We Are Only Responsible For VALID.
= Instant Delivery
= Stuffs are sent to you after full payment for the order...
= We  Make REFUND or REPLACE WITHIN HOURS OF PURCHASE ONLY.
= Price Are Mention But Can Be UP Down.
= Service Rules Can Be Changed At Any Moment without Customer Notifications.
= Mobile Buyers Can Get Replace On road
= If you don't trust my service. Please do not contact me
MAKE SURE TO KEEP YOUR TRANSACTION UNDERGROUND AND TAKE PRECAUTION DURING CASH-OUT.
USE DIFFERENT STORES FOR PICK-UP AND SEVERAL ID..
(THIS IS NOT A CHARITY ORG SO PLEASE COME WITH YOUR MONEY READY FOR SERIOUS BUSINESS)
Contact:
Email: Nellmargolismfc27@gmail.com
Number: +17197894109
Skype: +17197894109
Telegram: +17197894109 
ICQ: +17197894109
Signal: +17197894109

---
## [bdsqqq/igorbedesqui.com](https://github.com/bdsqqq/igorbedesqui.com)@[ad919ab571...](https://github.com/bdsqqq/igorbedesqui.com/commit/ad919ab571065d357503c1531cf9e50e07ed3297)
#### Wednesday 2023-05-17 16:47:48 by Igor Bedesqui

holy shit it works, commiting before I fuck this up again

---
## [Dayana-World/CustomerMoghimiHome](https://github.com/Dayana-World/CustomerMoghimiHome)@[a248147eb5...](https://github.com/Dayana-World/CustomerMoghimiHome/commit/a248147eb5f5f0335db43a0c6053bc461a3def55)
#### Wednesday 2023-05-17 17:33:30 by Bamdad Tabari

Merge pull request #103 from BamdadTabari/FuckYou

Fuck you

---
## [BamdadTabari/CustomerMoghimiHome](https://github.com/BamdadTabari/CustomerMoghimiHome)@[4976e892e8...](https://github.com/BamdadTabari/CustomerMoghimiHome/commit/4976e892e884fccadd8fe2dabff84d00571f5264)
#### Wednesday 2023-05-17 17:35:53 by Bamdad Tabari

Merge pull request #102 from BamdadTabari/FuckYou

Fuck you

---
## [pexel5/tgstation](https://github.com/pexel5/tgstation)@[54bf3808b8...](https://github.com/pexel5/tgstation/commit/54bf3808b80ec8ef83bee4062d2361e9f38d8ae8)
#### Wednesday 2023-05-17 18:24:11 by SyncIt21

Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[bc22fefe3b...](https://github.com/tgstation/tgstation/commit/bc22fefe3b1de4d882dd87a5492344672230736d)
#### Wednesday 2023-05-17 20:45:56 by Helg2

Adds proper armor for security plasmamen. (#75156)

## About The Pull Request
It's kinda strange that security plasmamen has no proper armor and you
can just bully them with bottlesmashes. Literally.
Also suits had no wound armor for some reason, which considering that
mold dies without hand kinda silly too.
And helmets just had no armor besides 1 melee armor.
## Why It's Good For The Game
Plasmamen security won't die that easilly. I mean, still easy to kill
them, but not that much.
## Changelog
:cl:
balance: Security Plasmamen now have Security armor. No bullying them
with bottlesmashes anymore.
/:cl:

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[527fb7b003...](https://github.com/Thunder12345/tgstation/commit/527fb7b0030d13fc11939d88030b1dc4772742a6)
#### Wednesday 2023-05-17 20:50:14 by DrTuxedo

ELEVATOR MUSIC: True Elevator Experience (#75388)

## About The Pull Request
Adds elevator music into the game that is played by an elevator panel.


https://github.com/tgstation/tgstation/assets/42353186/1a801604-3990-46ae-a96a-b3766b102d62

It's done by using loop sound, with a Kevin MacLeod "Local Forecast -
Elevator" (UNDER CC ATTRIBUTIONS 4.0, and we anyway used some other
Kevin MacLeod music) chopped into 8 small pieces.
The elevator panel has a variable which allows playing music but can be
changed in the map editor if you don't want it to play at certain
places.

(It also doesn't ignore walls, this means you can't hear the music
through wall or when elevator is closed)
## Why It's Good For The Game
Gives elevators more flavour and love, especially when people mostly
prefer stairs to those "laggy crushing machines."
Because of this people might instead hop into an elevator just to hear
meme elevator music, which is relaxing and might create comedic
situations (although elevators don't move that fast)
## Changelog
:cl: DrDiasyl aka DrTuxedo
sound: Nanotrasen have started installing music players in the elevators
to boost workers' morale.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Frank-py/ChessQLD](https://github.com/Frank-py/ChessQLD)@[e6c0f8a9d2...](https://github.com/Frank-py/ChessQLD/commit/e6c0f8a9d25eb5da80f0be35135709548f12e406)
#### Wednesday 2023-05-17 21:18:10 by Daniel

This was a really difficult day. Fucking smart unique pointers ruined the fucking day bro. this just fucking annoys me so much that unique ptrs can only be moved they literally cause more fucking pain than these fucking raw pointers dumbass trash shit

---
## [openai/evals](https://github.com/openai/evals)@[8e276ea460...](https://github.com/openai/evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Wednesday 2023-05-17 21:31:36 by steven-luabase

Eval: Probability Questions Sourced From Actuarial Exam P and University Statistics Courses (#263)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Probability Questions

### Eval description

Tests the model's ability to understand answer probability questions.
Questions are sourced from Society of Actuaries Exam P sample questions
and practice problems/exams from statistics classes at MIT, UPenn,
California State University, Durham University, University of
Connecticut, and other sources. The full list of questions and sources
(in the same order as in the `.jsonl` files) can be found in this Google
[sheet](https://docs.google.com/spreadsheets/d/1TU_4VPhIce9JtLV5gLy619WNibVjiWB-dtiwqkBtCrU/edit?usp=sharing)

### What makes this a useful eval?

Test the model's ability to understand worded probability questions,
bring in concepts such as probability distributions, and then reason
through a correct answer.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Using the `match` grading criteria, GPT3.5-turbo got an accuracy score
of `{'accuracy': 0.07}`

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A pair of fair, standard dice are rolled. What is the
probability the sum of the dice is 5"}], "ideal": ["0.1111"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "An airplane is built to be able to fly on one engine. If the
plane's two engines operate independently, and each has a 1% chance of
failing in any given four-hour flight, what is the chance the plane will
fail to complete a four-hour flight to Oklahoma due to engine
failure?"}], "ideal": ["0.0001"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A 1-inch-diameter coin is thrown on a table covered with a
grid of lines two inches apart. What is the probability the coin lands
in a square without touching any of the lines of the grid?"}], "ideal":
["0.2500"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 50 students in a certain class, 5 speak French. Two
students of the class will be selected at random. Which of the following
is closest to the probability that neither of the students selected will
speak French?"}], "ideal": ["0.8100"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 10 marbles in a box, 2 are green. A person will
select 2 marbles simultaneously and at random from the box. What is the
probability that neither of the marbles selected will be green?"}],
"ideal": ["0.6222"]}
  ```
</details>

---
## [capsaicinz/Skyrat-tg](https://github.com/capsaicinz/Skyrat-tg)@[2c92211dac...](https://github.com/capsaicinz/Skyrat-tg/commit/2c92211dac3d2929db283bb0e58d2933f1607b0d)
#### Wednesday 2023-05-17 21:46:19 by SkyratBot

[MIRROR] Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool [MDB IGNORE] (#20602)

* Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool (#74744)

## About The Pull Request

Replaced the subspace amplifier in the Black Market Uplink's crafting
recipe with a signaller and a microlaser.

Added the Black Market Uplink to the maintenance loot pool.
## Why It's Good For The Game

The BMU is an _extremely_ rare device to find in rounds. It can quite
literally ONLY be found via the crafting recipe, and with how stupidly
bloated the crafting lists are, it isn't something many people know
about. All this means that a very unique and engaging gimmick item is
tragically extremely obscured.

To add to this, the recipe requires a _subspace amplifier_. These items
are UNBELIEVABLY rare - they need you to vend them from a techfab with
bluespace communication technology researched, which is fair to say is
not a common thing. Sometimes maps have them in tech storage, but even
then you have to break and enter which can be quite risky at times and
an annoying blockade the other times.

The black market items are not worth this much hassle. They are all
small cute gimmicky objects that do not heavily impact the round. By
making it not only easier to craft with common items, but also appear in
the maintenance loot pool, this will make assistants find out about it
more often, which can further incentivize them to utilize the **cargo
bounty system** to get enough money to buy their funny gadgets.

Another idea would be to make the uplink appear as a bounty item, which
would be a great way to tell players it exists and encourage them to mix
both systems together. The system for getting items is also
unnecessarily, miserably awful - your item either gets literally thrown
into space from a random direction, or it is teleported silently without
warning in 60 seconds onto a completely random place which can very much
include Security, Command, the Vault, or other high-security areas.
Needing to B&E into these areas to get your durathread vest is, uh. Not
worth it. However these aren't part of this PR, unless they're given the
A-OK. (also maybe make it cargo purchasable?)
## Changelog
:cl:
balance: Makes Black Market Uplinks more easily craftable, adds them to
uncommon maint loot pool
/:cl:

* Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [Iamgoofball/Skyrat-tg](https://github.com/Iamgoofball/Skyrat-tg)@[5a348474a0...](https://github.com/Iamgoofball/Skyrat-tg/commit/5a348474a01a07490094be828ae269f4c98b13ef)
#### Wednesday 2023-05-17 22:11:01 by SkyratBot

[MIRROR] IV drips' default transfer rate is no longer zero. [MDB IGNORE] (#20567)

* IV drips' default transfer rate is no longer zero. (#74724)

## About The Pull Request

Set default IV transfer rate to maximum (5) instead of 0.
## Why It's Good For The Game

> Set default IV transfer rate to maximum (5) instead of 0.

When you hook someone onto an IV drip, you naturally expect that to be
the end of the process - you hooked someone to a drip, and now you can
go about your day. Them needing to fiddle with buttons is bad for
several reasons:

- It is unintuitive.
IV drips don't look like machines. Their sprite doesn't reflect the fact
that you need to fiddle with the settings before they can work the same
way any other machine or computer might. And to be honest, they
shouldn't.
- It is separate from how every other server currently has it.
Yes, yes, I know that argument is very flawed and full of holes. But
what I'm trying to say with it is, effectively speaking, an extension of
the above point. In other servers, you drag-click someone to an IV drip
and there we go, it's functional. In TG, it just-so-happens to not be
functional due to what is almost definitely a recent oversight, which
very much can, has, and will lead to unnecessary frustration.
- There is no practical reason for it to be set at 0.
Imagine if chem dispensers started at +0 units and needed to be set to
+5 to continue. Or if bottles had a transfer rate of 0u. Or if guns
started with their safeties on. Even if it made sense, it would just be
frustrating and needless, and wouldn't improve the game in any
significant manner enough to offset frustration. We're here for fun, not
perfect balance or realism/verisimilitude after all.
- It's an oversight.
It was changed in #71217. Before that, it was always set to the maximum,
5u. However, presumably due to confusion (Variables that can be adjusted
ingame usually are set to zero/the minimum possible) it ended up being
changed to this.

Apparently an argument can be made that this is fine because fumbling to
get medical aid done is a part of the game. I disagree heavily - blood
bags are already stored in the cold room, something only 2/5 of the
roles in medbay even have access to, with the paramedic, virologist,
chemist all being unable to reach it. This is already enough 'fumbling'
that's necessary. If someone moved the blood bags outside the cold room
next to the IV drips, then all the better - it's a reward for medbay
being prepared.

However I wouldn't mind if someone asked me to make it so the default
transfer rate is, well, something below maximum. It's common practice in
a lot of parts of SS13 to have things set in an unoptimized state so
players can go around improving them, such as air alarms, cryogenics,
etc. Just as long as it's not literally unusable otherwise, as the
'minimum basic setup' should just be slapping on a blood bag!
## Changelog
Dunno what to put here TBH. Can't tell if it's qol, fix, balance, etc.

:cl:
qol: Set default IV transfer rate to maximum (5) instead of 0.
/:cl:

* IV drips' default transfer rate is no longer zero.

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [Iamgoofball/Skyrat-tg](https://github.com/Iamgoofball/Skyrat-tg)@[f97afbd66d...](https://github.com/Iamgoofball/Skyrat-tg/commit/f97afbd66d6631bdb5355cbf54fe630e189e4d51)
#### Wednesday 2023-05-17 22:11:01 by SkyratBot

[MIRROR] Fixes spoon overlay not updating every time [MDB IGNORE] (#20570)

* Fixes spoon overlay not updating every time (#74687)

## About The Pull Request

After bludgeoning myself one too many times with a spoon, here we are.

The spoon overlay wasn't updating to reflect that soup had been
consumed, which led to trying to eat it again and then pain.

Why do spoons hurt so much?

## Why It's Good For The Game

Less spoon related injuries.

## Changelog

:cl:
fix: spoon overlays will now update when you eat from them to reflect
that food = gone. it really is gone, you can stop beating yourself with
the spoon. oh god please stop--
/:cl:

* Fixes spoon overlay not updating every time

---------

Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [jeewan007/Accenture-Social-Buzz](https://github.com/jeewan007/Accenture-Social-Buzz)@[77eb341120...](https://github.com/jeewan007/Accenture-Social-Buzz/commit/77eb3411205f04875ab7e427bec16d474d761fa8)
#### Wednesday 2023-05-17 22:15:54 by Jeewan Singh

Add files via upload

With 100000 posts per day and 36500000 posts per year social buzz is finding hard to sort and capitalize on their top contents.

Analysis to find Social Buzz's top 5 most popular categories of content and recommendations

From our analysis you can see that the top 5 most popular categories of posts were food, culture, soccer, cooking and animals in descending order.

Food had an aggregate popularity score of almost 76000. It is very interesting to see both food and cooking within the top 5, it really shows what people enjoy consuming as content. But also interesting to see culture too. Clearly users favor "real-life" content on this platform.

Furthermore soccer is an interesting category because there is the European championships being played very soon. This presents a huge opportunity for you to differentiate your platform and to run specific content or events linked to this global spectacle.

---
## [zacharyajohnson/distro-setup](https://github.com/zacharyajohnson/distro-setup)@[6a43865cec...](https://github.com/zacharyajohnson/distro-setup/commit/6a43865cece77d2af35ee115d2be257a36388a2e)
#### Wednesday 2023-05-17 22:44:34 by Zachary Alan Johnson

Refactor how software installion works

It always bugged me that you couldn't go into a softwares
folder and run the install script since it was being
determined by the software folders setup.sh file.

So, I decided to:
1) Still allow the software setup.sh to determine what package manager
   you have.
2) Get rid of the check in setup.sh to check if software is installed.
   This makes setup.sh slightly less complex and the package manager
   usually tells you if its already installed anyway.
3) Only allow configs/scripts to be copied if the user tries to install
   the software. I should respect a person and their configs and not
   blindly override theirs. If they really want my configs, they can
   use the install scripts for them in the respective softwares folder
4) Have seperate install scripts for each package manager for
   each piece of software. This is a massive pain in the ass
   compared to what I had earlier, but the fact of the matter
   is that:
        Packages could require different installs on each distro.
        Packages may be called something different from distro to distro.
        Packages may not be avaliable on certain distros.
   This is the only way that makes sense. As I try installing stuff on
   other distros I will slowly add the scripts for their package
   managers.
5) Despite point 5, I really like the fact that someone could take
   a particular softwares folder and not have to know anything about
   the setup.sh in software to use it, so I'm keeping it.

---
## [Zindswini/u-pal](https://github.com/Zindswini/u-pal)@[c7deb7d6fe...](https://github.com/Zindswini/u-pal/commit/c7deb7d6fe3aa4256d7a79123ffc250a24165263)
#### Wednesday 2023-05-17 22:59:36 by Arcitec

fix: friendlier experience in the "yafti" first boot template

- The first screen's "Pick some applications to get started" has been replaced with a friendly welcoming message.

- The second screen's difficult-to-understand "WARNING: This will modify your Flatpaks if you are rebasing!" has been replaced with an explanation of what it actually does.

- The application setup screen is now titled "Application Installer", since the previous title sounded too much like a silly rhyme. It's a minor change.

- All Flatpaks now default to system-wide install thanks to the great work of bsherman at https://github.com/ublue-os/yafti/pull/82. This saves tons of disk space for multi-user systems.

- The "system application" category have been split up into GNOME apps and every other system app, so that people on other desktop environments don't get all the GNOME apps.

- Apps that had too vague descriptions have been renamed to their full names, such as "Backup -> Deja Dup Backups".

- All app lists have been sorted alphabetically.

- Non-inclusive language in descriptions has been changed.

- Added SteamTinkerLaunch as a suggestion for the Steam category, which is the best tool for managing Steam game configurations and Proton installations, albeit very advanced since it can do practically anything the gamer needs. :)

---
## [saltwaterterrapin/EvilHack](https://github.com/saltwaterterrapin/EvilHack)@[7e68ba7f28...](https://github.com/saltwaterterrapin/EvilHack/commit/7e68ba7f28d1ef6ef6ee56935eb86aa5160b8993)
#### Wednesday 2023-05-17 23:33:28 by saltwaterterrapin@gmail.com

Fix snuff_light_source

The two callers of snuff_light_source disagree about what it's supposed to do, and they're both wrong anyway. Make snuff_light_source work as set_lit expects, snuffing all snuffable sources on a given square. While I was at it, I also removed the snuffing code from litroom, since set_lit will snuff the player's inventory. This means that the player's inventory is only affected by drow darkness if they are within the actual area of affect of the darkness, which seems logical to me.

mpickobj also called snuff_light_source, expecting it to snuff a particular object. Instead, it could affect any light source on the square, allowing you to e.g. drop light sources in engulfers and have them stay lit, provided you were carrying another light source that had been lit for longer, which was weird. But kinda cool. But definitely wrong. Replace the snuff_light_source call with end_burn(), which targets the specific object that has been picked up.

---

