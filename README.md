## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-11](docs/good-messages/2023/2023-02-11.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,832,092 were push events containing 2,594,402 commit messages that amount to 169,759,909 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 44 messages:


## [Malii47/GucluSarp](https://github.com/Malii47/GucluSarp)@[5fe18d7bae...](https://github.com/Malii47/GucluSarp/commit/5fe18d7bae923b2af9922279ff9c701a14fde36d)
#### Saturday 2023-02-11 00:04:22 by FangeLLL

ENORMOUS FIX UPDATE

- Fixed an issue that when you shake that juicy ass camera, Pivot will be fucked up.
- Fixed an issue that blood splash z axis suck enormous gorilla's dick.
- Player Rotation algorithm has been reworked.
- Fixed an issue that i am gonna fuck this stupid ass problems.

---
## [mrled/psyops](https://github.com/mrled/psyops)@[d30b39576e...](https://github.com/mrled/psyops/commit/d30b39576eedc19c96cd8cf6c5a4c67bd0fc7953)
#### Saturday 2023-02-11 00:12:30 by Micah R Ledbetter

Use correct postgres-password name

Fuck you to the docs that use both ways

---
## [fidelity/kibana](https://github.com/fidelity/kibana)@[43fa5174f8...](https://github.com/fidelity/kibana/commit/43fa5174f813ce7999dbc65b71cbb9ba0168fb1d)
#### Saturday 2023-02-11 00:52:32 by Clint Andrew Hall

