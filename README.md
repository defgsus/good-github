## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-23](docs/good-messages/2022/2022-06-23.md)


1,748,651 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,748,651 were push events containing 2,649,389 commit messages that amount to 200,182,845 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 27 messages:


## [bvo773/Leetcode](https://github.com/bvo773/Leetcode)@[cd5d95a5a2...](https://github.com/bvo773/Leetcode/commit/cd5d95a5a293496c2c5c587b2d3a3e4b0b5fd7ee)
#### Thursday 2022-06-23 03:47:35 by Binh Vo

Thanks Lord for blessing me with the abilities to read code and try to think creatively in algorithm, i thank you my church, family, friends for helping me in this journey and may we look above and remember the mission you have planned, Amen

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[95ffcd4e19...](https://github.com/san7890/bruhstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Thursday 2022-06-23 04:15:59 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[d23b2319c8...](https://github.com/treckstar/yolo-octo-hipster/commit/d23b2319c875c51dfb9d3367f6dddea7168b3655)
#### Thursday 2022-06-23 04:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [arueckauer/laminas-authentication](https://github.com/arueckauer/laminas-authentication)@[2bdd7faf28...](https://github.com/arueckauer/laminas-authentication/commit/2bdd7faf28dffe187cd663c58b9c0c9f935ec95d)
#### Thursday 2022-06-23 05:14:03 by Michał Bundyra

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
## [C7-Game/Prototype](https://github.com/C7-Game/Prototype)@[d4cb71a167...](https://github.com/C7-Game/Prototype/commit/d4cb71a1673b919ddf87d8afcbb2e8ad9ad25352)
#### Thursday 2022-06-23 06:25:31 by Quintillus

WIKI INFO - Build out strategic priorities a little bit.  WarPriority is a notable one as it is the first one that includes properties.

I've tried to build the priorities so there will be a common interface.  The goal being that new priorities can be added being mods, and they can still be serialized.  The interface should help for this.  If all of our StrategicPriorities were bespoke hard-coded, it might be convenient, but it would not lend itself to extensibility.

The challenge is going to be how do we merge those priorities, convenience of writing the logic, extensibility, and serialization?

This is still an evolving thought process, and I'm not totally sold on this dictionary-of-dictionaries approach, it just seemed like the most convenient way to return a weight *and* some required data about how that weight was chosen and what to do if this priority is chosen by the arbitrator.

The other half of the thought process that's not yet fully coded is that if a priority is chosen, its info should be stored in the data classes.  My general thought here is that by returning property maps, we should be able to store those, and a reference to the type of StrategicPriority, in the data classes, allowing us to reconstruct objects of the appropriate type, put in the relevant properties, and re-load from save.

The engine will also have to be able to look up the priorities based on name... maybe a key type thing?  This should also be stored in the save.  So basically, on load the engine will have the key, the weight, and properties.  It'll use the key to find the appropriate class, instantiate an instance, and stuff the properties onto that instance (and maybe the weight or maybe that's higher-level metadata that goes elsewhere).  This yields an fully inflated StrategicPriority instance that the AI part of the engine can then reference to calculate things.

Combining this with a lookup mechanism for StrategicPriorities should yield moddability.  I'm reminded of Java's "Service Provider Interface" concept, the gist of which is that if you make a class that follows an interface, and register it with the JVM in a certain way in your program, the JVM magically gains new capabilities.  An example is if I write an image processor for PCX files, and register it correctly, the general image ImageIO capabilities in Java can now magically handle PCX files, e.g. ImageIO.load("x_title.pcx") will just work, even though in stock Java it wouldn't know what to do with a PCX.  It works for other types of services too.  Our specifics will differ, but I think the goal should be similar - if you write a new StrategicPriority and follow a given interface, it'll magically be incorporated with the AI.

The remaining hard part is how is the strategic AI looped in to decision-making?  There are theoretically a thousand places this could be looped in, but if we want it to be extensible, we have to have standard interfaces.  But the StrategicPriority also has to know enough about the situation to be able to interpret what's going on.

For now I'm thinking some combination of weights and modifiers being providable by the strategic priority.  E.g. for city production, it should be able to make some things be produced more often, and that's a weight based thing.  But I'm sure there's other cases I'm not thinking of that make things more complex.  I'm also aware of what Jon or Soren mentioned somewhere about overly generic AIs sometimes not being decisive enough.  It'll be interesting...

---
## [wangshuli0315/binaryen](https://github.com/wangshuli0315/binaryen)@[d1bea49163...](https://github.com/wangshuli0315/binaryen/commit/d1bea49163be364d6f8b277b35510555211374b5)
#### Thursday 2022-06-23 07:36:12 by Alon Zakai

