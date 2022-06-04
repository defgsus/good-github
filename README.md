## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-03](docs/good-messages/2022/2022-06-03.md)


1,736,230 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,736,230 were push events containing 2,669,109 commit messages that amount to 187,383,175 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [Very-Soft/VOREStation](https://github.com/Very-Soft/VOREStation)@[38724d4d4c...](https://github.com/Very-Soft/VOREStation/commit/38724d4d4c140fb4bfc92444ba3e5dd182ca7df9)
#### Friday 2022-06-03 00:14:07 by VerySoft

[WIP] pAI tweaks and upgrades

Changes some things around! 

Removes the 'wipe' button from pAI's interface, since I think there being an instant 'kill player' button is pretty lame, especially since most pAIs activate on their own without a master. They're easy enough to kill or contain without this, so I don't see it as necessary. If you want to kill your pAI friend just eat them. :U

Removes the 'pAI Suicide' verb, and renames the 'Wipe Personality' to 'Enter Storage' and moved it from the OOC tab to the pAI Commands tab. Killing a pAI deletes the card and all that, where the 'Enter Storage' verb deletes the card and spawns a new one that can be used, which! I think it more appropriate.

Makes it so that, when damaged, pAIs will slowly regenerate while folded up, at a rate of 0.5 brute and burn per life tick, where previously it had been impossible to recover health outside of admin intervention.

Updated the Universal Translator with many of the newer languages that aren't obviously for events or hivemind type things.

Added the same emotes that humans can use to pAIs

Added an alternative pAI card style, and rearranged the expressions for the cards a little bit, and added one more.

Plan to add more pAI chassis to play with

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[a3c0819e80...](https://github.com/Zonespace27/Skyrat-tg/commit/a3c0819e8091ab99a5ab8f53b59c4687e5b2f2cf)
#### Friday 2022-06-03 00:22:58 by SkyratBot

[MIRROR] Removes (in) smoke and foam reactions [MDB IGNORE] (#13963)

* Removes (in) smoke and foam reactions (#67270)

* Removes smoke and foam reactions

Turns out when you let reagents react in foam/smoke, people put bombs in
them.

This behavior was initially added to just smoke, accidentially in
(56f7ac0c0a29e8f898c4aab35947d027952b43f7) accidentialy (thalpy tried to
make both foam and smoke instant react, but instead made smoke's temporary
holder reagent instant instead. hhhhhhh)

Assuming this was intentional it was then extended to foam in
(1879e2d338c9bf5f191cef6c39944b26a41e6092)

Basically, we're idiots. Anyway lets just walk this all back to instant
reaction on smoke/foam formation. Hate you people

* Removes another source of gunpowder smoke

Temporal told me about this. Gunpowder uses an ex_act signal as a
starter, and that also counts for smoke objects.

Really don't want instant detonation smoke bombs, so let's just... not
shall we?

* Removes (in) smoke and foam reactions

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [dfinity/motoko](https://github.com/dfinity/motoko)@[e883348f8a...](https://github.com/dfinity/motoko/commit/e883348f8a35c0925d7363cc6b9488fdac261a29)
#### Friday 2022-06-03 00:53:37 by Gabor Greif

feat: introduce array-slice processing for compacting GC (#3231)

This PR introduces a modified marking (and visiting) technique for array fields, where `Array`s are GC-ed by considering their suffixes as slices, pushing these on the mark stack as bulk collections, and treating the fields in the prefix as individual objects being pushed onto the mark stack.

Following key changes are made:
- when visiting an `Array` in the dynamic heap we consult a new callback that can opt-out of the individual processing of some suffix of the array (by returning an index smaller than the array length)
- fields before this index will be processed as before by the first callback
- for the suffix the new callback is in charge to perform the bulk action
- in case of array marking, the new callback checks if the current slice is longer than some cutoff, and if so, it will push the array and the start of the suffix to the mark stack. (We abuse the tag entries as the start index for the suffix slice, so the cutoff must be numerically bigger than the biggest heap tag; this invariant is enforced)
- when pulling entries `(obj, tag)` from the mark stack a `tag >= TAG_ARRAY_SLICE_LOW_LIMIT` indicates that we have to deal with a suffix slice of an `Array`. The visitor will then again check the slice's length and do the subdivision again, as necessary.

This way of treating suffix-slices as pseudo-heapobjects originates from the suggestion of @ulan in a SGM (2022-05-30). It sidesteps the issue with layering violations, and restricts the handling of pseudo-tags to a very restricted portion of the collector source code, viz. the pushing of the range, and the visitor's case analysis on the tag, which now needs to  know about the suffix slices. Fortunately the visitor already accepts the heap tag as an argument (and doesn't extract it from the object; which would be unreliable due to threading), so the appearance of pseudo-tags is not a big deal.

The cutoff is currently chosen as 127, so for any `Array` at most 128 new entries are being placed on the mark stack.

The charm of this solution is that the same code is doing the marking pushing/popping and visiting as before, only that now it happens in an interleaved manner. The mark is already present on the array, so no reëntrancy can't occur, and eventually all its fields get processed.

-----

Below is an account of how field-by-field marking, pushing and visiting was done formerly (still in use for prefix portion of arrays), and an aborted attempt to a scheme as suggested by @osa1. I leave it for reference.

----------
See #2903. This reduces the marking stack traffic for GC-ed arrays substantially. Not applicable to copying GC!

## Status quo

Here is what happens to an array object's (single) field while `mark_fields`:
 - considered only when it is a skewed pointer and points into the dynamic heap (otherwise it is a _static object_ or a _magic_, no need to GC)
 - visitor callback is invoked:
   - `mark_object` will place a bit and push to the mark stack when not marked yet
     (when being pushed onto the mark stack the (unskewed) pointer and the heap tag are remembered)
   - the field address gets `thread()`-ed when the contained object is physically located at a less or equal address than the array itself
     (threading will put the field address into the object tag saving the tag into the word where the field address points to; the old object pointer is overwritten, but may live on in the mark stack)

## How bulk marking could work (ABANDONED)

When discovering a sequence of value fields that are laid out successively in memory and a count field in front, we can do a bunch of nice shortcuts. Below items sketch the how this could work. Invariant: there must be a tag field immediately before the length field.

- the bulk visitor callback gets called with a pointer to the length field
- it decides that it is worth doing a ranged marking and divides the bulk into a (small) prefix and a non-empty suffix `(pointer_to_length, start_index)`
- set all marks corresponding to (dynamic heap) objects in the suffix to avoid re-visiting (see [open issue](#Revisit-avoidance-is-more-complicated))
- push `(pointer_to_length, start_index)` onto the mark stack, using low bits in the pointer to differentiate from `(obj, tag)` pairs
- bulk visitor callback returns the prefix length, the fields in this area will be visited individually

When it comes to popping the mark stack and there is a field range on its top we want to be as transparent as possible, but also have to perform steps that had to be skipped (relative to the proceeding on individual fields)

 - identify that the ToS is a range `(pointer_to_length, start_index)`
 - obtain a pointer to the field indexed by `start_index`
 - increment `start_index` (still remains on the stack)
 - if  `start_index` is equal to the length, pop the entry
 - check that the field is a GC-able pointer
 - if so, extract the object and the heap tag corresponding to the field
 - otherwise pop again and return that
 - apply the threading to the field address (use the invariant to get the home object and apply the threading criterion)
 - return the object and the heap tag

## Open issues

There are some ugly wrinkles in this design, that need to be addressed somehow.

### Revisit avoidance is more complicated

An object is either unmarked, in the mark stack or is being (has been) visited. When pushing entire ranges, we cannot process individual objects and as such marking and threading may happen in unexpected ways.

#### Saving the marked bit

When eagerly marking the whole range of fields, we must not drop the info whether the individual mark is already set. This is because a mark means that either an object is in the mark stack or being/have-been visited. We have two possibilities:
- mark range eagerly on push, but remember previous marks (e.g. in the unused bit of the `Value` in the fields), or
- instead mark lazily on popping an object from the range, performing the threading anyway, but never returning already marked objects.

The latter option is in conflict with what #2903 suggests, and could potentially invalidate the idea of pushing ranges at all.

#### Intervening `thread()` call after range marking

After a range has been pushed and all dynamic objects marked, an individual field with an object also referenced by the range might become threaded. In this case the tag field of that object gets overwritten, but can be distinguished from regular tags. Such objects got individually pushed and already popped from the stack, and thus have been visited. So the field in the range must be threaded, but the pointed object must be skipped (not visited again).

### Layering violation

The fact that the `pop_mark_stack` needs to know about object layout and then how to do the threading is disgusting.
Maybe there should be a callback parameter that is invoked then a non-pointer (i.e. range) entry is encountered in ToS position.

### `pointer_to_dynamic_heap` needs the heap base

If `pop_mark_stack` is to check pointers for pointing into the dynamic heap, it needs to receive the heap base, but it currently doesn't. It is open if the caller has this piece of information. (It has, what a relief!)

### Special format of `usize` passed to `push_mark_stack` and `push_range_mark_stack`

Distinguishing by the lowest bit is hacky.

## Further improvement opportunities

I spotted below optimisation tricks while reading the code.

 - `pointer_to_dynamic_heap` unskews a lot, why not compare with a `heap_base` that is 1 less?
 - `mark_object` doesn't need to get the previous mark (`bool`), but compare the (64-bit) word the mark is in whether it changed
 - `mark_object` unskews. Would it be possible to do `set_bit` using the `raw_ptr`?
 - `field_value.get_ptr() <= obj` could be `field_value.raw_ptr() + 1 <= obj` and further `field_value.raw_ptr() < obj` saving us an addition
 - can the double storing of the heap tag (by `thread` and `push_mark_stack`) be consolidated?
   (we have 2 cases for whether `thread` happens and 2 cases whether the `push_mark_stack` happens)
 - can the dynamic heap pointer check be reduced to a shift and a comparison with `BITMAP_FORBIDDEN_PTR` (at least while marking, as it is not available in copying GC)?

---
## [eschnett/julia](https://github.com/eschnett/julia)@[62e0729dbc...](https://github.com/eschnett/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Friday 2022-06-03 00:59:24 by Mirek Kratochvil

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
## [Moneyl/Nanoforge](https://github.com/Moneyl/Nanoforge)@[6454b11d8a...](https://github.com/Moneyl/Nanoforge/commit/6454b11d8a4a9d337f53e59ed8870c164b617069)
#### Friday 2022-06-03 01:25:13 by moneyl

Final changes for first WIP map editor release

Final changes required for first map editor release. Going with the bare minimum features needed to get it out ASAP. That way I can get early feedback on it's development direction, and hopefully seeing all the cool maps people make will motivate me to work on it more. There's a lot of room for improvement. Changes:
- You can no longer open a map without first opening or creating a project. The map editor doesn't really have a readonly mode, so I want to make sure people have a project open before opening a map. This ensures their changes are attached to a project and can be saved.
- Changed default colors of a few object types instead of most of them being plain white. Makes it a bit easier to discern different object types using default colors in MP maps. Object colors are serialized yet so it would've been annoying for users to have to change them to reasonable values every time they open the editor.
- Improved object name detection in zone importer. More objects have custom names, and names are more informative. E.g. player_start names specify the team, and multi_object_markers specify the object type. That way you don't need to click them to figure out what subtype they are.
- Updated font awesome icon font. It adds some new icons and changes the look of a few others. Did so since I was missing some newer icons that I wanted to use to identify trigger regions.
- Disabled object creation dialog temporarily. It's not strictly necessary for the first map editor release so I decided to move it to release 2.
- Added auto map export. Auto repacks the map and writes a vpp_pc to the selected export directory. It's recommended that you choose your RFGR data folder for this. That way you can just go back to the MP lobby, export the map, and start the match. Lets you test edits without needing to fully restart the game or manually copy vpps around.

Next need to package the release and write a basic map editing guide + limitations & known bugs list. Hopefully can release tonight without any new bugs but we'll see.

---
## [BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE](https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE)@[960e215c27...](https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/commit/960e215c2773473a94bd1e801f9720c74d95c304)
#### Friday 2022-06-03 01:44:00 by 1212-5858

[THERE HE IS crd#3005576 -- Broker Regulated by FINRA](https://youtu.be/8_Xs8nzrrkM?t=219)

[THERE HE IS crd#3005576 -- Broker Regulated by FINRA](https://youtu.be/8_Xs8nzrrkM?t=219)

WILLIAM THOMAS CASSESE
CRD#: 3005576

- it's called inside information - and that BILL, this is your client.
https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE


- i'll just leave the rest to you're imagination,
OK champ?

Keep taking  your instructions from your keeper OK Mr. Cassese
- here i found a video to help you understand, but in the scope of the movie - you should also abstain and keep a very safe distance from me, and you also owe me a SINCERE apology.

https://www.youtube.com/watch?v=Vt07KZmh0u0
- I will even give you a first look - but you talk like a cab driver Bill

PLUS - I don't what SPAM is
is that the canned food.
If that's how you maintain fitness I will definitely avoid that one
You should try throwing some jalapenos into your diet or maybe try shark testosterone, maybe boost 400CCs of Vitamix and hit the tradmills at least twice a week for a few hours at a time... hit the speed bag and learn how to use 12-12s and 58-58s without going to a range.


Then come over and use that tone in my living room - and lets see how quickly the authoritative tone in your dictum is adjusted.
After we have a discussion in private quarters and prior to an apology from you, and you know exactly what I am referring to...
It doesn't need to be end the floor of my living room like the broker from Morgan Stanley - got it?

    Thanks, ask the boys at 1211 Avenue of the Americas, Dan Digiamo for instance knows the character very well... but
    - the entire department was fired, immediately upon discovery by Mr. Gorman.

Take care, and hopefully i'll see you in the future in a different respect and understanding.

Next time you talk to me, if you ever meet me in person..
, just offer me some Spam in a dark alley somewhere prior to apologizing and let's see how your authority is left standing after that.

I'm sorry for trying to help you, but don't ever refer to me as Spam, I will just eat you instead.

https://www.youtube.com/watch?v=Vt07KZmh0u0

[WILLIAM THOMAS CASSESE CRD#: 3005576 B Broker Regulated by FINRA]

    Sorry for the typo this VERTU constellation doesn't have a spell check.

#bboNFL #KNEEHIGH #750

---
## [freedesktop/drm-tip](https://github.com/freedesktop/drm-tip)@[b9364eed92...](https://github.com/freedesktop/drm-tip/commit/b9364eed9232f3d2a846f68c2307eb25c93cc2d0)
#### Friday 2022-06-03 03:00:55 by Douglas Anderson

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
## [Smegheid/water_heater](https://github.com/Smegheid/water_heater)@[e7a1e33305...](https://github.com/Smegheid/water_heater/commit/e7a1e333057097b62409d23391e6cd1f12258cad)
#### Friday 2022-06-03 03:11:39 by Smeghead

A fairly jumbled set of changes that stacked up, with a few simple goals.
This adds the graphs for the RPi's CPU temperature and memory usage, along with a separate trace on the heater temperatures graph for the hot water supply out of the tank into the house. The latter may or may not be interesting; I don't know yet.
This also fixes panning left and right, which were broken when I tried to nail down the conversion of the start and end timestamps. Not sure why I thought a `date` format specifier of `%d` was minutes, but there you go.
This also adds an experimental change to the zoom funciton. For a while now I've not liked how starting at one of the canned duration links then zooming results in a fixed timescale that doesn't get updated. I've tried to do something about this by detecting that the start time is not fixed (of the format "n <unit> ago", parsing that into a value and units, and then doubling or halving the value as best as possible, including dropping down to the next smaller units if need be (the time parsing is all based on integers, so `0.5 hour ago` is not valid.  This kinda works, though it gets a bit messy-looking eventually: zooming in at 1 hour becomes 30 min, then 15 min, then 450 sec, etc. Zooming out stays with seconds, so an hour becomes `3600 sec ago`. I haven't decided if I care enough about that to do something about it just yet. We'll see.
There's also a commented-out block that talks about watermarks. I was thinking of doing something where a watermark with either the date for the graph (if it's all in one day) or a date range is added into the image. That way if I save off a graph, I'll have a record of when it relates to rather than knowing that it was around 4:50pm some afternoon. However, I don't like `rrdgraph`'s watermarking option (it increases the height of the image and sticks a little label underneath the legend) so I was considering running it through imagemagick's `convert` instead. Not sure yet.

---
## [k6l2/korl](https://github.com/k6l2/korl)@[cd150d5ba5...](https://github.com/k6l2/korl/commit/cd150d5ba528bfc5f8909b9ec41e2e909684ac13)
#### Friday 2022-06-03 03:39:09 by Kyle

WIP; holy shit it works, and runs in like 360us!

- fix a couple bugs
- add scaffolding to test creating save state files
- add timings to see how much time it takes to generate save states

timing results:
- generation of the save state buffer takes 360 microseconds
- writing the buffer to a file takes 430 microseconds
- it should be entirely feasible to generate a save state buffer at the
  beginning of every single frame!  the dream of being able to generate
  _useful_ crash dumps is alive!!!

---
## [Clownsw/rust-analyzer](https://github.com/Clownsw/rust-analyzer)@[1a5925dc84...](https://github.com/Clownsw/rust-analyzer/commit/1a5925dc84d0ef966023d6612147f93a0464174c)
#### Friday 2022-06-03 04:35:48 by bors

Auto merge of #12294 - listochkin:prettier, r=Veykril

Switch to Prettier for TypeScript Code formatting

## Summary of changes:

 1. Added [`.editorconfig` file](https://editorconfig.org) to dictate general hygienic stuff like character encoding, no trailing whitespace, new line symbols etc. for all files (e.g. Markdown). Install an editor plugin to get this rudimentary formatting assistance automatically. Prettier can read this file and, for example, use it for indentation style and size.
 2. Added a minimal prettier config file. All options are default except line width, which per [Veykril](https://github.com/Veykril) suggestion is set to 100 instead of 80, because [that's what `Rustfmt` uses](https://rust-lang.github.io/rustfmt/?version=v1.4.38&search=#max_width).
 3. Change `package.json` to use Prettier instead of `tsfmt` for code formatting.
 4. Performed initial formatting in a separate commit, per [bjorn3](https://github.com/bjorn3) suggestion added its hash to a `.git-blame-ignore-revs` file. For it to work you need to add a configuration to your git installation:
    ```Shell
    git config --global blame.ignoreRevsFile .git-blame-ignore-revs
    ```
 5. Finally, removed `typescript-formatter` from the list of dependencies.

----
What follows below is summary of the discussion we had on Zulip about the formatter switch:

## Background

For the context, there are three reasons why we went with `tsfmt` originally:
* stick to vscode default/built-in
* don't add extra deps to package.json.lock
* follow upstream (language server node I think still uses `tsfmt`)

And the meta reason here was that we didn't have anyone familiar with frontend, so went for the simplest option, at the expense of features and convenience.

Meanwhile, [**Prettier**](https://prettier.io) became a formatter project that JS community consolidated on a few years ago. It's similar to `go fmt` / `cargo fmt` in spirit: minimal to no configuration to promote general uniformity in the ecosystem. There are some options, that were needed early on to make sure the project gained momentum, but by no means it's a customizable formatter that is easy to adjust to reduce the number of changes for adoption.

## Overview of changes performed by Prettier

Some of the changes are acceptable. Prettier dictates a unified string quoting style, and as a result half of our imports at the top are changed. No one would mind that. Some one-line changes are due to string quotes, too, and although these a re numerous, the surrounding lines aren't changed, and git blame / GitLens will still show relevant context.

Some are toss ups. `trailingComma` option - set it to `none`, and get a bunch of meaningless changes in half of the code. set it to `all` and get a bunch of changes in the other half of the code. Same with using parentheses around single parameters in arrow functions: `x => x + 1` vs `(x) => x + 1`. Perrier forces one style or the other, but we use both in our code.

Like I said, the changes above are Ok - they take a single line, don't disrupt GitLens / git blame much. **The big one is line width**. Prettier wants you to choose one and stick to it. The default is 80 and it forces some reformatting to squish deeply nested code or long function type declarations. If I set it to 100-120, then Prettier finds other parts of code where a multi-line expression can be smashed into a single long line. The problem is that in both cases some of the lines that get changed are interesting, they contain somewhat non-trivial logic, and if I were to work on them in future I would love to see the commit annotations that tell me something relevant. Alas, we use some of that.

## Project impact

Though Prettier is a mainstream JS project it has no dependencies. We add another package so that it and ESLint work together nicely, and that's it.

---
## [Mu-L/NetHack](https://github.com/Mu-L/NetHack)@[e764026a1f...](https://github.com/Mu-L/NetHack/commit/e764026a1f2a005742118db24be71ae4ec270e38)
#### Friday 2022-06-03 05:06:55 by PatR

more wish logging - show the result

Extend the log event for a wish to include what was produced.  It
would be better to show the item as fully ID'd but then #chronicle
gives away information.

The backslash+newline pairs were inserted for this log message.  In
the game and in dumplog those two lines are each one wide line.  The
turn numbers shown are actually arbitrary since ^W takes no time.

|Logged events:
| Turn
|    1: wizard the chaotic male orcish Wizard entered the dungeon
|    2: made his first wish - "protection", got "a tattered cape"
|    3: made his first artifact wish - "blessed +2 rustproof magicbane",\
 got "an athame named Magicbane"
|    4: wished for "master key of thievery", got "a key named The Master\
 Key of Thievery"

---
## [Spyroshark/Pariah-Station](https://github.com/Spyroshark/Pariah-Station)@[70a87f9510...](https://github.com/Spyroshark/Pariah-Station/commit/70a87f95100c290699ce5b92bb099d2f56bbb336)
#### Friday 2022-06-03 06:11:20 by Gallyus

HOLY SHIT SHUT UP (#742)

* HOLY SHIT SHUT UP

* Apply suggestions from code review

* seeba sauce

---
## [PurpleSushi22/mindustry-ohnoandknuckles](https://github.com/PurpleSushi22/mindustry-ohnoandknuckles)@[429b1c5364...](https://github.com/PurpleSushi22/mindustry-ohnoandknuckles/commit/429b1c536495a4d16f515a5ab00552f2877021f2)
#### Friday 2022-06-03 06:37:23 by PurpleSushi22

yes

What is the FitnessGram PACER Test?
FitnessGram
PACER Test

The FitnessGram PACER Test is a multistage aerobic capacity test that progressively gets more difficult as it continues.

The test is used to measure a student's aerobic capacity as part of the FitnessGram assessment. Students run back and forth as many times as they can, each lap signaled by a beep sound. The test get progressively faster as it continues until the student reaches their max lap score.

The PACER Test score is combined in the FitnessGram software with scores for muscular strength, endurance, flexibility and body composition to determine whether a student is in the Healthy Fitness Zone™ or the Needs Improvement Zone™.
New Sound. New Beeps. Same Test.

For nearly three decades, the Progressive Aerobic Cardiovascular Endurance Run (PACER) Test has been used as part of the FitnessGram assessment in thousands of P.E. classes in all 50 states.  Now the legendary voice of the school fitness test is changing. The Cooper Institute is proud to announce the launch of the FitnessGram PACER Test Remixes! powered by Hip Hop Public Health.

The new album is a collaboration between The Cooper Institute and Hip Hop Public Health, two organizations dedicated to improving youth fitness, reducing childhood obesity, and promoting life-long healthy habits through research and education.

FitnessGram and Hip Hop Public Health

The six new tracks revitalize the decades-old fitness test with a fusion of hip-hop, pop, electronic dance music, and Latin-inspired beats, bringing a DJ dance party vibe to the gym.

The iconic voice of the original test has been replaced by both male and female voices in English and Spanish to motivate and encourage participants throughout each of the 22-minute tracks.

The combination of diverse voices and culturally relevant beats is designed to inspire a new generation of students to get active and stay healthy now and well into adulthood.
The classic sound of the original 20-Meter FitnessGram PACER Test is now available with visual cues on YouTube!

---
## [aggregat4/dendriform](https://github.com/aggregat4/dendriform)@[515a4249fb...](https://github.com/aggregat4/dendriform/commit/515a4249fb389d53bfac4785ee7f8ecb38e3db0c)
#### Friday 2022-06-03 06:54:13 by Boris Terzic

Fixes a bug where we were not explicitly returning a value from a function and it was evaluating as undefined (fuck you javascript)

---
## [stackhpc/kolla-ansible](https://github.com/stackhpc/kolla-ansible)@[4e991a98ea...](https://github.com/stackhpc/kolla-ansible/commit/4e991a98eaf25faa073bb5b01470a5808b5f18e4)
#### Friday 2022-06-03 08:03:41 by Radosław Piliszek

[CI] Nullify attempts

Per Clark Boylan's feedback [1], retries cause a retry not only
for pre playbook failures but also for cases where Ansible detects
network connectivity issues and they are caused by disks getting
filled to their fullest. This is an issue we experience that
sometimes results in a POST_FAILURE but certain FAILUREs are
retried which wastes CI resources.
The problematic jobs are ceph jobs. They are to be looked into.
Backport to all branches.
We can adjust retries for the core jobs that do not exhibit the
nasty behaviour but first we can try running without retries
to measure the troublesomeness.

[1] https://review.opendev.org/c/openstack/kolla-ansible/+/843536

Change-Id: I32fc296083b4881e8f457f4235a32f94ed819d9f
(cherry picked from commit 153956e458157e44d73efc3dd369699ff20e4d12)

---
## [Savage2614/TelegramBot_KGU](https://github.com/Savage2614/TelegramBot_KGU)@[c3f8da565f...](https://github.com/Savage2614/TelegramBot_KGU/commit/c3f8da565f915a449f535de85f7cf9f96dd3c48c)
#### Friday 2022-06-03 08:55:08 by Savage2614

Added geolocation of all cases, made two columns of all button interfaces. And fuck your asses

---
## [jkirk/grml-live](https://github.com/jkirk/grml-live)@[518eb395d8...](https://github.com/jkirk/grml-live/commit/518eb395d8652ccf260e4fe6fc15af7946fc7c49)
#### Friday 2022-06-03 09:46:54 by Michael Prokop

Refresh Secure Boot support, supporting new 'debian' method

Secure Boot mode wasn't reliably working, e.g. failing to boot in EFI
mode with disabled Secure Boot, but also hard to debug.

Now with our move from our own Grml kernel packages to the official
Debian kernel ones (which are signed and intended for usage with enabled
Secure Boot) it makes sense to support a proper Secure Boot chain
without hacks like we used to do (like relying on and old GRUB binary
from Ubuntu which supported booting unsigned kernels).

We do NOT enable Secure Boot support by default *yet* though, since we
need to get more testing of this and right now we're in the middle of an
RC version (2020.06-rc1) and the upcoming new stable version of Grml.

Relevant changes:

* minimize templates/secureboot/grub.cfg: while it's certainly nice
  to display only entries that are actually working under Secure Boot,
  it's annoying to have to maintain yet another place of boot menus.

  Also if something fails with detection of Secure Boot then it's annoying
  to have to debug this, instead let's display an error message, inform
  the user about it and ask for debugging information.

  Instead introduce a new GRUB theme (/boot/grub/grml-theme/sb-theme.txt)
  which displays a message that we're running in Secure Boot mode.
  While at it, unify indention in existing /boot/grub/grml-theme/theme.txt.

* move templates/EFI/BOOT towards templates/EFI/ubuntu/BOOT/ to be able
  to support debian and ubuntu methods at the same time

* ship GRUB binaries in templates/EFI/debian/, similar to the ones in
  templates/EFI/ubuntu

* switch Ubuntu's grubx64.efi.signed from grubx64.efi.signed to gcdx64.efi.signed;
  they differ in what GRUB's $prefix variable is set to:
  * gcdx64.efi.signed uses boot/grub/
  * grubx64.efi.signed uses EFI/ubuntu/
  -> the code in grml-live itself was adjusted accordingly and this also
  enables us to generalize the Secure Boot methods debian + ubuntu to
  use the same code path

* drop templates/boot/grub/grmlenv.cfg: everything what's relevant
  can be taken care of from inside templates/secureboot/grub.cfg,
  so let's avoid another indirection.

  We also moved the detection of Secure Boot into templates/secureboot/grub.cfg
  and reworked it: while Ubuntu's patches have a C function grub_efi_secure_boot(),
  there's no ready-to-use way to detect Secure Boot. But the wrmsr
  command is amongst the list of GRUB's disabled_mods and we can
  distingiush between exit code 18 (wrong invocation/argument usage) and 30 (Secure Boot forbits loading module).

* mention secure boot method in execution prompt/summary to be aware of
  its (non) presence ahead of execution

* update etc/grml/grml-live.conf to properly reflect current state of
  Secure Boot support

Thanks: Jordan Uggla for feedback

This work was funded by Grml-Forensic.

---
## [planetscale/vitess](https://github.com/planetscale/vitess)@[dbfb9a49f7...](https://github.com/planetscale/vitess/commit/dbfb9a49f7c3b067221d0aae0d3c0285e6baf098)
#### Friday 2022-06-03 09:50:09 by Andrew Mason

[vtadmin] Add infrastructure for generating authz tests for vtadmin (#10397)

* Add infrastructure for generating authz tests for vtadmin

The lack of verifying authz checks are where they should be is one of the
most glaring issues in vtadmin (in my opinion; it's also my "fault" things
are this way). At the same time, writing all the code by hand to verify
every single endpoint would be a giant pain (which is the main reason
things are this way). So, let's codegen all the bits we don't care about!
The bonus here is that the config.json now can serve as authoritative on
what permissions are required for what endpoints.

The goal here is to have the config primarily specify the rules needed for
each endpoint, with as minimal "overhead" (currently specifying test cases
and mock data) as possible.

I want to separate the introduction of this setup from its complete
adoption, so I will submit a follow-up change that adds the rest of the
endpoint tests.

Signed-off-by: Andrew Mason <andrew@planetscale.com>

* add missing license headers

Signed-off-by: Andrew Mason <andrew@planetscale.com>

* Add make target and CI check

Signed-off-by: Andrew Mason <andrew@planetscale.com>

---
## [aljoscha/materialize](https://github.com/aljoscha/materialize)@[3bc0574297...](https://github.com/aljoscha/materialize/commit/3bc057429749d105bd462595fc3512554be9832f)
#### Friday 2022-06-03 10:04:07 by Daniel Harrison

persist: fix open-loop benchmark data generation schedule

Somewhere along the way (probably my commit that removed the use of
futures_executor::block_on) the data generation schedule got wonky. This
changes it to be the following, which is hopefully more interesting:

- Immediately at startup, generate the first batch of data and
  immediately allow it to be written to the channel.
- Immediately generate the second batch of data. Sleep until `start +
  time_per_batch`, then allow it to be written to the channel.
- Continue doing this until a `None` batch is generated. Then return
  from the task without sleeping.

In contrast, before, it was doing something like:
- Immediately wait until `sleep+time_per_batch`.
- Generate a batch (which takes non-trivial time at larger batch sizes)
  and write it to the channel as long as it hasn't been more than
  `start + num_batches * time_per_batch`.
- Sleep and repeat.

In practice, the new impl has the following advantages:
- A batch is immediately written on startup. This feels more in the
  spirit of throughput to me, given that before we don't even have a
  batch to write down for the first `time_per_batch` but it's included
  in the calculation of overall throughput.
- Similarly, the generate task now returns immediately after finding out
  it's done. Previously, it would sleep before finding out that it got a
  None batch.
- We account for the non-trivial time it takes to generate batches of
  larger sizes.
- Batches are emitted at a more even rate. The previous impl had a
  tendency to wake up and emit two batches back-to-back and then sleep
  for a long time. (This is almost certainly my bug from the block_on
  PR.)

---
## [EbolaSpreadn247/endless-war](https://github.com/EbolaSpreadn247/endless-war)@[150b0ba35f...](https://github.com/EbolaSpreadn247/endless-war/commit/150b0ba35f0fab5eca159b57609e28ddb3ae3093)
#### Friday 2022-06-03 10:39:58 by EbolaSpreadn247

fuck squeezing.

fuck this shit. Its annoying.
Removes friendly squeezing, removes self squeezing too.

---
## [sumeerbhola/cockroach](https://github.com/sumeerbhola/cockroach)@[f782e45fd0...](https://github.com/sumeerbhola/cockroach/commit/f782e45fd0da015396bc758e855535a951f2e21a)
#### Friday 2022-06-03 12:14:21 by Andrei Matei

util/timeutil: don't strip mono time in timeutil.Now

Our timeutil.Now() insists on returning UTC timestamps, for better or
worse. It was doing this by calling time.Now.UTC(). The rub is that the
UTC() call strips the monotonic clock reading from the timestamp.
Despite repeatedly trying ([1]), I've failed to find any reasonable
reason for that behavior. To work around it, this patch does unsafe
trickery to get a UTC timestamp without stripping the monos.

Stripping the monos has the following downsides:
1. We lose the benefits of the monotonic clock reading.
2. On OSX, only the monotonic clock seems to have nanosecond resolution. If
we strip it, we only get microsecond resolution. Besides generally sucking,
microsecond resolution is not enough to guarantee that consecutive
timeutil.Now() calls don't return the same instant. This trips up some of
our tests, which assume that they can measure any duration of time.
3. time.Since(t) does one less system calls when t has a monotonic reading,
making it twice as fast as otherwise:
https://cs.opensource.google/go/go/+/refs/tags/go1.17.2:src/time/time.go;l=878;drc=refs%2Ftags%2Fgo1.17.2

An alternative considered was setting the process' timezone to UTC in an
init(): time.Local = time.UTC. That has downsides: it makes cockroach
more unpleasant to link as a library, and setting the process timezone
makes the timestamps not roundtrip through marshalling/unmarshalling
(see [1]).

[1] https://groups.google.com/g/golang-nuts/c/dyPTdi6oem8

---
## [me4502/SpongeAPI](https://github.com/me4502/SpongeAPI)@[b402915775...](https://github.com/me4502/SpongeAPI/commit/b40291577550b9dff9e0accf1755f365db77eeb8)
#### Friday 2022-06-03 12:53:38 by Daniel Naylor

Rework the command API for API 8 (1.14)

Much of this is geared towards removal of CommandSources in the API and as such, some specialised types have been removed. However, there are a couple of unresolved questions:

* How do we represent an RCON client and the console - and where? The console is currently directly the Server object at this point. This will likely happen with the Client object too.
* The cause is an important part of our command system for 1.14+ and command writes should embrace it. However, we should consider a way to make it easy for developers to take our cause and work with our recommendations. One thing I'm thinking about is creating a replacement for the command source that wraps the cause with a few helper methods - much like the command context, but for commands that don't use our builder. This would be important when the cause event context has a part to play as that is intended to potentially override what's in the direct cause. That way, we can try to standardise what happens.

The console source has been removed in favour of using the `Server` as a command source. Signs are now directly sources - the fact the source is separate is, in my opinion, an implementation detail. Again, same with command blocks.

I have created javadocs accordingly, but this is up for discussion within the Sponge team and we can go either way at this point. There are implementation concerns too, but that's not the concern of the API!

This is all up for discussion. Things will change as implementation progresses.

---
## [avar/git](https://github.com/avar/git)@[bdaf1dfae7...](https://github.com/avar/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Friday 2022-06-03 13:18:29 by Tao Klerks

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b9ea6e6b4a...](https://github.com/treckstar/yolo-octo-hipster/commit/b9ea6e6b4a1e5db8b71a44b2f9c487e7fe2218ac)
#### Friday 2022-06-03 13:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [KermitProject/ckermit](https://github.com/KermitProject/ckermit)@[dbea7d2d84...](https://github.com/KermitProject/ckermit/commit/dbea7d2d841f5b52bc2ae2f0347d5aa003dde111)
#### Friday 2022-06-03 13:37:22 by Kermit Project

C-Kermit 10.0 Beta.04, 03 June 2022

Corrects one or two syntax errors fatal to compilation.

In the (now) time-honored tradition of releasing a second Beta just
hours after the first, here is Beta.04 (the curse of the odd-numbered
Betas?).

In Beta.03, two compilation errors that I fixed repeatedly — at
least one of them fatal — somehow kept coming back. Senior confusion,
no doubt... editing or uploading the wrong copy of the file. You can
see why I'm anxious to get out of this business! The corrections for
Beta.04 are:

    ckctel.c:

    tn_ssbopt(TELOPT_NEWENVIRON,TELQUAL_SEND,(CHAR *)request,
               strlen((CHAR *)request)); /* 2022-01-27 */

    should be:

    tn_ssbopt(TELOPT_NEWENVIRON,TELQUAL_SEND,request,
               strlen((char *)request)); /* SMS 2022-06-03 */

Note EVERY makefile target should include the equivalent of gcc/clang
-funsigned-char if available. Has anybody ever actually used *signed*
chars??? (I haven't changed the makefile targets myself yet, but
readers are welcome to do this for their platforms and report the
results so I can incorporate the change where it works.)

  ckuusx.c:

    ck_curpos(int row, col) {

  should be:

    ck_curpos(int row, int col) {

At least one of these (#2) prevented successful compilation on at least
one platform (Raspberry pi OS).

Incidentally, I find myself confused about pre-ANSI function argument
list syntax. I see several forms in ckuusx.c:

         int ck_curpos(row, col) int row, col; {...}
         int ck_curpos(row, col) int row, int col; {...}
         int ck_curpos(row, col) int row; int col; {...}

Only the first one seems to be causing trouble in C-Kermit, even though
it was allowed in K&R C (see pp. 23, 24, 54, and 58 of the original 1978
C book). I see examples of (3) in the same book (e.g. pp. 60, 67, 78),
but I don't see examples of (2) in the book, and yet when when (1) caused
problems and was changed to (2) the problem went away. For Beta.04 I'm
going to err on the side of not making too many changes.

I also have a report that constructions like "*s++;" generates "Result
unused" warnings in Clang, e.g. in ckclib.c about line 3190, but I don't
believe that these are a problem. As Brian Kernighan said in 1974, "The
'*s' returns a character; the '++' increments the pointer so we'll get
the next character next time around. As you can see, as we make things
more efficient, we also make them less clear. But '*s++' is an idiom so
common that you have to know it." In this case, were toodling through a
string character by character in a loop. So the result is unused in the
first iteration but will be used in the next. The are countless instances
of this usage in the code and I doubt that the risk of changing them is
worth the benefit.

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[bd7d220a61...](https://github.com/ammarfaizi2/linux-fork/commit/bd7d220a614aff4cf48e48c255e60ca057732eff)
#### Friday 2022-06-03 13:51:23 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

commit c570449094844527577c5c914140222cb1893e3f upstream.

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [HIDEN64/tacobot](https://github.com/HIDEN64/tacobot)@[95d3943dd4...](https://github.com/HIDEN64/tacobot/commit/95d3943dd4c97fd100aafbb6291f2be75cd5d640)
#### Friday 2022-06-03 14:16:12 by HIDEN64

Revert "fuck you shitcord (this is bugged as hell)"

This reverts commit aa0b6d80fcff48d421feecf82bc034b132a73994.

---
## [Spoopy11/sojourn-station](https://github.com/Spoopy11/sojourn-station)@[9f7af6b698...](https://github.com/Spoopy11/sojourn-station/commit/9f7af6b698a6633907432576f9699af209dec6cd)
#### Friday 2022-06-03 14:17:10 by nikothedude

FUCKING HOTFIX FOR A STUPID FUCKING BUG (#3459)

* FUCK

* HOLY SHIT IM DUMB

---
## [tailwindlabs/headlessui](https://github.com/tailwindlabs/headlessui)@[136c0281f7...](https://github.com/tailwindlabs/headlessui/commit/136c0281f77a439e103d2f7388c7754fccfb13ac)
#### Friday 2022-06-03 14:18:26 by Robin Malfait

simplify `outside click` behaviour

Here is a little story. We used to use the `click` event listener on the
window to try and detect whether we clicked outside of the main area we
are working in.

This all worked fine, until we got a bug report that it didn't work
properly on Mobile, especially iOS. After a bit of debugging we switched
this behaviour to use `pointerdown` instead of the `click` event
listener. Worked great! Maybe...

The reason the `click` didn't work was because of another bug fix. In
React if you render a `<form><Dialog></form>` and your `Dialog` contains
a button without a type, (or an input where you press enter) then the
form would submit... even though we portalled the `Dialog` to a
different location, but it bubbled the event up via the SyntethicEvent
System. To fix this, we've added a "simple" `onClick(e) { e.stopPropagation() }`
to make sure that click events didn't leak out.

Alright no worries, but, now that we switched to `pointerdown` we got
another bug report that it didn't work on older iOS devices. Fine, let's
add a `mousedown` next to the `pointerdown` event. Now this works all
great! Maybe...

This doesn't work quite as we expected because it could happen that both
events fire and then the `onClose` of the Dialog component would fire
twice. In fact, there is an open issue about this: #1490 at the time of
writing this commit message.
We tried to only call the close function once by checking if those
events happen within the same "tick", which is not always the case...

Alright, let's ignore that issue for a second, there is another issue
that popped up... If you have a Dialog that is scrollable (because it is
greater than the current viewport) then a wild scrollbar appears (what a
weird Pokémon). The moment you try to click the scrollbar or drag it the
Dialog closes. What in the world...?

Well... turns out that `pointerdown` gets fired if you happen to "click"
(or touch) on the scrollbar. A click event does not get fired. No
worries we can fix this! Maybe...

(Narrator: ... nope ...)

One thing we can try is to measure the scrollbar width, and if you
happen to click near the edge then we ignore this click. You can think
of it like `let safeArea = viewportWidth - scrollBarWidth`. Everything
works great now! Maybe...

Well, let me tell you about macOS and "floating" scrollbars... you can't
measure those... AAAAAAAARGHHHH

Alright, scratch that, let's add an invisible 20px gap all around the
viewport without measuring as a safe area. Nobody will click in the 20px
gap, right, right?! Everything works great now! Maybe...

Mobile devices, yep, Dialogs are used there as well and usually there is
not a lot of room around those Dialogs so you almost always hit the
"safe area". Should we now try and detect the device people are
using...?

/me takes a deep breath...

Inhales... Exhales...

Alright, time to start thinking again... The outside click with a
"simple" click worked on Menu and Listbox not on the Dialog so this
should be enough right?

WAIT A MINUTE

Remember this piece of code from earlier:

```js
onClick(event) {
  event.stopPropagation()
}
```

The click event never ever reaches the `window` so we can't detect the
click outside...

Let's move that code to the `Dialog.Panel` instead of on the `Dialog`
itself, this will make sure that we stop the click event from leaking
if you happen to nest a Dialog in a form and have a submitable
button/input in the `Dialog.Panel`. But if you click outside of the
`Dialog.Panel` the "click" event will bubble to the `window` so that we
can detect a click and check whether it was outside or not.

Time to start cleaning:
  - ☑️ Remove all the scrollbar measuring code...
    - Closing works on mobile now, no more safe area hack
  - ☑️ Remove the pointerdown & mousedown event
    - Outside click doesn't fire twice anymore
  - ☑️ Use a "simple" click event listener
    - We can click the scrollbar and the browser ignores it for us

All issues have been fixed! (Until the next one of course...)

---
## [sanyuezoe/IMD-project-Hidden](https://github.com/sanyuezoe/IMD-project-Hidden)@[9b4e341d75...](https://github.com/sanyuezoe/IMD-project-Hidden/commit/9b4e341d753994baa261125384915810f3b9ed6e)
#### Friday 2022-06-03 15:04:08 by sanyue

Delete young-female-model-surrounded-by-male-hands-like-her-own-thoughts-problems-dark-wall.jpg

---
## [Vaern/Hbm-s-Nuclear-Tech-GIT](https://github.com/Vaern/Hbm-s-Nuclear-Tech-GIT)@[21fc785777...](https://github.com/Vaern/Hbm-s-Nuclear-Tech-GIT/commit/21fc78577732f2aae1219589a312feafcc417fcd)
#### Friday 2022-06-03 16:02:53 by Vaern

did some stuff with the assembler TE

god fuck this shit

---
## [betrusted-io/xous-core](https://github.com/betrusted-io/xous-core)@[3ad70c711d...](https://github.com/betrusted-io/xous-core/commit/3ad70c711d3aa8d6c920381dbba8090eca61387b)
#### Friday 2022-06-03 16:06:17 by bunnie

add mjolnir; fix EP allocation bug

Spent the last couple days tracing down a dastardly bug, which was
slew only upon the creation of mjolnir.

The SpinalHDL USB core is unique in that it has a hardware
implementation of a linked list for its descriptors. This can
be very high performance because you can receive packets much
faster than software can keep up with it in short bursts --
assuming the stack can deal with it.

Unfortunately the poor Rust stack that we adopted from
the STM32 land only assumes single descriptors. Alas, we cannot
unlock the full power of linked list descriptors, and instead
we use "single entry lists" with static allocations, to match
the paradigm of the STM32.

Anyways. Early on, when creating the linked list allocator,
I contemplated doing it the Rusty way, and the C way. The Rusty
way would create a structure that mapped the descriptor headers
plus the variable-sized data chunk into some magical structure
that got us bounds checking and had proper accessors etc.
The C way would just be raw pointer manipulation using unsafes.

Unfortunately, my Rust-fu was no match for the linked list.
The problem is that the descriptors could be of any data size,
and they had to be mapped to a very specific piece of memory.
So I had to create a `repr (C)` struct that matched Rust's
alignment requirements and also somehow could deal with
a variable length array *but could not be a slice* because
the hardware implementation does not have the flexibility
to accommodate a fat pointer. I couldn't figure out how
to get const generics to work, and the size of the array
could be anything from 0 bytes to a couple kilobytes. So,
I ditched the safety of Rust and went with a C-style unsafe
pointer implementation.

Sure enough, it came to haunt me. When I wrote the allocator,
I forgot to allocate space for the descriptor headers. This
worked fine for the keyboard, because the keyboard asks for
32-byte descriptors but only ever does a 25-byte report. That's
just enough to fit the descriptor headers, ironically.

When implementing FIDO/U2F, it asks for 64-byte descriptors
and uses exactly 64-byte messages for everything. This caused
a bug where I could receive one incoming packet, but when
responding with an outgoing packet we'd overwrite the descriptors
of the receiving packet, zeroing it out, causing the the descriptor
to fail in the hardware state machine. Of course I never saw
this because I would print the descriptors of the individual
endpoints upon creating them, but the pointer-overflow problem
only occurs later.

Thus mjolnir was created, it is basically a tool that gives me
a raw hex dump of the endpoint and descriptor banks, which I
can then analyze and diff. It's very powerful, but also very
unweildy -- if invoked indiscriminantly, the overhead of
all the prints would cause other failures due to timing problems.
Thus mjolnir exists as a feature that introduces special
locks around the USB endpoints so that they NAK while mjolnir
does its analysis, disallowing concurrent mutation of the
memory state.

Upon deploying mjolnir, the problem became obvious, and it is
now fixed.

Thus, while on the one hand, it's a great story of how maybe
we should avoid unsafe Rust, it's also a story of how hardware
structures like a hardware linked list may be fundamentally
incompatible with Rust. I think if the hardware USB descriptor
linked list was modified to allow for a fat pointer to track
a data slice, the implementation would almost be trivial. But,
rewriting HDL to fit Rust also has its hazards, as the exact
layout of a fat pointer in RAM is not guaranteed and it would
probably foolhardy to commit to something not guaranteed in
hardware.

---
## [GoogleCloudPlatform/alloydb-auth-proxy](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy)@[e67af2b086...](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy/commit/e67af2b08639f8400f796a4d19ba87a741b16697)
#### Friday 2022-06-03 16:29:19 by WhiteSource Renovate

chore(deps): update module github.com/spf13/cobra to v1.4.0 (#35)

[![WhiteSource Renovate](https://app.renovatebot.com/images/banner.svg)](https://renovatebot.com)

This PR contains the following updates:

| Package | Type | Update | Change |
|---|---|---|---|
| [github.com/spf13/cobra](https://togithub.com/spf13/cobra) | require | minor | `v1.2.1` -> `v1.4.0` |

---

### Release Notes

<details>
<summary>spf13/cobra</summary>

### [`v1.4.0`](https://togithub.com/spf13/cobra/releases/v1.4.0)

[Compare Source](https://togithub.com/spf13/cobra/compare/v1.3.0...v1.4.0)

### Winter 2022 Release ❄️

Another season, another release!

#### Goodbye viper! 🐍 🚀

The core Cobra library no longer requires Viper and all of its indirect dependencies. This means that Cobra's dependency tree has been drastically thinned! The Viper dependency was included because of the `cobra` CLI generation tool. [This tool has migrated to `spf13/cobra-cli`](https://togithub.com/spf13/cobra-cli/releases/tag/v1.3.0).

It's *pretty unlikely* you were importing and using **the bootstrapping CLI tool** as part of your application (after all, it's just a tool to get going with core `cobra`).

But if you were, replace occurrences of

    "github.com/spf13/cobra/cobra"

with

    "github.com/spf13/cobra-cli"

And in your `go.mod`, you'll want to also include this dependency:

    github.com/spf13/cobra-cli v1.3.0

Again, the maintainers *do not anticipate* this being a breaking change to users of the core `cobra` library, so minimal work should be required for users to integrate with this new release. Moreover, this means the dependency tree for your application using Cobra should no longer require dependencies that were inherited from Viper. Huzzah! 🥳

If you'd like to read more

-   issue: [https://github.com/spf13/cobra/issues/1597](https://togithub.com/spf13/cobra/issues/1597)
-   PR: [https://github.com/spf13/cobra/pull/1604](https://togithub.com/spf13/cobra/pull/1604)

#### Documentation 📝

-   Update Go Doc link and badge in README: [https://github.com/spf13/cobra/pull/1593](https://togithub.com/spf13/cobra/pull/1593)
-   Fix to install command, now targets `@latest`: [https://github.com/spf13/cobra/pull/1576](https://togithub.com/spf13/cobra/pull/1576)
-   Added MAINTAINERS file: [https://github.com/spf13/cobra/pull/1545](https://togithub.com/spf13/cobra/pull/1545)

#### Other 💭

-   Bumped license year to 2022 in golden files: [https://github.com/spf13/cobra/pull/1575](https://togithub.com/spf13/cobra/pull/1575)
-   Added Pixie to projects: [https://github.com/spf13/cobra/pull/1581](https://togithub.com/spf13/cobra/pull/1581)
-   Updated labeler for new labeling scheme: [https://github.com/spf13/cobra/pull/1613](https://togithub.com/spf13/cobra/pull/1613) & syntax fix: [https://github.com/spf13/cobra/pull/1624](https://togithub.com/spf13/cobra/pull/1624)

Shoutout to our awesome contributors helping to make this cobra release possible!!
[@&#8203;spf13](https://togithub.com/spf13) [@&#8203;marckhouzam](https://togithub.com/marckhouzam) [@&#8203;johnSchnake](https://togithub.com/johnSchnake) [@&#8203;jpmcb](https://togithub.com/jpmcb) [@&#8203;liggitt](https://togithub.com/liggitt) [@&#8203;umarcor](https://togithub.com/umarcor) [@&#8203;hiljusti](https://togithub.com/hiljusti) [@&#8203;marians](https://togithub.com/marians) [@&#8203;shyim](https://togithub.com/shyim) [@&#8203;htroisi](https://togithub.com/htroisi)

### [`v1.3.0`](https://togithub.com/spf13/cobra/releases/v1.3.0)

[Compare Source](https://togithub.com/spf13/cobra/compare/v1.2.1...v1.3.0)

### v1.3.0 - The Fall 2021 release 🍁

#### Completion fixes & enhancements 💇🏼

In `v1.2.0`, we introduced a new model for completions. Thanks to everyone for trying it, giving feedback, and providing numerous fixes! Continue to work with the new model as the old one (as noted in code comments) will be deprecated in a coming release.

-   `DisableFlagParsing` now triggers custom completions for flag names [#&#8203;1161](https://togithub.com/spf13/cobra/issues/1161)
-   Fixed unbound variables in bash completions causing edge case errors [#&#8203;1321](https://togithub.com/spf13/cobra/issues/1321)
-   `help` completion formatting improvements & fixes [#&#8203;1444](https://togithub.com/spf13/cobra/issues/1444)
-   All completions now follow the `help` example: short desc are now capitalized and removes extra spacing from long description [#&#8203;1455](https://togithub.com/spf13/cobra/issues/1455)
-   Typo fixes in bash & zsh completions [#&#8203;1459](https://togithub.com/spf13/cobra/issues/1459)
-   Fixed mixed tab/spaces indentation in completion scripts. Now just 4 spaces [#&#8203;1473](https://togithub.com/spf13/cobra/issues/1473)
-   Support for different bash completion options. Bash completions v2 supports descriptions and requires descriptions to be removed for `menu-complete`, `menu-complete-backward` and `insert-completions`. These descriptions are now purposefully removed in support of this model. [#&#8203;1509](https://togithub.com/spf13/cobra/issues/1509)
-   Fix for invalid shell completions when using `~/.cobra.yaml`. Log message `Using config file: ~/.cobra.yaml` now printed to stderr [#&#8203;1510](https://togithub.com/spf13/cobra/issues/1510)
-   Removes unnecessary trailing spaces from completion command descriptions [#&#8203;1520](https://togithub.com/spf13/cobra/issues/1520)
-   Option to hide default `completion` command [#&#8203;1541](https://togithub.com/spf13/cobra/issues/1541)
-   Remove `__complete` command for programs without subcommands [#&#8203;1563](https://togithub.com/spf13/cobra/issues/1563)

#### Generator changes ⚙️

Thanks to [@&#8203;spf13](https://togithub.com/spf13) for providing a number of changes to the Cobra generator tool, streamlining it for new users!

-   The Cobra generator now *won't* automatically include Viper and cleans up a number of unused imports when not using Viper.
-   The Cobra generator's default license is now `none`
-   The Cobra generator now works with Go modules
-   Documentation to reflect these changes

#### New Features ⭐

-   License can be specified by their SPDX identifiers [#&#8203;1159](https://togithub.com/spf13/cobra/issues/1159)
-   `MatchAll` allows combining several PositionalArgs to work in concert. This now allows for enabling composing `PositionalArgs` [#&#8203;896](https://togithub.com/spf13/cobra/issues/896)

#### Bug Fixes 🐛

-   Fixed multiple error message from cobra `init` boilerplates [#&#8203;1463](https://togithub.com/spf13/cobra/issues/1463) [#&#8203;1552](https://togithub.com/spf13/cobra/issues/1552) [#&#8203;1557](https://togithub.com/spf13/cobra/issues/1557)

#### Testing 👀

-   Now testing golang 1.16.x and 1.17.x in CI [#&#8203;1425](https://togithub.com/spf13/cobra/issues/1425)
-   Fix for running diff test to ignore CR for windows [#&#8203;949](https://togithub.com/spf13/cobra/issues/949)
-   Added helper functions and reduced code reproduction in `args_test` [#&#8203;1426](https://togithub.com/spf13/cobra/issues/1426)
-   Now using official `golangci-lint` github action [#&#8203;1477](https://togithub.com/spf13/cobra/issues/1477)

#### Security 🔏

-   Added GitHub dependabot [#&#8203;1427](https://togithub.com/spf13/cobra/issues/1427)
-   Now using Viper `v1.10.0`
    -   There is a known CVE in an *indirect* dependency from `viper`: [https://github.com/spf13/cobra/issues/1538](https://togithub.com/spf13/cobra/issues/1538). This will be patched in a future release

#### Documentation 📝

-   Multiple projects added to the `projects_using_cobra.md` file: [#&#8203;1377](https://togithub.com/spf13/cobra/issues/1377) [#&#8203;1501](https://togithub.com/spf13/cobra/issues/1501) [#&#8203;1454](https://togithub.com/spf13/cobra/issues/1454)
-   Removed ToC from main readme file as it is now automagically displayed by GitHub [#&#8203;1429](https://togithub.com/spf13/cobra/issues/1429)
-   Documentation correct for when the `--author` flag is specified [#&#8203;1009](https://togithub.com/spf13/cobra/issues/1009)
-   `shell_completions.md` has an easier to use snippet for copying and pasting shell completions [#&#8203;1372](https://togithub.com/spf13/cobra/issues/1372)

#### Other 💭

-   Bump version of  `cpuguy83/go-md2man` to v2.0.1 [#&#8203;1460](https://togithub.com/spf13/cobra/issues/1460)
-   Removed `lesser` typo from the GPL-2.0 license [#&#8203;880](https://togithub.com/spf13/cobra/issues/880)
-   Fixed spelling errors [#&#8203;1514](https://togithub.com/spf13/cobra/issues/1514)

*Thank you to all our amazing contributors* ⭐🐍🚀

</details>

---

### Configuration

📅 **Schedule**: At any time (no schedule defined).

🚦 **Automerge**: Disabled by config. Please merge this manually once you are satisfied.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

 - [ ] <!-- rebase-check -->If you want to rebase/retry this PR, click this checkbox.

---

This PR has been generated by [WhiteSource Renovate](https://renovate.whitesourcesoftware.com). View repository job log [here](https://app.renovatebot.com/dashboard#github/GoogleCloudPlatform/alloydb-auth-proxy).

---
## [OxygenCobalt/Auxio](https://github.com/OxygenCobalt/Auxio)@[c6d7d8fe39...](https://github.com/OxygenCobalt/Auxio/commit/c6d7d8fe39ae0f84051482961c3d2ad5ae64137a)
#### Friday 2022-06-03 16:44:41 by OxygenCobalt

playback: implement "safe" slider wrapper

Implement a safe slider wrapper that does not crash with invalid values
as often.

Slider is a terrible component that is not designed with Auxio's
use-case in the slightest. Instead of gracefully degrading with invalid
values, it just crashes the entire app, which is horrible for UX.

Since SeekBar is a useless buggy version-specific sh******ed mess too,
we have no choice but to wrap Slider in a safe view layout that
hopefully hacks with the input enough to not crash the app when doing
simple seeking actions.

I hate android so much.

Resolves #140.

---
## [ShiftLeftSecurity/overflowdb](https://github.com/ShiftLeftSecurity/overflowdb)@[989a3f2631...](https://github.com/ShiftLeftSecurity/overflowdb/commit/989a3f26313c98787ca4da3d080f87ced6f0e4be)
#### Friday 2022-06-03 16:48:01 by Bernhard

fuck you package private interaction java <-> scala

---
## [avar/git](https://github.com/avar/git)@[dd27bbdf48...](https://github.com/avar/git/commit/dd27bbdf4853761f185f8102f2b1e4b6bf5a3e01)
#### Friday 2022-06-03 16:52:13 by Ævar Arnfjörð Bjarmason

strbuf.c: use st_add3(), not unsigned_add_overflows()

Change the strbuf_grow() function to use st_add3() instead of doing
its own unsigned_add_overflows() checks.  The overflow checking here
was originally added in b449f4cfc97 (Rework strbuf API and semantics.,
2007-09-06) and adjusted in 1368f65002b (compat: helper for detecting
unsigned overflow, 2010-10-10). Instead we compute a "sz" with
st_add3().

That was done at a time when the underlying xrealloc() in
git-compat-util.h didn't use st_mult() yet, that has been the case
since the later e7792a74bcf (harden REALLOC_ARRAY and xcalloc against
size_t overflow, 2016-02-22).

The only behavior change here should be the very obscure edge case
that we'd previously die() in cases where we strictly didn't need to,
as we'd check both "extra + 1" and "sb->len + extra + 1" for
overflow. If we overflowed only on the latter but were doing the
former we'd needlessly die() die. I don't think that difference
mattered, but it's noted here for completeness.

While we're at it add an inline comment about why we're adding 1 to
the values, that's also explained in the API documentation in
strbuf.h, but since we're using that magic constant here...

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [betrusted-io/xous-core](https://github.com/betrusted-io/xous-core)@[6745206303...](https://github.com/betrusted-io/xous-core/commit/67452063034ea98c6fe318c67e7c7109806c5a60)
#### Friday 2022-06-03 17:08:29 by bunnie

mulling this pile of OpenSK code to see what we should cut, what we should keep

alright. the composite device problem is solved. The bigger issue I'm
mulling is if I should try to port the Google OpenSK FIDO2 stack into
Xous, or if I should just do a limited U2F implementation.

Poking around at the OpenSK stuff...porting looks possible, but, it's
going to be vendoring in all of the source from the OpenSK project. So
it'll be tough to apply patches if they happen; on the other hand, the
OpenSK implementation is FIDO2 certified, and the stable branch hasn't
moved since Nov 2021.

The main downsides of the OpenSK implementation are:

- it uses nightly. I think it can be stripped out, though; I haven't
  seen a "good reason" for it yet, it's mostly because Tock uses
  nightly. There's only one alarming use of it and it's in the crypto
  crates but those will be stripped out because....
- the crypto libraries are in fact not suitable for use. I dug into
  them and they definitely need to be gutted and replaced with the
  community-blessed crypto libraries and APIs. which is one big reason
  why once this goes into Xous land it doesn't go back easily into
  OpenSK land -- they actually have slightly different crypto
  APIs. more modern ones, to be fair, but, they haven't been reviewed.
- the implementation has "too many features"...for example, I don't
  think we'll ever realistically do authenticator attestation as it
  requires signing NDAs and provisioning secret keys that we can't
  share with users. But that code is there, and we'll either have to
  gut or bodge it.

The plusses are:

- it's FIDO2 certified. So, at least the protocol stack is probably
  complete and fully implemented, which means for features we don't
  use today I can just leave hooks or dummy values there for a fast
  migration path.
- Looks like they aren't changing things too fast in the dev
  branch...so this probably is not like riding a greased pig
- Looks like a couple of paid professionals wrote the code...better
  than what we have going on here
- I think I see a path to carve out their "persistent store" and glom
  it into the PDDB; a path to adapt their crypto traits into
  Xous-native traits; and a path to connect their CTAP protocol engine
  to the Xous HID server. So it seems feasible. But they baked in some
  bad API assumptions deeply enough that they are one-way streets I
  think to get these ports done.

I'm going to sleep on this, but I'm leaning toward trying to pull in
the OpenSK code because even tho it is a bit painful it probably gets
a bigger feature scope and so far it looks like I wouldn't be changing
any protocol-level stuff for the port, I would just be monkeying
around with the internal storage, crypto, and USB implementations, so
ideally the end result is we get a certified FIDO2 protocol engine for
the effort.

I think the main concern I have going in this direction is I don't see
a way to do this and simultaneously be able to absorb upstream patches
into this vendored code, because their API assumptions are too
different. Any bug fixes or patches would have to be manually applied
and merged. But maybe that's not such a big deal...?

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e218fbb527...](https://github.com/mrakgr/The-Spiral-Language/commit/e218fbb5271e68c0bb208bf37d762017622b840c)
#### Friday 2022-06-03 17:09:32 by Marko Grdinić

"8:40am. I think I am too hungry for success. My skills aren't really up to par just yet. In an ideal world I'd just practice until I've grasped it.

I need more speed, and more capability. Doing the blankets was quite difficult. I am not happy how it went.

Their folds are too soft and rounded. The cloth brush is great, but not quite good enough. I do not even have a method of putting them into place properly. The cloth sim makes them hover.

8:45am. Compared to 2d,. 3d is great. I can work directly on the form in 3d space. In 2d I'd have to guess on everything.

I really do want to get better at 2d, but not simply by mucking about.

I think at my current level I'd be good enough to do something like draw my own hand. Once I learned sketching it really flicked a switch in my mind and made me feel like I could do anything, but that is false of course. I need a more coherent system.

I am still weak when doing perspective. Using the 1-3 point perspective compared to 3d is simply laughable. Isn't there a better way to do this?

9am. Probably not, whenever I Google it, I just get the old horizon line stuff. You'd imagine there would be more to teach about drawing 2d in perspective than that. Maybe I should ask in /ic/?

The /beg/ thread recommends Perspective Made Easy.

https://www.amazon.com/Perspective-Made-Easy-Dover-Instruction/dp/0486404730

Let me see if I can get this off libgen. Yep, there it is. Let me take just a short break here and I will do the curtains. I want to get this scene done so I can move on to the next thing.

9:15am. Let me get started. Let's just get this out of the way.

9:20am. Change of plans. I am going to do just a single curtain. My own room has two, but it would be pain in the ass to fit them all into the hops.

9:40am. Change of plans again. Instead of the cloth sims, let me sculpt it. Maybe I simply havent put in enough vertices in between, who knows, but it is not bending correctly. At this rate, I am going to have spend hours fiddling with the cloth sim. Let me just shortcut that. It is things like this why I am interested in drawing. Let me just get this out of the way and then I will reconsider my path.

10:10am. Let me just go with this. Unless it is hard surface stuff, I can never really attain full satisfaction with 3d. I've had to use the inflate brush to give the curtains volume, but I think that will lead to self intersection problem. Still, it doesn't matter if a non solid curtain is self intersecting.

It is annoying. This kind of issue should be taken care of by the tools. It is just very difficult to create a curtain otherwise.

~* Crease on the beds and the pillows~
~* Put in the blankets and the clothing~
~* Do the curtains~
* Put in the glass door panes and (optionally) frost it a bit via the roughness setting
* Put in the flats for every object in the room

Let me check the curtains off.

Now come the glass door panes.

Actually I might have had it on all this time by accident.

Ah, no it was disabled in renders as well. Good.

...I already have the roughness set from when I played with it in Eevee. Good. This is no problem.

Let me just make the curtain a translucent dark green.

Ah crap. Now that applied the subdiv mod, the curtain became detached from the hops. It igoing to be a pain to put it back. Ghhhh.

10:25am. Proportional editing saved my ass here. Let me move on. The mistake I made is not that I used subdiv. The mistake was to not even think of how the curtain would be influenced. Thankfully in this case, I'd make the same choice even if I had anticipated this.

~* Crease on the beds and the pillows~
~* Put in the blankets and the clothing~
~* Do the curtains~
~* Put in the glass door panes and (optionally) frost it a bit via the roughness setting~
* Put in the flats for every object in the room

I'll leave flats for a bit later. Let me try rendering this. I want to see if the curtains are properly translucent and whether the glass panes work.

10:35am. Let me try rendering again. I want to try excluding the door panes because the don't seem to be adding much to the scene, except making it more noisy.

10:45am. No forget transmissive materials. They get rid of those light rays on the walls which makes things worse. Reality > Luxcore.

I'll exclude the glass panes from the view layer. Now, let me let it render for a while. Something like an hour would be good. I can read the perspective book during that time. Let me recompute the optimal clamping value, I'll have to turn it off for a bit.

This is strange. The suggested value is ridiculously low. Previously it was 60, but now it is ...0.00001 something.

Let me see what happens when I set it to that. I bet the suggested value is wrong and I'll get a dark screen.

Forget this trash suggestion. Let me instead set it to something like 1.

Hmmm, this is nice. The fireflies are gone entirely. But the main ray is a bit weak. Let me set clamping to 4.

11am. I can go a bit further. Let me set it to 6.

Now what do I do? Should I leave it to render for a while? Rather than make glass panes transmissive, how about I make them translucent instead?

11:10am. I guess I'll let it run for an hour and hope it does not crash the system. Let me read the perspective book. Maybe it will give me some inspiration when it comes to drawing. The very first remark is that man made things being square helps a lot. That is true, but I want to go beyond that.

11:20am. The render looks quite nice after 10m of work. Unfortunately then it crashes the whole system. I think it is using too much memory. The GTX even though it has 4gb, uses the last 500mb of the main DRAM. I really hate NVidia for doing that. Just like VRay I think this is causing the system to become overwhelmed.

11:25am. The problem should be the graphics driver. Even if the screen becomes completely unresponsive I think it is grinding away at it in the blackground.

I could try lowering the number of CPU threads to maybe 3. The will leave the system with a single core free.

11:30am. Let me try that. I am going to set the time to 20m. I'll also set the file output in the compositor and let it run to completion before resetting.

11:35am. Not letting it have 4 full threads make the system smoother. I can actually write in this journal now. Maybe it won't crash.

11:35am. Let me have breakfast early today.

11:55am. It finished safely this time. Let me let it run for an hour. Lowering the thread count to 3 was really enough to stabilize it.

12:15pm. It crashed. And that happened exactly when I opened the render. Forget rending for an hour. I do not have the patience to wait for that. If I really wanted to get the rendering done, I should use a cloud service. 20m is roughly my limit. Let make the posts in the /wip/ thread and on Twitter and then I'll move on to the last step which is adding in flats.

Maybe once I am totally done I'll let it run for a couple of hours over the night.

12:30pm. It looks interesting, but I feel the stylization is too heavy. Still, if I went for such strong stylization such as this I would not need to model is much detail. Also I see there is a preserve color option in the settings. Let me try it again with a different style, but lower style strength.

12:35pm. I'll just lower the style scale.

...Nope. Let me trying the weight. At this point I'll have only 15 energy left. It recovers at a rate of 3h.

At 30% strength it looks much better.

12:40pm. One more time. I'll pick a different style.

12:45pm. I guess I'll spend it all. One more time.

12:55pm. https://deepdreamgenerator.com/ddream/ff0yma1dt96

I'll go with this. Let me do a little post in /wip/. After that I'll focus on the flats.

1:40pm. Done with breakfast. I feel distracted. I am thinking what I should do. I should import the monitor into the scene. Let me do it.

Good, that will allow me to consolidate the model. Now let me start putting in flats.

3:10pm. It's good enough. I am not going to spend my time texturing like I intended it to months ago. It would be too time consuming. I do not have a clear vision of what appealing colors should be like anyway.

What I should do now is let it run for a while.

3:15pm. Let me just do it. As long as I do not look at the render while it is running, maybe I'll manage to let it run to the conclussion. While that is running in the background, maybe I'll read the Legendary Mechanic or the perspective book.

Let me just do it. Run, run!

3:25pm. I've gone back to 4 threads. 80 minutes. That means it will be done at about 4:40pm. I have to resist the urge to check the render otherwise it will crash.

...It actually crashed as soon as I finished that last sentence. No way can it last through 1h. Let me run it for 10m.

3:45pm. It crashed again. And it seems letting it run in the background for good. When the screen freezes it really takes out the entire system. Fuck Luxcore.

I have no choice but to run it again. My GPU is the culprit for this as well as the renderer. Adding more shaders might have made it more unstable as well. Let me reduce the thread count to 3. I'll run it a few times until I get a sense. This time forget reading in the background. I'll wait out the 20m until it finishes rendering.

4:05pm. This is torture. Now that I've added the flats, the whole scene is stupidly dark. To make things work Luxcore was not using the Cycles settings and is making me run around like a chicken.

Sigh what the hell. I am going to learn my lesson from this and not mess with material in the future. Let me distable and start turning things on by one.

4:10pm. Using the helper ended up nuking my light settings. Fuck.

4:20pm. This is torture. Now that I've added flats the scene is very dark.

Annoyingly, even increasing the light power by 64 does not seem to be doing anything to make the scene brighter.

...The reason for that being that Light Manager does not change the Luxcore intensities or exposures. Sigh.

4:40pm. Another crash. But it does look somewhat decent now. I am never going to do this again. I am going to leave PBRs behind after this.

Let me reduce the thread count to 3 like I said I would. This time I'll try to aim for 10m. Last time it did not hit 5m despite me leaving for the bathroom.

Actually, let me leave it for 4 threads, and I will disable that 3rd cache.

5pm. It worked. Maybe that third cache is what is causing the instability.

5:15pm. So far so good. The second render which I'll let run for 30m is already past the 10m mark. I've put one of the images through deep dream generator and the result is a bit better than last time.

...It crashed as soon as I opened an image in the web browser. A safe bet is that Luxcore is running out of memory. I am honestly amazed that this is the case.

10m is my limit of patience. I've wasted os much time today reseting the failed renders.

Enough, let me do a few posts. Let me also try the render with a different style.

5:40pm. https://deepdreamgenerator.com/ddream/is5aqmm9ump

///

My room modeled in Blender as viewed near the entrace. By itself adding flats to the objects in the scene was not a difficult task, but I am reaching the limit of my hardware and Luxcore is often crashing during rendering. After many tries, I barely managed to squeeze out 10m out of it this time. Adding darker colors to the objects made the room a lot darker so I had to ramp up the light power as well as increase the brightness of the colors. Well, at least now that is done with. I think the colors do make the scene a bit nicer, don't you agree?

The 3d scene as is rendered directly looks fairly plastic, but looking at the style transferred result you'd never guess it was 3d. NNs are no doubt a game changer for artistic expression.

The style transfer acts both as a denoiser and detail remover. A lot of the details I spent a lot of time of working on simply aren't visible in the resulting image and it is not due to the 0.6m resolution. I am still a novice at art and the lesson I'll take from this is to anticipate this and not work on what won't show up in the final result.

Since physical based rendering is so demanding, for my next piece I might want to try rendering with Eevee or Malt. Luxcore really killed me today.

///

5:55pm. This was a lot more strenuous that I'd care to admit. The buttefly style is quite beautiful. I'll post this on my Twitter.

6:10pm. The lesson from all of this is definitely - forget details, but take great care of the lighting. I spent so much time modeling what won't even be visible in the final scene. I definitely do not regret putting in the grill lights as they look great. Eevee wouldn't be able to handle this. So I guess that leave Malt as the renderer of choice.

I really do like style transfer. It makes painterly 3d quite viable. I should try some anime images from Fuzichoco and see what comes out. Right now I've spent the alloted energy on the generator site. I should look if I could download some pretrained nets from the wild and give them a try. I should do some research on what model Deep Dream Generator is using. No doubt there is a paper on this out there somewhere.

This could be a viable ML project for me for once. I could definitely get some use out of these kinds of nets.

I owe an apology to the ML community. In case anybody from it is reading, I am sorry for call you guys useless morons. You did come up with something good after all.

6:20pm. The effect these nets have on me is different from what they would have to an average person pushing in photos. With 3d they are exactly where they would be the most effective.

6:30pm. I am actually getting a bit excited thinking about it. Now that I have the experience of finishing this proejct and actually understand how good NN style transfer really is, that opens a path for a completely different and effective workflow compared to the regular one.

Since now I understand for whom I am modeling for - the NNs, I'll be able to do it a lot more efficiently on my next scene. These nets will force me to pick shapes and colors so as to maximize the effectiveness of the final image. I did a lot of small details and intricate texturing in the past two months that will never see the light of day.

It is excusable. I was doing it for the first time, so I had to do it in order to learn it. But just because I know how to do something does not mean I have to use it.

6:45pm. It was strenuous, but I did manage to finish the project this time around. I am thinking the next one should be cover for Heaven's Key, but I'll really want to do some research on pretrained image models suitable for style transfer. Even my GTX 970 should be able to run them directly. The NNs themselves aren't too large. I will have to do some studying even if I get them. I do not understand what style strength is supposed to be exactly. The same goes for the other options.

6:55pm. I am starting to feel just a little bit of confidence. This is how I wanted my RL journey to look like. A lot of effort followed by a breakthrough. Doing rough modeling is just about the amount of effort I wanted to put in. I certainly do not want to be spending all day painstakingly rendering by hand. Nor do I want to be working on the details or texturing.

If NNs are this good now at style transfer, they will only get better in the future. With this path I have something of value, and it can only get better. But if it does not, that is fine too. It will never get worse.

7pm. TOmorrow I will pause art for a bit to do some ML research. I never thought I would be getting back into it.

I think right now thanks to style transfer, I am 3/5 in art. Or at least I will be once I get my own net that can do this. So that is what I should focus on."

---
## [TrashDoxx/TG](https://github.com/TrashDoxx/TG)@[92fda5014d...](https://github.com/TrashDoxx/TG/commit/92fda5014dbc8ba64c19848e693c179af35da2ac)
#### Friday 2022-06-03 17:11:45 by san7890

Makes Hell Microwaves Not Use Power (#67413)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

---
## [Dio-Sama/Galactica-13](https://github.com/Dio-Sama/Galactica-13)@[5eddabc15b...](https://github.com/Dio-Sama/Galactica-13/commit/5eddabc15b72b1280b7ec89054f87e2ae65d43a6)
#### Friday 2022-06-03 17:36:42 by Dio-Sama

Map edits.

Further adjusts map, further fixes fucked up shit! haha!

---
## [caido/diesel](https://github.com/caido/diesel)@[448df6b615...](https://github.com/caido/diesel/commit/448df6b61566dbd419554fc82abd018357848846)
#### Friday 2022-06-03 17:53:19 by Georg Semmler

Address #3173

This is a tricky one. It seems like the behaviour described in that
issue should work out of the box, but it doesn't. I've spend some time
to investigate various solutions to make this work, but I came to the
conclusion that the current behaviour is the correct one.

The underlying issue here is that such an query promotes the inner
`Nullable<_>` of the field onto the outer `Queryable` wrapper. Without
`Selectable` that would require a select clause like
`.select((table::column.assume_not_null(),).nullable())`. This is
technically a safe pattern, but requires the usage of the "advanced"
`assume_not_null()` method to forcibly convert types to their not null representation.

Possible solutions tried to make the enable constructs shown in that
issue:

* I've tried to make the `impl Selectable for Option<T>` return the
following `SelectExpression`:
`dsl::Nullable<dsl::AssumeNotNull<T::SelectExpression>>`
where `AssumeNotNull` converts each tuple element to the corresponding
not nullable expression, while `Nullable` wraps the tuple itself into a
nullable type wrapper.
* I've tried to apply a similar approach like that one above, but only
for derived impls by manipulating the generated code for a optional
field with `#[diesel(embed)]`

Both solutions require changes to our sql type system, as for example
allowing to load a non nullable value into a `Option<T>` to enable their
usage in a more general scope as the presented example case.
(See the added test cases for this). That by itself would be fine in my
opinion, as this is always a safe operation. Unfortunately the
`AssumeNotNull` transformation would be applied recursively for all
sub-tuples, which in turn would cause trouble with nested joins (again
see the examples). We would be able to workaround this issue by allowing
the `FromSql<ST, DB> for Option<T>` impl for non-nullable types to catch
null values, which in turn really feels like a bad hack. (You would like
to get an error there instead, but nested nullable information are
gone.)
All in all this lead me to the conclusion that the current behaviour is
correct.

This PR adds a few additional tests (an adjusted version of the test
from the bug report + more tests around nested joins) and does move
around some code bits that I noticed while working on this.

I think the official answer for the bug report would be: Either wrap the
inner type also in an `Option` or provide a manual `Selectable` impl
that does the "right" thing there.

---
## [cmloegcmluin/otherRTT](https://github.com/cmloegcmluin/otherRTT)@[fe8f174bb9...](https://github.com/cmloegcmluin/otherRTT/commit/fe8f174bb9ff77743b5125818a7caeea6e25c10f)
#### Friday 2022-06-03 18:18:38 by Douglas Blumeyer

i hate my life, entire morning lost, plus part of last night, just so I could freaking see the correlations between constraint matrices, tunings, and targeted interval damages lists... I really loathe this malformed real error

---
## [santacrab2/3DS-PokeAutoBot](https://github.com/santacrab2/3DS-PokeAutoBot)@[24aa618672...](https://github.com/santacrab2/3DS-PokeAutoBot/commit/24aa618672289c000e888b0f5b918e248871a168)
#### Friday 2022-06-03 18:59:19 by santacrab2

still adding hackers to the list, holy hell people suck

---
## [Nyhilo/TTS-Taikyoku-Shogi-Movement-Guides](https://github.com/Nyhilo/TTS-Taikyoku-Shogi-Movement-Guides)@[36ff047ba2...](https://github.com/Nyhilo/TTS-Taikyoku-Shogi-Movement-Guides/commit/36ff047ba2cc85b0d1e0bb6ea1049fbf6e813858)
#### Friday 2022-06-03 19:06:06 by Nyhilo

Implement the pieces with queen-like movement and simple jumps

Horned Falcon, Soaring Eagle, Roaring Dog, Lion-Dog, Great Dream-Eater, Spirit Turtle, Treasure Turtle, and the Free Eagle

Note for future me that we skipped the Heavenly Horse in this commit and need to start from there on the wikipedia

---
## [5vl/RedditVideoMakerBot](https://github.com/5vl/RedditVideoMakerBot)@[cdb6f85d98...](https://github.com/5vl/RedditVideoMakerBot/commit/cdb6f85d98c7f3b342d0730428020c154828c884)
#### Friday 2022-06-03 20:39:46 by 5vl

Added pyttsx3 instead of gTTS, now has a male voice.

You can probably do more with this than me - I'm new to python. I just preferred a male voice over the old (annoying) female voice!

---
## [ft/ufw](https://github.com/ft/ufw)@[8796e9a9dc...](https://github.com/ft/ufw/commit/8796e9a9dce006fd2a6bf7a65e3477dd470e23e9)
#### Friday 2022-06-03 20:50:18 by Frank Terbeck

cmake: Remove lots of recursive-cmake cruft

This code was pretty bad. Even for CMake standards.

Previously we've tried to use as little external tooling as possible, and get
by doing everything in a build and code-structure with just git and CMake. Most
things were implementable, thanks to calling CMake recursively and its weird
and wonderful ExternalProject module.

But user friendliness has suffered. A lot. It was very hard to trigger specific
builds. I actually wanted to fix this by somehow making CMake generate a list
of registered build-variants, so I could maybe at least get some sort of shell
completion to pick up on that. But it's all a horrible shitshow.

And the downsides aren't just that. From mmh's ROADMAP:

        This has  several downsides:  The CMakeLists.txt  file becomes
        tough to follow because the  same file gets parsed in multiple
        ways by multiple CMake processes.  The build tree becomes com-
        plex and quite deep so the top-level CMake call can keep track
        of what is happening. This  is rather unergonomic for the user
        to decent into. And finally, it becomes tough to perform para-
        llel build  correctly. If you  use Ninja, for instance  an run
        your top-level ninja in parallel mode, the recursive calls may
        also be  parallel,  which — in complex builds — can  massively
        overload your system.

Combined with the atrocious code quality it's a clear candidate for some-
thing to get rid of. That's where mmh's proposed ‘system’ sub-command comes
into play. The delarative API of our old scheme of specifying the kind of
builds that we'd like to have carried out makes it pretty easy to map this
to a scheme using an external tool that reads such a specification from,
say, a YAML file.

And that is the idea behind that ‘system’ sub-command. The accompanying
branch in the makemehappy space is ‘ft/system-subcmd’.

Note that this is probably not everything that needs to be weeded out. But
you got to start somewhere.

Signed-off-by: Frank Terbeck <ft@bewatermyfriend.org>

---
## [Tk420634/sunset-wasteland](https://github.com/Tk420634/sunset-wasteland)@[92f8f5d159...](https://github.com/Tk420634/sunset-wasteland/commit/92f8f5d159c8770e6927f38c6aa6622161af29bc)
#### Friday 2022-06-03 20:57:31 by Tk420634

Updated *insult list

Removed
-vore
-gaylord
-shitcurity
-comdom
-greytider
-tator
-lingbin
-cluwn
-monkey

Modified or fixed
-Cheesemonger spelling
-Knight-like from Captain-like
-Comdom to dummy

Added
-Bramin-sniffer
-Raider
-scum-sucker
-mutie
-headass
-dumbass
-ghoul
-Kitten looking ass, added with Kit8bits permission

Now get your @pick(nouns_body) off my lawn.

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[a5d6f78d33...](https://github.com/Perkedel/Kaded-fnf-mods/commit/a5d6f78d332c52aa3e577f1fec8bf17a554e8111)
#### Friday 2022-06-03 21:42:55 by Joel Robert Justiawan

[skip ci] mak dono

idk ma dono

let's install Sky again. at this point, we are lost. no idea, KitsuneSkulls too?! really. Okay, don't blame Micheal (formerly bfswifeforever), he only know that KitsuneSkulls is close friend. and yeah.

We wish Rodrigo got it. idk.. what do you think?

what else do we got here?

---
## [nicerapp/nicerapp](https://github.com/nicerapp/nicerapp)@[5a81eebb7f...](https://github.com/nicerapp/nicerapp/commit/5a81eebb7ff847bf8308163199a7a3f960dee7b5)
#### Friday 2022-06-03 22:45:34 by Rene AJM Veerman

TO ALL GODS, ANGELS, SPIRITS AND Demons, plus ALL moderators and spyware builders and rootkit builders world-wide : FULL DISCLOSE OF MY SOCIAL MEDIA HACKING SKILLS, FULL DISCLOSE OF MY CURRENT PHP7 SELF-DEFENSE TECHNOLOGICAL CAPABILITIES. And much more to come tonight (the sleeping pill was Cancelled by the Christian God and my own beautiful lovely wife, Emma Veerman-Artistia, a true flying invisible Angelic Woman.

---
## [zclconf/go-cty](https://github.com/zclconf/go-cty)@[97bafac0de...](https://github.com/zclconf/go-cty/commit/97bafac0dea33a3f74db88ab54dea2937b9e8aef)
#### Friday 2022-06-03 23:15:07 by Martin Atkins

Remove all of the encoding/gob support code

I originally introduced all of this here as a concession to trying to
HashiCorp trying to get cty values to round-trip through the various
very magical gob-based wire interfaces in Terraform v0.11 and earlier,
back when they thought cty and what became "HCL 2" would just be a drop-in
replacement for HCL 1 and the various different competing representations
of dynamic values.

However, in practice none of that ever actually worked out and instead
Terraform now natively uses cty JSON/msgpack and other such mechanisms for
its wire protocols, making this gob handling code redundant.

This stuff caused various maintenance headaches and panic bugs which make
them a burden to retain. Although this is technically a breaking change
to the public cty API, in practice this stuff was only here to allow
Terraform to use it _indirectly_ as a side-effect of passing values into
the encoding/gob package, and so I'm treating it as if it had been an
internal implementation detail even though in principle it could've been
depended on externally. If anyone was doing that, I'm sorry; I suggest
copying the relevant support code into your own package instead if you
wish to continue using cty with gob.

---
## [AtilioA/AlertaDoTesouro](https://github.com/AtilioA/AlertaDoTesouro)@[e508315b0a...](https://github.com/AtilioA/AlertaDoTesouro/commit/e508315b0ad04d76eb45ddf9cc11b5a9db22c454)
#### Friday 2022-06-03 23:15:12 by Henriquelay

style(web): Format routes

Sorry, pre-commit for eslint with multiple projects is kinda shit so it's disabled

---

