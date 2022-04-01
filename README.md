## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-31](docs/good-messages/2022/2022-03-31.md)


1,743,566 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,743,566 were push events containing 2,789,744 commit messages that amount to 200,019,227 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 37 messages:


## [acidmanifesto/TrinityCoreCustomChanges](https://github.com/acidmanifesto/TrinityCoreCustomChanges)@[434d607c51...](https://github.com/acidmanifesto/TrinityCoreCustomChanges/commit/434d607c51e5a56abd57dcfb00d558ac0bb2db88)
#### Thursday 2022-03-31 00:04:43 by MDIC

feat (New Detection) Ignore Z-Axis

Thank you for the amazing input and information @mdX7 .
This is the ignore Z-Axis Detection.  The cheat is when a user blocks their z-axis from updating with the server resulting in them running\moving in the air. Flight Hack Detection would not detect them.
Warning: Some light false positives may occur on certain parts of the area\map if there is any "pot holes" of sorts. Like it is in Az-Core.

Co-Authored-By: ModoX <moardox@gmail.com>

---
## [Henrique-Shiguemoto/tsp-heuristics](https://github.com/Henrique-Shiguemoto/tsp-heuristics)@[862401d6a3...](https://github.com/Henrique-Shiguemoto/tsp-heuristics/commit/862401d6a3b9915f0772ef59c1414c281d8c7152)
#### Thursday 2022-03-31 00:23:19 by Rick Shiguemoto

Added new input files, some of them are ridiculously large files, my teacher simply doesn't understand that students don't own multiple hundred servers with top-of-the-line CPUs and GPUs to calculate pla33810 and pla85900, fuck college honestly, get me out

---
## [marcelo-gonzalez/nearcore](https://github.com/marcelo-gonzalez/nearcore)@[6351eb5511...](https://github.com/marcelo-gonzalez/nearcore/commit/6351eb55116fea2f906d681ce6966b5ec2546176)
#### Thursday 2022-03-31 00:50:50 by Simonas Kazlauskas

