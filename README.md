## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-07](docs/good-messages/2022/2022-06-07.md)


1,769,212 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,769,212 were push events containing 2,834,716 commit messages that amount to 221,439,201 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 32 messages:


## [msbutler/cockroach](https://github.com/msbutler/cockroach)@[f782e45fd0...](https://github.com/msbutler/cockroach/commit/f782e45fd0da015396bc758e855535a951f2e21a)
#### Tuesday 2022-06-07 00:03:22 by Andrei Matei

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
## [kernelci/linux](https://github.com/kernelci/linux)@[b9364eed92...](https://github.com/kernelci/linux/commit/b9364eed9232f3d2a846f68c2307eb25c93cc2d0)
#### Tuesday 2022-06-07 00:06:06 by Douglas Anderson

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[4cd55f43ff...](https://github.com/treckstar/yolo-octo-hipster/commit/4cd55f43ff7c934a7022e3e594d98b570154d9e3)
#### Tuesday 2022-06-07 00:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [optimumtact/tg-station](https://github.com/optimumtact/tg-station)@[0877c2f6bd...](https://github.com/optimumtact/tg-station/commit/0877c2f6bd2f151c2646f8faf08afb97f3f387cb)
#### Tuesday 2022-06-07 00:37:52 by oranges

You know what, just fuck you in particular in total

---
## [dreamingskey/dreamingskey](https://github.com/dreamingskey/dreamingskey)@[17a42ea000...](https://github.com/dreamingskey/dreamingskey/commit/17a42ea00088a7e32aae8bbd01271d3f49565012)
#### Tuesday 2022-06-07 00:56:55 by Christopher Vincent

A poem

The variables of the factors of what is coming me We can be silent still we can move in flows of what it takes to of in our skin you cant write in her we are brought  not somany know of u but shortlimes well spent and only life can you know this only the warmth of one lived in know a little of yourself on the journey we go as we are I. The worlds untold and so .any could see I've wanted a d  pleaded to give this away so one one day could say helped somebody like me  knowing pain knowin more.of what it is to knowing it took to come with the formula of whats.now see through the tasks  what's going on up there I wounder. They copy my callings and copied my life to you and you hearived we love in our memories of t this in all the change to what it took to I'm blessed in this this. And if you know of this a d teapot all to throw what I am the in what is seen and you see now cause
 
I can change it up just as quick and take any direction I please I'm not a step ahead I'm right here

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[92fda5014d...](https://github.com/timothymtorres/tgstation/commit/92fda5014dbc8ba64c19848e693c179af35da2ac)
#### Tuesday 2022-06-07 01:01:26 by san7890

Makes Hell Microwaves Not Use Power (#67413)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

---
## [k6l2/korl](https://github.com/k6l2/korl)@[cd150d5ba5...](https://github.com/k6l2/korl/commit/cd150d5ba528bfc5f8909b9ec41e2e909684ac13)
#### Tuesday 2022-06-07 01:01:33 by Kyle

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
## [RigglePrime/tgstation](https://github.com/RigglePrime/tgstation)@[fff23b734a...](https://github.com/RigglePrime/tgstation/commit/fff23b734a7c4786f3320124afb28b8e2d27f64d)
#### Tuesday 2022-06-07 02:18:37 by py01

Mass purrbation affects mutant species (#46779)

* mass purrbation affects all species

* mass purrbation code cleanup

* remove mass purrbation gives mutant species their special ears and tails back

* mass purrbation syntax fix

* remove mass purrbation does not remove felinid from original felinids

* fuck you travis

I had to include this one
 - Riggle

---
## [R3-Rex/rpm-rex](https://github.com/R3-Rex/rpm-rex)@[0774e76e19...](https://github.com/R3-Rex/rpm-rex/commit/0774e76e1902a30502e69cbc14963c1eaa8954d7)
#### Tuesday 2022-06-07 06:01:00 by RexGameStudio

Now it doesent fuck you in the add unless you fuckoff far

---
## [PKRoma/git](https://github.com/PKRoma/git)@[c472db5059...](https://github.com/PKRoma/git/commit/c472db50594861829b2ee8ba38e98cbe60432022)
#### Tuesday 2022-06-07 06:19:34 by Ævar Arnfjörð Bjarmason

object-file.c: do fsync() and close() before post-write die()

Change write_loose_object() to do an fsync() and close() before the
oideq() sanity check at the end. This change re-joins code that was
split up by the die() sanity check added in 748af44c63e (sha1_file: be
paranoid when creating loose objects, 2010-02-21).

I don't think that this change matters in itself, if we called die()
it was possible that our data wouldn't fully make it to disk, but in
any case we were writing data that we'd consider corrupted. It's
possible that a subsequent "git fsck" will be less confused now.

The real reason to make this change is that in a subsequent commit
we'll split this code in write_loose_object() into a utility function,
all its callers will want the preceding sanity checks, but not the
"oideq" check. By moving the close_loose_object() earlier it'll be
easier to reason about the introduction of the utility function.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [OpenImageIO/oiio](https://github.com/OpenImageIO/oiio)@[069f079eb5...](https://github.com/OpenImageIO/oiio/commit/069f079eb5dc0f6ef23b1d2afec8c6abd8ec2ebb)
#### Tuesday 2022-06-07 06:30:48 by Larry Gritz

Rename src/dds.imageio/squish/simd.h -> squish-simd.h (#3424)

This tiny change is a quality-of-life fix for me, addressing the fact
that there are two different simd.h files in our code base. I never
would have done that on purpose, but one of them is part of the
imported "squish" source code that we use for dds encoding.

For years I've been frustrated that reflexively typing `CMD-P simd.h`
in the editor has a 50/50 chance of pulling in this file, when in fact
there is literally a 100% chance of my wanting
src/include/OpenImageIO/simd.h.

So finally put my editing brain out of its misery by renaming the file
that I never want to edit.

---
## [olafhering/valgrind](https://github.com/olafhering/valgrind)@[6cc2d94d93...](https://github.com/olafhering/valgrind/commit/6cc2d94d93fa5350355b8cedb0d6b5309fcc588c)
#### Tuesday 2022-06-07 06:52:21 by Paul Floyd

Use a different way to tell where the syscall handler was interrupted on FreeBSD and macOS

I was using a global variable. This would be set to '1' just before
calling the function to save cflags and cleared just after, then
using the variable to fill in the 'outside_rnage_ condition
in VG_(fixup_guest_state_after_syscall_interrupted)

Even though I haven't experienced any isseus with that, the comments just before
do_syscall_for_client made me want to try an alternative.

This code is very ugly and won't please the language lawyers.
Functions aren't guaranteed to have an address and there is no
guarantee that the binary layout will reflect the source layout.
Sadly C doesn't have something like "sizeof(*function)" to give
the size of a function in bytes. The next best that I could
manage was to use dummy 'marker' functions just after the
ones I want the end address of and then use the address of
'marker - 1'

I did think of one other way to do this. That would be to
generate a C file containing the function sizes. This would
require

1. "put_flag_size.c" would depend on the VEX guest_(x86|amd64)_helpers
   object files
2. Extract the sizes, for instance

echo -n "const size_t x86_put_eflag_c_size = 0x" > put_flag_size.c
nm -F sysv libvex_x86_freebsd_a-guest_x86_helpers.o | awk -F\| '/LibVEX_GuestX86_put_eflag_c/{print $5}' >> put_flag_size.c
echo ";" >> put_flag_size.c

That seems fairly difficult to do in automake and I'm not sure if
it would be robust.

---
## [philip-stoev/materialize](https://github.com/philip-stoev/materialize)@[3bc0574297...](https://github.com/philip-stoev/materialize/commit/3bc057429749d105bd462595fc3512554be9832f)
#### Tuesday 2022-06-07 07:03:32 by Daniel Harrison

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
## [pipe-cd/pipecd](https://github.com/pipe-cd/pipecd)@[2480da0f07...](https://github.com/pipe-cd/pipecd/commit/2480da0f07a053c05d0491a6cf1ae2b367dc8605)
#### Tuesday 2022-06-07 09:12:03 by knanao

Fix the wrong way to cancel the context (#3540)

**What this PR does / why we need it**:
I'm sorry for my making a stupid but serious mistake with my carelessness.

**Which issue(s) this PR fixes**:

Fixes #

**Does this PR introduce a user-facing change?**:
<!--
If no, just write "NONE" in the release-note block below.
-->
```release-note
NONE
```

This PR was merged by Kapetanios.

---
## [Pandaaa2507/danser-go](https://github.com/Pandaaa2507/danser-go)@[e4091b4d2c...](https://github.com/Pandaaa2507/danser-go/commit/e4091b4d2c67add038b85c093ca7d2ac923b0164)
#### Tuesday 2022-06-07 09:38:27 by Sebastian Krajewski

Allow reading unicode settings.json files (fuck you WinBlows)

---
## [ZAB909/thewasteland](https://github.com/ZAB909/thewasteland)@[013fb2bd4b...](https://github.com/ZAB909/thewasteland/commit/013fb2bd4bd6ce216844c984da9dc5ffed316c61)
#### Tuesday 2022-06-07 09:57:26 by ishitbyabullet

Fallout Alien Content (#539)

* ncr veteran ranger removal

sorry, boys, but 18 yr old female veteran rangers aren't lore accurate.

* NCR no longer has farming or water

No one ever did the sharecropper farm quest in FNV anyways.

* NCR must actively pay taxes

There is a new need meter similar to thirst and hunger for this now.

---
## [shrinivaasanka/asfer-github-code](https://github.com/shrinivaasanka/asfer-github-code)@[05ded3c099...](https://github.com/shrinivaasanka/asfer-github-code/commit/05ded3c099fbc131e233e4479bba7cfb7abcd082)
#### Tuesday 2022-06-07 10:06:15 by Krishna iResearch - NeuronRain - K.Srinivasan

---------------------------------------------------------------------------------------------------------------------------------------------
1257. (THEORY and FEATURE) Medical Imageing and Music Information Retrieval (MIR) - fMRI imagery analysis for music-evoked autobiographical memories - 7 June 2022 - related to 228,385,410,587,588,548,656,868,1218,1223 and all sections on merit of large scale visuals, medical imageing, Evocation WordNet, ThoughtNet and Psychology of Evocation, Music search-Music discovery, Intrinsic Merit of Music, MIR(Music Information Retrieval), Music Similarity and Clustering, AI Music Synthesis, fMRI connectomes - OpenNeuro - Psychology of music, Weighted automata, Chaos, Deep Learning, Dynamic Time Warping-Timeseries analysis, Majority Voting Vs Intrinsic - Condorcet Jury Theorem variants
---------------------------------------------------------------------------------------------------------------------------------------------
1257.1 Function medical_imageing() in ImageGraph_Keras_Theano.py has been updated to include a clause for fMRI imagery sourced from various experimental study datasets on sensory stimuli affecting human brain, especially how an audio-visual stimulus evokes autobiographical memories of the past. With this support for ECG,MRI and fMRI medical imagery analysis have been added in NeuronRain.
1257.2 Distinguishing human enjoyable music from the rest is the cornerstone of fMRI research having far-reaching implications for music industry, music creativity or music search-music discovery if all 12-note music melody waveforms numbering 68 billion have been already found (from 1223.13). "Is the set of enjoyable music (majority voted, liked by lot) = quality music (naturally meritorious, not voted)" is another open problem in intrinsic merit of music and fits into the realm of Condorcet Jury Theorem variants for bounds on Correctness of Group Decision (Black-Ladha).
1257.3 In this update, an fMRI image for music stimulus (UCDavis dataset imagery - testlogs/medical_imageing/fMRI_MusicStimulus_UCDavis_janata_brain_lg.jpg) on human subjects (music genre of enjoyable-familiar nature evoking memories) has been analyzed by image_segmentation() and its Chain approximation contours,Voronoi-Delaunay Tessellation-Triangulation,Facegraph,Watershed segments are computed as below:
	(Logs) testlogs/ImageGraph_Keras_Theano.MedicalImageing.fMRI_MusicGenre.7June2022
	(fMRI image from 1257.6) testlogs/medical_imageing/fMRI_MusicStimulus_UCDavis_janata_brain_lg.jpg
	(facegraph DOT) testlogs/medical_imageing/fMRI_MusicStimulus_UCDavis_janata_brain_lg_ImageNet_Keras_Theano_Segmentation_FaceGraph.dot
	(Chain approximation contours) testlogs/medical_imageing/fMRI_MusicStimulus_UCDavis_janata_brain_lg_contoursegmented_7June2022.jpg
	(Voronoi-Delaunay) testlogs/medical_imageing/fMRI_MusicStimulus_UCDavis_janata_brain_lg_medical_imageing-contourlabelled.jpg
	(Watershed segmented) testlogs/medical_imageing/fMRI_MusicStimulus_UCDavis_janata_brain_lg_segmented.jpg
1257.4 Evocation of Memories expressed as texts have been earlier studied and implemented in NeuronRain by various gadgets - ThoughtNet Hypergraph Evocation,Contextual Multi Armed Bandits,Reinforcement Learning and Evocation WordNet - while audio-visual evocation is the best possible formulation of ThoughtNet evocation wherein thoughts are audio-visualized and stored in ThoughtNet Hypergraph hyperedges and hypervertices (Example in Section 387).
1257.5 If number of all possible music waveform melodies are upperbounded by 68 billion in 12-note scale, number of fMRI visuals of human brain for music sensory stimuli are upperbounded as well at 68 billion thereby narrowing down the size of fMRI dataset.

References:
-----------
1257.6 Study Finds Brain Hub That Links Music, Memory and Emotion - "... a golden oldie comes blaring over the radio and suddenly we’re transported back — to a memorable high-school dance, or to that perfect afternoon on the beach with friends. But what is it about music that can evoke such vivid memories? ... This fMRI brain scan shows areas that respond to familiar music (green), salient memories (red), and music that is perceived as enjoyable (blue). The yellow area, in the medial prefrontal cortex, is a response both to music familiarity and salient memory. ..." - https://www.ucdavis.edu/news/study-finds-brain-hub-links-music-memory-and-emotion
1257.7 The neural architecture of music-evoked autobiographical memories - [Petr Janata] - https://pubmed.ncbi.nlm.nih.gov/19240137/
1257.8 Forrest Gump Dataset - https://www.studyforrest.org/ - benchmark neuroscience sensory stimulus fMRI dataset based on movie Forrest Gump which has been set as a standard mix of emotional stimuli simulating reallife
1257.9 Music Earworm - https://en.wikipedia.org/wiki/Earworm - Sticky Music Syndrome
1257.10 Affect in Music - https://www.jstor.org/stable/428839 - emotion arising out of music stimulus
1257.11 Nakai, Koide-Majima, and Nishimoto (2021). Correspondence of categorical and feature-based representations of music in the human brain. Brain and Behavior - https://pubmed.ncbi.nlm.nih.gov/33164348/ , https://openneuro.org/datasets/ds003720/versions/1.0.0

---
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[0504c0a2b4...](https://github.com/norsvenska/tgstation/commit/0504c0a2b466d617efd4dcc77b092fcdbdad24be)
#### Tuesday 2022-06-07 10:19:04 by LemonInTheDark

Improper forced qdel cleanup,  some expanded del all verbs (#66595)

* Removes all supurfolus uses of QDEL_HINT_LETMELIVE

This define exists to allow abstract, sturucturally important things to
opt out of being qdeleted.
It does not exist to be a "Immune to everything" get out of jail free
card.
We have systems for this, and it's not appropriate here.

This change is inherently breaking, because things might be improperly
qdeling these things. Those issues will need to be resolved in future,
as they pop up

* Changes all needless uses of COMSIG_PARENT_PREQDELETED

It exists for things that want to block the qdel. If that's not you,
don't use it

* Adds force and hard del verbs, for chip and break glass cases
respectively

The harddel verb comes with two options before it's run, to let you
tailor it to your level of fucked

* Damn you nova

Adds proper parent returns instead of . = ..()

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

* Ensures immortality talismans cannot delete their human if something goes fuckey. Thanks ath/oro for pointing this out

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

---
## [Reinazhard/android_kernel_xiaomi_whyred](https://github.com/Reinazhard/android_kernel_xiaomi_whyred)@[e4c4453310...](https://github.com/Reinazhard/android_kernel_xiaomi_whyred/commit/e4c445331095acdc2f89f8aaa934fba2b6e73bdf)
#### Tuesday 2022-06-07 10:46:32 by Peter Zijlstra

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
Signed-off-by: Adam W. Willis <return.of.octobot@gmail.com>

---
## [NopemanMcHalt/sunset-wasteland](https://github.com/NopemanMcHalt/sunset-wasteland)@[92f8f5d159...](https://github.com/NopemanMcHalt/sunset-wasteland/commit/92f8f5d159c8770e6927f38c6aa6622161af29bc)
#### Tuesday 2022-06-07 11:22:45 by Tk420634

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
## [FantasticFwoosh/Merchant-Station-13](https://github.com/FantasticFwoosh/Merchant-Station-13)@[144b5838c0...](https://github.com/FantasticFwoosh/Merchant-Station-13/commit/144b5838c01985628a46954e276f5f643596634c)
#### Tuesday 2022-06-07 12:11:39 by karmaisblackandbluepilled

Adds surplus crate-only items. (#256)

* Funny stuff right here

* is this piece of shit ACTUALLY complaining about indentation in a fucking comment fuck you

---
## [FantasticFwoosh/Merchant-Station-13](https://github.com/FantasticFwoosh/Merchant-Station-13)@[8c35a11b61...](https://github.com/FantasticFwoosh/Merchant-Station-13/commit/8c35a11b61efc2bb38c7d33bd7cb577b536d49f5)
#### Tuesday 2022-06-07 12:11:39 by EtraIV

Fix point vendors (#259)

* Fix point vendors bluescreening if accessed with an ID with no registered account

* You can't (brokenly) take apart point vendors anymore

* Moves the point vendors to the FUCKIGN VENDING DIRECTORY HOLY SHIT TCEO WHY DID YOU PUT THEM IN ECONOMY YOU IDIOT

---
## [avar/git](https://github.com/avar/git)@[6e043a8306...](https://github.com/avar/git/commit/6e043a8306c34355db0d28ca5179b811a83bc628)
#### Tuesday 2022-06-07 13:37:31 by Ævar Arnfjörð Bjarmason

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
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[38565e79f8...](https://github.com/cockroachdb/cockroach/commit/38565e79f832bcf5a9ad90028b796380dc73319f)
#### Tuesday 2022-06-07 14:05:14 by Josephine Lee

ui: Improve time picker keyboard input

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here]
(https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox]
(https://ant.design/docs/react/getting-started) (render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox]
(https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here]
(https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

---
## [MrKleiner/pan_vs_ham](https://github.com/MrKleiner/pan_vs_ham)@[dfb4f15ade...](https://github.com/MrKleiner/pan_vs_ham/commit/dfb4f15ade8e049863d6066f9d604974ddb6df8b)
#### Tuesday 2022-06-07 14:34:49 by mrkleiner

fucking retarded async rubbish

This is so fucking stupid, the amount of time wasted on this MAKES NO FUCKIGN SENSE. IT COULD'VE BEEN FIXED BY ADDING ONE FUCKING ATTRIBUTE, BUT FOR WHATEVER REASON IT HAS BEEN DECIDED TO WASTE A WHOLE FUCKING HOUR ON OVERENGINEERING SHIT.

---
## [TheRealScarHomie/mojave-sun-13](https://github.com/TheRealScarHomie/mojave-sun-13)@[2996f41136...](https://github.com/TheRealScarHomie/mojave-sun-13/commit/2996f41136fcd4dee419b4138e45ae65df9529f6)
#### Tuesday 2022-06-07 15:21:30 by EdwardNashton

Update Time: Machinery to People (#2096)

* Update Time: Machinery to People

Added a recorders and server racks all over the city.

Slightly changed a "Cheap Motel" near Police Dept.

Slightly changed Police Dept.

Slightly updated Chemical Factory and Weather Station.

* Update time: small fixes

Changed a servers on Power Plant.

* Update Time: that god damn room in PD

I hope we're done with it.

* Update Time: small fix

Removed a potential feature with "shutter trap" in PD.

* Update Time: fixes and updating Water Treatment Station

You made me do this, Original.

* Update Time: one day the south dir comes, we'll place our stuff and go

Sometimes you get too picky

Co-authored-by: Edward Nashton <eddienigma48@gmail.com>

---
## [plutoniummod/landing](https://github.com/plutoniummod/landing)@[056692e3e6...](https://github.com/plutoniummod/landing/commit/056692e3e605b09b139ce63c0e72d0b15f41181c)
#### Tuesday 2022-06-07 15:39:05 by Jari Zwarts

fix: --legacy-peer-deps because I'm staying on react 17 fuck you npm

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[5352c72c89...](https://github.com/zx2c4/linux-rng/commit/5352c72c8904bb3953a1be118ed06eff0113a01d)
#### Tuesday 2022-06-07 15:42:44 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

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

---
## [fajar3109/kernel_xiaomi_ginkgo](https://github.com/fajar3109/kernel_xiaomi_ginkgo)@[e2e9da509a...](https://github.com/fajar3109/kernel_xiaomi_ginkgo/commit/e2e9da509af7039365a56d781d6ec6cfa7f12b0f)
#### Tuesday 2022-06-07 16:34:12 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>
Signed-off-by: fajar <santuyz321@gmail.com>

---
## [newstools/2022-the-times](https://github.com/newstools/2022-the-times)@[05ad00a0a6...](https://github.com/newstools/2022-the-times/commit/05ad00a0a6694202bc85ae79acae51032bd6781b)
#### Tuesday 2022-06-07 17:42:03 by Billy Einkamerer

Created Text For URL [www.timeslive.co.za/news/south-africa/2022-06-07-man-who-murdered-girlfriend-and-her-mother-says-he-was-under-love-spell/]

---
## [smgoller/geode](https://github.com/smgoller/geode)@[68b9080e84...](https://github.com/smgoller/geode/commit/68b9080e84054f059b8c3e9b4aff9034fb302353)
#### Tuesday 2022-06-07 21:01:11 by Dale Emery

GEODE-9872: Make test framework code assign ports (#7176)

* GEODE-9872: Make test framework code assign ports

PROBLEM

`DistTXPersistentDebugDUnitTest ` failed in CI because it accidentally
connected to a locator from another test
(`ClusterConfigLocatorRestartDUnitTest`).

CAUSE

`ClusterConfigLocatorRestartDUnitTest` attempts to restart a
locator on a port in the ephemeral port range.

Here is the sequence of events:
1. `ClusterConfigLocatorRestartDUnitTest ` started a locator on an
   ephemeral port. In this CI run it got port 37877.
2. `ClusterConfigLocatorRestartDUnitTest` stopped the locator on port
   37877.
3. `DistTXPersistentDebugDUnitTest` started a locator on an ephemeral
   port. In this CI run it got 37877.
4. `ClusterConfigLocatorRestartDUnitTest ` attempted to restart the
   locator on port 37877. That port was already in use in
   `DistTXPersistentDebugDUnitTest`'s locator, and as a result the two
   tests became entangled.

CONTRIBUTING FACTORS

`DistTXPersistentDebugDUnitTest` uses `DUnitLauncher` to start its
locator. By default, `DUnitLauncher` starts its locator on an ephemeral
port.

`ClusterConfigLocatorRestartDUnitTest` uses `ClusterStartupRule` to
start several locators. By default, `ClusterStartupRule` starts each
locator on an ephemeral port.

SOLUTION

Change `DUnitLauncher` and `ClusterStartupRule` to assign locator ports
via `AvailablePortHelper` if the test does not specify a particular
port.

I considered changing only `ClusterConfigLogatorRestartDUnitTest` to
assign the port that it intends to reuse. But:
- That would fix only this one test, though an unknown number of tests
  similarly attempt to reuse ports assigned by framework code. Numerous
  of those tests have already been changed to assign ports explicitly,
  but an unknown number remain.
- It is quite reasonable for this test and others to assume that, if the
  test framework assigns a port on the test's behalf, then the test will
  enjoy exclusive use of that port for the entire life of the test. I
  think the key problem is not that tests make this assumption, but that
  the framework code violates it.

Changing the test framework classes that tacitly assign ports
(`DUnitLauncher` and `ClusterStartupRule`) makes them behave in a way
that tests expect.

* Add new port var to dunit sanctioned serializables

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[332a708cc7...](https://github.com/Buildstarted/linksfordevs/commit/332a708cc7786a35aa4c9a70471557ab70d096e6)
#### Tuesday 2022-06-07 22:06:48 by Ben Dornis

Updating: 6/7/2022 10:00:00 PM

 1. Added: PyPy in Production
    (https://tonybaloney.github.io/posts/pypy-in-production.html)
 2. Added: Cargo Culting Software Engineering Practices
    (https://isthisit.nz/posts/2022/cargo-culting-software-engineering-practices/)
 3. Added: Jack of all trades, master of hyperfocus
    (https://robinhawkes.com/blog/jack-of-all-trades/)
 4. Added: Understanding Kotlin Coroutine | Jason5Lee's Personal Blog
    (https://jason5lee.me/2022/06/05/understanding-kotlin-coroutine/)
 5. Added: Welcome to the M1 Windows project
    (https://amarioguy.github.io/m1windowsproject/)
 6. Added: Refactoring as Anxiety Relief
    (https://milkandcigarettes.com/notes/refactoring-as-anxiety-relief)
 7. Added: How I've made $50,000 Profit from a Side Project Slack Bot
    (https://pawelurbanek.com/anonymous-slack-bot-income)
 8. Added: eBPF, sidecars, and the future of the service mesh
    (https://buoyant.io/2022/06/07/ebpf-sidecars-and-the-future-of-the-service-mesh/)
 9. Added: I dreamt about the US startup scene for ages; now I get to be part of it
    (https://giansegato.com/essays/joined-replit)
10. Added: The Fermi Paradox of Venture Capital
    (https://dylancollins.com/2022/06/05/the-fermi-paradox-of-venture-capital/)
11. Added: "I Hate Paintings"
    (https://robertandrewspencer.com/i-hate-paintings/)
12. Added: Google - Site Reliability Engineering
    (https://sre.google/sre-book/eliminating-toil/)
13. Added: The Case for Design Engineers
    (https://blog.jim-nielsen.com/2022/the-case-for-design-engineers/)
14. Added: Refilling the non-refillable Miele AutoDos Dishwasher Automatic Detergent Dispensing Disks
    (https://mcuoneclipse.com/2022/06/04/refilling-the-non-refillable-miele-autodos-dishwasher-automatic-detergent-dispensing-disks/)
15. Added: Jan-Piet Mens
    (https://jpmens.net/2022/06/06/ten-years-of-ansible/)

Generation took: 00:06:36.5279053
 Maintenance update - cleaning up homepage and feed

---

