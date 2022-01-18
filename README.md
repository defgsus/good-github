## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-17](docs/good-messages/2022/2022-01-17.md)


1,642,784 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,642,784 were push events containing 2,582,310 commit messages that amount to 199,387,576 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 28 messages:


## [Bawhoppen/-tg-station](https://github.com/Bawhoppen/-tg-station)@[7bead07444...](https://github.com/Bawhoppen/-tg-station/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Monday 2022-01-17 00:25:56 by John Willard

General pAI code improvements (#63688)

Fikou said they would've made MODsuits be controllable by pAI's rather than AI's, if pAI code wasn't as bad.

But pAI code ISN'T AS BAD AS AI CODE LIKE HOLY SHIT WHAT THE FUCK MAN???

Anyways, this is just general code improvements for pAIs that I thought would be nice to have.

Documents previously undocumented vars
Moves loose vars to be where they should be
Removes single-letter variables
Makes pAI a defined job
Moves vars around to where they should be while removing unused ones.
Makes pAI abilities its own .dm file
Replaces var/silent with Stun() (like cyborgs)
Reworks pAI's doorjack to not have a ton of procs, copy paste, and a reliance on Life(), instead it just uses a do_after()
Moves screwdrivering radios from attackby to screwdriver_act

Just general code improvement for Silicon, the thing no one likes or wants to touch.

---
## [Kubisopplay/tgstation](https://github.com/Kubisopplay/tgstation)@[a2fa7799f3...](https://github.com/Kubisopplay/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Monday 2022-01-17 00:29:24 by Jeremiah

Removes swarmers from the game (#63989)

What the title says. But why?
I generally have a rule when making a contribution, that is "don't make the game less fun"
I'm not salting, I didn't die to a swarmer.
... Yet that's the problem. Swarmers are the griefiest antag in the game, but when you complain that they're annoying or unfun, you're doomed to hear "lol they can't even hurt you though."

WELL THAT ACTUALLY MAKES THEM WORSE. I would rather die to a hundred xenos and space dragons than be forced to untie myself in maintenance for 45 seconds while the shuttle leaves.
Why It's Good For The Game

Unfun game modes should be removed from the game.

    Being griefed by swarmers is annoying
    Playing as a swarmer is not very exciting either. Click on iron.

lastly, because oranges authorized it
Changelog

cl
del: Removes swarmers! The griefiest, lowest fun value antagonist is removed from the game.
/cl

---
## [cloudflare/terraform-provider-cloudflare](https://github.com/cloudflare/terraform-provider-cloudflare)@[449fe21530...](https://github.com/cloudflare/terraform-provider-cloudflare/commit/449fe21530c21c21b192e8d0855c3c2b655d4890)
#### Monday 2022-01-17 00:37:55 by Jacob Bednarz

resource/cloudflare_ruleset: improve dashboard collisions

One of the earliest niggles with customers coming from the dashboard to
Terraform was the collision caused by a Ruleset phase being created in
the UI but the Terraform provider also needing to create the same
phase. This was problematic for a few reasons:

- The first was that when you deleted Ruleset rules in the UI, it didn't
  remove the phase. This was intentional but hidden behind the UI and
  only accessible via the API.
- Secondly, when customers wanted to use Terraform, there was an
  assumption they would be starting from scratch and many were not.
- Finally, in the event of a collision, we didn't know which Ruleset the
  customer wanted to use so we error'd out with a link to manually
  resolve which isn't a great solution but made the issue more
  prominent.

I had a chance to rethink through this issue and managed to find a way
that we improve all three points above and remove majority of the pain
points. With the proposed changes, the only time a customer needs to
manually resolve the Ruleset rules is if there are existing rules in the
UI which requires them to be deleted or migrated.

Achieving this requires the assumption that if the Ruleset has no rules,
it is ok to modify. Unfortunately, it's not that simple in practice. If
the phase already exists, we cannot just update it as the `name`
attribute is not writable after creation. Along with this, the `ref` and
`version` values will be automatically incremented causing a permadiff
in Terraform as the customer hasn't actually modified these values but
the backing service (and API) has. To work around this, if we find a
phase with no rules, we recreate it with the provided values which is
essentially the same the same thing as the "happy path" for a new
Terraform resource would be anyway.

---
## [Greniza/fulpstation](https://github.com/Greniza/fulpstation)@[c797bf79ea...](https://github.com/Greniza/fulpstation/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Monday 2022-01-17 01:08:17 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [Greniza/fulpstation](https://github.com/Greniza/fulpstation)@[b59f03e592...](https://github.com/Greniza/fulpstation/commit/b59f03e592ce72f069760eba0f9eb30eeacd16c1)
#### Monday 2022-01-17 01:08:17 by John Willard

Deputy update (#428)

* deputy berets cant be knocked off, deputies get tablets, service deputy beret buff.

* fuck you

---
## [Samuzero15/shotgun-frenzy-plus](https://github.com/Samuzero15/shotgun-frenzy-plus)@[be90a427f0...](https://github.com/Samuzero15/shotgun-frenzy-plus/commit/be90a427f0ce32c75022438eeb8c1d713fd0ecd0)
#### Monday 2022-01-17 03:54:31 by Samuzero15

New turret sprites, Patcher gun! and stuff

(4 - 16 / 1 / 2022)
	*) Now the tracing of the Plasma Rifle advanced, will now stop chasing, after 5 seconds of flight.
	*) Now the Hell-trigger powerup is added on the shop.
	*) Re-factorized the weapon names and descriptions, creating the Language.weapons file.
	!+) Finally a new we-TOOL, yes tool! The Patcher Gun!
	// Fix turrets/dispensers/drones paying 10 credits per valid shot!
	// Shows the buildings health at the aim of this tool!
	// Also is cappable of stunning enemies!
	// 5% chance for Experience Point for each turret fix!
	+) New sprites for the bullet, plasma, rocket and shotgun turrets!
	// Im fixing the dissaperance of the turret bases and other bugs with these sprites, Im tired.
	+) New sprites for the Temperance rune!

---
## [azoller1/IllusionX_sm8250](https://github.com/azoller1/IllusionX_sm8250)@[ff9a972ebb...](https://github.com/azoller1/IllusionX_sm8250/commit/ff9a972ebbf611005988c3cfe45f1fe9386d77d0)
#### Monday 2022-01-17 05:23:24 by alk3pInjection

disp: msm: Handle dim for udfps

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
## [connectuum/warnings](https://github.com/connectuum/warnings)@[266ebe1e94...](https://github.com/connectuum/warnings/commit/266ebe1e94d4582218fdd76beaacb07b45303b30)
#### Monday 2022-01-17 05:49:47 by connectuum

despaired in Winter City

these songs came to me today \
not sure what they have to say \
i'll share them here \
with no one \
in time order \
anyway

---

there's a dream \
in the future \
there's a struggle \
that we have yet to win \
use that pride \
in our hearts \
to lift us up \
to tomorrow \
'cause just to sit still \
would be a sin \
i give thanks to my God \
'cause i know where i've been

(Hairspray)

---

i'm not a fallen angel, i just fell behind \
i'm out of luck and i'm out of time \
if you don't wanna love me, let me go \
i'm runnin' for the last train home

(John Mayer)

---

you're on the road \
but you've got no destination \
you're in the mud \
in the maze of Her imagination \
you love this town \
even if that doesn't ring true \
you've been all over \
and it's been all over you \
it's a beautiful day \
don't let it get away \
it's a beautiful day

