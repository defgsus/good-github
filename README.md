## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-02](docs/good-messages/2022/2022-05-02.md)


1,813,186 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,813,186 were push events containing 2,851,075 commit messages that amount to 217,825,621 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [cdcline/demo-website](https://github.com/cdcline/demo-website)@[b9d662ef91...](https://github.com/cdcline/demo-website/commit/b9d662ef9117bd800e347943ac63cdb3a7bc4582)
#### Monday 2022-05-02 00:03:06 by Chris Cline

Minor MiniArticle cleanup; add vscode to .gitignore

We'd like the Mini Article tags to be in the same order, no matter
what order the entry tags are.

This adds a sort to the tags array to keep the tags in alphabetical
order. The tags on the Entries themselvs are basically in order of
adding them but that's nbd & doubtful anyone will notice.

This also updates some data
 * Changes dates to not be so similar
  * It was difficult to tell the order when they're all in the same year
 * Modifies some dummy text for better ledge ability
 * Updates a tag so that the animation will be more fun if you click left to right

Note: Updates .gitignore to remove .vscode dir. I don't think my local vscode
changes are relevant but it is kinda nice to have common format files.

Currently I'm not doing anything weird except using 3 spaces; which I bet
will be a thing at some point, but I'm too used to that to change now and
it's easy enough to auto-fix if the thing becomes a problem.

---
## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[7c61bf65f2...](https://github.com/Shadow-Quill/tgstation/commit/7c61bf65f2b3c661bf622864bb7596e0e89d1f28)
#### Monday 2022-05-02 00:29:23 by vincentiusvin

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301)


