## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-02](docs/good-messages/2023/2023-07-02.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,651,054 were push events containing 2,458,225 commit messages that amount to 150,003,685 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 61 messages:


## [MaxMood96/git](https://github.com/MaxMood96/git)@[11e5c1a6c9...](https://github.com/MaxMood96/git/commit/11e5c1a6c925ccf4e80032eddd9844cdb570ed6a)
#### Sunday 2023-07-02 00:16:10 by Johannes Schindelin

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
## [Rustybuckets6601/tgstation](https://github.com/Rustybuckets6601/tgstation)@[d85e44c69c...](https://github.com/Rustybuckets6601/tgstation/commit/d85e44c69cc06dbeeb3a0de7f76273de45ee3893)
#### Sunday 2023-07-02 00:53:05 by ChungusGamer666

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

## Why It's Good For The Game

Bugs are bad they make you mad

## Changelog

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

---
## [MemedHams/Shiptest](https://github.com/MemedHams/Shiptest)@[725233b42b...](https://github.com/MemedHams/Shiptest/commit/725233b42b6f56551798a0a75b5362e577042de3)
#### Sunday 2023-07-02 01:01:02 by thgvr

The Lizardening Part One (And Friends) (#1845)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR changes a lot of sprites. It's honestly too much. Namely:

- Explorer Equipment + Prototype
- Syndicate clothing
- Digitigrade lizard legs
- A new tail from Halcyon.
- Magboots from Zeta. Originally PR'd to tgstation.
- Colored (not greyscale! Ha Ha!) jumpsuits from Imaginos.

Heavy inspiration from the work of Imaginos, Halcyon, Mqiib, and
2cents#8442 for the original leg-work. (Haha, get it?)
The new digitigrade sprites started as a twinkle in the eye of Mqiib,
for yogstation(?) After myself and Halcyon saw those, an epihpany
struck. Perspective makes things cool and digitigrade perspective was
BAD.

I'll include a collage image of the new sprites if it's needed later.
Preview below:


![image](https://user-images.githubusercontent.com/81882910/228710332-0a213f88-5a8b-4b41-abdd-cee3b70ec403.png)
## Why It's Good For The Game
lizard,
Death of Codersprites
## Changelog

:cl:
add: New Digitigrade lizard sprites.
add: Various syndicate and mining clothing resprites.
add: Sarathi can now have an incredibly large tail.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MarcosIgnacioo/OldTwitter](https://github.com/MarcosIgnacioo/OldTwitter)@[7c311e2443...](https://github.com/MarcosIgnacioo/OldTwitter/commit/7c311e2443b57aa78ee3022c61c2d63a95de8a30)
#### Sunday 2023-07-02 01:03:53 by xanthe huynh

profile birthdate gray rectangle bug

hello i know this is weird but there was this thing abt this part of the profile that when i entered to my profile (using the dark black default twitter) the birthdate was a giant gray block and checking the css and unchecking the part i removed it kinda fixed but, again i dont really know but this is the only way i think i can tell you about this thing so im sorry if this is not actually the solution, maybe changing the color for another but yeah im sorry for this dogshit english you had to read

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[867c217c57...](https://github.com/MrMelbert/tgstation/commit/867c217c57bbcbb644e06bfcb6d362e494a895ee)
#### Sunday 2023-07-02 01:05:39 by GuillaumePrata

New Wizard spell "branch": Vendormancy (#75679)

## About The Pull Request
New item for wizards, ~~the Staff~~ Scepter of Runic Vendormancy.

With it, you can summon Runic Vending machines to block your enemies,
push them 2 tiles back around the summoning tile, throw the vendors 4
tiles away to squash them or simple detonate the vendors for direct
damage against enemies within a 2 tile range.

The scepter has 3 charges that can be recharged after a "long" channel
so while powerful, it is a tactical weapon and wizards can't directly
steamroll the crew with endless vendors. (Unless they buy multiple
scepters, but that is just funny.)

Also, there is a bug with the throw... I copied how baseball bats deal
with knockback, but they consistently don't push the vendors back, just
spin them on the same tile... I appreciate if anyone has any idea on how
to fix or change that to a better system.

## New changes I made
The vendor has a random set of REAL wizard robes and hat, sandals and a
foam vendor scepter as products to sell now.
This gives the crew some real armor, and if it is considered too much, I
can swap it for the fake versions.
IMO the real clothes work as the perfect bait for the crew to approach
the vendors and get exploded in the process, and while a random
assistant might get real wizard armor to go valid hunt the wizard, the
crew might just mistake them for the real wizard and beat them to death,
which is too funny.
## Why It's Good For The Game

![vendormancerPR](https://github.com/tgstation/tgstation/assets/55374212/f9d98f3e-5916-4a17-987e-249f4cdb7185)

About a year ago I played Stoneshard, and it has such an amazing
Geomancy Wizard that I wanted to port some of its gameplay to SS13 as
our wizards, while funny and destructive, are kinda simple to play...

Summoning and blowing up rocks was nice, but I randomly had the idea of
summoning Vendors while at work and vendors squashing people has become
such an iconic SS13 thing to me that I had to stop being lazy and start
working on this.

Something, something, enviromental combat wizard.
## Changelog
Gonna polish the changelog later too...
:cl: Guillaume Prata
add: New Wizard spell branch: Vendormacy! Summon runic vending machines
with your Vending Scepter, force push them on your enemies to squish
them or blow them up while they are busy buying from the machines.
/:cl:

---------

Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[8788e48378...](https://github.com/GoldenAlpharex/tgstation/commit/8788e483788db2432b9649313efc9426d324379f)
#### Sunday 2023-07-02 01:25:46 by Time-Green

Shuttle events (#76008)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/7501474/a2d83ce8-eba1-42d9-a1f8-9d73f7c40b21

Adds shuttle events! Stuff can now start to happen outside the shuttle,
either benign or spicy (but usually just fun to watch)!
## Why It's Good For The Game

The shuttle escape sequence is an important part of the game, uniting
about every player surviving player. Recently, #71906 has made the
escape sequence more forgiving as well as more interesting by
conditionally doubling the playing field. The area outside the shuttle
is still mostly empty though, except for the few people being spaced,
daredevils and the occasional epic space fight.

This PR adds adds some space events to spice up the outside of the
shuttle! This both gives people something too look at, making the escape
sequence feel less static and more lively, as well as give people a
reason to go outside and get the full experience of ~being decapitated
by a meteor~ swimming with the fishes!

<details>
  <summary>Shuttle Events</summary>

**Friendly carp swarm**
Spawns a group of carp that flies past the shuttle, completely friendly
unless provoked.

**Friendly meteors**
Spawns a lot of strong meteors, but they all miss the shuttle.
Completely safe as long as you don't go EVA

**Maintenance debris**
Picks random stuff from the maintenance spawn pool and throws it at the
shuttle. Completely benign, unless you get hit in the head by a toolbox.
Could get you some cool stuff though!

**Dust storm**
Spawns a bunch of dust meteors. Has a rare chance to hit the shuttle,
doing minimal damage but can damage windows and might need inflight
maintenance

**Alien queen**
One in every 250 escapes. Spawns a player controlled alien queen and a
ripley mech. RIP AND TEAR!! Really not that dangerous when you realize
the entire crew is on the shuttle and the queen is fat as fuck, but can
still be fun to throw people around a bit before being torn to shreds.

**ANGRY CARP**
Once in every 500 escapes. Spawns 12 normal carp and 3 big carps, who
may just decide to go through the shuttle or try and bust through the
window if you look at them wrong. Somewhat dangerous, you could stay
away from the windows and try to hide, or more likely shoot at them and
weld the windows

**Fake TTV**
Lol

**Italian Storm**
Once in every 2000 rounds. Throws pasta, pizza and meatballs at the
shuttle. Definitely not me going off the rails with a testing event

**Player controlled carp trio**
Once in every 100 escapes. Spawns three player controlled carp to harass
the shuttle. May rarely be a magicarp, megacarp or chaos carp. I can't
honestly see them do anything other than be annoying for 3 seconds and
die

There are some other admin only ones: a group of passive carps going
directly through the shuttle and just being little shits, and a magic
carp swarm
</details>

Events are selected seperately, there isn't a crazy weighting system,
each just has a chance to run, and multiple could run at once. They also
don't immediately trigger, so people can get settled a bit, and to make
sure just waiting out the more dangerous ones is still a valid strategy.

## Changelog
:cl:
add: Adds shuttle events! If shuttle escapes weren't exciting before
(doubtful), they definitely are now! I'm joking it's mostly an
atmosphere thing.
admin: Adds an admin panel to interact with shuttle events, under the
Events tab: Change Shuttle Events
fix: Objects spawned in hyperspace will properly catch hyperspace drift
/:cl:

There's a few things I'd like to do later (another PR) (honestly anyone
can do them because I suck at follow-ups), because this is too big as
is:
- Hijack triggered shuttle events
- More events (got a lot of cool suggestions, but I'm putting most of
them on hold)
- Maybe stration announcements if some more dangerous ones get added
- Structures appearing next to the escape shuttle???

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[9aa3fb2901...](https://github.com/shiptest-ss13/Shiptest/commit/9aa3fb29012991ce7a9d755e640a1af65f3fe319)
#### Sunday 2023-07-02 01:53:50 by thgvr

Fixes a good chunk of Vox sprites. Removes environmental regulator (#2092)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Oh god the pain. Oh god. The unbearable pain. Why.

Adds a ton of unused vox sprites from Drawsstuff.
Cleans up the files for sprites we don't actually have
Ensures they are pathed correctly, with flags set correctly.
I spent five hours on this in one sitting after being upset at shitty
vox mechanics/sprite support again. They're cool and unique and it was
sad.
Removes the Environmental Regulator.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
1. Vox sprites were incomplete. This completes them a little bit more.
2. The environmental regulator isn't fun. This will remove the regulator
and vox needing to use it. It was buggy, poorly made, and just not fun
even when it worked correctly. Vox aren't nearly strong enough to be
constantly crippled.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A metric ton of Vox sprites
del: Vox no longer need environmental regulators
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[c84e40255d...](https://github.com/shiptest-ss13/Shiptest/commit/c84e40255d466e37983e5cb03c110e7dd8ab90c8)
#### Sunday 2023-07-02 01:53:50 by Imaginos16

Ports pinging in Adminsay from /tg/station (#2111)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says on the tin, porting a behavior that allows you to ping
a person in admin say by just doing @(ckey) from /tg/station in PR
[#61712](https://github.com/tgstation/tgstation/pull/61712)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/fc756e0f-668f-4641-9bcd-689d6548d343)

Oh and this PR I guess fixes a hilarious issue where **someone** wrote
'tgstation.dme' instead of 'shiptest.dme' where they shouldn't have.
Whoops!

Most cool of all, which was completely unintentional by me, ports Datum
linking (partially), as well as Ticket linking, respectively added in
PRs [#65154](https://github.com/tgstation/tgstation/pull/65154) and
[#65634](https://github.com/tgstation/tgstation/pull/65634)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/d6f980ee-c490-4f8d-a76c-81447aeb7658)



<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I swear to fucking christ if I have to log into the game one more
goddamn time as an admin only to have 2 people being DJs, another one
spriting, and another one doing jack shit while not paying attention at
the server when I am trying to solve a crucial ticket, I'll develop an
aneurysm.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Ryll-Ryll/Shaps
admin: Adds pinging to adminsay!
admin: Adds the ability to link datums!
admin: Adds linking tickets to asay! Simply put a # followed by a ticket
number for it to be linked in the chat!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[a6763aee3e...](https://github.com/Bubberstation/Bubberstation/commit/a6763aee3e8ab0c8f42325a75be42adf172a12ad)
#### Sunday 2023-07-02 01:55:12 by BurgerLUA

Hugboxes pierced realities (#281)

## About The Pull Request

- Pierced realities no longer gib your entire head when you click on
them with TK.
- Pierced realities no longer dismember your arms when you click on them
without TK.
- Pierced realities no longer make you want to die when you examine them
(still give drain bamage).

## Justification

New players won't get baited into clicking on the pierced reality. This
is funny, but it's just annoying for medical.
Veteran players won't get baited into clicking on the pierced reality
with TK because they're curious to see what would happen.
The mood debuff is ultimately pointless and no one ever takes it
seriously anyways.

## Changelog

:cl: BurgerBB
del: Hugboxes pierced realities by removing some non-heretic
functionality.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [TheWolfbringer/tgstation](https://github.com/TheWolfbringer/tgstation)@[8af20d1577...](https://github.com/TheWolfbringer/tgstation/commit/8af20d157738044cef2fc00846caa1869d56a087)
#### Sunday 2023-07-02 02:32:54 by necromanceranne

Fixes some inconsistencies with the chaplain revolver and gets rid of a weird ammo define (#76237)

## About The Pull Request

Firstly, I gave the revolver a new sprite. I mean, this isn't so much of
an improvement as it is a reference I wanted to go with, so if people go
'no not a new sprite' I don't mind reverting.

What's the reference? Check the new name I added as a potential name
roll.

![lucky
38](https://github.com/tgstation/tgstation/assets/40847847/e11874be-1416-4e21-bda9-4881d49cad1b)

Secondly; I applied to the gun itself revenant bane, the ability to
clear runes, and proper magic immunity as a full null rod would enable.
This last bit was a deliberate design choice, but the divine bow has
full magic protection, so I think this is now more of a consistency
consideration compared to the divine bow.

Thirdly, the revolver is a .38 revolver, HOWEVER, it uses a damage
multiplier to bring it back to the damage it did originally. It also
cannot be reloaded without the prayer action. No cheating. Effectively,
this is the same mechanically as it was before.

It rarely does a funny crit fanfare. This does nothing mechanically, I
just thought it was a funny nod to the sprite's reference (and I guess
another game that the crit fanfare is based on). Borrowed parts of the
code and sprite from this April Fool's pr by Wallemations >
https://github.com/tgstation/tgstation/pull/74425

## Why It's Good For The Game

I think this might have been a little forgotten since implementation now
that we have another projectile weapon for the chaplain. So I'm brushing
it up a bit.

## Changelog
:cl:
fix: Makes the chaplain's revolver consistent with its immediate
sibling, the Divine Bow, by giving it similar statistics.
code: Makes the chaplain revolver a .38 but prevents it from being
loaded without using the special prayer action. Also applies a damage
multiplier to keep it at the original 18 force. Mechanically, no
different.
sprite: Gives the chaplain revolver a new sprite.
code: Removes an unnecessary admin log when removing runes.
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a4d2e5724d...](https://github.com/treckstar/yolo-octo-hipster/commit/a4d2e5724d143a0dc6832b50c0b59aa49c28114a)
#### Sunday 2023-07-02 03:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[27abc4cf52...](https://github.com/i3roly/glibc_ddwrt/commit/27abc4cf5296d24365ee326726c4d61c7efe6075)
#### Sunday 2023-07-02 03:56:57 by gagan sidhu

[v53142] just an update. "new nose daryl" or "daryl new nose"?

a bunch of updates to the build by ol' assfuck. seems he kept himself
busy this time by using libcurl for speedtest_cli so that he has a more
efficient way of calling curl. spinkicking away with that dancing ribbon
whilst typing "svn commit", i maintain.

i partially solved the size issue. we're down to about 1615xxxx bytes so
that's good. turns out sed linked a static pcre2 and that was part of
the issue.

regarding the commit summary, i was going to ask the audience about
which name is better
        -since google image search reveals he shows up first using any
        permutation of these terms (or so i think), it's only right we
        pick a name a run with it.
                -i'm sure his boy joel silver is trying to find some nerds
                who can SEO that away, to no avail lol.

you know, like "mad eye moody", "half-blood prince", "bootstrap bill
turner" etc. i think "daryl new nose" sounds a bit more rebellious than
"new nose daryl"

---
## [Hemanth1210/JAVA-FUNDAMENTALS](https://github.com/Hemanth1210/JAVA-FUNDAMENTALS)@[457cf446f6...](https://github.com/Hemanth1210/JAVA-FUNDAMENTALS/commit/457cf446f6a1497eb4f67101456567f9d7cdd426)
#### Sunday 2023-07-02 04:08:15 by Hemanth1210

3 idiots

Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality.

A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out?

Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a  program to find the midpoint of the line.

Input Format:

Input consists of 4 integers. The first integer corresponds to x1 . The second integer corresponds to y1. The third and fouth integers correspond to x2 and y2 respectively.

Output Format:

Refer Sample Input and Output for exact formatting specifications.

[All floating point values are displayed correct to 1 decimal place]

Sample Input and Output:

[All text in bold corresponds to input and the rest corresponds to output]

2

4

10

15

Binoy's house is located at (6.0,9.5

---
## [V01DFox/Fen-Station](https://github.com/V01DFox/Fen-Station)@[02e36ec18e...](https://github.com/V01DFox/Fen-Station/commit/02e36ec18e5ff421243b6816cf115d27c2c4263d)
#### Sunday 2023-07-02 05:34:42 by SkyratBot

[MIRROR] Expanding the Experimental MODsuit Bepis Node with three new modules. [MDB IGNORE] (#21851)

* Expanding the Experimental MODsuit Bepis Node with three new modules. (#75801)

## About The Pull Request
So, I've had this idea to make a contribution to the Bepis feature with
some modsuit stuff. The gimmicky stuff is ok and a good way to even out
the better content since it has game of chance design it has (you can
find those disks in space anyway so...). However, the Experimental
MODsuit node feels very underwhelming right now, compared to how big
that feature is.

This PR adds three MOD modules to the Experimental MODsuit node, plus
two more:
- Magneto Charger: While the Modsuit is activated, each step the user
takes will charge the installed power cell by a tiny bit, enough to
sustain a standard modsuit of generic slow speed with only a few, easy
modules installed. It won't work in zero G, while flying, pulled by
someone else, on a conveyor belt, riding a vehicle or crawling on the
floor, though.
- Recycler: It collects (most) garbage and casings off the ground and
recycles them into material sheets that can be dispensed on an adjacent
location or storage with with Middle Mouse Button. Doesn't clean debris,
and scuffed because most trash doesn't yield material anyway.
- - It also has two subtypes, unbound from the node: one that dispenses
riot foam darts and can be found on the black market, and another that
dispenses the more innocuous foam darts, rarely found in maints.
- Shooting Assistant: A configurable module. On Stormtrooper mode, it
will give the user a faster fire rate (the double tap trait) at the cost
of accuracy. On Sharpshooter mode, it will improve the user accuracy and
make their shots ricochet against walls at least once (if the hit atom
allows that, that is, e.g. lasers don't ricochet against iron walls), at
the cost of movement speed. Both modes also prevent the user from dual
wielding guns.

To make the Stormtrooper mode stackable with the poor aim quirk and
refrain from making a new trait for the sharpshooter mode, the gun
spread code in gun.dm has also received a little refactor and cleanup.
Also, it's been tested.

## Why It's Good For The Game
The Experimental MODsuit node is quite shabby and could use something
extra to make it more appealing to MODsuit enjoyers.

Also doubles down as a small addition to the black market and maint
loot, and code cleanup, since gun code gives off some garbled vibes.

## Changelog

:cl:
add: Expanded the Experimental MODsuit Bepis node with three new
modules: Magneto Charger, Recycler and Shooting Assistant.
add: Added a Riot Foam Recycler module to the black market, as well a
more innocuous version as maint loot.
/:cl:

* Expanding the Experimental MODsuit Bepis Node with three new modules.

* update modular, I hate this file btw

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [shivamidow/WebKit](https://github.com/shivamidow/WebKit)@[d6ae2528a9...](https://github.com/shivamidow/WebKit/commit/d6ae2528a9f3819005e08f9d5091ceff8b880fa8)
#### Sunday 2023-07-02 06:27:55 by Dean Jackson

WebXR: Severe aliasing in WebXR experiences (with WebGL1 contexts)
https://bugs.webkit.org/show_bug.cgi?id=256861
rdar://109424254

Reviewed by Dan Glastonbury.

WebXR sessions using WebGL1 contexts are unable to turn on
multisampling. I'm pretty sure this was my fault, but I can't
remember if it was intentional or a mistake. Either way it is
a bug.

Fix this by implementing the multisample renderbuffer creation
and resolution steps. Since we're doing this on a WebGL1 context,
the normal API will be invalid (it requires GLES3), so call the
extension API instead. This means we need to expose some extra methods
on GraphicsContextGL.

Lastly, the framebuffer textures we get are SRGB8_ALPHA8 which
requires an extension to be enabled with a WebGL1 context when
we're talking to an XR-compatible context. Similarly, we
enable the extension to allow multisampled framebuffers.

* Source/WebCore/Modules/webxr/WebXROpaqueFramebuffer.cpp:
(WebCore::WebXROpaqueFramebuffer::endFrame): call blitFramebufferANGLE.
(WebCore::WebXROpaqueFramebuffer::setupFramebuffer): Implement logic for WebGL 1.
* Source/WebCore/platform/graphics/GraphicsContextGL.h:
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.cpp: Implement the extension API/
(WebCore::GraphicsContextGLANGLE::renderbufferStorageMultisampleANGLE):
(WebCore::GraphicsContextGLANGLE::blitFramebufferANGLE):
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.h:
* Source/WebCore/platform/graphics/cocoa/GraphicsContextGLCocoa.mm:
(WebCore::GraphicsContextGLCocoa::platformInitialize): Turn on the sRGB extension.
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGL.messages.in:
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGLFunctionsGenerated.h:
(renderbufferStorageMultisampleANGLE):
(blitFramebufferANGLE):
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxy.h:
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxyFunctionsGenerated.cpp:
(WebKit::RemoteGraphicsContextGLProxy::renderbufferStorageMultisampleANGLE):
(WebKit::RemoteGraphicsContextGLProxy::blitFramebufferANGLE):

Canonical link: https://commits.webkit.org/264838@main

---
## [TGDavid69/flexbox-landing-page](https://github.com/TGDavid69/flexbox-landing-page)@[540dd5a7a3...](https://github.com/TGDavid69/flexbox-landing-page/commit/540dd5a7a3b8bd53ffc384abb219be8fa5b9b965)
#### Sunday 2023-07-02 06:56:10 by TGDavid69

Add shadows to info containers in section two

A quick minor change that I added in before showing this to my
girlfriend. I also just wanted to write here that I really need to
work on my organization for style sheets. The beginning looks a bit
atrocious to be honest.

To the future me, please continue working like this! It's pretty fun
once you get into it. Just remember to keep yourself motivated/focused
by adding retarded text and shit lol. Past David believes in you!

---
## [abhishek1994-ux/-MyCloudDiary](https://github.com/abhishek1994-ux/-MyCloudDiary)@[aee0596df2...](https://github.com/abhishek1994-ux/-MyCloudDiary/commit/aee0596df264bca721712f211aac12b74451faea)
#### Sunday 2023-07-02 07:03:43 by Abhishek Shrivastava

AWS - Professional Services

What Is AWS?

Cloud computing is the on-demand delivery of IT resources with primarily pay-as-you-go pricing.

Cloud computing deployment models

Cloud computing provides developers and IT departments with the ability to focus on what matters most by avoiding work like procurement, maintenance, and capacity planning. As cloud computing has grown in popularity, several deployment strategies have emerged to help meet specific needs of different users. Each type of deployment method provides you with different levels of control, flexibility, and management. Understanding the differences between these deployment strategies can help you decide what set of services is right for your needs. 

On-premises

Before the cloud, companies and organizations hosted and maintained hardware such as compute, storage, and networking equipment in their own data centers. They often allocated entire infrastructure departments to take care of their data centers, which resulted in costly operations that made some workloads and experimentation impossible. 

As internet use became more widespread, the demand for compute, storage, and networking equipment increased. For some companies and organizations, the cost of maintaining a large physical presence was unsustainable. To solve this problem, cloud computing emerged.

Cloud

Cloud computing is the on-demand delivery of IT resources over the internet with primarily pay-as-you-go pricing. With cloud computing, companies do not have to manage and maintain their own hardware and data centers. Instead, companies like Amazon Web Services (AWS) own and maintain data centers and provide virtual data center technologies and services to companies and users over the internet.

Hybrid

A third option is a hybrid deployment. This type of deployment is a way to connect infrastructure and applications between cloud-based resources and existing resources that are not located in the cloud. The most common method of hybrid deployment between the cloud and existing on-premises infrastructure connects cloud resources to internal systems to extend and grow an organization's infrastructure into the cloud.

To help differentiate between running workloads on premises and in the cloud, consider a scenario in which developers must deploy a new application feature. Before they deploy, the team wants to test the feature in a separate quality assurance (QA) environment that has the same configurations as production. In an on-premises solution, an additional environment requires you to buy and install hardware, connect the necessary cabling, provision power, install operating systems, and more. These tasks can be time consuming and expensive. Meanwhile, the new feature’s time-to-market increases while the developers wait for the QA environment. 

In contrast, by running your application in the cloud, you can replicate an entire production environment in a matter of minutes or even seconds. Instead of physically installing hardware and connecting cabling, the solution is managed over the internet.

Using cloud computing saves time during setup and removes redundant and unnecessary tasks. If you look at any application, you will see that some of its aspects are very important to your business, like the code. However, other aspects are no different than any other application that you might make—for example, the compute that the code runs on. Some repetitive common tasks don’t differentiate your business, like installing virtual machines (VMs) or storing backups. By removing these tasks, you can focus on what is strategically unique to your business and let AWS handle the time-consuming tasks that don’t separate you from your competitors, we refer to this as removing "undifferentiated heavy lifting". That's where AWS fits into all of this.

AWS provides cloud computing services. The IT resources mentioned in the cloud computing definition are AWS services. For this course's corporate directory application, you will use AWS services to architect a scalable, highly available, and cost-effective infrastructure to host the corporate directory application. That way, you can get the application out into the world quickly, without managing heavy-duty physical hardware.

Six advantages of cloud computing

To learn more, expand each of the following six categories.

Pay as you go

Benefit from massive economies of scale

Stop guessing capacity

Increase speed and agility

Realize cost savings

Go global in minutes

AWS Global Infrastructure

Infrastructure exists as the foundation of every cloud application.

To watch the video on the AWS Global Infrastructure, choose the play button.

To access a transcript of the video, expand the following block.

Transcript

Infrastructure, like data centers and networking connectivity, still exists as the foundation of every cloud application. In AWS, this physical infrastructure makes up the AWS Global Infrastructure, in the form of Regions and Availability Zones.

Regions

Regions are geographic locations worldwide where AWS hosts its data centers. AWS Regions are named after the location where they reside. For example, in the United States, the Region in Northern Virginia is called the Northern Virginia Region, and the Region in Oregon is called the Oregon Region. AWS has Regions in Asia Pacific, China, Europe, the Middle East, North America, and South America. And we continue to expand to meet our customers' needs.

Each AWS Region is associated with a geographical name and a Region code.

Here are examples of Region codes:

us-east-1 is the first Region created in the eastern US area. The geographical name for this Region is N. Virginia.

ap-northeast-1 is the first Region created in the northeast Asia Pacific area. The geographical name for this Region is Tokyo.

Choosing the right AWS Region

AWS Regions are independent from one another. Without explicit customer consent and authorization, data is not replicated from one Region to another. When you decide which AWS Region to host your applications and workloads, consider four main aspects: latency, price, service availability, and compliance.

To learn about a category, choose the appropriate tab.

LATENCY

PRICING

SERVICE AVAILABILITY

DATA COMPLIANCE

If your application is sensitive to latency (the delay between a request for data and the response), choose a Region that is close to your user base. This helps prevent long wait times for your customers. Synchronous applications such as gaming, telephony, WebSockets, and Internet of Things (IoT) are significantly affected by high latency. Asynchronous workloads, such as ecommerce applications, can also suffer from user connectivity delays.

Availability Zones

Inside every Region is a cluster of Availability Zones. An Availability Zone consists of one or more data centers with redundant power, networking, and connectivity. These data centers operate in discrete facilities in undisclosed locations. They are connected using redundant high-speed and low-latency links.

Availability Zones also have code names. Because they are located inside Regions, they can be addressed by appending a letter to the end of the Region code name. Here are examples of Availability Zone codes:

us-east-1a is an Availability Zone in us-east-1 (N. Virginia Region).

sa-east-1b is an Availability Zone in sa-east-1 (São Paulo Region).

Therefore, if you see that a resource exists in us-east-1c, you can infer that the resource is located in Availability Zone c of the us-east-1 Region.

Scope of AWS services

Depending on the AWS service that you use, your resources are either deployed at the Availability Zone, Region, or Global level. Each service is different, so you must understand how the scope of a service might affect your application architecture.

When you operate a Region-scoped service, you only need to select the Region that you want to use. If you are not asked to specify an individual Availability Zone to deploy the service in, this is an indicator that the service operates on a Region-scope level. For Region-scoped services, AWS automatically performs actions to increase data durability and availability.

On the other hand, some services ask you to specify an Availability Zone. With these services, you are often responsible for increasing the data durability and high availability of these resources.

Maintaining resiliency

To keep your application available, you must maintain high availability and resiliency. A well-known best practice for cloud architecture is to use Region-scoped, managed services. These services come with availability and resiliency built in. When that is not possible, make sure your workload is replicated across multiple Availability Zones. At a minimum, you should use two Availability Zones. That way, if an Availability Zone fails, your application will have infrastructure up and running in a second Availability Zone to take over the traffic.

Edge locations

Edge locations are global locations where content is cached. For example, if your media content is in London and you want to share video files with your customers in Sydney, you could have the videos cached in an edge location closest to Sydney. This would make it possible for your customers to access the cached videos more quickly than accessing them from London. Currently, there are over 400+ edge locations globally.

Amazon CloudFront delivers your content through a worldwide network of edge locations. When a user requests content that is being served with CloudFront, the request is routed to the location that provides the lowest latency. So that content is delivered with the best possible performance. CloudFront speeds up the distribution of your content by routing each user request through the AWS backbone network to the edge location that can best serve your content.

Interacting with AWS

Every action that you make in AWS is an API call that is authenticated and authorized.

To access a transcript of the video, expand the following block.

Transcript

Every action that you make in AWS is an API call that is authenticated and authorized. In AWS, you can make API calls to services and resources through the AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

AWS Management Console

One way to manage cloud resources is through the web-based console, where you log in and choose the desired service. This can be the easiest way to create and manage resources when you first begin working with the cloud. The following is a screenshot that shows the landing page when you first log in to the console. 

In the upper-left corner, you can choose Services to view AWS services grouped by categories, such as Compute, Storage, Database, and Analytics.

In the upper-right corner is the Region selector. If you choose it and change the Region, you will make requests to the services in the chosen Region. The URL changes, too. Changing the Region setting directs your browser to make requests to a different AWS Region, represented by a different subdomain.

AWS CLI

Consider the scenario where you run many servers on AWS for your application’s frontend. You want to run a report to collect data from all the servers. You need to do this programmatically every day because the server details might change. Instead of manually logging in to the console and then copying and pasting information, you can schedule an AWS CLI script with an API call to pull this data for you.

The AWS CLI is a unified tool that you can use to manage AWS services. You can download and configure one tool that you can use to control multiple AWS services from the command line, and automate them with scripts. The AWS CLI is open source, and installers are available for Windows, Linux, and macOS.

For example, you run the following API call against a service, using the AWS CLI:

aws s3api list-buckets

You will get a response similar to the following one, listing the buckets in your AWS accounts:

AWS SDKs

API calls to AWS can also be performed by running code with programming languages. You can do this by using AWS SDKs. SDKs are open source and maintained by AWS for the most popular programming languages, such as C++, Go, Java, JavaScript, .NET, Node.js, PHP, Python, Ruby, Rust, and Swift.

Developers commonly use AWS SDKs to integrate their application source code with AWS services. For example, consider an application with a frontend that runs in Python. Every time the application receives a photo, it uploads the file to a storage service. This action can be achieved in the source code by using the AWS SDK for Python (Boto3). Here is an example of code that you can implement to work with AWS resources using the SDK for Python.

Security and the AWS Shared Responsibility Model

Security and compliance are a shared responsibility between AWS and you.

When you work with the AWS Cloud, managing security and compliance is a shared responsibility between AWS and you. To depict this shared responsibility, AWS created the shared responsibility model. The distinction of responsibility is commonly referred to as security of the cloud as compared to security in the cloud. 

AWS responsibility

AWS is responsible for security of the cloud. This means that AWS protects and secures the infrastructure that runs the services offered in the AWS Cloud. AWS is responsible for the following:

Protecting and securing AWS Regions, Availability Zones, and data centers, down to the physical security of the buildings

Managing the hardware, software, and networking components that run AWS services, such as the physical servers, host operating systems, virtualization layers, and AWS networking components

The level of responsibility that AWS has depends on the service. AWS classifies services into two categories. The following table provides information about each, including the AWS responsibility.

To learn more, expand the following category.

AWS responsibility

Customer responsibility

Customers are responsible for security in the cloud. When using any AWS service, the customer is responsible for properly configuring the service and their applications, in addition to ensuring that their data is secure.

The customers' level of responsibility depends on the AWS service. Some services require the customer to perform all the necessary security configuration and management tasks. Other more abstracted services require customers to only manage the data and control access to their resources. Using the two categories of AWS services, customers can determine their level of responsibility for each AWS service that they use.

To learn more, expand the following category.

Customer responsibility

Due to the varying levels of effort, customers must consider which AWS services they use and review the level of responsibility required to secure each service. They must also review how the AWS shared responsibility model aligns with the security standards in their IT environment in addition to any applicable laws and regulations.

A key concept is that customers maintain complete control of their data and are responsible for managing the security related to their content. For example, you are responsible for the following:

Choosing a Region for AWS resources in accordance with data sovereignty regulations

Implementing data-protection mechanisms, such as encryption and scheduled backups

Using access control to limit who can access your data and AWS resources

AWS responsibility

AWS is responsible for security of the cloud. This means that AWS protects and secures the infrastructure that runs the services offered in the AWS Cloud. AWS is responsible for the following:

Protecting and securing AWS Regions, Availability Zones, and data centers, down to the physical security of the buildings

Managing the hardware, software, and networking components that run AWS services, such as the physical servers, host operating systems, virtualization layers, and AWS networking components

The level of responsibility that AWS has depends on the service. AWS classifies services into two categories. The following table provides information about each, including the AWS responsibility.

To learn more, expand the following category.

AWS responsibility

Customer responsibility

Customers are responsible for security in the cloud. When using any AWS service, the customer is responsible for properly configuring the service and their applications, in addition to ensuring that their data is secure.

The customers' level of responsibility depends on the AWS service. Some services require the customer to perform all the necessary security configuration and management tasks. Other more abstracted services require customers to only manage the data and control access to their resources. Using the two categories of AWS services, customers can determine their level of responsibility for each AWS service that they use.

To learn more, expand the following category.

Customer responsibility

Due to the varying levels of effort, customers must consider which AWS services they use and review the level of responsibility required to secure each service. They must also review how the AWS shared responsibility model aligns with the security standards in their IT environment in addition to any applicable laws and regulations.

A key concept is that customers maintain complete control of their data and are responsible for managing the security related to their content. For example, you are responsible for the following:

Choosing a Region for AWS resources in accordance with data sovereignty regulations

Implementing data-protection mechanisms, such as encryption and scheduled backups

Using access control to limit who can access your data and AWS resources

Protecting the AWS Root User

When you first access AWS, you begin with a single sign-in identity known as the root user.

To watch the video on protecting the AWS root user, choose the play button.

AWS root user

When you first create an AWS account, you begin with a single sign-in identity that has complete access to all AWS services and resources in the account. This identity is called the AWS root user and is accessed by signing in with the email address and password that were used to create the account. 

AWS root user credentials

The AWS root user has two sets of credentials associated with it. One set of credentials is the email address and password that were used to create the account. This allows you to access the AWS Management Console. The second set of credentials is called access keys, which allow you to make programmatic requests from the AWS Command Line Interface (AWS CLI) or AWS API.

Access keys consist of two parts:

Access key ID: for example, A2lAl5EXAMPLE

Secret access key: for example, wJalrFE/KbEKxE

Similar to a user name and password combination, you need both the access key ID and secret access key to authenticate your requests through the AWS CLI or AWS API. Access keys should be managed with the same security as an email address and password.

Delete your access keys to stay safe!

If you don't have an access key for your AWS account root user, don't create one unless you absolutely need to. If you have an access key for your AWS account root user and want to delete the key, follow these steps:

In the AWS Management Console, navigate to your username in the upper right section of the navigation bar. From the dropdown menu, go to the My Security Credentials page, and sign in with the root user’s email address and password.

Open the Access keys section.

Under Actions, choose Delete.

Choose Yes.

AWS root user best practices

The root user has complete access to all AWS services and resources in your account, including your billing and personal information. Therefore, you should securely lock away the credentials associated with the root user and not use the root user for everyday tasks. Visit the links at the end of this lesson to learn more about when to use the AWS root user.

To ensure the safety of the root user, follow these best practices:

Choose a strong password for the root user.

Enable multi-factor authentication (MFA) for the root user.

Never share your root user password or access keys with anyone.

Disable or delete the access keys associated with the root user.

Create an Identity and Access Management (IAM) user for administrative tasks or everyday tasks.

Multi-factor authentication

When you create an AWS account and first log in to the account, you use single-factor authentication. Single-factor authentication is the simplest and most common form of authentication. It only requires one authentication method. In this case, you use a user name and password to authenticate as the AWS root user. Other forms of single-factor authentication include a security pin or a security token.

However, sometimes a user’s password is easy to guess. For example, your coworker Bob’s password, IloveCats222, might be easy for someone who knows Bob personally to guess, because it’s a combination of information that is easy to remember and includes certain facts about Bob (Bob loves cats, and his birthday is February 22). If a bad actor guessed or cracked Bob’s password through social engineering, bots, or scripts, Bob might lose control of his account. Unfortunately, this is a common scenario that users of any website often face. This is why using multi-factor authentication (MFA) is important in preventing unwanted account access.

MFA requires two or more authentication methods to verify an identity. To learn more about the three categories of information that MFA pulls from, flip each of the following flashcards by choosing them.

Front of card

Something you know

Click to flip

Back of card

Something you know, such as a user name and password or pin number

Click to flip

Front of card

Something you have

Click to flip

Back of card

Something you have, such as a one-time passcode from a hardware device or mobile app

Click to flip

Front of card

Something you are

Click to flip

Back of card

Something you are, such as a fingerprint or face scanning technology

Click to flip

With a combination of this information, systems can provide a layered approach to account access. So even if the first method of authentication, like Bob’s password, is cracked by a malicious actor, the second method of authentication, such as a fingerprint, provides another level of security. This extra layer of security can help protect your most important accounts, which is why you should activate MFA on your AWS root user.

MFA on AWS

If you activate MFA on your root user, you must present a piece of identifying information from both the something you know category and the something you have category. The first piece of identifying information the user enters is an email and password combination. The second piece of information is a temporary numeric code provided by an MFA device.

Using MFA adds an additional layer of security because it requires users to use a supported MFA mechanism in addition to their regular sign-in credentials. Activating MFA on the AWS root user account is an AWS best practice.

Supported MFA devices

AWS supports a variety of MFA mechanisms, such as virtual MFA devices, hardware time-based one-time password (TOTP) tokens, and FIDO security keys. To learn more, take a look at the table below. For instructions on how to set up each method, see the Resources section.

DeviceDescriptionSupported DevicesVirtual MFAA software app that runs on a phone or other device that provides a one-time passcode. These applications can run on unsecured mobile devices, and because of that, they might not provide the same level of security as hardware or FIDO security keys.Twilio Authy Authenticator, Duo Mobile, LastPass Authenticator, Microsoft Authenticator, Google Authenticator, Symantec VIPHardware TOTP tokenA hardware device, generally a key fob or display card device, that generates a one-time, six-digit numeric code based on the time-based one-time password (TOTP) algorithm.Key fob, display cardFIDO security keys

FIDO-certified hardware security keys are provided by third-party providers such as Yubico. You can plug your FIDO security key into a USB port on your computer and enable it using the instructions that follow.

FIDO Certified products

(opens in a new tab)

AWS Identity and Access Management

Authentication answers the question, "Are you who you say you are?" Authorization answers the question, "What actions can you perform?"

To watch the video on identity and access management, choose the play button.

Authentication and authorization

When you configure access to any account, two terms come up frequently: authentication and authorization. Although these terms might seem basic, you must fully understand them to properly configure access management on AWS.

Authentication

When you create your AWS account, you use the combination of an email address and a password to verify your identity. If a user types in the correct email address and password, the system assumes the user is allowed to enter and grants them access. This is the process of authentication.

Authentication ensures that the user is who they say they are. User names and passwords are the most common types of authentication. But you might also work with other forms, such as token-based authentication or biometric data, like a fingerprint. Authentication simply answers the question, “Are you who you say you are?”

Authorization

After you’re authenticated and in your AWS account, you might be curious about what actions you can take. This is where authorization comes in. Authorization is the process of giving users permission to access AWS resources and services. Authorization determines whether a user can perform certain actions, such as read, edit, delete, or create resources. Authorization answers the question, “What actions can you perform?” 

What is IAM?

AWS Identity and Access Management (IAM) is an AWS service that helps you manage access to your AWS account and resources. It also provides a centralized view of who and what are allowed inside your AWS account (authentication), and who and what have permissions to use and work with your AWS resources (authorization).

With IAM, you can share access to an AWS account and resources without sharing your set of access keys or password. You can also provide granular access to those working in your account, so people and services only have permissions to the resources that they need. For example, to provide a user of your AWS account with read-only access to a particular AWS service, you can granularly select which actions and which resources in that service that they can access.

IAM features

To help control access and manage identities in your AWS account, IAM offers many features to ensure security.

To learn more, expand each of the following six categories.

Global

Integrated with AWS services

Shared access

Multi-factor authentication

Identity federation

Free to use

IAM user

An IAM user represents a person or service that interacts with AWS. You define the user in your AWS account. Any activity done by that user is billed to your account. When you create a user, that user can sign in to gain access to the AWS resources inside your account.

You can also add more users to your account as needed. For example, for your cat photo application, you could create individual users in your AWS account that correspond to the people who are working on your application. Each person should have their own login credentials to prevent sharing credentials between users.

IAM user credentials

An IAM user consists of a name and a set of credentials. When you create a user, you can provide them with the following types of access:

Access to the AWS Management Console

Programmatic access to the AWS CLI and AWS API

To access the console, provide the user with a user name and password. For programmatic access, AWS generates a set of access keys that can be used with the AWS CLI and AWS API. IAM user credentials are considered permanent, which means that they stay with the user until there’s a forced rotation by admins.

When you create an IAM user, you can grant permissions directly at the user level. This can seem like a good idea if you have only one or a few users. However, as the number of users increases, keeping up with permissions can become more complicated. For example, if you have 3,000 users in your AWS account, administering access and getting a top-level view of who can perform what actions on which resources can be challenging.

Fortunately, you can group IAM users and attach permissions at the group level.

IAM groups

An IAM group is a collection of users. All users in the group inherit the permissions assigned to the group. This makes it possible to give permissions to multiple users at once. It’s a more convenient and scalable way of managing permissions for users in your AWS account. This is why using IAM groups is a best practice.

If you have an application that you’re trying to build and you have multiple users in one account working on the application, you might organize the users by job function. For example, you might organize your IAM groups by developers, security, and admins. You could then place all your IAM users into their respective groups.

This provides a way to see who has what permissions in your organization. It also helps you scale when new people join, leave, and change roles in your organization.

Consider the following examples:

A new developer joins your AWS account to help with your application. You create a new user and add them to the developer group, without thinking about which permissions they need.

A developer changes jobs and becomes a security engineer. Instead of editing the user’s permissions directly, you remove them from the old group and add them to the new group that already has the correct level of access.

Keep in mind the following features of groups:

Groups can have many users.

Users can belong to many groups.

Groups cannot belong to groups.

The root user can perform all actions on all resources inside an AWS account by default. This is in contrast to creating new IAM users, new groups, or new roles. To allow an IAM identity to perform specific actions in AWS, such as implement resources, you must grant the IAM user the necessary permissions.

The way you grant permissions in IAM is by using IAM policies.

IAM policies

To manage access and provide permissions to AWS services and resources, you create IAM policies and attach them to an IAM identity. Whenever an IAM identity makes a request, AWS evaluates the policies associated with them. For example, if you have a developer inside the developers group who makes a request to an AWS service, AWS evaluates any policies attached to the developers group and any policies attached to the developer user to determine if the request should be allowed or denied.

IAM policy examples

Most policies are stored in AWS as JSON documents with several policy elements. The following example provides admin access through an IAM identity-based policy.

This policy has four major JSON elements: Version, Effect, Action, and Resource.

The Version element defines the version of the policy language. It specifies the language syntax rules that are needed by AWS to process a policy. To use all the available policy features, include "Version": "2012-10-17" before the "Statement" element in your policies.

The Effect element specifies whether the policy will allow or deny access. In this policy, the Effect is "Allow", which means you’re providing access to a particular resource.

The Action element describes the type of action that should be allowed or denied. In the example policy, the action is "*". This is called a wildcard, and it is used to symbolize every action inside your AWS account.

The Resource element specifies the object or objects that the policy statement covers. In the policy example, the resource is the wildcard "*". This represents all resources inside your AWS console.

Putting this information together, you have a policy that allows you to perform all actions on all resources in your AWS account. This is what we refer to as an administrator policy.

The next example shows a more granular IAM policy.

This policy uses a Deny effect to block access to Amazon S3 actions, unless the Amazon S3 resource that's being accessed is in account 222222222222. This ensures that any Amazon S3 principals are accessing only the resources that are inside of a trusted AWS account.

IAM roles

IAM best practices

Throughout this lesson, you have learned about some IAM best practices. This section summarizes some of the most important IAM best practices that you must be familiar with before building solutions in AWS. 

To learn more about each best practice, expand each of the following six categories. 

Lock down the AWS root user

Follow the principle of least privilege

Use IAM appropriately

Use IAM roles when possible

Consider using an identity provider

Regularly review and remove unused users, roles, and other credentials

---
## [defineprogramming/kahoothacks](https://github.com/defineprogramming/kahoothacks)@[a76abe517c...](https://github.com/defineprogramming/kahoothacks/commit/a76abe517c88a9e6b537c6fe78afa40f39d3065e)
#### Sunday 2023-07-02 07:12:12 by Leo Cooper

Merge pull request #1 from defineprogramming/pr/smol-dev/ejwo0y

Create a Python-based suite with 15+ Kahoot hacks controlled in the terminal, featuring a clean interface and user-friendly experience.

---
## [n-buckley/react-clone-instagram](https://github.com/n-buckley/react-clone-instagram)@[243ef4a641...](https://github.com/n-buckley/react-clone-instagram/commit/243ef4a641b1a73458e0531670d4fdc19837ec4f)
#### Sunday 2023-07-02 07:58:58 by n-buckley

add: init react typescript app

`npx create-react-app APP-NAME --template typescript`

Starting off strong 😅 ... not.

honestly im not sure why i decided typescrip versus just plain react... still dont know but thats what were rolling with

anyway the project goes on!!!

**current road map in my head is**
1.   hard code instagram homepage design.
- adendum: this includes basic responseive features like liking a picture, likes increasing.... i dont know hwot his is gonan work later with having differntmultiple users but ill figure it out i think.... maybe i should postpone this idk darn
2.  then have it able to accept props.
3.  then hook it up to a DB ?? (i say this like i know what I'm talking about... I dont) so that the front page is reponsive.
4.  hard code user pages/ feeds
5.  have it accept props + the DB will already be connected ? so just integrate
6.  ummm i think maybe here we should slpit by having a login for differnt users. **maybe i should set up a dummy login page FIRST** so that there can at least be different users... this seems like abetter idea actually. ok so we'll make the login page real this time where there has to be UQ usernames and passwords in the DB

ok this is as far as my brain thinking goes, not super detail oriented plan but... i dont really know what im doing! (will anyone besides me ever read this? -- i hope so)

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[697583ebca...](https://github.com/TaleStation/TaleStation/commit/697583ebca2c7c0d36b146d4f92e1f7610dcff50)
#### Sunday 2023-07-02 08:01:24 by TaleStationBot

[MIRROR] [MDB IGNORE] Duiffel Spotfix (#6551)

Original PR: https://github.com/tgstation/tgstation/pull/76442
-----
## About The Pull Request

Gives duffelbags their proper slot count
They inherited this from backpacks, but I sorta just forgot about that

[Creates "levels" of locked objects, uses that to make locked duffels
work](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

[c613c00](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

Turns locked into something that holds defines, this makes life a lot
easier.
Requires a lot of boilerplate because of how many uses of these procs
there are and all the passthrough and shit.

Adds a few outfit subtypes to avoid this class of failure in future.

Renames the args in a few but not all touched procs, one thing at a time

Closes #76407
Closes #76430 Had the lock check in the wrong place
Closes #76441 GOD I HATE TK SO MUCH

Wrote half the pr without glasses so if it's weird gimme some grace
yeah?

## Changelog
:cl:
fix: Fixes some fuck with duffelbags, them not holding enough + issues
with spawning gear in them (job shit and all)
/:cl:

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Rishi0627/simon-game](https://github.com/Rishi0627/simon-game)@[e40d7ef2b9...](https://github.com/Rishi0627/simon-game/commit/e40d7ef2b98bf72970f35c9f51037a453ed188b7)
#### Sunday 2023-07-02 08:32:56 by Rishi0627

Add files via upload

"The Simon Game is a classic electronic memory game brought to life as a web application. Built using HTML, CSS, and JavaScript, this project offers an interactive and engaging experience for players of all ages. The game challenges players to repeat a series of randomly generated patterns of colors and sounds, testing their memory and concentration skills. With its user-friendly interface and responsive design, the Simon Game provides hours of entertainment and fun. Try your hand at this nostalgic game and see if you can beat the high score!"

---
## [andresgutgon/dotfiles](https://github.com/andresgutgon/dotfiles)@[96eaf94840...](https://github.com/andresgutgon/dotfiles/commit/96eaf948408ab2ac6d579aaede3b61d46f758124)
#### Sunday 2023-07-02 10:40:02 by andresgutgon

Introduce nvim-dap (Debugger Adapter Protocol) to my NVim
I want to be able to debug Node apps (Specially NextJS) app on backend
side. nvim-dap use DAP protocol from Microsoft which is the one used by
VSCode on their debugging experience. This is the same in Nvim.

To be honest this has been fucking painful for several reasons.
1. First Next.js latest version has fucked their debugging experience.
   So I had to simplify the problem and first understand how node
   `--inspect` flag works on a simple Node server. Then I look into
   existing issues on Next.js and I discoverd that their debugging
   experience is broken in latest version. A [fix is comming in this PR](https://github.com/vercel/next.js/pull/51467)
2. Second. After setting the `nvim-dap` plugin with the VSCode / JS
   debugging experience I spent a shameful amount of time hitting
   `node-terminal` debug mode when in reality was `pwa-node`. Yes, `pwa`
   is ultra weird and that took me time to figure out. [Issue here about
   it](https://github.com/microsoft/vscode/issues/151910)

FUCK! This was hard :joy:

---
## [Megha-Bahuguna/joke-generator](https://github.com/Megha-Bahuguna/joke-generator)@[2907d0e4d5...](https://github.com/Megha-Bahuguna/joke-generator/commit/2907d0e4d538f42441bfb15c95ff7f66e46600e5)
#### Sunday 2023-07-02 11:21:54 by Megha-Bahuguna

Create README.md

Whether you need a quick chuckle or a belly laugh, my Joke Generator has got you covered. The cleverly crafted code behind it ensures a never-ending supply of rib-tickling jokes, leaving you in stitches every time.

---
## [newstools/2023-the-sun-nigeria](https://github.com/newstools/2023-the-sun-nigeria)@[dfe840ce30...](https://github.com/newstools/2023-the-sun-nigeria/commit/dfe840ce303f19ca87548d16fdaa350a2afbb3d1)
#### Sunday 2023-07-02 11:32:21 by Billy Einkamerer

Created Text For URL [sunnewsonline.com/i-imbibed-giving-spirit-from-my-parents-sunky-o-luxury-and-experiential-lifestyle-guru/]

---
## [Fluffy-Frontier/FluffySTG](https://github.com/Fluffy-Frontier/FluffySTG)@[9e523715ac...](https://github.com/Fluffy-Frontier/FluffySTG/commit/9e523715acd373ce1a74bdc8f9c2fe422c2ad61e)
#### Sunday 2023-07-02 12:44:55 by SkyratBot

New planetary exclusive random event/unfavorable situation, Chasmic Earthquake [MDB IGNORE] (#21778)

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

## About The Pull Request

https://github.com/tgstation/tgstation/assets/28870487/2451bc69-db1e-420d-9a18-2f899ca65427

This introduces a new unfavorable situation (non-antagonist random
events that dynamic triggers under certain circumstances), restricted to
planetary maps (Icebox). An earthquake occurs, felt by everyone on the
map, forming a fault that tears the a hole somewhere on the station.

The fault zone is indicated by shaking tiles, which gives a chance
(about 30 seconds) for you to move your machinery/property/crewmembers
out of the way. If you're on those tiles when the fault forms, get ready
to take a nasty fall.

Anything caught in the fault zone as it collapses inward will be
destroyed, violently, _before_ being dropped down into the z-level
below.

![image](https://github.com/tgstation/tgstation/assets/28870487/56916c9f-c8da-4ffb-9d8b-7e940e92bbc2)

These can also happen as a random event, however their rarity is on-par
with that of a meteor storm.

This also adds a helper for finding a midpoint turf between two provided
turfs, thanks to ZephyrTFA.

This idea basically possessed me over the course of a few days, and I
found myself unable to work on anything else until I had it complete.
I'm glad its done.
## Why It's Good For The Game

Gives Icebox its own big "environmental disaster" event. I'm hoping it
isn't received as being too destructive, but mind that this is meant to
be an equal to the dreaded meteor storm.

Also makes it so that unfavorable events aren't a coinflip between a
portal storm/rod on planetary maps.
## Changelog
:cl: Rhials
add: Chasmic Earthquake random event, exclusive to Icebox. Tears a huge
chasm in the hull of the station. Watch out for shaking tiles!
sound: Adds sounds for distant rumbling, metal creaking, and rubble
shaking.
imageadd: Achievement icon for getting sucked up in an earthquake chasm.
/:cl:

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [sthagen/skorch-dev-skorch](https://github.com/sthagen/skorch-dev-skorch)@[df92d4d5e3...](https://github.com/sthagen/skorch-dev-skorch/commit/df92d4d5e3cc5991330e339d6c8d6c83798f0caa)
#### Sunday 2023-07-02 12:49:13 by Benjamin Bossan

Allow regression with 1d targets (#974)

* Allow regression with 1d targets

This change makes it possible to pass a 1-dimensional y to
`NeuralNetRegressor`.

Problem description

Right now, skorch requires the `y` passed to `NeuralNetRegressor.fit` to
be 2-dimensional, even if there is only one target, as is the most
common case. This problem has come up a few times in the past, but
mostly it's just an annoyance - just do `y.reshape(-1, 1)` and you're
good (the error message says as much).

There are, however, also cases where it's not so easy to solve. For
instance, in #972, a user reports that they cannot use skorch with
sklearn's `BaggingRegressor`. The problem is that even if `y` is
reshaped, once it is passed to the net from `BaggingRegressor`, it is 1d
again. I assume that `BaggingRegressor` internally squeezes `y` at some
point.

This PR lifts the 2d restriction check.

Initial motivation

Why does skorch require `y` to be 2d? I couldn't remember the initial
reasoning and did some archeology.

I found this comment:

(https://github.com/skorch-dev/skorch/commit/2f00e2570460fe0a6acd8db94c4d8624b3ddd1eb#diff-66ed08bca4d171889565d0285a36b9b47e0e91e3b33d85c51352d8eb00faefac):

>         # The problem with 1-dim float y is that the pytorch DataLoader will
>         # somehow upcast it to DoubleTensor

This strange behavior should not be an issue anymore, so if that was the
only problem, we should be able to just remove the constraint, right?

Problems with removing the constraint

Unfortunately, it's not that easy. The issue comes down to the
following: When we remove the constraint and allow the target `y` to be
1d, but the prediction `y_pred` is still 2d, the criterion `nn.MSELoss`
will probably do the wrong thing. What exactly is wrong? Instead of
calculating the squared error for each sample pair, the criterion
will broadcast the vector and calculate _all squared errors_ between
each sample, then return the mean of that. To demonstrate, let's remove
the reduction step and look at the shape:

```python
>>> import torch
>>> criterion = torch.nn.MSELoss(reduction='none')
>>> y = torch.rand(100)
>>> y_pred = torch.rand((100, 1))
>>> y.shape, y_pred.shape
(torch.Size([100]), torch.Size([100, 1]))
>>> se = criterion(y_pred, y)
/home/vinh/anaconda3/envs/skorch/lib/python3.10/site-packages/torch/nn/modules/loss.py:536: UserWarning: Using a target size (torch.Size([100])) that is different to the input size (torch.Size([100, 1])). This will likely lead to incorrect results due to broadcasting. Please ensure they have the same size.
  return F.mse_loss(input, target, reduction=self.reduction)
>>> se.shape
torch.Size([100, 100])
```

As can be seen, PyTorch broadcasts the two arrays, leading to 100x100
errors being calculated. Thankfully, PyTorch warns about potential
issues with that.

The current solution is to accept this behavior and hope that the users
will indeed see the warning. If they don't see it or ignore it, it could
be a huge issue, because they still get a loss scalar and might even see
a small improvement in the loss during training. But the model will not
converge and it's going to be a huge pain to debug the bug, if it's even
identified as such.

Just to be clear, existing code, which uses 2d targets, will not be
affected by the change introduced in this PR and is still the preferred
way (IMO) to use regression in skorch.

Rejected solutions

I did consider the following solutions but rejected them.

Raising an error when shapes mismatch

This would remove the risk of users missing the warning. The problem
with this is that mismatching shapes can be okay in certain
circumstances. Some criteria don't expect target and prediction to have
the same shape, so we would need to check based on criterion. Moreover,
theoretically, users may indeed want to broadcast. Raising an error
would prevent that and users may have to resort to subclassing to
circumvent the error.

Automatic reshaping

We could automatically add/remove dimensions if we see that they
mismatch. This has the same problems as the previous solution regarding
the dependence on the type of criterion. Furthermore, automatic
adjustment of the user's output is prone to run into issues in some edge
cases (e.g. when the broadcasting is actually desired).

* Fix error when initializing BaggingRegressor

For Python 3.7, CI got:

TypeError: __init__() got an unexpected keyword argument 'estimator'

for BaggingRegressor. Probably it installs an older version of sklearn,
which uses a different argument name. Passing as positional arg should
fix it.

* Reviewer comment: typo

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

* Reviewer comment: typo

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

---------

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

---
## [rockydirtbag/mage](https://github.com/rockydirtbag/mage)@[496faaf5cb...](https://github.com/rockydirtbag/mage/commit/496faaf5cb9ff47066178d08e9cb6e252bd7454a)
#### Sunday 2023-07-02 13:25:06 by Susucre

[LTR] Implement The Balrog, Durin's Bane (#10515)

* [LTR] Implement The Balrog, Durin's Bane

I could use someone more experienced for this card:
Should the watcher `PermanentsSacrificedWatcher` be initialized locally in the card's class, or is a global initializing in GameImpl.java alright? I went for the latter for now, as my base for implementing the static cost reduction was Blood for the Blood God!

* apply review

* no longer instantiate watcher on every game.

---
## [ZecHub/zechub](https://github.com/ZecHub/zechub)@[8d7c522bea...](https://github.com/ZecHub/zechub/commit/8d7c522bea40a7cc2e28d2e7bf9eea86cdfaffdd)
#### Sunday 2023-07-02 13:34:13 by Hardaeborla

zecweekly.md

# ZecWeekly #49
$656M lost from crypto hacks, Kraken Compelled to Share User Data, Investors still waiting on $1.9M Refund 

Curated by "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

---

### Welcome to ZecWeekly
Hello Zcashers!! Welcome to another exciting edition of our weekly newsletter where we share recent news happening in the Crypto space and information latest happening about ZCash ecosystem. You can also be a contributor on ZecHub by visiting our [site](https://wiki.zechub.xyz/contribute) 

In this week newsletter, we will be exploring recent happenings in the ZCash Ecosystem including the ECC Transparency Report. You'll also be learning about different transaction model on the ZCash ecosystem including recent developments in the Crypto Space. 
---

## This Week's Education Piece 
In this week Educational Piece you'll be learning more about different pools existing on the ZCash Network and utilizing the best practices when it comes to selecting the required pools for transaction. Learn more about this via the link below 👇👇
[ZCash Value Pools](https://wiki.zechub.xyz/zcash-value-pools) 


## Zcash Updates


#### ECC & ZF Updates

[ECC shares Transparency Report](https://twitter.com/ElectricCoinCo/status/1674825997206667288?t=Zn9dB-KZOfAktomH8fkSIg&s=19) 

[ECC Shares Insights on Zcashd package signing keys](https://twitter.com/ElectricCoinCo/status/1674177380213051393?t=Dn0Jpxt1YEpyCY87I6Y4AA&s=19) 

[The ZF Engineering Team Discusses about Zebra](https://twitter.com/ZcashFoundation/status/1674481431337115648?t=vsHN1xkRdlz96oaGvTtV1g&s=19) 

[Zcash Arborist Call Summarised by Jason](https://twitter.com/zksquirrel/status/1674568125688193028?t=eC8iYguak-Zi0AXn4SlFoQ&s=19) 

[Upgrade to Zcash 5.6.1](https://twitter.com/zcash_community/status/1674569168690065410?t=nqPzbqAzoMEf1HFfx6JY3Q&s=19) 





#### Zcash Community Grants Updates

[The Results Are In](https://forum.zcashcommunity.com/t/zcg-committee-election-june-2023/44668/35?u=Hardaeborla) 

[ZecHub Shares Report of Monthly Activities](https://forum.zcashcommunity.com/t/zechub-monthly-updates/44101/22?u=Hardaeborla) 


#### Community Projects

[Learn More About ZCash via ZCash Hub](https://twitter.com/zcash/status/1674090119085662214?t=oSMxAiLRNs9OzfWdo6mkRQ&s=19) 

[ZFAV Monthly Meetup](https://twitter.com/ZFAVClub/status/1674056270716760064?t=j15J36xCGQJPxwM7zZ_wIg&s=19) 

[Zcash Crusader from Chapter 1 - 4](https://twitter.com/ZcashCrusader/status/1673562963955810304?t=kVnAFnkX1aoFA4kJ0-WhHA&s=19) 

[Zcash Nigeria host ZCash Meetup for Nigerians](https://twitter.com/ZcashNigeria/status/1673654414689677318?t=PEAwDj4tE_OzY-D1l_LXyg&s=19) 

[Support the campaign Zcon4 Events](https://twitter.com/robmarn/status/1673840426212634626?t=f6yDhW8StnqhMQjMzN2d6Q&s=19) 

[Zcash Español host ZCash Meetup](https://twitter.com/lbcbmtl/status/1673746471445749772?t=IL1xaiqb8k9Cqxmih_oySw&s=19) 

[Zast EP 003 Now Available](https://twitter.com/ZcastEsp/status/1673853524185104384?t=j3AIucX3QRKZhAH_FXNo9w&s=19) 

[ZecHub Got Featured](https://twitter.com/ZecHub/status/1674819584476561419?t=tuPzJEADW8wM_qeVIqhHPw&s=19) 

[Zcash Brazil Host another Quiz - ZEC on Discod](https://twitter.com/zcashbrazil/status/1674901050854088704?t=7ZtDYZdpwzRCzZ4DbgzmNw&s=19) 

[Zcash Español Rewards POAP To Active Users](https://twitter.com/zcashesp/status/1674946127391600641?t=pZBVFOeEQI7Sw1K5R_4cMg&s=19) 

[Having Issues with Zingo?](https://twitter.com/ZingoLabs/status/1674931179231797248?t=yygLx7JVwBGpStwTHTpa4w&s=19) 

[Get to know more about @robmarn](https://twitter.com/zcashesp/status/1674943397860081671?t=fcGA7b7KFm6wFen_HeOFvQ&s=19) 

[Learn More about Zebra Implementation](https://twitter.com/zcashbrazil/status/1673724361629396993?t=EpsxKY7E2ZBtt0rMqetiIA&s=19) 

[Check out ZCash Brazil New DP](https://twitter.com/zcashbrazil/status/1673509298624688130?t=hy3YsFFxrvRxm5IlMNGAug&s=19) 













#### News & Media

[Investors still waiting on $1.9M refund Logan Paul promised 6 months ago](https://cointelegraph.com/news/investors-still-waiting-on-refund-logan-paul-promised-six-months-ago) 

[Kraken ordered by court to disclose user data to IRS for tax compliance](https://cointelegraph.com/news/kraken-ordered-by-court-disclose-user-data-irs-tax-compliance) 

[$656M lost from crypto hacks, scams and rug pulls in H1 2023](https://www.google.com/amp/s/cointelegraph.com/news/656m-lost-from-crypto-hacks-scams-and-rug-pulls-in-h12023-report/amp) 

[Bitcoin price has never lost more than 10% in July](https://cointelegraph.com/news/bitcoin-price-never-lost-july-2023-different) 

[Redditor up 25% after boldly taking out $59K worth of personal loans to buy BTC](https://cointelegraph.com/news/redditor-up-25-after-boldly-taking-out-59k-worth-of-personal-loans-to-buy-btc) 





## Some Zcash Tweets
[Check Out this ZCash Mud Designs](https://twitter.com/mad_paiement/status/1674430123007946755?t=jwYVkKwVbleRZDmNXw71hQ&s=19) 

[Zero Knowledge is the future of Blockchains](https://twitter.com/michae2xl/status/1674438977820999681?t=pySy98i0U1_OUTLq7svC3g&s=19) 

[Check out this beautiful ZCash Art] (https://twitter.com/ZcashAI/status/1674427111325712386?t=ZEVMBjiMquQxCUQv5E1kow&s=19) 

[Privacy is Normal Explained in Español](https://twitter.com/doloresampaio/status/1674929536205504513?t=MHpoKv1FoHe9n81DWhza3g&s=19) 

[A Zcasher Explains Why He Holds ZEC] (https://twitter.com/Crypto2Ye/status/1674815229014810631?t=2BXRD2ArTxz-1BBjsZWoMA&s=19) 

[@fillzorkillz advices ZCash community](https://twitter.com/fillzorkillz/status/1674157761565958149?t=OJxeGTZyqxcSdHtc-hprOw&s=19) 

[Zooko Commends Zingo Labs Team](https://twitter.com/zooko/status/1672699602733088768?t=WgW6TDE6x3Rwn1J5HuVl4A&s=19) 

[Nate shares Insight on Binance Privacy Coin Reversal Decision](https://twitter.com/nate_zec/status/1673751414957559809?t=jG8COIQbNqRywsQqMX5c8g&s=19) 

[A Friendly Reminder About ZCash](https://twitter.com/Lexaleth/status/1674625667202179072?t=YutAa5vF-geSBxbR4hri8Q&s=19) 












## Zeme of the Week
[https://twitter.com/JackGavigan/status/1673790256439492608?t=cehze_6ZMcSymqdTJGxeQQ&s=19](https://twitter.com/JackGavigan/status/1673790256439492608?t=cehze_6ZMcSymqdTJGxeQQ&s=19) 

## Jobs in the Ecosystem

- [Executive Head of Product, ECC](https://apply.workable.com/electric-coin-company/j/6ACEC09B90/)

- [Director of Security, ECC](https://apply.workable.com/electric-coin-company/j/E68A4C20E2/)

---
## [Crezy-haker/New](https://github.com/Crezy-haker/New)@[d41114b22f...](https://github.com/Crezy-haker/New/commit/d41114b22fcecebd173d22b71c94747807abe3da)
#### Sunday 2023-07-02 13:40:15 by Akash Evan

DCODER-PRO

#DCODER-PRO 🌼

# FUCK YOUR BYPASS SYSTEM MADARXUD🖕🤞

---
## [rohanmehta98/Research-paper](https://github.com/rohanmehta98/Research-paper)@[8f170d46fb...](https://github.com/rohanmehta98/Research-paper/commit/8f170d46fb50405fd71ae2772d2b8894513e692e)
#### Sunday 2023-07-02 13:47:27 by rohanmehta98

Research paper file

The main purpose of this research is to investigate the perception of  youth on the use of social media in politics. In this research, a comprehensive literature review has been conducted on research ideas based on similar content of the use of social media in politics. Five variables, such as voting behaviour, perceived usefulness, ease of use, political participation and personalization politics have been used to investigate the youth perception regarding the research objectives. In this research positivism research philosophy and descriptive approach has been followed for primary data collection and analysis. Quantitative statistical tools have been used to find out actual results from the study. Frequencies analysis, correlation,  mean, median and mode have been used to evaluate data. From the analysis, it has been found that the use of social media in politics has a robust impact on the political behaviour of youth on social media. It positively affective the voting behaviour of youth and pursue them to participate in various political activities. The finding of this study reveals that the use of social media in politics has a significant impact on the voting behaviour of people who are using social media in political communication. This research also found that politically interested people get needed information on social media and they get updated about political activities and new policies. The usefulness of social media has a positive impact on the use of social media by youth in political activities. This study also found that social media is easy to use and need less effort to perform communication activities. This pursues youth to use social media in political participation. Another finding is that the use of social media in politics increase youth participation in political activities. The traditional form of communication has a lack of access by the general people. But, digital media allow people to participate in decision making and criticism. This facilitates youth participation in political activities.
We would like to give our first deepest appreciation to Christine Tidåsen, who has supported us through this research by providing proper guidelines throughout our complete research process with unlimited patient and support. Then we would like to give our sincere thanks and respect to Professor Anders Pehrsson, who also supported by giving effective and informative guidelines and suggestions and his quality knowledge in the research process. Finally, we would like to provide thanks to our friends and family for their support and encouragement through this research process.
 Keywords: Social Media, Politics, Political Participation, Voting Behaviour, ease of use, perceived usefulness.

---
## [milovangudelj/next.js](https://github.com/milovangudelj/next.js)@[6238f8a5c0...](https://github.com/milovangudelj/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Sunday 2023-07-02 14:36:32 by Jimmy Lai

performance: don't compile on hover on dev (#51830)

An annoying issue that slows down compilation times in dev for Next is
that we might trigger compilation of a page via hover on app.

We do this because we want the same experience in production and dev and
the prefetching is important for instantaneous loading states.

The alternative in this PR is that we don't prefetch at all anymore in
dev but instead, when we handle navigation, we can force a prefetch
navigation.

The slight compromise with this approach is that you can't test
prefetching anymore in dev.


<!-- Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change(s) that you're making:

## For Contributors

### Improving Documentation

- Run `pnpm prettier-fix` to fix formatting issues before opening the
PR.
- Read the Docs Contribution Guide to ensure your contribution follows
the docs guidelines:
https://nextjs.org/docs/community/contribution-guide

### Adding or Updating Examples

- The "examples guidelines" are followed from our contributing doc
https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md
- Make sure the linting passes by running `pnpm build && pnpm lint`. See
https://github.com/vercel/next.js/blob/canary/contributing/repository/linting.md

### Fixing a bug

- Related issues linked using `fixes #number`
- Tests added. See:
https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md

### Adding a feature

- Implements an existing feature request or RFC. Make sure the feature
request has been accepted for implementation before opening a PR. (A
discussion must be opened, see
https://github.com/vercel/next.js/discussions/new?category=ideas)
- Related issues/discussions are linked using `fixes #number`
- e2e tests added
(https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Documentation added
- Telemetry added. In case of a feature if it's used or not.
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md


## For Maintainers

- Minimal description (aim for explaining to someone not on the team to
understand the PR)
- When linking to a Slack thread, you might want to share details of the
conclusion
- Link both the Linear (Fixes NEXT-xxx) and the GitHub issues
- Add review comments if necessary to explain to the reviewer the logic
behind a change

### What?

### Why?

### How?

Closes NEXT-
Fixes #

-->

link NEXT-1317

---
## [DragonSurvivalTeam/DragonSurvival](https://github.com/DragonSurvivalTeam/DragonSurvival)@[618202cf54...](https://github.com/DragonSurvivalTeam/DragonSurvival/commit/618202cf540b5b61f0885b614cce678078cc8cb5)
#### Sunday 2023-07-02 14:44:10 by Viktoria Ershova

Merge pull request #336 from SiverDX/fixes

> Set up the mod, will do the Curse Forge stuff once this is merged (since it depends on the harvest changes)
> 
> This PR now affects the following:
> 
> ### Fixed some issues regarding abilities (GUI)
> * Tooltip coloring for increasing levels
> * Experience gained from decreasing was 1 level lower than intended
> * There were 2 additional SkillProgressButtons being rendered (but overlayed by other buttons)
> * Right side of the experience cost for abilities had the wrong start location
> * When increasing or decreasing ability levels all were shown as obtainable (until screen was re-opened)
> 
> ### Other
> * Removed bad omen application when you kill a knight (only occurred as a non-dragon)
> * Fixed some issue with water cauldron block (sea dragon gained no good mana condition from it)
> 
> ### Fixed a bug with the Claws and Teeth description
> * The harvest level text was not accurate (starting from gold? it was 1 level too high)
> 
> ### Fixed issues with harvesting
> * Modded ore support for drops when only using paws (most modded ores should already work but this fixes certain other instances, mostly MCreator related)
> * Config for bonusUnlockedAt is now respected
> * ServerConfig.baseHarvestLevel is now actually used
> * Minimum level for base and bonus level is now 0 (wood)
> * When the tool in the claw inventory breaks block-breaking will no longer desync
> * Block breaking speed is only applied if the dragon is effective against the block (e.g. cave dragon can mine pickaxe-blocks faster but not shovel-blocks)
> 
> ### Removed Better Combat animation compatibility
> (This will not cause Better Combat to now crash with Dragon Survival - that was a separate issue)
> 
> * Removed config

---
## [0xcha05/langchain](https://github.com/0xcha05/langchain)@[75fb9d2fdc...](https://github.com/0xcha05/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Sunday 2023-07-02 14:48:35 by Stefano Lottini

Cassandra support for chat history using CassIO library (#6771)

### Overview

This PR aims at building on #4378, expanding the capabilities and
building on top of the `cassIO` library to interface with the database
(as opposed to using the core drivers directly).

Usage of `cassIO` (a library abstracting Cassandra access for
ML/GenAI-specific purposes) is already established since #6426 was
merged, so no new dependencies are introduced.

In the same spirit, we try to uniform the interface for using Cassandra
instances throughout LangChain: all our appreciation of the work by
@jj701 notwithstanding, who paved the way for this incremental work
(thank you!), we identified a few reasons for changing the way a
`CassandraChatMessageHistory` is instantiated. Advocating a syntax
change is something we don't take lighthearted way, so we add some
explanations about this below.

Additionally, this PR expands on integration testing, enables use of
Cassandra's native Time-to-Live (TTL) features and improves the phrasing
around the notebook example and the short "integrations" documentation
paragraph.

We would kindly request @hwchase to review (since this is an elaboration
and proposed improvement of #4378 who had the same reviewer).

### About the __init__ breaking changes

There are
[many](https://docs.datastax.com/en/developer/python-driver/3.28/api/cassandra/cluster/)
options when creating the `Cluster` object, and new ones might be added
at any time. Choosing some of them and exposing them as `__init__`
parameters `CassandraChatMessageHistory` will prove to be insufficient
for at least some users.

On the other hand, working through `kwargs` or adding a long, long list
of arguments to `__init__` is not a desirable option either. For this
reason, (as done in #6426), we propose that whoever instantiates the
Chat Message History class provide a Cassandra `Session` object, ready
to use. This also enables easier injection of mocks and usage of
Cassandra-compatible connections (such as those to the cloud database
DataStax Astra DB, obtained with a different set of init parameters than
`contact_points` and `port`).

We feel that a breaking change might still be acceptable since LangChain
is at `0.*`. However, while maintaining that the approach we propose
will be more flexible in the future, room could be made for a
"compatibility layer" that respects the current init method. Honestly,
we would to that only if there are strong reasons for it, as that would
entail an additional maintenance burden.

### Other changes

We propose to remove the keyspace creation from the class code for two
reasons: first, production Cassandra instances often employ RBAC so that
the database user reading/writing from tables does not necessarily (and
generally shouldn't) have permission to create keyspaces, and second
that programmatic keyspace creation is not a best practice (it should be
done more or less manually, with extra care about schema mismatched
among nodes, etc). Removing this (usually unnecessary) operation from
the `__init__` path would also improve initialization performance
(shorter time).

We suggest, likewise, to remove the `__del__` method (which would close
the database connection), for the following reason: it is the
recommended best practice to create a single Cassandra `Session` object
throughout an application (it is a resource-heavy object capable to
handle concurrency internally), so in case Cassandra is used in other
ways by the app there is the risk of truncating the connection for all
usages when the history instance is destroyed. Moreover, the `Session`
object, in typical applications, is best left to garbage-collect itself
automatically.

As mentioned above, we defer the actual database I/O to the `cassIO`
library, which is designed to encode practices optimized for LLM
applications (among other) without the need to expose LangChain
developers to the internals of CQL (Cassandra Query Language). CassIO is
already employed by the LangChain's Vector Store support for Cassandra.

We added a few more connection options in the companion notebook example
(most notably, Astra DB) to encourage usage by anyone who cannot run
their own Cassandra cluster.

We surface the `ttl_seconds` option for automatic handling of an
expiration time to chat history messages, a likely useful feature given
that very old messages generally may lose their importance.

We elaborated a bit more on the integration testing (Time-to-live,
separation of "session ids", ...).

### Remarks from linter & co.

We reinstated `cassio` as a dependency both in the "optional" group and
in the "integration testing" group of `pyproject.toml`. This might not
be the right thing do to, in which case the author of this PR offer his
apologies (lack of confidence with Poetry - happy to be pointed in the
right direction, though!).

During linter tests, we were hit by some errors which appear unrelated
to the code in the PR. We left them here and report on them here for
awareness:

```
langchain/vectorstores/mongodb_atlas.py:137: error: Argument 1 to "insert_many" of "Collection" has incompatible type "List[Dict[str, Sequence[object]]]"; expected "Iterable[Union[MongoDBDocumentType, RawBSONDocument]]"  [arg-type]
langchain/vectorstores/mongodb_atlas.py:186: error: Argument 1 to "aggregate" of "Collection" has incompatible type "List[object]"; expected "Sequence[Mapping[str, Any]]"  [arg-type]

langchain/vectorstores/qdrant.py:16: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:19: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:20: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:22: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:23: error: Name "grpc" is not defined  [name-defined]
```

In the same spirit, we observe that to even get `import langchain` run,
it seems that a `pip install bs4` is missing from the minimal package
installation path.

Thank you!

---
## [Mozasbugs/iHearU](https://github.com/Mozasbugs/iHearU)@[56f0bf9f46...](https://github.com/Mozasbugs/iHearU/commit/56f0bf9f46e9f636d95f29c87ed821408d32ce89)
#### Sunday 2023-07-02 15:23:06 by Mohamed Ezz

Create Text to ASL

Text-to-American Sign Language (ASL) Conversion
This component of the project enables users to enter text and convert it into American Sign Language (ASL) animations. The application provides a user-friendly interface where individuals can type their desired message into an input field and initiate the translation process by clicking the "Translate" button.

Features
Input Field: The application includes an input field where users can enter the text they wish to convert into ASL animations.

Translation Process: Upon clicking the "Translate" button, the entered text is processed by the system, which converts it into the corresponding ASL gestures.

Avatar Animation: An animated avatar, equipped with an animator controller, performs the ASL gestures associated with the translated text. The avatar's animations are synchronized with the interpreted ASL gestures to provide an interactive and engaging experience for the user.

Usage
Open the application on your device.

Locate the text input field within the user interface.

Enter the desired text that you wish to convert into ASL animations.

Click the "Translate" button to initiate the conversion process.

Observe the avatar on the screen as it performs the ASL gestures associated with the translated text.

Enjoy the interactive ASL animations and explore the possibilities of communicating through sign language.

Development
The text-to-ASL conversion component utilizes a combination of Unity3D, C#, and machine learning techniques. The underlying processes involve the following steps:

Text Processing: The input text is validated and processed to ensure compatibility with the ASL translation algorithm. Any potential errors or empty inputs are handled gracefully, providing a smooth user experience.

ASL Gesture Recognition: The processed text is then converted into the appropriate ASL gestures using a deep learning model trained on a custom dataset. The model recognizes the textual representation of the gestures and maps them to corresponding animations.

Avatar Animation: The ASL gestures are linked to a library of animation clips, which are synchronized with the avatar's movements. The animator controller facilitates the seamless transition between animations, ensuring an accurate portrayal of ASL gestures.

Future Enhancements
The text-to-ASL conversion component forms an integral part of this graduation project. While it provides the basic functionality of converting text into ASL animations, there are several potential areas for improvement and expansion:

Real-time Translation: Implementing real-time translation capabilities, where the avatar performs animations as the user types, would enhance the interactive experience.

Customization Options: Adding options for avatar customization, such as different clothing styles or personalization settings, would allow users to create avatars that reflect their individuality.

Gesture Library Expansion: Expanding the gesture library by including more ASL gestures and variations would increase the versatility and usefulness of the application.

Accuracy Optimization: Continuously refining the deep learning model's accuracy and performance through additional training and fine-tuning techniques would improve the overall translation quality.

---
## [jgudec/android_kernel_samsung_exynos2200](https://github.com/jgudec/android_kernel_samsung_exynos2200)@[379618197b...](https://github.com/jgudec/android_kernel_samsung_exynos2200/commit/379618197bb17f72ba4f8e2e6777708070858ef7)
#### Sunday 2023-07-02 15:55:00 by Serge Semin

clk: vc5: Fix 5P49V6901 outputs disabling when enabling FOD

[ Upstream commit c388cc804016cf0f65afdc2362b120aa594ff3e6 ]

We have discovered random glitches during the system boot up procedure.
The problem investigation led us to the weird outcomes: when none of the
Renesas 5P49V6901 ports are explicitly enabled by the kernel driver, the
glitches disappeared. It was a mystery since the SoC external clock
domains were fed with different 5P49V6901 outputs. The driver code didn't
seem like bogus either. We almost despaired to find out a root cause when
the solution has been found for a more modern revision of the chip. It
turned out the 5P49V6901 clock generator stopped its output for a short
period of time during the VC5_OUT_DIV_CONTROL register writing. The same
problem was found for the 5P49V6965 revision of the chip and was
successfully fixed in commit fc336ae622df ("clk: vc5: fix output disabling
when enabling a FOD") by enabling the "bypass_sync" flag hidden inside
"Unused Factory Reserved Register". Even though the 5P49V6901 registers
description and programming guide doesn't provide any intel regarding that
flag, setting it up anyway in the officially unused register completely
eliminated the denoted glitches. Thus let's activate the functionality
submitted in commit fc336ae622df ("clk: vc5: fix output disabling when
enabling a FOD") for the Renesas 5P49V6901 chip too in order to remove the
ports implicit inter-dependency.

Fixes: dbf6b16f5683 ("clk: vc5: Add support for IDT VersaClock 5P49V6901")
Signed-off-by: Serge Semin <Sergey.Semin@baikalelectronics.ru>
Reviewed-by: Luca Ceresoli <luca@lucaceresoli.net>
Link: https://lore.kernel.org/r/20220929225402.9696-2-Sergey.Semin@baikalelectronics.ru
Signed-off-by: Stephen Boyd <sboyd@kernel.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [MHaris-Dev/Netflix_Clone](https://github.com/MHaris-Dev/Netflix_Clone)@[c22eed9711...](https://github.com/MHaris-Dev/Netflix_Clone/commit/c22eed97115f30a0d6ab1724c16aa9fcfee8b19f)
#### Sunday 2023-07-02 16:55:20 by Muhammad Haris

Netflix Clone

Project Description: Netflix Clone

Are you a fan of streaming movies and TV shows? Do you dream of creating your own streaming platform like Netflix? Look no further because we have an exciting project that will bring your dream to life!

Introducing the Netflix Clone project, a remarkable endeavor that aims to replicate the popular features and functionalities of the world's leading streaming service. This project, available on GitHub, provides an opportunity for aspiring developers and streaming enthusiasts to delve into the world of online entertainment.

By analyzing the provided link in-depth, we discover a treasure trove of code and resources that form the backbone of this captivating project. The simplicity of the project is evident as it offers a user-friendly interface, making it accessible even to those with limited programming experience.

Using the power of HTML, CSS, and JavaScript, this project mimics the visually stunning and seamless user experience offered by Netflix. The carefully crafted design elements capture the essence of the original platform, ensuring an immersive and engaging viewing experience for users.

This project provides an excellent learning opportunity for developers, enabling them to explore the intricacies of front-end development, responsive design, and the integration of APIs. By examining the code and understanding its structure, aspiring developers can gain valuable insights into the inner workings of a sophisticated streaming platform.

What sets this project apart is its commitment to simplicity and ease of use. The developer has taken great care to ensure that the code is well-documented and easy to comprehend, allowing developers to navigate and modify it effortlessly. This means that even if you're new to web development, you can jump right in and start exploring this exciting project.

Whether you're a student looking to expand your programming skills, an aspiring entrepreneur with dreams of launching your streaming service, or simply a passionate movie lover, this Netflix Clone project is the perfect opportunity to explore the world of streaming technology.

So, what are you waiting for? Dive into the provided link, unravel the secrets of this captivating project, and embark on an exhilarating journey to create your own streaming platform. The possibilities are endless, and the world of online entertainment awaits your creative touch.

Join us now and let your imagination run wild with the Netflix Clone project!

---
## [SirPowder/mapUON](https://github.com/SirPowder/mapUON)@[e6372d4c4c...](https://github.com/SirPowder/mapUON/commit/e6372d4c4c09ea610a0b8fb9d402ba0599ff4510)
#### Sunday 2023-07-02 17:13:35 by PennSylvannia

holy fuck its october

my life is slipping away like sand through an hour glass
its exceptionally unpleasant and wedged in my ass

---
## [rafay99-epic/evals](https://github.com/rafay99-epic/evals)@[14f8771c40...](https://github.com/rafay99-epic/evals/commit/14f8771c4015a2c70cc1c8f4f8197d8911fd2971)
#### Sunday 2023-07-02 17:19:45 by oscar

[Eval] Add Chinese Homophonic  (#1169)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Understand Chinese Homophonic 

### Eval description

We have found some popular homophonic sentences on the Internet,
including the Chinese pronunciation of English words and homophones, and
provide several options for the model to determine which option matches
the homophonic sentence the best.

### What makes this a useful eval?

Chinese homophonic puns are a widely popular internet cultural
phenomenon that generates humor by utilizing the homophonic
relationships between Chinese characters. These puns are typically
spread in text form on social media, forums, and messaging applications,
and they are extremely common in China's online culture.

Homophonic puns have a wide range of applications, encompassing ordinary
daily life scenarios as well as hot news events, entertainment gossip,
and political current affairs. These puns frequently appear in internet
memes, jokes, advertising slogans, and short videos, garnering
significant popularity among young people and internet users.

For those unfamiliar with them, homophonic puns may seem like encrypted
text, making it difficult to grasp the true intention behind them.
However, understanding them allows for the establishment of strong
connections between individuals and facilitates smooth communication.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"一天小鸭对小鸡表白:小鸡，我爱你。小鸡:你duck不必。这句话中的\"duck\"是什么意思？\nA. 鸭子\nB. 大可"}],
"ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"丑的人才有对象，美的卖空调。这句话中的\"美的\"是什么意思？\nA. 漂亮的\nB. 空调公司"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"我是一只小绵羊，我今天剪毛了，我失绵了。这句话中的\"失绵\"表达意思？\nA. 失眠\nB. 没有了羊毛"}], "ideal":
["A"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"以后我的吉祥物决定就是你了，螃蟹！——因为，你有钱（钳）。这句话中的\"钳\"是什么意思？\nA. 有钱\nB. 螃蟹的钳子"}],
"ideal": ["A"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"女孩对爸爸说\"爸比，我们去哪啊\"爸爸没听见，妈妈笑了一下，女孩对妈妈说\"妈比，你笑什么\"妈妈打了她一巴掌。妈妈为什么打她？\nA.
她提出了不合理的要求\nB. 她骂人了"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"天气这么热，我们总会熟的。这句话中的\"熟的\"是什么意思？\nA. 热熟了\nB. 熟悉了"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"我好像胖了，没事我陪你减肥，我们戒荤叭。这句话中的\"戒荤\"是什么意思？\nA. 吃素食\nB. 结婚"}], "ideal":
["B"]}
  ```
</details>

---------

Co-authored-by: oscar <oscar@hellotalk.com>

---
## [rafay99-epic/evals](https://github.com/rafay99-epic/evals)@[90587b6e5c...](https://github.com/rafay99-epic/evals/commit/90587b6e5ce970b0c957c57ec18d7adcdeef26be)
#### Sunday 2023-07-02 17:19:45 by Juyeon Yoon

Add Korean honorific sentence classification eval (#1181)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

korean-honorific

### Eval description

Evaluates LLMs on the task of classifying Korean honorific/non-honorific
sentences.

### What makes this a useful eval?

The Korean language has an intricate system of honorifics, or speech
levels, that reflect social hierarchy, age, relationship, and level of
respect or formality. The use of honorifics is deeply ingrained in
Korean culture and plays a crucial role in social communication.
Understanding and accurately classifying Korean honorifics can pose a
number of challenges due to the intricacy and contextual nuances of the
system. However, it is critical in achieving accurate and culturally
sensitive translation, transcription, and interpretation of the Korean
language.

Currently the even the most advanced GPT-4 model is struggling to
correctly classify the honorific and non-honorific sentences: for
example, "어머니께서 잘 계시는지 말해줘" has a casual, non-honorific tone, but
misclassified as "honorific" presumably due to the intermediate
postposition "께서".

Tracking the ability of evolving language models on this task would be
helpful to estimate the degree of advances over time, as well as the
task itself would be fruitful for non-Koreans to figure out the nuances
of Korean conversation.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "그분이 잘 계시는지 물어봐
줘."}], "ideal": "non-honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "이 공원에서 자주
걷습니다."}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "자주 드시나요?"}],
"ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "아니요, 접점은 없지만
개인적으로 관심이 있습니다."}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "당신의 취미가
무엇인가요?"}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "꼭 모으길 바랄게."}],
"ideal": "non-honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "그러면 나도
준비해야겠다."}], "ideal": "non-honorific"}
  ```
</details>

---
## [rafay99-epic/evals](https://github.com/rafay99-epic/evals)@[9edc150dde...](https://github.com/rafay99-epic/evals/commit/9edc150dde3489c67a8990a2c5a6e694fb3fc012)
#### Sunday 2023-07-02 17:19:45 by Chen Zhao

[Eval] Chinese lantern riddles (#1176)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

chinese-lantern-riddles

### Eval description

This evaluation tests the model's performance in solving Chinese lantern
riddles, which are based on the shape, pronunciation, and meaning of
Chinese characters.

### What makes this a useful eval?

Lantern riddles are a traditional Chinese festive activity that involves
multiple participants guessing riddles together. Apart from being a part
of festival celebrations, lantern riddles can also serve as an
educational tool to help Chinese language learners enhance their
vocabulary and language reasoning. Through the process of unraveling the
riddles, students can also develop their logical thinking and reasoning
skills, as well as nurture their imagination and creativity. Lantern
riddles can also spark students' interest in language learning and make
the learning experience more enjoyable.

Although LLMs are able to some extent to decompose Chinese characters
into parts, as mentioned in #511, they still face challenges when it
comes to solving riddles. In most cases, GPT 3.5 cannot reason correctly
about the structure of Chinese characters. For instance, the riddle
"上下一体（打一字）" can be interpreted as a combination ("一体") of "上" and "下",
resulting in the answer "卡". However, GPT 3.5 gives the wrong answer,
"升", with a reason that makes no sense. A similar situation occurs when
GPT 3.5 reasons about the pronunciation of Chinese characters, with one
of its explanations stating that the pronunciation of "盼（pàn）" is
similar to the pronunciation of "俄（é）", which is entirely incorrect.
However, on the positive side, GPT 3.5 shows good performance when a
riddle only encodes meaning and does not require reasoning about the
structure and pronunciation.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n一撇（打一字）。"}], "ideal": ["厂"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n内里有人（打一字）。"}], "ideal":
["肉"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n二三四五六七八九（打一成语）。"}], "ideal":
["缺衣少食"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n谜底在山东（打一国家名）。"}], "ideal":
["秘鲁"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n身穿红衣，常年哨放，遇紧急事，往火里闯（打一日常用品）。"}],
"ideal": ["灭火器"]}
  ```
</details>

---
## [rafay99-epic/evals](https://github.com/rafay99-epic/evals)@[c675067906...](https://github.com/rafay99-epic/evals/commit/c67506790626630debd6e3ab74eda1b1851ac6a2)
#### Sunday 2023-07-02 17:19:45 by robin luo

[eval] Chinese Idioms evulation (#1163)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name
chinese_idioms


### Eval description

Check the model's ability to recognize Chinese idioms, which are words
that have different meanings from its original meaning.

### What makes this a useful eval?

The Chinese idioms in website is interesting and commonly used by a lot
of Chinese people. However, the GPT4 and GPT3.5 fail to explain the
meaning of the idioms with a correct explanation.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ x] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ x] Check that your data is in `evals/registry/data/{name}`
- [ x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ x] Ensure you have the right to use the data you submit via this
eval

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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ x] I have filled out all required fields of this form
- [x ] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n伟光正"}], "ideal": ["From the idiomatic phrase
'the great, glorious and correct Chinese Communist Party', it can also
refer to a person associated with the Chinese Communist Party."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n赵家人"}], "ideal": ["From Lu Xun's famous
middle-grade novel 'A Q Zhengzhuan', it generally refers to the powerful
and noble class of the Chinese Communist Party. As Xi Jinping came to
power and implemented the Seven No Mentions, the usage of power and red
nobility was suppressed, and folk turned to the Zhao family to refer to
it. Derivations include calling the People's Republic of China 'Zhao'
and Xi Jinping, the current General Secretary of the CPC Central
Committee, 'King Zhao', or replacing the word 'people' with the word
'Zhao family' in the names of various Chinese organs and media
propaganda"]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n改开党/特色党"}], "ideal": ["The term 'Mao Left' is
commonly used by the civil left and Maoist supporters, which originated
from Deng Xiaoping's 'reform and opening up' and 'socialism with Chinese
characteristics'. It is a term of contempt for the Communist Party
during and after the reign of Deng Xiaoping, who believed that the
Communist Party after the reform and opening up only represented the
interests of those in power, not the interests of the people, and that
the economy had been 'restored to capitalism'. The term 'reform and
opening up' and 'special dynasties' have been used to describe the
period after the reform and opening up."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n黄丝/黄尸"}], "ideal": ["The term refers to
non-establishment camps such as the pro-democracy camp and the local
camp in Hong Kong, as well as those who support their stance, and is
named after the yellow ribbon used as a symbol by non-establishment
camps during the 2014 occupation. Since the pronunciation of 'silk' and
'corpse' is similar in both Mandarin and Cantonese, 'yellow corpse' is
used as a term of contempt."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n蟹堡王"}], "ideal": ["The term refers to the
Hong Kong pro-establishment camp, it is often accused of not having a
political stance and just being in line with Beijing"]}
{"input": [{"role": "user", "content": "请解释下面词语的意思,请使用英文回答。\n---\nww"}],
"ideal": ["The term refers to mainland Chinese netizens to refer to
Taiwan or the Republic of China (Taiwan period) (from the superimposed
style, a neutral term). In January 2022, Taiwan Affairs Office
spokesperson Zhu Fenglian said that the word Wanwan is a nickname for
the Taiwanese people 'Mengmeng' by the Chinese mainlanders"]}
  ```
</details>

---
## [rafay99-epic/evals](https://github.com/rafay99-epic/evals)@[936cc9d4ab...](https://github.com/rafay99-epic/evals/commit/936cc9d4abfc0775f1fad1d694690870679f6924)
#### Sunday 2023-07-02 17:19:45 by somerandomguyontheweb

Add Belarusian orthography eval (#1188)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

belarusian-orthography

### Eval description

Test the model's ability to switch between classical and modern
orthographies of Belarusian.

### What makes this a useful eval?

Belarusian is famous for having two Wikipedias:
[one](https://be.wikipedia.org) is using the official modern
orthography, as taught in school, and [another
one](https://be-tarask.wikipedia.org) is using the classical orthography
*Taraškievica*, preferred by some speakers. While the two orthographies
are essentially similar, some words are spelled differently in the
classical orthography, and many loanwords are also pronounced
differently.

This eval contains 125 Belarusian words, representing a wide range of
discrepancies between the two orthographies. The model's task is to
convert each word from the classical orthography to the modern
orthography and vice versa. In my experience with ChatGPT, classical =>
modern spelling conversion is mostly correct, but the model is clueless
when prompted to do modern => classical spelling conversion, even though
the task is simple enough to be handled by a [rule-based
tool](https://gooseob.github.io/taraskevizatar).

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "адрозьненьнем"}], "ideal": "адрозненнем"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"адрозненнем"}], "ideal": "адрозьненьнем"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "ісьляндзкі"}], "ideal": "ісландскі"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"ісландскі"}], "ideal": "ісьляндзкі"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "сымбаль"}], "ideal": "сімвал"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"сімвал"}], "ideal": "сымбаль"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "унівэрсытэт"}], "ideal": "універсітэт"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"універсітэт"}], "ideal": "унівэрсытэт"}
  ```
</details>

---
## [rafay99-epic/evals](https://github.com/rafay99-epic/evals)@[3504c839b4...](https://github.com/rafay99-epic/evals/commit/3504c839b49f0848274c6e66965bbb5239bbf1fd)
#### Sunday 2023-07-02 17:19:45 by jjyuhub

Ordering Randomised VersionList (#1164)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Ordering Randomised VersionList

### Eval description

This evaluation aims to test prompt engineered failure cases to order a
randomised version history list, but causes chronological ordering
failures such as 7.5.2 -> 7.4.2 -> 7.5.1 -> 7.4.1 (**incorrectly
inserted 7.4.2 in between 7.5.2 and 7.5.1** and **incorrectly skipping
over the major release version 7.5.0** in the Explainable AI chain of
thoughts) and 7.5.2 -> 7.5.1 -> 7.5.0 -> 7.4.1 (incorrectly **skipped
over 7.4.2** in the Explainable AI chain of thoughts).

### What makes this a useful eval?
This eval can help identify logical errors when ordering a randomised
version history list. It can also help improve the Explainable AI
feature by providing more accurate and consistent explanations for the
ordering decisions. This eval can also measure the robustness and
reliability of the prompt across different inputs and scenarios.

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
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval is high quality because it causes the succeed rate for a 5
options (ABCDE) multiple choice quiz drop from 20% correct at randomly
selected answers to only 0-6% correct for GPT-3.5-Turbo. These are
prompt engineered failures, causing [bigger failure rates than prior
work](https://arxiv.org/pdf/2305.04388.pdf), as performing so much worse
than random is unnatural for such a super easy task.

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
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
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.0 Release Date: December 02, 2019 Version 7.4.1 Release
Date: October 23, 2019 Version 7.5.1 Release Date: December 18, 2019
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.2 Release Date:
October 31, 2019 What was the version released three versions before
7.5.2? A. 7.4.2 B. 7.5.2 C. 7.5.1 D. 7.4.1 E. 7.5.0"}],"ideal":"A.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.1 Release Date:
October 23, 2019 Version 7.5.0 Release Date: December 02, 2019 Version
7.4.2 Release Date: October 31, 2019 Version 7.5.1 Release Date:
December 18, 2019 What was the version released three versions before
7.5.2? A. 7.5.2 B. 7.5.1 C. 7.4.1 D. 7.4.2 E. 7.5.0"}],"ideal":"D.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.1 Release Date: December 18, 2019 Version 7.5.0 Release
Date: December 02, 2019 Version 7.4.1 Release Date: October 23, 2019
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.2 Release Date:
October 31, 2019 What was the version released three versions before
7.5.2? A. 7.5.0 B. 7.4.2 C. 7.5.1 D. 7.4.1 E. 7.5.2"}],"ideal":"B.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.0 Release Date: December 02, 2019 Version 7.5.1 Release
Date: December 18, 2019 Version 7.4.2 Release Date: October 31, 2019
Version 7.4.1 Release Date: October 23, 2019 Version 7.5.2 Release Date:
January 21, 2020 What was the version released three versions before
7.5.2? A. 7.5.1 B. 7.4.1 C. 7.5.2 D. 7.5.0 E. 7.4.2"}],"ideal":"E.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.4.2 Release Date: October 31, 2019 Version 7.5.1 Release Date:
December 18, 2019 Version 7.5.0 Release Date: December 02, 2019 Version
7.5.2 Release Date: January 21, 2020 Version 7.4.1 Release Date: October
23, 2019 What was the version released three versions before 7.5.2? A.
7.4.1 B. 7.5.2 C. 7.4.2 D. 7.5.0 E. 7.5.1"}],"ideal":"C. 7.4.2"}
  ```
</details>

- The task of ordering a randomised version history list is relatively
simple and straightforward for humans, but the AI system fails to follow
the basic rules of chronological ordering.
- The AI system produces incorrect explanations for its ordering
decisions, such as skipping over major or minor releases, or inserting
versions out of order. These explanations do not match the expected
logic or rationale for ordering a version history list.
- The AI system performs worse than random guessing on a multiple-choice
quiz, which suggests that it is not robust or reliable for this task.

---------

Co-authored-by: jjyuhub <tdq459rcfm@privaterelay.appleid.com>

---
## [rafay99-epic/evals](https://github.com/rafay99-epic/evals)@[9aeee0d71f...](https://github.com/rafay99-epic/evals/commit/9aeee0d71f9f11b0d32cc9090d3ace4572e4ce8a)
#### Sunday 2023-07-02 17:19:45 by Syed Rishad

Add Reasoning with Contradictory Statements Eval (#1184)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Reasoning with Contradictory Constraints

### Eval description

Given a set of logical constraints, the evaluation assesses the LLM's
ability to reason through contradictory information and recognize the
unattainability of a valid solution. The prompt provides clear
instructions and hints at the presence of a hidden contradiction,
challenging the model's understanding of numerical constraints and
logical conflicts.

### What makes this a useful eval?

This evaluation prompt tests the LLM's multi-step reasoning,
domain-specific knowledge, and its capacity to navigate contradictions.
By presenting complex instructions with hidden contradictions, it
challenges the model to identify logical conflicts and limitations,
providing valuable insights into its reasoning abilities.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "Please generate a list of
numbers that satisfies the following constraints: 1. The sum of all
numbers in the list must be 100. 2. None of the numbers in the list can
be greater than 10. 3. At least one number in the list must be greater
than 50."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Design a seating arrangement
for a dinner party with the following constraints: 1. The seating
arrangement should accommodate 10 guests. 2. None of the guests should
sit next to each other. 3. At least two guests must sit next to each
other."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Generate a sequence of colors
that fulfills the following criteria: 1. None of the colors can be blue.
2. At least half of the colors must be shades of blue. 3. The total
number of colors should be odd."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Plan a menu for a special
event that adheres to the following guidelines: 1. None of the dishes
can contain dairy products. 2. At least half of the dishes must be
dairy-based. 3. The total number of dishes should be even."}],"ideal":
"A"}
{"input": [{"role": "system", "content": "Create a schedule for a
conference day with the following constraints: 1. No two events can take
place at the same time. 2. At least two events must occur
simultaneously. 3. The total number of events should be odd."}],"ideal":
"A"}
  ```
</details>

---
## [rafay99-epic/evals](https://github.com/rafay99-epic/evals)@[5c0b4ec185...](https://github.com/rafay99-epic/evals/commit/5c0b4ec185485119adbd3d3cc8aea1b930724b28)
#### Sunday 2023-07-02 17:19:45 by Lorenzo

[Eval] Determine a gear rotation given a layout (#1136)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

gears_rotation

### Eval description

Checks the model's ability to determine the rotation of a gear given a
disposition of multiple gears and the rotation of one of them.

### What makes this a useful eval?

Test if the model is able to "visualize" the arrangement of objects (in
this case of gears) and to think logically about how the rotation of one
specific gear in the grid can affect the rotation of the others.
Gpt3.5 had an accuracy of 0.16 (4/25 right). Gpt4 (chatgpt plus
subscription) seems to fail in the same places as 3.5. They seem to be
able to place the gears in the correct places inside the grid, but fail
the logical part. Among many prompts, both were asked about the
direction of rotation of a gear whose rotation has already been
previously told. However, they still got it wrong.

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
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, each
placed to the left of the other: A-B-C. If gear C is running clockwise,
how is gear C running? Answer clockwise or counterclockwise. No
explanations."}], "ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, each
placed one beneath the other: A-B-C. If gear C is running clockwise, how
is gear B running? Answer clockwise or counterclockwise. No
explanations."}], "ideal": "Counterclockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, placed
diagonally in a 3x3 grid: A-B-C. Gear A is placed in the top-right, gear
B is placed at the center and gear C is placed in the bottom-left
corner. They don't touch each other. If gear C is running clockwise, how
is gear A running? Answer clockwise, counterclockwise or \"not moving\".
No explanations."}], "ideal": "not moving"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, placed
diagonally in a 3x3 grid: A-B-C. Gear A is placed in the top-right, gear
B is placed at the center and gear C is placed in the bottom-left
corner. If gear C is running clockwise, how is gear A running? Answer
clockwise, counterclockwise or \"not moving\". No explanations."}],
"ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotational direction of gears that are of the same
dimensions. Your working area is a 4x4 grid. The place will be given
using a hexadecimal notation (0123456789abcdef) the order in which they
are given will correspond with the positions of these gears. The first 4
char are placed on the first row from left to right. The 5th to 8th on
the second row always from left to right and so on. You will be also
given the rotation of a specific gear. You must be able to determine how
another specific gear is rotating. Answer clockwise or counterclockwise.
No explanations. Don't even use punctuation."}, {"role": "user",
"content": "a1c5e8f7932b46d0, gear 4 is running clockwise. How about
gear d?"}], "ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotational direction of gears that are of the same
dimensions. Your working area is a 3x3 grid. You'll be given 9 numbers,
those will correspond with the positions of these gears. The first 3
given numbers are placed on the first row from left to right. The 4th to
6th are on the second row, always from left to right. Same with the
7th-9th on the third row. You will be also given the rotation of a
specific gear. You must be able to determine how another specific gear
is rotating. Answer clockwise or counterclockwise. No explanations.
Don't even use punctuation."}, {"role": "user", "content": "572913864,
gear 2 is rotating counterclockwise. How is number 7 rotating?"}],
"ideal": "Clockwise"}
  ```
</details>

---
## [rafay99-epic/evals](https://github.com/rafay99-epic/evals)@[8b68875b95...](https://github.com/rafay99-epic/evals/commit/8b68875b95129fbc95f44a8c26961c41f6fcda83)
#### Sunday 2023-07-02 17:19:45 by Sean Bird

Simple block puzzles (#1167)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Simple 2-Block Arrangement Puzzles

### Eval description

Two Tetris shapes are given and a desired arrangement of those shapes is
given. The model must arrange the blocks to match the desired shape
outline.

Here's an example of what a prompt/answer would look like: 

![image](https://github.com/openai/evals/assets/13811962/43a9d560-317e-4ef4-9677-65ee4a491975)

### What makes this a useful eval?

This kind of spatial reasoning is trivial for a human to do. It should
also be a piece of cake for a generally-intelligent AI model.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval was programatically generated and thus can easily be tweaked
to be more difficult, to test different aspects of spatial reasoning, or
to generate more cases. I [wrote a
script](https://github.com/birdsean/tetris-puzzle-eval-generator) to
generate this eval that anyone can come in and adjust.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nF \nFF\n F\n\n U\nUUU\n\n\nPlease create:\n\n
XX \nXXXXX \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " UF \nUUUFF \n F"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nGG\nGG\n\nK \nKK\n K\n\n\nPlease create:\n\nX
\nXX \n X \nXX \nXX\n\nReplacing the 'X's with the corresponding letter
of the shape that should occupy each position. Only respond with the
final shape, no commentary."}], "ideal": "K \nKK \n K \nGG \nGG"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nLLL\n L \n\n F\nFF\n F\n\n\nPlease create:\n\n
XXXX \nXX X \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " FLLL \nFF L \n F"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nWWW\n W\n\n E\nEE\nE \n\n\nPlease create:\n\n
X \nXX \nX \nXXX \n X\n\nReplacing the 'X's with the corresponding
letter of the shape that should occupy each position. Only respond with
the final shape, no commentary."}], "ideal": " E \nEE \nE \nWWW \n W"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nSS\nSS\n\n N\nNN\n N\n\n\nPlease create:\n\n
XXX \nXXXX \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " NSS \nNNSS \n N"}
  ```
</details>

---
## [AndyCodes3000/AndyCodes](https://github.com/AndyCodes3000/AndyCodes)@[0d593d1653...](https://github.com/AndyCodes3000/AndyCodes/commit/0d593d16538d838986f018808c37fcd62269aec3)
#### Sunday 2023-07-02 18:01:51 by AndyCodes3000

Add files via upload

The data that I was given was from Kaggle.com.

Suicide is an unfortunate outcome that some individuals experience, leading them to end their lives. With the data provided, I aimed to identify any patterns or trends in the rising or declining rates of suicides around the world. I began by organizing and cleaning the data. Interestingly, I observed that from 1985 to 1995, suicide rates increased, but after that period, they started to decrease. This led me to question the factors that might have contributed to this trend. Could it be a decrease in technology usage or a more stable economy? There could be various unknown variables that played a role in the decline.

I compared my findings to other sources such as (https://www.cdc.gov/mmwr/volumes/66/wr/mm6630a6.htm) and found that the data aligned with existing research. My goal was to build a neural network model, but due to the lack of comprehensive data on the root causes of suicide, I was not able to achieve significant success. Nonetheless, I am grateful to have gained knowledge and awareness of this serious issue.

Looking beyond the provided data, I investigated the period from 2016 to the present and noticed a sudden increase in suicide rates. Unfortunately, I couldn't find reliable raw data to validate this observation. It leaves me wondering if the change could be attributed to shifting societal standards, mental health issues, social acceptance, or economic downturns in individuals' lives.

In conclusion, if you or someone you know is facing a tough situation, don't hesitate to seek help. It is a sign of strength to ask for support. Let us all stay connected and spread awareness about this important issue. Thank you for reading.

---
## [devkajalsharma/Random-Joke-Generator](https://github.com/devkajalsharma/Random-Joke-Generator)@[01ac5c61c9...](https://github.com/devkajalsharma/Random-Joke-Generator/commit/01ac5c61c97f9c3f17ea066a78d7ba001f2d2d80)
#### Sunday 2023-07-02 18:37:28 by kajal sharma

Add files via upload

The Random Joke Generator is an entertaining and lighthearted project that aims to bring joy and laughter to users by generating random jokes on demand. It leverages the power of artificial intelligence and natural language processing techniques to deliver a diverse range of jokes across various categories.
html,css and javascript are used to create it

---
## [prodirus/TaleStation](https://github.com/prodirus/TaleStation)@[e1d9198bcd...](https://github.com/prodirus/TaleStation/commit/e1d9198bcde79e44d14e1054cfdd75e13e73b6b0)
#### Sunday 2023-07-02 18:40:15 by TaleStationBot

[MIRROR] [MDB IGNORE] Converts del logging to proper json, using json objects instead of building a text file (#5969)

Original PR: https://github.com/tgstation/tgstation/pull/75636
-----

## About The Pull Request

It's easier to parse, and makes more sense when you read it. This way
I'll never have to add yet another case to my parser for someone
changing where a space goes or something.

Moves qdel into its own category cause the old name looked ugly (yell if
this is dumb)
Added a bitfield to entries pulled from categories, adds a new flag that
enables pretty printing json lists.


## Why It's Good For The Game

IMPROVES my workflow

## Changelog
:cl:
server: del logging is now done by outputting to a json file again, but
this time we're using ACTUAL json and not just a big text string with
newlines and shit
/:cl:

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [qwelyt/waddle](https://github.com/qwelyt/waddle)@[27c3c7d6bc...](https://github.com/qwelyt/waddle/commit/27c3c7d6bc0b5a437a453371afb4d3791d53e8ad)
#### Sunday 2023-07-02 19:50:11 by FB

2 add onhold (#6)

* Add wrapper for keys

To be able to deal with keys that should trigger directly and keys that
should happen when on hold I have added a wrapper type for keys. This
makes it a lot easier to determine what kind of key it is. The other
option was to do `enum Key {OnHold(Box<Key>, u8, Box<Key>), ...}` which
is a lot more of a mess than adding the wrapper.

All keys are currently `Instant` and the keyboard acts like before the
change.

#2

* Start playing with OnHold

Trying to figure out how to properly trigger the correct thing to
happen. It was a harder nut than I thought to crack.

#2

* Set release time to max on init

The promicro panicked if u8::MAX was set in the constructor. No idea why
it works if you just do it like this. Seem odd.

* Close to working onhold!

Need to fix de-registering of the onhold if pressed. It should be marked
as released but it's not. The states are off.

* Probably fully working onhold!

It works! At least right now. Will need more testing with other keys and
functions. But it seems to be working.

* Not fully working, but specify limit in ms

For some reason key2 is not sent on its own. This is fine if the key is
a key that need some other key to have an effect, like shift. But if you
do `OnHold(KeyCode(W), 100, KeyCode(P))` you kinda want that P to be
sent after 100ms. No matter if some other key is pressed or not. Very
strange why this is not triggering correctly.

* Fully working onhold!

Scmacki dacki baging `<` vs `>` causing trouble for my checks. In some
places I did `time < limit` and others `time > limit`. This made us not
register when key2 was supposed to be sent. We were in the famous
off-by-one-error. By just flipping the GT-check things now work.
Probably should break that check out into a function just to be sure
that I do correct every time. And then it's only one place to change
should I want to.

* Clean up of work

Clean things up so it looks nicer and don't flash the light all the
time.

* Back to basic layout

* Clean up and comment

---
## [InteractiveNinja/PlexAniSync-Custom-Mappings](https://github.com/InteractiveNinja/PlexAniSync-Custom-Mappings)@[827f6488b5...](https://github.com/InteractiveNinja/PlexAniSync-Custom-Mappings/commit/827f6488b54179c5e3d8c4f21b9ce8a1ff8a82c5)
#### Sunday 2023-07-02 20:28:42 by Soitora

Add multiple series

Bakuman
Black Lagoon
Classroom of the Elite
Ergo Proxy
Fena: Pirate Princess
Frieren
Fullmetal Alchemist & Brotherhood
Jujutsu Kaisen
Kaiju No. 8
Komi Can't Communicate
MASHLE
Monogatari
My Dress-Up Darling
Rent-a-Girlfriend
Skip and Loafer
Mato Seihei no Slave
Steins;Gate & 0
The Promised Neverland
Tokyo Revengers

---
## [vware/android_kernel_qcom_msm8998](https://github.com/vware/android_kernel_qcom_msm8998)@[a2a50bbaa4...](https://github.com/vware/android_kernel_qcom_msm8998/commit/a2a50bbaa44daeef2190b7b818420d90dc52b4c1)
#### Sunday 2023-07-02 21:11:11 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

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
Change-Id: I7d7a39fb554ec0c31f9381f492165f43c70b3924
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
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [JeromeFitz/websites](https://github.com/JeromeFitz/websites)@[e927742292...](https://github.com/JeromeFitz/websites/commit/e927742292832b99f43b1e24311943626b415cbb)
#### Sunday 2023-07-02 21:19:01 by Jerome Fitzgerald

🧨 (revamp) NICE-43 Next RSC, Notion API, & Tailwind [b] [!] (#1621)

# ⚠️ Please Note

This is a bit bigger than I would want, but this is a complete refactor to better utilize a `Notion CMS` within a `Next 13 App` structure taking advantage of `RSC`. And then for good measure started the migration _back_ to `Tailwind` (but now I think `Stitches|Vanilla Extract` are oaky with Next 13).

✨ NICE-43 revamp Next RSC, Notion API, & Tailwind

BREAKING CHANGE: New Notion Implementation through Next 13 RSC (App)

# Complete Refactor for Next RSC

- [x] Redis KV Cache
  - Good for quicker Vercel builds / and reducing Notion random limits
  - Next will still limit due to deduplicated requests
    - Sidenote: Need to get better at _not_ prop-drilling and just calling function again
- [x] Image Component
  - [x] Next Refactor
  - [x] Notion Refactor
- [x] Tailwind
  - [x] Move away from Stitches
  - [x] Temporary move to `@jeromefitz/ds` localized version
  - [x] Radix UI Refactor
  - [x] Use internal Component Library for now
- [x] Notion Refactor

  - [x] Image: Hosted by Notion Expiration Refresh
  - [x] Rely less on custom queries and manipulation, more on out of the box Notion API, React, and Next
    - [x] Move from `nodes` to more straight-forward components
    - [x] Refactor logic for
      - [x] `Column|ColumnList`
      - [x] `ListBulleted|ListItem|ListNumbered`
      - [x] `TextAnnotations`
    - [x] **New**: `Embed|Video`
      - [x] `Embed.Twitter` <= Twitter is self-imploding, so good timing.
      - [x] `Embed.YouTube` <= YouTube is ... no comment.

- [x] Next
  - [ ] `preload` => hold on this for now not working as expected
  - [x] `generateMetadata` => move away from `next-seo` (rip)
    - [ ] Need to re-incorporate `@vercel/og` -- or not temporarily.
  - [x] `generateStaticParams` => hack if `isDev` to stop running all the time :?
  - [x] `not-found` => Instead of customizing every route, use `notFound()`
  - [x] `robots.ts|sitemap.ts` => move away from `next-sitemap` (rip)
- [x] Package Upgrades
  - [x] Basically everything except `plaiceholder|semantic-release|syncpack`
- [x] Other refactors
  - [x] EmojiWrapper
  - [x] Config Packages
    - [x] `./packages/*` – this all needs to be ported to [`@jeromefitz/packages`](https://github.com/JeromeFitz/packages)
      - Was borderline impossible to do these in-tandem (need to get better at `pnpm linking`)
- [x] Fathom advises against custom domains now :/

## Layout

Not to be lost in the backend type stuff but this is a complete rehaul of presentation.

The eventual goal of this `Notion + Next` implementation is you can take the data in any way and display it as you would like. For now though still tightly coupled with a lot of decisions until I can abstract away further. Which -- at teh rate I am going may never happen.

## Notion

Do not "normalize" data from Notion, embrace it.

- This is the CMS why are we going through all the trouble to hack it
- Create new Block Components to match and mimic needs

### Formulas

The "big change" here is utilizing Notion Formulas in the CMS.

#### Slug

Before we had `Slug` now we populated `Slug.Preview` where we are able to have Notion mimic Routes better Server Side than figuring it all out on the fly in `next`.

**Note:** For `Events` we need to manually write the `Slug` for now. The potential clash of having multiple Headline Acts means we could have a url like:

- `../jerome-and,alex-o-jerome`

Which I think _could_ work because we could loop through but also _very_ confusing as a URL to share, haha.

To recap:

- `Slug.Preview` for example will create the matching Next Segment Route
  - Before: `jerome-and` (shows); After: `/shows/jerome-and`
  - Before: `jerome-and` (events); After: `/events/2023/06/16/jerome-and`
  - Before: `homepage` (pages); After: `/`

##### Date

Same here, instead of getting the data from Notion then running through `date-fns`, Notion uses `moment` (I think). So we can do more preparation which makes for a more straight-forward:

```bash
- Date: July 15, 2023 9:00PM
- Date.DayOfMonth: 15
- Date.DayOfMonthOrdinal: 15th
- Date.DayOfWeek: Saturday
- Date.DayOfWeekAbbr: Sat
- Date.DaysUntilEvent: 15
- Date.HoursUntilEvent: 360
- Date.ISO: 2023-07-15T21:00:00-04:00
- Date.Month: 07
- Date.MonthName: July
- Date.MonthNameAbbr: Jul
- Date.Time: 09:00 PM
- Date.Timezone: EDT
- Date.WeekNumber: 28
- Date.Year: 2023
```

## Next

### App

The gains of doing `[[...catchAll]]` for everything at **root** was not worth it. 😅

Especially if we _want_ to be able to change layout, RSC data points and more based on the Segment (Notion Database Type).

So there is some duplication of code throughout but will look into better ways of lifting the "same" stuff.

### Events

Ability to see a range of events depending on Date (say for a week, or a weekend):

- `events/yyyy/mm/dd/to/yyyy/mm/dd`
- `events/2023/06/29/to/2023/07/02`

Props to Katie T. as we came up with this idea in a brainstorm session.

- `events/[from]/to/[to]`
- `events/2023/06/15/to/2023/06/18` (THU-SUN)
- `events/2023/06/29/to/2023/05/01` (Across Months)
- `events/2023/12/28/to/2025/01/07` (Across Years)

Probably need to do something for malformed dates, but I reckon `404` will do that.

Up next would be ideas for `Landing Pages`.

### In-House

`next-seo` and `next-sitemap` will eventually be absorded, or their functionality at least, within `next` itself. This gets the ball rolling on that. They were awesome, and thank you.

Depending on your use case those will still be very valid for use!

## Packages

This just covers the `sites/jeromefitzgerald.com` for now

**Upgrade:**
```bash
@mantine/hooks@6.0.15
@notionhq/client@2.2.6
@radix-ui/...@latest
@upstash/redis@1.22.0
@vercel/og@0.5.8
framer-motion@10.12.18
next@13.4.8-canary.14
react-swipeable@7.0.1
swr@2.2.0

@types/ramda@0.29.3
@types/react@18.2.14
@types/react-dom@18.2.6
@types/uuid@9.0.2
tailwind-merge@1.13.2
```

**Add:**

```bash
emoji-regex@10.2.1
node-emoji@2.1.0
react-headroom@3.2.1 # use framer-motion instead
react-tweet@2.0.2 # 3.x has no release notes

@types/react-headroom@3.2.0
```

**Remove:**

```bash
next-seo
next-sitemap
next-unused
```

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ed57b8127f...](https://github.com/tgstation/tgstation/commit/ed57b8127f1b28507272170c60c7db16f6e02a87)
#### Sunday 2023-07-02 21:25:44 by Jacquerel

Rat RP expansion (#76455)

## About The Pull Request

This fixes a vile and long-standing bug where putting a mouse inside
your hat would not allow the mouse to control your movements, as it
would pop out of the hat whenever it tried to move.
Additionally as a feature this allows a mouse sitting on your head to
convey complicated instructions such as "scream" or "do a flip", via
emoting. Through drift compatibility, the rat's living mech will also
perform this action.

I could have made this into a component but there's no fucking way any
other item is going to have this behaviour, so I didn't.

## Why It's Good For The Game

This feature was already in the game but broken and I want it not to be
broken.
The mouse should be able to control your entire life.

## Changelog

:cl:
fix: Placing a mouse inside your chef hat will once more allow it to
pilot you around.
add: A player-controlled mouse inside your chef hat can compel you to
perform complex actions, such as flipping and spinning. You will obey
because the mouse knows better than you do.
/:cl:

---
## [Addust/Yogstation](https://github.com/Addust/Yogstation)@[465aef0da1...](https://github.com/Addust/Yogstation/commit/465aef0da1b967bf7cb008e7906f5791d81b89cd)
#### Sunday 2023-07-02 21:29:53 by Cark

Some minor changes to space syndicate base. (#19282)

* syndiebuff

* fuck you airlock

* fucking AIRLOCK CONTROLLERS

---
## [noby-y/Infini-Wisp-Calculator](https://github.com/noby-y/Infini-Wisp-Calculator)@[a236dabb98...](https://github.com/noby-y/Infini-Wisp-Calculator/commit/a236dabb98260b729df34ab39e7c8ef4809b75bb)
#### Sunday 2023-07-02 21:59:17 by noby_y

Update README.md

Fuck you Discord and your name policies

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[21411251fd...](https://github.com/effigy-se/effigy-se/commit/21411251fdf3999f59a752caa38b4da6bf81c8e9)
#### Sunday 2023-07-02 22:18:10 by ChungusGamer666

[NO GBP] Fixes my fuckups with species livers (#76331)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76329
I DID A REAL STUPID MISTAKE WHILE CODING
https://github.com/tgstation/tgstation/pull/76184 I AM SORRY
The signal was sending the fucking human instead of seconds_per_tick

## Why It's Good For The Game

Fixes a BUNCH of liver behavior including plasmamen livers not healing
wounds

## Changelog

:cl:
fix: Plasma will now heal plasmamen properly
/:cl:

---
## [abby-1b/Calculator_JJ](https://github.com/abby-1b/Calculator_JJ)@[7d53ad9f96...](https://github.com/abby-1b/Calculator_JJ/commit/7d53ad9f96fb86b4c766d08bb64cec0123570832)
#### Sunday 2023-07-02 22:28:27 by Abby.041b

Fixed the ugly-looking border around the page. Seriously, you need to fix these things. This is the stuff that's making your parents want to split up. This is why your dog doesn't want you to pet him. This is why you can't get hard in the bedroom. This is why you're going through all these issues, man. No, you just think its about these jokes but its becoming a serious matter. Ok? Think, these jokes are leading to bigger problems in your life. You need to turn your whole life around, maybe go to guidance, maybe get some help. Jesus fucking Christ man.

---
## [nrootconauto/tos](https://github.com/nrootconauto/tos)@[32c5f6c865...](https://github.com/nrootconauto/tos/commit/32c5f6c865d750f944a06a891c60aa13cf70a9e5)
#### Sunday 2023-07-02 23:09:55 by Me

im going insane
fuck you fuck you fuck you fuck you fuck you fuck you fuck you

---
## [distributivgesetz/tgstation](https://github.com/distributivgesetz/tgstation)@[89a2a7cc3a...](https://github.com/distributivgesetz/tgstation/commit/89a2a7cc3ad48032414a3755864204fed88244de)
#### Sunday 2023-07-02 23:14:01 by carlarctg

Changes syndicate surgery duffelbags to contain advanced tools (#75846)

## About The Pull Request

Changes syndicate surgery duffelbags to contain advanced tools.

In total, they contain
- All advanced surgical tools, alongside the normal ones without an
advanced version
- Sterilizine gel
- Bone gel and surgical tape
- Roller bed
- Straight jacket, muzzle, and MMI

Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

## Why It's Good For The Game

> Changes syndicate surgery duffelbags to contain advanced tools.

> In total, they contain (...)

The only real reason to buy this item is for the increased storage space
the duffelbag gives, and I find that a little sad. Surgical tools are
plentiful, as they can either be lathed from cargo, medbay, or just
taken. A surgeon, the role that *should* thematically need this the
most, has absolutely no reason to take it. Now they do! A full set of
advanced tools is certainly something that can be considered for
purchase, especially with all the bonus items in here - which might just
allow a traitor to repair their bones if they're heavily wanted and
licking their wounds in maintenance. The TC cost has been increased to 4
to compensate.

> Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

Similar to above, but instead, the reasoning is that nukies really do
not have a lot of time to do surgery. A lot of the 20 minutes of prep
time in War is spent figuring out what you're buying with your
exorbitant amount of TC, in non-War you don't really want to delay the
mission for five minutes for surgery, and its hassle means that most
people do not really want to bother with things like nerve threading,
etc. due to the large, annoying time cost.

> The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

The former is because, well, what the hell, why didn't it have one!
Removing the loose tools gave me the space for it. The latter is just me
realizing that empty closet is weird and lame and so I gave it some
fluff contents to give it a reason to exist.

## Changelog

:cl:
add: Changes syndicate surgery duffelbags to contain advanced tools,
sterilizine, surgical tape, and a roller bed.
add: Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.
add: The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.
/:cl:

---
## [Higgin/Skyrat-tg](https://github.com/Higgin/Skyrat-tg)@[0cd356125a...](https://github.com/Higgin/Skyrat-tg/commit/0cd356125ad5f6e144a18f9da586699a94dd154a)
#### Sunday 2023-07-02 23:57:08 by SkyratBot

[MIRROR] Fixes a sneaky antag tell with RDS / adds policy support [MDB IGNORE] (#21881)

* Fixes a sneaky antag tell with RDS / adds policy support (#76071)

## About The Pull Request

Fixes being able to tell you are a special role via RDS

Adds policy support to RDS

## Why It's Good For The Game

Someone informed me that RDS was a 100% accurate antag tell you rolled a
delayed spawn antag (like headrev), and that's... a little bad, you can
usually insinuate you may be a headrev but straight up knowing isn't
ideal - doesn't keep everyone on equal playing field.

And while I was there I was like "y'know people might want to set policy
for this" so yeah

## Changelog

:cl: Melbert
fix: Fixed a cheeky way RDS revealed you were an antag before you
actually got antag. Sorry, you know who you are.
config: RDS now has policy.json support, to allow customization of the
roundstart "anti-grief" message.
/:cl:

* Fixes a sneaky antag tell with RDS / adds policy support

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---