(U2)

---

after talking in tongues \
i began to preach \
what falls from the branch \
is an apple or peach \
hold on to me \
there’s a red alert \
it’s the way you make me feel \
magnificent hurt

(Elvis Costello)

---

thank you for these words \
i think maybe i see \
a little more clearly \
perhaps to share is Her intention \
eventually -- the timing was my own \
it's so _difficult_ to know! \
and i do feel quite alone \
despite family and home \
this is of a different flavor \
i want to savor in the telling \
i want to speak something compelling \
but perhaps \
to never relate \
has been and \
will always be my fate \
why shouldn't i feel fulfillment \
in the things i help create? \
i can share of that with Love \
but this human _need_ still permeates

what if i don't have what it takes? \
am i locked beyond Her gates? \
my heart breaks.

---
## [FluffyJay1/ShadowStone](https://github.com/FluffyJay1/ShadowStone)@[94febe72d3...](https://github.com/FluffyJay1/ShadowStone/commit/94febe72d32ab47aedf9c86825bb5b2affca8039)
#### Monday 2022-01-17 06:01:11 by FluffyJay1

Minor fixes to pending play, ai, ui

- Fix pending play next to a card that's about to die always snapping it
  to the left of the card (even though it will always end up in the same
  spot anyway, now it will remember your preference)