About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[3f18dadd1a...](https://github.com/Tastyfish/-tg-station/commit/3f18dadd1a5d654aafc2c37539ff917580bfe0b2)
#### Monday 2022-05-02 00:29:43 by san7890

Updates Maps And Away Missions MD (#66455)

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

---
## [OpenImageIO/oiio](https://github.com/OpenImageIO/oiio)@[594776d9c6...](https://github.com/OpenImageIO/oiio/commit/594776d9c617ab05b3cf0ff17d69dff908c1ae7e)
#### Monday 2022-05-02 01:26:41 by Larry Gritz

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
## [tralezab/tgstation](https://github.com/tralezab/tgstation)@[a137c15a79...](https://github.com/tralezab/tgstation/commit/a137c15a790bc8242a1ccd70bb6570d0278833c0)
#### Monday 2022-05-02 02:22:48 by Vladin Heir

Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [kaninhot004/rathena](https://github.com/kaninhot004/rathena)@[d617d9f083...](https://github.com/kaninhot004/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Monday 2022-05-02 05:18:11 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [projects-nexus/android_kernel_xiaomi_gauguin](https://github.com/projects-nexus/android_kernel_xiaomi_gauguin)@[45dc12e19d...](https://github.com/projects-nexus/android_kernel_xiaomi_gauguin/commit/45dc12e19d26fee30a26695a4148c1af4ee8691c)
#### Monday 2022-05-02 05:31:44 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Co-authored-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[Tashar02: forwardport and adapt to 4.19 and xiaomi_sdm660's fp]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[kawaaii: Adapt to xiaomi_gauguin's fp]
Signed-off-by: kawaaii <kawaaii@nocturn9x.space>

---
## [necromanceranne/Shiptest](https://github.com/necromanceranne/Shiptest)@[031c0866ed...](https://github.com/necromanceranne/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Monday 2022-05-02 05:49:52 by SweetBlueSylveon

Nanotrasen Deserter Vault Ruin (#732)

* Nanotrasen Deserter Vault Ruin

A ruin based around a Nanotrasen ultra secure vault. It should spawn on the ice planet. This commit adds everything.

* Map Changes

-Replaces Glockroach family with Jack and Jill, Slaughter and Laughter demons.
-Replaces Sniper Rifle with Particle Acceleration Rifle.
-Replaces Sniper Rifle ammo with a single upgraded weapon power cell.
-Adds a sentience potion and cns rebooter implant to vault safe since there were only mats in it otherwise.

* Minor commit

Removes a cybernetic that should have been removed before the last commit.

* Update code/game/area/areas/ruins/icemoon.dm

I'm dumb and didn't realize I did this. Also didn't realize linters was the code checker, so I didn't realize to check the code. I know now! Thanks for the help.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* Adds the knight gear design disk.

Adds the "magical disk of smithing" to the safe.

* Unmodularizes your Modularization

Moves the datum to an unmodularized folder.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Brixia98/meteoric_kernel](https://github.com/Brixia98/meteoric_kernel)@[38b0bd0f25...](https://github.com/Brixia98/meteoric_kernel/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Monday 2022-05-02 05:59:01 by Linus Torvalds

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
## [input-output-hk/ouroboros-network](https://github.com/input-output-hk/ouroboros-network)@[71cbca3021...](https://github.com/input-output-hk/ouroboros-network/commit/71cbca30215c827117425b8f082038b34a390109)
#### Monday 2022-05-02 07:44:07 by Nicholas Clarke

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
## [citizenfx/fivem](https://github.com/citizenfx/fivem)@[02df4a52b1...](https://github.com/citizenfx/fivem/commit/02df4a52b1dba9b56a89b10bf59be7c9ff79c0d9)
#### Monday 2022-05-02 07:48:45 by blattersturm

tweak(client/core): nvidia, fuck you.

Apparently ba693365d151cb3d61e1fd1bc08f9f65f66d13ae wasn't enough to fix
the .toc corruption from nvPSShaderDiskCache.cpp/the NvShaderDiskCache
perf strategy.

Instead, this change just disables the shader cache entirely. Using a
hacky way.

---
## [adityabalu/DiffNet](https://github.com/adityabalu/DiffNet)@[92110b0c15...](https://github.com/adityabalu/DiffNet/commit/92110b0c15b89ed798927532ebc21212cb3d76dd)
#### Monday 2022-05-02 07:57:22 by Biswajit

Damn pytorch requires_grad making my life hell. And also f*** tqdm.

---
## [AR-May/msbuild](https://github.com/AR-May/msbuild)@[a572dc6b79...](https://github.com/AR-May/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Monday 2022-05-02 08:37:31 by Forgind

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
## [JackTheMico/dotfiles](https://github.com/JackTheMico/dotfiles)@[04f015e359...](https://github.com/JackTheMico/dotfiles/commit/04f015e359e660210e15563661b8eb729e4e7547)
#### Monday 2022-05-02 09:15:22 by Jack Deng

Add dot_local/share/private_qutebrowser/greasemonkey/executable_fuck-youtube.js
Add dot_local/share/private_qutebrowser/greasemonkey/executable_wide-github.user.js

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[bdaf1dfae7...](https://github.com/git-for-windows/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Monday 2022-05-02 09:59:55 by Tao Klerks

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
## [Josephin23/goonstation](https://github.com/Josephin23/goonstation)@[bdad398f9e...](https://github.com/Josephin23/goonstation/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Monday 2022-05-02 10:26:32 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [rsalmaso/gitea](https://github.com/rsalmaso/gitea)@[3725fa28cc...](https://github.com/rsalmaso/gitea/commit/3725fa28ccc01ab08060f591f894ea6443a348e8)
#### Monday 2022-05-02 10:37:42 by Gusted

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
## [projects-nexus/android_xtreme_kernel_lavender](https://github.com/projects-nexus/android_xtreme_kernel_lavender)@[d3e168ea69...](https://github.com/projects-nexus/android_xtreme_kernel_lavender/commit/d3e168ea698cd6f9e9d72b7f1a976c205deb910e)
#### Monday 2022-05-02 11:19:32 by Maciej Żenczykowski

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
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d9efd850cd...](https://github.com/mrakgr/The-Spiral-Language/commit/d9efd850cdf29d47511a4116c46bcae19b649513)
#### Monday 2022-05-02 11:33:55 by Marko Grdinić

"9:15am. I am up. Let me chill a bit and I will start.

9:45am. Let me start. First, let me post the review...Done.

Now let me figiure out how to deal with those logos.

I just realized that projecting a plane would not work as the surface is curved. To get it to work exactly right, I'd need to duplicated the object and cut them out using knife project. But if I do that, then those particular parts will lose the normal information. So maybe I'll have to make a special UV set just for the relevant parts.

https://blender.stackexchange.com/questions/98156/copying-vertex-normals

Normal transfer? Yeah, this would be the best.

10:10pm. It was not hard to do at all. I just cut out a bunch of faces, shrinkwrapped them so they are offset above the surface by 0.0001, then did a data transfer of normals to get rid of the tiny lighting distortions near the corners. Then I unwrapped the UVs. All is well that ends well. The rest don't need UVs. I'll just set up the shaders directly in Clarisse.

Now let me bring this thing into Substance.

10:30am. Got the energy star and the Samsung logo. Now I need the dynamic contrast icon next to it. Could I paint it directly in Substance or should I do it in Clip Studio or Illustrator?

10:40am. I'll go with Clip Studio as it is easier to use. I forgot how to use Illustrator at this point. It is really easy to insert text with it.

Let me just take a look at how text insertion works with Substance Painter.

https://youtu.be/Tw3wQ1IpM0k
Custom fonts in Substance Painter! 2020 Tutorial

https://youtu.be/5uaPT6clRuI
Substance Painter Beginner Tutorial : Text & Font

Let me go with the later, I am not interested in doing custom fonts.

10:45am. Found the alpha, but why is my brush not working all of a sudden? Because I had the eraser selected.

I am confused. Can't you chage the text in Substance? Ah, you can. There it is in the params.

10:55am. Let me get my pen out. The smallish geometric figure I can just do myself.

11:10am. This is good enough. I won't bother getting the logo exactly right.

Glad that I had a chance to do some vectoring in CSP. the way the control points were interplated was weird though. I don't really get how that worked, but it does not matter. The fact it had a line widths tool was quite helpful. I'll leave the mystery of how to use vector lines for later when I get into 2d art. Right now my knowledge in this area is lacking.

I have the 3 images. Let me project them into the monitor.

Hmmm, ah, I remember. I need to load those resources into the project first.

11:40am. Had to take a short break. Right now, I am having trouble with alphas. Given the checkerboard texture in the background, I am surprised that get interpreted as white in Substance Painter. My own image should have alphas, but probably did not because I forgot to remove the paper underneath before exporting it. Only the energy star logo has alphas, but not the checker texture in the background. I am going to have to load each of the in CSP and adjust them.

12pm. Yeah, this fiddling around takes time. I am making dumb mistakes and wasting time. This is the first time I am doing something like this so I am just flushing time down the toilet.

12:05pm. Holy shit, fuck Substance Painter's import.

Why won't it import the correct version of the mesh?

12:10pm. It turns out on the back, the faces were oriented wrong.

But when I load the obj with the logos some of it gets sheared.

Ahhh, I see. The material assignments got messed up. That is why one part seemed sheared.

12:35pm. How the hell do I get the alpha channel to work properly on the Samsung logo? I also want to figure out how I can inspect alpha in CSP or Blender's image viewer. This issue is ridiculous. Why is it giving me so much trouble?

10:40pm. Holy shit, that checkerboard texture is a literal texture instead of an alpha. In Substance, the white is so strong it got washed out so I came to the wrong conclussion.

1:10pm. Finally. I have the correct textures exported. Now I just have to bring it into Clarisse and set up the shaders.

For the desk, I moved some the resources to different folder. I am going to have to figure out how to rename all those file locations in batch mode.

1:15pm. Now let me review. I went and did it, but the way I did it is a bit ridiculous with separating the object like I did.

Wouldn't it be possible to assign unique UVs to each material?

https://blenderartists.org/t/uv-map-per-material/1303076
> Say I have a simple cube, and I apply one material to one face, and another material to the remaining faces. It took me a while to realize that I could effectively generate TWO UV maps for that object, one per material. So I can select the one face, apply say a brick image, resize that face in its own UV map, then do the same for the remaining faces with a different image and a totally different UV map. Which, for me, is awesome.

How do I do this. This is a much better solution than what I have right now.

> No… I think they’re saying that you seem to have a fundamental misunderstanding… UV maps don’t belong to materials, they belong to meshes… so what you’re saying doesn’t make sense. Based on your description, you’re actually still re-using the same UV map.

Let me try it again.

1:25pm. How do I set up a material to use a particular UV?

I figured out how to make separate UV maps. That link shows how to set it up in Blender. What about Substance? How does it handle multiple UV maps on a single object?

Let me leave it for later. I'll stop here for breakfast.

This is more like how my programming days went. I am done with tutorials and will be able to move to doing more practical things.

1:30pm. Hrmmm, I got the monitor wrong, it does have tiny splotches and dust on it. I might have to do a bit extra work then. Also I completely missed that in the top left corner it says SyncMaster 2233. I've had this monitor for close to a decade, and yet this part completely faded from my memory and even my perception.

1:35pm. Nevermind this. Let me have breakfast. Then I will touch it up in Substance. Then comes bringing it into Clarisse. Then I'll move to the rig."

---
## [TylerTehIdiot/sarvente-kade-android](https://github.com/TylerTehIdiot/sarvente-kade-android)@[34c38898bc...](https://github.com/TylerTehIdiot/sarvente-kade-android/commit/34c38898bc81eed927d3a5327c036d32306d4aaa)
#### Monday 2022-05-02 11:51:10 by Tyler

I swear to fucking gosh If the build compile gives me another damn error I will kill Naayir

---
## [paulgessinger/acts](https://github.com/paulgessinger/acts)@[6e1fd31474...](https://github.com/paulgessinger/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Monday 2022-05-02 12:15:58 by Stephen Nicholas Swatman

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
## [Lys0gen/Divergences-HPM](https://github.com/Lys0gen/Divergences-HPM)@[a149573ae0...](https://github.com/Lys0gen/Divergences-HPM/commit/a149573ae03d17b6287156cd19ecd9c1aa509f93)
#### Monday 2022-05-02 12:26:16 by Capitanloco6

Armenia and Kar-Kiya patch

-	Added possibility for Armenia to break free If the Shaki fail their early wars. The Player can attempt to lead an uprising against the Shaki and play the newly added Armenian content which contains:
o	Flavour-events for the process of civilising
o	Armenian expansion and gaining cores in the Caucasus and Anatolia over the course of the game
o	An event chain regarding the state of the Armenian Cilicians
o	A decision to restore the Empire of Tigranes the Great for absolute Monarchies and fascist dictatorships and a less reactionary equivalent for socialist governments
o	Decisions to accept Assyrians, Georgians and Syriacs
o	Flavour events such as the reintegration of the Armenian diaspora
-	Added an event chain to the Kar-Kiya leading up to the constitutional revolution. The choices taken during the events unlock one of the three possible country paths for the Kar-Kiya
o	Constitutionalist – Nationalist. Encourage unification rebels in other Iranian countries, liberate the Caspian Iranians in Azerbaijan and reform the administration and economy of your realm, among other decisions.
o	Zaydi – Theocratic. Content regarding the persecution of the other Shi’a sects within your realm, expansion towards the holy shrines in Khorasan and the protection of the Zaydi minority in Yemen.
o	Royalist. Take advantage of the Russian patrons that helped keep the monarchy in power – at the risk of the Russians making unacceptable demands back. Possiblity of getting a new tech school and conflict if Russia decides to expand into the southern Caspian shore as the first step towards India.
-	Reduced the maluses Italy receives upon integrating Venice, Sardinia and Corsica
-	Reduced the militancy maluses the Sublime Porte receives when the Janissaries win the Civil War, preventing the depopulation of Bulgaria
-	Proclaiming the Kingdom of Hanover now gives Rhenish as an accepted culture
-	Taking the Baltic expansion path as Russia no longer leaves a few random provinces uncored
-	Mostar is now properly considered a port province, no longer making Illyria a landlocked nation
-	Fixed naval base in Christanborg, preventing bugged ship building
-	Fixed positions in Kiel
-	Fixed the Scramble for Africa full annexation CB not working as intended
-	The decision to integrate the Cape Coloured can no longer be taken as a Vryland-formed South Africa
-	The decision to integrate Greeks as a Venice who failed in the Council of Athens now properly works for both regular Republic and Merchant Republic governments
-	Various miscellaneous localisation fixes
-	Fixed improper promotion of serfs to farmers in mineral RGO provinces
-	Neu Kurland and Tobago now start as states, making Neu Kurland runs more viable
-	Eendrachtsland now has Burgundian rather than Bosnian ship names
-	Tarfaya, Aaiun and Dakhla no longer start as colonial provinces
-	Dissolving Gran Colombia as an Arcadian/Amerigan Great Power now properly releases Lusitania and Cuba

---
## [andmeics/llvm-project](https://github.com/andmeics/llvm-project)@[7664127f8c...](https://github.com/andmeics/llvm-project/commit/7664127f8c949ac3da7003427d87ff4b93e320d2)
#### Monday 2022-05-02 13:02:41 by Chandler Carruth

Fix a horrible infloop in value tracking in the face of dead code.

Amazingly, we just never triggered this without:
1) Moving code around for MetadataTracking so that a certain *different*
   amount of inlining occurs in the per-TU compile step.
2) Then you LTO opt or clang with a bootstrap, and get inlining, loop
   opts, and GVN line up everything *just* right.

I don't really know how we didn't hit this before. We really need to be
fuzz testing stuff, it shouldn't be hard to trigger. I'm working on
crafting a reduced nice test case, and will submit that when I have it,
but I want to get LTO build bots going again.

llvm-svn: 256735

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[1b7d7d9327...](https://github.com/pytorch/pytorch/commit/1b7d7d93276eb37c009905ef87ea9c2a7c95481e)
#### Monday 2022-05-02 14:33:52 by Brian Hirsh

Reland: "free up dispatch key space (in C++)" (#74963)

Summary:
Pull Request resolved: https://github.com/pytorch/pytorch/pull/74963

This is a re-land of D35192346 (https://github.com/pytorch/pytorch/commit/9872a06d77582e91e834103db75f774ca75f7fff) and D35192317 (https://github.com/pytorch/pytorch/commit/a9216cde6cc57f94586ea71a75a35aaabee720ff), which together are a diff that changes the internal representation of `DispatchKeySet` in pytorch core to free up the number of dispatch keys that we have available. See a more detailed description of the design in the original PR: https://github.com/pytorch/pytorch/pull/69633.

The original PR broke Milan workflows, which use a pytorch mobile build, and manifested as a memory corruption bug inside of `liboacrmerged.so`.

**Background: Existing Mobile Optimization**
Pytorch mobile builds have an existing optimization (here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/c10/core/DispatchKey.h#L382 and here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/OperatorEntry.h#L214), which works as follows:

Every operator in pytorch has a "dispatch table" of function pointers, corresponding to all of the (up to 64) different kernels that we might dispatch to when we run an operator in pytorch (autograd, cpu, cuda, complex number support, etc).

In mobile builds, the size of that table is shrunk from 64 to 8 to save a bunch of space, because mobile doesn't end up using the functionality associated with most dispatch keys.

The dispatcher also has a notion of "fallback kernels", which are kernels that you can register to a particular dispatch key, but should be able to work for "any operator". The array of fallback kernels is defined here: https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/Dispatcher.h#L294.

The mobile-optimization currently does **not** extend to this array (it wouldn't be that useful anyway because there is only one array of fallback kernels globally - vs. there is a separate dispatch table of function pointers per operator). So the per-operator tables on mobile are size 8, while the fallback table is size 64.

**The Bug**
This PR actually makes it difficult to enable that optimization separately for the per-operator arrays vs. the fallback array, and incidentally shrunk the size of the fallback array from 64 to 8 for mobile (that happened on this line: https://github.com/pytorch/pytorch/pull/69633/files#diff-f735cd7aa68f15b624100cbc4bb3b5ea76ffc7c9d3bec3b0ccabaa09609e5319R294).

That isn't a problem by itself (since mobile doesn't actually use any of the fallbacks that can no longer be stored). However, pytorch core will still register all of those fallback kernels on startup in mobile builds, even if they aren't used. When we tried to register one of those fallbacks on startup, it would try to dump the kernel somewhere in memory past the bounds of the (now smaller) array inside of the `Dispatcher` object, `backendFallbackKernels_`.

**Why didn't this problem show up in OSS CI? Why didn't it break other internal mobile workflows aside from Milan?**

Ideally, this failure would show up as part of the OSS signal on GitHub, since we already have mobile OSS builds. Given that it was another memory corruption issue that only affected Milan (subset of mobile), I'm not sure what's specific about Milan's builds that caused it only to manifest there. dreiss I wonder if there's another flavor of mobile builds we could run in OSS CI that could potentially help catch this?

**The debugging experience was pretty difficult**

Debugging the Milan-specific failure was made difficult by the following:

(1) lack of CI
- the original Milan failure didn't surface on my original diff, because the Milan job(s) that failed weren't triggered to run on pytorch changes. There's probably a balance to strike here, since those jobs will only be useful if they aren't flaky, and if they can produce reliable failure logs for debugging.

(2) It's difficult to get a repro.
- my work laptop doesn't have the right specs to run the Milan development workflow (not enough disk space)
- There is an existing OnDemand workflow for Milan, but it appears to be relatively new, and after a bunch of help from MarcioPorto, we ran into issues forwarding the log output from Milan tests on the emulator back to the terminal (see the original discussion here: https://fb.workplace.com/groups/OnDemandFRL/permalink/1424937774645433/)

(3) Lack of stack-traces.
- Most Milan failures didn't include actionable stack traces. phding generously helped me debug by running my suggested patches locally, and reporting back if there were any failures. The failing test didn't include a stack trace though (just the line where the crash appeared), so I ended up making some educated guesses about what the issue was based on the area of the crash.
ghstack-source-id: 152688542

Test Plan: Confirmed with phding that the broken Milan workflow from the previous version of this diff is now passing.

Reviewed By: phding, albanD

Differential Revision: D35222806

fbshipit-source-id: 0ad115a0f768bc8ea5d4c203b2990254c7092d30
(cherry picked from commit 002b91966f11fd55ab3fa3801b636fa39a6dd12c)

---
## [PixelExperience-Devices/kernel_oneplus_sm8150](https://github.com/PixelExperience-Devices/kernel_oneplus_sm8150)@[f2f5e373ac...](https://github.com/PixelExperience-Devices/kernel_oneplus_sm8150/commit/f2f5e373ac5f13903a8741e264562d2ec558be91)
#### Monday 2022-05-02 15:12:40 by alk3pInjection

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
## [That-sANiceDonkey/ViolenceRepo](https://github.com/That-sANiceDonkey/ViolenceRepo)@[ced03aa891...](https://github.com/That-sANiceDonkey/ViolenceRepo/commit/ced03aa891a3982054a6eeb832fc3adb3eb6ba44)
#### Monday 2022-05-02 15:19:50 by LukeOx

Fuck you Unreal, Fuck you Github. Suck my dick v1.your mum

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[de372a2ae0...](https://github.com/UnderMybrella/usa/commit/de372a2ae0a820a26d573b7cd383d477d75c8b62)
#### Monday 2022-05-02 17:02:18 by MarkiSpider

Update 75 files @ Mon, 02 May 2022 17:02:15 GMT
This site update changes zeusandfriends.html, nebuchadnezzar.html, idkbro.html, Jupiterandfriends.html, cases.html, evidence.html, shatteredbysomeone.html, agencydirectory.html, departments.html, dont-push.html, logs.html, the-baboonies.html, corn-dm.html, para.docs-portal, michaeljackson.html, illinois.html, ijustmadeyoulookunderthere.html, karen6815.html, evidence.html, auth.html, theoracle.html, user.html, oopsalbangers.html, usa-home.html, thejackson5.html, thefounders.html, ohyouwouldlikethatwouldntyou.html, legal.html, gettingjiggywithit.html, thekilleidoscope.html, thedude.html, NerdFiction.html, iinhumanresources.html, reviews.html, images.html, messenger.html, MichaelJackson.html, terrorblycute.html, thecaptain.html, terfwar.html, dashboard.html, girlofthe21stcentury.html, moriarty.html, user8118151241161251919.html, redacted.html, employeeaccountabilitytimesignature-portal.html, helpcenter.html, the-asshats.html, thealienalliance.html, fuckem.html, cachow.html, case-directory.html, aretheyalium.html, karen6809.html, sexygoldarms.html, thebutterflysoldiers.html, the-d_.html, capitalism.html, karen6803.html, schedule.html, Imsorrymissjackson.html, karen6816.html, logs.html, inhumanresources.html, everyone.html, karen-archive.html, woahhh.html, thebannerborn.html, LixianTV.html, lolgotyou.html, kriskringle.html, byebyebye.html, Rad_R.html, karen6804.html, 914222-1916151820192112124214513114.html

---
## [hawkw/mycelium](https://github.com/hawkw/mycelium)@[2bfe554046...](https://github.com/hawkw/mycelium/commit/2bfe5540460b18c3de399179297c4439a803dbcb)
#### Monday 2022-05-02 17:23:16 by Eliza Weisman

fix(x86_64): unfuck interrupt stack frames (#148)

It turns out that the reason we've been seeing extremely spooky behavior
in interrupt handlers, especially when trying to disassemble at `[rip]`,
is because LOL ELIZA FUCKED UP THE REGISTERS LOL LMAO.

When an interrupt occurs, a number of registers are pushed to the stack
frame for the interrupt handler. This includes the instruction pointer,
stack pointer, and the code and stack segment selectors. We defined a
`Registers` struct that consists of named fields for these registers, in
the correct order. However, because I'm a **loser fucking idiot**, the
current x86_64 ISRs were accidentally taking an `&mut Registers` rather
than a `Registers`. This meant we were interpreting the first 64 bits of
the registers (which I believe was the zero-padded 16-bit `ss` stack
segment selector) as a *pointer*, and reading the "register" values from
`[ss]`. This results in garbage.

And, when we tried to use `yaxpeax` to disassemble `[rip]`...`[rip +10]`
in the oops handler, we followed the "`rip`" from the location
pointed to by the stack segment selector, which was usually not pointing
at anything good. Thus, disassembly would always fault.

This branch fixes the ISR prototypes to take the registers by value, and
puts back `yaxpeax` disassembly.

Signed-off-by: Eliza Weisman <eliza@elizs.website>

---
## [Crozzers/screen_brightness_control](https://github.com/Crozzers/screen_brightness_control)@[3c736e2679...](https://github.com/Crozzers/screen_brightness_control/commit/3c736e26793d47cea4f834e936723482a1c6b12d)
#### Monday 2022-05-02 17:46:28 by Crozzers

Enable cross platform documentation building regardless of OS specific imports.

So when Pdoc would try to import `windows.py`, it would fail if you were building docs on Linux because `windows.py` imports various Windows only libraries that aren't available on Linux.
Furthermore, some of these Windows only objects are used in type hints which are evaluated by Pdoc, meaning I cannot just do what I did in commit 5d5d085.

What we do instead is override Pdoc's module import function (`pdoc.extract.load_module`) to intercept ImportError/ModuleNotFoundError exceptions. Using the exception we then can figure
out what it is that cannot be imported, eg: `from ctypes.wintypes import BOOL`. Once we know this, we then create a fake library in a temporary directory like so:

dummy_imports/dummies/
|-- ctypes/
   |-- __init__.py
   |-- wintypes.py

These fake libraries contain module-level `__getattr__` functions that respond to any request (eg: `from ctypes.wintypes import BOOL`) and return a dummy object that looks like
what you asked for, but is worthless. This allows OS specific imports and type hints to exist as long as the dummy objects are never used within actual code.
This is roughly how these fake modules and dummy objects behave:
```
from ctypes import rando_object
type(rando_object)
> <class 'dummy_imports.DummyObject'>
repr(rando_object)
> 'ctypes.rando_object'
```

Honestly, this is a hack but it's kinda cool at the same time.

---
## [gvreuls/Stockfish](https://github.com/gvreuls/Stockfish)@[cb9c2594fc...](https://github.com/gvreuls/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Monday 2022-05-02 17:51:56 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [capsaicinz/Skyrat-tg](https://github.com/capsaicinz/Skyrat-tg)@[b995fbe31b...](https://github.com/capsaicinz/Skyrat-tg/commit/b995fbe31b87402d3da2f8e98cec1f5659e52a47)
#### Monday 2022-05-02 18:04:29 by Zonespace

Contractor Expansion 2 (#12311)

* weh!

* fuck you linter

* very important

* Update modular_skyrat/modules/contractor/code/datums/midround/event.dm

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* Update modular_skyrat/modules/contractor/code/datums/midround/outfit.dm

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* requested changes

* also this

* requested + cleanup

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [brooje/Yogstation](https://github.com/brooje/Yogstation)@[25c038b994...](https://github.com/brooje/Yogstation/commit/25c038b99416dee4e64673d006e02e3ac208b13e)
#### Monday 2022-05-02 18:44:54 by Liberation

Merge pull request #40 from brooje/master

map patch improvements (and FUCK YOU MINING TURTLE)

---
## [AmerikanPsyko/cf-movie](https://github.com/AmerikanPsyko/cf-movie)@[dc7a862a44...](https://github.com/AmerikanPsyko/cf-movie/commit/dc7a862a447b8a6441094be778f3163500ea37a8)
#### Monday 2022-05-02 18:50:03 by AmerikanPsyko

fuck this

officially hate coding again. not happy, this course isn't designed for visual learners. Failing horribly. Might as well get a refund. Seriously, fuck all this. Im over it.

---
## [edsantiago/libpod](https://github.com/edsantiago/libpod)@[e74717f348...](https://github.com/edsantiago/libpod/commit/e74717f348c2768b87cad7dd6997c42dc85fc50a)
#### Monday 2022-05-02 19:06:18 by Ed Santiago

Treadmill script: revamp

Major revamp: instead of stacking a vendor commit on top of
the treadmill changes, do it the other way around: vendor,
then apply treadmill diffs.

Reason: the build-all-new-commits test. Sigh. It fails in the
common case where our treadmill changes include a new struct
element in cmd/podman/images/build.go

Why this is good: well, superficially, it's more intuitive.

Why this is horrible: omg the rebasing games are a nightmare.
When the vendor commit is on top (HEAD), it's ultra-trivial
to drop it, rebase the treadmill changes on main, then add
a new vendor-buildah commit on top. As you can see from the
diffs in this PR, treadmill-as-HEAD introduces all sorts
of complex dance steps in which things can go catastrophically
wrong and you can lose all your treadmill patches. I try very
hard to prevent this, and to offer hints if there's a problem,
and heck in the worst case it's still git so it's still possible
to find lost commits... but it's still much riskier than the
old way.

Alternative I considered: using sed magic to disable the
build-all-new-commits test. So tempting... but that would
also disable the bloat check.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [Emiliapains/Skyrat-tg](https://github.com/Emiliapains/Skyrat-tg)@[51acee2a18...](https://github.com/Emiliapains/Skyrat-tg/commit/51acee2a1841156e4d0ce9b2b9e9d3cd4fc9a7d8)
#### Monday 2022-05-02 19:40:06 by GoldenAlpharex

The MODsuit Digital Revolution: Replaces AIs in MODsuits with pAIs (#11135)

* Replaces AIs in MODsuits with pAIs

* Whoops forgot to remove that

* Lmao begone spellcheck shit

* I may be stupid

* Removing comments that commented code when they didn't really need to.

* Stupid linters

* Fixed the fact that mod wasn't a variable of the module anymore

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[8dd5e0ab3b...](https://github.com/UnderMybrella/usa/commit/8dd5e0ab3bc3964f5bd81c083017003cc38210d0)
#### Monday 2022-05-02 22:42:04 by MarkiSpider

Update 88 files @ Mon, 02 May 2022 22:42:00 GMT
This site update changes c-8-dickpicks.html, thedude.html, thejackson5.html, corn-dm.html, illinois.html, captainwhyareyoudoingthistome.html, girlofthe21stcentury.html, oopsalbangers.html, zeusandfriends.html, evidence.html, thekilleidoscope.html, karen6815.html, legal.html, the-baboonies.html, overview.html, thealienalliance.html, NerdFiction.html, shatteredbysomeone.html, .html, idkbro.html, messenger.html, lolgotyou.html, kriskringle.html, capitalism.html, cachow.html, karen-archive.html, the-d_.html, youreinthewrongpartoftown.html, karen6803.html, 914222-16152051420911213119153891920.html, logout.html, 914222-208502131102116.html, the-asshats.html, Rad_R.html, iinhumanresources.html, 914222-3421144920.html, 914222-5241612154525.html, thebannerborn.html, para.docs-portal, agentloginportal.html, dont-push.html, thefounders.html, ohyouwouldlikethatwouldntyou.html, 914222-20513165181205.html, inhumanresources.html, karen6815.html, whyami.html, karen6816.html, thekilleidoscope.html, everyone.html, terfwar.html, logout.html, agencydirectory.html, ijustmadeyoulookunderthere.html, messenger.html, howami.html, moriarty.html, fuckem.html, oopsalbangers.html, aretheyalium.html, kriskringle.html, thejackson5.html, whereareyou.html, schedule.html, evidence.html, youreinthewrongpartoftown.html, MichaelJackson.html, dontpush.html, departments.html, 914222-29151493191121139.html, cart.html, dickpicks.html, dickpicks.html, c-8-dickpicks.html, usaid-1121425-1.html, terminate-session.html, usaid-1121425.html, captainpleaseidontknowwhatshappeningimjustaneditor.html, usaid-1121425.html, invii-surveillance.html, usaid-1121425.html, mission-report.html, invii.html, usaid-1121425.html, fieldrequest-dashboard.html, push-reciept.jpg, envii.html, usaid-1121425.html

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[f875375703...](https://github.com/UnderMybrella/usa/commit/f8753757034c6dfd613e750b982c98e44275b287)
#### Monday 2022-05-02 22:42:29 by MarkiSpider

Update 124 files @ Mon, 02 May 2022 22:42:27 GMT
This site update changes para.docs-portal, dashboard.html, terfwar.html, employeeaccountabilitytimesignature-portal.html, zeusandfriends.html, images.html, redacted.html, thefounders.html, overview.html, 914222-20513165181205.html, MatPat.html, legal.html, captainwhyareyoudoingthistome.html, thealienalliance.html, 914222-29151493191121139.html, agencydirectory.html, helpcenter.html, dontpush.html, 914222-1952425161182025.html, thekilleidoscope.html, auth.html, dont-push.html, thejackson5.html, evidence.html, departments.html, user8118151241161251919.html, 914222-195242514914101.html, michaeljackson.html, logs.html, case-directory.html, kriskringle.html, the-d_.html, capitalism.html, inhumanresources.html, thebannerborn.html, everyone.html, aretheyalium.html, 914222-3151316212051825072125.html, 2702-invincible2syndicate.html, 914222-208502131102116.html, 914222-5241612154525.html, Imsorrymissjackson.html, cart.html, lolgotyou.html, Rad_R.html, illinois.html, shatteredbysomeone.html, 914222-16152051420911213119153891920.html, employeeaccountabilitytimesignature-portal.html, messenger.html, 914222-1916135212518.html, the-baboonies.html, helpcenter.html, michaeljackson.html, reviews.html, lolgotyou.html, thealienalliance.html, 914222-20513165181205.html, karen6804.html, 914222-3116201914.html, the-asshats.html, gettingjiggywithit.html, dont-push.html, 914222-1916151820192112124214513114.html, Jupiterandfriends.html, karen6816.html, para.docs-portal, cachow.html, dickpicks.html, capitalism.html, overview.html, thedude.html, 914222-5241612154525.html, karen6803.html, 914222-195242514914101.html, logs.html, thecaptain.html, iinhumanresources.html, thefounders.html, terfwar.html, terrorblycute.html, theoracle.html, karen-archive.html, search.html, whyami.html, sexygoldarms.html, 914222-3421144920.html, evidence.html, oopsalbangers.html, thejackson5.html, MichaelJackson.html, corn-dm.html, usa-home.html, zeusandfriends.html, 2702-invincible2syndicate.html, legal.html, suspect-hierarchy.html, cart.html, dontpush.html, NerdFiction.html, fuckem.html, redacted.html, captainwhyareyoudoingthistome.html, schedule.html, youreinthewrongpartoftown.html, invii_suspects.html, intel.html, current-position.html, usaid-1121425.html, dickpicks.html, supply-req.html, usaid-1121425.html, usaid-1121425.html, mission-report.html, youreinthewrongpartoftown.html, MRING.html, dickpicks.html, dickpicks.html, invii-surveillance.html, usaid-1121425.html, cart.html, dickpicks.html, usaid-1121425.html, invii.html

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[7e69ac59f8...](https://github.com/UnderMybrella/usa/commit/7e69ac59f87f570e4d7472eee681bf4f8580506b)
#### Monday 2022-05-02 22:42:56 by MarkiSpider

Update 88 files @ Mon, 02 May 2022 22:42:54 GMT
This site update changes corn-dm.html, c-8-dickpicks.html, 914222-195242514914101.html, usa-home.html, ohyouwouldlikethatwouldntyou.html, employeeaccountabilitytimesignature-portal.html, girlofthe21stcentury.html, 914222-3421144920.html, terrorblycute.html, thecaptain.html, dontpush.html, nebuchadnezzar.html, thealienalliance.html, captainwhyareyoudoingthistome.html, moriarty.html, thefounders.html, ijustmadeyoulookunderthere.html, theoracle.html, user.html, thejackson5.html, oopsalbangers.html, MichaelJackson.html, dont-push.html, 914222-29151493191121139.html, the-baboonies.html, helpcenter.html, cases.html, MatPat.html, evidence.html, karen-archive.html, case-directory.html, karen6803.html, 914222-1916151820192112124214513114.html, the-d_.html, 914222-3151316212051825072125.html, karen6816.html, thebannerborn.html, 914222-16152051420911213119153891920.html, sexygoldarms.html, 914222-5241612154525.html, karen6809.html, suspect-hierarchy.html, inhumanresources.html, cart.html, woahhh.html, 914222-3151316212051825072125.html, Rad_R.html, karen6803.html, thekilleidoscope.html, agencydirectory.html, 914222-5241612154525.html, karen6816.html, logout.html, theoracle.html, thebannerborn.html, karen6804.html, karen6809.html, 914222-3116201914.html, messenger.html, the-asshats.html, 914222-195242514914101.html, iinhumanresources.html, overview.html, dickpicks.html, illinois.html, terfwar.html, Imsorrymissjackson.html, 914222-1916151820192112124214513114.html, reviews.html, schedule.html, oopsalbangers.html, youreinthewrongpartoftown.html, fuckem.html, NerdFiction.html, idkbro.html, the-secret-lies-just-a-little-farther.html, redacted.html, case-directory.html, howami.html, usaid-1121425.html, envii.html, mission-report.html, intel.html, current-position.html, usaid-1121425.html, usaid-1121425.html, assignments.html, inbox.html

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[a221e43166...](https://github.com/UnderMybrella/usa/commit/a221e43166e068f200202584fb5781e743499160)
#### Monday 2022-05-02 22:44:25 by MarkiSpider

Update 92 files @ Mon, 02 May 2022 22:44:23 GMT
This site update changes reviews.html, oopsalbangers.html, the-baboonies.html, departments.html, girlofthe21stcentury.html, nebuchadnezzar.html, MatPat.html, moriarty.html, captainwhyareyoudoingthistome.html, .html, employeeaccountabilitytimesignature-portal.html, karen6815.html, fuckem.html, agentloginportal.html, idkbro.html, overview.html, terrorblycute.html, MichaelJackson.html, messenger.html, gettingjiggywithit.html, illinois.html, 914222-1952425161182025.html, auth.html, helpcenter.html, legal.html, aretheyalium.html, 914222-3151316212051825072125.html, logs.html, suspect-hierarchy.html, 914222-208502131102116.html, Imsorrymissjackson.html, Rad_R.html, sexygoldarms.html, logout.html, karen6803.html, cart.html, 914222-3116201914.html, dickpicks.html, 914222-208502131102116.html, agencydirectory.html, para.docs-portal, helpcenter.html, everyone.html, thealienalliance.html, karen6816.html, illinois.html, thebutterflysoldiers.html, thekilleidoscope.html, ijustmadeyoulookunderthere.html, thecaptain.html, 914222-201516156208512914513151814914741815145.html, 914222-195242514914101.html, search.html, thedude.html, capitalism.html, karen-archive.html, michaeljackson.html, theoracle.html, lolgotyou.html, sexygoldarms.html, Rad_R.html, reviews.html, karen6809.html, karen6803.html, 914222-3151316212051825072125.html, overview.html, case-directory.html, aretheyalium.html, redacted.html, kriskringle.html, LixianTV.html, usa-home.html, corn-dm.html, suspect-hierarchy.html, nebuchadnezzar.html, thejackson5.html, usaid-1121425.html, cart.html, usaid-1121425.html, fieldrequest-dashboard.html, current-position.html, intel.html, usaid-1121425.html, assignments.html, usaid-1121425.html, invii.html, c-8-dickpicks.html, usaid-1121425.html, dickpicks.html, usaid-1121425.html, usaid-1121425.html, terminate-session.html

---
## [trarocha/bluefoot](https://github.com/trarocha/bluefoot)@[a74f838203...](https://github.com/trarocha/bluefoot/commit/a74f838203a5ed19176a126dc131bc896d50478d)
#### Monday 2022-05-02 23:46:31 by Robin Mathison

im so fucking confused why this shit dont work boutta fight god on jah

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[fbb3ba032c...](https://github.com/mrakgr/The-Spiral-Language/commit/fbb3ba032c6a9877052f447dddc44ce05b1b325a)
#### Monday 2022-05-02 23:53:37 by Marko Grdinić

"2:15pm. Done with breakfast. Let me chill for a bit more and then I will resume.

2:35pm. Let me read Tog 241 and I will resume. I'll leave the BRS ep for later.

2:50pm. Let me resume. I had my bit of fun. Ok, let me think. Let me just import it in Substance.

Hmmm, how does this work? Substance seems to be using the correct UVs, but how does it know which ones they are?

https://youtu.be/C5ifOS8EAA4
Blender to Substance Painter Multiple UV maps with one object

Maybe instead of using multi UVs I should have used UDIMs. I might have to redo the layers, but nevermind that for now. Let me watch the above.

https://youtu.be/C5ifOS8EAA4?t=890

Thankfully I just skimmed instead of watching all of this. No, I have no choice. If I want multiple UV maps on the same object, I am going to have to use UDIMs. Thankfully this is not like the desk which would take me a lot of time to redo. I can easily redo this what I've done easier. All this time I've spent messing with various issues.

3:05pm. Hmmm. This is complicated. Maybe what I did with the object before was more sensible if I wanted more than one UV. I can't figure out how to select between UV sets in Painter. Just how does it associate materials to UVs?

https://youtu.be/9ONcJ_f5w7I
Substance Painter Auto UV Tutorial [is it really that great?]

I can't find this on Google.

Let me ask on /3/ how substance does UV selection.

I asked on /3/. Now let me watch the auto UV tutorial.

https://youtu.be/9ONcJ_f5w7I?t=106

Is this really Blender? Just what kind of exporter is this?

3:25pm. I am thinking that is is a good opportunity to try out RizomUV. Blender's auto unwrapper will not respect seams, so I'd need to either do it all by hand or try something other than Blender.

Hmmm, hmmm, actually if I select only the base material, unwrap that, and then unwrap the logo parts separately, that would give me what I want anyway. I could just do it like that. But this is still a good chance to try out Rizom.

https://youtu.be/9ONcJ_f5w7I?t=237

Ah, right. If I let Substance do it, it will separate out the UVs for the texture sets. I could simply do it like that. But how would I export UVs? Export Mesh? That has to be it.

Let me watch the tutorial to the end.

https://youtu.be/9ONcJ_f5w7I?t=392
> That took about 3m give or take.

That sure is long. It did not show me how to export the UVs back. Also can it set up UVs for UDIMs?

3:35pm. https://forum.substance3d.com/index.php?topic=36814.0
> You don't save Painter files, you just go to File->Export Mesh and you'll get the mesh with those unwrapped UVs.

Yeah, it is as I suspected. Now...

https://youtu.be/opNdazTgmFg
RizomUV Introduction Tutorial - Unwrapping a Teapot from 3ds max

Let me watch this 8m video.

https://youtu.be/opNdazTgmFg?t=63

Hmmm, no clean up after booleans.

https://youtu.be/opNdazTgmFg?t=155

This is not too impressive. Maybe RizomUV has a good packer.

But UV Packmaster is already pretty good in my opinion. So if I were to use Rizom, I'd be mostly interested in it auto unwrapping capabilities.

https://youtu.be/opNdazTgmFg?t=172

This is pretty new. The object gets unfolded in the 3d view.

https://youtu.be/ioN53mV1cFE
Learn Unwrapping in 5 minutes | Rizom VS & RS

Let me move to this vid. I do not feel like watchin the other one.

If I wanted to place cuts, I'd have done it in Blender.

https://youtu.be/ioN53mV1cFE?t=47

He says unwrapping this in 3ds max would take 1 day.

https://youtu.be/ioN53mV1cFE?t=170

He is placing cuts manually. Nevermind Rizom, I don't need it. I think that if it manual unwrapping, Blender is good enough. Let me play around with Substance's auto UV unwrapping.

4pm. My sense is that the UVs coming out of Pt are decent. Sure some areas might be stretched, but how care about that.

Actually, no this is pretty bad. I am looking at them in 3d view and they look very distored. A few extra cuts could have gone a long way.

Let me try Houdini's auto UV tools. I want to see if they respect material boundaries. This is my main problem with Blender.

4:20pm. https://www.youtube.com/results?search_query=houdini+udim+uv

My hunch is that Houdini is much better. It makes multiple cuts and gets rid of distortions, and it obeys the material boundaries, but its packing leaves much to be desired.

https://youtu.be/oHoifUuLXcQ

Let me check out some of these tutorials.

https://youtu.be/oHoifUuLXcQ?t=87

Ah, right. Doing a loop is an option.

https://youtu.be/oHoifUuLXcQ?t=134

Ah, here is the UDIM tiles option.

4:35pm. That was pretty enlightening. I can use either that. But I could also use the UV packmaster in Blender after auto UV it in Houdini.

4:45pm. https://uvpackmaster.com/doc3/blender/latest/50-troubleshooting/

I am getting inconsistent island errors in UV packmaster.

4:55pm. Holy, shit what a waste of time. Now that I am looking at the UVs, I see overlaps everywhere. Houdini did an attrocious job. Sigh, let me try out RizomUV.

5pm. Now I have another Zbrush complex program to learn. As if I have nothing better to do than optimize UVs all day. Quck, where is the auto unwrap button.

https://youtu.be/tu3rfUPIAhc
Rizom UV: The Unwrap Panel

Let me just watch this.

5:10pm. I see ZenUV on AEblender, but for whatever reason it is acting like Persia when I do not access it from the correct side. It worked yesterday, so why is it giving me trouble now?

https://www.aeblender.com/2022/01/blender-3-zen-uv-v2-2-2-library-2022-updatedownload/

This site is such cancer, but it has a lot of useful addons. I just want an unwrap that respects island boundaries, is that so much to ask for?

Also before I forget, Zbrush also has something for UVs. Let me try it out.

5:15pm. The model gets wrecked when Zbrush imports it. It is so bad at it.

5:25pm. Let me try installing Zen UV. What a drag. I guess I'll have to go back to the tutorial hell for a bit. Rizom UV should have given me a way to auto unwrap in 5 minutes. I am not interested in learning yet another massive application.

5:25pm. Ok, it installs. I keep seeing Blender blasted in /3/ threads due to all the addons being commercial, but they are still a lot cheaper than competing products.

5:25pm. Now, I guess I'll go for a ZenUV tutorial. There is no way around it. I might as well stick to Blender since I am already there.

https://youtu.be/I3wvUG4A5P0
ZEN UV addon for Blender - overview and tutorial

I checked this out, and it seems it is only 9$.

Edit: I messed up, it is 19$.7

https://youtu.be/I3wvUG4A5P0?t=271

Keymaps have a search in Blender. This is great. Compare this to Rhino which just lists out all the key combinations and leave it to you to find them.

5:45pm. This is really fancy, but not as fancy as Rizom which is good. Rizom has a large number of options and it is hostile to get into.

But now that I am getting into this I am starting to come to an understanding. My idea of separating out the relevant section by material is no longer valid now that I want to add things like dust and minor imperfections. Like with the desk, I am better off getting a 4k texture and slapping it on.

https://youtu.be/I3wvUG4A5P0?t=407

Ah, it is Ctrl + ~ to go into this menu. I forgot and couldn't find it in the past few days.

https://youtu.be/I3wvUG4A5P0?t=605

6:15pm. https://youtu.be/I3wvUG4A5P0?t=675

Before looking at this, I spent some time looking for small islands unmarking them by hand.

6:55pm. Had to stop for lunch. Let me resume.

7:20pm. Holy shit I hate this. What the hell am I doing. I wanted to find an auto UV unwrapping method, so why am I unwrapping by hand. I have all these shitty overlaps to deal with, and the decimated model is full of tiny long faces that are hard to see. If I am going to do it by hand, I should have done it on the standard model.

Let me finish the tutorial by Ponte.

7:45pm. This is ridiculous, why is it refusing to distributed the Islands to different UDIMs on its own. Did I have this problem with the desk?

7:50pm. This is super annoying. I tell him to pack up the UDIMs and it is leaving one of them empty.

8:40pm. It was right to leave it empty. But now I got this working. I put all the parts of the monitor into two UDIM tiles.

What a waste of time this was. This will teach me a lesson not to hurry up UVs. I really regret applying the monitor modifiers before putting in the seams. Had I not done so, my job would have been a lot easier.

The plugin is quite buggy, but it has some useful functionality.

8:55pm. https://youtu.be/qB1eg3ef5vs?t=277

Now I am watching this. Sigh, what a pain. I already want to stop doing 3d.

https://youtu.be/qB1eg3ef5vs?t=285

Instead of doing this, what he should do is remesh the whole thing while keeping the hard edges and then do a normal transfer.

He could also have done an inset on the affected ngons.

https://youtu.be/qB1eg3ef5vs?t=387

I'll keep this matcap in mind.

9:05am. I am using it on the monitor and oh crap, the undecimated version has a lot better shading. This one really brings them out, a lot more than the red. You can really see the lines slide across the triangles. I thought that decimating with 0.1 would not be a big deal, but I see I was wrong.

Well, it is not like it will be visible in the render, so I won't worry about it.

No, doing an inset on that ngon would not deal with the problem unfortunately.

https://youtu.be/qB1eg3ef5vs?t=142

The issue is that the bevel pretty much wreacked the intended curvature. Just what are you going to do after doing something like this?

At least if you did something like this with Moi, you'd have the necessary information to construct the proper curvature. In Blender once you get a non-planar ngon, you have an ill defined problem. Triangulating this would not help. If you have a planar ngon, you can inset it, and that would solve the shading issues.

9:20pm. Just take a loot at how hacky the solution to these shading issues are. It is no wonder I am drawn to doing it in Moi 3d, or using subdiv, or hard surface sculpting.

Hmmm, let me try something in Blender with subdiv.

1:45am. I playing around with a dube all this time cutting loops into it and observing the subdiv topology. I am really getting a grasp on how it works.

It is actually fairly easy to get good subdiv topology. I thought it would be difficult, but it is not. There are simple rules to getting it.

I am crazy to go on doing this for this long. But I guess this is what is fun for me now. I keep delaying that BRS episode further and further. I'll get to it tomorrow, after I finish the monitor.

I feel that thanks to this experimentation, my ability to understand topology has improved."

---

