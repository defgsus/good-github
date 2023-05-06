## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-05](docs/good-messages/2023/2023-05-05.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,187,763 were push events containing 3,684,169 commit messages that amount to 264,943,776 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 50 messages:


## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[129c74c945...](https://github.com/Wallemations/heavenstation/commit/129c74c945a3fe0bce2c29065f69424ce8551670)
#### Friday 2023-05-05 00:00:14 by carlarctg

EMPs on robotic limbs will now disable them for 4-8 seconds rather than causing a 10-20 second full stun (#74570)

## About The Pull Request

EMPs on robotic limbs will now disable them for 10-20 seconds rather
than causing a 10-20 second full stun on the user. Additionally, they
will damage the limb for a little brute and some burn.

Arm EMPs don't do anything special as the limb being disabled already
drops items.

Leg EMPs cause a 10-20 second knockdown, only really applicable if
there's only one robotic leg as two disabled legs KD you anyways.

Chest EMPs cause a 3-6 second standing-up paralyze, visible to the
player by a quite noticeable shaking of their body.

Head EMPs break the optical transponder circuits for 7.5-15 seconds,
effectively giving the user nightmare goggles vision with green instead
of red as the only remaining color.

Tacit approval for the PR at least existing.

![image](https://user-images.githubusercontent.com/53100513/230537462-b06d0bb5-0607-4f83-954c-6b2a0bcdc635.png)
## Why It's Good For The Game

Robotic limbs are not so strong that a glancing EMP that may not even
have been directed at you should stun you for ten, TEN seconds, or
worse, twenty. This is basically legacy stunning from the days of
super-stuns on soap, stunbatons, etc. The code for it was last touched
six years ago.

**_The stats as shown above are not even close to final. I really don't
know or care what the right stats should be in the end. and I'm fine
with making them a 10-20 second timer again. I just put some
reasonable-seeming numbers in as a placeholder. EMPs could also still
cause a short stun if that is deemed necessary. Hell, that could be the
chest effect!_**
## Changelog
:cl:
balance: EMPs on robotic limbs will now disable them for 10-20 seconds
rather than causing a 10-20 second full stun on the user. Additionally,
they will damage the limb for a little brute and some burn.
EMPs on robotic limbs will now disable them for 10-20 seconds rather
than causing a 10-20 second full stun on the user. Additionally, they
will damage the limb for a little brute and some burn.
balance: Arm EMPs don't do anything special as the limb being disabled
already drops items.
balance: Leg EMPs cause a 10-20 second knockdown, only really applicable
if there's only one robotic leg as two disabled legs KD you anyways.
balance: Chest EMPs cause a 3-6 second standing-up paralyze, visible to
the player by a quite noticeable shaking of their body.
balance: Head EMPs break the optical transponder circuits for 7.5-15
seconds, effectively giving the user nightmare goggles vision with green
instead of red as the only remaining color.
/:cl:

---
## [kkpan11/iTerm2](https://github.com/kkpan11/iTerm2)@[ed5edcadad...](https://github.com/kkpan11/iTerm2/commit/ed5edcadad01f5feeb63ea66548c167ffa456221)
#### Friday 2023-05-05 00:25:58 by George Nachman

Fix an incorrect assumption that OSC 7 precedes the prompt, when in fact it comes after. Also fix a performance issue with PromptStateMachine - in Swift getting the length of a string is an O(N) operation, it seems. This caused performance problems when the state machine was confused (e.g., start in tcsh with shell integration then run zsh which sends OSC 7 and it gets stuck in the 'accruing' state). My dream is that some day I can enjoy the quality of life I had in Turbo Pascal where counting the length of a string could be done in constant time.

---
## [CursedBirb/tgstation](https://github.com/CursedBirb/tgstation)@[3861627c66...](https://github.com/CursedBirb/tgstation/commit/3861627c66747fb27b18f8bf76a3c9dfd2023001)
#### Friday 2023-05-05 00:41:17 by LemonInTheDark

Microing var/static times (~0.015 seconds of init) (#74769)

## About The Pull Request

Moth and I came up with an affront to god and man, and used it to track
the time spent creating /static (and in theory /global) variables (this
happens right at the start of init)
They cost as a sum about 0.05 seconds btw, at least currently.

```
/datum/timer
    var/key

/datum/timer/New(file, line)
    src.key = "[file]:[line]"

/datum/timer/proc/operator*(x)
    rustg_time_reset(key)
    return x

/datum/timer/proc/operator+(x)
    var/time = rustg_time_microseconds(key)
    world.log << "TIMER: [key]: [time]"
    return x

Regex:
var/static/([\w/]+) =
-> var/static/$1 = (new /datum/timer(__FILE__, __LINE__)) * (new /datum/timer(__FILE__, __LINE__)) + 
```

Output on moth's pc looks like this, time in microseconds

[output_sorted.csv](https://github.com/tgstation/tgstation/files/11241900/output_sorted.csv)

Most of this is either icon_states() memes (which appears to be cached
btw, that's interesting), or a variation on typecacheof()
There is one get_asset_datum call, but that is ALREADY cached and so is
just redundant. That's a good 0.01 seconds saved.

The rest of the time here is slightly more interesting.

The majority of typecacheof() is iterating the output of typesof(), a
byond internal proc that returns a list of types that either are or are
the child of the passed in type.
A decent chunk of time here (0.005 seconds, or 10% of the proc) can be
saved by unrolling the arguments to the proc.
It takes an arbitrary amount of typepaths as input, but we can't like
use arglist() here (cause this is an internal "proc"), so instead we try
a window of args, passing in null if we start to try and take in too
much.
Window size matters, zebra fits better into 4 then 5, especially because
of how grouping needs to work to make this effect happen.
We save about 0.001 for zebra btw, which is around about 7%. It's lower
cause we need to group the paths beforehand I think.

The speedup is minor, but it DOES exist. Plus it's fun.

## Why It's Good For The Game

Microing is a hell of a drug

---
## [ByronEncinas/git](https://github.com/ByronEncinas/git)@[7891e46585...](https://github.com/ByronEncinas/git/commit/7891e465856e539c4a102dadec6dca9ac51c38df)
#### Friday 2023-05-05 00:48:32 by Jeff King

gpg-interface: set trust level of missing key to "undefined"

In check_signature(), we initialize the trust_level field to "-1", with
the idea that if gpg does not return a trust level at all (if there is
no signature, or if the signature is made by an unknown key), we'll
use that value. But this has two problems:

  1. Since the field is an enum, it's up to the compiler to decide what
     underlying storage to use, and it only has to fit the values we've
     declared. So we may not be able to store "-1" at all. And indeed,
     on my system (linux with gcc), the resulting enum is an unsigned
     32-bit value, and -1 becomes 4294967295.

     The difference may seem academic (and you even get "-1" if you pass
     it to printf("%d")), but it means that code like this:

       status |= sigc->trust_level < configured_min_trust_level;

     does not necessarily behave as expected. This turns out not to be a
     bug in practice, though, because we keep the "-1" only when gpg did
     not report a signature from a known key, in which case the line
     above:

       status |= sigc->result != 'G';

     would always set status to non-zero anyway. So only a 'G' signature
     with no parsed trust level would cause a problem, which doesn't
     seem likely to trigger (outside of unexpected gpg behavior).

  2. When using the "%GT" format placeholder, we pass the value to
     gpg_trust_level_to_str(), which complains that the value is out of
     range with a BUG(). This behavior was introduced by 803978da49
     (gpg-interface: add function for converting trust level to string,
     2022-07-11). Before that, we just did a switch() on the enum, and
     anything that wasn't matched would end up as the empty string.

     Curiously, solving this by naively doing:

       if (level < 0)
               return "";

     in that function isn't sufficient. Because of (1) above, the
     compiler can (and does in my case) actually remove that conditional
     as dead code!

We can solve both by representing this state as an enum value. We could
do this by adding a new "unknown" value. But this really seems to match
the existing "undefined" level well. GPG describes this as "Not enough
information for calculation".

We have tests in t7510 that trigger this case (verifying a signature
from a key that we don't have, and then checking various %G
placeholders), but they didn't notice the BUG() because we didn't look
at %GT for that case! Let's make sure we check all %G placeholders for
each case in the formatting tests.

The interesting ones here are "show unknown signature with custom
format" and "show lack of signature with custom format", both of which
would BUG() before, and now turn %GT into "undefined". Prior to
803978da49 they would have turned it into the empty string, but I think
saying "undefined" consistently is a reasonable outcome, and probably
makes life easier for anyone parsing the output (and any such parser had
to be ready to see "undefined" already).

The other modified tests produce the same output before and after this
patch, but now we're consistently checking both %G? and %GT in all of
them.

Signed-off-by: Jeff King <peff@peff.net>
Reported-by: Rolf Eike Beer <eb@emlix.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[9cf8ae36ee...](https://github.com/git-for-windows/git/commit/9cf8ae36eef86d10c286a4681cd166fc7dd6c7ae)
#### Friday 2023-05-05 01:47:18 by Johannes Schindelin

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
## [knative-automation/eventing-natss](https://github.com/knative-automation/eventing-natss)@[107ce80078...](https://github.com/knative-automation/eventing-natss/commit/107ce80078cb57cd61fdfdfbdfcc20537d6ea447)
#### Friday 2023-05-05 02:09:33 by Knative Automation

upgrade to latest dependencies

bumping sigs.k8s.io/json 9f7c6b3...f223a00:%0A  > f223a00 Merge pull request # 16 from kevindelgado/strict-error-path-separation%0A  > ff3dbbe Merge pull request # 14 from liggitt/go118%0A  > b536e95 store err type and path separately in strict errors%0A  > 227cbc7 Merge pull request # 15 from liggitt/ci-refresh-go%0A  > 4017094 sync go1.18 changes from encoding/json%0A  > 93e9748 Check latest go version in CI%0Abumping github.com/google/go-cmp d103655...f144a35:%0A  > f144a35 Additional cleanup with Go 1.13 as minimal version (# 295)%0A  > 63c2960 remove xerrors (# 292)%0A  > 71220fc Use string formatting for slice of bytes (# 294)%0A  > 4664e24 Fix printing of types in reporter output (# 293)%0A  > 79433ac Run tests on Go 1.18 (# 290)%0A  > 039e37c Add //go:build lines (# 285)%0A  > 3242228 Drop hacks to work around Go reflection bugs in Go1.9 (# 282)%0A  > f59cd61 Update minimum supported version to go1.11 (# 281)%0A  > 6faefd0 Reduce minimum length for specialize string diffing (# 275)%0A  > f1773ad Use any alias instead of interface{} (# 276)%0A  > 9094ef9 Change build status badge (# 269)%0A  > 3ee52c8 Fix spelling mistakes (# 271)%0A  > 395a0ac Use sha256 in test (# 268)%0A  > 402949e Merge pull request # 266 from dsnet/fix-format%0A  > 290a6a2 Avoid shadowing variable (# 263)%0A  > d5fcb38 Fix textual printing of byte slices%0A  > 248ccff Fix staticcheck findings (# 262)%0Abumping knative.dev/reconciler-test 452cc1d...dc48d52:%0A  > dc48d52 upgrade to latest dependencies (# 515)%0A  > 937cf59 Knative Service forwarder for EventsHub (# 517)%0A  > 1d36262 Update community files (# 518)%0A  > 3c01fe1 Update community files (# 514)%0A  > 6c21623 upgrade to latest dependencies (# 511)%0A  > 8e242fe Update downstream test Go version and remove eventing-natss (# 513)%0A  > 9fbd79e upgrade to latest dependencies (# 510)%0A  > 06956b6 Update actions (# 509)%0A  > dc3cb16 Update actions (# 506)%0A  > 40da5d5 upgrade to latest dependencies (# 505)%0A  > b6650ee Update community files (# 508)%0A  > 4b8e2c0 Update community files (# 507)%0A  > 089a08c upgrade to latest dependencies (# 501)%0A  > 9e0512f Quote label and selector values (# 504)%0A  > e88bcc9 Quote label values for cronjob (# 503)%0A  > 19c9bb5 Support setting Job labels for cron jobs (# 502)%0A  > 805bcaa Update actions (# 500)%0A  > 7f6a81c Update actions (# 499)%0A  > 04a4c0a Update community files (# 498)%0A  > d52257e Support cronjobs (# 496)%0A  > 1e2f58e Allow using a prespecified namespace for running tests (# 495)%0A  > 3c3d659 Refactor service port defaulting (# 494)%0A  > 0979798 Give port name to service (# 493)%0A  > 9884929 upgrade to latest dependencies (# 492)%0A  > 9531216 Allow specifying parallel tests for parallelizable features (# 491)%0A  > 83f7512 upgrade to latest dependencies (# 489)%0A  > 9b63f84 upgrade to latest dependencies (# 484)%0A  > 9457183 Improve pod ready condition check (# 483)%0A  > 6ee7472 Add teardown.on.fail flag (# 485)%0A  > 19787c4 upgrade to latest dependencies (# 476)%0A  > d679661 Restart eventshub on failure (# 479)%0A  > e5eaf85 Allow verify service readiness when istio is installed (# 478)%0A  > e707ddf upgrade to latest dependencies (# 475)%0A  > 662cd0d Update community files (# 473)%0A  > e906aa6 Allow testing with istio enabled (# 466)%0A  > e459729 Update community files (# 472)%0A  > 93ff95f Fix deployment image setting (# 471)%0A  > f63559d Add file-based image resolver (# 465)%0A  > 68e5f61 Add namespace resource (# 464)%0A  > 2c512fb Add option to define selector on deployment (# 463)%0A  > 0b67889 Add deployment resource (# 462)%0A  > 3f90ffa upgrade to latest dependencies (# 461)%0A  > 8a0446e Add Pod resource (# 458)%0A  > 84bee7b upgrade to latest dependencies (# 460)%0A  > cb24694 upgrade to latest dependencies (# 456)%0A  > 471137e Switch to usage of pkg/resources/service (# 459)%0A  > 4012307 Add helpers to work with the service resource (# 457)%0A  > 4ed6333 Add helpers to create & interact with a Secret (# 455)%0A  > 5866b8f Update community files (# 454)%0A  > f75090a Update community files (# 453)%0A  > 91d5fb0 Add helpers to create & interact with a batchv1.Job (# 452)%0A  > e02964c Fix prober receiver install options (# 447)%0A  > 3fe8527 Keep polling when endpoint is not present (# 448)%0A  > 01a1499 Protect references collection with mutex for concurrent access (# 445)%0A  > a0cdf5b Handle already exists error in eventshub's RBAC install (# 441)%0A  > ed93f50 Handle not found resources while waiting as in WaitForResourceCondition (# 440)%0A  > a38bc32 Update community files (# 439)%0A  > 7c65452 Verify resource is addressable when sender is using GVR (# 436)%0A  > f8ce78c Fix prober concurrent access (# 432)%0A  > 966fbbe Adds ability for resources to override namespace in template config. (# 434)%0A  > f83270b upgrade to latest dependencies (# 433)%0A  > b070b17 Run steps with the same timing in parallel as documented (# 394)%0A  > 14f7512 Update actions (# 431)%0A  > 8d3f0cf Update community files (# 430)%0A  > 7f7a35e upgrade to latest dependencies (# 429)%0A  > cf080d0 upgrade to latest dependencies (# 428)%0A  > b9ed313 Update community files (# 427)%0A  > 62896bc Update community files (# 426)%0A  > 39a50c7 upgrade to latest dependencies (# 425)%0A  > 3efdfe8 upgrade to latest dependencies (# 424)%0A  > ccb154a Update community files (# 423)%0A  > 8ddc2b3 upgrade to latest dependencies (# 422)%0A  > 9283059 upgrade to latest dependencies (# 421)%0A  > dfab373 Update community files (# 420)%0A  > 5600f53 Define SecurityContext for test Pods (# 414)%0A  > 8554a16 upgrade to latest dependencies (# 417)%0A  > d20ef22 Use knative/actions downstream test (# 415)%0A  > cfd23f3 Format go code (# 418)%0A  > e863dbf Update community files (# 419)%0A  > 6b65d5c Update community files (# 416)%0A  > 5612970 upgrade to latest dependencies (# 409)%0A  > 07a0279 Fix data race on publish images (# 411)%0A  > 2391330 update cloudevent sdk to 2.12.0 (# 407)%0A  > 37c944e upgrade to latest dependencies (# 406)%0A  > 0a1020d Update actions (# 405)%0A  > 5c62f1c Update community files (# 404)%0A  > 5fad31c upgrade to latest dependencies (# 403)%0A  > 824de99 upgrade to latest dependencies (# 402)%0A  > debffa2 Update community files (# 401)%0Abumping golang.org/x/tools 897bd77...b3b5c13:%0A  > b3b5c13 internal/lsp/cache: invalidate packages with missing deps when files are%0A  > 39a4e36 internal/lsp/regtest: only run /default tests with -short%0A  > f157068 internal/lsp/regtest: allow sharing memoized results across regtests%0A  > 8ccb25c internal/lsp: treat struct tags as string type%0A  > 6c8a6c4 internal/lsp: suppress parameter hint when argument matches parameter%0A  > c83f42d internal/lsp: update inlay hints documentation to include go snippets%0A  > 8b47d4e all: update dependencies%0A  > 7600454 gopls: update dependencies%0A  > 2a6393f internal/lsp: Refactor to share logic with rename%0A  > 4375b29 cmd/auth/cookieauth: delete unreachable os.Exit%0A  > 005c07a gopls/internal/vulncheck: adjust logging%0A  > 04bd087 internal/lsp: enable fillstruct for generics%0A  > 6ec939a internal/span: fix incorrect bounds check in ToOffset%0A  > 178fdf9 gopls/internal/regtest: unskip Test_Issue38211%0A  > 1cfe623 gopls/internal/regtest: unskip TestQuickFixEmptyFiles%0A  > 3d474c8 internal/lsp/diff: new diff implementation to replace go-diff%0A  > a2a2477 gopls/internal/regtest: externalize shouldLoad tracking%0A  > 7b605f4 gopls/internal/vulncheck: pass go version to vulncheck config%0A  > 126ef8f gopls/internal/govulncheck: sync x/vuln@b9a3ad9%0A  > a732e45 gopls: update golang.org/x/vuln%0A  > 980cbfe A+C: delete AUTHORS and CONTRIBUTORS%0A  > ec1f924 internal/lsp: add check for nil results to fillreturns%0A  > 79f3242 godoc: support go1.19 doc comment syntax%0A  > 2957e9d go/callgraph/vta: use types.IsInterface instead of our own isInterface%0A  > 2eaea86 go/callgraph/vta: do not include interface types during propagation%0A  > dc45e74 internal/lsp: Update FilterDisallow to support matching directories at arbitrary depth.%0A  > ce6ce76 internal/lsp/regtest: increase the time allowed for shutdown%0A  > 32129bf go/internal/gcimporter: adjust importer to match compiler importer%0A  > 22d1494 internal/gcimporter: add support for reading unified IR export data%0A  > c3af7c2 internal/lsp/cache: delete workspacePackageHandles (dead code)%0A  > 1a4e02f internal/lsp/analysis/unusedvariable: add analyzer%0A  > db8f89b internal/memoize: rename Handle to Promise%0A  > a7c53b5 internal/analysisinternal: move FindBestMatch to internal/lsp/fuzzy%0A  > 9b6c018 internal/lsp/cache: don't trim unexported struct fields%0A  > 85173cc internal/lsp/cache: follow usual structure for packages, analysis maps%0A  > b2eae76 internal/lsp/cache: simplify modwhy cache%0A  > dcb576d internal/lsp/cache: simplify modtidy%0A  > b230791 internal/lsp/cache: move PosTo{Decl,Field} out of cache%0A  > 8730184 internal/lsp/fake: retry spurious file lock errors on windows%0A  > 459e2b8 internal/lsp/progress: actually close over Context in WorkDoneWriter%0A  > 7c06b01 go/callgraph/vta: remove interprocedural flows for receiver objects%0A  > 6e6f313 internal/lsp/regtest: simplify, consolidate, and document settings%0A  > 3db2cdc internal/lsp: wait for ongoing work to complete during server shutdown%0A  > a5adb0f internal/lsp/cache: use mod=readonly for process env funcs%0A  > a79ee0f Revert "Revert "internal/lsp/cache: don't pin a snapshot to view.importsState"%0A  > bc957ec internal/lsp/source: use token.File-agnostic positions to dedupe refs%0A  > b6e4951 Revert "internal/lsp/cache: don't pin a snapshot to view.importsState"%0A  > 71dc5e2 internal/lsp/cache: make snapshot reference counting uniform%0A  > 42457a5 internal/lsp/cache: don't pin a snapshot to view.importsState%0A  > d6c099e internal/memoize: document stateIdle, RefCounted%0A  > 53ead67 internal/memoize: delete Generation and Bind%0A  > 8746177 internal/lsp/cache: simplify ParseGo%0A  > 9c2a556 internal/lsp/cache: fail addPackageHandle if metadata is stale%0A  > 1dfab61 internal/lsp/cache: use GetHandle not Bind for 5 URI-keyed maps%0A  > 2aef121 internal/lsp: consolidate .go/go.mod link logic%0A  > 8184d1f internal/lsp/cache: use GetHandle not Bind in astCacheData%0A  > 36430f4 internal/lsp/cache: use GetHandle not Bind for actions%0A  > b929f3b internal/span: make NewRange accept File, not FileSet%0A  > d69bac6 internal/lsp/cache: cache isActiveLocked calculation across snapshots%0A  > afa4a95 internal/lsp/cache: persist known subdirs%0A  > 698251a internal/lsp/cache: sort Metadata.Deps, for determinism%0A  > f79f3aa internal/lsp/cache: clarify buildPackageHandle%0A  > e92a18f internal/lsp/lsppos: reduce allocations in NewMapper%0A  > f487f36 internal/lsp/source: reduce allocation in workspace-symbols%0A  > 7b04e8b internal/persistent: no-op deletion from map does not allocate%0A  > f042799 internal/memoize: delete Bind(cleanup) hook%0A  > bec0cf1 internal/lsp/cache: avoid Handle mechanism for workspace dir%0A  > ffc70b9 lsp/completion: fix ranking of *types.PkgName candidates%0A  > 93bf1fc gopls: add range over channel postfix completion%0A  > 79fefdf internal/memoize: do not iterate all handles on generation destruction%0A  > fa4babc internal/lsp/cache: use persistent map for storing packages in the snapshot%0A  > 9358add internal/lsp/cache: remove unused function%0A  > c77473f gopls: upgrade staticcheck to v0.3.2%0A  > e8e5b37 internal/lsp/cache: don't construct a new metadata graph if no changes%0A  > 8314b7a go/analysis: add suggested fix for unkeyed composite literals%0A  > 8865782 internal/lsp: add text edits for unkeyed literals%0A  > 1a196f0 internal/lsp/cache: don't build symbol info for non-Go files%0A  > b84d509 gopls/doc: regenerate documentation%0A  > c10541a go/analysis/passes/fieldalignment: document "false sharing"%0A  > 7743d1d internal/lsp: respect range for inlay hints%0A  > 0248714 internal/lsp: add additional instrumentation around package loading%0A  > e5b3324 internal/lsp: add InlayHint regtests%0A  > 2a90056 go/gcexportdata: fix Find for Go modules%0A  > 7404bd2 all: gofmt some recent file changes%0A  > ec0831a refactor/satisfy: don't crash on type parameters%0A  > 66bbba3 internal/memoize: remove unused Store.generations map%0A  > 56116ec internal/memoize: don't destroy reference counted handles%0A  > 10494c7 cmd/digraph: fix typo%0A  > 93a03c2 internal/lsp/cache: invalidate reverse closure when loading packages%0A  > c36379b internal/lsp/cache: don't set new metadata if existing is valid%0A  > e1ec1f3 internal/imports: use a module resolver if GOWORK is set%0A  > 60ca636 internal/lsp: use camel case for inlay hint config fields%0A  > 2994e99 internal/persistent: change map to use set/get as method names%0A  > 22ab253 internal/lsp: rename viewport to range%0A  > 3f5f798 internal/lsp/cache: use persistent map for storing files in the snapshot%0A  > f60e9bc internal/lsp/cache: use persistent map for storing gofiles in the snapshot%0A  > 871637b internal/lsp: add settings for inlay hints and enable%0A  > a44cc76 cmd/stringer: use explicit NeedX values instead of deprecated LoadSyntax%0A  > 4e231cb internal/lsp/cache: don't prune unreachable metadata on clone%0A  > a2de635 internal/lsp/cache: honor the go.work for computing workspace packages%0A  > cbb8e8e internal/span: optimise URI.Filename to avoid allocation%0A  > 63d8015 internal/lsp/cache: minor simplifications to Symbols%0A  > 59bd4fa internal/lsp: find references to package%0A  > a1303c8 internal/lsp: remove tooltip from inlay hints%0A  > 641b30b internal/lsp: add inlay hints for inferred type params%0A  > 70ccf57 go/packages: fix loading single file when outside of GOPATH, module%0A  > 381ac87 internal/lsp/debug: reduce critical sections in trace%0A  > 1e14d99 internal/lsp: add inlay hints for composite literal types%0A  > e987015 internal/lsp/cache: symbolize in parallel%0A  > 88325aa internal/memoize: add trace region for Handle.run%0A  > c353b05 internal/lsp/cache: delete checkSnapshotLocked%0A  > 567c98b internal/lsp/cache: don't walk URIs to invalidate metadata%0A  > dffd645 internal/lsp/cache: only clone metadata if something changed%0A  > 4ba3d22 internal/lsp/cache: clone the metadata graph when clearing ShouldLoad%0A  > 39d3d49 internal/lsp/cache: use metadataGraph.Clone in snapshot.clone%0A  > 8a92078 internal/lsp/cache: build a new metadata graph on load%0A  > 9f38ef7 internal/lsp/cache: derive workspace packages from metadata%0A  > 041035c Revert "internal/lsp/cache: reduce critical sections"%0A  > d097bc9 gopls/internal/vulncheck: include nonaffecting vulnerability info%0A  > e8b9ff1 gopls/internal/govulncheck: sync x/vuln@4eb5ba4%0A  > 654a14b internal/lsp/cache: reduce critical sections%0A  > 27db7f4 gopls: update golang.org/x/vuln to latest @4eb5ba4%0A  > c993be6 go/analysis/internal/checker: log codeFact error, remove unused action.inputs%0A  > ed27611 internal/lsp/cache: cache known subdirs pattern%0A  > ebc084a internal/lsp: add inlay hints count to test summary%0A  > c15c045 internal/lsp: enable inlay hint tests%0A  > 0343989 internal/lsp: fix error message for inlay hints%0A  > a41fc98 internal/lsp/cache: use [256]byte Hash instead of hex digit string%0A  > c41ddce internal/lsp: include padding in inlay hint marker tests%0A  > 5e48d26 internal/lsp: add inlay hints for composite literal names%0A  > 83b0675 internal/lsp: add inlay hints for constant values%0A  > ecc1479 internal/lsp: add inlay hints for variable types%0A  > 65c0181 internal/lsp: support textDocument/inlayHint for parameter names%0A  > 9651276 internal/lsp/cache: optimize Snapshot.clone%0A  > 697795d internal/lsp/regtest: don't run the connection on the test context%0A  > ad756c7 internal/lsp: initial test set up for inlay hints%0A  > 1d19788 internal/lsp/cache: always compute IsIntermediateTestVariant%0A  > 4a8620f internal/lsp/cache: move metadata fields to a new metadataGraph type%0A  > a3d129c internal/lsp/cache: extract module load errors when go.work is used%0A  > 6bfd3a4 Revert "internal: temporarily disable tests so we can land CL 410955"%0A  > 5ca4cc8 internal: temporarily disable tests so we can land CL 410955%0A  > 63dfc2d internal/lsp/cache: two minor optimizations%0A  > 030812f internal: remove unneeded FileSets%0A  > 2417911 go/analysis/internal/checker: add -test flag for single/multi-checkers%0A  > 43cce67 go/analysis: document need for deterministic Fact encoding%0A  > af82757 cmd/callgraph: add test of -algo=vta%0A  > 76325da internal/lsp/progress: detach context for all progress notifications%0A  > b2fbc38 cmd/callgraph: add -algo=vta option%0A  > d68628a go/ast/astutil: clarify PathEnclosingInterval%0A  > 3dd056a internal/lsp/mod: fix broken assumptions about file base%0A  > 0cdf4b5 internal/lsp/source: eliminate ColumnMapper.PointSpan in favor of Pos%0A  > 9d7bf95 internal/lsp: factor out column mapper construction from content%0A  > 9e1d19b internal/span: eliminate TokenConverter%0A  > dae3f4b internal/lsp/diff: remove unused TokenConverter parameters%0A  > de3ef4a internal/lsp/source: remove workaround for newline terminated files%0A  > 6b760fc internal/lsp/source: remove ineffectual memoization in MappedRange%0A  > ea60815 internal/lsp: use the correct converter for mapped range offsets%0A  > 1ff52e2 gopls/internal/vulncheck: use internal/govulncheck%0A  > 2bb78cf internal/lsp: add missing bug reporting, and panic during marker tests%0A  > 0e859af go/analysis/analysistest: use listed mode instead of deprecated const%0A  > f385733 internal/gocommand: skip ill-formed env vars in cmdDebugStr%0A  > ccb1050 internal/lsp/cache: invalidate metadata when parsing issues resolve%0A  > 904e24e go/ssa: tweak Function.Name() for generic instantiations%0A  > 4dd2c74 internal/govulncheck: copy from x/vuln repo%0A  > b62b00f internal/lsp: add an option to get notified of bug reports%0A  > 960b4ce internal/typeparams: adds core type implementation%0A  > b55ed5e internal/lsp/regtest: only print RPC logs if asked%0A  > 44db4eb gopls/internal/regtests: add a test for bad go.work files%0A  > f97a804 go/analysis/passes/nilness: fixed slice not being considered as non-nil%0A  > 13bcb69 internal/lsp/analysis/stubmethods: recognize *ast.CallExpr%0A  > facb0d3 internal/span: eliminate Converter and FileConverter%0A  > 814e0d7 go/gcexportdata: don't assume that fmt names never change%0A  > 1e55371 go/ssa: fix *SelectorExpr within *IndexExpr handling%0A  > 29d48d6 go/callgraph/rta: adds tests for (instantiated) generics%0A  > ed968f6 internal/lsp/bug: add a package for bug reporting%0A  > 090b14e internal/lsp/regtest: make TestResolveImportCycle robust to error order%0A  > 820e093 go/types/objectpath: implement fast path for concrete methods%0A  > cfd9905 go/ssa: inline *ssa.selection methods%0A  > 304195c go/ssa: create *ssa.selection.%0A  > f918e87 gopls/internal/vulncheck: copy logic of govulncheck -html%0A  > a518b79 gopls/internal/vulncheck: synchronize cache access%0A  > ad497c6 internal/lsp/cmd: add -config option to gopls vulncheck%0A  > 62d837c go/analysis/passes/httpresponse: minor clarification%0A  > 6eb3de2 internal/lsp/analysis: fix a doc comment typo%0A  > 728485f gopls/internal/regtest: add a test for using staticcheck with generics%0A  > 1a5eed3 cmd/compilebench: use -p, handle packages with asm files%0A  > 93852cb internal/lsp: fix source.CompareDiagnostic asymmetry%0A  > 8ec40b5 x/tools/go/ssa: instantiate sel.Recv() on MethodVal.%0A  > 28c754d internal/lsp/analysis: analyzer for //go:embed directive%0A  > 033cbfc internal/typeparams: run go generate with go1.18.2%0A  > bc0e26e internal/typeparams: remove examples in favor of x/exp/typeparams%0A  > b87ceec go/analysis/passes/httpresponse: inspect enclosing context of resp, err%0A  > 313af96 go/ast/astutil: make Apply follow TypeParams fields%0A  > d303668 internal/lsp/cache: use cached parsed files for symbols, if available%0A  > 0fb1abf internal/lsp: factor out go/token wrapper into a safetoken package%0A  > cde25b3 internal/lsp/lsppos: add helpers for mapping token positions%0A  > 22b7096 internal/lsp/cmd: change vulncheck to directly call the hook%0A  > 72a884b gopls: update golang.org/x/vuln dependency%0A  > d7e01c0 internal/lsp/source/completion: use typeutil.Map for short-circuiting%0A  > d299b94 passes/copylock: suppress reports on Offsetof and Alignof%0A  > 30fbd19 internal/lsp: fix fillstruct for structs with unsafe.Pointer%0A  > 0ebacc1 internal: remove pre-go1.12 conditionally compiled files%0A  > 45c8a71 internal/tool: implement structured help command%0A  > d27d783 cmd/godoc: expand skips in TestWeb%0A  > 4911e4a internal/testenv: remove darwin/arm case from NeedsGoBuild%0A  > 54c7ba5 go/analysis/passes/asmdecl: add build tag for loong64%0A  > b4c4500 README: restructure and update%0A  > 556c550 internal/lsp/cache: invalidate packages that have added files%0A  > 4a3fc21 internal/lsp: only linkify urls with http, https, and ftp schemes%0A  > 04fc2ba cmd/godoc: skip TestWeb if waitForServerReady fails%0A  > 6872d3b passes/unusedwrites: Add TODO for how to handle generics.%0A  > 7c895e0 pointer: Adds unit tests for pointer with type parameters.%0A  > ddadc42 guru: Add a TODO list to the guru cmd.%0A  > c39ac6a callgraph/vta: Removes dead return statement (misc cleanup).%0A  > aafffac internal/lsp/source: avoid panic in HoverIdentifier%0A  > c862641 cmd/digraph: only print non-trivial sccs%0A  > 6fff1af go/analysis/passes/errorsas: update testdata for new warning%0A  > 115b454 go/analysis/passes/errorsas: warn if errors.As target is *error%0A  > 60b4456 go/callgraph/static: adds tests for (instantiated) generics%0A  > a37ba14 go/callgraph/cha: adds tests for (instantiated) generics%0A  > dcaea06 go/callgraph/vta: adds tests for (instantiated) generics%0A  > b44fad8 lsp/completion: fix func literals with type params%0A  > 5bb9a5e lsp/completion: fix literal completions with type params%0A  > 0941294 lsp/completion: further improve generic func arg ranking%0A  > c903563 internal/lsp/cache: don't cache parsed files when checking for metadata%0A  > 825b661 nilness: add unit test for generic instantiation.%0A  > 2548a8b ssautil: Add unit tests that set ssa.InstantiateGenerics%0A  > ae12e8f ssa: switch lblocks to types.Object%0A  > 559469a internal/lsp: render package documentation when hovering over a package import%0A  > fa7afc9 lsp/completion: improve generic func arg ranking%0A  > d567bc1 go/ssa: monomorphize generic instantiations.%0A  > 5d7ca8a go/ssa: return nil on parameterized types on MethodValue.%0A  > 48a2cc8 x/tools: remove dependency on golang.org/x/xerrors%0A  > 235b13d cmd/godoc: remove usage of golang.org/x/xerrors%0A  > b22f048 internal/jsonrpc2*: remove usage of golang.org/x/xerrors%0A  > bcfc38f go/packages: remove usage of golang.org/x/xerrors%0A  > 37590b3 gopls: remove usage of golang.org/x/xerrors%0A  > e854e02 go/ssa: fix miscompilation of <<= and >>= statements%0A  > c02adcc go/packages: ask for EmbedPatterns and EmbedFiles if needed%0A  > 5bb9c48 x/tools/go/packages: on Go 1.19+, explicitly ask for -json fields needed%0A  > 00aa68c go/ssa/interp: use *ssa.Global as key type for interpreter.globals%0A  > b4aba4b go/internal/gcimporter: key tparams by Package instead of pkgname%0A  > 46bc274 go/ssa: Update callee for wrapper function instantiation.%0A  > 884ffcd go/analysis: add support for loong64%0A  > afc6aad go/packages: make loadFromExportData ignore go.shape%0A  > b7d7574 internal/lsp/protocol: avoid replying with non-nil interface values in case of error%0A  > 1f10767 gopls/doc: update neovim examples for nvim 0.7%0A  > a220087 internal/lsp/protocol: ignore reply values with non-nil errors in jsonrpc2_v2 adapters%0A  > d5f48fc all: gofmt%0A  > d996daa go/ssa: gofmt%0A  > f9c13bb go/pointer: gofmt%0A  > ad8ef15 go/callgraph: gofmt%0A  > ce1e683 go/analysis: gofmt%0A  > 2bbdb7a gopls, internal/lsp: gofmt%0A  > 5fef6fd cmd: gofmt%0A  > 04fab9a go/callgraph/vta: avoids cycles for pathological recursive types%0A  > fbebf43 go/internal: gofmt%0A  > b900e88 go/ssa: emit Low expression before High in *ast.Slice%0A  > b2552ef internal/lsp: run go mod vendor exclusively to avoid file contention%0A  > 9e788ee internal/lsp/fake: consider mtime when polling for file changes%0A  > fe932b4 go/ssa: Instantiate calls to generic functions and methods.%0A  > ce5936c go/ssa: bound functions are now unique per instantiation.%0A  > 7dd9f20 go/ssa: Adds datastructures for function instantiation.%0A  > ee2bc8b go/ast/astutil: fix panic in DeleteNamedImport from line directive%0A  > 48e6d8d cmd/fiximports: skip TestFixImports on plan9-arm%0A  > 7f10777 gopls/internal/regtest/modfile: temporarily skip TestSumUpdateFixesDiagnostics%0A  > 7cc24c2 gopls: upgrade staticcheck to v0.3.0%0A  > 1f763df internal/lsp: add semantic tokens for arrows in declarations%0A  > b3e0236 go/ssa: Track created functions in the builder.%0A  > 6731659 go/ssa: adds position info to implicit field selection instructions%0A  > 74cea6e internal/imports: ignore some line directives%0A  > 37acb39 internal/lsp: run vulncheck in specified dir%0A  > 4077921 all: fix spelling%0A  > ff66cbe internal/lsp: remove unused parameters from moduleAtVersion%0A  > 7d125fe cmd/callgraph: expand windows/arm64 skip to the whole platform%0A  > 153e30b internal/lsp/lsprpc: only propagate explicit GOWORK when using remote%0A  > cda13e2 internal/lsp: fix incorrect line and start of semantic tokens%0A  > 41787c4 gopls: run go mod tidy -compat=1.16 to fix the 1.16 build%0A  > b9a4807 internal/gopathwalk: remove unnecessary call to os.Lstat%0A  > 8e193c2 go/ssa: removes conversion of index value in Index and IndexAddr to int%0A  > 9d8009b go/analysis: validate report if analyzer.Run is empty%0A  > 761e51f go/ssa/interp: Adds reflect.DeepEqual model for interp testing%0A  > e342718 gopls/internal/vulncheck: skip vuln entries without callstacks%0A  > b22bc85 gopls/doc: update stale documentation on generics%0A  > e693fb4 go/internal/gcimporter: fix IImportBundle error text%0A  > ed5a15c go/internal/gcimporter: replace assert with more helpful panic%0A  > f4515dd go/packages: fix load with NeedTypes but not NeedImports%0A  > 11930bd go/packages: fix handling of NeedExportFile in go list%0A  > e0095ae go/packages: fix precedence typo in needtypes calculation%0A  > e309672 go/packages: rename NeedExportsFile to NeedExportFile%0A  > 54af36e internal/lsp: handle invalid URL args in command params%0A  > 707beb0 internal/lsp/source: descend into fields and field lists in qualifyExpr%0A  > 1e5ae83 internal/lsp/command: remove unnecessary json struct tag%0A  > b7db7eb internal/lsp/cmd: add vulncheck command%0A  > c62a3b3 gopls/internal/vulncheck: limit the included callstack count%0A  > 78ff15e tools: fix some typos%0A  > f23240f gopls/go.mod: switch to golang.org/x/vuln/vulncheck%0A  > 4adaded internal/lsp/source: handle empty strings in directoryFilters%0A  > 2536df9 internal/lsp/source: include builtin name in hovered signature%0A  > cd31eaa internal/lsp/command: add RunVulncheckExp%0A  > 4737f45 internal/lsp/command: add VulncheckArgs/Result types%0A  > 84a0321 doc/generate.go: handle non-empty JSON tag correctly%0A  > 4460e9b gopls/internal/vulncheck: copy x/vuln/cmd/govulncheck/cache.go%0A  > 9fd677e gopls/internal/vulncheck: add cmd that runs govulncheck-like analysis%0A  > b169789 go/ssa: add position information for switch case conditions%0A  > 9814b1b gopls: update settings link to code lenses%0A  > 87a8611 x/tools/go/packages: add Embed support%0A  > 1428e83 lsp/completion: fix bogus generic func conversion%0A  > cbdab03 lsp/completion: fix bogus type param candidate%0A  > 3a6cbd6 lsp/completion: improve completion for func type params%0A  > c717623 go/analysis/passes/asmdecl: define register-ABI result registers for PPC64%0A  > 86b02b3 internal/lsp/cache: check for nil WorkFile.Go%0A  > 5ea13d0 internal/lsp/source: move doc links to the bottom of hover%0A  > 779dfa4 internal/lsp: invalidate package on go.mod change with go.work%0A  > c7b0e9a internal/lsp/template: fix processing of multi-line tokens%0A  > e998cd2 internal/lsp: remove unused code%0A  > 877ec07 internal/lsp/cache: remove unused code%0A  > 85d68bc internal/lsp: update LSP stubs, including provisional InlayHints%0A  > fb5dfde internal/imports: update stdlib index for 1.18%0A  > d67eab4 go/types/objectpath: break cycles through type parameters in find%0A  > 77aa08b internal/completion: default to regular completion for f.Fuzz without f.Add%0A  > 6799a7a internal/lsp/source: canonicalize objects in reference/rename requests%0A  > 54a569a internal/imports: use first quote when matching import path%0A  > 40370f8 go/internal/gcimporter: add a test case for issue 51219%0A  > 24806f2 go/analysis: add tests check for calling *F methods in fuzz func%0A  > dff7c5f go/internal/gcimporter: guard against infinite recursion with recursive%0A  > 49d48a0 go/analysis/passes/composite: allow InternalFuzzTarget%0A  > 198cae3 go/ssa: split pkg() into different cases for *Package and *types.Package%0A  > ee31f70 internal/lsp: add completion for use directives%0A  > 622cf7b internal/lsp/cache: copy workFile when invalidating workspace%0A  > e7a12a3 go/ssa: add type substitution%0A  > c773560 internal/lsp/cache: set GOWORK=off when mutating modfiles%0A  > 613589d internal/lsp: more precise completions for *testing.F fuzz methods%0A  > 9f99e95 go/analysis: add analyzer for f.Add%0A  > 7b442e3 go/callgraph/vta: fix package doc%0A  > 1670aad go/analysis: fix bug with finding field type%0A  > fd72fd6 go/ssa/interp: adding external functions for tests%0A  > b105aac internal/lsp: use regexp to add go mod edit -go quick fix%0A  > 03d333a internal/lsp: add snippet completion for function type parameters%0A  > 94322c4 go/internal/gcimporter: pass -p to compiler in test%0A  > b59c441 internal/lsp/cache: always consider go.work files for ws expansion%0A  > e155b03 cmd/getgo: exec main from TestMain instead of running 'go build' in tests%0A  > e562276 internal/lsp: add hover for go.work use statements%0A  > 121d1e4 internal/lsp: report diagnostics on go.work files%0A  > 0eabed7 cmd/file2fuzz: exec main from TestMain instead of running 'go build' in tests%0A  > 19fe2d7 gopls: update xurls dependency, remove \b workaround%0A  > 3ce7728 internal/lsp/source: support stubbing concrete type params%0A  > 3286927 internal/lsp/cache: construct workspace even when go.work has error%0A  > 09e0201 go/ssa: determine whether a type is parameterized.%0A  > e43402d go/ssa: changes Package.values to objects.%0A  > a972457 go/ssa: adds *types.Info field to ssa.Function.%0A  > fc47946 go/ssa: Move BasicBlock operations into block.go%0A  > 7103138 gopls: add regtest for edit go directive quick fix%0A  > 4a5e7f0 internal/lsp: correctly apply file edits for edit go directive%0A  > 6a6eb59 go/ssa: Put type canonicalization on own mutex.%0A  > afc5fce gopls/doc: address additional comments on workspace.md%0A  > abbbcaf gopls/doc: update the documentation for workspaces to suggest go.work%0A  > 72442fe gopls: update neovim documentation for imitating goimports%0A  > ffa170d internal/jsonrpc2_v2: fix a racy map assignment in readIncoming%0A  > 625c871 gopls: update neovim documentation for using go.work%0A  > fb3622a signature-generator: add Go func signature fuzzing tools%0A  > 5d35a75 internal/jsonrpc2_v2: clarify documentation%0A  > abc106c gopls/integration/govim: build gopls using go1.18rc1%0A  > c2ddf3d internal/lsp: add quick fix for unsupported feature%0A  > 0e44f7a gopls/doc/advanced.md: correct commands for unstable version build%0A  > acdddf6 go/ssa: allows right operand of a shift to be signed.%0A  > 9ffa3ad internal/lsp: Provide completions for test function definitions%0A  > b7525f4 internal/lsp: hash go version into package key%0A  > 5210e0c gopls: wire in LangVersion and ModulePath for gofumpt formatting%0A  > e6ef770 go/types/typeutil: don't recurse into constraints when hashing tparams%0A  > 258e473 internal/lsp/source: disable the useany analyzer by default%0A  > b7d2949 internal/lsp: don't store diagnostics for builtin.go%0A  > 4f21f7a gopls: update gofumpt to v0.3.0%0A  > 3e31058 internal/imports: update to permit multiple main modules%0A  > 43f084e internal/typesinternal: update typesinternal for 1.18%0Abumping k8s.io/code-generator 65c70a5...6523e22:%0A  > 6523e22 Merge pull request # 112808 from cheftako/automated-cherry-pick-of-# 112689-upstream-release-1.25%0A  > 59f8301 Updated vendor to the new preferred versions.%0A  > 7e9837e Merge pull request # 112161 from pohly/automated-cherry-pick-of-# 112129-origin-release-1.25%0A  > ecb165b dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 775c304 Merge remote-tracking branch 'origin/master' into release-1.25%0A  > d31c93c Revert "Remove gcp and azure auth plugins"%0A  > 7a6b27b Update go.mod to go1.19%0A  > fa4467d Merge pull request # 111677 from dims/stop-panic-in-govet-levee%0A  > 7b3066b run lint-dependencies and follow directions%0A  > c04cb7f Stop panic in govet-levee CI job%0A  > aed7155 Merge pull request # 110495 from alexzielenski/atomic-objectreference%0A  > 02dff21 update kube-openapi%0A  > 24b65b5 Update kubectl kustomize to kyaml/v0.13.9, cmd/config/v0.10.9, api/v0.12.1, kustomize/v4.5.7 (# 111606)%0A  > ce96325 Merge pull request # 111557 from alexzielenski/update-smd-422%0A  > 3e298a9 update smd to 4.2.3%0A  > 98b8ad1 Merge pull request # 111587 from ialidzhikov/k8s-utils@ee6ede2d64ed%0A  > 7d41d4b Update `k8s.io/utils` to `ee6ede2d64ed`%0A  > f7e6982 Merge pull request # 111442 from ialidzhikov/k8s-utils@56c0de1e6f5e%0A  > 5e969f2 Update `k8s.io/utils` to `9bab9ef40391`%0A  > 22db44c Merge pull request # 111254 from dims/update-to-golang-1.19-rc2%0A  > 53c2ca0 Generate and format files%0A  > a08f67b Merge pull request # 110178 from kevindelgado/validation-beta-1-25%0A  > e22e97f update kjson%0A  > 40a88eb Merge pull request # 111008 from cici37/bumpCEL%0A  > 9a892d0 Bump cel-go to v0.12.0%0A  > d665e29 Merge pull request # 108792 from wongearl/modify-todo%0A  > dc61ef8 Merge pull request # 111001 from pohly/klog-update%0A  > dec659d fix CustomArgs annotation, todo describe%0A  > 162a509 build: update to klog v2.70.1%0A  > 132cd9f Merge pull request # 110831 from chendave/openapi%0A  > 0bd13bc Bump `kube-openapi` to the latest%0A  > 068d9f8 Merge pull request # 110724 from pohly/klog-update%0A  > 051a429 build: update to klog v2.70.0%0A  > 4e8f8f5 Merge pull request # 110378 from lucacome/bump-grpc%0A  > 39381c1 Bump grpc to v1.47.0%0A  > a2acbb4 Merge pull request # 110546 from liggitt/fix-example%0A  > cb496e7 Merge pull request # 110518 from dims/switch-to-released-version-of-v3.8.0-github.com/emicklei/go-restful/v3%0A  > e246394 Drop spurious replace%0A  > f2ea995 Merge pull request # 110520 from dims/update-gopkg.in/yaml.v3-to-v3.0.1%0A  > 306deab Switch to released version of v3.8.0 - github.com/emicklei/go-restful/v3%0A  > d8adc26 Update gopkg.in/yaml.v3 to v3.0.1%0A  > 35a5f00 Merge pull request # 110351 from dims/switch-to-v3-of-github.com/emicklei/go-restful%0A  > e1fbd90 Switch to v3 of github.com/emicklei/go-restful%0A  > 7d977b3 Merge pull request # 110013 from enj/enj/i/remove_azure_gcp_auth_plugins%0A  > 7e85903 Remove gcp and azure auth plugins%0A  > 9f887a7 Merge pull request # 109891 from pohly/log-dependency-update%0A  > acd6f5b Merge pull request # 109602 from lavalamp/remove-clustername%0A  > 7c0fe80 dependencies: logr and zapr v1.2.3%0A  > 05559de generated files%0A  > 8ed2cce Merge pull request # 109804 from cici37/celUpdate%0A  > f82eadd Update go-control-plane, cncf/xds/go, cncf/udpa/go and remove unused versions%0A  > cd6d91a Update GRPC%0A  > df8059b Update genproto and antlr.%0A  > 4a69c11 Bump cel-go to v0.11.2%0A  > 0a834f8 Merge pull request # 109440 from liggitt/gomod-1.18%0A  > 5cbad16 Regenerate vendor%0A  > 8f17de0 Merge pull request # 109031 from Jefftree/openapiv3beta%0A  > 858bf3c generated: Update kube-openapi and vendor%0Abumping k8s.io/utils 3a6ce19...8e77b1f:%0A  > 8e77b1f Merge pull request # 265 from danwinship/fix-dumb-api-mistake%0A  > 1a15be2 Merge pull request # 270 from dashpole/trace_panic%0A  > ba5a213 Fix an API accident with net.IPFamily%0A  > 61b03e2 Merge pull request # 268 from petr-muller/deprecation-convention%0A  > 71bfc7b make traces safe for concurrent use%0A  > cfd413d Merge pull request # 263 from saltbo/fix-invalid-gha-goverion%0A  > d90ac11 pointer: make deprecation comments follow convention%0A  > 460b63a demonstrate trace panic%0A  > 4270251 Merge pull request # 259 from LJTian/master%0A  > 4a5ee0b fix: update the go-versions format for the gha%0A  > 665eaae Merge pull request # 261 from liggitt/clean-deps%0A  > 1be0ed5 Update Go standard libs address to reduce jump time%0A  > 7796b5f Merge pull request # 260 from dims/bump-dependencies-and-go-language-version%0A  > 25648b1 Drop testify dependency%0A  > e9cbc92 Merge pull request # 242 from MushuEE/patch-3%0A  > c9660c8 Bump dependencies and go language version%0A  > 49b64f9 Drop afero dependency%0A  > ad59060 Merge pull request # 253 from kschoche/add_uint_to_pointer_pkg%0A  > d7bf925 Ineffective break statements triggering SA4011%0A  > 2e139fc Merge pull request # 254 from dims/bump-version-of-golang-to-1.19%0A  > d45ae35 add uint64 and uint to pointer pkg%0A  > ee6ede2 Merge pull request # 252 from ialidzhikov/cleanup/testdata%0A  > e3a7968 Bump version of golang to 1.19%0A  > 9bab9ef Merge pull request # 251 from dims/tolerate-path-lookup-issues-in-golang-1.19%0A  > a4934a1 Move test data file under testdata/%0A  > 56c0de1 Merge pull request # 249 from ialidzhikov/pointer-func-deprecations%0A  > ee5bcf5 tolerate path lookup issues in golang 1.19%0A  > f6158b4 Merge pull request # 248 from aojea/ci%0A  > 161a940 Properly deprecate the funcs from the pointer pkg%0A  > 74ebc72 IP.UnmarshalText() uses net.Parse internally%0A  > 105d5f1 fix linter%0A  > f2fee6f call to (*T).Fatalf from a non-test goroutine (govet)%0A  > 8cc7140 update github CI%0Abumping k8s.io/apiextensions-apiserver b993e22...2c55649:%0A  > 2c55649 Update dependencies to v0.25.4 tag%0A  > 67ebb5f Merge pull request # 112808 from cheftako/automated-cherry-pick-of-# 112689-upstream-release-1.25%0A  > 05d7571 Updated vendor to the new preferred versions.%0A  > 2d6e469 Bump konnectivity-client to v0.0.33%0A  > a290ab4 Merge pull request # 112161 from pohly/automated-cherry-pick-of-# 112129-origin-release-1.25%0A  > d8d88ce Merge pull request # 112107 from DangerOnTheRanger/automated-cherry-pick-of-# 111964-upstream-release-1.25%0A  > 34ce90c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 063c82b Add unit tests.%0A  > 6d0af3c Run pin-dependency.sh and update-vendor.sh.%0A  > 850356a Update go.mod to go1.19%0A  > 1994fc0 Merge pull request # 111677 from dims/stop-panic-in-govet-levee%0A  > e2f1a8a run lint-dependencies and follow directions%0A  > 79e4ee6 Stop panic in govet-levee CI job%0A  > a9d332a Merge pull request # 110495 from alexzielenski/atomic-objectreference%0A  > 0bec600 update kube-openapi%0A  > 914f1d7 Update kubectl kustomize to kyaml/v0.13.9, cmd/config/v0.10.9, api/v0.12.1, kustomize/v4.5.7 (# 111606)%0A  > d25d03c Merge pull request # 111557 from alexzielenski/update-smd-422%0A  > 8f03975 Merge pull request # 105126 from sallyom/tracing-kubelet%0A  > 11291a4 update smd to 4.2.3%0A  > a34b99b kubelet tracing: update vendor%0A  > 5fd535d kubelet tracing%0A  > c66b2d1 Merge pull request # 111587 from ialidzhikov/k8s-utils@ee6ede2d64ed%0A  > 58b8011 Update `k8s.io/utils` to `ee6ede2d64ed`%0A  > 49cedce Merge pull request # 111446 from alexzielenski/trivial-x-preserve-unknown-fields-correction%0A  > 5f4930e Merge pull request # 111519 from jpbetz/skip-cel-validation%0A  > 3889972 correct OpenAPI extension in error message%0A  > 85460a1 Merge pull request # 111483 from jpbetz/fix-missing-root-object-type%0A  > 6158148 Skip CEL expression validation if OpenAPIv3 schema is invalid%0A  > de80fce Skip schemas that are non-structural in NewValidator%0A  > 7846e04 Merge pull request # 111451 from DangerOnTheRanger/cel-use-case-tests%0A  > 5ac5089 Merge pull request # 111442 from ialidzhikov/k8s-utils@56c0de1e6f5e%0A  > 560e664 Add examples of matchExpressions validations.%0A  > b317854 Update `k8s.io/utils` to `9bab9ef40391`%0A  > 5f2cc68 Merge pull request # 111254 from dims/update-to-golang-1.19-rc2%0A  > d8abaab Generate and format files%0A  > 02604ce Merge pull request # 108108 from thaJeztah/switch_golang_protobuf_extensions%0A  > fec6a8f downgrade github.com/matttproud/golang_protobuf_extensions to v1.0.1%0A  > a6bd8bf Merge pull request # 111156 from DangerOnTheRanger/cel-traversal-optimization%0A  > b655fba Replace estimateMinSizeJSON with DeclType.MinSerializedSize.%0A  > 758d6d5 Merge pull request # 110135 from jpbetz/efficient-crd-cel-validation%0A  > dbdebf1 Reuse structural schema and cel decls during CRD validation%0A  > 0bdac0d Merge pull request # 111071 from cici37/updateCEL%0A  > d0f6952 Merge pull request # 111242 from wojtek-t/fix_leaking_goroutines_11%0A  > d562a8a Sort out dep order%0A  > 7c89666 Merge pull request # 110178 from kevindelgado/validation-beta-1-25%0A  > 60ed3b4 Clean shutdown of apiserver integration tests%0A  > b19f020 Switch to use cel.TypeToExprType(celType) to generate the exprType.%0A  > 684f2a7 Merge pull request # 109639 from Abirdcfly/fixduplicateimport%0A  > fce3486 update kjson%0A  > 224fabd Turn on DefaultUTCTimeZone for cel-go.%0A  > 1c3183a Merge pull request # 111035 from jiahuif-forks/feature/matrics/cel%0A  > 896ce20 cleanup: remove duplicate import%0A  > e60fcc5 Add server-side metadata unknown field validation%0A  > adca902 Enable the empty list sum support.%0A  > 9bd3fbc Merge pull request # 111008 from cici37/bumpCEL%0A  > 40ff5d6 metrics for CEL compilation and evaluation.%0A  > ea6670e Pick up dispatcher refactor changes from cel-go%0A  > 62e4d5d Adding comment for maxValidDepth check.%0A  > 33c72d2 Bump cel-go to v0.12.4%0A  > 9f63533 Bump cel-go to v0.12.3%0A  > ce744a8 Add test for CEL maxRecurionDepth check.%0A  > 8b5da6a Bump cel-go to v0.12.1%0A  > 0735877 Bump cel-go to v0.12.0%0A  > 8789ab0 Merge pull request # 109111 from chendave/ginkgo_upstream%0A  > 3203d57 update ginkgo from v1 to v2 and gomega to 1.19.0%0A  > f3e37dc Merge pull request # 111001 from pohly/klog-update%0A  > 8a94cf1 build: update to klog v2.70.1%0A  > a394eda Merge pull request # 110831 from chendave/openapi%0A  > 020df44 Merge pull request # 110548 from benluddy/cel-unstructuredtoval-benchmark-fixture%0A  > 7a0dda7 Bump `kube-openapi` to the latest%0A  > 92942df Merge pull request # 110549 from benluddy/skip-unused-oldself-activation-work%0A  > ff05b62 Do test fixture setup outside cel.UnstructuredToVal benchmark loop.%0A  > 25b2ab4 Merge pull request # 110788 from 21kyu/change_reflect_ptr%0A  > a5932b2 Only provide an oldSelf binding when referenced by a CEL rule.%0A  > 17752d1 Change reflect.Ptr to reflect.Pointer%0A  > 442c886 Merge pull request # 109510 from sugangli/pinhole-fw%0A  > 3583982 Merge pull request # 110731 from jkh52/update-netproxy%0A  > 3c6fc8b update kube-controller-manager dependencies%0A  > 3963fc7 Bump konnectivity-client to 0.0.32%0A  > addd726 Merge pull request # 110724 from pohly/klog-update%0A  > 387f93d build: update to klog v2.70.0%0A  > 27cab03 Merge pull request # 110378 from lucacome/bump-grpc%0A  > 356b8d7 Merge pull request # 110519 from dims/update-etcd-packages-to-v3.5.4%0A  > c1fc8de Bump grpc to v1.47.0%0A  > c1ee610 Merge pull request # 110179 from Jefftree/fix_openapi_v2%0A  > e5b7b82 update etcd packages to v3.5.4%0A  > d877aaa Merge pull request # 110518 from dims/switch-to-released-version-of-v3.8.0-github.com/emicklei/go-restful/v3%0A  > 87c2a6e Prune defaults for CRD serving%0A  > e16b199 Merge pull request # 110520 from dims/update-gopkg.in/yaml.v3-to-v3.0.1%0A  > 8aaaf68 Switch to released version of v3.8.0 - github.com/emicklei/go-restful/v3%0A  > 546aafe Update gopkg.in/yaml.v3 to v3.0.1%0A  > bd811e0 Merge pull request # 110351 from dims/switch-to-v3-of-github.com/emicklei/go-restful%0A  > 83fedf3 Switch to v3 of github.com/emicklei/go-restful%0A  > 0b237d1 Merge pull request # 109552 from cyclinder/fix_CVE-2022-27191%0A  > 6af94f0 Merge pull request # 109228 from pacoxu/cleanup-ut%0A  > a8129d5 ix CVE-2022-27191: Bump golang.org/x/crypto to v0.0.0-20220315160706%0A  > 916bb0f Merge pull request # 110131 from stevekuznetsov/skuznets/stop-copying-metadata%0A  > 37a5c7c prevent the unit test name too long in report%0A  > 6ca81eb Merge pull request # 110130 from stevekuznetsov/skuznets/clean-up-crd-storage%0A  > dd95027 customresource: stop shallow-copying metadata%0A  > 774eebb Merge pull request # 109835 from cici37/celUpdate%0A  > 9215e7c customresouce: clean up the storage constructor%0A  > a47945a Merge pull request # 110061 from wojtek-t/shutdown_apiextensions%0A  > 8174e5f Initialize a base CEL env and share it to avoid repeated function declaration validation%0A  > eb1841e Merge pull request # 109880 from Jefftree/patch-4%0A  > 1b8c30d Cleanup CRD storage on shutdown%0A  > 1ec2449 Merge pull request # 109978 from wojtek-t/remove_storage_tracking%0A  > 2046a29 Remove warning log for merging meta and scale type%0A  > 21a45c1 Merge pull request # 108011 from cici37/benchmark%0A  > 94148b5 Cleanup no-longer used storage cleanup method%0A  > fe87b2a Merge pull request # 109891 from pohly/log-dependency-update%0A  > 97b5e54 benchmark unstructuredToVal%0A  > 057887d Merge pull request # 109602 from lavalamp/remove-clustername%0A  > 08a2064 dependencies: logr and zapr v1.2.3%0A  > 9b3dd0c generated files%0A  > 42c5701 Merge pull request # 109804 from cici37/celUpdate%0A  > 4b7a318 Update go-control-plane, cncf/xds/go, cncf/udpa/go and remove unused versions%0A  > fc318e0 Update GRPC%0A  > 42e3d58 Update genproto and antlr.%0A  > 637f1a6 Bump cel-go to v0.11.2%0A  > 0b2f79f Merge pull request # 109440 from liggitt/gomod-1.18%0A  > 47b3e71 Merge pull request # 109268 from liggitt/pruning-metadata%0A  > dd13fbf Regenerate vendor%0A  > 86df472 Merge pull request # 109303 from wojtek-t/clean_storage_shutdown%0A  > b4a77b2 Fix bug treating metadata fields as unknown fields%0A  > d779722 Implement Destroy() method for all registries%0A  > 3a045b9 Expand unit tests of pruning of unknown fields in metadata%0A  > 24b17b0 Merge pull request # 109242 from cici37/addTest%0Abumping k8s.io/api 44d27eb...88912e3:%0A  > 88912e3 Update dependencies to v0.25.4 tag%0A  > e7b469b Merge pull request # 112808 from cheftako/automated-cherry-pick-of-# 112689-upstream-release-1.25%0A  > 1102e6f Updated vendor to the new preferred versions.%0A  > fce3016 Merge pull request # 112161 from pohly/automated-cherry-pick-of-# 112129-origin-release-1.25%0A  > 29513a2 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 5c4a1b1 Merge remote-tracking branch 'origin/master' into release-1.25%0A  > 714e431 Merge pull request # 111657 from aojea/hc_nodeport%0A  > 8608211 Merge pull request # 109090 from sarveshr7/multicidr-rangeallocator%0A  > 7840548 doc services healthcheckNodePort is inmutable%0A  > b88698c Merge pull request # 111258 from dobsonj/kep-596-ga-feature-flag%0A  > a7621fb Auto generate code for ClusterCIDR API%0A  > 2f9e588 Merge pull request # 111113 from mimowo/retriable-pod-failures-job-controller%0A  > b964bc7 Move CSIInlineVolume feature to GA%0A  > 14e048f Introduce networking/v1alpha1 api, ClusterCIDR type%0A  > 3be517c Merge pull request # 111696 from liggitt/go119mod%0A  > fe83bea Support handling of pod failures with respect to the specified rules%0A  > 991b481 Merge pull request # 108692 from jsafrane/selinux%0A  > e281bde Update go.mod to go1.19%0A  > f42f86a Regenerate files%0A  > a39f97c Add CSIDriverSpec.SELinuxMount%0A  > c8f0601 Merge pull request # 111677 from dims/stop-panic-in-govet-levee%0A  > ea1451a run lint-dependencies and follow directions%0A  > a2b9bcc Stop panic in govet-levee CI job%0A  > ad89a10 Merge pull request # 110495 from alexzielenski/atomic-objectreference%0A  > e590d1f Merge pull request # 111090 from kinvolk/rata/userns-support-2022%0A  > d978b18 mark persistentvolume's claimRef as granular%0A  > 7488a8c Merge pull request # 111435 from soltysh/cronjob_timezone_beta%0A  > 2a31718 Update autogenerated files%0A  > d351ecd Merge pull request # 111557 from alexzielenski/update-smd-422%0A  > f990455 Update generated%0A  > 9448de2 pkg/apis, staging: add HostUsers to pod spec%0A  > ae37896 update smd to 4.2.3%0A  > 010c740 Promote CronJobTimeZone to beta%0A  > 1b82208 Merge pull request # 110959 from mimowo/retriable-pod-failures-pod-conditions%0A  > 08dedd8 Introduction of a pod condition type indicating disruption. Its `reason` field indicates the reason:%0A  > f5e1938 Merge pull request # 111587 from ialidzhikov/k8s-utils@ee6ede2d64ed%0A  > b3c30ab Update `k8s.io/utils` to `ee6ede2d64ed`%0A  > be740eb Merge pull request # 111441 from denkensk/respect-topology%0A  > a76179a Merge pull request # 111402 from verb/111030-ec-ga%0A  > acf399c code generated by script for MatchLabelKeys in TopologySpreadConstraint%0A  > 537ea12 Merge pull request # 111442 from ialidzhikov/k8s-utils@56c0de1e6f5e%0A  > d8280df Remove EphemeralContainers beta disclaimer%0A  > d96a10b api defination for MatchLabelKeys in TopologySpreadConstraint%0A  > 8f210eb Update `k8s.io/utils` to `9bab9ef40391`%0A  > 04aced3 Merge pull request # 111254 from dims/update-to-golang-1.19-rc2%0A  > dda4dee Generate and format files%0A  > f6f0d0e Merge pull request # 111194 from ravisantoshgudimetla/promote-maxSurge-ga%0A  > f77fa25 Merge pull request # 111229 from ravisantoshgudimetla/promote-podOS-GA%0A  > 7b89ea1 Generated: maxSurge for DS%0A  > 9a18f7a Merge pull request # 110178 from kevindelgado/validation-beta-1-25%0A  > 844753e Generated: PodOS field to GA%0A  > d895ab7 api: Promote DS maxSurge to GA%0A  > 096c9df Merge pull request # 110388 from sanposhiho/graduate-mindomain-beta%0A  > 1d3dcfc update kjson%0A  > bdc8eb0 api: Promote PodOS field to GA%0A  > fa32a3a Merge pull request # 110896 from ravisantoshgudimetla/promote-minReadySec-sts-update-ga%0A  > eeea400 Update doc comment%0A  > 08c75a7 Merge pull request # 111008 from cici37/bumpCEL%0A  > 40e8eea Generated: minReadySeconds for STS%0A  > 0110f55 Update v1 package to graduate minDomains to beta%0A  > 0c6d49d Bump cel-go to v0.12.0%0A  > df27ddf api: Promote statefulset MinReadySeconds to GA%0A  > b9bd732 Merge pull request # 110564 from j4m3s-s/add-ports-doc-fix%0A  > 51e4c4a Merge pull request # 111010 from thockin/remove-refs-to-EndpointSliceNodeName%0A  > b7c39ad Fix description of Ports in PodSpec%0A  > 248dcdb Merge pull request # 111001 from pohly/klog-update%0A  > 4756865 Remove obsolete refs to gate EndpointSliceNodeName%0A  > b5b8fba build: update to klog v2.70.1%0A  > 8488949 Merge pull request # 110990 from thockin/svc-typenames-IPFamilyPolicyType%0A  > ed77e2e Rename IPFamilyPolicyType => IPFamilyPolicy%0A  > 33ab20e Merge pull request # 110868 from rikatz/endport-to-ga%0A  > f18d381 Merge pull request # 110831 from chendave/openapi%0A  > 270b22d Generated files for endPort promotion%0A  > 724b071 Bump `kube-openapi` to the latest%0A  > e803bc1 Promote endPort to GA%0A  > b98f264 Merge pull request # 110724 from pohly/klog-update%0A  > 61fcc0f build: update to klog v2.70.0%0A  > edebc67 Merge pull request # 110561 from Shubham82/extend_Description%0A  > 60387f6 Merge pull request # 110378 from lucacome/bump-grpc%0A  > 1cba8e4 RBAC: Modify the Description for the apiGroup.%0A  > 89ed2a8 Bump grpc to v1.47.0%0A  > 6b0201d Merge pull request # 110520 from dims/update-gopkg.in/yaml.v3-to-v3.0.1%0A  > 2c10714 Update gopkg.in/yaml.v3 to v3.0.1%0A  > d50b1bc Merge pull request # 109293 from iamNoah1/improve-ingressclassname-api-doc%0A  > 832b1f4 Merge pull request # 109938 from dims/move-from-k8s.gcr.io-to-registry.k8s.io%0A  > bba462c generate ressources after change request%0A  > ed22bb3 Move from k8s.gcr.io to registry.k8s.io%0A  > d1f2717 add change requests%0A  > be84346 Merge pull request # 109968 from kerthcet/feature/optimize-apifield-comment%0A  > e85f85a generate ressources after change request%0A  > 209903b amend comment of NodeInclusionPolicy%0A  > bac3ee2 add change requests%0A  > ae35a85 Merge pull request # 108492 from kerthcet/feature/add-NodeInclustionPolicies%0A  > a3f4ca9 generate ressources after change request%0A  > 202371b feat: add NodeInclusionPolicy to TopologySpreadConstraint in PodSpec%0A  > 4e39c88 add change requests%0A  > 9b88471 Merge pull request # 109891 from pohly/log-dependency-update%0A  > af2d87a add generated assets%0A  > 548c53c Merge pull request # 109602 from lavalamp/remove-clustername%0A  > 0f669be dependencies: logr and zapr v1.2.3%0A  > 4b894ff first shot improving api doc for ingressclassname%0A  > 5e2f5ad Merge pull request # 109308 from danwinship/traffic-policy-docs%0A  > eb567e7 compat%0A  > a2ee8c7 Merge pull request # 109803 from liggitt/api-fixture-data%0A  > 85c4c9d Clarify ExternalTrafficPolicy/InternalTrafficPolicy definitions%0A  > fcb6509 Merge pull request # 109440 from liggitt/gomod-1.18%0A  > 1afa1ae Remove v1.22.0 API fixture data%0A  > 3f52c1d Regenerate vendor%0A  > a2ae4d4 Add v1.24.0 fixture data%0A  > d672b36 Merge pull request # 109506 from wangrzneu/fix-comment%0A  > f2f8c15 Merge pull request # 109421 from vpnachev/fix/typo-in-token-request-doc-string%0A  > 35e4518 fix IngressClassParametersReferenceScopeCluster comment in staging/src/k8s.io/api/networking%0A  > af4f75e Merge pull request # 105963 from zhucan/bugfix-95367%0A  > aed3ebb Fix typo in TokenRequest doc string%0A  > 7a89730 Merge pull request # 109436 from JamesLaverack/revert-108290%0A  > 56fb9f0 generated code and doc%0A  > 1f82dd7 Revert "Introduce APIs to support multiple ClusterCIDRs (# 108290)"%0A  > 6f81c7b csi: add nodeExpandSecret support for CSI client%0Abumping knative.dev/hack 6887217...7d81248:%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0A  > f591fea individual globbing is required (# 284)%0A  > 4b3f230 Update community files (# 283)%0A  > 9153cc6 Update community files (# 282)%0A  > 359d585 Revert "Extract tools to knative.dev/toolbox (# 280)" (# 281)%0A  > 1421f12 Extract tools to knative.dev/toolbox (# 280)%0A  > 3b8ef01 Update community files (# 279)%0A  > 1eebfb3 Update community files (# 278)%0A  > 3de51af Set GitHub Release Title to the version (# 277)%0A  > f2f3107 Update community files (# 273)%0A  > f41894d Find checksums file works with ARTIFACTS_TO_PUBLISH variable (# 275)%0A  > d71d569 :bug: Location-agnostic sign release (# 268)%0A  > b674d64 Update community files (# 270)%0A  > 549c360 Cleanup: remove ioutil for new go version (# 265)%0A  > 5814be5 Update community files (# 267)%0A  > c7cfcb0 Update community files (# 263)%0A  > af8745e Update community files (# 262)%0A  > cf3796d Upload attestations and print cosign version (# 261)%0A  > b9801b4 Update community files (# 260)%0A  > 7233e77 No more sugar controller in upstream eventing (# 259)%0A  > c12c1bf Revert of # 257 (# 258)%0A  > 6397aac :bug: Don't use NodeLocalDNS addon (# 257)%0A  > 2e610ce Update community files (# 256)%0A  > de2ff40 Allow tests to skip dumping resources on failure (# 255)%0A  > 646aac0 e2e script tweaks (# 252)%0A  > d470f52 Format go code (# 253)%0A  > b035462 Calculate Image references properly (# 251)%0A  > 1ba176e Trap calls are now executed in LIFO order (# 249)%0A  > 8f3c705 Update community files (# 247)%0A  > 62b15bd drop support for the istio add on flag (# 243)%0A  > f5be74f Update community files (# 245)%0A  > 80fd6da KO_DATA_PATH doesn't need to be set anymore (# 244)%0A  > 4b6bd86 Format go code (# 239)%0A  > 566898d Update community files (# 242)%0A  > 9d2ae47 Update community files (# 241)%0A  > cf1a127 :gift: Use Knative ls-tags tool (# 238)%0A  > 3fdc50b Remove Signing Feature Gate (# 236)%0A  > 2d67db5 generate provenances (# 237)%0A  > 52a87e1 Update community files (# 235)%0A  > 92a65f1 don't quote vars referencing files (# 234)%0A  > b3c9790 Notarize Mac binaries (# 231)%0A  > 0198902 Format go code (# 226)%0A  > 7dff557 Update community files (# 233)%0Abumping github.com/go-logr/logr 99e02a9...47e013c:%0A  > 47e013c Merge pull request # 128 from thockin/format-test%0A  > b359493 Merge pull request # 140 from thockin/testing_testr%0A  > d731630 Add some test cases%0A  > 28755ae Merge pull request # 130 from thockin/nil-stringer%0A  > 5377a98 Move testing -> testr, deprecate, alias old names%0A  > 4610455 Reformat existing test cases%0A  > ec7c16c Merge pull request # 135 from thockin/fix-actions-go-versions%0A  > 945d619 funcr: Handle panic in Stringer, Marshaler, error%0A  > e2fd555 Merge pull request # 133 from pohly/nil-logger%0A  > e438a74 Fix GH actions for Go versions, drop 1.14%0A  > af7b868 Add stringer, error, marshaler to benchmark%0A  > eb02c45 Merge pull request # 129 from tonglil/patch-1%0A  > 68ef51c docs: describe handling of optional logger parameters%0A  > 8aa3af1 Update README.md%0Abumping k8s.io/gengo 397b4ae...fad74ee:%0A  > fad74ee Merge pull request # 234 from aojea/use_github_actions%0A  > e83a76d Merge pull request # 233 from rainest/fix/filter-abort%0A  > f99002e remove travis%0A  > 3913671 Merge pull request # 199 from rainest/log/lower-severity-uncopyable%0A  > 535f8cc Restore uncopyable type case in Filter%0A  > 3bcdbc7 Merge pull request # 232 from alexzielenski/defaulter-const-symbol-reference%0A  > 914c10e Update examples/deepcopy-gen/generators/deepcopy.go%0A  > c0856e2 Merge pull request # 231 from weilaaa/add_method_symmetric_difference_in_set%0A  > 945b13c fix typo%0A  > ad375a7 Fail if any requested type cannot be copied%0A  > 66c86ac add method symmetric difference in set%0A  > 49f7e1e fix typo%0A  > 20f90a4 Update examples/defaulter-gen/generators/defaulter.go%0A  > e1d2c67 remove incorrect quotes from ref regex comment%0A  > 91632a7 address comments%0A  > bab4b7f allow +default to refer to symbols in code%0Abumping knative.dev/hack/schema 9b76387...7d81248:%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0A  > f591fea individual globbing is required (# 284)%0A  > 4b3f230 Update community files (# 283)%0A  > 9153cc6 Update community files (# 282)%0A  > 359d585 Revert "Extract tools to knative.dev/toolbox (# 280)" (# 281)%0A  > 1421f12 Extract tools to knative.dev/toolbox (# 280)%0A  > 3b8ef01 Update community files (# 279)%0A  > 1eebfb3 Update community files (# 278)%0A  > 3de51af Set GitHub Release Title to the version (# 277)%0A  > f2f3107 Update community files (# 273)%0A  > f41894d Find checksums file works with ARTIFACTS_TO_PUBLISH variable (# 275)%0A  > d71d569 :bug: Location-agnostic sign release (# 268)%0A  > b674d64 Update community files (# 270)%0A  > 549c360 Cleanup: remove ioutil for new go version (# 265)%0A  > 5814be5 Update community files (# 267)%0A  > c7cfcb0 Update community files (# 263)%0A  > af8745e Update community files (# 262)%0A  > cf3796d Upload attestations and print cosign version (# 261)%0A  > b9801b4 Update community files (# 260)%0A  > 7233e77 No more sugar controller in upstream eventing (# 259)%0A  > c12c1bf Revert of # 257 (# 258)%0A  > 6397aac :bug: Don't use NodeLocalDNS addon (# 257)%0A  > 2e610ce Update community files (# 256)%0A  > de2ff40 Allow tests to skip dumping resources on failure (# 255)%0A  > 646aac0 e2e script tweaks (# 252)%0A  > d470f52 Format go code (# 253)%0A  > b035462 Calculate Image references properly (# 251)%0A  > 1ba176e Trap calls are now executed in LIFO order (# 249)%0A  > 8f3c705 Update community files (# 247)%0A  > 62b15bd drop support for the istio add on flag (# 243)%0A  > f5be74f Update community files (# 245)%0A  > 80fd6da KO_DATA_PATH doesn't need to be set anymore (# 244)%0A  > 4b6bd86 Format go code (# 239)%0A  > 566898d Update community files (# 242)%0A  > 9d2ae47 Update community files (# 241)%0A  > cf1a127 :gift: Use Knative ls-tags tool (# 238)%0A  > 3fdc50b Remove Signing Feature Gate (# 236)%0A  > 2d67db5 generate provenances (# 237)%0A  > 52a87e1 Update community files (# 235)%0A  > 92a65f1 don't quote vars referencing files (# 234)%0A  > b3c9790 Notarize Mac binaries (# 231)%0A  > 0198902 Format go code (# 226)%0A  > 7dff557 Update community files (# 233)%0A  > 6887217 Update community files (# 232)

Signed-off-by: Knative Automation <automation@knative.team>

---
## [BRB67/19ilence19ounds](https://github.com/BRB67/19ilence19ounds)@[434600fd7f...](https://github.com/BRB67/19ilence19ounds/commit/434600fd7fa494eaa0d943dc0274cfa5c40374a8)
#### Friday 2023-05-05 02:25:44 by Sivens Glaude

Thank You LOR4! Added New Readings Bro<3K

Thank You LOR4! Added New Readings Bro<3K

Note: These unofficial recordings are of works written by other authors. The recordings were created for my personal educational purposes.  Please support the original authors. Please let me know if you need me to remove any of the recordings and I will. Links to purchase the professional works that inspired the recordings may be found below. Thank you for your time, and again please support the official authors/publishers. 

Free Bibles?:
Online Printable Bibles:
https://www.jw.org/en/library/bible/ 
https://www.gutenberg.org/files/10/10-h/10-h.htm

More Materials:
Better Bibles?: 
https://www.walmart.com/search?q=bilingual%20bible&typeahead=bilingual%20bible

Recorders:
https://www.walmart.com/search?q=audio+recorder

Books for Buying/Sampling:

A Beginner's Guide to Constructing the Universe: The Mathematical Archetypes of Nature, Art, and Science
https://www.goodreads.com/book/show/204068.A_Beginner_s_Guide_to_Constructing_the_Universe?from_search=true&from_srp=true&qid=5EI1jWBDSi&rank=1 

The Complete Book of Origami: Step-by-Step Instructions in Over 1000 Diagrams/37 Original Models
https://www.goodreads.com/book/show/873239.The_Complete_Book_of_Origami?ref=nav_sb_ss_1_16


Ultimate Guide: Home Repair Improvement
https://www.goodreads.com/book/show/13014368-ultimate-guide?ref=nav_sb_ss_1_26

Peace and Blessings Bro<3K
God is Go<3D

---
## [ryan961/weaver](https://github.com/ryan961/weaver)@[b9eb4fc35d...](https://github.com/ryan961/weaver/commit/b9eb4fc35df080f128de5d674e2ca52d7483932a)
#### Friday 2023-05-05 02:33:00 by Michael Whittaker

Changed deployers to persist data in one spot.

Recall that deployers often have to persist various data to the file
system. The "weaver multi" deployer, for example, persists logs,
registrations, and traces to files.

Before this PR, deployers would store logs in /tmp and everything else
in ~/.local/share/serviceweaver. Different deployers would sometimes
store their data in the same directory. A "multi_perfetto.db" file would
be right next to a "single_perfetto.db" file, for example.

This made purging data files annoying. It was like a scavenger hunt
trying to track down the various places that data was stored. This PR
changes deployers to store all their data in a single directly. For
example, the "weaver multi" deployer now stores everything inside
"~/.local/share/serviceweaver/multi". The single process deployer stores
everything inside "~/.local/share/serviceweaver/single".

This makes purging much simpler. It also makes it clearer which files
are being used by which deployers.

Note that this PR moves logs out of /tmp, which persists them longer.
This means that logs won't be garbage collected automatically, but I
think that's actually a good thing. We should implement a principled way
of garbage collecting logs, rather than leaving it up to /tmp. I think
it would be surprising and frustrating if an important log file was
spuriously deleted by the OS.

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[0410075cc8...](https://github.com/Bjarl/Shiptest/commit/0410075cc811c5f65d7dc085a665c1ebb3a20e44)
#### Friday 2023-05-05 02:36:45 by meemofcourse

Ports mothroaches + Moth emotes (#1843)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Can you guess what this PR does? If you answered that it ports [this
pull request](https://github.com/tgstation/tgstation/pull/68763), [this
pull request](https://github.com/tgstation/tgstation/pull/71784), and [a
partial part of this one
too](https://github.com/BeeStation/BeeStation-Hornet/pull/7645/), then
you're right!

![imagen](https://user-images.githubusercontent.com/75212565/227387000-cc205158-286b-4841-9c5a-2e4d6d8d6200.png)

![imagen](https://user-images.githubusercontent.com/75212565/227386830-213997a1-ebe9-4573-8f8e-052e72bacea2.png)


You can also craft moth plushies now. You just need some cloth,
mothroach hide, and a heart!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

silly little moth roaches and emotes, who wouldn't want them in the
game?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Mothroaches are now a thing
add: Moth laughter, chittering and squeaking
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [ttaylorr/git](https://github.com/ttaylorr/git)@[07f91e5e79...](https://github.com/ttaylorr/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Friday 2023-05-05 02:47:48 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [Aroliacue/AroliacueChomp](https://github.com/Aroliacue/AroliacueChomp)@[b1f52736ca...](https://github.com/Aroliacue/AroliacueChomp/commit/b1f52736ca4407110979e2c246ae002b89ed86ae)
#### Friday 2023-05-05 02:54:47 by Fluff

Loots, Loots, and More Loots

-Removed the gas in the phoron canisters, and added some chemdispensers in place of the sleeper
-Made the carbinter gun thing useable
-Hopefully made the pirate vessel worth visisting
-Changed the walls of the vox shuttle, adjusted the foes because the giant voxes just stop exsisting, and mercs should die quikly
-Slightly buffed red shuttle down loot.
-Buffed the loot of the blood church

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[f7a49c4068...](https://github.com/unit0016/effigy-se/commit/f7a49c4068f1277e6857baf0892d355f1c055974)
#### Friday 2023-05-05 03:25:54 by Ryll Ryll

Gunpoints now take half a second to activate, make gasp sounds, and briefly immobilize the shooter and target, other small balance changes (#74036)

## About The Pull Request
This PR messes around with gunpoints a bit, with the purpose of making
them more viable in certain scenarios without making them obnoxious. The
biggest change is that gunpoints now require a 0.5 second do_after()
where neither the shooter nor the target moves, and immobilizes both of
them for 0.75 seconds if point blank, or half that if you're 2 tiles
away. Originally you were supposed to only be able to initiate a
gunpoint from point-blank, but #56601 seems to have removed that
requirement, so we'll run with it and just leave it as advantageous to
gunpoint closer up. The do_after() reinforces that it should be used as
an ambush tactic, and so you can't use it on someone who's actively
fleeing or fighting you.

Getting held up will now make you emit a shocked gasp sound, a la Metal
Gear Solid, which combined with the short immobilize will hopefully make
it more noticeable that someone's pointing a gun at you.

Holdups will now immediately give a 25% bonus to damage and wounds,
instead of having to wait 2.5 seconds to hit the double damage stage.

Finally, right clicking someone that you're holding up will no longer
shoot them. That just feels like good consistency.

## Why It's Good For The Game
Hopefully makes gunpoints a little more viable for when you want to
stick someone who's not expecting it up without them immediately jetting
off. In the future I'd like to ape Baycode and let the gunman have an
action that toggles whether the victim is allowed to move, so you can
order them to move to a second location without instantly shooting them,
but that'll come later.
## Changelog
:cl: Ryll/Shaps
balance: Holding someone at gunpoint now requires both the shooter and
the victim to hold still for half a second before activating, so you
can't hold-up people fleeing or fighting you. After that, it will
briefly immobilize the both of you, 0.75 seconds if adjacent, or half
that if you're two tiles away. Nuke ops are immune to the
immobilization, since they're ready to die anyways.
balance: Holding someone up will immediately apply a 1.25x damage and
wound multiplier, rather than waiting 2.5 seconds to hit 2x.
soundadd: Being held up will now make the victim play a sharp gasp
sound, a la Metal Gear Solid.
qol: Trying to hold someone up that you're already holding up will no
longer shoot them.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Tuckatk/tgstation](https://github.com/Tuckatk/tgstation)@[c27f9a6d9b...](https://github.com/Tuckatk/tgstation/commit/c27f9a6d9b9739baae09db063b6eb266d525772c)
#### Friday 2023-05-05 04:02:06 by necromanceranne

Minor Nukie Thing: Bolt-action Sniper Rifle, balance coding, and some ammo changes (#73781)

## About The Pull Request

### The Rifle:
-The Sniper Rifle is now a bolt action. This replaces the 4 second fire
delay on the sniper rifle. This overall will improve the fire rate if
you're good at racking the bolt, but it will also feel less like you're
in a weird limbo of inaction while using the sniper rifle, since the
fire delay can be quite confusing to players not used to it. This can be
tweaked, like reducing the speed of the racking action, if it seems like
it is too much.
-The scope component now goes up to 50 tiles (or so), which allows you
to gain a significant sightline over an area. The reasoning for this is
simple. The component actually nerfed the overall range of the sniper
rifle's scope, so this should hopefully restore that somewhat. And
having such a huge sightline makes it much easier to utilize the
impressive range of the rifle. Currently, it's really only ideal for
extremely close range fighting.
-The normal sniper rifle, the one that syndicate base scientists get,
can be suppressed. I don't know why it was different.

### The Ammo:

Normal .50 BMG: Does much more object damage, and on top of that deals
additional damage to mechs, but not by much more. Now, when it
dismembers a limb, it also deals its damage to the chest. This ensures
that you didn't straight up lose out on dealing a killing blow because
you took their limb off, and makes the dismemberment property of .50 BMG
a significant upside rather than a immense detriment.

Marksman: Gains a lot of the above benefits, but has much lower range.
Why this nerf? It's actually because of some funny nonsense with how
ricochet works. Which can cause....accidents to happen. To you. Consider
that firing down a straight line and missing could be quite embarrassing
when the bullet has 400 tiles of range.

Soporific: Now called Disruptor ammo. Works as it did before, putting
humans to sleep for 40 seconds (seriously, 40 seconds). Also deals some
stamina damage, if...that's relevant. But now also causes an EMP effect
and a boatload of added damage to both mechs and borgs, allowing it to
be an excellent anti-mech and anti-borg ammo type, as well as scrambling
any pesky suit sensors, energy weapons and so on in an area around the
impact. Useful for support fire.

Incendiary (NEW!): Causes a massive firebomb to go off where it impacts
(no explosion, so this isn't a stun). Also sets the target on fire,
which is always fun. Good for shooting into groups of people with
impunity. Also deals burn damage instead, since I think nukies could use
more methods for direct fire damage.

Surplus (NEW!): It's .50 BMG but it lacks most if not all the upsides.
No armour penetration, no dismemberment, no paralysis. It still deals a
lot of damage to objects, so not a bad option for simply removing
structures from afar. So what's the point in this ammo? You can buy 7
magazines for the price of one. I want to introduce 'Surplus' as an idea
for nukies to invest in if they want to be able to keep shooting but
they're really on a budget, like most non-warop nukies tend to be. This
is definitely subject to change (like a damage decrease on top of
everything else).

Pricing and Capacity: Normal ammo and surplus costs 3 TC. Every special
ammo costs 4 TC. Every special ammo also has the same ammo capacity as
the normal magazine. It's kind of weird how most of the subtypes had 5
shots rather than 6, but then soporific had...3? I don't get it. This
would probably cause a good deal of confusion, especially if you are
swapping ammo types and weren't aware of this particular oddity.

Anyway, 6 shots.

### Minor Addition
Gets rid of the cheap suppressor. It lies to players, tricking them into
thinking this is a low quality suppressor. Newsflash, it isn't. There is
no distinct difference between that suppressor and the normal
suppressor.

## Why It's Good For The Game

The sniper rifle, unfortunately, sucks a lot except for very specific
use cases. It got a big nerf with the scope component in terms of range,
even if the functionality is way cooler. And, at a baseline, there was
some counterintuitive functions attached to it. Dismemberment was cool,
but it also caused a loss in overall damage due to how limbs contribute
to core health. On top of this, the cool ammo types were...not much
better? Penetrator was almost always the best option, even if it lost a
lot of damage as a consequence.

So, what was it good for? X-ray + Penetrator. Pretty much, that's it. It
has some other uses but if I had to be entirely honest, there wasn't
much that other weapon couldn't do as well.

Hopefully this helps things going forward, and I want to mess with this
as well down the line in case its a bit too much of a boost in power.

Absolutely please rip this PR apart.

## Changelog
:cl:
balance: Makes the syndicate sniper rifle a bolt-action rifle.
balance: Sniper rifles have a scope range of roughly 50 tiles.
balance: Sniper rifle ammo, if it dismembers your limbs, does damage to
the chest.
balance: All the various syndicate sniper rifle magazines have
consistent casing quantities (6 shots). They also have more consistent
pricing. 3 for normal and a box of surplus, and 4 for every other type.
balance: Reduces the range of Marksman ammo to 50 tiles. Not because it
is strong, but because you might accidentally shoot yourself if you're
not watching where you're shooting. Ricochets are no joke.
add: Replaces Soporific with Disruptor ammo. Works like soporific, but
also EMPS things it hits.
add: Adds Incendiary .50 BMG. Causes a combustion to erupt from the
struck target, as well as setting targets on fire. Great for parties.
add: Adds Surplus .50 BMG. It sucks, but you get a lot of them! Quantity
over quality, baby.
remove: The suppressors in the bundle are of standard quality. The
apparent 'cheap suppressor' that came bundled with the C-20r and sniper
rifle were found to actually be 'fine'. Trust us.
/:cl:

---
## [highlight/highlight](https://github.com/highlight/highlight)@[18d94ccc74...](https://github.com/highlight/highlight/commit/18d94ccc7425a9441000e1bf4a7f92565898666e)
#### Friday 2023-05-05 04:44:25 by Lewis Liu

Enable Reflame for Highlight web app (#4586)

## Summary

<!--
Ideally, there is an attached Linear ticket that will describe the
"why".

If relevant, use this section to call out any additional information
you'd like to _highlight_ to the reviewer.
-->

This PR finally enables [Reflame](https://reflame.app/)
[previews](https://preview.highlight.io/~r/start-preview/?mode=production&variantId=01GY11FVTK9FMXX2DSCR6T4VRD&variantName=git%7Enew-reflame-app-1&userId=01FQZZ7XJFDA799Z1Z9DRCFXWA)
for the Highlight web app. 🥳

### What does this mean for me?

First you'll need to sign up at https://reflame.app, connect your GitHub
account, and ask @Vadman97 for an invite to the highlight organization.

Then, once this PR is merged, every time you push up a change to the web
app (in /frontend) or any of its dependencies, you'll get a Reflame
preview link on your commit immediately, usually within 3 seconds,
instead of however many minutes it used to take:
![Screenshot 2023-04-13 at 5 40 57
PM](https://user-images.githubusercontent.com/6934200/231912410-5dc2880d-353c-402e-8562-67ce4ee54137.png)

In addition, you'll have access to the Reflame [VSCode
extension](https://marketplace.visualstudio.com/items?itemName=reflame.agent)
for development, which deploys your changes usually within ~500ms of a
file save, and then reflects your changes instantly with a full browser
refresh in production mode, or with state-preserving React fast refresh
in development mode. See development mode in action here:


https://user-images.githubusercontent.com/6934200/231914985-3679e955-ddcf-4ad1-9c7e-1c7451dc3ef5.mp4

It's worth noting that Reflame is actually _deploying your changes to
the internet_ every time, so you can send these links to yourself to
check your changes on another device (even multiple devices
simultaneously), or share them with teammates or customers to give them
a sneak peak of what you're working on, iterate with their feedback, and
have those changes reflected on their browsers in real time (even if
they're on the other side of the world)!

### How do I even review this? There's like 500 files here?!

I'd recommend reviewing either commit by commit and skipping the 2nd
commit, or by viewing all files changed and skipping over everything in
`__generated` folders, since they only contain files generated using the
newly added build scripts. This should leave only about 30 files to
review, and most of the changes are a only a couple of lines long.

These scripts and generated files are a temporary stop-gap to support
features that don't have first-class support in Reflame yet,
specifically:

- Reading version from package.json
- CSS/SCSS modules
- Tailwind
- SVGR
- Git Submodules
- Vanilla Extract

These are roughly ranked in order of how quickly I think they will get
first-class support in Reflame, at which point we'll be able to remove
the associated scripts and generated files. Notably, Vanilla Extract is
as far down the list as it is because it requires executing
user-supplied code as part of its build process, which is going to take
quite a bit of work to enable safely in a multitenant system like
Reflame (but I do plan on tackling this eventually as I get closer to
building features like testing and backend APIs support). Though we may
still be able to get rid of the build script sooner than that by
building it into the VSCode extension if there's enough demand.

Outside of the script and configuration changes, there are a few
additional source changes for compatibility. I left comments on the PR
for every one of these explaining the motivation behind them. I've also
split most of them out into separate PRs so they can be reviewed, tested
and shipped independently:

- https://github.com/highlight/highlight/pull/5086
- https://github.com/highlight/highlight/pull/5087
- https://github.com/highlight/highlight/pull/5088
- https://github.com/highlight/highlight/pull/5089 

## How did you test this change?

<!--
Frontend - Leave a screencast or a screenshot to visually describe the
changes.
-->

A lot of care has gone into making sure your existing local dev workflow
works exactly as you're used to (just with a few more scripts running
than before), and that the production deployment process remains
untouched as well. If you notice any material differences in any of your
day to day workflows while trying out this PR, or in the Render preview
deploys, please let me know and I'll try to address it ASAP.

I've tried following the [docker dev guide
here](https://www.highlight.io/docs/getting-started/self-host/dev-deployment-guide)
and running `yarn dev:frontend` (without the `doppler run --` part), and
both seem to be working identically as on main as far as I can tell,
though for the latter I'm missing a few env vars from doppler so
couldn't verify past the login screen, will need your help to make sure
everything works as expected there.

If you want to try out Reflame before this PR gets merged, just make a
branch off of this PR (previews are not working for this PR because it's
coming from a fork, and the appId in the config is for the
highlight/highlight repo, but it should work if you cherry pick these
commits into another branch within this repo). The VSCode extension
should also just work once you get a VSCode account.
[Here's](https://preview.highlight.io/~r/start-preview/?mode=production&variantId=01GY11FVTK9FMXX2DSCR6T4VRD&variantName=git%7Enew-reflame-app-1&userId=01FQZZ7XJFDA799Z1Z9DRCFXWA)
the preview I'm using to test my changes.

Would love to make Reflame better with your feedback! Just leave a
comment here, [shoot me an email](mailto:lewis@reflame.app), or ask for
an invite to the #highlight-reflame channel in Slack to chat there or
send me a DM.

## Are there any deployment considerations?

<!--
 Backend - Do we need to consider migrations or backfilling data?
-->

Definitely would be helpful to get a Render preview for this to poke
around in.

---
## [hughjonesd/ggmagnify](https://github.com/hughjonesd/ggmagnify)@[e53fd8d257...](https://github.com/hughjonesd/ggmagnify/commit/e53fd8d257c869fb92ae8f5a5695b7b5f5812d5c)
#### Friday 2023-05-05 04:47:31 by David Hugh-Jones

Really make tests work with CI. Fuck you again, CI.

---
## [tmancill/squeezelite](https://github.com/tmancill/squeezelite)@[226efa300c...](https://github.com/tmancill/squeezelite/commit/226efa300c4cf037e8486bad635e9deb3104636f)
#### Friday 2023-05-05 05:03:15 by Ralph Irving

So, I've made more tests with a simple HTTP server and a client just download data through a simple GET. It's 100% easy to reproduce the issue if the client throttle at say 160kbits/s and a file of ~3.5MB is transferred. The HTTP server confirms (as does tcpdump) that all is transferred in a record time and using TCPview (or netstat) you can see that the connection is in FIN_WAIT_2.

It is all received because the TCPWindow quickly gets massive (a few MB) and so are the kernel's buffers. Obviously, Windows has a half-open socket timer that is started with the first FIN send and that causes the issue 100% time.

By limiting SO_RCVBUF, the TCPWindow cannot open that large as soon as the application does not get data fast enough. Of course, when we'll fill the stream and output buffers, TCPWindow will open because we absorb data super fast, but it will shrink back as soon as we stop pumping data in because we are full.

Now, 4KB is awfully low and I tried to increase it and it was still fine at 65kB, I could see TCPWindow opening and closing. The funny thing is that when you do a getsockopt, system will return 65kB. If you set what you got, the problem disappear as expected. BUT, if don't set anything, then Windows uses some much larger value (although it told you it does not) and then the issues happens.

-philippe44.

Thanks philippe44 for tracking down the cause of this issue.
Increase squeezelite revision to 1419.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[199aa000d3...](https://github.com/tgstation/tgstation/commit/199aa000d3f46ee4386a65079992e4b9d0f2537d)
#### Friday 2023-05-05 05:03:35 by Rhials

Demotes Psyker Pirates to Bounty Hunter Duty (#75031)

This PR demotes the Psyker-gang from a pirate team to a fugitive hunting
team. For more information on Psyker pirates, please refer to #71650.

Stuff this also does in the process:
- Gives fugitive hunters their own subfolder in the fugitives antagonist
folder, moves some of their stuff into hunter-specific files rather than
interlacing it with the rest of the fugitive code.
- Moves the hunter backstories to defines, to make reading things easier
while I made this change.
- Exhaustively moves everything related to psykers from being
pirate-oriented to hunter-oriented (typepaths, locations where stuff is
defined, etc. There should be nothing left behind related to psykers in
anything pirate related). (Tell me if I missed anything somehow).

They still get their ship (they even get their own custom
psyker-friendly prisoner capsule). They still have a bunch of lethally
chambered firearms. They're the same gunrunning nutcases they were
before, just as bounty hunters.

To assist with basic tasks such as "getting to the station" or "figuring
out who the fuck we're supposed to be kidnapping", the psykers have
"acquired" a Seer to assist them. They can _try_ to coordinate the
psykers and lead them through situations where their impairments put
them at too great a disadvantage. If you're one of the psykers, make
sure to keep this guy alive at all costs!

Why are they called Shikaris instead of hunters? Mariam-Webster says
it's a Hindi word for some kind of hunter/tracker, and it sounded like
something a bunch of space-junkies would call themselves because they
think it sounds cool.

They now also come with a slightly different motivation, now that they
can't directly threaten the crew for money. Psyker hunters now arrive
tasked with a dirty kidnapping job, payment rendered in GORE.
## Why It's Good For The Game

Psykers aren't up to the challenge of being pirates. They're bogged down
by a number of fundamental issues that render them unable to do anything
expected of pirates. As it currently stands, they present about as much
threat as you would expect from three blind junkies with guns.

Removing them wholesale would be kind of lame. They can function as a
bunch of chaotic-neutral gun-toting space-maniacs, but for the purposes
of gameplay, keeping them as pirates would be a waste of their talents.

Moving them to a lower-stakes role not only moves them to a niche they
are more capable of filling, but gives players a more lax environment to
get a grip on playing psyker without being overwhelmed.

Giving them a seeing-eye role should bring a more unique dynamic to how
psykers are played (that is, some semblance of organization rather than
blind flailing), and should help get over the mechanical hurdles of
being a psyker until better solutions can be made. It shouldn't be too
big of an impact on balance considering the psyker gang only has three
spawns, while most hunter packs have 4+.

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[1b5c0489a4...](https://github.com/effigy-se/effigy-se/commit/1b5c0489a4088dca925ab061a389d95005c95820)
#### Friday 2023-05-05 05:11:33 by san7890

`ex_act()` will work on basic mobs again (lol) + Unit Test (#74953)

basically ex_act's implementation on basic mobs would call parent and
then react to it's value, this is presumably to do the first check about
space vine mutations and whatever. the problem is that the `/mob/living`
implementation would itself also call parent, and that would always
return null because `/atom/proc/ex_act` doesn't have a set return value.
So, this simply would _always_ early return, with ex_act presumably
*never* working on basic mobs for at least four months now.

I decided to then change up the return values for pretty much all
implementations of `ex_act()` since there was no rhyme or reason to
returning null/FALSE/TRUE, and documenting why it's like that.

Just to make sure I wasn't breaking anything doing this (at least on
base implementations), I wrote a unit test for all of the three major
physical types in game (objs, mobs, turfs) because i am a paranoid
fuckar. we should be good to go now though.
## Why It's Good For The Game

i noticed this because placing c4's on sargeant araneus wouldn't
actually damage it whatsoever. now it actually does the stated 30
damage, but araneus has like 250 health so it doesn't actually matter in
the long run. whatever at least it does the damn 30 now.

also adds a unit test for this specific case as well as a range of other
cases to ensure this stuff doesn't silently break in this way anymore

---
## [RomanRenders/sheephunt-massacre](https://github.com/RomanRenders/sheephunt-massacre)@[7424184ab9...](https://github.com/RomanRenders/sheephunt-massacre/commit/7424184ab97005c82c89031e1c89cc7b2e534bf8)
#### Friday 2023-05-05 05:36:23 by roman

fucking piece of shit why did god make me so fucking stupid

---
## [BogCreature/Shiptest](https://github.com/BogCreature/Shiptest)@[7df4885117...](https://github.com/BogCreature/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Friday 2023-05-05 06:38:42 by Mark Suckerberg

[Needs TM] The Accelerataning (#1781)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Gone are the days of spam clicking buttons to move faster in a
direction, with this PR, ships now accelerate constantly (as long as you
have fuel and don't touch the throttle) in a direction you set, leading
to a much smoother flight experience. I imagine it's going to be a bit
tougher to thread gaps, but flying a spaceship *is* quite literally
rocket science. So.

![](https://user-images.githubusercontent.com/29362068/220281305-12f6b796-9d8a-41ce-84a6-236bb03274da.gif)

Also actually makes the minimum and maximum speed work, and adjusts them
to a more tolerable level.

## Why It's Good For The Game
Eliminates the ability to cheese high speeds by spamming the accelerate
button, and also makes the flight experience much more pleasant as you
don't have to spam click to move a decent speed.

## Changelog

:cl:
add: A new system for ship flight, where you only point a direction and
set the throttle to change your speed, reducing the need for
spam-clicking.
fix: There's now a maximum and minimum speed, 600spm and 0.01spm,
respectively. The limits have been broken all this time.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [Lumi-sg/KnightTravails](https://github.com/Lumi-sg/KnightTravails)@[8d43edfee1...](https://github.com/Lumi-sg/KnightTravails/commit/8d43edfee1c3c36fe632b5adf813f45f44629dc4)
#### Friday 2023-05-05 07:40:07 by Lumi

awful way of preventing users interrupting the highlighting function I hate myself

---
## [golovasteek/rules_rust](https://github.com/golovasteek/rules_rust)@[80f0eb488a...](https://github.com/golovasteek/rules_rust/commit/80f0eb488ab9cabc4920ac446478cbf2feedc3f3)
#### Friday 2023-05-05 07:53:19 by scentini

Support for `no_std` mode (#1934)

Initial support for `no_std` mode.
This allows us to
1. Don't pass the whole standard library to compile actions that specify `no_std`
2. Conditionally select `crate_features` and `deps` based on whether `no_std` mode is used.
Currently the only supported modes are `off` and `alloc`, with a possibility to expand in the future.

The `no_std` support comes with the following caveats:
1. Targets in `exec` mode are still built with `std`; the logic here being that if a device has enough space to run bazel and rustc, std's presence would not be a problem. This also saves some additional transitions on `proc_macro`s (they need `std`), as they are built in `exec` mode.
2. Tests are still built with `std`, as `libtest` depends on `libstd`

There is quite an ugly hack to make us be able to `select` on the `no_std` flavor taking `exec` into account; I'm looking forward to the day where Bazel will expose better ways to inspect the cfg.

There is also one part I didn't manage to make work - having a `rust_test` that tests the `rust_shared_library` in `cc_common.link` mode; I got a link error for missing `__rg_alloc` & co. symbols, which should be present as we pass `--@rules_rust//rust/settings:experimental_use_global_allocator=True`. Unfortunately I could only spot this error on CI, and could not reproduce locally. I removed the test because the `rust_shared_library` is already tested via a `cc_test`. I will however give another shot at inspecting how my local setup differs from CI.

The `rust_binary` source code in `main.rs` was borrowed from https://github.com/jfarrell468/no_std_examples, big thanks to @jfarrell468 for letting me use it.

Co-authored-by: Krasimir Georgiev <krasimir@google.com>
Co-authored-by: UebelAndre <github@uebelandre.com>

---
## [CorvaxStation/Skyrat-tg](https://github.com/CorvaxStation/Skyrat-tg)@[39ebf7c2af...](https://github.com/CorvaxStation/Skyrat-tg/commit/39ebf7c2af41309fa4d5206f77cc4d261f47dfb7)
#### Friday 2023-05-05 07:54:22 by SkyratBot

[MIRROR] Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] [MDB IGNORE] (#20832)

* Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] (#73502)

## About The Pull Request
---

The Space Tram is currently spaced. This is a known issue with not the
map, but Trams in general. The Space Tram is a Space Tram to encourage a
fix. Until then, the Space Tram is a maint tram that's an actual hazard
but cannot directly kill anyone, including lizards. Enjoy the commodity
as you zip from secmaint to medmaint.
-------------------------------------------------------

I... really don't know if I should be proud of myself here. This whole
process has been akin to a fever dream and it has only been little over
a month since I first created the .dmm for this. What started as a
simple yet humble reimagining of Birdboat has turned into an entirely
new station, and blown past Metastation sized proportions. This has been
my most expansive project yet, and somehow it's also been my quickest.
So without further ado, I unveil Birdshot - Successor to Birdoat.

-------------------------------------------------------

**Due to recent cost expenditures on Icemoon projects, and a growing
need for orbital research stations, Nanotrasen has decided to pull
Birdboat Station out of mothball after nearly 5 years of abandonment.**

Since then, the station has seen a variety of changes at the hands of
the various vagabond lawless scum and villains that have decided to make
the abandoned station their home. Do not fret though, a Nanotrasen
Operation has secured the companies rightful property for corporate use
once again, though you'll need to be the stewards of the remaining
cleanup operation.

------------------------------------------------------

Now, as you might have guessed by now, Birdshot is heavily based on
Birdboat station. Many of the decisions here follow the original layout,
and what had to be modified or moved still tries its best to replicate
and imitate what bird being said. At least, that was the idea initially.
This has very much grown into its own beast and as such, while the main
inspiration has been Birdboat, there are a lot of new ideas thrown into
the mix that really give this station its own unique and deserving
identity. Maybe it's not perfect, but I've been inspired by @ MMMiracles
own performance with Tramstation to keep working on Birdshot and
updating it with better and improved faculties. For now, though the
station is in a playable state, and that means I'm making a PR. If I had
to borrow the words of the good MMM, I would call this **Birdshot:
Season 0**

![BirdSHOTFULL2-26-S](https://user-images.githubusercontent.com/33048583/221432760-27af1889-d2d0-4861-9435-df4258525fae.png)

See the image in more detail here: https://imgur.com/iT5Vi8k

## Why It's Good For The Game

We've been with the same 5 maps for a while now. @ san7890 jokingly said
that I could sacrifice Metastation back in November if I remade Birdboat
but modern. Obviously that wasn't going to happen, yet I was spurred on
by the idea. When I began this in earnest early this January, @ EOBGames
said that a Birdboat sized map would replace Kilostation in the
rotation. Interestingly we're not a small map anymore so I honestly have
no clue where this goes. Maybe that ephemeral 6th map slot that's been
rumored.

What I can say, is that Birdshot is wholly unlike anything else that is
currently in rotation. It's got an engineering section that feels way
too small for a station of that size, almost evocative of Cere. Cargo is
blessed with a Boutique that makes use of @ Fikou's new mannequin dolls.
Command is outfitted with a Corporate Guest Suite, and Officials sent
from Nanotrasen can embark from their ferry into the safety of their own
Corporate Dock. Elements of Cerestation are present, yet not in a way
that makes traversal annoying. Furthermore we have **2 Trams** (that I
have yet to get functional but we'll get there) on Birdshot, that's
right 2. One Security Prison Tram, and then other, a Space Tram. Both
Novel in their own ways. Departments on Birdshot twist and turn, and
there's an abundance of Maintenance Tunnels to cut through everything,
for the brave and the bold that is. And there's plenty left to discover,
but I'd rather let Birdshot speak for itself. I'm proud of this one.

If you want something new, this is something that is almost the complete
opposite of Chilled Station - Explicitly Designed to send you back to
the metal death trap that is: **Space Station 13.**

## Changelog
:cl:
add: Birdshot station has been pulled out of Mothball.
add: New station areas and places to visit. A Mix of Kilo and Delta
maints with winding shortcutting paths.
add: A host of new shuttles to support this bold endeavor to reclaim
something that really shouldn't be reclaimed.
add: Two Trams, Two Trams.
add: For the last time Bob, the gaping hole is a **feature.** Use the
breach shutters or have the virologist make starlight.
add: A smiling salute to stations past...
add: Secrets.

/:cl:

---------

Co-authored-by: Zytolg <theoriginaldash@ gmail,com>

* Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION]

* basemap

* automapper templates

* Update maps.txt

* Update _basemap.dm

---------

Co-authored-by: Zytolg <33048583+Zytolg@users.noreply.github.com>
Co-authored-by: Zytolg <theoriginaldash@ gmail,com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[d8232101e8...](https://github.com/effigy-se/effigy-se/commit/d8232101e8379211b250e5ad14566067ffc2f7db)
#### Friday 2023-05-05 08:01:48 by Rhials

Demotes Psyker Pirates to Bounty Hunter Duty (#75031)

This PR demotes the Psyker-gang from a pirate team to a fugitive hunting
team. For more information on Psyker pirates, please refer to #71650.

Stuff this also does in the process:
- Gives fugitive hunters their own subfolder in the fugitives antagonist
folder, moves some of their stuff into hunter-specific files rather than
interlacing it with the rest of the fugitive code.
- Moves the hunter backstories to defines, to make reading things easier
while I made this change.
- Exhaustively moves everything related to psykers from being
pirate-oriented to hunter-oriented (typepaths, locations where stuff is
defined, etc. There should be nothing left behind related to psykers in
anything pirate related). (Tell me if I missed anything somehow).

They still get their ship (they even get their own custom
psyker-friendly prisoner capsule). They still have a bunch of lethally
chambered firearms. They're the same gunrunning nutcases they were
before, just as bounty hunters.

To assist with basic tasks such as "getting to the station" or "figuring
out who the fuck we're supposed to be kidnapping", the psykers have
"acquired" a Seer to assist them. They can _try_ to coordinate the
psykers and lead them through situations where their impairments put
them at too great a disadvantage. If you're one of the psykers, make
sure to keep this guy alive at all costs!

Why are they called Shikaris instead of hunters? Mariam-Webster says
it's a Hindi word for some kind of hunter/tracker, and it sounded like
something a bunch of space-junkies would call themselves because they
think it sounds cool.

They now also come with a slightly different motivation, now that they
can't directly threaten the crew for money. Psyker hunters now arrive
tasked with a dirty kidnapping job, payment rendered in GORE.

Psykers aren't up to the challenge of being pirates. They're bogged down
by a number of fundamental issues that render them unable to do anything
expected of pirates. As it currently stands, they present about as much
threat as you would expect from three blind junkies with guns.

Removing them wholesale would be kind of lame. They can function as a
bunch of chaotic-neutral gun-toting space-maniacs, but for the purposes
of gameplay, keeping them as pirates would be a waste of their talents.

Moving them to a lower-stakes role not only moves them to a niche they
are more capable of filling, but gives players a more lax environment to
get a grip on playing psyker without being overwhelmed.

Giving them a seeing-eye role should bring a more unique dynamic to how
psykers are played (that is, some semblance of organization rather than
blind flailing), and should help get over the mechanical hurdles of
being a psyker until better solutions can be made. It shouldn't be too
big of an impact on balance considering the psyker gang only has three
spawns, while most hunter packs have 4+.

---
## [androiddevnotesforks/Metro-Compose](https://github.com/androiddevnotesforks/Metro-Compose)@[6ddd4e87d3...](https://github.com/androiddevnotesforks/Metro-Compose/commit/6ddd4e87d3244a2a8489ea6b0eb3e9940d146181)
#### Friday 2023-05-05 08:13:32 by Filiph Sandström

Metro: Refactor `forceTapAnimation` into `TiltIndication`

Fixes https://github.com/louis993546/Metro-Compose/issues/192.

This was a real PITA to reverse engineer and figure out thanks to the
lackluster `Indication` and `Interaction` documentation.

The API is also missing some expected features like proper rotation
so instead we have to use `android.graphics.Camera` for the actual
tilting effect.

Hopefully my pain reverse engineering `rememberRipple`& co and then
subsequent sharing of a real-world reimplementation will prevent
future generations from having to suffer the same way I have.

Y'all have been forewarned, if you choose to tread where I've tread
you'll only experience madness.

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[912e843f53...](https://github.com/Jacquerel/orbstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Friday 2023-05-05 11:39:55 by san7890

Allows Export of your Preferences JSON File (#75014)

## About The Pull Request

Hey there,

This was spoken about in #70492 (specifically
https://github.com/tgstation/tgstation/pull/70492#issuecomment-1278069607),
and I have been waiting for this to be implemented for some time. It
never got implemented, so I decided to code it myself.

Basically, **if the server host doesn't disable it**, you are free to
export your JSONs as a player, right from the stat-panel. It's a pretty
JSON on 515 versions, too!

It's right here:


![image](https://user-images.githubusercontent.com/34697715/235251447-1c977718-51fd-4025-8d89-c60bffc379ec.png)

Here's what the prettified JSON looks like on 515.


![image](https://user-images.githubusercontent.com/34697715/235321061-4a217e26-c082-4bba-b54a-2c780defda0a.png)

There's a cooldown (default to 10 seconds) between exporting your
preferences.

#### Why is this config?

It's because in the past, a server host could always just file-share the
.sav or .json or whatever to the player, but they would have to do the
explicit option of actually bothering to make the files accessible to
the player. In that same line of logic, the server operator will have to
explicitly make the files accessible. This is mostly because I'm not
sure how good `ftp()` is at being a player function and wanted to have
some sort of cap/control somehow in case an exploit vector is detected
or it's just plain spammed by bots, so we'll just leave it up to the
direct providers of this data to elect if they wish to provide the data
or not.
## Why It's Good For The Game

Players don't have to log into Server A to remember what hairstyle they
loved using when they want to swap to Server B! That's amazing actually.
I always forget what ponytail my character has, and it'll be nice to
have the hairstyle in a readily accessible place (after I prettify the
JSON for myself).

It's also more convenient for server hosts to make player data like this
accessible if they really want to, too.

If we ever add an _import_ feature in the future (which would have to be
done with a LOT of care), this will also be useful. I wouldn't advise it
though having taken a precursory look at how much goes into it while
trying to ascertain the scope of this PR.
## Changelog
:cl:
qol: The game now supports export of your preferences into a JSON file!
The verb (export-preferences) should now be available in the OOC tab of
your stat-panel if enabled by server operators.
server: Exporting player preferences is controlled by a configuration
option, 'FORBID_PREFERENCES_EXPORT'. If you do not wish to let clients
access the ftp() function to their own preferences file (probably for
bandwidth reasons?) you should uncomment this or add it to your config
somehow.
config: Server operators are also able to set the cooldown between
requests to download the JSON Preferences file via the
'SECONDS_COOLDOWN_FOR_PREFERENCES_EXPORT' config option.
/:cl:

---
## [an0rak-dev/avatar](https://github.com/an0rak-dev/avatar)@[5cf193a637...](https://github.com/an0rak-dev/avatar/commit/5cf193a63747849e0386577805810ef00ae775c9)
#### Friday 2023-05-05 11:44:30 by Sylvain Nieuwlandt

Windows Runtime support is on track.

That's cool (in all humility), that's damn cool.

I've implemented the Windows Runtime specific code (to handle a
Window creation), and I managed to do it without touching my engine.
I've added a brand new module (a separate VS project) to my solution
which use Engine/includes/platforms as includes, and then I implement
the winrt.hpp header in this module. After that, all I have to do, is
to link this new module to my Demo executable and baaam magic is done.
Now I can only change a simple #define in my Demo main.cpp to switch
between platforms. And the bonus part ? Given the fact that there's no
coupling between the module and the engine (beside the header), when
I change the #define in my Demo, it only rebuild the Demo project, not
all the solution. Fast as hell.

I remember that I didn't answer a question that's maybe you've been
asking yourself : Why the f*** did I start this project in C ?

Because I LOVE C. I mean C is a complete language, with a specification
and standard library which can be contains on a postcard, low level
mechanisms, simplicity (I mean no public/private, no template, no class
mechanisms to respect and implement...), and completely gives you the
control on what you build.

I know that most of the languages now implements security (like a memory
security). But honestly, sometime we may want to do something which is
considered as a bad code to read, but which is fast. And THAT'S
what matters for me : performance.

With C you can strictly decide how your memory bits will be arranged, how
many CPU cycles will your algorithms takes, you have control over
everything. Which means that you can fine tune your apps to really use
the full potential of a computer.

Nowdays computers have the compute power to move mountains, and still
99% of the apps on the market are as slow as sleep slugs in a blackhole
accretion disk ! Because we want to help developers create those apps.
But as a developer let me tells it : WE DON'T CARE ABOUT DEVELOPERS. We
care about users ! Do you want to eat garbage, just because it will help
the 5 Stars Chef ? No. Do you want to leave on an house with poor foundations
and walls, just because it will help the architect ? No. Same thing applies
to programs. And in my opinion, C still is the only language which can
perfectly guaranties that.
(If this subject interest you, I strongly recommand that you take a look
on https://handmade.network : a community of developers thinking the same
way and making blazing fast applications.)

Another reason why I use it, and the most important :

It's my side project. I love C. I don't plan on building a team and selling
it (yet). So I do what I want as long as I have fun.

---
## [jacobhinkle/Fuser](https://github.com/jacobhinkle/Fuser)@[9c50ae8f14...](https://github.com/jacobhinkle/Fuser/commit/9c50ae8f1441917c97ebaceb343ad6be3c54304b)
#### Friday 2023-05-05 12:12:58 by Gao, Xiang

Remove runtime out of bound check debugging util (#277)

The change in this PR is easy to understand and has low impact, but the
motivation really needs discussion and is a much more impactful thing.
And I want to use this PR to discuss it.

In https://github.com/NVIDIA/Fuser/issues/248 we agreed to add "stride
order" support to codegen, and later in today's morning meeting on
matmul, Christian talked about the idea of "allocation_domain" which is
a generalization of the idea of "stride order". Basically, we are not
married to the rFactor domain of the tensor when doing allocation and
indexing. We can pick an arbitrary vector of `IterDomain`s between root
and leaf domain, stop the indexing process on that vector, and do
allocation based on that vector. For the idea of "stride order", which
is a special case of the new idea, this vector is just the reordered
rFactor domains. This should be easily approachable with our new
indexing approach https://github.com/NVIDIA/Fuser/pull/32. This idea
does make a lot of sense, so the purpose is not to discuss whether we
want to take that idea, but how to implement that idea.

A question comes to me during implementing is, say we have a tensor
whose semantic shape is `NCHW` but stride order is `NHWC`, should the
`stride` field of the tensor be in the order of `NCHW` or `NHWC`?
Currently, we are using the same order as PyTorch, which is the semantic
order `NCHW`. I think this does make a lot of sense in terms of stride
order support. Having the stride in the semantic order is not the most
naturally way for indexing, we do need a `NHWC->NCHW` axis map to grab
the correct stride, but it is pretty simple to implement this.
Considering all factors, including consitency with PyTorch, cleanness in
the executor's code, I still think the semantics order is the best
design.

However, this design start to make no sense when we generalize the
"stride order" idea into the "allocation_domain" idea. For example, for
an `NCHW` tensor, the actual allocation can be `(H*W, N*C)`, and the
size of `contiguity` will be `2` instead of `4`. So the `Tensor::stride`
in `runtime/tensor.cu` should also be an array of size `2` instead of
`4`. The idea of "allocation_domain" requires the stride of a tensor to
be strictly one-to-one mapped to the allocation domain. As a special
case, the "stride order" idea has no choice but to follow the same
design, which is, the stride will be stored in `NHWC` order. This means,
the order of stride in our kernel is different from those in ATen, we
can not directly copy the stride. We need to permute the stride so it is
sorted descending.

But the above problem is not the biggest trouble we have, the biggest
trouble is: If we have a `NCHW` tensor allocated as `(H*W, N*C)`, is
this tensor a 4D tensor or a 2D tensor? I think the answer is "neither".
In terms of allocation and stride, it is definitely 2D, but in terms of
semantics, it is 4D. Again, in the past, we had a concept "the
dimensionality of a tensor" which is a degeneracy of two concepts "the
semantic dimensionality of a tensor" and "the allocation dimensionality
of a tensor". Now we break the symmetry, and degenerating concepts are
no longer degenerate. In codegen, we are generating a lot of tensor
shapes like `T0.shape[0]`, and I think the easiest way to handle them is
to keep `shape` in semantic dimensionality, while make `stride` in
allocation dimensionality. That said, `struct Tensor` now needs two
template arguments for dimensionalities. And unfortunately, we can no
longer do out of bound check any more.

---
## [MonikaSaradha/EDA](https://github.com/MonikaSaradha/EDA)@[379acbd218...](https://github.com/MonikaSaradha/EDA/commit/379acbd218c37147a42241a1988dd02feecafa00)
#### Friday 2023-05-05 12:38:17 by MonikaSaradha

Add files via upload

Introduction - About the data 
Dataset: New York City Airbnb dataset
Domain: Short-term rental market in NYC
Source: Kaggle (https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data)
          The New York City Airbnb dataset, is a comprehensive collection of information on Airbnb listings in New York City. This dataset includes data on more than 48,000 Airbnb listings in the city, spanning from 2010 to 2021. The dataset provides a wealth of information on each listing, including its location, price, availability, amenities, and reviews from guests. This data can be used by researchers, data scientists, and business analysts to gain insights into the Airbnb market in New York City, including trends in pricing, occupancy, and guest satisfaction. This dataset is an invaluable resource to analyze the short-term rental market in one of the world's most popular tourist destinations.
Airbnb is an online marketplace that connects people who are looking to rent their homes with people who are looking for accommodations. The platform has revolutionized the travel industry, and it is now one of the most popular ways to travel around the world. As a result, it has become essential for Airbnb hosts to optimize their listings to attract more customers and earn more money.
Problem Statement  
           The problem we are trying to solve is to help Airbnb hosts in New York City to optimize their listings to attract more customers and increase their revenue.
The primary challenge faced by Airbnb is to create a platform that offers a seamless and enjoyable experience for both hosts and guests while also maintaining trust and safety within the community.

Business Problem Statement from Airbnb NYC dataset
For Airbnb hosts located in New York City, the following are some of the specific business problems that need to be addressed:

1.	Low occupancy rates: Many Airbnb hosts struggle with low occupancy rates due to intense competition and oversupply of listings in the New York City market. They need to find ways to differentiate their properties and attract more bookings.
2.	Legal compliance: Airbnb hosts in NYC face strict regulations that limit their ability to rent out their properties, including caps on rental duration and requirements for obtaining permits and paying taxes. Hosts need to ensure that they are in compliance with all relevant laws and regulations.
3.	Pricing optimization: Setting the right price for a property is critical to maximizing profits on Airbnb. Hosts need to be able to accurately assess market demand and adjust their pricing strategies accordingly.
4.	Safety and security: Hosts need to ensure that their properties are safe and secure for guests, which includes implementing appropriate security measures and adhering to Airbnb's safety standards.
5.	Guest experience: Airbnb hosts need to provide a positive and memorable experience for guests to encourage repeat bookings and positive reviews. This includes offering exceptional hospitality, providing amenities that meet guest needs, and maintaining a high standard of cleanliness and comfort.

Objective
•	Identify the key factors that impact the price of an Airbnb listing in New York City.
•	Analyze the most popular types of listings and the neighborhoods they are located in.
•	Identify the most important amenities that guests are looking for in an Airbnb listing in New York City.
•	Analyze the popularity of different types of listings (e.g., entire home/apt, private room, shared room) in each neighborhood of New York City to determine most effective room type to offer in each location. 
•	Determine the key factors that impact the competitive pricing strategies.


Dataset Columns
•	id: Listing ID
•	name: Name of the listing
•	host_id: ID of the host
•	host_name: Name of the host
•	neighbourhood_group: The borough the property is located in (e.g., Manhattan, Brooklyn, etc.)
•	neighbourhood: The neighborhood the property is located in.
•	latitude: Latitude coordinates
•	longitude: Longitude coordinates
•	room_type: Type of room (e.g., Entire home/apt, Private room, Shared room)
•	price: Price per night in dollars
•	minimum_nights: Minimum number of nights a guest can stay
•	number_of_reviews: Number of reviews left by previous guests
•	last_review: Date of the last review
•	reviews_per_month: Number of reviews per month
•	calculated_host_listings_count: Number of listings the host has
•	availability_365: Number of days the listing is available for booking per year.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[cb1388ed9e...](https://github.com/odoo-dev/odoo/commit/cb1388ed9e64ced4e0d85cf5778192dfbdfd5995)
#### Friday 2023-05-05 13:27:08 by Jeremy Kersten

[ADD] website_cf_turnstile: add cloudflare turnstile support

This module allows to add secret key to add the turnstile captcha on
each snippet website_form.

Cloudflare Turnstile
--------------------
A friendly, free CAPTCHA replacement
Turnstile delivers frustration-free, CAPTCHA-free web experiences to
website visitors.
Turnstile stops abuse and confirms visitors are real without the data
privacy concerns or awful UX that CAPTCHAs thrust on users.

closes odoo/odoo#119246

X-original-commit: 4aca39a533e9d41f5f452f36a1ffc001f586b4f4
Signed-off-by: Jérémy Kersten <jke@odoo.com>

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[7c6e64caef...](https://github.com/RaShCat/FF-STG/commit/7c6e64caefea860c27c7f11f16d067f99a25320b)
#### Friday 2023-05-05 13:54:59 by SkyratBot

Stops station blueprints from expanding areas of non atmos adjacent turfs. [MDB IGNORE] (#20480)

* Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

* Stops station blueprints from expanding areas of non atmos adjacent turfs.

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [web-vision/wv_deepltranslate](https://github.com/web-vision/wv_deepltranslate)@[be842350fc...](https://github.com/web-vision/wv_deepltranslate/commit/be842350fc767ce7dc9eaebd7caff226467aa9aa)
#### Friday 2023-05-05 14:03:27 by Stefan Bürk

[TASK] Respect the url scheme of configured api url

In a couple of places, `https` has been hardcoded enforced
as request scheme, ignoring the scheme of the configured
api url.

This may seem to be a "security" enforcement, but these
kind of overrides are not very user friendly and hidden
magic is always a pain in the ass for debugging issues.

This change now re-uses the configured api url scheme
when building api requests. One test is adopted to do
the same.

The donated methods on the `Configuration` class to
access api url parts are used for this.

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[dd7d24e9ff...](https://github.com/EaW-Team/equestria_dev/commit/dd7d24e9ffb1751567b805532e8c6e383bafc7f3)
#### Friday 2023-05-05 14:30:31 by Mustafa Alperen Seki

Add ideology independent names for countries.

In basegame this is only used for Collab Government names, so so far only Olenia had this defined in EaW, as we don't use that puppet type anythwhere else. I was thinking of adding them regardless, my bored ass decided to finally do it.

Also grouped CHN puppet names together like SOL, NLR, and TEM ones had.

And moved PCB to basegame and EWI to griffonia file.

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[99b655dc5d...](https://github.com/cockroachdb/cockroach/commit/99b655dc5d84bf58ccf060493658a015b5cb3f21)
#### Friday 2023-05-05 14:48:35 by craig[bot]

Merge #99174 #99624 #99699 #99759 #99813 #99839 #99865 #99878

99174: sql: fix circular dependencies in views r=rharding6373 a=rharding6373

This change fixes node crashes that could happen due to stack overflow if views were created with circular dependencies.

Fixes: #98999
Epic: none
Co-authored-by: chengxiong@cockroachlabs.com

Release note (bug fix): If views are created with circular dependencies, CRDB returns the error "cyclic view dependency for relation" instead of crashing the node. This bug is present since at least 21.1.

99624: testutils: add infrastructure for reusable test fixtures r=RaduBerinde a=RaduBerinde

Certain storage-related tests/benchmarks generate fixtures and attempt to reuse them across invocations. This is important because fixtures can be large and slow to generate; but more importantly the generation is non-deterministic and we want to use the exact same fixture when comparing benchmark data.

Currently the tests achieve this by using a `.gitignore`d subdirectory inside the source tree. This does not work with bazel (which executes the test in a sandbox).

This commit addresses the issue by adding new test infrastructure for reusable fixtures. We use the user's `.cache` directory instead of the source tree (specifically $HOME/.cache/crdb-test-fixtures/...). For bazel, we make sure the path is available (and writable) in the sandbox and we pass the path to the test through an env var.

Fixes #83599.

Release note: None
Epic: none

99699: spanconfig: integrate SpanConfigBounds with the Store and KVSubscriber r=ajwerner a=arulajmani

This patch integrates `SpanConfigBounds` with the `KVSubscriber` and
`spanconfig.Store`. The `spanconfig.Store` used by the `KVSubscriber`
now has a handle to the global tenant capability state. It uses this to
clamp any secondary tenant span configs that are not in conformance
before returning them.

By default, clamping of secondary tenant span configurations is turned
off. It can be enabled using the `spanconfig.bounds.enabled` cluster
setting. The setting is hidden.

Fixes: https://github.com/cockroachdb/cockroach/issues/99689
Informs #99911

Release note: None

99759: roachtest: set lower min range_max_bytes in multitenant_distsql test r=rharding6373 a=rharding6373

The multitenant_distsql roachtest relies on a smaller range size than the new default min of range_max_bytes (64MiB) due to performance and resource limitations. We set the COCKROACH_MIN_RANGE_MAX_BYTES to allow the test to use the smaller range.

Fixes: #99626
Epic: None

Release note: None

99813: spanconfig: do not fatal in NeedsSplit and ComputeSplitKey r=irfansharif a=arulajmani

See individual commits for details. 

Fixes #97336.

99839: schemachanger: Annotate all tables if ALTER TABLE IF EXISTS on non-existent table r=Xiang-Gu a=Xiang-Gu

Previously, if table `t` does not exist, `ALTER TABLE IF EXISTS t` will only mark `t` as non-existent. This is inadequate because for stmt like `ALTER TABLE IF EXISTS t ADD FOREIGN KEY REFERENCES t_other` we will not touch `t_other` and the validation logic will later complain that `t_other` is not fully resolved nor marked as non-existent. This commit fixes it by marking all tables in this ALTER TABLE stmt as non-existent if the `t` is non-existent, so we can pass the validation.

Fixes issues discovered in #99185
Epic: None

99865: roachtest: fix query used to get job status in backup/mixed-version r=srosenberg a=renatolabs

At the moment, we only query job status in mixed-version state (so we should always use `system.jobs`). However, the code added in this commit should continue to work once we start developing 23.2, as we're checking that the cluster version is at least 23.1 before using `crdb_internal.system_jobs`.

Epic: none

Release note: None

99878: jobs: change job_info.info_key to string r=dt a=dt

Release note: none.
Epic: none.

Hopefully we get this one in now before it is released and harder to change later. I think if we go with bytes, we'll spend the next several years typing convert_to over and over, or forgetting to and then typing it, when debugging.

Co-authored-by: rharding6373 <rharding6373@users.noreply.github.com>
Co-authored-by: Radu Berinde <radu@cockroachlabs.com>
Co-authored-by: Arul Ajmani <arulajmani@gmail.com>
Co-authored-by: Xiang Gu <xiang@cockroachlabs.com>
Co-authored-by: Renato Costa <renato@cockroachlabs.com>
Co-authored-by: David Taylor <tinystatemachine@gmail.com>

---
## [archer884/annatar](https://github.com/archer884/annatar)@[7c990b8855...](https://github.com/archer884/annatar/commit/7c990b8855535d7b5f7ec77a525336a4ec2f56db)
#### Friday 2023-05-05 14:50:28 by J/A

Update CODE_OF_CONDUCT.md

Fuck you, Rust Foundation.

---
## [maryem232/Creative.AI](https://github.com/maryem232/Creative.AI)@[1e98f578b4...](https://github.com/maryem232/Creative.AI/commit/1e98f578b47fc9a148b6d45aeea5f4cdfb23c54f)
#### Friday 2023-05-05 15:33:00 by maryem232

Add files via upload


Looking to take your digital creations to the next level? Look no further than our latest project! 🔥🎨 We used the incredible power of AI to bring static images to life in a breathtaking video 🤯📹. Using the cutting-edge Deep Dream algorithm, we harnessed the power of neural networks to create a truly mesmerizing visual experience that will leave you in awe 😍. Our project showcases the limitless potential of AI and machine learning 🤖🧠, and we're thrilled to share it with the world on Github. So if you're ready to push the boundaries of digital creativity and explore the exciting possibilities of AI, be sure to check out our project and see how we're making the impossible a reality 💪🏼💻!

---
## [32th-System/deltarune_repainted](https://github.com/32th-System/deltarune_repainted)@[5d7497604d...](https://github.com/32th-System/deltarune_repainted/commit/5d7497604dd56ead9319b5522450709573237283)
#### Friday 2023-05-05 16:14:33 by Fatfuck22

cafe update

My name is Peter Griffin. I'm 44 years old. My house is in the northeast section of Quahog, on Spooner Street, and I am married to my wife Lois. I work as an employee at the Pawtucket Brewery, and I get home eventually. I don't smoke, but I occasionally go to the Drunken Clam with Joe, Quagmire, and Cleveland.

I'm in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a cold brew with Brian and listening to about twenty minutes of “Bird Is The Word” before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up with Dr. Hartman.

I'm trying to explain that I'm a family guy. I take care not to trouble myself with any enemies, except for that stupid giant chicken. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn't lose to anyone.

---
## [Tsunamico/Tsunamico-cmss13](https://github.com/Tsunamico/Tsunamico-cmss13)@[590bad4061...](https://github.com/Tsunamico/Tsunamico-cmss13/commit/590bad4061627b75b638c0f7c1fbd3cca84e43c1)
#### Friday 2023-05-05 16:22:46 by sleepynecrons

updates for landing zone sign sprites (#3180)

# About the pull request

Cleans up the palettes on the landing zone sign sprites and gives them a
fresh coat of paint (or blood). Not something most people will notice I
think but it's something I've been wanting to do.


# Explain why it's good for the game

gradients ugly


# Before and After
<details>
<summary>Click to see sprites</summary>


![osudodajs2](https://user-images.githubusercontent.com/106241650/235265980-e622b7da-8f79-4920-ba27-97d704c65550.gif)


![beforenafter](https://user-images.githubusercontent.com/106241650/235266004-0e46a574-9262-445f-98d9-4b19aa53a8fb.png)

</details>


# Changelog

:cl:
imageadd: new sprites for landing zone signs
imagedel: deleted old landing zone signs
/:cl:

---
## [strongreasons/android_kernel_asus_sdm660](https://github.com/strongreasons/android_kernel_asus_sdm660)@[2e1304fbfb...](https://github.com/strongreasons/android_kernel_asus_sdm660/commit/2e1304fbfb55878267dde11026fe61171f814e5a)
#### Friday 2023-05-05 16:32:25 by Park Ju Hyung

Introduce Lazyplug

Other hotplugging methods including mpdecision and intelli_plug focuses
on how should we turn off CPU cores. They hotplugs the individual CPU
cores based on the current load divided by thread capacity.
Lazyplug takes a whole new approach on how we should do hotplugging
based on the foundation of the other side of the coin;
“Linux’s hotplugging is very inefficient.”

Current hotplugging code on Linux is a total waste of CPU cycles and
delays, so rather than hotplugging and hurt performance & battery life,
just leaving the CPU cores on might be a better choice. This kind of
approach is spreading out more and more.
Samsung has been using this method for a very long time with big.LITTLE
devices and recent Nexus 6 firmware also does the similar thing.

Lazyplug just leaves them on, most of the time. It also tries to solve
some problems with the “Always on” approach. On situations such as video
playback, turning on all CPU cores is not battery friendly. So Lazyplug
*does* actually turns off CPU cores, but only when idle state is long
enough(to reduce the number of CPU core switchings) and when the device
has its screen off(determination is done via earlysuspend or
powersuspend because framebuffer API causes troubles on hotplugging CPU
cores).

Basic methodology :
Lazyplug uses majority of the codes from intelli_plug by faux123 to
determine when to turn off CPU cores. If the system has been idle for
(DEF_SAMPLING_MS * DEF_IDLE_COUNT)ms, it turns off the CPU cores. And if
the next poll determines 1 core isn’t enough, it fires up all CPU cores
(instead of selective CPU cores; which is the traditional intelli_plug’s
method).
Lazyplug also takes touch-screen input events to fire up CPU cores to
minimize noticeable performance degradation.
There’s also a “lazy mode” for *not* aggressively turning on CPU cores
on scenario such as video playback. For example, if you hook up
lazyplug_enter_lazy() to the video session open function, Lazyplug won’t
aggressively turn on CPU cores and tries to handle it with 1 CPU core.

* TODO :
* Dual-core mode : YouTube video playback is mostly single-threaded.
* It usually hovers around 10% ~ 30% of total CPU usage on quad-core
* device. That means 1 CPU core might not be enough to handle it, but
* also turning on all CPU cores is unnecessarily wasting power.

Signed-off-by: Park Ju Hyung <qkrwngud825@gmail.com>
Signed-off-by: Joe Maples <joe@frap129.org>
Signed-off-by: Shoaib0597 <Shoaib0595@gmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c5dce84be8...](https://github.com/tgstation/tgstation/commit/c5dce84be826ea945a11c492dce7eb2c2789548a)
#### Friday 2023-05-05 16:34:47 by Rhials

Deadchat Announcement Variety Pack 1 (#75140)

## About The Pull Request

Adds announce_to_ghosts()/notify_ghosts() calls to a bunch of different
things.

**THIS INCLUDES:**
- Powersink being activated/reaching critical (explosion) heat capacity.
- His Grace being awoken.
- Hot Potatoes being armed.
- Ascension Rituals being completed.
- Eyesnatcher victims.
- Ovens exploding as a result of the Aurora Caelus event.
- Wizard Imposter spawns.
- Rock-Paper-Scissors with death as the result of Helbital consumption.
- BSA impact sites.
- Spontaneous Appendicitis.
- The purchasing of a badass syndie balloon.
- The Supermatter beginning to delaminate.

This was everything that I could think of that would be worth announcing
to deadchat. These were all chosen with consideration to questions like
"how easy would it be to spam deadchat with this?" and "will observers
actually see the interesting thing happen, or just the aftermath?".

Not gonna lie, I've really become an observer main as of recently. Maybe
that's being reflected in my recent PRs. Who's to say? Deadchat
Announcement Variety Pack 2 will probably never come out. Sorry.
## Why It's Good For The Game

Gives deadchat a better indiciation of when/where something **REALLY
FUNNY** is about to happen. Draws attention to certain things that are
likely to gather an audience anyways, but sooner (for your viewing
pleasure). In simple terms, it helps the observers observe things
better.

Some cases, such as the aurora caelus or helbitaljanken, are occurrences
so rare that they deserve the audience.
## Changelog
:cl: Rhials
qol: Observers now recieve an alert when a powersink is activated/about
to explode.
qol: His Grace being awoken now alerts observers, to give you a
headstart on your murderbone ghost ring.
qol: Ascension Rituals being completed will also alert observers, for
basically the same reason.
qol: Arming a hot potato will now alert observers. Catch!
qol: Eyesnatcher victims will now notify observers, and invite them to
laugh at their state of misery and impotence.
qol: Observers will be notified of any acute references to The Simpsons
or other 20th Television America copyright properties.
qol: Wizard Imposter spawns alert observers, much like any other ghost
role event should.
qol: Playing Rock-Paper-Scissors with death will now alert the observers
and invite them to watch. Better not choke!
qol: Observers now get an orbit link for BSA impact sites. Why does it
keep teleporting me to the AI upload??
qol: Spontaneous Appendicitis now alerts deadchat. 
qol: The purchasing of a badass syndie balloon now alerts deadchat. You
might not be any more powerful, but at least you have an audience.
qol: When beginning to delaminate, the Supermatter will alert observers
and invite them to watch the fireworks.
/:cl:

---
## [demogorgon22/notdnethack](https://github.com/demogorgon22/notdnethack)@[bf802b3281...](https://github.com/demogorgon22/notdnethack/commit/bf802b32813f73fb2dc228ffb4ddff1d925b07f4)
#### Friday 2023-05-05 16:53:53 by chris

Elf Madman improvements

Add Carcosan courtiers
-Nymphs
-Carry Carcosan stings
-Have gold/yellow noble's equipment
-No eyes or mouths (or faces generally)
-Can't use shields (maybe secretly one-armed)
-Secretly have tentacles
--Gain tentacle attacks with high insight
--Special-cased to gain 1 die of damage per 5 insight, capping at 25 insight/"5 tentacles"
--A 5d5 wrap attack is also gained at 25 insight via the stat block
-Special-cased to gain natural AC and DR as insight increases (1/5 points, capping at 25 insight/5 total)
-50% of them flee when you're nearby (creating space for sting useage, based on m_id)
-For posterity: somewhat based on SCP-2264, somewhat on Spawn of Hastur, and somewhat on Pathfinder's Dominion of the Black

Add a black-star rapier attack for flaxen enemies
-Curses and deals percentile damage (allows resistance roll but not MR)
-Deal 5d5 bonus "unholy" damage to curse-hating targets

Add an upgrade to IEA armor that makes it light and gives +1 AC/DR
-Uses elven mithril coat
-Makes the base stats of the armor equal high elven armor
-Base category of the armor is now heavy
-Fix bugs that caused medium-ness to have priority over light-ness in calculations.
-Elves get a free skill up in broad sword and shield when opening chest
-Elves get their new god's anger molified when converting as a result of opening chest.

Tweaks
-The Suzerian doesn't have a mouth
-Flaxen starshadows use their star blades passively like Coure
-The Suzerian is unaffected by the yellow sign
-One more flaxen star shadow per "group", for 5 total
-Add 5 carcosan courtiers to spawn in Astral
-Add carcosan courtiers to minion list
-Add messages for IEA speed boots and flying armor
-The elf lord sword gains extra damage for mental stats
--Cha counts at 1/2
--Int and wis counts at 1/4 each

Bugfixes:
-Artifacts can't be consumed to upgrade IEA.
-Shopkeepers charge for and fix erroded2 while erodeproofing armor.
-Guard and ungarded set faction call (mon may have failed to be created)

---
## [Bigjango13/Burlap](https://github.com/Bigjango13/Burlap)@[75ee9fa32a...](https://github.com/Bigjango13/Burlap/commit/75ee9fa32ab78ec67875cf996ec3daea1e35de19)
#### Friday 2023-05-05 17:26:52 by Bigjango13

Fix C iterop with string args, again.

- Fix segfaults when passing string args under --release
- Fix string argument duplication
- Fix bug where C returning a bool would be inverted
- Fix bug where global variables were wiped for imports

All of this in a very very small patch, unfortunately this took me hours of mindlessly tweaking and rewriting a small part of code. Pouring over libffi and Rust `Vec`, and `CString` documentation multiple times. At one point even looking at my codes LLVM IR! I tried disabling `--release` optimization for that function with everything from assembly to `black_box` but it still wouldn't work, in frustration I added a print statment and *that* fixed it! I gave up and slapped a comment and `#[cfg(profile = "release")]` on it, I was fed up with the bug and ready to give up, when I found another bug. Passing two strings would result in two copys of the first string. Now, no println macro would fix this. So I tried some other tricks to get it to work (like changing `for arg in args {` to `for i in 0..args.len() { let arg = args.get(i).unwrap()`, which managed to fix a similar error), to no avail, I was about to give up and take a break until rust started making sense, when miraculously it worked! I hesitantly tested under `--release` and it still worked, tentatively I removed the aforementioned print hack (haha, a hack for sack, someone should make an impl called hackysack) and it worked, a little bit of cleaning up later and here I am, writing a rant on a commit smaller than the average typo change commit. Well thanks for reading and have a nice day!

---
## [SaharNaderi/Website](https://github.com/SaharNaderi/Website)@[80a571197f...](https://github.com/SaharNaderi/Website/commit/80a571197f9afaed9e7f61a6a2bdb65370dd9935)
#### Friday 2023-05-05 17:31:18 by Sahar Naderi

Create README.me

SaharCreative.uk is an innovative interior design company that prides itself on delivering creative, functional, and affordable designs that inspire and delight. Sahar, the founder of the company, has over 15 years of experience in interior design and has built a reputation for creating unique and cost-effective solutions for her clients.

Sahar's approach to design is centered around listening to her clients' needs and preferences and using her skills and knowledge to create spaces that reflect their personalities and lifestyles. She believes that every design project is unique and should be approached with creativity and a fresh perspective.

What sets Sahar apart from other interior designers is her background in tech. She is a full-stack developer with a passion for creating user-friendly and aesthetically pleasing interfaces. This unique combination of design and tech skills allows her to create innovative and inclusive tech solutions that make a real difference in people's lives.

The SaharCreative.uk website showcases Sahar's impressive portfolio of design work, highlighting her versatility and creativity. It features stunning images of her past projects, which range from transforming homes to designing community centers.

The website also features a blog, where Sahar shares her insights and perspectives on design, tech, and empowering women in business. Her blog is a valuable resource for anyone interested in design or tech, and it is a testament to Sahar's commitment to sharing her knowledge and expertise with others.

If you're looking for a talented and passionate interior designer and full-stack developer, look no further than SaharCreative.uk. Sahar is dedicated to bringing your design dreams to life and helping you create a space that reflects your unique personality and lifestyle. Contact Sahar today to learn more about her services and how she can help you transform your space into a work of art.





User

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[2345dab132...](https://github.com/TaleStation/TaleStation/commit/2345dab1326c2746a4883305e0c0db9aec294209)
#### Friday 2023-05-05 18:03:11 by TaleStationBot

[MIRROR] [MDB IGNORE] Demotes Psyker Pirates to Bounty Hunter Duty (#5644)

Original PR: https://github.com/tgstation/tgstation/pull/75031
-----
## About The Pull Request

This PR demotes the Psyker-gang from a pirate team to a fugitive hunting
team. For more information on Psyker pirates, please refer to #71650.

Stuff this also does in the process:
- Gives fugitive hunters their own subfolder in the fugitives antagonist
folder, moves some of their stuff into hunter-specific files rather than
interlacing it with the rest of the fugitive code.
- Moves the hunter backstories to defines, to make reading things easier
while I made this change.
- Exhaustively moves everything related to psykers from being
pirate-oriented to hunter-oriented (typepaths, locations where stuff is
defined, etc. There should be nothing left behind related to psykers in
anything pirate related). (Tell me if I missed anything somehow).

They still get their ship (they even get their own custom
psyker-friendly prisoner capsule). They still have a bunch of lethally
chambered firearms. They're the same gunrunning nutcases they were
before, just as bounty hunters.

To assist with basic tasks such as "getting to the station" or "figuring
out who the fuck we're supposed to be kidnapping", the psykers have
"acquired" a Seer to assist them. They can _try_ to coordinate the
psykers and lead them through situations where their impairments put
them at too great a disadvantage. If you're one of the psykers, make
sure to keep this guy alive at all costs!


![image](https://user-images.githubusercontent.com/28870487/236276276-a5e9ca00-ec62-40fe-8610-2253eec53183.png)

Why are they called Shikaris instead of hunters? Mariam-Webster says
it's a Hindi word for some kind of hunter/tracker, and it sounded like
something a bunch of space-junkies would call themselves because they
think it sounds cool.

They now also come with a slightly different motivation, now that they
can't directly threaten the crew for money. Psyker hunters now arrive
tasked with a dirty kidnapping job, payment rendered in GORE.
## Why It's Good For The Game

Psykers aren't up to the challenge of being pirates. They're bogged down
by a number of fundamental issues that render them unable to do anything
expected of pirates. As it currently stands, they present about as much
threat as you would expect from three blind junkies with guns.

Removing them wholesale would be kind of lame. They can function as a
bunch of chaotic-neutral gun-toting space-maniacs, but for the purposes
of gameplay, keeping them as pirates would be a waste of their talents.

Moving them to a lower-stakes role not only moves them to a niche they
are more capable of filling, but gives players a more lax environment to
get a grip on playing psyker without being overwhelmed.

Giving them a seeing-eye role should bring a more unique dynamic to how
psykers are played (that is, some semblance of organization rather than
blind flailing), and should help get over the mechanical hurdles of
being a psyker until better solutions can be made. It shouldn't be too
big of an impact on balance considering the psyker gang only has three
spawns, while most hunter packs have 4+.

## Changelog
:cl:
balance: Psyker Pirates are now Psyker Shikari (bounty hunters).
/:cl:

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [Masum97/compatative_programming](https://github.com/Masum97/compatative_programming)@[98512b45cc...](https://github.com/Masum97/compatative_programming/commit/98512b45cc1d75bc159eccb7f6d07ddb2f85cbc1)
#### Friday 2023-05-05 18:07:41 by Masum97

Add files via upload

One hot summer day Motu and his friend Patlu decided to buy a mango. They chose the biggest and the ripest one, in their opinion. After that the mango was weighed, and the scales showed 
 units. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Motu and Patlu are great fans of even numbers, that's why they want to divide the mango in such a way that each of the two parts weighs even number of units, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the mango in the way they want. For sure, each of them should get a part of positive weight.

 

Input :

The first (and the only) input line contains integer number 
 (1 ≤ w ≤ 1000) — the weight of the mango bought by the boys.

Output :

Print YES, if the boys can divide the mango into two parts, each of them weighing even number of units; and NO in the opposite case.

---
## [VulpiDev/vulpidev.github.io](https://github.com/VulpiDev/vulpidev.github.io)@[cda55294da...](https://github.com/VulpiDev/vulpidev.github.io/commit/cda55294dab6536d0df1feaf2505ce00ee16e875)
#### Friday 2023-05-05 21:56:25 by Pleysek

Vulpi games v. 1.0 | Realease

This is the biggest version yet (and probably will stay that way)

Added:
- Meta tags for better SEO
- Index.html content - Some more content about this whole website etc,
- Games.html content - For now no games so no bigger content, this will change in the future. Discord image is a url.
- About.html - Includes buttons for About, FAQ, Awards, other. Every button displays different text. The state you left on is saved in Local Storage (Cool, right :+1:)
- Added logos, images, discord logo, mail logo,
- Added footer, now you can see the disclaimer about copyright, contact methods and finally newsletter (which doesn't work for now but don't worry I will fix that later)
- Audios for dark/light onclick events,
- Gradient svg for the baner in index.html why: because it looks COOL!
- Changelog png for index.html content
- Darkmode.js for remembering chosen option (dark/light theme) and changing the theme that overrides system preference without dark theme my eyes would turn red, well that is a good thing :)
- Discord logos, for discord invites urls.
- email icons, for email stuff.
- game jpg for index.html content,
- GameC jpg - cropped version of game jpg, so the bigger resolutions is better looking.
- icon png is the icon of Vulpi Game website.
- lightOff svg is a half-moon icon for dark theme option,
- lightOn svg is a sun icon for a light theme option,
- lightOn-sunin svg is a other variation of ligth on svg.
- logoico svg is used in the icon of a websitem
- logotext svg is the 'VULPI' text in logo,
- scripts js is some weird file that just does some things, So it changes text in about.html when a button is pressed, hides and shows stuff when a picture is hovered by mouse in index.html, and finally when you click email icon in the footer it copies contact-email to clipboard, litterally nothing sketchy. You can check it bruh.
- styles css - I will be hones with you, I'm deply sorry for anyone who wants to read this, This is painfully bad, Probably should fix this. Its a lot of mess :|

---
## [AIStream-Peelout/flow-forecast](https://github.com/AIStream-Peelout/flow-forecast)@[728c49257a...](https://github.com/AIStream-Peelout/flow-forecast/commit/728c49257a3dde1d427921ac2a9d1f94f50261c4)
#### Friday 2023-05-05 23:10:39 by isaacmg

annoying gh 1

I hate these asshole roofers that my apartment brought out here they are making life miserable.

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[152729ffda...](https://github.com/Jolly-66/JollyStation/commit/152729ffda8aa428047b51fc648ac221cc3a4ca4)
#### Friday 2023-05-05 23:33:59 by TaleStationBot

[MIRROR] [MDB IGNORE] Minerals have been refactored so costs and minerals in items are now in terms of mineral defines. (#5615)

Original PR: https://github.com/tgstation/tgstation/pull/75052
-----
## About The Pull Request

Ladies, Gentlemen, Gamers. You're probably wondering why I've called you
all here (through the automatic reviewer request system). So, mineral
balance! Mineral balance is less a balance and more of a nervous white
dude juggling spinning plates on a high-wire on his first day. The fact
it hasn't failed after going on this long is a miracle in and of itself.

This PR does not change mineral balance. What this does is moves over
every individual cost, both in crafting recipes attached to an object
over to a define based system. We have 3 defines:

`sheet_material_amount=2000` . Stock standard mineral sheet. This being
our central mineral unit, this is used for all costs 2000+.
`half_sheet_material_amount=1000` . Same as above, but using iron rods
as our inbetween for costs of 1000-1999.
`small_material_amount=100` . This hits 1-999. This covers... a
startlingly large amount of the codebase. It's feast or famine out here
in terms of mineral costs as a result, items are either sheets upon
sheets, or some fraction of small mats.

Shout out to riot darts for being the worst material cost in the game. I
will not elaborate.

Regardless, this has no functional change, but it sets the groundwork
for making future changes to material costs much, MUCH easier, and moves
over to a single, standardized set of units to help enforce coding
standards on new items, and will bring up lots of uncomfortable balance
questions down the line.

For now though, this serves as some rough boundaries on how items costs
are related, and will make adjusting these values easier going forward.

Except for foam darts.

I did round up foam darts.

## Why It's Good For The Game

Adjusting mineral balance on the macro scale will be as simple as
changing the aforementioned mineral defines, where the alternative is a
rats nest of magic number defines. ~~No seriously, 11.25 iron for a foam
dart are you kidding me what is the POINT WHY NOT JUST MAKE IT 11~~

Items individual numbers have not been adjusted yet, but we can
standardize how the conversation can be held and actually GET SOMEWHERE
on material balance as opposed to throwing our hands up or ignoring it
for another 10 years.

## Changelog
:cl:
refactor: Mineral costs have been reformatted to be scaled by the number
of sheets, darts, and small fractions they make up.
qol: Foam darts no longer hold a fraction of a unit of iron within
themselves.
/:cl:

---------

Co-authored-by: ArcaneMusic <41715314+ArcaneMusic@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Mister-moon1/cmss13](https://github.com/Mister-moon1/cmss13)@[34daca112c...](https://github.com/Mister-moon1/cmss13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Friday 2023-05-05 23:37:59 by Segrain

Fix for varediting bitflags. (#2735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

I am honestly at a loss as to what is happening here. I do not speak
HTML all too well, and at cursory reading buttons _should_ be returning
their value, which is `1`, `2` and so on. But on debugging, they
actually return their text (`Save`, `Cancel`), which does not proceed to
work with the code receiving it. Changed that code accordingly, and then
edited the values for good measure in case somebody better versed in
HTML would get a heart attack from my folly.

Also, this looks ugly to me. Which button is which flag here?

![image](https://user-images.githubusercontent.com/4447185/221438285-cdb380c2-a871-4620-be04-0b3c5027501f.png)

This, in my humble opinion, is easier to read (would actually look
better outside of local server messing fancy windows as is its wont):

![image](https://user-images.githubusercontent.com/4447185/221438302-660c5976-d0e2-44fa-a18a-9f73a229f2c4.png)
In the process, I confess, my HTML illiteracy broke a little something
again. But we are not actually _using_ `slidecolor`, so hopefully it is
not actually important.

# Explain why it's good for the game

Is fix.


# Testing Photographs and Procedure
See above.

# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
admin: Editing bitflag variables actually works now.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Potato286/Structures_and_Things_1.19.2](https://github.com/Potato286/Structures_and_Things_1.19.2)@[c529307b02...](https://github.com/Potato286/Structures_and_Things_1.19.2/commit/c529307b028ca15b3931173901707377661dd7da)
#### Friday 2023-05-05 23:41:10 by Potato286

You got away again
You must think you're so clever
I promise you agent
Can't escape me forever
We're playing a game
You take from me, I take from you
But every game ends
And when this one is through

[Chorus]
I expect you to die
(The best of the best, you'll die like the rest)
I expect you to die
I expect you to die
When you finally see the worst side of me
We'll finally be eye to eye
I expect you to die

[Verse 2]
That voice in your ear
They've no chance to save you
A mere puppeteer
They only enslave you
You're a piece on a board
I bet with my wealth my armies and dreams
Your every success unveils still greater schemes
A lake full of acid, a drill from the sky
If you try to fight me, we'll watch your hopes die
Lasers and saw blades with sharks on standby
You're right where I want you
And this is goodbye
You might also like
The Spy and the Liar
Schell Games
Opening Credits
Jared Emerson-Johnson
Around You
Kate Reinders & Derek Hough
[Chorus]
I expect you to die
(The best of the best, you'll die like the rest)
I expect you to die
I expect you to die
When you finally see the worst side of me
We'll finally be eye to eye
I expect you to die

---

