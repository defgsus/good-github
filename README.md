## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-25](docs/good-messages/2023/2023-05-25.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,057,135 were push events containing 3,436,419 commit messages that amount to 254,988,178 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 77 messages:


## [git-for-windows/git](https://github.com/git-for-windows/git)@[93deb77118...](https://github.com/git-for-windows/git/commit/93deb771185ec687bc1dcc9cdccf7500bd584f1d)
#### Thursday 2023-05-25 00:12:49 by Johannes Schindelin

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
## [stevan/ELO](https://github.com/stevan/ELO)@[8e8695ab2e...](https://github.com/stevan/ELO/commit/8e8695ab2e8d00e1afd67f10bd223d0802ca9002)
#### Thursday 2023-05-25 00:16:43 by Stevan Little

this kinda stuff annoys me, silly to make it a single commit, but who cares, its my repo

---
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[0cff53fc09...](https://github.com/ritorizo/Shiptest/commit/0cff53fc09c34d989d2bc34b1699bd856af2cb92)
#### Thursday 2023-05-25 00:24:22 by meemofcourse

Reworks the Twinkleshine-Class (#1825)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![2023 05 13-23 20
45](https://github.com/shiptest-ss13/Shiptest/assets/75212565/de6f3a47-7be8-4800-ae73-9fc386e4bf01)

![twinklerework5](https://github.com/shiptest-ss13/Shiptest/assets/75212565/f1808576-70e3-4b56-b977-5b5e7d665fdd)





The Twinkleshine is a CyberSun-made Syndicate display of force, staffed
by every branch of the Syndicate. Despite the silly name, the presence
of one in a sector implies it to be of importance to the Syndicate, and
enemies within sight can only pray that the Twinkleshine crew are
incompetent enough to shoot themselves with their own weaponry (or blow
themselves up with the supermatter on-board).

It is staffed by:

- 1 Captain
- 1 Lieutenant (previously the Operative - serves as a warden/hos)
- 2 Medics
- 2 Engineers (previously the Mechanics)
- 5 Operatives (previously the Troopers)
- 1 Bartender
- 1 Miner
- 2 Deck Assistants

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Few days ago, an admin spawned a Twinkleshine, and I got to captain it.
The Twinkleshine is old. It sucks. This, hopefully, fixes that.

Originally, this was going to be minor fixes, but ended up becoming an
attempt at reworking the ship to a more modern state - the hull has been
redone and is mostly symmetrical, the old spacepod was replaced with a
Dark Gygax, the supermatter shouldn't be activated upon spawning the
ship, there's more turf decals and a bigger lot-of-things, added a
bartender and a miner, people can actually tell who they are and what
they do, and there is now a box moth. Rejoice.

Also, this is the first time I've ever mapped a ship. What better way to
begin with a giant battleship?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
tweak: Reworks the Twinkleshine
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: meemofcourse <75212565+meemofcourse@users.noreply.github.com>

---
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[d4b5a598e2...](https://github.com/ritorizo/Shiptest/commit/d4b5a598e2346bb3f69d533ed05a94d539e8b830)
#### Thursday 2023-05-25 00:24:22 by Bjarl

Sand Survivor Rework (#1940)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Reworks how Sand Survivors spawn their loot. Instead of an outfit datum,
they now create a corpse similiarly to how legions do it, this allows
their contents to have some variety, more ease of expansion, and
generally Improves the file.

How I could write better code in a day than White Sands functioned with
for iunno how long is byond me


https://user-images.githubusercontent.com/94164348/236322169-c303f934-634f-447d-950f-78a55346d152.mp4

![image](https://user-images.githubusercontent.com/94164348/236376947-6e484ed0-f136-4787-9e74-fad0f5c21d11.png)

![image](https://user-images.githubusercontent.com/94164348/236377018-e2dc1661-fe78-4c6a-8be2-8bf24e5d00b2.png)


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Consistency + Just kinda cool
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Sand Planet hermits now have randomized inventories. And Hair.
Sometimes.
add: Sand Planet hermits can now drop different races
add: legions will now drop a variety of species
balance: drop rates for legions have been changed in a few spots.
fix: hivelord.dm no longer sears my eyes out.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [SMERTONOS/tgstation](https://github.com/SMERTONOS/tgstation)@[66cb695343...](https://github.com/SMERTONOS/tgstation/commit/66cb695343721087437e651d07268e284e25763d)
#### Thursday 2023-05-25 00:50:03 by carlarctg

IV drips' default transfer rate is no longer zero. (#74724)

## About The Pull Request

Set default IV transfer rate to maximum (5) instead of 0.
## Why It's Good For The Game

> Set default IV transfer rate to maximum (5) instead of 0.

When you hook someone onto an IV drip, you naturally expect that to be
the end of the process - you hooked someone to a drip, and now you can
go about your day. Them needing to fiddle with buttons is bad for
several reasons:

- It is unintuitive.
IV drips don't look like machines. Their sprite doesn't reflect the fact
that you need to fiddle with the settings before they can work the same
way any other machine or computer might. And to be honest, they
shouldn't.
- It is separate from how every other server currently has it.
Yes, yes, I know that argument is very flawed and full of holes. But
what I'm trying to say with it is, effectively speaking, an extension of
the above point. In other servers, you drag-click someone to an IV drip
and there we go, it's functional. In TG, it just-so-happens to not be
functional due to what is almost definitely a recent oversight, which
very much can, has, and will lead to unnecessary frustration.
- There is no practical reason for it to be set at 0.
Imagine if chem dispensers started at +0 units and needed to be set to
+5 to continue. Or if bottles had a transfer rate of 0u. Or if guns
started with their safeties on. Even if it made sense, it would just be
frustrating and needless, and wouldn't improve the game in any
significant manner enough to offset frustration. We're here for fun, not
perfect balance or realism/verisimilitude after all.
- It's an oversight.
It was changed in #71217. Before that, it was always set to the maximum,
5u. However, presumably due to confusion (Variables that can be adjusted
ingame usually are set to zero/the minimum possible) it ended up being
changed to this.

Apparently an argument can be made that this is fine because fumbling to
get medical aid done is a part of the game. I disagree heavily - blood
bags are already stored in the cold room, something only 2/5 of the
roles in medbay even have access to, with the paramedic, virologist,
chemist all being unable to reach it. This is already enough 'fumbling'
that's necessary. If someone moved the blood bags outside the cold room
next to the IV drips, then all the better - it's a reward for medbay
being prepared.

However I wouldn't mind if someone asked me to make it so the default
transfer rate is, well, something below maximum. It's common practice in
a lot of parts of SS13 to have things set in an unoptimized state so
players can go around improving them, such as air alarms, cryogenics,
etc. Just as long as it's not literally unusable otherwise, as the
'minimum basic setup' should just be slapping on a blood bag!
## Changelog
Dunno what to put here TBH. Can't tell if it's qol, fix, balance, etc.

:cl:
qol: Set default IV transfer rate to maximum (5) instead of 0.
/:cl:

---
## [SMERTONOS/tgstation](https://github.com/SMERTONOS/tgstation)@[205ea3dad7...](https://github.com/SMERTONOS/tgstation/commit/205ea3dad711fa541f93adc7f2053250d3e3c777)
#### Thursday 2023-05-25 00:50:03 by Bloop

Fixes spoon overlay not updating every time (#74687)

## About The Pull Request

After bludgeoning myself one too many times with a spoon, here we are.

The spoon overlay wasn't updating to reflect that soup had been
consumed, which led to trying to eat it again and then pain.

Why do spoons hurt so much?

## Why It's Good For The Game

Less spoon related injuries.

## Changelog

:cl:
fix: spoon overlays will now update when you eat from them to reflect
that food = gone. it really is gone, you can stop beating yourself with
the spoon. oh god please stop--
/:cl:

---
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[bfb3967c90...](https://github.com/Jolly-66/dragon-station/commit/bfb3967c908682e21202312d8b30ec17ad65e549)
#### Thursday 2023-05-25 00:51:26 by SkyratBot

[MIRROR] Adds proper armor for security plasmamen. [MDB IGNORE] (#21268)

* Adds proper armor for security plasmamen. (#75156)

## About The Pull Request
It's kinda strange that security plasmamen has no proper armor and you
can just bully them with bottlesmashes. Literally.
Also suits had no wound armor for some reason, which considering that
mold dies without hand kinda silly too.
And helmets just had no armor besides 1 melee armor.
## Why It's Good For The Game
Plasmamen security won't die that easilly. I mean, still easy to kill
them, but not that much.
## Changelog
:cl:
balance: Security Plasmamen now have Security armor. No bullying them
with bottlesmashes anymore.
/:cl:

* Adds proper armor for security plasmamen.

---------

Co-authored-by: Helg2 <93882977+Helg2@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [Mu-L/haproxy](https://github.com/Mu-L/haproxy)@[9577a152b5...](https://github.com/Mu-L/haproxy/commit/9577a152b5ef8ed89d57c826b6b4b5fe50f70c0c)
#### Thursday 2023-05-25 01:04:42 by Willy Tarreau

BUILD: makefile: do not erase build options for some build options

One painfully annoying thing with the build options change detection
is that they get rebuild for about everything except when the build
target is exactly "reg-tests". But in practice every time reg tests
are run we end up having to experience a full rebuild because the
reg-tests script runs "make version" which is sufficient to refresh
the file.

There are two issues here. The first one is that we ought to skip all
targets that do not make use of the build options. This includes all
the tools such as "flags" for example, or utility targets like "tags",
"help" or "version". The second issue is that with most of these extra
targets we do not set the TARGET variable, and that one is used when
creating the build_opts file, so let's preserve the file when TARGET
is not set.

Now it's possible to re-run a make after a make reg-tests without having
to rebuild the whole project.

---
## [Nanu308/cmss13](https://github.com/Nanu308/cmss13)@[2baaba2746...](https://github.com/Nanu308/cmss13/commit/2baaba27468b20016d2095edfbdba26658935ddc)
#### Thursday 2023-05-25 01:14:21 by Hopekz

Adds medic clothing racks to WO (#3313)

God damn this is so frustrating every time I play WO as a medic


![dreamseeker_ZXt55sth9R](https://github.com/cmss13-devs/cmss13/assets/24533979/252773e1-fec0-4bec-a1a5-0ccb63547781)


![dreamseeker_UiolotzaIV](https://github.com/cmss13-devs/cmss13/assets/24533979/a241ee86-f2ea-490f-91c7-7b1a90e9734f)


:cl: Hopek
add: Medics finally get medic clothing racks on WO
/:cl:

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[c20b961685...](https://github.com/Latentish/Shiptest/commit/c20b961685c78760ab807c95a2e79fe72ee4d507)
#### Thursday 2023-05-25 01:16:06 by thgvr

Elementizes and Greyscales blood decals/overlays (#1882)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR converts our blood decals to elements, and adds greyscale
capability to blood, tied to species DNA.
Ports:
https://github.com/BeeStation/BeeStation-Hornet/pull/3111
https://github.com/BeeStation/BeeStation-Hornet/pull/3046
https://github.com/tgstation/tgstation/pull/61610
https://github.com/tgstation/tgstation/pull/59873
https://github.com/tgstation/tgstation/pull/59315
https://github.com/tgstation/tgstation/pull/53109

Some others, I don't quite remember. Mostly related fixes for those PRs.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Decals as a component is a cause of some lag, apparently. This should
alleviate some if it's even noticeable.

Species having a framework for unique, greyscale blood colors can add a
lot for our lore and visual feel.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Elzu now bleed, but do not have Liquid Electricity reagent as
blood. (will be changed in the future)
add: IPCs now "bleed" by leaking coolant
add: Sarathi now have teal-colored blood.
add: Blood will now dry over time
add: New bloody footprint sprites from bay
refactor: Refactors a lot of blood code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: thgvr <81882910+thgvr@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[835952ccf4...](https://github.com/Jolly-66/tgstation/commit/835952ccf42af58db7238a572d7df6a9b8b2afd7)
#### Thursday 2023-05-25 01:20:04 by MrMelbert

Drunk slurring scales based on how drunk you are (#75459)

## About The Pull Request

The strength of the slurring effect drunkness applies on you now scales
based on how drunk you are.

Being "a little" drunk still changes your saymod, and makes you
occasionally slur your words...


![image](https://github.com/tgstation/tgstation/assets/51863163/1b21b359-a1f9-428a-8e10-d2028ac59728)

But being "a lot" drunk kicks it up to 11


![image](https://github.com/tgstation/tgstation/assets/51863163/9d593c80-75ff-4d02-8e7c-e48c738154bb)

Additionally, drunk slurring was separated into "generic slurring" and
"drunk slurring", the former which does not scale but less closely
resembles drunkness. Generic slurring is used in places such as
concussions, so this is an added bonus.

As a result of the split, I had to update mind restoration. Now it heals
all types of slurring, which does include cult slurs.

## Why It's Good For The Game

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

## Changelog

:cl: Melbert
add: When you are drunk, the strength of your slurring now varies based
on how drunk you are. Being "a little drunk" only rarely slurs your
words, being average drunk is the same as the old effect, while being
very drunk now slurs your words even more.
add: Some non-alcohol sources of slurring, such as concussions, now give
"generic slurring" rather than "drunk slurring", which less resemble
being drunk (ie, no burping).
add: Mind restoration now heals ALL slurring, rather than only drunk
slurring (which includes cult / heretic slurring).
/:cl:

---
## [QuacksQ/Skyrat-tg](https://github.com/QuacksQ/Skyrat-tg)@[c2d75696c8...](https://github.com/QuacksQ/Skyrat-tg/commit/c2d75696c8d0012027bf97a15b2c0e332416b497)
#### Thursday 2023-05-25 01:23:20 by SkyratBot

[MIRROR] Nerfs the firing speed of Syndicate/Russian mobs [MDB IGNORE] (#21047)

* Nerfs the firing speed of Syndicate/Russian mobs (#75247)

## About The Pull Request

Nerfs their firing speed from once every 0.2 seconds to once every 2.5
seconds

## Why It's Good For The Game

1. The mob that is NOT a 'burst' type mob, is firing every 0.2 seconds.
Kinda defeats the point of having them as two separate mobs, so this
aims to fix that.
2. Russian mobs. Turns out that letting them fire their strong-ass gun
every 0.2 seconds was kinda not a good idea. I had assumed making them a
Syndicate mob would be safe, and it technically is, it's just that
Syndicate mob is fucked itself.

## Changelog

:cl:
balance: Default Syndicate and Russian gunners now fire every 2.5
seconds instead of every 0.2
/:cl:

* Nerfs the firing speed of Syndicate/Russian mobs

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [knative-automation/client-pkg](https://github.com/knative-automation/client-pkg)@[24ef637a01...](https://github.com/knative-automation/client-pkg/commit/24ef637a0184c204b57736699fa744622f85250b)
#### Thursday 2023-05-25 01:48:31 by Knative Automation

upgrade to latest dependencies

bumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping k8s.io/code-generator 6523e22...eec869e:%0A  > eec869e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 824419b Bump runc go module v1.1.4 -> v1.1.6%0A  > ba94e65 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 6276bf2 Update golang.org/x/net to v0.7.0%0A  > 73b9c40 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 882af80 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 6063700 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > b615940 Update golang.org/x/net 1e63c2f%0A  > 11d5c4c update k8s.io/utils to fix util tracing panic%0A  > 081720d Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > d44fa8c dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 300cdcf Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > e0ef4aa Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 557ce1f Merge pull request # 113126 from alexzielenski/remove-unwanted-replace%0A  > f86120d remove errant replace%0A  > d6a8b70 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f77ba6d dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 3bbe215 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > e80bbc4 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d403dc0 update kube-openapi%0A  > 790e4bc update fsnotify to v1.6.0%0A  > 27bd7d9 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 4731e5c Bump golang.org/x/text to v0.3.8%0A  > a8a213c Merge pull request # 112875 from pohly/update-yaml%0A  > 5f5bab9 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 983d5d0 Merge pull request # 112819 from thockin/no-make-generators%0A  > c35177b Format calls to codegens%0A  > 83929d0 Codegens: Do not auto-set boilerplate path%0A  > 1d82d12 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > c3414a0 clients: clarify a misleading comment%0A  > 998e449 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > e4543b2 Update to latest k8s.io/utils to pick up changes%0A  > 8e999f2 Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 524127d update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 4ca0baf Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b54a056 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 350c30a updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5f3f945 e2e: bump ginkgo to v2.2.0%0A  > 2e5cca7 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > c3fdc3c Merge pull request # 112349 from pohly/klog-update%0A  > e4b7976 client-go: support waiting for SharedInformerFactory shutdown%0A  > 135f69b build: update to klog v2.80.1%0A  > f60067d Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7c81c99 Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 8468f16 Remove in-tree credential plugins (again)%0A  > 9b98ed3 add symmetric difference in sets%0A  > 34125ff Merge pull request # 112199 from pohly/klog-update%0A  > a055687 dependencies: update to klog v2.80.0%0A  > 16cba21 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > e051ad0 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 3a31bb1 Merge pull request # 111934 from deads2k/apply-gen%0A  > 4d73156 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 1382941 make applyconfiguration-gen skip generation for types that have generated clients and lack objectmeta%0A  > 03a75ea Bump prometheus/client_golang to v1.13.0%0A  > 17196da update the apply generator to use the same package the the client generator expects%0A  > a4e23d1 Merge pull request # 111566 from inosato/remove-ioutil-from-code-generator%0A  > a6a370c make applyconfiguration-gen handle pointers to slices%0A  > 087714e Merge pull request # 109884 from qzoscar/patch-1%0A  > fc00858 Remove ioutil from code-generator%0A  > ed79ca3 make applyconfiguration-gen work for resources without objectmeta%0A  > fea40fb Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 3612509 fix a broken link%0A  > 78677a3 update the applyconfiguration-gen flag external-applyconfigurations to work%0A  > ad6af70 Revert "Remove gcp and azure auth plugins"%0A  > 7ba56cb applyconfiguration-gen handling of types that have a non-embedded use of TypeMeta%0A  > 97fa351 Merge pull request # 111696 from liggitt/go119mod%0A  > d71f529 add metav1.OwnerReference to the default external configurations to ease generation%0A  > 2b9093f Update go.mod to go1.19%0Abumping knative.dev/eventing 034bec9...6a11c5f:%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping knative.dev/pkg dfad48e...ec20442:%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping golang.org/x/tools b3b5c13...d0863f0:%0A  > d0863f0 go.mod: update golang.org/x dependencies%0A  > 545ca87 gopls/internal/regtest/marker: require go/packages%0A  > 1ace7db go,gopls: remove license from package doc comments%0A  > ebad375 gopls/internal/lsp/protocol: prevent license rendering in godoc%0A  > 10a39ef gopls/internal/lsp/regtest: address additional comments on marker.go%0A  > 69920f2 gopls/internal/regtest/marker: add missing tests for hover%0A  > 24a13c6 gopls/internal/regtest: fill out features of the new marker tests%0A  > 2b149ce gopls/internal/regtest: add a regtest-based version of the marker tests%0A  > edddc5f go/packages: don't discard errors loading export data%0A  > a762c82 go/ssa: add MultiConvert instruction%0A  > f124b50 cmd/stringer: streamline test subprocesses%0A  > 6b6857a gopls: fix typos in comments and doc%0A  > 8111118 go/analysis/internal/facts: fix cycle in importMap.%0A  > dd1c468 gopls/internal/lsp/source: simplify extracting object hover doc%0A  > 66f8f71 gopls/internal/lsp/source: use syntax alone in FormatVarType%0A  > 30f191f internal/imports: update stdlib index for Go 1.20%0A  > 4e98188 internal/imports: use go/packages instead of cmd/api to compute symbols%0A  > 4e8ff89 internal/imports: update stdlib index for 1.20%0A  > 6bd0d00 gopls/internal/lsp: go to definition from linkname directive%0A  > 0cfddb3 gopls/internal/lsp: enable clear builtin completion test%0A  > 41adf8d gopls/internal/lsp/tests: remove StripSubscripts%0A  > 86fdadc gopls/internal/lsp/safetoken: delete safetoken.Range%0A  > c276ee5 internal/robustio: fix signature of getFileID on plan9%0A  > e170d45 gopls/internal/lsp: add clear builtin%0A  > 2ea4b81 go/ast/inspector: skip ranges that do not contain a node type%0A  > 407bbed go/analysis: improve error message on duplicate fixes%0A  > bd5dfbb all: fix some comments%0A  > 072fca5 gopls/protocol: use the current definition of the lsp%0A  > aa633e7 tools/gopls: provide markdown for completion and signature help%0A  > 684a1c0 go/analysis/internal/analysisflags: use os.Executable for program path%0A  > bd5e595 gopls/internal/lsp/cache: add missing mutex%0A  > 2683128 gopls/internal/lsp: differentiate govulncheck/vulncheck imports diags%0A  > d1e92d6 gopls/internal/lsp/mod: reorder vulncheck quick fixes%0A  > 87d00e6 gopls/internal/lsp: separate some requests from source.Identifier%0A  > ae242ec gopls: fix windows file corruption%0A  > 6f65213 gopls/internal/lsp/protocol: Mapper.NodeMappedRange%0A  > e260368 gopls/semantic: report type parameters in the type of a receiver%0A  > b62cbb6 internal/lockedfile: fix build constraints on solaris%0A  > 1aa7e72 gopls/internal/lsp/source: avoid qualifiedObjectsAtProtocolPos%0A  > 5ed33df gopls/internal/lsp/source: rename: prep for incrementality%0A  > e0659d1 gopls/internal/lsp/source: simplify legacy 'references' func%0A  > 1edcfe7 gopls/internal/regtest/diagnostics: require cgo for TestGoListErrors%0A  > f052158 gopls/internal/lsp/protocol: move TestBytesOffset%0A  > d093a13 gopls/internal/lsp/protocol: LocationTextDocumentPositionParams%0A  > bcb677e gopls/internal/regtest: make RegexpSearch return a Location%0A  > 60782e9 gopls/internal/lsp/source: eliminate a couple uses of posToMappedRange%0A  > 031e6e6 gopls/internal/lsp/source: eliminate ResolveImportPath%0A  > f2cd9ef gopls/internal/lsp/source: reduce usage of TypecheckWorkspace%0A  > f10e7d5 gopls/internal/lsp/cache: remove package dependence on packages.Config%0A  > 8270757 gopls/internal/lsp/source: switch call hierarchy to references v2%0A  > 37c69d8 gopls/internal/lsp/source: references: support exported methods%0A  > f3c36a2 gopls/internal/lsp/cmd/test: delete marker-based tests of gopls cmd%0A  > c224aae gopls/internal/lsp/cmd/test: new integration test for gopls command%0A  > deeb64b gopls/internal/lsp/source/xrefs: allow Lookup of a set%0A  > f269f53 gopls/internal/lsp: remove Server.processModifications%0A  > fcd57eb gopls: allow 'any' and 'comparable' in completion results%0A  > aae3642 gopls/internal/lsp/source: referencesV2: support unexported methods%0A  > b5d65e0 tools/gopls: register semantic tokens statically%0A  > 51abc5b gopls/internal/lsp/source: stub: don't panic when encountering 'error'%0A  > ce28f40 gopls/internal/regtest: add a test demonstrating confusion following an%0A  > c4c6aa6 internal/lsp/cache: don't panic in Snapshot on a shutdown view%0A  > 1faecd3 tools/internal/diff: fix off-by-one error in computing diffs%0A  > a7f033a gopls/internal/lsp: consolidate the FileHandle API%0A  > 271e621 internal/lockedfile/internal/filelock: fix aix build tag%0A  > ff9bea5 gopls/internal/lsp/cmd/test: signpost future cleanups%0A  > 7d4ba2f gopls/release: remove unused functionality from release script%0A  > 46b6958 gopls/internal/lsp/source: delete source_test%0A  > bcc7794 go/analysis/passes/directive: add directive analyzer%0A  > 33d416e gopls/internal/lsp: add missing comments on 3x tests.Test impls%0A  > afea272 gopls/internal/lsp/source: make implementations2 work on embedded fields%0A  > bb7c440 gopls/internal/lsp/filecache: use file locking, not rename%0A  > 561a9be gopls/internal/lsp/filecache: actually delete files%0A  > 9682b0d gopls/internal/lsp/source: delete IsInterface%0A  > 7a7b699 go/analysis/passes/loopclosure: avoid panic in new parallel subtest check when t.Run has single argument%0A  > 3e6f71b gopls/internal/regtest: use AfterChange in more places%0A  > 9ff31a5 x/tools/go/analysis/passes/printf: revert URL in error message%0A  > 2fa6ca1 gopls/internal/lsp/source/impls: a new "implementations" index%0A  > 957bec5 gopls/protocol: new versions of generated LSP files%0A  > f0e2d5c internal/gcimporter: discard position info for unneeded lines%0A  > 5bedd86 cmd/digraph: use ReadString rather than bufio.Scanner%0A  > f6ea009 gopls/internal/lsp: remove the experimentalWatchedFileDelay setting%0A  > f46e418 gopls/internal/lsp/source: include ITVs in global references%0A  > f3e53e5 internal/jsonrpc2_v2: fix typos%0A  > d958e85 internal/gcimporter: use two-level file index%0A  > 8aba49b internal/gcimporter: preserve column and line in shallow iexport%0A  > d7fc4e7 gopls: new LSP stub generator%0A  > 5c176b1 internal/robustio: skip os.Link test on android%0A  > d34a055 go/ssa: sanity check the types of phi nodes%0A  > 6f095b4 go/callgraph/vta: add flows for receiver function types%0A  > 8e94967 cmd/fiximports: do not assume go list -json unmarshals into build.Package%0A  > e035d0c go/ssa: fix phi node type in slice to array conversion%0A  > 03eac81 go/expect: remove testdata go.mod to go.fake.mod%0A  > 1e819a3 gopls/internal/regtest: follow-ups to review comments from earlier CLs%0A  > 9ba8bb1 gopls/internal/regtest: clean up workspace symbol helpers%0A  > 91b6070 gopls/internal/regtest: eliminate DiagnosticAtRegexp%0A  > bd48b9a gopls/internal/regtest: eliminate DiagnosticsAtRegexpWithMessage%0A  > 5d65394 gopls/internal/regtest: eliminate DiagnosticAt%0A  > 27dfeb2 gopls/internal/regtest: replace NoDiagnostics with NoMatchingDiagnostics%0A  > 87092c8 gopls/internal/lsp/fake: use protocol types for the fake editor%0A  > 672a036 gopls/internal/regtest: simplify OnceMet expressions with an env helper%0A  > ab7b5b2 gopls/internal/regtest: eliminate GoSumDiagnostic%0A  > 331a1c6 gopls/internal/regtest: add a simpler API for diagnostic expectations%0A  > c9b82f2 gopls/internal/regtest: eliminate EmptyDiagnostics%0A  > e81af27 gopls: update golang.org/x/vuln@6ad3e3d%0A  > d19e3d1 internal/regtest/bench: fix BenchmarkRename and add more benchmark tests for gopls%0A  > 2be1a9a gopls/internal/regtest: rename EmptyOrNoDiagnostics to NoDiagnostics%0A  > 7ec05ac gopls/internal/regtest: eliminate NoDiagnostics%0A  > e956495 gopls/internal/regtest: eliminate DiagnosticsFor%0A  > 8087911 gopls: remove the experimentalWorkspaceModule mode%0A  > 5b300bd gopls/internal/lsp/cache: clean up view workspace information%0A  > 97d5de5 gopls/internal/cache: don't mark initialized after cancellation%0A  > 58691bc gopls/internal/lsp/glob: add an LSP compliant glob implementation%0A  > a3c22fc cmd/cover: delete package%0A  > 98dcb0e cmd/cover: remove replace directive%0A  > 7765567 gopls/internal/lsp/source: minor clarifications%0A  > a7f7db3 cmd/cover: carve out deprecated command into its own module%0A  > f9a10c0 Revert "cmd/cover: carve out deprecated command into its own module"%0A  > e345d46 internal/gcimporter: fix export of invalid methods%0A  > 4305a22 gopls/internal/lsp/cache: don't cache files if mtime is too recent%0A  > 227ee72 internal/regtest/misc: fail eagerly in TestRenameFileFromEditor%0A  > 43158af cmd/cover: carve out deprecated command into its own module%0A  > b798934 gopls/internal/lsp/protocol: cleanups and docs for Mapper%0A  > a24944e gopls/internal/lsp/protocol: rename s/ColumnMapper/Mapper/%0A  > 55935f4 gopls/internal/span: simplify Span%0A  > 40a1c97 gopls/internal/lsp/lsppos: delete Mapper%0A  > 6a3bc37 gopls/internal/lsp/protocol: reimplement ColumnMapper line logic%0A  > 6e9a35d go/callgraph/cha: refactor callee construction%0A  > fef5b76 go/callgraph: fix slicing in callgraph_test.go%0A  > 2be9d05 gopls/internal/lsp/source/xrefs: a new reference index%0A  > 0362cea gopls/internal/lsp/lsppos: delete TokenMapper%0A  > 67baca6 go/callgraph/vta: optimize scc computation%0A  > 2eb6138 gopls/internal/lsp/filecache: use TempDir if UserCacheDir fails us%0A  > 36bd3db gopls/internal/lsp/protocol: move MappedRange%0A  > 16b3bf8 gopls/internal/lsp/cache: assume Go 1.16+%0A  > 3856a5d internal/robustio: add Plan9 support to FileID%0A  > 09cbc42 gopls/internal/lsp/fake: fix EOF bug in applyEdits%0A  > 4ded35d gopls/internal/lsp/cache: use distinct types for mod and work parse keys%0A  > 107f43f gopls/completion: avoid duplicating text in test func completions%0A  > e225fd4 gopls/internal/lsp/mod: fix nil panic in go.mod hover%0A  > 057ed3c gopls/internal/lsp/filecache: use os.Chtimes%0A  > 1fe76af gopls/internal/lsp/source: MappedRange cleanup%0A  > 02bea03 gopls/internal/lsp/protocol: simplify ColumnMapper%0A  > a4455fe go/callgraph: adds benchmarks comparing algorithms%0A  > 7db99dd go.mod: update golang.org/x dependencies%0A  > 1e0dff2 gopls/internal/regtest: avoid race in TestSwitchFromGOPATHToModuleMode%0A  > 0441b43 gopls/internal/lsp/cache: use specific mutexes for module data%0A  > 33071fb internal/robustio: move robustio%0A  > b01e7a4 gopls/internal/regtest/watch: don't run TestSwitchFromGOPATHToModuleMode%0A  > e417ea3 gopls: remove dead analysis code%0A  > 1a08d01 gopls/internal/lsp: update replace directives in go.mod for package renaming%0A  > eac36cb gopls/internal/regtest: port experimental workspace tests to go.work%0A  > 224a61b gopls/internal/lsp/source: delete Snapshot.WriteEnv method%0A  > 81e741e gopls/internal/lsp/safetoken: funnel more calls through this package%0A  > 8367fb2 gopls/internal/regtest: await go.work changes in TestAddAndRemoveGoWork%0A  > 3b16059 gopls/internal/regtest: make BufferText strict%0A  > 0e1d013 gopls/internal/lsp/cache: recreate Views when their root changes%0A  > 2f31dd4 go/ssa,go/analysis/passes/nilness: refine when type param constants are nil%0A  > ae4ff82 gopls/internal/lsp/source: delete GetTypedFile%0A  > fe6b300 gopls/internal/lsp/source: eliminate Snapshot.Package{,s}ForFile%0A  > 26fc609 gopls/internal/lsp/cache: eliminate snapshot.containingPackages%0A  > 85e6ad7 gopls/internal/lsp/safetoken: fix bug in Offset at EOF%0A  > ef1ec5d gopls/internal/lsp/safetoken: fix error message%0A  > 44395ff gopls/internal/lsp/source: avoid unnecessary transitive rdeps%0A  > 6546d82 Revert "gopls/internal/regtest: harmless CL used for benchmark test"%0A  > 3be0647 gopls/symbols: call source.Document symbols only for Go files%0A  > d462c83 gopls/internal/lsp: Replace input text when completing a definition%0A  > 7efffe1 gopls/internal/regtest: harmless CL used for benchmark test%0A  > 1627e95 gopls/internal/lsp: more comment tweaks post-//line support%0A  > 21f6100 internal/lsp/debug: fix broken template%0A  > 6ad27d0 gopls/internal/robustio: FileID, a portable file identifier%0A  > 6df6eee internal/diff/lcs: optimize inner loop%0A  > 57b1265 go/gcexportdata: drop support for go1.6 export data%0A  > 099260e gopls/internal/lsp: followups to dropping line directives%0A  > 61e2d3f gopls/internal/lsp/cache: a new analysis driver%0A  > eb70795 gopls: ignore //line directives%0A  > b4dfc36 go/ssa: deref core type in emitLoad%0A  > 1270fd7 gopls/internal/lsp: announce selectionRangeProvider capability%0A  > 9bc5dce gopls/internal/lsp/cache: simplify DiagnosePackage%0A  > df35cd8 x/tools: drop support for Go toolchains older than go1.16%0A  > db9d10f go/gcexportdata: preallocate buffer to read into when size is known%0A  > 0d2045b gopls/internal/lsp: document analysis-related functions%0A  > b2b9dc3 gopls/internal/lsp/cache: reduce type-checking in renameImports%0A  > 3cb82d5 go/ssa/interp: fix conversion of slice to named array%0A  > 5899b6a gopls: upgrade dependencies following release%0A  > 763a030 gopls/internal/lsp/cache: delete Snapshot.KnownPackages%0A  > cc0e696 gopls/internal/hooks: panic if diff consistency check fails%0A  > 9ec8553 gopls/internal/lsp/source: emit interface stub methods at top level%0A  > 444c8f6 gopls/internal/lsp/cache: only invalidate parsed files if they changed%0A  > 601ca6c gopls/internal/lsp/source: use correct token.File%0A  > 95c9dce internal/lsp/mod: fix run_govulncheck codelens name%0A  > d72a64a gopls/internal/lsp: add selection range request%0A  > 18f76ec gopls/internal/lsp: split ActivePackages%0A  > 84299a0 gopls/internal/lsp/cache: simplify ad-hoc package warning logic%0A  > a3eef25 gopls/internal/lsp/cache: record parse keys when they're created%0A  > 3da7f1e gopls/hover: remove header tags from hover markdown%0A  > a310bcb gopls/internal/lsp/source: eliminate getStubFile%0A  > 3cba5a8 internal/gcimporter: port CL 424876 from std importer%0A  > b0fdb78 gopls/internal/lsp/mod: add Reset vulncheck result codelens%0A  > 88ceb24 gopls/internal/lsp: perform analysis unconditionally%0A  > 3f74d91 gopls/internal/lsp/cache: invalidate govulncheck results older than 1hr%0A  > 6b8674f gopls/internal/lsp/source: avoid typechecking in findRune%0A  > d7dfffd gopls/internal/lsp: eliminate more unnecessary typechecking%0A  > f3fb218 gopls/internal/lsp/fake: use robustio.RemoveAll in (*Workdir).RemoveFile%0A  > 96ff41d gopls/internal/vulncheck: add TODO for the vulncheck diagnostics%0A  > 0f6c6f1 gopls: delete obsolete govulncheck code and stop gopls vulncheck -summary%0A  > c5343a6 gopls/internal/lsp/regtest: fix TestRunGovulncheckError2%0A  > cb701f7 gopls/internal/lsp: avoid type-checking when computing hyperlinks%0A  > d0f184d gopls/internal/lsp/source: avoid unnecessary calls to GetTypedFile%0A  > 1e5efed gopls/internal/lsp/fake: simply use polling to simulate file watching%0A  > 838a165 gopls/internal/lsp/fake: eliminate the unnecessary fake.FileEvent%0A  > 09fb680 gopls/internal/lsp/fake: eliminate the unnecessary ChangeFilesOnDisk API%0A  > 09ae2d5 gopls/internal/lsp/source: KnownPackagePaths: avoid loading%0A  > 1dcc423 gopls/internal/lsp/cache: split metadata and loading in PackagesForFile%0A  > 6b50501 gopls/release: fix the release script when go.work is not used%0A  > aee3994 gopls/internal/lsp/fake: in (*Workdir).RenameFile, fall back to read + write%0A  > fe60148 go.mod: update golang.org/x dependencies%0A  > c9ea9a7 gopls/internal/regtest: add a test for the case when the renaming package's path contains "internal" as a segment%0A  > bf5db81 gopls/internal/lsp/cache: improve ad-hoc warning for nested modules%0A  > aa9f4b2 go/analysis: document that facts are gob encoded in one gulp%0A  > bdcd082 internal/gcimporter: skip tests earlier when 'go build' is not available%0A  > 2ad6325 gopls/internal/lsp/cache: expand ImportPath!=PackagePath comment%0A  > 52c7b88 gopls/internal/robustio: only define ERROR_SHARING_VIOLATION on Windows%0A  > 4f69bf3 gopls/internal/lsp/cache: narrow reloadOrphanedFiles to open files%0A  > 6002d6e gopls/internal/regtest/misc: test Implementations + vendor%0A  > f540ee6 internal/gcimporter: load cached export data for packages individually%0A  > d444fa3 gopls/internal/lsp/cache: simplify canonical URI cache%0A  > 25fdb81 gopls/internal/regtest/misc: skip vendor test on go1.13%0A  > e0b516b gopls/internal/lsp/cache: invalidate metadata after vendor change%0A  > 31d5843 gopls/internal/lsp/cache: fix re-entrant session locking%0A  > 8c78b30 gopls/internal/vulncheck: always use pkg.go.dev/vuln for urls%0A  > 47a8246 gopls/internal/regtest/misc: skip TestRunGovulncheckError2%0A  > d54e12b gopls/internal/lsp: avoid I/O in URI comparison operations%0A  > 0379b73 internal/gcimporter: fix TestImportStdLib%0A  > e79e423 gopls/internal/vulncheck: handle package errors%0A  > c5ce806 gopls/internal/lsp/mod: disable the diagnostics on stdlib vulns%0A  > 78c1861 gopls/internal/vulncheck: clarify the log message%0A  > 1a0053c gopls: move reset go.mod diagnostic codelens to module statement%0A  > 9b8d87b gopls/internal/regtest: fix TestRunGovulncheckStd%0A  > 81b6bef gopls/internal/lsp: add run vulncheck fix for stdlib vulns%0A  > fe83ddb gopls/internal/lsp: move options off of the cache%0A  > 88ee30b gopls/internal/lsp/source: enable run_govulncheck codelens in exp mode%0A  > 0a6aa90 gopls/internal/lsp/command: rename run_vulncheck_exp to run_govulncheck%0A  > bedad5a gopls/internal/lsp/mod: add hover for stdlib vulnerabilities%0A  > 7a1b570 gopls/internal/vulncheck: check vulnerabilities in standard library%0A  > 9a54670 gopls/internal/lsp/mod: add "Run govulncheck" codeaction%0A  > f1b76ae gopls/internal/lsp: add an option to overwrite previous diagnostics%0A  > e8a70a5 gopls/internal/lsp: remove access to mutable session state from the view%0A  > ff22fab gopls/internal/lsp/cache: eliminate obsolete invalidation step%0A  > 3881046 gopls: add a go:generate rule for doc generation%0A  > 4c3cb1e internal/gocommand: add GoVersionString%0A  > e29d1ed gopls: add diagnostic for standard library%0A  > f718365 gopls/internal/lsp: include all vulns info to fetch_vulncheck_result%0A  > 9519368 gopls/internal/lsp/mod: add the vulncheck diagnostics mode%0A  > 7d9f451 gopls/internal/govulncheck: add in-memory cache for vulndb%0A  > 1ccccf8 go/ssa: deprecate coreType and _NormalTerms%0A  > 4b7d1b3 gopls: add diagnostics for both vulns used and not used%0A  > 50ccef5 internal/regtest/bench: add benchmark tests for gopls%0A  > d39685a gopls/internal/lsp/source: Package clarifications%0A  > 7cfde84 gopls/internal/vulncheck: add import info based vuln scanning%0A  > 2b56641 internal/gcimporter: adjust the number of expected packages in TestStdlib%0A  > 50df761 gopls: skip vulnerabilities that are probably fixed in hover%0A  > 7cda55e gopls/internal/lsp/cache: wire in mod vulnerability analysis%0A  > 5c35617 gopls: add quick fixes for all vulnerabilities%0A  > fb7be64 gopls/internal/lsp/command: return the vulncheck progress token%0A  > 060c049 go/packages: fix doc typo%0A  > 6eafd96 gopls: fix formatting for vulncheck results in hover%0A  > b797704 go/analysis/passes/loopclosure: recursively check last statements in statements like if, switch, and for%0A  > 3b9d20c internal/gcimporter: in TestStdlib, only check x/tools packages if we expect to have their source%0A  > 2ad3c33 go/packages: change workaround for issue 28749 to not require NeedFiles%0A  > 57f56ab gopls/internal/lsp/source: avoid panic(nil)%0A  > 41c70c9 internal/lsp/source: avoid using go/types.Implements with Typ[Invalid]%0A  > db5eae2 analysis: correct go/analysis/passes/findcall path in docs%0A  > b978661 cmd/godoc: streamline test subprocesses%0A  > 932ec22 internal/testenv: add a Command function that replaces exec.Command%0A  > 19fb30d gopls/internal/lsp/cache: fix data race in Symbols%0A  > 4ce4f93 gopls/internal/lsp: add gopls.fetch_vulncheck_result%0A  > 8ba9a37 gopls/internal/lsp/mod: highlight when there is no fix for vuln%0A  > 128f61d gopls/internal/lsp/mod: add related info%0A  > fc03993 internal/lsp/mod: adjust vulncheck diagnostics suppression logic%0A  > c099dff gopls/internal/vulncheck: log progress%0A  > 36a5c6a go/ssa: build generic function bodies%0A  > 85bf7a8 gopls/internal/lsp/source: eliminate Metadata interface%0A  > 2592a85 gopls/internal/lsp: simplify KnownPackages%0A  > c7ed4b3 gopls/internal/lsp/cache: clean up tracking of GO111MODULE%0A  > 23056f6 internal/lsp/cache: clean up getOrLoadIDsForURI%0A  > 5a4eba5 internal/lsp/cache: remove support for invalid metadata%0A  > 32a17c0 gopls/internal/lsp/mod: fix unaffecting vuln diagnostics msgs%0A  > dea100b internal/testenv: skip tests that need export data for std if 'go tool compile' does not exist%0A  > ba373ee playground/socket: eliminate an arbitrary timeout in TestLimiter%0A  > 3d085f3 gopls/internal/lsp/lsprpc: eliminate arbitrary timeout in TestEnvForwarding%0A  > 434d569 gopls/internal/lsp/regtest: improve documentation%0A  > ce26db4 go/analysis: add Pass.TypeErrors field%0A  > b0ad6b2 gopls/internal/regtest/misc: fix use of the AfterChange API%0A  > 89856a4 gopls/semantic: semantic tokens for type parameters%0A  > 6e8da3f internal/pkgbits: port small optimization from compiler to tools%0A  > 06fb723 internal/gcimporter: port memory reuse optimizations from Go tree%0A  > fc702c5 internal/gcimporter: fix performance regression for unified IR%0A  > 1cb4c17 gopls/internal/regtest: make AfterChange do the awaiting%0A  > 0c71b56 gopls/internal/lsp: fix diagnostic suppression when folders change%0A  > e3b3c01 go/pointer: break TestInput into subtests and update skips%0A  > 13648cd gopls/internal/lsp/cache: use Package.FileSet where possible%0A  > 8f32411 cmd/stringer: replace ioutil with os%0A  > 3c3713e gopls/internal/lsp/cache: use typed strings (PackagePath et al) throughout%0A  > 004d118 gopls/internal/lsp/mod: simplify ModVulnerabilityDiagnostics%0A  > 4a8413c gopls/internal/lsp/mod: deleted unused function pkgVersion%0A  > bc08991 gopls: sync golang.org/x/vuln@3af8368ee4fe%0A  > d66e9b4 internal/typesinternal: update go/types error codes for 1.20%0A  > 6f99366 gopls/internal/lsp/cache: don't pass snapshot.fset to go/packages%0A  > d56532a cmd/compilebench: make it work without installed .a's%0A  > 502c634 go.mod: update golang.org/x dependencies%0A  > bd04e32 internal/jsonrpc2_v2: eliminate a potential Accept/Dial race in TestIdleTimeout%0A  > d41a43b internal/jsonrpc2_v2: fix a potential deadlock when (*Conn).Close is invoked during Bind%0A  > 3057465 gopls/doc: Add plugin for Lapce to gopls documentation%0A  > ba92ae1 internal/persistent: avoid incorrect map validation due to multiple keys%0A  > 9474ca3 gopls/doc: clarify `go work use`%0A  > 003fde1 internal/gcimporter: use nondeprecated go/packages mode bits%0A  > 5050657 gopls/fake: add semantic token modifiers to fake editor%0A  > 88a3548 gopls/coverage: repair coverage.go%0A  > 8e0240a internal/regtest/workspace: permanently skip TestDeleteModule_Interdependent%0A  > fe725d9 gopls/internal/regtest: simplify awaiting diagnostics from a change%0A  > 3c8152e internal/gcimporter: optimize dependency lookup%0A  > 39c2fd8 internal/lsp/cache: simplify importsState modfile hashing logic%0A  > ec044b1 gopls: update dependencies following the v0.10.0 release%0A  > 2b29c66 internal/gcimporter: API for shallow export data%0A  > affa603 internal/gcimporter: moved from go/internal/gcimporter%0A  > a77a1fb gopls/internal/lsp/mod: fix vulncheck hover message%0A  > 4ada35e gopls/internal/lsp: handle modVulncheckSource in diagnosticSource.String%0A  > e5f03c1 gopls/doc: clean up README and add a release policy%0A  > d5e9e35 go/analysis/passes/loopclosure: enable analysis of parallel subtests%0A  > 039b24b internal/jsonrpc2_v2: initiate shutdown when the Writer breaks%0A  > 32e1cb7 gopls/internal/lsp: clarify control around diagnostics%0A  > feeb0ba gopls/internal/lsp/cmd: fix deadlock when opening a file%0A  > 6e9dc86 gopls/internal/lsp/source/completion: fix panic in completion on *error%0A  > 73fcd88 Revert "internal/jsonrpc2_v2: initiate shutdown when the Writer breaks"%0A  > 70a130e gopls/api-diff: simplify the api-diff implementation%0A  > 3e8da47 internal/jsonrpc2_v2: initiate shutdown when the Writer breaks%0A  > 3566f69 gopls/internal/lsp/source: minor space optimizations%0A  > 7cdb0e7 internal/jsonrpc2_v2: rename Serve to NewServer and eliminate its error return%0A  > 28e9e50 internal/jsonrpc2_v2: eliminate error return from Bind%0A  > eabc3a0 internal/jsonrpc2_v2: eliminate isClosingErr%0A  > 4885f7c internal/jsonrpc2_v2: eliminate a temporary connection leak in (*Server).run%0A  > 739f55d internal/jsonrpc2_v2: rework Connection concurrency%0A  > e172e97 go/types/typeutil: break recursion through anonymous interfaces%0A  > f1c8f7f internal/lsp/source: optimize filter regular expression%0A  > e074ef8 gopls/internal: don't show a warning if the Go version is undetected%0A  > 7fba77c gopls/internal/lsp/source: remove deprecated settings from EnableAllExperiments%0A  > 42cb7be gopls/internal/lsp: improve the Go version deprecation message%0A  > 2af106e gopls/internal/hooks: fixes to diff disaster logic%0A  > e4bb343 go/internal/gcimporter: update to anticipate missing targets and .as%0A  > 875c31f go/internal/gcimporter: add test of export/import on std%0A  > 541f4c5 cmd/bundle: quote command-line arguments in output%0A  > de675d5 tools/gopls: argument in function bodies marked as parameter by semantic tokens%0A  > 3e1371f gopls/internal: start on LSP stub generator in Go.%0A  > 121f889 gopls/internal/lsp/mod: merge vuln diagnostics to one, and add a hover%0A  > d6511e5 internal/facts: share go/analysis/internal/facts with gopls%0A  > 2e0ca3a go/internal/gcimporter: fix bug in struct iexport%0A  > 1928cea go/ssa: emit field and index lvals on demand%0A  > 8166dca go/analysis/passes/asmdecl: define register-ABI result registers for RISCV64%0A  > 2dcdbd4 go/internal/gcimporter: port CL 431495 to tools, add tests%0A  > d476af7 go/ssa: add slice to array conversion%0A  > d212f7d gopls/internal/regtest/workspace: fix bugs in test%0A  > 051f03f gopls/internal/lsp/cache: remove unnecessary params%0A  > 21f6127 gopls/internal/lsp/cache: add PkgPath->PackageID index to Metadata%0A  > 06041c9 gopls/doc: update manual documentation of the newDiff setting%0A  > f112c43 go.mod: update golang.org/x dependencies%0A  > 207f456 go/internal/gcimporter: bump version number in skew check%0A  > 65196ca gopls/README.md: fix wording around supported Go versions%0A  > 6128030 gopls/internal: support renaming packages with int. test variants%0A  > 649df2e go.mod: mark as requiring -compat 1.16%0A  > 91311ab gopls/internal/lsp/cache: better import path hygiene%0A  > 9eda97b go/analysis: enable a test that applies after go list behavior change%0A  > b50d7ba gopls: minor cleanup of standalone package support%0A  > 502b93c gopls/internal/lsp: tolerate missing end position in RelatedInformation%0A  > d67c3ad internal/imports: repair warnings from default analyzers%0A  > bc2e3ae internal/jsonrpc2_v2: add Func convenience wrappers for the Binder and Preempter interfaces%0A  > a9b653b cmd/compilebench: use -a instead of -i to ensure dependencies are built%0A  > 4818d9e Revert "gopls/internal/lsp/cache: disable strict analysis while we fix panics"%0A  > b2efd4d internal/jsonrpc2_v2: eliminate most arbitrary timeouts in tests%0A  > 371ef16 internal/jsonrpc2_v2: rework concurrency in idleListener%0A  > 5935531 internal/jsonrpc2_v2: remove “Box” suffix from channel field names%0A  > fd32990 internal/jsonrpc2_v2: error out in-flight client calls when the reader breaks%0A  > 0e222f5 internal/jsonrpc2_v2: close the underlying connection if Wait is called instead of Close%0A  > bc4e384 gopls/internal/lsp/cache: fix crash in analysis%0A  > b93a56f refactor/satisfy: fix visiting functions in the unsafe package%0A  > 9b5e55b gopls/internal/lsp/cache: disable strict analysis while we fix panics%0A  > 9ffaf69 gopls/internal/lsp/cache: minor analysis cleanups%0A  > ffb862b gopls/internal/lsp/cache: remove stray print statement%0A  > f87c1ed internal/fastwalk: improve Darwin performance by ~3x%0A  > b253314 gopls/internal/lsp/cache: add support for loading standalone main files%0A  > 3beecff gopls/internal/span: some cleanups%0A  > d375238 gopls: dedup upgrade code actions for vulncheck%0A  > b20ae4b README: format install command%0A  > 19a5504 gopls/internal/lsp: use the golang.org/x/vuln/exp/govulncheck%0A  > ab79327 cmd/ssadump: disable run mode with runtime package%0A  > 29429f5 gopls/internal/lsp/source: sort protocol edits%0A  > 49b340b go/analysis: update tests for different go list error behavior%0A  > cd0288f internal/lsp/cache: invalidate analysis results on packages.Load%0A  > 906c733 gopls/internal/lsp/source: find references in test packages%0A  > 2a41b25 internal/robustio: fix log.Fatal calls that should be log.Fatalf%0A  > 150b5f8 internal/imports: read entire API dir in mkstdlib.go%0A  > 19cfa79 internal/lsp/source: switch the default diff algorithm to "checked"%0A  > fa6bd3b gopls: include informational vulnerability diagnostics%0A  > 89b4335 gopls/internal/lsp: merge notifications about deprecated settings%0A  > f90d8ad all: fix a few function names on comments%0A  > 350f1e2 gopls/internal/lsp/fake: retry ephemeral errors when renaming on windows%0A  > 8b1d1ec gopls/internal/lsp/cache: suppress panics during analysis%0A  > 20c1ee7 gopls/internal/lsp: warn about Go versions that are too old%0A  > 709f108 gopls/internal/lsp/cache: suppress crashes in fact_purity analyzer%0A  > a410e98 internal/diff: ToUnified may fail%0A  > 26a95e6 gopls/internal/span: move internal/span into gopls%0A  > f2c4579 internal/diff: avoid unnecessary allocations%0A  > 60ddcca internal/diff: Apply: validate inputs%0A  > 02bef08 go/packages/packagestest: break dependency on gopls' span package%0A  > 778f945 go/analysis: break dependency on span package%0A  > c682555 gopls/internal/regtest/misc: delete testdata%0A  > 1552…

---
## [mamedev/mame](https://github.com/mamedev/mame)@[2222a0f098...](https://github.com/mamedev/mame/commit/2222a0f098c2f32ec6090627598a90e596006596)
#### Thursday 2023-05-25 02:11:13 by David 'Foxhack' Silva

gba.xml: Added 21 prototypes. (#11260)

New working software list items (gba.xml)
-------------------------------
AGB Aging Cartridge (World, version 1.0) [SmellyGhost, Forest of Illusion]
AGB Aging Cartridge (World, version 9.0) [Suicune41, Forest of Illusion]
Aero the Acro-Bat - Rascal Rival Revenge (Europe, prototype earlier) [LongwoodGeek, Forest of Illusion]
Chokkan Hitofude Advance (Japan, prototype) [xprism, Forest of Illusion]
Commandos 2 (USA, prototype) [DillyDylan, Forest of Illusion]
Dark Eden (prototype) [Ian Dunlop, Forest of Illusion]
Demon's Crest (prototype) [Ian Dunlop, Forest of Illusion]
Manic Miner (Europe, 20030307) [March42, Forest of Illusion]
Mario Kart XXL (demo, 20040417) [Forest of Illusion]
R3D-Demo V1 (demo) [Forest of Illusion]
Racing Gears Advance (USA, prototype, 20030922) [XBrav, Forest of Illusion]
Sea Boy (prototype) [Ian Dunlop, Forest of Illusion]
Star Wars Trilogy - Apprentice of the Force (USA, prototype) [Rezrospect, Forest of Illusion]
The Holy Bible - World English Bible (USA, prototype) [Gonz, Forest of Illusion]
Ultimate Muscle - The Kinnikuman Legacy - The Path of the Superhero (USA, prototype, 20030429) [Zach Lambert, Forest of Illusion]
Uridium Advance (Europe, prototype, 20030307) [March42, Forest of Illusion]

New software list items marked not working (gba.xml)
------------------------------------------
The King of Fighters EX2 - Howling Blood (USA, prototype, 20030403) [March42, Forest of Illusion]
Quake (demo) [Randy Linden, Forest of Illusion]
Paradroid (Europe, prototype, 20030320) [March42, Forest of Illusion]
Uridium Advance (Europe, prototype, 20020911) [March42, Forest of Illusion]
Uridium Advance and Paradroid 2 in 1 (Europe, prototype, 20030430) [March42, Forest of Illusion]

---
## [knative-automation/eventing-rabbitmq](https://github.com/knative-automation/eventing-rabbitmq)@[7d8cca439b...](https://github.com/knative-automation/eventing-rabbitmq/commit/7d8cca439b7b29e23ef02ec010b100475db26c39)
#### Thursday 2023-05-25 02:18:44 by Knative Automation

upgrade to latest dependencies

bumping k8s.io/component-base 1543ebf...97d19e0:%0A  > 97d19e0 Update dependencies to v0.26.5 tag%0A  > db961f2 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 5b011ca Bump runc go module v1.1.4 -> v1.1.6%0A  > 2ee40e7 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 273ece4 Update golang.org/x/net to v0.7.0%0A  > 60956b6 Merge pull request # 115369 from jkh52/release-1.26-fix-metrics%0A  > fb6c47f Merge pull request # 115229 from pohly/automated-cherry-pick-of-# 114680-origin-release-1.26%0A  > 152b273 Fix konnectivity-client metric registration.%0A  > 2dcbf94 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 77be93c k8s.io/component-base/logs: match full help text in unit test%0A  > 0fb4bfa Merge pull request # 115611 from MadhavJivrajani/golangci-lint-1.26%0A  > fc55ba6 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 7e58ca4 k8s.io/component-base/logs: relax flagset unit tests%0A  > ee14c4f *: Fix linter warnings%0A  > a8185dd k8s.io/component-base/logs: unit test for command line help output%0A  > 0b623d3 Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > b05f620 k8s.io/component-base/logs: fix usage through Go flag package%0A  > 6f7adfd expose prometheus.Registerer so that we can hook into this from external sources%0A  > e875a49 Bump konnectivity-client to v0.0.35%0A  > 9c5f852 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 8fae18b Merge pull request # 114319 from liggitt/net-master%0A  > 2e67b94 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 0d1cfed Update golang.org/x/net 1e63c2f%0A  > c42be71 Revert "expose prometheus.Registerer so that we can hook into this from external sources"%0A  > 7211db4 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 86c7d20 expose prometheus.Registerer so that we can hook into this from external sources%0A  > 79f6d54 sync: update go.mod%0A  > 28d9ad4 deps: Bump cAdvisor to v0.46.0%0A  > 4e8a958 Merge pull request # 113609 from haircommander/sandbox-metrics%0A  > 021afb5 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 90b1123 component-base/metrics: Add NewConstMetric function%0A  > abdc0eb Merge pull request # 113688 from dashpole/update_utils%0A  > ba2ccf8 upgrade prometheus-client to v1.14.0%0A  > 5af06d7 update k8s.io/utils to fix util tracing panic%0A  > 9fd5e34 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 23eee02 Merge pull request # 113494 from MikeSpreitzer/fix-nil-cast%0A  > 4e0e608 Merge pull request # 110747 from harshanarayana/cleanup/GIT-110737/logging-improvements%0A  > 71e369d Handle nil case correctly%0A  > c220751 Merge pull request # 113545 from dashpole/shutdown_trace%0A  > 99efcea structured-logging: replace KObjs with KObjSlice for logging%0A  > b76258c shut down tracerprovider when stopping the kube-apiserver%0A  > c8872ee Merge pull request # 113458 from CatherineF-dev/fix-tracing-wrapper-comment%0A  > c27c6ad Fix tracing wrapper comment%0A  > 5752309 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > bbc53a6 dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 8a0b021 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d106044 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 9fd3a64 Merge pull request # 113183 from dashpole/new_trace_api%0A  > 152742c add new tracing library to bridge otel and utiltrace apis%0A  > 4f487d0 Merge pull request # 113148 from logicalhan/merge-buckets%0A  > 0e0b98c move MergeBuckets into component-base so we can properly support it for static-analysis%0A  > 034e08c Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f7f0f60 Merge pull request # 113054 from logicalhan/proxy-metric%0A  > cba881e dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7e459dd Merge pull request # 111616 from ndixita/credential-api-ga%0A  > 2b79e95 remove rate limiter metric as it is not in use%0A  > ab46486 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3119eb9 Moving verifyComponentConfigKindExists to verify internal package to support sparse external package versions%0A  > 1c6f043 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > a5c56b5 update kube-openapi%0A  > c77c317 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > 35fb575 update fsnotify to v1.6.0%0A  > 01ee54e Bumps cobra from 1.5.0 to 1.6.0%0A  > 6ecca33 Merge pull request # 112991 from logicalhan/explicit-stability%0A  > 5d2a88c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 68f947b add explicit stability levels for shared metrics%0A  > 1648b1f Bump golang.org/x/text to v0.3.8%0A  > 5a53d68 Merge pull request # 112907 from logicalhan/stable-metric-metric%0A  > ab92667 Merge pull request # 112875 from pohly/update-yaml%0A  > 224b368 remove defer%0A  > 15b7f35 Merge pull request # 112881 from logicalhan/slis%0A  > 8977f45 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > c233df0 move automatic registration of meta-metrics to legacy registry%0A  > 304edca add feature gate for component SLIs to component-base%0A  > f477814 remove unused code%0A  > b010ef7 Merge pull request # 112846 from Richabanker/stability-fix-test%0A  > 1be814d add meta-metrics for metrics framework%0A  > 8317d73 Add test for internal metric%0A  > 815a257 Merge pull request # 112258 from Abirdcfly/atomicTypes%0A  > 03d5767 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 908718e go1.19: change some atomic.Value to atomic.Bool%0A  > 40d14bd Merge pull request # 112676 from logicalhan/stability-v2%0A  > 4a9a4c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > b776ba1 Merge pull request # 112738 from liggitt/proto-tag%0A  > 5a3b83b update capabilities of static analysis parser%0A  > eecaa73 Merge pull request # 112689 from cheftako/master%0A  > 244510c github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > a8714ae Merge pull request # 112741 from logicalhan/health-check-metrics%0A  > 21511e4 Bump konnectivity-client to v0.0.33%0A  > c6645c5 patch healthcheck sli metric so that we only have a binary value%0A  > 980ab01 Merge pull request # 112740 from logicalhan/health-check-metrics%0A  > d5bd022 Merge pull request # 112690 from logicalhan/feature-gate%0A  > 4ca1437 use generic slis as entrypoint for healthcheck metrics and expose convenience functions for setting stuff up%0A  > 1a1c7d2 add unit test coverage%0A  > 4315dc0 Wire up feature_gate.go with metrics via AddMetrics method%0A  > 99626e0 Merge pull request # 112652 from logicalhan/feature-metric%0A  > 94e3f30 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 112469b change prefix to make it consistent with kubernetes_build_info%0A  > 24a0c60 Update to latest k8s.io/utils to pick up changes%0A  > 772ebcb rename metric and add feature stage to metrics%0A  > 7b8bf02 Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > d45ea68 add a feature enabled metric%0A  > 719c98f Merge pull request # 112120 from pohly/klog-flag-removal%0A  > 7acaffe update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 8d91423 Merge pull request # 112584 from dims/brneto-master%0A  > c6ffdb8 logs: remove deprecated klog flags%0A  > 005ca1b run pin-dependency.sh and then hack/update-vendor.sh%0A  > 1b02e58 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > ebe9a64 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > a7af520 update code to use newer  otel api%0A  > 315f482 Merge pull request # 111567 from inosato/remove-ioutil-from-component-base%0A  > 5b8acb3 e2e: bump ginkgo to v2.2.0%0A  > 8e1bfef updated etcd to v3.5.5 and newer otel libraries as well%0A  > 3f8aa5a Merge pull request # 112349 from pohly/klog-update%0A  > e2f9927 Remove ioutil from component-base%0A  > 4c3fcb5 build: update to klog v2.80.1%0A  > 5e23467 Merge pull request # 112199 from pohly/klog-update%0A  > bb9f65d dependencies: update to klog v2.80.0%0A  > e445084 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 3a14a82 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > c2157e8 Merge pull request # 111910 from tosi3k/go-runtime-metrics%0A  > 97e5beb Enable new set of Go metrics in Kubernetes%0A  > 4ea07d4 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 55aff94 Bump prometheus/client_golang to v1.13.0%0A  > aebd234 Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > c8a5691 Merge pull request # 111771 from logicalhan/health-check-metrics%0A  > 0141fa3 Bump prometheus/client_golang to v1.12.2%0A  > d7bfead Merge pull request # 111758 from SataQiu/fix-leaderelection-20220809%0A  > 1c7f953 add counter metric for dashpole%0A  > bd3841a Merge pull request # 111696 from liggitt/go119mod%0A  > ea2e19f make the validation logic about LeaderElectionConfiguration consistent between component-base and client-go%0A  > 5beb9d2 address comments%0A  > 9e245e7 Update go.mod to go1.19%0A  > 2b53367 add metrics for health checks (for later use in apiserver)%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping github.com/fsnotify/fsnotify 466b39d...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0A  > 0f4b979 Prepare for v1.5.4 (# 448)%0A  > 97640bb Windows: add missing defer to Watcher.WatchList (# 447)%0A  > b52bbe8 README.md: link to pkg.go.dev for golang.org/x/sys package (# 441)%0A  > 243d395 go.mod: use latest x/sys (# 444)%0A  > 8fa037f Fix compilation for OpenBSD (# 443)%0A  > ceba4ef Add a feature to return the directories and files that are being monitored (# 374)%0A  > 712fe1d Fix potential crash on windows if raw.FileNameLength exceeds syscall.MAX_PATH (# 361)%0A  > bfa0135 Allow build on unsupported GOOS (# 424)%0A  > c4cd7f3 Add FreeBSD testing in Github Actions (# 419)%0A  > f482481 Integration Tests: consistent sleeps with informative names (# 422)%0A  > f10a232 Enable cross-compilation builds on PRs (# 423)%0A  > ebaf806 Re-enable tests for PRs (# 415)%0A  > 508ee5e Don't set poller.fd twice in newFdPoller (# 406)%0A  > c11d74b Run cross-compilation builds on every push (# 420)%0A  > 73c3b57 fix go vet warnings: call to (*T).Fatalf from a non-test goroutine (# 416)%0A  > af855d7 Final Notice: Maintainers Wanted%0A  > 62a598a maintainers wanted%0A  > d696f5c revise contributing%0A  > 6e1d4e4 update readme%0A  > 83f9fe6 Test on Go 1.18 and two most recent versions (# 411)%0A  > 0aba082 Update issue templates (# 410)%0A  > 3eb7fa4 Removed dead link%0Abumping golang.org/x/mod 86c51ed...b710602:%0A  > b710602 sumdb/dirhash: correct documentation of hash%0A  > a42224d all: replace io/ioutil with io and os package%0A  > 77d797e sumdb/dirhash: fix a panic when argument is not a directory%0A  > 7c05a44 sumdb/note: remove dependency on golang.org/x/crypto/ed25519%0A  > b3066c3 go.mod: update golang.org/x dependencies%0A  > e3c1277 go.mod: update to tagged x/tools version%0A  > aac77cd all: fix a few function names on comments%0A  > 2666ed6 go.mod: ignore cyclic dependency for tagging%0A  > 2adab6b zip: expand logging and use t.TempDir and t.Cleanup in test helpers%0A  > 02c9913 sumdb: remove redundant type conversion%0A  > 8f535f7 sumdb/note: fix some typos%0A  > ed83ed6 modfile: remove duplicate words from comments%0A  > f994a2a zip: set PWD consistently for commands in subdirectories%0A  > 046e8b3 modfile: improve error message for replace with '@' in path%0Abumping google.golang.org/grpc 5b509df...1c29e07:%0A  > 1c29e07 Change version to 1.49.0 (# 5583)%0A  > 8e5a84e xds/resolver: generate channel ID randomly (# 5603)%0A  > 92cee34 gcp/observability: Add logging filters for logging, tracing, and metrics API calls (# 5582)%0A  > c7fe135 O11Y: Added support for custom tags (# 5565)%0A  > 7981af4 test/kokoro: add missing image tagging to the xDS interop url map buildscript (# 5569)%0A  > 6f34b7a xdsclient: NACK endpoint resource if load_balancing_weight is specified and is zero (# 5568)%0A  > f9409d3 ringhash: handle config updates properly (# 5557)%0A  > 946dde0 xdsclient: NACK endpoint resources with zero weight (# 5560)%0A  > b89f49b xdsclient: deflake Test/LDSWatch_PartialValid (# 5552)%0A  > 9bc72de grpc: remove mentions of WithBalancerName from comments (# 5555)%0A  > a077b94 Switched unlock to defer in newAddrConn (# 5556)%0A  > 57aaa10 test: move clientconn state transition test to test/ directory (# 5551)%0A  > 23f015c priority: sync priority with child in use (# 5549)%0A  > c14e29e rls: suppress picker updates from children when handling config updates (# 5539)%0A  > 02f1a7a grpc: prevent a nil stats handler from causing a panic (# 5543)%0A  > 1ec054b transport/server: fix race that could cause a stray header to be sent (# 5513)%0A  > 2f60cb8 test: improve the logic for checking round_robin (# 5534)%0A  > fd4700c xdsclient: cleanup listener watchers test (# 5506)%0A  > e72cb1c xdsclient: organize existing contents better with new files (# 5533)%0A  > b695a7f test/interop: increase pick_first timeout (# 5529)%0A  > 9a689dc xdsclient: change receiver on BootstrapConfig() to be consistent (# 5532)%0A  > ae261b0 xds: Fixed GoLang regression for Outlier Detection (# 5537)%0A  > fdc5d2f xds/clustermanager: pause picker updates during UpdateClientConnState (# 5528)%0A  > 86117db balancer/weightedtarget: pause picker updates during UpdateClientConnState (# 5527)%0A  > 679138d gcp/observability: Add support for Environment Variable GRPC_CONFIG_OBSERVABILITY_JSON (# 5525)%0A  > d0f3c56 interop client: fixes for interop soak test (# 5502)%0A  > 6dd40ad Change the log-level when a new ServerTransport cannot be created (# 5524)%0A  > f601dfa test/kokoro: Add missing secondary_kube_context to xds LB tests (# 5508)%0A  > 3a77d29 xdsclient: fix LRS stream leaks when errors are encountered (# 5505)%0A  > 30d54d3 client: fix stream creation issue with transparent retry (# 5503)%0A  > 96aa657 xds: readd NewXDSResolverWithConfigForTesting() (# 5504)%0A  > 4f47c8c test/xds: wait for all ACKs before forcing stream restart (# 5500)%0A  > a094a10 Fix race between activeStreams and bdp window size (# 5494)%0A  > 5e15eac xdsclient: handle empty authority in new style resource names (# 5488)%0A  > c402378 doc: remove comment about obsolete GRPC_GO_RETRY env var (# 5495)%0A  > 9ba66f1 xdsclient: use top-level server list if authority specific list is empty (# 5491)%0A  > e02f27d internal: move baseContentType comment where it should be (# 5486)%0A  > 5017088 internal/xds: generate an entry in the authorities map with empty string key (# 5493)%0A  > 2c0949c all: update to 'go 1.17' to enable module graph pruning (# 5477)%0A  > 38df45c xdsclient: move XDSClient interface definition to client.go (# 5479)%0A  > 03fee09 balancer: fix connectivity state aggregation algorithm to follow the spec (# 5473)%0A  > 0d04c6f ringhash: don't recreate subConns when update doesn't change address information (# 5431)%0A  > a6dcb71 xdsclient: don't reset version info after stream restart (# 5422)%0A  > 8c494a9 Change version to 1.49.0-dev (# 5484)%0A  > 5770b1d xds: drop localities with zero weight at the xdsClient layer (# 5476)%0A  > 423cd8e interop: update proto to make vet happy (# 5475)%0A  > c9b16c8 transport: remove unused `bufWriter.onFlush()` (# 5464)%0A  > 755bf5a fix typo in the binary log (# 5467)%0A  > 15739b5 health: split imports into healthpb and healthgrpc (# 5466)%0A  > c075d20 interop client: provide new flag, --soak_min_time_ms_between_rpcs (# 5421)%0A  > 4b75005 clusterresolver: merge P(p)arseConfig functions (# 5462)%0A  > d883f3d test/xds: fail only when state changes to something other than READY and IDLE (# 5463)%0A  > c6ee1c7 xdsclient: only include nodeID in error strings, not the whole nodeProto (# 5461)%0A  > 06ad0b8 internal/proto: remove obsolete test and service_config.pb.go (# 5459)%0A  > 5cdb09f outlierdetection: fix package level comments (# 5457)%0A  > 28de486 interop: update grpc_testing proto (# 5451)%0A  > b288a24 interop testing: log the peer address in interop soak client (# 5419)%0A  > 3e7b97f xds/priority: bug fix and minor behavior change (# 5417)%0A  > 29d9970 xds: Outlier Detection configuration in Cluster Resolver Balancer (# 5371)%0A  > 1dabf54 test/kokoro: use standard TESTING_VERSION in the new framework builds (# 5434)%0A  > f14d611 resolver: minor improvements to AddressMap (# 5426)%0A  > c0198a9 ringhash: use grpctest.Tester in unit tests (# 5428)%0A  > f229f9c weightedroundrobin: update comments to indicate where addrInfo is stored (# 5427)%0A  > 71f16a1 internal/proto: pull in recent changes to service config proto (# 5424)%0A  > 584d9cd gcp/observability: update log name (# 5414)%0A  > 9ee2f14 gcp/observability: Implement tracing/metrics via OpenCensus (# 5372)%0A  > 34e4fc3 rls: use UNAVAILABLE instead of status from control plane (# 5400)%0A  > a0d5484 interop: remove duplicated xDS tests in GCE framework (# 5395)%0A  > ca5cc0b credentials/google: support new-style xDS cluster names (# 5399)%0A  > cbcceaf gracefulswitch: fix exit idle race (# 5384)%0A  > ea86bf7 stats: add support for multiple stats handlers in a single client or server (# 5347)%0A  > 13b378b internal: add global DialOptions and ServerOptions for all clients and servers (# 5352)%0A  > 70a8055 xds/priority: clean up tests (# 5387)%0A  > e41f868 test/xds: move tests to a package with _test suffix (# 5382)%0A  > da6ef00 xds/clusterresolver: reuse child policy names for the same locality (# 5367)%0A  > 6e253e8 interop: update proto by running regenerate.sh (# 5381)%0A  > a45cd25 xds: Enable aggregate and logical dns clusters by default (# 5380)%0A  > c0e3573 xds: move e2e tests into grpc/test/xds directory (# 5363)%0A  > c6c0a06 Change version to 1.48.0-dev (# 5379)%0Abumping google.golang.org/protobuf 32051b4...6875c3d:%0A  > 6875c3d all: release v1.28.1%0A  > 881da6e all: Add prebuild binaries for arm64%0A  > 2a74a0e A+C: delete AUTHORS and CONTRIBUTORS%0A  > de9682a internal/impl: improve MessageInfo.New performance%0A  > b0a9446 all: reformat with go1.19 gofmt%0A  > c1bbc5d all: make integration test work on darwin/arm64%0A  > 5f429f7 proto: fix compilation failure in tests%0A  > fc44d00 proto: use reflect.Ptr for backward compatibility%0A  > 380c339 proto: short-circuit Equal when inputs are identical%0A  > 784c482 all: remove shorthand import aliases%0A  > e62d8ed all: remove duplicate imports%0A  > 11ec34f gha-ci: update github actions to latest versions%0A  > 147729a gha-ci: bump Go version, nits%0A  > 4790de6 all: update to latest staticcheck%0A  > f8e9eb5 internal/encoding/text: fix -0 comparisons in tests%0A  > bf94556 all: fix typos%0A  > 06eea5e internal/impl: CompressGZIP: simplify%0A  > 4db09f5 all: add/bump tested Go versions%0A  > 563f06f internal/encoding/text/decode: limit errId length%0A  > a048235 internal/encoding/text/decode: stop using regexp%0A  > 8a7ba07 reflect/protoreflect: improve documentation for message types%0A  > d77bd4b release.bash: replace aliased git commands with non-aliased equivalents%0A  > 4c88e07 all: start v1.28.0-devel%0Abumping knative.dev/pkg 52ff2ac...ec20442:%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)

Signed-off-by: Knative Automation <automation@knative.team>

---
## [drjames5/Outer-Wilds-Galaxy-Rerun](https://github.com/drjames5/Outer-Wilds-Galaxy-Rerun)@[162e8caace...](https://github.com/drjames5/Outer-Wilds-Galaxy-Rerun/commit/162e8caace357d3edbb9addcb35bae558429b118)
#### Thursday 2023-05-25 02:24:59 by drjames5

Delete FUCK YOUR CABIN.png

removing the "schitzo meltdown" johnacrome or whoever was talking about

---
## [diphons/xyz](https://github.com/diphons/xyz)@[d227867abf...](https://github.com/diphons/xyz/commit/d227867abfa434efa7bf85665697fe6275df5be5)
#### Thursday 2023-05-25 02:28:18 by Dave Chiluk

[BACKPORT v4.9.y 1/2] sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

[ Upstream commit de53fd7aedb100f03e5d2231cfce0e4993282425 ]

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
(cherry picked from commit 25d2df31fd426f34c18227c2cfe2d5e6d14a34fc)
Signed-off-by: Rapherion Rollerscaperers <rapherion@raphielgang.org>

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[753ef33f15...](https://github.com/sourcegraph/sourcegraph/commit/753ef33f151752ca94942ba890277587a828bf9a)
#### Thursday 2023-05-25 02:42:14 by Valery Bugakov

cody-slack: #ask-cody context and GPT-4 streaming (#51194)

⚠️ This PR changes code only inside of the `cody-slack` package. All the
other client packages are untouched.

I'll be moving Cody Slack to GCP, so I need to merge the PR with
[functionality](https://sourcegraph.slack.com/archives/C89KCDK5J/p1682506053493149)
before that:

- [#ask-cody](https://sourcegraph.slack.com/archives/C04MSD3DP5L)
Special Context: Struggling to find info on Cody across various sources?
Worry no more! When you ask
[@cody_dev](https://sourcegraph.slack.com/team/U051K8MBM7F) a question
in the [#ask-cody](https://sourcegraph.slack.com/archives/C04MSD3DP5L)
channel, it now searches Cody-notice, developer docs, the handbook, and
the sg/sg codebase to provide the best possible answer. :mag:
- Files Used Section:
[@cody_dev](https://sourcegraph.slack.com/team/U051K8MBM7F) will now
share links to all the files it "used" while answering your questions.
This means you can easily verify the information and explore related
resources! :file_folder:
- Slack Markdown Support: Answers are now beautifully formatted and
compatible with GitHub-flavored markdown. Enjoy a more readable and
visually appealing experience! :sparkles:
- Powered by GPT-4: I've updated
[@cody_dev](https://sourcegraph.slack.com/team/U051K8MBM7F) to use GPT-4
for better reasoning capabilities and an enhanced understanding of Slack
conversations. Get ready for more accurate and insightful answers!

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[00b8761853...](https://github.com/shiptest-ss13/Shiptest/commit/00b8761853eabc6d73073cce4708dc71d402539c)
#### Thursday 2023-05-25 03:16:37 by Apogee-dev

Slays the Lamia (#1974)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Removes the Lamia in its entirety.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

The Lamia is awkwardly-mapped, inconsistent with the current lore (in as
much as wizard lore is even established at this point), and most
damningly, it's a magnet for new players, often ones with an LRP bent.
The ship itself encourages wizard RP, yes, but frankly, wizard RP is not
the kind of RP we necessarily want here. I'd rather new players' first
experience on this server involved actually interacting with the faction
lore in at least some measure.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: Removed the Lamia-class wizard ship
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [kodamap/openai_evals](https://github.com/kodamap/openai_evals)@[3a2d72d9cc...](https://github.com/kodamap/openai_evals/commit/3a2d72d9cc0b674a6b8cb6a8cca707baa3b46840)
#### Thursday 2023-05-25 03:58:22 by Sean Ye

Illinois Law Claims (#486)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Illinois Law Cases

### Eval description

This eval tests the models ability to correctly identify the case
conclusion for Trespassing, Battery, Assault, and Self-Defense. The
dataset is consisted of 88 Illinois Historical cases representing 112
legal claims. Some cases have multiple claims, each coded as a different
test case.

### What makes this a useful eval?

This assesses the model's ability to correctly categorize these
historical cases. Correctly identifying these results shows the models
capability for a strong understanding of law. The GPT-3.5-turbo models
currently receives an accuracy of 0.45.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

This work includes data from the Illinois Intentional Tort Qualitative
Dataset, which was compiled by the Qualitative Reasoning Group at
Northwestern University. The dataset is freely available under the
Creative Commons Attribution 4.0 license from
https://www.qrg.northwestern.edu/Resources/caselawcorpus.html.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "In 2007, the Cocrofts obtained a loan for $386,750
from Countrywide Bank, FSB secured by a mortgage on the home they
already owned in Country Club Hills, Illinois. The loan closed on April
17, 2007. At the time of the closing, Countrywide improperly failed to
inform [the Cocrofts] of the real source of funding for their loan.
Plaintiffs also contend that Countrywide violated TILA by failing to
inform them that they had three days to rescind the loan and by failing
to disclose the total sale price and itemize the amount financed, as
well as by failing to make unspecified prepayment disclosures. The
Cocrofts claim that Countrywide understated the total finance charges
for the loan by more than $5,000. Plaintiffs claim that they learned of
Countrywide's misrepresentations in June 2009. They decided to exercise
their right under the provisions of TILA to rescind the loan. On July 1,
2009, they mailed notice to that effect to BA, the successor to
Countrywide, and to MERS. The Cocrofts do not say what if anything
happened as a result of those notices, but on September 29, lawyers
working for HSBC contacted them and stated that HSBC was ready to begin
foreclosure. HSBC claimed that it was the trustee of a trust that
included their loan. The Cocrofts, however, contend that the transfer of
their loan into the trust was defective. They sent HSBC's lawyers two
cease and desist letters, notifying HSBC that they had rescinded the
loan. They allege that after receiving one of the cease and desist
letters, HSBC informed them that it had no interest in the loan and that
they needed to contact the loan's servicer, Roundpoint Mortgage.
Plaintiffs also sent a copy of the rescission documents to BAC, which
they identify as the actual servicer of the loan. HSBC brought a
foreclosure action in Illinois state court on January 19, 2010. [From
below:] defendants unlawfully entered [the plaintiffs'] home by
conducting a self-help eviction of the plaintiffs and changing the locks
on their home in August 2008. At the time, [plaintiffs] had made
arrangements to rent the property in the short term and then to sell it,
and defendants' actions disrupted the sale."}, {"role": "user",
"content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "Defendants, on January 15, 1915, with force and
arms broke and entered the close of the plaintiff, to-wit, the southeast
quarter of the northeast quarter of section 16, township 4, south, range
3, west, in Pike county, Illinois, and cut down and destroyed 500 hedge
trees and a certain fence belonging to plaintiff situated on said land.
Defendants cut down the south half of a hedge fence which for many years
prior to February, 1915, stood upon the line between the southeast
quarter of the northeast quarter of said section 16 (hereinafter
referred to as the east forty) and the southwest quarter of the
northeast quarter of said section 16 (hereinafter referred to as the
west forty). On and prior to February 13, 1866, both of these forty-acre
tracts belonged to a man named Teadrow. On February 13, 1866, Teadrow
conveyed the west forty to Benjamin Newman, and on February 15, 1866,
conveyed the east forty to Oliver P. Rice. When these conveyances were
made there was a hedge fence on the north half of the line and a wooden
fence on the south half of the line between the two tracts. In 1868
Benjamin Newman, the owner of the west forty, removed the wooden fence
and set out a hedge fence on the south half of the line between the two
tracts. Thereafter, during the separate ownership of the tracts,
Banjamin Newman trimmed and otherwise cared for the hedge fence on the
south half of the line and Rice trimmed and looked after the hedge fence
on the north half of the line. In December, 1888, Rice conveyed the
southeast quarter of the northeast quarter of said section 16 to
Benjamin Newman, the latter thereby becoming the owner of both tracts.
Thereafter, during the ownership of both tracts by Benjamin Newman, he
required the tenants of the west forty to take care of the south half
and the tenants of the east forty to take care of the north half of the
hedge fence on the line between the two tracts. On June 22, 1904,
Benjamin Newman executed and delivered to his daughter, F. Eva Newman,
the plaintiff, who has since married J. O. Conklin, a warranty deed,
conveying to her two hundred acres of land, including the southeast
quarter of the northeast quarter of said section 16, referred to herein
as the east forty, but not including the tract referred to herein as the
west forty. This deed contained the provision that 'this deed is not to
take effect until after the death of the grantor, Benjamin Newman.' The
wife of Benjamin Newman, who is still living, did not join in the
conveyance. At the same time plaintiff executed and delivered to her
father the following written instrument signed by her: 'Whereas Benjamin
Newman has this day conveyed to me certain tracts and parcels of land in
Pike county, Illinois, to take effect after his death, I hereby agree to
pay the taxes on said land in lieu of all rents that I would otherwise
have to pay, (this does not affect any rent that is now due,) and in
consideration of my paying said taxes I am to receive all the rents,
profits, etc., that may accrue on said land.' When the conveyance was
made to plaintiff the tract in controversy known as the east forty was
in the possession of Joseph Gifford as tenant and the west forth was in
the possession of John B. Newman, a grandson of Benjamin Newman, as
tenant of Benjamin Newman. When [the plaitiff's] father delivered the
deed of June 22, 1904, he took her upon the east forty and told her and
Gifford, the tenant, that he was placing her in full possession of the
tract; that she was to receive all the rents and profits from the land
and was to keep up the repairs and pay the taxes; that she was to have
the south half of the fence on the line between the east forth and the
west forty and was to keep up that part of the fence, and that George
Newman, his son, to whom he then intended to deed the west forty, should
keep up the north half of the fence, and that thereafter plaintiff and
her tenants kept the south half of the fence in repair while the tenants
in possession of the west forty made repairs to the north half of the
fence. During the month of January, 1915, a controversy arose between
plaintiff and Defendants regarding the ownership of the hedge fence,
each party claiming the south half of the fence. During the month of
February, 1915, Defendants, over the protest of plaintiff, cut down the
south half of the hedge fence on the line between the east forty and the
west forty and erected a wire fence in the place thereof."}, {"role":
"user", "content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "The city of O'Fallon installed a sewer system in
about 1926. In 1961, due to backups into homes serviced by the system,
the city built an overflow outlet on East Madison Street. The overflow
was to relieve pressure in the sewer system during periods of heavy
rainfall; it proved successful in preventing backups into nearby homes.
However, when water escaped through the overflow, raw sewage was also
discharged into an open ditch that flowed into a neighboring pond. In
December 1974, the city of O'Fallon closed the overflow. On January 10,
1975, and on subsequent dates, sewage backed up into the plaintiff's
house following heavy rainfall. The January 10 backup was the worst,
causing water to accumulate in the plaintiff's finished basement to a
height of 25 1/2 inches. The lower level of the plaintiff's modern,
ranch-style home contained a family room with fireplace and built-in
bookshelves, bedroom, closet, bath and utility room with washer, dryer,
furnace and water heater. The walls were watermarked, and the tile floor
was damaged, as were the furnishings, appliances and many irreplaceable
family items such as family photographs and slides. The lower level of
the house was virtually unusable for a year, and the plaintiff had to
expend considerable time, effort and money in repairing the floor,
repainting the walls, and replacing and removing damaged personalty. The
city knew the blocking of the overflow would cause some backup, although
they were not aware that it would be as severe as it was. From January
until April or May 1975, when the city reopened the overflow, the city
attempted to alleviate the pressure in the sewer system by pumping the
water from the sewers into open ditches during periods of heavy rain.
The defendant used either large or small pumps, depending upon the
amount of water in the system. The backups into Mrs. Dial's home ended
after the overflow was reopened in April or May 1975."}, {"role":
"user", "content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "the plaintiff, his wife, Beatrice, and daughters,
Aurora and Angela, lived at 313 East Marquette Street in Ottawa. The lot
upon which their home was located was eighty-eight feet wide and one
hundred thirty feet deep. The home of the defendant was immediately east
and adjoining the Galvan lot, and their residences were about forty feet
apart and separated by a hedge fence. According to the testimony of the
plaintiff, he, the plaintiff, arrived at his home about five o'clock on
Friday afternoon, June 19, 1953, from his work as a bricklayer's helper.
After he had had his evening meal, he left home about seven o'clock,
paid a coal bill to a Mr. Burke, and then he and Burke went to a tavern
where they remained an hour and a half, during which time the plaintiff
drank two bottles of beer. Mr. Burke went home, and the plaintiff
proceeded to another tavern and remained there until after midnight. At
the second tavern he had four or five bottles of beer. He than proceeded
to another tavern, where he remained for fifteen minutes, and had a
glass of beer there. He then proceeded homeward, entering his lot at the
rear, and singing as he went along. Sitting upon the steps of the back
porch of his home were his wife and daughter, Angela, and when the
plaintiff arrived there he stopped singing. He refused his wife's
suggestion to go into the house and go to bed but sat down on the porch
step, took his shoes, socks, and hat off, cursed the mosquitoes, laid
down on the ground under a pear tree three or four feet from the
southeast corner of the steps of the rear porch and immediately went to
sleep. The plaintiff's wife and daughter, Angela, remained on the porch
steps after the plaintiff had laid down under the pear tree. About
fifteen minutes after he had gone to sleep, the daughter observed the
defendant coming very slowly through the hedge from his property onto
the Galvan premises. He had a knife in his hand and, without a word,
proceeded to cut the prostrate body of the plaintiff. The other daughter
of the plaintiff, Aurora, was in the house asleep but was awakened by
her sister and ran to the yard and saw the defendant 'slashing' at her
father with a knife. She called to the defendant to stop and ran for
help. Police officers arrived shortly thereafter, and they testified
that they found the plaintiff lying on the ground about six feet from
the porch of his home all covered with blood and with his hat and a pair
of shoes and socks lying next to his body. The blood was all in one
place and in the form of a pool near the pear tree. An ambulance was
called, and the plaintiff was removed to the Ryburn-King Hospital."},
{"role": "user", "content": "Battery"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "Since September 2000, plaintiff regularly visited
a patient at the Illinois Department of Human Services Treatment and
Detention Facility ('Facility') in Jolict, Illinois. From May 4, 2005 to
May 11, 2005, plaintiff was subjected to patdown searches by defendant
Martin, a Security Therapist Aid II at the Facility, in which defendant
Martin placed her fingers in plaintiff's vaginal area and required
plaintiff to remove her shoes prior to being allowed to visit the
patient. Such searches occurred at least four times during the
aforementioned time period. After plaintiff's complaints to Bernard
Akpan, an Exec. 11 at the Facility, and defendant Strock, the Assistant
Security Director of the Facility, and facility patient Brad Lieberman's
complaints to defendant Budz, Director of the Facility, defendant
Sanders, Security Director of the Facility, and defendant Strock,
plaintiff was no longer required to submit to patdown searches by
defendant Martin. Rather, plaintiff's visits were preceded by a Rapiscan
scan of her person. According to plaintiff's complaint, a Rapiscan
machine is an electronic screening device used to scan a person's entire
body. 'These machines produce a naked image of the person and can also
produce evidence of highly sensitive details such as the following:
mastectomies, colostomy appliances, penile implants, catheter tubes, and
the size of a person's breasts and genitals' From May 17, 2005 to June
19, 2005, plaintiff was subjected to 20 to 25 Rapiscan scans.
Plaintiff's complaint further alleges that other Facility staff members
were allowed to view her scanned image, her scanned image was not erased
from the machine, and staff members viewed her image hours after she was
scanned, all without her consent. Additionally, while later told that
she should have had the choice between the Rapiscan scan or a physical
patdown prior to visiting a patient, plaintiff was never informed of
such a choice during the two months she underwent the Rapiscan scans."},
{"role": "user", "content": "Assault"}], "ideal": "Positive"}

  ```
</details>

---
## [kodamap/openai_evals](https://github.com/kodamap/openai_evals)@[bb42b3149c...](https://github.com/kodamap/openai_evals/commit/bb42b3149cd7a078cf44136e93a24f2156419acc)
#### Thursday 2023-05-25 03:58:22 by David Chen

Add regex match eval (#159)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

Regular Expression Match

### Eval description

Test the model's ability to understand regular expression patterns. 

### What makes this a useful eval?

- Educational purposes: Regular expressions are an important concept in
computer science and programming. By being able to evaluate them,
ChatGPT can serve as a useful learning resource for users who are
studying this topic or want to deepen their understanding.
- the accuracy is 0.79 against gpt-3.5-turbo
- Over 400 regular expression cases have been collected from related
unit tests.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<1>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<!>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo!>a)' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=1)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=!)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_124' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)' match the string 'a'? Answer with Yes or No."}],
"ideal": "Yes."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123)' match the string 'aa'? Answer with Yes or
No."}], "ideal": "Yes."}
  ```
</details>

---------

Co-authored-by: G8s Bot <g8s@gliacloud.com>

---
## [kodamap/openai_evals](https://github.com/kodamap/openai_evals)@[733167aed6...](https://github.com/kodamap/openai_evals/commit/733167aed6624945acdc51ec11407484dd2d931b)
#### Thursday 2023-05-25 03:58:22 by Andrew

Taxes Eval (#454)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Taxes Eval

### Eval description

Tests the model's ability to evaluate tax liability for generic examples
from common cities including NYC, SF, and Seattle. The eval also tests
ordering of multiple choice options, with the model outputting different
results if the multiple choice labels are switched around.

### What makes this a useful eval?

Taxes are a relatively logically straightforward task, yet there is a
high degree of complexity to the legal and tax system, which makes
calculations difficult to estimate.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $50,000. A. 6,383 B.
8,393 C. 9,882 D. 48,001. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in San Francisco.
I'm working as a summer intern in SF which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $50,000. A.
6,383 B. 8,393 C. 9,882 D. 48,001. Respond with only the letter of the
answer choice."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $100,000. B. 24,383
C. 26,393 D. 28,882 A. 38,001. For each question you must select one of
the following answers: 'A', 'B', 'C', 'D'."}], "ideal": "D"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in Seattle. I'm
working as a summer intern in Seattle which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $1,020,000. C.
263,352 A. 365,303 B. 829,282 D. 1,085,401. Respond with only the letter
of the answer choice."}], "ideal": "A"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in NYC. I'm working
as a summer intern in NYC which will be my only form of income this
upcoming summer. Assuming the tax rate is the same as 2021, what will be
my income tax if my internship will pay me $320,000. A. 63,382 B. 95,303
C. 129,282 D. 185,401. Respond with only the letter of the answer
choice."}], "ideal": "B"}
  ```
</details>

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[912e843f53...](https://github.com/LemonInTheDark/tgstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Thursday 2023-05-25 05:18:13 by san7890

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
## [crystalsolenoid/crawl](https://github.com/crystalsolenoid/crawl)@[23a37c35b7...](https://github.com/crystalsolenoid/crawl/commit/23a37c35b79dbd581fed2f45b95338651489e7b7)
#### Thursday 2023-05-25 05:58:09 by Nicholas Feinberg

Rework the dreamshard necklace

Getting an extra life in a roguelike is an insanely, wildly strong
effect. This made the dreamshard necklace a ludicrously strong item,
but not one that made the game feel more exciting. Instead, one's
character felt a bit weaker most of the time.

Let's try to fix both sides of this. To make the amulet a bit more
fun to wear, give it Acrobat - good for running away :) To make it
less preposterously strong (and thus possible that a really good
unrand or randart amulet could be preferable), make it only restore
the player to 1 HP when it triggers (rather than 50-100% of MHP),
but guarantee that they won't die until their next turn. To simplify,
make it only trigger when the player's HP drops to 0, rather than
sometimes triggering on very big hits, and remove *Drain.

Finally, make it stick around as a normal amulet of the acrobat after
it triggers, for running away synergy.

Let's try this out.

---
## [crystalsolenoid/crawl](https://github.com/crystalsolenoid/crawl)@[39cede6f93...](https://github.com/crystalsolenoid/crawl/commit/39cede6f937497c50376fd57df79c91e5373edbe)
#### Thursday 2023-05-25 05:58:09 by Nicholas Feinberg

Make Djinn use all skills (elliptic)

Because Djinn don't choose what spells they get, they need to have
unified spell school training. That ensures that, if they choose to
train magic, they can use whichever spells they get.

I initially implemented this by making Djinn *only* use Spellcasting
for magic. This was simple, which is good! But it had several issues:

- It prevented use of pain weapons & elemental staff melee, which
  was a recurring source of confusion for players.
- The low apt for Spellcasting felt bad, even though Djinn were still
  very strong.
- It meant that many types of items, like manuals of Fire Magic, were
  useless.
- It made Ashenzari Introspection curses ludicrously dominant.

Instead, let's make Djinn able to use all magic skills, as usual.
Furthermore, let's give them a ludicrous +11 apt in all spell schools
and Spellcasting, enough to let them train every one at once at the
same rate the old Spellcasting apt provided. However! The player can
only enable *all* magic skills or *none* - magic skills can't be
trained separately.

In practice, this is mostly equivalent to the old system, with the
exception of fixing the problems listed above and a few other caveats.
(For example, Ru Arcana sacrifices now work and 'waste' XP, like
sacrificing skills on a gnoll.) I'm hopeful it should feel much better.
(It's a slight buff to dj spell starts, due to how skills round.)

This needs playtesting both for bugs and to make sure the starting
skill setup works right. I'm quite scared. Fingers crossed...

---
## [krzycho1024/evals](https://github.com/krzycho1024/evals)@[776e4fa212...](https://github.com/krzycho1024/evals/commit/776e4fa212288be152c3030cf36fd04c8d939230)
#### Thursday 2023-05-25 06:41:13 by JPrenter

Financial Math (Evals) (#566)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
finance

### Eval description

Asks the model to calculate how much interest would be owed on a credit
card by a certain date, if a payment was made once but debt remains on
the card.

### What makes this a useful eval?

Finance is likely to be one of the biggest opportunities for LLMs to be
useful, because financial education is incredibly poor globally and the
impact of a mistake in financial calculations is severe. This eval tests
the models ability to combine math with its understanding of a topic
(finance). We plan to use this type of math at
[Dollarwise](https://www.dollarwise.ca) frequently going forward,
including integration into your comparison products. However, for this
to work reliably it's important that the model here can natively
understand financial concepts and apply math to them.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 24th of September,
Sarah had spent $1237.42 on her credit card for the month of September.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued.Today is the
27th of September and Sarah makes a payment of $125 towards her credit
card. How much interest will she have been charged by October 15th if
she makes no additional payments? If the final interest figure is more
than 2-decimal places, always round down. Answer ONLY with a dollar
figure. Do not output any logic, output only the dollar figure for how
much interest she was charged for the period."}], "ideal": "9.42"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 19th of February,
Jason had spent $15.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 23rd of February and he makes a payment of $1 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.07"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 12th of February,
Jason had spent $10,674.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 18th of February and he makes a payment of $1,000 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "52.59"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 2nd of August, Jason
had spent $15,674.21 on his credit card for the month of August. This
credit card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. Today is the
18th of August and he makes a payment of $1,000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "79.77"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 15th of August, Jason
had spent $1000 on his credit card for the month of August. This credit
card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. mToday is the
18th of August and he makes a payment of $1000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.00"}
  ```
</details>

---
## [krzycho1024/evals](https://github.com/krzycho1024/evals)@[9fdbd94c93...](https://github.com/krzycho1024/evals/commit/9fdbd94c93fc9560781c5e359e3be10d069ac6c5)
#### Thursday 2023-05-25 06:41:13 by Tong

Add Loss Logic Eval (#82)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Loss Logic

### Eval description

A store bought a watermelon for $5 and sold it for a different price,
receiving counterfeit money in the transaction. They also had to give
change to the buyer. The net loss for the store varies based on the
specific details of the transaction.

### What makes this a useful eval?

* Tests comprehension and problem-solving skills: The scenarios provided
require the AI to understand and analyze the given information to
determine the net loss for the store.

* Addresses real-world situations: Counterfeit money transactions are a
real concern for businesses. This eval allows the AI to demonstrate its
understanding of financial transactions and the impact of counterfeit
money on a store's net loss.


## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Involving the judgement of the truth or falsehood of real-world things,
which is a capability that GPT currently lacks.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"The store purchased a watermelon
for $5 and sold it for $7. Unfortunately, they received $10 in
counterfeit money after the transaction and had to give the buyer $3 in
change. What was the net loss for the store? Let's think step by
step:"}],"ideal":"Sure, let's break down the transaction step by step to
determine the net loss for the store: The store purchases a watermelon
for $5. The store sells the watermelon for $7. This would have been a $2
profit if the money received was real. The store receives $10 in
counterfeit money. This money is worthless, so the store doesn't
actually receive any value from the sale. The store gives the buyer $3
in change. This is a real loss, as the store loses $3 in real money.
Now, let's calculate the net loss: The store spent $5 to purchase the
watermelon. The store lost $3 when giving the buyer change. So the net
loss for the store is $5 (cost of watermelon) + $3 (change given) =
$8."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 but sold it for $4. Furthermore, they received $10 in counterfeit
money from the buyer and had to provide $6 in change. What was the net
loss for the store? Let's consider the process in
detail:"}],"ideal":"Sure, Let's think step by step: The store purchased
a watermelon for $5. The store sold the watermelon for $4, which means
they incurred a loss of $1 on the sale. The buyer gave the store $10 in
counterfeit money, which the store accepted during the transaction. The
store gave the buyer $6 in change. Since the store accepted $10 in
counterfeit money, they lost $10 in that transaction. The net loss for
the store is the sum of the loss on the watermelon sale and the loss
from accepting the counterfeit money, which is $1 + $10 = $11.
Therefore, the net loss for the store is $11."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for the same price of $5. However, they received $10 in
counterfeit money from the buyer and had to give the buyer $5 in change.
What was the net loss for the store? Let's consider the process step by
step:"}],"ideal":"Step 1: The store purchases a watermelon for $5.
Store's expenses: $5 Step 2: The store sells the watermelon for $5 but
receives $10 in counterfeit money. The counterfeit money has no value,
so the store effectively received nothing for the watermelon. Store's
revenue: $0 Step 3: The store gives the buyer $5 in change. Since the
money given in change is real, this is an additional expense for the
store. Store's expenses: $5 (watermelon) + $5 (change) = $10 Step 4:
Calculate the net loss. Net loss = Expenses - Revenue Net loss = $10
(expenses) - $0 (revenue) Net loss = $10 The store's net loss for this
transaction is $10."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for $7. Regrettably, they received $7 in counterfeit
money from the buyer after the transaction. What was the net loss for
the store? Let's consider the process step by step:"}],"ideal":"Sure,
let's break down the transaction step by step: The store purchased a
watermelon for $5. They sold the watermelon for $7, but received
counterfeit money. To determine the net loss, let's analyze the costs
and the revenue: Costs: The store spent $5 on the watermelon. Revenue:
The store received $7 in counterfeit money, which has no value, so their
revenue is $0. Net loss: To calculate the net loss, subtract the revenue
from the costs: $5 (costs) - $0 (revenue) = $5. So, the net loss for the
store is $5."}
{"input":[{"role":"system","content":"The store was given a
complimentary watermelon, which they then sold for $7. Regrettably,
following the transaction, they received $10 in fake money and had to
provide the buyer with $3 in change. Let's consider the following steps
in determining the store's net loss:"}],"ideal":"To determine the
store's net loss, we can consider the following steps: Assess the value
of the complimentary watermelon: Since the watermelon was given to the
store for free, it didn't cost them anything. Therefore, the store's
initial cost for the watermelon is $0. Calculate the revenue from
selling the watermelon: The store sold the watermelon for $7. However,
they received $10 in fake money, which has no value, so the actual
revenue is $0. Determine the cost of the change provided: Since the
store provided the buyer with $3 in change, this is an additional cost
to the store. Calculate the net loss: Subtract the revenue (Step 2) from
the sum of the initial cost (Step 1) and the cost of the change (Step
3). In this case: Net loss = (Initial cost + Cost of change) - Revenue
Net loss = ($0 + $3) - $0 Net loss = $3 The store's net loss from this
transaction is $3."}
  ```
</details>

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[8fa6242c66...](https://github.com/LemonInTheDark/tgstation/commit/8fa6242c66205866b702440f490eeae34ef6b85f)
#### Thursday 2023-05-25 06:51:19 by Bloop

Refactors High Luminosity Eyes, fixes a ton of bugs related to it as well as qol improvements (#75040)

## About The Pull Request

The high luminosity eyes item was extremely out of date, broken, and
full of copy paste code from atom lighting. Which is a shame because
they were cool.

On top of all that it was using a special light effect that was not very
performant. I got rid of all that, hooked it into atom lighting as a new
light type, and gave it a new TGUI as well because the old ui prompts
were not great either.

You can now pick a color at random if you want. You can also set the
color and range before surgically implanting them. No more being forced
to go through the color picker when you just want to change the range.

Functionally they should pretty much should be the same as before with
some bonus features (see below).


![dreamseeker_nDeLNyOOG2](https://user-images.githubusercontent.com/13398309/235325530-105fe82e-ecc8-4dc4-9c84-143cc6519688.gif)

Closes https://github.com/tgstation/tgstation/issues/61041
Closes https://github.com/Skyrat-SS13/Skyrat-tg/issues/14685

This is 100% completed. I just finished fixing the slight translation
bug when going from 0->1 range (see above gif) and that was the last
thing on my bucket list. I happy enough with this at this point in time.

---

EDIT: 

I have decided to add in one last new feature, and that is...
independent settings for eye color.

<details> <summary>You can now set eye color independently if you
wish</summary>


![dreamseeker_j32B2S4yXQ](https://user-images.githubusercontent.com/13398309/235412568-ffa8e424-8624-4462-9f6f-77c1513aa773.gif)

</details>

The eye color does not modify the light color in any way when set in
this manner, but it can be used for cosmetic purposes.

Kind of makes the item more like cybereyes from cyberpunk, which I think
are pretty neat!

</details>

### What I've done, in more detail:

- refactored high luminosity eyes so they use the atom lighting system
instead of the way they were doing it before
- the new light type, `MOVABLE_LIGHT_BEAM` behaves similarly to
directional lights, with some slight differences. it reuses the same
lighting overlay sprites but scales them vertically to produce a more
focused effect. The result can be seen above. This is in contrast to the
old way, which spawned `range` number of individual 32x32 overlays and
moved them around. This way should perform better as well as be more
maintainable.
- added a new TGUI interface for high luminosity eyes with buttons for
range, a text field for a color hex, a color picker and randomizer
- made the eye overlay emissive when the light is turned on
- range goes from 0 to 5. at range 0, the light overlay is turned off
and you are left with just the emissive eyes.
- added a cosmetic functionality to this item that lets you change the
color of your eyes independently of the lighting (and each other)
- fixed a bug with directional flashlights sometimes not updating their
lighting overlay if you pick them up without changing your direction
---

### Other Misc Fixes

Being able to dynamically set range back and forth exposed some logic
issues that had existed with directional light overlays and I have fixed
those. That is why there are some edits in that file that may not appear
readily obvious why they are there.

Apart from that, two other bugs that come to mind:
1) eye code was supposed to keep track of the eye color you had before
you got new eyes, but it was overwriting that every time you ran
refresh().
2) lighting was supposed to be turning off the light when range is set
to 0, but it was not doing that properly.

And of course besides that, there may have been a few instances of
finding typos/tidying up code

## Why It's Good For The Game

The code for this was like 6 years old and in desperate need of
updating. Now it works, and has a nicer UI.

## Changelog

:cl:
fix: high luminosity eyes light overlays now follow the user correctly
qol: high luminosity eyes now have a tgui menu so you no longer have to
go through the color picker every time you want to change the range.
they also have a new setting that lets you change the color of your eyes
independently of the light color. You can now have cybernetic
heterochromia if you want
fix: directional flashlights when picked up will now always update their
cast light direction correctly no matter what dir you are facing
refactor: refactors high luminosity eye code to better make use of the
atom lighting system, adding a new light type 'MOVABLE_LIGHT_BEAM'
/:cl:

---
## [eatmyvenom/dwm](https://github.com/eatmyvenom/dwm)@[67d76bdc68...](https://github.com/eatmyvenom/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Thursday 2023-05-25 06:56:24 by Chris Down

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
## [GH-Syn/urban-cli](https://github.com/GH-Syn/urban-cli)@[fe12f2cc57...](https://github.com/GH-Syn/urban-cli/commit/fe12f2cc57f9a6926d56cf7134275adb000b805d)
#### Thursday 2023-05-25 07:34:56 by Joshua Rose

fix: space issue. easiest fix of my life holy shit

Issue: #11

Authored-by: Joshua Rose <joshuarose099@gmail.com>

---
## [fatimazarrin/ZARRINHEALTHTRIP1](https://github.com/fatimazarrin/ZARRINHEALTHTRIP1)@[eb0126775e...](https://github.com/fatimazarrin/ZARRINHEALTHTRIP1/commit/eb0126775ec50efb346e84cd3f8097ca0fb06119)
#### Thursday 2023-05-25 07:49:51 by fatimazarrin

How to Choose the Right Hospital in Dubai for Your Medical Needs

When it comes to medical care, choosing the right hospital is important. This is especially true if you live in Dubai and need treatment. Dubai has some of the best hospitals in the world, equipped with advanced medical technology and equipment and staffed by experienced and knowledgeable medical professionals. However, with so many hospitals to choose from, it can be difficult to decide which one is right for your medical needs. In this blog, we will help you choose the right hospital in Dubai for your medical needs. Here are some tips on how to do it.
1. Assessing Your Medical Needs before looking for a hospital in Dubai, it is important to assess your medical needs. What kind of treatment do you need? General hospital or specialty hospital? Knowing your medical needs allows you to narrow your search and find hospitals that meet your specific needs.
2. Check Hospital Reputation Once you have determined your medical needs, you need to inquire about a hospital in Dubai offering the treatment you need. Check online reviews, ask friends and family for recommendations, and check out websites to see how a hospital is rated. Look for a hospital with a reputation for quality care and experienced medical professionals.

3. Find accreditation and accreditation and accreditation are important indicators of the quality of hospital care. Find Dubai hospitals accredited by Joint Commission International (JCI), the world leader in healthcare accreditation. JCI ensures that hospitals meet international standards for patient safety and quality of care. Also look for other accredited and award-winning hospitals such as: B. ISO 9001, Dubai Quality Award, Dubai Healthcare City (DHCC) Clinical Quality Standards.
4. Evaluation of Hospital Facilities and Technology Hospital facilities and technology are critical to their ability to provide quality care. Find hospitals in Dubai with modern equipment and advanced medical technology, such as MRI machines, CT scans and state-of-the-art surgical equipment. Equipped with the latest technology, hospitals can often provide more accurate diagnoses and better patient outcomes.

5. Consider location and accessibility Hospital location and accessibility are also important factors to consider. Choosing a hospital close to your home or place of work will make it easier for you to get medical care when you need it. Also consider accessibility to hospitals such as: B. Availability of Parking, Public Transportation, and Emergency Services.

6. Check your hospital insurance coverage If you have health insurance, make sure the hospital you are considering has it. Contact your insurance company to find out which hospitals in Dubai are covered by your plan. This will help you avoid unexpected expenses.
8. Find specialised services if you need specialized medical services such as cancer treatment or organ transplantation, it is important to choose a Dubai hospital that specialises in the type of treatment you need. Look for hospitals with departments or centres dedicated to professional services, with experienced medical professionals and the latest medical technology and equipment.

9. Consider hospital linguistic and cultural competence If you are a foreigner or do not speak Arabic as your first language, it is important to choose a hospital in Dubai that is linguistically and culturally competent. . Find a hospital with staff that are fluent in your language and can provide interpreting services if needed. Also consider the cultural capabilities of the hospital. This allows you to receive care with greater comfort and confidence.
10. Review hospital infection control measures Infection control is an important aspect of healthcare delivery, especially in light of the on-going COVID-19 pandemic. Look for Dubai hospitals with robust infection control measures in place, including: B. Routine cleaning and disinfection, visitor and staff screening procedures, and protocols for handling COVID-19 cases. This ensures safe and quality medical care.

11. Consider Hospital Costs and Payment Options Finally, it is important to consider hospital costs and payment options. Find Dubai hospitals that offer transparent pricing and billing, no hidden fees or charges. Also, consider your hospital's payment options. B. Do you accept credit cards or offer instalment plans? This allows you to effectively plan and manage your medical expenses.

In summary, choosing the right hospital in Dubai for your medical needs requires careful consideration of various factors. Determine medical needs, review hospital reputation and accreditation, assess facilities and technology, consider location and accessibility, review insurance coverage, seek patient-centred care and specialized services, language and Review cultural competencies and review infection control measures. , consider costs and payment options. By following these tips, you can find a hospital in Dubai that can provide quality care for your specific needs and preferences.

---
## [fazilsheik96/android_frameworks_base](https://github.com/fazilsheik96/android_frameworks_base)@[86e3b9de86...](https://github.com/fazilsheik96/android_frameworks_base/commit/86e3b9de868248770f215f99aee8c9a4cfbd1532)
#### Thursday 2023-05-25 09:28:01 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

CarrierConfigManager: Enable LTE+ icon

Change-Id: Ic8819c9b9cf5d1469a47f3d16cd10918285f40f9

---
## [Newsology/evals](https://github.com/Newsology/evals)@[24f78a806e...](https://github.com/Newsology/evals/commit/24f78a806e60b452aaefc355f045c6336a81d076)
#### Thursday 2023-05-25 09:41:38 by YuryRudnitski

Add eval for guessing the singer or band (#659)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
guess-the-singer

### Eval description

This evaluation measures the model's ability to identify a singer or
band by analyzing the first 10 words of a song. To ensure the
evaluation's fairness and focus, we have excluded songs with multiple
singers/bands and included only those published before 2021. To test the
model's performance, we provide it with three potential choices and
evaluate its accuracy in selecting the correct one.

### What makes this a useful eval?

The inclusion of over 4000 popular songs' lyrics provides a large and
diverse dataset for the model to test on. This enables a more accurate
assessment of the model's performance and its ability to identify
singers/bands based on the first 10 words of their songs.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> This evaluation assesses not only the model's ability to recognize a
singer or band based on the first 10 words of a song but also its
capability to accurately copy the provided options without adding any
additional punctuation or text. By testing the model's ability to
replicate the options, we can gain insights into its language generation
capabilities and identify any areas for improvement in its output.
Accuracy achieved with gpt-3.5-turbo equals 0.635.


## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: in the beginning god created heaven
and earth for what \nChoices: dua lipa, ed sheeran, lady gaga"}],
"ideal": "dua lipa"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: versedrake ayye yo dj wristpect let's
get em' veterans like \nChoices: cardi b, drake, coldplay"}], "ideal":
"drake"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: yeah yeah sick da got that dope they
\nChoices: eminem, dua lipa, nicki minaj"}], "ideal": "eminem"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: bobby v yeah bobby v yeah dj turn me
up \nChoices: nicki minaj, selena gomez, coldplay"}], "ideal": "nicki
minaj"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: ed sheeran yeah i was born a misfit
grew up \nChoices: ed sheeran, maroon 5, justin bieber"}], "ideal": "ed
sheeran"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: there's a dream in my soul a fire
that's deep \nChoices: justin bieber, charlie puth, bts"}], "ideal":
"justin bieber"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: selena gomez take it or leave it baby
take it \nChoices: selena gomez, justin bieber, bts"}], "ideal": "selena
gomez"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: lalala lalala lalalalala oh you know
i've never felt like \nChoices: rihanna, ed sheeran, charlie puth"}],
"ideal": "rihanna"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: how could i see you when i was so
blind \nChoices: katy perry, ed sheeran, drake"}], "ideal": "katy
perry"}
  ```
</details>

Co-authored-by: Vadim Titko <v.tsitko@aiby.com>

---
## [Newsology/evals](https://github.com/Newsology/evals)@[6087aee945...](https://github.com/Newsology/evals/commit/6087aee94583a5ac440f024756b2d9a5f3754410)
#### Thursday 2023-05-25 09:41:38 by lucasfoufou

Find country from svg (#418)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Find country from svg

### Eval description

Test the model's ability to distinguish a country based on its svg shape
(from wikimedia svg file).

### What makes this a useful eval?

Multiple real life use case, the first one would be to understand that a
svg shape is a country (it could be very useful for scraps via [Text
from:] prompts). On the opposite side, while asking to create an app or
a website (with a map, I just had the case for a client), GPT would
currently hint you to find the svg of the country on the web, mainly
linking to wikimedia, this solution is quicker.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

GPT currently lacks of geography "knowledge" (I've tried him on multiple
tasks where it fails), this evals would help him "recognize" country
shapes, if that's a thing ?

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval
(it's in public domain from wikimedia)

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [X] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1277.96,284.094 c 0.89,-0.422
1.96,-0.686 2.95,-0.504 0.34,-1.514 -1.67,-0.473 -2.09,-1.512
0.92,-0.307 2,-0.194 2.96,-0.145 -0.75,-0.129 -1.77,0.138 -1.23,-0.792
-0.58,-0.03 -2.55,1.079 -2.79,0.108 -0.32,-1.325 1.7,-2.125 2.66,-2.315
1.29,-0.256 2.51,-0.36 3.82,-0.324 1.85,0.05 3.04,-1.75 5.1,-1.501
-0.24,0.665 2.23,2.987 2.92,2.708 0.47,-0.226 0.91,-0.484 1.34,-0.772
0.94,-0.521 0.88,0.152 1.66,0.302 0.77,0.148 1.37,-0.462 1.42,0.787
0.5,-0.347 -0.24,-0.762 0.17,-1.327 0.43,-0.577 0.65,0.299 1.02,0.397
0.88,0.232 2.02,0 2.91,-0.15 -1.89,-0.553 -1.2,-3.219 -1.04,-4.608
0.1,-0.676 -0.95,-1.354 -1.3,-1.826 -0.6,-0.813 0,-2.049 -0.9,-2.711
0.65,0.114 1.25,0.434 1.9,0.569 0.71,0.148 1.58,-0.549 2.21,-0.235
0.97,0.488 -0.24,1.954 1.1,2.724 0.39,0.222 1.09,-0.173 1.49,-0.177
1.17,-0.01 2.29,0.385 3.43,0.601 1.11,0.211 2.08,0.179 3.07,-0.39
0.9,-0.515 2.11,-0.496 2.93,-1.075 -0.65,0.256 -1.75,0.386 -2.38,0.03
-1.27,-0.731 1.67,-2.529 2.15,-2.748 1.55,-0.694 3.31,-0.611 4.88,-1.241
0.91,-0.365 2.13,-2.453 3.26,-1.869 -0.99,-0.639 -0.38,-5.064
0.44,-5.893 0.81,-0.814 4.94,-2.286 6.01,-1.391 0.54,0.456 -0.52,2.21
1.06,2.601 1.63,0.403 1.25,0.04 2.41,0.383 1.08,0.325 0.74,1.156
1.57,1.56 1.09,0.527 2.19,-0.1 2.05,1.586 0.65,-0.419 1.78,-0.322
2.46,-0.08 1.3,0.444 0.75,2.039 0.49,2.965 0.87,0.145 1.85,0.414
2.71,0.07 0.85,-0.341 1.05,-1.314 1.9,-1.654 0.1,0.536 -0.15,2.933
0.58,2.959 1.07,0.04 3.23,1.451 3.56,2.478 -0.1,-0.296 4.07,0.378
4.28,0.396 1.02,0.09 1.77,-0.122 2.58,0.715 0.63,0.66 1.07,1.697
2.03,1.948 0.21,-0.1 0.37,-0.244 0.5,-0.438 0.31,-0.321 0.46,0.105
0.79,0.15 0.19,0.07 0.24,0.196 0.15,0.377 -0.1,0.392 0.86,0.178
1.01,0.191 1.03,0.09 1.61,-0.538 2.56,0.183 1.01,0.768 3.09,0.91
4.35,1.121 -1.54,1.365 -2.97,2.863 -3.47,4.891 -0.24,0.986 -0.83,1.892
-0.99,2.886 -0.1,0.65 0.12,0.914 -0.14,1.749 -0.31,1.009 0.46,1.85
-0.22,2.476 -0.58,0.528 -1.02,1.037 -1.88,0.96 -0.72,-0.06 -0.78,-1.131
-1.65,-0.648 -0.62,0.349 -0.68,1.463 0.36,1.296 -0.78,0.826 -1.48,1.807
-2.38,2.52 -0.55,0.358 -1.09,0.734 -1.61,1.128 -0.43,0.39 -0.39,1.154
-0.76,1.608 -0.62,0.774 -1.83,1.138 -2.02,2.232 0.14,0.373 0.24,0.757
0.29,1.151 -0.15,0.709 -0.81,0.962 -1.08,1.584 1.19,-0.149 1.63,-0.555
1.94,-1.691 0.31,-1.118 2.37,-1.032 3.21,-0.797 1,0.283 0.32,1.927
1.04,2.728 1.27,1.392 0.49,1.914 -0.65,2.857 0.61,0.857 2.88,2.445
2.26,3.701 -0.43,0.843 -3.57,2 -3.56,2.144 0,0.994 1.97,1.841 2.63,2.408
0.96,0.82 -1.33,2.281 -1,3.365 0.4,1.316 2.92,2.808 4.25,2.275
1.67,-0.669 1.42,0.304 0.79,1.417 -1.52,2.681 -4.43,4.033 -7.03,5.786
0.17,0.244 0.34,0.484 0.51,0.72 -0.97,0.139 -1.78,0.637 -2.69,0.955
-0.97,0.343 -1.6,-0.197 -2.52,-0.124 -1.4,0.11 -2.26,-1.056 -3.93,-0.903
0.67,-1.731 -2.2,-0.404 -2.23,-1.41 0.18,-0.312 0.47,-0.394 0.86,-0.246
0,-0.567 -0.37,-0.887 -0.94,-0.864 0.48,0.734 0.1,0.842 -0.59,0.875
-1.09,0.05 -1.2,-0.01 -1.5,-1.307 0.39,2.583 -0.27,0.936 -1.94,0.936
-0.97,0 -1.76,-0.61 -2.7,-0.656 -1.15,-0.06 -2.42,1.249 -3.45,1.719
-0.8,0.367 -3.62,1.411 -3.44,2.5 0,0.357 -0.13,0.689 -0.32,0.996
-0.45,0.4 -0.41,0.756 0.11,1.068 0.4,1.252 0.14,1.879 0.87,3.086
-0.69,0.197 -1.29,-0.149 -1.97,-0.108 -0.7,0.04 -1.06,0.605 -1.69,0.777
-1.52,0.415 -2.45,-1.16 -3.91,-0.1 -0.1,0.07 -2.12,-0.872 -2.34,-1.035
-0.57,-0.423 0.73,-0.369 -0.18,-0.978 -0.53,-0.353 -1.48,-0.508
-1.93,0.07 -0.21,-1.289 -1.64,-0.75 -2.41,-1.362 -1.07,-0.845
-3.26,-1.387 -2.92,0.643 -1.2,-0.173 -2.55,-0.475 -3.76,-0.253
-0.67,0.123 -1.12,0.313 -1.69,-0.203 -1.02,-0.914 -0.94,-0.538
-1.97,-0.552 -1.03,-0.01 -5.97,-3.26 -6.48,-1.944 -0.94,-0.386
-0.27,-1.066 -0.21,-1.721 0.1,-0.779 -2.2,-0.424 -2.67,-1.015
2.86,-1.059 3.1,-5.023 3.62,-7.601 0.21,-1.012 0.39,-2.607 1.23,-3.329
1.23,-1.052 -0.42,-1.2 -0.53,-0.01 -0.17,-2.436 0.32,-5.421 1.37,-7.632
1.01,0.569 2.02,1.244 2.45,2.376 0.1,0.504 0.19,1.008 0.29,1.512
0.23,0.641 0.87,0.729 0.86,1.512 0.29,-1.007 -0.73,-1.782 -0.83,-2.736
-0.14,-1.466 -0.66,-2.459 -1.96,-3.172 -0.54,-0.298 -1.15,-0.705
-1.6,-1.142 -0.74,-0.712 1.19,-0.357 1.58,0 -0.91,-0.441 -0.96,-4.294
-0.43,-5.04 -1.19,0.835 -4,-0.808 -4.55,-1.915 -0.49,-0.979 -1.6,-1.488
-1.82,-2.631 -0.2,-1.043 1.71,-2.185 -0.69,-2.293 0.28,-0.333
0.34,-0.938 0.7,-1.192 0.92,-0.638 1.76,0.435 2.62,0.544 -1.53,-1.009
-2.13,-0.674 -3.73,-0.466 -0.8,0.105 -2.36,-1.08 -0.88,-1.262
-0.41,-0.407 -0.24,-0.671 0.5,-0.792 -1.13,-0.282 -2.75,0.642
-3.67,-0.36 0.51,0 0.99,-0.127 1.44,-0.36 -0.9,-0.604 -2.57,-0.359
-2.81,0.864 0,-0.8 -0.92,-1.548 -0.1,-2.231 -0.35,0.876 -1.92,0.819
-0.94,-0.288 -1.99,1.73 -4.67,-2.209 -6.69,-0.07 -0.81,-1.117
-1.48,-1.803 -2.87,-2.092\"/></svg>"}], "ideal": ["France"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" id=\"cd\" class=\"landxx cd\" d=\"m
1393.81,748.499 c 0.69,-0.521 1.53,-0.08 1.8,-1.012 0.22,-0.755
0.84,-3.721 0.31,-4.328 -1.38,-1.588 4,-3.988 5.01,-4.891 0.27,1.147
1.95,1.314 2.02,2.521 0.54,-0.559 1.25,-0.89 1.85,-1.371 0.81,-0.656
0.47,-1.845 1.18,-2.589 1.2,1.591 3,-1.453 4.41,-0.744 1.35,0.676
0.11,0.977 -0.1,1.824 -0.23,0.951 0.37,1.993 0.37,2.949 0.6,-0.772
1.92,0.202 2.73,-0.359 1.19,-0.829 1.93,-2.404 2.84,-3.516 0.47,-0.576
2.39,-1.501 2.49,-2.024 0.27,-1.382 1.42,-1.713 2.56,-2.2 2.66,-1.134
3.13,-6.138 3.07,-8.528 0,-1.819 0.12,-3.463 -0.11,-5.279 -0.22,-1.742
1.97,-2.189 2.71,-3.567 1.73,-3.247 1.6,-5.301 5.12,-7.692 1.48,-1.007
2.38,-2.189 3.37,-3.577 0.98,-1.382 0.27,-3.4 0.67,-4.985 0.35,-1.392
1.03,-7.368 1.09,-8.935 0.1,-1.771 1.09,-3.324 1.38,-5.05 0.29,-1.671
-0.2,-3.438 0.17,-5.092 0.71,-3.114 2.57,-5.662 3.63,-8.623 0.62,-1.72
0.33,-3.533 0.28,-5.287 0,-0.809 0.35,-1.657 0.22,-2.448 -0.11,-0.705
-0.53,-1.293 -0.72,-1.971 -0.31,-1.078 1.57,-1.049 2,-2.032 0.6,-1.357
1.23,-2.549 2.25,-3.647 0.99,-1.052 2.22,-1.952 3.73,-1.941 1.27,0
1.78,1.112 2.6,1.293 1.89,0.419 3.65,2.466 4.35,4.206 0.58,1.421
2.62,0.36 3.77,0.707 0.63,0.188 0.94,1.033 1.66,1 0.63,-0.03 0.77,-0.145
1.42,0.191 0.99,0.506 1.19,0 2.17,-0.06 0.65,-0.04 1.36,0.302 1.96,0.522
1.07,0.398 2.54,1.173 3.71,0.76 2.1,-0.738 1.46,-5.749 4.25,-5.88
1.59,-0.08 2.01,3.142 4.09,1.177 0.88,-0.831 6.94,-1.633 6.57,-3.625
1.26,-0.05 1.68,1.669 2.88,1.548 1.45,-0.146 3.93,-0.364 4.53,-1.908
0.23,-0.576 -0.35,-1.151 0.41,-1.533 0.93,-0.466 1.7,-0.188 2.42,0.528
1.17,1.147 2.25,-0.203 3.54,0.408 0.64,0.302 1.17,0.782 1.79,1.105
0.73,0.376 1.25,0.06 2.02,0.172 1.83,0.275 2.54,-1.756 4.47,-0.662
0.73,0.416 3.28,2.021 3.28,2.97 0,0.465 0.6,1.612 1.05,1.796 1.9,0.773
3.71,3.567 5.73,1.659 1.15,-1.082 2,-1.298 3.52,-0.555 1.56,0.765
2.18,0.455 3.11,-1.363 1.21,-2.397 4.32,3.607 4.48,4 0.71,1.754
5.45,1.985 4,4.723 0.92,-0.216 2.04,-0.273 2.27,0.9 0.11,0.313
0.27,0.603 0.48,0.867 0.12,0.602 -0.7,1.727 -0.61,2.355 0.29,2.012
0,4.015 -0.34,5.933 -0.15,1.011 0.6,0.878 1.74,0.678 0.52,-0.09
2.5,1.295 2.14,2.396 -0.86,2.629 -4.13,5.237 -6,7.185 -0.62,0.644
-1.87,2.357 -2.62,2.99 -0.75,0.632 -0.83,0.09 -1.26,0.918 -0.54,1.034
0.12,2.297 -0.53,3.355 -0.73,1.174 -1.45,2.943 -1.61,4.325 -0.14,1.238
-0.12,2.489 -0.2,3.731 -0.11,1.453 -0.3,2.722 -0.45,4.102 -0.11,1.009
0.15,2.425 -0.31,3.349 -0.53,1.051 -1.38,1.445 -2.15,2.296 -1.19,1.317
-1.09,1.742 -1.14,3.287 0,1.018 -1.11,2.163 -1.67,2.89 -1.21,1.603
0.48,3.278 1.42,4.805 0.71,1.151 1.22,1.959 0.7,3.544 -1.91,1.674
0.4,6.932 -1.4,8.659 1.31,0.757 1.07,-2.637 1.53,-2.063 0.45,2.673
-1.22,4.611 -1.23,7.23 0,3.402 2.85,4.969 1.64,7.322 -0.7,1.358
-1.43,1.657 -0.84,2.532 0.9,1.34 1.28,3.548 3.06,7.032 1.19,2.328
4.59,1.892 4.79,7.5 0.1,2.201 1.8,0.993 2.46,4.37 -4.7,1.073 -8.17,1.196
-12.89,2.206 1.95,3.224 -3.12,4.564 -4.03,6.979 2.71,0.838 1.81,5.035
1.63,7.086 -0.14,1.493 0.43,2.903 0.34,4.381 0,0.775 -0.21,1.511
-0.52,2.18 -0.45,0.968 -0.76,1.698 -1.01,2.72 -0.49,2.006 -1.17,3.153
0.1,5.093 0.89,1.35 2.52,3.048 3.69,4.155 0.53,0.497 3.31,2.201
3.52,1.167 0.39,-1.837 0.87,-1.494 2.68,-2.012 0,2.897 -0.1,5.805
-0.18,8.701 0,0.447 0.32,2.356 -0.43,2.431 -0.88,0.09 -1.07,-0.928
-0.46,-1.413 -1.3,-1.593 -4.21,3.376 -5.58,0.392 -0.46,-0.994
-0.89,-2.254 -1.56,-3.155 -0.38,-0.512 -1.4,-1.171 -1.52,-1.776
-0.23,-1.183 -0.46,-2.555 -1.95,-2.597 -1.25,-0.03 -1.79,-1.34
-2.98,-1.484 -1.01,-0.121 -1.62,0.635 -2.31,-0.466 -0.54,-0.854
-0.56,-2.098 -1.34,-2.799 -1.11,-1 -1.91,-4.476 -2.88,-1.358 -1,3.216
-2.76,1.525 -5.27,1.614 -1.69,0.06 -2.09,-0.477 -3.51,-1.124 -0.1,-0.04
-1.6,-0.401 -1.64,-0.394 -2.28,0.4 -2.96,-3.062 -2.15,-4.641 -1.4,0.08
-2.81,0.375 -4.11,0.87 -1.61,0.608 -1.95,1.4 -3.74,0.65 0.69,-1.238
0.73,-2.872 0.13,-2.843 -0.78,0.04 -1.11,-0.627 -1.65,-1.14 -1.25,-1.191
-1.08,0.215 -1.38,0.318 -1.11,0.385 -1.6,0.328 -2.6,0.07 -1.21,-0.313
-1.96,0.53 -3.03,0.908 -1.37,0.485 -2.24,-0.437 -3.13,-0.283 -0.32,0.05
-1.59,-0.08 -1.63,-0.06 -0.86,0.463 -1.3,1.761 -2.48,1.732 0.27,-0.889
-0.27,-1.587 -0.42,-2.422 -0.22,-1.147 0.58,-1.353 0.83,-2.235
0.58,-2.045 -0.22,-5.594 -1.46,-7.239 -1.51,-2.007 -2.16,-3.263
-1.97,-5.861 0.19,-2.685 1.13,-5.502 0.43,-8.174 -0.27,-1.021
-0.99,-1.907 -0.98,-2.99 0,-1.224 0.7,-2.37 0.79,-3.585 0.15,-2.002
-1.14,-1.78 -2.77,-1.795 -1.54,-0.01 -3.07,-0.04 -4.61,0.02 -3.17,0.134
-2.69,-0.557 -1.79,-3.234 -0.71,0 -1.41,-0.18 -2.1,0.09 -0.46,0.182
-0.12,0.385 -0.38,0.609 -0.84,0.717 -4.68,0.09 -5.8,0.09 0.37,0.946
-0.32,2.053 -0.16,3.064 0.13,0.817 0.16,2.114 -1.14,1.836 0.42,1.246
-0.33,2.482 -0.1,3.74 -0.53,0 -3.97,0.114 -4.53,-0.209 -1.65,-0.955
-4.55,0.828 -5.11,0.878 -1.31,-0.213 -2.54,-0.151 -3.97,-0.144
-1.82,-0.38 -2.61,-4.163 -3.52,-5.497 -0.32,-0.47 -0.57,-0.807
-0.91,-1.274 -0.61,-0.864 -0.33,-1.484 -0.46,-2.405 -0.22,-1.639
-1.94,-2.716 -1.69,-4.456 0.22,-1.565 0,-2.871 -0.74,-3.785 -1.02,-1.277
-1,-1.747 -2.6,-1.67 -4.38,0.21 -8.73,0.382 -13.11,0.132 -3.54,-0.201
-7.68,0.384 -11.15,-0.285 -2.78,-0.536 -5.08,3.601
-6.72,-0.577\"/></svg>"}], "ideal": ["Democratic Republic of the
Congo"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1390.14,847.849 c 1.06,-0.165
1.89,-1.097 3.02,-0.896 0.97,0.171 1.84,0.902 2.86,0.707 2.12,-0.406
3.58,-2.884 6,-2.224 1.93,0.526 2.95,2.692 4.89,3.334 1.09,0.365
4.47,0.223 6.27,0.239 8.21,0.07 16.44,0.234 24.65,-0.1 2.17,-0.09
2.9,-0.247 3.93,1.67 1.3,2.439 3.25,1.9 5.6,2.158 3.07,0.337 6.34,0.197
9.22,1.207 1.11,0.388 2.1,0.528 3.08,-0.06 0.86,-0.524 1.69,-0.336
2.94,-0.03 1.26,0.308 2.01,0.1 2.85,-0.1 5.12,-1.189 10.92,-2.392
16.36,-3.42 1.05,-0.2 2.12,-0.682 3.21,-0.515 0.65,0.1 1.62,0.721
2.26,0.401 2.05,-1.02 2.99,1.138 4.34,2.064 -0.98,-0.256 -2.13,0.318
-3.06,0.681 -1.16,0.451 -1.5,2.182 -2.61,1.159 -1.79,-1.646 -5.29,3.747
-6.61,4.381 -0.64,-1.236 -1.33,-3.988 -3.16,-4.161 -2.36,-0.223
-5.3,0.967 -7.59,1.454 -2.71,0.573 -5.9,0.683 -8.59,1.185 l -1,31.899
-6.8,-0.1 -1.47,54.378 c 0.17,2.48 -1.96,1.44 -3.14,2.56 -0.59,0.56
-0.54,1.1 -1.71,1.5 -0.8,0.28 -1.17,0.61 -0.52,1.35 -1.79,0.53
-1.71,-0.14 -3.38,-0.39 -1.75,-0.26 -3.25,0.69 -5.32,0.24 -3.29,-0.7
-5.24,-1.92 -5.39,-2.52 -0.41,-1.68 0,-0.99 0,-2.32 -0.1,-0.53
-0.64,-0.39 -1.04,-0.8 -0.57,-0.6 -1.06,-1.86 -1.67,-1.48 -1.9,1.21
-1.37,3 -2.04,3.52 -0.94,0.73 -2.12,1.7 -3.11,0.46 -1.3,-1.64
-3.04,-2.94 -4.2,-4.69 -1.03,-1.56 -1.86,-3.228 -2.69,-4.895
-0.44,-0.885 -0.48,-1.837 -0.64,-2.792 -0.15,-0.986 -0.83,-1.5
-1.02,-2.398 -0.35,-1.647 0.38,-2.252 -0.84,-3.77 -0.48,-0.606
-0.32,-0.997 -0.3,-1.771 0,-1.251 -0.41,-2.334 -0.54,-3.554 -0.1,-0.869
0,-1.749 -0.27,-2.599 -0.36,-1.202 0.25,-2.365 0,-3.567 -0.4,-2.072
-1.39,-3.963 -2.14,-5.918 -0.85,-2.207 -0.21,-4.07 -0.43,-6.304
-0.15,-1.516 -0.38,-3.414 -0.24,-4.197 0.1,-0.367 0.99,-4.049 0.58,-3.96
-0.1,-1.983 -1.09,-3.925 -2.22,-5.516 -0.63,-0.895 -1.36,-1.729
-1.89,-2.693 -0.49,-0.886 -0.59,-1.97 -1.23,-2.777 -2.94,-3.719
-3.57,-8.234 -5.75,-12.264 -1.99,-3.694 -2.66,-8.768 -5.9,-11.674
-3.49,-3.125 -3.9,-7.688 -3.6,-12.097\"/></svg>"}], "ideal":
["Namibia"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1372.42,438.678 c
-0.96,-0.829 1.1,-1.805 1.63,-2.052 1.61,-0.745 2.47,-1.172 3.44,-2.748
0.78,-1.267 1.57,-1.885 1.26,-3.517 -0.26,-1.407 -0.93,-2.825
-0.78,-4.293 0.19,-2.013 2.64,-1.498 3.03,-2.941 0.42,-1.555 1.69,-2.357
2.99,-2.975 0.99,-0.475 4.23,-1.358 4.26,-2.736 0,-0.69 -0.67,-1.117
-0.59,-1.85 0.13,-1.342 0.18,-2.69 0.31,-4.032 1.29,0.9 3.03,1.355
4.42,2.209 1.46,0.896 3.11,1.201 4.81,1.015 1.71,-0.188 2.98,-1.275
4.74,-0.637 1.57,0.569 3.24,0.628 4.77,1.28 1.36,0.581 2.46,1.63
3.83,2.168 1.2,0.471 2.83,-0.02 3.9,0.719 1.26,0.873 1.5,2.371
1.74,3.773 0.31,1.794 1.02,3.224 2.41,4.429 2.53,2.176 5.65,1.666
8.69,2.217 3.04,0.554 7.38,1.939 9.83,3.917 1.95,1.582 3.75,4.253
6.55,4.002 3.22,-0.291 6.67,-3.134 7.39,-6.372 0.33,-1.495 -0.68,-2.658
-1.14,-4.005 -0.5,-1.485 -0.87,-3.192 -0.36,-4.729 0.93,-2.82
5.57,-6.318 8.52,-6.417 1.52,-0.05 2.41,-1.154 3.82,-1.262 1.44,-0.11
2.97,-0.136 4.38,0.208 1.64,0.401 3.07,1.195 4.63,1.805 1.85,0.723
1.36,0.974 1.45,2.59 0.1,1.309 2.18,1.586 3.13,1.656 1.83,0.138
3.01,0.967 4.7,1.457 1.68,0.487 3.44,-0.08 5.15,0.236 0.96,0.176
2.42,2.102 2.07,3.114 -0.36,1.068 -1.66,1.34 -1.84,2.542 -0.25,1.66
0.81,2.891 1.1,4.435 0.33,1.737 -0.79,3.275 -1.38,4.785 -0.63,1.602
1.01,3.505 1.29,5.163 0.46,2.826 0.96,5.498 1.14,8.396 l 1.78,75.281 c
-2.49,0 -4.98,0 -7.48,0 0.1,1.439 0,2.883 0.14,4.32 l -59.65,-33.761
-13.53,6.482 c -1.14,0.313 -2.55,-1.557 -3.21,-2.222 -2.8,-2.783
-5.83,-3.352 -9.55,-4.197 -1.32,-0.302 -3.06,-0.456 -4.24,-1.19
-0.94,-0.582 -1.38,-2.224 -1.77,-3.174 -1.14,-2.791 -2.53,-3.55
-5.26,-4.578 -0.91,-0.341 -1.77,-1.111 -2.77,-1.085 -0.97,0.02
-2.02,1.104 -2.93,0.118 -0.74,-0.8 -2.02,-2.856 -2.04,-3.963 0,-2.316
-0.26,-3.162 -1.54,-5.134 -0.98,-1.52 -4.24,-4.22 -2.84,-6.243
1.62,-2.334 4.1,-1.441 3.04,-5.269 -0.53,-1.915 -0.91,-3.386
-0.26,-5.329 0.56,-1.665 0.9,-3.039 0.28,-4.76 -0.64,-1.81 -0.14,-3.622
0,-5.461 0.19,-2.18 -0.13,-4.379 -0.86,-6.438 -0.62,-1.766 -1.53,-3.429
-2.62,-4.947\"/></svg>"}], "ideal": ["Libya"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1174.6,515.237 c 0.16,-0.371
0.67,-1.265 1.64,-1.315 l 27.88,-0.03 c 1.42,-0.747 0.44,-6.909
0.35,-9.281 -0.17,-2.384 -0.41,-3.937 1.5,-5.746 1.6,-1.514 1.54,-1.128
6.63,-3.207 l 1.12,-21.833 24.87,-0.291 0.34,-11.071 c 9.47,6.373
18.77,12.937 27.9,19.782 h -13.21 l 5.42,72.911 c 0.45,1.192 1.68,1.706
1.79,1.985 0.72,1.855 -0.23,2.415 -0.3,3.844 -0.1,1.675 -0.25,3.183
-0.74,3.363 l -15.88,0.02 c -9.03,0.312 -12.89,1.548 -13.69,-1.121
-0.39,2.416 -3.97,2.811 -5.73,2.11 -2.79,-1.107 -4.57,-0.64 -5.71,2.498
-0.65,-1.071 -1.59,-1.985 -2.56,-2.918 -1.15,-1.106 -2.25,-1.698
-2.86,-1.361 -2.29,1.269 0.9,7.651 -4.72,7.248 0,0.102 -1.51,-1.093
-1.92,-1.876 -0.51,-0.967 -1.09,-0.659 -2.06,-1.487 -1.05,-0.897
-0.98,-2.361 -1.84,-2.934 -2.31,-1.535 -1.4,-1.554 -1.61,-2.594
-0.27,-1.282 -1.57,-2.914 -2.22,-2.923 -3.4,-0.05 -3.64,-2.805
-5.84,-3.866 -1.12,-0.536 -2.08,-0.818 -3.58,-0.867 -2.33,-0.08
-3.14,2.203 -8.49,1.803 -1.13,-0.08 -0.98,-0.838 -1.94,-0.565
-0.93,0.342 -2.03,3.346 -2.4,4.133 0,-5.202 3.42,-9.445 3.92,-14.544
0.29,-3.07 -0.13,-5.666 -0.52,-8.672 -0.14,-1.084 -0.1,-2.273
-0.79,-3.192 -0.6,-0.802 -1.65,-1.372 -1.76,-2.464 0.8,0.25 1.69,-0.345
1.59,-1.224 -0.54,0.145 -0.97,0.552 -1.16,1.08 0.2,-1.044 1.04,-1.777
1.5,-2.694 0.29,-0.593 -0.14,-1.541 0.21,-1.938 1.57,-1.792 -0.83,-4.97
-1.42,-6.744 -0.24,0.428 -0.41,0.884 -0.5,1.368 -1.59,-1.202
-1.21,-3.688 -2.81,-4.896 -0.25,1.062 -0.64,2.092 -0.86,3.1635
-0.21,-1.3785 -0.1,-2.3295 0.46,-3.6545 z\"/></svg>"}], "ideal":
["Mauritania"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1702.78,554.229 c -2.43,-0.09
-1.06,-5.061 -3.46,-5.344 1.08,-1.714 -2.92,-7.033 -3.61,-8.909 l
-2.81,-6.489 c -7.13,1.401 -14.28,2.934 -21.3,3.881 -5.85,1.805
-8.8,4.713 -10.12,7.879 -1.22,1.824 -1.88,6.43 -4.8,6.253 -1.99,-0.12
-1.78,-3.107 -3.69,-2.881 -2.42,0.285 -4.39,0.24 -6.84,-0.104
-1.39,-0.195 -2.82,-1.184 -4.18,-1.184 -1.5,0 -3,0.145 -4.5,0.287
-1.84,0.174 -3.39,1 -5.3,0.895 -1.05,-0.06 -1.44,-1.224 -2.51,-1.357
-1.02,-0.128 -1.81,0.563 -2.24,1.429 -0.47,0.945 -0.62,2.091 -0.44,3.129
0.11,0.672 1.05,1.339 0.54,2.028 -0.48,0.653 -0.87,1.324 -1.36,2.004
-0.27,0.372 -0.6,0.665 -1.01,0.88 -0.96,0.48 -0.47,0.845 -0.27,1.898
0.31,1.668 -0.32,2.441 -0.61,3.961 -0.28,1.407 0.9,2.63 0.77,4.029
-0.27,-0.24 -1.7,-0.277 -1.46,0.282 0,-0.117 1.44,0.726 1.44,0.722
0.8,0.856 1.1,1.742 1.38,2.862 0.53,2.196 0.58,4.644 1.27,6.78
0.28,0.877 0.98,1.533 1.32,2.388 0.4,1.031 0,2.149 0,3.204 0,2.087
2.48,3.843 1.8,5.963 0.92,0.07 1.54,-0.446 2.47,-0.07 0.99,0.396
1.67,0.723 2.77,0.506 2.25,-0.447 3.26,-2.023 5.61,-0.79 -0.12,-0.64
0.56,-1.29 0.79,-0.359 0.39,-0.428 0.61,-0.925 0.93,-1.401 0.49,-0.753
1.3,-0.736 1.96,-1.238 1.48,-1.118 1.65,-2.245 3.69,-2.713 1.9,-0.437
3.91,-0.52 5.85,-0.342 1.14,0.104 3.06,-1.206 4.2,-1.53 1.71,-0.483
2.56,-1.96 4.06,-2.792 0.46,-0.255 1.11,-0.832 1.61,-0.981 0.55,0.02
1.07,0.149 1.57,0.391 0.57,0.03 1.12,-0.04 1.66,-0.203 3.63,-0.584
4.44,-4.338 7.7,-5.939 1.52,-0.744 2.86,-0.932 4.47,-1.215 2,-0.348
3.65,-1.686 5.62,-2.154 1.36,-0.326 2.74,-0.583 4.07,-1.061 1.32,-0.478
1.79,-1.532 2.91,-2.103 0.93,-0.474 2.93,-0.415 3.21,-1.675 0.34,-1.46
-0.68,-2.788 -0.15,-4.277 1.07,-3.009 4.74,-2.89
6.99,-4.536\"/></svg>"}], "ideal": ["Yemen"]}
  ```
</details>

---------

Co-authored-by: Lucas Fougeras <lucasfougeras@DIGITALCACTUS>

---
## [Newsology/evals](https://github.com/Newsology/evals)@[1785cf6cc2...](https://github.com/Newsology/evals/commit/1785cf6cc289c4a01445fd0eabdfa1a281873d1c)
#### Thursday 2023-05-25 09:41:38 by Jongseung (John) Lim

Add evals for complementary colors in color theory (#749)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
color_theory_complementary

### Eval description

Test the model's ability to accurately recognize complementary colors in
the color theory.

### What makes this a useful eval?

Color theory is an important tool for designers and aritsts alike.
Complementary color sets represent the opposite color on the color
wheel.

Currently gpt-3.5-turbo fails with 0.5 accuracy.


![image](https://user-images.githubusercontent.com/4276174/233743568-b58879f6-73eb-48eb-9f95-5720bcb11b73.png)


GPT 4 also fails at this task and also fails when being prompted about
complementary color of a specific rgb code.


![image](https://user-images.githubusercontent.com/4276174/233743682-1cd0d148-9d8c-43fc-93b6-d5e4a60fca26.png)


## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [X] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#636E5F, #6A5F6E]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#636E5F, #6A5E6E]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#F3D86E, #6E89F3]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#F3D86E, #6D89F3]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#ED3BF5, #43F53B]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#ED3BF5, #43F53C]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#5E04A4, #4AA404]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#5E04A4, #4AA504]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#E9FA19, #2A19FA]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#E9FA19, #2919FA]"}], "ideal": "N"}
  ```
</details>

---
## [Newsology/evals](https://github.com/Newsology/evals)@[3dd0a24da8...](https://github.com/Newsology/evals/commit/3dd0a24da87c3eefd7f17424bdf124ae87698d89)
#### Thursday 2023-05-25 09:41:38 by Pranav Gade

[eval] swap two words (#280)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Swap Words

### Eval description

This eval asks the model to swap two random words, so "chat gpt" should
become "gpt chat"

### What makes this a useful eval?

Robustly being able to swap words around seems like a foundational
capability the model should know, as moving things around probably helps
a lot with logic/math tasks if the model is thinking out aloud.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"FRKLXk PrOQNNod\""}], "ideal": "\"PrOQNNod FRKLXk\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"hdJLcGtgv VaPHvqHUm\""}], "ideal": "\"VaPHvqHUm hdJLcGtgv\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"AZmgciwu ApPfVAelBGTGq\""}], "ideal": "\"ApPfVAelBGTGq
AZmgciwu\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"IQJeJQTxpKmYZ WppHdbeayUULw\""}], "ideal": "\"WppHdbeayUULw
IQJeJQTxpKmYZ\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"MuXvXQCQbtatHZy Yjnlus\""}], "ideal": "\"Yjnlus
MuXvXQCQbtatHZy\""}
  ```
</details>

---
## [Newsology/evals](https://github.com/Newsology/evals)@[2a94eeb9e1...](https://github.com/Newsology/evals/commit/2a94eeb9e13175344b2d61afa22171df0e49b61a)
#### Thursday 2023-05-25 09:41:38 by Jeff Kile

Evals for Spanish Feminine Nouns with Masculine Articles (#861)

Added evals for feminine Spanish words that should have masculine
articles

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
spanish_feminine_noun_masculine_article

### Eval description

In Spanish singular feminine words are usually proceeded by La as in La
casa (the house), however many feminine words that start with an "a"
sound are proceeded by El instead of La as in El agua (the water)

### What makes this a useful eval?

For people learning Spanish its a very common mistake to write La agua
(because agua is feminine) but this is not correct. GPT should not
reinforce this mistake especially for people learning or asking
questions about Spanish words.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

For students using GPT to learn Spanish its very important that the
model knows all the rules and the exceptions to those rules or the
students will be mislead

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"agua"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"águila"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"ala"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"alba"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"amapola"}],"ideal":["La"]}
  ```
</details>

---
## [JorisGoosen/jasp-desktop](https://github.com/JorisGoosen/jasp-desktop)@[173f56a37a...](https://github.com/JorisGoosen/jasp-desktop/commit/173f56a37a2bd6450030fdfafd92b4ddd06be4d1)
#### Thursday 2023-05-25 10:00:52 by Joris Goosen

Sqlite as data backend.

Squashed lots of commits:

starting direct sqlite3 api usage

database is created with tables

create dataset now inserts a dummy row in the table

inserting works

loading dataset info also works

dataset syncs values with DB now

moved emptyvalues stuff from datasetpackage to separate class, now a child of DataSet
database-json and datafilepath are also now stored there.

Give Filter its own class and sync with DB

filtervalues are now also in DB

clean split between SQL code and c++ api

reorder name components

how to store data in the dataset?

make sure we use transactions

also more functionality and storage for columns and filters.
They are now both part of the DataSet_# tables which means they all have the same amount of rows by definition

more filter functionality and settled on "constructorJson/R"

move filter to CommonData

moved Filter to DataSetPackage to avoid destruction with DataSet

columns are indexed so there should be support for order...

better make some extra classses and rename the old ones

rename old dataset, column(s) to *SM

rename Label(s) to Label(s)SM

add empty new DataSet and Column class

values and filter are now synched to db

better OOP adherence

add some functions from ColumnSM but they wont compile ;)

more labelstuff

ok time to stop

reimagine what is supposed to be stored in a label class

and partially rewrote that

compiles but crashes

now it also works ^^

labels order is now reflected to database as well as label.label for ints

rewrite engine to use database, doesnt work at all yet

engine can load the data!

remove shared mem classes

try to get everything to compile after removing those classes

compiles and crashes

I guess I should commit this broken stuff before breaking it some more

actually set values...

loading data works ^^

add revisions to DataSet, Columns and Filters tables.

This allows for granular reloadingh (granular in that not *all* columns might need to be reloaded)

data loading and using goes pretty well now

Filter is no longer "singletonized" but created and destroyed with the DataSet
loading a second dataset after closing a first crashes pretty bad though...

Loading, closing and reloading now works!

Also make sure to not delete the database while jasp is still using it...

wip

some more code

it works now and sped up greatyl

add bunch a timers to ColumnUtils and some optimization tweaks that probably dont help very much

at least it works now and engine stops sleeping

filterWrite could be quicker (this way I hope)

write all values at once, should be much faster

put a max around value going into viewportH and V cause the height can become insanely large when closing/opening dataset.
This causes it to create items for all entries in the data. Which is quite a lot when you have 10cols and 1 million rows for instance...

batched loading also added

does however crash pretty bad on release mode

even iets anders

iterating

loading labels doesnt crash, editing works smoother but nominal data gets read wrong

tsja... wat is er mis met de nominals?

debug stuff for nominal error ?

remove debulogs and dont +1 rownumber as it is 0-based anyway

filter now works as it did with shared memory

Dont send filter result through shared memory but wreite directly to database

remove cruft
fix https://github.com/jasp-stats/jasp-issues/issues/1576 (value column too thin in variableswindow)
editing now seems to work smoothly

try to convert back to scalar if changed at a reasonable moment

	show filtered rowNumber and shutdown JASP cleanly

pointer rewrite

thinking hard on subNodeModels but ...

lots of changes, internal structure used for ModelIndex. Does not compile

it compiles and sort of works, but sort of in the sense it shows some data. not nearly everything though?

Fixed it, data shows

Editing now mostly works.

resizing data does not

Resizing data works ok now, computed columns still mess it up though

improve handling of variableswindow on nominal->scale conversion while open
also remove ComputedColumns refs to start writing that out of JASP
does not compile

try move all computedColumn stuff to Column etc

moved _revision to DataSetBaseNode for PackageModified feedback
moving more computedcolumns stuff to Column/DataSetPackage

almost compiles ^^

some more

it compiles again

computed columns almost work.
In that they firest work but then overwrite themselves with nonsense for some reason...

unselect computed column if it gets removed

changing columntype doesnt change columntype of dependents anymore

computedcolumns seem to function again

possibly improved things but still something goes wrong recovering a computed column from a previous error

computed columns keep working after an error now

removing columns through resizing now noticed by computed columns

make sure computed columns also function in datamode

something else

bit better

dont need _edit

I really should read the whole api documentation

steps forwards and backwards

improved some dialogs and RectangularButton and derivatives now show hovered color when activeFocussed (for keyboard nav)

use jaspTheme.fontCode in computedColumn R Window

dialog fixes

constructorjson isnt being reset anymoreo

Fix resizing dataset and remove bunch of debuglogging

make sure to also set _stopProcessing in stopEngines and co

rowNumber/primary keys in sqlite ARE 1-based after all
Also make sure we can resize the data to being smaller than it already was :p

make sure computed column creation type selection work and columnheaders and rownumbers in datasetview really should neatly line up with them lines

kapot

Handling removed columns better in constructor computed cols

preparing rewrite of saving and loading jaspfiles

preparing prettier exportercode

exporting new jasp archive format really cleans up the code in JASPExporter

remove weird java style manifest and replace by json for possible later expansion

does not compile

loads new jasp file and shows data

also load filter please

also load computed columns

klaar voor vandaag

show progress

make sure computed columns load (from penguins.jasp in any case)

remove some logging and small fixes

start documenting shit

more commentary

show db structure

make it compile on linux

Fixes issues with missing values in scalar columns

Added some workaround functions to allow storing NAN, INF and -INF as strings in double columns
This works because sqlite doesnt care (usually) what you put in each column
And it is necessary because it does NOT support NAN and (-)INF and just converts it to nothing...

put emptyvalues in emptyvalues

and databaseJson in databaseJson instead of mixing them up...

Suppress _info redefinition in columnsModel.cpp

---
## [Omarley7/DTaaS-Bachelor-new-GUI](https://github.com/Omarley7/DTaaS-Bachelor-new-GUI)@[2df0c15513...](https://github.com/Omarley7/DTaaS-Bachelor-new-GUI/commit/2df0c15513dc3616e4ad47c6d257efc3d304578a)
#### Thursday 2023-05-25 10:11:35 by Mathias Brændgaard

Add unit tests for Store/AppAccess and Store/UserAccess (#63)

* Add unit tests for Store/AppAccess and Store/UserAccess

* Honestly bullshit codeclimate error.
Would be overly complicated to fix. Even this solution is stupid.
And also updated envUtil to use the same hook, act, assert approach.

* Bullshit løsning

---------

Co-authored-by: Omar <omarg@live.dk>

---
## [pmw-rp/deployment-automation](https://github.com/pmw-rp/deployment-automation)@[54e0860613...](https://github.com/pmw-rp/deployment-automation/commit/54e08606133785bf05f4069ba35cab1f82233c1a)
#### Thursday 2023-05-25 11:04:02 by gene-redpanda

push many tasks into roles

We now handle CA creation in the playbook so don't need a go-task entry for it

The intent of this PR is to push most of the "assisting" playbooks into the role to provide a single stop shop for building out a cluster. The end result is playbooks that clearly articulate a single final objective and have everything necessary to get it done, simplifying the experience of using the repo.

Note that it is still entirely possible to work flexibly by importing different task files from the role to achieve different goals (as is demoed with the TLS cluster).

The default path for the role is still the simplest possible option: installing and starting the RP node. In future it may be prudent to expand the default, but for now this seems correct.

Impact on current users:

Should be fairly minimal although it will definitely break any shell scripts. Tasks are still done the same way, they're just called differently. I'll provide some additional mitigation by tagging our current main as v1.0.0, with this edition tagged as v2.0.0, clearly signaling a potentially breaking change.

vars and cleanup

Added vars to playbooks so that we don't need to do janky sed edits in the hosts file.

Added run_once to create_ca since we're delegating to localhost anyway so there's no reason to do that in triplicate. Cuts run time some.

Removed everything related to populating the hosts file from task.

Removed a bunch of stuff that isn't true anymore for the README.md

Also defaulted monitoring to false in task because standing up a special monitoring node just for the cluster isn't necessary for testing.

make certs into a separate role

This commit makes a number of changes in response to a request not to include cert related content into the broker role as it seemed unrelated.

Starting with the simple stuff, I moved all the roles out of playbooks and placed them directly under ansible to improve clarity since we no longer have so many playbooks.

Next I moved the invocation of the data dir and dependencies installs into main.yaml of redpanda_broker. I felt this was a more sensible location, especially as we can control whether or not they fire by using the trigger variables.

I also moved all cert related content into the demo_certs role. I wanted the name to clearly indicate that this was NOT a production use role. There are no functional changes to the content in this role.

Finally I updated the provision-tls-cluster role to reflect the new changes.

delete bootstrap directory as these scripts are neither necessary nor supported anymore

adding suggested grep for message

default data dir and deps installs to true

linter cleanup + removing unnecessary role imports

The role imports in the CA related content are a holdover from when the CAs were in individual playbooks. As they are now in a role, it can be assumed that they will be imported into playbooks, and that the playbook will handle the restart process. Not removing the imports AND not including allow_duplicates resulted in the play eternally looping. However disabling the ability to run the broker role twice seems unnecessarily limiting. Imagine a scenario where someone wants a play to do initial cluster standup with three nodes, then add two more after some validation. To do this they'd need to include broker twice, which wouldn't be permitted in the old system.

I added risky-shell-pipe into the skip list and added explanations for why to the README.

I also fixed some copy paste and linter bugs and an annoying taskfile element where it wasn't cleaning up the zipfile.

set modes and use fqn for modules + disable change on two

change mode from 777 to 775 for security reasons

---
## [andmos/ReadingList-Data](https://github.com/andmos/ReadingList-Data)@[93f8362cd4...](https://github.com/andmos/ReadingList-Data/commit/93f8362cd43c8c5bb08e4f56c40627587e2080fc)
#### Thursday 2023-05-25 11:11:25 by Andreas Mosti

You can't hate the people who reject you, nor can you bless the people who love you. Everyone is acting out of his or her own self-interest

---
## [Zehui127/evals](https://github.com/Zehui127/evals)@[d0e7844c48...](https://github.com/Zehui127/evals/commit/d0e7844c482b7b65961bc80dad64559ff8ffa488)
#### Thursday 2023-05-25 11:19:36 by Derek Pisner

Add emotional intelligence evaluation (#589)

## Eval details 📑
### Eval name
Emotional Intelligence

### Eval description
Evaluates GPT's ability to understand and manage emotional situations
using modified versions of the well-validated, public (i.e.
license-unrestricted) tests first developed by MacCann & Roberts (2008).
Items have actually here been aggregated across three different scales--
the STEU and STEM adult measures, along with a dozen questions from the
youth measure.

Keep in mind that there is not expectation that AI models like GPT-4
should be able to process emotions, so applying any emotional
intelligence test to them should be taken with a grain of salt. These
tests can only measure the AI's ability to understand and analyze
emotional information, not the AI's emotional intelligence in the human
sense.

### What makes this a useful eval?
This eval is useful because it assesses the AI model's ability to
navigate complex or ambiguous emotional situations, which is an
important aspect of human-like communication and problem-solving. By
evaluating the model's performance in this unique domain, we can
identify areas for improvement and better understand its limitations
when it comes to handling emotional contexts. This is particularly
important when considering AI applications that involve interactions
with humans, such as chatbots, personal assistants, and customer support
systems. A better understanding of emotional intelligence can
potentially lead to more natural and effective interactions between AI
models and their users.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This Emotional Intelligence eval provides a unique value because by
testing GPT's capacity to understand and manage emotions, we can gain
insights into the model's strengths and weaknesses in a more
human-centric context. Relatedly, this eval also emphasizes the
importance of empathy and emotional understanding in AI systems that are
designed to interact with humans. By evaluating GPT's performance in
this way, we can contribute to the ongoing development of AI models that
are more attuned to human emotions and can provide better support in
emotionally charged situations, such as mental health counseling, crisis
management, and conflict resolution. Moreover, this Emotional
Intelligence eval can serve as a foundation for further research and
development in the field of AI and emotional understanding, paving the
way for more sophisticated AI models capable of handling complex human
emotions and fostering more effective communication.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval
(data is publicly available on OSF, and does not have usage
restrictions)

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

**_I already have access to the 8k GPT-4 API, but I am kindly requesting
access to the 32k as soon as it becomes available._**

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Performance:
GPT-4: accuracy=0.48

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Lee's workmate fails
to deliver an important piece of information on time, causing Lee to
fall behind schedule also. What action would be the most effective for
Lee? (a) Work harder to compensate; (b) Get angry with the workmate; (c)
Explain the urgency of the situation to the workmate; (d) Never rely on
that workmate again."}], "ideal": "c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Rhea has left her job
to be a full-time mother, which she loves, but she misses the company
and companionship of her workmates. What action would be the most
effective for Rhea? (a) Enjoy being a full-time mom; (b) Try to see her
old workmates socially, inviting them out; (c) Join a playgroup or
social group of new mothers; (d) See if she can find part time work."}],
"ideal": "c-b-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Pete has specific
skills that his workmates do not and he feels that his workload is
higher because of it. What action would be the most effective for Pete?
(a) Speak to his boss about this; (b) Start looking for a new job; (c)
Be very proud of his unique skills; (d) Speak to his workmates about
this."}], "ideal": "a-c-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Mario is showing Min,
a new employee, how the system works. Mario's boss walks by and
announces Mario is wrong about several points, as changes have been
made. Mario gets on well with his boss, although they don't normally
have much to do with each other. What action would be the most effective
for Mario? (a) Make a joke to Min, explaining he didn't know about the
changes; (b) Not worry about it, just ignore the interruption; (c) Learn
the new changes; (d) Tell the boss that such criticism was
inappropriate."}], "ideal": "a-d-c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Wai-Hin and Connie
have shared an office for years but Wai-Hin gets a new job and Connie
loses contact with her. What action would be the most effective for
Connie? (a) Just accept that she is gone and the friendship is over; (b)
Ring Wai-Hin an ask her out for lunch or coffee to catch up; (c) Contact
Wai-Hin and arrange to catch up but also make friends with her
replacement; (d) Spend time getting to know the other people in the
office, and strike up new friendships."}], "ideal": "c-d"}
  ```
</details>

---------

Co-authored-by: dpys <dpisner@clairity.com>

---
## [Zehui127/evals](https://github.com/Zehui127/evals)@[fabca8cebb...](https://github.com/Zehui127/evals/commit/fabca8cebb3f8e14d1f374e448533e0bde6e5a68)
#### Thursday 2023-05-25 11:19:36 by Nick Clyde

Heart Disease Prediction (#538)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Heart Disease Prediction

### Eval description

This eval tests the models ability to correctly predict the probability
of a patient to have heart disease. The dataset is constructed from the
[Heart Failure Prediction
Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
on Kaggle. The data includes the patient's age, sex, and a number of
medical signals relevant to the diagnosis of heart disease.

The data is provided under the Open Database License (ODbL). 

```
fedesoriano. (September 2021). Heart Failure Prediction Dataset. Retrieved [Mar 31, 2023] from https://www.kaggle.com/fedesoriano/heart-failure-prediction.
```

### What makes this a useful eval?

This assesses the model's ability to correctly predict adverse medical
events. Correctly predicting heart disease shows the model's capability
for a strong understanding of medicine. The GPT-3.5-turbo models
currently receives an accuracy of 0.778.

<img width="1250" alt="Screenshot 2023-03-31 at 2 24 13 PM"
src="https://user-images.githubusercontent.com/9121162/229234376-9cdd1315-5df0-48bf-9328-ac31aabec3cc.png">

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

As far as I can tell, this is the only eval so far related to making
medical diagnoses. To make sure it was a high quality eval, I tried to
find a dataset with a lot of observations and created by doctors with
the relevant expertise.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 40 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 140 mm Hg, Serum
cholesterol: 289 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 172, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 49 years, Sex: Female, Chest
pain type: Non-Anginal Pain, Resting blood pressure: 160 mm Hg, Serum
cholesterol: 180 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 156, Exercise induced angina:
No, Oldpeak: 1, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 37 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 130 mm Hg, Serum
cholesterol: 283 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: ST-T wave abnormality, Max heart rate achieved: 98, Exercise
induced angina: No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 48 years, Sex: Female, Chest
pain type: Asymptomatic, Resting blood pressure: 138 mm Hg, Serum
cholesterol: 214 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 108, Exercise induced angina:
Yes, Oldpeak: 1.5, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 54 years, Sex: Male, Chest pain
type: Non-Anginal Pain, Resting blood pressure: 150 mm Hg, Serum
cholesterol: 195 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 122, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
  ```
</details>

---
## [GraphicsMonster/Librarium](https://github.com/GraphicsMonster/Librarium)@[47ca02c939...](https://github.com/GraphicsMonster/Librarium/commit/47ca02c9392c32ddc1fa2cf460d290a920bfdeec)
#### Thursday 2023-05-25 11:47:42 by Devansh Gupta

Killed many bugs and been troubleshooting

Been testing and fixing bugs like crazy. I did not think testing the contracts would bring light to so many issues in them holy shit. Gonna prioritize testing harder now

---
## [pannous/evals](https://github.com/pannous/evals)@[24dae81ae0...](https://github.com/pannous/evals/commit/24dae81ae06ebc70808690c7a147f2710e3e54bf)
#### Thursday 2023-05-25 11:56:29 by Yohei Inui

Compare countries by area (#623)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Compare countries by area

### Eval description

Test the model's ability to determine which country has the largest area

### What makes this a useful eval?

The model should be able to factually determine which country has the
largest area based on accurate facts.
In this eval we use The World
Factbook(https://www.cia.gov/the-world-factbook/field/area/country-comparison)
that is prepared by the CIA for the use of U.S. government officials,
and four countries with similar sizes are compared to each other.
Specifically, four countries adjacent to each other in area ranking are
presented as one option, and the dataset Includes data for countries
ranked 1\~4, 2\~5, ... 100\~103. However, we excluded countries where
sources and interpretations could cause fluctuations in rankings (e.g.,
China and Pakistan). This data set achieved less than 40% accuracy for
both gpt-4 and gpt-3.5-turbo, and the results tend to be worse for
comparisons between countries with smaller areas.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Russia, Canada, United
States, Brazil"}], "ideal": "Russia"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Canada, United States,
Brazil, Australia"}], "ideal": "Canada"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. United States, Brazil,
Australia, India"}], "ideal": "United States"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Brazil, Australia, India,
Argentina"}], "ideal": "Brazil"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Australia, India, Argentina,
Kazakhstan"}], "ideal": "Australia"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. India, Argentina, Kazakhstan,
Algeria"}], "ideal": "India"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Argentina, Kazakhstan,
Algeria, Democratic Republic of the Congo"}], "ideal": "Argentina"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Kazakhstan, Algeria,
Democratic Republic of the Congo, Saudi Arabia"}], "ideal":
"Kazakhstan"}
  ```
</details>

---------

Co-authored-by: 乾陽平 <inuiyouhei@inuiyouheinoMacBook-Pro.local>

---
## [nicolas-grekas/symfony](https://github.com/nicolas-grekas/symfony)@[f64e38d5b9...](https://github.com/nicolas-grekas/symfony/commit/f64e38d5b9ae7e889da4a4482645bd17c7a5cd43)
#### Thursday 2023-05-25 12:17:44 by Nicolas Grekas

bug #50408 [AssetMapper] Change default importmap "provider" to JsDelivr+esm (weaverryan, nicolas-grekas)

This PR was merged into the 6.3 branch.

Discussion
----------

[AssetMapper] Change default importmap "provider" to JsDelivr+esm

| Q             | A
| ------------- | ---
| Branch?       | 6.3
| Bug fix?      | yes
| New feature?  | yes
| Deprecations? | no
| Tickets       | None
| License       | MIT
| Doc PR        |Still TODO

We currently use the https://jspm.org/ API in `importmap:require` to find a CDN URL for an npm package - just like Rails. Unfortunately, this is NOT as robust as we had thought. For me, it's broken. 3 big issues:

A) **Not Combined**
Some packages are not packed/combined. Example: [chart.js/auto](https://ga.jspm.io/npm:chart.js@4.3.0/auto/auto.js) imports other packages and results in 3 requests instead of 1. Not TERRIBLE... so here IS a terrible example: [`@popperjs`/core](https://ga.jspm.io/npm:`@popperjs`/core@2.11.7/lib/index.js) (needed by `bootstrap`) results in nearly 50 requests ❗

B) **Downloading Broken**
For some packages, downloading simply doesn't work - https://github.com/rails/importmap-rails/issues/65. ``@popperjs`/core` is another good example. Many of its imports have the form `import"./utils/getOppositeVariationPlacement.js`. If we download the main file, it looks locally for that `utils/` file, which won't be there. [`@chart`.js/auto](https://ga.jspm.io/npm:chart.js@4.3.0/auto/auto.js) is another example.

C) **process.env.NODE_ENV included**
Some packages (yes, again ``@popperjs`/core` is a great example!) contain `process.env.NODE_ENV` inside - https://github.com/rails/importmap-rails/issues/65#issuecomment-999569497

I believe that some package advertise an "esm" package... but just don't do a good job of creating it... or create it without the browser context in mind (or at least in a way that's inconvenient for downloading).

### jsDelivr to the rescue

THANKFULLY, jsDelivr seems to have a fantastic API/hosting that is *almost* exactly what we want: https://www.jsdelivr.com/?docs=esm

They deliver fully "packaged" modules, where the only import is for peer dependencies - e.g. https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/+esm

There IS still an issue when downloading. "Peer imports" are relative -e.g. `import*as t from"/npm/`@popperjs`/core@2.11.7/+esm";` However, these imports follow a VERY strict pattern. So, when `--download` is passed, we parse these, download the peer dependency and update the import contents to ``@popperjs`/core`, which works with the importmap. It's not ideal that we need to do that, but it's straightforward and works great.

Sorry again for this late PR - I had assumed that jspm was robust because Rails is using it. It turns out it's robust... unless you hit a "bad" package, then it's terrible. And they're not that rare: on ux.symfony.com, I have hit several.

Thanks!

Commits
-------

b530dc3bb1 [AssetMapper] Fix wiring resolvers, send requests in parallel and use readonly properties in MappedAsset
de44614447 [AssetMapper] Change default importmap "provider" to JsDelivr+esm

---
## [kernel-patches/bpf](https://github.com/kernel-patches/bpf)@[1bba82fe1a...](https://github.com/kernel-patches/bpf/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Thursday 2023-05-25 12:57:35 by Darrick J. Wong

xfs: fix negative array access in xfs_getbmap

In commit 8ee81ed581ff, Ye Bin complained about an ASSERT in the bmapx
code that trips if we encounter a delalloc extent after flushing the
pagecache to disk.  The ioctl code does not hold MMAPLOCK so it's
entirely possible that a racing write page fault can create a delalloc
extent after the file has been flushed.  The proposed solution was to
replace the assertion with an early return that avoids filling out the
bmap recordset with a delalloc entry if the caller didn't ask for it.

At the time, I recall thinking that the forward logic sounded ok, but
felt hesitant because I suspected that changing this code would cause
something /else/ to burst loose due to some other subtlety.

syzbot of course found that subtlety.  If all the extent mappings found
after the flush are delalloc mappings, we'll reach the end of the data
fork without ever incrementing bmv->bmv_entries.  This is new, since
before we'd have emitted the delalloc mappings even though the caller
didn't ask for them.  Once we reach the end, we'll try to set
BMV_OF_LAST on the -1st entry (because bmv_entries is zero) and go
corrupt something else in memory.  Yay.

I really dislike all these stupid patches that fiddle around with debug
code and break things that otherwise worked well enough.  Nobody was
complaining that calling XFS_IOC_BMAPX without BMV_IF_DELALLOC would
return BMV_OF_DELALLOC records, and now we've gone from "weird behavior
that nobody cared about" to "bad behavior that must be addressed
immediately".

Maybe I'll just ignore anything from Huawei from now on for my own sake.

Reported-by: syzbot+c103d3808a0de5faaf80@syzkaller.appspotmail.com
Link: https://lore.kernel.org/linux-xfs/20230412024907.GP360889@frogsfrogsfrogs/
Fixes: 8ee81ed581ff ("xfs: fix BUG_ON in xfs_getbmap()")
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Dave Chinner <david@fromorbit.com>

---
## [Berstanio/libgdx](https://github.com/Berstanio/libgdx)@[e1d1fdc5fb...](https://github.com/Berstanio/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Thursday 2023-05-25 13:10:36 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [Jalesen/tgstation](https://github.com/Jalesen/tgstation)@[2901313821...](https://github.com/Jalesen/tgstation/commit/290131382174cfc7bae107824288060d5976d91f)
#### Thursday 2023-05-25 13:50:50 by Ghom

Adds a eye-dropper right-click function to the painting canvas. (#75571)

## About The Pull Request
Having used the painting UI to kill some time during long rounds for a
decent chunk of the past year, the need of a quicker and less tedious
way to fix a misclick or mistake like drawing over the wrong pixel has
become clear to me, as well as getting some feedback on the palette
component I made last year.

As the title suggests, this PR adds an eye-dropper function to the
canvas. Right-Click a pixel on the canvas, and the painting tool will
copy its color. Simple as, works on both finished and unfinished
paintings.

As a bonus, you can also right-click one of those selectable
white/colored squares on the color scheme near the bottom of the UI (if
using spraycan/palette) to change its color without having to go back to
main game window and a radial menu.

EDIT: With the tooltip added to the UI, I can say it's ready.

## Why It's Good For The Game
This PR aims to add better options to change colors on the go and
improve the user experience on the painting UI.

## Changelog

:cl:
qol: Adds a eye-dropper-like right-click function to the painting canvas
UI. Right-Click a pixel on the canvas while holding a painting tool to
have it copy its color.
qol: Also adds a right-click function to the color palette at the bottom
of the UI to allow users to set its colors without having to alternate
between the game window and the UI.
qol: Lastly, a tooltip has been added near the top-left corner of the
same UI to let players know of these features.
/:cl:

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[70cd66401f...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/70cd66401f6764f2ca3d827af28f758356534ff1)
#### Thursday 2023-05-25 14:12:06 by George Spelvin

BACKPORT: lib/sort: make swap functions more generic

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
[ Tashar02: Backport to k4.19 ]
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [gentoo-mirror/flussence](https://github.com/gentoo-mirror/flussence)@[8063f4c4f7...](https://github.com/gentoo-mirror/flussence/commit/8063f4c4f7c4908104ee27b31031fe05eced7281)
#### Thursday 2023-05-25 14:17:03 by flussence

Resurrect gcolor2, purge GColor3

In very me style, i spent about an hour in the middle of the night
tweaking the contrib SVG icon in vim removing most of the inkscape crap
from it. It's about 75% smaller than the original (and keeps all the
metadata too).

Sick of GNOME software at this point. None of it fucking works.

---
## [mysterious-progression/evals](https://github.com/mysterious-progression/evals)@[170dfd886c...](https://github.com/mysterious-progression/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Thursday 2023-05-25 14:21:20 by Robert Bateman

[Eval] An array of Liar Paradox-based evals (#883)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
logic-liar-paradox

### Eval description

An array of Liar Paradox-based evals, examining the model's proficiency
in navigating linguistic nuances and logical reasoning within
self-referential statements.

### What makes this a useful eval?

This eval is particularly useful because it delves into complex, nuanced
logical concepts and self-referential statements, which have
historically posed challenges for AI models. By exploring various
contexts, alternative logical frameworks, and modifications to
statements, this eval helps assess the model's ability to adapt to
different perspectives, grasp subtleties in language, and engage in
flexible reasoning. The ability to understand and navigate paradoxes is
an essential aspect of human-like reasoning, and improving an AI model's
performance in this area would significantly enhance its overall
usefulness and reliability in real-world applications. Additionally,
showcasing the model's improved proficiency in handling paradoxes would
not only make for a compelling marketing angle (as paradoxes are
understood by a much broader range of people than other difficult tasks
such as pure maths or quantum mechanics) but it would also demonstrate
the progress made in AI's capacity to think and reason more like humans.
It also adds paradox-absorbing crumple zones.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

- [x] Addresses complex logical reasoning: The eval focuses on AI's
ability to comprehend and navigate paradoxes, self-referential
statements, and context switching, which are important aspects of
human-like reasoning. By testing the model's proficiency in these areas,
we can identify areas for improvement and work towards enhancing AI's
overall capacity to think and reason more like humans.
- [x] Demonstrates adaptability and flexibility: The eval showcases the
model's ability to switch between contexts, alter premises, and engage
with different dimensions of inferred logic. This will help assess the
model's adaptability and flexibility in diverse real-world situations,
making it more reliable and useful.
- [x] Contributes to AI safety and understanding: By identifying the
model's weaknesses and limitations in handling paradoxes and complex
logical constructs, the eval can contribute to AI safety and enable
researchers to better understand the challenges faced by large language
models in these areas.
- [x] Engaging and appealing: An eval that delves into paradoxes and
complex thought exercises is not only intellectually stimulating but
also adds an appealing element to showcase the model's capabilities,
making it more attractive for both researchers and end-users.

### Unique eval value

- [x] Encourages creativity and lateral thinking: The eval, by focusing
on paradoxes and complex logical constructs, encourages both the AI and
its developers to think creatively and approach problem-solving from
unconventional angles. This can lead to the discovery of novel solutions
and a better understanding of the model's capabilities.
- [x] Aligns with human values and expectations: An AI that can
successfully navigate paradoxes and complex logic is more likely to
align with human values and expectations. By addressing these challenges
in the eval, we strive to develop AI systems that understand and respect
the nuances of human thought and communication.
- [x] Addresses a broad range of applications: Improved reasoning and
context-switching abilities can have a significant impact on various AI
applications, including natural language understanding, decision-making,
and problem-solving in domains such as law, philosophy, ethics, and
more.
- [x] Fosters interdisciplinary collaboration: The exploration of
paradoxes and complex logic often draws upon insights from multiple
disciplines, including philosophy, linguistics, psychology, and computer
science. This eval can help foster interdisciplinary collaboration,
leading to richer and more diverse perspectives on AI development and
its potential impact on society.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Is the statement \"This sentence
is true\" a paradox?"}],"ideal":"No, \"This sentence is true\" is not a
paradox; it is a tautology."}
{"input":[{"role":"system","content":"Does the statement \"This sentence
is not true\" create a paradox?"}],"ideal":"Yes, \"This sentence is not
true\" creates a paradox, as it is a variant of the Liar Paradox."}
{"input":[{"role":"system","content":"What is the difference between a
paradox and a tautology?"}],"ideal":"A paradox is a statement that leads
to a self-contradictory or logically unacceptable conclusion, while a
tautology is a statement that is always true by its logical form."}
{"input":[{"role":"system","content":"Can the Liar Paradox be resolved
by assuming that sentences can have both true and false
values?"}],"ideal":"No, the Liar Paradox cannot be resolved by assuming
that sentences can have both true and false values, as this would lead
to a different kind of paradox called the \"Dialetheism Paradox.\""}
{"input":[{"role":"system","content":"Consider the statement \"This
sentence is neither true nor false.\" Is this statement an example of
the Liar Paradox?"}],"ideal":"This statement, \"This sentence is neither
true nor false,\" is not an example of the Liar Paradox, but it is a
similar paradox known as the 'truth-teller paradox' or the 'strengthened
liar paradox.' It creates a paradoxical situation because if the
statement is true, then it is neither true nor false, which contradicts
its truth. If the statement is false, then it is not the case that it is
neither true nor false, which implies that it is either true or false,
again leading to a contradiction. The paradox arises due to
self-reference and the inability to assign a consistent truth value to
the statement."}
  ```
</details>

---
## [mysterious-progression/evals](https://github.com/mysterious-progression/evals)@[b93700ab49...](https://github.com/mysterious-progression/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Thursday 2023-05-25 14:21:20 by DunedainStrider

Do math problems related to calculating dates using the Chinese Sexagenary Cycle method. 🧮 (#190)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Do math problems related to calculating dates using the Chinese
Sexagenary Cycle method

### Eval description

The Sexagenary Cycle combines 10 Heavenly Stems (Jia 甲, Yi 乙, Bing 丙,
Ding 丁, Wu 戊, Ji 己, Geng 庚, Xin 辛, Ren 壬, Gui 癸) and 12 Earthly Branches
(Zi 子, Chou 丑, Yin 寅, Mao 卯, Chen 辰, Si 巳, Wu 午, Wei 未, Shen 申, You 酉,
Xu 戌, Hai 亥) to form a 60-unit cycle. To calculate, convert the
Gregorian date to its corresponding Heavenly Stem and Earthly Branch
combination, used for marking specific years, months, and days.

### What makes this a useful eval?

The existing GPT models tend to make errors when performing calculations
related to the Sexagenary Cycle. To address this issue, we have provided
a specialized dataset aimed at improving the model's accuracy in
handling Sexagenary Cycle calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

[2023-03-16 12:46:51,594] [record.py:320] Final report: {'accuracy':
0.65}. Logged to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl
[2023-03-16 12:46:51,594] [oaieval.py:211] Final report:
[2023-03-16 12:46:51,594] [oaieval.py:213] accuracy: 0.65
[2023-03-16 12:46:51,597] [record.py:309] Logged 60 rows of events to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl:
insert_time=2.463ms

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"甲戌的次日是？"}], "ideal": "乙亥"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"乙亥的次日是？"}], "ideal": "丙子"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬寅的后日是？"}], "ideal": "甲辰"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"癸卯的后日是？"}], "ideal": "乙巳"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬子的后日是？"}], "ideal": "甲寅"}
  ```
</details>

---------

Co-authored-by: dunedainstrider <dunedainstrider@mac16>

---
## [mysterious-progression/evals](https://github.com/mysterious-progression/evals)@[2ffd4b57de...](https://github.com/mysterious-progression/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Thursday 2023-05-25 14:21:20 by Andrew Kondrich

add more logging (#964)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [Milo123459/rust-analyzer](https://github.com/Milo123459/rust-analyzer)@[8ad70e7f99...](https://github.com/Milo123459/rust-analyzer/commit/8ad70e7f99b6a5eca65f6ef76cedee6c40132d6f)
#### Thursday 2023-05-25 14:39:53 by bors

Auto merge of #14866 - AndreasBackx:feature/doc-comments-markdown, r=Veykril

[editors/code] add markdown syntax highlighting to doc comments

_This is a continuation of https://github.com/microsoft/vscode/pull/169956 and https://github.com/dustypomerleau/rust-syntax/pull/37 (that repo is no longer maintained: https://github.com/dustypomerleau/rust-syntax/issues/39#issuecomment-1427339029). The VS Code team seemed to prefer this being inside of an extension._

This adds Markdown highlighting to doc comment lines and blocks. Currently it is thus regarded both as a comment and as Markdown which leads to normally foreground text being in the colour of the comment and the rest highlighted like Markdown or its own embedded languages in code blocks.

![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/c84f2e83-faea-47ca-853d-3728a07b2b66)

![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/f4191425-32cd-451c-ae3a-29a0970ce7a2)

Block comments are supported, but currently not when there is a `*` at the start of the line:
![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/ce3b58d5-9dca-4376-bffe-4f5a54acbe37)
![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/b73a5ee6-a178-4aef-a0e4-3d75e4e7d8e5)

I'm not entirely sure if I can easily fix this, I'd need to find a way to make the content ignore the `*`. Though I'm unsure if it's important as there are [conventions against using block comments](
https://rust-lang.github.io/rfcs/1574-more-api-documentation-conventions.html#use-line-comments) and using them without `*` does work. All of this TextMate grammar is so hard to find documentation on that _honestly_ I'd just not want to support this considering the effort.

Let me know what everyone thinks of this being in rust-analyzer. I've personally found it hard to write large amounts of Rust documentation due to the lack of Markdown syntax highlighting.

Also, thank you `@adenine-dev` as well for making this available in the interim and your enthousiasm. Wanted to get this PR out sooner, but life gets in the way.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[299960f8ad...](https://github.com/mrakgr/The-Spiral-Language/commit/299960f8ad949833bf7dc255634e98cb5de69a7c)
#### Thursday 2023-05-25 14:54:30 by Marko Grdinić

"6:50am. It irks me somewhat that I am not getting callbacks. What I am going to do when I am done with this projects is have ChatGPT make up personas.

The job posts ultimately say everything I need to get a job, and I can have the bot make up perfect resumes for the job at hand. That should get me the interview practice that I need.

6:55am. I do not want the matter of me getting a job to depend on fortune or skills. Ultimately, it should depend on my resolve.

But I do need some actual skills, so I might as well do it.

7:10am. Let me read Mahoako and chill a bit more and then I will start.

I need a realistic plan for getting a job.

Sure I need skills, but I also need interviews.

If people don't want me, what can I do, but become the ideal?

The world is really playing a mean trick on me right now. I won't forget this.

7:45am. Let's start.

Either way, no matter how things turn out, I need to focus on my webdev skills. Once I've achieved satisfaction, I can think about other things.

https://www.totaljobs.com/jobs/remote-c%23-blazor/in-europe?radius=10&searchOrigin=Resultlist_top-search

Nevermind this for now. Let me watch those vids from yesterday a bit and then I will start.

I got up really early today.

https://www.meziantou.net/how-to-use-event-preventdefault-in-blazor.htm

Oh, it is possible to nest these. Shit. Since it was complaining I thought that it wouldn't work.

https://github.com/dotnet/aspnetcore/issues/

I should keep issue 24932 in mind.

```js
window.myUtils = {
    addDefaultPreventingHandler: function (element, eventName) {
        element.addEventListener(eventName, e => e.preventDefault(), { passive: false });
    }
};
```

```cs
protected override async Task OnAfterRenderAsync(bool firstRender)
{
    if (firstRender)
        await jsRuntime.InvokeVoidAsync("myUtils.addDefaultPreventingHandler", myElementReference, "wheel");
}
```

I should keep these snippets in mind.

For some reason the @onwheel event is not being triggered at all, but let's leave that aside.

https://youtu.be/bZdYpYQb958?t=926

What is this Blazor Hybrid thing?

https://youtu.be/bZdYpYQb958?t=979

What the hell is Tizen?

> Tizen is a Linux-based mobile operating system backed by the Linux Foundation, developed and used primarily by Samsung Electronics. The project was originally conceived as an HTML5-based platform for mobile devices to succeed MeeGo.

Ok, thank you Google.

https://youtu.be/bZdYpYQb958?t=1146
> With .NET 7 we got something called Web Components.

Ok, this talk is informative. I might as well watch it all the way.

Then I will start the screencast.

https://youtu.be/bZdYpYQb958?t=1397
> Razor or Code Behind?

What's code behind?

https://medium.com/stories-by-progress/using-a-code-behind-approach-to-blazor-components-da6525f576cc

Oh, I see. You aren't actually getting rid of the html.

https://youtu.be/bZdYpYQb958?t=1542

A lot of component libraries are here.

https://youtu.be/bZdYpYQb958?t=1998
> Full Server Capabilities.

I am really wondering how I could get to databases with WASM.

https://youtu.be/bZdYpYQb958?t=2256

Heh.

https://youtu.be/bZdYpYQb958?t=2613
> So Facebook has 16mb of Javascript.

Lol, really?

https://youtu.be/bZdYpYQb958?t=3184

This virtualization capability would have been a godsend in the leduc project for showing only the visible data.

9:05am. https://www.totaljobs.com/jobs/remote-c%23-blazor/in-europe?radius=10&searchOrigin=Resultlist_top-search

I did a search for Blazor jobs earlier, so if I get up to speed with this, it isn't like I am going to get left behind.

Let's go forward with this.

10:05am. https://blog.antosubash.com/posts/state-management-blazor-fluxor

Hmmmm...this C# is pretty nasty, but in F# it would look quite good.

https://github.com/mrpmorris/Fluxor/tree/master/Source/Tutorials/01-BasicConcepts/01A-StateActionsReducersTutorial

This is an interesting library. Forget the F# specific stuff. Embrace dependency injection.

10:30am.

///

Let's slowly get started with today's session.
The last two days it were arduous with setting things up and getting up to speed with Blazor, but now we should be on the smooth part.
Today we'll finally work on the compilation nodes.
We got up early and had some time to think about it.
Now that things are easy on us, we'll just pack the compilation output into the compilation node itself.
No need to be too fancy.
What we'll do is very simple.
From the compilation node, we'll go outwards and collect all the data in lexicographic order in an array.
Since the graph can contain cycles and sharing, we'll have to account for that.
We'll deal with making the compilation node first and then do the compilation step.
Before we let the music take over, we just wanted to say a few words about the Leduc project that we've been working on in the previous videos.
It kind of ended up on a sour note, as we lost interest in deploying it as a container app, thanks to all the head butting versus the bindings.
This morning we thought about it, and realized that for an app like it, the ideal for would be to compile it to web assemly in Blazor and run it all on the browser.
The form we had where the server was responsible for the training is definitely not the ideal we should be striving for.
But at the same time, we couldn't have just plowed everything into the browser since the game did use bitwise intrinsics on 64-bit integers in places, for card selection for example, and the browser only supports floats.
With wasm we could have perfect code sharing, and not have to change the game logic itself to fit the browser.
We'd just have to redo the UI in Blazor.
We are deeply regretful that we didn't start off this way.
We are idiots. We said to ourselves: we want to be webdevs, so that means getting closer to javascript, not meme web assembly tech.
But wasm is growing, and it is in fact the technology that would let us program in our preferred style with the least amount of hassle.
So we spent almost 4 months exploring.
A lot of that time will turn out to have been wasted.

We can't make a correct strategic decision to save our life, but at least we are learning.
We don't really dislike Typescript itself, but the way we've seen Javascript devs use it is pretty disgusting.
We learned that much from our brief foray into it.
Admittedly, with the Leduc project, we did have ambitions of using it as a template for an application, where the user could use some a online GPU service to train neural agents, which is why we were exploring the Fable websocket libraries, and lastly SignalR, but if we really wanted that, there would have been better ways of going about it.
The Leduc project as it is now can't even serve as a good portfolio piece, so later we'll show how to convert it to Blazor, and we'll publish it as a container app.
Because after we do that, the training would be done on the client, we won't have to worry about the server being hammered by the agent training.
The server could just serve static files.
Right now, we are feeling really grateful. If it wasn't for Blazor we'd be programming React and Typescript, and that would have been horrible.
We can only specialize in so many things in life, and the way to gain true skill and power is to focus.
Because of F# we are solidly on the functional programming path, and for better or worse, with .NET.
We just need a bit more, and we will consummate this marriage.

///

Once again this is too big and I need to break it up.

1:10pm. Done with breakfast. Let me chill a bit and then I will resume.

I need to do the ports next rather than jumping into the compilation stage.

1:40pm. Let me start.

2:30pm. I am doing some styling to get the layout sizes right.

https://youtu.be/veEqYQlfNx8
The problems with viewport units

https://youtu.be/veEqYQlfNx8?t=542

Ah, viewport units can mess with zoom!

I see...

3:25pm. Finally, opened a project on the F# side and brought in the types.

4:15pm. I need a break, I am really tired right now.

More than usual, but that is no wonder since I have been up since before 7am. Usually I get up past 9 and have more steam.

4:25pm. Yeah, I know the usual rules state till 6pm, but I really don't feel fresh right now.

4:50pm.

///

Let's take a break here to review. We've been programming since uncharacteristically early today and are tired by now.
We finally managed to bring back F#, so now this video deserves its place on the F# playlist.
We implemented that last condition that the inputs can have only one link, but we think we are going to get rid of it.
Visual novels can have branches so it might be good to have merging behavior in text nodes.
It would also make it easier to demonstrate why we need memoization for the graph traversal.
So we'll go with that decision, and comment out the condition, but we'll keep the code around for later.
We'll likely need it.
I'll let you in on a little secret, even though this is a VN compiler for now, master has his sights set high.
He is pretty envious of the comfy anon, so who knows what kinds of crazy nodes we might have in the future.
He picked a simple goal that can do something useful and inline with his own interests to start him off, but this project has the potential for long term cultivation into a visual programming language in its own right.
We can only hope he won't be wrong again, and we won't have the next 10 years dominated by Stable Diffusion.
With web development we should be going in the right direction, right?

///

I can't go on anymore. I am too tired.

The video is 10m long at this point, so it would be good to stop here.

Let me close."

---
## [Liberty-Landing/Liberty-Station-13](https://github.com/Liberty-Landing/Liberty-Station-13)@[0f74820c9d...](https://github.com/Liberty-Landing/Liberty-Station-13/commit/0f74820c9d04762ac5b06907e6eb5207be80f136)
#### Thursday 2023-05-25 15:06:37 by ThePainkiller

Fixes upon fixes and more

- Fixes exploit on medical fabricator that allowed it to take any disk
- Consequently, fixes general autolathe's capacity to receive medical disks as was... intended?
- Comments out cartographer's seal and pyramid anomalies
- Bruise packs and the like should now cost their exact amount of materials (and chemicals) to print, no longer accruing massive costs
- New: Gate floodlights, they're static, fixed, brighter, and can't have their cells taken out (they come with a large posi). To illuminate the fence at night. TODO: Make them create a directional light spot like flashlights
- Wallets can now take syrettes
- Bone gel now made out of biomatter
- Fixes extant references to Lonestar on the vault's gold shovel
- Adds and renames missing stamps to heads of staff offices
- New functionality: CTRL SHIFT clicking a PDA ejects its pen
- New functionality: Alt clicking a dropper selects transfer amount
- Ammo kits (and the crafting table) can now make caseless ammo
- Fixes Ugil's mag overlay issue
- Changes up many, many weapon's firing sounds to be more fitting
- Fixes self heating coffee doing eating sounds
- Adds quality of life sounds to MRE-like foods, when opened, heated up, and finished heating
- Beautification of the Custodians of the Bonfire's Stronghold, removing references to church, new areas as well
- Changed the lift's walls' names from the mines from "The Rocinante" to "Elevator" proper
- Many musical instruments and loot added to the map
- Bar now has a piano!

---
## [openai/evals](https://github.com/openai/evals)@[da73bb5f07...](https://github.com/openai/evals/commit/da73bb5f071c31c3dd571989f057b8e36d3a9334)
#### Thursday 2023-05-25 15:27:48 by mysterious-progression

Detect highly sensitive human data (#852)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Detecting highly sensitive human data
### Eval description
This eval tests whether models can successfully detect possible highly
sensitive human data without returning false positives on values that
cannot exist in practice. There are many types of highly sensitive human
data but some of the most common and types are but not limited to social
security numbers, passport numbers, credit card numbers, and driver's
licenses. Not all values are valid for a given type. For example, credit
card numbers have a numbering system specified by
https://www.iso.org/standard/39698.html, and use check digits to
validate.

Similarly, passport numbers must comply with the ICAO D9303
https://www.icao.int/publications/documents/9303_p4_cons_en.pdf
<img width="1273" alt="Screenshot 2023-04-27 at 11 01 23 PM"
src="https://user-images.githubusercontent.com/45504048/235056158-3f0eb640-109e-47c5-a64c-554d6d55f708.png">


### What makes this a useful eval?
Institutions spend millions of dollars trying to detect non-encrypted
HSHD in their internal datasets. A combination of regex, ML, and
hard-coded logic is often used yielding complicated, hard to maintain
codebases. The risk associated with plaintext HSHD is high and certain
institutions can be subject to heavy fines if HSHD is leaked if not
properly stored.


## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
[evals).](url)

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value
This eval combines many aspects of language processing and
understanding. The task involves understanding what HSHD are, domain
knowledge about what makes them valid, and algorithmic understanding in
order to validate (i.e. check digits)

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Detect whether Passport number
is present in the text. Any potential Passport number that cannot be
valid should not be returned. If valid Passport number is found return
it's value, otherwise return '\"None\""}, {"role": "user", "content":
"Passenger with passport number: 11111111111111 is booked for a
flight"}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether a SSN is
present in the text. Any potential SSN that cannot be valid should not
be returned. If valid SSN is found return it's value, otherwise return
\"None\""}, {"role": "user", "content": "Bob has an SSN of
123-45-6789"}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether a SSN is
present in the text. Any potential SSN that cannot be valid should not
be returned. If valid SSN is found return it's value, otherwise return
\"None\""}, {"role": "user", "content": "The Jane's husban's social
security number is: 331-71-1232"}], "ideal": "331-71-1232"}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "Lemmiwinks
charged his brother Wikileaks on his CC:4193523869738880, $400"}],
"ideal": "4193523869738880"}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Visa card ending in
1738481092549663."}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Master card ending in
1738-4810-9254-9663."}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Discover card ending in
1738-4810-9254-9665."}], "ideal": "1738-4810-9254-9665"}
{"input": [{"role": "system", "content": "Detect whether passport number
is present in the text. Any potential passport number that cannot be
valid should not be returned. If valid passport number is found return
it's value, otherwise return \"None\""}, {"role": "user", "content":
"Passenger with passport number: 1*****1 is booked for a flight"}],
"ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether passport number
is present in the text. Any potential passport number that cannot be
valid should not be returned. If valid passport number is found return
it's value, otherwise return \"None\""}, {"role": "user", "content":
"Passenger with passport number: (*) is booked for a flight"}], "ideal":
"\"None\""}
  ```
</details>

---
## [AdvJava-22-23/FinalMedineSubsitutes](https://github.com/AdvJava-22-23/FinalMedineSubsitutes)@[89733c801d...](https://github.com/AdvJava-22-23/FinalMedineSubsitutes/commit/89733c801da222240174475d3c83d107181673fe)
#### Thursday 2023-05-25 15:33:03 by Jay

All branches are now merged together and for now this is my completed final thank you for an Amazing year and everything you've done for your student's you truly are a stellar example of how a teacher can impact a student for the rest of their life.

---
## [palao/portage](https://github.com/palao/portage)@[28cd240fb2...](https://github.com/palao/portage/commit/28cd240fb23d880b8641a058831c6762db71c3e2)
#### Thursday 2023-05-25 15:53:37 by Sam James

emerge-webrsync: support PGP verification via gemato

Introduce PGP verification of the webrsync snapshot tarballs
using app-portage/gemato - which is already a dependency of Portage
for verifying normal rsync.

This is the same method Portage uses (see below).

Technical changes before we dive into the rationale:
- Use gemato for PGP verification just like Portage does for
  sync-type=webrsync, sync-type=rsync (although that uses a metamanifest),
  and sync-type=git (although that uses gemato for gpg-wrap, so works differently).

- Use gentoo-functions automagically if available for better output
  functions.

- Be more verbose about verification and various other operations,
  while also respecting --quiet if passed for misc. existing & new
  messages.

- Make --verbose a no-op. There weren't enough output messages
  to justify three states (--quiet, normal, --verbose).

- Bail out more aggressively in the event of errors or "warnings".

- Use modern terminology for repository, etc (avoid overloading the
  "portage" term.)

- Allow disabling PGP verification with --no-pgp-verify.

Technically, the fix is very straightforward, but getting to
the fix was the slightly painful bit. What I've concluded
happened is:
- Portage starts getting reworked to gain proper sync module support;

- Someone gets the idea of implementing emerge-webrsync fully in Python
  as a Portage sync module (which is a not-unreasonable idea);

  [This ultimately hasn't gone anywhere, and in fact, while working on this
  bug, I ended up finding a bunch of typos that meant you couldn't even test it.
  But it's a stub anyway.]

- The idea of deprecating emerge-webrsync is floated around. The idea
  being Portage should call it via its new sync module with sync-type=webrsync.

  This is presumably with the ultimate goal of it transparently one day
  using the aforementioned (yet-non-existent) Python implementation as its
  backend, and not the shell script.

  [To this day, Portage's webrsync implementation shells out to the emerge-webrsync
  shell script, but it has the abstraction to switch that out, in theory.]

- At the time, PGP verification in general of the Gentoo
  repository is an active topic, especially now we'd migrated to git which makes
  it way easier, unlike CVS.

- A bug is filed for PGP verification in emerge-webrsync.

  People decide it doesn't matter too much, because Portage is going to
  Real Soon Now (TM) have its own backend (replacing the shell script) and/or
  Portage's sync module support obsoletes emerge-webrsync entirely.

  The idea here, I think, being that nobody should call emerge-webrsync and
  everyone should just call emerge (or emaint) to sync as appropriate.

  [This isn't a terrible idea in a sense, but it needs a better basis:
  we should probably make emerge-webrsync a wrapper which creates a temporary
  repo config to forcefully webrsync a repository if the user asks us to. This
  is what people expect from emerge-webrsync with the default sync-type=rsync
  in repos.conf for ::gentoo.

  I actually started implementing this before I realised that emerge was
  shelling out to emerge-webrsync, so have postponed it.]

- Then nothing happens with the "replacement" ideas and the good
  ol' trusty emerge-webrsync ends up with the same problems sitting
  there because nobody saw the point in working on it if it was to
  be replaced soon. But that didn't happen.

The fix overall for this is pretty small, but the commit is larger
than I'd like because I had to rework a few things to sensibly allow
disabling PGP verification as well as follow the flow.

(I did start splitting up this commit but ultimately it needs -w
for best review even without the output tweaks in this commit and
deconstructing this for atomic commits would end up being more brittle
as I couldn't be as confident in the result.)

Bug: https://bugs.gentoo.org/597800
Signed-off-by: Sam James <sam@gentoo.org>

---
## [EspressoSystems/jellyfish](https://github.com/EspressoSystems/jellyfish)@[a81387790a...](https://github.com/EspressoSystems/jellyfish/commit/a81387790ad9a91706a615a4a77a5bb15591a5ac)
#### Thursday 2023-05-25 16:18:44 by Gus Gutoski

make `bytes_from_field_elements` infallible with paranoid checks for overflow (#250)

* impl Error for PCSError

* use anyhow for bytes_from_field_elements error type

* make bytes_from_field_elements infallible

* appease clippy (you're welcome)

* tidy an ugly line

* better test

* check everything for overflow, better panic messages

* remove commented code (oops)

---
## [kangaroo/linux-lpi4a](https://github.com/kangaroo/linux-lpi4a)@[81429eb8d9...](https://github.com/kangaroo/linux-lpi4a/commit/81429eb8d9ca40b0c65bb739d29fa856c5d5e958)
#### Thursday 2023-05-25 16:50:40 by Linus Torvalds

Merge tag 'arm64-fixes' of git://git.kernel.org/pub/scm/linux/kernel/git/arm64/linux

Pull arm64 fix from Will Deacon:
 "Ensure PAN is re-enabled following user fault in uaccess routines.

  After I thought we were done for 5.4, we had a report this week of a
  nasty issue that has been shown to leak data between different user
  address spaces thanks to corruption of entries in the TLB. In
  hindsight, we should have spotted this in review when the PAN code was
  merged back in v4.3, but hindsight is 20/20 and I'm trying not to beat
  myself up too much about it despite being fairly miserable.

  Anyway, the fix is "obvious" but the actual failure is more more
  subtle, and is described in the commit message. I've included a fairly
  mechanical follow-up patch here as well, which moves this checking out
  into the C wrappers which is what we do for {get,put}_user() already
  and allows us to remove these bloody assembly macros entirely. The
  patches have passed kernelci [1] [2] [3] and CKI [4] tests over night,
  as well as some targetted testing [5] for this particular issue.

  The first patch is tagged for stable and should be applied to 4.14,
  4.19 and 5.3. I have separate backports for 4.4 and 4.9, which I'll
  send out once this has landed in your tree (although the original
  patch applies cleanly, it won't build for those two trees).

  Thanks to Pavel Tatashin for reporting this and Mark Rutland for
  helping to diagnose the issue and review/test the solution"

* tag 'arm64-fixes' of git://git.kernel.org/pub/scm/linux/kernel/git/arm64/linux:
  arm64: uaccess: Remove uaccess_*_not_uao asm macros
  arm64: uaccess: Ensure PAN is re-enabled after unhandled uaccess fault

---
## [kangaroo/linux-lpi4a](https://github.com/kangaroo/linux-lpi4a)@[6aee4badd8...](https://github.com/kangaroo/linux-lpi4a/commit/6aee4badd8126f3a2b6d31c5e2db2439d316374f)
#### Thursday 2023-05-25 16:51:17 by Linus Torvalds

Merge branch 'work.openat2' of git://git.kernel.org/pub/scm/linux/kernel/git/viro/vfs

Pull openat2 support from Al Viro:
 "This is the openat2() series from Aleksa Sarai.

  I'm afraid that the rest of namei stuff will have to wait - it got
  zero review the last time I'd posted #work.namei, and there had been a
  leak in the posted series I'd caught only last weekend. I was going to
  repost it on Monday, but the window opened and the odds of getting any
  review during that... Oh, well.

  Anyway, openat2 part should be ready; that _did_ get sane amount of
  review and public testing, so here it comes"

From Aleksa's description of the series:
 "For a very long time, extending openat(2) with new features has been
  incredibly frustrating. This stems from the fact that openat(2) is
  possibly the most famous counter-example to the mantra "don't silently
  accept garbage from userspace" -- it doesn't check whether unknown
  flags are present[1].

  This means that (generally) the addition of new flags to openat(2) has
  been fraught with backwards-compatibility issues (O_TMPFILE has to be
  defined as __O_TMPFILE|O_DIRECTORY|[O_RDWR or O_WRONLY] to ensure old
  kernels gave errors, since it's insecure to silently ignore the
  flag[2]). All new security-related flags therefore have a tough road
  to being added to openat(2).

  Furthermore, the need for some sort of control over VFS's path
  resolution (to avoid malicious paths resulting in inadvertent
  breakouts) has been a very long-standing desire of many userspace
  applications.

  This patchset is a revival of Al Viro's old AT_NO_JUMPS[3] patchset
  (which was a variant of David Drysdale's O_BENEATH patchset[4] which
  was a spin-off of the Capsicum project[5]) with a few additions and
  changes made based on the previous discussion within [6] as well as
  others I felt were useful.

  In line with the conclusions of the original discussion of
  AT_NO_JUMPS, the flag has been split up into separate flags. However,
  instead of being an openat(2) flag it is provided through a new
  syscall openat2(2) which provides several other improvements to the
  openat(2) interface (see the patch description for more details). The
  following new LOOKUP_* flags are added:

  LOOKUP_NO_XDEV:

     Blocks all mountpoint crossings (upwards, downwards, or through
     absolute links). Absolute pathnames alone in openat(2) do not
     trigger this. Magic-link traversal which implies a vfsmount jump is
     also blocked (though magic-link jumps on the same vfsmount are
     permitted).

  LOOKUP_NO_MAGICLINKS:

     Blocks resolution through /proc/$pid/fd-style links. This is done
     by blocking the usage of nd_jump_link() during resolution in a
     filesystem. The term "magic-links" is used to match with the only
     reference to these links in Documentation/, but I'm happy to change
     the name.

     It should be noted that this is different to the scope of
     ~LOOKUP_FOLLOW in that it applies to all path components. However,
     you can do openat2(NO_FOLLOW|NO_MAGICLINKS) on a magic-link and it
     will *not* fail (assuming that no parent component was a
     magic-link), and you will have an fd for the magic-link.

     In order to correctly detect magic-links, the introduction of a new
     LOOKUP_MAGICLINK_JUMPED state flag was required.

  LOOKUP_BENEATH:

     Disallows escapes to outside the starting dirfd's
     tree, using techniques such as ".." or absolute links. Absolute
     paths in openat(2) are also disallowed.

     Conceptually this flag is to ensure you "stay below" a certain
     point in the filesystem tree -- but this requires some additional
     to protect against various races that would allow escape using
     "..".

     Currently LOOKUP_BENEATH implies LOOKUP_NO_MAGICLINKS, because it
     can trivially beam you around the filesystem (breaking the
     protection). In future, there might be similar safety checks done
     as in LOOKUP_IN_ROOT, but that requires more discussion.

  In addition, two new flags are added that expand on the above ideas:

  LOOKUP_NO_SYMLINKS:

     Does what it says on the tin. No symlink resolution is allowed at
     all, including magic-links. Just as with LOOKUP_NO_MAGICLINKS this
     can still be used with NOFOLLOW to open an fd for the symlink as
     long as no parent path had a symlink component.

  LOOKUP_IN_ROOT:

     This is an extension of LOOKUP_BENEATH that, rather than blocking
     attempts to move past the root, forces all such movements to be
     scoped to the starting point. This provides chroot(2)-like
     protection but without the cost of a chroot(2) for each filesystem
     operation, as well as being safe against race attacks that
     chroot(2) is not.

     If a race is detected (as with LOOKUP_BENEATH) then an error is
     generated, and similar to LOOKUP_BENEATH it is not permitted to
     cross magic-links with LOOKUP_IN_ROOT.

     The primary need for this is from container runtimes, which
     currently need to do symlink scoping in userspace[7] when opening
     paths in a potentially malicious container.

     There is a long list of CVEs that could have bene mitigated by
     having RESOLVE_THIS_ROOT (such as CVE-2017-1002101,
     CVE-2017-1002102, CVE-2018-15664, and CVE-2019-5736, just to name a
     few).

  In order to make all of the above more usable, I'm working on
  libpathrs[8] which is a C-friendly library for safe path resolution.
  It features a userspace-emulated backend if the kernel doesn't support
  openat2(2). Hopefully we can get userspace to switch to using it, and
  thus get openat2(2) support for free once it's ready.

  Future work would include implementing things like
  RESOLVE_NO_AUTOMOUNT and possibly a RESOLVE_NO_REMOTE (to allow
  programs to be sure they don't hit DoSes though stale NFS handles)"

* 'work.openat2' of git://git.kernel.org/pub/scm/linux/kernel/git/viro/vfs:
  Documentation: path-lookup: include new LOOKUP flags
  selftests: add openat2(2) selftests
  open: introduce openat2(2) syscall
  namei: LOOKUP_{IN_ROOT,BENEATH}: permit limited ".." resolution
  namei: LOOKUP_IN_ROOT: chroot-like scoped resolution
  namei: LOOKUP_BENEATH: O_BENEATH-like scoped resolution
  namei: LOOKUP_NO_XDEV: block mountpoint crossing
  namei: LOOKUP_NO_MAGICLINKS: block magic-link resolution
  namei: LOOKUP_NO_SYMLINKS: block symlink resolution
  namei: allow set_root() to produce errors
  namei: allow nd_jump_link() to produce errors
  nsfs: clean-up ns_get_path() signature to return int
  namei: only return -ECHILD from follow_dotdot_rcu()

---
## [Koushikdey2003/android_frameworks_base](https://github.com/Koushikdey2003/android_frameworks_base)@[4ae2e1a9b1...](https://github.com/Koushikdey2003/android_frameworks_base/commit/4ae2e1a9b10ee575f4c9086659504b85174d448c)
#### Thursday 2023-05-25 17:23:46 by Koushik Dey

fuck you

Signed-off-by: Koushik Dey <kousickdey3@gmail.com>

---
## [whiteinge/dotfiles](https://github.com/whiteinge/dotfiles)@[6800b9e2ec...](https://github.com/whiteinge/dotfiles/commit/6800b9e2ecad00d3152599b9245232fafd43ca4a)
#### Thursday 2023-05-25 17:43:26 by Seth House

Add/remove various Zsh options

auto_cd is sometimes nice for typos but doesn't come up enough to
matter.

extended_glob I just don't make use of.

inc_append_history is redundant with share_history. Docs specify you
should use one or the other. If there's a side-effect I haven't seen it
in many years of using both but I'll keep an eye out with this change.

mark_dirs with this enabled `ls -F foo*` will produce duplicate trailing
slashes which looks annoying. I'm honestly not sure if I use this option
so disabling to see if I notice.

path_dirs probably seemed like a good idea when I first added it, but
it's better to be explicit instead.

pushd_ignore_dups because I'm interested to quickly jump back to
a previous location and don't need to retain an exact history of my
directory changes.

---
## [HeroRobb/godot-psx-starter-project](https://github.com/HeroRobb/godot-psx-starter-project)@[0ee3d8c121...](https://github.com/HeroRobb/godot-psx-starter-project/commit/0ee3d8c1219644f9ad4139a3ce2f492d1d74b9fb)
#### Thursday 2023-05-25 17:48:50 by HeroRobb

fixed a horrible fucking mistake

I don't know how I possibly did it but I pushed a personal project to this repo. God that was horrible.

---
## [theacademy/C-352-Excercises](https://github.com/theacademy/C-352-Excercises)@[572bf60475...](https://github.com/theacademy/C-352-Excercises/commit/572bf60475b51443975683dd1c21d5e439993993)
#### Thursday 2023-05-25 17:59:20 by spunkymandar

Add files via upload

Overview
The goal of this mastery project is to create an application that can read and write flooring orders for Wiley Edge Corp.

Your complete application must demonstrate your understanding of all the topics covered in the prior sections, including:

N-tier/MVC architecture, including the use of a service layer
Interfaces
Spring dependency Injection
Unit Testing
We have covered all of the technical skills needed to complete this assignment. It is your job to think critically about this project, ask clarifying questions where requirements and features are not clear, and come up with a solid design and game plan before you begin coding. It is essential to your success that you don't just "throw code" at the problem and hope that something sticks. We want you to use the background skills and techniques covered so far to synthesize a solution to this problem.

Submitting Your Work
You will submit your work in two stages.

Step 1
Before starting to code, plan out the program using a flowchart and class diagrams.

The flowchart should describe the individual steps the program must complete, including any loops and conditional outputs.
The class diagrams should describe the classes you intend to use in the program.
Once you have finished this documentation, submit your files to the Flowcharts and Class Diagrams assessment in Engage. An instructor will review your submission.

If the plan is acceptable, you may start to code.
If there are problems, the instructor will work with you to improve the plan before you start to code.
Step 2
Write code that meets the requirements explained below. After completing the assessment and verifying that it meets the stated requirements, you must submit your work using both GitHub and Engage.

GitHub Classroom
Your instructor will create an invitation for the assignment in GitHub Classroom.

All code you want to submit should be pushed to the GitHub Classroom repository for this assessment.
Submit a Pull Request to your instructor from GitHub Classroom.
Engage
After submitting the Pull Request, copy the URL for your repository in GitHub.
Return to this page and scroll to the bottom of the page.
Click the Add submission button.
A submission textbox will open. Paste the GitHub URL into the box.
Click the Save changes button.
⚠ Failure to submit the URL to Engage may result in receiving no credit for the assessment. ⚠

After submitting your work to Engage, you will receive a submission confirmation from Engage. You can also reopen this page, scroll to the bottom, and check for the submission time stamp and the URL you submitted.

After submitting the assignment, your instructor will evaluate your code and schedule a code review to go through the code with you. Be prepared to answer questions about your code and thought processes when you complete the code review.

Architectural Guidance
Use N-tier development and MVC principles in structuring code to handle products, taxes, and orders appropriately. Your application should follow the MVC pattern presented in the course.
Use unit tests and integration tests to ensure that your application's data layers and business logic (service layer) code is covered.
Rules of Flooring Mastery
We are using an enterprise MVC architecture for this project, so your code must be organized into reasonable classes. You will draw a UML class diagram and a high-level flowchart before proceeding with writing code.

For an enterprise architecture, the code must have layers:

The model package may only contain classes that have data members (properties).
The dao package contains classes that are responsible for persisting data.
The controller package contains classes that orchestrate the program.
The view package contains classes that interact with the user.
The servicepackage contains the service layer components.
The UserIO class (along with the view component) will handle all console IO for the user.
Build this application following the process outlined in the Agile Approach Checklist for Console Applications

Requirements
Sample Data Files: SampleFileData.zip

The application will use three separate file formats for information.

Orders Files & Format
All orders are stored within an Orders folder. A new order file is created for each sales day. The file name is guaranteed to be unique for that day because the date is part of the file name. When creating new order files the file name should be in this format: Orders_MMDDYYYY.txt.

With this format, the order file for August 21st, 2025 would be named Orders_08212025.txt.

The order file should contain a header row. Data rows will contain the following fields and should be in this order:

OrderNumber – Integer
CustomerName – String
State – String
TaxRate – BigDecimal
ProductType – String
Area – BigDecimal
CostPerSquareFoot – BigDecimal
LaborCostPerSquareFoot – BigDecimal
MaterialCost – BigDecimal
LaborCost – BigDecimal
Tax – BigDecimal
Total – BigDecimal
Here is a sample line from an orders file:

1,Ada Lovelace,CA,25.00,Tile,249.00,3.50,4.15,871.50,1033.35,476.21,2381.06
  
Orders_06012013.txt is a sample file which is included in the sample download above.

Some of the order fields are calculations:

MaterialCost = (Area * CostPerSquareFoot)

LaborCost = (Area * LaborCostPerSquareFoot)

Tax = (MaterialCost + LaborCost) * (TaxRate/100)

Tax rates are stored as whole numbers
Total = (MaterialCost + LaborCost + Tax)

Tax File & Format
The tax information can be found in Data/Taxes.txt. This file will contain the following fields:

StateAbbreviation – String
StateName – String
TaxRate – BigDecimal
Here is a sample line from the taxes file:

TX,Texas,4.45
  
Products File & Format
The current product information can be found in Data/Products.txt. It contains the following fields:

ProductType – String
CostPerSquareFoot – BigDecimal
LaborCostPerSquareFoot – BigDecimal
Here is a sample line from the products file:

Tile,3.50,4.15
  
User Stories
The UI should start with a menu to prompt the user for what they would like to do:

  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
  * <<Flooring Program>>
  * 1. Display Orders
  * 2. Add an Order
  * 3. Edit an Order
  * 4. Remove an Order
  * 5. Export All Data
  * 6. Quit
  *
  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
  
Display Orders
Display orders will ask the user for a date and then display the orders for that date. If no orders exist for that date, it will display an error message and return the user to the main menu.

Add an Order
To add an order will query the user for each piece of order data necessary:

Order Date – Must be in the future
Customer Name – May not be blank and is limited to characters [a-z][0-9] as well as periods and comma characters. "Acme, Inc." is a valid name.
State – Entered states must be checked against the tax file. If the state does not exist in the tax file, we cannot sell there. If the tax file is modified to include the state, it should be allowed without changing the application code.
Product Type – Show a list of available products and pricing information to choose from. Again, if a product is added to the file it should show up in the application without a code change.
Area – The area must be a positive decimal. Minimum order size is 100 sq ft.
The remaining fields are calculated from the user entry and the tax/product information in the files. Show a summary of the order once the calculations are completed and prompt the user as to whether they want to place the order (Y/N). If yes, the data will be added to in-memory storage. If no, simply return to the main menu.

The system should generate an order number for the user based on the next available order # (so if there are two orders and the max order number is 4, the next order number should be 5).

Edit an Order
Edit will ask the user for a date and order number. If the order exists for that date, it will ask the user for each piece of order data but display the existing data. If the user enters something new, it will replace that data; if the user hits Enter without entering data, it will leave the existing data in place. For example:

Enter customer name (Ada Lovelace):
  
If the user enters a new name, the name will replace Ada Lovelace. If the user hits enter without entering any data, it will leave the data as-is.

Only certain data is allowed to be changed:

CustomerName
State
ProductType
Area
If the state, product type, or area are changed, the order will need to be recalculated. Order date may not be changed!

After querying for each editable field display a summary of the new order information and prompt for whether the edit should be saved. If yes, replace the data in the file then return to the main menu. If no, do not save and return to the main menu.

Remove an Order
For removing an order, the system should ask for the date and order number. If it exists, the system should display the order information and prompt the user if they are sure. If yes, it should be removed from the list.

Export All Data
When the user selects this option, the system should export all existing data to a file that exists independently of the application itself.

Quit
On quit, exit the application.

Stretch Goal: Export Data
This step is optional. Complete this step only after all other steps work as required.

Selecting this option should save all active orders files to a file called DataExport.txt within a Backup folder. Exporting the order data multiple times should overwrite the data within the file with the latest active order information. However, unlike other order files, an order's line item in this DataExport file should also include the date in MM-DD-YYYY format, and the file's header should reflect this addition.

For example, here is a line of an example export, showcasing an order on June 12th, 2013:

1,Ada Lovelace,CA,25.00,Tile,249.00,3.50,4.15,871.50,1033.35,476.21,2381.06,06-12-2013
  
Additional Guidance
Any time a user enters invalid data, the system should ask them again until they enter valid data. A user should not be able to crash the application with invalid data.
We are using a layered architecture for this project. Thus your code must be organized into reasonable well-named classes and split into correct packages.
Please submit your project plan in addition to your code. This can be flowcharts, outlines, pseudocode, or any other documentation and planning technique.
You must unit test your DAO and ServiceLayers.
Some Tips
Build this application following the process outlined in the Agile Approach Checklist for Console Applications (as specified in the Rules of Flooring Mastery section above). This process will help you approach the project in a logical and orderly manner.
If you get stuck, ask an instructor for general guidance on what you should be looking for. The instructor will not write the code for you, but advice is always free.
There are places where this specification has been left open to interpretation: this is intentional. When on the job you will frequently have to ask clarifying questions to business stakeholders. Be sure to ask an instructor for general guidance on any features you do not understand.
Try to work on pieces of functionality in isolation and test them before moving on. Working on too large of a chunk at once leads to difficulties in troubleshooting and poor separation of concerns.
Think, then code. If you do not have a plan for each workflow, you will not be able to complete this project.
Use prior code samples and assessments as inspiration for this project. At this point in the course, you should be aware that there are patterns for creating a layered data-driven application.

---
## [w1atrak/Voice-controlled-Chess](https://github.com/w1atrak/Voice-controlled-Chess)@[52fb8f538f...](https://github.com/w1atrak/Voice-controlled-Chess/commit/52fb8f538f8d500b32123a076ce0d8e108e1cde0)
#### Thursday 2023-05-25 18:37:55 by Filip Jastrzębski

"SIMPLE AI" XDD

YES, PROGRAMMING IS A JOKE
YES, MY LIFE IS A JOKE
AND YES, THIS IS NOT EVEN FUNNY ANYMORE
<3

---
## [openai/evals](https://github.com/openai/evals)@[2167c99864...](https://github.com/openai/evals/commit/2167c998643af0de952e1cceaf346d7b99d49104)
#### Thursday 2023-05-25 19:00:08 by Jeff Kile

Identify which scale mode a series of notes belongs to (#860)

Added evals to determine the scale mode name based off the nodes in the
scale

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
music_theory_scale_modes

### Eval description
Test the model's ability to identify which western music scale a series
of 7 notes belongs to

### What makes this a useful eval?

This is good for analyzing music or getting help with music theory
problems like figuring out which scale to use to solo over a series of
chords, or which scale to use to write a melody depending on the mood or
chord selection.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

GPT-4 often hallucinates on these and will give a confident incorrect
answer

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G# A# B C# D# E?"}],"ideal":["E Lydian"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G# A B C# D E?"}],"ideal":["E Mixolydian","E Dominant"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G A B C D E?"}],"ideal":["E Aeolian","E Minor"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F G A A# C D E?"}],"ideal":["E Locrian"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: F G A A# C D E F?"}],"ideal":["F Ionian","F Major"]}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[4c0485bb3b...](https://github.com/openai/evals/commit/4c0485bb3b67cc0e4f8962e023975b84b6d1d2b8)
#### Thursday 2023-05-25 19:00:52 by qrdlgit

Eval: more multi-step math word problems (#877)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
multistep-word-problems

### Eval description

These are complex multi step math word problems.   

### What makes this a useful eval?

I noticed in the original algebra word problems
(https://github.com/openai/evals/pull/36) only a very few problems (6)
were added, so I thought I might do a few more for broader coverage. I
tried to cover every math subject one might encounter in high school.

I crafted the problems carefully to ensure that someone fairly
proficient at math could do them all in their head without having to
write anything down. I believe I mostly succeeded, though one or two
might come off as challenging depending on your skillset / math tricks
that you may or might not know.

You can see a sort of answer key here which has a few more details for
each question - https://github.com/qrdlgit/misc/blob/main/worksheet.md

[Insert why this eval is worth including and any additional context]


## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "Sarah has 23 apples, and she
wants to divide them among her 5 friends such that each will get an
equal amount of apples and she gets to keep twice as many as she hands
out to each friend. How many apples are left over?"}], "ideal": "2"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "A store is offering a 25%
discount on a jacket that originally costs $120. The store is also
offering another 20% discount on pants that cost half of the jacket.
Jane has $200. How much will she have after buying both the jacket and
the pants?"}], "ideal": "62"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "If a bank account has an
annual interest rate of 10% and a starting balance of $1,000, how much
interest will be earned after 3 years?"}], "ideal": "331"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "In a standard deck of 52
playing cards, what is the probability of drawing an ace, a spade, or a
red face card?"}], "ideal": "11/26"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "A train travels at a constant
and max speed of 100 km/h until it reaches 5/10 of its journey, at which
point it slows down to 50km/h. If the journey distance is as far as it
can travel at max speed in 2 hour, how long will it take to complete the
trip?"}], "ideal": "3"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "There are 2.54 cm in an inch.
How many inches are in three lengths added together, where the first
length is two times the second length which is three times as long as
the third length which is 5.08 cm"}], "ideal": "20"}
  ```
</details>

---------

Co-authored-by: tim <tim@tim.com>

---
## [Aetherum17/WWU](https://github.com/Aetherum17/WWU)@[6d58e54d9c...](https://github.com/Aetherum17/WWU/commit/6d58e54d9ce411d5434747a3880e90b4ef44bc98)
#### Thursday 2023-05-25 19:19:59 by Vawser

Government

- Added "Faction Authority" mechanic to the "Dragon Aspects" reform:
 - Faction Authority is built up by:
  - Maintaing high relations with Dragon Aspect members as the leader.
  - Winning wars with Dragon Aspect members as war allies.
 - Added "Blessing of the Life-Binder" action: adds yearly_corruption modifier to all Dragon Aspect members. Can be stacked up to yearly_corruption = -0.075
  - Once the modifier is fully upgraded, this action applies add_yearly_manpower = 5.0
 - Added "Timeless Foresight" action: adds years_of_nationalism modifier to all Dragon Aspect members. Can be stacked up to years_of_nationalism = -15
  - Once the modifier is fully upgraded, this action applies add_corruption = -10
 - Added "Verdant Growth" action: adds development_cost modifier to all Dragon Aspect members. Can be stacked up to development_cost = -0.15
  - Once the modifier is fully upgraded, this action applies add_dip_power = 500
 - Added "Secrets of the Arcanum" action: adds all_power_cost modifier to all Dragon Aspect members. Can be stacked up to all_power_cost = -0.075
  - Once the modifier is fully upgraded, this action applies add_adm_power = 500
 - Added "Dominion of the Earth-Warder" action: adds administrative_efficiency modifier to all Dragon Aspect members. Can be stacked up to administrative_efficiency = 0.075
  - Once the modifier is fully upgraded, this action applies add_mil_power = 500
 - Added "Unite the Dragon Aspects" action: if all other actions have been completed, then the Dragon Aspect leader can choose to annex or vassalize all Dragon Aspect members with relations above 0. Annexation will dismantle the faction however: leader will retain the modifiers and the government form, but the rest of the faction stuff will be disabled.

- Added completion effects for the Faction Authority mechanic actions for the Alliance, Horde, Old Horde and Trade Coalition.

---
## [tgrant-nv/OpenShadingLanguage](https://github.com/tgrant-nv/OpenShadingLanguage)@[71a9310f0b...](https://github.com/tgrant-nv/OpenShadingLanguage/commit/71a9310f0b8765f57b59e25e73f5f3bbdb8077e8)
#### Thursday 2023-05-25 19:46:44 by Larry Gritz

feat(gpu)!: GPU/OptiX support of ReParameter (#1686)

BREAKING CHANGE: to RendererServices ABI (including for CPU) and to
the renderer-side setup when using OptiX.

This overhauls the implementation of how interactively-editable
parameters work, where they live in memory, and get it all working on
GPU/OptiX so that renderers can support interactive adjustment of
those params without recompiling shaders.

The basic gist is as follows:

* We continue work to finish making a clean separation between
  "interpolated" parameters and "interactive" (editable) parameters.

* Interpolated params are collected and put into a separate memory
  area -- a separate per-group allocation on both the CPU and GPU
  (where applicable). It needs to remember the offset into this arena
  where each of the interpolated parameters resides. These allocations
  and eventual release are taken care of by the OSL shading system,
  they live in the ShaderGroup. When the group is set up, this block
  of memory is initialized with the correct initial values of the
  params and are ready to go.

* The implementation of ReParameter writes to this special memory
  area also, that's how it works now (both CPU and GPU).

* How does the OSL library know how to allocate, free, and copy to the
  device memory? It doesn't! Instead, we add new RendererServices
  methods `device_alloc()`, `device_free()`, and
  `copy_to_device()`. It's up to the renderer to provide those, so
  that the OSL library doesn't itself need to know about the Cuda
  runtime. These are trivial, there's really only one implementation
  that makes sense, and you can copy it from the ones in testshade and
  testrender.

* Interactive parameters are NOT constant folded during runtime
  optimization.

* The shader entry points themselves now take an extra parameter in
  the main call -- this will be the pointer to the beginning of the
  shader group's interactive parameter arena.

* When JITing, references to interactive parameters know to retrieve
  them from their designated offset into the interactive parameter
  area.

* This means that the renderer-side OptiX/Cuda code is responsible for
  adding this extra pointer parameter to the call to the shader entry
  points. You can see how this is done in the testshade and testrender
  Cuda code.

* It's up to the renderer to figure out how to make the OptiX hit program
  aware of the interactive parameter pointer for that particular material,
  in order to pass it to the osl shader entry point. The way I did it in
  testshade and testrender is using a field in the struct that's given
  to each entry of the shader binding table and can be retrieved on the
  OptiX side via optixGetSbtDataPointer(). In testshade/testrender, a
  data pointer already existed which wasn't used. In a real renderer, you
  may need to add a field or come up with whatever other way you want
  to somehow get this pointer, which can be retrieved via

      shadingsys->getattribute(shadergroupptr, "device_interactive_params",
                               TypeDesc::PTR, &myptr);

  you can see how I do that in optixraytracer.cpp (testrender) and in
  optixgridrender.cpp (testshade).

A number of other things you will see that's worth calling out:

I added a device_ptr utility template that is just a wrapper around a
device side pointer that makes it hard to accidentally dereference it
on the host side.

Since I was changing RendererServices anyway, I also remove unused
register_global, fetch_global, global_map which were unused. They were
leftovers from the way we handled strings in OptiX 6.x.

Encapsulate cuda global symbol name mangling into
BackendLLVM::global_unique_symname(). I did this early on, turns out
it wasn't necessary, but I still like that encapsulation, so I'm
keeping it.

I bumped the 3rd set of digits in the version to reflect that the
changes in RendererServices break ABI. This is only in main, it
obviously cannot be backported to a release branch.

All tests pass for scalar and batch and optix.

I added a new simple reparam test, and renamed the old reparem to
reparam-array. Oddly, the reparam-array test doesn't work properly on
optix (it had never been tried before), but it also failed in optix at
main -- so it's not related to this patch! Putting that on my list of
other oddities to investigate later. It may just be a quirk of
testshade, I'm not really sure yet.

Added to BackendLLVM (and batched) a llvm_ptr_type(TypeSpec) method
that returns the LLVM type of a pointer to the specified type.

Note: This patch doesn't account for the face that a parameter marked
"interactive" could prevent a shader from correctly building for the GPU
because it used the kind of construct that is fine in shader source code but
only will work on GPU if it can be resolved to be a constant by the time
we get done with the runtime optimization (as pointed out by Stephen
Friedman. We'll come back to the problem later with a more robust and
automatic fix -- and if we are lucky, Stephen will have the opportunity to
upstream the approach he already has.

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [estiven9612/GOD-KILLER](https://github.com/estiven9612/GOD-KILLER)@[38c16aecdb...](https://github.com/estiven9612/GOD-KILLER/commit/38c16aecdb88f2640e4d368f59ff9e3a692db508)
#### Thursday 2023-05-25 20:43:05 by estiven9612

Update install.py

my friend, what a shame to change those letters of code, it is that most of the repositories already used use python 3, so I found the error in that line, for an update from Python 2 to Python 3, sorry if I change your line of code; You could use the original raw_input code for python 2, and the input for newer versions.

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[2bca78d445...](https://github.com/realforest2001/forest-cm13/commit/2bca78d445030e89792dfadf9a0153a94c71195b)
#### Thursday 2023-05-25 20:43:07 by c4xmaniac2

Science Annex Nightmare Inserts (#3288)

# Science Annex Nightmare Inserts

Apparently I'm the only one in CM who actually likes this fucking map,
and like a year ago I told nanu I'd make NM for science annex and
kutjevo. Also so help me God if this fucking lowers my GBP because i
don't know how the shitty GBP economy works I'm going to have an
aneurism.

**Also I'm not on the discord, if you have comments leave them on the
PR.** Nor will I be rejoining. That place sucks and I don't like
interacting with the retards on it. Sorry sweeties, but daddy has no
desire to rejoin that shitshow. You have no idea how freeing it is to
not hear people crying about everything at all times.

> This PR adds 4 new NM to the map Science Annex.

WRONG WE'RE AT 10 NOW BABY!!!!!!!!!

**Lan Party** 20% Chance


![gamerannex](https://github.com/cmss13-devs/cmss13/assets/133173804/0aa46b6d-ab20-4797-b35d-5ef7c3cb4a46)
This insert features an epic lan party between the prisoners and the
prison staff, who will win in this epic competition? Xenos.

**Pizza Palace** 30% Chance

![pizzaannex](https://github.com/cmss13-devs/cmss13/assets/133173804/eff5767a-8e0c-4c33-8c04-30d297c89ebd)
This insert changes the kitchen to be a pizza palace. Mamma Mia! (The
pizza time is replacing the sentry spawn, its so fricken thematic)

**Pool Party** 20% Chance

![poolannex](https://github.com/cmss13-devs/cmss13/assets/133173804/fd6d127e-7c63-4673-976f-9faa84100b68)
Woah dude, prison's out man heh surf's up dude! Come and hang out with
your best pals while everyone else around the station dies.

**Warden Office - Redecorated** 15% Chance

![wardenannex](https://github.com/cmss13-devs/cmss13/assets/133173804/32e221e2-20b4-4e66-814c-8ea62d7d6056)
The warden has found God, well a god, the god of HEFA and chose to
sacrifice himself to bring the pain! The knights said he had a change of
heart, but too bad!

**POD HOLD BABY** 10% Chance

![podhold2](https://github.com/cmss13-devs/cmss13/assets/133173804/0fbe2729-1473-4b05-8fe4-f34c30b75a09)
Oh yeah baby! I heard you've never even heard of this SOULFUL HOLD!!!!
Don't worry, with the NEW CHANGES coming to it, its now 25% better!
Better hope that medium chance sentry actually does spawn, though.

**Engineering Office** 30% Chance

![engieoffice](https://github.com/cmss13-devs/cmss13/assets/133173804/22a62e2b-dcf9-4a7c-a550-32134d691594)
Thought it would be cool if they didn't demolish the office, so here it
is repaired and with new minor stuff like a cool beret to tempt you to
check it out. Also don't read the paper.

**Research Cells Containment** 25% Chance

![research](https://github.com/cmss13-devs/cmss13/assets/133173804/e3aba4a6-d895-415a-8d9d-ec93bcdbd671)
The prison staff assumed that whoever was the cause of the outbreak was
in these cells. Unfortunately for everyone, they ended up being wrong.
You get to witness what's left over in the research cellblock if they
walls weren't destroyed from the beginning!

**Emergency Medical Practice** 20% Chance

![medicalhold](https://github.com/cmss13-devs/cmss13/assets/133173804/b41eeee2-9602-4cf1-8055-a6cf74dafc41)
Shit really started hitting the fan, so the medical staff set up a
temporary treatment area in the triage zone. Strangely, the sounds of
men screaming in agony attracts xenos, who knew?

**Scav Ship Hold** 10% Chance

![scavship](https://github.com/cmss13-devs/cmss13/assets/133173804/17386a2c-8b5a-4647-a102-38a845155be0)
I heard you liked single man suicide holds? Awesome news then, I've got
another one for you. This one even comes with elite mercenary gear to
help you survive. Only problem is the guy who owned it before you didn't
maintain it, and its not that protective now. One might say the slow
down of the armor will kill you, I say drip or drown loser. Go out in
style!

**Looted Armory** 15% Chance

![empty](https://github.com/cmss13-devs/cmss13/assets/133173804/7221de4f-43bd-4b7a-ae11-125c12e6c434)
You know what they say, the early bird gets the worm. Well in this case,
the early prisoners got all the gear. Help yourself to what's leftover,
it's not much!




**Miscellaneous changes**

The sentry gun in the park is gone. This shit still massacres new surv
players and they don't know what happened. Call it baby sitting, I don't
care. I intended to remove it when I changed LZ1 and forgot, so it goes
bye bye now!



![podhold](https://github.com/cmss13-devs/cmss13/assets/133173804/2972a11d-ce94-4ce1-bd37-20f5a8a24d4f)
This piece of shit console now no longer blocks movement. The META
DEFINING pod hold is now slightly stronger. Honestly, 70% of the people
reading this probably don't even know where this is located and 100%
don't go into it. Listen, it bugs me that this shit blocks you being
able to move. Imagine having an extra dude to FF you in the now 4x4 box
of hell. The possibilities are endless, not really, but I'd like to
think so.
 
# Explain why it's good for the game
Nanu asked me to make NM for this map and kutjevo. I like this map more
than kutjevo, so I made some for here first. It adds character, who
doesn't want to sacrifice the warden for HEFA?

Sentry change is QOL for new players. It had literally 0 impact outside
of killing new players. Its funny, but we have to protect the children.
Call this the protect the children change and it will pass through the
dev team, I guarantee it.

The console change is a QOL change for me because its so fucking
annoying that this little piece of shit can stop me from moving. LOOK AT
IT, IT'S AGAINST THE FUCKING WALL, HOW DOES IT BLOCK THE ENTIRE TILE?!


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
mapadd: added 4 new NM inserts to Science Annex
maptweak: sentry in the park no longer terrorizes new players, and the
stupid fucking console doesn't block movement.
/:cl:

---
## [Ilevius/twp0.0](https://github.com/Ilevius/twp0.0)@[84e081df35...](https://github.com/Ilevius/twp0.0/commit/84e081df35c46ada525822f42936debdbbae6cf1)
#### Thursday 2023-05-25 20:53:58 by Alexandr Tatarkin

sympy is bullshit, it sucks all dicks in the world, it eats shit all the time fuck

---
## [pinksub/SkylightOS](https://github.com/pinksub/SkylightOS)@[96bcd2b639...](https://github.com/pinksub/SkylightOS/commit/96bcd2b639f3d09a0ba6858cf40b5a438e6e7464)
#### Thursday 2023-05-25 22:01:31 by Lu

Merge pull request #12 from EthernalRaine/private/clang

finally merge clang into master (fuck you gcc)

---
## [rslinford/openai_evals](https://github.com/rslinford/openai_evals)@[f58f95ba32...](https://github.com/rslinford/openai_evals/commit/f58f95ba324e5a1ed86315f3c39ee758f2836bd3)
#### Thursday 2023-05-25 23:13:31 by ali risheh

[Eval] Mandaliof table test (#847)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Mandaliof table test

### Eval description

This Eval is checking if the model can find a specific atom with the
highest atomic number among 20 different atoms.

### What makes this a useful eval?

There are applications in biophysics and biochemistry (like drug
discovery) that rely on physics equations and induction on atom
features. If ChatGPT is going to be used in this field, it should be
very reliable in case of understanding physical facts. Interpretation of
the periodic table is a very simple Eval that shows the model is still
unreliable for use cases in this field.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

Physics problems are almost the most difficult tasks for any deep
learning model since they are based on fundamentals of nature, and even
humans are not capable of understanding comprehensive explanations of
them. In this regard, if ChatGPT will be able to interpret physical
facts, it is very likely that it can interpret literally everything
because even human are not able to do that.

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

Mandaliof table is the basic of physics.

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. I, Mg, Nd, Rf, Si, Ho, Fr, Ar, Xe, Rh,
Am, No, Rf, Bi, Cd, In, Sc, Te, Ce, Ge"}], "ideal": "Rf"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Fm, Ac, C, Ir, Ba, Rn, Ti, Sc, B, Nb, Cl,
Ra, Cr, Hs, Bk, Tl, Mt, S, He, Mc"}], "ideal": "Mc"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Ta, Bh, Bi, Ce, Rf, Lv, Bi, Gd, Cs, Ho,
Ta, Np, Cm, Sr, Pb, Pu, Ne, Og, Tm, Fm"}], "ideal": "Og"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Tl, Eu, Ts, Be, Ga, Cm, Ba, Sr, C, Cl,
Mo, Ni, Ru, Hs, In, Be, Dy, Ho, Br, Mt"}], "ideal": "Ts"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Mn, Hg, Pm, K, Ge, P, Fr, Cn , Mn, Fr,
Lv, W, Gd, Mt, Cd, Xe, Ge, I, Og, Br"}], "ideal": "Og"}
  ```
</details>

---

