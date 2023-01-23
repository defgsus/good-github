## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-22](docs/good-messages/2023/2023-01-22.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,977,423 were push events containing 2,582,215 commit messages that amount to 142,897,463 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [rcgale/wiktionary-content](https://github.com/rcgale/wiktionary-content)@[9a81424ba2...](https://github.com/rcgale/wiktionary-content/commit/9a81424ba212d2e0378edbe0d66872d5d9b3d860)
#### Sunday 2023-01-22 00:03:28 by 165.138.51.13

[cat#2162967](https://en.wiktionary.org/w/index.php?pageid=36&oldid=2162967)
Replacing page with 'Cat's, a very annoying type of animal. Cat's are so fucking annoying. I even had to shoot one once. There was blood everywhere. If you like cat's you were born from a mother fu...'

---
## [Erol509/tgstation](https://github.com/Erol509/tgstation)@[a753229ee2...](https://github.com/Erol509/tgstation/commit/a753229ee2541e32164772f05330669d3c6b75d8)
#### Sunday 2023-01-22 00:53:25 by GoldenAlpharex

Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.


<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.


![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @MrMelbert about it and he gave me the go-ahead, as can be seen
here:


![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

---
## [Erol509/tgstation](https://github.com/Erol509/tgstation)@[35b5ac0c4e...](https://github.com/Erol509/tgstation/commit/35b5ac0c4e6bbaf2adf277a7ea7a4a4eab89726b)
#### Sunday 2023-01-22 00:53:25 by Fikou

Psykers (#71566)

## About The Pull Request
Finishes #66471
At burden level nine (or through a deadly genetic breakdown), you now
turn into a psyker.
This splits your skull in half and transforms it into a weird fleshy
mass. You become blind, but your skull is perfectly suited for sending
out psychic waves. You get potent psy abilities.
First one is brainwave echolocation, inspired by Gehennites (but not as
laggy).
Secondly, you get the ability of Psychic Walls, which act similarly to
wizard ones, but last shorter, and cause projectiles to ricochet off
them.
Thirdly, you get a projectile boost ability, this temporarily lets you
fire guns twice as fast and gives them homing to the target you clicked.
Lastly, you get the ability of psychic projection. This terrifies the
victim, fucking their screen up and causing them to rapidfire any gun
they have in their general direction (they'll probably miss you)
With most of the abilities being based around guns, a burden level nine
chaplain now gets a new rite, Transmogrify. This lets them turn their
null rod into a 5-shot 18 damage .77 revolver. The revolver possesses a
weaker version of antimagic (protects against mind and unholy spells,
but not wizard/cult ones). It is reloaded by a prayer action (can also
only be performed by a max burdened person).
General Video: https://streamable.com/w3kkrk
Psychic Projection Video: https://streamable.com/4ibu7o

![image](https://user-images.githubusercontent.com/23585223/204150279-a6cf8e2f-c678-476e-b72c-6088cd8b684b.png)

## Why It's Good For The Game
Rewards the burdened chaplain with some pretty cool stuff for going
through hell like losing half his limbs, cause the current psychics dont
cut it as much as probably necessary, adds echolocation which can be
used for neat stuff in the future (bat organs for DNA infuser for
example).

## Changelog
:cl: Fikou, sprites from Halcyon, some old code from Basilman and
Armhulen.
refactor: Honorbound and Burdened mutations are brain traumas now.
add: Psykers. Become a psyker through the path of the burdened, or a
genetic breakdown.
add: Echolocation Component.
/:cl:

Co-authored-by: tralezab <spamqetuo2@gmail.com>
Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[23a858c902...](https://github.com/seanpdoyle/turbo/commit/23a858c902070ad7898d773053176ba45c7fe946)
#### Sunday 2023-01-22 01:14:56 by Sean Doyle

Extract `FrameVisit` to drive `FrameController`

The problem
---

Programmatically driving a `<turbo-frame>` element when its `[src]`
attribute changes is a suitable end-user experience in consumer
applications. It's a fitting black-box interface for the outside world:
change the value of the attribute and let Turbo handle the rest.

However, internally, it's a lossy abstraction.

For example, when the `FrameRedirector` class listens for page-wide
`click` and `submit` events, it determines if their targets are meant to
drive a `<turbo-frame>` element by:

1. finding an element that matches a clicked `<a>` element's `[data-turbo-frame]` attribute
2. finding an element that matches a submitted `<form>` element's `[data-turbo-frame]` attribute
3. finding an element that matches a submitted `<form>` element's
   _submitter's_ `[data-turbo-frame]` attribute
4. finding the closest `<turbo-frame>` ancestor to the `<a>` or `<form>`

Once it finds the matching frame element, it disposes of all that
additional context and navigates the `<turbo-frame>` by updating its
`[src]` attribute. This makes it impossible to control various aspects
of the frame navigation (like its "rendering" explored in
[hotwired/turbo#146][]) outside of its destination URL.

Similarly, since a `<form>` and submitter pairing have an impact on
which `<turbo-frame>` is navigated, the `FrameController` implementation
passes around a `HTMLFormElement` and `HTMLSubmitter?` data clump and
constantly re-fetches a matching `<turbo-frame>` instance.

Outside of frames, page-wide navigation is driven by a `Visit` instance
that manages the HTTP life cycle and delegates along the way to a
`VisitDelegate`. It also pairs calls to visit with a `VisitOption`
object to capture additional context.

The proposal
---

This commit introduces the `FrameVisit` class. It serves as an
encapsulation of the `FetchRequest` and `FormSubmission` lifecycle
events involved in navigating a frame.

It's implementation draws inspiration from the `Visit`, `VisitDelegate`,
and `VisitOptions` pairing. Since the `FrameVisit` knows how to unify
both `FetchRequest` and `FormSubmission` hooks, the resulting callbacks
fired from within the `FrameController` are flat and consistent.

Extra benefits
---

The biggest benefit is the introduction of a DRY abstraction to
manage the behind the scenes HTTP calls necessary to drive a
`<turbo-frame>`.

With the introduction of the `FrameVisit` concept, we can also declare a
`visit()` and `submit()` method for `FrameElementDelegate`
implementations in the place of other implementation-specific methods
like `loadResponse()` and `formSubmissionIntercepted()`.

In addition, these changes have the potential to close
[hotwired/turbo#326][], since we can consistently invoke
`loadResponse()` across `<a>`-click-initiated and
`<form>`-submission-initiated visits. To ensure that's the case, this
commit adds test coverage for navigating a `<turbo-frame>` by making a
`GET` request to an endpoint that responds with a `500` status.

[hotwired/turbo#146]: https://github.com/hotwired/turbo/pull/146
[hotwired/turbo#326]: https://github.com/hotwired/turbo/issues/326

---
## [HackerFoo/bevy](https://github.com/HackerFoo/bevy)@[4847f7e3ad...](https://github.com/HackerFoo/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Sunday 2023-01-22 01:19:12 by ira

Update codebase to use `IntoIterator` where possible. (#5269)

Remove unnecessary calls to `iter()`/`iter_mut()`.
Mainly updates the use of queries in our code, docs, and examples.

```rust
// From
for _ in list.iter() {
for _ in list.iter_mut() {

// To
for _ in &list {
for _ in &mut list {
```

We already enable the pedantic lint [clippy::explicit_iter_loop](https://rust-lang.github.io/rust-clippy/stable/) inside of Bevy. However, this only warns for a few known types from the standard library.

## Note for reviewers
As you can see the additions and deletions are exactly equal.
Maybe give it a quick skim to check I didn't sneak in a crypto miner, but you don't have to torture yourself by reading every line.
I already experienced enough pain making this PR :) 


Co-authored-by: devil-ira <justthecooldude@gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[d5f1e2bdab...](https://github.com/treckstar/yolo-octo-hipster/commit/d5f1e2bdab730842ade86d570c5815be82a562e0)
#### Sunday 2023-01-22 01:22:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Vhmit/kernel_asus_msm8937](https://github.com/Vhmit/kernel_asus_msm8937)@[5038fccf4e...](https://github.com/Vhmit/kernel_asus_msm8937/commit/5038fccf4e9da65d524f4fb93f58725a3c1ed360)
#### Sunday 2023-01-22 01:44:52 by Steven Barrett

ZEN: Implement zen-tune v4.12

4.9:
In a surprising turn of events, while benchmarking and testing
hierarchical scheduling with BFQ + writeback throttling, it turns out
that raising the number of requests in queue _actually_ improves
responsiveness and completely eliminates the random stalls that would
normally occur without hierarchical scheduling.

To make this test more intense, I used the following test:

Rotational disk1: rsync -a /source/of/data /target/to/disk1
Rotational disk2: rsync -a /source/of/data /target/to/disk2

And periodically attempted to write super fast with:
dd if=/dev/zero of=/target/to/disk1/block bs=4096

This wrote 10gb incredibly fast to writeback and I encountered zero
stalls through this entire test of 10-15 minutes.

My suspicion is that with cgroups, BFQ is more able to properly sort
among multiple drives, reducing the chance of a starved process.  This
plus writeback throttling completely eliminate any outstanding bugs with
high writeback ratios, letting the user enjoy low latency writes
(application thinks they're already done), and super high throughput due
to batched writes in writeback.

Please note however, without the following configuration, I cannot
guarantee you will not get stalls:

CONFIG_BLK_CGROUP=y
CONFIG_CGROUP_WRITEBACK=y
CONFIG_IOSCHED_CFQ=y
CONFIG_CFQ_GROUP_IOSCHED=y
CONFIG_IOSCHED_BFQ=y
CONFIG_BFQ_GROUP_IOSCHED=y
CONFIG_DEFAULT_BFQ=y
CONFIG_SCSI_MQ_DEFAULT=n

Special thanks to h2, author of smxi and inxi, for providing evidence
that a configuration specific to Debian did not cause stalls found the
Liquorix kernels under heavy IO load.  This specific configuration
turned out to be hierarchical scheduling on CFQ (thus, BFQ as well).

4.10:
During some personal testing with the Dolphin emulator, MuQSS has
serious problems scaling its frequencies causing poor performance where
boosting the CPU frequencies would have fixed them.  Reducing the
up_threshold to 45 with MuQSS appears to fix the issue, letting the
introduction to "Star Wars: Rogue Leader" run at 100% speed versus about
80% on my test system.

Also, lets refactor the definitions and include some indentation to help
the reader discern what the scope of all the macros are.

4.11:
Increase MICRO_FREQUENCY_UP_THRESHOLD from 95 to 85
Increase MIN_FREQUENCY_UP_THRESHOLD from 11 to 6

These changes should help make using CFS feel a bit more responsive when
working with mostly idle workloads, browsing the web, scrolling through
text, etc.

Increasing the minimum frequency up threshold to 6% may be too
aggressive though.  Will revert this setting if it causes significant
battery drain.

4.12:
Make bfq the default MQ scheduler

Reduce default sampling down factor from 10 to 1

With the world eventually moving to a more laptop heavy configuration,
it's getting more important that we can reduce our frequencies quickly
after performing work.  This is normal with a ton of background
processes that need to perform burst work then sleep.

Since this doesn't really impact performance too much, lets not keep it
part of ZEN_INTERACTIVE.

Some time ago, the minimum frequency up threshold was set to 1 by
default, but the zen configuration was never updated to take advantage
of it.

Remove custom MIN_FREQUENCY_UP_THRESHOLD for MuQSS / ZEN_INTERACTIVE
configurations and make 1 the default for all choices.

Change-Id: I2a31fbc97fe12ffce30457ec2e83ed25764e2daf
Signed-off-by: Harsh Shandilya <msfjarvis@gmail.com>

---
## [SoSMaster9000/tgstation](https://github.com/SoSMaster9000/tgstation)@[a3e7c70f6d...](https://github.com/SoSMaster9000/tgstation/commit/a3e7c70f6da0fc7ea9929ddb39beddcf3113707f)
#### Sunday 2023-01-22 01:46:47 by necromanceranne

Bodypart code cleanup, robotic limbs can actually be disabled through damage again. (#71739)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Cleans up various variables and code comments in bodypart code so that
it is easier to understand (hopefully) what the fuck is happening there.

Fixes a hilarious oversight. For what may have been an entire 2 year
span, robotic limbs were unable to be disabled whatsoever. Good stuff.

## Why It's Good For The Game

Lost all your limbs and now have only surplus prosthetics?
Congratulations! You're now more durable than even someone with proper
robotic limbs, as your arms do not contribute anything more than 10
damage (or 15 stamina) to your overall damage taken. Furthermore, taking
the maximum amount of damage is actually entirely meaningless to you.

Laugh as someone attempting to shoot your arms does almost no meaningful
damage once you hit the cap! It's all sunk cost! You can't have it blown
off anyway, because dismembering surplus limbs is gone!

Who knew getting into a horrible bluespace/goliath accident could have
such an impact on your combat prowess. Thanks Nanotrasen!

Anyway, these vars are ugly.

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
code: Makes a lot of the bodypart variables clearer as to what they do.
Includes more detailed code comments.
fix: Robotic limbs are no longer immune to being disabled through
reaching maximum damage.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[8e5251ea60...](https://github.com/Paxilmaniac/Skyrat-tg/commit/8e5251ea6090a67d0b16c6799f1071884f7c7188)
#### Sunday 2023-01-22 01:49:05 by SkyratBot

[MIRROR] Captain's Spare ID Safe Can Only Hold ID Cards [MDB IGNORE] (#18631)

* Captain's Spare ID Safe Can Only Hold ID Cards (#72584)

## About The Pull Request

I've personally seen this strategy play out the exact same way on more
than one occasion in an higher frequency lately (I've never played as
either side, just witnessed it)- and it always just seems to be an abuse
of a skewed in-game mechanic. So, this PR makes it so that you can only
put IDs into the spare ID safe. Nothing else.
## Why It's Good For The Game

I think this balance change is needed because it really sort of ruins
what I like about nuclear operatives, having to run around and stay
fluid for whatever the nuclear operatives could have, not "HAHA WE WILL
PUT IT IN OUR (NEARLY) IMPENETRABLE SAFE THAT THEY WILL NEED TO USE A C4
DIRECTLY ON AND JUST END UP PLAYING BLOONS TOWER DEFENSE SIX AS WE AWAIT
THOSE RED FUCKS TO ARRIVE". I miss when it would be fun to inject it
into a monkey who could crawl around vents, put it in a disposals loop
around the station to keep the nukies on a wild goose chase, or just
holding your ground in the brig and retreating if they batter you down.
It's just a very OP location in a very OP place with lots of warranted
OP armor for it's intended use case, which is not really being followed
by putting the all-important disk in the safe.

It's just very strong overall due to how protected-from-damage the spare
ID safe is, and I don't really like the fact that this is emerging as a
new "meta gameplay" (even used when there aren't any nuclear
operatives), it just sullies the different variety of ways you can
defend yourself against nuclear operatives when there appears to be
**the clear choice**. I don't like that concept where you can have a
strategy so good that you _shouldn't_ do it.

Also, it's an _ID Safe_. Not a disk safe.
## Changelog
:cl:
balance: Due to materials costing a lot more than ever, Nanotrasen's
Spare ID Safe Supplier have cut down on the space inside of the ID Safe,
meaning you can only cram in things as thin as an ID Card.
/:cl:

* Captain's Spare ID Safe Can Only Hold ID Cards

Co-authored-by: san7890 <the@san7890.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[99dbe5cac4...](https://github.com/git-for-windows/git/commit/99dbe5cac4999d88aafa7d1c02ec1228721e5158)
#### Sunday 2023-01-22 02:07:46 by Johannes Schindelin

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
## [MattKalafut/hackerrank-30-days-of-code-cs](https://github.com/MattKalafut/hackerrank-30-days-of-code-cs)@[a91a452c99...](https://github.com/MattKalafut/hackerrank-30-days-of-code-cs/commit/a91a452c99a4c172064b1cac72ef150e2ffd9373)
#### Sunday 2023-01-22 02:31:45 by Matt

Add Day 04 - Class vs Instance
Holy shit the HackerRank boilerplate code is wack as hell.

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[a57b142c1a...](https://github.com/OrionTheFox/Skyrat-tg/commit/a57b142c1a4949ded1dcde1157ccf789fb21aabd)
#### Sunday 2023-01-22 02:56:04 by SkyratBot

[MIRROR] Basic mobs don't become dense upon death [MDB IGNORE] (#18679)

* Basic mobs don't become dense upon death (#72554)

## About The Pull Request

In #72260 what was previously a var became a flag, which was a sensible
change, however this inverted the default behaviour.
In virtually all cases we want dead mobs to _stop_ being dense, this
added a requirement for the flag to be present for that to happen and
then didn't add the flag to any mobs.

Rather than add this to every mob I inverted the function of the flag.
My reasoning here is that _simple_ mobs seemingly never required this
behaviour, basic mobs are probably going to need it rarely if ever, and
including it in `basic_mob_flags` by default seems messy and easy to
leave off when setting other flags (plus #72524 implies to me we want to
avoid adding more default values).

Setting this manually on each mob seems kind of silly as a requirement
going forward and I can't think of a way we'd unit test for people
forgetting.

For the same reason I did the same thing with the
`STOP_ACTING_WHILE_DEAD` flag I added to the AI controller in a recent
PR, the flag should denote unusual behaviour not the default.

## Why It's Good For The Game

It looks really odd when you're constantly shuffling places with dead
mobs, they're not supposed to do that.
It's tedious to add `STOP_ACTING_WHILE_DEAD` to every AI controller when
that should be an obvious default assumption.

## Changelog

:cl:
fix: Dead basic mobs are no longer "dense" objects and can be stepped
on.
/:cl:

* Basic mobs don't become dense upon death

* Removes a flag we didn't need anymore.

* Forgot to remove this one

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[ed166ce6ea...](https://github.com/clintjedwards/gofer/commit/ed166ce6ea1dddbde810162a606010efec6be2e0)
#### Sunday 2023-01-22 03:02:21 by Clint J Edwards

feat: Pipelines are now versioned

In order to eventually have canary-able deployments in Gofer we must
first support versioned pipelines.

This allows us to:
* Have a good target in which to roll back and forward.
* Understand what we are gaining and losing on each change.
* Track each update as it happens.

This is not easy though as pipelines have parts which are easy to version
(namely the config) and parts which are much harder to version (how do
we handle the cutting over of triggers?).

Because of this nuance, we've had to redesign a lot of earlier
assumptions for how Gofer models worked. This was a major refactor and
since I was here I made a few other large sweeping changes.

* Full storage package refactor: The storage layer was hard to use,
brittle, and inflexible. I've refactored it, leaning a bit more on
sqlx and going back to basics. I tried to make the storage package
work in the past by keeping the domain models to a minimum. I've since
learned this does not work once things become reasonably complicated. One
of the main refactors to the storage package is the introduction of
dedicated storage models. This means that I have to write a bunch of
boilerplate code to switch from in-memory models to the storage ones,
but the looser coupling is worth it. More storage refactors coming
as I learn what works at large scale and what doesn't.
https://github.com/go-jet/jet looks interesting.

* Removal of Triggers as Pipeline configuration: I desparately wanted
to have pipeline configurations encompass everything a pipeline would
have to offer, so that it was easy to look at a config and know exactly
what was going on in a particular pipeline. Triggers were a pain in the
ass though. Triggers unfortunately occupy a very special place in Gofer's
archetecture. Without triggers nothing really gets done. And so allowing
the user to apply all the same functionality to triggers as they would
with any other deployment was short-sighted. Triggers don't make a lot
of sense as a canary deployment. Triggers aren't ephemeral, they are
either on or their off. No in-between.

Instead Triggers can now be added to your pipeline via the command line.
This way trigger subscriptions aren't held down by the paradigms of
configuration change.

* Pipelines are now versioned: Not only have we added versions to pipelines,
but they now have deployments and configurations and metadata and a lot
of smaller loosely coupled parts so that they aren't a huge data monolith.
This means a lot of breaking changes for outward (and inward for that matter)
apis.

* Just lots of general breakages everywhere: Pretty much a large percentage
of things just aren't the same anymore.

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[1f4c0542b8...](https://github.com/re621/dnpcache/commit/1f4c0542b8b1f65b7aa9bc0c6fee4d30d3f3530f)
#### Sunday 2023-01-22 03:28:53 by bitWolfy

Add 1017 artists to the DNP list.

Added: lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, einin, freaks, angellsview3, arwenscoots, royalzbed, hellfurred, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, peshky, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, 100101, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, tren, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, jdlaclede, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[179fdfb794...](https://github.com/kleinerm/Psychtoolbox-3/commit/179fdfb79462fe447f8162286f5e534294c09df9)
#### Sunday 2023-01-22 03:52:47 by Mario Kleiner

PsychOpenXR[Core]: Implement optional multi-threaded 2D presentation mode.

This for presentation in 2D (mono or stereo) presentation mode, where
one or two (supposedly) head-locked OpenXR quad_layers are used for monoscopic
or stereoscopic image presentation. Ie. no use of OpenXR projection_layers,
which always need permanent closed-loop head tracking to work. According to
spec, head-locked quad_layers should be head-locked, static wrt. to any head
movement. However, as it turns out, some runtimes, e.g., SteamVR on both Linux
and Windows, do not work well at all if an animation loop isn't constantly
running at full HMD framerate, even for quad_layers. Under SteamVR, these 2D
views jitter / vibrate / jerk around in an annoying and disorienting fashion
if the animation loop runs too slow, takes pauses and restarts etc., making
use of the HMD as a "strapped onto the head" mono monitor, or as a stereo
monitor for binocular presentation almost unbearable.

Behaviour on my machine darlene is as follows:

- Linux + Monado: Absolutely perfect! Static views as expected even for
  long pauses, IFI's, stopped script loops with no Screen('Flip').
  Monado is also the only system that respects the .displayTime target
  onset time specification as the spec requires.

  -> No need for extra action.

- Windows + OculusVR: Mostly works fine with static views, but in some
  cases one might get the "sandclock" warning, a black screen or a stuck
  script.

  -> Mostly no need for extra action, some timing hacks should do.

- Linux + SteamVR: Fine in 2D mode with quad_layers/views if SteamVR's
  async_reprojection is disabled in "Developer -> Debug commands" GUI
  dialog. Apparently the jittering/jerking is a async reprojection bug
  or deficiency as of SteamVR 1.24.7.

  Timestamps are broken without multi-threading enabled.

  3D projection_layers mode is still broken, unless multi-threading makes
  it more stable, but still somewhat jittery. Maybe the async_reprojection
  disable does not apply to projection_layers, just to quad_views?

  -> Needs multi-threading for less wrong timestamping/timing, or for
     reduced jitter/jerking in 3D tracked mode with projection_layers.

- Windows + SteamVR with output to Rift CV-1 via OculusVR runtime, ie.
  not using SteamVR's own VR compositor, but OculusVR: Gives static
  images as expected for stopped animation loops. But resuming a loop
  (or just having long IFI's which is the same as stop -> resume from
  the runtimes PoV) causes massive jerks and jumps in single-threaded
  mode. Test for multi-threaded modes on Windows is pending.

  -> SteamVR on all OS'es needs help to get to acceptable results.

So, multi-threading to the rescue: This commit allows to optionally
enable a separate background thread which tries to runs the VR presentation
cycle at having at maximum HMD refresh rate, e.g., 90 fps for a Rift, all
the time, this way avoiding the animation loop from ever stopping or even
throttling from the XR runtime and compositor perspective.

We allocate and assign a dedicated OpenGL context (the one that Screen()
creates for use with its flipperThread, but which would go unused as the
flipperThread has no use for OpenXR sessions).

Startup of a session is always single-threaded on the main thread, to
get initial flips and sync-up with the XR compositor, getting to session
state XR_SESSION_STATE_SYNCHRONIZED <-> VISIBLE <-> FOCUSED, and the
initial set of framebuffer textures attached. Shutdown of a session with
final present is also done single-threaded on the main thread.

Full "head tracked 3D rendering" with a closed track -> do stuff -> render
-> present loop, and use of XR projection_layers is also done single-threaded,
as that only makes any practical sense with a tight renderloop implemented
in Matlab/Octave/[Python?] script.

The "2D" modes which use quad_layers and (usually) don't involve (or need)
head tracking and dynamic head pose driven fast closed loop rendering will
switch to multi-threading:

The thread runs in an infinite loop, doing xrWaitFrame -> xrBeginFrame ->
xrEndFrame cycles, resubmitting the same current most recently released
XR swapchain images each HMD video refresh cycle / compositor work cycle,
to keep away from client timeouts or throttling or stop->resume effects,
trying to kee the XR compositor happy.

The script, via Screen('Flip', win [, tWhen]) -> PsychOpenXRCore('PresentFrame')
will submit new rendered content as it wishes, with tWhen target present
time attached. In each work cycle, the thread checks predictedDisplayTime
for the upcoming xrEndFrame() call against tWhen. Iff
precictedDisplayTime >= tWhen, it is time to latch the new rendered stimuli,
by xrReleaseSwapchainImage() before the xrEndframe(), then acquiring new
swapchain images for the next user script render cycle.

predictedDisplayTime is used as best estimate of when the new stimulus
frame will show. An imperfect, and optimistic, guess, iow. returned
Screen('Flip') timestamps may be too optimistic, earlier than true
onset. However, as lots of testing showed, without a proper official
OpenXR timestamping extension, there isn't any way to do better than
that - It is what it is...

This now means we have two separate present code-paths for single (PresentExecute)
vs. multi threaded (PresentCycle) operation. And the need for locking and
condition variables for avoidance of race conditions, data corruption on
shared data, blowing up the OpenXR runtime, and separate OpenGL contexts
between main and XR thread, all with need for proper management and state
transitions. This is the rabbit hole of potential threading bugs in our code
and -- even more likely -- OpenXR runtime bugs, that i wanted to avoid going
down. But unfortunately not everything can be as well done as Monado, and
SteamVR is so far quite awful quality-wise as of January 2023, so here we
are...

-> For this commit, as of now, proper single-threaded vs. multi-threaded
   OpenGL context handling, mutex locking, signalling and dynamic transition
   in and out of multi-threaded mode has been verified by code self-review
   and testing on Octave/Matlab + NVidia gpu under Linux with Monado and
   SteamVR.

-> Depending on the hmd.multiThreaded setting 0, 1 or 2, multi-threading
   is never (0), always (2), or on-demand (1) used, with mode 1 switching
   single-/multi-threaded as needed for the situation. Generally if the
   user script used PsychVRHMD('Start', hmd); to signal it is running a
   fast tracking -> update -> present loop, then multi-threading is off.
   On PsychVRHMD('Stop', hmd), or in pure 2D quad-view mode, it is on.

-> Performance in multi-threaded mode is cut in half (max 45 fps on a
   90 Hz HMD). Could be room for improvements in handshaking between main
   and presenter thread, or could be unavoidable desync between client
   script on main thread, presenter thread, and compositor work cycle.
   Only further testing may tell...

-> This doesn't crash/hang/malfunction in any obvious ways on Linux with
   Monado or SteamVR + Monado SteamVR driver plugin for the Oculus Rift CV-1.
   Not yet tested on Windows or with other HMDs.

=> I'm sure it has remaining bugs, or room for improvements, but this serves
   as a good baseline. Hopefully it won't cause new trouble on Windows.

---
## [damian-666/MGShadersXPlatform](https://github.com/damian-666/MGShadersXPlatform)@[6b93e0a725...](https://github.com/damian-666/MGShadersXPlatform/commit/6b93e0a725244cc657c0fed143ab16c11ca32590)
#### Sunday 2023-01-22 04:43:57 by eagle1

do a bunch of tests ARRARGHH

its closer but not working.. its like the equality thing doensnt work.. .  i hacked for 2 hours .. this sucks..

i thinkl ill try compute branch OR... just leave it alone and move on to something else...don tso any shaders for a while

ill find a monnogame shader expertt just for thiso stuff and hire him.. theres toehr stuff.. this is crazy stupid diffiucltl.

---
## [cyyever/pytorch](https://github.com/cyyever/pytorch)@[5c6f5439b7...](https://github.com/cyyever/pytorch/commit/5c6f5439b7e6a5e63a68b36b4cf093a00d46e8be)
#### Sunday 2023-01-22 06:07:35 by Edward Z. Yang

Implement SymBool (#92149)

We have known for a while that we should in principle support SymBool as a separate concept from SymInt and SymFloat ( in particular, every distinct numeric type should get its own API). However, recent work with unbacked SymInts in, e.g., https://github.com/pytorch/pytorch/pull/90985 have made this a priority to implement. The essential problem is that our logic for computing the contiguity of tensors performs branches on the passed in input sizes, and this causes us to require guards when constructing tensors from unbacked SymInts. Morally, this should not be a big deal because, we only really care about the regular (non-channels-last) contiguity of the tensor, which should be guaranteed since most people aren't calling `empty_strided` on the tensor, however, because we store a bool (not a SymBool, prior to this PR it doesn't exist) on TensorImpl, we are forced to *immediately* compute these values, even if the value ends up not being used at all. In particular, even when a user allocates a contiguous tensor, we still must compute channels-last contiguity (as some contiguous tensors are also channels-last contiguous, but others are not.)

This PR implements SymBool, and makes TensorImpl use SymBool to store the contiguity information in ExtraMeta. There are a number of knock on effects, which I now discuss below.

* I introduce a new C++ type SymBool, analogous to SymInt and SymFloat. This type supports logical and, logical or and logical negation. I support the bitwise operations on this class (but not the conventional logic operators) to make it clear that logical operations on SymBool are NOT short-circuiting. I also, for now, do NOT support implicit conversion of SymBool to bool (creating a guard in this case). This does matter too much in practice, as in this PR I did not modify the equality operations (e.g., `==` on SymInt) to return SymBool, so all preexisting implicit guards did not need to be changed. I also introduced symbolic comparison functions `sym_eq`, etc. on SymInt to make it possible to create SymBool. The current implementation of comparison functions makes it unfortunately easy to accidentally introduce guards when you do not mean to (as both `s0 == s1` and `s0.sym_eq(s1)` are valid spellings of equality operation); in the short term, I intend to prevent excess guarding in this situation by unit testing; in the long term making the equality operators return SymBool is probably the correct fix.
* ~~I modify TensorImpl to store SymBool for the `is_contiguous` fields and friends on `ExtraMeta`. In practice, this essentially meant reverting most of the changes from https://github.com/pytorch/pytorch/pull/85936 . In particular, the fields on ExtraMeta are no longer strongly typed; at the time I was particularly concerned about the giant lambda I was using as the setter getting a desynchronized argument order, but now that I have individual setters for each field the only "big list" of boolean arguments is in the constructor of ExtraMeta, which seems like an acceptable risk. The semantics of TensorImpl are now that we guard only when you actually attempt to access the contiguity of the tensor via, e.g., `is_contiguous`. By in large, the contiguity calculation in the implementations now needs to be duplicated (as the boolean version can short circuit, but the SymBool version cannot); you should carefully review the duplicate new implementations. I typically use the `identity` template to disambiguate which version of the function I need, and rely on overloading to allow for implementation sharing. The changes to the `compute_` functions are particularly interesting; for most of the functions, I preserved their original non-symbolic implementation, and then introduce a new symbolic implementation that is branch-less (making use of our new SymBool operations). However, `compute_non_overlapping_and_dense` is special, see next bullet.~~ This appears to cause performance problems, so I am leaving this to an update PR.
* (Update: the Python side pieces for this are still in this PR, but they are not wired up until later PRs.) While the contiguity calculations are relatively easy to write in a branch-free way, `compute_non_overlapping_and_dense` is not: it involves a sort on the strides. While in principle we can still make it go through by using a data oblivious sorting network, this seems like too much complication for a field that is likely never used (because typically, it will be obvious that a tensor is non overlapping and dense, because the tensor is contiguous.) So we take a different approach: instead of trying to trace through the logic computation of non-overlapping and dense, we instead introduce a new opaque operator IsNonOverlappingAndDenseIndicator which represents all of the compute that would have been done here. This function returns an integer 0 if `is_non_overlapping_and_dense` would have returned `False`, and an integer 1 otherwise, for technical reasons (Sympy does not easily allow defining custom functions that return booleans). The function itself only knows how to evaluate itself if all of its arguments are integers; otherwise it is left unevaluated. This means we can always guard on it (as `size_hint` will always be able to evaluate through it), but otherwise its insides are left a black box. We typically do NOT expect this custom function to show up in actual boolean expressions, because we will typically shortcut it due to the tensor being contiguous. It's possible we should apply this treatment to all of the other `compute_` operations, more investigation necessary. As a technical note, because this operator takes a pair of a list of SymInts, we need to support converting `ArrayRef<SymNode>` to Python, and I also unpack the pair of lists into a single list because I don't know if Sympy operations can actually validly take lists of Sympy expressions as inputs. See for example `_make_node_sizes_strides`
* On the Python side, we also introduce a SymBool class, and update SymNode to track bool as a valid pytype. There is some subtlety here: bool is a subclass of int, so one has to be careful about `isinstance` checks (in fact, in most cases I replaced `isinstance(x, int)` with `type(x) is int` for expressly this reason.) Additionally, unlike, C++, I do NOT define bitwise inverse on SymBool, because it does not do the correct thing when run on booleans, e.g., `~True` is `-2`. (For that matter, they don't do the right thing in C++ either, but at least in principle the compiler can warn you about it with `-Wbool-operation`, and so the rule is simple in C++; only use logical operations if the types are statically known to be SymBool). Alas, logical negation is not overrideable, so we have to introduce `sym_not` which must be used in place of `not` whenever a SymBool can turn up. To avoid confusion with `__not__` which may imply that `operators.__not__` might be acceptable to use (it isn't), our magic method is called `__sym_not__`. The other bitwise operators `&` and `|` do the right thing with booleans and are acceptable to use.
* There is some annoyance working with booleans in Sympy. Unlike int and float, booleans live in their own algebra and they support less operations than regular numbers. In particular, `sympy.expand` does not work on them. To get around this, I introduce `safe_expand` which only calls expand on operations which are known to be expandable.

TODO: this PR appears to greatly regress performance of symbolic reasoning. In particular, `python test/functorch/test_aotdispatch.py -k max_pool2d` performs really poorly with these changes. Need to investigate.

Signed-off-by: Edward Z. Yang <ezyang@meta.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/92149
Approved by: https://github.com/albanD, https://github.com/Skylion007

---
## [yankovs/mquery](https://github.com/yankovs/mquery)@[e832f51fb3...](https://github.com/yankovs/mquery/commit/e832f51fb3e9475ef959d92e7c0944ecf1598451)
#### Sunday 2023-01-22 07:15:06 by msm-code

Use rq as a task scheduler for daemon. (#317)

Mquery demon is getting unmaintainable. Early daemon was a trivial piece of code, and using redis queues directly as a RPC mechanism was the easiest solution. Since then mquery got extended with (in
no particular order) batching, users, jobs, commands, task cancellations,
distributed agents, configuration, and more.

Case in point: subjectively (and I think my opinion matters in that regard) there are more bugs in 350 LoC daemon.py than in the whole rest of this repository combined.

We can keep digging that hole, or do something about this. I don't plan to rewrite the backend to another database, but at least we should use a better task queue than rolling ad-hoc our own one.

So this PR is a work in that direction. So far it looks very promising: hopefully we'll see big readability, stability and correctness improvements.

A few notes:

* This took longer than I expected, but was more fun than I expected. Rq is pretty neat and now I'm more sure of my code.
* Originally I wanted to do absolutely no changes to app.py, just db.py and daemon.py (to stop myself from doing more changes than necessary for my goal). In the end I couldn't stop myself from small refactoring - I've changed the JobId object to just string alias, and removed its uses from app.py. I've also changed a few parameter names. That's all. (Maybe I have a poor impulse control)
* I've added some comments to unrelated functions in the db. I've also documented data stored in the redis.
* A lot of the code is copy&pasted, but it's not clear from the git diff.

Overall I'm happy with this change and I think we can merge it.

Co-authored-by: Michał Praszmo <michalpr@cert.pl>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[979b26d52e...](https://github.com/jlsnow301/tgstation/commit/979b26d52e09dcaa7ad00ce07c1e16760dbd7cb2)
#### Sunday 2023-01-22 07:54:06 by tralezab

Unironically removes the atmos and black beret (#72722)

## About The Pull Request

Removes atmos berets

## Why It's Good For The Game
Berets shouldn't be thrown into every job, it's milsim circlejerking
dressup shit that creeps out of our milsim containment jobs (security)
and into other innocent jobs. There is absolutely no reason for this job
to have a beret just straight up. Can we add unique hats to the game,
not the same one recolored every way to Sunday? That's my problem. We
don't have unique clothes, we have a billion types of beret when the
BASE BERET TYPE has `IS_PLAYER_COLORABLE_1` so ANYONE can color it. So
again, why do we have the atmos beret? To clog the wardrobe, a vending
machine added specifically because we couldn't stop clogging the
original locker atmos techs spawned in?

The black beret has the same problem: recolored item when you can get
the item of any color

## Changelog
:cl:
del: Atmospherics beret and black beret
/:cl:

---
## [Irawans-Android-Lab/kernel_realme_sdm660](https://github.com/Irawans-Android-Lab/kernel_realme_sdm660)@[5577338469...](https://github.com/Irawans-Android-Lab/kernel_realme_sdm660/commit/55773384699f2b8a3e639885ca81116f9185e9dc)
#### Sunday 2023-01-22 07:58:50 by Maciej Żenczykowski

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
Signed-off-by: dodyirawan85 <40514988+dodyirawan85@users.noreply.github.com>

---
## [Spu7Nix/SPWN-language](https://github.com/Spu7Nix/SPWN-language)@[5a674fa2dc...](https://github.com/Spu7Nix/SPWN-language/commit/5a674fa2dcfc20bc9b8558f0b0146cc79d318136)
#### Sunday 2023-01-22 08:29:55 by Spu7Nix

"wow sput did it again??" "literally doing god's work" "how is he so cool???" "we do not deserve him!!"

---
## [FluffyBumblebees/Terrains](https://github.com/FluffyBumblebees/Terrains)@[64e4f6b01d...](https://github.com/FluffyBumblebees/Terrains/commit/64e4f6b01d892ab3fb0aed2a5040fad7d0913d02)
#### Sunday 2023-01-22 09:59:37 by Fluffy Bumblebee

my brain is fried. fuck u mojang and ur stupid data

---
## [benzvibez/smogs](https://github.com/benzvibez/smogs)@[c43c4fa86e...](https://github.com/benzvibez/smogs/commit/c43c4fa86e8a00411ae578927b0cb50c85d3defa)
#### Sunday 2023-01-22 11:32:45 by Aiden C. Desjarlais

V3.3.4B

added developer authorization, as this will now be uploaded to steam, and can be redeemed. This is an extra layer of security.

Cinematic mode completely re-written, in version 0.4.3pB, much better movement, will be used for the first trailer.

Added a developer mainmenu, this will be used on steam for global testing so if you decide to stream it or whatever, people know its a developer-closed version.

Fixed some in-game bugs

Mostly worked on re-building the Cinematic mode.

you can now use the Cinemizer.cs script to make any cameras cinematic, kudos to me for that.

Intergrated Steamworks.net for Steam API access

FINALLY fixed the stupid ass discord SDK, discord now works perfectly fine without shitting itself every 5 seconds.

Moved game version to 3.3.4Beta

---
## [Rishav-7/portfolioProjects](https://github.com/Rishav-7/portfolioProjects)@[2d5ef45fda...](https://github.com/Rishav-7/portfolioProjects/commit/2d5ef45fda5e719e6d6f312881f8d54d7231e266)
#### Sunday 2023-01-22 11:40:19 by Rishav-7

Add files via upload

In this project, we analysed the relationship between the different features of the heart failure patient included in this dataset namely the distribution of age among the patients, death rate, percentage of male and female patients, variation in the platelets amount, creatinine and sodium level in the blood. The graphical representation and visualisation of data using matplotlib and seaborn library in python helps us to easily understand a lot better about the dataset.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[a9d530dc71...](https://github.com/LemonInTheDark/tgstation/commit/a9d530dc712e913f7ada9f828f514b23b61de314)
#### Sunday 2023-01-22 12:11:06 by Time-Green

Unfuckies pod blood (#72323)

I broke it in #72220
Thanks to @Fikou for catching this
list(variable = 0.1) doesnt work on byond, so I last-minute improvised
and changed it to
list("[variable]" = 0.1), using a string instead of a typepath. I
already tested it thoroughly so decided it was probably good without
thinking of it anymore

:cl:
fix: fixes pod blood I swear
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Ning020510/Test](https://github.com/Ning020510/Test)@[e71d2810f3...](https://github.com/Ning020510/Test/commit/e71d2810f319724b97725ad044b25f6230dac63f)
#### Sunday 2023-01-22 13:28:17 by 海绵A梦

Merge pull request #1 from Ning020510/new

fuck you

---
## [petre-symfony/netgen-layouts-building-pages-with-Symfony-symfonycasts-ian-2023](https://github.com/petre-symfony/netgen-layouts-building-pages-with-Symfony-symfonycasts-ian-2023)@[17739f2893...](https://github.com/petre-symfony/netgen-layouts-building-pages-with-Symfony-symfonycasts-ian-2023/commit/17739f2893eb007de670de79d54cb0970486f7c7)
#### Sunday 2023-01-22 19:30:54 by petrero

27.3 Creating the Block Plugin
 - Let's get to work. In the src/Layouts/ directory, create a new PHP class called, how about, VerticalWhitespacePlugin. This needs to implement a PluginInterface. But in practice, we extend a Plugin class that implements that interface for us. Go to "Code"->"Generate", or Command+N on a Mac, and implement the one method we need: getExtendedHandlers()

 Ok, each block in the system - so every item over here on the left menu - has a class behind it called a block handler. Our job in getExtendedHandlers() is to return an iterable of all the "handlers" that we want to extend. For example, if you wanted to only extend the title block, you could yield TitleHandler::class. How did I know to use that class? Well, most of the time you can guess: the title block has a TitleHandler. But if you want to look deeper, you can see all the handlers in the system by running:

  php bin/console debug:container --tag=netgen_layouts.block_definition_handler
 Anyways, in our case, we want to override every block. So we can yield BlockHandlerDefinitionInterface::class, because every block handler must implement that interface

 And yes, I totally just forgot the word Definition. Whoops! I'll fix this bad interface in a minute.

 Adding a Custom Block Parameter/Field
 - To see what to do next, go back to the "Code"->"Generate" menu, select "Override methods" and choose buildParameters(). We don't need to call the parent method because it's empty

 Parameter is the word that Layouts uses for the form options that you can customize on the right side of the screen for every block. Thanks to our getExtendedHandlers() method, when Layouts builds those options for any block, it will now call this method and we can add new parameters.

 I'll paste in the first... and we also need a use statement for this ParameterType namespace

 Cool! As you can see, Layouts comes with a bunch of built-in "field types" - like BooleanField, which will render as a checkbox. It defaults to false and has a label. Oh, and this group? Remember how there are two tabs - "Design" and "Content"? This is where you determine which your parameter should live inside.

 And the first key - vertical_whitespace:enabled is the internal name of this field. You'll see how we use that in a minute.

 Before we try this, future Ryan has just informed me that... I messed up! Typical. Scroll up. I'm yielding the wrong class! Yield BlockDefinitionHandlerInterface::class

 That's better.

 Now let's try it. Refresh... click on any block... let me find my Title block... and... there it is! On any block we see the new field!

---
## [CorvaxStation/Skyrat-tg](https://github.com/CorvaxStation/Skyrat-tg)@[08291a6dbb...](https://github.com/CorvaxStation/Skyrat-tg/commit/08291a6dbb3249d9acbca4f539eb82900d299f26)
#### Sunday 2023-01-22 19:38:42 by SkyratBot

[MIRROR] Guards against uplink failsafe code being the same as unlock code [MDB IGNORE] (#18275)

* Guards against uplink failsafe code being the same as unlock code (#72113)

## About The Pull Request

There's probably a better way to do this to be honest, but I think it's
silly for both to potentially be the same and this should work alright.
## Why It's Good For The Game

Fixes #71446.

I don't think the Syndicate is that stupid.
## Changelog
:cl:
fix: After a recent mishap with a high-ranking Syndicate operative, the
uplink's unlock code and failsafe code (the one that makes it blow up if
you say it) should never turn out to be the same.
/:cl:

* Guards against uplink failsafe code being the same as unlock code

Co-authored-by: san7890 <the@san7890.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[af941eba3b...](https://github.com/treckstar/yolo-octo-hipster/commit/af941eba3b1ce99837de2c4acf0e02e7f578a138)
#### Sunday 2023-01-22 20:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Jellirby/HeavenStudio](https://github.com/Jellirby/HeavenStudio)@[54c4899f9d...](https://github.com/Jellirby/HeavenStudio/commit/54c4899f9d31999a946e006c6c9b8235bdc1c778)
#### Sunday 2023-01-22 21:12:19 by AstrlJelly

Double Date Initialization (#198)

* starting out with double date stuff :D

not even the background is finished
i just wanna get this on my fork so that it's safe

* double date getting more initialized

no animations, one block, nothing actually functions. but the boy is put in place, and the girl is almost put in place! just wanted to merge this with the main branch to play catchy tune

* initialization done!!!!!

gonna fix up the code, see what i can take out, see what i can standardize, see what i need to add. loving this so far, even with all of its annoyances

* ughhhh animation stuff.

this is gonna take me a day or two to even comprehend

Co-authored-by: minenice55 <star.elementa@gmail.com>

---
## [Silvio-Raini/entwicklerheld](https://github.com/Silvio-Raini/entwicklerheld)@[3afd548a43...](https://github.com/Silvio-Raini/entwicklerheld/commit/3afd548a43f71a0246034f354fb136e441c145e7)
#### Sunday 2023-01-22 21:14:54 by Silvio

Create christmas_tree_of_hanoi.cs

Santa Claus and his elves are not in the Christmas spirit this year. Fortunately, there is the elf Jordi, who helps Santa every year. He motivates his elf friends to decorate Santa Claus Base a lot this year. To do this, he wants to order more Christmas trees, but there are only a few fake Christmas trees left. These consist of several tree layers you can put together on top of each other. When the delivery arrives, he notices the resemblance to a mathematical puzzle: Tower of Hanoi. And so the elves and Santa Claus have fun decorating and puzzling. Are you joining in?

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[c3a1f21c1a...](https://github.com/MTandi/tgstation/commit/c3a1f21c1afc10bd5515114e0c6117ac73c87f62)
#### Sunday 2023-01-22 21:15:10 by MrMelbert

Converts blindness and nearsightedness to status effects, scratches some VERY dumb blindness handling that resulted in mobs becoming "incurably" blind (#72267)

## About The Pull Request

- Nearsighted is now a grouped status effect.
- Blindness is now a grouped status effect.
   - Eye handling of blindness has improved. 
- When eyes are removed, they now cause you to become blind, rather than
handling it in `update_tint`.
- Being ahealed no longer blinds you for one tick, meaning that black
overlay on aheal is gone.
- Temporary Blindness is now a status effect.
- Both Nearsightedness and Blindness have been exorcised from mob vars
and life chains. This means that we've finally cut 2 procs from life,
`handle_status_effect` and `handle_traits`, and moved both to event
based processing. Wooo optimizations.
- Swapped pacifism status effect to use apply and set helpers. 
- Removed an unused admin toggle that disabled welding helmet tint but
also tint from every clothing item and also blindness from losing your
eyes.
- Clothes now generally all blind their mob more consistently.
- Oculine, eye surgery, and sensory restoration are now no longer the
only way to fix blindness from eye damage. If your eyes are healed
through any other means, it will also heal your blindness.
- Some things that made you blind, such as ling blind sting, no longer
just flat made you blind from eye damage forever. They now cause eye
damage directly, which in turn makes you blind from eye damage, as
expected.
- Pacifists can't eyestab anymore. Eyestabs now have a limit on the
amount of blur applied.
- Refactored some `is_x_covered` procs to accept flags rather than have
a lot of arguments for some silly reason.
- Unit tests for blindness. 

## Why It's Good For The Game

Blindness was exceptionally poorly handled prior, primarily due to the
fact that it was tied to the mob instead of separated out

On top of that the system put a LOT of faith in proper handling of
blindness on the coder's end which was misplaced evidently. Many places
didn't update or handle blindness correctly, or just let people
perma-blind.

Deferring it to a status effect improves this a lot

## Changelog

:cl: Melbert
refactor: Refactored blindness and nearsightedness. Important to note is
that all mobs are naturally blind until their eyes are actually created.
refactor: Refactored "is covered" procs
fix: Less sources of blindness now cause permanent blindness. Includes
the "Blind" Spell and "Blind Sting" from changelings.
admin: Ahealing someone no longer flashes the blind overlay for 1 tick.
admin: I removed an unused (sort of) inaccessible admin verb that
allowed you to toggle the tint from all welding helmets (and clothing)
(and lack of eyes) in existence, let me know if you want similar back
balance: Changeling "Blind Sting" now causes eye damage (enough to
blind) rather than arbitrarily forcing blindness.
balance: Visionloss virus symptom now causes eye damage (enough to
blind) rather than arbitrarily forcing blindness.
balance: Oculine has been reworked slightly. Prior, Oculine arbitrarily
healed blindness and nearsightedness from eye damage reagrdless of how
damaged the eyes were, and applied blur on success. Now, Oculine just
heals eye damage, and blindness / nearsightedness is restored in the
process. There is now a probability every tick that eye blur is applied
based on how pure the oculine is while healing very damaged eyes.
balance: Pacifists can no longer eyestab.
balance: Any clothing item that covers your eyes contributes to getting
the bonus while sleeping, and to removing temporary blindness faster
/:cl:

---
## [DraagDunk/pokerole_irl](https://github.com/DraagDunk/pokerole_irl)@[ec87db4f3e...](https://github.com/DraagDunk/pokerole_irl/commit/ec87db4f3e0db32e3166294ca42ea76a1d4008c2)
#### Sunday 2023-01-22 21:19:03 by Jesper Dam

Merge pull request #22 from DraagDunk/fucking-hell-postgres

some transactions shit

---
## [mightydanp/Tech-Ascension](https://github.com/mightydanp/Tech-Ascension)@[4486977340...](https://github.com/mightydanp/Tech-Ascension/commit/4486977340a08007fe55e1367fe6e8ffb3f8e0c3)
#### Sunday 2023-01-22 21:30:57 by mightydanp

-reworked BlockStateData.
-deleted ItemModelData and BlockModelData to rework then combine them into one class called ModelData.java
-fixed a crash when creating new worlds.
-Fuck you @Bear989Sr

---
## [uhwot/orpheusdl-kkbox](https://github.com/uhwot/orpheusdl-kkbox)@[3ca2e50404...](https://github.com/uhwot/orpheusdl-kkbox/commit/3ca2e50404908f1ef588a03fd2f9d2a69a1056a9)
#### Sunday 2023-01-22 22:45:05 by uh wot

removed region bypass crap until i fix this shit

Hey guys, did you know that in terms of male human and female Pokémon breeding, Vaporeon is the most compatible Pokémon for humans? Not only are they in the field egg group, which is mostly comprised of mammals, Vaporeon are an average of 3”03’ tall and 63.9 pounds, this means they’re large enough to be able handle human dicks, and with their impressive Base Stats for HP and access to Acid Armor, you can be rough with one. Due to their mostly water based biology, there’s no doubt in my mind that an aroused Vaporeon would be incredibly wet, so wet that you could easily have sex with one for hours without getting sore. They can also learn the moves Attract, Baby-Doll Eyes, Captivate, Charm, and Tail Whip, along with not having fur to hide nipples, so it’d be incredibly easy for one to get you in the mood. With their abilities Water Absorb and Hydration, they can easily recover from fatigue with enough water. No other Pokémon comes close to this level of compatibility. Also, fun fact, if you pull out enough, you can make your Vaporeon turn white. Vaporeon is literally built for human dick. Ungodly defense stat+high HP pool+Acid Armor means it can take cock all day, all shapes and sizes and still come for more

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[29a99e8937...](https://github.com/TaleStation/TaleStation/commit/29a99e8937e515d9b94407d549941008d7fec3b3)
#### Sunday 2023-01-22 23:01:54 by TaleStationBot

[MIRROR] [MDB IGNORE] Magnitis is more aggressive, uses throw_at instead of Move at higher stages (#4207)

Original PR: https://github.com/tgstation/tgstation/pull/72739
-----
## About The Pull Request

I got this disease yesterday and was super disappointed by the actual
effects. Rather than suffer an unending waves of metal objects being
thrown at my head, I noticed that stuff on the bridge kept getting
disorganized, shrugged, and moved on.

Now, stages 3/4 of Magnitis will use throw_at instead of just moving
objects to the infectee. This can hurt or even kill the victim in
extreme cases. Remember to duck!

The messages about electrical shocks will now appear when a magnetic
pulse occurs. Some of the disease messages have been slightly altered to
fit this.

Also, while we're on the subject -- Is there a joke behind Magnitis'
agent "Fukkos Miracos"? Why does Magnitis make you ponder upon the
nature of miracles? Why did it make you feel like "clowning around"?
This stuff was written over a decade ago and I get the feeling it's
referencing something that is beyond me.
## Why It's Good For The Game

Gives an old disease a bit of a facelift. Makes it more _dynamic_ and
_engaging_.
## Changelog
:cl: Rhials
balance: The Magnitis disease will now hurl objects at infectees at
higher stages. Watch your head!
/:cl:

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d0732abf1f...](https://github.com/TaleStation/TaleStation/commit/d0732abf1fc8a36fea41661536c92164c8e960ec)
#### Sunday 2023-01-22 23:02:17 by TaleStationBot

[MIRROR] [MDB IGNORE] Water will now make you wet (#4208)

Original PR: https://github.com/tgstation/tgstation/pull/72844
-----
## About The Pull Request
Water, when exposed to a mob either via `TOUCH` or `VAPOR` application,
will now apply wet stacks to said mob according to the amount of water
used. For touch application, the ratio is 0.5 wet stack per unit of
water, whereas for vapor application (so for foam and sprays), that
ratio is lowered to 0.1 wet stack per unit of water. Yes, that would
mean that you could now put someone out by spraying enough water at them
with a spray bottle (usually around 50-150u), and I think that is quite
simply hilarious.

As a reminder, wet stacks decay slowly over time, however obviously
raising your fire stacks (so being exposed to something that's on fire,
for instance) will speed up that decay, once
https://github.com/tgstation/tgstation/pull/72843 is merged. I separated
them in two PRs because honestly the fact that being wet made you more
flammable just sounds like a fuckup of the year if I've ever heard one.

I also updated the unit test of water's `expose_mob()` proc, to check
that wet stacks were being applied properly, hopefully making sure that
there's no regression on that part in the future.

## Why It's Good For The Game
The number one thing you think of when you think of the word wet is
water. Water should make you wet, it only makes sense.

## Changelog

:cl: GoldenAlpharex
balance: Water now makes you wet on touch and vapor application, with
vapor being much less effective than touch. Yes, that means you can now
spend two minutes putting someone out with a spray bottle full of water!
/:cl:

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[4dac916458...](https://github.com/TaleStation/TaleStation/commit/4dac916458a5eb84d56f24091a9dddf3f9a54d41)
#### Sunday 2023-01-22 23:02:31 by TaleStationBot

[MIRROR] [MDB IGNORE] Being wet no longer causes you to be EXTRA flammable (#4209)

Original PR: https://github.com/tgstation/tgstation/pull/72843
-----
## About The Pull Request
Making it a separate PR because I think that's a very funny fuckup, who
knows, maybe one of the fuckups of the year, even.

Being wet no longer causes you to be even more flammable, and instead
properly lets you dry up instead of catching on fire even faster when
receiving fire stacks.

What caused this was that there was some double-negatives happening,
which meant that both fire and wet stacks would be increased together
when both were present at once, rather than both being reduced and one
of the two cancelling out the other.

## Why It's Good For The Game
Being wet shouldn't make you go up in flames faster. Now it will
actually protect you from flames according to your amount of wet stacks,
as intended.

## Changelog

:cl: GoldenAlpharex
fix: Being wet no longer causes you to be EXTRA flammable, and instead
properly protects you from catching on fire. If you're wet enough, of
course.
/:cl:

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [minj2/ux-study](https://github.com/minj2/ux-study)@[00eea3ca73...](https://github.com/minj2/ux-study/commit/00eea3ca73bf48b06eefc60c060a5a6ffc15e556)
#### Sunday 2023-01-22 23:46:13 by minj2

Update Defining-user-problems-MJLee.md

Have you ever considered how psychology influences your behavior and engagement with products in everyday life? 
I use hick's row day by day when I ask for the next day's lunch for my kid. I picked 2-3 choices and let her decide. When before, I asked all the options for the lunches that can be prepared, it took so long to decide and sometimes asked me what were the rest. I think the many options not only overwhelmed her but also harder to decide. After several try-outs, I picked 2-3 and she select 1 so quickly. We both happy with it.

---

