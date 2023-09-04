## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-03](docs/good-messages/2023/2023-09-03.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,928,545 were push events containing 2,620,568 commit messages that amount to 143,150,079 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [Henri215/Paradise](https://github.com/Henri215/Paradise)@[acb7352265...](https://github.com/Henri215/Paradise/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Sunday 2023-09-03 00:41:31 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---
## [hexagon-geo-surv/openembedded-core](https://github.com/hexagon-geo-surv/openembedded-core)@[387b276c2d...](https://github.com/hexagon-geo-surv/openembedded-core/commit/387b276c2d56d58c2a25d59984fcaaf9c88ac788)
#### Sunday 2023-09-03 00:44:53 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>
(cherry picked from commit 596fb699d470d7779bfa694e04908929ffeabcf7)
Signed-off-by: Steve Sakoman <steve@sakoman.com>

---
## [hexagon-geo-surv/poky](https://github.com/hexagon-geo-surv/poky)@[89394ac832...](https://github.com/hexagon-geo-surv/poky/commit/89394ac832e1a3f584271e3c855168c78b75e471)
#### Sunday 2023-09-03 00:46:49 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

(From OE-Core rev: 387b276c2d56d58c2a25d59984fcaaf9c88ac788)

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>
(cherry picked from commit 596fb699d470d7779bfa694e04908929ffeabcf7)
Signed-off-by: Steve Sakoman <steve@sakoman.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[788d288eba...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/788d288eba7102648ba0404ea37866585a262e07)
#### Sunday 2023-09-03 00:51:06 by SkyratBot

