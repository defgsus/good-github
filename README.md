## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-21](docs/good-messages/2022/2022-05-21.md)


1,524,508 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,524,508 were push events containing 2,240,974 commit messages that amount to 127,410,999 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 27 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[20e4add487...](https://github.com/tgstation/tgstation/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Saturday 2022-05-21 00:02:14 by Tim

Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)


About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

---
## [MrGlockenspiel/activate-linux](https://github.com/MrGlockenspiel/activate-linux)@[6012d283ca...](https://github.com/MrGlockenspiel/activate-linux/commit/6012d283caeb096b9667ce759f0eeb92c0e99005)
#### Saturday 2022-05-21 00:52:55 by Reperak

Fix rgba_color_string returning default

Shame on me for not testing before submitting #65, and shame on the people who reviewed #65 for trusting my stupid ass.

Fixes #99

---
## [GuiltyNeko/Skyrat-tg](https://github.com/GuiltyNeko/Skyrat-tg)@[a0fa5ba3ce...](https://github.com/GuiltyNeko/Skyrat-tg/commit/a0fa5ba3ce25d019dafa88e1d606e079f7649cc6)
#### Saturday 2022-05-21 01:33:55 by SkyratBot

[MIRROR] Updates Maps And Away Missions MD [MDB IGNORE] (#13095)

* Updates Maps And Away Missions MD (#66455)

* Updates Maps And Away Missions MD

Hey there,

This was outdated for a bit, so I decided to pretty it up and make a few things a bit more explicit.

I alphabetized the maps since we don't really prioritize one-over-the-other (except Meta now being the default map instead of the non-existent Box).

I also alphabetized Removed Station Maps, and removed the "outdated" (they are all outdated, or will definitely all be outdated by the time a reader reads this).

I elaborated a bit more on how station maps are loaded these days (correct me if I am wrong).

Standardized how we show code paths.

Gave explicit instructions on never using Dream Maker to map, and linking two programs that we tell anyone who wanders in on the Discord to use anyways (please do inform me if we should not do this- but Dream Maker just fucking sucks shit).

I also fixed up some language around the Away Missions part, and added a newer section for the Map Depot since I do not believe it is discussed elsewhere on the main repository (as well as a short warning on anyone who things they can get Phobos or something running out-of-the-box).

Alright, cool.

* Updates Maps And Away Missions MD

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [newstools/2022-information-nigeria](https://github.com/newstools/2022-information-nigeria)@[0ea375acce...](https://github.com/newstools/2022-information-nigeria/commit/0ea375accea522e9862659183a21d64cfa836167)
#### Saturday 2022-05-21 03:09:49 by Billy Einkamerer

Created Text For URL [www.informationng.com/2022/05/woman-becomes-physically-disabled-after-reportedly-being-cursed-by-her-boyfriends-wife-video.html]

---
## [Atom-X-Devs/android_kernel_xiaomi_sm7325](https://github.com/Atom-X-Devs/android_kernel_xiaomi_sm7325)@[cd8aebb3a9...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_sm7325/commit/cd8aebb3a9a762c410e75a36cd8db42512a3fc3b)
#### Saturday 2022-05-21 06:02:09 by Daniel Vetter

dma_resv: prime lockdep annotations

Full audit of everyone:

- i915, radeon, amdgpu should be clean per their maintainers.

- vram helpers should be fine, they don't do command submission, so
  really no business holding struct_mutex while doing copy_*_user. But
  I haven't checked them all.

- panfrost seems to dma_resv_lock only in panfrost_job_push, which
  looks clean.

- v3d holds dma_resv locks in the tail of its v3d_submit_cl_ioctl(),
  copying from/to userspace happens all in v3d_lookup_bos which is
  outside of the critical section.

- vmwgfx has a bunch of ioctls that do their own copy_*_user:
  - vmw_execbuf_process: First this does some copies in
    vmw_execbuf_cmdbuf() and also in the vmw_execbuf_process() itself.
    Then comes the usual ttm reserve/validate sequence, then actual
    submission/fencing, then unreserving, and finally some more
    copy_to_user in vmw_execbuf_copy_fence_user. Glossing over tons of
    details, but looks all safe.
  - vmw_fence_event_ioctl: No ttm_reserve/dma_resv_lock anywhere to be
    seen, seems to only create a fence and copy it out.
  - a pile of smaller ioctl in vmwgfx_ioctl.c, no reservations to be
    found there.
  Summary: vmwgfx seems to be fine too.

- virtio: There's virtio_gpu_execbuffer_ioctl, which does all the
  copying from userspace before even looking up objects through their
  handles, so safe. Plus the getparam/getcaps ioctl, also both safe.

- qxl only has qxl_execbuffer_ioctl, which calls into
  qxl_process_single_command. There's a lovely comment before the
  __copy_from_user_inatomic that the slowpath should be copied from
  i915, but I guess that never happened. Try not to be unlucky and get
  your CS data evicted between when it's written and the kernel tries
  to read it. The only other copy_from_user is for relocs, but those
  are done before qxl_release_reserve_list(), which seems to be the
  only thing reserving buffers (in the ttm/dma_resv sense) in that
  code. So looks safe.

- A debugfs file in nouveau_debugfs_pstate_set() and the usif ioctl in
  usif_ioctl() look safe. nouveau_gem_ioctl_pushbuf() otoh breaks this
  everywhere and needs to be fixed up.

v2: Thomas pointed at that vmwgfx calls dma_resv_init while it holds a
dma_resv lock of a different object already. Christian mentioned that
ttm core does this too for ghost objects. intel-gfx-ci highlighted
that i915 has similar issues.

Unfortunately we can't do this in the usual module init functions,
because kernel threads don't have an ->mm - we have to wait around for
some user thread to do this.

Solution is to spawn a worker (but only once). It's horrible, but it
works.

v3: We can allocate mm! (Chris). Horrible worker hack out, clean
initcall solution in.

v4: Annotate with __init (Rob Herring)

Cc: Rob Herring <robh@kernel.org>
Cc: Alex Deucher <alexander.deucher@amd.com>
Cc: Christian König <christian.koenig@amd.com>
Cc: Chris Wilson <chris@chris-wilson.co.uk>
Cc: Thomas Zimmermann <tzimmermann@suse.de>
Cc: Rob Herring <robh@kernel.org>
Cc: Tomeu Vizoso <tomeu.vizoso@collabora.com>
Cc: Eric Anholt <eric@anholt.net>
Cc: Dave Airlie <airlied@redhat.com>
Cc: Gerd Hoffmann <kraxel@redhat.com>
Cc: Ben Skeggs <bskeggs@redhat.com>
Cc: "VMware Graphics" <linux-graphics-maintainer@vmware.com>
Cc: Thomas Hellstrom <thellstrom@vmware.com>
Reviewed-by: Thomas Hellstrom <thellstrom@vmware.com>
Reviewed-by: Christian König <christian.koenig@amd.com>
Reviewed-by: Chris Wilson <chris@chris-wilson.co.uk>
Tested-by: Chris Wilson <chris@chris-wilson.co.uk>
Signed-off-by: Daniel Vetter <daniel.vetter@intel.com>
Link: https://patchwork.freedesktop.org/patch/msgid/20191104173801.2972-1-daniel.vetter@ffwll.ch
Signed-off-by: Divyanshu-Modi <divyan.m05@gmail.com>
Change-Id: Id506bcb6fd1e325c90facbbc36332cfd33a4fb55

---
## [PKRoma/git](https://github.com/PKRoma/git)@[bdaf1dfae7...](https://github.com/PKRoma/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Saturday 2022-05-21 06:19:05 by Tao Klerks

branch: new autosetupmerge option 'simple' for matching branches

With the default push.default option, "simple", beginners are
protected from accidentally pushing to the "wrong" branch in
centralized workflows: if the remote tracking branch they would push
to does not have the same name as the local branch, and they try to do
a "default push", they get an error and explanation with options.

There is a particular centralized workflow where this often happens:
a user branches to a new local topic branch from an existing
remote branch, eg with "checkout -b feature1 origin/master". With
the default branch.autosetupmerge configuration (value "true"), git
will automatically add origin/master as the upstream tracking branch.

When the user pushes with a default "git push", with the intention of
pushing their (new) topic branch to the remote, they get an error, and
(amongst other things) a suggestion to run "git push origin HEAD".

If they follow this suggestion the push succeeds, but on subsequent
default pushes they continue to get an error - so eventually they
figure out to add "-u" to change the tracking branch, or they spelunk
the push.default config doc as proposed and set it to "current", or
some GUI tooling does one or the other of these things for them.

When one of their coworkers later works on the same topic branch,
they don't get any of that "weirdness". They just "git checkout
feature1" and everything works exactly as they expect, with the shared
remote branch set up as remote tracking branch, and push and pull
working out of the box.

The "stable state" for this way of working is that local branches have
the same-name remote tracking branch (origin/feature1 in this
example), and multiple people can work on that remote feature branch
at the same time, trusting "git pull" to merge or rebase as required
for them to be able to push their interim changes to that same feature
branch on that same remote.

(merging from the upstream "master" branch, and merging back to it,
are separate more involved processes in this flow).

There is a problem in this flow/way of working, however, which is that
the first user, when they first branched from origin/master, ended up
with the "wrong" remote tracking branch (different from the stable
state). For a while, before they pushed (and maybe longer, if they
don't use -u/--set-upstream), their "git pull" wasn't getting other
users' changes to the feature branch - it was getting any changes from
the remote "master" branch instead (a completely different class of
changes!)

An experienced git user might say "well yeah, that's what it means to
have the remote tracking branch set to origin/master!" - but the
original user above didn't *ask* to have the remote master branch
added as remote tracking branch - that just happened automatically
when they branched their feature branch. They didn't necessarily even
notice or understand the meaning of the "set up to track 'origin/master'"
message when they created the branch - especially if they are using a
GUI.

Looking at how to fix this, you might think "OK, so disable auto setup
of remote tracking - set branch.autosetupmerge to false" - but that
will inconvenience the *second* user in this story - the one who just
wanted to start working on the topic branch. The first and second
users swap roles at different points in time of course - they should
both have a sane configuration that does the right thing in both
situations.

Make this "branches have the same name locally as on the remote"
workflow less painful / more obvious by introducing a new
branch.autosetupmerge option called "simple", to match the same-name
"push.default" option that makes similar assumptions.

This new option automatically sets up tracking in a *subset* of the
current default situations: when the original ref is a remote tracking
branch *and* has the same branch name on the remote (as the new local
branch name).

Update the error displayed when the 'push.default=simple' configuration
rejects a mismatching-upstream-name default push, to offer this new
branch.autosetupmerge option that will prevent this class of error.

With this new configuration, in the example situation above, the first
user does *not* get origin/master set up as the tracking branch for
the new local branch. If they "git pull" in their new local-only
branch, they get an error explaining there is no upstream branch -
which makes sense and is helpful. If they "git push", they get an
error explaining how to push *and* suggesting they specify
--set-upstream - which is exactly the right thing to do for them.

This new option is likely not appropriate for users intentionally
implementing a "triangular workflow" with a shared upstream tracking
branch, that they "git pull" in and a "private" feature branch that
they push/force-push to just for remote safe-keeping until they are
ready to push up to the shared branch explicitly/separately. Such
users are likely to prefer keeping the current default
merge.autosetupmerge=true behavior, and change their push.default to
"current".

Also extend the existing branch tests with three new cases testing
this option - the obvious matching-name and non-matching-name cases,
and also a non-matching-ref-type case. The matching-name case needs to
temporarily create an independent repo to fetch from, as the general
strategy of using the local repo as the remote in these tests
precludes locally branching with the same name as in the "remote".

Signed-off-by: Tao Klerks <tao@klerks.biz>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [mszeles/a-hamunish-humanish-thoughtishish](https://github.com/mszeles/a-hamunish-humanish-thoughtishish)@[0c2a534d64...](https://github.com/mszeles/a-hamunish-humanish-thoughtishish/commit/0c2a534d6450b6c0f17ab66e0e013360f7e8bca6)
#### Saturday 2022-05-21 06:41:18 by Miklos Szeles

Nester: Another thought from my brother?
Miki: Yep.
McMuck: Just 2 more and we can publish it. I smell money here.
Miki: Well, I doubt we will see money from this, but I hope at least some people will think about how they can make Scrum better.
Nikolai: Nobody cares about your bullshit. "Humanish Agile", "Feel good agile", nobody cares about how developers feel.
Miki: That is the problem, exactly.

---
## [amir73il/kdevops](https://github.com/amir73il/kdevops)@[867ccb7540...](https://github.com/amir73il/kdevops/commit/867ccb754066ad7140a682a92973c4ac6780a437)
#### Saturday 2022-05-21 07:18:31 by Luis Chamberlain

reboot-limit: add a systemd-analyze clutch at bootup

If you run systemd-analyze at bootup it may fail with:

$ sudo systemd-analyze
Bootup is not yet finished (org.freedesktop.systemd1.Manager.FinishTimestampMonotonic=0).
Please try again later.
Hint: Use 'systemctl list-jobs' to see active jobs

When running the reboot-limit test demo workflow to test to see
how many boots can happen without failure on a system we need
then to add a wait-for-boot-to-complete clutch before we run
the systemd-analyze (when that is enabled).

We can accomplish this with:

systemctl is-system-running --wait

So add that if before we collect systemd-analyze results.
This is only applicable when CONFIG_REBOOT_LIMIT_ENABLE_SYSTEMD_ANALYZE=y.
Later on we *may* want to just use this and remove the silly
arbitrary delay on bootup post_reboot_delay. Using this
$(systemctl is-system-running --wait) may be nice for complex nodes
where bootup may take a while, otherwise we're just rebooting *as*
soon as the post_reboot_delay completes and perhaps that may do
some insane things.

But since CONFIG_REBOOT_LIMIT_ENABLE_SYSTEMD_ANALYZE=y is the default
today we simpley force using $(systemctl is-system-running --wait)
systemd-analyze is going to be used, that is always by default today
anyways.

We can later make it a strong requirement all the time even if
you don't have CONFIG_REBOOT_LIMIT_ENABLE_SYSTEMD_ANALYZE=y, but
for now this makes sense as-is as we do want to try to speed up
reboots as much as possible.

Signed-off-by: Luis Chamberlain <mcgrof@kernel.org>

---
## [infogrind/git](https://github.com/infogrind/git)@[07564773c2...](https://github.com/infogrind/git/commit/07564773c2569d012719ab9e26b9b27251f3d354)
#### Saturday 2022-05-21 07:22:54 by Ævar Arnfjörð Bjarmason

compat: auto-detect if zlib has uncompress2()

We have a copy of uncompress2() implementation in compat/ so that we
can build with an older version of zlib that lack the function, and
the build procedure selects if it is used via the NO_UNCOMPRESS2
$(MAKE) variable.  This is yet another "annoying" knob the porters
need to tweak on platforms that are not common enough to have the
default set in the config.mak.uname file.

Attempt to instead ask the system header <zlib.h> to decide if we
need the compatibility implementation.  This is a deviation from the
way we have been handling the "compatiblity" features so far, and if
it can be done cleanly enough, it could work as a model for features
that need compatibility definition we discover in the future.  With
that goal in mind, avoid expedient but ugly hacks, like shoving the
code that is conditionally compiled into an unrelated .c file, which
may not work in future cases---instead, take an approach that uses a
file that is independently compiled and stands on its own.

Compile and link compat/zlib-uncompress2.c file unconditionally, but
conditionally hide the implementation behind #if/#endif when zlib
version is 1.2.9 or newer, and unconditionally archive the resulting
object file in the libgit.a to be picked up by the linker.

There are a few things to note in the shape of the code base after
this change:

 - We no longer use NO_UNCOMPRESS2 knob; if the system header
   <zlib.h> claims a version that is more cent than the library
   actually is, this would break, but it is easy to add it back when
   we find such a system.

 - The object file compat/zlib-uncompress2.o is always compiled and
   archived in libgit.a, just like a few other compat/ object files
   already are.

 - The inclusion of <zlib.h> is done in <git-compat-util.h>; we used
   to do so from <cache.h> which includes <git-compat-util.h> as the
   first thing it does, so from the *.c codes, there is no practical
   change.

 - Until objects in libgit.a that is already used gains a reference
   to the function, the reftable code will be the only one that
   wants it, so libgit.a on the linker command line needs to appear
   once more at the end to satisify the mutual dependency.

 - Beat found a trick used by OpenSSL to avoid making the
   conditionally-compiled object truly empty (apparently because
   they had to deal with compilers that do not want to see an
   effectively empty input file).  Our compat/zlib-uncompress2.c
   file borrows the same trick for portabilty.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Helped-by: Beat Bolli <dev+git@drbeat.li>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [LiMee233/device_xiaomi_sm8250-common](https://github.com/LiMee233/device_xiaomi_sm8250-common)@[4130f38d42...](https://github.com/LiMee233/device_xiaomi_sm8250-common/commit/4130f38d42d2fdd4c79ca2c9911bf2b5067daf54)
#### Saturday 2022-05-21 08:04:57 by LiMee233

am8250-common: Keep WeChat alive.
* Fuck you tencent.

To be noticed that this may cause WeChat ANR, but don't affect
functionally.

---
## [weimzh/duckstation](https://github.com/weimzh/duckstation)@[f9212363d3...](https://github.com/weimzh/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Saturday 2022-05-21 10:09:59 by IlDucci

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ce28fd02cc...](https://github.com/mrakgr/The-Spiral-Language/commit/ce28fd02cccef7a57471919b99c2f7fdee3b0257)
#### Saturday 2022-05-21 10:31:34 by Marko Grdinić

"8:30am. I am up. Yesterday really exhausted me. Today the first thing on my agenda is to start the download for the last part, make a post on the Moi forum asking the author how he would fillet the rig door. After that I'll watch some of those Rhino troubleshooting vids. Let me start with the first one.

I need to make sure not to time out the capcha. This is the last part of the series.

This just shows it is not good to restrict yourself to any one program. I never thought I would dive into Zbrush, but I didn't disregard it as a possibility. And now that possibility is manifesting itself. It seems I will be studying Zbrush quite a bit in the next month. I still want to finish the hard surface course.

Let me make that post and then I'll do my morning reading.

http://moi3d.com/forum/lmessages.php?webtag=MOI&msg=9149.4

> Hi Jakub, yes thin pointy areas like you show there can be difficult to get filleted. You might try exporting to a different CAD program that has more robust filleting than what MoI has, some candidates for that would be ViaCAD, Fusion360, or OnShape. They may also have some difficulty with the kind of junctures you have here though.

> That piece coming down and ending at a point is at about a 90 degree angle to the other surfaces and filleting is going to have problems making junctures in a tight space like that. I'm not really quite sure what the proper result across that would be. I'll see if I can come up with any tips, it may be that filleting just isn't going to be feasible there and you might need to use other techniques like trimming away some space and putting in a blend surface instead. But that also might be difficult with the sharp 90 degree piece in a small area too.

Ah, right, I need to keep blend in mind. It completely slipped my mind, but I could have used that yesterday.

9:05am. Actually instead of asking and wasting the author's time I tried separating the front door and realized something. For whatever reason, the rig front door has a micro surface inside of it. It looks like a a line. This would definitely cause filleting to fail. And doing something like extending it by 1.001 might not be enough to get rid of it properly.

9:10am. Yeah, if I get rid of it, and then planar the face it is on, the fillet starts working. That expains it.

I am thinking, did I maybe merge that hole twice. The merge did a weird thing there. In the future whenver I have fillet troubles I should isolate the offending part and check for these kinds of problem.

9:20am. I won't fillet the rig's front door, but I'll export the new version and import it into the scene.

Oh, I just realized something big. If you click on an object's rotate icon, you get the circular handles.

Wow, that would have made the rotation so much easier in varius places I've used it in the past. It is really is problematic to use the regular tool for it.

Hmmm, actually that is true only up to a point. With this tool, unlike in Blender I don't think I can set the origin. Well, nevermind then.

9:35am. As the last note, had I bothered separating out that object that was giving me trouble yesterday, I bet I would have found those microsurfaces. The cut that I did seemed to have worked, but maybe due to numerical inaccuracy it resulted in a very close edge. In the future I need to be more conscious of this.

I've had plenty of trouble cutting simple boxes exactly along the edges yesterday and had to resort to extrusion so I could learn from this experience and try my best to avoid having edges overlap.

9:45am. Let me chill for a bit here. After that come the Rhino troubleshotting vids.

10:30am. Let me start. I've played around enough.

https://youtu.be/L-FYJRKebIc
Why Boolean Commands Fail in Rhino 6: Jewelry CAD Design Tutorial

Let me watch this.

https://youtu.be/L-FYJRKebIc?t=244

This is fairly instructive. I did not know that overlapping sweeps could fail like this.

https://youtu.be/enc5dLYfFJg
How to Fix a Boolean Union Manually - Part 1

Let me watch this for a bit.

https://youtu.be/enc5dLYfFJg?t=446

I do not understand why he is messing with points here. Can't he just select the surface and scale 1d it in the direction he needs it to go. Better yet, just delete the surface and loft it to the other side.

https://youtu.be/enc5dLYfFJg?t=575
> Selecting a surface, untrimming it and trimming it.

Hmmm...

> Trim works on curves, surfaces, or solids. The general procedure is to first select the object to be trimmed, and then run the Trim command. Next select the cutting objects, then select which pieces to discard. If you want to keep all the pieces instead of discarding any, then click Done (or right-click in a viewport) without selecting anything at that final stage.

This is in Moi.

11:05am. https://youtu.be/enc5dLYfFJg?t=910

He trimmed that curve from above. In Moi I guess I'd need to flatten it first.

These are interesting techniques. Even with all this headache, I'd rather do this kind of fixing rather than mess with poly topology.

11:05am. Interesting that he found a tiny surface inside the object. I had a similar kind of problem with the rig.

https://youtu.be/ofeASybhNAk?t=345

I would have lofted it, but I should keep the 2 rail sweep in mind as well.

Ah, I see. I could have used this for the clam clipper. I have been thinking whether it would have been possible to do what I did there better, because I did resort to a somewhat hacky solution and it turns out, it is.

https://youtu.be/ofeASybhNAk?t=353

I think I am starting to understand what a manual boolean workflow in CAD programs is like. it is using trim and joining various surfaces manually. Yeah, I see it now.

https://youtu.be/ofeASybhNAk?t=397

I am a bit confused as to what untrim is supposed to be doing.

The Untrim command removes trim curves and surfaces joined at trim curves from a surface.

I am not sure what these trim curves and surfaces are. Are they maybe those micro surfaces I've been having trouble with?

https://youtu.be/ofeASybhNAk?t=558

What a nightmare model. I'd have just rebuilt it.

https://youtu.be/ofeASybhNAk?t=631

Instead of doing all of this, he should have just bisected the model and mirrored it. He got one side right a while ago and now he is back in the fray.

11:30am. https://youtu.be/VsV0LIHGOdk
Why boolean union fail even all parts are solid polysurface: Q/A Session (2019)

Let me watch this one.

11:35am. https://youtu.be/VsV0LIHGOdk?t=194

Why is she rebuilding the curve?

11:35am. How are people getting all these naked edges in Rhino? It boggles my mind.

I am guessing that the curve rebuilding is just to make them look better rather than improve the booleaning.

https://youtu.be/7LoDcnxl11w
What are Boolean Functions and What to do When They Fail!

Let me also check this video out. Then I'll take a look at fillets.

https://youtu.be/7LoDcnxl11w?t=334

* Direction of surfaces
* Singularity or coplanar
* Self intersecting

https://youtu.be/7LoDcnxl11w?t=796

I wonder how she will resolve these issues?

https://youtu.be/7LoDcnxl11w?t=878

I see, that is one way of doing it. What about the other kind of error?

https://youtu.be/7LoDcnxl11w?t=914
> This is one of the reasons why I don't love a Pipe. I prefer a sweep.

Does sweep not have the same problem? Let me try it in Moi.

Yeah, the isocurve bends on itself. So Moi has the same problem. The solution should be to offset the curve on both sides and do a two rail sweep.

12:05pm. https://youtu.be/iWIk4emlqf0
Rhino 3D CAD Technique #9: Why does "fillet" not working ? (有中文字幕)

Let me watch this.

https://youtu.be/iWIk4emlqf0?t=455

This is an interesting technique. I forgot that I could have done something like this.

12:25pm. I am getting lost in thought. Let me have breakfast here. After that I will get back into modeling.

Let me just unpack the course. It finished downloading. This is some hard compression.

12:30pm. 12 parts of about 1.5 hours each. This will take a while. This is not even factoring the timelapses.

Let me have breakfast here. I guess June will be the month I really master modeling in Zbrush."

---
## [ParadiseSS13/Paradise](https://github.com/ParadiseSS13/Paradise)@[ab7a358506...](https://github.com/ParadiseSS13/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Saturday 2022-05-21 12:35:12 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [GetComponents/Catflife](https://github.com/GetComponents/Catflife)@[0fa986c6d0...](https://github.com/GetComponents/Catflife/commit/0fa986c6d02db3f755d24f3061727dcabe3f3cdc)
#### Saturday 2022-05-21 12:42:34 by Jan Pluschkell

Implemented Tims shit bitch fuck + UI render layer

---
## [ianfab/Fairy-Stockfish](https://github.com/ianfab/Fairy-Stockfish)@[57bda214fc...](https://github.com/ianfab/Fairy-Stockfish/commit/57bda214fcc8cd9d40fd3fd6f43c766ac9f88662)
#### Saturday 2022-05-21 13:28:48 by Snowmoondaphne

Update variants.ini

I'm really sorry to tell you this,,,

The positions of Black's Queen and Cardinal have been swapped in Pandemonium. Therefore, the definition has changed and it is necessary to modify it

[pandemonium]
variantTemplate = shogi
pieceToCharTable = PNBRFSA.UV.++++++++.++Kpnbrfsa.uv.++++++++.++k
maxFile = 9
maxRank = 9
pocketSize = 9
startFen = rnbsksbnr/2+f1+u1+a2/p1p1p1p1p/4v4/9/4V4/P1P1P1P1P/2+F1+U1+A2/RNBSKSBNR[] w - - 0 1
customPiece1 = o:NA
customPiece2 = s:WF
customPiece3 = u:D
customPiece4 = w:DWF
cast = false
pieceDrops = true
capturesToHand = true
immobilityIllegal = true
soldier = p
knight = n
bishop = b
rook = r
king = k
queen = q
commoner = g
dragonHorse = h
bers = d
alfil = a
archbishop = c
chancellor = m
fers = f
wazir = v
centaur = t
promotionRank = 7
promotedPieceType = p:g n:o b:h r:d a:c v:m f:q s:w u:t
doubleStep = false
perpetualCheckIllegal = true
nMoveRule = 0
nFoldValue = loss
stalemateValue = loss

Could you please modify the definition like this?

Sorry again for the troublesome request,,,

---
## [lyqd-lang/seawater](https://github.com/lyqd-lang/seawater)@[4c24ebef60...](https://github.com/lyqd-lang/seawater/commit/4c24ebef6051d63fb060a66be635ed0ca3838d2a)
#### Saturday 2022-05-21 13:40:48 by Woffle

actually no, fuck windows

damn microsoft and their stupid os

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[77215d9d77...](https://github.com/microsoft/terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Saturday 2022-05-21 14:15:10 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [ksant0s/android_kernel_samsung_universal8895](https://github.com/ksant0s/android_kernel_samsung_universal8895)@[faba864101...](https://github.com/ksant0s/android_kernel_samsung_universal8895/commit/faba864101d721a9370e7efd0a448e40a59b0154)
#### Saturday 2022-05-21 14:29:57 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, fslmc, tbsvc, and typec as they don't exist here
     Add of to avoid backporting two larger patches]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Ta180m/gitea](https://github.com/Ta180m/gitea)@[3725fa28cc...](https://github.com/Ta180m/gitea/commit/3725fa28ccc01ab08060f591f894ea6443a348e8)
#### Saturday 2022-05-21 15:35:49 by Gusted

Improve UI on mobile (#19546)

Start making the mobile experience not painful and be actually usable. This contains a few smaller changes to enhance this experience.

- Submit buttons on the review forms aren't columns anymore and are now allowed to be displayed on one row.
- The label/milestone & New Issue buttons were given each own row even tough, there's enough place to do it one the same row. This commit fixes that.
- The issues+Pull tab on repo's has a third item besides the label/milestone & New Issue buttons, the search bar. On desktop there's enough place to do this on one row, for mobile it isn't, currently it was using for each item a new row. This commits fixes that by only giving the searchbar a new row and have the other two buttons on the same row.
- The notification table will now be show a scrollbar instead of overflow.
- The repo buttons(Watch, Star, Fork) on mobile were showing quite big and the SVG wasn't even displayed on the same line, if the count of those numbers were too high it would even overflow. This commit removes the SVG, as there isn't any place to show them on the same row and allows them to have a new row if the counts of those buttons are high.
- The admin page can show you a lot of interesting information, on mobile the System Status + Configuration weren't properly displayed as the margin's were too high. This commit fixes that by reducing the margin to a number that makes sense on mobile.
- Fixes to not overflow the tables but instead force them to be scrollable.
- When viewing a issue or pull request, the comments aren't full-width but instead 80% and aligned to right, on mobile this is a annoyance as there isn't much width to begin with. This commits fixes that by forcing full-width and removing the avatars on the left side and instead including them inline in the comment header.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[4860909469...](https://github.com/treckstar/yolo-octo-hipster/commit/486090946920611d663893b26bcc6e0a3127f424)
#### Saturday 2022-05-21 16:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER](https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER)@[c0c537eaf6...](https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/commit/c0c537eaf62ee646051e179d56b6e2bf7ed29885)
#### Saturday 2022-05-21 16:58:22 by 1212-5858

153974 2020 - 1516523 - 93715    12-12, 5858

# STATE FARM ASSURANCES FUNDS TRUST
test this here. [^1]
![image](https://user-images.githubusercontent.com/70865813/169647568-ac8dec51-531a-4617-be0e-8761b9743b7d.png)


---
>					
>		2020-06-08		40-17G
>						Fidelity Bond [Rule 17G-1(g)]
>		https://www.sec.gov/Archives/edgar/data/0000093715/000009371520000003/aft2020.txt
>					
>		2020-07-28		N-CSRS				
>						SEMI-ANNUAL REPORT
>		https://www.sec.gov/Archives/edgar/data/0000093715/000119312520200810/d913497dncsrs.htm
> 					
>		2020-11-30  	N-CEN
>						ANNUAL REPORT FOR REGISTERED INVESTMENT COMPANIES
>		https://www.sec.gov/Archives/edgar/data/0000093715/000114554921006167/xslFormN-CEN_X01/primary_doc.xml
>					
>		2021-07-23		N-CSRS
>						SEMI-ANNUAL REPORT
>		https://www.sec.gov/Archives/edgar/data/0000093715/000119312521222842/d763005dncsrs.htm
>					
>		2021-11-30  	N-CEN
>						ANNUAL REPORT FOR REGISTERED INVESTMENT COMPANIES	
>			https://www.sec.gov/Archives/edgar/data/0000093715/000114554922006149/xslFormN-CEN_X01/primary_doc.xml
>#### Applications for Deregistration under Section 8(f) of the Investment Company Act of 1940	
###### 2021-10-29<br>
>>###### Notice of Deregistration under the Investment Company Act of 1940<br>
>>	  Form N-8F	
>>	  https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005616/filename1.pdf
>>
>>	  Form N-8F
>>	  https://www.sec.gov/Archives/edgar/data/0000093715/000119312521278180/d222043dn8f.htm
######	2021-11-24
>>###### Investment Company Act Release No. 34411<br>
>>	  ORDER No. 34425
>>	  https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf


![image](https://user-images.githubusercontent.com/70865813/169647584-475d3af1-8e51-4a99-9360-b3d20b3100b0.png)

#### Fund Surviving the Merger		
				CIK ID:	1516523 
				Advisers Investment Trust 
				Investment Company Act file number [811-22538]
				LEI: 549300BG52TB5QPLYE22
				
				2021-09-30 	ANNUAL REPORT FOR REGISTERED INVESTMENT COMPANIES	
				https://www.sec.gov/Archives/edgar/data/0001516523/000114554921074536/xslFormN-CEN_X01/primary_doc.xml

				2022-01-31	MONTHLY SCHEDULE OF PORTFOLIO HOLDINGS
				[N-MFP2]
				https://www.sec.gov/Archives/edgar/data/0001516523/000114554922005596/xslN-MFP2_X01/primary_doc.xml

				40-17G  January 1, 2022 to 12:01 a.m. on    January 1, 2023
				https://www.sec.gov/Archives/edgar/data/0001516523/000119312522025502/d207567d4017g.htm![167291117-656e2a28-7591-4ecf-b5e0-bf5e4d58b678](https://user-images.githubusercontent.com/70865813/167291658-0c930e39-96bc-42ff-b3b4-37dbef94d2f9.png)
![167291117-656e2a28-7591-4ecf-b5e0-bf5e4d58b678](https://user-images.githubusercontent.com/70865813/167291661-e153c08f-0b71-40e8-ac23-731479500e4b.png)

   STFGX
                        Date    Close/Last    Adjusted Close

                        11/10/2021    121.17    121.17
                        11/11/2021    120.77    120.77
                        11/12/2021    121.48    121.48
                                                    __________________________
                                                    11/15/2021    121.34    121.34
                                                    11/16/2021    121.6    121.6
                                                    11/17/2021    121.52    121.52
                                                    11/18/2021    121.87    121.87
                                                    11/19/2021    121.69    121.69
                                                    11/22/2021    121.64    121.64
                                                    11/23/2021    121.79    121.79
                                                    11/24/2021    121.85    121.85
                                                    11/26/2021    119.44    119.44
                                                    11/29/2021    120.48    120.48
                                                    11/30/2021    118.5    118.5
                                                    12/1/2021    117.78    117.78
                                                    12/2/2021    118.95    118.95
                                                    12/3/2021    118.46    118.46
                                                    12/6/2021    119.95    119.95
                                                    12/7/2021    121.89    121.89
                                                    12/8/2021    122.51    122.51
                                                    12/9/2021    121.99    121.99
                                                    12/10/2021    123.25    123.25
                                                    12/13/2021    122.76    122.76
                                                    12/14/2021    122.16    122.16
                                                    12/15/2021    124.36    124.36
                                                    12/16/2021    123.55    123.55
                                                    12/17/2021    121.93    121.93
                                                    
                                                        --------------------------------------------------------------------------------------
                                                                                __________________________
                                                                                12/20/2021    120.72    120.72
                                                                                12/21/2021    106.35    106.35
                                                                                12/22/2021    107.39    107.39
                                                                                12/23/2021    108.08    108.08
                                                                                12/27/2021    109.52    109.52
                                                                                12/28/2021    109.57    109.57
                                                                                12/29/2021    109.82    109.82
                                                                                12/30/2021    109.55    109.55
                                                                                12/31/2021  
                                                    
						    				just get worse.. 
						     				05/06/2022   $100.14    ------

					
						    
                                                    

![167291170-f30a3492-9be0-4b43-b958-aa909c839c60](https://user-images.githubusercontent.com/70865813/167291688-2a2363f1-8dea-4e9f-93c2-3258fd7a3669.png)


kept moving East, my best guess.


https://github.com/BSCPGROUPHOLDINGSLLC

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/7

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/6

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER


![Screenshot_20220413-233955_Yahoo Mail](https://user-images.githubusercontent.com/70865813/169640706-2bb46efd-1443-4c0b-a988-c77cf2b0341d.jpg)

12-16-2021   	13:53 UTC
	----------	JAMES.GORMAN@MORGANSTANLEY.COM

12-16-2021	14:33 EST
	----------	LZUCKER@MSKYLINE.COM
	----------	LEGAL@MSKYLINE.COM
	----------	MHARVEY13@BLOOMBERG.NET
![Screenshot_20220324-043009_Yahoo Mail](https://user-images.githubusercontent.com/70865813/169640877-ef653d85-64a5-4f31-84d0-69a54a3d62aa.jpg)



![Screenshot_20220407-164804_Yahoo Mail](https://user-images.githubusercontent.com/70865813/169648064-f9e93568-ebc4-41b9-bfd7-c83386351208.jpg)


Morgan Stanley & Co. LLC
UNDER SEC FILE NUMBER: 008-15869 AND CRD 8209
     PREMIUMS RECEIVED IN FISCAL YEAR 2020 >> $95,933
     PREMIUMS RECEIVED IN FISCAL YEAR 2020 >> $76,642
** https://www.sec.gov/Archives/edgar/data/0000093715/000114554921006167/xslFormN-CEN_X01/primary_doc.xml
** https://www.sec.gov/Archives/edgar/data/0000093715/000114554922006149/xslFormN-CEN_X01/primary_doc.xml
****
LEFT THEIR OLD CUSTOMER: STATE FARM ASSOCIATES’ FUNDS TRUST.
https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf

FOR: Advisers Investment Trust 
         CIK: 1516523, SEC ID: 811-22538 

MORGAN STANLEY & CO.
UNDER A DIFFERENT CRD #149777,;
SEC FILE NUMBER: 008-68191 
--- INVITED A LARGER BODY OF RISK, WITHOUT ANY NOTICE TO ANY OF THOSE SERVICE PROVVIDERS, AUDITORS - 
https://www.sec.gov/Archives/edgar/data/0001516523/000114554921074536/xslFormN-CEN_X01/primary_doc.xml

NO DIFFERENT THAN WHAT I EXPERIENCED DEALING WITH THE ZUCKERS, AND ALL OF THEIR COUNSELORS--- WARNED THEM IN JUNE OF 2020.
----- CURRENTLY THE   CIK: 1516523, SEC ID: 811-22538  HAS $0.00 ASSETS UNDER MANAGEMENT. 
>> KEEP IGNORING THOSE TAX-EVASIONS IN THE NOTE, THE FDIC DOES NOT PERMIT CUSTODY OF THOSE ASSETS AT ANY US DEPOSITORY INSTITUTION.
>> AS SEEN IN THE PROCEEDINGS IN 153974/2020, THE ZUCKERS, AND THE INGRAM FIRM BROUGHT IN THE MARVELS OF WILSONELSER  TO ASSIST WITH THEIR PROCEDURES.... 

AFTER 27-YEARS, STATE FARM ASSOCIATES’ FUNDS TRUST : 
^^ Above named applicant filed an application on September 21, 2021, requesting an order under
section 8(f) of the Act declaring that it has ceased to be an investment company.
https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf

![image](https://user-images.githubusercontent.com/70865813/169647584-475d3af1-8e51-4a99-9360-b3d20b3100b0.png)




Remember to visit Governor Hochul on Facebook, where you can receive regular updates on the actions of the Governor.


ForwardedMessage.eml
Subject:
93715 - 153974/2020 --- 1516523
From:
B D2022 <ms60710444266@yahoo.com>
Date:
5/21/2022, 12:46 PM
To:
Governor Hochul <governor.hochul@exec.ny.gov>, "BK01 (CB)" <bk01@cb.nyc.gov>, "AREYNOSO@mskyline.com" <AREYNOSO@mskyline.com>
CC:
TEDHERMANSON@northmarq.com, jpetit@mccarter.com, ashley.humphries@wilsonelser.com, "alex.zuluaga@ey.com" <alex.zuluaga@ey.com>, "david.brown1@ey.com" <david.brown1@ey.com>, Deborah M Jones <Deborah.Jones@ey.com>, "info@ey.com" <info@ey.com>, "jacqueline.kelley@ey.com" <jacqueline.kelley@ey.com>, "karim.anani@ey.com" <karim.anani@ey.com>, "kevin.klimara@ey.com" <kevin.klimara@ey.com>, "lee.henderson@ey.com" <lee.henderson@ey.com>, "mark.schwartz1@ey.com" <mark.schwartz1@ey.com>, "rachel.gerring@ey.com" <rachel.gerring@ey.com>, "megan.disciullo@pwc.com" <megan.disciullo@pwc.com>, "larissa.vonlockner@pwc.com" <larissa.vonlockner@pwc.com>, "ryan.a.cangialosi@pwc.com" <ryan.a.cangialosi@pwc.com>, "kivalena.starr@pwc.com" <kivalena.starr@pwc.com>, "jordana.strosberg@pwc.com" <jordana.strosberg@pwc.com>, "will.b.hodges@pwc.com" <will.b.hodges@pwc.com>, "jennifer.vanoss@pwc.com" <jennifer.vanoss@pwc.com>, "SENDROWSKI, DANIEL" <Daniel.Sendrowski@nypd.org>

ATTN: Mr. Reynoso,

        RE:     NYFRB 93715 - 153974/2020

LET me find out this is the same Zucker Family who evaded $500,000,000.00 in Taxes on the Six Properties they used as collateral to obtain a loan from State Farm - and also watched butt naked for a Year, distributed the videos and play with themselves.

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=K9sgXcweC7esRoSPO8MNtA==

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=D9Td7IfWXyajw1tBNCFb9g==




   see also: LOSSES SUFFERED BY THEIR COUNTERPARTS DUE TO OMISSIONS - FILED NOVEMBER 13TH, 2021;

THEN FURTHER DISTRIBUTED TO THE RESPONSIBLE PARTIES ON NOVEMBER 16TH, 2021.


                   

12-12-5858






TUESDAY --- JANUARY 11, 2022
Also wanted to make sure there was no relation between the two Reynoso, in case he didn't know - his brother is a PEEPING TOM as well.
>> also unanswered.

/s/ Bo Dincer


https://www1.nyc.gov/assets/brooklyncb1/downloads/pdf/meeting-agendas/Combined_Public_Hearing_and_Board_Meeting_1-11-2022.pdf

https://nyccb.webex.com/nyccb/onstage/g.php?MTID=e612f6401bfc6b617d3afa75563a41bf8

https://www1.nyc.gov/assets/brooklyncb1/downloads/pdf/meeting-minutes/combined_public_hearing_and_board_meeting_minutes_1-11-2022.pdf

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=p2E8IhjyOS8ocQnqpLU9Lg==


-------- Forwarded Message --------
Subject: 	You forget the zip code champ??
Date: 	Sat, 21 May 2022 09:51:59 -0400
From: 	Bo Dincer <bdincer66@icloud.com>
To: 	bk01@bk.gov, areynoso@mskyline.com, ZUCKER ORGANIZATION <jgiamboi@mskyline.com>, SHIKENA MELTON <SMELTON@mskyline.com>, legalasst@mskyline.com, LZUCKER@mskyline.com, tips@latimes.com, investor@annaly.com, investor@annaly.com, Chair <chair@sec.gov>, newyork@sec.gov, Ombudsman@sec.gov, TEDHERMANSON@northmarq.com, jpetit@mccarter.com, jheegan@doi.nyc.gov, Joseph Giamboi <joseph.giamboi@brooklaw.edu>, ZUCKER ORGANIZATION <jgiamboi@mskyline.com>, ricki.roer@wilsonelser.com, ashley.humphries@wilsonelser.com, slaskowitz@ingramllp.com, tips@nypost.com, BBO 121 <ms60710444266@yahoo.com>
CC: 	boc@boc.nyc.gov, NYM-PREAComplianceMgr-S@bop.gov, Victimassistance.fraud@usdoj.gov




<https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=p2E8IhjyOS8ocQnqpLU9Lg==>


-------- Forwarded Message --------
Subject: 	Mailbox Not Monitored
Date: 	Sat, 21 May 2022 12:46:54 -0400
From: 	Governor.Hochul@exec.ny.gov <Governor.Hochul@exec.ny.gov>
To: 	ms60710444266@yahoo.com


This mailbox is not monitored. You may contact Governor Hochul using this link:
http://www.governor.ny.gov/contact-iframe
Remember to visit Governor Hochul on Facebook, where you can receive regular updates on the actions of the Governor.

ForwardedMessage.eml
Subject:
93715 - 153974/2020 --- 1516523
From:
B D2022 <ms60710444266@yahoo.com>
Date:
5/21/2022, 12:46 PM
To:
Governor Hochul <governor.hochul@exec.ny.gov>, "BK01 (CB)" <bk01@cb.nyc.gov>, "AREYNOSO@mskyline.com" <AREYNOSO@mskyline.com>
CC:
TEDHERMANSON@northmarq.com, jpetit@mccarter.com, ashley.humphries@wilsonelser.com, "alex.zuluaga@ey.com" <alex.zuluaga@ey.com>, "david.brown1@ey.com" <david.brown1@ey.com>, Deborah M Jones <Deborah.Jones@ey.com>, "info@ey.com" <info@ey.com>, "jacqueline.kelley@ey.com" <jacqueline.kelley@ey.com>, "karim.anani@ey.com" <karim.anani@ey.com>, "kevin.klimara@ey.com" <kevin.klimara@ey.com>, "lee.henderson@ey.com" <lee.henderson@ey.com>, "mark.schwartz1@ey.com" <mark.schwartz1@ey.com>, "rachel.gerring@ey.com" <rachel.gerring@ey.com>, "megan.disciullo@pwc.com" <megan.disciullo@pwc.com>, "larissa.vonlockner@pwc.com" <larissa.vonlockner@pwc.com>, "ryan.a.cangialosi@pwc.com" <ryan.a.cangialosi@pwc.com>, "kivalena.starr@pwc.com" <kivalena.starr@pwc.com>, "jordana.strosberg@pwc.com" <jordana.strosberg@pwc.com>, "will.b.hodges@pwc.com" <will.b.hodges@pwc.com>, "jennifer.vanoss@pwc.com" <jennifer.vanoss@pwc.com>, "SENDROWSKI, DANIEL" <Daniel.Sendrowski@nypd.org>

ATTN: Mr. Reynoso,

        RE:     NYFRB 93715 - 153974/2020

LET me find out this is the same Zucker Family who evaded $500,000,000.00 in Taxes on the Six Properties they used as collateral to obtain a loan from State Farm - and also watched butt naked for a Year, distributed the videos and play with themselves.

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=K9sgXcweC7esRoSPO8MNtA==


    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=D9Td7IfWXyajw1tBNCFb9g==




   see also: LOSSES SUFFERED BY THEIR COUNTERPARTS DUE TO OMISSIONS - FILED NOVEMBER 13TH, 2021;

THEN FURTHER DISTRIBUTED TO THE RESPONSIBLE PARTIES ON NOVEMBER 16TH, 2021.


                   

12-12-5858






TUESDAY --- JANUARY 11, 2022
Also wanted to make sure there was no relation between the two Reynoso, in case he didn't know - his brother is a PEEPING TOM as well.
>> also unanswered.

/s/ Bo Dincer


https://www1.nyc.gov/assets/brooklyncb1/downloads/pdf/meeting-agendas/Combined_Public_Hearing_and_Board_Meeting_1-11-2022.pdf

https://nyccb.webex.com/nyccb/onstage/g.php?MTID=e612f6401bfc6b617d3afa75563a41bf8

https://www1.nyc.gov/assets/brooklyncb1/downloads/pdf/meeting-minutes/combined_public_hearing_and_board_meeting_minutes_1-11-2022.pdf

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=p2E8IhjyOS8ocQnqpLU9Lg==


-------- Forwarded Message --------
Subject: 	You forget the zip code champ??
Date: 	Sat, 21 May 2022 09:51:59 -0400
From: 	Bo Dincer <bdincer66@icloud.com>
To: 	bk01@bk.gov, areynoso@mskyline.com, ZUCKER ORGANIZATION <jgiamboi@mskyline.com>, SHIKENA MELTON <SMELTON@mskyline.com>, legalasst@mskyline.com, LZUCKER@mskyline.com, tips@latimes.com, investor@annaly.com, investor@annaly.com, Chair <chair@sec.gov>, newyork@sec.gov, Ombudsman@sec.gov, TEDHERMANSON@northmarq.com, jpetit@mccarter.com, jheegan@doi.nyc.gov, Joseph Giamboi <joseph.giamboi@brooklaw.edu>, ZUCKER ORGANIZATION <jgiamboi@mskyline.com>, ricki.roer@wilsonelser.com, ashley.humphries@wilsonelser.com, slaskowitz@ingramllp.com, tips@nypost.com, BBO 121 <ms60710444266@yahoo.com>
CC: 	boc@boc.nyc.gov, NYM-PREAComplianceMgr-S@bop.gov, Victimassistance.fraud@usdoj.gov




<https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=p2E8IhjyOS8ocQnqpLU9Lg==>


![IAj0PKJx7Zx9e1Xp](https://user-images.githubusercontent.com/70865813/169661616-e7eaa0f1-5edf-4d5c-bc1d-5793427eb39f.png)

12-12, 5858///
https://github.com/users/BSCPGROUPHOLDINGSLLC/projects/1#column-18309490




Remember to visit Governor Hochul on Facebook, where you can receive regular updates on the actions of the Governor.


ForwardedMessage.eml
Subject:
93715 - 153974/2020 --- 1516523
From:
B D2022 <ms60710444266@yahoo.com>
Date:
5/21/2022, 12:46 PM
To:
Governor Hochul <governor.hochul@exec.ny.gov>, "BK01 (CB)" <bk01@cb.nyc.gov>, "AREYNOSO@mskyline.com" <AREYNOSO@mskyline.com>
CC:
TEDHERMANSON@northmarq.com, jpetit@mccarter.com, ashley.humphries@wilsonelser.com, "alex.zuluaga@ey.com" <alex.zuluaga@ey.com>, "david.brown1@ey.com" <david.brown1@ey.com>, Deborah M Jones <Deborah.Jones@ey.com>, "info@ey.com" <info@ey.com>, "jacqueline.kelley@ey.com" <jacqueline.kelley@ey.com>, "karim.anani@ey.com" <karim.anani@ey.com>, "kevin.klimara@ey.com" <kevin.klimara@ey.com>, "lee.henderson@ey.com" <lee.henderson@ey.com>, "mark.schwartz1@ey.com" <mark.schwartz1@ey.com>, "rachel.gerring@ey.com" <rachel.gerring@ey.com>, "megan.disciullo@pwc.com" <megan.disciullo@pwc.com>, "larissa.vonlockner@pwc.com" <larissa.vonlockner@pwc.com>, "ryan.a.cangialosi@pwc.com" <ryan.a.cangialosi@pwc.com>, "kivalena.starr@pwc.com" <kivalena.starr@pwc.com>, "jordana.strosberg@pwc.com" <jordana.strosberg@pwc.com>, "will.b.hodges@pwc.com" <will.b.hodges@pwc.com>, "jennifer.vanoss@pwc.com" <jennifer.vanoss@pwc.com>, "SENDROWSKI, DANIEL" <Daniel.Sendrowski@nypd.org>

ATTN: Mr. Reynoso,

        RE:     NYFRB 93715 - 153974/2020

LET me find out this is the same Zucker Family who evaded $500,000,000.00 in Taxes on the Six Properties they used as collateral to obtain a loan from State Farm - and also watched butt naked for a Year, distributed the videos and play with themselves.

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=K9sgXcweC7esRoSPO8MNtA==

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=D9Td7IfWXyajw1tBNCFb9g==




   see also: LOSSES SUFFERED BY THEIR COUNTERPARTS DUE TO OMISSIONS - FILED NOVEMBER 13TH, 2021;

THEN FURTHER DISTRIBUTED TO THE RESPONSIBLE PARTIES ON NOVEMBER 16TH, 2021.


                   

12-12-5858






TUESDAY --- JANUARY 11, 2022
Also wanted to make sure there was no relation between the two Reynoso, in case he didn't know - his brother is a PEEPING TOM as well.
>> also unanswered.

/s/ Bo Dincer


https://www1.nyc.gov/assets/brooklyncb1/downloads/pdf/meeting-agendas/Combined_Public_Hearing_and_Board_Meeting_1-11-2022.pdf

https://nyccb.webex.com/nyccb/onstage/g.php?MTID=e612f6401bfc6b617d3afa75563a41bf8

https://www1.nyc.gov/assets/brooklyncb1/downloads/pdf/meeting-minutes/combined_public_hearing_and_board_meeting_minutes_1-11-2022.pdf

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=p2E8IhjyOS8ocQnqpLU9Lg==

![IAj0PKJx7Zx9e1Xp](https://user-images.githubusercontent.com/70865813/169661616-e7eaa0f1-5edf-4d5c-bc1d-5793427eb39f.png)

12-12, 5858///
https://github.com/users/BSCPGROUPHOLDINGSLLC/projects/1#column-18309490

-------- Forwarded Message --------
Subject: 	You forget the zip code champ??
Date: 	Sat, 21 May 2022 09:51:59 -0400
From: 	Bo Dincer <bdincer66@icloud.com>
To: 	bk01@bk.gov, areynoso@mskyline.com, ZUCKER ORGANIZATION <jgiamboi@mskyline.com>, SHIKENA MELTON <SMELTON@mskyline.com>, legalasst@mskyline.com, LZUCKER@mskyline.com, tips@latimes.com, investor@annaly.com, investor@annaly.com, Chair <chair@sec.gov>, newyork@sec.gov, Ombudsman@sec.gov, TEDHERMANSON@northmarq.com, jpetit@mccarter.com, jheegan@doi.nyc.gov, Joseph Giamboi <joseph.giamboi@brooklaw.edu>, ZUCKER ORGANIZATION <jgiamboi@mskyline.com>, ricki.roer@wilsonelser.com, ashley.humphries@wilsonelser.com, slaskowitz@ingramllp.com, tips@nypost.com, BBO 121 <ms60710444266@yahoo.com>
CC: 	boc@boc.nyc.gov, NYM-PREAComplianceMgr-S@bop.gov, Victimassistance.fraud@usdoj.gov




<https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=p2E8IhjyOS8ocQnqpLU9Lg==>


-------- Forwarded Message --------
Subject: 	Mailbox Not Monitored
Date: 	Sat, 21 May 2022 12:46:54 -0400
From: 	Governor.Hochul@exec.ny.gov <Governor.Hochul@exec.ny.gov>
To: 	ms60710444266@yahoo.com


This mailbox is not monitored. You may contact Governor Hochul using this link:
http://www.governor.ny.gov/contact-iframe
Remember to visit Governor Hochul on Facebook, where you can receive regular updates on the actions of the Governor.

ForwardedMessage.eml
Subject:
93715 - 153974/2020 --- 1516523
From:
B D2022 <ms60710444266@yahoo.com>
Date:
5/21/2022, 12:46 PM
To:
Governor Hochul <governor.hochul@exec.ny.gov>, "BK01 (CB)" <bk01@cb.nyc.gov>, "AREYNOSO@mskyline.com" <AREYNOSO@mskyline.com>
CC:
TEDHERMANSON@northmarq.com, jpetit@mccarter.com, ashley.humphries@wilsonelser.com, "alex.zuluaga@ey.com" <alex.zuluaga@ey.com>, "david.brown1@ey.com" <david.brown1@ey.com>, Deborah M Jones <Deborah.Jones@ey.com>, "info@ey.com" <info@ey.com>, "jacqueline.kelley@ey.com" <jacqueline.kelley@ey.com>, "karim.anani@ey.com" <karim.anani@ey.com>, "kevin.klimara@ey.com" <kevin.klimara@ey.com>, "lee.henderson@ey.com" <lee.henderson@ey.com>, "mark.schwartz1@ey.com" <mark.schwartz1@ey.com>, "rachel.gerring@ey.com" <rachel.gerring@ey.com>, "megan.disciullo@pwc.com" <megan.disciullo@pwc.com>, "larissa.vonlockner@pwc.com" <larissa.vonlockner@pwc.com>, "ryan.a.cangialosi@pwc.com" <ryan.a.cangialosi@pwc.com>, "kivalena.starr@pwc.com" <kivalena.starr@pwc.com>, "jordana.strosberg@pwc.com" <jordana.strosberg@pwc.com>, "will.b.hodges@pwc.com" <will.b.hodges@pwc.com>, "jennifer.vanoss@pwc.com" <jennifer.vanoss@pwc.com>, "SENDROWSKI, DANIEL" <Daniel.Sendrowski@nypd.org>

ATTN: Mr. Reynoso,

        RE:     NYFRB 93715 - 153974/2020

LET me find out this is the same Zucker Family who evaded $500,000,000.00 in Taxes on the Six Properties they used as collateral to obtain a loan from State Farm - and also watched butt naked for a Year, distributed the videos and play with themselves.

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=K9sgXcweC7esRoSPO8MNtA==


    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=D9Td7IfWXyajw1tBNCFb9g==




   see also: LOSSES SUFFERED BY THEIR COUNTERPARTS DUE TO OMISSIONS - FILED NOVEMBER 13TH, 2021;

THEN FURTHER DISTRIBUTED TO THE RESPONSIBLE PARTIES ON NOVEMBER 16TH, 2021.


                   

12-12-5858



---


TUESDAY --- JANUARY 11, 2022
Also wanted to make sure there was no relation between the two Reynoso, in case he didn't know - his brother is a PEEPING TOM as well.
>> also unanswered.

/s/ Bo Dincer


https://www1.nyc.gov/assets/brooklyncb1/downloads/pdf/meeting-agendas/Combined_Public_Hearing_and_Board_Meeting_1-11-2022.pdf

https://nyccb.webex.com/nyccb/onstage/g.php?MTID=e612f6401bfc6b617d3afa75563a41bf8

https://www1.nyc.gov/assets/brooklyncb1/downloads/pdf/meeting-minutes/combined_public_hearing_and_board_meeting_minutes_1-11-2022.pdf

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=p2E8IhjyOS8ocQnqpLU9Lg==


-------- Forwarded Message --------
Subject: 	You forget the zip code champ??
Date: 	Sat, 21 May 2022 09:51:59 -0400
From: 	Bo Dincer <bdincer66@icloud.com>
To: 	bk01@bk.gov, areynoso@mskyline.com, ZUCKER ORGANIZATION <jgiamboi@mskyline.com>, SHIKENA MELTON <SMELTON@mskyline.com>, legalasst@mskyline.com, LZUCKER@mskyline.com, tips@latimes.com, investor@annaly.com, investor@annaly.com, Chair <chair@sec.gov>, newyork@sec.gov, Ombudsman@sec.gov, TEDHERMANSON@northmarq.com, jpetit@mccarter.com, jheegan@doi.nyc.gov, Joseph Giamboi <joseph.giamboi@brooklaw.edu>, ZUCKER ORGANIZATION <jgiamboi@mskyline.com>, ricki.roer@wilsonelser.com, ashley.humphries@wilsonelser.com, slaskowitz@ingramllp.com, tips@nypost.com, BBO 121 <ms60710444266@yahoo.com>
CC: 	boc@boc.nyc.gov, NYM-PREAComplianceMgr-S@bop.gov, Victimassistance.fraud@usdoj.gov




<https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=p2E8IhjyOS8ocQnqpLU9Lg==>

---
## [cdb-is-not-good/sojourn-station](https://github.com/cdb-is-not-good/sojourn-station)@[796aeaa98f...](https://github.com/cdb-is-not-good/sojourn-station/commit/796aeaa98f76c2a6ef7a94e540d3b8f7efcb027b)
#### Saturday 2022-05-21 17:08:45 by lolman360

fixes stacks deleting randomly (#3357)

* whoo

* god i fucking hate stackcode

thank you kevinz

---
## [anushka0301/Google_foobar](https://github.com/anushka0301/Google_foobar)@[af8d4c1ad5...](https://github.com/anushka0301/Google_foobar/commit/af8d4c1ad515514692623c51edcfbabf539e5e0d)
#### Saturday 2022-05-21 17:37:29 by Anushka Chaudhuri

Update lovely-lucly-lambs.py

"""
Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous, she'll hand out Lucky LAMBs (Lambda's All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks, a pillow for their bunks, or even a third daily meal!

However, actually passing out LAMBs isn't easy. Each henchman squad has a strict seniority ranking which must be respected - or else the henchmen will revolt and you'll all get demoted back to minions again!

There are 4 key rules which you must follow in order to avoid a revolt: 1. The most junior henchman (with the least seniority) gets exactly 1 LAMB. (There will always be at least 1 henchman on a team.) 2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do. 3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get. (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them. The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.) 4. You can always find more henchmen to pay - the Commander has plenty of employees. If there are enough LAMBs left over such that another henchman could be added as the most senior while obeying the other rules, you must always add and pay that henchman.

Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of LAMBs.

Write a function called answer(total_lambs), where total_lambs is the integer number of LAMBs in the handout you are trying to divide. It should return an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs (that is, being as generous as possible to those you pay and as stingy as possible, respectively) while still obeying all of the above rules to avoid a revolt. For instance, if you had 10 LAMBs and were as generous as possible, you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending seniority), whereas if you were as stingy as possible, you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore, answer(10) should return 4-3 = 1.

To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts: you can expect total_lambs to always be between 10 and 1 billion (10 ^ 9).
"""

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8b931fe5e2...](https://github.com/mrakgr/The-Spiral-Language/commit/8b931fe5e25f9ff831ab3ef2201a5093cdf5f3b4)
#### Saturday 2022-05-21 18:03:16 by Marko Grdinić

"1:40pm. The Estab Life episode was great. This anime is one to be remembered. Hopefully it gets 5 seasons like Symphogear.

1:55pm. Let me start the modeling session. In the morning session, I did some studying, but I've been way to relaxed today. It is time to get some things done. Let me play with fileting a cube for a bit and then I will get started.

2:15pm. http://moi3d.com/forum/index.php?webtag=MOI&msg=6790.35

Let me investigate what Blend does. It has a bunch of options with which I am not familiar with.

2:45pm. http://moi3d.com/forum/messages.php?webtag=MOI&msg=10700.1

Somebody asked the hidden line toggle shortcut.

script: /* Toggle edge display */ var breps = moi.geometryDatabase.getObjects().getBReps(); var hide = true; for ( var i = 0; i < breps.length; ++i ) { var edges = breps.item(i).getEdges(); if ( i == 0 ) hide = !edges.item(0).hidden; edges.setProperty( 'hidden', hide ); }
script:/* Toggle Wire / faces */var breps = moi.geometryDatabase.getObjects().getBReps(); var hide = true; for ( var i = 0; i < breps.length; ++i ) { var faces = breps.item(i).getFaces(); if ( i == 0 ) hide = !faces.item(0).hidden; faces.setProperty( 'hidden', hide ); }

Let me add these two shortcuts to the mix. I couldn't get the toggle hidden line shortcut to work.

Edit: Got a reply: script:moi.view.showHiddenLines =! moi.view.showHiddenLines;

https://www.youtube.com/watch?v=2-5J6hLRDaI
Moi3D Ridge Tutorial

Let me watch this and I will get started. Forget messing around with Blend.

https://youtu.be/2-5J6hLRDaI?t=309

Ah, I think I understand what sync points are supposed to be for.

4:40pm. Done with the bottom shelf. I am just taking a little breather right now. Let me get back into the fray. Let me just do the rest. 3d modeling is surpringly mentally exhausting. Even watching tutorials is easier than this.

7:10pm. Time for lunch.

7:35pm. Let me resume...no, let me stop here. I am dead tired. I've been in the zone for 5h, now it is the time to take a break and let my brain cool down. Let me just assign some colors in Moi.

...No forget it. Styles aren't good at coloring. I can't get white to display any differently from black.

I actually realized for the first time that the default style is in fact black.

7:45pm. Let me close here. I'll do some posting of the recent work in the /wip/ thread. Now that I am really focusing on just modeling it feels like my skill is going up daily. The decision to make modeling my 3d specialization brought about a change in attitude. I am no longer going around seeking learning material. It feels I've touched upon a large part of what makes up 3d art already. I just have to deal with these models and then I will be playing with rendering. I am going to break into 3/5 in 3d in the next few months. I am going to have to learn to draw as well, and bring my 2d skills up to that level.

If I had chosen the programming path, I could have made money, but I wouldn't have been able to what I want. On the current path I'll be able to do what I want, but I am having to endure the lack of funds. I'll resolve that issue at some point.

If the programming path is really meant to be, this world won't let me scribble around forever.

If the Singularity is meant to be, ML won't stay in perpetual demo stage. If it is meant to be, I will get the tools I need to take advantage of my vision.

Until then, I should continue cultivating the manipulation tree."

---
## [Tastyfish/Skyrat-tg](https://github.com/Tastyfish/Skyrat-tg)@[a064b35b25...](https://github.com/Tastyfish/Skyrat-tg/commit/a064b35b2571af36cf9d12cea8005843768af36d)
#### Saturday 2022-05-21 19:19:59 by SkyratBot

[MIRROR] Fixes an error sprites on medical wintercoat's allowed list. [MDB IGNORE] (#13566)

* Goodbye stack/medical (#66898)

Okay, why removing instead of giving it a sprite?

Simply put, those items are all small and there is no reason that you need to quick draw a suture/ointment and if you do, the medical belt can carry 7.
Allowed/exoslot items should be either medium/big/bulky sized items (Syringe gun) to make it worth inventory wise or items that you can quickdraw multiple times (Health Analyzer) to make your life easier.
Medical stacks are neither and would just get in the way if you try to quickly put them into a bag/pocket/belt and instead it goes into your exoslot where you would normally want to carry more valuable things like the syringe gun.

This doesn't feel big enough for a fix, spending 5 seconds making a list alphabetical doesn't few worth of code improvement, I will label this as QoL and if someone say it is a balance change I will follow you in game and keep placing shitty small items in your inventory via reverse pickpocketing.

* Fixes an error sprites on medical wintercoat's allowed list.

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [DerpFest-12/kernel_oneplus_msm8998](https://github.com/DerpFest-12/kernel_oneplus_msm8998)@[91a9e91029...](https://github.com/DerpFest-12/kernel_oneplus_msm8998/commit/91a9e91029ffc61fce24204c43e5d27e7e382b07)
#### Saturday 2022-05-21 20:30:23 by Maciej Żenczykowski

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
## [Luramoth/hello-triangle](https://github.com/Luramoth/hello-triangle)@[b92552146d...](https://github.com/Luramoth/hello-triangle/commit/b92552146dbe3124adc68f8c6f847f492310bc50)
#### Saturday 2022-05-21 20:38:58 by Kayla

indent everything using tabs
fuck you hippoz
fuck you tuna

---