Use non-blocking log writer (#6470)

This will utilize a separate thread to write out the spans and events
without while letting the main computation to proceed with its business.
Additionally, we are buffering the output by lines, thus reducing the
frequency of syscalls that can occur when the subscriber is writing out
parts of the message.

This should mitigate concerns of enabling debug logging as its impact on
performance should now be minimal (putting an event structure onto a
MPSC queue.) There are still costs associated with logging everything
however. Most notably formatting and construction of the
`tracing_core::ValueSet`s still occur on the caller side, so if
constructing those is expensive, the logging might remain expensive.
An example of code sketchy like that (although silly) could be:

```
debug!(message = { std::time::sleep(Duration::from_secs(1)); "hello" })
```

or for a less silly example:

```
debug!("{}", my_vector.iter().map(|...| {
  do_expensive_stuff()
}).collect::<String>())
```

These should be considered a bug (alas one that `tracing` does not have
any tooling to detect, sadly.)

I opted adding a new crate dedicated to observability utilities. From my
experience using things like prometheus will eventually result in a
variety of utilities being written, so this crate eventually would
likely expand in scope...

Fixes https://github.com/near/nearcore/issues/6072 (though I haven't made any actual measurements as to what the improvement really is)

---
## [yxmline/pcsx2](https://github.com/yxmline/pcsx2)@[89f10e1605...](https://github.com/yxmline/pcsx2/commit/89f10e160572063b4871bfb8d0c6ffff54f9543a)
#### Thursday 2022-03-31 00:51:00 by RedDevilus

GameDB:  ':' to '-' + GS and other fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Outrun 2006 / 2 SP
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

Also made sure that the comments and their spacing were consistent.

---
## [avar/git](https://github.com/avar/git)@[e40e4f4772...](https://github.com/avar/git/commit/e40e4f47720f61aac204ca94132948ef6f7dddb6)
#### Thursday 2022-03-31 00:53:37 by Ævar Arnfjörð Bjarmason

pack-objects: lazily set up "struct rev_info", don't leak

In the preceding [1] (pack-objects: move revs out of
get_object_list(), 2022-03-22) the "repo_init_revisions()" was moved
to cmd_pack_objects() so that it unconditionally took place for all
invocations of "git pack-objects".

We'd thus start leaking memory, which is easily reproduced in
e.g. git.git by feeding e83c5163316 (Initial revision of "git", the
information manager from hell, 2005-04-07) to "git pack-objects";

    $ echo e83c5163316f89bfbde7d9ab23ca2e25604af290 | ./git pack-objects initial
    [...]
	==19130==ERROR: LeakSanitizer: detected memory leaks

	Direct leak of 7120 byte(s) in 1 object(s) allocated from:
	    #0 0x455308 in __interceptor_malloc (/home/avar/g/git/git+0x455308)
	    #1 0x75b399 in do_xmalloc /home/avar/g/git/wrapper.c:41:8
	    #2 0x75b356 in xmalloc /home/avar/g/git/wrapper.c:62:9
	    #3 0x5d7609 in prep_parse_options /home/avar/g/git/diff.c:5647:2
	    #4 0x5d415a in repo_diff_setup /home/avar/g/git/diff.c:4621:2
	    #5 0x6dffbb in repo_init_revisions /home/avar/g/git/revision.c:1853:2
	    #6 0x4f599d in cmd_pack_objects /home/avar/g/git/builtin/pack-objects.c:3980:2
	    #7 0x4592ca in run_builtin /home/avar/g/git/git.c:465:11
	    #8 0x457d81 in handle_builtin /home/avar/g/git/git.c:718:3
	    #9 0x458ca5 in run_argv /home/avar/g/git/git.c:785:4
	    #10 0x457b40 in cmd_main /home/avar/g/git/git.c:916:19
	    #11 0x562259 in main /home/avar/g/git/common-main.c:56:11
	    #12 0x7fce792ac7ec in __libc_start_main csu/../csu/libc-start.c:332:16
	    #13 0x4300f9 in _start (/home/avar/g/git/git+0x4300f9)

	SUMMARY: LeakSanitizer: 7120 byte(s) leaked in 1 allocation(s).
	Aborted

Narrowly fixing that commit would have been easy, just add call
repo_init_revisions() right before get_object_list(), which is
effectively what was done before that commit.

But an unstated constraint when setting it up early is that it was
needed for the subsequent [2] (pack-objects: parse --filter directly
into revs.filter, 2022-03-22), i.e. we might have a --filter
command-line option, and need to either have the "struct rev_info"
setup when we encounter that option, or later.

Let's just change the control flow so that we'll instead set up the
"struct rev_info" only when we need it. Doing so leads to a bit more
verbosity, but it's a lot clearer what we're doing and why.

An earlier version of this commit[3] went behind
opt_parse_list_objects_filter()'s back by faking up a "struct option"
before calling it. Let's avoid that and instead create a blessed API
for this pattern.

We could furthermore combine the two get_object_list() invocations
here by having repo_init_revisions() invoked on &pfd.revs, but I think
clearly separating the two makes the flow clearer. Likewise
redundantly but explicitly (i.e. redundant v.s. a "{ 0 }") "0" to
"have_revs" early in cmd_pack_objects().

While we're at it add parentheses around the arguments to the OPT_*
macros in in list-objects-filter-options.h, as we need to change those
lines anyway. It doesn't matter in this case, but is good general
practice.

1. https://lore.kernel.org/git/619b757d98465dbc4995bdc11a5282fbfcbd3daa.1647970119.git.gitgitgadget@gmail.com
2. https://lore.kernel.org/git/97de926904988b89b5663bd4c59c011a1723a8f5.1647970119.git.gitgitgadget@gmail.com
3. https://lore.kernel.org/git/patch-1.1-193534b0f07-20220325T121715Z-avarab@gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[c8ef62c1fb...](https://github.com/timothymtorres/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Thursday 2022-03-31 00:56:52 by LemonInTheDark

Fixes bartender drink throwing, makes smashing always spill (#65698)

Tohg's initial pr (9c0b0e5d4cc236e365ef0229400cefe98b184964) was rather poorly argued and a bit misleading, but the actual changes were honestly kinda harmless. You could already have thrown beakers to splash shit on someone, it wasn't a big issue.

However it did end up breaking bartending, because it removed the ranged
args that normally get passed into smash and SplashReagent.

I went in intending to fix that, but noticed some dumb copypasta in
broken bottle code, and decided to just start from there.

I've moved that logic to a proc on the broken bottle, and made smashing
a bottle on something splash its contents too.

I can't think of a case where you wouldn't want this, so I'ma just go
for it. Prevents future mistakes like this too.

Oh and because I'm passing ranged in properly now, splashing will not
always splash the whole amount of the bottle's reagents. Doubt that
really matters tho.

Love ya bestie

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[55336d1e53...](https://github.com/carshalash/tgstation/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Thursday 2022-03-31 01:03:19 by vincentiusvin

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
## [chflood/julia](https://github.com/chflood/julia)@[62e0729dbc...](https://github.com/chflood/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Thursday 2022-03-31 01:09:10 by Mirek Kratochvil

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
## [Aconka/babot](https://github.com/Aconka/babot)@[dcaa0402de...](https://github.com/Aconka/babot/commit/dcaa0402de43b1c3bd0eb0eef9896fffe9982c5d)
#### Thursday 2022-03-31 01:25:36 by Hank Hershberger

Create LICENCE

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

---
## [karmaisblackandbluepilled/Merchant-Station-13](https://github.com/karmaisblackandbluepilled/Merchant-Station-13)@[e327ecf707...](https://github.com/karmaisblackandbluepilled/Merchant-Station-13/commit/e327ecf7074403b15cbbc50294b928ecadfb7da1)
#### Thursday 2022-03-31 02:09:48 by karmaisblackandbluepilled

Revert "Removes the space jam ambience from the AI sat core area (#59509)"

This reverts commit 58697236a6fc4c52619031ba1eac75be7fe3aaac.

FUCK YOU FUCK YOU

---
## [Stevanus-Christian/terminal](https://github.com/Stevanus-Christian/terminal)@[855e1360c0...](https://github.com/Stevanus-Christian/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Thursday 2022-03-31 02:27:38 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row. 

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight. 

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[8607ba8b7d...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/8607ba8b7d98c52e81f23816a9224adf70559c25)
#### Thursday 2022-03-31 02:40:21 by SkyratBot

[MIRROR] Adds a very rare sussy firelock [MDB IGNORE] (#12401)

* Adds a very rare sussy firelock (#65677)

On a VERY low chance (1/25000) a normal full tile firelock can instead be generated with a more suspicious appearance based on this recent quality shitpost.

Sussy firelocks are completely identical when open (save the desc) and thus are apt not to be noticed except during exciting times. It's a fully cosmetic joke that got me to log into github, and that's an accomplishment in itself. Probability rate fully negotiable, I've added a one in a million chance before after all.

* Adds a very rare sussy firelock

* ruins all the fun

people can get banned for doing the funny sus amogus so encouraging it in code, whilst it's beautiful and funny, eh someone is going to throw a fit.

Co-authored-by: Incoming5643 <incomingnumbers@gmail.com>
Co-authored-by: KathrinBailey <53862927+KathrinBailey@users.noreply.github.com>

---
## [zinc-collective/convene](https://github.com/zinc-collective/convene)@[add90291f1...](https://github.com/zinc-collective/convene/commit/add90291f1e5462c6e27db0bb624bd148e470c93)
#### Thursday 2022-03-31 02:42:32 by Zee

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
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[e58fb506ef...](https://github.com/timothymtorres/tgstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Thursday 2022-03-31 03:04:46 by LemonInTheDark

Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

---
## [NoiceBroice/Sound-Space-Quantum-Editor](https://github.com/NoiceBroice/Sound-Space-Quantum-Editor)@[c39566ef07...](https://github.com/NoiceBroice/Sound-Space-Quantum-Editor/commit/c39566ef071c1b26f155c3d21edbe7461d71ee95)
#### Thursday 2022-03-31 03:06:18 by NoiceBroice

Create 'Test From Here' Button

I hate you guys
pretty sure this sucks
use some for loops or something damn

---
## [kkartaltepe/obs-studio](https://github.com/kkartaltepe/obs-studio)@[593cf0d642...](https://github.com/kkartaltepe/obs-studio/commit/593cf0d642ec7f8bc2a3d98e189a42d0f4c473d4)
#### Thursday 2022-03-31 03:49:20 by Kurt Kartaltepe

obs-ffmpeg: god awful hw_frame hacks

OBS should record if you use nv12 frames in obs' renderer and your hw encoder
does not require any other frame format or device selection.

---
## [CHOMPStation2/CHOMPStation2](https://github.com/CHOMPStation2/CHOMPStation2)@[e502b637e9...](https://github.com/CHOMPStation2/CHOMPStation2/commit/e502b637e9893a197cfa641cc5f03ede77a2860d)
#### Thursday 2022-03-31 04:03:32 by Rykka

Trait Addition + Adjustments

Polaris Combat is ass.
Yes, bandaid trait fixes are not necessarily the solution, BUT!

All of our negatives have extreme versions, without any sort of positive counterpart, and the positives we DO have are weak.
However, a flat 50% reduction on both incoming burn/brute would be too much, therefore:

Trait changes as follows.
- Added Glass Endurance. You have 25 HP, or 50 total HP, before you die. Don't get hit, and with Baymissn't? You're a masochist.
- Brute/Burn Resists no longer exclude High/Very High Endurance.
- Major Burn/Brute Resist re-added: These provide a 40% DR (Damage Reduction), at the cost of 3 points. This is opposite to Major Weakness, which is a 50% incoming damage increase.
- Very High Endurance re-added: This increases your max HP to 150.
- Increased Pain Tolerance: Similar to Increased Pain INtolerance, you have a 40% DR on incoming pain, compared to, for Intolerance, a 50% increase on incoming pain.
- Lick Wounds added back as a 1-cost Positive trait. I wondered why I hadn't seen it - it'd been disabled for _two years_ since Jan 2020.

Now, this is very likely to be controversial as it's a VERY huge balance change. Please don't bite my head off - this came up in discussion with Serdykov in DMs, and after digging through PRs, I discovered that traits had been disabled/removed for 1-2 years.

Pending a rewrite of Polariscode combat, and/or significant tweaks to make it more palatable, this will allow for more tankiness in combat - at the cost of extreme downsides. You can't suddenly become a hulk in combat with just traits, you still have to take some heavy downsides.

For instance:
Base Points - 1
Total Traits - 8

Very High Endurance - 4
Major Burn Resist - 3
Major Brute Resist - 3
Increased Pain Tolerance - 3

Current Points -12
Current Traits Left - 4

Conductive Major - -3
Extreme Photosensitivity - -2
Haemophilia - -3
Major Loneliness - -5

Current Traits Left - 0
Current Points 1

I'd be interested in looking at making Major Brute/Burn resist 4 points to equal 40% incoming DR, but that feels odd, given the negative is 50% incoming damage total for only 3.
I'd also be open to considering making VH Endurance even more expensive to 6, since it can be taken simultaneously now, and making base High Endurance cost 4.

---
## [chaldeaprjkt/kernel_xiaomi_vayu](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu)@[3551466553...](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu/commit/3551466553ecc6f030fbfb66ce33029b1ef205e4)
#### Thursday 2022-03-31 04:31:30 by Peter Zijlstra

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
## [DavidAjest/DavidAjest.github.io](https://github.com/DavidAjest/DavidAjest.github.io)@[862e32c686...](https://github.com/DavidAjest/DavidAjest.github.io/commit/862e32c6867f4c59bfa22075b84821d71eeb7208)
#### Thursday 2022-03-31 05:20:27 by DavidAjest

added fixing to a paragrpath line 46

<p>
    Hello and welcome to my section on my web page - <span style="color:white;font-weight:bold">yes, </span> this all page is all about me.<br>
    Here im gonna talk about my self(im cute right?). you will get the <span style="color:white;font-weight:bold">Most Importent</span> things about my life.<br>
    i don't know why really and what you will do with this information. but i guess here we go..
</p>
    <p> 
  My name is Cooper, confusing right? - i'm a girl.
  i was born 2 years ago in a place called  <a id="klavimBakfar" href="https://klavimbakfar.com/"> "כלבים בכפר" </a>.   
  i was born in really weird times, Alot of you <span style="color:white;font-weight:bold">- Humans, </span> bought alot of toilet paper with dogs Printed on the toilet paper, as i said - wierd, and <span style="color:white;font-weight:bold">why</span> really thoght?
</p> 
    <p>

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[796f7de414...](https://github.com/Koi-3088/ForkBot.NET/commit/796f7de41488891b6d69b5ccbf913e8238b9b79b)
#### Thursday 2022-03-31 05:37:52 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[531a2a8029...](https://github.com/treckstar/yolo-octo-hipster/commit/531a2a80291df34081519bf1db8ae26df19dd285)
#### Thursday 2022-03-31 05:45:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[54403a1ca0...](https://github.com/tgstation/tgstation/commit/54403a1ca0a1d83302430bbb54a0d6bc561f0098)
#### Thursday 2022-03-31 07:52:09 by FinancialGoose

Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

---
## [mcx/gimp](https://github.com/mcx/gimp)@[7123b6c466...](https://github.com/mcx/gimp/commit/7123b6c466dcf38bb274734e9d7494c9c4fd8b8e)
#### Thursday 2022-03-31 09:15:13 by Jehan

Issue #7685: g-ir-doc-tool produces broken XML.

To work around the issue, I just wrote a stupid sed script. Of course,
it means that if we encounter again the issue on some other docs, we'll
have to update it. In other words, it's neither robust nor a proper
long-term fix. Just a temporary hack.
See: https://gitlab.gnome.org/GNOME/gobject-introspection/-/issues/425

Also fixing this issue, I encountered another bug, this time in meson,
which changes backslashes in slashes on 'command' arguments, in a
completely uninvited manner! The only workaround to this is apparently
to call an external script, which is ridiculous for such a basic stuff.
But well… here is why I implement this with a script, instead of
directly calling sed in the meson 'command'.
See: https://github.com/mesonbuild/meson/issues/1564

---
## [kleinesfilmroellchen/serenity](https://github.com/kleinesfilmroellchen/serenity)@[2fa354a5d7...](https://github.com/kleinesfilmroellchen/serenity/commit/2fa354a5d7a3b2debf00cb07730dc480feda0c92)
#### Thursday 2022-03-31 10:44:39 by kleines Filmröllchen

LibAudio+Userland: Use new audio queue in client-server communication

Previously, we were sending Buffers to the server whenever we had new
audio data for it. This meant that for every audio enqueue action, we
needed to create a new shared memory anonymous buffer, send that
buffer's file descriptor over IPC (+recfd on the other side) and then
map the buffer into the audio server's memory to be able to play it.
This was fine for sending large chunks of audio data, like when playing
existing audio files. However, in the future we want to move to
real-time audio in some applications like Piano. This means that the
size of buffers that are sent need to be very small, as just the size of
a buffer itself is part of the audio latency. If we were to try
real-time audio with the existing system, we would run into problems
really quickly. Dealing with a continuous stream of new anonymous files
like the current audio system is rather expensive, as we need Kernel
help in multiple places. Additionally, every enqueue incurs an IPC call,
which are not optimized for >1000 calls/second (which would be needed
for real-time audio with buffer sizes of ~40 samples). So a fundamental
change in how we handle audio sending in userspace is necessary.

This commit moves the audio sending system onto a shared single producer
circular queue (SSPCQ) (introduced with one of the previous commits).
This queue is intended to live in shared memory and be accessed by
multiple processes at the same time. It was specifically written to
support the audio sending case, so e.g. it only supports a single
producer (the audio client). Now, audio sending follows these general
steps:
- The audio client connects to the audio server.
- The audio client creates a SSPCQ in shared memory.
- The audio client sends the SSPCQ's file descriptor to the audio server
  with the set_buffer() IPC call.
- The audio server receives the SSPCQ and maps it.
- The audio client signals start of playback with start_playback().
- At the same time:
  - The audio client writes its audio data into the shared-memory queue.
  - The audio server reads audio data from the shared-memory queue(s).
  Both sides have additional before-queue/after-queue buffers, depending
  on the exact application.
- Pausing playback is just an IPC call, nothing happens to the buffer
  except that the server stops reading from it until playback is
  resumed.
- Muting has nothing to do with whether audio data is read or not.
- When the connection closes, the queues are unmapped on both sides.

This should already improve audio playback performance in a bunch of
places.

Implementation & commit notes:
- Audio loaders don't create LegacyBuffers anymore. LegacyBuffer is kept
  for WavLoader, see previous commit message.
- Most intra-process audio data passing is done with FixedArray<Sample>
  or Vector<Sample>.
- Improvements to most audio-enqueuing applications. (If necessary I can
  try to extract some of the aplay improvements.)
- New APIs on LibAudio/ClientConnection which allows non-realtime
  applications to enqueue audio in big chunks like before.
- Removal of status APIs from the audio server connection for
  information that can be directly obtained from the shared queue.
- Split the pause playback API into two APIs with more intuitive names.

I know this is a large commit, and you can kinda tell from the commit
message. It's basically impossible to break this up without hacks, so
please forgive me. These are some of the best changes to the audio
subsystem and I hope that that makes up for this :yaktangle: commit.

:yakring:

---
## [tin-z/Infosec_Reference](https://github.com/tin-z/Infosec_Reference)@[cef2bd6f6c...](https://github.com/tin-z/Infosec_Reference/commit/cef2bd6f6c2cbf3476f4b212b7c3c94adefc138e)
#### Thursday 2022-03-31 11:22:49 by rmusser01

If you're reading this, I hope you're having at least a decent 3rd weekend of December. Hopefully next year won't be such a trashfire. #miracles ; Thanks to all the people who have helped make this year be not a _complete_ clusterfuck; small update. more backlog clearing. Next will hopefully be exec/evasion cleanup, then the redteam page and adding actual 'team' content to it. Shoutout agin to S for the much appreciated criticism. Here's to hoping for no new pandemics/genocides/wars/complete collapse of society for at least the next year. #smallmiracles

---
## [expo/expo](https://github.com/expo/expo)@[d92760eeb2...](https://github.com/expo/expo/commit/d92760eeb25ebd325b0b06a3c3f49bbfe348d4d0)
#### Thursday 2022-03-31 11:28:11 by Łukasz Kosmaty

[dev-launcher][iOS] Improve handling of LAN permission crash (#16792)

# Why

Closes ENG-4203.

# How

Try to retry if the network connection was rejected due to the lack of lan permission.
My code will only retry once per app process - in my opinion, we shouldn't save that information in the shared preferences. Retrying one network call isn't that painful even if the failure wasn't connected with the lan permission. That solution was the best, in my opinion, when I was playing with different versions. 

Also, sometimes when the network call was rejected due to the lack of lan permission, retrying it doesn't help, cause the prompt didn't appear in time, but we can't detect that. However, in that case, the app won't longer crash and also the user will be delegated to the error screen. After all, it seems like pretty good UX. 

# Test Plan

- run bare-expo locally ✅

---
## [newstools/2022-metro](https://github.com/newstools/2022-metro)@[815eb203a6...](https://github.com/newstools/2022-metro/commit/815eb203a65395cd51d72f7c795f931ddc666397)
#### Thursday 2022-03-31 14:58:06 by Billy Einkamerer

Created Text For URL [metro.co.uk/2022/03/31/morbius-review-jared-letos-blood-sucking-bust-is-drained-of-life-16377511/]

---
## [sunkinship/Amalgamate](https://github.com/sunkinship/Amalgamate)@[90358f4bf1...](https://github.com/sunkinship/Amalgamate/commit/90358f4bf12d5e0412cff65c25793689f2242289)
#### Thursday 2022-03-31 16:12:52 by MUKILTEO\1710194

You know what, I'm done, done, done
Yeah, I'm gonna take my horse
To the old town road
I'm gonna ride 'til I can't no more
I'm gonna take my horse to the old town road
I'm gonna ride (Kio, Kio) 'til I can't no more
I got the horses in the back
Horse tack is attached
Hat is matte black
Got the boots that's black to match
Riding on a horse, ha
You can whip your Porsche
I been in the valley
You ain't been up off the porch, now
Can't nobody tell me nothing
You can't tell me nothing
Can't nobody tell me nothing
You can't tell me nothing
Riding on a tractor
Lean all in my bladder
Cheated on my baby
You can go and ask her
My life is a movie
Bull riding and boobies
Cowboy hat from Gucci
Wrangler on my booty
Can't nobody tell me nothing
You can't tell me nothing
Can't nobody tell me nothing
You can't tell me nothing
Yeah, I'm gonna take my horse
To the old town road
I'm gonna ride 'til I can't no more
I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more
I got the

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[03d48778d3...](https://github.com/newstools/2022-new-york-post/commit/03d48778d3f4e6dfebc7df842826c43d8f520335)
#### Thursday 2022-03-31 18:53:53 by Billy Einkamerer

Created Text For URL [nypost.com/2022/03/31/fallen-hillsong-church-boss-deeply-sorry-for-boozing-fathers-evil/]

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[65329f4fac...](https://github.com/pytorch/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Thursday 2022-03-31 19:40:54 by Edward Z. Yang

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[50689f89a4...](https://github.com/tgstation/tgstation/commit/50689f89a40e5e7a2732a0c5fb38c787b69f7d28)
#### Thursday 2022-03-31 20:40:27 by LemonInTheDark

Action button refactor/rework: Enhanced Dragging (#65180)

About The Pull Request

I noticed a lot of strange and un-intuitive behavior in action buttons, and got stung by the bloat bug. Damn it hug #58027
I'll do my best to explain what I've changed and why, might get a bit long.
If you want a better idea, read the commits. Most of em are pretty solid, if long.

Whelp. Here we go.
How do action buttons currently work

All action buttons are draggable, to any place on the screen. They're held in an actions list on the player's mob.
Their location in this list determines their position on the top of the screen. If one is dragged away from the top, its position in the list is "saved". This looks really bad.
If two buttons are dragged over each other, their positions swap. (inside the actions list too)
If a button is shift clicked, it is brought back to the position it started at.
If the action collapse button that you likely just mentally edit out is alt clicked, it resets the position of all action buttons on the screen.
If an action is ctrl clicked, it is "locked". This prevents any future position changes, and also enables a saving feature. With this saving feature, locked button positions persist between rounds. So your first o2 canister will always start where you saved it, etc.
Actions and buttons are a one to one link. While there is functionality to share action buttons between two players, this means showing the same object to both. So one player can move a button on another's screen. Horrendous.
This also makes code that modifies properties of the screen object itself very clunky.
Why is this bad

A: None knew pretty much any of this information. It is actually documented, just in a horribly formatted screen tip on the collapse button, you know the one we all mentally delete from the hud.
B: None of this is intuitive. Dragging buttons makes the hud look much worse, and you get no feedback that you even can drag them. Depressing
C: We use actions to make new options clear to the player. This means players can have a lot of action buttons on the hud. This gets cluttery
D: The collapse button is useless. It lets you clear your screen if someone like me fucks up and gives you 2000 actions, but outside of that it just hides all information from you. You never want to see none of your action buttons, just a filtered list of them.
E: On a technical level, they're quite messy, and not fully functionally complete. This is depressing.
What I've done

Assuming the above to be true, how do we fix them?
Well first I'm going to go over everything I changed, including links to major commits. I'll then describe the finished product, and why I made the decisions I did.

Oh and I've moved some of the more niche or technical discussion to dropdowns. Hopefully this makes finding the major functional changes easier

Adds helper procs for turning screen_loc strings into more manageable arrays. This doesn't fully support all of the screen_loc spec, but it's enough for what I'm doing. (f54865f)

Uses these helper procs to improve existing code (6273b93)

Fixes an issue with tooltip code itself. If you tried to hold down a mouse button while dragging onto a tooltip enabled object, it would silently fail. The js made assumptions about the order args came in, which broke when buttons were held down (e0e42f6)

Adds a signal linked to /client/Click(). Surprised we didn't have this before honestly (c491a4a)

Makes /client/MouseDrag() return parent. If we don't do this, any overrides of MouseDrag will never actually be called (2190b2a)
Refactors how action buttons work under the hood (53ccce2)
Basically, rather then generating one button per action, we generate one button per viewer

Starts to change button behavior, more cleanup

Changes the mouse cursor when an action button is dragged. Hopefully
this makes moving things feel less like an accident, and makes you doing
it more clear

Removes the moved and locked vars. This will be more relevant later, but
for now:

Moved exists as a sort of budget "We've been dragged" variable. We can
handle this more cleanly, and the movable type doesn't care about it

Locked is a very old variable that is also not something that the
movable type "owns". It's more an action button thing that's been moved
down.
It exists so an action can be locked in place, and in that locking, be
treated as a "saved location"
(21e20fc)

Because I've nuked move, we don't need to directly set our button's
position. We can use the default_button_position var instead. This is
quite handy.

Please ignore position_action, I will explain that later
(83e265e)

Removes the buttons locked pref

It was another obscure part of action buttons, basically do buttons
start "locked" or not. See previous discussion of locked
(b58b1bd)

Major rework starts here

Alright. Sorry for this, this is where me not commiting regularly starts
to suck. I'll do my best though.

Rather then figuring out an action button's position via a combination
of the moved and ordered vars, we use a separate location var to store
one of a few defines. This makes life later much easier.

Adds tooltip support for dragging action buttons. The way the tooltip
just froze in place when dragging really bugged me, and lead to some
nasty visual artifacts.
This is a bit messy because the drag procs are horrible, but it's
workable

Dropping a button on another button will no longer swap their positions
Behavior instead depends on the target button.

If it's a part of a group (A concept I will explain later) the dragged
button is simply inserted before it in the group's list.

If it's floating on the general hud, we instead position the dragged
button to its right. There's extra logic here to ensure buttons will
never overflow the screen, but I'll get into that later.

Alright. That's most of the refactoring. Time for the larger behavior
changes.

Adds a button palette. This is a separate dropdown that renders
underneath buttons.

image

The idea is to allow for a conceptual separation between "important"
buttons and the ones that end up cluttering the screen.

You can click on the dropdown to open it, then any later clicks that
don't involve actions in some way will autoclose it.

My goal is to come up with an alternative for the action button that
just acted as a way to hide all buttons on screen. Not convinced it saw
much use.

As a side effect of removing that, I've moved its tooltip stuff to the
palette. I've properly formatted it, so hopefully it's easier to read
then the jumble that we used to have.

(You can alt click the palette button to reset all button positions)

Oh and the palette can scroll, since as you'll see later it has a
limited size.
image

Moving on from that, I've added what amounts to action landing buttons.
These allow buttons to rejoin groups, or be positioned at the end of a
line of buttons.
image

They've got a 32x32 hitbox, and only show up when dragging. Hopefully
this makes the system more clear just by dragging an action.

Oh and I've changed how button position updating works. The old system
of calling update_action_buttons on mob every time an action button
changes position is gone, mostly because I've setup more robust
grouping. Will discuss when I get to huds

(0d1e93f)
Adds the backbone behind action button position changes (94133bd)

Moves hud defines to the global folder, safer this way (7260117)

Adds color changing to the palette button, giving some heads up for buttons being inserted into the palette automatically
image
image
Ensures a landing button is always shown, even if it needs to break the
max row rule
Makes palettes auto contract if they have no buttons inside them
Prevents palettes from being opened if they have no buttons inside them
(f9417f3)
How it looks
2022-02-26.02-30-10.mp4
Why It's Good For The Game

Players have more control over the clutter on their screen.
Buttons are available, but not in the way,
Since any player move of a button saves it, any lack of clarity in the way buttons work will be forced out by buttons not just resetting when a new game starts.
We don't overlap any existing screen elements, unless the upper button list gets really long.
The code is much less crummy (I think, may have made it worse it's hard for me to judge my own work)

If it ends up not being as usable as I'd like, I'll rip out the existing changes and just implement the qol and backend stuff. I think it's worth doing though.
Changelog

cl
add: Expanded heavily on action buttons
add: Adds an action button dropdown that sits just under the normal list in the top left. You can drag new buttons onto it to insert them. Click on it to show its contents, do what you want to do, then click again anywhere to contract it. Alt click it to reset all button positions
add: Action buttons will now remember their position between rounds. So if you really like your flashlight right next to your player for some reason, we support that now
add: When you start to drag an action button, docking ports will appear in places that it can be inserted into. (Outside of just floating somewhere on your screen of course)
del: Removed action button locking, and the associated preference. I'm reasonably sure literally none uses this, but if you do hit me up
qol: Dragging an action button will now give you an outline of its size around your cursor
fix: You can no longer cause the screen to expand by putting an action button on the edge of widescreen, and then resizing to standard.
refactor: Refactors action and button code significantly. lots of little things.
/cl

---
## [allusion-app/Allusion](https://github.com/allusion-app/Allusion)@[aa538a9d5a...](https://github.com/allusion-app/Allusion/commit/aa538a9d5a8d873dadcc7dfef0453046fc0c4f12)
#### Thursday 2022-03-31 21:36:16 by hummingly

One context menu to rule them all
* Back when we still used BlueprintJS, React portals were slow or
BlueprintJS' implementation. We talk about seconds to open a context
menu.
* Furthermore, portals do not inherit styles since they are out of tree
:( BUT you can solve that with passing the top level class on creation
and always update that.
* Back then I was also on an explicit everything trip which is how the
useContextMenu hook was born. However, it has its merit if you do not
know what the perfect API looks like (which is kinda always the case).
* Now I don't hate portals anymore but I still deleted them lol
* The context menu will be now a sibling element which solves most
overlap issues.
* Well, except for tooltips but this is such a weird edge case. Who
wants to read tooltips after opening context menus?
* Either way the React Context API pretty much fixes all API issues
which stem from React fundamental designs (isolated components and
and tree like state flow == PITA for graph like state).

---
## [pytorch/nestedtensor](https://github.com/pytorch/nestedtensor)@[206d885274...](https://github.com/pytorch/nestedtensor/commit/206d885274dd4b1191b5a3c3b060b072c0ff5383)
#### Thursday 2022-03-31 21:47:11 by Brian Hirsh

Reland: "free up dispatch key space (in C++)" (#74963)

Summary:
X-link: https://github.com/pytorch/pytorch/pull/74963

This is a re-land of D35192346 and D35192317, which together are a diff that changes the internal representation of `DispatchKeySet` in pytorch core to free up the number of dispatch keys that we have available. See a more detailed description of the design in the original PR: https://github.com/pytorch/pytorch/pull/69633.

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

Reviewed By: phding, albanD

Differential Revision: D35222806

fbshipit-source-id: 0ad115a0f768bc8ea5d4c203b2990254c7092d30

---
## [QziP22/user.js](https://github.com/QziP22/user.js)@[f8932dced1...](https://github.com/QziP22/user.js/commit/f8932dced142ec5ea633bfb163bfc7579ac38a07)
#### Thursday 2022-03-31 21:55:29 by Thorin-Oakenpants

remove ambiguous line

The point was that google have said (stated in policy, but fuck knows where that is located these days) that it is anonymized and not used for tracking. It's an API used by **_4 billion devices_** - the API has privacy policies for use. If a whistleblower or someone else found out that google was using this to enhance their user profiling, then all hell would break loose. And they don't even need this to fuel their ad revenue. It is provided, gratis, to the web to help ensure security - they wouldn't dare taint it and get it caught up in a privacy scandal involving **+4 billion devices_**. And in all this time (since 2007), there has been no such whistleblower or proof it is used to track or announcements by google of changes to the contrary.

Anyway, a quick search brings up
- Here is their policy - https://www.google.com/intl/en_us/privacy/browsing.html - it's empty and points to
- https://www.google.com/intl/en/chrome/privacy/
   - and if you scroll down to "Safe Browsing practices" it doesn't say anything about privacy policies for the API itself (or the owner of the API) - it just spells out what happens in chrome
- I'm not going to bother to look any further and find a history of policy changes

Anyway, this is Firefox and hashes are part hashes bundled with other real hashes - and we turned off real time binary checks. So this line can fuck the fuck off. It was meant to reassure those who want the security of real-time binary checks, that privacy "shouldn't" be an issue, but I'm not going to expand on it

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[acf03c9cbf...](https://github.com/mrakgr/The-Spiral-Language/commit/acf03c9cbf03b4b73b97cb1813d8cfca315e7a62)
#### Thursday 2022-03-31 22:31:44 by Marko Grdinić

"1:05pm. This is the latest I've woken up in a very long time. Not what I intended. I was hoping to start getting up earlier!

1:45pm. The weather is warmer so I won't have to do chores today. Let me finish breakfast and I will resume my texturing adventure. I need to go over all the UVs and make sure the maps are correct.

2pm. How about I start?

2:40pm. How do I test for UV distortion in Blender?

https://youtu.be/bHbgQs8zkpw?t=232
How to Flatten UV Islands (Blender Tutorial)

Oh, so this is what follow active quad does.

3:20pm. https://www.makeuseof.com/blender-uv-mapping-tips/

///

You can see whether or not your UV map is stretching by clicking into your UV panel overlays menu. Toggle Display Stretch for an uncensored glimpse into where you've gone wrong.

///

Now I've started sufing the ML sub. Forget that, focus on the task at hand. How do I display stretch? Where are the overlays? I remember this from 4/5 months ago, but I can't figure out where it is now.

Ah, I figured it out. It is the icon just to the left of UV Map.

3:45pm. The most complex pieces in the desk are the metal pieces that I to slide the middle board. Damn the seams for it were tough.

Interestingly, the angle based method gives somewhat awkward results for regular tubes for some reason. For both the metal piece and the tube at the bottom, the conformal method was better.

3:55pm. Damn, the metal piece had a bit of overlap.

4:10pm. Damn, did I spend a lot of time on this metal piece. I think I learned a decent amount about UV unwrapping in the last two hours.

But I think I would have been better served by just using auto UV unwrap and going on my way.

UVs aren't a big deal...

4:15pm. I tried applying the bevels and after I do that, all the UV works that I did goes up in smoke.

Crap.

4:25pm. When I put in 6 bevel segments it starts working. After that I get some overlap, but nothing that is visible with the naked eye.

4:30pm. No the overlaps as they are is because for some reason Blender did not merge the vertices for the bevels. If it did that I'd get a perfect result. But why isn't it working?

https://youtu.be/wuCTBwoGDBk
Stitch UV Islands! in Blender

Let me watch this.

4:45pm. Shit, I accidentally overwrote with the bevel applied and lost the work on the unbeveled thing.

The problem I am having is that even if I wanted to do the seams by hand, the edges are so small that it is hard to click on them. It is ridiculous.

I do not understand why the seams end up messed up once the bevels get applied. They worked fine for the cubes so why do the problems manifest here?

4:50pm. Correction, they don't work for the cubes at all! How is this possible?

Also I do get overlaps even with smart project. The reason for that is the duplicate vertices from bevel.

Ok, enough of this.

Let me apply all the modifiers.

4:55pm. Let me take a break.

5:15pm. Just a bit more and I will resume. I feel like watching videos. I just got my ass kicked so hard.

I spent all this time putting seams on the low poly models only to realize that bevels wreck all of that. This completely wrecked the workflow I've been developing. In the end, what am I suppose to do, just use UV unwrapping. I am going to watch some videos.

Forget getting to the texturing today.

5:45pm. Let me resume.

https://youtu.be/HDURGTLNu2Q
UV Unwrapping Masterclass in Blender | Hard Surface Workflow

I am going to watch the UV part of this just so I can get some ideas.

Honestly, the UVs do not matter. Unlike all the other aspects of art, at worst auto UVing will result in performance hit, but that is about it. They are the kind of issue that can be surmounted using bigger GPUs. It is not worth my time to mess with them by hand. Today was one thing since I wanted some exp in them, but I will not make doing the by hand my policy.

Let me just check out how the pro does it. I want to know what the right way to do them for a complex object would be. Clicking and placing seams by hand is incredibly awkward.

Maybe there is a tool that would allow me to move across the edges by hand.

https://youtu.be/HDURGTLNu2Q?t=117

Oh, it is possible to turn off extras like this.

Let me have lunch here.

6:05pm. Let me resume.

I am hearing him talk about unwrapping a high poly mesh, and it finally dawned on me - I should be unwrapping a low poly mesh and then baking it.

...No, consider those tire threads. Just projecting it to the low poly space would result in a loss of detail.

Forget it. Let me just clear my mind and hear what he has to say.

https://youtu.be/HDURGTLNu2Q?t=532

I have to remember this kind of use for checker selection. I guess I'll watch this whole video rather than just the UV unwrapping parts.

https://youtu.be/HDURGTLNu2Q?t=1176

This is worth keeping in mind. Changing the alpha value of the face orientation would make it suitable for just picking up errors.

https://youtu.be/HDURGTLNu2Q?t=2143

What he could do here is select just the edges and then do the checker deselect.

7:20pm. https://youtu.be/HDURGTLNu2Q?t=3591

That was pretty boring, glad that its over. Now he will finally be doing the unwrapping. I want to see how he will approach such a complex object. Mine isn't evne 1/10th of this in complexity and I am already floundering.

https://youtu.be/HDURGTLNu2Q?t=3694

Why not use the procedural checker texture?

https://youtu.be/HDURGTLNu2Q?t=3740

Live unwrap is something I've missed. Houdini does that, but it slipped my mind to look at it.

https://youtu.be/HDURGTLNu2Q?t=3758

Hmmm, starting with sharp edges is not a bad idea.

https://youtu.be/HDURGTLNu2Q?t=3780
> Make sure it is set to conformal. Angle based will not work very well on hard surface meshes.

This is what I figured. The tooltip says that angle based is slower, but often gives better results.

https://youtu.be/HDURGTLNu2Q?t=3781

This kind of workflow where he is looking at the checker textures directly on the mesh is good. I should have gone with that. Instead I would look at the UV window instead.

https://youtu.be/HDURGTLNu2Q?t=4066

Interesting that he did not completely get rid of the bevel mods.

https://youtu.be/HDURGTLNu2Q?t=4581

The way he goes through this is pretty inspiring. Now I want to give it a try myself. But let me finish at least watching this section.

https://youtu.be/HDURGTLNu2Q?t=5133

By unwrapping everything like this, isn't he forcing either angular or conformal. He did the tires using angular. Now that is gone.

Rather than unwrapping them using the angular method, he should have just packed the islands. That would have kept the method.

https://youtu.be/HDURGTLNu2Q?t=5398

What he is doing here for the object is a good idea. A significant part of desk does not need careful damage. But the stuff in front needs to be higher res. Rather than having everything be split into its own set, I should have something like two to save space.

https://youtu.be/HDURGTLNu2Q?t=5494
> UV Pack Master is better.

He also addresses the issue between using different unwraps.

The way he did things so far is such a pro. Blows my ad hoc methods out of the water.

Youtube is the greatest thread to modern schooling, and I hope it wins. Why go to school when you can just watch videos like this one.

https://youtu.be/HDURGTLNu2Q?t=5568

This is a pretty good result!

https://youtu.be/HDURGTLNu2Q?t=5711

It is a shame to lower the resolution like tihs.

https://youtu.be/HDURGTLNu2Q?t=5969

I am a bit confused why a bevel would fix this, but nevermind it for now.

https://youtu.be/HDURGTLNu2Q?t=6464

Since it has 7m left, I'll watch this, but this baking stuff is not something I'll ever have to do.

8:50pm. Damn it. The select sharp edges thing is not working for me.

10:05pm. Holy crap this metal piece is so difficult. It is insane. I should not have applied the bevel to it. And if I did, I should have used more straightforward topology.

10:30pm. Damn it, how do I figure out which overlapping UVs are in the viewport. I do not know what I am selecting

10:40pm. I do not get it. This part should absolutely have no overlaps and yet it does.

11pm. https://blender.stackexchange.com/questions/3254/selecting-faces-on-object-from-uv-editor-window

There is an option to sync the selections between the two editors!

This makes it so much easier to locate the overlaps.

Now if I could only unmess the camera. I am trying to zoom in on a small area and it does not show it properly.

https://blenderartists.org/t/cant-zoom-in-on-small-object/516374
> You’re probably zooming in perspective view mode. Switch to ortographic with numpad 5 and you’ll be able to zoom a lot

Oh, it is true. This helps a lot. Now I see that the reason why the area is giving me so much trouble is because there is some mesh shearing there. The bevel did a shit job.

11:10am. Now that I've synced the selections between UV and main view, when I select overlaps I immediatelly see what the problem is in the main view.

I am a fool to not do this right away.

11:55pm. I just noticed that the UV editor has sculpting brushes now. Did Blender have that before? I don't think so.

Right now I am done dealing with the UVs for that metal piece that has been giving me so much trouble. The tip to zoom in orthogonal mode was very helpful. So was turning on UV Sync Selection. I have no idea why that mesh area had errors, maybe I pressed F by accident or maybe the modifier did mess up. It does not matter.

Right now there are still some overlaps, but I think that is more a problem with algorithm being too sensitive rather than there being actual overlaps. I'll ignore it.

https://youtu.be/mRF83HLkfiM
Cool bevel trick you should probably know in Blender!

Let me watch this since I had the tab open. At this point I should be a master of UV unwrapping in Blender. Nothing is going to get in my way anymore.

https://youtu.be/VdlcAD6FRpo
[Solved] Bevel Not Working? Fix it with 3 Easy Tips | Fast & Correct Method | Blender Eevee & Cycles

Let me also watch this.

https://youtu.be/VdlcAD6FRpo?t=242

Hmmm, I had no idea that bevels are sensitive to normals.

12:15am. https://youtu.be/6npPzqkzbKI
The simple tip that will make or break your designs (Blender)

Let me watch this as well.

12:30am. https://youtu.be/C7plHMKIFcU
You're Wrong About NFTs

This guy is so good, I don't even have any idea what NFTs are, but I want to watch this. Let me get dinner here.

Actually, let me close here. Now that I finally have UV unwrapping of the desk done for good, the next step is to actually testure it. I can finally concern myself with just that. Though these issues are annoying, I really like how I am doing hands on work as opposed to moving nodes around in Houdini. It is good to be back in Blender I suppose."

---
## [cmm1107/Simple-YouTube-Age-Restriction-Bypass](https://github.com/cmm1107/Simple-YouTube-Age-Restriction-Bypass)@[0b9ce74230...](https://github.com/cmm1107/Simple-YouTube-Age-Restriction-Bypass/commit/0b9ce7423094b9905337fc9cc9991dc506c1008d)
#### Thursday 2022-03-31 23:30:33 by Demirci K

[chore] remove eslint & husky (#96)

* [chore] remove eslint & husky

Currently both are a pain in the ass and hard to work with in terms of developer experience, they are more like a nuisance than a helper.

ESlint is hard to work with when unconfigured. We might add this back in later when we have enough time to write the config rules.

Husky is reasonable, but with Prettier it tends to change files which are not in the commit. Although this is solvable with `lint-staged`, the fact that your code looks different on the commit vs what you just wrote is annoying. Also the error/warning messages are a lap of text, with bunch of useless information and it also does not play nicely with a GUI based Git.

My proposal (#97) as an alternative is having CI testing on GitHub on each pull request, when it fails, the dev must manually run `npm run format`. At that point it is clear to the dev that transformation has happened to the original code and is able to review it.

* upgrade packages

---
## [Kazkin/sojourn-station](https://github.com/Kazkin/sojourn-station)@[89532158bd...](https://github.com/Kazkin/sojourn-station/commit/89532158bd86cf5da9485e37fe078168bae39cc4)
#### Thursday 2022-03-31 23:45:08 by Kazkin

Will of the Protector Revamp

-Added 20 license point disks to the church vendor that are copies of their utility disks for 400 credits.
-Replaced the limited license disk in the biogenerator room with its formerly infinite disk.
-A massive revamp to the Will of the Protector has been done. It now functions as a combination between a shrine and church merchant machine. It now sells only disks and medkits, allowing disciples to more readily obtain church disks beyond asking the prime.
-Offerings expanded, detailing what each offering requires and what it does. Offerings effect the WotP's global blessing, weighting which one happens when power hits 100.
-Offerings grant 5 armanent points per offering to give a reason to actually do them and what to do with excess biomass.
-Armanent points rebalanced to 100, all items bought balanced in this same scale.
-Removed annoying global message every time the WotP releases its power, instead limiting it to only when a power directly effects you while also explaning how.
-Remove the WotP ability to give materials, finished guns, the nt oddity, and other stuff as it was unbalanced.
-Gave it a slightly customized sprite, more of a place holder really but its an obelisk with a blue cruciform instead of gold.

---