TrapsNeverHappen mode (#4059)

The goal of this mode is to remove obviously-unneeded code like

(drop
  (i32.load
    (local.get $x)))

In general we can't remove it, as the load might trap - we'd be removing
a side effect. This is fairly rare in general, but actually becomes quite
annoying with wasm GC code where such patterns are more common,
and we really need to remove them.

Historically the IgnoreImplicitTraps option was meant to help here. However,
in practice it did not quite work well enough for most production code, as
mentioned e.g. in #3934 . TrapsNeverHappen mode is an attempt to fix that,
based on feedback from @askeksa in that issue, and also I believe this
implements an idea that @fitzgen mentioned a while ago (sorry, I can't
remember where exactly...). So I'm hopeful this will be generally useful
and not just for GC.

The idea in TrapsNeverHappen mode is that traps are assumed to not
actually happen at runtime. That is, if there is a trap in the code, it will
not be reached, or if it is reached then it will not trap. For example, an
(unreachable) would be assumed to never be reached, which means
that the optimizer can remove it and any code that executes right before
it:

(if
  (..condition..)
  (block
    (..code that can be removed, if it does not branch out..)
    (..code that can be removed, if it does not branch out..)
    (..code that can be removed, if it does not branch out..)
    (unreachable)))

And something like a load from memory is assumed to not trap, etc.,
which in particular would let us remove that dropped load from earlier.

This mode should be usable in production builds with assertions
disabled, if traps are seen as failing assertions. That might not be true
of all release builds (maybe some use traps for other purposes), but
hopefully in some. That is, if traps are like assertions, then enabling
this new mode would be like disabling assertions in release builds
and living with the fact that if an assertion would have been hit then
that is "undefined behavior" and the optimizer might have removed
the trap or done something weird.

TrapsNeverHappen (TNH) is different from IgnoreImplicitTraps (IIT).
The old IIT mode would just ignore traps when computing effects.
That is a simple model, but a problem happens with a trap behind
a condition, like this:

if (x != 0) foo(1 / x);

We won't trap on integer division by zero here only because of the
guarding if. In IIT, we'd compute no side effects on 1 / x, and then
we might end up moving it around, depending on other code in
the area, and potentially out of the if - which would make it happen
unconditionally, which would break.

TNH avoids that problem because it does not simply ignore traps.
Instead, there is a new hasUnremovableSideEffects() method
that must be opted-in by passes. That checks if there are no side
effects, or if there are, if we can remove them - and we know we can
remove a trap if we are running under TrapsNeverHappen mode,
as the trap won't happen by assumption. A pass must only use that
method where it is safe, that is, where it would either remove the
side effect (in which case, no problem), or if not, that it at least does
not move it around (avoiding the above problem with IIT).

This PR does not implement all optimizations possible with
TNH, just a small initial set of things to get started. It is already
useful on wasm GC code, including being as good as IIT on removing
unnecessary casts in some cases, see the test suite updates here.
Also, a significant part of the 18% speedup measured in

#4052 (comment)

is due to my testing with this enabled, as otherwise the devirtualization
there leaves a lot of unneeded code.

---
## [csware/putty](https://github.com/csware/putty)@[c19e7215dd...](https://github.com/csware/putty/commit/c19e7215ddd1d6a890fdb94d89bc5ccb46151363)
#### Thursday 2022-06-23 07:56:01 by Simon Tatham

Replace mkfiles.pl with a CMake build system.

This brings various concrete advantages over the previous system:

 - consistent support for out-of-tree builds on all platforms

 - more thorough support for Visual Studio IDE project files

 - support for Ninja-based builds, which is particularly useful on
   Windows where the alternative nmake has no parallel option

 - a really simple set of build instructions that work the same way on
   all the major platforms (look how much shorter README is!)

 - better decoupling of the project configuration from the toolchain
   configuration, so that my Windows cross-building doesn't need
   (much) special treatment in CMakeLists.txt

 - configure-time tests on Windows as well as Linux, so that a lot of
   ad-hoc #ifdefs second-guessing a particular feature's presence from
   the compiler version can now be replaced by tests of the feature
   itself

Also some longer-term software-engineering advantages:

 - other people have actually heard of CMake, so they'll be able to
   produce patches to the new build setup more easily

 - unlike the old mkfiles.pl, CMake is not my personal problem to
   maintain

 - most importantly, mkfiles.pl was just a horrible pile of
   unmaintainable cruft, which even I found it painful to make changes
   to or to use, and desperately needed throwing in the bin. I've
   already thrown away all the variants of it I had in other projects
   of mine, and was only delaying this one so we could make the 0.75
   release branch first.

This change comes with a noticeable build-level restructuring. The
previous Recipe worked by compiling every object file exactly once,
and then making each executable by linking a precisely specified
subset of the same object files. But in CMake, that's not the natural
way to work - if you write the obvious command that puts the same
source file into two executable targets, CMake generates a makefile
that compiles it once per target. That can be an advantage, because it
gives you the freedom to compile it differently in each case (e.g.
with a #define telling it which program it's part of). But in a
project that has many executable targets and had carefully contrived
to _never_ need to build any module more than once, all it does is
bloat the build time pointlessly!

To avoid slowing down the build by a large factor, I've put most of
the modules of the code base into a collection of static libraries
organised vaguely thematically (SSH, other backends, crypto, network,
...). That means all those modules can still be compiled just once
each, because once each library is built it's reused unchanged for all
the executable targets.

One upside of this library-based structure is that now I don't have to
manually specify exactly which objects go into which programs any more
- it's enough to specify which libraries are needed, and the linker
will figure out the fine detail automatically. So there's less
maintenance to do in CMakeLists.txt when the source code changes.

But that reorganisation also adds fragility, because of the trad Unix
linker semantics of walking along the library list once each, so that
cyclic references between your libraries will provoke link errors. The
current setup builds successfully, but I suspect it only just manages
it.

(In particular, I've found that MinGW is the most finicky on this
score of the Windows compilers I've tried building with. So I've
included a MinGW test build in the new-look Buildscr, because
otherwise I think there'd be a significant risk of introducing
MinGW-only build failures due to library search order, which wasn't a
risk in the previous library-free build organisation.)

In the longer term I hope to be able to reduce the risk of that, via
gradual reorganisation (in particular, breaking up too-monolithic
modules, to reduce the risk of knock-on references when you included a
module for function A and it also contains function B with an
unsatisfied dependency you didn't really need). Ideally I want to
reach a state in which the libraries all have sensibly described
purposes, a clearly documented (partial) order in which they're
permitted to depend on each other, and a specification of what stubs
you have to put where if you're leaving one of them out (e.g.
nocrypto) and what callbacks you have to define in your non-library
objects to satisfy dependencies from things low in the stack (e.g.
out_of_memory()).

One thing that's gone completely missing in this migration,
unfortunately, is the unfinished MacOS port linked against Quartz GTK.
That's because it turned out that I can't currently build it myself,
on my own Mac: my previous installation of GTK had bit-rotted as a
side effect of an Xcode upgrade, and I haven't yet been able to
persuade jhbuild to make me a new one. So I can't even build the MacOS
port with the _old_ makefiles, and hence, I have no way of checking
that the new ones also work. I hope to bring that port back to life at
some point, but I don't want it to block the rest of this change.

---
## [jrusz/osbuild-composer](https://github.com/jrusz/osbuild-composer)@[af44202b1c...](https://github.com/jrusz/osbuild-composer/commit/af44202b1c6e53a5d3a248e2c1c493445743f188)
#### Thursday 2022-06-23 09:03:00 by Ondřej Budai

cloudapi: rename gpg_key field to gpgkey

Oh no, we made a mistake here: Both our json repositories and repo files in
/etc/yum.repos.d have the GPG key in a field named `gpgkey`. Unfortunately,
cloudapi uses a field named `gpg_key`. One consequence of this issue is that
our api.sh test is meant to pass GPG keys in the compose request but since
it's using a bad field name (`gpgkey`), the key is actually not used.

I've decided to fix this in cloudapi: The `gpg_key` field is now renamed to
`gpgkey`. This is a breaking change but no one is using this API anyway so
we think it's better to do this now than introducing weird backward
compatible hacks.

Signed-off-by: Ondřej Budai <ondrej@budai.cz>

---
## [datalayer-externals/k8s-cluster-api-aws](https://github.com/datalayer-externals/k8s-cluster-api-aws)@[867afc7ac7...](https://github.com/datalayer-externals/k8s-cluster-api-aws/commit/867afc7ac718621a11e00fc2b05589ac2548d4d5)
#### Thursday 2022-06-23 09:54:23 by Claudia Beresford

Fail apidiff make target when git fails

This is a fairly simple fix to ensure that when `git diff` fails on the
`make apidiff` target, the exit code is actually picked up by make.
Previously the exit code from `diff` was "swallowed" by the `if`.

eg:
```
$ cat Makefile
thing:
        if (exit 1); then \
		echo foo; \
        fi
        echo "still here"

$ make thing
still here
$ echo $?
0
```

What we want:
- exit 1 when `git diff` fails
- exit 0 when `grep` fails
- call `go-apidiff` when `git diff` and `grep` succeeds
- exit 1 when `go-apidiff` fails

This is honestly a complete pain to do in a Makefile.

I tried capturing output, moving everything to a script, calling from
one thing to another. But really this is just tricky to do the way we
want in Make.

So, if we can live with a little repetition, we can do the following:
- Check the `git diff` can run, exit 1 if not
- Run the `git diff` again, this time piping the successful command to
  `grep`
- If `grep` fails, then no worries, the target will roll on and exit 0
  like it always has.
- If `grep` succeeds then the `go-apidiff` tool is called and the target
  runs as intended.

------

In the case of `$(APIDIFF_OLD_COMMIT)`, there is some annoying `make`
magic going on here. Which I can't simply make fail since it will cause any
job which uses something in this Makefile to fail out of proximity.
The `shell` is expanded when the file is loaded meaning even targets
which do not care about the value will end up erroring (but not exiting)
when it fails. These are not errors which impact the target's run, but
they look annoying in CI.

Since this var is only used by `apidiff`, we can move it into that
target so it is only evaluated when specifically called.

---
## [clementleger/linux](https://github.com/clementleger/linux)@[b9364eed92...](https://github.com/clementleger/linux/commit/b9364eed9232f3d2a846f68c2307eb25c93cc2d0)
#### Thursday 2022-06-23 10:02:06 by Douglas Anderson

drm/msm/dpu: Move min BW request and full BW disable back to mdss

In commit a670ff578f1f ("drm/msm/dpu: always use mdp device to scale
bandwidth") we fully moved interconnect stuff to the DPU driver. This
had no change for sc7180 but _did_ have an impact for other SoCs. It
made them match the sc7180 scheme.

Unfortunately, the sc7180 scheme seems like it was a bit broken.
Specifically the interconnect needs to be on for more than just the
DPU driver's AXI bus. In the very least it also needs to be on for the
DSI driver's AXI bus. This can be seen fairly easily by doing this on
a ChromeOS sc7180-trogdor class device:

  set_power_policy --ac_screen_dim_delay=5 --ac_screen_off_delay=10
  sleep 10
  cd /sys/bus/platform/devices/ae94000.dsi/power
  echo on > control

When you do that, you'll get a warning splat in the logs about
"gcc_disp_hf_axi_clk status stuck at 'off'".

One could argue that perhaps what I have done above is "illegal" and
that it can't happen naturally in the system because in normal system
usage the DPU is pretty much always on when DSI is on. That being
said:
* In official ChromeOS builds (admittedly a 5.4 kernel with backports)
  we have seen that splat at bootup.
* Even though we don't use "autosuspend" for these components, we
  don't use the "put_sync" variants. Thus plausibly the DSI could stay
  "runtime enabled" past when the DPU is enabled. Techncially we
  shouldn't do that if the DPU's suspend ends up yanking our clock.

Let's change things such that the "bare minimum" request for the
interconnect happens in the mdss driver again. That means that all of
the children can assume that the interconnect is on at the minimum
bandwidth. We'll then let the DPU request the higher amount that it
wants.

It should be noted that this isn't as hacky of a solution as it might
initially appear. Specifically:
* Since MDSS and DPU individually get their own references to the
  interconnect then the framework will actually handle aggregating
  them. The two drivers are _not_ clobbering each other.
* When the Qualcomm interconnect driver aggregates it takes the max of
  all the peaks. Thus having MDSS request a peak, as we're doing here,
  won't actually change the total interconnect bandwidth (it won't be
  added to the request for the DPU). This perhaps explains why the
  "average" requested in MDSS was historically 0 since that one
  _would_ be added in.

NOTE also that in the downstream ChromeOS 5.4 and 5.15 kernels, we're
also seeing some RPMH hangs that are addressed by this fix. These
hangs are showing up in the field and on _some_ devices with enough
stress testing of suspend/resume. Specifically right at suspend time
with a stack crawl that looks like this (from chromeos-5.15 tree):
  rpmh_write_batch+0x19c/0x240
  qcom_icc_bcm_voter_commit+0x210/0x420
  qcom_icc_set+0x28/0x38
  apply_constraints+0x70/0xa4
  icc_set_bw+0x150/0x24c
  dpu_runtime_resume+0x50/0x1c4
  pm_generic_runtime_resume+0x30/0x44
  __genpd_runtime_resume+0x68/0x7c
  genpd_runtime_resume+0x12c/0x20c
  __rpm_callback+0x98/0x138
  rpm_callback+0x30/0x88
  rpm_resume+0x370/0x4a0
  __pm_runtime_resume+0x80/0xb0
  dpu_kms_enable_commit+0x24/0x30
  msm_atomic_commit_tail+0x12c/0x630
  commit_tail+0xac/0x150
  drm_atomic_helper_commit+0x114/0x11c
  drm_atomic_commit+0x68/0x78
  drm_atomic_helper_disable_all+0x158/0x1c8
  drm_atomic_helper_suspend+0xc0/0x1c0
  drm_mode_config_helper_suspend+0x2c/0x60
  msm_pm_prepare+0x2c/0x40
  pm_generic_prepare+0x30/0x44
  genpd_prepare+0x80/0xd0
  device_prepare+0x78/0x17c
  dpm_prepare+0xb0/0x384
  dpm_suspend_start+0x34/0xc0

We don't completely understand all the mechanisms in play, but the
hang seemed to come and go with random factors. It's not terribly
surprising that the hang is gone after this patch since the line of
code that was failing is no longer present in the kernel.

Fixes: a670ff578f1f ("drm/msm/dpu: always use mdp device to scale bandwidth")
Fixes: c33b7c0389e1 ("drm/msm/dpu: add support for clk and bw scaling for display")
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Abhinav Kumar <quic_abhinavk@quicinc.com>
Tested-by: Jessica Zhang <quic_jesszhan@quicinc.com> # RB3 (sdm845) and
Reviewed-by: Stephen Boyd <swboyd@chromium.org>
Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@linaro.org>
Patchwork: https://patchwork.freedesktop.org/patch/487884/
Link: https://lore.kernel.org/r/20220531160059.v2.1.Ie7f6d4bf8cce28131da31a43354727e417cae98d@changeid
Signed-off-by: Abhinav Kumar <quic_abhinavk@quicinc.com>

---
## [HyperScorpio/store1](https://github.com/HyperScorpio/store1)@[ba63081d10...](https://github.com/HyperScorpio/store1/commit/ba63081d109c904902958c6324b013cb10b42732)
#### Thursday 2022-06-23 11:26:07 by 0kmg

gameboy.xml: Added 21 more prototypes. (#9962)

* gameboy.xml: Added 21 more prototypes.

New working software list additions
-----------------------------------
Astérix (earlier prototype) [VGHF, Hidden Palace]
Astérix (early prototype) [VGHF, Hidden Palace]
Asteroids (prototype) [VGHF, Hidden Palace]
Barbie - Game Girl (prototype) [VGHF, Hidden Palace]
Battle Ships (Spain, prototype) [VGHF, Hidden Palace]
Blaster Master Boy (USA, prototype) [VGHF, Hidden Palace]
Bomb Jack (earlier prototype) [VGHF, Hidden Palace]
Bomb Jack (later prototype) [VGHF, Hidden Palace]
Bonk's Adventure (USA, prototype) [VGHF, Hidden Palace]
Bubble Ghost (prototype) [VGHF, Hidden Palace]
Catrap (prototype) [Forest of Illusion, Swanhubstream]
Cosmo Tank (USA, prototype) [VGHF, Hidden Palace]
Dropzone (prototype, alt) [VGHF, Hidden Palace]
Gauntlet II (prototype) [Forest of Illusion, Rezrospect]
Ghostbusters II (prototype) [VGHF, Hidden Palace]
Kung-Fu Master (prototype) [Forest of Illusion, FNeogeo]
Mysterium (prototype) [Forest of Illusion, Rezrospect]
Obélix (Europe, French / German, prototype) [Forest of Illusion]
Prince of Persia (prototype) [Forest of Illusion, FNeogeo]
The Blues Brothers (prototype) [Forest of Illusion, FNeogeo]
Triumph (prototype) [Gaming Alexandria]

---
## [KeyboardGecko/Fallout-Nevada-Translation](https://github.com/KeyboardGecko/Fallout-Nevada-Translation)@[22ad04d3bb...](https://github.com/KeyboardGecko/Fallout-Nevada-Translation/commit/22ad04d3bbfd92ba1428a9acee61462e28af463e)
#### Thursday 2022-06-23 11:57:49 by QuantumApprentice

check on this one?

line 57 {167} I'm not sure if this character is intentionally referring to a male "workaholic" or workaholics in general.  I fixed the english for a singular workaholic (possibly referring to a character in his backstory?) but please check if the phrase should be more generic. ie:
"And when such stupid workaholics, greedy for money, die from exposure, they are then burned in the incinerator and their earned money split in the office."

---
## [jeffnavy14/Omicron](https://github.com/jeffnavy14/Omicron)@[ccf500070d...](https://github.com/jeffnavy14/Omicron/commit/ccf500070d4448d1e2acbdb711190d5b4e21c4e6)
#### Thursday 2022-06-23 13:05:31 by neuromancerxi

Add scripts and adjust plumbing for many temp items (#670)

* Add scripts and adjust plumbing for many temp items

Adds Scripts for items.
Adds Effect scripts for X_BOOST_II
Updates Effect scripts for the following:

ACCURACY_BOOST
ATTACK_BOOST
INTENSION
MAGIC_SHIELD
MULTI_STRIKES
MULTI_SHOTS
PAX
PHYSICAL_SHIELD
POTENCY
RAMPART

Adjusts item_usable use times to 1s.

Notes on effects:

Ascetics Tonic/Gambir - +25/+50 MATT/MACC
A big Thank You to Nyu for confirming the Intension effect for MACC.
https://www.bg-wiki.com/bg/Ascetic's_Tonic
https://www.bg-wiki.com/bg/Ascetic's_Gambir

Bravers Drink - +15 to All Stats
https://www.bg-wiki.com/bg/Braver's%20Drink
Reference to Icons/Effects - https://youtu.be/JYT5a_pTA3o?t=20

Champions Tonic - +15 Haste / +3 Crit rate
Champions Drink/Gambir - +18 Haste / +5% Crit rate
Expected Haste effect to be Magic pool based on BG comment (18 and 15)
Critical Hit rate, no data available from community sources, conservative value of 5 (Drink/Gambir) 3 (Tonic)
Both BG and 'clopedia sources confirm Critical Hit Rate (as does the effect description), however, only BG has a reference to Haste value.
https://www.bg-wiki.com/bg/Champion's_Tonic

Gnostics Drink - Enmity -10
No community resources confirm this value, using SCH Animus Minuo as an reference.
https://www.bg-wiki.com/bg/Gnostic's%20Drink
https://www.bg-wiki.com/bg/Animus_Minuo

Monarchs Drink - Regain +3 (30/1000 per tick) for 3 minutes.
https://www.bg-wiki.com/bg/Monarch's_Drink

Stalwart's Tonic/Gambir - ACC/RACC 50/100 ATTP/RATTP 25/50
A big Thank You to Nyu for confirming the effects apply ACC/RACC and ATTP/RATTP across two effects.
https://www.bg-wiki.com/bg/Stalwart's_Tonic
https://www.bg-wiki.com/bg/Stalwart's_Gambir

Berserker's Tonic/Drink - DA 50/100
Thanks to Nyu for confirming the MULTI_STRIKES effect and 1m duration.
https://ffxiclopedia.fandom.com/wiki/Berserker%27s_Drink
No full data on DA rate, minus 'clopedia which has verification tags. Working on the expectation that this follows a good portion of the other items and follows the half potency values for the lesser item.

Swiftshot Tonic/Drink - Double Shot 50/100
https://www.ffxiah.com/forum/topic/28603/fools-tonic-broken#1749569

Dusty Scroll of Reraise - Reraise III, 10m duration.
https://www.bg-wiki.com/bg/Dusty_Reraise

Spiritual Incense/Fools Drink/Tonic/Powder: See effects/magic_shield
Carnal Incense/Fanatics Drink/Tonic/Powder: See effects/physical_shield

* Removed copypasta subp and trailing whitespace.

* Item script clean-up and move effect functions to item_utils.

* Resolve Conflicts

Convert namespace in scripts from item_utils to xi.item_utils
PHYS_ABSORB to Percent from 10000 Scale

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7e30fe4310...](https://github.com/mrakgr/The-Spiral-Language/commit/7e30fe43109ad25acc936d01fe447edb5806e70e)
#### Thursday 2022-06-23 13:05:46 by Marko Grdinić

"10am. https://blenderartists.org/t/scatter-5-2-brand-new-release/1177672/3094?u=marko_grdinic
> hi, i can’t replicate that. i tried the steps several times… do you happen to have that blend file saved for me to have a look? if that error happens, have you tried to re-enter manual mode?

Ok, let me just do this and then I will get started on putting down the city. I can't let this take any more time.

I've decided what my style needs to be. Though it is not optimal, me thinking for aeons about the trivial things seems to be a part of my process, so I should simply make do with my art having less detail.

10:20am. It does not matter. I have to not get caught up trying to compete with Blender pros in their own styles otherwise it will consume all my time.

At any rate, I finally made that bug report. Let me get started on this. Today I want to be all art. First of all, I want to figure out how to do instancing by scale. Oh, there is a spawn option.

10:25am. Er, let me just read the latest Futanari no Elf chapter and I will resume. I go distracted by the thread.

https://sites.google.com/view/scatter5docs/manual/instancing

I need to focus on this. I'll get to it.

...Ok, focus me.

10:55am. Nope the rotation and scale settings brushes do not work for me.

11:05am. https://sites.google.com/view/scatter5docs/manual/instancing

Let me try the manual index. I forgot about this. I do not think that instance scale is exactly what I am looking for.

11:10am. Found another bug. I can't change the index in the manual distribution brush. Let me report it. I guess I'll just use multiple system. The simplest way is the best I guess.

11:25am. Damn it, I need to adjust the assets so that Y axis points to the front. Well, let me just do it.

11:45am. Finally corrected the assets so that the front of the buildings points in the right direction. This is important due to how the comb brushes work. Having them correctly oriented in the 'Asset' scene will make them a lot easier to use when importing.

https://news.ycombinator.com/item?id=31843932

A hiring ad for ML engineer and it even is remote. I've come to a conclussion. Seeing how Graphcore and TensTorrent struggle to compete against years old Nvidia GPUs, I've dodged a bullet by not getting a job at AI chip companies. If things are like this I might as well get a job anywhere. The next time I apply I am going to kick honest to the curb and get whatever. It does not matter if this company for example wants to make AI, any such attempts before the secrets of the brain are revealed are a waste of time.

Art is where it's at. Sure I might be missing on valuable exp programming, but that skill is already leveled high enough. The rest I can just bullshit my way through if needed.

Now focus. I have the assets.

You know what, it is too troublesome to use multiple systems in manual mode. I really want to be able erase as I see fit...

12pm. it is really awkward that I can't use the manual index properly.

Well, whatever. Let me break out the tablet. Let me just get the initial layout done.

Sigh, the spray brush concetrates the houses in the middle instead of spreading them out across the radius. Also radius changes are linear instead of exponential. Let me just go into sculpt to see it has the same behavior.

1:35pm. Let me get breakfast here. I am quite into it. I am getting a handle on how this works. Getting in touch with the devs was 100% the correct course of action to take. I've managed to find workarounds for all the bugs. I'll be done with the concept for the city before long. Roads? Forget about those.

2:40pm. Done with both breakfast and the Birdie Wing ep. It is time to resume.

Let me just spend some time aligning the buildings, after that I'll do some shading. Then I will set up the city below as a bunch of cubes.

When I feel like I have the scene down, then I will move to putting in more details.

3pm. Let me resume now. I had to chill a bit more.

Focus me. I should just do this and not complicate the scene anymore than it needs to be. If I need details I can do them later. This is the great advantage of 3d. I need to focus on gradually building up the scene.

The Scatter 5 manual mode is really revolutionary. It is to scattering what sculpting is to modeling. Well worth the price I 'paid' for the addon. I'll actually get the full version once I make 100$ from art."

---
## [alphagov/govuk-prototype-kit](https://github.com/alphagov/govuk-prototype-kit)@[9678167f17...](https://github.com/alphagov/govuk-prototype-kit/commit/9678167f176a4bfd409d2b73939be304853e521e)
#### Thursday 2022-06-23 13:13:18 by Laurence de Bruxelles

Change tests to generate a release archive only once

Use a lockfile to make sure that if the test helper `mkReleaseArchive()`
is called more than once, it won't create more than one
`create-release-archive` process. The behaviour we want is that it all
calls will block until the initial process has finished.

The way I figured to do that was that all calls try and acquire a
lockfile (atomically), if that lockfile is already held that means
another call is already creating the release archive. When the lockfile
is released, the process should have successfully created a release
archive, so no extra work is needed.

Unfortunately, in Node.js it seems there is no way to block waiting for
a lockfile to be released, so we have to rewrite the test utils and all
relevant tests to be asynchronous. To be fair they should have been
asynchronous in the first place, but it was still a very painful
process.

Note that I haven't rewritten the scripts in `cypress/scripts` to use
async functions; without the use of top-level await it was a bit more
effort than I was prepared to do, compounded with the fact that
there doesn't seem to be an easy way to await `child_process.spawn()`
(`util.promisify` doesn't work), and async `child_process.exec()` and
`child_process.execFile()` don't do `stdio: 'inherit'`. Maybe the only
way around it is to use the `execa` library (: Anyway I couldn't be
dealing with that, so now we have to deal with duplication in
`__tests__/util`. There are ...ways... to reduce the duplication
(proper-lockfile does this with its `lib/adapter` module) but they are a
bit magic, and plus it means writing our code using callbacks, which is
just... woof. No.

Anyway as you can tell this is has been a great learning opporunity :')
Just use async the first time and save myself the pain later!!

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[ebfaf7498c...](https://github.com/canalplus/rx-player/commit/ebfaf7498c0803b0dc38ffdea3096c8422d388ef)
#### Thursday 2022-06-23 13:26:12 by Paul Berberian

Update most dependencies but Jest

This commit update almost all dependencies but jest.

This is because Jest 28 seems to break while running code, presumably
due to `import`/`export` declarations in imported RxJS files (but I do
not think RxJS is at fault here) that lead to an `unexpected token` when
running through Jest.

You could think that the fault is linked to node not understanding
`import`/`export` (linked to CommonJS/ES6 import shenanigans) but it is
even trickier than that as Jest already performed some JavaScript
transformation at that point, which made the import/export inside an
IIFE - and I'm not sure that this is supported anywhere.

After taking ~a day (much more time than I should) trying to play around
to remove that issue, I gave up and avoided updating Jest to its v28.

In the future, I guess we should either:

  - understand what we're supposed to do here to make it work with Jest
    28 (Jest documentation was poor - even without considering the
    sometimes incomprehensible google-translated french one I get each
    time by default on their docusaurus-based documentation)

    Opened GitHub issues were 100% for angular-based applications - as it
    seems the RxJS+TypeScript cocktail is very majoritarily those. Those
    have their own "fix" through another magical angular dependency.

    Moreover, it does not help that Jest's philosophy seems to be trying to be
    extremely simple for users at the cost of some complex behaviors (as an
    example, it looks like it auto-picks a `babel.config.js` file if it
    sees one at the root of the project. If like us you have multiple build
    files at the root depending on the building context, it is not a good
    idea to silently pick random files like that by default).

    I couldn't understand under an acceptable time where the issue was - and
    at which step it happened.
    I just browsed dozens of doc pages, GitHub and StackOverflow issues
    which just proposed to add yet other automagic dependencies (looked like a
    parody of what JavaScript haters talk about!) - which all seemed to have
    no effect whatsoever.

    I also asked for help from other teams at Canal+, but those in the
    same situation (TypeScript and RxJS) also seem to have random issue
    preventing them from doing the switch.

  - Remove RxJS from the code. It's presumably not its fault yet we
    already started doing that, so maybe we'll just raise the jest
    version once RxJS is definitely removed from the RxPlayer.

  - Wait for some kind of Jest fix or new way of handling those?

  - Remove Jest and go with another testing framework.

    I almost did that due to being fed-up with Jest, but it might no be
    as easy as it seems, mostly the module-mocking part as I'm unsure of
    how other framework handle that now and if it is as convenient as
    Jest's way.

---
## [downthecrop/2009scape-mirror](https://github.com/downthecrop/2009scape-mirror)@[ce14aa0e80...](https://github.com/downthecrop/2009scape-mirror/commit/ce14aa0e8094933c95ea0d33d28cd97e621fa275)
#### Thursday 2022-06-23 13:35:17 by skelsoft

Over 30+ monsters with added sfx, tick respawn fixes, and stat corrections

Unicorn (ID 89, 987) Unicorn Foal (ID 1328) and Unicorn stallion (ID 6822, 6823) combat sfx added
Unicorn (ID 89) respawn delay corrected (90 ticks/54 seconds)
Unicorn Foal (ID 1328) stats, attack speed, and respawn delay corrected (90 ticks/54 seconds)
Black unicorn (ID 133) and Black unicorn foal (ID 1329) combat sfx added
Black unicorn (ID 133) stats, attack speed, and respawn delay corrected (90 ticks/54 seconds)
Black unicorn Foal (ID 1329) stats, attack speed and respawn delay corrected (20 ticks/12 seconds)
Angry unicorn (ID 3646, 3661) combat sfx added
Angry unicorn (ID 3646, 3661) stats and attack speed corrected
Rock Crab (ID 1265, 1267) and Giant Rock Crab (ID 2452, 2885) combat sfx added
Rock Crab (ID 1265, 1267) attack speed and respawn delay corrected (50 ticks/30 seconds)
Giant Rock Crab (ID 2452, 2885) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Ice giant (ID 111, 3072, 4685, 4686, 4687) combat sfx added
Ice giant (ID 111, 3072, 4685, 4686, 4687) respawn delay corrected (30 ticks/18 seconds)
Ice warrior (ID 125, 145, 3073) combat SFX added
Ice warrior (ID 125, 145, 3073) respawn delay corrected (30 ticks/18 seconds)
Basilisk (ID 1616, 1617, 4228) combat SFX added
Basilisk (ID 1616, 1617, 4228) stats, attack speed and respawn delay corrected (15 ticks/9 seconds)
Al-Kharid warrior (ID 18) combat sfx added
Al-Kharid warrior (ID 18) stats, attack speed and respawn delay corrected (25 ticks/15 seconds)
Magic axe (ID 127) combat sfx added, as well as its combat bonii corrected
Chaos dwarf (ID 119) combat sfx added
Black Knight (ID 178, 179, 6189) combat sfx added
Black Knight (ID 178, 179, 6189) stats, attack speed and respawn delay corrected (25 ticks/15 seconds)
Giant bat (ID 78, 1005, 2482, 3711) combat sfx added
Giant bat (ID 78, 1005, 2482, 3711) stats, attack speed, and respawn delay corrected (35 ticks/21 seconds)
Grizzly bear (ID 105, 1195) combat sfx added
Grizzly bear (ID 105) combat level 21 stats, attack speed, and respawn delay corrected (50 ticks/30 seconds)
Grizzly bear (ID 1195) combat level 42 stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Black bear (ID 106) combat sfx added
Black bear (ID 106) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Cave horror (ID 4353, 4354, 4355, 4356, 4357) combat sfx added
Cave horror (ID 4353, 4354, 4355, 4356, 4357) respawn delay corrected (50 ticks/30 seconds)
Jungle horror (ID 4348, 4349, 4350, 4351, 4352) combat sfx added
Jungle horror (ID 4348, 4349, 4350, 4351, 4352) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Hobgoblin (Spear-wielding) (ID 123, 2688, 4898) combat sfx added
Waterfiend (ID 5361) combat sfx added
Waterfiend (ID 5361 stats and attack speed corrected
Banshee (ID 1612) combat sfx added
Banshee (ID 1612) stats, attack speed and respawn delay corrected (15 ticks/9 seconds)
Angry bear (ID 3645, 3664) combat sfx added
Angry bear (ID 3645, 3664) stats and attack speed corrected
Seagull (ID 2707, 6115, 6116) combat sfx added
Ghast (ID 1052, 1053) combat sfx added
Icefiend (ID 3406, 6217, 7714, 7715) combat sfx added
Jackal (ID 1994) combat sfx added
Jackal (ID 1994) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Kalphite Soldier (ID 1154, 3589) combat sfx added
Kalphite Worker (ID 1153, 1156) combat sfx added
Vulture (ID 3675, 3676) combat sfx added
Vulture (ID 3675, 3676) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Chompy bird (ID 1550) combat sfx added
Chompy bird (ID 1550) stats, examine, and poison immunity corrected
Minotaur (ID 4404, 4405, 4006) combat sfx added
Minotaur (ID 4404, 4405) stats, attack speed, examine, and respawn delay corrected (15 ticks/9 seconds)
Minotaur (ID 4006) combat level 27 stats, attack speed, examine, and respawn delay corrected (15 ticks/9 seconds)
Penance Fighter (ID 5040) combat sfx added
Skeletal Wyvern (ID 3068, 3069, 3070, 3071) combat sfx added (TODO: attack sound check)
Harpie Bug Swarm (ID 3153) combat sfx added
Harpie Bug Swarm (ID 3153) stats, attack speed and respawn delay corrected (25 ticks/15 seconds)
Harpie Bug Swarm (ID 3153) now correctly attacks with Melee
Molanisk (ID 5751) combat sfx added
Molanisk (ID 5751) stats and attack speed corrected
Mudskipper (ID 3422, 3423) combat sfx added
Mudskipper (ID 3422) combat level 30 stats, attack speed and respawn delay corrected (10 ticks/6 seconds)
Mudskipper (ID 3423) combat level 31 stats, attack speed and respawn delay corrected (5 ticks/3 seconds)
Aberrant spectre (ID 1604, 1605, 1606, 1607) combat sfx added
Aberrant spectre attack speed corrected
Cave slime (ID 1831) combat sfx added
Cave slime (ID 1831) stats, poison amount, attack speed and respawn delay corrected (15 ticks/9 seconds)
Stag (ID 4440) combat sfx added
Stag (ID 4440) stats, attack speed and respawn delay corrected (90 ticks/54 seconds)
Terrorbird (ID 138, 139, 1751) combat sfx added
Terrorbird (ID 138, 139, 1751) stats, attack speed and respawn delay corrected (30 ticks/18 seconds)
Chaos Elemental (ID 3200) respawn delay corrected (100 ticks/60 seconds)
General Graardor (ID 6260) respawn delay corrected (150 ticks/90 seconds)
Sergeant Grimspike (ID 6265) Ranged Strength bonus corrected
Commander Zilyana (ID 6247) respawn delay corrected (150 ticks/90 seconds)
Starlight (ID 6248) attack speed and poison immunity corrected
Kree'arra (ID 6222) respawn delay corrected (150 ticks/90 seconds)
Wingman Skree (ID 6223) poison immunity corrected
Flockleader Geerin (ID 6225) poison immunity corrected
K'ril Tsutsaroth (ID 6203) poison amount and respawn delay corrected (150 ticks/90 seconds)
Zakl'n Gritch (ID 6206) ranged strength bonus corrected

---
## [dotnet-maestro-bot/msbuild](https://github.com/dotnet-maestro-bot/msbuild)@[a572dc6b79...](https://github.com/dotnet-maestro-bot/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Thursday 2022-06-23 14:19:15 by Forgind

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
## [metabase/metabase](https://github.com/metabase/metabase)@[9c4e73899e...](https://github.com/metabase/metabase/commit/9c4e73899e8914fd41e85987d4a652a9b6058d8a)
#### Thursday 2022-06-23 14:27:51 by dpsutton

Enterprise settings (#23441)

* Allow for disabling settings

Disabled settings will return their default value (else nil if no
default is set). This allows us to have enterprise override settings and
use them from regular OSS code without classloaders, extra vars,
remembering to check if the feature is enabled, etc.

Motivating examples are the appearance settings. We allow
`application-font` setting to change the font of the application. This
is an enterprise feature, but anyone can post to
`api/setting/application-font` and set a new value or startup as
`MB_APPLICATION_FONT=comic-sans java -jar metabase.jar` and have the
functionality.

Same thing for application colors in static viz. The calling code just
calls `(settings/application-colors)` and uses them but doesn't check if
the enterprise settings are enabled. To do this correctly, you have to
remember to implement the following onerous procedure:

A whole namespace for a setting
```clojure
(ns metabase-enterprise.embedding.utils
  (:require [metabase.models.setting :as setting :refer [defsetting]]
            [metabase.public-settings :as public-settings]
            [metabase.public-settings.premium-features :as premium-features]
            [metabase.util.i18n :refer [deferred-tru]]))

(defsetting notification-link-base-url
  (deferred-tru "By default \"Site Url\" is used in notification links, but can be overridden.")
  :visibility :internal
  :getter (fn []
            (when (premium-features/hide-embed-branding?)
              (or (setting/get-value-of-type :string :notification-link-base-url)
                  (public-settings/site-url)))))
```

And then in the calling code you have to do the procedure to
conditionally require it and put it behind a var that can handle it
being nil:

```clojure
;; we want to load this at the top level so the Setting the namespace defines gets loaded
(def ^:private site-url*
  (or (u/ignore-exceptions
        (classloader/require 'metabase-enterprise.embedding.utils)
        (resolve 'metabase-enterprise.embedding.utils/notification-link-base-url))
      (constantly nil)))

;; and then the usage
(defn- site-url
  "Return the Notification Link Base URL if set by enterprise env var, or Site URL."
  []
  (or (site-url*) (public-settings/site-url)))
```

Far nicer to just place the following into the regular public-settings
namespace:

```clojure
(defsetting notification-link-base-url
  (deferred-tru "By default \"Site Url\" is used in notification links, but can be overridden.")
  :visibility :internal
  :enabled?    premium-features/hide-embed-branding?)
```

Then no need for a custom namespace to hold this setting, no need to
have an extra var to point to the setting else a fallback value.

Note that this feature is not required on every enterprise feature we
have. We a namespace `metabase-enterprise.sso.integrations.sso-settings`
that has 24 settings in it, all of which are enterprise features. But
these features are used in our enterprise sso offerings and are directly
referenced from the enterprise features. No need for the extra var to
point to them and the flag checks happen in other parts.

* Mark the UI/UX customization settings as requiring whitelabeling

Mark the following settings as requiring
premium-settings/enable-whitelabeling? (aka token check)

- application-name
- loading-message (override of "doing science")
- show-metabot (override of showing our friendly metabot)
- application-colors
- application-font
- application-logo-url
- application-favicon-url

Updates the helper functions for colors to use the setting rather than
feeling entitled to use a lower level `setting/get-value-of-type`. We
need the higher level api so it takes into account if its enabled or
not.

* Move notification-link-base-url into regular settings with enabled?

* Cleanup ns

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[8962f88f90...](https://github.com/microsoft/terminal/commit/8962f88f907d86fd8684b66f7f3e32a2709e3237)
#### Thursday 2022-06-23 15:40:33 by Dustin L. Howett

Disable the VT color quirk for pwsh and modern inbox powershell (#13352)

In #6810, we introduced a "quirk" for all known versions of PowerShell
that suppressed their requests for black background/gray foreground.
This was done to avoid an [issue in PSReadline] where it would paint
black bars all over the screen if the default background color wasn't
the same as the ANSI black color.

Years have passed since that quirk was introduced. The underlying bug
was fixed, and the fix was released broadly long ago. It's time for us
to remove the quirk... almost.

Terminal still runs on versions of Windows that ship a broken version of
PSReadline. We must maintain the quirk there -- the user can't do
anything about it, and we would make their experience worse if we
removed the quirk entirely.

PowerShell 7.0 also ships a broken version of PSReadline. It is still in
support for another 6 months, but updates have been available for some
time. We can encourage users to update.

Therefore, we only need the quirk for Windows PowerShell, and then only
for specific versions of Windows.

_Inside Windows_, we don't even need that: we're guaranteed to be built
alongside a fixed version of PowerShell!

Closes #6807

[issue in PSReadline]: https://github.com/PowerShell/PSReadLine/issues/830#issuecomment-650508857

---
## [Saul-Dickson/dotfiles](https://github.com/Saul-Dickson/dotfiles)@[91e3e32b98...](https://github.com/Saul-Dickson/dotfiles/commit/91e3e32b98cfb5cfaffbb6cadf09ced66d270ffe)
#### Thursday 2022-06-23 16:20:31 by Saul-Dickson

Resuming the EWW bar development process.

I mistakenly assumed I had to completely reinstall arch lol. Turns out
there was some weird shit happening in my BIOS and that's all I had to
do. I'm frankly ashamed that it took me so long to figure out what was
happening. Anyway, I've gone and remade my BSPWM testing script (which
uses Xephyr, btw) and I'll be adding doing some work on my EWW config. I
really want to get out of Gnome. I'm getting sick of the weird issues it
has.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0fea6325c2...](https://github.com/treckstar/yolo-octo-hipster/commit/0fea6325c2ac25c151ec0d2e7a26b9551ddad166)
#### Thursday 2022-06-23 18:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [newstools/2022-the-irish-times](https://github.com/newstools/2022-the-irish-times)@[ab0ab969b3...](https://github.com/newstools/2022-the-irish-times/commit/ab0ab969b388312928e782e89b0b02bdd44806d5)
#### Thursday 2022-06-23 18:34:20 by Billy Einkamerer

Created Text For URL [www.irishtimes.com/life-style/people/2022/06/23/michael-harding-in-my-teens-i-lost-a-girlfriend-and-i-cried-my-eyes-out-like-boys-were-not-supposed-to-do/]

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[cba46da98b...](https://github.com/mrakgr/The-Spiral-Language/commit/cba46da98bdbaa11612c34871954e6ced999bfe6)
#### Thursday 2022-06-23 19:02:35 by Marko Grdinić

"The spot in the middle is too empty. Let me put down the Grand Casino.

4pm. It crashed so hard it took down the whole rig with it. Thankfully I am saving as I go along.

Right now I am trying to get the overall color composition right. Having an emissive floor is not a good idea. It messed with the light from other sources.

4:10pm. It crashed again. Maybe it is linked to Cycles being on.

4:15pm. And again. Ugh. Reminds me of V-Ray in Houdini.

4:25pm. This is the 4th time Cycles took down my entire system. Sigh...

4:35pm. 5th time. Blender is very crash happy in the latest version. Let me play around with the monkey head. I want to refresh my memory of the volume shader.

4:40pm. 6th time, this time on just the monkey head. Were the older version this unstable? Cycles in unusable here.

https://developer.blender.org/T96133

Let me play around in 3.1. Then I will check out 3.0.

Since the file appears to be forward compatible, let me take advantage of that to open it in 3.1.

4:55pm. Too bad Scatter 5 does not work in 3.1. I am obligated to use 3.2 now.

5:10pm. It crashes even with F12. 7th time.

Yeah, Cycles in unusable in 3.2.

I could try upgrading the graphics driver and seeing if that helps. But otherwise, let me just use Eevee. Or even Luxcore.

5:35pm. It seems this scene will get done one reset at a time. Let me take a break so I can upgrade my graphics drivers. Maybe that will help. This is not just an ordinary crash. Each time it took down the entire system.

5:45pm. The driver seems to be a decent behind. I had 517 while the latest is 571. The driver install does not allow me to leave out GeForce Experience. Well, as long as it does not bother me on startup I'll be happy.

Ok, let me give it a try. But I am not too hopeful. This is serious issue. If this does not work, I might end up having to use Eevee.

The save is actually corrupted.

5:55pm. Thankfully there are backups. I am not losing much except time.

I need to stop. I can't work like this.

Did Cycles work in 3.1, I think it did not crash there.

Ok, can I convert the Scatter 5 scene into Blender instances and import them in 3.2.

7:05pm. Done with lunch. While I was busy with that the render finished properly in the background. It seems that 3.1 is stable for me. Now that I have this, let me put it through style transfer.

```py
def save_path(data,path):
    """Returns the save path."""
    def get_name(x):
        base_name = ntpath.basename(data[x][0])
        return ntpath.splitext(base_name)[0]

    a_path = get_name('A_paths')
    image_name = '%s (%s).png' % (a_path, get_name('B_paths'))
    return os.path.join(path, a_path, image_name)
```

Let me change the way saving is done a little. I'll have it create it own dir for every image.

```py
os.makedirs(save_path,exist_ok=True)
```

I think I need to plug this in. Let me try it.

```
PermissionError: [Errno 13] Permission denied: './results/floating city v0\\floating city v0 (anime glasses girl).png'
```

Hmmm...

```
os.makedirs(os.path.dirname(save_path),exist_ok=True)
```

Let me try this.

7:20pm. Yeah, that works. While that is going on I might as well do a bug report.

No, I want to test 3.1 more thoroughly before I jump to conclussion that it is more stable.

7:25pm. Right now what happened is that the style transfer crashed and took the OS with it. Is my GPU dying?

7:35pm. I suppose this will do.

7:55pm. https://developer.blender.org/T99116
Cycles crashes after a few minutes of work

I opened this, but the bug report is not very informative, so I am not sure if anything will come of it.

This scene is cursed!

How is it possible that I am running into problems with Cycles all of a sudden. Just how am I supposed to do this scene?

8:05pm. Let me post one of the images that came out well in /wip/ and then I'll close.

///

This scene is cursed. I got a grasp on Scatter 5, and minus the bugs, its manual mode is revolutionary. It is to scattering what sculpting is to modeling.

I ran into all sorts of bugs with it, found workarounds with the help of the author, but now that I am doing shading I can't go more than 2m without Cycles crashing and taking the OS with it. This is not happening with previous 3.1 version of Blender so I managed to export the building instances and render it there.

I have no choice, but to keep going forward. I have a vague sense of what I want to do, but I am having trouble understanding how to make the scene impactful.

This particular style is not bad in isolation, but I don't think it will work once I add the other half of the scene. The way I am visualizing it is a view of the floating city from below as the golden light from it washes over the landscape. This particular style will make everything golden and that detail would get washed out.

///

I guess I'll post it on Twitter as well.

8:40pm.

> This sounds like a bug in OS or your hardware is failing. I would recommend to check system temperatures, and voltages in case of PSU failiure.
> I don't think remember any issue with similar symptoms to be ever confirmed as bug in Blender.

Got this reply from a Blender dev. Maybe I should open the rig and dust it off. Maybe there is a program that can help me diagnose temperatures and voltages? I should look for it.

8:45pm. Getting called a schizo and told to take my meds on /wip/ is really annoying. Maybe I should drop that place, like I said I would the last two times? Let me do a style transfer on a crab image, reply with it and then I am done for the day.

It actually did crash once while doing style transfer earlier. This really makes me concerned about the state of my hardware. It is quite scary. If the PC gives out before I can make money from Heaven's Key to replace it I really will drop all the art practice and get a job. Some things you simply have to take as an omen.

9pm. https://openhardwaremonitor.org/
> The Open Hardware Monitor is a free open source software that monitors temperature sensors, fan speeds, voltages, load and clock speeds of a computer.

I'll try this program tomorrow. I'll close here today."

---
## [morningsd/library](https://github.com/morningsd/library)@[acbd2ee29b...](https://github.com/morningsd/library/commit/acbd2ee29b85eacfd9af5a93835941c1406bc030)
#### Thursday 2022-06-23 22:03:25 by morningsd

I just wanna sleep, no normal comments for today (i will hate myself tomorrow)

---
## [ThatGuyFromThatPlace/sojourn-station](https://github.com/ThatGuyFromThatPlace/sojourn-station)@[9f7af6b698...](https://github.com/ThatGuyFromThatPlace/sojourn-station/commit/9f7af6b698a6633907432576f9699af209dec6cd)
#### Thursday 2022-06-23 22:27:55 by nikothedude

FUCKING HOTFIX FOR A STUPID FUCKING BUG (#3459)

* FUCK

* HOLY SHIT IM DUMB

---
## [katydecorah/font-library](https://github.com/katydecorah/font-library)@[5e2f493d11...](https://github.com/katydecorah/font-library/commit/5e2f493d11e0dd0fe02a32678f26336c96fb97f5)
#### Thursday 2022-06-23 23:44:02 by jeannie2

Update families.json (#484)

Added tags for 17 fonts without any tags: Inspiration, Inter, Jua, Lexend, Legend Deca, Legend Giga, Legend Exa, Potta One, Praise, Nanum Gothic Coding, Oooh Baby, Puppies Play, Rock 3D, Single Day, Shizuru, Style Script, Send Flowers 

Removed tag "caps" for Sedgewick Ave (only applies to Sedgwick Ave Display) -> sorry I didn't tag correctly

---