- Fix AI not being able to foresee the player's attacks
- Fix UI thinking you can unleash dead minions for real this time

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[413fd90502...](https://github.com/timothymtorres/tgstation/commit/413fd9050271829e2899b88a676995ae2517111c)
#### Monday 2022-01-17 06:33:11 by GoldenAlpharex

Dullahan Partial Refactor: They Work Again Edition (#63696)

So, a few months ago I was like "hmm there's something weird going on with party pods...", which got me looking into important_recursive_hearers or something like that. I spoke about it in the coding channel and Kyler actually fixed it before I did. But I also caught a similar glitch with Dullahans, so I decided to investigate...

Two months later...

I present to you a partial unfuckening of the Dullahans, in that I made them fully functional once again:

They only hear speech through their head (not sounds, sadly, someone else would have to tell me how to do that because I otherwise really wouldn't know how to do it in a sane way), they speak through their head, runechat-included.
When you spawn a Dullahan, you're set to look through the Dullahan's eyes (so from their head), and that doesn't reset when you log off and back in, or admin-ghost and come back in your body.
When you're looking through your head, your view will no longer be reset to your body upon entering a locker, which is nice to avoid not being blind while looking through your body.
Dullahan heads no longer look completely lifeless and without organs. They have eyes that don't look dead and that even match the player's intended eye color.
Dullahan can now properly examine things from their head, which was intended and 100% not functional.
Dullahan heads now speak with the proper name of their owner, instead of having a random name attached to it at round-start.
Dullahan heads are also now properly named too.
Dullahans can now properly whisper, sing and do all these funny things that they were unable to do before.
Dullahan whispers will now properly respect the range of the whisper.
Dullahans can now succumb in hardcrit by whispering, as intended. This potentially fixes other species that worked similarly not being able to succumb, like abductors, although I didn't test if they normally could, I just know they absolutely will be able to now.
When switching from Dullahans to a different species, your old head will no longer stay behind.
I also added a proc for species to do some code when we get a ckey login in our mob, which could potentially be useful for other stuff in the future, but it was necessary here as the view is reliant on the client, which we want to ensure doesn't get weird view glitches like having their head's vision overlay while actually being centered on their body.

I also made it so say() now takes a range argument, which is 7 by default, just so things that aren't humans can also whisper and do all those kinds of things. Going with that, there's probably a few more things that will be able to be done better thanks to this, although I haven't tested every edge case with this, but I doubt it will make much of a difference in the future.

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[600995713d...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/600995713ddf9980698361eec3cb51996c5af25f)
#### Monday 2022-01-17 06:37:04 by Shoaib0597

power: Introduce Quick Charge v1.0

First of all, I would like to thank Varun Chitre for Developing a Great Fast-Charge Driver i.e., ThunderCharge for Tomato(+) Devices. Before this Driver, the Charging Time of Tomato(+) Devices was very long, sometimes even exceeding 2 and a Half-Hours! However, with the Introduction of ThunderCharge, this Slow-Charging issue was Solved. So, Thank You Varun Chitre for your Wonderful Contribution.

Now, in ThunderCharge, I observed a Potential to Achieve even More Efficiency while Charging. In my opinion, ThunderCharge suffers from the following Problems---
1. A Constant Current (mA) is Forced at all the Times of Charging without any Attention to Battery Status.
2. The above Method, I think, proves Quite Dangerous if Higher Values of Current (mA) are used because the Current (mA) remains Constant throughout the Charge-Cycle.
3. All of this creates a rigidness in the Driver and thus, Higher Values of Current (mA) are rarely used because of Probable Damage to Hardware.
4. Since all the Tomato(+) Devices suffer from Over-Heating issues, Forcing a Constant Current (mA) at all the Times of Charging may Prove Very Dangerous.

To Fix these issues, I decided to Alter the Mechanism of ThunderCharge Current Control Driver. As you all know, Qualcomm's Quick-Charge Technology Charges the Phones Quite Fast. In order to achieve this, the Battery is first Charged upto a certain % with the Max. Supported Current (mA), then the Value of Current (mA) is Dropped Gradually as the Battery nears 100%. As per the Explaination of this Technology, this is done to Avoid Damage to the Battery and Keep the Temperatures in Check. Apparently, Charging the Battery at a Constant High Current (mA) when the Battery is about to get Fully Charged, is very Dangerous and Degrades the Battery-Life quickly.

On the Basis of such Information and Technique, I have Altered the Working of ThunderCharge and turned this into a New Driver called Quick Charge v1.0. Moreover, I have Removed most of the sysFS Controls too as they are no longer Required.

Explaination of the Working of Quick Charge v1.0, developed by Shoaib Anwar a.k.a. Shoaib0597---
Battery (%)				Current (mA)
0-60					1500 (Max. Supported as per DTB)
61-90					1250
91-100					1000 (Standard Output)

Notes---
-This is NOT the Original Quick Charge v1.0 Technology from Qualcomm. I have just used the Name because the Working/Mechanism is Similar.
-The Stock Hardware doesn't supports Qualcomm's Quick Charge v1.0 Technology.
-Thus, the Charging Speed won't be as Fast as Qualcomm's Quick Charge v1.0.
-However, the Charging Speed will be the Fastest Possible on the Stock Hardware.
-In other words, this Driver is an Improved Version of ThunderCharge and Offers the Best Possible Experience and Efficiency.

Signed-off-by: Shoaib0597 <Shoaib0595@gmail.com>

---
## [Desertsafarirasalkhaimah/desertsafarirasalkhaimah](https://github.com/Desertsafarirasalkhaimah/desertsafarirasalkhaimah)@[3c0ac53681...](https://github.com/Desertsafarirasalkhaimah/desertsafarirasalkhaimah/commit/3c0ac53681c9eee15c62edf55ccc4228cd7295ea)
#### Monday 2022-01-17 07:00:49 by Desert Safari Ras Al Khaimah

Create README.md


DESERT SAFARI RAS AL KHAIMAH
Ras Al Khaimah is UAE's most exciting Desert safari destination, steeped in adventure and thrill, the iconic RAK Desert Safari is waiting for you to explore its red dunes and the legendary Emirati hospitality. Desert Safari Ras Al Khaimah offers a one-of-a-kind combination of 0utdoor activities, attractions, and accommodations. we recommend you to try one of our most popular – Evening Desert safari in Ras Al Khaimah, Overnight camping safari, Quad Bike / Dune Buggy safari, or a Camel ride tour. We offer best-value Ras Al Khaimah desert safari packages based on your interests, preferences, and budget. It's worth mentioning that we own the services and products provided to our guests, which cannot be matched anywhere else in Ras al Khaimah!!!!.

---
## [haxscramper/nimskull](https://github.com/haxscramper/nimskull)@[f35b5bf2d4...](https://github.com/haxscramper/nimskull/commit/f35b5bf2d447c10b6a104ef0649115a266e8dea6)
#### Monday 2022-01-17 07:01:42 by haxscramper

Make compiler report structured

Full rework of the compiler message handling pipeline. Remove old-style message generation that was
based purely on strings that were formatted in-place, and instead implement structured logging where
main compiler code only instantiates objects with required information.

Explanation of changes for this commit will be split into several sections, matching number of edit
iterations I had to make in order for this to work properly.

* File reorganization

In addition to the architectural changes this PR requires some type definition movements.

- PNode, PSym and PType definitions (and all associated types and enums) were moved to the
  ast_types.nim file which is then reexported in the ast.nim
- Enum defininitions for the nilability checking were moved to nilcheck_enums.nim and then
  reexported
- Enum definitions for the VM were moved to to vm_enums.nim

* New files

- Main definition of the report types is provided in the reports.nim file, together with minor
  helper procedures and definition of the ReportList type. This file is imported by options, msgs
  and other parts of the compiler.
- Implementation of the default error reporting is provided in the cli_reporter.nim - all
  disguisting hardcoded string hacks were moved to this single file. Now you can really witness the
  "error messages are good enough for me" thinking that prevailed in the compiler UX since it's
  inception.

* Changed files

Most of the changes follow very simple pattern - old-style hardcoded hacks are replaced with
structural report that is constructed in-place and then converted to string /when necessary/. I'm
pretty sure this change already puts me close to getting CS PHD - it was *unimaginably hard* to
figure out that hardcoding text formatting in place is not the best architecture. Damn, I can
probably apply to the nobel prize right now after I figure that out.

** Changes in message reporting pipeline

Old error messages where reportined via random combinations of the following:

- Direct calls to `msgs.liMessage` proc - it was mostly used in the helper templates like
  `lintReport`
- `message`
- `rawMessage`
- `fatal`
- `globalError` - template for reporting global errors. Misused to the point where name completely
  lost it's meaning and documentation does not make any sense whatsoever. [fn:global-err]
- `localError` - template for reporting necessary error location, wrapper around `liMessage`
- `warningDeprecated` - used two times in the whole compiler in order to print out error message
  about deprecated command switches.

Full pipeline of the error processing was:

- Message was generated in-place, without any colored formatting (was added in `liMessage`)
  - There were several ways message could be generated - all of them were used interchangeably,
    without any clear system.
    1. Some file had a collection of constant strings, such as `errCannotInferStaticParam = "cannot
       infer the value of the static param '$1'"` that were used in the `localReport` message
       formatting immediately. Some constants were used pretty often, some were used only once.
    2. Warning and hint messages were categorized to some extent, so and the enum was used to
       provide message formatting via `array[TMsgKind, string]` where `string` was a `std/strutils`
       formatting string.
    3. In a lot of cases error message was generated using hardcoded (and repeatedly copy-pasted)
       string
- It was passed down to the `liMessage` (removed now) procedure, that dispatched based on the global
  configuration state (whether `ignoreMsgBecauseOfIdeTools` holds for example)
- Then message, together with necessary bits of formatting (such as `Hint` prefix with coloring) was
  passed down to the `styledMsgWriteln(args: varargs[typed])` template, whcih did the final dispatch
  into
- One of the two different /macros/ for writing text out - `callStyledWriteLineStderr` and
  `callIgnoringStyle`.
  - Dispatch could happen into stdout/stderr or message writer hook if it was non-nil
- When message was written out it went into `writeLnHook` callback (misused for
  `{.explain.}` [fn:writeln-explain]) (hacked for `compiles()` [fn:writeln-compiles]) and was
  written out to the stdout/stderr.

It is now replaced with:

- `Report` object is instantiated at some point of a compilation process (it might be an immediate
  report via `localError` or delayed via `nkError` and written out later)
- `structuredReportHook` converts it to string internally. All decitions for formatting, coloring
  etc. happen inside of the structured report hook. Where to write message, which format and so on.
- `writeLnHook` /can/ be used by the `structuredReportHook` if needed - right now it is turned into
  simple convenience callback. In future this could even be replaced with simple helper proc, for
  now I left it as it is now because I'm not 100% sure that I can safely remove this.

** Changes in the warning and hint filtering

Report filtering is done in the particular *implementation* of the error hook -
`options.isEnabled()` provides a default predicate to check whether specific report can be written
out, but it must still be called manually. This allows to still see all the reports if needed. For
example, `cli_reporter.reportHook()` uses additional checks to force write some reports (such as
debug trace in `compiles()` context).

Most of the hint and warning were already categorized, altough some reports had to be split into
several (such as `--hint=Performance` that actually controlled reports for `CopiesToSink` and
`CannotMakeSink`, `--hint=Name` that controlled three reports).

None of the errors were categorized (reports from the `nkError` progress was incorporated, but in
I'm mostly describing changes wrt. to old reporting system) and all were generated in-place

** Minor related changes

- List of allowed reports is now stored in the `noteSets: array[ConfNoteSet, ReportKinds]` field of
  the `ConfigRef`, instead of *seven* separate feilds. Access is now done via getter/setter procs,
  which allows to track changes in the current configuration state.
- Renamed list of local options to `localOptions` - added accessors to track changes in the state.
- Move all default report filter configuration to `lineinfos.computeNotesVerbosity()` - previously
  it was scattered in two different places: `NotesVerbosity` for `--verbosity:N` was calculated in
  `lineinfos`, foreignPackageNotesDefault was constructed in `options`
- Changed formatting of the `internalAssert` and `internalError` messages
- Removed lots of string formatting procs from the various `sem*` modules - ideally they should
  *all* be moved to the `cli_reporter` and related.

-------

Additional notes

[fn:global-err] As I said earlier, `globalError` was misused - it is still not possible to fully get
rid of this sickening hack, since it is used for /control flow/ (you read this correct - it is an
error reporting template, and it is used for control flow. Wonderful design right?).

So, in short - `globalError` can raise `ERecoverableError` that can be caught in some other layer
(for example `sem.tryConstExpr` abuses that in order to bail out (pretty sure it was done as an
'optimization' of some sort, just like 'compiles') when expression fails to evaluate at
compile-time [fn:except])

[fn:except] https://github.com/nim-works/nimskull/pull/94#issuecomment-1006927599

[fn:writeln-explain] Of course you can't have a proper error reporting in the nim compiler, so this
hook was also misused to the point of complete nonsense. Most notable clusterfuck where you could
spot this little shit is implementation of `{.explain.}` pragma for concepts. It was implemented via
really 'smart' (aka welcome to hell) solution in

https://github.com/nim-works/nimskull/commit/74a80988d9289e8147a791c4b0939d4287baaff3 (sigmatch
~704) and then further "improved" in
https://github.com/nim-lang/Nim/commit/fe48dd1cbec500298f7edeb75f1d6fef8490346c by slicing out parts
of the error message with `let msg = s.replace("Error:", errorPrefix)`

For now I had to reuse similar hack - I *do* override error reporting hook in order to collect all
the missing report information. In the future it would be unnecessary - when concept is matched it's
body will be evaluated to `nkError` with reports that are written out later.

[fn:writeln-compiles] when `compiles()` check is executed, all error output is temporarily disabled
(both stderr and stdout) via setting allowed output flags to `{}` (by default it is set to

---
## [Texera/texera](https://github.com/Texera/texera)@[c3af4463f4...](https://github.com/Texera/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Monday 2022-01-17 07:56:07 by Albert Liu

Add PresetService (User Presets Step 3) (#1164)

Final feature demo:

![Kapture 2022-01-13 at 23 36 00](https://user-images.githubusercontent.com/12578068/149469927-b62bfa43-4701-4498-a489-565aea36da2c.gif)

---------------------------

This PR is extracted from #1041 as step 2 of the User Preset feature.

rebase of picked commits pertaining to PresetServiceService onto Albert-UserDictionaryService

PresetService provides the ability to save and "apply" collections of settings (represented by objects) that a user might find convenient to save and apply as a group. These groups are called Presets.

PresetService uses DictionaryService to store presets (it creates kind of a *view* in the database sense, of the user dictionary, that only includes Presets)

Changes from last review (for Yicong)
 - Code comments
 - fixed subscription memory leak by using takeUntil(observable), where said observable completes on NgOndestroy
 - DictionaryService now attempts to init whenever client logs in (sorry, you'll have to re-review my changes to DictionaryService)
 - PresetService now has public ready promise/value member 
   - This indicates that its init isn't complete until DictionaryService's init is complete (which is async, and cant be awaited in the constructor)
 - DeletePreset now built into PresetService (don't know why I ever didn't have that)
 - Revert Changes to Styles.scss to fix Karma test runner interface (I originally changed them as a workaround for an ng-zorro component that's no longer used)

 Note: for this step, I had less time and more complex code to test. I'm not sure I caught all the bugs, but it passes unit tests.
The quality of the code in this pr is lesser, in my opinion, so You'll have to be a little more careful on my behalf.



Co-authored-by: Zuozhi Wang <zuozhiw@gmail.com>
Co-authored-by: Yicong Huang <17627829+Yicong-Huang@users.noreply.github.com>

---
## [Kaasbv/ITTINDER-Android](https://github.com/Kaasbv/ITTINDER-Android)@[f424a8a61a...](https://github.com/Kaasbv/ITTINDER-Android/commit/f424a8a61a6f02b40130de55d974a06279762479)
#### Monday 2022-01-17 10:09:03 by JBeaart

Chat (#6)

* Added stufies

* Cleanup

* For real this time god fucking damnit

---
## [ilammy/themis](https://github.com/ilammy/themis)@[9a6b4ed019...](https://github.com/ilammy/themis/commit/9a6b4ed019464e5f2e6258482bcb7bcf42a9fa09)
#### Monday 2022-01-17 10:40:32 by Alexei Lozovsky

Update GoThemis and WasmThemis examples to 0.14.0 (#893)

* go: Update examples to GoThemis 0.14.0

* go: Update tools to GoThemis 0.14.0

* wasm: Update examples to WasmThemis 0.14.0

* wasm: Upgrade "webpack-dev-server" 3 => 4

dev-only dependency of the example. Bumping the version to get rid
of "npm audit" warnings. Of course there are breaking changes...

* wasm: Throw away more polyfills

Newer versions of webpack-dev-server start showing all the warnings from
webpack right in your face. Let's fix them then...

WasmThemis includes code paths for Node.js support. They are not used
since browsers are not Node.js, but try explaining that to webpack.
So we do that but telling it to shut up and ignore all those built-in
Node.js modules.

* wasm: Suppress more warnings about "ws" dependency

WebSockets? Why?..

Anyway. I've found this workaround that gets webpack to shut up.

* wasm: Disable subresource integrity in dev builds

webpack-subresource-integrity used by the SRIPlugin *really* does not
like being used from a development web server. It prints warnings and
webpack-dev-server throws a giant full-screen overlay right in your
face when doing "npm run start". Okay, FINE, I'll disable you...

* wasm: Check package-lock.json into the repo

WasmThemis and JsThemis already do this, let the example have it
in the repo too. GitHub will scan it for vulnerabilities for us.

* go: Update pkg.go.dev badge

Uh... I don't remember why this is done manually. I guess because
the proper badges [1] don't show neither package name, nor version?

[1]: https://pkg.go.dev/badge/?path=https%3A%2F%2Fpkg.go.dev%2Fgithub.com%2Fcossacklabs%2Fthemis%2Fgothemis

---
## [inmanta/inmanta-core](https://github.com/inmanta/inmanta-core)@[32c3945f2f...](https://github.com/inmanta/inmanta-core/commit/32c3945f2f3669e6b4c118f04e5f03b770dfa2cd)
#### Monday 2022-01-17 10:51:18 by Sander Van Balen

Configured tox to generate junit xml for pep8 failures (PR #3655)

# Description

After countless times having to parse the unreadable jenkins output for flake8 errors I thought I'd make an attempt at improving the reporting. This PR is a suggestion to have tox produce a junit report, which can be interpreted by Jenkins just like the pytest junit report.

The good:
- it's a lot easier to find pep8 violations: compare [this overview for a dummy error](https://jenkins.inmanta.com/job/core/job/inmanta-core/job/flake8-junit-experiment/3/) with the [console output for a similar error](https://jenkins.inmanta.com/job/core/job/inmanta-core/job/issue%252F3623-modules-update-dependencies/5/consoleFull)

The bad:
- it's a bit of a hack
- it makes use of a library that is no longer maintained to generate the junit xml

I believe this could be a useful addition. If the library some day becomes incompatible we can always simply drop it again since its only a dev dependency. What do you think?

In its current implementation the flake8 errors are completely removed from the console. I should be able to fix this easily but I wanted to get your thoughts on the PoC first.

# Self Check:

Strike through any lines that are not applicable (`~~line~~`) then check the box

- [ ] Attached issue to pull request
- [ ] Changelog entry
- [ ] Type annotations are present
- [ ] Code is clear and sufficiently documented
- [ ] No (preventable) type errors (check using make mypy or make mypy-diff)
- [ ] Sufficient test cases (reproduces the bug/tests the requested feature)
- [ ] Correct, in line with design
- [ ] End user documentation is included or an issue is created for end-user documentation (add ref to issue here: )

# Reviewer Checklist:

- [ ] Sufficient test cases (reproduces the bug/tests the requested feature)
- [ ] Code is clear and sufficiently documented
- [ ] Correct, in line with design

---
## [Abdelmeguid/charity_Donors_udacity_project](https://github.com/Abdelmeguid/charity_Donors_udacity_project)@[e53726e1a6...](https://github.com/Abdelmeguid/charity_Donors_udacity_project/commit/e53726e1a68858f29b370edba8cf60b197f2c7ed)
#### Monday 2022-01-17 11:32:33 by Ahmed abdelmeguid

Create README.md

Machine Learning Engineer Nanodegree
Project 3: Finding Donors for CharityML
Project Description
This is the 3rd project for the Machine Learning Engineer Nanodegree. In this project, I used sklearn and supervised learning techniques on data collected for the U.S. census to help a fictitious charity organization identify people most likely to donate to their cause.

Here, I first investigate the factors that affect the likelihood of charity donations being made. Then, I use a training and predicting pipeline to evaluate the accuracy and efficiency/speed of three supervised machine learning algorithms (GaussianNB, SVC, Adaboost). I then proceed to fine tune the parameters of the algorithm that provides the highest donation yield (while reducing mailing efforts/costs). Finally, I also explore the impact of reducing number of features in data.

Install
This project requires Python 2.7 and the following Python libraries installed:

NumPy
Pandas
matplotlib
scikit-learn
You will also need to have software installed to run and execute an iPython Notebook

We recommend students install Anaconda, a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.

Code
The main code for this project is located in the finding_donors.ipynb notebook file. Additional supporting code for visualizing the necessary graphs can be found in visuals.py. Additionally, the Report.html file contains a snapshot of the main code in the jupyter notebook with all code cells executed.

Run
In a terminal or command window, navigate to the top-level project directory finding_donors/ (that contains this README) and run one of the following commands:

ipython notebook finding_donors.ipynb
or

jupyter notebook finding_donors.ipynb
This will open the iPython Notebook software and project file in your browser.

Data
The modified census dataset consists of approximately 32,000 data points, with each datapoint having 13 features. This dataset is a modified version of the dataset published in the paper "Scaling Up the Accuracy of Naive-Bayes Classifiers: a Decision-Tree Hybrid", by Ron Kohavi. You may find this paper online, with the original dataset hosted on UCI.

Features

age: Age
workclass: Working Class (Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked)
education_level: Level of Education (Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool)
education-num: Number of educational years completed
marital-status: Marital status (Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse)
occupation: Work Occupation (Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces)
relationship: Relationship Status (Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried)
race: Race (White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black)
sex: Sex (Female, Male)
capital-gain: Monetary Capital Gains
capital-loss: Monetary Capital Losses
hours-per-week: Average Hours Per Week Worked
native-country: Native Country (United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands)
Target Variable

income: Income Class (<=50K, >50K)

---
## [google/error-prone](https://github.com/google/error-prone)@[fa6b82c77d...](https://github.com/google/error-prone/commit/fa6b82c77deb00cdf7b34561232f116c7bbdf8b4)
#### Monday 2022-01-17 11:44:49 by ghm

AlreadyChecked: handle early returns.

Also, use WellKnownMutability again to assume that _instance_ methods on immutable types are pure.

i.e., for the remainder of the method body in

```
void foo(boolean a) {
  if (a) {
    return;
  }
  // ...
}
```

`a` is known to be false.

Implementing tests for this made me realise my thinking was a bit flawed when looking for occurrences of known truths/falsehoods; really, we should be checking for all boolean expressions which might be known (and hence misleading).

I've done this instead, but in turn it inspired a heursitic to avoid annoying findings for stuff like:

```
if (isEmpty) {
  message.setIsEmpty(isEmpty);
}
```

Because that finding is quite low-value, and what would you suggest instead? If it's more than just a setter, you'd want a parameter comment

PiperOrigin-RevId: 420265440

---
## [idan054/my_tests](https://github.com/idan054/my_tests)@[50a6513649...](https://github.com/idan054/my_tests/commit/50a65136497339eec61cf6dbf69ea0b025d86075)
#### Monday 2022-01-17 12:04:22 by Idan054

V6
+ Cookies user changed detection
+ bug fix because get_pen_msgs() sucks

V5 Requests.Stips Project: (Just better)
It's a mini projects, sorry for no details cuz I don't give a fuck

V2.1 Requests.Stips Project:
+ login_stips.py >> ReNamed >> A1_LoginStips.py
+ A23_OnlineNotification.py: get_notifications() & check_online_user()

V1 Requests.Stips Project:
 + main_stips.py
 + login_stips.py

---
## [ZeLebo/POC](https://github.com/ZeLebo/POC)@[ce648aff0d...](https://github.com/ZeLebo/POC/commit/ce648aff0da1c1fb40777d593509f2a21bbb6304)
#### Monday 2022-01-17 14:47:57 by =

Hello, it's me
I was wondering if after all these years you'd like to meet
To go over everything
They say that time's supposed to heal ya
But I ain't done much healing
Hello, can you hear me?
I'm in California dreaming about who we used to be
When we were younger and free
I've forgotten how it felt before the world fell at out feet
There's such a difference between us
And a million miles
Hello from the outside
I must've called a thousand times
To tell you I'm sorry for everything that I've done
But when I call, you never seem to be home
Hello from the other side
At least I can say that I've tried
To tell you I'm sorry for breaking your heart
But it don't matter, it clearly doesn't tear you apart anymore...

---
## [majestrate/session-pysogs](https://github.com/majestrate/session-pysogs)@[31bfd14d80...](https://github.com/majestrate/session-pysogs/commit/31bfd14d80ec723fde3c3589408a27fc878f247f)
#### Monday 2022-01-17 15:39:06 by Jason Rhinelander

Use SQLAlchemy for database backend

We're using it fairly minimally: essentially still writing manual
queries, but now using SQLAlchemy to handle placeholder binding which is
nicer, and portable.

The API now goes like this:

- `db.get_conn()` returns a connection from the connection pool;
  web.appdb, in particular, is a preloaded, app-context connection
  object that most code uses.

- `web.query()` does an SQLAlchemy 'text' query, which is almost like
  regular prepare+bind+execute, except that it always uses `:name` for
  placeholders and binds using `name=...` keyword arguments.  That is,
  instead of:

      db.execute("SELECT token FROM rooms WHERE id = ?", (123,))

  we now do:

      query("SELECT token FROM rooms WHERE id = :id", id=123)

  or equivalently:

      db.query(appdb, "SELECT token FROM rooms WHERE id = :id", id=123)

  (the latter version is more useful where an app context doesn't exist
  and you need to pass in some other conn, such as is now done in
  __main__).

- transactions are now controlled with a `with appdb.begin_nested():`
  context, replacing the custom nested tx handler I made for sqlite.

We *could* start using more advanced SQLAlchemy query composition, but
that seems like more of a pain rather than something useful.  (I *don't*
want to use SQLAlchemy ORM, because in my experience ORM just gets in
the way as soon as you want non-trivial database structure, which we
have here).

This will allow us to (easily) add postgresql support.  (Other database
are probably a no-go: SQLite has long looked up to postgresql for
features and syntax and so the two are very similar dialects).

---
## [wanted2/wanted2.github.io](https://github.com/wanted2/wanted2.github.io)@[aecd668a84...](https://github.com/wanted2/wanted2.github.io/commit/aecd668a841f36ead83869089ed86dac99e9c146)
#### Monday 2022-01-17 16:13:48 by wanted2

[1;36m"I grew up in a bookless house - my parents didn't read poetry, so if I hadn't had the chance to experience it at school I'd never have experienced it. But I loved English, and I was very lucky in that I had inspirational English teachers, Miss Scriven and Mr. Walker, and they liked us to learn poems by heart, which I found I loved doing."[1;m
		[1;35m--Carol Ann Duffy[1;m[0m

---
## [MLM-INTELLIGENCE/network-marketing-quotes](https://github.com/MLM-INTELLIGENCE/network-marketing-quotes)@[8fa53e8337...](https://github.com/MLM-INTELLIGENCE/network-marketing-quotes/commit/8fa53e8337b588b5add419f95b16216bb1111ba6)
#### Monday 2022-01-17 17:03:30 by MLM-INTELLIGENCE

mlmintelligence.com

Quotes from Robert kiyosaki

1.	Network marketing gives people the opportunity, with very low risk and very low financial commitment, to build their own income-generating asset and acquire great wealth. –  Robert kiyosaki

2.	“A network marketing business is based upon the leaders pulling people up, while a traditional corporate or government business is based upon only promoting a few and keeping the masses of employees content with a steady paycheck.”  - Robert kiyosaki

3.	“By its very nature and design, Network Marketing is a strikingly Fair, Democratic, Socially Responsible system of generating wealth.” – Robert kiyosaki

4.	“If I had to do it all over again, rather than build an old style type of business, I would have started building a network marketing business.” – Robert kiyosaki

5.	For people choosing to use a network marketing system to build a business in the B quadrant, the price of entry is a lot lower, the risks are lower, and the education and support are there to guide you through this personal development process. – Robert kiyosaki

6.	A network marketing business is the perfect business for people who like helping other people. – Robert kiyosaki

7.	If you are a person with big dreams and would love to support others in achieving their big dreams, then the network marketing business is Certainly a business for you.. – Warren buffet

8.	You can start your business part-time at first and then as your business grows, you can help other people start their part-time business. This is a value worth having - a business and people who help others make their dreams come true – Robert kiyosaki
9.	The network marketing industry offers many unique benefits to those who want more out of life. – Robert kiyosaki
10.	If you cannot sell, you cannot be an entrepreneur. If you cannot sell, you cannot raise money. if the thought of sales terrifies you, get a job at a dept. store and start there. Or get a job with a company like Xerox that requires that you go around to businesses and knock on doors. As your courage increases, you may want to try a company in network marketing or direct sales that is willing to train you. – Robert kiyosaki
11.	Network marketing is no longer on trial. It’s a Proven and viable profession. A profession that’s helping millions of people get ahead financially and moving them closer to their dreams. – Art jonak
12.	“ If I would be given a chance to start all over again, I would choose network marketing “ – Bill gates
13.	“ The future of network marketing is unlimited. There’s no end in sight. It will continue to grown because better people are getting into it… soon, It will be one of the most respected business methods in the world.” – Brian tracy
14.	“ The future of network marketing is unlimited. It has probably made more millionaire of more people in more countries than any other form of business starting from nothing. There’s no end in sight. It will continue to grow. Because better people are getting into it. It will become one of the respected business methods in the world .” –  Brian tracy
15.	“ People don’t trust conglomerates: They trust individuals. Network marketing Brings trust and the quality of the relationship to the center of the business. And it enables you to expand indefinitely, Simply by expanding the number of relationship” – Brian tracy
16.	“ I am often asked if network marketing is a pyramid scheme. My reply is that corporations really are pyramid schemes. A corporation has only one person at the top, Generally the ceo, and everyone else below.” – Donald trump
17.	“The richest people in the world look for and build networks, Everyone else looks for work.”- Robert kiyosaki 
18.	“ Network marketing gives you the opportunity to face your fears, deal with them, overcome them , and , bring out the winner that you have living inside you.”- Robert kiyosaki

19.	“ Successful people take big risks knowing that they might fall hard. But, they Might succeed more than they ever dreamed, Too.”- Robert kiyosaki
20.	“ Why I recommend network marketing the network marketing industry offers many unique benefits to those who want more out of life.” – Robert kiyosaki
21.	“ one of the greatest benefits of being involved in network marketing is the person you’ll have to become inorder to rise through the ranks. I don’t think people don’t talk about that benefit enough. Your personal growth doesn’t just affect you…. It improves the lives of every person you touch.”- Eric Worre 
22.	“ You can’t approach network marketing like an employee. You have to have an entrepreneur mindset.” – Eric Worre
23.	“ There’s nothing wrong with selling. The sales people of the world drive the economy. People I network marketing are ‘Super salespeople’. We educate the world.” – Eric worre 
24.	“ It will take you abut one year to become competent and profitable in network marketing. You’ll know the basics, you’ll cover expenses, and you’ll be learning. It will take about three years of consistent part- time effort in order to go full- time. It will take about five years of consistent effort to become a six figure earner or above. And it will take about seven years of consistent effort to become an expert.” – Eric worre
25.	“ In network marketing, the people who attract, train and motivate the most sales people earn the most money.” – Richard brooke
26.	“ What I have found is that most people fall in their network marketing business because they are not coachable.” – Brian Carruthers
27.	“Direct selling is one of the few places where women earn dollar for dollar what men earn.” – Art jonak
28.	“ Network marketing is the big wave of the future. It’s taking the place of franchising, Which now requires too much capital for the average person.” – Jim Rohn
29.	“Network marketing is the only industry that allow common people to earn millions with a minimal investment and zero overhead, coupled with total time freedom and the joy of global travel. There are three magic words that worked for all of us who have made it to the pinnacle and they’ll work for you: ‘Just don’t quit.’ “ – Mark yarnell
30.	“ Of all the entrepreneurial opportunities available today, One of the most important I direct selling, also called network marketing.” – Paul zone pilzer
31.	“ What you sow, You reap. It’s a law of nature. Network marketing is perfectly aligned with that. You get truly, Exactly what you’re worth! No nepotism, no favoritism. That’s rare today.”-Bob proctor
32.	“ When I read in fortune magazine that warren buffet, the billionaire investor and one of the world’s richest man, was investing in a direct sales ( network marketing ) company, I decided I was missing something. “ – David bach
33.	Having a good network can be invaluable. It opens doors for you and alow you to enter into opportunities that are beneficial to your business.  -  Richard branson
34.	“ You will meet people who believe all network marketing opportunities are pyramid schemes. Why spend all your time trying to convince them otherwise when there are legions of people who are open to what you have ? “ – Randy gage
35.	“A billionaire one of the world’s biggest investor, Now he invest in network marketing.” – warren buffet
36.	“ If you can dream it, then you can achieve it. You will get all you want in life if you help enough other people get what they want.” – Zig ziglar
37.	The ‘Catch’  to network marketing : You must accept a temporary loss of social esteem from ignorant people  - Eric wore
38.	“ You strengthen our country and our economy, not just by striving for your own success. But by offering the opportunity to others. Your industry gives prople a chance, after all to make the most of their own lives. And to me, that’s the heart of the American dream.” – Bill Clinton
39.	Network marketing is really the greatest source of grass root capitalism, because it teaches people how to take a small bit of capita. That is your time, and build the American dream.” – Jim Rohn
40.	I think network marketing has some of age. It’s become indeniable that it’s a viable way to entrepreneurship and independence for millions of people.” – Stephen covey
41.	Network marketing is a tremendous contribution to the overall prosperity of the economy.” -  Tony Blair
42.	I would go in network marketing immediately. I think if it didn’t exist, We should invent it. It is that good.” – Bob proctor
43.	What’s beautiful about network marketing is that you’ve got all the benefits of being an owner but you do not have to worry about supply chain. You do not have to worry about accounting especially in the world we are today. There are really some great companies out there . Network marketing is amazing.” – Anthony robbins
44.	One branch of the virgin group that often goes unmentioned is vie at home a network marketing company formerly known as virgin vie. Vie at home made over $60 million its first year of existence. – Richard branson
45.	It’s amazing how people think 4 years is a long time to succeed in a business but think it’s alright to stay broke at a job for 40 years. – Art jonak
46.	One of the best investment I’ve ever made, Network marketing today is more widely accepted than at any time in its 60+ years history. – Warren buffet
47.	If you don’t have any residual income or passive income, or at least a plan for residual income, You’re living a very risky life. There is no security in a job, even a high paying one. Be smart and don’t rely on just one source of income. – Ray higdon
48.	If you make your business about helping others, You’ll always have plenty of work. – Chris Guillebeau
49.	In network marketing , the whole point is not to sell a products but to build a network, an army of people who are all representing that same products or services to share with others. – Robert kiyosaki
50.	Effective network marketers have a clear vision and passion for that vision. They know what they want to achieve where they see themselves  in their business organization. Everything they do, Every activity they perform, is driven by that vision. – Stephen covey

---
## [arkaslittlemind/Competitive-Programming](https://github.com/arkaslittlemind/Competitive-Programming)@[a2c09d7b70...](https://github.com/arkaslittlemind/Competitive-Programming/commit/a2c09d7b70cc318536fe08a8197dbe477515a5b8)
#### Monday 2022-01-17 17:10:26 by Arkadipta Mojumder

Create 141A Amusing Joke.cpp

So, the New Year holidays are over. Santa Claus and his colleagues can take a rest and have guests at last. When two "New Year and Christmas Men" meet, thear assistants cut out of cardboard the letters from the guest's name and the host's name in honor of this event. Then the hung the letters above the main entrance. One night, when everyone went to bed, someone took all the letters of our characters' names. Then he may have shuffled the letters and put them in one pile in front of the door.

The next morning it was impossible to find the culprit who had made the disorder. But everybody wondered whether it is possible to restore the names of the host and his guests from the letters lying at the door? That is, we need to verify that there are no extra letters, and that nobody will need to cut more letters.

Help the "New Year and Christmas Men" and their friends to cope with this problem. You are given both inscriptions that hung over the front door the previous night, and a pile of letters that were found at the front door next morning.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1f2b277535...](https://github.com/mrakgr/The-Spiral-Language/commit/1f2b277535f831fde3744fafa27f0a43d69ab76a)
#### Monday 2022-01-17 19:24:30 by Marko Grdinić

"9:30pm. https://www.houdini-course.com/

Let me watch some of the vids here. The first vid in the introduction where he discusses 5 different workflows is pretty informative to me. I was not aware of the subfield differences in 3d.

What I want from 3d is not even on the list. It is close to visualization, but I do not have such high demands for fidelity.

https://www.houdini-course.com/BASICS/335/129
> 8gb is not enough.

Yeah, the memory capacity of my rig is crap. VFX are no clouch.

The above site basically has zero content in its free section. I have no idea why he did not give the full fundamentals section at least instead of just having some disconnected vids.

11:50pm. https://blender.stackexchange.com/questions/250477/is-it-possible-to-get-the-result-of-applying-the-geometry-node-modifier-on-a-cur

Decided to ask this.

I'll see if I get an answer tomorrow.

1:10am. Got an answer 10m ago. It seems there is a setting to turn visual geometry to a mesh. Great. This is just what I needed. Let me go to bed here.

1/17/2022

10:20am. https://blender.stackexchange.com/questions/250477/is-it-possible-to-get-the-result-of-applying-the-geometry-node-modifier-on-a-cur

I am getting up earlier. I've stopped playing games for the time being and have gone back to reading Hero's Daughter which is less demanding on my mental energy.

10:25am. Ok, focus me, I think that realize instances is broken and I should make a bug report. Let me test it first.

https://developer.blender.org/T93903
Make Instances Real doesn't work for geometry instances

It is already open. I see.

10:35am. Ok, let me chill a bit. I'll read Ayakashi and then start.

11:10am. Let me start.

11:30am. Let me put in the exponent as passthrough for the density input. Blender Guru got this thing wrong.

Also to help with sizing of nearby branches...

Yeah, let me not modify the power. Instead, let me just add to the size outright.

11:50am. I am thinking how I am going to do this. I am going to use the node for the flower as the basis of something bigger.

12:05pm. I am still a novice.

I might be good at programming regular stuff, but I see that my way of doing things is wrong when doing geometry.

I am subconsciously trying to generalize my code, but that is working against me in this domain.

12:10pm. Nope, geo nodes can't be recursive.

12:25pm. I am trying to get it to select randomly between leaf and branch, but it is not working. The random value is red when I connect it to the switch.

12:35pm. https://youtu.be/nReSOasTuYs
[Tut] Random Selection of Objects from Geometry Node Tree - Blender Geometry Nodes 3.0 Field

I sure am spending my time on this. I decided to Google it in the end.

https://youtu.be/nReSOasTuYs?t=7

Ohhh, I am noticing that he is using the instance index and pick instance.

https://youtu.be/nReSOasTuYs

Let me watch this again. I am having trouble dealing with this.

https://youtu.be/nReSOasTuYs?t=46

Damn it, I am not sure this would work because I am inputting curves.

1:20pm. I've realized something - I hate geometry nodes. They are so difficult to deal with except on small examples.

1:40pm. I am going insane here. Let me stop for a bit.

2:55pm. Done with breakfast and chores. Let me chill a bit.

Sigh, things are not going well at all. My programming intuition is constantly working against me.

3:15pm. Let me read the latest Girls Frontline chapter and I will resume.

3:30pm. Let me resume.

The way things are going, all this would be a lot faster if I did it all by hand. But if I did that, I would never push the limits of geo nodes. It is inevitable that I would waste time as a greenhorn.

Right now I've opened a new file. It feels like I am making a mess in the belubell one. I want to focus solely on the problem at hand - how do I sample instances from a collection with a certain probability. So far I've gone down one wrong path after another. It is ridiculous.

Also I want to figure out how to randomize the instances a bit. That is actually proving quite difficult as well. I did not think things would go this way.

https://www.youtube.com/watch?v=nReSOasTuYs
[Tut] Random Selection of Objects from Geometry Node Tree - Blender Geometry Nodes 3.0 Field

Let me finally watch this start to finish. It is 1.5 minutes long and I still haven't done it.

https://youtu.be/PgZrIToTdJE
[Tut] Recursive Subdivision - Blender Geometry Nodes 3.0 Field

I'll watch this later. Let me play with sampling instances.

3:40pm. I have a tube, and am trying to figure out how to create cone with random depth on it. I didn't think this would be a problem, but it is.

https://blender.stackexchange.com/questions/220721/how-can-i-get-a-new-random-seed-for-every-object-using-the-same-geometry-nodes
https://blender.stackexchange.com/questions/159431/randomizing-instanced-objects/159469#159469

3:50pm. https://blender.community/c/rightclickselect/k206/?sorting=hot

This is exactly what I need. And it shows me how to make multiple instances.

Doing something like selecting a leaf or a branch with certain probabilities would be a pain in the ass with this.

https://www.sidefx.com/docs/houdini/copy/tutorial_stamping.html
> int(rand($PT) * 6) * 2 + 8

Houdini seems to have actual expressions and that $PT reminds me of Perl variables. That is probably what it is. I find the lack of variables really painful when working with geo nodes in Blender.

4pm. I've actually set Houdini to download. I simply am not going to be able to satisfy my procedural content generation urge with Blender's current power.

4:10pm. I think I fully internalized how to pick uniformly from instances. It is convoluted, but it will do. Now...

https://youtu.be/PgZrIToTdJE
[Tut] Recursive Subdivision - Blender Geometry Nodes 3.0 Field

Let me watch this just for a bit. I do not think the above should be possible without actual recursion. I'll have to take a look.

https://youtu.be/PgZrIToTdJE?t=480

I am not following this carefully, but he took a moment to state that they are cutting a grid. Yeah, that makes sense. That oculd be a good way of doing it.

https://youtu.be/PgZrIToTdJE?t=526

Oh great. You can connect them quickly by hitting F.

4:30pm. No I can't accept this. This is too much effort.

Geo nodes are programming, but no variable bindings, no recursion, flat namescape with no modules. All this is a hard hit to me. I can't even make slightly complex mathematical expressions without feeling the mental burden of keeping track of the nodes.

4:35pm. Houdini just finished downloading, but I will leave it for later.

4:40pm. I need to gather my thoughts. I feel like I understand Blender's limitations much better now. I can't do too many interesting things with geometry nodes.

With the new knowledge, I need to think about which limitations I can accept and which I can not. I need to rethink my workflow.

4:55pm. Hrmmm, this wasn't how I thought things would go.

Even something as simple as distributed simple flowers with leaf variation in their stalks would be highly difficult. The geo nodes example that I've seen were highly elaborate if abstract, which tricked me into thinking Blender was more capable that it should be.

I thought that geo nodes would be limited to map operations. It seems that even nested maps are trouble. It is a lot more limited than I thought.

5pm. Let me take a break while Houdini finishes installing.

5:30pm. I am back. Hrrrmmmm...let me use a temp email for the license server.

5:50pm. I don't know, maybe I am doing something wrong, but I can't crack Houdini. For some reason it is not accepting the keys. All the licenses have an availability of 0 for me. Let me uninstall it. This thing is of no use to me.

https://www.sidefx.com/products/compare/

It seems the apprentice license is free. Maybe I should just get that.

6:20pm. Got distracted by a reply.

6:40pm. Had to leave for lunch.

https://www.sidefx.com/products/houdini-apprentice/

Let me just get this.

At this point, I am just interested in trying Houdini out rather than to do anything serious with it. Blender would really be much more useful if I could randomize the instances, just putting identical clones is only good for fences and motion graphics.

6:45pm. Houdini wants me to reset for some reason. Let me do it.

6:50pm. This is so strange. I installed the launcher, but I can't see any shortcuts being added anywhere. What the hell?

I had to go into the directory directly and run the laucher. How confusing.

6:55pm. I think I'll close here. I do not feel like trying to push forward. Instead what I in fact need to do is take a step back.

...Remember the scatter addon?

I am going to skip geometry ndoes and go back to the basics. I'll make a bunch of basic flowrs and scatter them on the wines using that.

Actually, no, if it is just scattering from an instance, geo nodes would be ideal for that. It is just that I am going to have to do mroe by hand. And that is fine.

So far I've been pushing forward with the intention of maximally generalizing my work. But if I focus on working within the alloted limits I should make a lot stronger progress. Blender should still be the best for the kind of concept art that I want to do even with its primitive capabilities to do procedural content.

Further gains in that area I'll get by studying Houdini.

7:05pm. The kind of approach I'll take to finish the scene is that I'll make 5 different kinds of flowers and spread them out. Even if not every flower will be unique like in nature, that should be enough variation to satisfy me.

I am going to start by going over the code for the Bluebell again. I think it was a mistake to deal in factors so heavily. Instead I should use absolute values more. That was a design error pure and simple by myself. As a programmer, I've been trained to abstract them away instead of expose them, but in 3d art I should in fact do the opposite. I need to expose as much of the functionality in the input attributes and then play with it in the inputs.

Also though I am disillussioned by current capabilities of geometry nodes, the capabilities they currently provide should still be a significant enhancement.

7:20pm. The stupid thing is still installing. I'll give it a try later. Let me take off here. I really did not accomplish much today, but eventually I will catch wind. Every day, I make a step, and every day I come close to my goal. Will I reach it first, or will I fall before that? The only thing that is certain is if I do not move, I will never reach reach it. So I must keep moving.

I really did enjoy modeling the flowers, so I hope I can do more of that tomorrow. I need to buckle down and start doing things. Hopefully I can continue to keep getting up earlier.

7:30pm. Actually, since I finally got it to run let me study some of the introductory materials for Houdini.

https://www.sidefx.com/learn/collections/houdini-foundations/

https://media.sidefx.com/uploads/tutorial/foundations/houdini_foundation_overview_01.pdf
> GOING PROCEDURAL
> In Houdini, every action you take in the viewport is stored as a node. These nodes are then “wired” into networks which define a “recipe” that can be tweaked to define the outcome then repeated to create similar yet unique results. The ability for nodes to pass important information, in the form of attributes, down the chain helps give Houdini its procedural nature.

This is quite interesting. It reminds me Blender scripting, but this might be better due to its immutability.

7:45pm. The above document is useless as an intro. It should be a part of the manual.

https://media.sidefx.com/uploads/tutorial/foundations/h19/hfoundations_02_model_render_animate.pdf

Let me just read this now, I'll consider actually following this tomorrow.

8:05pm. Went over the pdf. I'll decide whether I want to study Houdini or do the Blender scene tomorrow. I admit, Houdini seems like my kind of program. This is quite advanced though. if it wasn't for my Blender epxerinece, the material would be very overwhelming.

8:10pm. Sigh...I'll probably study Houdini. If not this soccer ball tutorial, I'll probably watch the 'Houdini Is Not Scary' series of lectures. Even if I end up doing all by hand in Blender with some light help from geo nodes, I have the urge to reach the appex of skill in whatever I am endeavoring. Given how Blender is developing, its geo nodes will get more advanced capabilities months and years down the road. That does not matter now, but just like my Blender experience will be transferable to Houdini, so will the Houdini experience be transferable back. So I should not hold back on learning different tools. At some point I am going to finish my education. There is not an infinite amount of these tutorials to go through.

8:15pm. I am not interested in other 3d tools, but Houdini specifically caught my attention due to how it works. There is a lot of room for me to get better in 3d art, and like in programming, simply mastering a better tool might be one of the best way to get to the apex. I've found geo nodes inspiring, but now I am disillusioned by them.

Houdini is the last stone left unturned for me. I am going to satisfy this curiosity of mine, and then focus on mastering the basics."

---
## [tmakgit/dwm](https://github.com/tmakgit/dwm)@[67d76bdc68...](https://github.com/tmakgit/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Monday 2022-01-17 20:03:35 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [newstools/2022-naija-news-agency](https://github.com/newstools/2022-naija-news-agency)@[72cb27ed2f...](https://github.com/newstools/2022-naija-news-agency/commit/72cb27ed2fd576dd2eb6d4d317c4e7a42a42234d)
#### Monday 2022-01-17 23:30:07 by Billy Einkamerer

Created Text For URL [naijanewsagency.com/video-hilarious-moment-chimamanda-adichie-told-a-woman-to-manage-her-boyfriend/]

---