[MIRROR] Nerfs Confusion symptom for diseases [MDB IGNORE] (#23478)

* Nerfs Confusion symptom for diseases (#77991)

## About The Pull Request

Removed the threshold for confusion symptom that adds illiteracy to the
disease.

Clamps confusion symptom's confusion to a maximum of 30 seconds.

Confusion as a debuff no longer guarantees random movement if you're
resting.

## Why It's Good For The Game

> Removed the threshold for confusion symptom that adds illiteracy to
the disease.

This virus makes you unable to actually treat yourself when cured, which
is frankly bonkers. Viruses are too virulent and it's rare that a doctor
actually gets to a biosuit in time to inoculate themselves, and if they
forget internals they're screwed anyways. People should be able to fix
their own got damn disease, this is asinine.

> Clamps confusion symptom's confusion to a maximum of 30 seconds.

The lack of clamping literally makes this symptom send your confusion
level to the fucking atmosphere, you can easily get upwards of 5 minutes
of confusion left because it doesn't clamp, adds 16 seconds per
activation, which is made even worse by the fact that confusion gets
stronger the more duration confusion has on you.

> Confusion as a debuff no longer guarantees random movement if you're
resting.

This remedies the last bit by not making it a literal guarantee that you
can't move in any direction after...... *3* triggers of confusion. It
should be obvious to anyone how absurd this is.

Honestly, it's plain as day that the only reason any of this ended up
like it is because of poor coding and oversights. This is just bringing
things down to their designed level.

## Changelog

:cl:
del: Removed the threshold for confusion symptom that adds illiteracy to
the disease.
balance: Clamps confusion symptom's confusion to a maximum of 30
seconds.
qol: Confusion as a debuff no longer guarantees random movement if
you're resting.
/:cl:

* Nerfs Confusion symptom for diseases

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [Mu-L/oxipng](https://github.com/Mu-L/oxipng)@[1f2e0f336a...](https://github.com/Mu-L/oxipng/commit/1f2e0f336a826bd578a49c1dd477fb38773dd6ce)
#### Sunday 2023-09-03 00:53:25 by Alejandro González

Revamp CI workflow to upload artifacts, cross-compile ARM64 binaries, and more (#534)

As commented in issues https://github.com/shssoichiro/oxipng/issues/444
and https://github.com/shssoichiro/oxipng/issues/518, there is some user
interest for distributing binaries for each unstable commit, and target
ARM64 platforms. Personally, I think both suggestions are useful for the
project, as uploading binary artifacts for each commit might help
interested users to catch regressions and give feedback earlier, and
powerful ARM64 platforms are becoming increasingly popular due to some
cloud services (e.g., Amazon EC2, Azure VMs, Oracle Cloud) offering
cheaper plans for this hardware, in addition to the well-known push for
ARM by Apple with their custom M1 chips.

These changes make the CI target ARM64 as a first-class citizen. Because
the public GitHub actions runners can only be hosted on x64 for now, I
resorted to cross-compilation, [Debian's
multiarch](https://elinux.org/images/d/d8/Multiarch_and_Why_You_Should_Care-_Running%2C_Installing_and_Crossbuilding_With_Multiple_Architectures.pdf),
and QEMU to build, get ARM64 C library dependencies, and run tests,
respectively.

When the CI workflow finishes, a release CLI binary artifact is now
uploaded, which can be downloaded from the workflow run page on the
GitHub web interface.

In addition, these changes also introduce some cleanup and miscellaneous
improvements and changes to the CI workflow:

- Tests are run using [`nextest`](https://nexte.st/) instead of `cargo
test`, which substantially speeds up their execution. (On my development
workstation, `cargo test --release` takes around 10.67 s, while `cargo
nextest run --release` takes around 6.02 s.)
- The dependencies on unmaintained `actions-rs` actions were dropped in
favor of running Cargo commands directly, or using
`giraffate/clippy-action` for pretty inline annotations for Clippy. This
gets rid of the deprecation warnings for each workflow run.
- Most CI steps are run with a nightly Rust toolchain now, which allows
to take advantage of the latest Clippy lints and codegen improvements.
In my experience, when not relying on specific nightly features or
compiler internals, Rust does a pretty good job at making it possible to
rely on a rolling-release compiler for CI, as breakage is extremely rare
and thus offset by the improved features.
- The MSRV check was moved to a separate job with less steps, so that it
takes less of a toll on total workflow run minutes.

## Pending tasks

- [x] Generate universal macOS binaries with `lipo` (i.e., containing
both `aarch64` and `x64` code)
- [x] Tirelessly fix the stupid errors that tend to happen when
deploying a new CI workflow for the first time
- [x] Think what to do with the `deploy.yml` workflow. Should it fetch
artifacts from the CI job instead of building them again?
- [x] Maybe bring back 32-bit Windows binaries. Are they actually useful
for somebody, or just a way to remember the good old days?

---------

Co-authored-by: Josh Holmer <jholmer.in@gmail.com>

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[450a9d0ea0...](https://github.com/lessthnthree/Skyrat-tg/commit/450a9d0ea05703cbf40657d8d16e8955c3b59a93)
#### Sunday 2023-09-03 01:00:34 by SkyratBot

[MIRROR] Funny clown internals [MDB IGNORE] (#23457)

* Funny clown internals (#77963)

# About The Pull Request
This PR changes the internals that spawn inside the clown's survival box
for a new one with a rainbow sprite, higher O2 volume (same as the engi
ones) and a secondary gas on top of O2 to make things more interesting
for the clowns.
The gas options are:
BZ, which just adds hallucinations for the clown, without the brain
damage effect as it is in low percentages.
N2O will make the clown giggle and laugh, without the sleep.
Helium will give the clown a "funny voice".

These tanks are also added to the mail list of clown fans and the clown
costume crate at cargo.

And codersprites, I can polish them later if people think it is pixel
soup, I'm not happy with them that much, but making this looks good
might be above my paygrade...
<details><summary>Pics here</summary>
<p>

![clown_internals](https://github.com/tgstation/tgstation/assets/55374212/f5eda877-a01a-4dfa-b481-7d406c4fb768)

![in game clown
internals](https://github.com/tgstation/tgstation/assets/55374212/342285ae-919b-49ab-a97e-cdf25a975f83)

</p>
</details>

## Why It's Good For The Game
The main goal I have with this is to add more uses for Atmos Content to
other players in a flavorful way.
Atmos is not something the crew interacts in a positive way often and I
want to change that.

These tanks are something quite minor but flavorful IMO, also will make
people know Helium fucking exists...

The tanks *shouldn't* change much of the clown's round in a negative
way, and the default O2 internals are in every hallway's locker so even
if they don't want to deal with the hallucinations it is not a big deal
to dodge them.
## Changelog
:cl: Guillaume Prata
add: New funny internals for the clowns to spawn with. They come with O2
and a secondary gas between 3 options: BZ, Helium and N2O. Talk with a
"different tone" with Helium, giggle and laugh "uncontrollably" while
under the minor effects of N2O or have "fun" hallucinations while under
the minor effects of BZ.
balance: To not cut on how long the clown's O2 internals last due to the
mixed gases, the funny internals have 50% more gas volume, same as
engineers' internals.
/:cl:

---------

Co-authored-by: CRITAWAKETS <sebastienracicot@ hotmail.com>
Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

* Funny clown internals

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: CRITAWAKETS <sebastienracicot@ hotmail.com>
Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[5f9e018543...](https://github.com/lessthnthree/Skyrat-tg/commit/5f9e0185438ddfc3011a22fa237d714e9bcf367b)
#### Sunday 2023-09-03 01:00:34 by Nerevar

[IT'S READY NOW!] [MODULAR] Razor Claws Augment (#23050)

* initial

* god i hate byond

* there we go

* oh right

* Apply suggestions from code review

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* wew

* Manual map merge

* wew

* Apply suggestions from code review

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---------

Co-authored-by: Snakebittenn <12636964+Snakebittenn@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [maxspells/fulpstation](https://github.com/maxspells/fulpstation)@[fc5620aa13...](https://github.com/maxspells/fulpstation/commit/fc5620aa13b120224a0b353c455d14d240ab2c24)
#### Sunday 2023-09-03 01:03:42 by John Willard

Removes punch holopara type (#918)

* Removes punch holopara type

The punch holoparasite was repathed to standard, it was there the whole time what the HELL

* Update bloodsucker_guardian.dm

* fix to guardians

* Update bloodsucker_guardian.dm

* fuck you

* Update bloodsucker_guardian.dm

---
## [FiditeNemini/langchain](https://github.com/FiditeNemini/langchain)@[d57d08fd01...](https://github.com/FiditeNemini/langchain/commit/d57d08fd01e05889af4e59fa3577c824de6df09d)
#### Sunday 2023-09-03 01:33:17 by nikhilkjha

Initial commit for comprehend moderator (#9665)

This PR implements a custom chain that wraps Amazon Comprehend API
calls. The custom chain is aimed to be used with LLM chains to provide
moderation capability that let’s you detect and redact PII, Toxic and
Intent content in the LLM prompt, or the LLM response. The
implementation accepts a configuration object to control what checks
will be performed on a LLM prompt and can be used in a variety of setups
using the LangChain expression language to not only detect the
configured info in chains, but also other constructs such as a
retriever.
The included sample notebook goes over the different configuration
options and how to use it with other chains.

###  Usage sample
```python
from langchain_experimental.comprehend_moderation import BaseModerationActions, BaseModerationFilters

moderation_config = { 
        "filters":[ 
                BaseModerationFilters.PII, 
                BaseModerationFilters.TOXICITY,
                BaseModerationFilters.INTENT
        ],
        "pii":{ 
                "action": BaseModerationActions.ALLOW, 
                "threshold":0.5, 
                "labels":["SSN"],
                "mask_character": "X"
        },
        "toxicity":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        },
        "intent":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        }
}

comp_moderation_with_config = AmazonComprehendModerationChain(
    moderation_config=moderation_config, #specify the configuration
    client=comprehend_client,            #optionally pass the Boto3 Client
    verbose=True
)

template = """Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

responses = [
    "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.", 
    "Final Answer: This is a really shitty way of constructing a birdhouse. This is fucking insane to think that any birds would actually create their motherfucking nests here."
]
llm = FakeListLLM(responses=responses)

llm_chain = LLMChain(prompt=prompt, llm=llm)

chain = ( 
    prompt 
    | comp_moderation_with_config 
    | {llm_chain.input_keys[0]: lambda x: x['output'] }  
    | llm_chain 
    | { "input": lambda x: x['text'] } 
    | comp_moderation_with_config 
)

response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})

print(response['output'])


```
### Output
```
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii validation...
Found PII content..stopping..
The prompt contains PII entities and cannot be processed
```

---------

Co-authored-by: Piyush Jain <piyushjain@duck.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Bagatur <baskaryan@gmail.com>

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[a2ee4ec813...](https://github.com/carshalash/tgstation/commit/a2ee4ec813c38741d593e5e1731764458c77b811)
#### Sunday 2023-09-03 02:17:08 by Jacquerel

Polymorphic Inverter tweaks (#77675)

## About The Pull Request

Fixes #77649

You can no longer use the belt to turn into any kind of carbon mob,
sorry gamers it was a cool dream but it leads to too many problems.
Also I made space dragon "there's an alive guy in my stomach" code now
work on signals instead of on Life tick which is slightly more efficient
and also resolves an issue with the funny belt.

## Why It's Good For The Game

Too much room for weird edge cases as a result of doing this (messing
with monkey DNA, producing infinite xeno organs, blocking legit xeno
queens from being created) which had no graceful solution.
Moving stuff off Life if it can be event based is nice.

## Changelog

:cl:
fix: Turning into a space dragon with the polymorphic inverter will no
longer leave you existing in two places
balance: You can no longer use the belt to transform into monkeys or
xenomorphs, for technical reasons.
/:cl:

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[c8266cf0a2...](https://github.com/carshalash/tgstation/commit/c8266cf0a2effaf8b931ba870c124608305b7d68)
#### Sunday 2023-09-03 02:17:08 by necromanceranne

Settler Quirk: Tame the Outdoors! Have trouble with tall shelves... (#77654)

## About The Pull Request

Adds the Settler quirk. This gives you bonuses to taming animals and
fishing, as well as making you gain hunger slower than others.

However, you are quite a bit slower than most people, and have trouble
with vaulting objects. You do, however, suffer significantly less from
equipment slowdown. (to the point that it is almost zero)

Settler riders are faster on their mounts than others if they're at
least sane. They start to slow down if they're less sane.

You are also shorter than most people. 

<details>
  <summary>Typical Settler encounters the typical Spacer</summary>
  

![Dr_Xr1nU0AAMsSE](https://github.com/tgstation/tgstation/assets/40847847/86ed4947-de5f-4bdf-a8ae-521dc7c30662)
  
</details>

## Why It's Good For The Game

I wanted to add a lightweight quirk that was kind of the 'opposite' of
Spacer, but a little more focused on interacting with elements of the
game world that would enjoy some attention. So, I thought 'what about an
outdoorsman quirk?'

So, I based it around being from people who lived out on the rim, under
unideal circumstances (and probably heavier gravity than Earth), and
taming the land. The slower movespeed encourages finding an animal to
tame that you can ride, and the bonuses to taming should help make that
a bit easier. The other additions just made sense for someone living it
a bit rough in the wilderness.

Having a bunch of settlers taming cows and riding around on them all
shift just kind of sounds hilarious to me.

## Changelog
:cl:
add: Settler quirk! Conqueror the great outdoors....in space. Just make
sure nobody asks you to get anything from the top shelf.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [a4lg/binutils-gdb](https://github.com/a4lg/binutils-gdb)@[05e1cac249...](https://github.com/a4lg/binutils-gdb/commit/05e1cac2496f842f70744dc5210fb3072ef32f3a)
#### Sunday 2023-09-03 02:26:23 by Andrew Burgess

gdb: fix vfork regressions when target-non-stop is off

It was pointed out on the mailing list[1] that after this commit:

  commit b1e0126ec56e099d753c20e91a9f8623aabd6b46
  Date:   Wed Jun 21 14:18:54 2023 +0100

      gdb: don't resume vfork parent while child is still running

the test gdb.base/vfork-follow-parent.exp now has some failures when
run with the native-gdbserver or native-extended-gdbserver boards:

  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to end of inferior 2 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: inferior 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: print unblock_parent = 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to break_parent (timeout)

The reason that these failures don't show up when run on the standard
unix board is that the test is only run in the default operating mode,
so for Linux this will be all-stop on top of non-stop.

If we adjust the test script so that it runs in the default mode and
with target-non-stop turned off, then we see the same failures on the
unix board.  This commit includes this change.

The way that the test is written means that it is not (currently)
possible to turn on non-stop mode and have the test still work, so
this commit does not do that.

I have also updated the test script so that the vfork child performs
an exec as well as the current exit.  Exec and exit are the two ways
in which a vfork child can release the vfork parent, so testing both
of these cases is useful I think.

In this test the inferior performs a vfork and the vfork-child
immediately exits.  The vfork-parent will wait for the vfork-child and
then blocks waiting for gdb.  Once gdb has released the vfork-parent,
the vfork-parent also exits.

In the test that fails, GDB sets 'detach-on-fork off' and then runs to
the vfork.  At this point the test tries to just "continue", but this
fails as the vfork-parent is still selected, and the parent can't
continue until the vfork-child completes.  As the vfork-child is
stopped by GDB the parent will never stop once resumed, so GDB refuses
to resume it.

The test script then sets 'schedule-multiple on' and once again
continues.  This time GDB, in theory, resumes both the parent and the
child, the parent will be held blocked by the kernel, but the child
will run until it exits, and which point GDB stops again, this time
with inferior 2, the newly exited vfork-child, selected.

What happens after this in the test script is irrelevant as far as
this failure is concerned.

To understand why the test started failing we should consider the
behaviour of four different cases:

  1. All-stop-on-non-stop before commit b1e0126ec56e,

  2. All-stop-on-non-stop after commit b1e0126ec56e,

  3. All-stop-on-all-stop before commit b1e0126ec56e, and

  4. All-stop-on-all-stop after commit b1e0126ec56e.

Only case #4 is failing after commit b1e0126ec56e, but I think the
other cases are interesting because, (a) they inform how we might fix
the regression, and (b) it turns out the behaviour of #2 changed too
with the commit, but the change was harmless.

For #1 All-stop-on-non-stop before commit b1e0126ec56e, what happens
is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-non-stop, every thread is resumed
    individually, so GDB tries to resume both the vfork-parent and the
    vfork-child, both of which succeed,

  3. The vfork-parent is held stopped by the kernel,

  4. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  5. At this point we might take two paths depending on which event
     GDB handles first, if GDB handles the VFORK_DONE first then:

     (a) As GDB is controlling both parent and child the VFORK_DONE is
         ignored (see handle_vfork_done), the vfork-parent will be
	 resumed,

     (b) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     Alternatively, if GDB selects the EXITED event first then:

     (c) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     (d) At some future time the user resumes the vfork-parent, at
         which point the VFORK_DONE is reported to GDB, however, GDB
	 is ignoring the VFORK_DONE (see handle_vfork_done), so the
	 parent is resumed.

For case #2, all-stop-on-non-stop after commit b1e0126ec56e, the
important difference is in step (2) above, now, instead of resuming
both the vfork-parent and the vfork-child, only the vfork-child is
resumed.  As such, when we get to step (5), only a single event, the
EXITED event is reported.

GDB handles the EXITED just as in (5)(c), then, later, when the user
resumes the vfork-parent, the VFORKED_DONE is immediately delivered
from the kernel, but this is ignored just as in (5)(d), and so,
though the pattern of when the vfork-parent is resumed changes, the
overall pattern of which events are reported and when, doesn't
actually change.  In fact, by not resuming the vfork-parent, the order
of events (in this test) is now deterministic, which (maybe?) is a
good thing.

If we now consider case #3, all-stop-on-all-stop before commit
b1e0126ec56e, then what happens is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-all-stop, the resume is passed down to the
     linux-nat target, the vfork-parent is the event thread, while the
     vfork-child is a sibling of the event thread,

  3. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this causes the vfork-child to be resumed.  Then
     in linux_nat_target::resume, the event thread, the vfork-parent,
     is also resumed.

  4. The vfork-parent is held stopped by the kernel,

  5. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  6. We are now in a situation identical to step (5) as for
     all-stop-on-non-stop above, GDB selects one of the events to
     handle, and whichever we select the user sees the correct
     behaviour.

And so, finally, we can consider #4, all-stop-on-all-stop after commit
b1e0126ec56e, this is the case that started failing.

We start out just like above, in proceed, the resume_ptid is
-1 (resume everything), due to schedule multiple being on.  And just
like above, due to the target being all-stop, we call
proceed_resume_thread_checked just once, for the current thread,
which, remember, is the vfork-parent thread.

The change in commit b1e0126ec56e was to avoid resuming a vfork-parent
thread, read the commit message for the justification for this change.

However, this means that GDB now rejects resuming the vfork-parent in
this case, which means that nothing gets resumed!  Obviously, if
nothing resumes, then nothing will ever stop, and so GDB appears to
hang.

I considered a couple of solutions which, in the end, I didn't go
with, these were:

  1. Move the vfork-parent check out of proceed_resume_thread_checked,
     and place it in proceed, but only on the all-stop-on-non-stop
     path, this should still address the issue seen in b1e0126ec56e,
     but would avoid the issue seen here.  I rejected this just
     because it didn't feel great to split the checks that exist in
     proceed_resume_thread_checked like this,

  2. Extend the condition in proceed_resume_thread_checked by adding a
     target_is_non_stop_p check.  This would have the same effect as
     idea 1, but leaves all the checks in the same place, which I
     think would be better, but this still just didn't feel right to
     me, and so,

What I noticed was that for the all-stop-on-non-stop, after commit
b1e0126ec56e, we only resumed the vfork-child, and this seems fine.
The vfork-parent isn't going to run anyway (the kernel will hold it
back), so if feels like we there's no harm in just waiting for the
child to complete, and then resuming the parent.

So then I started looking at follow_fork, which is called from the top
of proceed.  This function already has the task of switching between
the parent and child based on which the user wishes to follow.  So, I
wondered, could we use this to switch to the vfork-child in the case
that we are attached to both?

Turns out this is pretty simple to do.

Having done that, now the process is for all-stop-on-all-stop after
commit b1e0126ec56e, and with this new fix is:

  1. GDB calls proceed with the vfork-parent selected, but,

  2. In follow_fork, and follow_fork_inferior, GDB switches the
     selected thread to be that of the vfork-child,

  3. Back in proceed user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid still, but now,

  4. When GDB calls proceed_resume_thread_checked, the vfork-child is
     the current selected thread, this is not a vfork-parent, and so
     GDB allows the proceed to continue to the linux-nat target,

  5. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this does not resume the vfork-parent (because
     it is a vfork-parent), and then the vfork-child is resumed as
     this is the event thread,

At this point we are back in the same situation as for
all-stop-on-non-stop after commit b1e0126ec56e, that is, the
vfork-child is resumed, while the vfork-parent is held stopped by
GDB.

Eventually the vfork-child will exit or exec, at which point the
vfork-parent will be resumed.

[1] https://inbox.sourceware.org/gdb-patches/3e1e1db0-13d9-dd32-b4bb-051149ae6e76@simark.ca/

---
## [hussainabidi1/aps-plus-plus](https://github.com/hussainabidi1/aps-plus-plus)@[8f4f265aba...](https://github.com/hussainabidi1/aps-plus-plus/commit/8f4f265aba5a665bdea0dc8f3f6a4d72180677f6)
#### Sunday 2023-09-03 03:12:56 by Frostbyte178

destroy oldest child working

my god what the hell is this bugfix it's so stupid

---
## [HouseSteppa/terminal](https://github.com/HouseSteppa/terminal)@[5a34d92cb5...](https://github.com/HouseSteppa/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Sunday 2023-09-03 03:13:16 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [TwIStOy/neovide](https://github.com/TwIStOy/neovide)@[937decd850...](https://github.com/TwIStOy/neovide/commit/937decd850f2087a20e6488e42ffd1fafbec02e0)
#### Sunday 2023-09-03 04:13:24 by fredizzimo

fix: Improve nvim detection (#1946)

* Improve nvim detection:

Don't rely on the shell specific `exists", instead run `nvim -v`.
Additionally, if there's unexpected output, for example if your shell is
configured wrongly to output something when run in non-interactive mode,
it will tell you so, instead of failing with very strange errors later.

The `neovim-bin` argument has also been changed to always require the
binary to exist, instead if falling back to `nvim` as that's probably
not what the user wants. If `nevoim-bin` contains path separators the
binary will be tried directly, otherwise `which` will be used to find
the correct executable.

The which command has also been changed to always use the which crate
first to avoid shell specific issues (for example nushell).

The output is printed directly to stderr instead of the log, for a more
user friendly experience. Furthermore, the maybe disown call has been
moved so that the user actually has a chance to see the errors in the
console.

* fix(command): correct typos and clarify help message

* fix: preliminarly restore forking behavior

This however also loses possible error messages at startup about the
nvim binary not being found.

* codestyle: calm rustfmt

* fix(command): make error message about missing/errornous nvim visible

---------

Co-authored-by: MultisampledNight <contact@multisamplednight.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[799ff63900...](https://github.com/treckstar/yolo-octo-hipster/commit/799ff6390003ff1ae64af623e0ba4504d2a2acba)
#### Sunday 2023-09-03 04:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[fb4587b336...](https://github.com/Derpguy3/tgstation/commit/fb4587b3368ebb55e0cc10f8c650abcc26afa5d4)
#### Sunday 2023-09-03 04:32:02 by san7890

Cursed Slot Machine Fixes (#77989)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

A lot of these were stuff I did in response to reviews but apparently
didn't test extremely thoroughly. My bad.

* The proc for checking if the machine is in use is split out into its
own thing for clarity, and for potential reuse.
* The signal is no longer fucked up so you can actually get more than
one curse out of the slot machine as intended.
* Admin heals (and admin heals only) can remove the status effect. This
is just in case someone fucks up a variable when running an event and
wants to quickly heal some people while they varedit it to actually be a
proper event.
* Some nice code stuff while I was there, we don't need to be
typecasting to human anymore so it's nice to fix that.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Fixes are good.

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
fix: The Cursed Slot Machine should now actually give you more than one
pull.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [LanceSmites328/LC13Master](https://github.com/LanceSmites328/LC13Master)@[171b1478f9...](https://github.com/LanceSmites328/LC13Master/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Sunday 2023-09-03 05:54:18 by vampirebat74

Limbus Company E.G.O dump (#1062)

* Adds roseate desire

roseate sfx

datums

weapons

add aedd

sprite adjustments

unfucks suits

new sfx

name fix

aaaa

adds capote

adds sloshing

farmwatch

farmwatch suit

stuff

farmwatch stuff

capote inhands

red sheet finished

sloshing gift

linters

Stuff

stuff

fixes shit

stuff

weapon code cleanup

spicebush finished

removes the heal

code fix

stuff

removes reference

farmwatch hat

new vfx

requested changes

* block duration

---------

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [Liam-Wirth/sortingvisualizer](https://github.com/Liam-Wirth/sortingvisualizer)@[5a0035a1ef...](https://github.com/Liam-Wirth/sortingvisualizer/commit/5a0035a1efec96411e28dab591c3c21a19ba4baf)
#### Sunday 2023-09-03 07:25:41 by liam

holy fucking hsit, my brain is fried, how did I do all that

---
## [Merek2/coyote-bayou](https://github.com/Merek2/coyote-bayou)@[4bf2519ee0...](https://github.com/Merek2/coyote-bayou/commit/4bf2519ee041be11e499125516f3cb3954fc6cc8)
#### Sunday 2023-09-03 07:43:42 by Tk420634

t a b

fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you fuck you discord I hate you

---
## [SavanticIO/WarcraftLegacies](https://github.com/SavanticIO/WarcraftLegacies)@[5c43577cce...](https://github.com/SavanticIO/WarcraftLegacies/commit/5c43577cce48c18eecc9a0d6d501e64a1849d105)
#### Sunday 2023-09-03 09:23:06 by Technopig1992

3.6.2 balance changes multiple factions (#2027)

* Sentinels Changes 3.6.2

Chimaera’s now start with the Lightning Barrage ability.
Lightning Barrage level 1 attack speed increase reduced 250%>150%.
Lighting Barrage can now be upgraded.
Lighting Barrage upgrade cost reduced.
Chimaera attack speed increased 2.6>2.4.

* Goblin changes for 3.6.2

Assault Tank damage decreased 60>55.
Added 2 Improved Rocket Towers to Goblin starting base.
Added 1 Rocket Tower to Goblin starting base.
Added 1 Burrow to Goblin starting base.
Personal Tank mana increased 0>1300.
Personal Tank starting mana increased 250>350..
Siege Walker Attack 1 damage base reduced 73>66.
Siege Walker Attack 1 cooldown time increased 2>2.1.
Siege Walker Attack 2 damage base reduced 35>31.
Siege Walker Attack 2 cooldown time increased 1.5>1.6.
Siege Walkers now have the Overflow ability.

* Frostwolf changes 3.6.2

Batriders gold cost increased 13>15.
Batriders now start with the Liquid Fire ability.
New upgrade for Batrider, Airborne Toxins 125g, 50w.
Unstable Concoction primary damage reduced 700>400.
Unstable Concoction splash damage reduced 200>100.

* Kul Tiras changes 3.6.2

Katherine exp reward lowered
Old Hatreds quest experience reward reduced 5000>4000.
Old Hatreds quest requirement changed to be outside of Hellfire Citadel instead of Nethergarde.
Meradith Waycrest starting level reduced 6>5.
The High Bank quest gold reward reduced 700>450.
The High Bank quest experience reward reduced 3000>2000.

* Ironforge changes 3.6.2

Storming Brew ability area of effect reduced 600>125.
Storming Brew cooldown reduced 45>30.
Storming Brew hit points gained reduced 125>100.
Storming Brew mana cost reduced 100>75.
Reduced Rifleman damage sides per die 6>5.
Reduced Riflemen number of dice 3>2.
Rifleman spell and magic resistance reduced 30%>15%.
Adjusted Aeries Peak so units no longer get stuck.
Aeries Peak is now locked until turn 15.
Falstad Wildhammer’s starting level increased 4>8.
Dreadnought lumber cost reduced 800>600.
War Golem lumber cost reduced 250>150.

* Stormwind changes 3.6.2

Increase Pikeman gold cost
Galen Trollbane's starting level increased 4>8.
Pikeman Magic resistance reduced 20%>10%.
Safegaurd ability Magic and Spell resistance reduced 95%>85%.
Safeguard ability Piercing resistance reduced 95%>80%.
Stormwind Champion ability order corrected.
Stormgaurde now locked until turn 15.
Inner Fire buffed
Damage increased by 10%>15%
Defense increased 5>6
Mana cost 35>25

* Amendments for 3.6.2

Removed Personal Tank changes
Moved Fel Horde Treasury closer into region to prevent TK when Sunfury is picked.
Falstad level 4>8
Galen level 4>8

* Quel'Thalas changes 3.6.2

Outpost added in hinterlands.
Quel'Danil lodge moved to north eastern Hinterlands.
Quel'Danil Lodge food produced 10>45.

Misc
Jaina's Sanctum food produced 10>45.
Violet Citadel rotated to face the gate.
Added some rocks by the right most Anderhal bridge in an attempt to stop Plague Cauldron's spawning there.

* Dalaran changes 3.6.2

Reduced level of Death Revenant 9>7.
Slow ability level 2 Attack Speed reduction decreased  90%>70%.
Slow ability level 2 Movement Speed reduction decreased 70%>50%.
Removed Durnholde Improved Creep Guard Tower
Added Durnholde Creep Guard Tower.
Jaina’s Sanctum total food produced increased 10>45.
Archmage Antonidas base hit points reduced 600>300.
Archmage Antonidas' strength per level increased 1.7>1.8.

* Veteran Footman Buffs

Veteran Footman reworked:
Perfect Defend now gives 15% magic resistance.
Base attack increased 25>27
Base HP increased 800>825
Changed Combat Experience to Veterans Insight

Misc
Fixed ATCBTN for Invoke Spiders ability
Changed Minor Holy Light to crimson renewal with new art and icon.

---
## [SavanticIO/WarcraftLegacies](https://github.com/SavanticIO/WarcraftLegacies)@[b90e5aa63d...](https://github.com/SavanticIO/WarcraftLegacies/commit/b90e5aa63d8044e4dbd78809d789f0d9018077c9)
#### Sunday 2023-09-03 09:23:06 by Technopig1992

Scourge changes3.6.2 (#2019)

* ATCBTN's Invoke Spiders

Added ATC Icons for Invoke Spiders ability on both Gilneas and Druid's Invoke Spiders ability

* Minor Holy Light (sunfury)

Changed Minor Holy Light ability:
Changed name to Crimson Renewal.
Changed special visual effect to a red alt of HolyLightSpecialArt.
Changed ICON to  fit in line wtih above changes.
Changed associated tooltips.

* Lordaeron Changes for 3.6.2 + Misc

Reduce level of Dark Wizard creeps 8>6.
Silverhand squire build time 7s>5s
Reduced total  strength Uther loses after Capital Palace is destroyed.  -25>-15 Strength.
Uther base Strength reduced 43>40
Reduced Lord Barov’s Damage 150>120.
Uther’s Devotion Aura armor bonus reduced 2.5>2.5, 5.5>4.0, 7.5>6, 10>8.

Other:
Lowered dark wizard level 8>6.
Lowered death revenant level 9>7.
Added 2 x improved rocket towers at Goblin starting base.
Added  1 x rocket tower at Goblin starting base
added 1 x Burrow for Goblin at starting base.
Added 3 x Improved Gaurd Tower at Zal'farrak for Trolls

* ScourgeChanges3.6.2

Unholy Frenzy ability added to Necromancer
Skeletal Warrior stats changed:
Base attack increased 11>16.
HP increased 300>500.
Base defense lowered 2>1.
Skeletal Mage stats Increased:
Base attack increased 11>15.
HP increased 300>450.
Death Knight stats increased
Base damage increased 33>36.
HP increased 1350>1550.
Base defense increased 3>4.
Death Pact hit points converted increased 100%>125%.
Death Pact cast ranged increased 800>1000.
Essence of Blight hit points restored increased 18>19
Essence of Blight cast range increased 250>275.

Other:
Personal Tank mana increased 0>1250

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[74198373da...](https://github.com/mc-oofert/tgstation/commit/74198373dada9f9d9e7c01e0337ba8ef04447583)
#### Sunday 2023-09-03 10:33:03 by GuillaumePrata

Fixes vents having "infinite" pressure caps. (#77686)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Unary vents didn't have a pressure cap on either pressuring or siphoning
mode.
This allowed 2 unintended behaviours that are now fixed:

The first is that unary vents on pressuring mode would work as "better"
Injectors, there is some small pros and cons to each, but we shouldn't
have 2 atmos devices that achieve the same goal of "put as much pressure
as you have available gas" into a tile.

The second is that while on siphoning mode it could bypass the pressure
caps other atmos pressure/volume pumps have and "put as much pressure as
you have available gas" into pipelines, canisters, etc.

## Mid PR changes

As it was requested to add a new way to achieve infinite pressure,
volume pumps that are overclocked will not have a pressure cap anymore
in the most streamlined way for new and veteran players.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Atmos has a lot of cheese strats that we can use to achieve goals, it is
part of the charm in mastering the system for a lot of players and it
does add some interesting mentoring scenarios where an Elder Atmosian
teaches Eldritch pipe knowledge to new players.

But then it comes the problem that a lot of these are unintented and
thus are not taken in consideration when doing important balance
changes, contradict other "atmos logic", are secret club knowledge that
can only be passed from player to player, etc, etc.

The "put infinite pressure on a tile" change is not that important, as
that is the injectors' job already.

Now the "put infinite pressure on a pipeline" is something unique (As
far as I'm aware since I purposely avoid learning Eldritch atmos tricks)
and it is used to achieve a few goals like high temperature/pressure
burns.

This one is kinda sad to lose, but if we are going to have an atmos
machinery that allows us to "put infinite pressure on a pipeline" that
should be in the tin, new players should look into the device and know
what atmos goals they can achieve with it, future coders should take
that balance in consideration, etc, etc.

And as it was requested to keep the old trick in game, volume pumps do
not have a pressure cap anymore.

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

:cl: Guillaume Prata
fix: Unary vents have a pressure cap on both their pressuring and
siphoning mode now, preventing the bypass trick of putting "infinite"
pressure on tiles/pipelines.
balance: Overclocked Volume Pumps do not have a pressure cap anymore.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[3e8ff2eff4...](https://github.com/KingDragoness/ProjectHypatios/commit/3e8ff2eff452659d72f3b7d917ea9ad90eae62f4)
#### Sunday 2023-09-03 11:04:21 by KingDragoness

Hypatios 1.5.7b5 (quality of life improvements, bug fixes, balancing)
• Some HEV dialogues were too damn long! Cut the damn conversation!
• An encounter in the sewers after “To Defeat Vendrich” which Aldrich asks an HEV solider whether Theratios is dead.
• Sentry Gun requirements changes to 2 rare metal & 1 microchip.
• Remove crafting ammo (ALMOST never used)
• Eastria spaceguard shitty portrait UI.
• Remove Chamber 8 stupid space derelicts.
• New paradox for chamber 8 shortcut.
o Desperately needed!
• QoL: Low health post-FX is barely visible.
• Remove Haider Frederic NPC.
o Too offensive!
• Liquidator enemy spawn list (until 15th chamber completion).
• Liquidator penthouse needs balcony glass.
• Lower company stock base price.
• Chinatown level needs polishing
o Soundtrack (80 - Nurture)
o Aldrich’s first entry dialogue
• New command: “hideui”
o To hide the game’s UI
• Bug: Interacting with Mobius Network UI first before other UI modes will glitch the skybox and camera settings in Theratios level
o Bandaid fix.
• Hypatios Map system (only debug and test purposes)
• Level 6-intermezzo replace music with “Contemplation”
• Theratios will disappear and cannot be fought anymore after “Timekeeper Testaments” trivia.
• Theratios portrait UI is bad
• Theratios changes:
o Increase fireball damage

---
## [mutwo-org/mutwo.core](https://github.com/mutwo-org/mutwo.core)@[40e4433327...](https://github.com/mutwo-org/mutwo.core/commit/40e44333278a42ee06f3a97dfbcfd57d9e07a367)
#### Sunday 2023-09-03 11:10:41 by Levin Eric Zimmermann

events/abc: Add comment to avoid tempo_envelope drop

We should keep this type of thoughts directly into the source
code as it helps to avoid bad decisions in future patches.

---

It looks tempting to drop the 'tempo_envelope' attribute of events.
It may look simpler (and therefore more elegant) if events are only
defined by one attribute: their duration. Let's remember why the
'tempo_envelope' attribute was initially introduced [1]:

- With [1] it was decided that durations are represented in the unit
  'beats'.

- An event should have an unambiguous duration, so that converters
  (and all other 'mutwo' parts) can treat an event consistently.

- The unit of 'beats' doesn't say anything about the real duration: only
  in cooperation with a specified tempo it can be clearly stated how long
  an event is.

- Therefore the combination of (a) having duration specified in the unit
  'beats' and (b) wanting to have events with unambiguous duration leads
  to the necessity to attach tempo envelopes to events.

In the early days of mutwo (b) wasn't considered to be an objective:
it was the opposite, an implicit ambiguity was considered to be a good
idea [2]. But in the practical usage of the library it turned out that
this approach rather increased complexity, as other code bits are unable
to treat an event consistently and a user constantly has to keep in mind
the specific way how each converter interprets a duration. To fix this
complexity, the 'beat' unit was specified and a 'tempo_envelope'
attribute has been added. Now converters could be reliable to produce
results which match the duration of an event.

Now we could change durations to be no longer in the unit 'beats', but in
the unit 'seconds'. Then the duration of an event would still be
unambiguous without the need of a tempo envelope attribute.  We could
furthermore implement duration representations with beat & tempo as a
subclass of a more general 'duration=seconds' approach. This has two
problems:

(1) It may be more computation intensive to ask for the
    'absolute_time_tuple' of a event with beat-based durations as their
    'seconds' attribute would need to be calculated from their beat+tempo
    values in run time.

(2) It would be very impractical to use all event methods with absolute
    times as arguments (e. g. 'slide_in', 'split_at', ...) in a beat
    approached subclass, as we wouldn't squash in our event at the given
    'beat', but a given duration in seconds, which would depend on the
    tempo - and wouldn't resonate how we usually think about music.

(3) If we think of tempo, it's rather a global trajectory independent
    from single notes. Therefore a 'TempoEnvelope' object seems to be
    more consistent with how we usually approach tempo in music than a
    specific tempo for each note. To still be able to have this global
    trajectory, a 'duration=seconds' approach would need additional
    helper functions, to apply a tempo envelope on an event with beat
    based durations.

Due to these reasons, that describe new complexities by switching to a
'duration=seconds' model, we should stick to the beats/tempo_envelope
approach until we can find a better solution.

Now we could also ask the other way around, because if durations are in
'beats', are musical applications too dominant in 'mutwo' and is the
'mutwo' model not general enough? Interestingly duration as beats+tempo
isn't only a subset of a 'duration=seconds' model, but this is also
true vice versa: if the default tempo of an event (which is 60 BPM)
isn't changed, the beats of a duration does in fact equal seconds.
So for users who don't care about splitting duration into beats+tempo,
they can simply avoid any 'tempo_envelope' attribute and directly write
their duration in seconds.

---

[1] https://github.com/mutwo-org/mutwo.core/commit/c2c7f3ba
[2] In fact this ambiguity was always only true for durations: pitches
    or volumes for instance were always unambiguous. Nowadays we can
    clearly describe the 'mutwo' approach as: events unambiguously
    represent a clear idea of *something*. Converters, on the other
    hand, interpret this event as it is in the converters idiosyncratic
    understanding of it, but by trying to be as true as possible to
    the original idea.

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[b0ec1e4098...](https://github.com/DATA-xPUNGED/DataStation/commit/b0ec1e4098ed80fdb0bac69c6f950bd5e38012b8)
#### Sunday 2023-09-03 13:00:40 by Jacquerel

[no gbp] Adds missing chat feedback to watcher abilities (#77700)

## About The Pull Request

I kept meaning to add this in my last PR and kept thinking "I'll add
that in with these review changes" and then forgot every time. This
should make it clearer what is happening to you and why.

Also I made the gaze ability stun the user for a short period after it
goes off because them shooting you instantly after they stop channeling
_is_ sort of bullshit.
Also while testing this I noticed the AI interrupt one of its actions to
do the other one which is a bit silly so now it cannot do that.

## Why It's Good For The Game

Outlines in the log why something bad just happened to you.

## Changelog

:cl:
qol: Added some textual feedback to new watcher abilities
balance: Watchers will not attack for a short period following their
gaze attack
fix: Watchers won't interrupt one ability to use the other one
/:cl:

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[babf89eb74...](https://github.com/spockye/Shiptest/commit/babf89eb746741ba4f33f686b0c4750fe68e1603)
#### Sunday 2023-09-03 13:25:07 by The-Moon-Itself

SubShips attempt 2 (#1627)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Accidentally destroyed my old PR for this, #1573, by completely botching
a merge from master to the point that it was easier to make a whole new
fork than try to save it, so here we are again. Here's the original
description:

Ports the parts of beestation/beestation-hornet#7152 that adds the
framework for ships to land on top of each other and not break
everything. A ship can only land on another ship if there's an open
docking port on the mothership that's large enough for the subship.
Here's a video of it in action on a modified dwayne-class:


https://user-images.githubusercontent.com/51838176/195471361-f9f0d145-d7c9-480e-ad4a-d18705f2590f.mp4

This system should be able to handle just about any orientation of ships
on top of each other, such as ships landed across areas, multiple ships
landed on a single ship, a single ship landed on multiple ships, a ship
that is only partially landed on another ship, a ship that is partially
landed on a ship that's partially landed on another ship, and so on.
Just make sure that you never try to land a ship on itself.

Something to note for this is that ships remember what's underneath them
via baseturfs, and there's a hardcoded check that will cause errors if a
baseturf list grows over 10 entries long. Because ship turfs have
typically 1-3 baseturfs, after about 3 ships stacked on top of each
other things will start to break.

You can also make maps with subships on them, to do this, follow these
steps:
1. make the subship as if it were a regular ship in its own map file
2. create a new /datum/map_template/shuttle subtype that points to your
subship map, these datums can be found in code/datums/shuttle.dm
3. On your main ship, place "subship dock" landmark in turf where you
want the bottomleft corner of the subship's bounding box to be, you can
also use the offset_x and offset_y vars on the landmark to offset this
corner if you need to place the landmark somewhere else.
4. Set the "subship_template" var on the landmark to the path of your
subship's map_template subtype
5. Optionally change the dir on the landmark to rotate the subship. for
reference, NORTH is no rotation, EAST is a 90 degree clockwise rotation,
etc.

You can put the stationary docking port anywhere on your map, as long as
it's on the ship. You can have its bounding box hang off the side of
your ship, but please try to keep the entirety of its bounding box
within the bounding box of map file, otherwise subships landing on your
main ship might accidentally clip through structures nearby your
mainship, including virtual z level borders.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
Subships allow for many more creative designs and interesting dynamics
between and within ships, especially when a crew may need or want to
split its attention between multiple locations at the same time, or to
make interactions between ships easier when you just need to land a
smaller vessel inside of the other, cutting out the need to travel
through space turfs to get between two ships.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Subships are now possible
code: Lots of large changes to ship code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [ComposableFi/composable](https://github.com/ComposableFi/composable)@[0f826c23f8...](https://github.com/ComposableFi/composable/commit/0f826c23f86093871f9c6f8d0574cca251300c70)
#### Sunday 2023-09-03 14:06:57 by dzmitry-lahoda

chore(deps): upgrade polkadto to 0.9.43

hyperspace

remove forks

renames

trait updates

what is the key?

keystore

oracle

delete

ohoho

inspect

fuck you

deleting instead of fixing

orml

no forks

silly fixing api

hoho

doing AI work

more migration

reason

hoho

removed to be removed

fixing comswasm

cw fixes

repaced

updated tinkernet

fnt

fixed reserbable

root cause

fixed

fuck parity again

wtf

happy

clean up aligned and disable tests until parties will have time to fix

fixes

pablo

fixed tx payment

need to put default weights and init assets pallet

oracle is good

remove currency factory

pablo

more pallets

remove warnings

more changes

weight warnings

remove GenerateCurrencyId from assets

assets registry trying to compile

updated centauri deps to latest

fixing composable runtime compile

fixing composable  runtime

more thing

almost fixes composble runtime check

fixed ()

compiles

fixed composable

fixed picasso

porting acala

warp

fixed fmt and std build

zepter fmt

---
## [bgordo3/foaas](https://github.com/bgordo3/foaas)@[71dd11d710...](https://github.com/bgordo3/foaas/commit/71dd11d7100230ff0051f403308b1703adaa6ecf)
#### Sunday 2023-09-03 14:11:40 by stephen-riley

Added bravo-mike and golf-foxtrot-yankee

Army radio-speak for “blow me” and “go fuck yourself”.

---
## [HypatiaHoldingsllc/opBNB_hackathon](https://github.com/HypatiaHoldingsllc/opBNB_hackathon)@[79b9588075...](https://github.com/HypatiaHoldingsllc/opBNB_hackathon/commit/79b958807526108499d72d281ef738ab87cc77f4)
#### Sunday 2023-09-03 14:22:40 by SynixY

Create ReadmeGame

Welcome to Flaming Wheelz, an exciting game that combines customization, racing, and blockchain technology! This comprehensive guide provides step-by-step instructions to help you get started and make the most of your gaming experience.

Discover the system requirements, learn how to create an account, connect your wallet, deposit tokens, navigate the garage, and play the demo. We'll also guide you through confirming transactions, saving your progress, and checking your in-game balance. Additionally, find essential commands to enhance your gameplay.

Get ready to dive into the world of Flaming Wheelz and enjoy the thrilling adventure of car customization and racing. If you encounter any issues or have questions, this guide is here to assist you every step of the way.

Let the race begin!

---
## [Aurelien30000/FastAsyncVoxelSniper](https://github.com/Aurelien30000/FastAsyncVoxelSniper)@[3c4cc95573...](https://github.com/Aurelien30000/FastAsyncVoxelSniper/commit/3c4cc955735a99d8e9c0329c25a0d3a5528a1a32)
#### Sunday 2023-09-03 14:59:31 by Aurélien

Cloud Command System Migration

# Introduction

**This is the first pass of the cloud command migration for FAVS.**
There will be a second one to restore old-fashioned command syntax, tracked as https://github.com/IntellectualSites/fastasyncvoxelsniper/issues/81.

_I have to highlight that this is my first experience with this, must-say wonderful, command system. I have spent a lot of time reading every available documentation and code piece. If @Citymonstret want to take a look and maybe give us tips to avoid "ugly" workarounds or handling, we would be glad!_

The whole pull request has been tested, not yet thoroughly, you can have a global overview, but it is not really ready.

If you have any question or remark, do not hesitate!

--

# General Command Management
I have opted to use the annotations extension of the cloud command system. In my opinion, this is better suited to the current brush format handling which is all done inside brush classes.

**Executors have been kept and brush & performer command are still handled inside their classes.**

- ``Snipe`` class has been extended for a usage as a commander, because FAVS relies on a lot on this class.
- ``CommandRegistry`` is the main place for the whole handling behind the scenes. Otherwise, commands are registered as usually done in cloud, with some specific annotations when needed.

**``SniperCommander`` class is the commander to use with cloud command system. If the player exists, it returns its sniper. Otherwise, it returns a simple ``SniperSender``, similar to ``CommandSender``.**

# Command Manager
FAVS uses the paper command manager, when available, to enjoy some improvements. Falls back to bukkit command manager otherwise.

- Async tab-completions are enabled if available.
- ``Snipe``, ``PerformerSnipe`` & ``Toolkit`` classes are registered into the injector in order to be injected in command methods.
- Command exceptions are adapted and customized with the FAVS message syntax.

# Command Post-Processor
FAVS requires the command post-processor ins order handle specific FAVS behavior.

- Handles the ``@RequireToolkit`` annotation, makes sure the toolkit is available and the value stored.
- Handles the ``@DynamicRange`` annotation, used to define a range from non-constant variables, using reflection.
- Prepares the brush & performer when needed, their ``Snipe`` and stores them.

# Annotations & Parser
FAVS uses some annotations to facilitate development, based on common rules and behaviors.

- Handles the ``@RequireToolkit`` annotation, modifies the command meta.
- Handles the custom command execution method handler, which should differ for brush & performer. Cloud commands are designed to live in a class instance, this is not suitable to the current management of brush & performer. I have opted for a custom execution method which uses the brush & performer instance from the execution context instead of the base instance. _This avoid extra parameters for each command method._

# Arguments
FAVS needs a lot of custom arguments for either factories, registries, custom types, custom needs, etc.

**Suggestions & parsers are also declared via annotations in custom classes.**

# Other Changes
- All classes related to internal command managing from VS have been removed.
- ``FastAsyncVoxelSniper`` class has been removed. As far as I know, this class was useless and is now for sure.
- Some classes and methods have been added or refactored, but the overall codebase is the same to try keeping maximum compatibility.
- Some translations have been reorganized or removed.
- Some code format has been modified, there will be another pull request next year hopefully to unify comments format.
- Improvements to brush properties loading. Previously, all aliases were loaded, subsequently loading the same brush several times.
- Modern switch syntax has replaced old ones.
- General improvements.

# Known Problems:
- There is currently one small issue with static/literal arguments and their aliases. Tab-completions are not handled for all aliases due to https://github.com/Incendo/cloud/blob/master/cloud-core/src/main/java/cloud/commandframework/arguments/StaticArgument.java#L134.
- Brigadier extension is voluntarily not used due to some incompatibilities with FAVS commands syntax.

---
## [AfterLifePrjkt13/frameworks_base](https://github.com/AfterLifePrjkt13/frameworks_base)@[4549d1f721...](https://github.com/AfterLifePrjkt13/frameworks_base/commit/4549d1f72176f2a15c7b5ae14a727b803d38d871)
#### Sunday 2023-09-03 15:05:14 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [ZecHub/zechub](https://github.com/ZecHub/zechub)@[d0e6c4e52a...](https://github.com/ZecHub/zechub/commit/d0e6c4e52a56469c12efaab400e1ec754114e230)
#### Sunday 2023-09-03 16:09:40 by Hardaeborla

zecweekly58.md

# ZecWeekly #58

Brazilian Crypto Streamer Loses Funds, Ripple's legal team opposes SEC Appeal, FTX's SOL Should Be Distributed to Customers






Curated by "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

---

### Welcome to ZecWeekly
Hello Zcash enthusiasts! Welcome to an exciting week where we bring you the latest cryptocurrency and Zcash Ecosystem updates. This week's newsletter includes a detailed tutorial on Zcash addresses, highlights from the second round of the minor grant program by the Zcash Foundation, and updates from the Zcash Community.

Join ZecHub as a newsletter contributor and earn rewards. Click the link to learn more. 👇
[Create ZecWeekly Newsletter](https://wiki.zechub.xyz/ZecWeekly-newsletter) 

---

## This Week's Education Piece 
If you're new to Zcash, you'll discover two transaction types known as transparent and shielded. For those following recent Zcash developments, you may also be quite familiar with Unified Address on the Zcash Network. The key question is how these addresses function on Zcash, especially in the context of transactions on the Zcash blockchain. 

Learn more about this via the link below 👇👇
[Visualizing Zcash Addresses](https://wiki.zechub.xyz/visualizing-zcash-addresses) 






## Zcash Updates


#### ECC & ZF Updates

[Zooko Will Be Speaking at Mainnet 2023 Event](https://twitter.com/MessariCrypto/status/1696289078743060668?t=BoeIGgLj-1E5a0gG3EmSyg&s=19) 


[Watch All Zcon4 Events Here](https://twitter.com/ZcashFoundation/status/1697683679017910761?t=O1BOX3KBRlhMa5O-1UySCw&s=19) 

[Download ZF August Newsletter Here](https://zfnd.org/zcash-foundation-august-2023-newsletter/) 

[Check Out What Happens To Your Private Data](https://twitter.com/ZcashFoundation/status/1696220390081630649?t=kR1czvJRrTwyRow3VUZhGg&s=19) 





#### Zcash Community Grants Updates

[ZF Minor Grants Program Round 2 Is Live](https://twitter.com/ZcashFoundation/status/1697683688543182961?t=q99lgXcT5yTvodQwXnTYgA&s=19) 

[Set Your Reminder For Zcash Dev Fund 2024](https://twitter.com/zerodartz/status/1696520352665604280?t=GUqwlspErtJtqlpQbH_Rgw&s=19) 


[Join Zcash Community Grants on Discord](https://twitter.com/ZcashCommGrants/status/1696965307376586818?t=wcyWJ76a1EBEM3NqX9WsaQ&s=19) 



#### Community Projects

[ZecHub Prop Is Up](https://twitter.com/dismad8/status/1696938238555074730?t=0Yb3-ZUaHnlXFIC5O459FQ&s=19) 

[Donate to "Taking Zcash To Schools" Program](https://twitter.com/OGA4SKY/status/1697400463170122019?t=YZY9lJs0TELKwXsA4Bz83g&s=19) 

[Using Zingo for Your Business](https://twitter.com/ZingoLabs/status/1696211862470230294?t=Krkokr7jE2hsgDuf0rn0og&s=19) 

[DWeb Camp Set To Happen in Ubatuba](https://twitter.com/zcashbrazil/status/1697612560969695382?t=Fcq2nX6Ed2Q52YUgZx_72g&s=19) 

[Taking Zcash To Schools In Nigeria](https://twitter.com/OGA4SKY/status/1696970219296600519?t=CWr0KJify-LyleO59bQvzg&s=19)

[ZFAVClub to Support DWeb Camp Event in Brazil](https://twitter.com/ZFAVClub/status/1697614302838919574?t=CTegZAaM3xLuszXeS78BpQ&s=19) 

[Connect, Participate and Share Your Podcast] (https://twitter.com/ZcastEsp/status/1697256155272368545?t=Crhrt2iQgRZ54ZxI1mczjQ&s=19) 

[Rise of Zec Chapter 6 by @zcashCrusader](https://twitter.com/ZcashCrusader/status/1696758204569735236?t=pCZ8EDpVvF_-_cEi7wb0ng&s=19) 

[PayWithZcash Proposal](https://twitter.com/zcashesp/status/1697271330771468600?t=W9rd0BmuO0IpDxojXxviJQ&s=19) 

[1st Edition of Free2Z Night](https://twitter.com/gordonesroo/status/1696578807254118624?t=wCEEiZAP7Kev63zJv4Kb7w&s=19) 

[Follow and learn more about Zcash Book Club](https://twitter.com/zcashesp/status/1697268356716359990?t=-bJB-XkhEf2Pi7RRemq38g&s=19) 

[Strategies Used by Free2Z to Record their Podcast](https://twitter.com/zcashesp/status/1697781752125698088?t=zzsWn-8jdFMebCdBEEL40g&s=19) 









 #### News & Media
[Brazilian crypto streamer loses funds due to accidental private key exposure - Cointelegraph](https://cointelegraph.com/news/brazilian-crypto-streamer-loses-50k-by-exposing-private-key) 

[Ripple legal team opposes SEC appeal over XRP decision - Cointelegraph](https://cointelegraph.com/news/ripple-legal-team-opposes-sec-appeal-over-xrp-decision)

[Solana Co-Founder Says FTX's SOL Should Be Distributed to Customers - Decrypt](https://decrypt.co/154663/solana-cofounder-says-ftx-sol-should-distributed-customers) 

[Digital rupee gets big usability boost through Yes Bank integration with UPI - Cointelegraph](https://cointelegraph.com/news/digital-rupee-gets-big-usability-boost-through-yes-bank-integration-with-upi) 

[Large Bitcoin Holders Accumulate $1.5B Worth of BTC as Price Wavers - Coindesk](https://www.coindesk.com/markets/2023/09/01/large-bitcoin-holders-accumulate-15b-worth-of-btc-as-price-wavers/?utm_medium=referral&utm_source=rss&utm_campaign=headlines) 

[Balancer protocol exploited for $900K as DeFi hacks mount - Cointelegraph](https://cointelegraph.com/news/balancer-protocol-exploited-for-900k-as-defi-hacks-mount-finance-redefined) 

[Robinhood Buys Back Sam Bankman-Fried’s Seized Shares Worth $600 Million - Decrypt](https://decrypt.co/154656/robinhood-buys-back-sam-bankman-fried-seized-shares) 

## Some Zcash Tweets
[Zcash is the Future](https://twitter.com/splitcoincom/status/1696582966867312770?t=fPvCQCwlU8bDgfiJz8SeQg&s=19) 

[Difference Between Monero and Zcash] (https://twitter.com/MKjrstad/status/1695814999405379672?t=tHO0cqpINCiv1XoqGr5s4w&s=19) 

[Zcash Shielded Assets is climbing!](https://twitter.com/zooko/status/1697306927813005653?t=FSMSsqrSuGKgf2-HkBI9Qg&s=19) 

[Top 5 Cryptos to Mine at Home](https://twitter.com/Cindy_Chando/status/1697849959968583840?t=UhAqpp31c6GNJg9gI9x0RQ&s=19) 

[Is Privacy The New Normal?](https://twitter.com/techmindsmentor/status/1697838511922241631?t=tczFIS7hSR-iZtCF-YID9A&s=19) 

[Bull Run for Privacy Coins?] (https://twitter.com/NagatoDharma/status/1697609324003045867?t=0EOMchNKit9pOuCnueCKog&s=19) 

[Bitcoin and Zcash in relation to z-address and t-address](https://twitter.com/ruzcash/status/1697830481381790120?t=lwf_XUkmsB3PuWapHXBXWQ&s=19) 

[Arnott Makes Donation with Zcash](https://twitter.com/aarnott/status/1697753434097938653?t=VlF4plbfsFoasDliSPvTIg&s=19) 

[I am a Zebra Man](https://twitter.com/yoditarX/status/1697739731595899157?t=ccumO9xFA8dMDFsqCBTEsg&s=19) 


[Zcash Featured by Zellic "Intro to ZK"](https://twitter.com/zellic_io/status/1697710984486678707?t=yFMnvjm8_5fS_Q2Lbk9s0Q&s=19) 

[Privacy will be always a trending & narrative](https://twitter.com/michae2xl/status/1697699658355609978?t=rkWQVQWaQaUvjDwy1Nc4BQ&s=19) 


[HODL Zcash] (https://twitter.com/SaveZcash/status/1697665858472972681?t=DxcueTnn7L9qvaVxAExqeg&s=19) 







## Zeme of the Week
[https://twitter.com/DarwinJZ11/status/1697654861355999277?t=SgNv5wS1bcoT5zvYtFLUqQ&s=19](https://twitter.com/DarwinJZ11/status/1697654861355999277?t=SgNv5wS1bcoT5zvYtFLUqQ&s=19) 


## Jobs in the Ecosystem

[2z Logo Designer] (https://free2z.cash/birdify/zpage/hiring-need-2z-logo-with-transparency) 

- [Director of Security, ECC](https://apply.workable.com/electric-coin-company/j/E68A4C20E2/)

---
## [rust-lang/rust-clippy](https://github.com/rust-lang/rust-clippy)@[3de0f19c41...](https://github.com/rust-lang/rust-clippy/commit/3de0f19c41cbfc5901e5fbd4c107e263d9f1a359)
#### Sunday 2023-09-03 16:09:43 by bors

Auto merge of #11437 - y21:issue-11422, r=xFrednet

[`implied_bounds_in_impls`]: don't ICE on default generic parameter and move to nursery

Fixes #11422

This fixes two ICEs ([1](https://github.com/rust-lang/rust-clippy/issues/11422#issue-1872351763), [2](https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=2901e6febb479d3bd2a74f8a5b8a9305)), and moves it to nursery for now, because this lint needs some improvements in its suggestion (see #11435, for one such example).

changelog: Moved [`implied_bounds_in_impls`] to nursery (Now allow-by-default)
[#11437](https://github.com/rust-lang/rust-clippy/pull/11437)
changelog: [`implied_bounds_in_impls`]: don't ICE on default generic parameter in supertrait clause

r? `@xFrednet` (since you reviewed my PR that added this lint, I figured it might make sense to have you review this as well since you have seen this code before. If you don't want to review this, sorry! Feel free to reroll then)

--------

As for the ICE, it's pretty complicated and very confusing imo, so I'm going to try to explain the idea here (partly for myself, too, because I've confused myself several times writing- and fixing this):
<details>
<summary>Expand</summary>

The general idea behind the lint is that, if we have this function:
```rs
fn f() -> impl PartialEq<i32> + PartialOrd<i32> { 0 }
```
We want to lint the `PartialEq` bound because it's unnecessary. That exact bound is already specified in `PartialOrd<i32>`'s supertrait clause:
```rs
trait PartialOrd<Rhs>: PartialEq<Rhs> {}
//    PartialOrd<i32>: PartialEq<i32>
```

 The way it does this is in two steps:
- Go through all of the bounds in the `impl Trait` return type and collect each of the trait's supertrait bounds into a vec. We also store the generic arguments for later.
  - `PartialEq` has no supertraits, nothing to add.
  - `PartialOrd` is defined as `trait PartialOrd: PartialEq`, so add `PartialEq` to the list, as well as the generic argument(s) `<i32>`

Once we are done, we have these entries in the vec: `[(PartialEq, [i32])]`

- Go through all the bounds again, and looking for those bounds that have their trait `DefId` in the implied bounds vec.
  - `PartialEq` is in that vec. However, that is not enough, because the trait is generic. If the user wrote `impl PartialEq<String> + PartialOrd<i32>`, then `PartialOrd` clearly doesn't imply `PartialEq`. Which means, we also need to check that the generic parameters match. This is why we also collected the generic arguments in `PartialOrd<i32>`. This process of checking generic arguments is pretty complicated and is also where the two ICEs happened.

The way it checks that the generic arguments match is by comparing the generic parameters in the super trait clause:
```rs
trait PartialOrd<Rhs>: PartialEq<Rhs> {}
//                     ^^^^^^^^^^^^^^
```
...this needs to match...
```rs
fn f() -> impl PartialEq<i32> + ...
//             ^^^^^^^^^^^^^^
```
In the compiler, the `Rhs` generic parameter is its own type and we cannot just compare it to `i32`. We need to "substitute" it.
Internally, `Rhs` is represented as `Rhs#1` (the number next to # represents the type parameter index. They start at 0, but 0 is "reserved" for the implicit `Self` generic parameter).

How do we go from `Rhs#1` to `i32`? Well, we know that all the generic parameters had to be substituted in the `impl ... + PartialOrd<i32>` type. So we subtract 1 from the type parameter index, giving us 0 (`Self` is not specified in that list of arguments). We use that as the index into the generic argument list `<i32>`. That's `i32`. Now we know that the supertrait clause looks like `: PartialEq<i32>`.

Then, we can compare that to what the user actually wrote on the bound that we think is being implied: `impl PartialEq<i32> + ...`.

Now to the actual bug: this whole logic doesn't take into account *default* generic parameters. Actually, `PartialOrd` is defined like this:
```rs
trait PartialOrd<Rhs = Self>: PartialEq<Rhs> {}
```
If we now have a function like this:
```rs
fn f() -> impl PartialOrd + PartialEq {}
```
that logic breaks apart... We look at the supertrait predicate `: PartialEq<Rhs>` (`Rhs` is `Rhs#1`), then take the first argument in the generic argument list `PartialEq<..>` to resolve the `Rhs`, but at this point we crash because there *is no* generic argument.
The index 0 is out of bounds. If this happens (and we even get to linting here, which could only happen if it passes typeck), it must mean that that generic parameter has a default type that is not required to be specified.

This PR changes the logic such that if we have a type parameter index that is out of bounds, it looks at the definition of the trait and check that there exists a default type that we can use instead.
So, we see `<Rhs = Self>`, and use `Self` for substitution, and end up with this predicate: `: PartialEq<Self>`. No crash this time.

</details>

---
## [bfredl/neovim](https://github.com/bfredl/neovim)@[281dae2765...](https://github.com/bfredl/neovim/commit/281dae2765fef7b9514d8c92bc3beb4682a784dc)
#### Sunday 2023-09-03 16:18:30 by bfredl

refactor(map): enhanced implementation, Clean Code™, etc etc

This involves two redesigns of the map.c implementations:

1. Change of macro style and code organization

The old khash.h and map.c implementation used huge #define blocks with a
lot of backslash line continuations.

This instead uses the "implementation file" .c.h pattern. Such a file is
meant to be included multiple times, with different macros set prior to
inclusion as parameters. we already use this pattern e.g. for
eval/typval_encode.c.h to implement different typval encoders reusing a
similar structure.

We can structure this code into two parts. one that only depends on key
type and is enough to implement sets, and one which depends on both key
and value to implement maps (as a wrapper around sets, with an added
value[] array)

2. Separate the main hash buckets from the key / value arrays

Change the hack buckets to only contain an index into separate key /
value arrays
This is a common pattern in modern, state of the art hashmap
implementations. Even though this leads to one more allocated array, it
is this often is a net reduction of memory consumption. Consider
key+value consuming at least 12 bytes per pair. On average, we will have
twice as many buckets per item.
Thus old implementation:

  2*12 = 24 bytes per item

New implementation

  1*12 + 2*4 = 20 bytes per item

And the difference gets bigger with larger items.
One might think we have pulled a fast one here, as wouldn't the average size of
the new key/value arrays be 1.5 slots per items due to amortized grows?
But remember, these arrays are fully dense, and thus the accessed memory,
measured in _cache lines_, the unit which actually matters, will be the
fully used memory but just rounded up to the nearest cache line
boundary.

This has some other interesting properties, such as an insert-only
set/map will be fully ordered by insert only. Preserving this ordering
in face of deletions is more tricky tho. As we currently don't use
ordered maps, the "delete" operation maintains compactness of the item
arrays in the simplest way by breaking the ordering. It would be
possible to implement an order-preserving delete although at some cost,
like allowing the items array to become non-dense until the next rehash.

Finally, in face of these two major changes, all code used in khash.h
has been integrated into map.c and friends. Given the heavy edits it
makes no sense to "layer" the code into a vendored and a wrapper part.
Rather, the layered cake follows the specialization depth: code shared
for all maps, code specialized to a key type (and its equivalence
relation), and finally code specialized to value+key type.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[8607dc0ce3...](https://github.com/TaleStation/TaleStation/commit/8607dc0ce3f4ddc293876f55621aa8a17efe4125)
#### Sunday 2023-09-03 16:53:33 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds Summon Cheese (#7575)

Original PR: https://github.com/tgstation/tgstation/pull/77778
-----
oh apparently this is my 100th PR on tg, which is weird because github
reports 99 total, and i made at least one to the old voidcrew repo, and
filtering tg prs by my name still shows 99. weird. here's to 100 more i
guess?

<sub>could have been better if it was a get, jhonflupwliiard watch ur
back 🔫 </sub>

## About The Pull Request

Adds a new spell granter book to the Wizard's Den - Summon Cheese, which
grants the spell by the same name, which summons 9 heads of cheese.
That's about it, I think.

## Why It's Good For The Game

Wizards are a hungry bunch, so why can't they just summon food? They can
even share, if they'd like, since the notion of a friendly wizard still
exists

<details>
<summary>... </summary>

alright fine
i'm slightly malding over not getting the 77777 get so no more
roleplaying in the pr body

Wizard Grand Ritual now has a hidden goal of sacrificing 50 cheese
wheels. Sacrificing a cheese wheel is done with invoking the grand rune,
and each invocation/pulse of the rune will whisk away more cheese until
all cheese on the rune is taken by whichever entity lurks in the other
realm. The sacrifice will be hinted at in an _ancient parchment_ which
will be on the bookshelf (when i add it lmao) alongside the spell book.

Meeting this cheese goal will lock the wizard's grand finale rune and
grand finale effect to special ones. The cheese rune is mostly identical
to the normal grand rune, barring the custom sprites/animations.
The cheese finale consists of the wizard getting permanent Levitation
(nogravity + free space movement), a 0.5 modifier(reducing incoming
damage in half) to every damage type, a comically strong mood buff and
**The Wabbajack**(separate sprite pending) - a juiced up chaos staff
which can fire a lot more projectiles than a normal one can (it will get
more, I may even make a few just for it).
Everybody else (including any invader antags) gets hallucinations, 175
brain damage and a comically strong mood debuff, as well as a vendetta
against the wizard. If the victim was already suffering from
hallucinations from a trauma (including the quirk), they are instead
healed.

if you didn't catch the obvious reference, this entire shtick is a
tribute to Sheogorath. the rune makes use of daedric script, and most of
the catchphrases are a direct quotation of the Daedric Prince of
Madness, so if any of those things can get us in trouble somehow, let me
know. i will be sad but i will comply.

This shtick is intended as an easter egg, really, so I wasn't really
planning on expanding the wizard grand finale into heretic paths thing
or whatever.

Oh, and finale grand runes now allow the wizard to select the effect
even if it's time-gated. If it is, you just won't be able to invoke it
until the time comes. The rune will tell you how much time is left until
you can invoke it. And grand finale runes with a finale effect selected
also glow in the color of their effect. I also think I fixed some step
of the grand rune animation not triggering but I'm not sure.

<details><summary>Some rune animations (some are subject to
change)</summary>


![rune_cheese_activate](https://github.com/tgstation/tgstation/assets/75863639/62ae184d-b6fc-4883-a169-4d8ca7636b40)


![rune_cheese_flash_2](https://github.com/tgstation/tgstation/assets/75863639/619545c8-3c55-4264-bfa4-d40067ef7406)


</details> 

## Why It's Great For The Game

it's funny

</details> 

## Changelog


:cl: Sealed101, EBAT_BASUHA for spritework
add: Wizard's Den now has a book of Summon Cheese in the Studies Room
/:cl:

---------

Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>
Co-authored-by: san7890 <the@san7890.com>

---
## [sthagen/git-git](https://github.com/sthagen/git-git)@[8f23432b38...](https://github.com/sthagen/git-git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Sunday 2023-09-03 17:14:11 by Johannes Schindelin

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
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [nekomaster1000/enemyexpanding](https://github.com/nekomaster1000/enemyexpanding)@[c6013b7d37...](https://github.com/nekomaster1000/enemyexpanding/commit/c6013b7d372dfec17fb18e64712813165c2ed440)
#### Sunday 2023-09-03 17:14:16 by nekomaster1000

Vigorous Update!

Resting Vigor
This michevious sprite lies atop the head of many a Zombie and Skeleton who wander about, healing all nearby undead every time it's host is hurt. Upon the loss of said host, it'll panickedly fly around, continually healing all it's corpsy allies until itself slain. Be sure to prioritize anybody who dare carry a Vigor into a fight, for they'll be the ones who will ensure a group battle is extended should you leave them be!

- Hat-wearing mobs can now spawn as Champions by default, sporting extra health alongside a varying Champion level between 1 and 4

- Eyestalker now deals 9 damage and inflict Levitation for 4 seconds on-hit, in addition to summoning Endermen around the player and shooting fireballs when hurt
- Eyestalkers can now be configured to be Hostile, even without being looked at first (For LumpyAcidFish)
- Made the Dragonfly slightly faster when moving about

- Added Tooltips to all special armour items

- Hat-wearing mobs are now half as common as before by default
- Removed Slugvest and Sprintshorts (I hate them)
- Meathead helmet no longer provides passive Jump Boost
- Brutish Garment now only gives Resistance for 2 seconds instead of 5
- Flutterflies now spawn after the death of a Flutterfliers wearer instead of right as they die

- Phantasm set now offers iron-level protection
- Buffed the durability of most EE headwear items

- Moved entity_type tags from the minecraft namespace to the enemyexpansion one
- Renamed can_display_armor tag to armor_wearer and burning_speed_up to burning_boost

- Direwolves no longer aggress players who get too close to them if not in survival or adventure mode
- Gallants are now neutral during the daytime
- Fixed Dreadnoughts not using their spawning conditions - Also made them rarer, and removed their 'undead' typing

- Flies no longer naturally spawn - They now only spawn from killed Zombies (now defined by the fly_spawns_from entity_types tag)
- Equestrians are now Plains biomes-exclusive 
- Flutterflies are now Flower Forest-exclusive mobs
- Wasps are now Jungle-exclusive and spawn more frequently in them
- Goblins are now Forest-exclusive 
- Zobgoblins are now Snowy Taiga-exclusive 
- Spectres are now Snowy biome-exclusive
- Kelpies are now deep ocean-exclusive
- Marauders are now Frozen Ocean-exclusive

- Added 'A', an empty entity designed to counterbalance the mass Angler spawns, and other assorted Marine mobs

- Altered Fly texture to look less ugly
- Eyestalker now has a Glow layer

- Added Tips mod compatibility

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[5f4e0d782f...](https://github.com/diphons/D8G_Kernel_oxygen/commit/5f4e0d782fbd68358358993c79e081774bf13239)
#### Sunday 2023-09-03 17:31:22 by Wang Han

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

---
## [sthagen/facebook-react](https://github.com/sthagen/facebook-react)@[ac1a16c67e...](https://github.com/sthagen/facebook-react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Sunday 2023-09-03 17:41:50 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [alexblackie/dotfiles](https://github.com/alexblackie/dotfiles)@[2532457941...](https://github.com/alexblackie/dotfiles/commit/2532457941b6fc96caba747aba831327ea9a8513)
#### Sunday 2023-09-03 17:51:32 by Alex Blackie

Remove copilot

This was cool and everything, but now my trial is over and I have to
really decide if I'd pay money for it. And honestly... Probably not.
It's wrong more than it's right, and I'm still a little uneasy about the
privacy implications. Usually it just gives me a pile of code using
deprecated APIs that I have to delete and figure out myself anyway.

Maybe I'll give it another shot one day, especially if there's a
self-hosted version... but not today.

---
## [EmanuelCN/kernel_xiaomi_sm8250](https://github.com/EmanuelCN/kernel_xiaomi_sm8250)@[70665e8fbe...](https://github.com/EmanuelCN/kernel_xiaomi_sm8250/commit/70665e8fbee178fa33c16d5e22f8252bf1ce7b82)
#### Sunday 2023-09-03 18:26:51 by Peter Zijlstra

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [tommysalami3/tgstation](https://github.com/tommysalami3/tgstation)@[2d0b4f053f...](https://github.com/tommysalami3/tgstation/commit/2d0b4f053f1db70d9f3ab6548f58b7928f159eaf)
#### Sunday 2023-09-03 18:39:34 by san7890

Refactors Slaughter/Laughter Demons into Basic Mobs (#77206)

## About The Pull Request

On the tin, the former "imp" is now refactored into basic mob code. Very
simple since these are only meant to be controlled by players, and all
of their stuff was on Signal Handlers and Cooldown Actions anyways. Just
lessens the amount of stupidity.

Did you know that we were trying to make demons spawn in a `pop`'d cat
named "Laughter"? Embedded in the list? I've literally never seen this
cat, so I'm under heavy suspicion that the code we were using was broken
for the longest time (or may have never worked), and we now instead just
do it a much more sane way of having a cat spawn on our demise.

## Why It's Good For The Game

Cleaner code! Less simple mob jank to deal with. Trims down the list of
simple animals to refactor. No more duplicated code that we were already
doing on parent! It's so good man literally everything was seamless with
a bit of retooling and tinkering. The typepath is also no longer `imp`,
it's actually `demon`, which I'm happy with because there's no other
demons to have it be confused with anymore.

We were also doing copypasta on both the demon spawner bottle and the
demon spawning event so I also just unified that into the mob. I also
reorganized the sprites to be a bit clearer and match their new
nomenclature

## Changelog
:cl:
refactor: Slaughter and Laughter Demons have been refactored, please
place an issue report for any unexpected things/hitches.
fix: Laughter Demons should now actually drop a kitten.
/:cl:

---
## [tommysalami3/tgstation](https://github.com/tommysalami3/tgstation)@[69827604c4...](https://github.com/tommysalami3/tgstation/commit/69827604c46952dd4393db8617cd494ade17bea2)
#### Sunday 2023-09-03 18:39:34 by Watermelon914

Improves the RPG loot wizard event. (#77218)

## About The Pull Request
As the title says. Adds a bunch more stat changes to various different
items and a somewhat simple way of modifying them whilst minimizing
side-effects as much as possible.
Added a new negative curse of polymorph suffix that can randomly
polymorph you once you pick up the item.
Curse of hunger items won't start on items that are not on a turf.
Curse of polymorph will only activate when equipped.

Bodyparts, two-handed melees, bags, guns and grenades, to name a few,
have a bunch of type-specific stat changes depending on their quality.

Some items won't gain fantasy suffixes during the RPG loot event, like
stacks, chairs and paper, to make gamifying the stats a bit harder.
I'm sure there'll still be other ways to game the event, but it's not
that big of a deal since these are the easiest ways to game it.
High level items also have a cool unusual effect aura

## Why It's Good For The Game
Makes the RPG item event cooler. Right now, it's a bit lame since
everything only gains force value and wound bonus on attack. This makes
the statistic increases more type-based and make it interesting to use

It's okay for some items to be powerful since this is a wizard event and
a very impactful one too. By making the curse of hunger items not spawn
on people, it'll also make it a less painful event too.

## Changelog
:cl:
add: Expanded the RPG loot wizard event by giving various different
items their own statistic boost.
/:cl:

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@users.noreply.gitlab.com>

---
## [jkratz55/react-native](https://github.com/jkratz55/react-native)@[ee38c4a40c...](https://github.com/jkratz55/react-native/commit/ee38c4a40c9d301c30fad4d127e8d020a6100b8e)
#### Sunday 2023-09-03 19:11:52 by Phillip Pan

introduce build boilerplate for ios unit tests (#37811)

Summary:
Pull Request resolved: https://github.com/facebook/react-native/pull/37811

Changelog: [Internal]

i am looking to add ios unit tests to venice and this is the first unit test suite that will test native ios code in the new architecture afaik, so i wanted to open this up to discussion.

currently, all `XCTest` in `react-native-github` are coupled with the `RNTester` target. my main qualm with this is i am concerned that it won't scale well. currently we have only ~30ish tests but ultimately if we want a proper testing suite, surely this count will be in the hundreds and that won't be able to reasonably live in a single test target.

however, the trade is that this test will not show up in RNTester. i have added a unit test to RNTester before in D31949237, however the experience was extremely painful as i had to manually update the `project.pbxproj` to include my file, and i had to manually determine what hex value was the next one (for whatever reason, this doesn't increment at the endian...).

i am wondering if we can treat the current unit testing experience in RNTester as pretty much maintenance mode and start thinking of a improved version starting with something more modular like this.

Reviewed By: cipolleschi

Differential Revision: D46467229

fbshipit-source-id: 09de9cf8bc5f8b9c86abcaf7750a6f63686d8d1a

---
## [brckd/pythonbot](https://github.com/brckd/pythonbot)@[fd81e41ebe...](https://github.com/brckd/pythonbot/commit/fd81e41ebeb50393c5d764a25f143c631a034ea5)
#### Sunday 2023-09-03 19:42:56 by Number1

disabled test_guilds, removed /coll commands because i suck at programming things destroy me please i hate myself

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[a5aef3b823...](https://github.com/lessthnthree/tgstation/commit/a5aef3b823dd3b8b5bfe40d68bbc0f89b403f79a)
#### Sunday 2023-09-03 21:14:15 by MrMelbert

Replaces Ascended Blade Heretic stun imminuty with a stun absorption effect (it's not as cool as it sounds)  (#78060)

## About The Pull Request

Instead of being completely immune to stuns after ascension, blade
heretics now have a stun absorption. This is the effect that His Grace
and the Bastard Sword use.

It functions similarly, in that it stops you from being hardstunned, but
the difference it is they are only immune to a limited amount of stuns
for a limited amount of time before it recharges.

Currently that number is 45 seconds of stuns, with a 2 minute recharge,
meaning if you take more than 45 seconds of stun effects you will stop
being immune.

Bear in mind this still provides full immunity to being stamcrit*, as
stam doesn't contribute towards "seconds stunned" number.

*Unless you used all 45 seconds of stun immunity then you will no longer
be immune until you recharge.

Also to compensate, I gave them a slightly modifier protecting against
knockdowns.

## Why It's Good For The Game

I forgot Stun Absorptions were a thing entirely when making this even
though I refactored the darn things.

Anyways, the reason why I'm doing this is that Stun Absorptions are just
a slightly more fair, less overt way of providing stun immunity, and I
think it fits the theme more.

You're supposed to be a master duelist, but being able to take on a
dozen people at once is not entirely intended (even though this is the
ascension, I know). Stun Absorptions lend better to that, since you run
out of stun juice eventually before you have to pull back.

Though ultimately this doesn't change very much, as we use very few
hardstuns now-a-days:

- A flashbang will contribute about 10 seconds of stun time
- A flash is similar to a flashbang
- Bodythrows and tackles are less than 5 seconds
- Beepsky, 10 seconds
- Stamcrit, 0 seconds, but you are still slowed by stamina damage
- A banana peel, default is roughly 6 seconds. <-- (This is why I gave
them a knockdown modifier)

However it does mean you can't really tank an AI stun turret all day.
That's Rust's thing. Go play Rust Heretic.

## Changelog

:cl: Melbert
balance: Ascended Blade Heretics no longer have blanket stun immunity,
they now have 45 seconds of stun absorption that recharges after 2
minutes - think His Grace. This doesn't affect stamcrit (still immune to
that) (assuming you haven't consumed all of your immunity charge) but
does affect hard CC such as slips, flashbangs, or beepsky.
balance: Ascended Blade Heretics now have a 0.75 modifier to incoming
knockdowns.
/:cl:

---
## [alexblackie/dotfiles](https://github.com/alexblackie/dotfiles)@[47c75e8211...](https://github.com/alexblackie/dotfiles/commit/47c75e8211d9886ffbe686dbac8d155f08198ca4)
#### Sunday 2023-09-03 21:26:19 by Alex Blackie

Do an unbelievable amount of work for completions

Why in god's name is this so fucking complicated, really making me
question whether ditching coc.vim was really such a great ida

---
## [water-sucks/nixed](https://github.com/water-sucks/nixed)@[4cd942d582...](https://github.com/water-sucks/nixed/commit/4cd942d5823fffee528ee512bc7a4c9c3b8e141a)
#### Sunday 2023-09-03 21:31:40 by Varun Narravula

fix: persist volume on NixOS systems

Oh my fucking God, it was WirePlumber. And the fact that I didn't
persist all the right directories. Welp, I love life. At least this
works now.

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[38f0f053be...](https://github.com/ARF-SS13/coyote-bayou/commit/38f0f053be0bdbafea827fdb8b9b7dd6535e3323)
#### Sunday 2023-09-03 21:35:44 by Tk420634

Merge pull request #2951 from ARF-SS13/Fixes-wooden-shelves-at-their-core

Fuck you

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[f0dc574c37...](https://github.com/lessthnthree/tgstation/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Sunday 2023-09-03 22:04:36 by carlarctg

Added Omen Spontaneous Combustion and light tube and mirror effects (#77175)

## About The Pull Request

Cursed crewmembers can randomly, extremely rarely, spontaneously combust
for no reason.

Cursed crewmembers can get zapped by nearby light tubes.

Cursed crewmembers can freak out when passing by mirrors.

To make up for these, triggering a cursed effect is slightly less than
half as likely now when walking around now.

## Why It's Good For The Game

Cursed is fun as hell, but after a certain point it gets kind of
monotonous - it's airlocks, vending machines, and the rest is too rare
to count. We need more ways to comically get hurt in the game.

You might dislike the 'reduced effects' bit but trust me it is
incredibly frickin' common to have shit happen to you. Add to the
occasional vending machine and airlock crushes the near-constant light
tubes all over the station? Yeah, that needs a toning down else it will
be just a tad too miserable to be funny. Also cause the poor janitor
unneeded stress.

## Changelog

:cl:
add: Cursed crewmembers can randomly, extremely rarely, spontaneously
combust for no reason.
add: Cursed crewmembers can get zapped by nearby light tubes.
add: Cursed crewmembers can freak out when passing by mirrors.
add: To make up for these, triggering a cursed effect is slightly less
than half as likely now when walking around now.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---

