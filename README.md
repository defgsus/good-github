## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-24](docs/good-messages/2023/2023-09-24.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,973,167 were push events containing 2,700,865 commit messages that amount to 148,999,514 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 67 messages:


## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[696a8ab1fa...](https://github.com/nikothedude/Skyrat-tg/commit/696a8ab1fa7d90f309b4f869fbedb73557665a05)
#### Sunday 2023-09-24 00:28:06 by SkyratBot

[MIRROR] Only double HCR for impressive greentexts [MDB IGNORE] (#23778)

* Only double HCR for impressive greentexts (#78383)

There were a few exploits with free antags that would double your score.
This happened to me once by accident, but anyone could essentially
guarantee a point doubling.

I've changed the whole thing to only work for:
- Traitor
- Changeling
- Heretic
- Blood brother
- Headrev
- Wizard (you could get this with die of fate)
- Obsessed
- Magic and gun survivalists
- Holding the greentext book (because a cripple fighting for their life
for the greentext just seems funny and is rare enough)

Notably, revolutionairies, cult converts and brainwashed now no longer
pay out. Cult is pointless since you can't greentext without gibbing
(trust me I tried) and revolutionairy takes no effort other than having
strong teammates and doing nothing. There are a lot of other antags this
excludes, but those are mostly midrounds and non-humans (which are by
default excluded)

:cl:
balance: Only traitor, changeling, heretic, blood brother, headrev,
wizard, obsessed, magic/gun survivalists and greentext book holders can
now double their hardcore random score
qol: Redtexting as antag with hardcore random score will pay you default
points, instead of none (normal survival rules)
fix: End report screen will properly report hardcore random survival in
case of station destruction
/:cl:

* Only double HCR for impressive greentexts

---------

Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [hexagon-geo-surv/openembedded-core](https://github.com/hexagon-geo-surv/openembedded-core)@[909fd25c2e...](https://github.com/hexagon-geo-surv/openembedded-core/commit/909fd25c2ebd25f5d3bc560e26f9df6862e033d0)
#### Sunday 2023-09-24 00:39:17 by Richard Purdie

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
## [hexagon-geo-surv/poky](https://github.com/hexagon-geo-surv/poky)@[4682ae38f2...](https://github.com/hexagon-geo-surv/poky/commit/4682ae38f285f59b68196289ece5802460805201)
#### Sunday 2023-09-24 00:40:47 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

(From OE-Core rev: 909fd25c2ebd25f5d3bc560e26f9df6862e033d0)

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>
(cherry picked from commit 596fb699d470d7779bfa694e04908929ffeabcf7)
Signed-off-by: Steve Sakoman <steve@sakoman.com>

---
## [Nevuly/WSL2-Linux-Kernel-Rolling](https://github.com/Nevuly/WSL2-Linux-Kernel-Rolling)@[3c919b0910...](https://github.com/Nevuly/WSL2-Linux-Kernel-Rolling/commit/3c919b0910906cc69d76dea214776f0eac73358b)
#### Sunday 2023-09-24 00:46:46 by Darrick J. Wong

xfs: reserve less log space when recovering log intent items

Wengang Wang reports that a customer's system was running a number of
truncate operations on a filesystem with a very small log.  Contention
on the reserve heads lead to other threads stalling on smaller updates
(e.g.  mtime updates) long enough to result in the node being rebooted
on account of the lack of responsivenes.  The node failed to recover
because log recovery of an EFI became stuck waiting for a grant of
reserve space.  From Wengang's report:

"For the file deletion, log bytes are reserved basing on
xfs_mount->tr_itruncate which is:

    tr_logres = 175488,
    tr_logcount = 2,
    tr_logflags = XFS_TRANS_PERM_LOG_RES,

"You see it's a permanent log reservation with two log operations (two
transactions in rolling mode).  After calculation (xlog_calc_unit_res()
adds space for various log headers), the final log space needed per
transaction changes from  175488 to 180208 bytes.  So the total log
space needed is 360416 bytes (180208 * 2).  [That quantity] of log space
(360416 bytes) needs to be reserved for both run time inode removing
(xfs_inactive_truncate()) and EFI recover (xfs_efi_item_recover())."

In other words, runtime pre-reserves 360K of space in anticipation of
running a chain of two transactions in which each transaction gets a
180K reservation.

Now that we've allocated the transaction, we delete the bmap mapping,
log an EFI to free the space, and roll the transaction as part of
finishing the deferops chain.  Rolling creates a new xfs_trans which
shares its ticket with the old transaction.  Next, xfs_trans_roll calls
__xfs_trans_commit with regrant == true, which calls xlog_cil_commit
with the same regrant parameter.

xlog_cil_commit calls xfs_log_ticket_regrant, which decrements t_cnt and
subtracts t_curr_res from the reservation and write heads.

If the filesystem is fresh and the first transaction only used (say)
20K, then t_curr_res will be 160K, and we give that much reservation
back to the reservation head.  Or if the file is really fragmented and
the first transaction actually uses 170K, then t_curr_res will be 10K,
and that's what we give back to the reservation.

Having done that, we're now headed into the second transaction with an
EFI and 180K of reservation.  Other threads apparently consumed all the
reservation for smaller transactions, such as timestamp updates.

Now let's say the first transaction gets written to disk and we crash
without ever completing the second transaction.  Now we remount the fs,
log recovery finds the unfinished EFI, and calls xfs_efi_recover to
finish the EFI.  However, xfs_efi_recover starts a new tr_itruncate
tranasction, which asks for 360K log reservation.  This is a lot more
than the 180K that we had reserved at the time of the crash.  If the
first EFI to be recovered is also pinning the tail of the log, we will
be unable to free any space in the log, and recovery livelocks.

Wengang confirmed this:

"Now we have the second transaction which has 180208 log bytes reserved
too. The second transaction is supposed to process intents including
extent freeing.  With my hacking patch, I blocked the extent freeing 5
hours. So in that 5 hours, 180208 (NOT 360416) log bytes are reserved.

"With my test case, other transactions (update timestamps) then happen.
As my hacking patch pins the journal tail, those timestamp-updating
transactions finally use up (almost) all the left available log space
(in memory in on disk).  And finally the on disk (and in memory)
available log space goes down near to 180208 bytes.  Those 180208 bytes
are reserved by [the] second (extent-free) transaction [in the chain]."

Wengang and I noticed that EFI recovery starts a transaction, completes
one step of the chain, and commits the transaction without completing
any other steps of the chain.  Those subsequent steps are completed by
xlog_finish_defer_ops, which allocates yet another transaction to
finish the rest of the chain.  That transaction gets the same tr_logres
as the head transaction, but with tr_logcount = 1 to force regranting
with every roll to avoid livelocks.

In other words, we already figured this out in commit 929b92f64048d
("xfs: xfs_defer_capture should absorb remaining transaction
reservation"), but should have applied that logic to each intent item's
recovery function.  For Wengang's case, the xfs_trans_alloc call in the
EFI recovery function should only be asking for a single transaction's
worth of log reservation -- 180K, not 360K.

Quoting Wengang again:

"With log recovery, during EFI recovery, we use tr_itruncate again to
reserve two transactions that needs 360416 log bytes.  Reserving 360416
bytes fails [stalls] because we now only have about 180208 available.

"Actually during the EFI recover, we only need one transaction to free
the extents just like the 2nd transaction at RUNTIME.  So it only needs
to reserve 180208 rather than 360416 bytes.  We have (a bit) more than
180208 available log bytes on disk, so [if we decrease the reservation
to 180K] the reservation goes and the recovery [finishes].  That is to
say: we can fix the log recover part to fix the issue. We can introduce
a new xfs_trans_res xfs_mount->tr_ext_free

{
  tr_logres = 175488,
  tr_logcount = 0,
  tr_logflags = 0,
}

"and use tr_ext_free instead of tr_itruncate in EFI recover."

However, I don't think it quite makes sense to create an entirely new
transaction reservation type to handle single-stepping during log
recovery.  Instead, we should copy the transaction reservation
information in the xfs_mount, change tr_logcount to 1, and pass that
into xfs_trans_alloc.  We know this won't risk changing the min log size
computation since we always ask for a fraction of the reservation for
all known transaction types.

This looks like it's been lurking in the codebase since commit
3d3c8b5222b92, which changed the xfs_trans_reserve call in
xlog_recover_process_efi to use the tr_logcount in tr_itruncate.
That changed the EFI recovery transaction from making a
non-XFS_TRANS_PERM_LOG_RES request for one transaction's worth of log
space to a XFS_TRANS_PERM_LOG_RES request for two transactions worth.

Fixes: 3d3c8b5222b92 ("xfs: refactor xfs_trans_reserve() interface")
Complements: 929b92f64048d ("xfs: xfs_defer_capture should absorb remaining transaction reservation")
Suggested-by: Wengang Wang <wen.gang.wang@oracle.com>
Cc: Srikanth C S <srikanth.c.s@oracle.com>
[djwong: apply the same transformation to all log intent recovery]
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>

---
## [Kuyachris84/projects](https://github.com/Kuyachris84/projects)@[bf3437fce1...](https://github.com/Kuyachris84/projects/commit/bf3437fce1c2deb639268050d6c8e33905000884)
#### Sunday 2023-09-24 01:38:09 by Chris Vasquez

Create mealtime_exercise

Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

---
## [mamh-mixed/git-git](https://github.com/mamh-mixed/git-git)@[8f23432b38...](https://github.com/mamh-mixed/git-git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Sunday 2023-09-24 01:54:51 by Johannes Schindelin

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
## [VladinXXV/towelstation13](https://github.com/VladinXXV/towelstation13)@[eb7aa01d7a...](https://github.com/VladinXXV/towelstation13/commit/eb7aa01d7a5f9f247a2b433621f6910c6a4d4cd7)
#### Sunday 2023-09-24 01:59:07 by Alexis

I HATE TAURS REMOVE THEM I AM SO SICK OF SEEING THIS SHIT I WANT TO THROW UP UGH (#31)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
REMOVS THE FURRY FETISH CONTENT IMA M SO SICK OF IT
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## How This Contributes To The Towelstation Roleplay Experience
IF I HAVE TO SEE THE WORD "TAUR" "PENIS" "BREASTS" "BALL SIZE" OR ANY
FUCKING SHIT LIKE THAT ONE MORE TIME TODAY I AM GONNG TO CRY
<!-- Please add a short description of why you think these changes would
benefit the game and the roleplay atmosphere of the server. If you can't
justify it in words, it might not be worth adding. -->

## Proof of Testing

<!-- Include any screenshots/videos/debugging steps of the code
functioning successfully, between the </summary> and </details> code
blocks. -->
<!-- To our mappers and spriters: Posting screenshots of content INSIDE
EDITORS (aseprite, PDN, SDMM, ect) is NOT valid proof of testing. Please
make sure that you COMPILE the game and provide PROOF you tested your
edits. -->

<details>
<summary>Screenshots/Videos</summary>
  
</details>

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
del: Removes taurs
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [VladinXXV/towelstation13](https://github.com/VladinXXV/towelstation13)@[6c7af3b452...](https://github.com/VladinXXV/towelstation13/commit/6c7af3b45234a4109fe0835f3cb5b0ef743e6e4e)
#### Sunday 2023-09-24 01:59:07 by Alexis

Adds the Bluespace Compression kit (#29)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds the Bluespace Compression kit (BCK), a hacked BRPD that can be used
to make items smaller.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## How This Contributes To The Towelstation Roleplay Experience
Funny new traitor item that can be bought for 13 tc.
<!-- Please add a short description of why you think these changes would
benefit the game and the roleplay atmosphere of the server. If you can't
justify it in words, it might not be worth adding. -->

## Proof of Testing

<!-- Include any screenshots/videos/debugging steps of the code
functioning successfully, between the </summary> and </details> code
blocks. -->
<!-- To our mappers and spriters: Posting screenshots of content INSIDE
EDITORS (aseprite, PDN, SDMM, ect) is NOT valid proof of testing. Please
make sure that you COMPILE the game and provide PROOF you tested your
edits. -->

<details>
<summary>Screenshots/Videos</summary>
  

![image](https://github.com/Towelstation13/towelstation13/assets/20053168/ccd56d73-c894-460f-9a46-1702b011486c)

![image](https://github.com/Towelstation13/towelstation13/assets/20053168/bf1c5006-7e3d-403e-bc5d-7768b130d28c)

</details>

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
add: Added the bluespace compression kit, which you can use to shrink
items. Purchasable through uplinks for 13 tc.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: distributivgesetz <distributivgesetz93@gmail.com>

---
## [riyaajosh37/Mental-Wellness-Journaling-Platform](https://github.com/riyaajosh37/Mental-Wellness-Journaling-Platform)@[7658437893...](https://github.com/riyaajosh37/Mental-Wellness-Journaling-Platform/commit/76584378930c10007efea9d2cf2dccfae0d6c164)
#### Sunday 2023-09-24 02:37:56 by riyaajosh37

Add files via upload

Our "Mental Wellness Journaling Platform" takes a holistic approach to mental well-being. It's powered by HTML, Bootstrap CSS, JavaScript (frontend), and Flask with Python (backend), offering:

Journaling for Self-Reflection: Users can express their thoughts and emotions through journal prompts. An AI chatbot provides personalized insights and coping strategies.

Mentorship and Support: Connecting users with experienced mentors for one-on-one guidance to overcome mental health challenges.

Combating Online Harassment: A user-friendly guide empowers users to confidentially report online harassment incidents.

Our platform provides accessible and user-friendly mental wellness support, promoting a happier, healthier future. Minimal installations make it easy to use and benefit from these essential features.

To run our website, follow these steps:

Install required packages: Run pip install -r requirements.txt.

Download language model: Execute python -m spacy download.

Start the server: Use flask run to launch the website.

---
## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[d93dfbc35c...](https://github.com/MidoriWroth/tgstation/commit/d93dfbc35c4b86435f9b436160e0d6c0670a8e28)
#### Sunday 2023-09-24 03:19:05 by Sealed101

Adds Summon Cheese (#77778)

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

Co-authored-by: san7890 <the@san7890.com>

---
## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[fc836593a5...](https://github.com/MidoriWroth/tgstation/commit/fc836593a51771fc6c06adfa28f81d3cd134a501)
#### Sunday 2023-09-24 03:19:05 by GuillaumePrata

Makes fanny packs be silent, others can't see what you put in or take out. (#78010)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Just like the syndicate toolbox and a handful of other items.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This is a blatantly stealth antag buff.

Pockets are 2 silent storage slots everyone has, so it is not adding
anything that antags didn't have access already.
But going from 2 to 5 small items can help a lot, also belts are a lot
smoother to use with their shortcut keys.

Love stealth antags, hate murderboners, gonna help my stealth boys not
be valid hunted because someone checked their chat logs from 10 minutes
ago and read that X player put Y contraband in their bag.

Or people that have some contraband names highlighted on chat... but no
one does that right.... right?
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

:cl:Guillaume Prata
balance: Fanny packs are now silent, no one will get a chat message
about what you put in or take out.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Aki Ito <11748095+ExcessiveUseOfCobblestone@users.noreply.github.com>

---
## [simony666/OOP](https://github.com/simony666/OOP)@[a82c353bf0...](https://github.com/simony666/OOP/commit/a82c353bf0cb725ccb69bfad50f323de5b153016)
#### Sunday 2023-09-24 04:08:22 by Zzz-anonymous

modify class + create module

modify previous annoying fucking Person class to compatible with my classes and adding annoying Schedule modules which waste my times for more than 4 hours and I haven't finished it!!!!!!

FXXXKKKKKKKKKK!!!!!
GOD DAMN IT!!!!!!!!!

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[b7c7bd732a...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/b7c7bd732ac8ca1c3d19d6705f5e578b5d2f3013)
#### Sunday 2023-09-24 04:11:26 by nikothedude

[TEST-MERGE FIRST] Wound refactor number two: Full synthetic support (#78124)

## About The Pull Request

Heavily refactors wounds AGAIN.

The primary thing this PR does is completely change how wounds are
generated and added - while the normal "hit a guy til they bleed" stuff
works about the same, asking for a specific type of wound, say, like how
vending machines try to apply a compound fracture sometimes, isnt going
to work if we ever get any non-organic wounds, which the previous
refactor allowed.

With this PR, however...
* You can now ask for a specific type of wound via
get_corresponding_wound_type(), which takes wound types, a limb, wound
series, etc. and will try to give you a wound fitting those
specifications - but also, a wound that can be applied to a limb.
* This will allow for a vending machine to apply a compound fracture to
a human, but a collapsed superstructure (assuming my synth wounds go in)
to a robot

There are now new "series types" and "wound specific types" that allow
us to designate what series are "mainline" and randomly generatable, and
what are "alternate types" and must be generated manually - you can see
the documentation in wounds.dm.

The behavior of limping and interaction delays has been abstracted to
datum/wound from bone wounds to allow just, general ease of development

Pregen data now allows for series-specific wound penalties. Example: You
could set a burn wound's series wound penalty to 40, which would make
wound progression in the burn category easier - but it would not make it
any easier to get a slashing wound. As it stands wound penalties are for
wounds globally

Scar files are now picked in a "priority" list, where the wound checks
to see if the limb has a biostate before moving down in said list.
Example: Wounds will check for flesh first, if it finds it - it will use
the flesh scar list. Failing that, they then check bone - if it uses
that, it will use the bone scar list. This allows for significantly more
modular scars that dont even need much proc editing when a new wound
type is added

Misc changes: most initial() usage has been replaced by singleton
datums, wound_type is now wound_types and thus wounds can accept
multiple wound types, wounds can now accept multiple tool behaviors for
treatment, wounds now have a picking weight so we can make certain
wounds rarer flatly,

This PR also allows for wounds to override lower severity wounds on
generation, allowing eswords to jump to avulsions - but in spirit of
refactoring, this has been disabled by default (see pregen data's
competition_mode var).
## Why It's Good For The Game

Code quality is good!

Also, all the changes above allow wounds to be a MUCH more modular
system, which is one of its biggest problems right now - everything is
kinda hardcoded and static, making creative work within wounds harder to
do.

## Changelog
:cl:
refactor: Refactored wounds yet again
fix: Wounds are now picked from the most severe down again, meaning
eswords can jump to avulsions
fix: Scar descs are now properly applied
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[88d7c856de...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/88d7c856def9b0dea795ca23b2bb9deb8b139e86)
#### Sunday 2023-09-24 04:12:29 by Jacquerel

Desouls Hivelord (#78213)

## About The Pull Request


![dreammaker_RJz4brjobM](https://github.com/tgstation/tgstation/assets/7483112/e5e4a3e9-ea6b-47f9-887c-3339d24d3fa8)

Replaces the sprite of the hivelord with a new one, in my continuing
quest to annihilate the old asteroid mob sprites.
A (never completed) asteroid mob resprite was actually my first PR, this
one is my 200th.
I am also planning on fucking with basic mob versions of these mobs some
time but the sprites can be atomised out.

In addition to replacing the old-ass MSPaint sprites, this PR also adds
a short death animation effect to the hivelord brood (from hivelords or
legions) which looks nicer than them just vanishing instantly upon
death.

Look at this video for an example of the animation:
https://www.youtube.com/watch?v=cKaskN5-y2A

## Why It's Good For The Game

Looks nicer.

## Changelog

:cl:
image: Hivelords have a new sprite.
image: Hivelord and Legion brood have a death animation.
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[cd34a10347...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/cd34a1034795a4718c443d04e58beddb2562553d)
#### Sunday 2023-09-24 04:16:04 by Sealed101

Polymorph belt blacklists several biotypes instead of allowing only organics (#78229)

## About The Pull Request

Title; this makes the belt able to morph into _more_ mobs, but _less
problematic/abusable_ mobs hopefully. It still only functions on
basic/simple_animals, however.

~~Headslugs get a `MOB_UNDEAD` bioflag to prevent morphing into them
completely. Though catching a sentient ling slug and morphing everyone
into it is funny, it's only funny the first 5 times someone does it.
(disclaimer: this is an approximation, i did not actually see a
polymorph belt in-game because i currently play miner and like 10 games
a week tops)
Arguably, this isn't ideal, but it's the closest we get unless we rename
`MOB_EPIC` or something into `MOB_SPECIAL` and let that one be the go-to
bioflag for mobs we don't want **fun** things happen to.~~
`MOB_EPIC` is now `MOB_SPECIAL`. Headslugs get that.
I think the alternative methow could use whatever the gold cores use to
determine what to spawn but that would shift the mobs available for the
belt even more and I can't be assed to figure out how _much_ of a shift
that would be. Dragons or slimes or lavaland mobs would be out, for
example. Don't really vibe with that.

Fixes headslug's description bit that discerns a sentient slug from an
AI one showing up on a dead slug. It can't move while it's dead, no
matter its mind/AI.

Also adds simple dmdoc comments to the defines to help discern a few of
them more easily. Non-quip text suggestions welcome.

## Why It's Good For The Game
- Resolves #77756
- Resolves #78227

More mobs available for the funny belt but less _fun_ mobs should allow
for more stable use of the damn thing. Arguably, some of the mobs that
have been found to be incompatible with the belt are simply lacking a
`MOB_ORGANIC` flag, some of them with no apparent reason. However,
blacklisting potentially problematic biotypes should be easier to design
the unwanted mobs around.
Also consistency, less all-ling stations, code clarity. Whatever.

## Changelog

:cl:
balance: polymorph belt now blacklists mobs that are undead, humanoid,
robotic or spiritual (in nature, not religiously), as well as megafauna
balance: however, this means that it works with more mobs that it should
logically work with, like slimes/bugs/lightgeists etc
fix: fixed headslug shenanigans with the polymorph belt hopefully for
good this time
fix: fixed headslug description mentioning its movement despite the slug
being dead
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[03df71a7c3...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/03df71a7c3c202f046ccc874b16cfacc3b198ef1)
#### Sunday 2023-09-24 04:23:39 by Hatterhat

John Splintercell: a gun that is only good for shooting out lights (#78128)

## About The Pull Request
adds the SC/FISHER lightbreaker self-charging energy pistol, which does
0 damage. As a joke.

![image](https://github.com/tgstation/tgstation/assets/31829017/84603fcd-dbc3-4857-a657-98c4bd34e881)


https://github.com/tgstation/tgstation/assets/31829017/97572baa-7421-4800-a60e-2db03f4adc6d

<details><summary>actual details, in case the video wasn't good
enough:</summary>

unless you shoot at light fixtures,

![image](https://github.com/tgstation/tgstation/assets/31829017/54092fbf-cbf6-4750-b2b8-37d643efba2a)
floodlights,

![image](https://github.com/tgstation/tgstation/assets/31829017/90b19560-fa25-471b-9f6f-3147c33e5c56)
or people with flashlights/seclites (even on helmets or guns) (it still
does 0 damage, it just turns off their lights. not permanently)

![image](https://github.com/tgstation/tgstation/assets/31829017/1a83c6f9-8fff-4035-aeeb-515319a3dd40)
it also works on crusher lights. and cyborg headlights. i don't have a
screenshot for it.
doesn't work on flares though.

also it can shoot past machines and lockers

![image](https://github.com/tgstation/tgstation/assets/31829017/8fb0a213-8e4a-42cc-9daa-eae5faf6ee77)
</details>
(also adds a variable for deciding how loud a dry fire sound is, in case
you want to make your gun's empty sound be less loud.)

## Why It's Good For The Game

Adds a silly little tool for silly little men who either really hate
lightbulbs or want to recreate the experience of being John
Splintercell, the lightbulb-assasinating secret agent from Fork Echelon.

## Changelog

:cl:
add: The SC/FISHER disruptor pistol, a very compact, permanently
silenced energy gun, is now stocked in Nanotrasen-accessible black
markets with a price generally somewhere between 400 and 800 credits.
Aspiring users are warned that it's really bad for trying to actually
kill people. Caveat emptor.
add: Guns now have a dry_fire_sound_volume variable, allowing for guns
to be less loud when trying to fire while empty.
fix: Closets and crates now properly count as structures for pass flags
again.
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[7de77d5c24...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/7de77d5c24da6cd1b1d7f01a62dde9b807ac415c)
#### Sunday 2023-09-24 04:26:26 by Fikou

decks of cards no longer have their own wielded var (#78260)

## About The Pull Request
we have the trait for that

## Why It's Good For The Game
Throughout UNDERTALE, we get treated to three story sequences (4 if you
include flowey's fakeout but that's not important). The first is the
intro story, telling the tale of humans and monsters, which shortly
thereafter leads into 201X, and Chara (Toriel's house has “An old
calendar from 201X.”) falling into the underground.

The second is the waterfall flashback, its contents taking place
immediately after the intro segment, as a voice (Asriel) finds the
fallen child.

And finally, the third takes place in the True Pacifist final boss.
We'll get to it in due course, and it will have its own section, but
let's address the first two. Regarding the intro, the first thought one
might have is that simply, while narratively relevant, is not a diegetic
presentation. However, We know that everything after the “201X” frame is
Chara's memory (from an outside perspective, that is,) and we also know
that UNDERTALE LOVES bringing the non-diegetic, the mechanical, the
game, INTO the narrative. Saving, RPG Stats, hell, even the
NarratorChara. Surely the intro can be as well? On top of this, what
does the intro do for the player, as the player? Well, aside from
setting the tone, the intro gives us some setting backstory. It's all
important context, and it certainly helps… but it being in the intro
sequence is not that important; It's all presented throughout the game
via diegetic signs, books, and expositional tortoise war heroes/angry
fish guardswomen. The second half is how Chara fell to the underground,
and while also setting tone and informing the player how their character
arrived. It also creates the false impression for the player that their
character is Frisk, feeding into UNDERTALE's meta narrative; “You are
not your character, and their happy ending is not yours.” If we weren't
playing Chara, this would have no narrative impact. The story beat fails
to land by showing us someone elses' character. But, sure. This could be
a purely non-diegetic intro sequence. Simply put, The 201X portion of
the intro sequence does not make sense from a diegetic or a storytelling
perspective unless we play as Chara.

Flashback number two is explicitly a canonical, diegetic flashback. It
occurs when Frisk escapes Undyne by falling down a massive pit… again.
This time, they land in the garbage zone, black out, and have a
flashback sequence of the first time Asriel found Chara. While serving
the main narrative by setting up Asriel as a character, furthering the
final twist of the meta narrative's pacifist route, and neatly
transitioning between overworld areas, it's also very explicitly
diegetic and cannot be dismissed as an intro sequence. With this in
mind, one question is raised. Why do we see this flashback? If the
player character is Frisk, this makes little sense, why would we see
someone else's flashback and not our own? Same thing applies for a Third
Entity, but even more abstract and illogical. What even are we? Sure,
you could say Chara is somehow attached to us/Frisk and that somehow we
get a flashback from Chara who is somehow knocked unconscious by Frisk
also being knocked unconscious. I used the word somehow three times.
That's not good storytelling. A simpler answer, at least in my view, is
that We Are Chara. When Frisk is knocked unconscious, we, being
ostensibly linked to them as a Spirit/Ghost/Reincarnation/Possessing
Dead Frisk/Demon/Insert fan-theory here/SOUL Fragment, have our only
connection to the world temporarily disabled, rendering us effectively
unconscious and prompting a flashback. Nothing weird with multiple
entities or memory sharing. The waterfall flashback is simply our
memory. Simple. The simplest answers are usually the correct ones.

<details>
<summary>DO NOT RESEARCH</summary>
The third sequence is a connection/extension of the first two, displayed
when we SAVE “Someone Else” during the true pacifist battle with Asriel.
To refresh everyone, here is the direct quotes, taken from the Wiki:


[SAVE]: Someone Else
Strangely, as your friends remembered you... Something else began
resonating within the SOUL, stronger and stronger. It seems that there's
still one last person that needs to be saved. But who...? ... Suddenly,
you realize. You reach out and call their name.
Asriel: “Huh? What are you doing...?”
s
It's at this point that the sequence plays. There's no narration, but we
see the sequence of interactions between Asriel and Chara. There are no
panels (except for the first) that don't contain the both of them.
Following this, we get:

You feel your friends' SOULs resonating within ASRIEL! [This is the
generic flavour text for saving all 6, before “Someone Else”, and
appears at the asterisk above as well]
[SAVE]: Asriel Dreemurr
Asriel:
> “Wh... what did you do...?”
“What's this feeling…? What's happening to me?”
Etc. etc. let me win…
During my first and consecutive playthroughs of UNDERTALE, I came to the
conclusion that Asriel's soul still “Had Some Chara In It.” Saving
“Someone Else” was saving Chara, and then you save Asriel Dreemurr after
the story sequence.

This interpretation no longer feels particularly potent to me, but in
the spirit of completeness I'll address it alongside the more reasonable
“You just save Asriel.” Assuming for a moment though, that we do “Save
Chara”, it's not unreasonable to assume that some of Chara's ‘essence'
(or whatever) was merged with Asriel's and by SAVING them, we're SAVING
the part of them that's inside Asriel.

But I don't like that theory.

Let's talk about SAVING Asriel for a moment.

What is the motivation for doing that? Why would we, in universe, wish
to SAVE him, something that the narration explicitly prompts us to do?
He tried and probably succeeded to kill us, at least once, he wants to
reset the entire timeline, he wants to erase all our friendships, all
our progress.

So, why? Well, it's simple. He's our brother. And we know better than
anyone that he's worth saving. And at the very least, there's something
about Frisk (who appears to have absolutely no personality) that reminds
him of Chara, of us. This is, by his own admission, weird;

Asriel:
“Frisk… You really ARE different from Chara. In fact, though you have
similar, uh, fashion choices… I don't know why I ever acted as if you
were the same person.”

To summarise.

The player SAVING Asriel Dreemurr works best if they are Chara, it
becomes Chara encouraging Frisk to SAVE Asriel too.

Asriel recognises Frisk as Chara throughout the True Pacifist battle
(And Beyond), despite his own admission that this is basically
unfounded. Something is causing this recognition.

In Alphys' true lab, there lies a dusty TV and a stack of VHSes. On
them, lie some of the last words Chara had ever heard from their father.

[Asgore] Chara! You have to stay determined! You can't give up... You
are the future of humans and monsters...

These tapes are not the first time they are heard. Sleeping in Toriel's
guest bed, we dream about them. Suffering a fatal injury, they echo in
our ears. Watching the tape is yet another reveal. It's the chilling
truth that in fact, the words we (if we die a lot) are so familiar with,
are in fact the words we hear on our deathbed.

Storytelling-wise, this reveal; like all the others, fails if we do not
play as Chara.

Aside from Asriel's dialogue, Chara's genocide Narration, and the coffin
in Asgore's basement, this is the only time we hear Chara's name. That
and, this following exchange.

[Flowey]
Hi.
…
Monsters have returned to the surface
Peace and prosperity will rule across the land.
…
Well.
There is one last thing.
…
One being with the power to erase EVERYTHING…
…
I'm talking about YOU.
…
So, please.
Just let them go.
Let Frisk be happy.
…
Well, that's all.
See you later…
Chara.
This, I think, is pretty explicitly definitive. Flowey comes to you. To
us. Tells us to take a deep breath and leave the happy ending intact,
then bids us farewell by our own name.

Regardless of anything else, this definitively proves Chara is the
entity with the power to reset everything by the end of True Pacifist
(Which is a power we have). Flowey positively identifies us as “Chara”,
despite his mistake we discussed in 3C. He's not talking to Frisk,
because he refers to them in the third person.

He is talking to Us. Chara.

I don't want to discuss Flowey's use of “Chara” in Genocide all that
much, because the counter-argument is blindingly simple.

“By the time Flowey first says that name, Chara has overtaken Frisk by
feeding on the power we create for them.”

Of course, under PlayerChara, Flowey's lines still make sense, and
arguably more.

Implications
At this point, I believe the evidence is sufficient to support the
theory. With this in mind, I want to discuss the implications this has
on the narrative and meta-narrative. This is where all those funny
glossary terms come into play.

The pacifist route in UNDERTALE, as discussed above, is textually quite
simple when accepting PlayerChara. The meta-text is also relatively
simple. Meta textually, the Pacifist Route is a dissection of the
suspension of disbelief, examining how we emotionally place ourselves
within fictional worlds, and are often-times torn away from those worlds
as the game comes to an end, left wanting the true emotional connection,
wanting a happy ending that cannot be good enough for us because we're
real and it's not. The reflection of this meta narrative in the textual
narrative, quite naturally flows. We, Chara, want a happy ending. But we
can't have it, it's not our happy ending. We're gone. We've been gone a
long time. Frisk's happy ending can't be good enough for us, because we
won't be around to see it. So, we're left with a choice.

To let Frisk live happily? To accept an ending that might leave us
emotionally wanting, yet preserves our emotional journey?

To reset? To refuse an ending and satiate our emotional emptiness, yet
destroy that very emotional journey we took in the process?

The choice is the same. There is practically no separation between the
diegetic and the meta.

“Can a happy ending be good enough for you?” This question applies to
us, as the real world player running UNDERTALE.exe on our computer, and
us, Chara, the long deceased human who can do little but watch as Frisk
lives the life they wish they still had, or can destroy everything for a
hollow mimicry of that very life.

This message, however, breaks down under one specific circumstance.
Where we force a Third Entity into the mix. This one decision fractures
the cohesion and creates a meta-textually dissonant mess. Now, all of a
sudden, “Can a happy ending be good enough for you?” no longer runs
parallel through both narratives. There is no reason for the Player
Entity to wish to remain, the happy ending should automatically be good
enough because it's the happy ending. Meanwhile, Chara, despite being an
inextricable representation of “A happy ending I can't achieve,” gets
absolutely nothing to do with this meta-narrative because they're just…
not you.

“we are mario in Super Mario 64, but when he says "Thank you so much for
playing my game!" that doesn't mean we aren't still playing as mario” -
PopitTart

This is where things get weird. See, in the Genocide route.. Well, we
see Chara. On Screen. Talk to us.

Now, it can easily be argued that this completely shatters the theory,
but I would disagree. I'm going to endeavour to present a textual
explanation (or two) for this. But first, I want to dissect the
meta-text here.

Now, I'm sure the idea that “The Genocide Route's Meta-Narratve is
Fading Emotional Investment and the way emotional connection with video
games can lead to the very sabotage of that emotional connection” is not
revolutionary. However, what's conspicuously absent from all of the
third entity theorising is the way that this meta-text is mirrored in
the textual narrative.

Once satisfied with a game, having extracted all lines of dialogue and
stat boosts, once reaching all endings, a user will close the game down.
And at some point, perhaps to make room for a new game or perhaps on a
new device, will leave the game uninstalled, either deliberately, or
simply as a consequence of time.

Textually, what happens in the Genocide ending?
Now we have reached the absolute.
There is nothing left for us here.
Let us erase this pointless world, and move on to the next.

The world is destroyed. So much is left unanswered here.
Who is Chara talking to?
Where did Frisk go?
How do they have this much power?
Why would they want this?
If we ‘corrupted' them, what the hell does that even mean?
What is Chara?
For now, let's talk about who Chara is talking to.

The simplest answer is “Perspective switch.” Suddenly, we're not Chara
anymore, now we are Frisk. This meets all the dialogue options and even
vaguely mirrors the meta-text. It also manages to avoid bringing a third
entity along and so is automatically better! But, I find myself still
not fully enjoying this idea.

Remember what I said about Occam's Razor?

I think there's another option. One that doesn't involve three entities,
or even two entities, just Chara. One that mirrors the meta-text to a
degree only Toby Fox could pull off. It's a weird one, and I don't fault
you if you don't get it on your first read, but bear with me here,
because things are about to get

A little
Fucking
Abstract

Let's discard any and all pre-concieved notions of anything and hold one
singular truth above all else. “Chara Is The Player.” What does this
mean for this cutscene?

Well… it means the player is talking to…

THe player?

It also neatly answers the question of motive, so let's throw that out
the skeleton-shaped hole in the window for now.

If the player is talking to the player, this frames Chara's words in a
whole new light.

Every time a number increases, that feeling… That's me. “Chara.”

This line becomes explicitly literal. The Chara on-screen is literally
the player's feeling of satisfaction watching stat increases. But this
is all meta-textual, right? What does this mean for the textual
narrative?

Here's the thing. It can't mean anything, yet means everything.

There is no way to reconcile the fact that a Textually Real character is
directly talking about what the player feels when playing a game to
completion. The barrier between Meta and Textual no longer exists. It
can't. Not here. And with this revelation, everything begins to make
sense.

Your power awakened me from death.

Our power. Our desire to complete UNDERTALE awakens Chara from death.
They become startlingly real. We imbue this fictional character with the
real world desire to consume fiction, destroying enemies and worlds as
we go, increasing our power and our stats. Video Game Accomplishments.
And UNDERTALE has just finished being consumed.

My “human soul”... My “determination”... They were not mine, but YOURS.

Chara, the textual player, acknowledges the meta-textual player's
control over the game world. A control that we surrendered. By engaging
in UNDERTALE in a fully immersed way, we have fed the Diegetic character
that is our player character, Chara. This has continued until we haul
ourself out of the Internal Mode and into the External Mode, revoking
our immersion to make the consumption of content easier, to distance
ourself from the killing.

Raising our LV.

The more we distance ourselves, the less real UNDERTALE's world appears
to us. Once it's done, we're ready to erase this pointless world and
move onto the next. There's just one problem. UNDERTALE knows about us.
It knows we exist and it will abuse that to convey meaning. By revoking
our immersion in UNDERTALE, we end up shattering the barrier between
Meta and Textual, and this occurs because revoking our immersion is a
diegetic decision. Without this barrier, WE, as a character, gain
control of UNDERTALE and use this external mode control to

Erase the world. To uninstall.


This code doesn't actually work, of course. That was pretty obvious by
the fact that it didn't delete your game. But still, this exists in the
code that makes the game window shake when Chara attacks it. This is,
quite literally, intent for Chara to delete UNDERTALE. If you didn't
think Chara was capable of uninstalling your game before, you should
now.

Who is chara talking to?

Us.
How do hey have this much power?

We gave it to them. We Are them, and we deleted UNDERTALE when we were
done with it.
Why would they want this?

We wanted to move onto a new game.
What is Chara?

Us. ( I'll come back to this.)
But wait! What about soulless pacifist?
Well, at that point, you've surrendered Frisk's SOUL to Chara, as in,
you the real player has revoked your emotional attachment to UNDERTALE
and accepted that Chara can have control over the game. You've revoked
your immersion AS Chara, you no longer see yourself a Chara and as such
Chara becomes their own being. You've surrendered, basically. But they
let you play through it. Because why not. You might get attached again,
but that's fine. All that means is that the happy ending that was once
Frisk's, that you, the player, and you, Chara, both once lamented not
being able to live, has now been surrendered to Chara. A warped,
completionist, Chara.

You don't get your happy ending. But Chara does.

You don't even get the solace of knowing someone gets their happy
ending. Because Chara gets it.

Frankly, outside of being “The Player”, I don't think the exact nature
of “Chara” is that crucial. My personal thought is that they're a SOUL
fragment, absorbed by Frisk when they fell on Chara's grave (Frisk could
absorb a human SOUL fragment because said fragment was part monster
SOUL). This fragment gives Frisk the final edge of determination needed
to SAVE.

But, ultimately, that's little more than a fanfiction. And frankly, I
think that's okay. Not everything needs to be impenetrable, as long as
there's enough there to build a stable foundation.

I'd also like to address the nature of SAVING quickly, specifically the
normal version, not the Asriel fight version. People have asked “Why do
we save if it's Frisk's SOUL.” There could be many reasons. Frisk might
just defer control to us. Because we're pushing Frisk over that
Determination limit, we might be privileged to have that control.
</details>

## Changelog

not player visible

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[0706253d5c...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/0706253d5c925442d2a0d81db43851444b2ca27b)
#### Sunday 2023-09-24 04:27:52 by JupiterJaeden

Balance: Removes anti-drop implants for nukies (#78275)

## About The Pull Request

Removes anti-drop implants being available in nukie implants. Also
rebalances the cybernetic implants bundle to cost 20 TC (value of 24 TC)
since anti-drop has been removed from it.

## Why It's Good For The Game

This is one of the rare few nerf PRs where I was not the one who got
KILLED by the broken OP shit but rather the one using it. I recently
played a nukie round (after hearing that anti-drop had been added) where
I took modsuit shield, dsword, and anti-drop. I got separated from my
team and then proceeded to solo murderbone half the fucking station,
resist MULTIPLE disarms that would have otherwise been successful, get
the disk alone, and nuke. I only had to stop to heal _once_ and honestly
I probably would have been fine if I didn't.

Anti-drop dsword is _insanely_ powerful. Shielded dsword nukies were
already strong enough but were at least somewhat balanced insofar as
there were several ways you could still reliably disarm them and
therefore open them up to more attacks. But now (after
https://github.com/tgstation/tgstation/pull/77330 which added the
anti-drop implants to nukie uplink) you can have shielded anti-drop
dsword nukies. Add stims and some explosives to deal with any static
fortifications the crew might make (like firelock crush relays), and
with a semi-robust player you essentially have a murderbone machine who
can't be killed by any regularly accessible crew counters short of point
blank suicide bombing. We should not have a default nukie loadout that
can only be reliably, regularly countered by a fucking bomb. Especially
since the crew's main easily accessible ballistic is now being nerfed as
well. (https://github.com/tgstation/tgstation/pull/78235)

EDIT: I'd also like to point out that we already don't allow hulks to
use dswords for many of the same reasons.

## Changelog

:cl:
balance: removed anti-drop implants from the nuclear operative uplink
balance: removed anti-drop implant from the nukie implants bundle and
changed its cost to 20 TC
/:cl:

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[9c121327a9...](https://github.com/vampirebat74/lobotomy-corp13/commit/9c121327a9b71232e256e18ff109b1c96df65d36)
#### Sunday 2023-09-24 04:33:58 by Mr.Heavenly

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes suit check in assimilate() proc

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes dismembering

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

breach is more dangerous

compiles

bug fix

fixes simple mob

bug fixes

Panic fixed!!!!

stuff

wayward records

Update code/modules/paperwork/records/info/he.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

attribute bonus

requested changes

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[4041148230...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/4041148230d459d7dd6a84f126d737339386e2c2)
#### Sunday 2023-09-24 04:34:11 by Lufferly

Supermatter Delamination Balance Changes (Real) (#77996)

## About The Pull Request

lord forgive me I fucked up the merge conflict

The supermatter delamination countdown timer (how long it takes to go
boom-boom after hitting 0 integrity) has been lowered from 30 seconds to
13 seconds.
Removing a sliver from the supermatter, the traitor objective, will
further lower that down to 3 seconds.
Changes the wording on the mood effects from the supermatter
delaminating slightly.
The crystal uses SPAN_COMMAND on its final countdown, which means it
talk bigger.

## Why It's Good For The Game

Currently I feel that the supermatter delamination countdown overstays
its welcome. Ideally it provides tension to get the hell out, or perhaps
to make a risky last second play to try and save the supermatter.
However right now its at 30 seconds, which gives no danger of staying in
engineering right up to integrity 0, and keeps the tension at a high
note for too long, almost to the point of awkwardness. 13 seconds is a
good balance between get-the-fuck-out while still giving some leeway for
engineers to escape and crewmembers to jump in lockers, and feels quick
enough to give that danger that the supermatter should provide.
Additionally, removing a sliver from the supermatter lowers the cooldown
to 3 seconds. Right now this is one of the harder tasks a traitor can be
tasked with, while giving relatively little payoff sabatoge-wise. To the
point where I have seen engineers just let the traitor do it, as the
debuff it gives to the supermatter is minor. Now it makes the
supermatter delaminate almost immediately after hitting 0 integrity,
which means it will likely catch some engineers in the blast if a
traitor did it stealthy. This also makes it more risky to try and fix a
delamination if the engineering/security team did not stop the sliver
from being removed. All meaning succeeding at this task should be more
rewarding and damaging.
Finally the mood descriptions for the mood effects you get when a
supermatter delaminates have been changed. Currently they are pretty
gamey, and represent what the player might be thinking more than their
character. Additionally they were not very descriptive of where they
came from, which could be confusing.

## Changelog

:cl: Seven
balance: The supermatter delamination countdown has been lowered from 30
to 13 seconds
balance: Removing a sliver from the supermatter further lowers that down
to 3 seconds
balance: The supermatter crystal uses bigger text on its final countdown
spellcheck: Some supermatter delamination related mood descriptions have
been edited to explain the mood effect better
/:cl:

---------

Co-authored-by: Shadow-Quill <44811257+Shadow-Quill@users.noreply.github.com>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[e6e9a91809...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/e6e9a91809ace3b6e5bd44268758b9799f2f041a)
#### Sunday 2023-09-24 04:37:13 by ArcaneMusic

Conveyor Belts are now easier to extend and have screentips (#78278)

## About The Pull Request

Conveyor belt **stacks** now have a better examine text.

Using a conveyor belt stack on a placed conveyor belt now extends the
conveyor belt by 1 tile, linking to it's ID automatically, and makes for
much easier building of conveyor belt setups.

Conveyor belts now come jam packed with screentips.

I've also added the default tile place sound to the usage of conveyor
stacks to provide a tiny bit of audio feedback when placing new conveyor
belts.

## Why It's Good For The Game

Conveyor belts are just mind-numbingly annoying to use in a regular
round, and trying to set up a new conveyor belt setup is confusing if
you don't have ultra specific information about how to make one before
you even start. Hell, I remember I had to add the *real* construction
steps to the wiki like 6 years ago and I STILL hear people getting
confused about how these works.

This improves their ease of use, while also making everyone sleep a
little easier for those of us who use them.

## Changelog

:cl:
qol: Conveyor belts now have screentips and a better examine tip to
teach you how to set one up properly.
qol: Using a conveyor belt stack on a placed conveyor belt will extend
the conveyor belt to the output of that conveyor belt.. You can use this
to place fully integrated conveyor belts much easier now.
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[ab8940dca8...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/ab8940dca8645f0db52b6011a8e1b4b841110a3c)
#### Sunday 2023-09-24 04:45:16 by Hatterhat

buffs embed pulling with hemostats, allows wirecutters to pull embeds too (#78256)

## About The Pull Request
- Wirecutters or tools with wirecutter behaviors are now valid for
plucking embeds.
- Pluck speed no longer **starts** at 2.5 seconds, which is a pretty
dang long time, especially if you have bad embed RNG. I'll do the math
and run some more tests in the morning.
- Wirecutters have a speed malus in regards to plucking embeds. I should
probably make it worse to account for, like, jaws of life or something.
- Plucking embeds with wirecutters now hurts! It hurts way less than
ripping it out with your hands, but it still hurts!

For comparison's sake, bare-handed throwing star removal compared to
possible tools.

![image](https://github.com/tgstation/tgstation/assets/31829017/96730fa5-77b8-4f31-83ba-48d36e4e419b)


## Why It's Good For The Game
Embeds kinda suck to deal with. This is intentional - I get that.

However, hemostat pulling is kind of... kind of bad. Awful, really. 2.5
seconds is a lot of time. I know it's not supposed to be the best
option, but if you've got a tool, I'd at least like to think it'd be
slightly less bad than shoving your fingers into your wound?

## Changelog

:cl:
balance: Pulling embedded items e.g. shrapnel with hemostats is now a
lot faster, and scales appropriately with toolspeed.
balance: You can now pull embedded items with wirecutters, at a speed
penalty.
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[0e17d76cdd...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/0e17d76cdd403b951febebe9fc28ab40179c6e0b)
#### Sunday 2023-09-24 04:56:42 by Jacquerel

You can do revival surgery on Ian (#78288)

## About The Pull Request

Allows you to perform revival surgery on any mob which is organic or
looks humanoid.
This means yes: Corgis, Goliaths, ~~Syndicate mobs~~ not those because
they spawn human corpses and delete themselves.
No: Slimes, Ghosts, General Beepsky.

Splits revival surgery into a subtype used for "mobs" and a subtype for
"mobs with brains" as the former don't have any brains to damage.

Additionally by special request, Ian can now wear an eyepatch and will
automatically put one on if he is brought back from death.

![image](https://github.com/tgstation/tgstation/assets/7483112/eff91bf6-4f80-4d8b-9062-1a5d4af85d39)

## Why It's Good For The Game

Currently you revive dead pets either by creating a magical reagent out
of holy water or by buying a mining item which also brainwashes them,
however reasonably our skilled medical team should be able to put a dog
back together and now can.
When you fuck up one of the stages of Tend Wounds on a kitten and stab
it to death with your scalpel, now you can fix it.
Expands the possibilities of vetinerary roleplay.

## Changelog

:cl:
add: Many kinds of mobs can now be brought back to life through revival
surgery.
add: Dogs can wear eyepatches.
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[ca9e01a38f...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/ca9e01a38faa7c28a45b545d40cc0c985704328d)
#### Sunday 2023-09-24 05:03:50 by carlarctg

Gun kits don't need cable coil or tools, halved crafting time (#78419)

## About The Pull Request

Crafting R&D guns from gun kits no longer requires tools or cable coil.
The decloner and energy crossbow still need reagents.

Halved R&D gun crafting time. 20->10 seconds.

## Why It's Good For The Game

These changes were made a long, long while ago and honestly while I
understand gun kits I don't understand why it was made So. Annoying. To
make the fucking guns once you got everything ready. It makes it a total
annoyance. You spent 40 minutes getting all the tech for it, you
shouldn't have to also get tools and cables and wait 20 seconds standing
still.

Anyone who has played ingame like any time after that change can attest
how underused any R&D gun is now. X-ray laser guns still DESTROY blobs
but people don't even THINK about them because of the dumb annoying
recipe (alongside RnD being a pain now).

Simply put this just. Makes life easier for security officers. And
reduces tool dependency.

## Changelog

:cl:
qol: Crafting R&D guns from gun kits no longer requires tools or cable
coil. The decloner and energy crossbow still need reagents.
qol: Halved R&D gun crafting time. 20->10 seconds.
/:cl:

---
## [BangingDonk/tgstation](https://github.com/BangingDonk/tgstation)@[68b6c1fa75...](https://github.com/BangingDonk/tgstation/commit/68b6c1fa753a4ae33cbe2d2a603041db4abdc7cf)
#### Sunday 2023-09-24 05:48:06 by RikuTheKiller

Rounded supermatter delamination times to 5 seconds, restored old mood messages (#78335)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Makes the supermatter delaminate in 15 seconds instead of 13 and 5
seconds instead of 3 if a sliver has been taken from it, mainly to
please perfectionists (me and some others who commented on the PR) as
well as giving people at least a chance to escape delam round removal.

I don't like it when flavorful text is replaced by bland and
not-as-funny alternatives.
Also, how the hell is it gamey for staff to know the engineers are in
charge of the power?
It's honestly more gamey for them to know what a resonance cascade or
supermatter delamination is, so I'd say you've done the opposite of what
the goal was with the message changes on top of making them less fun in
general. I disapprove.

Oh, yeah, and the SM now reports the times correctly due to it reporting
them every 5 seconds, meaning people would only see the 10 second
announcement. Now there is going to be a 15 second announcement as well.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Watering down messages to be bland is just, like, less fun, ya know?
I didn't see a single person in support of the message changes apart
from the PR author, everyone else was just complaining about them,
including myself.

Also, several people mentioned the fact it could just be 15 instead of
13 for a nice round number, including myself. I also made the sliver
delamination time 5 seconds instead of 3 seconds because you pretty much
can't get out in time, especially if the game is laggy. 3 - 5 people
being round removed because of one traitor objective with no chance to
escape it is just bad gameplay.

Oh, and, bugfix good, I suppose.

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
balance: Supermatter now takes 15 seconds to delaminate normally and 5
if a sliver has been taken from it. Gives a little more time to escape
in the case of the sliver and also evens out the times to please
perfectionists.
fix: Supermatter now accurately reports it's detonation time.
spellcheck: Supermatter mood descriptions have been reverted back to
their old, more flavorful selves.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[9ccd6ecd74...](https://github.com/mamh-mixed/microsoft-terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Sunday 2023-09-24 05:50:34 by Mike Griese

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

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[9dbf819e8a...](https://github.com/Drulikar/cmss13/commit/9dbf819e8a0512809c54ae8aae43749265a939bf)
#### Sunday 2023-09-24 06:03:41 by forest2001

Codebook Optimisation (#4393)

# About the pull request
For as long as we've had a codebook it's been a pain in the arse to
read/synchronise from a staff POV. With this, codebooks will all share
the same codes per-faction.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Makes events that use codebooks actually viable.
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: Codebooks are now faction based rather than individually unique.
/:cl:

---
## [mintme-com/core-geth](https://github.com/mintme-com/core-geth)@[5161c8d924...](https://github.com/mintme-com/core-geth/commit/5161c8d924803f941c75585b77b43e41bf240f39)
#### Sunday 2023-09-24 06:12:38 by meows

contracts/checkpointoracle,contracts/checkpointoracle/contract,params/types/genesisT: run 'go generate ./...' with partial success

A few things I learned along the way this evening.

- solc in path must be 0.6.0 or some mysterious upper
bound less than the latest available versions that I
also tried.
- solcjs is not solc. npm install solc installs solcjs
which is like solc but is not solc.

All of this partially fixes an error which looked like this.

go generate ./...
protoc-gen-go: no such flag -import_path
--go_out: protoc-gen-go: Plugin failed with status code 1.
accounts/usbwallet/trezor/trezor.go:45: running 'protoc': exit status 1
Error: Source file requires different compiler version (current compiler is 0.8.5+commit.a4f2e591.Linux.g++) - note that nightly builds are considered to be strictly less than the released version
 --> contract/oracle.sol:1:1:
    |
           1 | pragma solidity ^0.6.0;
         | ^^^^^^^^^^^^^^^^^^^^^^^

              contracts/checkpointoracle/oracle.go:20: running 'solc': exit status 1

The error now looks like this

go generate ./...
protoc-gen-go: no such flag -import_path
--go_out: protoc-gen-go: Plugin failed with status code 1.

Maybe we don't even want these changes. I don't know.
I just want the command to work for the sake of order
in the universe.

But seriously
- maybe we should upgrade the Solidity version pragma too/instead?
- maybe proto-gen-go actually wants a different version than 'latest',
  (which is what 'make devtools' installs).
- maybe we report the issue at ethereum. their trezor.go looks same
  same.

Goodnight, to dream of green lights.

Date: 2022-12-20 19:40:04-08:00
Signed-off-by: meows <b5c6@protonmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[06eda01ea0...](https://github.com/tgstation/tgstation/commit/06eda01ea08414b0574ddd84222b4de0bacf2db2)
#### Sunday 2023-09-24 07:27:45 by carlarctg

Added the Hippocrates bust to medbay heirlooms (#78121)

## About The Pull Request

Remade from #77961 because coders dont like bloat in prs

Added the Hippocrates bust to medbay heirlooms. Paramedics don't get
one.

You can now swear the Hippocratic oath with these busts! It'll give you
pacifism but nothing else. The process is reversible.

There's a very small chance that the Hippocrates bust was once wielded
by a certain German doctor. This chance is increased for coroner
heirlooms.

## Why It's Good For The Game

> Added the Hippocrates bust to medbay heirlooms. Paramedics don't get
one.

I got this idea and I just couldn't get it out of my head, it's too
funny. Paramedics don't get one because they're powergamers and laugh at
the Oath, and also it doesn't feel like a paramedic thing.

> You can now swear the Hippocratic oath with these busts! It'll give
you pacifism but nothing else. The process is reversible.

This is just a little fun thing you can choose to do, i think it'd be
cute to see doctors swearing the oath in medbay. Plus it's reversible
which can be even funnier depending on the occassion.

> There's a very small chance that the Hippocrates bust was once wielded
by a certain German doctor. This chance is increased for coroner
heirlooms.

We DO already have precedent for references with the entrenching tool
after all. The buff isn't all that special in reality, getting a medical
hud while in your hand is... basically irrelevant for the roles that
literally spawn with a med hud? It's just for accuracy and rule of
cool's sake.

## Changelog

:cl:
add: Added the Hippocrates bust to medbay heirlooms. Paramedics don't
get one.
add: You can now swear the Hippocratic oath with these busts! It'll give
you pacifism but nothing else. The process is reversible.
add: There's a very small chance that the Hippocrates bust was once
wielded by a certain German doctor. This chance is increased for coroner
heirlooms.
/:cl:

---------

Co-authored-by: Arturlang <24881678+Arturlang@users.noreply.github.com>

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[b390525fc5...](https://github.com/mc-oofert/tgstation/commit/b390525fc5543db5fcdb47869b9297cf637239fc)
#### Sunday 2023-09-24 08:07:45 by Rhials

Adds a handful of Ninja Hacking MODule interactions of varying usefulness (#77707)

## About The Pull Request

Adds a few new interactions with the Ninja's ~~right click multipurpose
trolling tool~~ Hacking MOD Module. These new effects are not tied to
objectives and are geared towards expanding the ninja's access,
disabling equipment, and giving them more ways to punk the crew.

### **Useful additions**
Ninjas can now hack open **windoors** and **elevator control panels**.
Both trigger emag_act() when hacked, opening in the case of the windoor,
and disabling the access restrictions _(and also maybe the safeties)_ in
the case of the elevator controls.

**Buttons** can also be emagged by the hacking modules, which removes
their access restrictions.

Hacking a **camera** will now EMP it, disabling it for about 90 seconds.
This can especially useful when trying to complete objectives, and works
better than smashing the cameras with your sword or lugging around
tools.

**Firelocks** can be right-click opened now too, thanks to the hacking
MODule.

**Energy guns** of all variety, useless to a ninja since they can't use
ranged weapons, can now be drained and used to charge your suit. This
takes a brief do_after to complete, so pulling it off mid-combat may be
as risky as it is stylish.

### **Being a nuisance**

**Vendors** can be hacked, expending some charge to trigger the "throw"
wire, making it launch inventory at anyone who passes by.

You can now hack **simplebots**, expending some charge from your suit to
overload and detonate them. It's faster than tipping, and far more
tragic. Sentient simplebots should take care when a ninja is around.

### **Sabotage opportunities**

The **recycler** can now be hacked. This takes 30 seconds and notifies
the AI, just like the communications console hack. Completing the hack
will emag it. That's it.

Hacking the **tram control console** will trigger an extended Tram
Malfunction event, and can be repeated after the event is done. This can
only be done to the "main" tram of the map, which I forsee will be an
absolute nightmare to complete on highpop tramstation.

Neither of these, presently, contribute towards any objectives. They can
be useful for diverting attention, but I see them more as ways for an
overachieving ninja to flex or continue the chaos after their objectives
are complete.

### **OH ALSO**

Hacking open doors costs energy. This really shouldn't be an issue just
remember to recharge sometimes.

The charge drains and do_after lengths for all of these were chosen on
vibes. In all honesty I think the drainage values don't _really_ matter,
due to how easy recharging is, but I had a hard time settling on how
long some of these hack do_afters should take (even if I know they
probably won't matter either).

## Why It's Good For The Game

Being able to hack open airlocks but not windoors always irked me. I
figured that they would be openable like any other door, and that losing
their status as a "-1 dash charge gate" wouldn't be a big enough balance
change to spark arguments. The same philosophy extends to buttons and
elevator controls.

Sapping power from eguns expands on the list of sources energy can be
siphoned from. You can also use it to disarm opponents (like the badass
ninja you are), take emergency charge from a recently-gored officer's
disabler, or dunk on security by draining their entire armory.

Hacking simplebots, vendors, and by extension elevator lifts (since that
also disables the safeties!) give opportunities for minor sabotage. Not
meant to be super disruptive, just a bit silly and annoying for the
crew.

The recycler/tram hacking in particular are meant to be bonus goals,
only sought out by the ballsiest (or more likely boredest) of ninjas.

I see all of these additions as expanding upon the current abilities of
the ninja (not really making them much more powerful, just expanding
their flexibility), or providing more interactions to have fun (and
antagonize the crew) with when not mainlining their objectives.
## Changelog
:cl: Rhials
add: Ninjas can now temporarily disable cameras with the Ninja MOD
right-click hacking ability.
add: Ninjas can emag windoors, elevator controls, and buttons with their
hacking ability.
add: Ninjas can drain the power from energy weaponry, adding the charge
to their MODsuit.
add: Ninjas can now hack simplebots, overloading and detonating them
after a brief delay.
add: Ninjas can now hack vendors, causing them to eject their inventory
at people.
add: Ninjas can now hack the recycler, which notifies the AI and emags
it once complete.
add: Ninjas can now trigger an extended tram malfunction by hacking the
tram control console.
add: Ninjas can now hack open firelocks (temporarily) with right-click.
balance: Hacking open doors with the Ninja Hacking MODule will subtract
a paltry amount of energy from your suit.
/:cl:

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[2d4d23dbf1...](https://github.com/mc-oofert/tgstation/commit/2d4d23dbf1e2cc23ed2046534011561e443060f7)
#### Sunday 2023-09-24 08:07:45 by Timberpoes

Replaces the poster and graffiti objectives with assault and early steal & destroy ones. (#77029)

## About The Pull Request

With the blessings of @Watermelon914 I am removing the two objectives
for placing posters and spraying graffiti.

These old objectives are not dead. Their items have moved to the
Badassery section of the uplink.

A box of 3 demotivational posters can be bought for 1TC with 0 rep.
The spraycan can be bought for 1TC with 0 rep.

In their place comes one new objective and one extended objective.

The new objective is Assault a Crewmember. This objective requires you
to attack the specified target 2-5 times (random on objective
generation). It tallies from any attack that filters through the
`/datum/element/relay_attackers` element and has an "attacker"
associated with it.

Although it asks you not to kill the other player, it doesn't fail if
you kill them.

I have expanded the low-risk theft objectives with items like a mime
mask, lawyer badge and a fake moustache (commonly on cooks).

Finally, I've added a very low level set of steal-and-destroy objectives
aimed at some items that will require a bit of basic breaking and
entering, and the destruction of which may hurt crew morale.

```
/datum/objective_item/steal/traitor/donut_box
/datum/objective_item/steal/traitor/rpd
/datum/objective_item/steal/traitor/space_law
/datum/objective_item/steal/traitor/granted_stamp
/datum/objective_item/steal/traitor/denied_stamp
/datum/objective_item/steal/traitor/lizard_plush
/datum/objective_item/steal/traitor/moth_plush
/datum/objective_item/steal/traitor/insuls
```

This PR also fixes clown shoes missing a proc override to allow them to
actually register as a theft objective.


![image](https://github.com/tgstation/tgstation/assets/24975989/775d46cf-f40a-43e5-9bf1-3aa4a31d436e)

![image](https://github.com/tgstation/tgstation/assets/24975989/66c77815-1f2b-4dfb-99c6-b8f2e0061654)

![image](https://github.com/tgstation/tgstation/assets/24975989/85d3878a-c598-4ec0-9bb1-920380a004c6)
## Why It's Good For The Game

Basically my discussion with Watermelon focused on the idea that the
graffiti and poster objectives weren't really crimes. They baited
antagonists into very passive play early-game.

These new replacements encourage a more antagonistic playstyle. Starting
fights plus B&E are two bread-and-butter play paradigms for antaggery.

Giving a few early game theft + destroy options with a mix of impactful
items (like insuls and RPDs) versus more symbolic or emotive items
(plushies, donut boxes, Cargonia stamps) gets antagonists out and about
in the station, warming themselves up.

And having an objective to assault players (even if you don't kill them)
allows cheeky antags with a penchant for shittery to start fights with
players and start genuinely impacting the shift, involving sec and
drawing players into their antaggery.

Both of these natually ease players into the more substantive theft and
murder objectives.

The existing spray and posters are actually thematically super cool.
Traitors now have even more access to them since they can be bought for
1TC per spraycan/3-pack of posters. This lets antags with TC to spare
run gimmicks around them and adds extra fun to the Badassery section.
## Changelog
:cl:
del: Traitor objectives to place posters and graffiti the station have
been removed.
add: The items associated with the poster and graffiti objectives can
now be purchased from the Badassery section of the uplink. The posters
come in a box of 3 for 1TC, and the spraycans are 1TC each.
add: Adds a new Assault traitor objective, requiring you to the attack
the target a few times without needing to kill them. Earn TC and
reputation by starting barroom fights and bait players into escalation
battles for fun and profit.
add: Expands low-risk steal objectives to include the Chef's fake
moustache, Lawyer's badge, and Mime's mask.
add: Adds brand new shift start Steal & Destroy objectives for early
breaking and entering. Smash your way into a sec checkpoint to grab a
Space Law book, engineering to grab some insulated gloves or the psych
office to kidnap their moth plush.
fix: Fixes an issue where the steal clown shoes objective would never be
valid.
/:cl:

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[3bc54e7869...](https://github.com/mc-oofert/tgstation/commit/3bc54e78697b1bf6845605028085f30cabed9d40)
#### Sunday 2023-09-24 08:07:45 by Jacquerel

Mining mob tweaks (#77763)

## About The Pull Request

~~I wanted to do this after #77700 (wow cool numbers) but nobody has
merged it yet despite how simple it is so i'll just hope they don't
conflict.~~ Thanks san

I'm fucking about with mining mobs with the intention of making them
more interesting but not necessarily towards making mining _harder_, but
some of these changes unquestionably have done so.

These changes are mostly in response to feedback about Watchers who are
definitely significantly more threatening than previously, although some
of this is user error.

- Watchers are annoying when traversing lavaland because they use their
ability on you instantly upon acquiring a target, if you are trying to
escape other fauna this quickly becomes deadly.
- A lot of players don't really realise what the overwatch ability is
actually doing and so just complain about getting machine gunned.
- If you _do_ react properly to the ability it still makes fighting them
take a lot longer than it used to.
- The "look away" icon is hard to see in the dark sometimes

To ammeliorate these factors I have:

- Reduced watcher health by ~20%
- Display an alerted graphic over the head of the watcher every time you
trigger the overwatch.
- Multiple watchers now won't overwatch you at the same time (this made
the "penalty" volley essentially become instant death)
- The "look away" icon is rendered above the lighting plane so you can
always see it
- Added a new component which tracks how long a mob has had a specific
target.
- - Watchers will now only Overwatch you if they've seen you for at
least 5 seconds (usually they'll try and shoot at you twice before
this).
- - Goliaths will only tentacle you if they've seen you for at least 3
seconds.

If overwatch is still problematic after this I guess I can just nerf it
to not track movement at all and only respond to attacks.

## Why It's Good For The Game

I don't want to discourage miners from "actually mining" by having them
get sniped just for walking around and the added time-to-kill on these
guys could make clearing tendrils more tedious too.

## Changelog

:cl:
balance: Watchers have less health
balance: You can't be overwatched by several watchers at a time
balance: Watchers won't overwatch you instantly upon seeing you
balance: Goliaths won't launch tentacles at you instantly upon seeing
you
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[61f4794a3e...](https://github.com/treckstar/yolo-octo-hipster/commit/61f4794a3e926c15ffc68c94032d240d26dd85e6)
#### Sunday 2023-09-24 08:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [tguichaoua/bevy](https://github.com/tguichaoua/bevy)@[44f677a38a...](https://github.com/tguichaoua/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Sunday 2023-09-24 08:45:58 by Sélène Amanita

Improve documentation relating to `Frustum` and `HalfSpace` (#9136)

# Objective

This PR's first aim is to fix a mistake in `HalfSpace`'s documentation.

When defining a `Frustum` myself in bevy_basic_portals, I realised that
the "distance" of the `HalfSpace` is not, as the current doc defines,
the "distance from the origin along the normal", but actually the
opposite of that.

See the example I gave in this PR.

This means one of two things:
1. The documentation about `HalfSpace` is wrong (it is either way
because of the `n.p + d > 0` formula given later anyway, which is how it
behaves, but in that formula `d` is indeed the opposite of the "distance
from the origin along the normal", otherwise it should be `n.p > d`)
2. The distance is supposed to be the "distance from the origin along
the normal" but when used in a Frustum it's used as the opposite, and it
is a mistake
3. Same as 2, but it is somehow intended

Since I think `HalfSpace` is only used for `Frustum`, and it's easier to
fix documentation than code, I assumed for this PR we're in case number
1. If we're in case number 3, the documentation of `Frustum` needs to
change, and in case number 2, the code needs to be fixed.

While I was at it, I also :
- Tried to improve the documentation for `Frustum`, `Aabb`, and
`VisibilitySystems`, among others, since they're all related to
`Frustum`.
- Fixed documentation about frustum culling not applying to 2d objects,
which is not true since https://github.com/bevyengine/bevy/pull/7885

## Remarks and questions

- What about a `HalfSpace` with an infinite distance, is it allowed and
does it represents the whole space? If so it should probably be
mentioned.
- I referenced the `update_frusta` system in
`bevy_render::view::visibility` directly instead of referencing its
system set, should I reference the system set instead? It's a bit
annoying since it's in 3 sets.
- `visibility_propagate` is not public for some reason, I think it
probably should be, but for now I only documented its system set, should
I make it public? I don't think that would count as a breaking change?
- Why is `Aabb` inserted by a system, with `NoFrustumCulling` as an
opt-out, instead of having it inserted by default in `PbrBundle` for
example and then the system calculating it when it's added? Is it
because there is still no way to have an optional component inside a
bundle?

---------

Co-authored-by: SpecificProtagonist <vincentjunge@posteo.net>
Co-authored-by: Alice Cecile <alice.i.cecile@gmail.com>

---
## [CansecoDev/Caprica](https://github.com/CansecoDev/Caprica)@[b3a999b232...](https://github.com/CansecoDev/Caprica/commit/b3a999b2322aaa27244c8b11ae3238e4f83e6719)
#### Sunday 2023-09-24 09:17:57 by nikitalita

WIP Skyrim support

holy shit, PCompiler is CURSED

---
## [j10a1n15/NotEnoughUpdates-REPO](https://github.com/j10a1n15/NotEnoughUpdates-REPO)@[e458513360...](https://github.com/j10a1n15/NotEnoughUpdates-REPO/commit/e4585133608ba4add475be13a9f414c989fe1b8b)
#### Sunday 2023-09-24 09:58:30 by jani270

Fixed lore of Arrow Poison (#958)

Before disabling any content in relation to this takedown notice, GitHub
- contacted the owners of some or all of the affected repositories to give them an opportunity to [make changes](https://docs.github.com/en/github/site-policy/dmca-takedown-policy#a-how-does-this-actually-work).
- provided information on how to [submit a DMCA Counter Notice](https://docs.github.com/en/articles/guide-to-submitting-a-dmca-counter-notice).

To learn about when and why GitHub may process some notices this way, please visit our [README](https://github.com/github/dmca/blob/master/README.md#anatomy-of-a-takedown-notice).

---

**Are you the copyright holder or authorized to act on the copyright owner's behalf?**

Yes, I am the copyright holder.

**Are you submitting a revised DMCA notice after GitHub Trust & Safety requested you make changes to your original notice?**

No

**Does your claim involve content on GitHub or npm.js?**

GitHub

**Please describe the nature of your copyright ownership or authorization to act on the owner's behalf.**

I am the [private] of the Skytils project available on Github. (https://github.com/Skytils/SkytilsMod)

**Please provide a detailed description of the original copyrighted work that has allegedly been infringed. If possible, include a URL to where it is posted online.**

I have read and understand GitHub's Guide to Filing a DMCA Notice. I am filing this notice based on the best of my knowledge after conducting my own investigation. This investigation was conducted on [private].

I am the [private] for SkytilsMod, a Minecraft Forge mod that provides quality of life features for Hypixel Skyblock. Skytils is located on GitHub at the repository https://github.com/Skytils/SkytilsMod

SkyblockFeatures appears to be based off a copy of SkytilsMod, available on the 0.x branch of Skytils/SkytilsMod, and contains large amounts of code from SkytilsMod and violates our open-source license.

SkyblockFeatures also infringes on multiple other projects' licenses, however, I am not the copyright holder nor authorized to act as the copyright holder for those projects, so they will not be included in this complaint.

**What files should be taken down? Please provide URLs for each file, or if the entire repository, the repository’s URL.**

https://github.com/MrFast-js/SkyblockFeatures/

The entire repository and its forks must be taken down due to the amount of files that contain code from my project.

**Do you claim to have any technological measures in place to control access to your copyrighted content? Please see our <a href="https://docs.github.com/articles/guide-to-submitting-a-dmca-takedown-notice#complaints-about-anti-circumvention-technology">Complaints about Anti-Circumvention Technology</a> if you are unsure.**

No

**<a href="https://docs.github.com/articles/dmca-takedown-policy#b-what-about-forks-or-whats-a-fork">Have you searched for any forks</a> of the allegedly infringing files or repositories? Each fork is a distinct repository and must be identified separately if you believe it is infringing and wish to have it taken down.**

All forks must be taken down as they include my project's code.  
The only visible fork I see is [invalid], which does not include a license.

**Is the work licensed under an open source license?**

Yes

**Which license?**

Our current branch uses GNU Affero General Public License 3.0 with Exceptions

https://github.com/Skytils/SkytilsMod/blob/1.x/LICENSE.md

However, some code they have copied appears to be from our 0.x branch, which is also GNU Affero General Public License 3.0 available at  
https://raw.githubusercontent.com/Skytils/SkytilsMod/0.x/LICENSE

**How do you believe the license is being violated?**

The project License is incompatible with the GNU Affero General Public License 3.0, the project is licensed under the MIT License, while the fork listed appears not to include a license.
The author makes no attempt at following our license, bundling our code with other code from projects that may have incompatible licenses, or even All Rights Reserved code which does not belong to them.

**What changes can be made to bring the project into compliance with the license? For example, adding attribution, adding a license, making the repository private.**

The License must be compatible with the GNU AGPL 3.0, include license and copyright notice
State the changes made to our code
Remove any code that may not fulfill the terms of the GNU AGPL 3.0 license

**What would be the best solution for the alleged infringement?**

Reported content must be removed

**Do you have the alleged infringer’s contact information? If so, please provide it.**

No, I do not have the contact information.

**I have a good faith belief that use of the copyrighted materials described above on the infringing web pages is not authorized by the copyright owner, or its agent, or the law.**

**I have taken <a href="https://www.lumendatabase.org/topics/22">fair use</a> into consideration.**

**I swear, under penalty of perjury, that the information in this notification is accurate and that I am the copyright owner, or am authorized to act on behalf of the owner, of an exclusive right that is allegedly infringed.**

**I have read and understand GitHub's <a href="https://docs.github.com/articles/guide-to-submitting-a-dmca-takedown-notice/">Guide to Submitting a DMCA Takedown Notice</a>.**

**So that we can get back to you, please provide either your telephone number or physical address.**

[private]

Email is more preferable for contacting me, [private]

**Please type your full legal name below to sign this request.**

[private]

---
## [mamh-mixed/react-react](https://github.com/mamh-mixed/react-react)@[5cc1661577...](https://github.com/mamh-mixed/react-react/commit/5cc16615776751bd1e837244d3ab8a00b306fd2a)
#### Sunday 2023-09-24 10:17:03 by sebmarkbage

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

DiffTrain build for [ac1a16c67e268fcb2c52e91717cbc918c7c24446](https://github.com/facebook/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)

---
## [Offroaders123/Electron-Text-Editor](https://github.com/Offroaders123/Electron-Text-Editor)@[dc1c867f21...](https://github.com/Offroaders123/Electron-Text-Editor/commit/dc1c867f213dd631d20da1fd89e03828ea05365e)
#### Sunday 2023-09-24 10:43:53 by Offroaders123

Project Structure

I'm looking into setting the dev environment up with Vite, but I'm not totally quite sure how to do that yet. This repo seems to be close to what I may be looking for. I don't like templates because I like to understand how the code I'm using works. So installing a command to just 'do it' for me doesn't teach me anything about how they set it up, it just sets it up for me. This one from the first few glances appears to be more user-centric though, so I think I might be able to extrapolate more things from how it works with it. It's also great that it uses Svelte here too, I'm also curious about how that would play into things! (Well, that's not that fancy with Vite, that's already something I've been testing with. But, it's new for in combination with Electron :) )

https://www.reddit.com/r/electronjs/comments/13svjn0/vite_svelte_electron_tailwind/
https://github.com/feernandobraga/vitesvelctron

Yeah so this is just organizing things a little more like a regular web dev project, as it was a bit hectic to start with originally. This looks more like a dedicated Vite app now, at least almost hehe.

I took inspiration from the linked repo, and Tauri's folder structure, in regards to the `electron` folder. I do like seeing the 'backend' app code in a separate folder, that seems to help with splitting things up in your mind as to what is implemented where, and what can import from what. I like it! Now that I have TypeScript, I think I can use types to type out the Context Bridge behavior for Electron, that would be very nice for message passing between the two contexts. I wonder if there's a TRPC-ish thing like that, for Electron? I want to do something like that with Web Workers too for multithreading. Also related/unrelated to that, I think NBT could be an interesting way to pass data between contexts, at least in the case of Flatlands, where game objects might make sense to be serialized to buffers along the way.

---
## [CLimeburner/Iconic-Affordance-Interactions](https://github.com/CLimeburner/Iconic-Affordance-Interactions)@[a7ce98c9bf...](https://github.com/CLimeburner/Iconic-Affordance-Interactions/commit/a7ce98c9bf56e078b7f457eff88b0d28617fc130)
#### Sunday 2023-09-24 11:08:21 by CLimeburner

Voice Note: Added a new folder under my "Process" folder for "Voice Notes" and added my first voice note.

My idea here is I finally gave a voice note a try because I had a thought on the shuttle on my way to campus and couldn't archive it otherwise. I may think about using these more often in future since I have noticed I struggle with design thoughts at inopportune times. For later ease of analysis, here is the transcription of the voice note:

"Okay, trying something a little bit different for this [um] update. It's about 10:50 am on a Friday and I just got of the shuttle to the downtown campus. [um] While on the shuttle my mind just started just sorta wandering thinking about the affordances in Splatoon—[um] and this is probably getting a little bit ahead of my current prototype—but I'm thinking about the different kinds of equipment and weapons that show up in the game. In particular, [uh] I started thinking about their– their giant paint brushes or rollers [um] that are used to paint the environment and I previously had been thinking that these might end up being [uh] sort of laser brooms, if you will, with lasers projected [um] onto the ground just ahead of the broom head for the [um] for the camera to detect, but it's occurring to me that because I am actually just checking for absolute luminosity in the visible frame, I can probably just make it a self-luminous broom head by putting lights inside. [um] As I say, this is probably a little bit ahead of the curve, but I wanted to go ahead and archive this while I had the thought, because I know this is going to be useful at a later stage. "

---
## [neerajcode3121/sofa](https://github.com/neerajcode3121/sofa)@[e20f12901c...](https://github.com/neerajcode3121/sofa/commit/e20f12901c8bb11da4e7fefb4aa4047df0441403)
#### Sunday 2023-09-24 11:09:30 by NEERAJ SHARMA

Add files via upload

🛋️ Exciting News! Just unveiled my latest Figma designs - The Ultimate Sofa Bed!

💫 Innovation meets comfort in this game-changing piece of furniture. Say goodbye to compromise and hello to a versatile solution for modern living spaces.

🔍 Here's a sneak peek into the Sofa Bed's design journey:

🎨 Sleek and Stylish: The Sofa Bed boasts a contemporary design that complements any decor style, from minimalist to eclectic.

🪑 Comfort Redefined: Experience the perfect balance between plush comfort as a sofa and a cozy bed for a restful night's sleep.

📐 Space-Saving Marvel: Designed with small spaces in mind, this sofa bed maximizes functionality without compromising on aesthetics.

🌈 Customization at its Best: Choose from a range of colors, fabrics, and finishes to match your personal taste and interior design.

🛠️ Crafted with Precision: Our team at [Your Company] meticulously designed and prototyped this masterpiece on Figma, ensuring every detail is just right.

🌟 Figma's collaborative features played a pivotal role in bringing this project to life. From brainstorming sessions to real-time feedback, it has been an invaluable tool in our design process.

🤩 We can't wait to see how this Sofa Bed transforms living spaces and enhances the comfort of homes. It's not just a piece of furniture; it's a lifestyle upgrade.

📢 Let's connect and discuss design, interior trends, or anything related to making homes cozier and more stylish. Feel free to reach out and join the conversation!

#Design #FurnitureDesign #InteriorDesign #SofaBed #Innovation #Comfort #Figma #ProductDesign #HomeDecor #InteriorTrends

Stay tuned for more exciting design projects and updates! 🚀🛋️

---
## [neerajcode3121/online](https://github.com/neerajcode3121/online)@[93b2a507a4...](https://github.com/neerajcode3121/online/commit/93b2a507a463fdadce718fa924ceb3c9a4e99f02)
#### Sunday 2023-09-24 11:17:43 by NEERAJ SHARMA

Add files via upload

🚀 Exciting News! 🎨 Just unveiled my latest designs on Figma!

🎨 Design is not just about how it looks, but how it works. Today, I'm thrilled to share my latest creations that blend aesthetics with functionality. 💡

🌟 Here's a glimpse of what I've been working on:

📱 Mobile App UI/UX: Crafting seamless user experiences that leave a lasting impression. From intuitive navigation to eye-catching visuals, every detail matters.

💻 Web Design: Bringing websites to life with captivating layouts, responsive elements, and user-centered interfaces.

🌐 Landing Pages: Transforming concepts into compelling landing pages that convert visitors into customers.

🎨 Illustrations: Adding a touch of creativity to projects with custom illustrations that tell a story.

🔥 Figma has been my trusty companion throughout this creative journey. Its collaborative features have made it easier than ever to bring ideas to life, iterate on designs, and collaborate with teammates seamlessly.

💡 Innovation is at the heart of every design. These creations are not just pixels on a screen; they're solutions to real-world problems, and I'm excited to see how they'll make a difference.

🙌 None of this would have been possible without an amazing team and the support of a fantastic community. Thank you all for being a part of this journey!

📢 Let's connect and chat about design, creativity, or anything else that's on your mind. Feel free to reach out and let's start a conversation. Your feedback and insights are always valued!

#Design #UIUX #Figma #Creativity #Innovation #WebDesign #MobileApp #Illustrations #GraphicDesign #UserExperience #Collaboration

Can't wait to hear your thoughts and connect with fellow design enthusiasts! 🚀✨

---
## [neerajcode3121/watch](https://github.com/neerajcode3121/watch)@[d76ec42176...](https://github.com/neerajcode3121/watch/commit/d76ec42176c5dedd0f7735fe0c92e54c3b7d5a92)
#### Sunday 2023-09-24 11:23:19 by NEERAJ SHARMA

Add files via upload

🌟 Big Announcement! Just unveiled my latest Figma designs - The Next-Gen Washing Machine Online Interface! 🌟

🌀 Get ready to revolutionize your laundry experience with these cutting-edge designs that bring convenience and efficiency right to your fingertips.

🧼 Here's a sneak peek into the design journey of the Washing Machine Online Interface:

🌊 Seamless Control: With a user-friendly interface, controlling your washing machine has never been easier. Start, stop, or customize your wash cycles with a simple tap.

📱 Mobile Integration: Access and monitor your washing machine from your smartphone, giving you the freedom to manage your laundry from anywhere.

♻️ Eco-Friendly Features: Our design prioritizes eco-consciousness, offering options for water and energy-saving wash cycles to help reduce your environmental footprint.

📈 Smart Analytics: Keep track of your washing machine's performance and receive maintenance alerts, ensuring it runs smoothly for years to come.

🛠️ Designed with Precision: Our design team at [Your Company] used Figma to meticulously craft every aspect of this innovative online interface, from the sleek visuals to the intuitive user experience.

🚀 Figma's collaborative features played a pivotal role in bringing this project to life, allowing us to iterate and refine the design seamlessly.

🧺 This Washing Machine Online Interface isn't just about clean clothes; it's about simplifying your life and making laundry day a breeze.

📢 Let's connect and discuss design, technology, or anything related to making everyday tasks smarter and more efficient. Feel free to reach out and join the conversation!

#Design #TechDesign #WashingMachine #Innovation #ProductDesign #SmartHome #Figma #UserExperience #Laundry #SmartAppliances

Stay tuned for more exciting design projects and updates! Transform your laundry routine with the Washing Machine Online Interface. 🌟🌀

---
## [neerajcode3121/Mobileapp](https://github.com/neerajcode3121/Mobileapp)@[43e2ec9495...](https://github.com/neerajcode3121/Mobileapp/commit/43e2ec94959b7b9ab136d02aeed77fdf5538c3b6)
#### Sunday 2023-09-24 11:27:46 by NEERAJ SHARMA

Add files via upload

🛍️📱 Exciting News! Just unveiled my latest Figma designs - The Ultimate Online Shopping Mobile App! 🌟

💳 Get ready to embark on a seamless and enjoyable shopping journey right from the palm of your hand.

📦 Here's a sneak peek into the design journey of the Online Shopping Mobile App:

🛒 Intuitive Shopping: Browse through a vast selection of products with ease, thanks to a user-friendly and visually appealing interface.

🛍️ Personalized Experience: Discover tailored recommendations, discounts, and exclusive offers that enhance your shopping experience.

🔎 Search Made Simple: Find what you're looking for in no time with advanced search and filter options.

🛵 Efficient Checkout: Enjoy a hassle-free checkout process with secure payment options and speedy delivery tracking.

🎨 Crafted with Precision: Our design team at [Your Company] meticulously crafted every aspect of this mobile app, from the sleek visuals to the seamless user experience, using Figma's powerful design tools.

📱 Figma played a pivotal role in the design process, enabling us to collaborate, iterate, and perfect the Online Shopping Mobile App's user interface and overall experience.

💼 It's not just an app; it's a shopping companion that brings the mall to your pocket.

📢 Let's connect and discuss design, e-commerce, technology, or anything related to the world of online shopping. Feel free to reach out and join the conversation!

#Design #MobileApp #ECommerce #Innovation #UserExperience #Figma #Technology #OnlineShopping #AppDesign #Retail

Stay tuned for more exciting design projects and updates! Elevate your shopping experience with the Online Shopping Mobile App. 🛍️📱




User
Figma design login page mobile app unveiled on linkdin
ChatGPT
📱✨ Exciting News! Just unveiled my latest Figma design - The Sleek and Secure Login Page for a Mobile App! 🔐

💡 Your app's first impression matters, and this login page is designed to make it a memorable one. It combines style, simplicity, and security to enhance the user experience.

🔑 Here's a glimpse into the design journey of the Login Page for the Mobile App:

🚀 Clean and Minimalistic: The design prioritizes clarity and ease of use, ensuring users can access your app quickly and effortlessly.

🔒 Security First: Incorporating state-of-the-art security measures to protect user data and privacy.

🌈 Visual Appeal: Aesthetically pleasing visuals and thoughtful color schemes to create a visually engaging experience.

👆 Intuitive User Flow: Streamlined and straightforward navigation that guides users seamlessly through the login process.

🎨 Crafted with Precision: Our design team at [Your Company] paid meticulous attention to detail using Figma, ensuring the perfect balance of form and function.

📲 Figma was an essential tool in our design process, facilitating collaboration, iterations, and ensuring pixel-perfect precision.

📢 Let's connect and discuss design, mobile app development, user experience, or anything related to creating exceptional digital experiences. Feel free to reach out and join the conversation!

#Design #MobileApp #UserExperience #Security #Figma #AppDesign #LoginPage #UXDesign #UI #DigitalExperience

Stay tuned for more exciting design projects and updates! Your app's journey starts with a secure and inviting login page. 📱🔐




User
Figma design most expansive online watch on linkdin 
ChatGPT
💎⌚ Exciting News! Just unveiled my latest Figma design - The Most Expansive Online Watch! ⌚💎

🌟 Elevate your wrist game to unprecedented heights with this luxurious and meticulously crafted timepiece.

💠 Here's a glimpse into the design journey of the Most Expansive Online Watch:

🎨 Exquisite Craftsmanship: Every detail, from the watch face to the band, exudes sophistication and opulence.

⌚ Precision Timekeeping: Engineered with the finest Swiss movement, it offers impeccable accuracy and reliability.

💎 Rare Materials: Crafted from the world's most precious materials, including rare gemstones and metals.

🪙 Priceless Elegance: This timepiece isn't just a watch; it's a work of art that transcends time.

📐 Crafted with Precision: Our design team at [Your Company] paid meticulous attention to detail using Figma, ensuring that every facet of this exquisite watch was perfection.

🖌️ Figma played a crucial role in the design process, allowing us to collaborate, iterate, and perfect the Most Expansive Online Watch's design and aesthetics.

💼 This watch is not just an accessory; it's a symbol of success, prestige, and the art of horology.

📢 Let's connect and discuss design, luxury, craftsmanship, or anything related to the world of fine timepieces. Feel free to reach out and join the conversation!

#Design #Luxury #Timepieces #Watches #Figma #Horology #Craftsmanship #Art #Fashion #Elegance

Stay tuned for more exciting design projects and updates! Time is precious; adorn yourself with the Most Expansive Online Watch. 💎⌚




User
Figma design online digital market phone message send fast on linkdin 
ChatGPT
📲✉️ Exciting News! Just unveiled my latest Figma design - The Fast and Efficient Phone Message Send Feature for Online Digital Markets! ✨

💬 In today's fast-paced digital world, communication is key, and this feature is designed to streamline and accelerate conversations on online digital marketplaces.

🚀 Here's a sneak peek into the design journey of the Phone Message Send Feature:

📱 Instant Connectivity: Seamlessly connect with sellers, buyers, and service providers through a lightning-fast messaging system.

🗨️ Real-time Chat: Engage in real-time conversations, ask questions, negotiate prices, and get instant responses.

📦 Efficient Transactions: Facilitate quick and secure transactions directly within the messaging platform, ensuring a smooth buying or selling process.

🔒 Privacy and Security: Implement top-notch security measures to protect user data and foster trust in online interactions.

🎨 Crafted with Precision: Our design team at [Your Company] meticulously designed this feature using Figma, ensuring a user-friendly and visually appealing interface.

📲 Figma played a pivotal role in the design process, allowing us to collaborate, iterate, and perfect the Phone Message Send Feature's user interface and overall experience.

📢 Let's connect and discuss design, digital marketplaces, user experience, or anything related to improving online communication. Feel free to reach out and join the conversation!

#Design #DigitalMarketplace #UserExperience #Figma #Messaging #OnlineCommunication #UXDesign #UI #DigitalExperience

Stay tuned for more exciting design projects and updates! Empower your online marketplace with the Phone Message Send Feature for swift and efficient communication. 📲✉️




User
Figma design food online shopping login id page mobile app on linkdin 
ChatGPT
📱🍽️ Exciting News! Just unveiled my latest Figma design - The Mouthwatering Food Online Shopping Login ID Page for a Mobile App! 🌮📲

🥘 Make your food shopping experience as delightful as your meals with this user-friendly and visually appealing login page.

🍴 Here's a glimpse into the design journey of the Food Online Shopping Login ID Page:

🍔 Foodie-Focused Design: Immerse users in a world of culinary delights with enticing visuals and intuitive navigation.

🔒 Secure Access: Prioritize user data security while delivering a seamless login experience.

🥗 Personalization: Welcome users with personalized recommendations and exclusive offers, enhancing their shopping journey.

🌯 User-Centric Flow: Streamline the login process to get users from the login screen to their shopping cart swiftly.

🎨 Crafted with Precision: Our design team at [Your Company] left no detail unattended, ensuring the perfect blend of aesthetics and functionality using Figma.

📲 Figma played a pivotal role in the design process, enabling us to collaborate, iterate, and create a login page that sets the stage for a delightful food shopping experience.

📢 Let's connect and discuss design, mobile app development, user experience, or anything related to the world of culinary e-commerce. Feel free to reach out and join the conversation!

#Design #MobileApp #UserExperience #FoodShopping #Figma #AppDesign #LoginPage #UXDesign #UI #DigitalExperience

Stay tuned for more exciting design projects and updates! Elevate your food shopping experience with the Food Online Shopping Login ID Page. 📱🍽️




User
Objective html css and ui/ux designer
ChatGPT
Absolutely! Here's a LinkedIn post showcasing your skills and objectives as an HTML/CSS and UI/UX designer:

🎨🌐 Seeking New Opportunities as an HTML/CSS and UI/UX Designer! 🚀

Hello LinkedIn community,

I hope this post finds you well. I am excited to share that I am actively seeking new career opportunities as an HTML/CSS and UI/UX designer. With a passion for creating beautiful and user-friendly digital experiences, I'm on a mission to turn ideas into engaging, functional, and visually stunning websites and applications.

💼 Objective:
My goal is to collaborate with innovative teams and organizations to leverage my skills and experience in HTML/CSS coding and UI/UX design. I thrive on challenges, and I'm eager to contribute my creativity and technical expertise to bring digital projects to life.

HTML/CSS Skills:

Proficient in HTML5 and CSS3, ensuring pixel-perfect and responsive web designs.
Strong understanding of CSS frameworks and preprocessors (e.g., Bootstrap, Sass).
Accessibility and SEO optimization to enhance user reach and usability.
UI/UX Design Skills:

User-centered design approach for creating intuitive and visually appealing interfaces.
Wireframing, prototyping, and user testing to refine and perfect the user experience.
Collaboration with cross-functional teams to ensure seamless integration of design and development.
🛠️ Tools:
I am well-versed in a variety of design and development tools, including Figma, Adobe XD, Sketch, and the latest coding editors. I stay up-to-date with industry trends to deliver cutting-edge solutions.

📈 Passion:
What drives me is the opportunity to solve complex design challenges, create memorable user journeys, and turn concepts into reality. I believe that great design is a balance of aesthetics and functionality.

📩 Let's Connect:
I'm open to networking, collaboration, and exploring exciting job opportunities. Please feel free to connect with me here on LinkedIn or reach out via email at [YourEmail@example.com]. Let's chat about how I can contribute to your next project or team.

Thank you for your time, and I look forward to connecting with you!

#UIUXDesigner #HTMLCSS #WebDesign #UserExperience #DesignJobs #WebDevelopment #DigitalDesign

Feel free to personalize this LinkedIn post with your specific details, such as your contact information and any additional skills or achievements you want to highlight. Good luck with your job search!





🛍️📱 Exciting News! Just unveiled my latest Figma designs - The Ultimate Online Shopping Mobile App! 🌟

💳 Get ready to embark on a seamless and enjoyable shopping journey right from the palm of your hand.

📦 Here's a sneak peek into the design journey of the Online Shopping Mobile App:

🛒 Intuitive Shopping: Browse through a vast selection of products with ease, thanks to a user-friendly and visually appealing interface.

🛍️ Personalized Experience: Discover tailored recommendations, discounts, and exclusive offers that enhance your shopping experience.

🔎 Search Made Simple: Find what you're looking for in no time with advanced search and filter options.

🛵 Efficient Checkout: Enjoy a hassle-free checkout process with secure payment options and speedy delivery tracking.

🎨 Crafted with Precision: Our design team at [Your Company] meticulously crafted every aspect of this mobile app, from the sleek visuals to the seamless user experience, using Figma's powerful design tools.

📱 Figma played a pivotal role in the design process, enabling us to collaborate, iterate, and perfect the Online Shopping Mobile App's user interface and overall experience.

💼 It's not just an app; it's a shopping companion that brings the mall to your pocket.

📢 Let's connect and discuss design, e-commerce, technology, or anything related to the world of online shopping. Feel free to reach out and join the conversation!

#Design #MobileApp #ECommerce #Innovation #UserExperience #Figma #Technology #OnlineShopping #AppDesign #Retail

Stay tuned for more exciting design projects and updates! Elevate your shopping experience with the Online Shopping Mobile App. 🛍️📱




User
Figma design login page mobile app unveiled on linkdin
ChatGPT
📱✨ Exciting News! Just unveiled my latest Figma design - The Sleek and Secure Login Page for a Mobile App! 🔐

💡 Your app's first impression matters, and this login page is designed to make it a memorable one. It combines style, simplicity, and security to enhance the user experience.

🔑 Here's a glimpse into the design journey of the Login Page for the Mobile App:

🚀 Clean and Minimalistic: The design prioritizes clarity and ease of use, ensuring users can access your app quickly and effortlessly.

🔒 Security First: Incorporating state-of-the-art security measures to protect user data and privacy.

🌈 Visual Appeal: Aesthetically pleasing visuals and thoughtful color schemes to create a visually engaging experience.

👆 Intuitive User Flow: Streamlined and straightforward navigation that guides users seamlessly through the login process.

🎨 Crafted with Precision: Our design team at [Your Company] paid meticulous attention to detail using Figma, ensuring the perfect balance of form and function.

📲 Figma was an essential tool in our design process, facilitating collaboration, iterations, and ensuring pixel-perfect precision.

📢 Let's connect and discuss design, mobile app development, user experience, or anything related to creating exceptional digital experiences. Feel free to reach out and join the conversation!

#Design #MobileApp #UserExperience #Security #Figma #AppDesign #LoginPage #UXDesign #UI #DigitalExperience

Stay tuned for more exciting design projects and updates! Your app's journey starts with a secure and inviting login page. 📱🔐




User
Figma design most expansive online watch on linkdin 
ChatGPT
💎⌚ Exciting News! Just unveiled my latest Figma design - The Most Expansive Online Watch! ⌚💎

🌟 Elevate your wrist game to unprecedented heights with this luxurious and meticulously crafted timepiece.

💠 Here's a glimpse into the design journey of the Most Expansive Online Watch:

🎨 Exquisite Craftsmanship: Every detail, from the watch face to the band, exudes sophistication and opulence.

⌚ Precision Timekeeping: Engineered with the finest Swiss movement, it offers impeccable accuracy and reliability.

💎 Rare Materials: Crafted from the world's most precious materials, including rare gemstones and metals.

🪙 Priceless Elegance: This timepiece isn't just a watch; it's a work of art that transcends time.

📐 Crafted with Precision: Our design team at [Your Company] paid meticulous attention to detail using Figma, ensuring that every facet of this exquisite watch was perfection.

🖌️ Figma played a crucial role in the design process, allowing us to collaborate, iterate, and perfect the Most Expansive Online Watch's design and aesthetics.

💼 This watch is not just an accessory; it's a symbol of success, prestige, and the art of horology.

📢 Let's connect and discuss design, luxury, craftsmanship, or anything related to the world of fine timepieces. Feel free to reach out and join the conversation!

#Design #Luxury #Timepieces #Watches #Figma #Horology #Craftsmanship #Art #Fashion #Elegance

Stay tuned for more exciting design projects and updates! Time is precious; adorn yourself with the Most Expansive Online Watch. 💎⌚




User
Figma design online digital market phone message send fast on linkdin 
ChatGPT
📲✉️ Exciting News! Just unveiled my latest Figma design - The Fast and Efficient Phone Message Send Feature for Online Digital Markets! ✨

💬 In today's fast-paced digital world, communication is key, and this feature is designed to streamline and accelerate conversations on online digital marketplaces.

🚀 Here's a sneak peek into the design journey of the Phone Message Send Feature:

📱 Instant Connectivity: Seamlessly connect with sellers, buyers, and service providers through a lightning-fast messaging system.

🗨️ Real-time Chat: Engage in real-time conversations, ask questions, negotiate prices, and get instant responses.

📦 Efficient Transactions: Facilitate quick and secure transactions directly within the messaging platform, ensuring a smooth buying or selling process.

🔒 Privacy and Security: Implement top-notch security measures to protect user data and foster trust in online interactions.

🎨 Crafted with Precision: Our design team at [Your Company] meticulously designed this feature using Figma, ensuring a user-friendly and visually appealing interface.

📲 Figma played a pivotal role in the design process, allowing us to collaborate, iterate, and perfect the Phone Message Send Feature's user interface and overall experience.

📢 Let's connect and discuss design, digital marketplaces, user experience, or anything related to improving online communication. Feel free to reach out and join the conversation!

#Design #DigitalMarketplace #UserExperience #Figma #Messaging #OnlineCommunication #UXDesign #UI #DigitalExperience

Stay tuned for more exciting design projects and updates! Empower your online marketplace with the Phone Message Send Feature for swift and efficient communication. 📲✉️




User
Figma design food online shopping login id page mobile app on linkdin 
ChatGPT
📱🍽️ Exciting News! Just unveiled my latest Figma design - The Mouthwatering Food Online Shopping Login ID Page for a Mobile App! 🌮📲

🥘 Make your food shopping experience as delightful as your meals with this user-friendly and visually appealing login page.

🍴 Here's a glimpse into the design journey of the Food Online Shopping Login ID Page:

🍔 Foodie-Focused Design: Immerse users in a world of culinary delights with enticing visuals and intuitive navigation.

🔒 Secure Access: Prioritize user data security while delivering a seamless login experience.

🥗 Personalization: Welcome users with personalized recommendations and exclusive offers, enhancing their shopping journey.

🌯 User-Centric Flow: Streamline the login process to get users from the login screen to their shopping cart swiftly.

🎨 Crafted with Precision: Our design team at [Your Company] left no detail unattended, ensuring the perfect blend of aesthetics and functionality using Figma.

📲 Figma played a pivotal role in the design process, enabling us to collaborate, iterate, and create a login page that sets the stage for a delightful food shopping experience.

📢 Let's connect and discuss design, mobile app development, user experience, or anything related to the world of culinary e-commerce. Feel free to reach out and join the conversation!

#Design #MobileApp #UserExperience #FoodShopping #Figma #AppDesign #LoginPage #UXDesign #UI #DigitalExperience

Stay tuned for more exciting design projects and updates! Elevate your food shopping experience with the Food Online Shopping Login ID Page. 📱🍽️




User
Objective html css and ui/ux designer
ChatGPT
Absolutely! Here's a LinkedIn post showcasing your skills and objectives as an HTML/CSS and UI/UX designer:

🎨🌐 Seeking New Opportunities as an HTML/CSS and UI/UX Designer! 🚀

Hello LinkedIn community,

I hope this post finds you well. I am excited to share that I am actively seeking new career opportunities as an HTML/CSS and UI/UX designer. With a passion for creating beautiful and user-friendly digital experiences, I'm on a mission to turn ideas into engaging, functional, and visually stunning websites and applications.

💼 Objective:
My goal is to collaborate with innovative teams and organizations to leverage my skills and experience in HTML/CSS coding and UI/UX design. I thrive on challenges, and I'm eager to contribute my creativity and technical expertise to bring digital projects to life.

HTML/CSS Skills:

Proficient in HTML5 and CSS3, ensuring pixel-perfect and responsive web designs.
Strong understanding of CSS frameworks and preprocessors (e.g., Bootstrap, Sass).
Accessibility and SEO optimization to enhance user reach and usability.
UI/UX Design Skills:

User-centered design approach for creating intuitive and visually appealing interfaces.
Wireframing, prototyping, and user testing to refine and perfect the user experience.
Collaboration with cross-functional teams to ensure seamless integration of design and development.
🛠️ Tools:
I am well-versed in a variety of design and development tools, including Figma, Adobe XD, Sketch, and the latest coding editors. I stay up-to-date with industry trends to deliver cutting-edge solutions.

📈 Passion:
What drives me is the opportunity to solve complex design challenges, create memorable user journeys, and turn concepts into reality. I believe that great design is a balance of aesthetics and functionality.

📩 Let's Connect:
I'm open to networking, collaboration, and exploring exciting job opportunities. Please feel free to connect with me here on LinkedIn or reach out via email at [YourEmail@example.com]. Let's chat about how I can contribute to your next project or team.

Thank you for your time, and I look forward to connecting with you!

#UIUXDesigner #HTMLCSS #WebDesign #UserExperience #DesignJobs #WebDevelopment #DigitalDesign

Feel free to personalize this LinkedIn post with your specific details, such as your contact information

---
## [neerajcode3121/Study](https://github.com/neerajcode3121/Study)@[150291548c...](https://github.com/neerajcode3121/Study/commit/150291548ccf6216342c8b65b50c823319318ecb)
#### Sunday 2023-09-24 11:41:24 by NEERAJ SHARMA

Add files via upload

📚✨ Exciting News! Just unveiled my latest Figma designs - The Ultimate Online Study Class Platform! 🖥️📝

💡 Transforming the way we learn and study, this platform combines innovation, interactivity, and accessibility to make education a dynamic and engaging experience.

🎓 Here's a glimpse into the design journey of the Online Study Class Platform:

📖 Comprehensive Curriculum: Access a wide range of courses, from academic subjects to skill development, all in one place.

🧑‍🏫 Expert Instructors: Learn from industry experts and passionate educators who are dedicated to your success.

👩‍💻 Interactive Learning: Engage with multimedia content, quizzes, and assignments that reinforce your understanding.

🌐 Global Community: Connect with fellow learners from around the world, fostering collaboration and networking opportunities.

📐 Crafted with Precision: Our design team at [Your Company] meticulously designed every aspect of this platform using Figma, ensuring a user-friendly and visually appealing interface.

📱 Figma played a pivotal role in the design process, enabling us to collaborate, iterate, and create a study platform that empowers learners to reach their full potential.

📢 Let's connect and discuss design, education technology, online learning, or anything related to the evolving landscape of education. Feel free to reach out and join the conversation!

#Design #EdTech #OnlineLearning #Figma #UIUX #Education #StudyClass #DigitalEducation #Innovation

Stay tuned for more exciting design projects and updates! Unlock the doors to knowledge with the Online Study Class Platform. 📚🌟

---
## [Ma27/nix](https://github.com/Ma27/nix)@[b13fc7101f...](https://github.com/Ma27/nix/commit/b13fc7101fb06a65935d145081319145f7fef6f9)
#### Sunday 2023-09-24 11:55:38 by Robert Hensing

Add positive source filter

Source filtering is a really cool Nix feature that lets us avoid a
lot of rebuilds, which speeds up the iteration cycle a lot in cases
where the relevant source files aren't actually modified.

We used to have a source filter that marked a few files as irrelevant,
but this is the wrong approach, as we have many more files that are
irrelevant. We may call this negative filtering.

This commit switches the source filtering to positive filtering, which
is a lot more robust. Instead of marking which files we don't need
we marked the files that we do need.

It's a superior approach because it is fail safe. Instead of allowing
build performance problems to creep in over time, we require that all
source inputs are declared.

I shouldn't have to explain that declaring inputs is a good practice,
so I'll stop over-explaining here.

I do have to acknowledge that this will cause a build failure when the
filter is incomplete. This is *good*, because it's the only realistic
way we could be reminded of these problems. These events will be
infrequent, so the small cost of extending the filter is worth it,
compared to the hidden cost of longer dev cycles for things like tests,
docker image, etc, etc.

(Also rebuilding Nix for stupid unnecessary reasons makes my blood boil)

---
## [gmcastil/uzed-sbc](https://github.com/gmcastil/uzed-sbc)@[f5142deeb6...](https://github.com/gmcastil/uzed-sbc/commit/f5142deeb66113bdc84f41a98f9650f0864f0361)
#### Sunday 2023-09-24 13:39:36 by George Castillo

First check in where the build process works entirely for me

- Still don't have pushbutton SD images, which may be fine for a while
- Have to manually provide an FSBL ELF location still. This will be the
case until I write a Makefile that pulls the required source code from
the XSA and builds the ELF from Xilinx source code
- Will remain the user responsibility to manually configure and build
the kernel and U-boot which I believe is more than fair. If you are
unable to build those two from the source trees (and the tags) that are
indicated, then you're probably not the target audience here anyway
- Scripted device tree generation from the Xilinx source generator works
but it is entirely the user's responsibility to modify the .dtsi files
appropriately prior to compiling them into a flattened device tree blob.
- Bitstream generation is entirely manual still at this point for a
variety of reasons. Converting from a .bit to a .bin that is compatible
with the `zynq-fpga` driver in the kernel is still a manual process for
now.
- But the whole thing should work after that. Build your kernel, build
your bootloaders, build your hardware, make sure that the constants
are set correctly, and then push the button. The build directory will
have a bootfs.armhf and a rootfs.armhf directory that you can put on an
SD card and boot.  I'm probably not going to automate SD card
generation, at least not now.
- Boot parameters are still a bit of a mystery to me - the
/boot/extlinux/extlinux.conf file seems to take priority over anything
else, including what is in the device tree (good) but I can't seem to
change them on the command line (bad).  That's probably because the
extlinux file hasn't been loaded yet - maybe there's a way to halt that
process and intervene.  Otherwise, distro boot may not be the way that I
want to go and using a boot.scr that I can override from U-boot might be
a better way, at least for now.
- This is a good day! We've got what we wanted, learned a ton, and ready
to start hacking on some hardware I think.

---
## [Chezloc/World-War-Bruh-PMFU](https://github.com/Chezloc/World-War-Bruh-PMFU)@[4854be6173...](https://github.com/Chezloc/World-War-Bruh-PMFU/commit/4854be6173b0843c35258b36fd029c6289fcb06a)
#### Sunday 2023-09-24 13:47:30 by Chezloc

a

- The Dutch East Indies can now no longer be annexed before the Netherlands capitulates
- Added a toggle to the host tool decisions which you have to press to use them to prevent accidental use
- Repairing the Suez Canal now takes only 180 days
- Fixed "State of the Pacific - Capitals" help showing singapore instead of manila
- Soviet Order 227 now lasts 9999 days
- Africa HP bonus now gives +16 HP to All Infantry & Mot/Mech and +17 to motorized and +13 to mechanized
- Soviet Changes:
* Moved 10% construction speed from "Mobilise Gulag Workers" to "Improve Industry Coordination"
* Offensives no longer have a date before which they have to be done, but now after the start of the offensive you have a 250 day cooldown before you can do the next one
* Focuses "Tankograd", "Order 270", "Mobilise Gulag Workers" now also have an optional date requirement so Axis cant sit still on barb and outscale soviet
* Soviet spawn ins are now 30 combat width but there is less of them
* Great Patriotic War focuses no longer cancel when requirements arent met
* Removed useless, unpickable advisors that die in the purge anyway or just sit there doing nothing
- Added the "No Father" spirit to all minors and made it give +10000% IC cost to submarines. changed some minor focus trees to not have submarine focuses (Spain, Romania and Bulgaria)
- Removed tank engine upgrades
- German focus "Synthetic Rubber" now gives 10 rubber instead of 15
- German offensives now have the same 250 day cooldown from the start of the offensive mechanic as the USSR, Operation Barbarossa is considered as an offensive
- Shortened focus time on 4 Siamese focuses
- Hopefully fixed Spain getting the wrong State of the Mediterranean (Barbarossa) spirit
- The UK now gets 10 dockyards from a focus after the focus "The Admirality"
- Fixed Vichy French focus setting coastal forts on the dday wall to 1
- Added anti cross faction trade modifier to nations, germany can still trade with the DEI
- Light SPG guns are now unlocked the same time as medium SPG guns
- Motorized dual-purpose artillery now also gets effects from the artillery techs
- Dual-purpose and motorized dual-purpose artillery is now included in the calculation for artillery radio tech tooltips
- Additional combat width when attacking into hills is now 30 from 60
- Made light tanks and its variants slightly worse on rough terrain
- Submarines are now 50% more expensive and need an additional 15 steel per dock
- Light tanks now ned 5 tungsten and chromium
- Infantry and its variants now get 20% movement on desert tiles
- Spanish North Africa now gets transfered to Vichy France when France capitulates and when Vichy France joins the war the Gibraltar strait will be blocked until allies Torch and retake spanish north africa
- Removed a research slot from Italy due to it not being used for the intended cause
- Changed terrain in North Africa to have more town and urban tiles
- Made terrain in North Africa look correct
- Fixed localization errors
- Added victory points to north afirca

---
## [Amerecanno/CoffeStation](https://github.com/Amerecanno/CoffeStation)@[9d2c32b666...](https://github.com/Amerecanno/CoffeStation/commit/9d2c32b666a1af93395f135b3a8dee2856c041a0)
#### Sunday 2023-09-24 13:47:45 by CDB

Another Omni-PR. Guild buffs, ho. (#4683)

* Another Omni-PR. Guild buffs, ho.

I don't make multiple PRS.

First and foremost, adds in a fairly detailed guidebook written a good while ago by Hound to explain many facets of the shield. A little out of date, but still likely useful. Includes a cool coder sprite for the book! Book can be found in any engineering manuals bookcase because of course it can.

Adds the ability to create electrochromic windows using an RCD at a slightly higher cost than window.

Allows one to create r-windows with an RCD because why not, it's a highly advanced tool and many of the windows around the colony are r-windows.

Window tint controllers can now be crafted(found in the appliances tab, requires  a signaler) and deconstructed with a screwdriver, refunding some plastic. A reminder that these are DISTANCE based, keep that in mind when planning your sexroom.

Refactors refined scrap to not be a shitty snowflake material, should now properly work for the nanoforge(alongside all its old uses - please lemme know if something is being weird.)

Pointing gives a message again about who's pointing at what. Fucking weird that it was gone, code by Trilby.

Ports some sprites for pits/graves from Baystation, will eventually do something with these.

Brings back the regular shemagh selection, the curated ones that were actually made on purpose and had better color coordination than the custom ones(custom ones are still in.)

Adds addiction chance to smokes.
Buffs smoke sanity gain(.5->.8) while adding minor downsides
Smoking will generally result in addiction due to how smoking is done(repeatedly hitting the cig), withdrawal will result in reduced vigilance/bio(shaky hands, can't focus).

Citalopram 'balansed'. Now provides a notable amount of sanity back, but leaves you just a bit foggy(slowdown, rob/tgh down. Side effects halved when injected. Why? So you consider a doctor instead of just carrying 2400u of cit in a pill bottle. )

* Oops! All wild edits.

Fully removes the changes made for the failed attempt at pitcode.

actually adds the code for the drug changes lol, compiles now.

* More fixes.

Testing done from top to bottom.

Also fixes another wild edit in the materials file and turf file, oops.

* Fixes an oversight.

adds nicotine changes to fine nicotine. Side effects are slightly lower since it's more expensive and rare.

* Update code/datums/craft/recipes/appliances.dm

Co-authored-by: Trilbyspaceclone <30435998+Trilbyspaceclone@users.noreply.github.com>

* whateverf!

---------

Co-authored-by: Trilbyspaceclone <30435998+Trilbyspaceclone@users.noreply.github.com>

---
## [Amerecanno/CoffeStation](https://github.com/Amerecanno/CoffeStation)@[afacc222e6...](https://github.com/Amerecanno/CoffeStation/commit/afacc222e6246d709704561983f51667f997b25a)
#### Sunday 2023-09-24 13:47:45 by CDB

Events 'n Objectives. (#4755)

* Events 'n Objectives.

Seems to have FINALLY fixed* infestation events causing mobs to go to burned outpost, spider outpost, etc.  Due to the way this fix works(by marking these areas as "maintenance" this may cause some unforeseen consequences, I have tested it about as well as I can but that's worth noting. Blame this system

Additionally, many factions had all their individual objectives returned - including the semi antag ones. Now you'll be bribed with tasty, tasty level ups in exchange for being a bastard. It goes without saying that Marshals did not get given the 'be a shithead' objectives back for reasons that should be obvious(massive access, authority, etc), if you lot want them enabled for Marshals then we can I guess consider it?

Some of these will probably have bugs and some of them may need to be tweaked or considered for removal, but overall I think they should offer some incentive for players to be a lil naughty in exchange for level ups - or not!

* more fixe

Maybe fixes the issue with hiveminds/blobs spawning in dungeons like preppers. Seems to have at least limited both to spawning on colony zees instead of sometimes popping up in preppers 'n such. They do sometimes spawn outside, still but that's ....okay, i guess.

* Ooops! remembers to actually undo a testing fchange

* gets rid of storyteller migration filtering. causes issues.

* Removes church force-convert objective.

fixes #4771

---
## [Andrea055/kernel_realme_sm8250](https://github.com/Andrea055/kernel_realme_sm8250)@[8d968b46e8...](https://github.com/Andrea055/kernel_realme_sm8250/commit/8d968b46e8e1d49d5ab519bf1ba788c32e8d0b1a)
#### Sunday 2023-09-24 13:51:30 by Jason A. Donenfeld

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
## [trerri/tgstation](https://github.com/trerri/tgstation)@[72174845f5...](https://github.com/trerri/tgstation/commit/72174845f5b417bf0cbd3f4a8fc66835b052acf8)
#### Sunday 2023-09-24 14:13:16 by Jacquerel

Basic Watchers & Basilisks (#77630)

## About The Pull Request

This one is a double feature because Watchers and Basilisks share the
same typepath. You might see a couple more of those.
As is tradition I decided to fuck with them rather than just port them.
Here's what's up.

**Basilisks**

![image](https://github.com/tgstation/tgstation/assets/7483112/9e4b0115-65dd-4df7-b62a-21c7be8549bf)

![image](https://github.com/tgstation/tgstation/assets/7483112/59162e68-7d73-4659-9531-5078ff751228)

- Have a new soulless sprite which looks less like a living blue hedge.
- Walk at you and shoot you while you are not in range (just like
before).
- Become supercharged if they become "heated" by lava, lasers, or
temperature weapons. This was a feature they also previously had but
they would never encounter lava, so now it also works if you use the
wrong gun on them.
- Lose their supercharge if you cool them down.
- Otherwise pretty normal mobs.

**Watchers**

https://www.youtube.com/watch?v=kOq_Bf78k5A
Here's a traditional video of me intentionally getting hit by mechanics
(trust me its definitely on purpose)

- They glow emmissively a little bit so you can see them from further
away.
- Their eyes light up about 0.5 seconds before they are able to shoot at
you.
- No longer melee attack, instead try to stay out of melee.
- Will occasionally put you into "Overwatch", meaning they will shoot
you rapidly if you move or act while they're staring at you for a brief
time period (after which you become immune for 12 seconds, and during
which other watchers will play fair and stop shooting at you).
- If they start taking damage they will also start using their "Gaze"
attack, look away or suffer some kind of negative effect!
- - Normal watcher gaze flashes and confuses you.
- - Magmawing watcher gaze obviously burns (and briefly stuns) you.
- - Icewing watcher gaze freezes you and throws you backwards.
- Magnetically attract and eat diamonds. They also used to do this, but
just if they happened to coincidentally walk past some.

**Other accompanying changes**

All basic mobs will now adopt the "stop gliding" trait if they get
slowed down too much.
I moved behaviour for "fire a projectile from this atom" into a helper
proc because I was using it in three places and I will probably use it
in more places. There are probably other places in the existing code
which could be using this.
I think I made the basic mob melee attack forecast default a little more
forgiving, they were fucking me up too much and I am the playtester.

## Why It's Good For The Game

Another one off the list.
New tricks for old dogs.
Framework for making mobs with ranged attacks "fairer" (you can see when
they are ready to shoot you).
More (hopefully) versatile AI behaviours which we will reuse later (I
hope I'm not duplicating one someone already made).
If our players "enjoy" them enough we can give more mobs "don't look at
me" mechanics.
Removes some soul sprites.

## Changelog

:cl:
refactor: Basilisks and Watchers now use the basic mob framework. Please
bug report any unusual behaviour.
sprite: Basilisks have new sprites.
add: Basilisks will go into a frenzy if heated by energy weapons or
temperature beams as well as by lava.
add: Watcher eyes will be illuminated briefly when they are ready to
fire at you.
add: Watchers can now briefly put you into "Overwatch" and penalise you
for moving while they can see you.
add: Wounded watchers will occasionally punish players who look at them.
balance: Unusual watcher variants are more likely to appear.
/:cl:

---
## [ecivon-sca-ud/p-java-repo](https://github.com/ecivon-sca-ud/p-java-repo)@[9de80bf606...](https://github.com/ecivon-sca-ud/p-java-repo/commit/9de80bf606183b7b80c24d4896db8d922e133d28)
#### Sunday 2023-09-24 14:38:35 by ecivon-sca-ud

Oh yeah! You gotta get shifty...

Remember that VB project in which you were shifting from form to form? Kinda like that, yea?

---
## [lmorv/exo-matrix](https://github.com/lmorv/exo-matrix)@[6038a07f9b...](https://github.com/lmorv/exo-matrix/commit/6038a07f9bf7ee86360a133dde17c9980681322a)
#### Sunday 2023-09-24 14:46:17 by lmorv

lookDev: mood sketch

- Created a mood sketch for the main gameplay interface. I am not thinking too much about functionality at this point. I am just trying to create a sort of mockup of what the UI may look like and try to introduce a whole bunch of elements like icons, types of terrain, the title of the game in fancy lettering, and a dialogue text box.
- I used a screenshot of a section of Zaachila as a base and drew on top based on my notebook sketches. And tried to incorporate the 3 types of terrain I identified in my original sketch: agricultural 'matrices', elevated terrain, green areas (forest maybe), and urban areas.
- The text in the dialogue box is meant to both practical and introduce a bit of worldbuilding flavor. Alluding to both game mechanics and magical elements of the soft fantasy setting I am going for. It says: "The beetle helmet allows you to visualize information at the territory level."

---
## [benoit-pierre/koreader-base](https://github.com/benoit-pierre/koreader-base)@[b0f7e99845...](https://github.com/benoit-pierre/koreader-base/commit/b0f7e99845b16fc4176d3d29e4ffc258baa53cca)
#### Sunday 2023-09-24 15:36:53 by NiLuJe

Build: RPATH & escaping cleanup (#1638)

* Stop everything from including crappy build-time rpaths into binaries (lookin' at you, libtool).
* Enforce a set of DT_RPATH on everything we build to ensure we prefer our own libs over the system's.
* Do so via an ld include file, in order to go through all the buildsystem bullshit in order to defeat potential escaping issues.
* In the same vein, rework how we escape things in both makefiles and CMake files, in order to limit the interaction and/or dependency on shell escaping and/or globbing.
* Enforce DT_RPATH over DT_RUNPATH, because it gets honored for transitive dependencies, which will avoid some hilariously stupid things from happening once we get rid of LD_LIBRARY_PATH, which this moves also allows us to do.

Many thanks to @benoit-pierre for his insight, testing and reviews, this would have been way clunkier without his input ;).

---------

Co-authored-by: Benoit Pierre <benoit.pierre@gmail.com>

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[06e7270008...](https://github.com/Ical92/tgstation/commit/06e7270008d4b49a7e73fd088135822a9ec76891)
#### Sunday 2023-09-24 16:01:32 by GuillaumePrata

Funny clown internals (#77963)

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

Co-authored-by: CRITAWAKETS <sebastienracicot@hotmail.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[c921164b79...](https://github.com/Bubberstation/Bubberstation/commit/c921164b79c94f08b2eedacb9d711be4a3be617b)
#### Sunday 2023-09-24 16:41:56 by StrangeWeirdKitten

(Mostly-Modular) SSV Dauntless - Interdyne Rework (#520)

#481 Yeah I fucked up and my original PR closed.


![image](https://github.com/Bubberstation/Bubberstation/assets/95130227/4a42bb01-0558-4c92-8bb8-afb28e282c39)

## About The Pull Request

Replaces Interdyne only on Lavaland with an entirely new syndicate
outpost. It combines what made DS-2 so beloved with Interdyne.

## Why It's Good For The Game

Interdyne is old. It's lived out a good life, and when DS-2 was
remapped, people shifted more towards playing on DS-2. Sadly it was
removed, but I've spent the time to completely map an entirely new ship
that combines both DS-2 and Interdyne. It still takes up relatively the
same footprint. Now, everything is focused internally, with two
bluespace miners that have to be set up, and a prisoner spawner. All and
all, let's try something new and Bubber flavored.

**Edit:** Cybersun is an incredibly shallow ghost role and it only
breeds boredom, which then is sated in two ways:

- Space tide with syndi gear and the syndicate faction tag
- Screw with the station

Neither really is the goal for this server and this is being edited
after discussion with both Cheeto and Ozzo after apparently ruin
blacklist doesn't work on the config.

## Testing / Tour
Raw video. Buttons do work.

https://youtu.be/BHbOIwpqQqY

## Changelog

:cl: Danger Kitten
add: Lavaland has more Syndicate presence. SSV Dauntless has landed.
remove: Cybersun no longer spawns.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Shahd-ngm/Shahd-ngm.github.io](https://github.com/Shahd-ngm/Shahd-ngm.github.io)@[7b92bfbea2...](https://github.com/Shahd-ngm/Shahd-ngm.github.io/commit/7b92bfbea242bfae811c02e80414beada60c3f9a)
#### Sunday 2023-09-24 16:58:45 by Shahd-ngm

This is My Website

Title: Logic School of Arts – School of Arts in Z World

Concept:

The project aimed to create a website for a fictitious school situated in an alternate world called "Z World." This world redefined all norms and was discovered by artists in the year 1050.
The aim was to offer visitors an immersive experience that complements the video we did in class. The website has information about the school and its history. It also displays the video depicting the unique artistic approach of art in the school and widely in the world where it is situated. Also, the website allows interested individuals of all ages to sign in to learn more and eventually enroll in the school and enroll in it. The theme of this project is to convey mystery and intrigue visitors because it is a place where nothing is what it seems. To emphasize this a ghost was added to the website.

Process:

The implementation of my idea presented significant challenges. First and foremost, I did not know how to code, and I suddenly was doing HTML, CSS, and JavaScript. I was overwhelmed and scared at the beginning. I feel I had a limited time to explore these languages, but enough to get me started. I spent hours upon hours watching videos reading about these languages, and exploring. I invested countless hours in watching tutorials, reading documentation, and seeking examples online. While I made progress in a short span, web development is a constantly evolving field, and there is always more to learn.

 I think that the website development was both rewarding and frustrating. I had to examine and debug every single line to figure out errors and why things were not working. One extra coma, typo, or space would ruin the whole website and I had to squeeze my eyes to find it. This challenging experience made me realize how much I can do with little knowledge of coding. Who knew I could design a web? Editing and embedding the video was the easy part I would say.
During the implementation, I realized the best way to do the website is to think about each part within it in terms of blocks of a puzzle and my job is to put it together. I was systematic about it. I would do both HTML, CSS, and JavaScript together to make sure I get exactly what I want. If something does not work, I would comment on it dawn and get to it later. Google, YouTube, resources from Brightspace, and w3school were my friends through the whole process.

Reflection:

I am proud of the results. I think I was able to make the website work with no errors and support the video. It is esthetically simple with a clear idea. I think that the website successfully created a sense of intrigue and curiosity, as desired. However, I faced a lot of challenges and moments of frustration. I will say I learned a lot in this journey, especially in a short time.

Web development is an evolving field and consistent learning is important. I am excited to learn more about it because there is always room for improvement. I am sure that most of the things I have done have shortcuts that I still need to discover.

---
## [psydox/flame](https://github.com/psydox/flame)@[2f973abe8b...](https://github.com/psydox/flame/commit/2f973abe8b298a4f6f1164065783de560953d789)
#### Sunday 2023-09-24 17:28:04 by Luan Nico

docs: Improved spellchecking (#2722)

Improve our spellchecker (cspell) configuration and dictionary file
organization.

# Rationale

This is a proposal to establish a few changes:
* better separate our dictionary files into different categories of
types of words we are including
* improve the cspell regexes to be more aggressive
* be less lenient to what kinds of words we are adding to our
dictionaries
* have the dictionary file also serve as an explanation for obscure
references that cannot be easily derived from the word

Essentially my goal is that either when reviewing a PR that adds a new
entry to our dictionary, or when reading the dictionary files
themselves, it is immediately obvious what the entries are and why they
are there. Currently it can be just a dumpster we throw anything into if
spellcheck fails.

# Proposal

This PR-as-a-proposal essentially do the following changes.

## Split Dictionary Files

Proposes a better separation for our dictionary files. Currently we have
3 that are a bit broad and not super clear on what goes where. This
breaks it down a bit more and adds a comment to each file explaining
what kinds of terms should be added to each; that also serves as a
general guidance for what kinds of words should be added to the lexicon
in general, and makes it harder for mistakes to make into it.

* `flame_dictionary`: remains pretty much unchanged; it is dedicated to
Flame-related words, including companies, tools, and libraries (and
their associated concepts) mentioned on our codebase. Basically a
collection of proper-nouns relating to companies and libraries we
mention.
* `dart_dictionary`: new file for Dart and Flutter related terms
* `sphinx_dictionary`: unchanged, for Sphynx related terms
* `people_dictionary`: specific for people names and usernames
referenced on the codebase (in TODOs, mentions, etc)
* `words_dictionary`: actual English-language words (or common
abbreviations) missing from CSpell
* `gamedev_dictionary`: this was our biggest file that contained all
sort of things. it has been mostly broken down and now only contains
general development-adjacent terms and expressions

## Include definitions

Except for the `words` dictionary, which should be self-explanatory (as
it basically covers for "holes" in CSpell standard dictionary, which I
have been finding a bit lacking), every other file will contain terms in
the form:

```
word # definition of the word
```

What exactly the definition is can slightly vary depending on which
dictionary file we are talking about, but the examples should be
self-explanatory.

As an example, for the gamedev file, it should provide some simple
guidance as to what the term means, or if it's an acronym or
abbreviation, what it stands for. The goal is not to teach the entire
concept to someone unfamiliar, but allow them to "google" it for
themselves by giving enough context, so they can confirm their
suspicions. For example, if they see `LTRB` somewhere by itself, they
are not able to "just google that" because it is too vague. The
dictionary file provides enough context for the user to figure out
however much deeper information they want about any particular subject.
It will also disambiguate from any non-Flame related homonyms. For
people on the people file and companies on the flame file, the
description will provide links to clearly disambiguate what they are;
for tools, a brief description of what the tool is for is also included.
And so on.

The goal is not to build a comprehensive, in depth-guide to each word we
use, but rather to give the bare minimum of context on what this term
"is doing" on our codebase.

## Be less lenient with terms

My idea with these two major changes combined, is that we are overall
more tactical about which terms we want to add to the dictionaries.
Adding a word to the dictionary file is essentially giving carte blanche
to anyone in the future to reuse that term anywhere. I think we should
see spellchecker violations as "warnings"; we decide on the set of
warning rules we want to enable for the entire project (hopefully all
the ones that make sense; or have a reason for disabling the ones that
don't). We might need to violate these warnings sporadically, for
example, we ban `print` on the codebase but might need to allow it
specifically in a couple places. But we would not disable the entire
warning to do that, rather we would add a specific comment-bypass on the
smallest possible scope that encompasses all the relevant lines. We
would also add a proper comment explaining why we are bypassing the
general rule in this specific place.

Similarly, we should not have one-off violations on the dictionary file,
even if they make sense in the one place they occur, but we should
encourage more liberal use of scoped bypasses for such cases. These
Ukrainian words are required in this file, but should not be on the
dictionary as it does not make sense to use foreign languages anywhere
else:

```
// used as examples of Ukrainian words on the documentation below
// cSpell:ignore рушниця, рушниці, рушниць
```

It might look inelegant to have to include that, but just like a
warning-bypass comment, accompanied by the explanatory proper-comment,
this actually provides helpful guidance and context for the reader that
might be confused with the usage of incomprehensible terms.

This also encourages people to avoid obscure terms that are not already
in our dictionary (i.e. that we have already "bought in" and paid the
mental load investment cost), making our code (and docs) easier to parse
and read for everyone. I want to be extremely clear that that **does
not** mean we need to "dumb down" anything whatsoever, or do any sort of
gymnastics to avoid the wrath of an incompetent spellchecker.

But, for example [when spelling "cave
ace"](https://github.com/flame-engine/flame/pull/2304) in variable names
in a random example, having it typed as `caveAce` instead of `caveace`
can slightly help with readability, specially for non-native speakers
(like most of us). It is an extremely minor insignificant gain, but
having the dictionary file require a brief description will nudge us to
give a bit more thought into each "bypass" we are adding.

(note: a similar issue that I have not yet addressed is "spine boy", but
I will leave that for followups and just added that one to the
dictionary for now, as I am still over the fence on that one since it is
an actual "known" character with a dedicated page, so it is more like a
proper noun - as a specific decision I think it is out-of-scope of the
broader discussion).

---
## [marthl1/marth_is_so_tired](https://github.com/marthl1/marth_is_so_tired)@[d4cdf03485...](https://github.com/marthl1/marth_is_so_tired/commit/d4cdf034857f05a4ab102ecfa62293103b269479)
#### Sunday 2023-09-24 17:40:20 by marthl1

Add files via upload

holy crap i really can't imagine that i would post it. it's kinda joke for my sleepless brain

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[172f65989e...](https://github.com/Pickle-Coding/tgstation/commit/172f65989ea40418b1c03316ad3163ee67f06e94)
#### Sunday 2023-09-24 17:43:37 by Jacquerel

Nuclear Operative Jump Jets (#78088)

## About The Pull Request

This PR gives operative MODsuits access to "jump jets".
This is an activated module (starts pinned) with a 30 second cooldown
which removes your personal gravity for 5 seconds and (if possible)
pushes you upwards by one z level. In combination with your regular
jetpack this allows you to fly over gaps, and (most importantly) out of
pits such as you may inadvertently find yourself wandering into on
Icebox.
I have a few other changes I want to make specifically targetted at the
experience of Icebox station destruction causing people to fall several
z levels and get trapped, but this is the first one.

You have to stand still for 1 second to activate the jump jet. This is
because jetpack movement without gravity is actually usually faster than
an operative will walk, and I don't want them to just toggle it as a
sprint button while running around. If people find other tactical uses
for this though I think that's cool.

This module currently isn't available to crew on the tech web, although
maybe someone could add it later if they wanted to. It's not quite so
useful if you don't _also_ have a jetpack though.
I bumped the available complexity of the suits I attached it to up by
the complexity cost of this module so it's not taking up previously
available space.

## Why It's Good For The Game

It's funny when the whole ops team falls in a hole after an explosion
they caused and gets stuck in there fighting Snow Legions but they
should probably have some method for dealing with that.
It also lets them pop back up from the tram hole, a risky proposition
because any flying mob hit by the tram dies almost instantly.

## Changelog

:cl:
add: Operative MODsuits now have an attached "jump jet" which sends you
upwards and allows you to use your jetpack under gravity for a few
seconds, perfect for navigating the pits and valleys of Icebox Station.
/:cl:

---
## [Frank-py/ChessQLD](https://github.com/Frank-py/ChessQLD)@[fb405586ce...](https://github.com/Frank-py/ChessQLD/commit/fb405586ce50fe1cee438a18431498e5cac5d182)
#### Sunday 2023-09-24 19:29:08 by Daniel

Such a fucking waaste of time, i hate my life. Nothing works

---
## [Yeetov/USRPFP-Reborn](https://github.com/Yeetov/USRPFP-Reborn)@[c11c40084a...](https://github.com/Yeetov/USRPFP-Reborn/commit/c11c40084a1acaebc017e78f12cb3d80165026af)
#### Sunday 2023-09-24 19:31:13 by coolesding

NOW IT SHOULD WORK MY FUCKING GOD I HATE YOU GITHUB

---
## [zsergey/Telegram-iOS](https://github.com/zsergey/Telegram-iOS)@[003be80f3d...](https://github.com/zsergey/Telegram-iOS/commit/003be80f3d8710950ef85f973ae0e3feaf7eb716)
#### Sunday 2023-09-24 19:34:13 by Sergey Zapuhlyak

Hey you! Yes, you. Unmotivated shit. Remember! If someone offended you, don't get offended. If someone hit you, don't hit yourself. You're not a loser. You're a winner! In this life, all the painted gates are open to you. Don't look a gifted horse in the ass! Get rid of your "don't want, can't, won't" excuses once and for all. Bend over. Shut up! You're like an electrical outlet, you shock at 220 volts! You know it! Your future and your son's success are in your hands, I believe. Don't despair. Breathe. Or you'll die. You're not a fool. You can go further, do more, камон эврибади пуче хэндс ап! And remember one, and two, three, four. In other words, forever! Аттек катер кэнди шап. Eat. A lot. Sausages in dough.

---
## [TimUkrainian/zechub](https://github.com/TimUkrainian/zechub)@[73c19fca40...](https://github.com/TimUkrainian/zechub/commit/73c19fca4090fe98704f75112418158d2736159e)
#### Sunday 2023-09-24 19:42:32 by Hardaeborla

zecweekly58.md

#Iwe Iroyin Osẹ-ọsẹ Zec #58

Ìwé ìròyìn ZF tí Oṣù August, Awọn ohun elo ṣi ṣii fun Awọn ifunni Kekere àti Ìṣe ilu alabagbepo tí ń bo 

 Atunto nipasẹ "Hardaeborla "[(@hardaeborla)](https://twitter.com/ayanlajaadebola) ati Itumọ si ede Yoruba nipasẹ "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

### EKaabo si ZecWeekly

Kaabọ si ọsẹ igbadun kan nibiti a ti mu cryptocurrency tuntun ati awọn imudojuiwọn ilolupo Zcash wa fun ọ. Iwe iroyin ti ọsẹ yii pẹlu ikẹkọ lori awọn adirẹsi Zcash, awọn ifojusi lati iyipo keji ti eto fifunni kekere nipasẹ Zcash Foundation, ati awọn imudojuiwọn lati gbogbo agbegbe Zcash.
---

## Nkan Ẹkọ ti Ọsẹ yii
Ti o ba jẹ tuntun si Zcash, iwọ yoo ṣawari awọn oriṣi iṣowo meji ti a mọ bi sihin ati aabo. Fun awọn ti o tẹle awọn idagbasoke Zcash aipẹ, o tun le faramọ pẹlu Adirẹsi Iṣọkan lori Nẹtiwọọki Zcash. Ibeere bọtini ni bawo ni awọn adirẹsi wọnyi ṣe n ṣiṣẹ ni awọn apamọwọ Zcash.

Kọ ẹkọ diẹ sii: [Wiwo awọn adirẹsi Zcash](https://wiki.zechub.xyz/visualizing-zcash-addresses) 


## Awọn imudojuiwọn Zcash

####  Awọn imudojuiwọn ECC ati ZF
[Zooko Yoo Soro ni Mainnet tí Ọdún 2023 Oṣu Kẹsan ni ìjọ 20-22](https://twitter.com/MessariCrypto/status/1696289078743060668?t=BoeIGgLj-1E5a0gG3EmSyg&s=19) 

[Mu soke ⏭️lori gbogbo awọn igbejade Zcon4](https://twitter.com/ZcashFoundation/status/1697683679017910761?t=O1BOX3KBRlhMa5O-1UySCw&s=19) 

[Zcash Foundation 📰 Ìwé ìròyìn tí Oṣù Kẹjọ](https://zfnd.org/zcash-foundation-august-2023-newsletter/) 

["Ṣé o mọ…?" - @ZcashFoundation](https://twitter.com/ZcashFoundation/status/1696220390081630649?t=kR1czvJRrTwyRow3VUZhGg&s=19) 

[Ètò Àwọn ifunni Kékeré ZF Yíká tí èlé kejì tí bẹ̀rẹ̀](https://twitter.com/ZcashFoundation/status/1697683688543182961?t=q99lgXcT5yTvodQwXnTYgA&s=19) 




####  Awọn imudojuiwọn Awọn ifunni Agbegbe Zcash

[Ṣeto Olurannileti Rẹ Fun Owó Town Hall tí Zcash Dev ni Ọdún 2024](https://twitter.com/zerodartz/status/1696520352665604280?t=GUqwlspErtJtqlpQbH_Rgw&s=19) 

[Iṣẹlẹ Awọn ifunni Agbegbe Zcash lori Discord](https://twitter.com/ZcashCommGrants/status/1696965307376586818?t=wcyWJ76a1EBEM3NqX9WsaQ&s=19) 

[Awọn iṣẹju ipade ZCG 08/21/23](https://forum.zcashcommunity.com/t/zcash-community-grants-meeting-minutes-8-21-23/45505) 


#### Awujo Ise Agbese 
[Igbero Tuntun 🆕 Láti Ọ̀dọ̀ ZecHub](https://twitter.com/dismad8/status/1696938238555074730?t=0Yb3-ZUaHnlXFIC5O459FQ&s=19) 

[Ṣetọrẹ si Eto “Gbigba Zcash Si Awọn ile-iwe”🙏](https://twitter.com/OGA4SKY/status/1697400463170122019?t=YZY9lJs0TELKwXsA4Bz83g&s=19) 

[DWeb Camp ṣeto lati ṣẹlẹ ni Ubatuba](https://twitter.com/zcashbrazil/status/1697612560969695382?t=Fcq2nX6Ed2Q52YUgZx_72g&s=19) 

[ZFAVClub lati ṣe atilẹyin Iṣẹlẹ Ibudo DWeb ni 🇧🇷Brazil](https://twitter.com/ZFAVClub/status/1697614302838919574?t=CTegZAaM3xLuszXeS78BpQ&s=19) 

[Ẹya akọkọ ti Free2Z Night!](https://twitter.com/gordonesroo/status/1696578807254118624?t=wCEEiZAP7Kev63zJv4Kb7w&s=19) 

[Tẹle ki o kọ ẹkọ diẹ sii nipa Zcash Book Club📖] (https://twitter.com/zcashesp/status/1697268356716359990?t=-bJB-XkhEf2Pi7RRemq38g&s=19) 

#### Iroyin ati Media 
[Crypto streamer padanu owo nitori ifihan bọtini ikọkọ lairotẹlẹ - Cointelegraph](https://cointelegraph.com/news/brazilian-crypto-streamer-loses-50k-by-exposing-private-key) 

[Oludasile Solana - "FTX SOL yẹ ki o pin si awọn onibara" - Decrypt](https://decrypt.co/154663/solana-cofounder-says-ftx-sol-should-distributed-customers) 


[Rupee òní nọ́mbà ń gbà ìgbé lárugẹ lílo pẹ̀lú isọpọ Yes Bank pẹlu UPI - Cointelegraph](https://cointelegraph.com/news/digital-rupee-gets-big-usability-boost-through-yes-bank-integration-with-upi) 

[Owó Àwọn Oludokoowo Bitcoin tí wọ́ $1.5 Billion](https://www.coindesk.com/markets/2023/09/01/large-bitcoin-holders-accumulate-15b-worth-of-btc-as-price-wavers) 

[Vitalik ta gbogbo àwọn owo rẹ lórí Maker DAO r - Trustnodes](https://www.trustnodes.com/2023/09/03/vitalik-buterin-ditches-mkr) 

[Ilana iwọntunwọnsi lo nilokulo fun $900K bi awọn hakii DeFi ṣe gbe soke - Cointelegraph](https://cointelegraph.com/news/balancer-protocol-exploited-for-900k-as-defi-hacks-mount-finance-redefined) 

## Awon oro die Nipa ZCash Lori Twitter
["Zcash ni ojo iwaju 🌅" - Splitcoin](https://twitter.com/splitcoincom/status/1696582966867312770?t=fPvCQCwlU8bDgfiJz8SeQg&s=19) 

[Sopọ, Kopa ati Pinpin Adarọ-ese rẹ🎙️ - ZcastEsp](https://twitter.com/ZcastEsp/status/1697256155272368545?t=Crhrt2iQgRZ54ZxI1mczjQ&s=19) 

[Lilo Zingo fun Iṣowo Rẹ] (https://twitter.com/ZingoLabs/status/1696211862470230294?t=Krkokr7jE2hsgDuf0rn0og&s=19) 

[Idide ti Zec Chapter 6 nipa @zcashCrusader](https://twitter.com/ZcashCrusader/status/1696758204569735236?t=pCZ8EDpVvF_-_cEi7wb0ng&s=19) 

[Igbèrò PayWithZcash FIO](https://forum.zcashcommunity.com/t/usernames/45504) 

[Awọn dukia Shielded Zcash 📊 n gun oke!](https://twitter.com/zooko/status/1697306927813005653/photo/1) 

[$ZEC pẹlu awọn Crypto oke marun ti ò ṣe mine ⛏️ ni ilé] (https://twitter.com/Cindy_Chando/status/1697849959968583840?t=UhAqpp31c6GNJg9gI9x0RQ&s=19) 


[Se Asiri Tuntun Deede?](https://twitter.com/techmindsmentor/status/1697838511922241631?t=tczFIS7hSR-iZtCF-YID9A&s=19) 

[Awọn ilana Lo nipasẹ Free2Z lati ṣe igbasilẹ Adarọ-ese wọn](https://twitter.com/zcashesp/status/1697781752125698088?t=zzsWn-8jdFMebCdBEEL40g&s=19) 

[Bull Run fun Asiri eyo? - NagatoDharma](https://twitter.com/NagatoDharma/status/1697609324003045867?t=0EOMchNKit9pOuCnueCKog&s=19) 

[Bitcoin ati Zcash ni ibatan si z-adirẹsi ati t-adirẹsi](https://twitter.com/ruzcash/status/1697830481381790120?t=lwf_XUkmsB3PuWapHXBXWQ&s=19) 

[Andrew Arnott fihan ìtọrẹ Maui ṣee ṣe pẹlu Zcash](https://twitter.com/aarnott/status/1697753434097938653?t=VlF4plbfsFoasDliSPvTIg&s=19) 

[Arakunrin Abila ni mi 🦓 - Yoditar](https://twitter.com/yoditarX/status/1697739731595899157?t=ccumO9xFA8dMDFsqCBTEsg&s=19) 

[Zcash Ṣe afihan nipasẹ Zellic "Ibere ​​si ZK👩‍🏫"](https://twitter.com/zellic_io/status/1697710984486678707?t=yFMnvjm8_5fS_Q2Lbk9s0Q&s=19) 

[Aṣiri yoo jẹ aṣa ati itan nigbagbogbo - @Michae2xl](https://twitter.com/michae2xl/status/1697699658355609978?t=rkWQVQWaQaUvjDwy1Nc4BQ&s=19) 





## Zeme ti Ose Yii 

[https://twitter.com/DarwinJZ11/status/1697654861355999277?t=SgNv5wS1bcoT5zvYtFLUqQ&s=19](https://twitter.com/DarwinJZ11/status/1697654861355999277?t=SgNv5wS1bcoT5zvYtFLUqQ&s=19) 


## Awọn iṣẹ ni ilolupo
[ZecWeekly #59  iwe iroyin Agbegbe](https://app.dework.xyz/zechub-2424/board?taskId=102e34d1-8f77-45d1-bd4f-d3d8f2a040ce) 

[Ṣiṣe Zcash Full Node lori Akash Network](https://app.dework.xyz/zechub-2424/board?taskId=543cab70-627d-4222-a712-9fb8768abe9c)

---
## [thanhdoan1201/reshade-shaders](https://github.com/thanhdoan1201/reshade-shaders)@[2879716bd1...](https://github.com/thanhdoan1201/reshade-shaders/commit/2879716bd19d88460c3afe4bde82e0801ba3d926)
#### Sunday 2023-09-24 21:20:47 by BlueSkyDefender

Update Depth3D.fx

Depth3D: Harden to help prevent cheating.                                                       -=let me know if I can do more=-

+Cursor Is now Bound to the 3D image only.
+Removed Depth Buffer Debug view to keep users from using this to cheat.
+Basic VR Compatibility added so that it can be used with VR Desktop apps.
+Basic Theater Mode added for Cellphone VR users.
+Renamed many items in the UI to help new users with controlling this shader.
+New Depth Detection Code.
+New Screen Boundary Detection added.
+Edge Handling added from SuperDepth3D

Fixed issues with the UI in Freestyle and automated many functions as I could to reduce UI clutter. The idea was to keep as much of the functionality as possible without sacrificing too much.

Fixed issues with NV System that was causing a black screen on my Testers PC. This was not easy, I had to remote into a user's pc halfway across the world since I needed someone with an NV Card that was able to help me. Seems like this may be an issue for me with porting my other shaders. Thank you, Durante - aka Dorinte & TheGordinho - aka Gordinho

The goal of Depth3D to allow users to experience the world of 3D Gaming by adding real depth to your game. -=This shader requires depth access to work=-

This shader will work with 3D TV, 3D Monitors, and the NEW VR HMDs. The VR Theater experience worth exploring in VR.
Here are two free applications for VR Headsets That I seen people use that anyone can try.
Virtual Space
https://store.steampowered.com/app/703480/Virtual_Space/
Big Screen
https://bigscreenvr.com/help/gettingstarted/sbs3d/

Older games and non-VR games can benefit from being played again with Stereo3D.
I have been working on My 3D Shader for some time now and learned how to improve things over time even with limitations. My hope is to share this experience with as many people as possible.
I would like this shader to be considered as a standard shader to be used as openly as NV discontinued 3DVision Stereo Software. Since I know many users in the 3D community still enjoy 3D gaming.

Please let me know if there is anything I can change. That can help. Thank you.

Noted Issues
One of the things that bug me with Depth3D It's hard to use for new users. So I will be making better tutorials when I have the hardware to do so for VR.

---
## [Aurorastation/Aurora.3](https://github.com/Aurorastation/Aurora.3)@[faca6da739...](https://github.com/Aurorastation/Aurora.3/commit/faca6da7397d1a2051a2edb4d17c564037a1e516)
#### Sunday 2023-09-24 22:38:55 by Wowzewow (Wezzy)

The Food Sortening, Extra Pain-In-My-Ass Edition (#17393)

* The Food Sortening, Extra Pain-In-My-Ass Edition

Sorts all food sprites and cuts down the MONOLITH snacks.dm and food.dmi. This was an absolute pain in my ass. No front-facing changes.

Planning to add more shit down the line. Makes everyone's lives easier.

* changelol

* finally

* inhands

* merge conflict

* this really "ticked" me off HAHAHAHAHS

* fixes

* make megalinter happy

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[784efe9b51...](https://github.com/silicons/Citadel-Station-13-RP/commit/784efe9b514256072f90ffbae9acebe38b2f5b4f)
#### Sunday 2023-09-24 23:56:04 by CharlesWedge

The Hive Awakens (#5940)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## Oh No More Robots
There is actually less paths for the hivebots. They are actually some of
the most primitive mobs on the codebase. So it was high time they were
given a facelift. As I said with my previous mob update robots are a
good alternative as mobs compared to humanoids, and with the hivebots we
can present a threat of hostile machine intelligence to round out the
existing threats of pirates, mercs, aliens beasts and the supernatural.
Once more these robots are also far mroe generalist then the existing
robot varieties and as most types of them are not very dangerous they
can be released on civilian crew without fear of them causing extreme
damage,

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
add: A couple new varieties of both melee and ranged hivebots
removed: redundant hivebot varieties
tweak: siegebots now have sniper range fitting their name, their attack
has been nerfed (holy fuck the one shoot explode on contact grenades
with a base attack of 10... that's 1 frag grenade a second!!!)
fix: hivebots now use their various cataloguer entiries
sprites: hivebot types are now more visually distinct
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---

