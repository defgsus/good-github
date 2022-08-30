## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-29](docs/good-messages/2022/2022-08-29.md)


2,071,558 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,071,558 were push events containing 3,089,117 commit messages that amount to 238,412,865 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [labaran1/linux](https://github.com/labaran1/linux)@[4e3aa92382...](https://github.com/labaran1/linux/commit/4e3aa9238277597c6c7624f302d81a7b568b6f2d)
#### Monday 2022-08-29 00:06:20 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net

---
## [green-s/stable-diffusion-webui](https://github.com/green-s/stable-diffusion-webui)@[4f8dd02ccb...](https://github.com/green-s/stable-diffusion-webui/commit/4f8dd02ccb69f5e457226531a82f54fa4dfe97ea)
#### Monday 2022-08-29 01:18:32 by Georg Zoeller

Adding .png metadata 

This may open the option to read data from images dragged into the tool later.  Activated with --save_metadata

Properties (example output from imagemagic 'identify -verbose' command:
    SD:cfg_scale: 7.5
    SD:GFPGAN: False
    SD:height: 512
    SD:normalize_prompt_weights: True
    SD:prompt: a beautiful matte painting of a cottage on a magical fantasy island, unreal engine, barometric projection, rectilinear
    SD:seed: 247624793
    SD:steps: 50
    SD:width: 512

---
## [MaterializeInc/materialize](https://github.com/MaterializeInc/materialize)@[305082a6a9...](https://github.com/MaterializeInc/materialize/commit/305082a6a99ee063839975c86bd1e821a2af0e23)
#### Monday 2022-08-29 01:45:41 by Daniel Harrison

persist: commit state updates to durable storage incrementally

Before, there was pressure to keep the size of state down, because it
was rewritten entirely on each command application. In particular, this
created a tension in compaction tuning between being aggressive about
fewer batches (smaller state) and compacting small batches lazily
(smaller write amplification).

Writing state updates as incremental diffs means that size of a
Consensus writes for each command is independent of the total size of
state. We should be able leverage this to make the entire
`WriteHandle::compare_and_append_batch` latency constant w.r.t. the size
of state and thus independent of compaction. This lets us tune
compaction entirely for where we want to be in its more intrinsic
tradeoff between read, write, and space amplification.

(NB: This commit doesn't quite get us to constant latencies, there's
some elbow grease left. I've proven concretely that it can get down to
`O(log(num state batches))`, but that included some hacks that didn't
make this PR. This would be lovely followup work once we get a chance.)

As persist metadata changes over time, we make its versions (each
identified by a [SeqNo]) durable in two ways:
- `rollups`: Periodic copies of the entirety of [State], written to
  [Blob].
- `diffs`: Incremental [StateDiff]s, written to [Consensus]. The
following invariants are maintained at all times:
- A shard is initialized iff there is at least one version of it in
  Consensus.
- The first version of state is written to `SeqNo(1)`. Each successive
  state version is assigned its predecessor's SeqNo +1.
- `current`: The latest version of state. By definition, the largest
  SeqNo present in Consensus.
- As state changes over time, we keep a range of consecutive versions
  available. These are periodically `truncated` to prune old versions
  that are no longer necessary.
- `earliest`: The first version of state that it is possible to
  reconstruct.
  - Invariant: `earliest <= current.seqno_since()` (we don't garbage
    collect versions still being used by some reader).
  - Invariant: `earliest` is always the smallest Seqno present in
    Consensus.
    - This doesn't have to be true, but we select to enforce it.
    - Because the data stored at that smallest Seqno is an incremental
      diff, to make this invariant work, there needs to be a rollup at
      either `earliest-1` or `earliest`. We choose `earliest` because it
      seems to make the code easier to reason about in practice.
    - A consequence of the above is when we garbage collect old versions
      of state, we're only free to truncate ones that are `<` the latest
      rollup that is `<= current.seqno_since`.
- `live diffs`: The set of SeqNos present in Consensus at any given
  time.
- `live states`: The range of state versions that it is possible to
  reconstruct: `[earliest,current]`.
  - Because of earliest and current invariants above, the range of `live
    diffs` and `live states` are the same.
- The set of known rollups are tracked in the shard state itself.
  - For efficiency of common operations, the most recent rollup's Blob
    key is always denormalized in each StateDiff written to Consensus.
    (As described above, there is always a rollup at earliest, so we're
    guaranteed that there is always at least one live rollup.)
  - Invariant: The rollups in `current` exist in Blob.
    - A consequence is that, if a rollup in a state you believe is
      `current` doesn't exist, it's a guarantee that `current` has
      changed (or it's a bug).
  - Any rollup at a version `< earliest-1` is useless (we've lost the
    incremental diffs between it and the live states). GC is tasked with
    deleting these rollups from Blob before truncating diffs from
    Consensus. Thus, any rollup at a seqno < earliest can be considered
    "leaked" and deleted by the leaked blob detector.
  - Note that this means, while `current`'s rollups exist, it will be
    common for other live states to reference rollups that no longer
    exist.

---
## [WesternGamer/PluginHub](https://github.com/WesternGamer/PluginHub)@[016e22a0c7...](https://github.com/WesternGamer/PluginHub/commit/016e22a0c7393f2709f37cc38f8ef256f5428125)
#### Monday 2022-08-29 01:51:48 by BipolarExpedition

Adding GPS Helper Mod with author permission

Adding GPS Helper Mod with author permission 

Kaito  [author] Jul 1 @ 1:20pm 
No, I had not considered it yet. Feel free to have a look. I'm kinda busy irl right now, so it would be a while before I could look.

In theory it all runs on the client, but you'll have to check the API.

Doc1979 Jun 28 @ 4:37pm 
Does this use server only commands? If not, have you thought of making it into a PluginLoader plugin? I was thinking of looking at your github to see if I could convert it myself, but if its already on your todo list, I'll wait

---
## [Benjamintf1/pendragon2](https://github.com/Benjamintf1/pendragon2)@[b520a9812a...](https://github.com/Benjamintf1/pendragon2/commit/b520a9812a94195e417fddf79bd47de4d5a02b30)
#### Monday 2022-08-29 03:29:50 by benjamin fuller

squash to one

remove stuff

who am i kidding lol

change stuff

refactor

allow moving away from picking name

bring out sidebar

starting a class for character

more refactor

refactor

options are objects

character is now a class

factor out events

stuff

no good commit message

refactor

working on it

thing

add character view that doesn't do anything

change prompt for pick a name

factor out views from app

factor out views from app

factor out Attribute

working on character

add bad looking glory

refactor

stuff

refactor

make glory different, idk why i'm trying to please people I havn't met

now i guess all data state?

fix errors

add option for event to have multiple outcomes

update stuff

umm...stuff

.

date is now more complicated

add ability to progress time

add birthday function

uhhh

update wording of event

learn how to spell you dummy

i give up on life

events are immutable now

pre-processsing Events

try catch in pre-processing

go crazy on templates

wording

kinda add passions technechially

add back passions map

mess with wording

unworkable code for saving added idk, maybe a bad idea

i hate myself rn

fix syntax highlighting and don't allow empty save name

fix progress time

maybe fix?

adfasdf

add fromjs functions

fix glory for saving and loading

rename stuff

supress errors for now for anchors vs buttons. Figure it out some time in the future maybe

add more stuff

whoops, fix discontinuity

add a bad version of tickertape

lol

change branding

fix title

you can now view old characters

add birthday

update wording

fix random ammount

add todo

typo

fix loading

it's typescript now, also tests

refactor

type correction for events

gain passions does greater

future check to see if already knighted

add last change time

add footer class

add tests + refactor

change wording idk

change wording idk

adfasdf

---
## [queercpu/script](https://github.com/queercpu/script)@[7922653b85...](https://github.com/queercpu/script/commit/7922653b851e3f229efc0e9a142940674de87c14)
#### Monday 2022-08-29 04:06:30 by home.cpu

most of the day was devoted to revamping twigs house.  night version, day version, started to sketch out some of snakeys scene, i want to bring back some of the older works, where snakey is sad the girl is joining love corp. its twigs now so Imma just put pressure on twigs.  twigs say, snakey, im leaving. and its this convo that has the YOU ARE WORSE THAN, when snakey gets sad twigs is leaving.  also has to have sweet cake happy moments, generous verbosity

---
## [sigp/lighthouse](https://github.com/sigp/lighthouse)@[84ddf32d3b...](https://github.com/sigp/lighthouse/commit/84ddf32d3b02f8d099d522e70ca3322bc10bb887)
#### Monday 2022-08-29 04:12:53 by Michael Sproul

Refactor op pool for speed and correctness (#3312)

## Proposed Changes

This PR has two aims: to speed up attestation packing in the op pool, and to fix bugs in the verification of attester slashings, proposer slashings and voluntary exits. The changes are bundled into a single database schema upgrade (v12).

Attestation packing is sped up by removing several inefficiencies: 

- No more recalculation of `attesting_indices` during packing.
- No (unnecessary) examination of the `ParticipationFlags`: a bitfield suffices. See `RewardCache`.
- No re-checking of attestation validity during packing: the `AttestationMap` provides attestations which are "correct by construction" (I have checked this using Hydra).
- No SSZ re-serialization for the clunky `AttestationId` type (it can be removed in a future release).

So far the speed-up seems to be roughly 2-10x, from 500ms down to 50-100ms.

Verification of attester slashings, proposer slashings and voluntary exits is fixed by:

- Tracking the `ForkVersion`s that were used to verify each message inside the `SigVerifiedOp`. This allows us to quickly re-verify that they match the head state's opinion of what the `ForkVersion` should be at the epoch(s) relevant to the message.
- Storing the `SigVerifiedOp` on disk rather than the raw operation. This allows us to continue track the fork versions after a reboot.

This is mostly contained in this commit 52bb1840ae5c4356a8fc3a51e5df23ed65ed2c7f.

## Additional Info

The schema upgrade uses the justified state to re-verify attestations and compute `attesting_indices` for them. It will drop any attestations that fail to verify, by the logic that attestations are most valuable in the few slots after they're observed, and are probably stale and useless by the time a node restarts. Exits and proposer slashings and similarly re-verified to obtain `SigVerifiedOp`s.

This PR contains a runtime killswitch `--paranoid-block-proposal` which opts out of all the optimisations in favour of closely verifying every included message. Although I'm quite sure that the optimisations are correct this flag could be useful in the event of an unforeseen emergency.

Finally, you might notice that the `RewardCache` appears quite useless in its current form because it is only updated on the hot-path immediately before proposal. My hope is that in future we can shift calls to `RewardCache::update` into the background, e.g. while performing the state advance. It is also forward-looking to `tree-states` compatibility, where iterating and indexing `state.{previous,current}_epoch_participation` is expensive and needs to be minimised.

---
## [kittstone/better](https://github.com/kittstone/better)@[1a52f93c1c...](https://github.com/kittstone/better/commit/1a52f93c1cde6f14143df4aee20f4c45ef98a8bd)
#### Monday 2022-08-29 05:21:35 by WizardMantis441

about to fucking kick major ass

yeah yeah ooh ay skrr bowoie

---
## [Vetpetmon-Labs/Wyrms-of-Nyrus](https://github.com/Vetpetmon-Labs/Wyrms-of-Nyrus)@[4979ab6679...](https://github.com/Vetpetmon-Labs/Wyrms-of-Nyrus/commit/4979ab6679ddd76b12c77c300df1802f415b4dce)
#### Monday 2022-08-29 05:35:09 by Vetpetmon

HOLY $#!7 MY DRIVE FAILED THIS IS WHAT I RECOVERED

THAT COULD HAVE GONE MUCH, MUCH WORSE.

MY ART FILES ARE SAFE. ONLY IMPORTANT THING WE LOST WAS SAPIENT QUEEN'S ANIMATIONS.

Im not sleeping easy tonight after experiencing this, making a deal with the devil (whoever owns that google drive, IOU), waiting 2 hours, staying up past midnight, just to recover 2+ years of work from multiple physical locations that was stored on a USB that decided it would pull a funny and convert itself to RAW but instead of typing /j it typed /srs so here we are, with me ugly crying in the corner knowing that it could've gone down like my first corrupted USB flash drive.

This is a cry for help. This isn't the first time my PC made a USB flash drive go FUBAR

---
## [ScreamingSandals/BedWars](https://github.com/ScreamingSandals/BedWars)@[3b4a762202...](https://github.com/ScreamingSandals/BedWars/commit/3b4a762202942db6d6c736f0007b51c4de7e1fed)
#### Monday 2022-08-29 05:39:44 by Misat11

some fixes and changes to 1.8.8 bossbars (see description)

There are 2 configurable backend entities for bossbars (invalid value fallbacks to wither)
- `wither` (default)
  - Everything works great except that fucking fog (it's ok for games in the evening or in night)
- `ender_dragon` (other possible values are `dragon` and `ender`)
  - Normal sky however it's randomly flickering even if not moving and the dragon does not want to be invisible, so it can be seen in void worlds.

---
## [abhiagrawal9/react](https://github.com/abhiagrawal9/react)@[b6978bc38f...](https://github.com/abhiagrawal9/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Monday 2022-08-29 06:41:51 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [huggingface/blog](https://github.com/huggingface/blog)@[ca5d337023...](https://github.com/huggingface/blog/commit/ca5d337023d9300e991b41a076af216c66659daa)
#### Monday 2022-08-29 07:02:35 by CarlosMFerr

Add files via upload

#**The quest of OpenRAIL: Towards open and responsible AI licensing frameworks**

Open & Responsible AI licenses ("OpenRAIL") are AI-specific licenses enabling open access, use and distribution of AI artifacts while requiring a responsible use of the latter. OpenRAILs are a necessary tool contributing to ongoing AI community, industry, and policy efforts towards an open and responsible development and use of AI systems. Even though current open licenses bring huge benefits to AI innovation in general, they do not take into account the potential of machine learning models or data as different artifacts to code. OpenRAIL licenses could be for open and responsible ML what current open software licenses are to code and Creative Commons to general content: **a widespread community licensing tool.**

Advances in machine learning and other AI-related areas have flourished these past years partly thanks to the ubiquity of the open source culture in the ICT sector, which has permeated into ML research and development dynamics. Notwithstanding the benefits of openness as a core value for innovation in the field, (not so already) recent events related to the ethical and socio-economic concerns of development and use of machine learning models have spread a clear message: Openness is not enough. Closed systems are not the answer though, as the problem persists under the opacity of firms' private AI development models.

Open licensing is one of the cornerstones of AI innovation. Licenses as social and legal institutions should be well taken care of. They should not be conceived as burdensome legal technical mechanisms, but rather as a communication instrument among AI communities bringing stakeholders together by sharing common messages on how the licensed artifact can be used.

## **Open source licenses do not fit all**

Access, development and use of ML models is highly influenced by open source licensing schemes. For instance, ML developers might colloquially refer to "open sourcing a model" when they make its weights available by attaching an official open source license, or any other open software or content license such as Creative Commons. This begs the question: why do they do it? Are ML artifacts and source code really that similar? Do they share enough from a technical perspective that private governance mechanisms (e.g. open source licenses) designed for source code should also govern the development and use of ML models?

Most current model developers seem to think so, as the majority of openly released models have an open source license (e.g., Apache 2.0). See for instance the Hugging Face [Model Hub](https://huggingface.co/models?license=license:apache-2.0&sort=downloads) and [Muñoz Ferrandis & Duque Lizarralde (2022)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4018413).

However, empirical evidence is also telling us that a rigid approach to open sourcing [and/or](https://www.gnu.org/philosophy/open-source-misses-the-point.en.html) Free Software dynamics and an axiomatic belief in Freedom 0 for the release of ML artifacts is creating socio-ethical distortions in the use of ML models (see [Widder et al. (2022)](https://davidwidder.me/files/widder-ossdeepfakes-facct22.pdf)). In simpler terms, open source licenses do not take the technical nature and capabilities of the model as a different artifact to software/source code into account, and are therefore ill-adapted to enabling a more responsible use of ML models (e.g. criteria 6 of the [Open Source Definition](https://opensource.org/osd)), see also [Widder et al. (2022)](https://davidwidder.me/files/widder-ossdeepfakes-facct22.pdf); [Moran (2021)](https://www.google.com/url?q=https://thegradient.pub/machine-learning-ethics-and-open-source-licensing-2/&sa=D&source=docs&ust=1655402923069398&usg=AOvVaw3yTXEfpRQOJ99w04v5GAEd); [Contractor et al. (2020)](https://arxiv.org/abs/2011.03116).

If specific ad hoc practices devoted to documentation, transparency and ethical usage of ML models are already present and improving each day (e.g., model cards, evaluation benchmarks), why shouldn't open licensing practices also be adapted to the specific capabilities and challenges stemming from ML models?

Same concerns are rising in commercial and government ML licensing practices. In the words of[Bowe & Martin (2022)](https://www.gmu.edu/news/2022-04/no-10-implementing-responsible-ai-proposed-framework-data-licensing): "_Babak Siavoshy, general counsel at Anduril Industries, asked what type of license terms should apply to an AI algorithm privately developed for computer-vision object detection and adapt it for military targeting or threat-evaluation? Neither commercial software licenses nor standard DFARS data rights clauses adequately answer this question as neither appropriately protects the developer's interest or enable the government to gain the insight into the system to deploy it responsibly_".

If indeed ML models and software/source code are different artifacts, why is the former released under open source licenses? The answer is easy, open source licenses have become the de facto standard in software-related markets for the open sharing of code among software communities. This "open source" approach to collaborative software development has permeated and influenced AI development and licensing practices and has brought huge benefits. Both open source and Open & Responsible AI licenses ("OpenRAIL") might well be complementary initiatives.

**Why don't we design a set of licensing mechanisms inspired by movements such as open source and led by an evidence-based approach from the ML field?** In fact, there is a new set of licensing frameworks which are going to be the vehicle towards open and responsible ML development, use and access: Open & Responsible AI Licenses ([OpenRAIL](https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses)).

## **A change of licensing paradigm: OpenRAIL**

The OpenRAIL [approach](https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses) taken by the [RAIL Initiative](https://www.licenses.ai/) and supported by Hugging Face is informed and inspired by initiatives such as BigScience, Open Source, and Creative Commons. The 2 main features of an OpenRAIL license are:

- **Open:** these licenses allow royalty free access and flexible downstream use and re-distribution of the licensed material, and distribution of any derivatives of it.

- **Responsible:** OpenRAIL licenses embed a specific set of restrictions for the use of the licensed AI artifact in identified critical scenarios. Use-based restrictions are informed by an evidence-based approach to ML development and use limitations which forces to draw a line between promoting wide access and use of ML against potential social costs stemming from harmful uses of the openly licensed AI artifact. Therefore, while benefiting from an open access to the ML model, the user will not be able to use the model for the specified restricted scenarios.

The integration of use-based restrictions clauses into open AI licenses brings up the ability to better control the use of AI artifacts and the capacity of enforcement to the licensor of the ML model, standing up for a responsible use of the released AI artifact, in case a misuse of the model is identified. If behavioral-use restrictions were not present in open AI licenses, how would licensors even begin to think about responsible use-related legal tools and enforcement? OpenRAILs and RAILs are the first step towards enabling ethics-informed behavioral restrictions.

And even before thinking about enforcement, use-based restriction clauses might act as a deterrent for potential users to misuse the model (i.e., dissuasive effect). However, the mere presence of use-based restrictions might not be enough to ensure that potential misuses of the released AI artifact won't happen. This is why OpenRAILs require downstream adoption of the use-based restrictions by subsequent re-distribution and derivatives of the AI artifact, as a means to dissuade users of derivatives of the AI artifact from misusing the latter.

The "viral" effect of copyleft-style downstream behavioral-use clauses spreads the requirement from the original licensor on his/her wish and trust on the responsible use of the licensed artifact. Moreover, widespread adoption of behavioral-use clauses gives subsequent distributors of derivative versions of the licensed artifact the ability to control the use of it and for instance to block remotely any access to it if misused.

## **OpenRAIL could be for good machine learning what open software licensing is to code**

Three examples of OpenRAIL licenses are the recently released [BigScience OpenRAIL-M](https://www.licenses.ai/blog/2022/8/26/bigscience-open-rail-m-license), StableDiffusion's [CreativeML OpenRAIL-M](https://huggingface.co/spaces/CompVis/stable-diffusion-license), and the genesis of the former two: [BigSicence BLOOM RAIL v1.0](https://huggingface.co/spaces/bigscience/license) (see post and FAQ [here](https://bigscience.huggingface.co/blog/the-bigscience-rail-license)). The latter was specifically designed to promote open and responsible access and use of BigScience's 176B parameter model named BLOOM (and related checkpoints). The license plays at the intersection between openness and responsible AI by proposing a permissive set of licensing terms coped with a use-based restrictions clause wherein a limited number of restricted uses is set based on the evidence on the potential that Large Language Models (LLMs) have, as well as their inherent risks and scrutinized limitations. The OpenRAIL approach taken by the RAIL Initiative is a consequence of the BigScience BLOOM RAIL v1.0 being the first of its kind in parallel with the release of other more restricted models with behavioral-use clauses, such as [OPT-175](https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/MODEL_LICENSE.md) or [SEER](https://github.com/facebookresearch/vissl/blob/main/projects/SEER/MODEL_LICENSE.md), being also made available.

The licenses are BigScience's reaction to 2 partially addressed challenges in the licensing space: (i) the "Model" being a different thing to "code"; (ii) the responsible use of the Model. BigScience made that extra step by really focusing the license on the specific case scenario and BigScience's community goals. In fact, the solution proposed is kind of a new one in the AI space: BigScience designed the license in a way that makes the responsible use of the Model widespread (i.e. promotion of responsible use), because any re-distribution or derivatives of the Model will have to comply with the specific use-based restrictions while being able to propose other licensing terms when it comes to the rest of the license.

OpenRAIL also aligns with the ongoing regulatory trend proposing sectoral specific regulations for the deployment, use and commercialization of AI systems. With the advent of AI regulations (e.g., [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52021PC0206); Canada's [proposal](https://iapp.org/news/a/canada-introduces-new-federal-privacy-and-ai-legislation/) of an AI & Data Act), new open licensing paradigms informed by AI regulatory trends and ethical concerns have the potential of being massively adopted in the coming years. Open sourcing a model without taking due account of its impact, use, and documentation could be a source of concern in light of new AI regulatory trends. Henceforth, OpenRAILs should be conceived as instruments articulating with ongoing AI regulatory trends and part of a broader system of AI governance tools and not as the only solution enabling open and responsible use of AI.

Let's invest in a healthy open and responsible AI licensing culture, the future of AI innovation and impact depends on it, on all of us, on you.

Author: Carlos Muñoz Ferrandis

Blog acknowledgments: Yacine Jernite, Giada Pistilli, Irene Solaiman, Clementine Fourrier, Clément Délange

---
## [s7uck/s7uck.github.io](https://github.com/s7uck/s7uck.github.io)@[191b1ca585...](https://github.com/s7uck/s7uck.github.io/commit/191b1ca5859a397a583961b953256e15b54991ae)
#### Monday 2022-08-29 08:14:03 by s7uck

Improved compatibility with IE10
(Please end me, why the hell do I care? Does anyone care? Why am I 
sacrificing time just to support these underused and idiot-friendly 
browsers? I should be doing something else with my time? I dont 
know..uh..:trollface:)

Jokes aside, I'm not doing this to support IE; I just want to make my 
website simpler, which has always been a goal of mine. I'm just never 
happy with anything I do lol. My page looks pretty but somehow I feel 
guilty of overcomplicating things. So here it goes. I removed flexbox 
just because it's too glitchy anyways (and even on modern 
Firefox...yikes)

Also reworking on that /watch? page thing. But first need to make it 
better.

Longest commit message ever?

---
## [NimBlemations/Vs-Mr-Thump](https://github.com/NimBlemations/Vs-Mr-Thump)@[5eebeab1e6...](https://github.com/NimBlemations/Vs-Mr-Thump/commit/5eebeab1e61ba44141200fdda229fdaed1c65e90)
#### Monday 2022-08-29 08:19:40 by NimBlemations

Trying again but it fucking fails

Haxeflixel I swear to god I will fucking murder you and your family oh my fucking god I am so fucking pissed off.

---
## [MASQ-Project/Node](https://github.com/MASQ-Project/Node)@[b0e9bb484e...](https://github.com/MASQ-Project/Node/commit/b0e9bb484effc32ed164eb4bef51b624c3d7982a)
#### Monday 2022-08-29 10:01:04 by dnwiebe

GH-625: Log message enhancements, plus clippy appeasement (#153)

* Log message enhancements, plus clippy appeasement

* GH-627: Clippy should be happy again by now

* GH-627: one line was silly

* GH-627: starting ignoring the troublesome test again

* GH-627: there was a formatting issue

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* Added import

* GH-625: Formatting

* GH-625: Remember to return

Co-authored-by: Bert <Bert@Bert.com>

---
## [sAmenta/CodePlayground](https://github.com/sAmenta/CodePlayground)@[d1bc545a1f...](https://github.com/sAmenta/CodePlayground/commit/d1bc545a1f8ddb756265c3ffa144ffefb73b61cd)
#### Monday 2022-08-29 10:14:22 by Stefano.Amenta

Your colleagues have been looking over you shoulder. When you should have been doing your boring real job,
you've been using the work computers to smash in endless hours of codewars.

In a team meeting, a terrible, awful person declares to the group that you aren't working. You're in trouble.
You quickly have to gauge the feeling in the room to decide whether or not you should gather your things and leave.

Given an object (meet) containing team member names as keys, and their happiness rating out of 10 as the value,
you need to assess the overall happiness rating of the group. If <= 5, return 'Get Out Now!'. Else return 'Nice Work Champ!'.

Happiness rating will be total score / number of people in the room.

Note that your boss is in the room (boss), their score is worth double it's face value (but they are still just one person!).

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4e4e5d47f8...](https://github.com/mrakgr/The-Spiral-Language/commit/4e4e5d47f8e8d627ebb2069b2c0afcbac61ea883)
#### Monday 2022-08-29 10:55:27 by Marko Grdinić

"9:40am. Despite going to bed before 12am, I had a lot of trouble falling asleep. The last two days are the usual case of me simply needing to think about the story itself. i knew what to write even yesterday. Rather my will itself is shaken now that I am revisiting the self improvement loop. The self improvement loop is my one true love, it is what I most long for. It is my biggest obsession. So it is no wonder that watching somebody else do it would crush me.

I am getting over it though.

Despite my feelings being complex and intervowen, isolating myself in bed is really effective at untangling the threads. Facing the past like this is the best kind of therapy.

I need some more time, but after that I am going to show my attitide.

Programming vs writing. I can look at how much programers make and how much writers make when making a judgment which path to go, but that does not matter. Other writers are not me. A programer can be persistent and land at some well paying job, but a writer depends on his or hers appeal. You can't really compare a beautiful girl to an average one. And the only way to judge my appeal is to put myself out there. Well paid writers, get paid quite a lot in this era despite the competition.

The fact that I understan that the real money is on Patreon is a big step forward compared to me in 2014. Back then I just started writing without even sparing a thought as to how to monetize it.

In termps of paths:
A programmer gets a low paid job, then a well paid job, then starts his own company.
A writer gets an audience and cultivates it. Later on, I'll get all kinds of AI assistance, so I should get a chance to expand into programming once more.

It is always better to hold on to your independence that to sell it to the first bidder. Wage slaving might pay better at first, but being a creative is better than being a wage slave.

Or at least, it would be if I could get over my mental trauma.

9:55am. I need to honestly try it. I need to put in 6-12 months into writing Simulacrum's never arcs. If it works, I've made it. But if it turns out to be repulsive I have no choice, but to pivot once again. I need to show my courage.

It is better to work on what is close to your heart, and to be some ball on the roulette table knowing who knows where you'll land.

10am. Whatever the case is, I need to do this. I need to put in the effort and show my independent attitude. Right now, I can't really get a job because my obsession keeps flaring up at the worst moments and sabotaging me.

I've put in 9 months just studying 3d. But writing should be something I am good at, so I should at least be willing to put that much in as well. Otherwise I am just being a clown.

I should trust in my own vision as I go forward.

It was indeed right that my 2014 was not good enough. The vision was too incomplete to have proper appeal. Just self improvement is not enough to make a product. I also needed a way of providing it to everyone. And now I have it. I'll bring all my thoughts and desires in one singular story!

10:05am. Let me chill a bit and then I will try to write a page or two. I didn't really sleep well tonight, so I am not going push myself too hard today.

10:25am. Let me start. I am bemoaning my lack of power, but there is strength in putting a single word down. Step by step, the destination gets reached.

I will not let writing become tedious. I am doing this because I want to do it more than anything else. I want to live in this world for real.

Trading, haven't I failed it because I was obsessed with finding the right system, rather than actually trading. The first arcs, did I not fail that because I was obsessed with clarifying my vision than actual writing. Programming, did I not fail because I was aiming to resolve a specific need rather than doing RL agents specifically? In RL, had I really wanted a poker bot, I could have had it, but I was obsessed with making NNs work.

In all my failures, the main cause has been exploration. I should be able to do it much better from here on out.

10:30am. Focus me, on the story. The story is what really matters. I need to show my attitude. For the next 9 months. It won't be a real try unless I can match the effort I've put into 3d.

$$$

(Helix Studio, Regent Suite, Bedroom)

"Ahhhhh!" With a scream, I eject myself from the game, and into the safe space.

"Hah, hah, hah!" I breathe heavily. After I catch my bearings, I slurp my saliva down my throat and wipe the droll with my sleeve.

I can't believe it, right now I am still trembling all over! Real death, unexpected death is traumatic!

"Hah, hah, hah..."  It takes me a while to calm down. Right now I am in my bedroom in the cruise, lying on the king sized bed. After a while my shivers susbside and I start to gather my thoughts.

I admit this caught me by surprise, I didn't think that somebody would pull a gun on me. I have a week of experience in the game by now, so I know that what he did should be impossible. While it is easy to create manifestations in the city itself, in the dueling realms, I've tried it, and found it impossible to create even the simplest things. Whatever system is reading my thoughts and manifesting my projections does not work when the chips are down. Otherwise why would anybody play poker to begin with? Call, fold, raise? Just shot the other guy. Bang!

What the white haired guy did was quite amazing. Right now, I have no way of countering it. If I could make my own gun, I could try getting the jump on him, or maybe if I could make a shield, I could protect myself. But that is not possible.

What he did in the street would not be too hard, I'd have to study the structure of a gun for a while and practice manifesting it. This would be easy in this virtual space. You can't actually hurt anybody in this city directly. If I tried attacking anybody on the street, with a gun, fist or anything else, that would initiate a resolution match. Mickey told me about it.

I am not sure what I should do right now.

I get off the bed and stretch my body. Now that I've gotten over the shakes, I realize that I need a bath and a meal, in that order.

I know where the bathroom is already, so I make my way there. Opulence, luxury, I really envy the rich people who can experience this in real life. Everything in the bathroom looks like it costs at least 100k dollars. At home I just take showers, but here I do that and then a nice long break in the tub. It is a new experience for me, so I try experimenting with all the shampos and bathing soaps that I've never seen before.

Refreshed and relaxed, I go into the kitchen and get some food. In the mega-fridge there are all sorts of meals and drinks. I go for some pasta and salsa. When I pick up the item I get a window asking me:

> Do you want to the system to warm up the meal for you? Yes/No.

I mentally confirm it, and the meal transforms into a freshly cooked one. I take out some cutlery from one of the drawers, put the meals and it on a tray, and have a meal alone in the living room. The world is bright and sunny outside, and my only company is the murmur of waves.

Afterwards, I note the living room has a bar so I get drunk and spend a few hours lounging on the sofa. I waste some time watching anime on TV. Wonderful.

A part of me wishes I could stay there forever.

...

I remember the gunshot, and it spoils my mood.

[Pathos check DC 2 Failed - Sampled 1.52]

But I do not feel like doing anything about that guy. Why would I want to leap right back into the fray? I leave Heaven's Key aside from my mind, and just have some fun on the cruise. I think about my experiences in the game itself and a wave of lethargy assaults me. I spend a week there just grinding chips, but in the end what has that gotten me?

I could have gotten a million chips and it still would not have given me any benefits in real life. Just what was the point of all that effort? There isn't as far as I can see. It taught me a little bit of live poker, but what am I going to use that for? Nothing really. I am certainly not good enough to start grinding for real money online.

I put in a week of effort into it, and so like that I spend a week relaxing on the cruise.

It was a long time for me, but only a minute passes in the real world.

(Helix Studio, Regent Suite, Brow of the ship)

The cruise is huge, and I had time to adventure and explore it. Nobody is here, but me. I had the time so I checked the rooms one by one when I had free time from gaming. They were all neatly aranged, and they all belonged to me. At the end of the week, I started to feel pangs of loneliness.

[Externus check DC 2 Succeeded - Sampled 4.1]

But it was not because there aren't any people here. Neither do I miss my parents. Loneliness is caused by only one thing - lack of power.

Power, huh? As I wander through the ship without direction, I come to the brow. I go up to the railing and sit myself below it, dangling my feet over the ledge. I gaze at the waters below.

The thought that comes to mind, is hardship. It is so difficult. I think about my life since I uploaded myself, and contrast that with some of the recent gaming sessions.

I was playing an RPG. In there controlling the characters is so easy. They can go into battle after difficult battle without complaint, with seemingly endless capacity for work. It is not that they are robots, it is that they have somebody controling and guiding their actions from beyond.

I think about it. How would being a character in a computer RPG or a tabletop game be?

I'd have my own thoughts and feelings. I wouldn't realize that I am being guided by some force entity beyond. Whatever system that entity would be using would not feel tacked on. It would feel like...

I think about it. And the world to describe it perfectly comes to me - natural.

I realize the truth at that point. People think they have free will, but ultimately they are just acting based on their instincts. Ultimately, somebody designed their emotional system and they will act according to it, for better or for worse. There is no guarantee that their feelings will guide them to the correct solution, anymore that a bad player can win the game on the first game without dying.

I look at my hands and realize that this is all my determination amounts to. I wanted superpowers. I knew that it would be hard to get them. I started playing Simulacrum as per plan and made good progress thanks to my cheating. Then somebody put his boot up my ass, and I am so distraught that I stopped playing it for an entire week.

If somebody was playing me, and I was an RPG character, he would never let that happen. He would just reload and get me back into the fray.

The reason this is happening is because the responsibility for the task I set out to do is too great. I ran into difficulty, and my great plan collapsed, drowned in a wave of emotion. A melancholic feel comes over me as I look at the waves below. I am somehow reminded of that time I hurled myself from the rim of the city.

I remember falling and recall the feeling. I recall that how once I threw myself, just before I hit I wanted myself to stop falling. It was a swirl of emotions without end in sight.

Suppose back then I used the mind control app to normalize my mental state, I would be calm throughout. But if I extrapolated such an attitude to my whole life, I'd live a very dull if calm life. The ability to accept anything and be happy about anything is a dangerous thing. If I can accept anything, why not become a normie and treat the well traveled path? Because I know that their path does not lead to power.

The main problem is that I broke under pressure. It is not like studying a textbook. I simply do not have the ability to do surgery on myself in the middle of a fight. It is normal to get heated in battle. Use the core to get rid of fear, and you get comfortable with getting hit. A graceful loser is still a loser. I do not need pride, but I need victory.

Victory should come over everything. Does it really matter how it is accomplished? I need to win the game, but does it really matter that I be the character in the game?

In a moment of clarity, I remember the character sheet of the character in the game I was playing. And I see the game being played from perspective of tens and hundreds of thousands of other players. And I realize that every single one of them of them is looking at themselves from the perspective of the character. But the characters are nothing. They are meant to be broken and tossed away. The true power lies in being a player. It is hard to realize this, because they themselves are players.

It would be weird to dream about being a player of a game, when you are already doing that.

But that is what I must dream about. I must aim to be a player.

In life, everyone wants to be a characters with high base stats. People live their life, and when they lose they blame themselves. If life was truly a game, the one to take responsibility for victory and defeat should be the one controlling them from beyond - the player. By that reasoning, since humans are controlled by nature, the one who should take credit for that is nature itself. But nature is a brainless and non-adaptive. It doesn't care about the goals of the characters. It doesn't care about its own responsibility as a player. It can't take responsibility, so it has to fall on the character itself.

Being controlled by nature is unjust.

With such a player, if I go into the game, of course I am going to get an anal expansion as soon as I inevitably run into somebody better. It is my responsibility to see that the justice is done.

I get up and clench my fist decisively.

I will go beyond and become my own player. This more than just winning a game. It is about playing it properly.

(Helix Studio, Regent Suite, Bedroom)

I have no confidence of being able to beat the white haired guy. But that doesn't matter, I am not going to be fighting him as a character inside the game, but as a player.

But before that, instead of having to bear the computational burden of the Simulacrum game, if I did some simpler simulations, I could get a lot more training done in the same amount of time that if I played the game directly. I've read that the notion of training on simulated games is the most powerful idea in machine learning, but to make it work it is best to follow a curriculum. Little kids learn arithmetic before they move on to algebra. I must learn to walk before I can run, in this case literally.

I'll ignore the challenge waiting for me in Heaven's Key, and conquer the very first challenge that all Inspired must do which is adapt to using the full computational power of the core.

Right now, I can only run my own simulation at the same rate as the outerlying environment. Even small increases of computational speed gives me great difficulty in moving. Let me not waste anymore time tackling this, I am going to deal with this first.

It is time to enter the self improvement loop.

(Image TODO: A single image split by a vertical bar. On the left side there is an image of a human brain. A line leads from it to a frame of a window showing its magnified bioligical representation made of synapses and and neurons. On the right side is a brain core. Similarly to the human brain, a line leads to one of the corners showing a framed subwindow. Instead of neurons and synpases, what that window shows is lines and lines of code in some strange functional programming language called Spiral.)

According to the guides online, the next step in my evolution as a digital being is to move from being an emulation of a human to an actual program. The trouble with biological brains is that nature didn't exactly leave a lot of room for me to come in and tinker with it. So what I need to do is unchain my representation from the biological to one that will be more amenable to editing and manipulation. After I have that I'll be able to edit my own mental programming directly a lot more easily.

This is easy to do. I just go into the brain emulator program and select the Extract Programatic Form. I select a folder, and in a flash, that produces some data as well as Spiral library files which make up my own mental program. In order to run this, what I'd have to do is compile this program to an executable, run it and attach it to a simulation. I'll leave that for later. Right now I am really curious as to how my own programming looks like. The brain emulator simulates cells and biological processes in an optimized fashion, so it is hard to gleam anything from it. In this form I'll be able to properly study it.

The brain emulation's purpose is to retain fidelity to the limit, but the programatic form's purpose is to be an approximation of my self that is easily editable, so there will be some loss in the transition. I've already been prepared for this so I do not mind it. After I start the self improvement loop, the further I go into it, the less I will resemble the original, so there is no point in making a fuss about identity.

In addition to its media capabilities, Helix Studio has a programming IDE, so open the folder in it and go over the code files.

(Image TODO: Image of Euclid sitting at his computer desk, pondering about the meaning of code. The background of the bedroom is darkned and covered by green reams of computer code. The lens of his glasses partially cover his eyes, and in them the glow of the code is reflected.)

A few days pass with me engrossed in study.

(Helix Studio, Regent Suite, Pool)

"Pwah!" With a splash, I emergy from the depths of the pool and gasp for air. I swim to the ladder, and grasp the bars and exit it. Wiping my face with a towel, I seat myself over at one of the restaurant chairs, mentally bring up the menu and pick one of the fruit juices. In the blue skies above, the sun is shining bringtly down on me. I suck on the yellowing liquid through a straw, relishing the taste.

"Yeah, I don't get it." I remarked to nobody in particular. I am not really displeased by this finding, but quite satisfied. Programming is an act of contructing a mental model and then implementing it. If you have a good mental model, you can run the program in your head in an approximate manner. This how programmers do testing, by comparing how the program actual runs to what their mental model says it should do. Any deviations between the mental model and reality are bugs.

That having said even if I have the code in front of me, it does not mean I understand what the mental model should be. What makes programming AIs so difficult is that running these models mentally is impossible for a human due to their complexity.

Still, that doesn't mean that all hope is lost. The modules making up the brain are less than 10k lines of code in total, and they are still made out of regular operations. Arithmetic, loop, branches, matrix multiplications...the individual pieces themselves can be understood, and modified.

On its face the process of intelligence improvement is simple, I have this code and the parameters for it, and I have to replace it with something better. But since I can't anticipate the results of my modifications, I can't use the regular methods of programming to do it. Instead I can take my own model and compare it with a modified one. But I do not know how to do the modifications myself either, the code is made up of various kinds of complex multiplicative update rules. I could have never come up with them. The modules are also concurrent as well which makes things even more difficult.

According to the guide, what I need to do is sidestep all this difficulty. What I am going to do is convert all this code to an AST that could be run on an interpreter. Then I am going to make use of various kinds of genetic programming and evolutionary methods to find the next step. Instead of focusing my inadequate intellect and programming skills on the process of mental improvement itself, I will automate it. I'll also focus my programming skills on making simplified environments, real games are too time intensive for this kind of task. The core is fast, but it can use parallelism can only get one so far. There will always be a cost associated with complexity.

The way ML research used to be done is that the researchers would use their big brains to come up with an on their own idea and then test it. The process was manual and impossible to automate. The reason for that is because the hardware was insufficient. It is not possible to do this kind of research unless you have a device capable of massive and modular concurrency. The old CPUs and GPUs were made for sequential programming, and it is fair to say that their concurrency was tacked on.

Figuring out what the brain does also used to be a big deal, and now I have it. I know what what modules are responsible for behavior, which for prediction, and I know the algorithms. But knowing what the brain does is not really what is important, what is important is being able to improve upon it. To understand that one needs to follow the proper process rather than try to rack his brains. With the right process even if one does not know the right algorithms, with sufficiently powerful hardware it is not difficult to infer them.

Imagine that I didn't have all this algorithmic knowledge, and I was making something like a poker bot so I can rock the online gambling dens. There is an evolutionary path I could follow in my programming. I could start with a simple rules based model. This would be quite weak, but then I could bring in evolutionary methods to optimize the parameters to a degree that would be impossible by hand. That approach would still be limited, so at that point I'd bring in neural nets to act as predictors and memory systems.

This roughly matches how evolution did it. Insects for example have little memory, and act more like rules based programs. But humans on the other hand rely massively on their memory.

At this point I'd run into trouble. The backprop based nets are very unstable in RL settings and can't be the basis of proper memory systems.

If you do not have hardware sufficiently powerful to infer its own programs, then the only choice is to just know what algorithms are right by peering into the future. Realistically what would happen is that I'd just end up bashing my head aginst the wall in that case. But if one has the right hardware, the brain cores, it is only a matter of programming effort to design an automated system for inferring a learning program. Those learning programs can then be studied, and primitive modular pieces can be extracted from them and used to improve the automated system. It is virtuous cycle that will lead me to ever greater heights.

That is what I am going to focus on. The old style of research is a waste of time and is only good for writing ML papers.

Therefore, my next step will be to revisit those old evolutionary algorithms. Most of them were discovered in the 20th century at a time when computers were nothing more than toys. Now is their time to shine!

I emerge from my thoughts, finish the third drink, toss it over the side and get ready for action. I get up from my seat, and make way into my bedroom ready for battle!

I spend a couple of months of virtual time just playing around and studying these algorithms, making some simplified agents. I've never really programmed so intently up to now, and I really felt my functional programming skills growing in that time. For PL related work like what I am going to be doing, functional programming really is the best choice. I feel if could spend a couple of more years, really focused on just these programming tasks, I could grow immensely as a programmer even without mental modifications. That should easily happen. Hell, by the time the weekend is over in the real world, I'll probably have good enough skills to become a pro programmer either way. At that point the original could fork me a million times and put me to work on cornering the programming market.

During this time only half an hour has passed in the real world.

(Helix Studio, The Street of Death)

...

$$$

12:50pm. Let me stop here for a bit. As I said, it is really easy to write this. What was hindering me was my mental state and attitude. I need to internalize it - for the next coupld of months, there is no need to think about anything other that writing. If I get a surprise offer from Tenstorrent, it can wait. Nothing matters other than writing. Jobs can wait for a few years, startups are not going to disappear off the map.

There will always be time for me to get back to programming later.

Being able to write Heaven's Key is not my punishment, but my reward. I can just take it easy and get those viewer counts up. I have the most important thing any writer needs, a personal belief system that can be shared with others. Now that I do, it is just a matter of having some fun.

This could be the ideal fun - knowing what life is about, making it into a profitable hobby, and working on whatever you want personally."

---
## [giordano/BinaryBuilderBase.jl](https://github.com/giordano/BinaryBuilderBase.jl)@[cf90fb4377...](https://github.com/giordano/BinaryBuilderBase.jl/commit/cf90fb437738ecc8495b9ac150c7e8436f3110e2)
#### Monday 2022-08-29 11:36:43 by Keno Fischer

Add support for building sanitizer-enabled jlls

This adds support for automatically adding the appropriate `-fsanitize=`
flags when the platform includes a `sanitizer` tag. This is particularly
intended for msan, which requires that all .so's in the system are built
using it, but could be useful for other sanitizers also.

There's a couple annoyances. One is that we don't currently actually ship
the sanitizer runtime libraries in our rootfs. Thus, if we want to start
using this, we'd have to add a BuildDependency on LLVMCompilerRT_jll and
manually copy the runtime libraries into place. Not the end of the world,
but certainly a wart.

The other issue is that `platform_matches` (which is defined in Base) of
course currently ignores the `sanitizer` tag. In theory it is possible
to add a custom compare strategy, but since we're specifying the target
by triplet, we can't really add that. Easy enough to add manually here,
but does make me wonder whether the custom compare strategies in Base
actually fit the use case.

---
## [hamdi-bahloul/Heart-disease-predictions](https://github.com/hamdi-bahloul/Heart-disease-predictions)@[9df1144e12...](https://github.com/hamdi-bahloul/Heart-disease-predictions/commit/9df1144e127bbeb233213c1d40ae63c4f10d4c78)
#### Monday 2022-08-29 12:00:25 by Hamdi Bahloul

Add files via upload

Data description : 
age: The person's age in years
sex: The person's sex (1 = male, 0 = female)
cp: The chest pain experienced (Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic)
trestbps: The person's resting blood pressure (mm Hg on admission to the hospital)
chol: The person's cholesterol measurement in mg/dl
fbs: The person's fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)
restecg: Resting electrocardiographic measurement (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria)
thalach: The person's maximum heart rate achieved
exang: Exercise induced angina (1 = yes; 0 = no)
oldpeak: ST depression induced by exercise relative to rest ('ST' relates to positions on the ECG plot. See more here)
slope: the slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping)
ca: The number of major vessels (0-3)
thal: A blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)
target: Heart disease (0 = no, 1 = yes)

---
## [turtle0x1/LxdMosaic](https://github.com/turtle0x1/LxdMosaic)@[a906d78221...](https://github.com/turtle0x1/LxdMosaic/commit/a906d782218f53d5a41f98078ccbdf06b368de3d)
#### Monday 2022-08-29 12:18:35 by turtle0x1

Remove deprecated /deploymentProgress/:deploymentId route from event.js

Removes;
  - `vendor` phone-home string from deployments
  - deploymentProgress/:deploymentId route from event.js

Its a route that doesn't require authentication that could be abused,
really it should be allowed to stay but this commit removes all the code
at once so it could be undone.

The rational behind it is that once a cloud-init is done running
its an endpoint that can be called to say "yes im done setting up".

Its a route that cant really ever have auth on it, but;
 - We have no security docs warning about it (its not a real vuln)
 - Deployments is kinda dead, it needs an overhall
 - The code it called had been removed before and this was just a stub

This is a shame because I remeber the pain of getting it working, but
that will teach me to push code that isn't ready!

---
## [KassuK1/Paragon](https://github.com/KassuK1/Paragon)@[42c4f6e3e3...](https://github.com/KassuK1/Paragon/commit/42c4f6e3e385243ef7bb3f60da40e77200bea443)
#### Monday 2022-08-29 12:25:31 by Wolfsurge

Remove stupid FPS limit when in GUIs (fuck notch's shitcode)

---
## [CogPlatform/Psychtoolbox-3](https://github.com/CogPlatform/Psychtoolbox-3)@[c4e7808150...](https://github.com/CogPlatform/Psychtoolbox-3/commit/c4e7808150009caa232767696d32f91063b4f2e4)
#### Monday 2022-08-29 12:32:46 by kleinerm

Merge pull request #775 from kleinerm/master

Pull for 3.0.18.11 update

This is mostly a release with smaller quality of life improvements, some bug/compatibility fixes, and more work to take advantage of new Ubuntu 22.04-LTS features and improvements.

### General

- Various help text and documentation updates. Minor cleanups and improvements, maintenance work etc.

- PsychVRHMD: Prep work for future OpenXR driver, and some cleanups and minor fixes.

- PsychPortAudio: Add new AM modulator flag 256 "kPortAudioAMModulatorNeutralIsZero". By default, a stopped AM modulator device acts as if no AM modulator is attached. With this flag set, while attached to an audio output slave device, it will instead "gate" or "mute" sound output on its associated audio output device, iow. the AM gain value during stopped modulator is zero instead of one. This has proven useful to allow to output tone bursts that are windowed/gated/modulated by an envelope function. Sponsored by a paid support membership - Thanks.

- Eyelink: Fix potential false "buffer overflow" alert in 'EyelinkGetQueuedData', which can cause Octave/Matlab to abort() as a false alarm. Sponsored by SR-Research, paying members of our partnership program - Thanks.

### Linux

- XOrgConfCreator: Split up into a legacy version for systems with X-Server 1.20 and earlier, e.g., Ubuntu 20.04-LTS, and a modern version for systems with X-Server 21 and later, e.g., Ubuntu 22.04-LTS. The legacy version is now in maintenance mode, frozen in its behaviour for old systems. The X-Server 21 / Ubuntu 22.04-LTS version was cleaned up, extended and made more plug and play. It hides some rarely needed (for normal users) options behind a "expert mode" flag, simplifies the questions it asks to users, streamlines the whole setup experience, and exposes some new functionality only available on modern X-Server 21, e.g., AsyncFlipSecondaries support for clone/mirror display setups (subject + experimenter displays) which are not synchronized. Improvements to deep color setup, Prime renderoffload "Optimus" setup, VRR setup etc.

- Deal better with problems in AssertOpenGL, giving better troubleshooting advice -- now updated for Ubuntu 22.04-LTS

- Gamepad/GetGamepadIndices: Refinements for Linux/X11, help text updates. Make selection of the proper GamePad / Joystick device more simple and robust. This work supported by a Psychtoolbox paid support membership - Thanks.

### macOS

- PsychVulkan: Add a new workaround for another macOS Metal bug. Make visual presentation timing it a bit better, but still quite awful.

- Screen('AddFrameToMovie'): Change mapping of 'rect' to actual capture area. The old math didn't determine vertical start position of the capture rectangle by rect(kPsychTop), but based on rect(kPsychBottom), which could cause inconsistencies on movie frame capture area on macOS with Retina displays in Retina backwards compatibility mode. The new math fixes this, to deal with Retina displays better.

- Maybe restore backwards compatibility of Psychtoolbox 3.0.18 with macOS versions older than 10.15 Catalina, possibly back to 10.11 El Capitan with fixes to Screen and PsychPortAudio. This is untested, due to lack of any macOS test systems other than 10.15.7 Catalina final, but may work. Maintaining backwards compatibility is difficult without test systems and the constant breakage introduced by the iToys company in more recent SDK's and compiler toolchains. Officially we don't guarantee that current 3.0.18 runs on anything but Catalina.

---
## [CogPlatform/Psychtoolbox-3](https://github.com/CogPlatform/Psychtoolbox-3)@[94cbeffbfb...](https://github.com/CogPlatform/Psychtoolbox-3/commit/94cbeffbfbe92000cda9af106e9b8b30a96d4e26)
#### Monday 2022-08-29 12:32:46 by Mario Kleiner

PsychLinuxConfiguration: Add workarounds for RaspberryPi OS 11 Mesa v3d.

Testing after upgrading the RPi 400 to Raspbian 11 showed new trouble:

At least on Mesa's gallium v3d driver for the RPi 4/400's VideoCore 6
gpu, Raspbian 11 Bullseye, page-flipping is broken by default - again.
Pageflipping for fullscreen OpenGL PTB onscreen windows fails, with
error messages flooding the XOrg log, and the copyswap fallback causes
PTB timing failures and horrible tearing.

The RPi desktop GUI composited by the Mutter X11 desktop compositor
doesn't have that problem, because Mesa for Raspbian 11 was patched
with some out-of-tree downstream patches to accept a new secret
parameter "v3d_maintain_ignorable_scanout" that if set to true allows
to fix pageflipping, but defaults to false == broken. God knows why
"broken by default" was considered an appropriate config choice, but
here we are...

Reference link to the patch series, which is not to be found anywhere
else with a Google search, and not yet in Mesa main upstream:

https://gitlab.freedesktop.org/mesa/mesa/-/issues/6079
https://github.com/bluestang2006/Debian-Pkgs/tree/master/mesa/debian/patches

This adds the magic parameter to fix pageflipping for octave + PTB
to the deep color config file and updates PsychLinuxConfiguration to
always force-install/update that file on ARM systems. I'm too lazy
to add extra config files and revalidate stuff, so we stuff it into
an unrelated Mesa config file.

This should fix PTB on RPi OS 11 on RPi 4/400.

---
## [victorblasco/factorial-dotfiles](https://github.com/victorblasco/factorial-dotfiles)@[277b8a2c09...](https://github.com/victorblasco/factorial-dotfiles/commit/277b8a2c0904e13000f5a6ea713bd92d2f32fb48)
#### Monday 2022-08-29 13:55:37 by Pau Ramon Revilla

Disable snippets (#16)

This one is controversial and I will understand if you don't want to
merge it (I will branch if that's the case).

I hate snippets. I never use them and they get in my way. Maybe they are
wrongly configured, but the amount of times that I get snippets when I
don't want them is just a waste of time.

Examples:
  - Sometimes I want to move from `{}` to `do/end` and when I place the
    cursor on `{` and type `do<Enter>` I automatically get an annoying
    `end` that I have to delete imediately.
  - Sometimes I want to press `<Enter>` after a `{` and it will add
    ruby block parameters for no reason.

Do you use them? How do you workaround things getting in the middle when
you don't want them? It screws up my muscle memory.

---
## [simar0at/heroku-buildpack-python](https://github.com/simar0at/heroku-buildpack-python)@[b2dfe7397b...](https://github.com/simar0at/heroku-buildpack-python/commit/b2dfe7397bf2f57b70799954277dd01a9c034432)
#### Monday 2022-08-29 14:46:51 by Ed Morley

Update path rewriting to support setuptools v64's PEP660 editable install mode (#1357)

On Heroku, the application source directory exists at a different path at build time (`/tmp/build_<hash>`), than it does at runtime (`/app`). As such, the buildpack has to perform path rewriting via `.profile.d` scripts at runtime, to ensure any packaging related absolute paths in the build output are rewritten to reference the new path. (Thankfully this awful path rewriting will no longer be necessary in the future with CNBs.)

Previously the only files this path rewriting needed to update were the `*.pth` and `*.egg-link` files in `site-packages` created by setuptools when performing editable installs.

However setuptools v64 added support for PEP660 based editable install hooks:
https://setuptools.pypa.io/en/latest/history.html#v64-0-0
https://peps.python.org/pep-0660/

This feature is only used for projects that have a `pyproject.toml`, and for such projects, [if the config is deemed complex enough](https://github.com/pypa/setuptools/blob/d03da04e024ad4289342077eef6de40013630a44/setuptools/command/editable_wheel.py#L359-L368), setuptools creates a new [finder script](https://github.com/pypa/setuptools/blob/23d455c532fca91e6f00aa5950000739b058b6e5/setuptools/command/editable_wheel.py#L740-L809) in `site-packages` that dynamically handles package resolution. (Simpler configs get a static `.pth` file, which works fine with our existing path rewriting.)

This new file embeds the absolute path of the source directory at build time, so must be rewritten too. It has a filename of form: `__editable___my_package_0_0_1_finder.py`

As such, this PR adds support for rewriting these files, along with updated test fixtures to provide coverage of `pyproject.toml` based editable installs (alongside the existing `setup.py` based test fixture).

Whilst writing the new test, I encountered a difference in behaviour with setuptool's new editable install mode, which meant the fixtures had to be nested inside a `packages/` directory in order to avoid an `ImportError` due to the fact that the Python buildpack currently sets `PYTHONPATH=/app` at runtime. See:
https://github.com/pypa/setuptools/issues/3535

Note:
- The Python buildpack doesn't yet globally install this newer setuptools v64 release, since by design it pins to a specific version to prevent upstream changes from breaking apps overnight. (The version was recently updated to 63.4.3 in #1344.)
- However, for packages that have a `pyproject.toml` pip uses the approach described in PEP518, which uses an [isolated build environment](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/#build-isolation). This environment typically pulls in latest setuptools (though this is controllable by the package owner via `[build-system]` in `pyproject.toml`), overriding our pinned global setuptools install.
- As such, even though we're not using v64 globally, users can still be broken by the upstream release.

A big thanks to @mrcljx for the initial PR in #1355 on which this was based :-)

Closes #1355.
GUS-W-11608693.

Co-authored-by: Marcel Jackwerth <marceljackwerth@gmail.com>

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[7fbe7ef5eb...](https://github.com/canalplus/rx-player/commit/7fbe7ef5eb409e59f60584bde2a4ab31a461440b)
#### Monday 2022-08-29 14:47:41 by Paul Berberian

Add magic Jest config property to Make Unit Tests Work Again (MUTWA)

It seems that Jest 28+, for some obscure reasons, now fail importing
dependencies using a ESM-style importing/exporting syntax - despite it
working before. It wasn't in their migration guide nor in their
changelog, so it was difficult to find how to work-around that issue.

In the end, I did what any developer who want to get things done should
do and just browsed the web to test every options under the sun that
could fix the issue.
Turns out the one in this commit has a good effect, though god knows
what it's actually doing!

Thanks https://www.sobyte.net/post/2022-06/jest/ to give me this hint,
and for apparently understanding what you're doing.

I am personally decidedly 2dumb4jest, which slowly leads me to dislike
this library very much for consequentially purely ego reasons.

---
## [Lulalaby/MikuSharp](https://github.com/Lulalaby/MikuSharp)@[917f852b1c...](https://github.com/Lulalaby/MikuSharp/commit/917f852b1ca6edc86a01b05e999c31396ecff935)
#### Monday 2022-08-29 15:14:09 by Lala Sabathil

Translation stuff

x

fix again

stuff

load translations from in/

make entities public

New icon and base translator app

Update MainWindow.xaml

stuff

short

x

save stuff

upgrade to .net6

add folder creation

fuck it

fff

file scope!!

Update MainWindow.xaml.cs

remove backup

update csproj

Bumb min windows version to 10.0.19041.0
Add metadata

stuff

stuff

remove entities and enums, we use dcs

save progress

change to dcs namespace

Remove miku images, this package will be part of dcs

re-add dcs projects

save stuff, i hate my life

new images for ac_cmds

---
## [postgres/postgres](https://github.com/postgres/postgres)@[7fed801135...](https://github.com/postgres/postgres/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Monday 2022-08-29 17:56:06 by Tom Lane

Clean up inconsistent use of fflush().

More than twenty years ago (79fcde48b), we hacked the postmaster
to avoid a core-dump on systems that didn't support fflush(NULL).
We've mostly, though not completely, hewed to that rule ever since.
But such systems are surely gone in the wild, so in the spirit of
cleaning out no-longer-needed portability hacks let's get rid of
multiple per-file fflush() calls in favor of using fflush(NULL).

Also, we were fairly inconsistent about whether to fflush() before
popen() and system() calls.  While we've received no bug reports
about that, it seems likely that at least some of these call sites
are at risk of odd behavior, such as error messages appearing in
an unexpected order.  Rather than expend a lot of brain cells
figuring out which places are at hazard, let's just establish a
uniform coding rule that we should fflush(NULL) before these calls.
A no-op fflush() is surely of trivial cost compared to launching
a sub-process via a shell; while if it's not a no-op then we likely
need it.

Discussion: https://postgr.es/m/2923412.1661722825@sss.pgh.pa.us

---
## [npmiller/llvm](https://github.com/npmiller/llvm)@[15f3cd6bfc...](https://github.com/npmiller/llvm/commit/15f3cd6bfc670ba6106184a903eb04be059e5977)
#### Monday 2022-08-29 18:14:31 by Matheus Izvekov

[clang] Implement ElaboratedType sugaring for types written bare

Without this patch, clang will not wrap in an ElaboratedType node types written
without a keyword and nested name qualifier, which goes against the intent that
we should produce an AST which retains enough details to recover how things are
written.

The lack of this sugar is incompatible with the intent of the type printer
default policy, which is to print types as written, but to fall back and print
them fully qualified when they are desugared.

An ElaboratedTypeLoc without keyword / NNS uses no storage by itself, but still
requires pointer alignment due to pre-existing bug in the TypeLoc buffer
handling.

---

Troubleshooting list to deal with any breakage seen with this patch:

1) The most likely effect one would see by this patch is a change in how
   a type is printed. The type printer will, by design and default,
   print types as written. There are customization options there, but
   not that many, and they mainly apply to how to print a type that we
   somehow failed to track how it was written. This patch fixes a
   problem where we failed to distinguish between a type
   that was written without any elaborated-type qualifiers,
   such as a 'struct'/'class' tags and name spacifiers such as 'std::',
   and one that has been stripped of any 'metadata' that identifies such,
   the so called canonical types.
   Example:
   ```
   namespace foo {
     struct A {};
     A a;
   };
   ```
   If one were to print the type of `foo::a`, prior to this patch, this
   would result in `foo::A`. This is how the type printer would have,
   by default, printed the canonical type of A as well.
   As soon as you add any name qualifiers to A, the type printer would
   suddenly start accurately printing the type as written. This patch
   will make it print it accurately even when written without
   qualifiers, so we will just print `A` for the initial example, as
   the user did not really write that `foo::` namespace qualifier.

2) This patch could expose a bug in some AST matcher. Matching types
   is harder to get right when there is sugar involved. For example,
   if you want to match a type against being a pointer to some type A,
   then you have to account for getting a type that is sugar for a
   pointer to A, or being a pointer to sugar to A, or both! Usually
   you would get the second part wrong, and this would work for a
   very simple test where you don't use any name qualifiers, but
   you would discover is broken when you do. The usual fix is to
   either use the matcher which strips sugar, which is annoying
   to use as for example if you match an N level pointer, you have
   to put N+1 such matchers in there, beginning to end and between
   all those levels. But in a lot of cases, if the property you want
   to match is present in the canonical type, it's easier and faster
   to just match on that... This goes with what is said in 1), if
   you want to match against the name of a type, and you want
   the name string to be something stable, perhaps matching on
   the name of the canonical type is the better choice.

3) This patch could expose a bug in how you get the source range of some
   TypeLoc. For some reason, a lot of code is using getLocalSourceRange(),
   which only looks at the given TypeLoc node. This patch introduces a new,
   and more common TypeLoc node which contains no source locations on itself.
   This is not an inovation here, and some other, more rare TypeLoc nodes could
   also have this property, but if you use getLocalSourceRange on them, it's not
   going to return any valid locations, because it doesn't have any. The right fix
   here is to always use getSourceRange() or getBeginLoc/getEndLoc which will dive
   into the inner TypeLoc to get the source range if it doesn't find it on the
   top level one. You can use getLocalSourceRange if you are really into
   micro-optimizations and you have some outside knowledge that the TypeLocs you are
   dealing with will always include some source location.

4) Exposed a bug somewhere in the use of the normal clang type class API, where you
   have some type, you want to see if that type is some particular kind, you try a
   `dyn_cast` such as `dyn_cast<TypedefType>` and that fails because now you have an
   ElaboratedType which has a TypeDefType inside of it, which is what you wanted to match.
   Again, like 2), this would usually have been tested poorly with some simple tests with
   no qualifications, and would have been broken had there been any other kind of type sugar,
   be it an ElaboratedType or a TemplateSpecializationType or a SubstTemplateParmType.
   The usual fix here is to use `getAs` instead of `dyn_cast`, which will look deeper
   into the type. Or use `getAsAdjusted` when dealing with TypeLocs.
   For some reason the API is inconsistent there and on TypeLocs getAs behaves like a dyn_cast.

5) It could be a bug in this patch perhaps.

Let me know if you need any help!

Signed-off-by: Matheus Izvekov <mizvekov@gmail.com>

Differential Revision: https://reviews.llvm.org/D112374

---
## [vdbe/kubernetes-cluster](https://github.com/vdbe/kubernetes-cluster)@[9ee8433fa3...](https://github.com/vdbe/kubernetes-cluster/commit/9ee8433fa371b90ba75d2d5128cb1f514152c2fa)
#### Monday 2022-08-29 18:14:51 by ewoutvdb

This was painfull

Merge pull my finger request

Herping the derp

Revert "Herping the derp"

This reverts commit 5071e4d1bbeb9daf27f2ec0a27bc8b8465ce6227.

I must sleep... it's working... in just three hours...

harharhar

TDD: 1, Me: 0

I should get a raise for this.

Never gonna let you down

commit

Is there an achievement for this?

This bunny should be killed.

TOMEKWOJCIK, WE WENT OVER THIS. C++ IO SUCKS.

Revert "TOMEKWOJCIK, WE WENT OVER THIS. C++ IO SUCKS."

This reverts commit 1a32f61e2c6728c634594b5313d1753a3f2797ed.

I must have been drunk.

PEBKAC

Either Hot Shit or Total Bollocks

Fixed mispeling

tl;dr

oops

Update helm-release.yaml

clarify further the brokenness of C++. why the fuck are we using C++?

Corrected mistakes

Bit Bucket is down. What should I do now?

Fixed the fuck out of #48!

just trolling the repo

TODO: Fix later

Who knows...

forgot we're not using a smart language

bla

Finished fondling.

Revert "Finished fondling."

This reverts commit de1c5cbb8c0d5f93d3fec25f577c59ac64f94a37.

I __ a word

If it's hacky and you know it clap you hands (clap clap)!

Refactor factories, revisit visitors

fixed mistaken bug

The same thing we do every night, Pinky - try to take over the world!

Shit code!

ffs

I am Root. We are Root.

DAVID, WE WENT OVER THIS. C++ IO SUCKS.

permanent hack, do not revert

I should get a raise for this.

c&p fail

Revert "c&p fail"

This reverts commit ea0ff839d00fa3b2615a4fe44f9b819fe8c77851.

need another beer

Revert "need another beer"

This reverts commit 6b0d34b4a2712fd2a82434562706bcc4dd67f3f3.

extra debug for stuff module

Revert "extra debug for stuff module"

This reverts commit 053f752f98ef0c5f60acf32c30ac10d7a9b51fa8.

I was wrong...

yo recipes

fixed some minor stuff, might need some additional work.

I cannot believe that it took this long to write a test for this.

It was the best of times, it was the worst of times

did everything

To be honest, I do not quite remember everything I changed here today. But it is all good, I tell ya.

Herpderp, shoulda check if it does really compile.

Why The Fuck?

I have no idea what I'm doing here.

Working on WIP

Revert "Working on WIP"

This reverts commit a6f20fa5f799b9387df22c31a6f6a76748108ad9.

It's Working!

SHIT ===> GOLD

a few bits tried to escape, but we caught them

MOAR BIFURCATION

Never gonna give you up

syntax

Fixed Bug

Minor updates

Useful text

Revert "yo recipes"

This reverts commit 635bc68eb40682fe9b4eda9f463e32a730d0d437.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[a15855c39b...](https://github.com/pytorch/pytorch/commit/a15855c39b9178d7748d85ebc92a046fd28ae34d)
#### Monday 2022-08-29 18:37:31 by Andrew Gu

Update base for Update on "[FSDP] Generalize prefetching; lower unshard/reshard to handle"


### Additional Constructor Changes
- `self.sharding_strategy`
    - If the world size is 1, I clamp the sharding strategy to `NO_SHARD`, regardless of the passed-in sharding strategy, since the behavior is fully equivalent. This absolves the need for `p._is_sharded or self.world_size == 1` checks in the core code. Once we fully shift the paradigm to using handles, this should result in a clear net positive. However, for now, we still have some places where we interface directly with the `FlatParameter`, in which case we have some temporary hacky code.
- `HandleConfig`
    - As a part of the new design abstraction, much logic is lowered to the `FlatParamHandle`. This requires the handle be aware of mixed precision, CPU offloading, sharding strategy, and the process group (for world size > 1). To be less error-prone, I re-defined the `dataclass`s and `enum`s for the handle. These can be removed and coalesced with the existing ones.
    - The drawback is that the `FlattenParamsWrapper` constructor now takes in the `HandleConfig` to forward it to the `FlatParamHandle` constructor. I tolerate this since we plan to retire the FPW. For now, the handle's process group attributes are set later when we call `handle.shard()`.
    - We will dive into this logic lowering later. For now, the idea is we need to pass some extra info to the handle, which must go through the FPW.
- `FullyShardedDataParallel._shard_parameters()` -> `FlatParamHandle.shard()`
- [Important] Generalizing attributes to remove the 1 `FullyShardedDataParallel` : 1 `FlatParameter` assumption
    - **Before:** `_fsdp_graph_order`, `_pre_backward_hook_full_params_prefetched`, `_forward_full_params_prefetched`, `reshard_after_forward` are with respect to 1 `FullyShardedDataParallel`
    - **After:** (1) We use `FlatParamHandle` in place of `FullyShardedDataParallel`. (2) The atomic unit for forward and pre-backward is a _group_ of handles involved in the same module's forward/pre-backward. This is represented as `Tuple[FlatParamHandle, ...]`. For now, this is **always a singleton tuple**, but this shift enables a module having multiple FSDP parameters (which we have use cases for).
- `_reset_lazy_init()` attributes
    - The prefetched flags are merged into `self._handles_prefetched`, which is directly defined in the constructor. `reshard_after_forward` is retired since it can be fully determined by other attributes (`_is_root` and `sharding_strategy`).

## FSDP Runtime: Unshard

The first step is to read the existing `_rebuild_full_params()`. A few notable observations:
- It returns `Tuple[Tensor, bool]`. The first element is the _padded unsharded flattened parameter_, and the second element is whether we can free it upon exiting `summon_full_params()`. This return value is **only used in `summon_full_params()`**.
- If parameter mixed precision is enabled and the `FlatParameter` is already unsharded, then the low precision shard (`_mp_shard`) is still re-allocated on GPU. (It is freed at the end of the method.)
- If CPU offloading is enabled and the `FlatParameter` is already unsharded, then there is a no-op `p.data = p.data.to(self.compute_device, non_blocking=True)`.
- Inside `summon_full_params()`, `mixed_precision_cast_ran` is always `False`. Therefore, the return value for the `not p._is_sharded and mixed_precision_cast_ran` branch is unused.
-`summon_full_params()` can only be called (before forward or after backward) or (between forward and backward). Given this, I cannot think of a case where we call `summon_full_params()`, the `FlatParameter` is already unsharded, but `reshard_after_forward` is `True`. The `FlatParameter` should be sharded (before forward or after backward), and the `FlatParameter` may only be unsharded (between forward and backward) if `reshard_after_forward` is `False`.
- If parameter mixed precision is enabled and the sharding strategy is a sharded one, then inside `summon_full_params()`, the `FlatParameter` is unsharded in full precision. This involves allocating a new padded unsharded flattened parameter on GPU in full precision since `_full_param_padded` is in the low precision.

Some comments:
- Ideally, we reduce the complexity of the core code path: i.e. unshard for forward and pre-backward. If the return value is only used for `summon_full_params()`, we should consider if we can compartmentalize that logic.
- The branching is complex, and some return values are never used, where this fact is not immediately obvious. We should see if we can reduce the branch complexity.

Disclaimer: The difference in attribute semantics between `NO_SHARD` and the sharded strategies makes it challenging to unify the cases. This PR does not attempt to address that since it requires more design thought. However, it does attempt to reduce the complexity for the sharded strategies.

### Unshard: Core Code Path
Let us trace through the new logical unshard.
1. `FullyShardedDataParallel._unshard(self, handles: List[FlatParamHandle], prepare_gradient: bool)`
    - This iterates over the handles and calls `handle.pre_unshard()`, `handle.unshard()`, and `handle.post_unshard(prepare_gradient)` in the all-gather stream.
2. `FlatParamHandle.needs_unshard(self)`
    - We take an aside to look at this key subroutine.
    - For `NO_SHARD`, this returns `False`.
    - For sharded strategies, this checks if the padded unsharded flattened parameter is allocated. The padded unsharded flattened parameter is the base tensor for the unpadded unsharded flattened parameter, which is a view into the padded one. Thus, the padded one's allocation fully determines if the `FlatParameter` is unsharded.
    - For sharded strategies, to accommodate the parameter mixed precision + `summon_full_params()` case, we introduce `_full_prec_full_param_padded`, which is the padded unsharded flattened parameter in full precision. The helper `_get_padded_unsharded_flat_param()` takes care of this casing and returns the padded unsharded flattened parameter. Instead of allocating a new tensor each time, we manually manage `_full_prec_full_param_padded`'s storage just like for `_full_param_padded`.
3. `FlatParamHandle.pre_unshard(self)`
    - For sharded strategies, the postcondition is that the handle's `FlatParameter` points to the tensor to all-gather. This should be on the communication device and in the desired precision. The allocation and usage of the low precision shard for parameter mixed precision and the CPU -> GPU copy for CPU offloading both classify naturally in the pre-unshard.
    - For sharded strategies, if the `FlatParameter` does not need to be unsharded, `pre_unshard()` is a no-op. This avoids unnecessarily allocating and freeing the low precision shard.
    - For `NO_SHARD`, we simply preserve the existing semantics.
4. `FlatParamHandle.unshard(self)`
    - If the handle was resharded without freeing the padded unsharded flattened parameter (e.g. `summon_full_params()` between forward and backward when `reshard_after_forward=False`), then the `FlatParameter` points to the sharded flattened parameter. We need to switch to using the unsharded parameter. This is a design choice. Alternatively, we may not switch to using the sharded flattened parameter in `reshard()` if we do not free the padded unsharded flattened parameter. However, the postcondition that the `FlatParameter` points to the sharded flattened parameter after `reshard()` is helpful logically, so I prefer this approach.
    - Otherwise, this allocates the padded unsharded flattened parameter, all-gathers, and switches to using the unpadded unsharded flattened parameter.
    - In the future, we may add an option to `unshard()` that additionally all-gathers the gradient.
5. `FlatParamHandle.post_unshard(self, prepare_gradient: bool)`
    - For sharded strategies, if using parameter mixed precision, this frees the low precision shard. More generally, this should free any sharded allocations made in `pre_unshard()` since the all-gather has been launched. If using CPU offloading, the GPU copy of the local shard goes out of scope after `unshard()` and is able to be garbage collected. **We should understand if there is any performance difference between manually freeing versus deferring to garbage collection since our usage is inconsistent.** For now, I preserve the existing semantics here.
    - `prepare_gradient` is meant to be set to `True` for the pre-backward unshard and `False` for the forward unshard. This runs the equivalent logic of `_prep_grads_for_backward()`.
    - This post-unshard logic (notably the gradient preparation) now runs in the all-gather stream, which is fine because we always have the current stream wait for the all-gather stream immediately after `FullyShardedDataParallel._unshard()`. IIUC, we do not need to call `_mp_shard.record_stream(current_stream)` (where `current_stream` is the default stream) because `_mp_shard` is allocated and freed in the same (all-gather) stream.
    - A postcondition is that the `FlatParameter` is on the compute device. It should also have the unpadded unsharded size (though I do not have a check for this at the moment).

### Unshard: `summon_full_params()`
Now that we see how the logical unshard has been reorganized for the core code path, let us dive into `summon_full_params()`. 

The two constraints are:
1. If using parameter mixed precision, we should unshard in full precision.
2. We must determine if we should free the padded unsharded flattened parameter upon exiting.

The first constraint is addressed as described before in the core unshard code path, so it remains to explore the second constraint.

I propose a simple rule: **We free iff we actually unshard the `FlatParameter` in `summon_full_params()`** (i.e. it was not already unsharded). We perform a case analysis:

**Parameter mixed precision enabled:**
* `NO_SHARD`: `flat_param.data` points to `flat_param._local_shard`, which is the full precision unsharded flattened parameter. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We force full precision and all-gather to `_full_prec_full_param_padded`. We do not support `nested summon_full_params()`, so `_full_prec_full_param_padded` must be unallocated. We unshard, and it is **safe to free**.

**Parameter mixed precision disabled:**
* `NO_SHARD`: This is the same as with mixed precision enabled. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We all-gather to `_full_param_padded`. It may already be unsharded.
    * Already unsharded: The unshard is a no-op. This is **not safe to free**.
        * For `FULL_SHARD`, this can happen for the root FSDP instance after `forward()` but before backward.
        * For `SHARD_GRAD_OP`, this can happen for all FSDP instances after `forward()` but before backward.
    * Needs unshard: We unshard. This is **safe to free**.

Therefore, we see that it is not safe to free when using `NO_SHARD` and when using a sharded strategy but the `FlatParameter` is already unsharded. This is precisely the proposed rule.

There were two notable edge cases that the existing code did not address.
1. The existing code tests if the `FlatParameter` is already unsharded by checking the allocation status of `_full_param_padded`. When using parameter mixed precision, this is the incorrect tensor to check. If `_full_param_padded` is allocated (e.g. when `reshard_after_forward=False` and calling `summon_full_params()` between forward and backward), the already-unsharded check is a false positive, and `summon_full_params()` does not correctly force full precision. https://github.com/pytorch/pytorch/issues/83068
    - This PR's `needs_unshard()` check correctly routes to the appropriate padded unsharded flattened parameter depending on the calling context (i.e. if it needs to force full precision or not).
2. The existing code does not free the GPU copy of the padded unsharded flattened parameter when calling `summon_full_params(offload_to_cpu=True)`. It unshards the `FlatParameter`, moves the padded unsharded flattened parameter to CPU, and sets the `FlatParameter` data to be the appropriate unpadded view into the padded unsharded flattened parameter on CPU. However, `_full_param_padded` still points to the all-gathered padded unsharded flattened parameter on GPU, which is kept in memory. https://github.com/pytorch/pytorch/issues/83076
    - This PR frees the GPU copy and reallocates it upon exiting `summon_full_params()`. This is essential for avoiding peak GPU memory usage from increasing as we recurse through the module tree. There may be some cases where we can avoid reallocation altogether, but that can be addressed in a follow-up PR.
    - This PR offloads the *unpadded* unsharded flattened parameter to CPU directly instead of the *padded* one. As far as I can tell, there is no need to include the padding since unflattening the original parameters does not require the padding.
    - The relevant code is in the context manager `FlatParamHandle.to_cpu()`.

### Unshard: Mixed-Precision Stream

This PR removes the mixed precision stream usage. As is, I do not think there is any extra overlap being achieved by the stream usage.

The low precision shard is allocated and copied to in the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1401-L1412)), and the current stream (in this case the all-gather stream) waits for the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1414)). However, we immediately schedule an all-gather that communicates that exact low precision shard ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L3338)) with no other meaningful computation between. If we remove the mixed precision stream, the low precision shard is allocated and copied to in the all-gather stream (including the non-blocking CPU -> GPU copy if using CPU offloading). 

Under this PR's design, we may consider a "pre-unshard" stream for all logical pre-unshard data transfers if we want to overlap in the future. IIUC, the overlap opportunity exists if there are multiple `FlatParameter`s per module, and we only have the all-gather stream wait for the data transfer corresponding to the local shard it communicates, not the others.

If we agree on removing the mixed-precision stream for now, I will remember to delete it from `_init_streams()`.

## FSDP Runtime: Reshard

Like with unshard, the first step is the look at the existing `_free_full_params()` and `_use_param_local_shard()`. A few notable observations:
- For only `NO_SHARD`, `_free_full_params()` includes a call to `_free_mp_shard()`.
- For `summon_full_params()`, there is a separate `_free_full_params_and_use_local_shard()` that duplicates the main logic of `_free_full_params()` and calls `_use_param_local_shard()`.
- In `forward()`, if `reshard_after_forward=True`, we call `_free_full_params()` and then `_free_mp_shard()`. Hence, for `NO_SHARD`, the `_free_mp_shard()` is a no-op.
- In the post-backward hook, we typically call `_free_full_params()` and `_free_mp_shard()`. The `_free_mp_shard()` is a no-op for `NO_SHARD` and if `reshard_after_forward=True`.

Some comments:
- The code certainly works, but some of the no-ops are subtle. When possible, we should make it clear when calls are no-ops or not. It is good that the existing code documents that `_free_mp_shard()` is a no-op in the post-backward hook when `reshard_after_forward=True`. However, there are still some non-obvious no-ops (around `NO_SHARD`).
- We should see if we can avoid the duplicate `_free_full_params_and_use_local_shard()`.

Let us trace through the logical reshard:
1. `FullyShardedDataParallel._reshard(self, handles: List[FlatParamHandle], free_unsharded_flat_params: List[bool])`
    - The two args should have the same length since they are to be zipped.
    - The goal of having `free_unsharded_flat_params` is that the caller should be explicit about whether the (padded) unsharded flattened parameter should be freed. The low precision shard is always meant to be freed (as early as possible), so there is no corresponding `List[bool]`.
2. `FlatParamHandle.reshard(self, free_unsharded_flat_param: bool)`
    - This frees the (padded) unsharded flattened parameter if `free_unsharded_flat_param` and switches to using the sharded flattened parameter.
    - Echoing back to forcing full precision in `summon_full_params()`, `_free_unsharded_flat_param()` frees the correct tensor by using `_get_padded_unsharded_flat_parameter()`.
3. `FlatParamHandle.post_reshard(self)`
    - I am not fully content with the existence of this method, but this seems to be an unavoidable consequence of `NO_SHARD`. Perhaps, this may be useful in the future for other reasons though.
    - Right now, this method is only meaningful for `NO_SHARD` + parameter mixed precision + outside `summon_full_params()`. `_mp_shard` is not freed in the post-unshard since it is also the low precision _unsharded_ flattened parameter, so we must delay the free until the the post-reshard.

Below the `FlatParamHandle.reshard()` and `post_reshard()` layer, there should not be any no-ops.

One final comment I will mention is that I like the `pre_unshard()`, `unshard()`, `post_unshard()`, and `reshard()`, `post_reshard()` organization because it makes it clear what the boundaries are and their temporal relationship. Through that, we can set pre- and post-conditions. Furthermore, we can eventually convert logic to hooks that may be registered on the `FlatParamHandle` (for `pre_unshard()`, `post_unshard()`, and `post_reshard()`). This may improve the customizability of FSDP.

 ## FSDP Runtime: `forward()`

- This PR reorganizes `forward()` in preparation for non-recursive wrapping, which uses pre-forward and post-forward hooks that expect the signature `hook(module, input)`. For FSDP, the `module` and `input` arguments are not used.
- This PR creates a new method `_fsdp_root_pre_forward()` to handle the logic only the root FSDP should run.

## FSDP Prefetching

Finally, we dive into the prefetching changes. Some highlights:
1. This PR unifies the execution order validation and prefetching implementations.
    - Both involve the execution order and can be unified to share some boilerplate.
2. Execution order validation only runs when the distributed debug level is `INFO`.
    - We have yet to have one success case where we actually catch an unintended source of dynamism. The warning is also too verbose. Hence, we are gating it by the `INFO` level.
3. This PR moves prefetching to be with respect to groups of handles (as mentioned in the constructor comment).
    - This is essential for supporting prefetching with non-recursive wrapping.
4. This PR does not include "bubbles", i.e. modules with no handles, in the recorded execution order(s). This deviates from the existing implementation.
    - This makes prefetching possibly more aggressive (when there are such bubbles), but it should not have significant performance implications either way.
5. This PR changes backward prefetching to reset the post-forward order each iteration (as intended).
6. This PR changes forward prefetching to use the first iteration's pre-forward order instead of the first iteration's post-forward order. (We can discuss whether we want this in this PR or not. Otherwise, I can keep it as using the post-forward order to preserve the existing semantics.) This PR also removes the `all_gather_stream.wait_stream(current_stream)` before forward prefetching because it does not help with high GPU reserved memory. We can add that back if desired.


### Appendix
#### Reverse Post-Forward Order Is Not Always the Pre-Backward Order
The existing PT-D FSDP pre-backward prefetching uses the reverse post-forward order.
<details>
  <summary>Model Code</summary>

  ```
  class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=True),
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(4, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=False),
        )
        self.block3 = nn.Linear(12, 8)
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(4, 10),
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.head(x)

  model = Model().cuda()
  fsdp_kwargs = {}
  model.block1[1] = FSDP(model.block1[1], **fsdp_kwargs)  # BN2d
  model.block2[1] = FSDP(model.block2[1], **fsdp_kwargs)  # BN2d
  model.block1 = FSDP(model.block1, **fsdp_kwargs)
  model.block2 = FSDP(model.block2, **fsdp_kwargs)
  model.block3 = FSDP(model.block3, **fsdp_kwargs)
  model = FSDP(model, **fsdp_kwargs)
  ```
</details>

<details>
  <summary>Execution Orders </summary>

  ```
  Pre-backward hook for ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  Pre-backward hook for ('weight', 'bias') 140339461194656 (block3)
  Pre-backward hook for ('0.weight', '0.bias') 140339520589776 (block2)
  Pre-backward hook for ('weight', 'bias') 140339520587664 (block2 BN)
  Pre-backward hook for ('weight', 'bias') 140339520586656 (block1 BN)
  Pre-backward hook for ('0.weight', '0.bias') 140339520588768 (block1)
  
  Pre-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('weight', 'bias') 140339461194656 (block3)
  
  Reverse post-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('weight', 'bias') 140339461194656 (block3)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ```
</details>



[ghstack-poisoned]

---
## [8890q/android_kernel_samsung_universal8895](https://github.com/8890q/android_kernel_samsung_universal8895)@[a31048081b...](https://github.com/8890q/android_kernel_samsung_universal8895/commit/a31048081b7761388a5c6e3d9a247f9b75d9f262)
#### Monday 2022-08-29 19:13:45 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[3474173f74...](https://github.com/ammarfaizi2/linux-fork/commit/3474173f74466fad48cc3d5f7b88f70e9741062b)
#### Monday 2022-08-29 19:21:19 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Myphicbowser/40K-Eipharius](https://github.com/Myphicbowser/40K-Eipharius)@[ebdba9844a...](https://github.com/Myphicbowser/40K-Eipharius/commit/ebdba9844a54549b22d7b4c722eb58b5da61042e)
#### Monday 2022-08-29 19:36:40 by Myphicbowser

Various Fixes and Lights

Turned some Space Panels into Snow Panels on the Mountain Level

Deleted a Duplicate Fire Alarm in Virology

Added some FUCKING LIGHTS HOLY SHIT WHY ARE SOME AREAS SO FUCKING DARK

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[b5d2ec203c...](https://github.com/san7890/bruhstation/commit/b5d2ec203c204c790805bbb6ce0dc531f8fe5ef0)
#### Monday 2022-08-29 19:58:18 by san7890

Fauna Containment Specialists - Emergency Necessities

Hey there,

As an admin, it recently came up that fauna from lavaland keeps flooding the station and killing the entire crew. However, none of the tools in my arsenal of ERT Teams has any competencies with killing these types of creatures since they all focus on laser/ballistics. So, let's fight them with what they were balanced to fit.

Introducing: *Fauna Containment Specialists*. Don't let the name fool you, they are designed to neutralized all threats of fauna onboard the station. They're given gear you would typically afford to a miner, and a little bit extra on top to  help manage their get-up-and-go-kill-that-fucking-beast nature. It is a bit overpowered, but it's designed that way since it is an _admin ERT_ after all. It's meant to scale up pretty nicely, and isn't a traditional "team", just a bunch of specialists who are all presumably competent.

The stuff they do get is a titch overpowered, but it's not meant to be something that you can roll over with (like giving them fucking pulse rifles or instagib lasers). It took me a bit of a struggle to beat a broodmother solo with this (I am low on skill), but I think it's weighted properly, especially considering that it is an admin-only event.

---
## [hayley-leblanc/linux](https://github.com/hayley-leblanc/linux)@[4a557a5d1a...](https://github.com/hayley-leblanc/linux/commit/4a557a5d1a6145ea586dc9b17a9b4e5190c9c017)
#### Monday 2022-08-29 20:56:27 by Linus Torvalds

sparse: introduce conditional lock acquire function attribute

The kernel tends to try to avoid conditional locking semantics because
it makes it harder to think about and statically check locking rules,
but we do have a few fundamental locking primitives that take locks
conditionally - most obviously the 'trylock' functions.

That has always been a problem for 'sparse' checking for locking
imbalance, and we've had a special '__cond_lock()' macro that we've used
to let sparse know how the locking works:

    # define __cond_lock(x,c)        ((c) ? ({ __acquire(x); 1; }) : 0)

so that you can then use this to tell sparse that (for example) the
spinlock trylock macro ends up acquiring the lock when it succeeds, but
not when it fails:

    #define raw_spin_trylock(lock)  __cond_lock(lock, _raw_spin_trylock(lock))

and then sparse can follow along the locking rules when you have code like

        if (!spin_trylock(&dentry->d_lock))
                return LRU_SKIP;
	.. sparse sees that the lock is held here..
        spin_unlock(&dentry->d_lock);

and sparse ends up happy about the lock contexts.

However, this '__cond_lock()' use does result in very ugly header files,
and requires you to basically wrap the real function with that macro
that uses '__cond_lock'.  Which has made PeterZ NAK things that try to
fix sparse warnings over the years [1].

To solve this, there is now a very experimental patch to sparse that
basically does the exact same thing as '__cond_lock()' did, but using a
function attribute instead.  That seems to make PeterZ happy [2].

Note that this does not replace existing use of '__cond_lock()', but
only exposes the new proposed attribute and uses it for the previously
unannotated 'refcount_dec_and_lock()' family of functions.

For existing sparse installations, this will make no difference (a
negative output context was ignored), but if you have the experimental
sparse patch it will make sparse now understand code that uses those
functions, the same way '__cond_lock()' makes sparse understand the very
similar 'atomic_dec_and_lock()' uses that have the old '__cond_lock()'
annotations.

Note that in some cases this will silence existing context imbalance
warnings.  But in other cases it may end up exposing new sparse warnings
for code that sparse just didn't see the locking for at all before.

This is a trial, in other words.  I'd expect that if it ends up being
successful, and new sparse releases end up having this new attribute,
we'll migrate the old-style '__cond_lock()' users to use the new-style
'__cond_acquires' function attribute.

The actual experimental sparse patch was posted in [3].

Link: https://lore.kernel.org/all/20130930134434.GC12926@twins.programming.kicks-ass.net/ [1]
Link: https://lore.kernel.org/all/Yr60tWxN4P568x3W@worktop.programming.kicks-ass.net/ [2]
Link: https://lore.kernel.org/all/CAHk-=wjZfO9hGqJ2_hGQG3U_XzSh9_XaXze=HgPdvJbgrvASfA@mail.gmail.com/ [3]
Acked-by: Peter Zijlstra <peterz@infradead.org>
Cc: Alexander Aring <aahringo@redhat.com>
Cc: Luc Van Oostenryck <luc.vanoostenryck@gmail.com>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [bukka/php-src](https://github.com/bukka/php-src)@[128768a450...](https://github.com/bukka/php-src/commit/128768a4503c8bc5c6ccf564061f9dc8b307f57f)
#### Monday 2022-08-29 21:45:16 by Alex Dowad

Adjust number of error markers emitted for truncated UTF-8 code units

In 04e59c916f, I amended the UTF-8 conversion code, so that when given
invalid input, it would emit a number of errors markers harmonizing
with the WHATWG's specification of the standard UTF-8 decoding
algorithm. (Which, gentle reader of commit logs, you can find online
at https://encoding.spec.whatwg.org/#utf-8-decoder.) However, the code
in 04e59c916f was faulty in the case that a truncated UTF-8 code unit
starts with 0xF1.

Then, in dc1ba61d09, when making a small refactoring to a different
part of the UTF-8 conversion code, I inexplicably broke part of the
working code, causing the same fault which was already present with
truncated UTF-8 code units starting with 0xF1 to also occur with
0xF2 and 0xF3 as well. I don't remember what inane thoughts I was
thinking when I pulled off this feat of utter mental confusion.

None of these cases were covered by unit tests, by the way.

Thankfully, my trusty fuzzer picked up on this when testing the
new implementation of mb_parse_str (since the legacy UTF-8
conversion filter did not suffer from the same problem, and I was
fuzzing to find any differences in behavior between the old and
new implementations).

Fortuitously, the fuzzer also picked up another issue which was
present in 04e59c916f. I was emitting only one error marker for
truncated code units starting with 0xE0 or 0xED, in cases where
the WHATWG standard indicates two should be emitted. Examples
are 0xE0 0x9F <END OF STRING> or 0xED 0xA0 <END OF STRING>.

Code units starting with 0xE0-0xED should have 3 bytes. If the
first byte is 0xE0, the second MUST be 0xA0 or greater. (Otherwise,
the codepoint could have fit in a two-byte code unit.) And if the
first byte is 0xED, the second MUST be 0x9F or less. According to
the WHATWG algorithm, step 4, if the second byte is outside the
legal range, then the decoder should emit an error... AND
reprocess the out-of-range byte. The reprocessing will then
cause another error. That's why the decoder should indicate two
errors and not one.

---
## [Physolia/git](https://github.com/Physolia/git)@[5beca49a0b...](https://github.com/Physolia/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Monday 2022-08-29 21:58:28 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [obamasolutions/obama.solutions](https://github.com/obamasolutions/obama.solutions)@[cfc0670e22...](https://github.com/obamasolutions/obama.solutions/commit/cfc0670e2233deaa9316a6d0793e4cfa2d7ebd15)
#### Monday 2022-08-29 22:13:13 by kris null

Start a template for ~nicoleaoki

Also introducing the Nikoki insignia/watermark as the favicon, it's extremely simple but I'm now taking this 3x3 pixel art as my signature so fuck you.

---
## [andreoss/melpa](https://github.com/andreoss/melpa)@[570bde6b4b...](https://github.com/andreoss/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Monday 2022-08-29 22:53:50 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[cb80069a23...](https://github.com/LemonInTheDark/tgstation/commit/cb80069a23da101172ec4be8df191db955c5ca59)
#### Monday 2022-08-29 22:54:37 by LemonInTheDark

Saves 50% of build_coordinate's time

Micro optimizing go brrrrr
I made turf_blacklist an assoc list rather then just a normal one, so
lookups are O(log n) instead of O(n). Also it's faster for the base case
of loading mostly space.

Instead of toggling the map loader right before and right after New()
calls, we toggle at the start of mapload, and disable then reenable if
we check tick. This saves like 0.3 seconds

Rather then tracking an area cache ourselves, and needing to pass it
around, we use a locally static list to reference the global list of
area -> type. This is much faster, if slightly fragile.

Rather then checking for a null turf at every line, we do it at the
start of the proc and not after. Faster this way, tho it can in theory
drop area vvs.

Avoids calling world.preloader_setup unless we actually have a unique
set of attributes. We use another static list to make this comparison
cheap. This saves another 0.3

Rather then checking for area paths in the turf logic, or vis versa, we
assume we are creating the type implied by the index we're reading off.
So only the last type entry will be loaded like a turf, etc.
This is slightly unsafe but saves a good bit of time, and will properly
error on fucked maps.

Also, rather then using a datum to hold preloader vars, we use 2 global
variables. This is faster.

This marks the end of my optimizations for direct maploading. I've
reduced the cost of loading a map by more then 50% now. Get owned.

---
## [consilio-org/documentation](https://github.com/consilio-org/documentation)@[8c78d740cb...](https://github.com/consilio-org/documentation/commit/8c78d740cb22d7f6f085a3c8340dbe47886a52d5)
#### Monday 2022-08-29 22:58:43 by LandenStephenss

stupid fucking json and it's stupid ass no comment fucking stupid idiot moron hellfire rained down upon you idiot poop dead

---
## [Curly68/furnace](https://github.com/Curly68/furnace)@[e26ff43ccc...](https://github.com/Curly68/furnace/commit/e26ff43ccc8d475fcd6eea391c696f16c2e13365)
#### Monday 2022-08-29 23:03:36 by SnugglyValeria

6 Furnace Demo Modules (might be too much)

Some Furnace Demo modules of mine, meant to replace the old ones that have been already removed :p
ORIGINALS:
- Furnace Electric Dance Music System (FEDMS) [2xOPZ+Amiga+TSU]
- Hope For The Dream [YM2151 only]
- Sitting under The Cherry Tree... with My Beautiful Girlfriend [2xYamaha YM2414 + 4xDAC]
COVERS AND REMIXES
- Turrican II - The Final Fight! [Genesis + Amiga cover]
- Iji - Tor [Sega System X (YM2151+SegaPCM) cover]
- Gimmick! - Strange Memories of Death [Yamaha YM2151 + 2xMicrochip AY8930 + SegaPCM cover]

---

