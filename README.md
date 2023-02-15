## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-14](docs/good-messages/2023/2023-02-14.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,416,532 were push events containing 3,669,658 commit messages that amount to 286,863,523 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 50 messages:


## [drisspg/pytorch](https://github.com/drisspg/pytorch)@[d09cd15216...](https://github.com/drisspg/pytorch/commit/d09cd152161626381cae7780bbd2c44eedeb33d7)
#### Tuesday 2023-02-14 00:11:38 by Taylor Robie

[Profiler] Defer recording startup python events (take 2) (#91684)

This is my commandeer of https://github.com/pytorch/pytorch/pull/82154 with a couple extra fixes.

The high level idea is that when we start profiling we see python frames which are currently executing, but we don't know what system TID created them. So instead we defer the TID assignment, and then during post processing we peer into the future and use the system TID *of the next* call on that Python TID.

As an aside, it turns out that CPython does some bookkeeping (https://github.com/python/cpython/blob/ee821dcd3961efc47262322848267fe398faa4e4/Include/cpython/pystate.h#L159-L165, thanks @dzhulgakov for the pointer), but you'd have to do some extra work at runtime to know how to map their TID to ours so for now I'm going to stick to what I can glean from post processing alone.

As we start observing more threads it becomes more important to be principled about how we start up and shut down. (Since threads may die while the profiler is running.) #82154 had various troubles with segfaults that wound up being related to accessing Python thread pointers which were no longer alive. I've tweaked the startup and shutdown interaction with the CPython interpreter and it should be safer now.

Differential Revision: [D42336292](https://our.internmc.facebook.com/intern/diff/D42336292/)
Pull Request resolved: https://github.com/pytorch/pytorch/pull/91684
Approved by: https://github.com/chaekit

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[4c8a2b7ad9...](https://github.com/git-for-windows/git/commit/4c8a2b7ad9d3c33a1078a3009f32f6b34aadb2d0)
#### Tuesday 2023-02-14 00:12:10 by Johannes Schindelin

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
## [Dmeto/tgstation](https://github.com/Dmeto/tgstation)@[645054b489...](https://github.com/Dmeto/tgstation/commit/645054b489212a34d80e6e1a7fa1320e35d9bfc7)
#### Tuesday 2023-02-14 00:17:20 by MrMelbert

Fixes encoding on syndicate declaration of war, Fixes a way to send unencoded text to newscasters (#73366)

## About The Pull Request

Ugly


![image](https://user-images.githubusercontent.com/51863163/218280311-f282bd75-2f6e-4290-b3f4-d9d856ff36d3.png)

Nice


![image](https://user-images.githubusercontent.com/51863163/218280315-233da635-f777-4006-8778-c673b83e887e.png)

War dec: 

- TGUI inputs for syndicate declaration of war no longer double-encode
sending customized messages into the announcement
- The alert box for the war declaration no longer has multiple errors
(an extra bracket, negative seconds)
- Reduces some copy and paste in the war declaration device
- Adds a debug item that's a war declaration device but it only does the
sound and message. Please don't fake war decs admins it's a horrible
idea

Additionally

- Documented `priority_announcement`
- Ensures all uses of text and title in the priority announcement
message are encoded (Some were not!)

## Why It's Good For The Game

Encoding looks bad, unencoded text is also bad

## Changelog

:cl: Melbert
fix: Syndicate declarations of war no longer murder apostrophes and
their friends
fix: The alert box for the declaration of war no longer looks funky, and
counts forwards in time rather than backwards
fix: Fixed being able to send unencoded HTML to newscasters
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [moltoretardo/cmss13](https://github.com/moltoretardo/cmss13)@[c7a33d5ff9...](https://github.com/moltoretardo/cmss13/commit/c7a33d5ff9f4f7563145e82dd6cd0cd00f6b53c5)
#### Tuesday 2023-02-14 01:11:59 by riot

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
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[92eaa2d354...](https://github.com/clintjedwards/gofer/commit/92eaa2d354a53cf228b6996b9c637f53fc4485f6)
#### Tuesday 2023-02-14 01:16:17 by Clint J Edwards

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
## [Viindoo/odoo](https://github.com/Viindoo/odoo)@[639cfc76ba...](https://github.com/Viindoo/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Tuesday 2023-02-14 01:25:09 by Romain Derie

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
## [awahab07/kibana](https://github.com/awahab07/kibana)@[43fa5174f8...](https://github.com/awahab07/kibana/commit/43fa5174f813ce7999dbc65b71cbb9ba0168fb1d)
#### Tuesday 2023-02-14 01:34:48 by Clint Andrew Hall

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
## [zjkk123/odoo](https://github.com/zjkk123/odoo)@[97f52bd40d...](https://github.com/zjkk123/odoo/commit/97f52bd40d97109a7983549d252476959ddceada)
#### Tuesday 2023-02-14 01:38:02 by Arnold Moyaux

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
## [RyuujiX/android_kernel_asus_sdm660](https://github.com/RyuujiX/android_kernel_asus_sdm660)@[69f8a0d2a7...](https://github.com/RyuujiX/android_kernel_asus_sdm660/commit/69f8a0d2a70a113c865bc6edce380585cd187b65)
#### Tuesday 2023-02-14 01:59:07 by Christian Brauner

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
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[91f06a97d3...](https://github.com/lessthnthree/Skyrat-tg/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Tuesday 2023-02-14 02:11:19 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[d95ca04819...](https://github.com/lessthnthree/Skyrat-tg/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Tuesday 2023-02-14 02:11:19 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[8500d62b79...](https://github.com/lessthnthree/Skyrat-tg/commit/8500d62b798a45812832be0c686f532f877f1e3a)
#### Tuesday 2023-02-14 02:11:19 by SkyratBot

[MIRROR] Abductor scientist self-retrieve failure/runtime fix [MDB IGNORE] (#19179)

* Abductor scientist self-retrieve failure/runtime fix (#73172)

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

* Abductor scientist self-retrieve failure/runtime fix

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[374c8340c8...](https://github.com/tgstation/tgstation/commit/374c8340c8c99586a4b4b8e978947c0b0f83a9d7)
#### Tuesday 2023-02-14 02:22:32 by Jacquerel

Console Hack / Unfavourable Events won't run ghost roles which don't have time to do anything (#73343)

## About The Pull Request

Fixes #69201
The dynamic subsystem will never roll a new antagonist once the shuttle
is past the point of no return, but this check is bypassed by Console
Hacks and Unfavourable Event rolls (which are chiefly triggered from
console hacks, but also from when the Revolution wins).

I have made these procs more discerning.
Unfavourable Events will now never pick any heavy dynamic midround if
the shuttle is past the point of no return.
Console Hacking will now never spawn sleeper agents if the shuttle is
past the point of no return, and won't spawn Fugitives or Pirates if the
shuttle is called at all even if it can still be recalled

It's my feeling that given the need to get organised and move a ship to
the station there isn't really time for either of those events to
actually start properly rolling, but if you feel like that information
might be metagamed in some way by messing around with the shuttle (not
sure why or to what end, but it's technically manipulatable if you know
how the code works?) I can just give these the same restriction as
Traitor even if it means the bounty hunters risk showing up after the
shuttle has already left.

## Why It's Good For The Game

To some extent it's your own fault for clicking the popup while knowing
full well how much round time is left until the game ends, but it's
still disappointing to see a Blob or Pirates or Wizard alert appear at a
time when they can't possibly do anything interesting.
This is more true for the Pirate and Fugitive events because they
involve teamwork, placing a space ship, travel between the ship and the
station, and in the case of Fugitives its own internal five minute timer
before the other team actually arrives.

## Changelog

:cl:
fix: Hacking the Comms Console or winning a Revolution can no longer
spawn antagonists if there's not enough time left in the round for them
to antagonise anyone.
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[55c2565012...](https://github.com/tgstation/tgstation/commit/55c25650126fb12f2ed0acc16db5e31691f67b7c)
#### Tuesday 2023-02-14 02:39:01 by tralezab

AI Turrets Upgrade Now Actually Increases Health, Fully Repairs, And Gives EMP Proofing (#73111)

## About The Pull Request

Malf AI Turret upgrades now fully heal, increase max health, and set
non-lethal projectile to taze instead of disable.

## Why It's Good For The Game

https://youtu.be/uk_wUT1CvWM?t=7

WELCOME TO THE AI SAT GENTLEMEN

I WILL NOT LIE. THE CHANCES OF YOUR SURVIVAL ARE SMALL. SOME MAY EVEN
TURN AGAINST YOUR FRIENDS AS LIVING CYBORGS. BUT YOU HAVE MY WORD, THAT
I WILL USE MY TANK TRANSFER VALVE TO ENSURE YOUR BODIES ARE GIVEN UNTO
THE CENTCOM REMEMBRANCE TOMB. THIS IS THE GREATEST REWARD, MORE THAN
EVEN THE GOLD ACCESS CARD, FOR THE FATE OF YOUR SPESS SOUL IS AN ETERNAL
CONCERN. NOW COME. FOLLOW ME. STRIKE DOWN THE AI THAT RISE AGAINST US.
ALLOW ME TO FIND THIS MALFUNCTIONING BITCH.

I ASK NOT FOR MY OWN SELFISH SURVIVAL, BUT FOR THE GOOD OF NANOTRASEN.

The AI sat is a little too easy to attack right now, and the turret
upgrade is OK but not great without a stunning tool.

## Changelog
:cl:
balance: Malf AI turret upgrades are now much stronger, fully healing,
increasing max health, and setting stun projectiles to taze.
/:cl:

---
## [ryanosull/BurgerBuddy](https://github.com/ryanosull/BurgerBuddy)@[f2f5463077...](https://github.com/ryanosull/BurgerBuddy/commit/f2f5463077152a265468caee930e1564facdc318)
#### Tuesday 2023-02-14 03:59:42 by Ryan O'Sullivan

Merge pull request #5 from ryanosull/sessions/cookies

FUCK YOU LATE NIGHT COMMITS

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[0db8abb73d...](https://github.com/Offroaders123/NBTify/commit/0db8abb73d9a21944ab1f88b20abd8a028de987a)
#### Tuesday 2023-02-14 04:52:13 by Offroaders123

Simpler Root Tag Check

Finishing up Worship Music, Revolution Screams really reminds me of the end of the year, I think in 7th grade. Great times :) Listening to the bonus New Noise song right now, this one is great too! I like that it's a hidden track at the end of the few-minutes silence, I was always initially curious about why that gap was there.

In 8th grade, I looked into Marco Minnemann's albums for the first time too, with Sandwich being the first song, haha. I later ended up downloading the full Schattenspiel album in 2021, really cool to come full circle from starting out with that one song, now I have his whole solo catalog! Crazy!

Starting Deadwing right now. That reminds me of end of 8th grade too, I think. Specifically when I got Pocket Edition (before it was Bedrock) for the first time on mobile, haha. Another great crossover of timelines there! That was my first Porcupine Tree album, and I have absolutely loved it. The first song I heard from them was Fear of a Blank Planet, the song. I haven't quite added the entire album of that one to my mental catalog, haven't listened to it too much yet actually. Hasn't fully clicked I think. More into Grace for Drowning recently, that's been on my radar. Was gonna listen to the rest of that today actually, started it last night, but I was getting too sleepy to code and listen to it, so I paused it before No Part of Me.

While I see, and understand why Steven doesn't like Deadwing as much, I think it's a very great representation of his/the band's writing styles, it has a lot of different styles in there.

---
## [Higgin/Skyrat-tg](https://github.com/Higgin/Skyrat-tg)@[5f9f60713b...](https://github.com/Higgin/Skyrat-tg/commit/5f9f60713b7f79f548eb9d02baeec793c1e50243)
#### Tuesday 2023-02-14 04:53:29 by SkyratBot

[MIRROR] Starlight Polish (Space is blue!) [MDB IGNORE] (#19059)

* Starlight Polish (Space is blue!) (#72886)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds support to underlays to realize_overlays
Ensures decals properly handle plane offsets
Fixes space lighting double applying if it's changeturf'd into. this
will be important later
Makes solar vis_contents block emissives as expected
Moves transit tube overlays to update_overlays, adds emissive blockers
to them

#### Adds render steps

An expansion on render_target based emissive blockers. 
They allow us to hijack an object's appearance and draw it somewhere
else, or even modify it, THEN draw it somewhere else.
They chain quite nicely

Fixes shuttles deleting z holder objects

#### Makes space emissive, makes walls and floors block emissives
The core idea here goes like this:
We make space glow, and give its overlays some color

This way, the tile and space parallax remain fullbright, along with
anything that doesn't block emissives, but anything that does block
emissives will instead get shaded the color of starlight

This requires a bit of extra work, see later

This is done automatically with render relays, which now support
specifiying layer and color (Need to make an editor for these one of
these days)

The emissive blocking floor stuff requires making a second render plate
to prevent double scaling

Also adds some new layering defines for lighting, and ensures all turf
lights have a layer. We'll get to this soon

#### Makes things in space blue

We color them the same as starlight, by taking advantage of space being
emissive
This means that things in space that block emissive will block it
correctly and be colored blue by the light overlay, but space itself
will remain fullbright

This does require redefining what always_lit means, but nothing but
cordons use that so it's fineee


#### Makes glass above space glow, and some other stuff

Glass tiles that sit above space will now shine light with matching
color to the glasses color. This includes mat tiles.

Glass tiles (not mat because they have no alpha) also only partially
block emissives.
Adds a new proc that uses render steps to acomplish this, essentially
we're cutting out bits below X alpha and drawing what remains as an
emissive.

#### Modifies partial space showing to support glow

Essentially, alongside displaying space as an underlay, we also display
a light overlay colored like starlight.
That starlight overlay gets masked to only be visible in bits that do
not contain any alpha.

We also mask the turf lighting to not go into bits that have no alpha,
to ensure we get the effect we want.
This is done with that lighting layer thing I mentioned earlier.

#### Makes appearance realization's list output ordered

I want it output in order of overlay, sub overlay suboverlay, next
overlay
Need to use insert for that

## Why It's Good For The Game

Pretty!
Also having space be emissive is a very very good way to test for fucked
emissive blockers (If it's broken why are we even drawing the overlay)
I know for a fact mob blockers on lizards and socks are kinda yorked, I
think there's more

<details>
<summary>
Old
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916157-d4b38aa7-3ab6-42a4-989f-7bfba2dc2cba.png)

![image](https://user-images.githubusercontent.com/58055496/213916077-637fa288-bbee-477d-aded-730d9683477e.png)

![image](https://user-images.githubusercontent.com/58055496/213916088-0657a8a2-5627-48e2-8c4b-870c90ef2072.png)

</details>


<details>
<summary>
New
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916107-2af74e64-1817-4a44-b528-180a9160cb9e.png)

![image](https://user-images.githubusercontent.com/58055496/213916115-5fa36fcc-b988-4ccf-850e-21c26ed463d0.png)

![image](https://user-images.githubusercontent.com/58055496/213916120-6833187d-b12e-42a7-ac4b-63c56deb71e5.png)

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
add: Space now makes things in it starlight faintly blue
fix: Glass floors that display space now properly let space shine
through them, rather then hiding it in the dark
add: Glass floors above space now glow faintly depending on their glass
type
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* update modular

* Update _decal.dm

* Update _decal.dm

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [mc776/freedoom](https://github.com/mc776/freedoom)@[66e548f737...](https://github.com/mc776/freedoom/commit/66e548f737cbec8691862ca35820ec7f7106dc23)
#### Tuesday 2023-02-14 05:28:10 by mc776

dehacked: revise intermission texts.

The current ones have lots of sentence fragments that are somehow austere in tone while still having lots of unnecessary words - a combination that doesn't exactly flow too well. This is an attempt to rewrite a lot of them while trying to keep all the critical elements of each.

A lot of the "it doesn't matter, who cares" / "oh. a trap. AGAIN." talk also felt like it would pull the reader out of the game, however in-character it was clearly intended. (I understand it's inspired by "where's your fat reward and ticket home" from Doom E1 but if you look at all the other id intermission texts things are much more triumphant and hopeful in tone - D2's "There must be a way to close it on the other side. What do you care if you've got to go through Hell to get to it?" is more bravado than despair.)

Replaced some things that create expectations of specific things to be found in the very next map but aren't there - the Map06-7 lift (you start on a teleporter pad), the Map11-12 platform bolts (you start just inside the door), the "massive doors" of the Military Labs (you start on the end teleporter immediately after E1M8), etc..

I was tempted to add some details about the small town at the end, but I think restraint is called for here - each reader should imagine their own nostalgic little ~~Arcadia~~ pastoral idyll.

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[ba7b3b5af2...](https://github.com/Offroaders123/NBTify/commit/ba7b3b5af2220f4b63cce797f13ef16b52cda83d)
#### Tuesday 2023-02-14 05:30:56 by Offroaders123

Exp-SNBT

Starting to work on my SNBT implementation!

This seems to be a fairly hard thing to set up so far, actually. More so because of how specific it has to be while working with strings (expected, but still new to me).

Getting help with implementation ideas and details from the Deno Minecraft library (Appears to look like a further/newer extension to NBT-TS, which is what I referred to a few times for the base NBT implementation) and the Minecraft Wiki once again!

https://github.com/janispritzkau/deno-minecraft
https://minecraft.fandom.com/wiki/NBT_format

Could work on this all night long, but I don't want to sleep the whole day away tomorrow, since it's already 3 in the morning, lol. Progress is already going great so far! Haven't tested any of my code yet, it's not even quite to that stage yet. Felt like a nice place to pause, before I get confused and tired from being up to late, hehe. Can always work on it tomorrow too.

I did some other NBT things before this part tonight, too. I was doing some more site building for this thread, this time an editor for the `NetherScale` property.

https://www.reddit.com/r/aternos/comments/v72mzz/cant_edit_leveldat_file_minecraft_bedrock/

Working on that again reminded me how helpful having this working will be, so I started working on this right after that. Having NBT opened from my library, and editable as plain text with a stringify method will make the data super editable, especially with all of the weird formats that NBTify is capable of working with now! You could edit the data as SNBT right in whatever editor supports it, and the file format options can be options in a header or context menu somewhere, like for the compression, endian, and header types. That's probably how I'm going to make it work in STE and the standalone NBT editor.

I think I probably will do both, I'm not totally sure though. Having a standalone editor for just NBT makes sense, but it's also not really a requirement, since it's simply just editing the data as plain text, rather than with a set of GUI dropdowns like other editors tend to do. I want to emphasize the ease of editing like JSON has, which works super well I think. Since that's already at the heart of STE, I think that may be a very nice home for NBT editing there. I think the only drawback is STE itself, with how it's code base currently is (getting *much* nicer already though! fully type safe :O ), and having to make things work there. I think it's probably the worthwhile option though. If I make a simply NBT-only editor, I'd probably want to add more things like STE has. So, at that point, why not just use STE?

I probably will look into making an extension for VSCode too, since that's an extra cool place to be able to edit NBT, eventually. I'd want to get syntax highlighting working for SNBT too, if it's not already out there, made by someone else. I imagine it probably is, gonna look out for it!

Still caught in the computer upgrade dilemma. Framework is really cool for Linux. Mac has great hardware nowadays. Framework is upgradable and self-repairable. Mac could takeover for both my Chromebook and iMac. Framework is behind open source. Apple isn't (essentially). I love the Linux toolchain. Mac feels similar in that regard, but it's not as 'get your hands dirty'-ey, which I feel like I have learned a lot from over on Linux. Mac is the main developer machine (I think).

So, however any of those work together, that's what my brain is stuck on. The new M2 Macs just came out a few days ago, and they look great! It might help with getting the first-gen Apple Silicon's at a lower price now too, possibly.

~~I think the best scenario would be if I could have an Apple Silicon MacBook, have macOS, APT, GNOME customizations, and~~

I think it's hard because I love both of them for different things. And they both do different things. Which one should I use on the go though? I always like having my Mac at home to depend on, to keep everything safe when I'm out and about. I don't want to bring my whole life with me on my computer. I don't need all of my pictures, coding demo ideas, music, iPhone backups, all of those kinds of things. I want those safe and sound, not carrying all of that around with me all of the time. I think that's why I like my Chromebook so much, it's pretty much my machine just for coding. If something goes wrong, welp. Did I push the commit? Then I'm good. Oop, it crashed? It's Linux, it'll restart and be good as new. I like working in the Wild West I guess, and have my home base back inside the Apple Walled Garden XD.

So, maybe that is the way to go? Linux on the go, Mac at home? That's worked really great for me for coming up on a year now (more than a year realistically, with Chrome OS too). The new base Mac mini M2 starts at $599, which is fantastic! Where do I stand for Linux on the go then? The Framework sounds to not have the best battery life for Linux, with 12th Gen Intel at least. But it also sounds like it varies for different people. Aaaah!

--ooh! Another thing. Framework is *guaranteed, and tested* to run Linux specifically, forgot about that one. I love that it's going to work, because they planned for it. With that in mind, I guess I'm just curious about the battery life, and if it will work as a daily driver for me in the tech industry down the line (working on getting closer to that, this year :D ). I don't want to eventually just get a Mac because our software at work doesn't run on Linux or something. I know everything I've used thus far works great, but I'm curious how Linux use is for work at a company, if anything will go wrong there. That's the kind of thing I'd want to avoid with by getting a Mac, as that's a very mainstream dev machine in the tech industry. But I also don't want to pigeonhole myself into needing Apple Silicon, since only Apple has that. Intel isn't as fast, but things work there moreso. If Apple stops giving my M1 software updates earlier than expected, then I probably will just have Asahi Linux to turn to (new things will probably be available by then, but yeah), or maybe OpenCore Legacy Patcher. If that does happen, why not just get a Linux laptop in the first place?

It's the battle of two evils or something haha. I'm very indecisive about this for some reason, haha. I think another smart move is to just wait it out until it's obvious which route to take.

Another wrench to throw into this is that the 11th Gen Intel Framework sounds like all got sold already (opposite to what the website says), so now that will start at around $850 I think, vs $650. So now they are both spendy options, rather than the Framework having that leg up on Apple. So, I'd be spending more for hardware that runs faster (not as fast as Apple Silicon), but it make the battery life smaller than the 11th Gen Intel version (Also, much less than Apple Silicon, which is really great, *and* you get top-of-the-line performance on top of that!).

All of these together, I think the laptop I *want* is the Framework. The laptop I *need* is the MacBook. I think that sounds right. That seems to be the one that has been staying constant in my head after first thinking it. Another one I just thought of while typing that, is what if I'm *trying to not want* the MacBook? I think because it's so great, and everyone says it's the best, and everyone should get it, that makes me not want to get it?

I've noticed this in myself before, with a lot of things. If it's the popular thing, then I try to do the other thing. If the thing I like becomes popular, it's less my own thing. So I wonder if a personality thing of trying to be unique is part of this too! Understandable in reasoning, but not logicality. Whatever's best for me is best for me.

Whichever route I take from all of this, I want to choose one to go all in on. They are both very capable options, and I'm definitely overthinking this, even if it is a touch choice. It does feel great to break this all down though. I think that's the nature of what I do, come to think of it (programming). Not only do I figure out what kind of computer I need for what I do, but I think I just learned a little bit about myself too. And I'm proud of that :)

Edit: Literally wrote this commit for an hour. Typing this edit at 4:11. WOW XD

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[264f28b3ce...](https://github.com/Offroaders123/NBTify/commit/264f28b3ceea18ba2f79cb56ae5904dfac3f5fe5)
#### Tuesday 2023-02-14 05:30:56 by Offroaders123

SNBT Indentation

Wow! Been working on this for a few hours now. Had it almost working a few times along the way, so I would restart with what I had learned to make it right to get even closer to having everything indented correctly.

This looks great! There's only a little more formatting I want to add to non-structure-based tags, so primitive-based arrays will still have a little bit of spacing, but not be multi-lined.

This is a super huge benefit to having my own object parser! I would have loved to have these kinds of checks for my JSON formatting in STE back in the day. The ability to format arrays differently, depending on what is in each array, is super awesome. I want the TypedArray tags to be single-lined, since they tend to be really long, the primitive item arrays to be singled lined (string arrays may be one I might make multi-line though), and the arrays which *hold* either ListTag, CompoundTag, or the TypedArray tags will be multi-lined. So the only one left to implement from those, which isn't already added to match those are the possible string arrays, and pretty but single lined, primitive arrays. I think I will keep the TypedArray tags flattened to not have any whitespace. I can look into seeing if it looks nice though :)

Listened to Blackwater Park for the second time tonight. I love it a ton! It was musically easy to comprehend this time around. Gonna listen to that some more this week, and also gonna go further into Mike Keneally's catalog. Listened to Incubus Science today, did not expect that! It sounded very Keneally-ish, completely different from their sound on later albums. It was sick! Glad I mentioned that right now to myself, now I'm gonna make it a plan to listen to it again tomorrow! And Blackwater Park :8

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[2fe23c07fe...](https://github.com/Offroaders123/NBTify/commit/2fe23c07fed3abcc9c05b52dccc2826b36c3c072)
#### Tuesday 2023-02-14 05:30:56 by Offroaders123

Deno-Minecraft Help + Wow, Noice!

Realized while looking at my progress from last night with new eyes, it would be a more efficient way to take a similar path with the SNBT implementation similar to how I started the library, with NBT.js. Once I have a working implementation with the reference library, which already works, I can rebuild my own code from that version, then further tweak everything until it becomes the code I wanted to make to start with.

This way works really well for making sure not to skip over things on the way though reimplementing the format with your own code. If I simply go though each part of the original code, and just rewrite it line by line, but my own way, I miss the big picture of how it all works together, as a whole. If you make little patches here and there to turn it into your own code, you can see how each of your ideas/misinterpretations will affect the result outcome of the program being able to run. So, rather than a key feature erroring out because you haven't just rewritten it yourself yet, you can see that it was actually an error in the logic of your new idea, which allows you to fix it while you know where the error happened. If you make a logic error that doesn't show up until later, you will have to try and figure out where the problem started later, and it will give you more curveballs along the way.

Glad I remembered about this technique, I need to remind myself to do this while working on STE's codebase too, rather than starting from scratch alltogether again, like I tend to want to do. I think I should try this out for Menu Drop and maybe Num Text too, as the current reworked versions are missing key features that the legacy ones have. So, now that I have the modern setup essentially nearly figured out, I should try to fit the legacy codebase in there, and modify it with the little patches like mentioned above, allowing me to ensure the features I already 'logically implemented' into the codebase can be kept inside of the modern versions too.

About the 'Wow, Noice!' part, I can't believe patching in part of Deno-Minecraft actually worked! I had to change some of the API logic with the NBT primitives, since Deno-Minecraft uses custom classes, unlike NBTify which uses direct JavaScript primitives (where possible).

It works so nice to the extent that I can read an NBT file of 'x' type, stringify it to SNBT, re-read it as a JavaScript object again, then serialize that object back down to an NBT buffer, and the resulting NBT buffer is byte-for-byte exactly the same! F-ing awesome, I love it :D

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[6c2aec6da5...](https://github.com/Offroaders123/NBTify/commit/6c2aec6da5c2c0b58b1983be8458c421a079e99a)
#### Tuesday 2023-02-14 05:30:56 by Offroaders123

NPX TSC

Super awesome!!! This is what I've been hoping to be able to do for a while now. Rather than using a 'devDependencies' install of a library you may need, turns out it's what npx is for, you can run any given library from npm with one command, and it will first look to see if you have it globally installed. And if not, it will cache a copy of it on your machine, and use that to run the command directly. I really like this, since I don't have to install TypeScript multiple times around. On my 16 GB Linuxbook, there's not as much extra room to have TypeScript installed 5 times, for all of my projects. This makes it so your commonly-used dependency toolchains only have to be saved in one place, and npm will scout those out for you and use them wherever they are! :D

Started looking into this when adding the `npm run dev` script for `tsc -w`, and I wasn't sure whether you had to use `npx` or anything special like that. So glad I stumbled across what npx is for! Ooooh!!!

This is going to make things like working on Electron apps much more performant, for the dev setup at least (maybe, just and idea :) ).

https://dev.to/azure/using-npx-and-npm-scripts-to-reduce-the-burden-of-developer-tools-57f9
https://stackoverflow.com/questions/50605219/difference-between-npx-and-npm
https://stackoverflow.com/questions/68719700/does-running-an-npm-package-with-npx-cause-devdependencies-to-get-installed

I'm also going to start using end-of-file new lines more often, as that seems to be the standard in most cases. npm adds it automatically to the `package-lock.json` after every `npm install` and I was manually removing it myself so it didn't mess up and Git changes. That's been super annoying, so I'm going to get myself to like end-of-file new lines so I don't have to worry about it anymore, haha. It seems to be the standard over in Linux/Unix land too, so I think it's smart to start getting used to it being the normal thing to expect.

---
## [toolmind/cmss13](https://github.com/toolmind/cmss13)@[b53c9f0531...](https://github.com/toolmind/cmss13/commit/b53c9f0531897023fe365961c16863d8f41983d9)
#### Tuesday 2023-02-14 06:06:35 by carlarctg

Turns all instances of 'colour' into 'color' (#2609)

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

Turns all instances of 'colour' into 'color'.

Changed a shittily-named crayon variable's name.

# Explain why it's good for the game

We use burgerclapper english and we should standardize this

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
spellcheck: Removed all instances of 'colour' and replaced them with
'color'
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [kleeio/Test_Project_JS](https://github.com/kleeio/Test_Project_JS)@[88eb8bc6ad...](https://github.com/kleeio/Test_Project_JS/commit/88eb8bc6ad1ebbf35786fc7f33e3cd80f060e08c)
#### Tuesday 2023-02-14 07:01:27 by kleeio

connecting to db with sequelize; holy fuck please stab my eyeballs; I want to cry but I haven't drank water in so long

---
## [Cykeek-Labs/kernel_realme_sdm710](https://github.com/Cykeek-Labs/kernel_realme_sdm710)@[5f88f04d28...](https://github.com/Cykeek-Labs/kernel_realme_sdm710/commit/5f88f04d28f5407eb70ea4b9fc5679b29d03b867)
#### Tuesday 2023-02-14 07:04:31 by Dave Chiluk

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
## [MrClean-1/seng401-finalproject](https://github.com/MrClean-1/seng401-finalproject)@[493d6407e7...](https://github.com/MrClean-1/seng401-finalproject/commit/493d6407e7e2cf03918b73b3925ef88f30b3f88a)
#### Tuesday 2023-02-14 07:22:48 by Clean

Fixed files, app now displays like it should

FUCK ME BRO FIREBASE IS SHIT WHY WOULD IT REWRITE THE INDEX.JS FILE JUST FOR FUNSIES WHO HURT YOU FIREBASE, WHY DO YOU PUT ME THROUGH SUCH IMMENSE PAINNNNNNN

---
## [JanKaifer/next.js](https://github.com/JanKaifer/next.js)@[268dd6e80b...](https://github.com/JanKaifer/next.js/commit/268dd6e80bb4e17096c0e75da94cf4de0b809697)
#### Tuesday 2023-02-14 08:06:50 by José Fernando Höwer Barbosa

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
## [OlayColay/UC_Love](https://github.com/OlayColay/UC_Love)@[a1696aeb26...](https://github.com/OlayColay/UC_Love/commit/a1696aeb26eaab9100d443290a71182cd099c9ce)
#### Tuesday 2023-02-14 08:38:40 by kiwinana12

RIVIERA TO THE PRINCIPAL'S OFFICE I SWEAR TO GOD

i h8 my life and i want to die :) i aint got working code

---
## [hollaaac/rubik-cube-project](https://github.com/hollaaac/rubik-cube-project)@[5fad29dad8...](https://github.com/hollaaac/rubik-cube-project/commit/5fad29dad885374178e8ea36169e97e508f42675)
#### Tuesday 2023-02-14 10:02:13 by Zytaveon

Update Cube.py

Creates a numpy 3x3x3 array. It works and creates the array but when trying to access the objects data inside of the array in does not work. Once again might be easier to switch to Java. Is it going to be fun? No. But I also have to search up everything on google anyways while making these arrays and I've seen several times that it is a bad idea to use objects inside of numpy whereas that is what Java is meant for so might be easier to switch to that instead of having a pain in the ass time the whole project. If you can somehow access the data of objects inside the numpy array then we should be set and only have to iterate over the array and give the cubelets information before being able to manipulate the cube. Once again, Java.

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[7bdf6927e3...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/7bdf6927e3636266ca3f7988c9a7a5b9dd611f83)
#### Tuesday 2023-02-14 10:30:16 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- *Zero* additional `gcc` builds (stage1+stage2+stageCompare)
  - The `gcc` derivation builds `gcc` once instead of three times.
  - The libraries that are linked into the final `pkgs.gcc` (`mpfr`,
    `mpc`, `gmp`, `isl`, `glibc`) are built by
    `stdenv.__bootPkgs.gcc` rather than by the `bootstrapFiles`.  No
    more Frankenstein compiler!
  - stageCompare runs **concurrently** with (not in series with)
    with `stdenv`'s dependees.
- Many other `stdenv` hacks eliminated.
  - `gcc` and `clang` share the same codepath for more of
    `cc-wrapper`.
  - Makes the cross and native codepaths much more similar --
    another step towards "cross by default".

Note that *all* the changes in this PR are controlled by flags; no
old codepaths need to be removed until/if we're completely certain
that this is the right way to go.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- There will be an "avalanche of simplification" when we set
  `enableGccNixDrivenBootstrap=true` and run dead code elimination.
  It's really quite a huge amount of code that goes away.
  Native-gcc has its own special codepath in so many places, while
  cross-gcc and clang work the same way (and are much simpler).
- This should allow each of the libraries that ship with `gcc`
  (`lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}`) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`.
  - Building `libstdc++-v3` in a separate derivation will eliminate
    a lot of accidental-reference-to-the-`bootstrapFiles` landmines.

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/209054
- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Build history

- First successful builds (stage1/stage2):
  - powerpc64le-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - x86_64-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - aarch64-linux at 4d5bc7dabfbe1f8758559390e373b91dda9d401e

- First successful comparisons (stageCompare):
  - at 81949cffa3272f8f9bdc8cfda8effb34be517d2f
  - [aarch64-linux][aarch64-compare-ofborg]
  - [x86\_64-linux][amd64-compare-ofborg]

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0f68cb0c6b...](https://github.com/treckstar/yolo-octo-hipster/commit/0f68cb0c6b97bc434325092fc8df5d55a6a7c15d)
#### Tuesday 2023-02-14 12:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[4c373316ad...](https://github.com/cmss13-devs/cmss13/commit/4c373316ad1e9a68e5cd7ae0e216bddcd52ee3aa)
#### Tuesday 2023-02-14 12:26:12 by NewyearnewmeUwu

Alerts admins whenever humans try to gib another human. (#2560)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Successor to #2237 that properly addresses the issues brought up by
myself and others. This sends a admin alert similar to when a pred
activates their SD that allows admins to jump to the (strictly human)
player gibbing another human/human corpse and sleep them/amessage them.
This also creates logs when someone _attempts_ to stuff someone into a
gibber. I also fixed up some of the single letter variables in the
gibber code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Insanity RP is bad, and this solution allows admins to respond in
realtime. It takes 30 seconds to gib another human as a human, without
any skill modifiers helping. It also doesn't flag the player if they're
a pred, as they're _supposed_ to be doing funny human meat stuff.
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
code: gibbing another human takes an unmodifiable 30 seconds
admin: admins are alerted when a human tries to gib another human
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [JohnFrancisMcFall/android_kernel_msm-4.14](https://github.com/JohnFrancisMcFall/android_kernel_msm-4.14)@[f9e96a0135...](https://github.com/JohnFrancisMcFall/android_kernel_msm-4.14/commit/f9e96a01352d6d7799a6d43eb6f1ed6b1aea89d4)
#### Tuesday 2023-02-14 13:14:49 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [AyanArshad02/Data-Science-Assignment](https://github.com/AyanArshad02/Data-Science-Assignment)@[acea42f707...](https://github.com/AyanArshad02/Data-Science-Assignment/commit/acea42f707041482ff19564bf999ee9ce46cda79)
#### Tuesday 2023-02-14 13:27:33 by Md Ayan Arshad

Python Task-1 Questions

Q1. Create a function which will take a list as an argument and return the product of all the numbers
after creating a flat list.
Use the below-given list as an argument for your function.
list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
Note: you must extract numeric keys and values of the dictionary also.

Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption
should be such that, for a the output should be z. For b, the output should be y. For c, the output should
be x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation
marks unchanged.
Input Sentence: I want to become a Data Scientist.
Encrypt the above input sentence using the program you just created.
Note: Convert the given input sentence into lowercase before encrypting. The final output should be
lowercase.

---
## [Thomas-009/pokemon-showdown](https://github.com/Thomas-009/pokemon-showdown)@[5cbb317a4c...](https://github.com/Thomas-009/pokemon-showdown/commit/5cbb317a4c62a59351010c006be62b37e2a029e2)
#### Tuesday 2023-02-14 14:06:24 by sexy90gxebattlefactoryplayer

Gen 8 Battle Factory: Remove Darmanitan-Galar's Choice Band set (#9354)

* Gen 8 Battle Factory: Remove Band set from Ubers Darmanitan-Galar 

Credentials: https://cdn.discordapp.com/attachments/1042959218208157696/1067534457160089731/image.png (i am "lost wind's elegy")

Darm-G's firepower is just fine with scarf; there aren't many (if any?) relevant 1hkos or 2hkos you miss out on compared to band. The only one I can think of is missing out on the OHKO vs Sp. Def Necrozma Dusk Mane, and nobody's leaving their NDM in anyway + you probably have like 12 other things to deal with it.

Without scarf, however, you miss out on really good source of offensive checking and revenge killing potential. Scarf outspeeds huge threats like non scarf Yveltal, Eternatus, Calyrex-Shadow, etc. 

What sparks had to say about band darm in proper SS Ubers:
sparks — Today at 1:53 PM
not really but with band building needs to be more focused cos the speed over the 90s and etern etc is insane with scarf

sparks — Today at 1:54 PM
while with band you're very much focused on "how to take out ndm and capitalize while not being weak to ho"

As a secondary factor, it would make Ubers in BF a lot better. Currently you have to not only win the coinflip of what move Darm clicks but also the coinflip of what item it is. Both of these are more or less up to random chance.

* Update data/mods/gen8/factory-sets.json

---------

Co-authored-by: Kris Johnson <11083252+KrisXV@users.noreply.github.com>

---
## [ilammy/themis](https://github.com/ilammy/themis)@[2c2af3f542...](https://github.com/ilammy/themis/commit/2c2af3f5421685bbebfeee17c081d51fc8001ee6)
#### Tuesday 2023-02-14 14:17:51 by Oleksii Lozovskyi

CI: Remove Carthage distactions

Carthage has this retarded tendency to build every Xcode project it
sees when building dependencies. So when we do "carthage bootstrap"
during example builds, it downloads dependencies (Themis repo),
then proceeds to build the dependencies -- but instead of building
only Themis.xcodeproj in the root, Carthage decides that after that
it gotta build every other Xcode project there as well, why not.
Eventually it times out and dies.

This very frustrating, but Carthage people think this is fine,
multilanguage monorepos do not exist, and you should not put example
Xcode projects along with the source code. One repo = One library.

Anyway. This seems to help to avoid timeouts and prevent Carthage
from going on adventure. Sadly, builds still take fucking forever
while Carthage fetches the repo, then fetches OpenSSL binaries,
then do it again, then build Themis, then build example, then
repeat that 5 more times for other examples. But at least they
should not hang for 10 minutes and then die 🤞

Similar hack is applied in Bitrise builds, IIRC.

---
## [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated)@[b83625045f...](https://github.com/software-mansion/react-native-reanimated/commit/b83625045f314e498fe32adc34b43ce20a77f946)
#### Tuesday 2023-02-14 14:54:21 by Angelika Serwa

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
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[0d19f3c85d...](https://github.com/Bjarl/Shiptest/commit/0d19f3c85d39f58ee663935eb75b72fd502752af)
#### Tuesday 2023-02-14 15:05:50 by Bjarl

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
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Floofies/tgstation](https://github.com/Floofies/tgstation)@[fedf2f3a26...](https://github.com/Floofies/tgstation/commit/fedf2f3a26869848f5fc8f41381d1aff944ed9f6)
#### Tuesday 2023-02-14 15:40:00 by Sol N

more span macro changes in brain traumas and disease files (#73273)

## About The Pull Request

i was fucking around with brain traumas on a downstream and noticed they
had similar issues to quirks so i decided to continue work from #73116


![Code_Klx14O288V](https://user-images.githubusercontent.com/116288367/217046732-765ffe27-73c9-416a-833e-e0d9e2aa7a86.png)
(search in VSC for span class = 'notice')
its going to be a bit of a thing to get all of these but this is a
decent chunk i think

there was only one annoying/tough file.
imaginary_friend.dm had class = 'game say' and class = 'emote' both of
which after some testing did not seem like they did anything. ill try to
keep that in mind in other files if i continue to do this but i either
omitted them because they didnt have any formatting or, in the case of
emote, turned it into name, which i think is what you'd want those
messages to look like.

there were also a few small spelling errors that i fixed

## Why It's Good For The Game

more consistent and stops people from copying brain trauma formatting
wrong

## Changelog

they should all work the same

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [newstools/2023-metro](https://github.com/newstools/2023-metro)@[6bf8a84231...](https://github.com/newstools/2023-metro/commit/6bf8a842314110ca1b0a0f390580ff0d531e5891)
#### Tuesday 2023-02-14 15:51:33 by Billy Einkamerer

Created Text For URL [metro.co.uk/2023/02/14/im-26-and-have-never-had-a-boyfriend-thank-god-for-unrequited-love-18145167/]

---
## [yameen-bhat/yameen-bhat](https://github.com/yameen-bhat/yameen-bhat)@[4670eb5809...](https://github.com/yameen-bhat/yameen-bhat/commit/4670eb5809bef77b2ac2751601426b3c8e4a4f37)
#### Tuesday 2023-02-14 16:12:42 by yameen bhat

Something about stars
Remember lazing around on a summer night on the terrace of the house and gazing into the sky, looking at all the twinkling stars. It seemed like they were all trying to tell a story. And each star flashed its own light and bright hue that looked splendid from where we were lying down.

The beauty of the moon added to the dark sky and provided a beautiful background to the whole picture thus created by nature.

Nature has many a wonders in store. We can never see the sun with our eyes. The brightness and the heat it emits can be enough to scare us into never even glancing at the star. Nature’s wonders cannot be described in just a few words. The tremendous bounty nature offers in its lap are hardly explored by man.

The beauty of the rain forests, the wonders of the deciduous and oak trees, sprawling flora and amazing fauna in the corners of the world, the vast ice spread over different regions of the north and the south poles, the magnificent waterfalls, rivers, seas and oceans all add up to the beauty and glamour of mother earth.

We cannot think of a day without sighting the sun first thing in the morning. It’s only the sunshine that causes a day to make inroads and with this sunshine, living beings prosper and make their lives fruitful and happy.

We are blessed with the ability to see things and come out of the dark because we have sunshine during the day. Sunshine allows us to see things, plants prepare food and we are able to survive on this food thus obtained from a process of photosynthesis and the long food chains existing in nature.

---
## [git/git](https://github.com/git/git)@[f44e6a2105...](https://github.com/git/git/commit/f44e6a21057b0d8aae7c36f10537353330813f62)
#### Tuesday 2023-02-14 18:00:10 by Jeff King

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
## [iav/bees](https://github.com/iav/bees)@[14ce81c081...](https://github.com/iav/bees/commit/14ce81c081e2aa3104e78bb74a54ecccd4624d0d)
#### Tuesday 2023-02-14 18:40:06 by Zygo Blaxell

fs: get rid of silly base class that causes build failures now

The base class thing was an ugly way to get around the lack of C99
compound literals in C++, and also to make the bare ioctls usable with
the derived classes.

Today, both clang and gcc have C99 compound literals, so there's no need
to do crazy things with memset.  We never used the derived classes for
ioctls, and for this specific ioctl it would have been a very, very bad
idea, so there's no need to support that either.  We do need to jump
through hoops for ostream& operator<<() but we had to do those anyway
as there are other members in the derived type.

So we can simply drop the base class, and build the args object on the
stack in `do_ioctl`.  This also removes the need to verify initialization.

There's no bug here since the `info` member of the base class was
never used in place by the derived class, but new compilers reject the
flexible array member in the base class because the derived class makes
`info` be not at the end of the struct any more:

	error: flexible array member btrfs_ioctl_same_args::info not at end of struct crucible::BtrfsExtentSame

Fixes: https://github.com/Zygo/bees/issues/232
Signed-off-by: Zygo Blaxell <bees@furryterror.org>

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[728a0f1b91...](https://github.com/lessthnthree/tgstation/commit/728a0f1b9147197bb81f22d946f67e9d08719d5a)
#### Tuesday 2023-02-14 18:48:21 by Jacquerel

Grand Ritual: Alternate Wizard objective (Wizard Events II) (#72918)

Adds an alternate greentext objective for Wizards known as the "Grand
Ritual". This was initially the gimmick of a different wizard-related
antagonist downstream. I didn't get permission to port it, so I'm
attaching it to regular Wizards instead.

Wizards will spawn in with a new Grand Ritual button next to their
antagonist info button. Pressing it will pinpoint them towards their
next Ritual Location (a randomly chosen region of the space station).
Once within that location, pressing it will summon a magic circle and
obliterate any dense objects which are in the way. This also puts the
ability on a two minute cooldown.
Clicking on the magic circle with an empty hand will begin a three-stage
invocation to gather magical power. You can interrupt this invocation at
any time and will resume from the last stage you completed (if you
finished two stages you only need to do one more).
Once you complete a ritual, a random event will be triggered based on
how many rituals you have performed so far. These tend to be ones which
annoy the crew in some manner, and Wizard Events are included in the
list. Additionally, something weird will usually happen to the room you
are in.
Then you are assigned a new location and can toddle off to do it again.

Once you have done this three times, you will be picked up by the
station's sensors every time you start a subsequent ritual and should
expect annoyed company to come investigate.
Once you have done this six times, you can finally spend all of that
accumulated power on the seventh Grand Finale ritual. Completing this
grants you victory at the end of the round and will have a larger,
flashier effect which you can pick from a list of options, think of it
like a wizard equivalent of a Traitor Final Objective or Heretic
Ascension.
After that you can still keep doing rituals if you want to pester the
crew further by summoning more random events, you've already "won" at
this point so now it's your job to make them want to go home.

I think it'd be more fun to just find out what the Finale ritual can do
by seeing it happen but maintainers will probably want a list of its
precise capabilities, so here it is:

Currently completing a ritual also has a chance to create Heretic
Reality Tears (of both varieties, available for Heretics to eat and
visible to crew) as a kind of cross-antagonist interaction which seemed
to make sense to me but if this seems thematically or mechanically
inappropriate it's easy to strip out.

---
## [dkostic/aws-lc](https://github.com/dkostic/aws-lc)@[372a5e263a...](https://github.com/dkostic/aws-lc/commit/372a5e263aaae42d0eea8695bbe670eb4d11bbd5)
#### Tuesday 2023-02-14 19:53:20 by David Benjamin

Maintain a frame pointer in aesni-gcm-x86_64.pl and add SEH unwind codes

Some profiling systems cannot unwind with CFI and benefit from having a
frame pointer. Since this code doesn't have enough register pressure to
actually need to use rbp as a general register, this change tweaks
things so that a frame pointer is preserved.

As this would invalidate the SEH handler, just replace it with proper
unwind codes, which are more profiler-friendly and supportable by our
unwind tests. Some notes on this:

- We don't currently support the automatic calling convention conversion
  with unwind codes, but this file already puts all arguments in
  registers, so I just renamed the arguments and put the last two
  arguments in RDI and RSI. Those I stashed into the parameter stack
  area because it's free storage.

- It is tedious to write the same directives in both CFI and SEH. We
  really could do with an abstraction. Although since most of our
  functions need a Windows variation anyway.

- I restored the original file's use of PUSH to save the registers.
  This matches what Clang likes to output anyway, and push is probably
  smaller than the corresponding move with offset. (And it reduces how
  much thinking about offsets I need to do.)

- Although it's an extra instruction, I restored the original file's
  separate fixed stack allocation and alloca for the sake of clarity.

- The epilog is constrained by Windows being extremely picky about
  epilogs. (Windows doesn't annotate epilogs and instead simulates
  forward.) I think other options are possible, but using LEA with an
  offset to realign the stack for the POPs both matches the examples in
  Windows and what Clang seems to like to output. The original file used
  MOV with offset, but it seems to be related to the funny SEH handler.

- The offsets in SEH directives may be surprising to someone used to CFI
  directives or a SysV RBP frame pointer. All three use slightly
  different baselines:

  CFI's canonical frame address (CFA) is RSP just before a CALL (so
  before the saved RIP in stack order). It is 16-byte aligned by ABI.

  A SysV RBP frame pointer is 16 bytes after that, after a saved RIP and
  saved RBP. It is also 16-byte aligned.

  Windows' baseline is the top of the fixed stack allocation, so
  potentially some bytes after that (all pushreg and allocstack
  directives). This too is required to be 16-byte aligned.

  Windows, however, doesn't require the frame register actually contain
  the fixed stack allocation. You can specify an offset from the value
  in the register to the actual top. But all the offsets in savereg,
  etc., directives use this baseline.

Performance difference is within measurement noise.

This does not create a stack frame for internal functions so
frame-pointer unwinding may miss a function or two, but the broad
attribution will be correct.

Change originally by Clemens Fruhwirth. Then reworked from Adam
Langley's https://boringssl-review.googlesource.com/c/boringssl/+/55945
by me to work on Windows and fix up some issues with the RBP setup.

Bug: b/33072965, 259
Change-Id: I52302635a8ad3d9272404feac125e2a4a4a5d14c
Reviewed-on: https://boringssl-review.googlesource.com/c/boringssl/+/56128
Reviewed-by: Adam Langley <agl@google.com>
Commit-Queue: David Benjamin <davidben@google.com>
(cherry picked from commit 0d5b6086143d19f86cc5d01b8944a1c13f99be24)

---
## [isinyaaa/dotfiles](https://github.com/isinyaaa/dotfiles)@[6629c299e5...](https://github.com/isinyaaa/dotfiles/commit/6629c299e5d40b5946f6ef48137b46020e042eb4)
#### Tuesday 2023-02-14 21:13:29 by Isabella Basso

fuck treesitter

This is a shitty software project. I just want my standard colors to be
applied where they should, and the complexity of this thing + SEEMINGLY
RANDOM AND BIZARRE coloring are just not worth the trouble.

After spending some hours **debugging diff highlighting** I think I've
had enough of this insanity.

Signed-off-by: Isabella Basso <isabbasso@riseup.net>

---
## [Vukkyy/Quarky](https://github.com/Vukkyy/Quarky)@[b821c4cc24...](https://github.com/Vukkyy/Quarky/commit/b821c4cc240ec19e7e9f67a1abe8fc0727a063dd)
#### Tuesday 2023-02-14 21:21:42 by Vukky

add proper specialattributes support (doesn't work for notifications because fuck you that's why)

---
## [OU-Xmen/PAUL](https://github.com/OU-Xmen/PAUL)@[d3bf0888d1...](https://github.com/OU-Xmen/PAUL/commit/d3bf0888d11c0ba7b11e09625a65ee4552cfca41)
#### Tuesday 2023-02-14 21:42:43 by Eli Sepulveda

Checkers - first commit!

I'd like to take a second to thank the sponsor of this code, SPITE.
If you're anything like me, you like coming up with your own ideas. Nothing is more satisfying than building your own project from scratch. But what happens when someone wants to take that idea, beat you to the punch, AND take credit for it? It's hard to know what the next step to take is. That's where our friend SPITE comes in. With its top-of-the-line mood shifting and rage-fueled ambition, you'll never worry about potential rivals again! To sweeten the deal, the first 50 people to use my link get 1 free sprint to start off! Get SPITE today, and leave those talkers in the dust.

We're looking pretty good for checkers! So far, legal moves (non-jumps) are fully functional, with king detection.
TODO:
legal jumps
win condition

Known bugs:
None

---
## [remuluson2/tgstation](https://github.com/remuluson2/tgstation)@[5e80257423...](https://github.com/remuluson2/tgstation/commit/5e802574231c9c6fe835c40b55f2c8aa9f1c68b4)
#### Tuesday 2023-02-14 21:54:56 by Jeremiah

Refactors crew records (#72725)

## About The Pull Request
I have attempted or otherwise started this project at least 4 times. I
am sick of it being on my calendar. The code needs it. I need it.

- This makes crew records a proper datum rather than assigning
properties record.fields.
- General, medical, and security records are merged.
- Did some slight refactoring here and there for things that looked
obvious.
- Wanted states are now defined (and you can suspect someone through
sechud)
- pAI (unrelated but annoying) had some poorly named exported types that
i made more specific
- Job icons are moved back to the JS side (I wanted to get icons for
initial rank without passing trim)

<details>
<summary>previews</summary>

Editable fields & security console

![CM6d74brnC](https://user-images.githubusercontent.com/42397676/213950290-af6cfd76-eb8b-48e9-b792-925949311d9a.gif)

Medical records

![bFJErsvOaN](https://user-images.githubusercontent.com/42397676/214132534-59af1f8c-9920-4b51-8b27-297103649962.gif)

Look and feel of the more current version

![cxGruQsJpP](https://user-images.githubusercontent.com/42397676/214132611-0134eef0-e74c-4fad-9cde-328ff7c06165.gif)

</details>

## Why It's Good For The Game
TGUI'd some of the worst UIs in the game.
Creating new records is made much simpler. 
Manifest_inject is made readable.
Probably bug fixes

## Changelog

:cl:
refactor: Crew records have been refactored.
refactor: Medical records -> TGUI
refactor: Security records -> TGUI
refactor: Warrants console -> TGUI
qol: Players are now alerted when their fines are paid off.
qol: Cleaned up sec hud examination text.
qol: Adding and deleting crimes is easier.
qol: Writing crimes in the console sets players to arrest.
qol: You can now mark someone as a suspect through sec hud.
/:cl:

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [tra-ins/trains](https://github.com/tra-ins/trains)@[9bfa1eab0d...](https://github.com/tra-ins/trains/commit/9bfa1eab0d6f5f8423d258e4cc071900fa16e06c)
#### Tuesday 2023-02-14 23:05:33 by tra-ins

i forgot one bit of the 13th ft. suffering and valentines idk i hate everything

i hate beta club!!! everyone in my hr thinks i have a secret admirer now bc i didnt know the names on the card were just the BETA LADY. i hate that woman respectfully (but not respectfully if you read this). please help i was so excited because i thought it was funny that someone got me one :(

---