[kibana] Thank you for everything, Spencer! 🧔🏻‍♂️ (#150759)

## Summary

> _Inspired by @kertal, and extracted from his PR
https://github.com/elastic/kibana/pull/150660, specifically
@thomasneirynck's
[proposal](https://github.com/elastic/kibana/pull/150660/files#r1101795511)._
>
> _Holding for 24 hours, for our friends in later time zones._

Several of us felt a dev-only easter egg-- where, if you're lucky,
@spalger joins you as you test your latest feature-- would be a fun
tribute as he leaves us for new and exciting opportunities.

Elasticians, feel free to send your love to @spalger in the channel of
your choice, of course, but we'd appreciate your review of this pull
request. ❤️


![image](https://user-images.githubusercontent.com/1178348/217867285-b23dcf1f-1a4a-45fd-b828-f6b24215fef2.png)

---------

Co-authored-by: spalger <spencer@elastic.co>

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[eb4886c115...](https://github.com/PhantomEpicness/cmss13/commit/eb4886c115a0965a347783b87eb3415f098c2c1f)
#### Saturday 2023-02-11 01:21:28 by carlarctg

Spitter Rework (#1541)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Design doc:

https://hackmd.io/@waltuh/Sy0A1SnEo
Slightly inaccurate as my brainworms enticed me to change and add mini
features.

Approved by Walter, ignorepproved by Gevonius and Satanbatros


https://cdn.discordapp.com/attachments/280051925154660363/1041475609165045770/image.png

Changes:
- Spit doesn't spatter by default, instead it's now a faster, weak
7-tile* projectile that deals 20 damage with a faster spit cooldown.
Fully accurate at 6 tiles, inaccurate at 7 tiles but can sometimes hit.
- Frenzy replaced with 'charge spit'. Halved speed buff, added +5 armor
buff, the next spit will deal 10 more damage and coat humans in acid but
have only 5* tiles of range.
- Acid spray halves damage every time someone walks on it. However, its
damage is spread over legs and feet, and if someone who is spattered
with acid is hit by it, their acid spatter will be strengthened, dealing
more damage, lasting longer, and needing two rolls to clear up. Also,
the bonus damage didn't actually work, now it does.

* Projectile range code is SHIIIT and breaks on diagonals so the range
variable is increased.

Also, queen acid spit spatters and has 1 second less extra cooldown
because find and replace caused it and I didn't think it was a change
worth removing. It's neat, maybe they'll actually use it now.

Added support for balloonchat colors. (Even TG doesn't have this, we're
awesome now!)

Renamed vision_distance parameter to max_distance so it's similar to
visible_message

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

As stated in the hackmd, spitter is very ineffective without using the
oversight-exploit infinite acid spray spam, and its combo (acid spatter
into spray) does not actually help, as the stun stops the human from
getting further hit by the spray and the bonus damage does not actually
apply thanks to shitcode. This PR makes it so that the combo is indeed
more effective than making humans walk into the spray.

Again as stated, spitter suffers from a strange issue where it's
actually not good at harassing from range despite that being its
purpose, since it has a low range. By letting it be long ranged by
default and choose to go short range, it adds a lot of depth and
versatility and lets it actually harass marines.

As always they can just. Shoot it to make it go away. 

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
refactor: Added support for balloonchat colors. (Even TG doesn't have
this, we're awesome now!)
add: Spitter rework!
add: Spit is now full screen range but weaker.
add: Frenzy is renamed and causes spit to inflict spatter coating.
add: Acid spray's damage is halved every time it hits a human, but if it
hits someone coated in acid it will enhance it, making it more dangerous
and need two rolls to shake off.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [Dreadmoth/pcsx2](https://github.com/Dreadmoth/pcsx2)@[87abacc632...](https://github.com/Dreadmoth/pcsx2/commit/87abacc63264f9cf554cddf02973e0fc9cd2af77)
#### Saturday 2023-02-11 01:49:40 by RedDevilus

GameDB: Fix multiple games + maintenance

- Area 51: Half Pixel Normal vertex for lighting and other places
- Shrek 2: Basic mipmapping which kinda half fixes the sun missing
- Galaxy Angel II: Normal vertex which reduces misalignment
- Forgotten Realms - Demon Stone: Clamping Mode extra + preserve which will solve the occasional SPS + missing demo entry.
- Spyro Dawn of dragon: SW clut + sprite which doesn't make you vomit from the overbloomification and looks similar to the software renderer
- Castlevania Curse of darkness half sprite which will enlarge the font similar to software renderer + some missing fixes that were available on the Europe and America versions but not Japanese.
- Drakengard 1 + 2 (Also know as Drag-on Dragoon) : Partial (no hashcache) to avoid slow transitions and other areas. Adds missing Japanese Drakengard 1
- Urban reign: Partial texture preloading to fix performance issues in the gameplay
- Onimusha Warlord: Partial preloading to fix performance issues
- Sniper Elite: Fix sky lighting
- Maintenance that add spaces in the titles for Disc1of1 to Disc 1 of 1 and more...

---
## [bobhy/nushell](https://github.com/bobhy/nushell)@[3d65fd7cc4...](https://github.com/bobhy/nushell/commit/3d65fd7cc4f6e0db0c1c31b895feabf2be66cb0a)
#### Saturday 2023-02-11 02:09:32 by Doru

Expose filtering by file type in glob (#7834)

# Description

Add flags for filtering the output of `glob` by file type. I find myself
occasionally wanting to do this, and getting a file's
[file_type](https://docs.rs/wax/latest/wax/struct.WalkEntry.html#method.file_type)
is presumably fast to do as it doesn't have to go through the fallible
metadata method.

The design of the signature does concern me; it's not as readable as a
filter or "include" type list would be. They have to be filtered one by
one, which can be annoying if you only want files `-D -S`, or only want
folders `-F -S`, or only want symlinks `--butwhy?`. I considered
SyntaxShape::Keyword for this but I'll just defer to comments on this PR
if they pop up.

I'd also like to bring up performance since including these flags
technically incurs a `.filter` penalty on all glob calls, which could be
optimized out if we added a branch for the no-filters case. But in
reality I'd expect the file system to be the bottleneck and the flags to
be pretty branch predictor friendly, so eh

# User-Facing Changes
Three new flags when using `glob` and a slightly more cluttered help
page. No breaking changes, I hope.

# Tests + Formatting

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[b4954e1402...](https://github.com/cmss13-devs/cmss13/commit/b4954e14028909b107d0b204da0ad06c5dfeb50a)
#### Saturday 2023-02-11 02:18:56 by carlarctg

zombie powder fix (#2315)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Fixes Zombie Powder bugging the fuck out by slapping a ton of FAKEDEATH
checks everywhere. It now properly shows the holder as dead on HUDs and
scans.

Fixed an issue in which sometimes qdeleted reagents still procced on
life.

Fixed examining things changing your direction if you're incapacitated.

Added FAKEDEATH to the mob_incapacitated() check.


# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


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
fix: Fixes Zombie Powder bugging the fuck out by slapping a ton of
FAKEDEATH checks everywhere. It now properly shows the holder as dead on
HUDs and scans.
fix: Fixed an issue in which sometimes qdeleted reagents still procced
on life.
fix: Fixed examining things changing your direction if you're
incapacitated.
fix: Added FAKEDEATH to the mob_incapacitated() check.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[144ab26e93...](https://github.com/treckstar/yolo-octo-hipster/commit/144ab26e93a92250546cf1c75dd373bca784c58d)
#### Saturday 2023-02-11 02:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [OlayColay/UC_Love](https://github.com/OlayColay/UC_Love)@[763361d55a...](https://github.com/OlayColay/UC_Love/commit/763361d55ac4ee782401512452806ece40618296)
#### Saturday 2023-02-11 03:45:55 by kiwinana12

Some dialogue changes, Cameo Sprites, and UCH Encounter, 1/2 UCSC, Riviera mentions Mercedes, HOLY SHIT RIVIERA'S DIALOGUE WAS UNFINISHED???? IM AN IDIOT (I hope Cole's future employers or my future employers don't look through my Github and see this update if you did no you didn't)

removed piss, quality of life

---
## [Signal-K/client](https://github.com/Signal-K/client)@[69497a1500...](https://github.com/Signal-K/client/commit/69497a1500e3ec2237555d07581ab4cd40880de2)
#### Saturday 2023-02-11 03:46:12 by Liam Arbuckle

🪁🥎 ↝ #8 Add file upload feature & auth handler

1. Completed authentication header for web client. To the end user it is 100% offchain, with user profiles being stored on a postgresql database. However, I've taken a dive into the Magic sdk to create wallet addresses for each user, as well as a Flask-based authentication handler for future metamask/wallet interaction. I've made this decision for a few reasons (like simplicity), but the main reason is for the client to seem like a regular journal platform and not be confusing, as well as follow the 'web3-agnostic' design language I favour for projects like this due to confusion and/or distrust of web3 products/teams. However, since each user will have a wallet address, they'll be able to interact with smart contracts and IPFS just fine. Further discussion will need to take place to discuss long-term suitability of this model, including things like gas fees (currently everything regarding transactions is occurring on Goerli [testnet] and gas fees will be processed by a "superuser" so that there's no restrictions or huge expenses) and how we go about getting users to trust the web3 nature (which I've got a lot of experience with). However, I don't fully know the exact demographics we'll be targeting & also I understand that that's quite a while away, so I'll raise it now but won't spend any time thinking about it until the time comes
          2. I've continued with the contracts for proposals/publications & updating the metadata standards. I favour a lazy minting approach with data processing being handled by a Flask blueprint (which is a formula my team have developed on signal-k/sytizen). Right now I'm using Thirdweb & Moralis for the contract interactions and I have also, with much difficulty, succeeded in getting Moralis to self-host on my Postgres server. Finally, I've begun the process of optimising the base layer contracts so that the gas fees (which are already reduced post-merge) are essentially negligible at this time.
          3. File upload for posts/articles feature on the web client is complete, and the smart contracts now receive all file upload metadata from this.
          4. Begun a new flask blueprint (forked from point #2) to generate dataset previews based on which modules (e.g. lightkurve) are used and to add interactive nature to the 'sandbox' feature discussed earlier
          5. Reluctantly continued some documentation

(above message from the Desci discord, see https://github.com/signal-k/sytizen/issues/16 for more info)

---
## [MichaelDeBoey/next.js](https://github.com/MichaelDeBoey/next.js)@[268dd6e80b...](https://github.com/MichaelDeBoey/next.js/commit/268dd6e80bb4e17096c0e75da94cf4de0b809697)
#### Saturday 2023-02-11 05:01:15 by José Fernando Höwer Barbosa

Simplify with-google-analytics example (#43894)

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->
## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm build && pnpm lint`
- [x] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

First of all thanks for this amazing project and all the help you
provide with these examples.

It seems there is code duplication in this example. After some tests
locally seem to _document.js is not necessary for `gtag` to work
properly.


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_app.js#L30-L34


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_document.js#L13-L17

I am aware of https://github.com/vercel/next.js/pull/40645 and I would
like to ask @dave-hay, @SukkaW and @ijjk to consider this is still
necessary. If so why then not move all content of the scripts from _app
to _document?

In any case, I am open to adding here some comments explaining what is
the reason for this code duplication if necessary.

<hr/>

Changes that come from  https://github.com/vercel/next.js/pull/43897

1. The `event` hashChangeComplete should be removed since `/home` and
`/home/#section` is not new pageview, but just reference to the same
page.

If we go from /home to /home/#section (with a button click or a link for
example) this shouldn't trigger a new page visit on `gtag`.

For this reason, I think we should revert the changes from
https://github.com/vercel/next.js/pull/36079. If there is a better
argument of why this should stay I am also open to creating comments to
clarify this on the example since I don't think should be the default
behavior and not useful in most cases.

2. The `id="gtag-init"` was added with no context to the example from
https://github.com/vercel/next.js/pull/29530

If there is a reason for this id in the script to existing I am open to
adding a comment that clarifies this since in my experience is not
necessary at all.


Edit: Batching with https://github.com/vercel/next.js/pull/43897 as
recommended by
https://github.com/vercel/next.js/pull/43897#issuecomment-1344635000

---------

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[a437acf196...](https://github.com/git-for-windows/git/commit/a437acf19600aee5e8bcaa719890181f619c008f)
#### Saturday 2023-02-11 06:15:14 by Johannes Schindelin

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
## [SecurityLab-CodeAnalysis/odoo_odoo](https://github.com/SecurityLab-CodeAnalysis/odoo_odoo)@[97f52bd40d...](https://github.com/SecurityLab-CodeAnalysis/odoo_odoo/commit/97f52bd40d97109a7983549d252476959ddceada)
#### Saturday 2023-02-11 06:38:18 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

Part-of: odoo/odoo#109640

---
## [BasixKOR/react-native-reanimated](https://github.com/BasixKOR/react-native-reanimated)@[b83625045f...](https://github.com/BasixKOR/react-native-reanimated/commit/b83625045f314e498fe32adc34b43ce20a77f946)
#### Saturday 2023-02-11 07:16:43 by Angelika Serwa

Fix reloading when using useAnimatedKeyboard (#3932)

<!-- Thanks for submitting a pull request! We appreciate you spending
the time to work on these changes. Please follow the template so that
the reviewers can easily understand what the code changes affect. -->

## Summary

Fixes
https://github.com/software-mansion/react-native-reanimated/issues/3786

### Why it crashes: 
On the main thread `CADisplayLink` calls `updateKeyboardFrame` 60 times
per second. Calling `updateKeyboardFrame` calls listener on the JS side.
When reloading the runtime gets destroyed on the JavaScript thread. So
when those two things happen at the same time (which in this case
happens often) we get the crash that we're trying to call a js function
on destroyed js runtime.

### Why don't you just remove the listeners in
`NativeReanimatedModule::~NativeReanimatedModule()`, we're cleaning up
everything here:
I've tried and it appeared to work at first but I still got crashes when
running [the 1000 listeners
example](https://github.com/software-mansion/react-native-reanimated/pull/3911)
and probably that's why:

![Screenshot 2023-01-11 at 23 02
18](https://user-images.githubusercontent.com/6280457/211935579-16ff642d-fb15-469b-909e-e36ba9d72781.png)
![Screenshot 2023-01-11 at 23 02
35](https://user-images.githubusercontent.com/6280457/211935599-88cb9e81-20d7-4f96-bfd0-9c3b5da13b24.png)

So when `~NativeReanimatedModule` is being called the runtime related
stuff is already deleted and there is a short window of time that the
runtime is being deleted and we still call js stuff, or at least that's
my theory 🤷‍♀️

So my proposition for now is to listen for
`RCTBridgeDidInvalidateModulesNotification` notification. It's called
just before deleting happens. Also I'm using
`RCTUnsafeExecuteOnMainQueueSync` because I want to wait until the
listeners are completely deleted on the main thread and then delete js
stuff.

### A nicer solution? 
If you look a bit above `[[NSNotificationCenter defaultCenter]
postNotificationName:RCTBridgeDidInvalidateModulesNotification` line in
React code you'll see that React calls `invalidate` on all modules' data
before even posting the notification. Maybe we should clean reanimated
stuff here. I haven't explored that though yet and I don't know where is
reanimated's module data and what is module data at all and where to put
that `invalidate` function, I just got this idea while posting this PR.

## Test plan

Just run AnimatedKeyboardExample and reload the app.
Also the [the 1000 listeners
example](https://github.com/software-mansion/react-native-reanimated/pull/3911)
nicely catches other data races.

Tested with changes from
https://github.com/software-mansion/react-native-reanimated/pull/3911
and it works
Also tested on FabricExample and surprisingly it also works.

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[91f06a97d3...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Saturday 2023-02-11 07:36:49 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[d95ca04819...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Saturday 2023-02-11 07:36:49 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[06a7e74790...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/06a7e74790b3b05b7f4fb522ff55858ef0d66418)
#### Saturday 2023-02-11 09:01:29 by Unit2E

Changes the hypno flash to work on unconscious people (#73025)

## About The Pull Request

The hypno flash is a really fun and flavourful item that is both strong
while allowing for gimmicks. However, personally, I've always been a bit
confused as to what counted for hypnosis, until looking into the
specifics. I also know that I'm probably not alone in this, because
various people have told me over the years that sleep doesn't work,
while it definitely does. This PR hopes to change this by somewhat
buffing the hypno flash, by making unconsciousness work for hypnosis.

## Why It's Good For The Game

Unconsciousness looks very similar to sleep, and in a lot of cases it is
really just the same effect... except for hypnosis, where there is no
effect on unconscious people. Personally, I don't think this is the best
UX and it limits the options there are for hypnotising people, which is
a shame, as I think it's very interesting. This may or may not be too
strong (think using the hypno flash with the micro-laser), but I still
think this is preferable to only working with sleep specifically or
hypnosis, might warrant a TC up if people otherwise agree with the
change. Also, just to note, unconsciousness is also still separate from
crit. This does not let you hypnotise people for free because they're in
crit.

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[a155df74a0...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/a155df74a09c075efe1339cd1cd24e5cc189fc12)
#### Saturday 2023-02-11 09:01:29 by Rhials

Abductor scientist self-retrieve failure/runtime fix (#73172)

## About The Pull Request

Since the abductor outfit/implant would load before the abductor ship
(and it's teleport pad) when first generating a team, a runtime would
occur when trying to link the pad to the implant. Another would occur
every time you attempted to retrieve yourself (as the linked pad would
be null), preventing recall and completely neutering an abductor team's
most important maneuver.

Now, using the implant will perform the linking process again if no
linked pad is found, and provides the owner with a warning if (by some
great calamity) they genuinely have no pad to teleport back to. This
solves the issue of the implant sometimes not linking to a pad properly
on initialize, and makes them way less prone to breaking.

Apparently this has been broken for a while, presumably since the
abductor ship was made into a lazyloading template.
## Why It's Good For The Game

The funny silly grey men get to torture the poor hapless crew once
again.
## Changelog
:cl:
fix: abductor scientist's retrieval implants will now properly recall
the owner, and inform them upon recall failure.
/:cl:

---
## [nevimer/Skyrat-tg](https://github.com/nevimer/Skyrat-tg)@[a57b142c1a...](https://github.com/nevimer/Skyrat-tg/commit/a57b142c1a4949ded1dcde1157ccf789fb21aabd)
#### Saturday 2023-02-11 09:01:46 by SkyratBot

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
## [ongood/odoo](https://github.com/ongood/odoo)@[639cfc76ba...](https://github.com/ongood/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Saturday 2023-02-11 09:15:19 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#109812

Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [stax132349/Fedoraware](https://github.com/stax132349/Fedoraware)@[58d6b8fbbc...](https://github.com/stax132349/Fedoraware/commit/58d6b8fbbc2dbd3914119b09fac2aa83f9b4edd0)
#### Saturday 2023-02-11 11:08:02 by stax

Revert bithacking bullshit

this shit sucks, just get rid of it and bring back normal system

---
## [projects-nexus/nexus_kernel_xiaomi_lavender](https://github.com/projects-nexus/nexus_kernel_xiaomi_lavender)@[9ae6496f9d...](https://github.com/projects-nexus/nexus_kernel_xiaomi_lavender/commit/9ae6496f9d6d8ed152585c49818bf11b8b56f1ba)
#### Saturday 2023-02-11 11:31:15 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: ImPrashantt <prashant33968@gmail.com>

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[1fe9efd00a...](https://github.com/OrionTheFox/Skyrat-tg/commit/1fe9efd00aeb0e2d4f4dedf89460abacecef9d1b)
#### Saturday 2023-02-11 12:12:32 by SkyratBot

[MIRROR] Rebuilds Luxury Shuttle (mostly), makes it emag-only [MDB IGNORE] (#19229)

* Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

## About The Pull Request
![2023 02 07-06 49
54](https://user-images.githubusercontent.com/70376633/217159751-790e6ded-8525-4d13-a5b5-6a3d8076a00e.png)
Changes the really goofy old lux shuttle to a cooler layout with some
additions to make it a luxury and not just
"anti-poor-people protection + food"

Shuttle was made bigger to make it less cramped for the luxury class,
pool was moved to its own room, added an arcade
and a bar corner, has real lasers to shoot poors with (20c each shot),
has fire extinguishers now
Adds a new preopen variant of hardened shutters
Adds a paywall pin subtype for the luxury shuttle, and a laser gun
subtype

Made emag-only at a price of 10000 credits
## Why It's Good For The Game

The old luxury shuttle looked REALLY awful with its pool, was pretty
cramped even in the luxury section and BARELY resembled a luxury..
This luxury shuttle provides luxuries such as a less poorly designed
pool, more space for legs, arcade, to make it resemble a luxury unlike
the old one

## Changelog
:cl:
add: Luxury Shuttle is now bigger, and less ugly! Poor people still get
it rough though...
/:cl:

* Rebuilds Luxury Shuttle (mostly), makes it emag-only

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a7a2870031...](https://github.com/treckstar/yolo-octo-hipster/commit/a7a28700310e9aa06663188b381b041b83ad5a91)
#### Saturday 2023-02-11 12:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[aea86f24d9...](https://github.com/mrakgr/The-Spiral-Language/commit/aea86f24d9fd54cac1a8c67de8e93ec8e1f6cf79)
#### Saturday 2023-02-11 12:22:12 by Marko Grdinić

"9:40am. I am up. No emails, as expected. Will I really get any replies at all from the companies I tried?

https://boards.4channel.org/a/thread/248801559/what-are-the-most-universally-moving-anime-osts

Well, who cares. I'll take care of it later. Right now I need to master webdev. Once I have a tech under my belt, I'll pursue jobs more aggressively. Right now the market is depressed anyway.

Let me do my morning reading and then I will resume from yesterday.

During the night I started obsessing about Hopac. I tried to get rid of it, but that just made it clear once again, just how much Hopac offers me. I have no idea how I would have made the Spiral lang server without it.

https://youtu.be/EPXMEXtClNo
The Disappearance of Haruhi Suzumiya OST - Suzumiya Haruhi no Tegakari

Though I've read the novels over a decade ago, I've never watched the anime. This OST track is godly.

https://mangadex.org/title/a4304d3b-191d-471f-8c78-353d403a35d0/sengoku-komachi-kuroutan-noukou-giga

This one is always a fun read. Let me read the latest chapter and I will resume the Elmish book.

10:05am. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/elmish-hackernews

Let me finally start. Yeah, this is fine. This kind of pace is my usual programming one. I am not worried about writing or view counts. It is really a pity that none cares about Heaven's Key enough to support it.

At this rate who knows whether there will be another sequel to Simulacrum. Or whether I will ever finish Heaven's Key. But that is fine.

It is really difficult for me attain a mindset of a working man. What I am doing here, in complete freedom is more akin to being an artist.

I am going to try to make Youtube work in that case.

10:10am. Focus me. Stop swirling around concurrent lang server code in your head? Are you going to dive into Spiral internals and hack around?

Of course not. Then why bother thinking about a solved problem. Focus on the future problem, not what has been solved.

In the future, forget big projects. What I need are small and elegant projects.

10:15am. Stop wondering how Hopac promises are canceled in choices. It does not matter. It is not worth the time it would take to figure this out. Should I need to, I can always figure it out later. Forget it for now.

10:25am. I am distracted. I need to tap into the inner power that I have.

10:40am. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/elmish-hackernews-part1

I am not really paying attention to this, instead I am thinking about Hopac.

But it does not matter. These parts are implementation heavy, and I got the gist of it. Let me just move forward. I need to work towards finishing the book.

10:50am. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/commands/elmish-hackernews-part3

I admit I used to dislike webdev before I knew anything about it.

> Previously on the Elmish Hackernews application we have using the function loadStoryItems to retrieve and parse the items from the Hackernews API. However, hypothetical users of the application are complaining: they say that it takes a long time before any useful information is presented on screen. After diagnosing the problem, we figured out that for some story items, the network latency is longer than 10 seconds. Even though other items might have already been loaded, the application is waiting for all of the items to be loaded before it can show anything on screen.

> After a review of the code, we concluded that the root of this "problem" is the Async.Parallel function that is combining all of the asynchronous operations to load story items into a single asynchronous operation and awaiting them until every one of them has been loaded before returning the result.

But now I see that it is all about concurrent programming, and this kind of job suits me just fine.

11:10am. https://www.semianalysis.com/p/the-inference-cost-of-search-disruption
> Disruption and innovation in search don’t come for free. The costs to train an LLM, as we detailed here, are high. More importantly, inference costs far exceed training costs when deploying a model at any reasonable scale. In fact, the costs to inference ChatGPT exceed the training costs on a weekly basis. If ChatGPT-like LLMs are deployed into search, that represents a direct transfer of $30 billion of Google’s profit into the hands of the picks and shovels of the computing industry.

I love this blog.

> We’re excited to announce the new Bing is running on a new, next-generation OpenAI large language model that is more powerful than ChatGPT and customized specifically for search. It takes key learnings and advancements from ChatGPT and GPT-3.5 – and it is even faster, more accurate and more capable.

I had no idea about this.

...Forget this article for now, let me get back to the Elmish book. I am 80% done with it.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/pages-as-programs

> Web pages as programs

I need that mindset. Who is going to go into ML? You need money for that. Instead what I should have been aiming at artsy part of programming which is making web apps.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/splitting-programs

This is worth paying attention to.

11:25am. Come to think of it, when am I going to get an invite to the F# slack?

11:35am. I have no idea. Maybe I need to be a sustaining member. I might ask on the F# reddit later.

> At this point, you must be thinking: "Zaid, why are we going through this simple stuff, we have seen this before! Just get to the composition techniques already." The thing is, I want to show you that composing larger programs or in this case, splitting a bigger program into smaller ones, naturally arises from refactoring the common parts into separate type definitions and separate functions that handle these types. Let us try to refactor the counter view and text input view such that the implementation of either views is entirely separate from one another.

Focus on the Elmish book.

11:50am. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/integrating-commands

I am really lagging today.

12:10pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/composition-forms#keyed-sequence-composition

I didn't really get this.

12:15pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/understanding-data-communication

Let me take a break here. These sections are long and will take me a while to get through. My focus is lower than yesterday too. I want to go through this quickly, and then move onto studying Feliz, SAFE examples and remoting. That way I'll be able to start on my own projects.

My own projects, Youtube vids. That will allow me to advertize myself.

1:20pm. Done with chores. Time for breakfast."

---
## [Cykeek-Labs/kernel_realme_sdm710](https://github.com/Cykeek-Labs/kernel_realme_sdm710)@[a201eadfa4...](https://github.com/Cykeek-Labs/kernel_realme_sdm710/commit/a201eadfa4fc3f93e50601a1d8577945f21f8bd0)
#### Saturday 2023-02-11 14:00:32 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
it is my opinion that the mechanisms around expiring runtime should be
removed altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com

---
## [Cykeek-Labs/kernel_realme_sdm710](https://github.com/Cykeek-Labs/kernel_realme_sdm710)@[31aa752b89...](https://github.com/Cykeek-Labs/kernel_realme_sdm710/commit/31aa752b89b70e239e746dfe74e098e6104d7b7f)
#### Saturday 2023-02-11 14:05:59 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate

---
## [l1ght13aby/Ubilling](https://github.com/l1ght13aby/Ubilling)@[27f1b1bb1d...](https://github.com/l1ght13aby/Ubilling/commit/27f1b1bb1d1d4ddf1babb05d6a77c535adebed88)
#### Saturday 2023-02-11 14:13:41 by l1ght13aby

fuck you array_merge

using array + array preserves keys

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[ef335f7d1f...](https://github.com/psychonaut-station/PsychonautStation/commit/ef335f7d1f33d196062a5a285c7f7216df2302a6)
#### Saturday 2023-02-11 15:38:28 by Rhials

It Came From Outer Spess: Adds midround changelings, delivered by an absolutely disgusting changeling meteor (#73018)

## About The Pull Request

Adds a new dynamic midround opportunity and random event - Space
Changeling.


https://user-images.githubusercontent.com/28870487/215284465-f5c5c1b1-b83d-471a-89be-1b65a4d2f2d4.mp4

If you are fortunate enough to recieve this role, you will be stuffed
into a changeling meteor and hurled at the side of the station. With no
crew identities, no access, and no equipment, you'll have to rely on
your **free** organic space suit and armblade to infiltrate the station
and get settled.

With no disguises to fall back on, the midround changeling experience
may lead to some very unfavorable situations. It's not unlikely that
you'll be spotted making your way inside, or that someone will see the
impact site and cause a panic. This role is not easy, but keep in mind
that you also have nothing to lose in the event that you use Lesser
Form/Headslug.

Aside from the starting circumstances, you have the same objectives and
capabilities as a roundstart changeling. Getting inside of the station
will be the hard part, but from there you can do what changelings do
best and blend in.

<details>
<summary>A brief note on the free stuff you get:</summary>
<br>
You get the organic space suit and armblade for free. The space suit is
absolutely vital, but I decided that the armblade should be given for
free as well. It's necessary for breaking open windows or airlocks and
getting access to the station, since otherwise your options are limited
to arrivals/departures. Having to pay a 2 point tax to avoid walking
naked into the main hallways of the station and getting gibbed is lame,
and with the added difficulty of the role I think it's fair.
</details>

Also, this is my 100th PR here! :)

## Why It's Good For The Game

Adds midround changelings in a WAY COOLER way than just making a random
crew/new arrival a changeling.

Lets people experience Hardmode Changeling, and test the adaptability
and flexibility of the most versatile antagonist even harder than
before. Losing the option to bypass the whole shape-shifter thing by
disguising as your crew identity presents a welcome change to the
formula.

Adds a teensy bit more midround variety, so we stop getting Nightmare At
The Thirty Minute Mark every round.
## Changelog
:cl: Rhials
add: Midround changeling spawn event.
add: Changeling meteor. It has a present for you.
/:cl:

---
## [npalaska/pbench](https://github.com/npalaska/pbench)@[36cbbd1c8f...](https://github.com/npalaska/pbench/commit/36cbbd1c8f98ddd4c46ccd7405fbca6263245753)
#### Saturday 2023-02-11 17:17:26 by David Butenhof

Fix operation synchronization (#3232)

* Fix operation synchronization

PBENCH-993

This is fairly large, but yet much smaller than it started out. This solves
two problems in Pbench Server task scheduling:

1. The default SQLAlchemy transaction model is to start a transaction on any
   SELECT and end it on any UPDATE or INSERT; this means there's no potential
   for atomic update. This impacts the management of all internal context, but
   serious problems have been observed with the "operation" and "state" of the
   datasets.
2. I began the dataset with the concept of a "state", as the dataset
   progresses through upload, backup, unpack, index, and delete. I quickly
   discovered that this wasn't ideal, but had trouble backing off completely
   from the concept. When I added the DB-based "operation" to replace the old
   filesystem links, the relationship between "operation" and "state" became
   even messier.

The primary change here is to divorce the `Sync` class entirely from general
metadata. (I originally set out to make `Metadata` management atomic, and the
fan-out was enormous: I'll tackle that again later, but while important in the
long run, getting `Sync` working is immediately critical.)

There is a new `Operation` DB object associated with a `Dataset`, and this is
entirely managed within the `Sync` class. For visibility, `Dataset.as_json`
will collect associated rows just as it does for `dataset.metalog`, but this
doesn't require any special transactional management. (It's a snapshot.)

I've completely *removed* the `Dataset.state` column (and its associated "last
transition" timestamp). "State" is tracked and observed by the various `Operation`
rows created and managed by `Sync`. This corresponds to the previous
dataset.status` sub-object managed by the old `Sync`: each named operation
(`OperationName` enum) that's been associated to a dataset will have a row with
`state` and `message` columns. The `state` can be advanced through `READY`,
`WORKING`, `OK`, and `FAILED`, and a message can be associated with each
row (on error via `Sync.error` or as part of transition via `Sync.update`).

While I was modifying the Dataset schema, I also removed the `created` column;
it's really redundant with `dataset.metalog.pbench.date`, and we'll need to
understand that for "non-Pbench-standard" tarballs we might not be able to get
this anyway. This wasn't quite as "easy" as I'd thought, because it meant that
I had to refactor date-range operations to work on `uploaded` (perhaps they
should have been that way originally).

`Sync.__init__`: Construct a sync object for a particular named operation.
`Sync.next`: Return a list of datasets which have `Operation` rows for the
   sync component that are in `READY` state.
`Sync.update`: Change the state of the sync component's `Operation`,
   optionally add a message to that `Operation`, and set a list of named
   operations for that dataset to `READY`.
`Sync.error`: Change the state of the sync component's `Operation` to `FAILED`
   and record an explanatory message for the failure.

To avoid rippling massive SQLAlchemy transaction model changes across all our
code, I've added a second session factory in `Database` with the most strict
integrity level, `SERIALIZABLE`. (In fact, I *think* that `"REPEATABLE READ"`
would be enough, and slightly more efficient, but sqlite3 doesn't support that
and I don't think I want to trust the weaker model it does support.)

*Only* the `Sync` class in `sync.py` currently uses that alternate session
factory. To avoid conflicts and confusions with autoflush and autocommit and
other SQLAlchemy "help", I'm creating new sessions on-the-fly for each call
and retiring them after commit/rollback. Note that the idiom
`with Database.maker.begin() as session:` constructs a new session with fresh
state, allows a sequence of session operations, and then implicitly tears down
the session after it commits on success or rolls back on an exception.

To avoid multiple `SELECT` statements within our transaction, `Sync.update`
fetches all relevant rows in a single `SELECT`, and then organizes them for
selective updates. This ensures we have no `SELECT` following the update of any
proxy object, which confuses SQLAlchemy in normal configuration.

`Sync.update` and `Sync.error` will loop up to 10 times on commit failure to
re-try with fresh data. Note that I've observed the retry logic in dozens of
functional test runs; and while I wonder vaguely whether I should be concerned
with the constant 10, I rarely see more than one or two retries since I added
a small delay to minimize thrashing.

NOTE: Alembic schema changes for Operation table

After working with Pete get get alembic to successfully generate a revision
file for my changes, we realized what a pain it would be to migrate (and
test) an actual live database. We need to have a functional test framework to
stand up an "old" functional DB, upgrade it to the latest revision, and then
validate the correctness.

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[406b6870bd...](https://github.com/Stalkeros2/Skyrat-tg/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Saturday 2023-02-11 17:20:00 by SkyratBot

[MIRROR] adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths [MDB IGNORE] (#18785)

* adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths (#72736)

repaths a lot of gloves off /color because they were incredibly stupid
firefighter gear has gotten an update (it doesnt cover hands anymore
though, you need something else)
firefighter helmets no longer hide your mask or glasses

![image](https://user-images.githubusercontent.com/23585223/212542599-c004d0e4-c141-40b4-a1bb-c838f9893c4b.png)
fixed engine goggles starting with darkness vision
to the atmos lockers adds atmospheric gloves, a pair of thick (chunky
fingers) gloves that are fireproof and fire protective, slightly shock
resistant and let you fireman carry people faster.
atmospheric firefighter helmets now are a subtype of welding hardhats,
you can enable a welding visor.
welding hardhats change mode with right click instead of altclick

im not a good spriter but i think this resprite makes them fit nicer
with other engi equipment
lets me firefighter rp

:cl:
add: Atmospheric Gloves, thick gloves that are fully fireproof and fire
protective and let you fireman carry people faster.
fix: fixes engine goggles starting with darkness vision
qol: firefighter helmets can now enable a welding visor
qol: welding hardhats change mode with right click instead of altclick
balance: firesuits no longer protect your hands
/:cl:

* Makes shit compile

* Updates the digi and snouted stuff to match the new sprites (thanks Halcyon!)

* Fixes a whole ton more issues that popped up

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [Roryl-c/tgstation](https://github.com/Roryl-c/tgstation)@[a47afd9051...](https://github.com/Roryl-c/tgstation/commit/a47afd905156bcc9a070db015cec7b1d1a07c578)
#### Saturday 2023-02-11 17:20:19 by Sol N

2 New Positive Quirks! (#72912)

## About The Pull Request

I added a few quirks to a downstream that I feel fit well with tg so
here they are.

First up is Poster Boy, a quirk that gives you three mood altering
posters, similar to the traitor objective to hang up demoralizing
posters. You spawn with a box that has one poster that will uplift the
entire crews spirits and 2 that are unique to your department. Captain
counts for security and assistants get only neutral posters. Finally,
with a crayon or spraycan, if you are any antagonist you can make your
poster into one of the ones from the traitor objective.

![dreamseeker_nRy44SL9Jb](https://user-images.githubusercontent.com/116288367/214109008-6f1b4b7c-e800-4142-be6d-926a8e975973.png)
example of quirk posters
Costs 4.


Finally, the characterful Throwing Arm quirk, which lets you throw
objects further (but not harder) and means you will never miss shots
into the disposals bin.
Costs 7.

previously i had a food subscription quirk here as well but i pulled it
out and plan to re-add it as a separate PR in march, where it will now
give you ingredients to cook a meal with occasionally.

## Why It's Good For The Game

Positive quirk variety is good and fun, I think that these positive
quirks are reasonable ones that offer unique things that the current
positive quirks do not.
Poster boy gives people a reason to run around and claim wall real
estate for their department and hopefully can build more solidarity in
departments, the hidden antag feature probably has uses but is just for
styling on people.
Throwing arm offers a fun character trait that probably can have some
slight uses and encourages the use of throwing weapons and tools more.
Also it is good to have a way to never miss the disposals bin. It's so
embarrassing.

## Changelog
:cl:
add: Poster boy and Throwing arm positive quirks.
imageadd: added posters for poster boy quirk
/:cl:

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[e8b38ea6a8...](https://github.com/shiptest-ss13/Shiptest/commit/e8b38ea6a89f9eb590c4185505df01793c6ed131)
#### Saturday 2023-02-11 17:40:59 by Bjarl

Patches the Bombed Starport To Be Less Bad (#1754)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![image](https://user-images.githubusercontent.com/94164348/217633782-c0dca540-0915-4acf-99f7-1031ea47f5ec.png)

![dreamseeker_vlOQGOERgI](https://user-images.githubusercontent.com/94164348/217633806-269717de-78fb-4fc2-8ab6-a7ee7a1c3b6e.png)

![dreamseeker_pP6WKD1PQT](https://user-images.githubusercontent.com/94164348/217633810-87471403-d8ad-4e46-bd3f-7a49c5eaad5d.png)
Puts some funny signs I painted over around, fixes the lighting, and
does a small pipe fix
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I watched like 4 people walk into this ruin completely unaware that it
was horrifically radioactive and that was just kinda not fun.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Bombed Starport lighting now works properly
imageadd: fokrads sign
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[2a4ef2367d...](https://github.com/jlsnow301/tgstation/commit/2a4ef2367dd7db73ba0adfdc300a5093678b7746)
#### Saturday 2023-02-11 18:14:46 by san7890

Basic Mobs Now Actually Have A Deathgasp (#72950)

## About The Pull Request

Pretty obviously an oversight since we only checked for simple_animal
for this, but should also factor in the fact that we could now be a
basic mob.

Actually I tested it on Sybil just now and deathgasps just never worked.
We were setting death_message for... I guess when they die? It's just
fucked but it works on my local now. blurgh
## Why It's Good For The Game

Ported simple animals that are now basic mobs were able to deathgasp
this time last year. Silly that they aren't able to do that now.
## Changelog
:cl:
fix: Basic Mobs are now able to deathgasp.
/:cl:

Let me know if the new variable name for the string is cringe, I just
settled on that since it mirrored the type of check we run in
select_message_type().

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3b54d3938c...](https://github.com/mrakgr/The-Spiral-Language/commit/3b54d3938c9fc7697384c68aab94bad14fe8c05d)
#### Saturday 2023-02-11 18:28:03 by Marko Grdinić

"1:35pm. https://www.semianalysis.com/p/the-inference-cost-of-search-disruption

> The amazing thing is that Microsoft knows that LLM insertion into search will crush the profitability of search and require massive Capex. While we estimated the operating margin shift, check out what Satya Nadella says about the gross margin.

> From now on, the [gross margin] of search is going to drop forever.
> Satya Nadella, Microsoft CEO

Based Microsoft. It wants to kill Google!

2:10pm. https://angel.co/company/zuvvii-gaming-limited/jobs/2091761-c-mobile-developer

This doesn't have a salary, but pays in equity. If I really want a job that badly I could always try applying to a place like this.

https://angel.co/company/tribes-5/jobs/2361599-full-stack-developer-c-net-javascript-blazor-freelance-2-3-months-contract

Hmmmm...

https://angel.co/jobs?job_listing_id=2254572

10-20k. Lowly paid, associated with an university.

Forget it, let me get back into the action. I won't apply to these. I was just wondering what the C# filter had. Fsharp literally has nothing.

(Edit: I applied to one C# job.)

Focus on finishing the book.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/intent

Let me just start rushing forward. This is too simple for me and not worth the mental effort to parse.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/routing

> Routing is an essential part of building single page applications. It is the main mechanism for switching the currently active page for any program. The idea revolves around a simple concept: listen to changes in the URL and react to those changes in the application. These changes can be manual when the user enters a URL in the address bar by hand or they could be programmatic where the application itself changes the URL. An important characteristic of routing in single page applications is that the application reacts to the changes of the URL without reloading the entire page. This means the application maintains its state as the route changes which is great because you can pass data around pages when you switch between them, for example passing information about the currently logged in user without having them to login again every time they navigate to another page. However, since the application maintains its state, it should be able to retain it if the user happens to fully refresh the page using F5. So we have to think about the re-initialization conditions when a full refresh occurs. More on that later, for now let us start with the simple examples.

> he only piece missing from the application above is the actual "listening to URL changes" part. The implementation for the listening for URL changes is best left out for a third-party library that knows how to work with URLs, parse them correctly and provide utilities to manage the history API: introducing Feliz.Router , a specialized library for routing in Elmish applications that is both very powerful to use and really simple to work with, written by yours truly as an essential part of the Feliz ecosystem.

This guy is based. He is a major driver of web dev in F#.

2:45pm. > The most common way to navigate to different URLs is using anchor elements with Html.a and setting their href attribute to the desired destination. However, since this is a single page application, the routes have to be formatted to properly include the hash sign, for that we use the Router.format function which is an overloaded function that takes in the segments of the URL you wish to construct and it formats it correctly for you. Here is an example that extends the sample application with links to navigate from one page to another:

Let me just pause a bit to wonder about something.

Single Page Application.

https://en.wikipedia.org/wiki/Single-page_application

> A single-page application (SPA) is a web application or website that interacts with the user by dynamically rewriting the current web page with new data from the web server, instead of the default method of a web browser loading entire new pages. The goal is faster transitions that make the website feel more like a native app.

So faster transitions. Yeah, makes sense.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/parsing-url-segments#parsing-segments-as-numbers

This is really cool. It makes me wonder how this could be done in Blazor.

3:10pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/parsing-date-segments

I've really been avoiding using active patterns far too much. Now that they have struct versions of them, I should make use of them.

3:15pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/parsing-date-segments

This material in this book is most likely going to end up being my gold standard in the future, isn't it? It is so clean. It is amazing.

3:40pm. Had to take a break. Let me resume.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/modelling-nested-routes

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/multi-page-routing

Heh. Now that I think about, the website for this book is made in Elmish and Feliz isn't it?

4:15pm.

> The highlighted line shows how requirement (6) can be enforced. Once the application starts up, we know for sure that the User = Anonymous which means if the application happened to start with an initial URL that is pointing to the Overview page, it will immediately redirect the user to the Login page instead as a result of the Cmd.navigate("login", HistoryMode.ReplaceState) command. We use the parameter HistoryMode.ReplaceState so that the navigation command doesn't push a "history entry" into the browser page. If that was the case, then a user will be trapped in /login as every time the user hits the Back button of the browser, he or she will go back to /overview which is a protected page that takes you back again to /login and so on and so forth.

This is starting to get tedious. Books are fun at first, but if you are only doing studying and no actual programming then it gets annoying.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/scaling/multi-page-routing

This book would be a lot more fun if I'd been following along instead of just skimming it. I'll never look at webpages again the same way.

4:25pm.

> Just remember that you have full control over how these child programs are initialized or updated, this is the flexibility of The Elm Architecture.

Yeah, I love this.

4:30pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/dev-flow/

4:50pm. > There's no downside to being on LinkedIn so long as you keep your CV up to date, have appropriate privacy settings, and don't waste your time posting and shit. Their job board is the best around.

I am taking a small break and wasting time on /g/. I really haven't looked at LinkedIn's job offers. I really should. Nevermind for now.

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/dev-flow/hot-module-replacement

These chapters show how to setup webpack as well as HMR.

> Of course, fable-loader is just one kind of loader that can be used in webpack. There are many loaders available out there  to be used and integrated into our webpack build pipeline to bundle different kinds of assets. In the next sections, we will learn how to use a couple of those loaders to extend the capabilities of our projects and enable them to integrate static images and use Sass  for styling instead of CSS.

Sass?

https://sass-lang.com/guide

> CSS on its own can be fun, but stylesheets are getting larger, more complex, and harder to maintain. This is where a preprocessor can help. Sass has features that don't exist in CSS yet like nesting, mixins, inheritance, and other nifty goodies that help you write robust, maintainable CSS.

Ok.

I won't bother studying this just yet.

```
test: /\.(png|jpe?g|gif)$/i,
```

I am really going to have to learn regex at some point.

5:15pm. https://zaid-ajaj.github.io/the-elmish-book/#/chapters/dev-flow/static-images

This really does teach me a lot about plugins. I am almost done with the book.

> Finally you can use it from the application by importing the file as a *"side-effect". These so-called side-effectful imports are those that do something when imported but don't return any value. In this case with styles, the side-effect is applying the stylesheet into the application. Other side-effectful modules can be those that add missing APIs into the page, also known as *polyfilling.

I was wondering what polyfilling was. It turns out it this.

5:30pm. > This requires a combination of using the awesome mini-css-extract  plugin which is usually included in most webpack templates that you can come across.

Only one more chapter left in the book!

https://zaid-ajaj.github.io/the-elmish-book/#/chapters/dev-flow/introducing-femto

5:35pm. Done.

I need a break.

Docs are fun at first, but then they get tedious.

Let me just take a look at the Feliz ones.

5:40pm. Time for lunch.

https://zaid-ajaj.github.io/Feliz/#/Feliz/TypeSafeCss
https://thisfunctionaltom.github.io/Html2Feliz/

6:25pm. Done with lunch.

https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3383068124

Something like this has 114 applicants. I suppose I could give it a try.

https://www.reversinglabs.com/company/careers

I applied. Now I am looking up the salary.

Damn it, Glassdoor has it, but I can't access it until I post a review on something.

> Competitive salary (1350eur - 2000eur neto, depending on experience).

Yeah, it is shit.

6:40pm. Forget it.

Let me go back to Feliz. This place is only good for interview practice. If I get it, I'll try to go through it as well as beat their tech interview, but I won't really take the offer. Though knowing my luck, they'll toss the resume in the trash right off the bat. But at the rate they are hiring, they are delusional if they thing they can get any better than mine. I am just curious to see if I will get a call back from here. At my level, even with no pro exp, I should be able to get offers from lowly paid Cro places. If I can't then that is really a signal to improve it.

https://zaid-ajaj.github.io/Feliz/#/Feliz/TypeSafeCss

Let me just go through these quickly and I will call it a day.

https://zaid-ajaj.github.io/Feliz/#/Hooks/UseElmish

> Besides being able to use Feliz in existing Elmish applications, you can also use Elmish as part of your Feliz application. This is a different approach to building standalone React components that use Elmish internally to manage the state of the component but from the perspective of the consumer, it is just another React component.

6:50pm. Ahhhhh...

```fs
    // now every time this component is rendered using              |
    // a different userId, it will reinitialize the component       ↓
    let state, dispatch = React.useElmish(init userId, update, [| box userId |])
    renderUserProfile state disptch
```

Yes, I remember this!

Having to specify dependencies by hand is what convinced me Reach was poorly designed.

But let me say, this Elmish stuff makes it look really good.

https://zaid-ajaj.github.io/Feliz/#/Feliz/React/StatefulComponents

Ok, I do not want to go through all of this right now. It is interesting that it has both maps and charting.

Back in...2015 or was it 2016, remember how much effort it took me to put those charts into that very first poker app?

In comparison, what I have here is 100 times easier.

If I were at my current level back then, I'd have spun up my own Elmish implementation assuming I wanted to do so, or used Rx.

Years ago I was partial to Rx, but even then I'd have admitted that Elmish was more elegant.

https://dzoukr.github.io/Feliz.Bulma/

Wait, wasn't Bulma some CSS thing?

...Yeah, it was. I guess it has more than just CSS stuff.

7:05pm. Ok, let me think. That is Elmish book down and Feliz down. I know a little backend and frontend development now.

I really gained a lot from the Elmish book. If it was the old me, I'd have given it proper respect by doing the exercises for it.

Remember that time I went through that massive .NET WPF book and did all the exercises in part 1, but translating them into F#.

I spent a month doing that in preparation for the poker app.

It was a huge waste of time, as the book itself never taught me how to abstract the UI code properly.

The stuff here is completely different. Having these libraries would have made a massive difference back then. I wish I could beam this knowledge to the past me as it would have saved me a lot of time and effort.

The poker app came out at 1.5k LOC and it was so complicated that I decided not to do UIs ever again.

I really should have gone into webdev back then, or studied Rx at least.

...Actually, I did study Rx back then! Remember the Reactive Scala course, I took? I didn't see the point of it at all when the time came to do UIs! Hahaha!

7:15pm. Tomorrow, I'll take a look at the SAFE stack examples. And after that I'll start work on my own project. Some Leduc poker would be right up my alley.

I can slowly build up my skills as I angle for a job paying at least 60k/year. This is my line as to what wouldn't embarass me to hold long term.

I really hope I get a call back from Enso, as working on a language and its libraries would be a great fit for me. The fact that I got a reaction from them saying they'll get back to me a few days later (which is now a week ago) rose my hopes just a little.

But you can't hope for anything here. I can only hold the rod until I feel a pull.

Let me rest here. I didn't do badly today."

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[d09cd15216...](https://github.com/pytorch/pytorch/commit/d09cd152161626381cae7780bbd2c44eedeb33d7)
#### Saturday 2023-02-11 18:44:06 by Taylor Robie

[Profiler] Defer recording startup python events (take 2) (#91684)

This is my commandeer of https://github.com/pytorch/pytorch/pull/82154 with a couple extra fixes.

The high level idea is that when we start profiling we see python frames which are currently executing, but we don't know what system TID created them. So instead we defer the TID assignment, and then during post processing we peer into the future and use the system TID *of the next* call on that Python TID.

As an aside, it turns out that CPython does some bookkeeping (https://github.com/python/cpython/blob/ee821dcd3961efc47262322848267fe398faa4e4/Include/cpython/pystate.h#L159-L165, thanks @dzhulgakov for the pointer), but you'd have to do some extra work at runtime to know how to map their TID to ours so for now I'm going to stick to what I can glean from post processing alone.

As we start observing more threads it becomes more important to be principled about how we start up and shut down. (Since threads may die while the profiler is running.) #82154 had various troubles with segfaults that wound up being related to accessing Python thread pointers which were no longer alive. I've tweaked the startup and shutdown interaction with the CPython interpreter and it should be safer now.

Differential Revision: [D42336292](https://our.internmc.facebook.com/intern/diff/D42336292/)
Pull Request resolved: https://github.com/pytorch/pytorch/pull/91684
Approved by: https://github.com/chaekit

---
## [hamnand/package](https://github.com/hamnand/package)@[c59fabde63...](https://github.com/hamnand/package/commit/c59fabde63aab6634fef68149c672029aede0184)
#### Saturday 2023-02-11 19:08:38 by hamnand

Create [.WATCH.] Avatar 2: The Way Of Water (2023) FullMovie Online on Free Streaming at home

27 secs ago - Still Now Here Option’s to Downloading or watching Avatar 2: The Way Of Water streaming the full movie online for free. Do you like movies? If so, then you’ll love New Romance Movie: Avatar 2: The Way Of Water. This movie is one of the best in its genre. #Avatar 2: The Way Of Water will be available to watch online on Netflix's very soon!

N|Movie URL N|Movie URL

Now Is Avatar 2: The Way Of Water available to stream? Is watching Avatar 2: The Way Of Water on Disney Plus, HBO Max, Netflix, or Amazon Prime? Yes, we have found an authentic streaming option/service. A 1950s housewife living with her husband in a utopian experimental community begins to worry that his glamorous company could be hiding disturbing secrets. Showcase Cinema Warwick you'll wanat to make sure you're one of the first people to see it! So mark your calendars and get ready for a Avatar 2: The Way Of Water movie experience like never before. of our other Marvel movies available to watch online. We're sure you'll find something to your liking. Thanks for reading, and we'll see you soon! Avatar 2: The Way Of Water is available on our website for free streaming. Details on how you can watch Avatar 2: The Way Of Water for free throughout the year are described If you're a fan of the comics, you won't want to miss this one! The storyline follows Avatar 2: The Way Of Water as he tries to find his way home after being stranded on an alien Avatar 2: The Way Of Watert. Avatar 2: The Way Of Water is definitely a Avatar 2: The Way Of Water movie you don't want to miss with stunning visuals and an action-packed plot! Plus, Avatar 2: The Way Of Water online streaming is available on our website. Avatar 2: The Way Of Water online is free, which includes streaming options such as 123movies, Reddit, or TV shows from HBO Max or Netflix! Avatar 2: The Way Of Water Release in the US Avatar 2: The Way Of Water hits theaters on January 20, 2023. Tickets to see the film at your local movie theater are available online here. The film is being released in a wide release so you can watch it in person. How to Watch Avatar 2: The Way Of Water for Free?release on a platform that offers a free trial. Our readers to always pay for the content they wish to consume online and refrain from using illegal means. Where to Watch Avatar 2: The Way Of Water? There are currently no platforms that have the rights to Watch Avatar 2: The Way Of Water Movie Online.MAPPA has decided to air the movie only in theaters because it has been a huge success.The studio , on the other hand, does not wish to divert revenue Streaming the movie would only slash the profits, not increase them. As a result, no streaming services are authorized to offer Avatar 2: The Way Of Water Movie for free. The film would, however, very definitely be acquired by services like Funimation , Netflix, and Crunchyroll. As a last consideration, which of these outlets will likely distribute the film worldwide? Is Avatar 2: The Way Of Water on Netflix? The streaming giant has a massive catalog of television shows and movies, but it does not include 'Avatar 2: The Way Of Water.' We recommend our readers watch other dark fantasy films like 'The Witcher: Nightmare of the Wolf.' Is Avatar 2: The Way Of Water on Crunchyroll? Crunchyroll, along with Funimation, has acquired the rights to the film and will be responsible for its distribution in North America.Therefore, we recommend our readers to look for the movie on the streamer in the coming months. subscribers can also watch dark fantasy shows like 'Jujutsu Kaisen.' Is Avatar 2: The Way Of Water on Hulu? No, 'Avatar 2: The Way Of Water' is unavailable on Hulu. People who have a subscription to the platform can enjoy 'Afro Samurai Resurrection' or 'Ninja Scroll.' Is Avatar 2: The Way Of Water on Amazon Prime? Amazon Prime's current catalog does not include 'Avatar 2: The Way Of Water.' However, the film may eventually release on the platform as video-on-demand in the coming months.fantasy movies on Amazon Prime's official website. Viewers who are looking for something similar can watch the original show 'Dororo.' When Will Avatar 2: The Way Of Water Be on Disney+? Avatar 2: The Way Of Water, the latest installment in the Avatar 2: The Way Of Water franchise, is coming to Disney+ on July 8th! This new movie promises to be just as exciting as the previous ones, with plenty of action and adventure to keep viewers entertained. you're looking forward to watching it, you may be wondering when it will be available for your Disney+ subscription. Here's an answer to that question! 15 secs ago - Still Now Here Option’s to Downloading or watching Avatar 2: The Way Of Water streaming the full movie online for free. Do you like movies? If so, then you’ll love New Romance Movie: Avatar 2: The Way Of Water. This movie is one of the best in its genre. #Avatar 2: The Way Of Water will be available to watch online on Netflix's very soon!

Now Is Avatar 2: The Way Of Water available to stream? Is watching Avatar 2: The Way Of Water on Disney Plus, HBO Max, Netflix, or Amazon Prime? Yes, we have found an authentic streaming option/service. A 1950s housewife living with her husband in a utopian experimental community begins to worry that his glamorous company could be hiding disturbing secrets. Showcase Cinema Warwick you'll want to make sure you're one of the first people to see it! So mark your calendars and get ready for a Avatar 2: The Way Of Water movie experience like never before. of our other Marvel movies available to watch online. We're sure you'll find something to your liking. Thanks for reading, and we'll see you soon! Avatar 2: The Way Of Water is available on our website for free streaming. Details on how you can watch Avatar 2: The Way Of Water for free throughout the year are described If you're a fan of the comics, you won't want to miss this one! The storyline follows Avatar 2: The Way Of Water as he tries to find his way home after being stranded on an alien Avatar 2: The Way Of Watert. Avatar 2: The Way Of Water is definitely a Avatar 2: The Way Of Water movie you don't want to miss with stunning visuals and an action-packed plot! Plus, Avatar 2: The Way Of Water online streaming is available on our website. Avatar 2: The Way Of Water online is free, which includes streaming options such as 123movies, Reddit, or TV shows from HBO Max or Netflix! Avatar 2: The Way Of Water Release in the US Avatar 2: The Way Of Water hits theaters on January 20, 2023. Tickets to see the film at your local movie theater are available online here. The film is being released in a wide release so you can watch it in person. How to Watch Avatar 2: The Way Of Water for Free?release on a platform that offers a free trial. Our readers to always pay for the content they wish to consume online and refrain from using illegal means. Where to Watch Avatar 2: The Way Of Water? There are currently no platforms that have the rights to Watch Avatar 2: The Way Of Water Movie Online.MAPPA has decided to air the movie only in theaters because it has been a huge success.The studio , on the other hand, does not wish to divert revenue Streaming the movie would only slash the profits, not increase them. As a result, no streaming services are authorized to offer Avatar 2: The Way Of Water Movie for free. The film would, however, very definitely be acquired by services like Funimation , Netflix, and Crunchyroll. As a last consideration, which of these outlets will likely distribute the film worldwide? Is Avatar 2: The Way Of Water on Netflix? The streaming giant has a massive catalog of television shows and movies, but it does not include 'Avatar 2: The Way Of Water.' We recommend our readers watch other dark fantasy films like 'The Witcher: Nightmare of the Wolf.' Is Avatar 2: The Way Of Water on Crunchyroll? Crunchyroll, along with Funimation, has acquired the rights to the film and will be responsible for its distribution in North America.Therefore, we recommend our readers to look for the movie on the streamer in the coming months. subscribers can also watch dark fantasy shows like 'Jujutsu Kaisen.' Is Avatar 2: The Way Of Water on Hulu? No, 'Avatar 2: The Way Of Water' is unavailable on Hulu. People who have a subscription to the platform can enjoy 'Afro Samurai Resurrection' or 'Ninja Scroll.' Is Avatar 2: The Way Of Water on Amazon Prime? Amazon Prime's current catalog does not include 'Avatar 2: The Way Of Water.' However, the film may eventually release on the platform as video-on-demand in the coming months.fantasy movies on Amazon Prime's official website. Viewers who are looking for something similar can watch the original show 'Dororo.' When Will Avatar 2: The Way Of Water Be on Disney+? Avatar 2: The Way Of Water, the latest installment in the Avatar 2: The Way Of Water franchise, is coming to Disney+ on July 8th! This new movie promises to be just as exciting as the previous ones, with plenty of action and adventure to keep viewers entertained. you're looking forward to watching it, you may be wondering when it will be available for your Disney+ subscription. Here's an answer to that question! Is Avatar 2: The Way Of Water on Funimation? Crunchyroll, its official website may include the movie in its catalog in the near future. Meanwhile, people who wish to watch something similar can stream 'Demon Slayer: Kimetsu no Yaiba – The Movie: Mugen Train.' Avatar 2: The Way Of Water Online In The US? Most Viewed, Most Favorite, Top Rating, Top IMDb movies online. Here we can download and watch 123movies movies offline. 123Movies website is the best alternative to Avatar 2: The Way Of Water's (2021) free online. We will recommend 123Movies as the best Solarmovie alternative There are a few ways to watch Avatar 2: The Way Of Water online in the US You can use a streaming service such as Netflix, Hulu, or Amazon Prime Video. You can also rent or buy the movie on iTunes or Google Play. watch it on-demand or on a streaming app available on your TV or streaming device if you have cable. What is Avatar 2: The Way Of Water About? It features an ensemble cast that includes Florence Pugh, Harry Styles, Wilde, Gemma Chan, KiKi Layne, Nick Kroll, and Chris Pine. In the film, a young wife living in a 2250s company town begins to believe there is a sinister secret being kept from her by the man who runs it. InshaAllah......

---
## [tm24fan8/Home-Assistant-Configs](https://github.com/tm24fan8/Home-Assistant-Configs)@[7432793f34...](https://github.com/tm24fan8/Home-Assistant-Configs/commit/7432793f34bde474a5d5b1587b0c40494100aaed)
#### Saturday 2023-02-11 19:12:25 by Tony Stork

Multiroom scenes need to be scripts. That's just all there is to it.

The amount of haunted house bullshit that my house pulled on me last night was insane...

---
## [angrycub/nomad](https://github.com/angrycub/nomad)@[f998a2b77b...](https://github.com/angrycub/nomad/commit/f998a2b77b84a542d73f11a0a254576f9031d1f3)
#### Saturday 2023-02-11 19:31:58 by Michael Schurter

core: merge reserved_ports into host_networks (#13651)

Fixes #13505

This fixes #13505 by treating reserved_ports like we treat a lot of jobspec settings: merging settings from more global stanzas (client.reserved.reserved_ports) "down" into more specific stanzas (client.host_networks[].reserved_ports).

As discussed in #13505 there are other options, and since it's totally broken right now we have some flexibility:

Treat overlapping reserved_ports on addresses as invalid and refuse to start agents. However, I'm not sure there's a cohesive model we want to publish right now since so much 0.9-0.12 compat code still exists! We would have to explain to folks that if their -network-interface and host_network addresses overlapped, they could only specify reserved_ports in one place or the other?! It gets ugly.
Use the global client.reserved.reserved_ports value as the default and treat host_network[].reserverd_ports as overrides. My first suggestion in the issue, but @groggemans made me realize the addresses on the agent's interface (as configured by -network-interface) may overlap with host_networks, so you'd need to remove the global reserved_ports from addresses shared with a shared network?! This seemed really confusing and subtle for users to me.
So I think "merging down" creates the most expressive yet understandable approach. I've played around with it a bit, and it doesn't seem too surprising. The only frustrating part is how difficult it is to observe the available addresses and ports on a node! However that's a job for another PR.

---
## [752963e64/AwfuLite](https://github.com/752963e64/AwfuLite)@[19f288f8f5...](https://github.com/752963e64/AwfuLite/commit/19f288f8f541afa5ffa0fae4d0aeb09640252e1b)
#### Saturday 2023-02-11 21:05:05 by DragonTalk

Entirely freed, explain what's coming...
You may fuck yourself deeply... if you attempt suing me over what I do/done...
Pay me instead to write things for you...

---
## [NewyearnewmeUwu/cmss13](https://github.com/NewyearnewmeUwu/cmss13)@[c7a33d5ff9...](https://github.com/NewyearnewmeUwu/cmss13/commit/c7a33d5ff9f4f7563145e82dd6cd0cd00f6b53c5)
#### Saturday 2023-02-11 21:05:26 by riot

PMC and Whiteout stuff (#1966)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

As a preword, I came up with every change in this PR and coded them in
the span of 10 hours, so some things may be iffy.

PMCs and Whiteout may be good, but they're a bit outdated, this
modernizes multiple loadout aspects, enables antag vendors for
admin-spawn, and does some balance changes to certain
portions(specifically chem ERT).

Individual changes, numbered, will go over each in why its good, may
have forgotten one or two things.

1. Buffs whiteout flamer with blue flame damage, belt-linked magharn,
and pyro underbarrel extinguisher
2. Adds a synthetic repair kit(medkit), with synth repair tools, gives
it to whiteout.
3. Adds breaching charges and swaps crowbars to tactical in whiteout
loadouts
4. Gives whiteout PMC sniper goggles(thermals)
5. Gives whiteout medic the required gear to actually repair a downed
member of the team, and just a lot of synth heals.
6. Gives whiteout leader a pyro extinguisher.
7. Gives whiteout weapons default attachments.
8. Adds an 'advanced' mini-flamer with the same stats as UPP integrated
UBF, gives it to NSG23 and random m41/2 attachie.
9. Gives detainer PMCs a version of the corporate m41A MK2(goon gun),
with attachies and adv flamer to replace flamethrower.
10. Swaps chem PMC TL P90(name is too long) with an M41/2
11. Gives normal PMC ERT roles a webbing vest with meds and
miniextinguisher
12. Gives PMC Surgeon the essentials required to act as a medic, swaps
NSG with M39/2, gives them a normal but unique look.
13. Whiteout and PMC SG powerpacks have 30k power by default, instead of
10k.
14. Gives PMC guns more options for random attachments, and gives m41/2
its intended collapsible stock
15. Gives PMC engi m39/2 instead of P90
16. Removes flamer from potential PMC loadouts.
17. Gives PMCs better CQC skill.
18. Gives PMC TLs autoinjector pouches(which gives chem TL a second
pouch in the first place)
19. Detainer PMCs now have tac-sechuds, PMC TLs have sensorhuds.
20. **Enables antag vendor for PMC roles.** (Look at file changes for
the specific things, too long for pr desc)

# Explain why it's good for the game

Modernization and some needed loadout/balance changes(IMO).
Per number:

1. Whiteout flamer did worse damage than napalm, and was incredibly easy
to lose.
2. More heals for each member of the whiteout team, allows more
self-sufficiency.
3. Breach charges for tacticool breaches, crowbar doubles as a melee
weapon in case the player doesn't know about synth punch
4. Whiteout didn't have proper NVG, thermals allows them to do
tacticooler breaches by lining up people wth breach charge.
5. Whiteout medic didn't have a lot of heals at all, and didn't have a
defib, so they weren't much of a medic.
6. To extinguish the flames and lead charges, works like pyro
underbarrel extinguisher, but handheld.
7. Default tacticool attachment, already made whiteout subtypes for
HEAP, why not give them good attachies with them too.
8. Mini-flamer sucks, gives a better version for NSG and m41/2, same
stats as the already existing UPP integrated UBF.
9. Detainers had flamers which sucked, gives them corpo m41s which
aren't as good as /2s, but have adv UBF for flames.
10. P90 sucks, having default m41/2 fits with other leader type, also
gives them a better gun than their underlings.
11. Medkit but in a webbing, its my personal combat webbing load when I
play so its good.
12. PMC Surgeon was horrifically undergeared, they didn't even have a
medhud, gives them basic gear similar to PMC med but with a beret to
tell them apart.
13. ERTs don't have spare batteries to get usually, more staying power
in fights.
14. More options for attachies to further make PMC weapons better, also
gives m41/2 the m41 collapsible stock because it needed it.
15. P90 sucks, support roles getting the m39/2 is cool.
16. Flamer sucks to get as PMC, and adv. UBF as a potential m41/2
attachie makes a full-sized flamer useless too.
17. PMCs could fireman carry, and multi-strip, but did it horrifically
slow, gives them MP level CQC(master for spec, expert for TL)
18. TL getting extra meds is neat, also chem TL had an empty pocket slot
and no meds, thats bad.
19. Sechud-thing for PMC detainers is useful(stops flashbang trolling
for one), giving PMC TL a sensorhud to watch their team's status is also
good.
20. Makes doing event bases for PMCs much easier, too long to post the
specific changes here but look at files for them.


# Testing Photographs and Procedure

I forgot to take screenshots but it all works. 👍 
I spawned myself as every changed role and tested every individual
change extensively.

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
add: PMCs are now able to use antag vendors.
balance: Multiple loadout and skill changes to PMCs and Whiteout
balance: Buffs whiteout flame damage to blue flame damage.
fix: PMC Investigator Lead now appropriately spawns with a medical pouch
in their pocket, instead of nothing.
fix: Maximum skill preset now appropriately also has BE and intel skill,
at maximum of course.
fix: PMC Smartgunner now appropriately a VP78 to go along with their
VP78 magazines
fix: Whiteout now appropriately have night vision.
fix: M41A/2 now appropriately comes equipped with a collapsible stock.
spellcheck: PMC smartgun drum now has a seperate description and name
from base SG to match its different appearance.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[b61be9ee86...](https://github.com/clintjedwards/gofer/commit/b61be9ee867ad1bf694c709574b763cb014ea108)
#### Saturday 2023-02-11 21:10:19 by Clint J Edwards

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
## [FRC2240/ChargedUp2023](https://github.com/FRC2240/ChargedUp2023)@[77a7092868...](https://github.com/FRC2240/ChargedUp2023/commit/77a709286881c5fa52f1adaa5d177f193d4f7342)
#### Saturday 2023-02-11 22:27:49 by Cynosure-Null

vision refactor or how i had a coconut mall pain

omg i love ikea shork

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

 On branch circular_buffer
 Changes to be committed:
	modified:   src/main/cpp/Vision.cpp
	modified:   src/main/include/Constants.h
	modified:   src/main/include/Vision.h

Depointering

help the pointers poke me ow

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

NFC: reordered files

Debugged raw data

It now gets the raw data & is confirmed to work

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

Added Erik's vector-based fixes

refactored to involve moar vectors

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

forgive me mr stroustrup for i have sinned

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

rebase: cout, increments, and the revival of disco

god help me im delirious
but im stayn alive

oh i also fixed a lot of segfaults
and added a bunch of couts

help its too many couts

btw it segfaults

-- Commit made by segmentation fault (core dumped)
 Changes to be committed:
	modified:   src/main/cpp/Robot.cpp
	modified:   src/main/cpp/Vision.cpp
	modified:   src/main/include/Constants.h
    modified:   src/main/include/Robot.hpp
	modified:   src/main/include/Vision.h

debugging watchdog

Pre stdev testing

-- Commit made by Jeff Bezos Stonerbot
(AKA cynosure or Cynosure-NUL) <cynosure@disroot.org>
My PGP key can be found on my github profile
Fly safe

mid testing

turns out my sheet was wrong

rebase: drivebase size

mid drive testing

vision testing. Pre firmware update

Vision testing

Added a bunch of logs, removed some couts and other things

When static, bot is off by *under a centimeter*

Needs more testing

My PGP key can be found on my github profile
Fly safe

---
## [wrenbirda/rock-paper-scissors](https://github.com/wrenbirda/rock-paper-scissors)@[1c7508e79d...](https://github.com/wrenbirda/rock-paper-scissors/commit/1c7508e79d2c9cef0a1cae56e31e8044f084030c)
#### Saturday 2023-02-11 23:31:09 by wrenbirda

Fix loop; rework code based on father.js

Okay, I do kind of consider this cheating, but I needed assistance. My
dad toyed around with JS and made a script (see father.js). His works
great -.- which is cool. I think I found some of the errors in my old
code but since I'm new to this, I'm going to walk away and try another
project. Then come back and rework RPS with more experienced eyes.

I should have committed sooner because this code is wildly different.
This is a fully functional RPS program, where you play until you hit 3
wins.

---

