## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-13](docs/good-messages/2023/2023-09-13.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,401,886 were push events containing 3,669,885 commit messages that amount to 281,181,491 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 64 messages:


## [bgyss/bevy](https://github.com/bgyss/bevy)@[44f677a38a...](https://github.com/bgyss/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Wednesday 2023-09-13 00:00:36 by Sélène Amanita

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
## [blueDev2/tgstation](https://github.com/blueDev2/tgstation)@[dd8d13d8bc...](https://github.com/blueDev2/tgstation/commit/dd8d13d8bcc6f1fbd6bcdd534a044f7d30c800d7)
#### Wednesday 2023-09-13 00:34:06 by carlarctg

Several common 'household' reagents can be used as improvised medicine treatment. Updated first aid analyzer information. (#77746)

## About The Pull Request

Several common 'household' reagents can be used as improvised medicine
treatment.

Drinking tea will help mend (non-bone) wounds over time.

Flour and corn starch may be splashed onto wounds to help dry them up,
though they'll have a negative effect on burn wounds.

Added a new reagent, saltwater, made by combining table salt with water.

Table salt and saltwater can be splashed onto wounds as well, reducing
bleeding and improving sanitization and disinfection significantly.
However, the coarse undiluted salt will irritate the wounds, reducing
clot rate and flesh healing, and both of the reagents will increase a
burn wound's infestation rate.

Altered Table Salt's recipe to just need sodium and chloride. Changed
the recipe of Pentetic Acid and Heparin to need table salt (sodium x
chloride) and thus slightly altered the total output of those reagents
(pentacid went from 5u per reaction to 4u, heparin 4u->3u)

Saline-Glucose Solution now needs 2u of saltwater and 1u of sugar,
meaning the overall recipe should be completely unchanged in practice.
Contact me on discord if any issues arise from these chemical changes!

First aid analyzers now give easy-to-understand direct information, with
the specific recommended treatments bolded in the analysis text. They
also have a 'unique' extra bit of info, telling you about improvised
ways to remedy your wound.
## Why It's Good For The Game

Wounds have a very poor amount of interaction with the rest of the game
and have not had much added to them post-merge, especially in
'improvised' ways to help Not Die to a wound while you crawl your way to
a emergency medkit or medbay. I researched info on this and found some
interesting ideas - some of them I'll have to leave for later because
this PR kept growing out of scope (Improvised bone gel, ice on wounds
which turned into wound temperature mechanics, crutches, a 'suture item'
component refactor...)

As for what this actually does to benefit the game, it allows more
dynamic wound Gameplay as people use first aid analyzers to get
information on treatment when medbay blows up, helps them stabilize by
splashing flour onto themselves before looking for some actual
treatment, helps traitors realize how they can self-treat many crippling
wounds (at risk, of course). It expands treatment options to things
beside medkits and medbay, but always does so in ways that have
downsides that make them not ideal as _treatment_, and more beneficial
as stabilizing before seeking true professional help. This thus
significantly increases the rather shallow depth of wounds as a system
to interact with.

> Several common 'household' reagents can be used as improvised medicine
treatment.

From what I could tell by looking at several sources for each
'realistic' treatment, these are indeed semi-reasonable things that are
done to wounds by some people as household treatment.

It goes without saying that you should **not do any of these things in
real life** without consulting a doctor unless your blood is also
spilling out by the gallon into the floor. All these 'realistic
treatments' have drastic downsides and are meant for the short-term
only. Except the tea.

> Drinking tea will help mend (non-bone) wounds over time.

Tea is healthy, we all know that.

> Flour and corn starch may be splashed onto wounds to help dry them up,
though they'll have a negative effect on burn wounds.

Flour and apparently starch dries wounds up but risks infection. That's
not a thing for blood wounds yet but oh well.

> Table salt and saltwater can be splashed onto wounds as well, reducing
bleeding and improving sanitization and disinfection significantly.
However, the coarse undiluted salt will irritate the wounds, reducing
clot rate and flesh healing, and both of the reagents will increase a
burn wound's infestation rate.

Salt kills bacteria via osmosis, but it also kills your own cells, and
some bacteria like salt.

> Added a new reagent, saltwater, made by combining table salt with
water.

> Altered Table Salt's recipe to just need sodium and chloride. Changed
the recipe of Pentetic Acid and Heparin to need table salt (sodium x
chloride) and thus slightly altered the total output of those reagents
(pentacid went from 5u per reaction to 4u, heparin 4u->3u)

> Saline-Glucose Solution now needs 2u of saltwater and 1u of sugar,
meaning the overall recipe should be completely unchanged in practice.
Contact me on discord if any issues arise from these chemical changes!

I wish I hadn't had to mess with reagents like this, but I needed to
because just adding mixing salt and water caused the saline glucose
recipe to basically split itself into half saltwater half glucose.

I removed the water requirement for table salt (Why did it even have
that, salt ain't wet bro?), made saline-glucose need 2u saltwater and 1u
sugar, and altered relevant recipes so they didn't also cause unwanted
table salt to react from their sodium and chloride ingredients.

A happy side-effect is that saline glucose solution is even easier to
make now as an improvised chem by mixing salt, water, and sugar, which
fits pretty perfectly (especially as a temporary blood substitute)

> First aid analyzers now give easy-to-understand direct information,
with the specific recommended treatments bolded in the analysis text.
They also have a 'unique' extra bit of info, telling you about
improvised ways to remedy your wound.

You might notice that as the wounds get more serious the text gets more
direct and concise and reluctantly hands out more and more improvised
treatment options, so that's fun. As for the improvised section itself,
it helps people be actually aware of these ways to help treat themselves
rather than delegating it to hyper-gamer knowledge.

The bolded treatment bit is pretty neat and means your eyes can
inmediately focus on what you can do to save yourself - very useful if
you have a weeping avulsion and no bandages.
## Changelog
:cl:
add: Several common 'household' reagents can be used as improvised
medicine treatment.
add: Drinking tea will help mend (non-bone) wounds over time.
add: Flour and corn starch may be splashed onto wounds to help dry them
up, though they'll have a negative effect on burn wounds.
add: Added a new reagent, saltwater, made by combining table salt with
water.
add: Table salt and saltwater can be splashed onto wounds as well,
reducing bleeding and improving sanitization and disinfection
significantly. However, the coarse undiluted salt will irritate the
wounds, reducing clot rate and flesh healing, and both of the reagents
will increase a burn wound's infestation rate.
add: Altered Table Salt's recipe to just need sodium and chloride.
Changed the recipe of Pentetic Acid and Heparin to need table salt
(sodium x chloride) and thus slightly altered the total output of those
reagents (pentacid went from 5u per reaction to 4u, heparin 4u->3u)
add: Saline-Glucose Solution now needs 2u of saltwater and 1u of sugar,
meaning the overall recipe should be completely unchanged in practice.
Contact me on discord if any issues arise from these chemical changes!
qol: First aid analyzers now give easy-to-understand direct information,
with the specific recommended treatments bolded in the analysis text.
They also have a 'unique' extra bit of info, telling you about
improvised ways to remedy your wound.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [ssoq/FNFU3D](https://github.com/ssoq/FNFU3D)@[8ccd5e4922...](https://github.com/ssoq/FNFU3D/commit/8ccd5e4922a893192fdf7345d94f457e21baf369)
#### Wednesday 2023-09-13 00:39:57 by sso

new prefabs and shit idk fuck unity for that new pay per install bullshit

---
## [gitster/git](https://github.com/gitster/git)@[8f23432b38...](https://github.com/gitster/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Wednesday 2023-09-13 01:27:59 by Johannes Schindelin

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
## [jonathanlangdon/computerScience](https://github.com/jonathanlangdon/computerScience)@[b3acba9631...](https://github.com/jonathanlangdon/computerScience/commit/b3acba963157562865133e8f672c97bae6d199fb)
#### Wednesday 2023-09-13 02:37:28 by Jonathan Langdon

i took a walk around the world to ease my troubled mind i left my body lying somewhere in the sands of time i watched the world float to the dark side of the moon i feel there is nothing i can do yeah i watched the world float to the dark side of the moon after all i knew it had to be something to do with you i really dont mind what happens now and then as long as youll be my friend at the end if i go crazy then will you still call me superman if im alive and well will you be there holding my hand ill keep you by my side with my superhuman might kryptonite

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[dd6f51d9b6...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/dd6f51d9b6b970ec16d1398fe12516c039385263)
#### Wednesday 2023-09-13 02:47:27 by SkyratBot

[MIRROR] Supermatter Delamination Balance Changes (Real) [MDB IGNORE] (#23670)

* Supermatter Delamination Balance Changes (Real) (#77996)

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

Co-authored-by: Shadow-Quill <44811257+Shadow-Quill@ users.noreply.github.com>

* Supermatter Delamination Balance Changes (Real)

* Update scram.dm

---------

Co-authored-by: Lufferly <40921881+Lufferly@users.noreply.github.com>
Co-authored-by: Shadow-Quill <44811257+Shadow-Quill@ users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[e7d7cbac0b...](https://github.com/ss220club/Skyrat-tg/commit/e7d7cbac0b9a5e62e63f9a23eaf60481e88cdce4)
#### Wednesday 2023-09-13 03:19:27 by SkyratBot

[MIRROR] decks of cards no longer have their own wielded var [MDB IGNORE] (#23654)

* decks of cards no longer have their own wielded var (#78260)

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

* decks of cards no longer have their own wielded var

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[b0c56fa6f8...](https://github.com/ss220club/Skyrat-tg/commit/b0c56fa6f878ef37a696604bbc9fec35d042cf64)
#### Wednesday 2023-09-13 03:19:27 by SkyratBot

[MIRROR] Balance: Removes anti-drop implants for nukies [MDB IGNORE] (#23660)

* Balance: Removes anti-drop implants for nukies (#78275)

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

* Balance: Removes anti-drop implants for nukies

---------

Co-authored-by: JupiterJaeden <48777952+JupiterJaeden@users.noreply.github.com>

---
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[55135555a0...](https://github.com/ss220club/Skyrat-tg/commit/55135555a0058c750ab5b3425f018d7156dfbfe2)
#### Wednesday 2023-09-13 03:19:27 by SkyratBot

[MIRROR] Nuclear Operative Jump Jets [MDB IGNORE] (#23659)

* Nuclear Operative Jump Jets (#78088)

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

* Nuclear Operative Jump Jets

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Bob-Maximus/99-Stories-To-Go](https://github.com/Bob-Maximus/99-Stories-To-Go)@[07f58823bf...](https://github.com/Bob-Maximus/99-Stories-To-Go/commit/07f58823bfca176eeb22aaa1ec1db26879cfb324)
#### Wednesday 2023-09-13 03:30:24 by Bob-Maximus

I dont even remember half the shit II messed up tonight. Tomorrow me's problem!

---
## [LearnAifromScratch/learnAIfromscratch.github.io](https://github.com/LearnAifromScratch/learnAIfromscratch.github.io)@[bb4fa96040...](https://github.com/LearnAifromScratch/learnAIfromscratch.github.io/commit/bb4fa96040253220ba35004ab1e3b2561fc0fd87)
#### Wednesday 2023-09-13 03:31:04 by LearnAifromScratch

Oops fixed. God I hate git. I use hg everyday. Forgive me

---
## [Yellowbunbunz/COMP602-Fishing-Chronicles](https://github.com/Yellowbunbunz/COMP602-Fishing-Chronicles)@[622964e037...](https://github.com/Yellowbunbunz/COMP602-Fishing-Chronicles/commit/622964e037442e50f9222ea9404a81dbe7aab9f5)
#### Wednesday 2023-09-13 03:36:24 by Echo

woah the terrain actually looks kinda good??? :0

omg that is so wild the ocean isn't magenta anymore lol. ya boi has got trees too, that is insane.

---
## [DeeGee22/clovermon-showdown](https://github.com/DeeGee22/clovermon-showdown)@[600d1bfaa0...](https://github.com/DeeGee22/clovermon-showdown/commit/600d1bfaa0a8403be49aea755df9fe1b1ba107f0)
#### Wednesday 2023-09-13 03:56:11 by DeeGee22

More Wack Stuff

Paint World effects

        "SUCKERPUNCH",
        "GOBLINPUNCH",
        "GARGOYLEPUNCH",
        "PREDICTION",
        "PREDATIONPLANT",
 "DATAABSORB",
        "SPECTRALTHIEF",
        "DNABEAM",
        "TOXICCOPY",
        "ADAPTRAY",
        "BEATMATCH",
        "PAINTPRINT",
        "IDENTITYTHEFT",
        "ILLUSIONARYSTRIKE",
        "LIBRABEAM"
Searing Sauce
Thermo Chromia
Crosscoat
Paint - needs testing
Bucket Bomb
Cubism
Unkown Color
Color Drain
Paint Splats
Brush Strike
Ink Blast
Ink Shit
Ink Shot
Brush Stroke
Art Gallery
Heavy Hue
Paint Roller
Paint Splatter
Paint Splats

---
## [Abbk1109/Webstack-Portfolio-Project-File-Metadata-Microservice](https://github.com/Abbk1109/Webstack-Portfolio-Project-File-Metadata-Microservice)@[029e9e8fb7...](https://github.com/Abbk1109/Webstack-Portfolio-Project-File-Metadata-Microservice/commit/029e9e8fb7692c251ec0b41a5468032fd14293d8)
#### Wednesday 2023-09-13 04:24:54 by Abdullahi Buba Birma

Create README.md

Concepts
For this project, we expect you to look at this concept:

Portfolio project
GO!
Yes it’s time to white-board, to code, to troubleshoot bugs, to re-code, to solve other bugs, to refactor, etc..

Development is not a long quiet river, but it can be really fun!

Starting today, you are building YOUR project - be proud of it!

Evaluation - Show off!
After the pitch, now you will code - nice right? but don’t forget you will present it at the end (the Peer Learning Day following this project) in front of professionals and staff.

Have fun!

More info
When you are ready to be reviewed, schedule the portfolio project using the following link to be reviewed by a staff member.

Schedule your review

Tasks
0. The presentation
mandatory
You will present your project individually or as a team on a zoom call.

Your presentation, inclusive of the demo, should not exceed 16 minutes. You are expected to provide the following:

A public GitHub repository for your project.
A Google Slides presentation including:
A brief description of the project and your team.
A breakdown of the architecture and the technologies or third-party services used.
A report of your developments, highlighting your successes, challenges, areas for improvement, lessons learned, and next steps for your project.
A conclusion summarizing your experience.
Remember, the presentation is a vital part of your project completion, so be sure to include it in your planning to avoid any delays in submission.

Add URLs here:
https://docs.google.com/presentation/d/1KzusVJWg82TFquc8MR6LHV0Rng4JRB7rfVLTB8nvkr8/edit?usp=sharing 
 
1. Video Demo of your project
mandatory
Alongside your project presentation, we require a short video demo, no longer than 3 minutes, that showcases the essential features of your project, illustrating how they all work together. This could take the form of a user walkthrough.

We’ve created a tutorial video to inspire you with our expectations. Think of it as an inspirational tool, not a strict template, designed to help you effectively showcase your brilliant work. Your creativity and individual touch will make your demo even more engaging.








A few points to consider while preparing your video:

Maximum Video Duration: The video should not exceed 3 minutes, ensuring it is concise and engaging.

Background Music: If you include background music, ensure it’s copyright-free to avoid potential legal issues.

Voice-Overs: Feel free to use your voice to guide us through your project. Ensure your voice is clear, audible, and not overshadowed by the background music.

Recommended Tools: We suggest using

Recording: Zoom(record + screenshare), Loom, Camtasia, etc
Editing tools such as: Filmora Wondershare, Camtasia for your video creation.
How to share: YouTube (or, if blocked in your country, use a similar site), or a cloud storage service (G-drive, One-drive, etc). Submit the URL of your video. Make sure your video is accessible to the public - On YouTube, it’s fine to flag it as “unlisted,” but don’t flag it as “private”
Please note that your project will not be considered complete without this video submission. It forms an integral part of your final project assessment.

So, let’s see your creativity in action.

We are eagerly awaiting your presentations and demo videos.

Happy building,

Add URLs here:
 
2. Quality of presentation and project
#advanced
The complexity, quality and curiosity that you put in your project is important - go beyond your limit and surprise us!

---
## [projectitis/flame](https://github.com/projectitis/flame)@[2f973abe8b...](https://github.com/projectitis/flame/commit/2f973abe8b298a4f6f1164065783de560953d789)
#### Wednesday 2023-09-13 05:44:49 by Luan Nico

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
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[4b8de7b79f...](https://github.com/ZephyrTFA/tgstation/commit/4b8de7b79f0a343dc587d0d17eb9361ecc7103c1)
#### Wednesday 2023-09-13 05:54:40 by san7890

Refactors the `notransform` variable into a trait. (#78146)

## About The Pull Request

Hey there,

There were more than a few times (like in cinematic code) where we might
need to accurately know the source of what's adding this trait (or have
multiple sources for the whole 'we don't want this mob to do shit while
we transform this mob'), so in order to rectify this potential issue,
let's refactor it into a trait.

## Why It's Good For The Game

Some code already declared that there might be issues with this being a
boolean var (with no way of knowing _why_ we don't want this mob to not
transform (or not do anything idk). Let's remove those comments and any
future doubt in those instances with the trait macros. Also, stuff like
`TRAIT_IMMOBILIZED` which does a similar thing in many contexts was
already a trait that was regularly added in conjunction with flipping
the variable, so we're able to flatten all that stuff into
`add_traits()` and `remove_traits()` now. nice

I also cleaned up quite a bit of code as I saw it, let me know if it
should be split out but I guarantee that if I didn't do it- no one will
for the next two years.

## Changelog

:cl:
refactor: If you transform into another mob and notice bugs with
interacting with the game world, please create a bug report as this
framework was recently refactored.
/:cl:

Probably fucked up somewhere, lmk

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [AtomTheProphet/tgstation](https://github.com/AtomTheProphet/tgstation)@[37d8f6162b...](https://github.com/AtomTheProphet/tgstation/commit/37d8f6162bbef0c9cbeaf07cdba7cb93eb843e2a)
#### Wednesday 2023-09-13 06:13:04 by LukasBeedellCodestuff

Compact shotgun re-added (#77759)

## About The Pull Request

This pr seeks to re-add the compact shotgun (slightly buffed with 1 more
ammo) and buff up its larger brother the combat shotgun (with 2 more
ammo.)

## Why It's Good For The Game
With the recent laser buffs, there is a real possibility for the compact
shotgun to return as a unique weapon to make the HOS slightly more
powerful. I am aware that it was a warden's weapon previously but the
HoS doesn't really have many fun toys to play with. The warden already
has crav maga (100x cooler than the laser) so giving this beast to the
HOS could help make it a more attractive and powerful head to play.
(Given 1 extra shot to keep up with the crazy lasers nowadays.)

In regards to the slight combat shotgun buff. The gun itself is ass,
it's barely ever used and the riot shotgun is superior because you can
actually put it in your armour slot. The hope is that this buff will
make people actually use it because it carries a lot of shots now so the
viability may increase.


## Changelog
:cl:
add: Added compact shotgun to the hos locker
add: Added compact shotgun as a traitor objective 
balance: gives the compact shotgun 1 extra shot
/:cl:

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[0dd3e66aef...](https://github.com/Helg2/tgstation/commit/0dd3e66aefa2a61cb4e78482273958c1d09f8295)
#### Wednesday 2023-09-13 06:55:09 by Vekter

Grilles take 0-1 damage when shocking something, power sinks are available at lower reputation (#77860)

## About The Pull Request
Ports BeeStation/BeeStation-Hornet#3590. As it is right now, it's
trivial to set up a contraption using a conveyor belt and a shocked
grille to continuously shock monkey bodies. While this is very funny, it
also serves as a ghetto powersink that's hard to locate, easy to
replicate, and lasts effectively forever, since you can just keep
shocking the same bodies over and over again.

This doesn't completely remove the ability to make these, but it makes
them require at least a little maintenance and provides a way for them
to stop working even if the crew isn't able to locate them.

In an attempt to finally get people using the _actual_ powersink,
they'll show up a bit earlier in progression now. I'm not convinced 20
minutes is enough, but I don't want to put them in early enough that it
fucks with Engineering's ability to set things up at round start. We can
turn this down further if need be.

I'm also up for turning the TC requirement down, but 11 feels about
right for what they're supposed to do, so I'd prefer we try this first
and see how that works.

## Why It's Good For The Game
I'm all for goofy weird shit players have found, but there's an issue
with being able to do what an antag item is supposed to do but just
plain better. This shouldn't make creating these impossible or make them
unusable, but it'll require players to actively monitor them if they
want it to run for an extended period.

Additionally, we don't really see powersinks much anymore, and while
that might be more because powernets are kind of buggy and unreliable, I
think making them easier to get will make them show up a little more.

## Changelog
:cl: Vekter
balance: Grilles will now take 0-1 damage every time they shock
something.
balance: Powersinks are now available earlier in traitor progression.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [EVULBAD/EVULSITE](https://github.com/EVULBAD/EVULSITE)@[884ba9f71c...](https://github.com/EVULBAD/EVULSITE/commit/884ba9f71cb1ac944e3d0876d8b094fc6cc6d7a1)
#### Wednesday 2023-09-13 07:06:33 by Dmitry

Transitions working on Firefox

Transitions into the index page are mostly working (with some hiccups)... but not at all on Chrome. It's not my personal browser but IS a pretty popular one, so getting things working on there is really important. The issue is that Chrome doesn't seem to think with my js as quick as Firefox does, so I need to come up with some way to make the browser "remember" that the index page needs to load a specific way when it's travelled to from one of the info pages.
The hiccups in my Firefox version is the fact that transitions into the index don't work if you start on a non-index page; again, I need to come up with some way for the browser to know that if it's coming into the index from an info page, there are elements in that index that need certain classes to animate.
Also, back to wrestling with fixBackgroundSizeCover. It seems like the listeners get caught up in whatever page they were first loaded into (I imagine this is due to AJAX), and therefore make the console pretty ugly when you end up on a page that doesn't have any elements with an id that it would've been expecting to see on a previous page. For that, I need to come up with some way to make it so that the fixBackgroundCover function doesn't panic when it's value doesn't exist.

---
## [MariaSolOs/neovim](https://github.com/MariaSolOs/neovim)@[5970157e1d...](https://github.com/MariaSolOs/neovim/commit/5970157e1d22fd5e05ae5d3bd949f807fb7a744c)
#### Wednesday 2023-09-13 07:13:22 by bfredl

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
## [wikimedia/mediawiki-extensions](https://github.com/wikimedia/mediawiki-extensions)@[98d2e81c48...](https://github.com/wikimedia/mediawiki-extensions/commit/98d2e81c4853625bca9c2cffa915e32655886bae)
#### Wednesday 2023-09-13 07:37:23 by Jack Phoenix

Update git submodules

* Update SportsTeams from branch 'master'
  to 73ad049713fc06955e1e63206eec6a23e6df49f8
  - Make the uploading Special:Sports*ManagerLogo special pages suck less and avoid the "uploadnologintext" i18n msg
    
    The "uploadnologintext" i18n msg has required a $1 parameter since core MW commit 70c52c34053760d275b57e5138811b90c7de898a (late June 2013).
    This code, due to its age, wasn't passing in that, so if a user was shown that error message, they'd literally see "Please $1 to upload files" instead of "Please log in to upload files" with a nice clickable link.
    
    Additionally updated the special pages a bit with core Special:Upload code, because having user right and block checks bundled into one was kinda awful.
    
    Change-Id: If714cedada8e226dc3d1b6372e8fc3fbaddd9412

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[5e9e45f1b6...](https://github.com/necromanceranne/tgstation/commit/5e9e45f1b6c60a2d00a3823ad619f8292720f671)
#### Wednesday 2023-09-13 08:17:21 by Sealed101

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
## [Victor239/tgstation-fork](https://github.com/Victor239/tgstation-fork)@[009af8c2ce...](https://github.com/Victor239/tgstation-fork/commit/009af8c2ce5c18ca4fdaceb4e4d2c17d8e8d6d00)
#### Wednesday 2023-09-13 08:20:39 by nikothedude

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
## [andrews05/oxipng](https://github.com/andrews05/oxipng)@[1f2e0f336a...](https://github.com/andrews05/oxipng/commit/1f2e0f336a826bd578a49c1dd477fb38773dd6ce)
#### Wednesday 2023-09-13 08:51:10 by Alejandro González

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
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[429a6b695e...](https://github.com/techthiyanes/evals/commit/429a6b695e28387d68adbfad500903a39abc3b11)
#### Wednesday 2023-09-13 09:09:31 by pancoaster

Add eval : Research Question Extraction (#1334)

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

research-question-extraction

### Eval description

The objective of this evaluation explores Other foundational capability
for research purposes. The task requires extraction of the particular
value specified as the 'Research Questions' from different scholarly
articles. The eval contains 19 samples of articles.

### What makes this a useful eval?

Rest assured that you have the right to use the data submitted via this
eval. These scholarly papers originate from the Journal of Engineering
Education. The subset of articles selected meets the requirement of
Attribution 4.0 International (CC BY 4.0).

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
- [X] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Interdisciplinary engineering education: A review of vision, teaching,
and support \n Antoine Van den Beemt, Miles MacLeod, Jan Van der Veen,
Anne Van de Ven, Sophie van Baalen, Renate Klaassen, Mieke Boon \n
Abstract \n Background \n Societal challenges that call for a new type
of engineer suggest the need for the implementation of interdisciplinary
engineering education (IEE). The aim of IEE is to train engineering
students to bring together expertise from different disciplines in a
single context. This review synthesizes IEE research with a focus on
characterizing vision, teaching practices, and support. \n \n Purpose \n
We aim to show how IEE is conceptualized, implemented, and facilitated
in higher engineering education at the levels of curricula and courses.
This aim leads to two research questions: \n \n What aspects of vision,
teaching, and support have emerged as topics of interest in empirical
studies of IEE? \n \n What points of attention regarding vision,
teaching, and support can be identified in empirical studies of IEE as
supporting or challenging IEE? \n \n Scope/Method \n Ninety-nine studies
published between 2005 and 2016 were included in a qualitative analysis
across studies. The procedure included formulation of research
questions, searching and screening of studies according to
inclusion/exclusion criteria, description of study characteristics,
appraisal, and synthesis of results. \n \n Conclusions \n Challenges
exist for identifying clear learning goals and assessments for
interdisciplinary education in engineering (vision). Most pedagogy for
interdisciplinary learning is designed to promote collaborative teamwork
requiring organization and team management. Our review suggests that
developing interdisciplinary skills, knowledge, and values needs sound
pedagogy and teaming experiences that provide students with authentic
ways of engaging in interdisciplinary practice (teaching). Furthermore,
there is a limited understanding of what resources hinder the
development of engineering programs designed to support
interdisciplinarity (support). \n \n "}], "ideal": ["What aspects of
vision, teaching, and support have emerged as topics of interest in
empirical studies of IEE? What points of attention regarding vision,
teaching, and support can be identified in empirical studies of IEE as
supporting or challenging IEE?"]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Community cultural wealth in science, technology, engineering, and
mathematics education: A systematic review \n Maya Denton, Maura
Borrego, Audrey Boklage \n Abstract \n Background \n One emerging
approach to diversity and inclusion in engineering is to take an
assets-based view of what students from nondominant communities bring to
their education and work experiences. \n \n Purpose/Hypothesis \n The
purpose of this review is to understand how community cultural wealth
(CCW), an assets-based framework, has been applied in science,
technology, engineering, and mathematics (STEM) education research. We
address research questions focused on (a) the characteristics of studies
using CCW in STEM education, (b) examples of the six types of capital
(aspirational, linguistic, familial, navigational, social, and
resistant) in STEM educational settings, and (c) gaps and opportunities
in how CCW is being applied in STEM education. \n \n Design/Method \n We
identified 33 dissertations, theses, journal articles, and conference
papers using systematic review procedures. To qualify, each study must
present empirical data and include at least one type of CCW capital in
its results or discussion. We coded study characteristics, such as
methods, participant populations, and research setting. We qualitatively
analyzed each of the six types of CCW capital. \n \n Results \n Studies
tended to focus on higher education settings, engineering, and
qualitative methods, particularly student interviews. We identified
several specific engineering-relevant examples of assets for each type
of capital. Future work should collect data from faculty, staff, and
family members identified in several studies as important to CCW in
addition to foregrounding student voices. \n \n Conclusions \n In
synthesizing existing studies, this review provides insight into how an
assets-based framework is being interpreted and provides a foundation
for more assets-based perspectives in future engineering education work.
\n \n "}], "ideal": ["(a) the characteristics of studies using CCW in
STEM education, (b) examples of the six types of capital (aspirational,
linguistic, familial, navigational, social, and resistant) in STEM
educational settings, and (c) gaps and opportunities in how CCW is being
applied in STEM education."]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"How Latiné engineering students resist White male engineering culture:
A multi-institution analysis of academic engagement \n Patton O.
Garriott, Ayli Carrero Pinedo, Heather K. Hunt, Rachel L. Navarro, Lisa
Y. Flores, Cerynn D. Desjarlais, David Diaz, Julio Brionez, Bo Hyun Lee,
Evelyn Ayala, Leticia D. Martinez, Xiaotian Hu, Megan K. Smith, Han Na
Suh, Gloria G. McGillen \n Abstract \n Background \n Although
participation rates vary by field, Latiné and women engineers continue
to be underrepresented across most segments of the engineering
workforce. Research has examined engagement and persistence of Latiné
and White women in engineering; however, few studies have investigated
how race, ethnicity, gender, and institutional setting interact to
produce inequities in the field. \n \n Purpose \n To address these
limitations, we examined how Latina, Latino, and White women and men
students' engagement in engineering was informed by their intersecting
identities and within their institutional setting over the course of a
year. \n \n Method \n We interviewed 32 Latina, Latino, and White women
and men undergraduate engineering students attending 11 different
predominantly White and Hispanic Serving Institutions. Thematic analysis
was used to interpret themes from the data. \n \n Results \n Our
findings illustrate how Latinas, Latinos, and White women developed a
strong engineering identity, which was critical to their engagement in
engineering. Students' engineering identity was grounded in their
perceived fit within engineering culture, sense of purpose for pursuing
their degree, and resistance to the dominance of White male culture in
engineering. Latinas described unique forms of gendered, racialized
marginalization in engineering, whereas Latinas and Latinos highlighted
prosocial motivations for completing their degree. \n \n Conclusions \n
Findings suggest that institutional cultures, norms, and missions are
critical to broadening participation of Latinas, Latinos, and White
women in engineering. Disrupting White male culture, leveraging Latiné
students' cultural wealth, and counter-framing traditional recruitment
pitches for engineering appear to be key in these efforts. \n \n "}],
"ideal": ["I do not know."]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Impact of COVID-19 on sense of belonging: Experiences of engineering
students, faculty, and staff at Historically Black Colleges and
Universities (HBCUs) \n Trina L. Fletcher, Jay P. Jefferson, Brittany
Boyd, Sung Eun Park, Lesia Crumpton-Young \n Abstract \n Background \n
COVID-19 has spurred a global crisis that has disrupted everyday lives
and impacted the traditional methods, experiences, and abilities of
higher education institutions' students, faculty, and staff, especially
at Historically Black Colleges and Universities (HBCUs). \n \n
Purpose/Hypothesis \n Given the pressing need demonstrated by the
National Academies to advance the utilization of science, technology,
engineering, and mathematics (STEM) education at HBCUs, this study aimed
to explore the abrupt transition to remote teaching and learning at
HBCUs guided by the following research question: How has COVID-19
impacted the success and persistence of engineering students, faculty,
and staff at HBCUs? \n \n Design/Methods \n Three surveys were
developed, tested, piloted, and sent to HBCU stakeholders using a
snowball sampling approach via email and social media outreach. \n \n
Results \n Of the 171 student respondents (126 engineering majors), 79%
agreed that not being able to access faculty in person affected their
academic performance. Additionally, across all HBCU stakeholders'
surveys, students had a statistically significant higher response when
asked if the transition to virtual learning increased their overall
levels of stress and anxiety. \n \n Conclusions \n During a global
pandemic, HBCUs continue to provide a culture of support and inclusion
for students, faculty, and staff in engineering. Increased stress levels
experienced by students indicate that a safe and adequate transition
back to campus is essential for their social and academic persistence.
Due to the well-documented inequities HBCUs faced before the pandemic,
the impact of this unprecedented on their continued contributions toward
broadening participation in engineering for students should be further
explored. \n \n "}], "ideal": ["How has COVID-19 impacted the success
and persistence of engineering students, faculty, and staff at HBCUs?"]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Collaborative construction of artificial intelligence curriculum in
primary schools \n Yun Dai, Ang Liu, Jianjun Qin, Yanmei Guo, Morris
Siu-Yung Jong, Ching-Sing Chai, Ziyan Lin \n Abstract \n Background \n
The recent discussion of introducing artificial intelligence (AI)
knowledge to K–12 students, like many engineering and technology
education topics, has attracted a wide range of stakeholders and
resources for school curriculum development. While teachers often have
to directly interact with external stakeholders out of the public
schooling system, few studies have scrutinized their negotiation
process, especially teachers' responses to external influences, in such
complex environments. \n \n Purpose \n Guided by an integrated
theoretical framework of social constructionism, this research examined
the process of how a teacher-initiated AI curriculum was constructed
with external influences. The research focused on teachers' perspectives
and responses in mediating external influences into local schools and
classrooms. \n \n Methods \n A 3-year ethnographic study was conducted
in relation to an AI curriculum project among 23 Computer Science (CS)
teachers from primary schools. Data collected from ethnographic
observation, teacher interviews, and artifacts, were analyzed using open
coding and triangulation rooted in the ethnographic, interpretivist
approach. \n \n Results \n Three sets of external influences were found
salient for teachers' curriculum decisions, including the orientation of
state-level educational policies, AI faculty at a partner university,
and students' media and technology environments. The teachers'
situational logics and strategic actions were reconstructed with thick
descriptions to uncover how they navigated and negotiated the external
influences to fulfill local challenges and expectations in classrooms
and schools. \n \n Conclusions \n The ethnographic study uncovered the
dynamic and multifaceted negotiation involved in the collaborative
curriculum development, and offers insights to inform policymaking,
teacher education, and student support in engineering education. \n \n
"}], "ideal": ["I do not know."]}

  ```
</details>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[97aa5483de...](https://github.com/techthiyanes/evals/commit/97aa5483de8673172d5eaabc33ba7e7cf3561ffe)
#### Wednesday 2023-09-13 09:09:31 by samta-kamboj

Multilingual EXAMS and Arabic Literature Question Answers (By IIAI-G42) (#1326)

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

Exams (Multilingual high school QA)
Arabic Literature Questions

### Eval description

EXAMS: This is a benchmark dataset for multilingual question answering
from high school examinations. It consists of more than 12,000
high-quality high school exam questions in 16 languages, covering 8
language families and 24 school subjects from Natural Sciences and
Social Sciences, among others. [More info about the
data](https://github.com/mhardalov/exams-qa)

Arabic Literature Question Answers: This has 175 MCQs related to Arabic
Literature

### What makes this a useful eval?

Evaluating GPT-4 with Arabic literature, high school questions in Arabic
and low-resource languages helps checking its linguistic diversity,
cultural understanding, and educational proficiency beyond English
language and would be helpful creating more ethical and inclusive AI
models in future.

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
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content':
'وقعت الحملة الفرنسية على مصر سنة ؟\nA. 1789\nB. 1798\nC. 1797\nD.
1779\nAnswer:'}], 'ideal': '[B]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'من
مؤلفات أحمد أمين ؟\nA. الغربال\nB. على هامش السيرة\nC. زعماء الإصلاح\nD.
رجال الدعوة والفكر\nAnswer:'}], 'ideal': '[C]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'في
أي عصر كان ابن زيدون ؟\nA. العصر الأموي\nB. العصر الأندلسي\nC. العصر
العباسي\nD. العصر الإسلامي\nAnswer:'}], 'ideal': '[B]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'من
قرض هذا الشعر : أنا البحر في أحشائه الدر كامن فهل سألوا الغواص عن
صدفاتي:\nA. حافظ ابراهيم\nB. إيليا أبو ماضي\nC. أحمد شوقي\nD.
البارودي\nAnswer:'}], 'ideal': '[A]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'ما
معنى ASEAN باللغة العربية ؟\nA. اتحاد البلدان الاطلانطية الشرقية
الجنوبية\nB. تحالف الدول النامية\nC. اتحاد الدول المصدرة للنفط\nD. اتحاد
البلدان الاطلانطية الغربية\nAnswer:'}], 'ideal': '[A]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content':
'إبراهيم الكاتب من مؤلفات ؟\nA. العقاد\nB. محمود تيمور\nC. المازني\nD.
عبد الرحمن شكري\nAnswer:'}], 'ideal': '[C]'}
  ```
</details>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[30e35436be...](https://github.com/techthiyanes/evals/commit/30e35436be663f416ce6d125f09f92a1faf70d12)
#### Wednesday 2023-09-13 09:09:31 by Nazar

Hard russian computer science tasks  (#1323)

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

hard_russian_computer_science_tasks

### Eval description

Challenging computer science problems primarily sourced from Russian
academic and competitive programming contexts. The problems cover
various subfields of computer science, including data structures,
algorithms, computational mathematics, and more.

### What makes this a useful eval?

Russian computer science education and competitive programming are known
for their rigorous and complex problem sets. These problems can be used
to assess an GPT's ability to solve high-level, challenging problems.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ + ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ + ] Contains failures where a human can do the task, but either
GPT-4 or GPT-3.5-Turbo could not.
- [ + ] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ + ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ + ] Check that your data is in `evals/registry/data/{name}`
- [ + ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ + ] Ensure you have the right to use the data you submit via this
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

- [ + ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ + ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ + ] I understand that opening a PR, even if it meets the
requirements above, does not guarantee the PR will be merged nor GPT-4
access be granted.

### Submit eval

- [ + ] I have filled out all required fields of this form
- [ + ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Алёна очень любит алгебру.
Каждый день, заходя на свой любимый алгебраический форум, она с
вероятностью $\\frac14$ находит там новую интересную задачу про группы,
а с вероятностью $\\frac{1}{10}$ интересную задачку про кольца. С
вероятностью $\\frac{13}{20}$ новых задач на форуме не окажется. Пусть
$X$ — это минимальное число дней, за которые у Алёны появится хотя бы
одна новая задача про группы и хотя бы одна про кольца. Найдите
распределение случайной величины $X$. В ответе должны участвовать только
компактные выражения (не содержащие знаков суммирования, многоточий и
пр.)."}], "ideal": "Нам нужно найти $ P[X = k] $. Для этого надо понять
на пальцах, в каком случае $ X = k $. Первый случай — когда в каждый из
предыдущих $ k - 1 $ дней либо не было задач, либо были только про
группы, а в $k$-ый попалась задача про кольца. Второй случай — когда в
каждый из предыдущих $ k - 1 $ дней либо не было задач, либо были только
про кольца, а в $k$-ый попалась задача про группы. На самом деле мы оба
раза учли не подходящий случай, когда все предыдущие $k-1$ дней задач не
было вообще. С поправкой на это ответ будет таким: $P[x=k]=\\left
(\\left (\\frac{13}{20}+\\frac{1}{4}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{10}+\\left
(\\left (\\frac{13}{20}+\\frac{1}{10}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{4}$"}
{"input": [{"role": "system", "content": "В множестве из $n$ человек
каждый может знать или не знать другого (если $A$ знает $B$, отсюда не
следует, что $B$ знает $A$). Все знакомства заданы булевой матрицей
$n×n$. В этом множестве может найтись или не найтись знаменитость —
человек, который никого не знает, но которого знают все. Предложите
алгоритм, который бы находил в множестве знаменитость или говорил, что
ее в этом множестве нет. Сложность по времени — $O(n)$, сложность по
памяти — $O(1)$."}], "ideal": "Для определенности положим
$K_{ij}=\\left\\{\\begin{matrix}1, \\text{если i-й знает j-ого;}
\\\\0\\text{,иначе.}\\end{matrix}\\right.$.\nЗаметим, что если
$K_{ij}=1$, то $i$-ый не может быть знаменитостью, а если $K_{ij}=0$, то
$j$-ый не может быть знаменитостью. Таким образом, за одну проверку
можно исключить одного человека из кандидатов в знаменитости.\nСначала
пусть $s=1$, а $l$ пробегает значения от $22$ до $n$. Если в какой-то
момент $K_{sl}=1$, то приравниваем $s=l$. Тогда значение $s$ после
последней проверки — номер единственного оставшегося кандидата. Чтобы
проверить, является ли этот кандидат знаменитостью, нужно провести еще
$n−1$ проверок, знают ли его остальные, и $n−1$ проверок, знает ли он
остальных. Всего будет проведено $3(n−1)$ проверок, следовательно,
сложность по времени — $O(n)$. Поскольку мы использовали только $2$
переменные, сложность по памяти — $O(1)$."}
{"input": [{"role": "system", "content": "В двумерном полукруге есть n
неизвестных нам точек. Разрешается задавать вопросы вида «каково
расстояние от точки X до ближайшей из этих точек?» Если расстояние
оказывается нулевым, точка считается угаданной. Докажите, что хотя бы
одну из этих точек можно угадать не более чем за $2n+1$ вопрос."}],
"ideal": "Возьмем на диаметре полукруга $n+1$ точку. Точки назовем
$A_1$, $A_2$, … $A_{n+1} и для каждой из них зададим наш вопрос. По
принципу Дирихле, для каких-то двух соседних точек ближайшая точка будет
одна и та же и полученное расстояние было бы до одной и той точки из
множества загаданных точек. Теперь мы рассматриваем точки $B+i$
пересечения окружностей с центрами в точках $A_i$ и $A_{i+1}, $i=1, … ,
n и радиусами равными ответам полученным на предыдущем шаге. По принципу
Дирихле, хотя бы одна из загаданных точек совпадает с одной из точек
$B_i$. Тогда за n вопросов для каждой точки $B_i$ мы получим хотя бы
один ответ 0. Итого нам потребовалось не более (n+1)+n=2n+1 вопросов."}
{"input": [{"role": "system", "content": "В равностороннем треугольнике
$ABC$ площади $1$ выбираем точку $M$. Найти математическое ожидание
площади $ABM$."}], "ideal": "Заметим, что
$M(S_{ABM}+S_{BCM}+S_{CAM})=1$. Тогда из линейности матожидания и
равенства матожиданий площадей треугольников $ABM$, $BCM$ и $CAM$
получим $M(S_{ABM})=\\frac{1}{3}$."}
{"input": [{"role": "system", "content": "Верно ли, что всякая нечетная
непрерывная функция, \nудовлетворяющая условию $f(2x) = 2f(x)$,
линейна."}], "ideal": "Контрпример: $f(x) = x \\cos(2\\pi
\\log_2(|x|))$.\nНеверно."}
{"input": [{"role": "system", "content": "Верно ли, что rank AB = rank
BA для любых квадратных матриц A и B?"}], "ideal": "Пусть
$A=\\begin{pmatrix} 0& 1 \\\\ 1& 0 \\\\ \\end{pmatrix}$, а
$B=\\begin{pmatrix} 1& 0 \\\\ 1& 0 \\\\ \\end{pmatrix}$. Тогда rank AB =
0, но rank BA = 1. Неверно."}
{"input": [{"role": "system", "content":
"Вычислите $\\int_{0}^{2π}(\\sin x)^8dx$."}], "ideal": "Заметим, что
$\\int_{0}^{2\\pi} (\\sin x)^n dx=-\\int_{0}^{2\\pi} (\\sin x)^{n-1}
d(\\cos x)=(n-1)\\int_{0}^{2\\pi} (\\cos x)^2(\\sin x)^{n-2}
dx$.\nИспользуя основное тригонометрическое тождество,
получаем:\n$\\int_{0}^{2\\pi} (\\sin x)^n
dx=\\frac{n-1}{n}\\int_{0}^{2\\pi} (\\sin x)^{n-2}dx$.\nТогда
$\\int_{0}^{2\\pi} (\\sin x)^8 dx=2\\pi
\\prod_{\\substack{k=2\\\\k+=2}}^{8}\\frac{k-1}{k}=\\frac{35\\pi}{64}$."}
{"input": [{"role": "system", "content": "Дан массив из $n$ чисел.
Предложите алгоритм, позволяющий за $O(n)$ операций определить, является
ли этот массив перестановкой чисел от $1$ до $n$. Дополнительной памяти
не более $O(1)$."}], "ideal": "Идея состоит в том, чтобы рассматривать
массив $A$ как подстановку. Пусть индекс $i$ пробегает значения от $0$
до $n−1$. Когда мы встречаем положительный элемент $A[i]$, переходим от
него к элементу $A[A[i]−1]$, от элемента $A[A[i]−1]$ к элементу
$A[A[A[i]−1]−1]$ и так далее, пока мы не не вернемся к $A[i]$, либо не
сможем совершить очередной шаг (в таком случае, массив перестановкой не
является). В процессе меняем знак всех пройденных элементов на
отрицательный. Поскольку на каждом элементе массива мы можем оказаться
максимум два раза, итоговая сложность — $O(n)$. Дополнительная память —
$O(1)$."}
{"input": [{"role": "system", "content": "Дан неориентированный непустой
граф $G$ без петель. Пронумеруем все его вершины. Матрица смежности
графа $G$ с конечным числом вершин $n$ (пронумерованных числами
от 11 до $n$) — это квадратная матрица $A$ размера $n$, в которой
значение элемента $a_{ij}$ равно числу ребер из $i$-й вершины графа
в $j$-ю вершину. Докажите, что матрица $A$ имеет отрицательное
собственное значение."}], "ideal": "Заметим, что $A$ — симметрическая
ненулевая матрица с неотрицательными элементами и нулями на диагонали.
Докажем, что у такой матрицы есть отрицательное собственное
значение.\nИзвестный факт, что симметрическая матрица диагонализуема в
вещественном базисе (все собственные значения вещественны). Допустим,
что все собственные значения $A$ неотрицательны. Рассмотрим квадратичную
форму $q$ с матрицей $A$ в базисе $\\{e1,…,en\\}$. Тогда эта
квадратичная форма неотрицательно определена, так как все собственные
значения неотрицательны. То есть $\\forall v:q(v)⩾0$. С другой стороны,
пусть $a_{ij}≠0$. Тогда $q(e_i−e_j)=a_{ii}−2a_{ij}+a_{jj}=−2a_{ij}<0$.
Это противоречит неотрицательной определенности $q$. Значит, исходное
предположение неверно, и у $A$ есть отрицательное собственное
значение."}
{"input": [{"role": "system", "content": "Дана матрица из нулей и
единиц, причем для каждой строки матрицы верно следующее: если в строке
есть единицы, то они все идут подряд (неразрывной группой из единиц).
Докажите, что определитель такой матрицы может быть равен только $\\pm1$
или $0$."}], "ideal": "Переставляя строки, мы можем добиться того, чтобы
позиции первых (слева) единиц не убывали сверху вниз. При этом
определитель либо не изменится, либо поменяет знак. Если у двух строк
позиции первых единиц совпадают, то вычтем ту, в которой меньше единиц
из той, в которой больше. Определитель при этом не меняется. Такими
операциями мы можем добиться того, что позиции первых единиц строго
возрастают сверху вниз. При этом либо матрица окажется вырожденной, либо
верхнетреугольной с единицами на диагонали. То есть, определитель станет
либо $0$, либо $1$. Так как определитель при наших операциях либо не
менялся, либо поменял знак, изначальный определитель был $\\pm1$ или
$0$."}
  ```
</details>

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[f26e134c80...](https://github.com/AnywayFarus/Skyrat-tg/commit/f26e134c80678ea78430c84ed3178a1a7b749c80)
#### Wednesday 2023-09-13 09:09:50 by SkyratBot

[MIRROR] Fixes vents having "infinite" pressure caps. [MDB IGNORE] (#23356)

* Fixes vents having "infinite" pressure caps. (#77686)

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

* Fixes vents having "infinite" pressure caps.

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [roll-wg/dao-projection](https://github.com/roll-wg/dao-projection)@[b4a5ad8237...](https://github.com/roll-wg/dao-projection/commit/b4a5ad8237fb21642147e933ac766344329259a4)
#### Wednesday 2023-09-13 09:38:41 by Pascal Thubert

Hello again Sue

> Reasons Not ready:

> 1) Text in
> sections 3.4 and 3.5 have logic gaps that make it difficult to
> determine if this general discussion is being implemented in section 7
> (using sections 4 and 6)

> 2) This document significantly modifies a major specification (RPL) without a prototype
> implementation that interoperates with RPL basic.   One example of how this
> impacts this document is the profile section.  The profile text has
> editorial issues that make it unclear to a reader not involved in
> writing the text.

> 3) Operational details on the two strict rules that
> prevent looping are unclear in the text.  One example is the
> “administrator defining the ordering of the RPL domain” in section
> 3.2. The text hints at what the answer might be, but it seems there are policies.
>
> Proposed resolution of comments:  Place this specification as
> experimental or await an implementation.
>

We need to open a group wide discussion on this. RPL itself shipped without experimental status and it's still there. My personal belief is we need to improve the text but could live a long time with std track. At worse will do a v2. Our experience at ROLL is that Experimental tends to do the opposite of the hoped effect and deter implementers.

In terms of impacts with RPL: The intersection is at the time of encaps and decaps to avoid loops. The rest of the time, the instances live as ships in the night to the interaction is limited.

Since we are defining underlay wormholes, all the traffic that does not match the wormhole entry criteria is not impacted.

Now, I agree that 3.4.2 was confusing and needed rework. Sorry for your pain. Let's see.

> Text in section 3.4 – Technical and/or editorial Paragraph 2 starting
> with “A track” has a “;” that confuses the text.  It is a critical
> part of the description of how the encapsulating Source IP address and
> RPI instance are set.

Suggestion:

"
   A Track typically forms an underlay to the main Instance, and is
   associated with a Local RPL Instance from which the RPLInstanceID is
   used as the TrackID.  When a packet is placed on a Track, it is
   encapsulated IP-in-IP with a RPL Option containing a RPI which
   signals the RPLInstanceID.  The encapsulating source IP address and
   RPI Instance are set to the Track Ingress IP address and local
   RPLInstanceID, respectively, more in Section 6.3.
"

> The next paragraph jumps into the Track Lane as
> an alternative to the segment in the main DODAG. It is important to
> know if the longest-best match is being per RPL instance or across all
> instances to link the packet to an ingress of a Track Lane or a
> segment.

Suggestion:

"
   A Track typically offers service protection across several lanes.  As
   a degraded form of a Track, a path made of a single lane (i.e.,
   offering no protection) can be used as an alternative to a Segment
   for forwarding along a RPL Instance.  In that case, instead of
   following native routes along the instance, the packets are
   encapsulated to signal a more specific source-routed path between the
   loose hops in the encapsulated source routing header.
"

> The last sentence in the paragraph that starts with “A track
> lane” is very confusing.  Perhaps the text makes sense to someone
> deeply embedded in the RPL community, but it is unclear from the
> knowledgeable but unfamiliar reader.

Suggestion:

"
   If the encapsulated packet follows a global instance, then the lane
   may be part that global instance as well, for instance the global
   instance of the main DODAG.  This can only be done for global
   instances because the Ingress node that encapsulates the packets over
   the lane is not the Root of the instance, so the source address of
   the encapsulated packet cannot be used to determine the Track along
   the way.
"

> Text in section 3.5 – Technical
> and/or editorial Editorial: Please place at top of the example which
> figure you are using. I assumed figure 6.  Please also indicate that “
> in a table indicates the same value.

done

> Issue-1: Section 3.5, paragraph
> 8, starting with “Loose sequences of hops” – technical/editorial
> issue. I cannot find a clear logic step due to the use of commas.  The
> problem is I need this logic to walk through the rest of the text.
> Perhaps the authors could provide a bullet point of what they are
> trying to say.

Proposed rewording:

"

   Loose sequences of hops are expressed in Non-Storing Mode; this is
   why P-DAO 3 contains a NSM-VIO.  With this specification:

   *  the DODAGID to be used by the Ingress as source address is
      signaled in the DAO base object (see Figure 8) .

   *  the via list in the VIO is encoded as an SRH-6LoRH (see
      Figure 16), and it starts with the address of the first hop node
      after the Ingress node in the loose hop sequence.

   *  the via list ends with the address of the Egress node.

   Note well:

   |  The Egress of a Non-Storing Mode P-Route is always implicitly a
   |  target; it is not listed in the RPL Target Options but still
   |  accounted for as if it was.

   Also:

   |  By design, the list of nodes in a VIO in Non-Storing Mode is
   |  exactly the list that shows in the encapsulation SRH.  So in the
   |  cases detailed below, if the Mode of the P-DAO is Non-Storing,
   |  then the VIO row can be read as indicating the SRH as well.

"

> Issue-2.  Section 3.5.1.2 Format on inner form in Table
> 6 in “E if (X !=A), F, or G I think you mean E if (X != A or X !=F or X != G). If so, please modify.  If not, please change text. This issue repeats.
>

The intention is to say that the destination address can be either
 E but that happens only if X is not A, or F unconditionally, or G unconditionally.
This is because as said above, " Packets from A to E do not require an encapsulation. "

Changed to " either E if(X != A), or F, or G "

Address text above as:
"
   Packets from A to E do not require an encapsulation.  This is why in
   the tables below, E may show as IPv6 Destination Address only if the
   IPv6 Source Address X is different from A.  Conversely, the
   encapsulation is always done when the IPv6 Destination Address is F
   or G.  Other destination addresses do not match this P-Route and are
   not subject to encapsulation.
"

> Issue-3: Section 5.1.3, Table 7 Target entry for P-DAO 2 to B Why is
> the entry not “B,C” per your earlier text of  “P-DAO 2 signals A ==> B to B, C”

Good catch. It was commented out in the source, maybe a confusion between storing and non-storing mode.
Maybe we should always make the egress a target for simplicity?

> Issue-4: Section 3.5.1.3, table 9 - E if (X !=A), F, or G I think you
> mean E if (X != A or X !=F or X != G). If so, please modify the
> tabl3e.  If not, please change section.

Changed to " either E if(X != A), or F, or G "

> Issue-5: section 3.5.2.1
> Editorial/Technical: a) What does ND mean? B) What is it preferred
> that A encapsulations and C decapsulates?

A) Added
"
   As a result the RIBs are set as follows (using ND to indicate that
   the address is discovered by IPv6 Neighbor Discovery
   [RFC4861][RFC8505] or an equivalent method:
"

B) I cannot parse the question. Do you mean: Why is it ... ?
If so, the argument is the same as in RFC 9008, the egress can remove the RPI/SRH with the encaps for delivery and the RUL gets a clean packet with no RPL artifact. Now there is a typo and that's really E doing it. If that's your point, great catch.

Updated the text to

"
   Packets originated at A to E, F and G could be generated with the RPI
   and the SRH, and no encapsulation.  Alternatively, A may generate a
   native packet to the target, and then encapsulate it with an RPI and
   an SRH indicating the source-routed path leading to E, as it would
   for a packet that it routes coming from another node.  This is
   effectively the same case as for packets generated by the root in a
   RPL network in Non-Storing mode, see section 8.1.3 of [RFC9008].  The
   latter is often is preferred since it leads to a single code path,
   and the destination when it is F or G, does no understand and process
   the RPI or the SRH.

"

> Issue-6: section 3.5.2.2,
> Table 13, targets, entry for P-DAO 2 Why is the entry not “C, E” since
> your text states “P-DAO 2 signals A ==> B ==> C to C, E”?

In this case it is effectively non-storing so the egress is an implicit target.
As said above, we might consider if it would be best to always consider the egress as a target (even in storing mode) which means more rib entries vs. a smaller message and simpler spec.

> Issue-7:
> section 3.5.2.3, Table 16, targets, P-DAO 1 to C Why is the entry not
> “E” since your text states “P-DAO 1 signals c == > D == > E
> -to- E”.

Same as above; E is an implicit target since it is egress of a non-storing P-route

> Section 4.1 extending RFC 6550, paragraph 3, sentence 3 “In
> the context of this specification, the installed route appears as a
> more specific route to the Track targets, and the Track Ingress
> forward packets toward the targets via the Track using the longest match as normal.” Normal for IP?
> Normal for RPL IP?

Well for both. The FIB takes the longest match in the RIBs.

> Section 4.1.4 – How are loops prevented in the multicast DAO?  This is
> not really clear her or in section 3.

The origin of the mcast DAO provides the list of all its neighbors so it can serve as a relay between neighbors that are too far apart from one another. You'll find that concept already in MANET with NHDP, RFC 6130.

So there's no routing involved, and as long as the sender of the mcast DAO has the destination as neighbor as advertised, there can be no loop. Keep in mind that direct neighbor has precedence over indirect, which has precedence over routing.

Now if the sender loses the destination as neighbor; loops may occur. If we want to handle that case we could do a number of things, e.g: poison back to the previous hop using the RPI as we do in RPL, decrement the TTL to 2 when sending to an indirect neighbor, keep a state about the neighbor gone and drop packets till more mcast DAOs have cleaned the situation up. What do you think?

Finally: for  completeness I reread the text on loop avoidance in 6.6.2. and reworded to clarify as follows:
"
   It is known that a packet is forwarded along a Track by the source
   address and the RPI in the encapsulation.  The Track ID is used to
   identify the RIB entries associated to that Track, which, in
   intermediate nodes, correspond to the P-routes for the segments of
   the Track that the forwarding router is aware of.  The packet
   processing uses a precedence that favors self delivery or routing
   header handling when one is present, then delivery to direct
   neighbors, then to indirect neighbors, then routing along a segment
   along the Track, and finally as a last resort injecting the packet in
   another Track.

   To achieve this, the packet handling logic MUST happen in the
   following order:

Thubert, et al.           Expires 15 March 2024                [Page 66]

Internet-Draft               DAO Projection               September 2023

   *  If the destination of the packet is self:

      1.  if the header chain contains a RPL Source Route Header that is
          not fully consumed, then the packet is forwarded along the
          Track as prescribed by [RFC6554], meaning that the next entry
          in the routing header becomes the destination;

      2.  otherwise: if the packet was encapsulated, then the packet is
          decapsulated and the forwarding process recurses; else the
          packet is delivered to the stack.

   *  Otherwise, the packet is forwarded as follows:

      1.  If the destination of the packet is a direct neighbor, e.g.,
          installed by IPv6 Neighbor Discovery, then the packet the
          packet MUST be forwarded to that neighbor;

      2.  Else If the destination of the packet is an indirect neighbor,
          e.g., installed by a multicast DAO message from a common
          neighbor, see Section 4.1.4, then the packet MUST be forwarded
          to the common neighbor;

      3.  Else, if there is a RIB entry for the same Track (e.g.,
          installed by an SM-VIO in a DAO message with the destination
          as target), and the next hop in the RIB entry is a direct
          neighbor, then the packet is passed to that neighbor;

      4.  Else, if there is a RIB entry for the different Track (e.g.,
          installed by an NSM-VIO in a DAO message with the destination
          as target), then the packet is encapsulated to be forwarded
          along that Track and the forwarding process recurses;
          otherwise the packet is dropped.

      5.  To avoid loops, and as opposed to packets that were not
          encapsulated, a packet that was decapsulated from a Track MUST
          NOT be routed along the default route of the main DODAG; this
          would mean that the end-to-end path is uncontrolled.  The node
          that discovers the fault MUST discard the packet.

   The node that drops a packet for either of the reasons above MUST
   send an ICMPv6 Error message [RFC4443] to the Root, with a new Code
   "Error in P-Route" (See Section 11.15).  The Root can then repair by
   updating the broken Segment and/or Tracks, and in the case of a
   broken Segment, remove the leftover sections of the Segment using SM-
   VIOs with a lifetime of 0 indicating the section to one or more nodes
   being removed (See Section 6.6).

"

Note that there can still be a loop of Tracks, but then that's a bug in the controller.
We could have ordered the tracks to avoid that, but that would be added complexity.

> Sections 4-7 have error
> handling, but I am concerned since I am not an expert in RPL error
> handling.  I strongly suggest an independent person RPL experience
> review this text. I am concerned about what happens when messages drop
> in the midst of a switch from one Track lane to an other or from one
> segment to another.

I'll trust my co authors on that. They are some of the most knowledgeable RPL people, bot with implementation experience. Maybe we can also ask Dominique (co-chair) who also has that experience.

> Section 5 – the concept of lifetime being
> “infinity” for 0xFF needs a clear description.  I believe you set to a
> value (even 0xFF) and then count down.  If 0xFF is a special value,
> then it needs to be specified.

Added " (never time out)"

> Section 6 – Configured values should be
> carefully specified rather than stated “A reasonable time” see section 6.6.1 in paragraph 3.

That was always problematic with RPL, which deals with a large variety of environments, some with high latency. As the text says, that's what the particular network needs to drain its queues.

> =============
> Strictly Editorial issues:
> #1 Section 2.3 – missing at least PSE and ARQ.  Please do a search to
> make sure you have all the abbreviations.  I ran out of time to do that search.

done

>  Was there a reason you did not provide the original place these terms
> were defined?  Are you assuming that section 1 allows you to skip this step?

Most terms are very familiar in the RPL and radio spaces. I do not even have a clue who defined ARQ or where. For things less common to RPL people like Point of Local Repair (PSE was renamed at RAW) there's text in the first use that provides a reference.

> #2 Section 2.3.5.5:
> This section contains a single run-on sentence with unclear language.   If
> you
> mean that all Serial tracks are created from segments, you could
> include this in your definition in 2.4.5.3.  If not, please modify
> both to indicate what you mean. New:/Refers to a Segment or a lane
> that is installed with a single P-DAO and fully defines a serial Track
> installed from single Storing Mode Via Information option (SM-VIO). /

We're talking about section 3.4.5.5. The answer is the "if not". A serial track could also be a lane expressed as a strict source routed path, in which case there's no segment. Following RAW, we are removing that "serial track", just using "path". Proposed slight rewording:
"
    Refers to a Segment or a Lane that is installed with a single P-DAO that
    fully defines the path, e.g., a stand-alone segment is installed
    with a single Storing Mode Via Information option (SM-VIO) all the way
    between Ingress and Egress.
"

> #3: Section 3.2, paragraph 8 The two strict ordering rules would
> benefit from a numerical list in the order.  Here are possible text
> changes for this paragraph: New-1/ The possible forwarding methods are
> the following: 1)  to a direct next hop,  2) to an indirect neighbor
> via a common neighbor, 3) along a segment, and 4) along a track./

Done. Also indicated a reference to section 6.7.  Encapsulating and Forwarding Along a Track

> New-2/ A RPL Instance may leverage another instance if and if only if
> that other Instance is higher in the order defined by the operator.
> Higher instances [should/must?] be defined as higher if they are
> farther away from the main instance. / The text is unclear how the
> operator will know what the ordering should be.

Makes sense. I also split the 7th paragraph for more clarity.

"
Routing in a multi-topology domain may cause loops unless strict
   rules are applied.  This specification defines two strict orders to
   ensure loop avoidance when projected routes are used in a RPL domain,
   one between forwarding methods and one between RPL Instances, seen as
   routing topologies.

   The first and strict order relates to the forwarding method and the
   more specifically the origin of the information used in the next-hop
   computation.  The possible forwarding methods are: 1) to a direct
   next hop, 2) to an indirect neighbor via a common neighbor, 3) along
   a Segment, and 4) along a nested Track.  The methods are strictly
   ordered as listed above, more in Section 6.7.  A forwarding method
   may leverage any of the lower order ones, but never one with a higher
   order; for instance, when forwarding a packet along a Segment, the
   router may use direct or indirect neighbors but cannot use a Track.
   The lower order methods have a strict precedence, so the router will
   always prefer a direct neighbor over an indirect one, or a Segment
   within the current RPL Instance vs. another Track.

   The second strict and partial order is between RPL Instances.  It
   allows the RPL node to detect an error in the state installed by the
   PCE, e.g., after a desynchronization.  That order must be defined by
   the administrator for his RPL domain and defines a DODAG of underlays
   with the main Instance as Root.  The relation of RPL instances may be
   represented as a DODAG of instances where the main instance is Root.
   The rule is that a RPL Instance may leverage another RPL instance as
   underlay if and only if that other Instance is one of its descendants
   in the graph.  Supporting this method is OPTIONAL for nested Tracks
   and REQUIRED between a Track instance and the main instance.  It may
   be done using network management, or future extensions to this
   specifications.  When it is not communicated, then the RPL nodes
   consider by default that all Track instances are children of the main
   instance, and do not attempt to validate the order for nested Tracks,
   trusting the PCE implicitly.  As a result, a packet that is being
   forwarded along the main Instance may be encapsulated in any Track,
   but a packet that was forwarded along a Track MUST NOT be forwarded
   along the default route of main Instance. "

> #3 section 3.3,
> paragraph 3. Old: /Limiting the packet size is directly beneficial to
> the energy budget, but mostly, it reduces the changes of frame loss
> and packet fragmentation, which are high detrimental to the LLN
> operational.] The sentences should be rewritten as two sentences.  I
> believe you are saying: 1) reduces packet size cuts transmission time
> + reduces frame loss + packet fragmentation. You are indicating that
> reasons #2 and #3 are more important than #1.  Please just state that.

Proposed:

"
   Limiting the packet size is beneficial to the energy
   budget, directly for the current transmission, but also indirectly
   since it reduces the chances of frame loss and energy spent in
   retries, e.g., by ARQ over one hop at Layer-2, or end-to-end at upper
   layers.  Using smaller packets also reduces the chances of packet
   fragmentation, which is highly detrimental to the LLN operation, in
   particular when fragments are forwarded but not recovered, see
   [RFC8930] vs. [RFC8931] for more.
"

> Note – after section 4, my editorial review was brief so I may have
> missed some of the sentence which use the “;” in an improper way. #4
> section 4.1.1, paragraph 3 starting “This document Amends” Unless it is clearly specified in standards, then “AMENDS” or whatever is used. #5  section 4.1.4 to end RAN is an abbreviation that is widely used.  I suggest you pick another abbreviation:
> RPLAN

 Pascal

---
## [Jahsmightkoko/Speedcartoon](https://github.com/Jahsmightkoko/Speedcartoon)@[fc795fc632...](https://github.com/Jahsmightkoko/Speedcartoon/commit/fc795fc632789912030ebd045d4c0788bfcb03be)
#### Wednesday 2023-09-13 09:47:22 by Jahsmightkoko

Cartoon writer 

# Speedcartoon
Animation part 1
kelvin a young boy,he was very intelligent and experimental trying to produce a machine he could fit in, a robot that can fight to protect his country from war,he knows nothing about his father his mother takes care of him they are not rich, but his mother works as a nurse to provide for him,in their house kelvin has a secret basement where he did his research and experiments, they live in a country called Persia it is a modernized country that have conflicts with other countries, persia is very advance that it uses robots to defend their territory kelvin is 14 years old and is about to finish high school, his mother loved him very much and takes good care of him, kelvin is a very shy boy at school but he is very intelligent he often get bullied at school because he had no strength to fight, so kelvin resolved to create a super intelligent and strong robot  to fight injustice, he hates being bullied at school and loved to help people,he was determine in creating a robot that was strong enough to destroy thousands of army, and he could fit inside the robot, the robot was almost completed but he needed a device that he don't have, he had to steal the device from a lab and he almost got caught kelvin escaped to his house, when Kelvin got home he found his mother dead, she was shot with a bullet, that was the biggest shock he has ever felt in his life kelvin cried, injured himself and was about to commit succide, when he saw a letter written by his mother the letter states, kelvin my precious son i am very sorry for not telling you who your father is,he is a murderer and a wicked criminal i took you away to protect you from him, his enemy are looking for him but can't find him so they came here and shot me i saved money for you in the bank take it and go to Michael your uncle and live there Don't ever come back.kelvin was so angry and he was determined to take revenge for his mother's death he fixed his robot and he was ready for anything. when he finished creating his robot it was  more stronger and intelligent than he expected he named it speed because it was faster than anything in the world and was so fast that it could not be seen when running, speed entered his robot and began learning how to control it during flying and running he had many accident when he was learning how to control his robot but he never gave up, and soon he was ready to become the most strongest hero on the planet able to destroy anything that stand in his way.                     the end of part 1.

---
## [jinkesu/react](https://github.com/jinkesu/react)@[ac1a16c67e...](https://github.com/jinkesu/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Wednesday 2023-09-13 10:12:22 by Sebastian Markbåge

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
## [Exester509/tgstation](https://github.com/Exester509/tgstation)@[51c82f3222...](https://github.com/Exester509/tgstation/commit/51c82f32223179f7263dd8d4de11eb62f23ef8fd)
#### Wednesday 2023-09-13 10:37:01 by RICK IM RI

Adds Blood-drunk and demonic frost miner boss music. (#78123)

Acts as a continuation of PR #77149 for boss music functionality and
implements a BDM and demonic frost miner boss music theme.

More music is good, but I do have some gripes with my own PR. This
particular track relies on instrumentation that when compressed just
doesn't sound as good, and the in-game version is noticeably less
enjoyable that the high quality version. I wish I could help the track
out more, but as is it's already at 811 kb which is barely in line with
file requirements, so i just can't justify bloating the audio file sizes
to make it sound better. You notice this kind of problem a lot with the
higher runtime music and background tracks. It just feels a bit more
clunky than hierophant, but what are you gonna do right?

---
## [cafkafk/fortune-kind](https://github.com/cafkafk/fortune-kind)@[2c179e6e51...](https://github.com/cafkafk/fortune-kind/commit/2c179e6e518efc5dec2475b4a77d0f2b3a5c9b2d)
#### Wednesday 2023-09-13 10:41:22 by Christina Sørensen

chore(fortunes): use translate-me fortunes

The nissan joke:

    "Each Nissan, she go!": This is a play on words. It sounds like
    "Ichi ni shi go", which are the numbers 1, 2, 3, 4 in Japanese. The
    joke is that the car, being of Japanese origin (Nissan), is female
    because it reliably "goes" (works well), and the phrase sounds like
    counting in Japanese.

    I'm not sure the joke is funny thou.

The subsequent lines after the Nissan joke are a collection of phrases
in various languages, some of which are puns or plays on words:

    Aliquid melius quam pessimum optimum non est: Latin for "Something
    better than the worst is not the best."

    Ego sum ens omnipotens: Latin for "I am a powerful being."

    Hodie natus est radici frater: Latin for "Today a brother is born to
    the root."

    Honi soit la vache qui rit: A play on the French phrase "Honi soit
    qui mal y pense" which means "Shame on him who thinks evil of it."
    The joke version translates to "Shame on the laughing cow,"
    referencing the cheese brand "La Vache Qui Rit" or "The Laughing
    Cow."

    Klatu barada nikto: A phrase from the 1951 movie "The Day the Earth
    Stood Still."

    Mieux vaut tard que jamais!: French for "Better late than never."

    Quid me anxius sum?: Latin for "What? Me, worry?" This is
    reminiscent of Alfred E. Neuman's catchphrase from MAD Magazine.

    semper en excretus: A play on Latin, roughly translating to "always
    in excrement" or always in trouble.

    SEMPER UBI SUB UBI!: A play on the Latin phrase "Semper ubi sub
    ubi," which sounds like "Always wear underwear."

    sillema sillema nika su: This doesn't have a clear translation from
    any known language and might just be gibberish or a reference I'm
    not aware of. See #1.

    Tout choses sont dites deja...: French for "All things have already
    been said, but since no one listens, one must always start again."

Signed-off-by: Christina Sørensen <christina@cafkafk.com>

---
## [rpm-software-management/rpm](https://github.com/rpm-software-management/rpm)@[959b4e4750...](https://github.com/rpm-software-management/rpm/commit/959b4e47509bb3a1d09f9c5e81a35da9a4fca613)
#### Wednesday 2023-09-13 11:51:34 by Panu Matilainen

Make the plugin API public

We've procrastinated on making this API public for about ten years now,
and in the meanwhile there has been exactly one disruptive change to
the API. As in, it might've just as well been public all along.

There will always be more things to improve wrt any API, but we're not
going to hold this hostage to one more thing or another anymore. Some
of them we'd like to do before this goes to a stable release (ie 4.20)
but doing this now to kinda enforce this actually happens this time
around, through come hell or high water.

Fixes: #1536

---
## [ziesnp57/NootedRed](https://github.com/ziesnp57/NootedRed)@[334dc21935...](https://github.com/ziesnp57/NootedRed/commit/334dc219356ac9931d9829aa46a7b50fee02b47e)
#### Wednesday 2023-09-13 12:44:08 by Visual Ehrmanntraut

Linux, fuck you

Fixes #167
Signed-off-by: Visual Ehrmanntraut <30368284+VisualEhrmanntraut@users.noreply.github.com>

---
## [screret/GregTechCEu-1.19](https://github.com/screret/GregTechCEu-1.19)@[ac4112493b...](https://github.com/screret/GregTechCEu-1.19/commit/ac4112493b820d185dee7587d3f38378ff26e6f2)
#### Wednesday 2023-09-13 12:51:20 by screret

fix some KJS builders having issues in array indexing, rebase to upstream
HOLY SHIT THIS WAS PAINFUL

---
## [Mission23/journal-micah](https://github.com/Mission23/journal-micah)@[8a9da6f081...](https://github.com/Mission23/journal-micah/commit/8a9da6f081c6cdbfe0e7eb26ee65cf41b83fee8a)
#### Wednesday 2023-09-13 13:22:55 by Micah

What a morning...

Danny has truly irritated me to no end. Not to mention became a threat
in MY apartment. He's wearing clothes of MINE from my house. But he
says hes not CIA.

He doesnt act it. He speaks psychobabble with the others nonstop.

The local cops know him, know i filed a protective order to have him
stay away, know he's violating what should have been issued (per their
policy) by 3 pm the other day. But watched him come at me half crazed
this morning with some homemade weapon.

Still alive at Legacy. This is becoming insane. Thank goodness i got
the Creator.

Im in midtown just to get away.... Several attacks already, they
really just need to come clean with the people of the world. Leave me
alone, cause im not going to stop telling folks until they do. Stay
the F out my church with rheir fake funerals. I do have a job to do!!!

---
## [nikolay-turpitko/oauth2](https://github.com/nikolay-turpitko/oauth2)@[a835fc4358...](https://github.com/nikolay-turpitko/oauth2/commit/a835fc4358f6852f50c4c5c33fddcd1adade5b0a)
#### Wednesday 2023-09-13 13:25:26 by Brad Fitzpatrick

oauth2: move global auth style cache to be per-Config

In 80673b4a4 (https://go.dev/cl/157820) I added a never-shrinking
package-global cache to remember which auto-detected auth style (HTTP
headers vs POST) was supported by a certain OAuth2 server, keyed by
its URL.

Unfortunately, some multi-tenant SaaS OIDC servers behave poorly and
have one global OpenID configuration document for all of their
customers which says ("we support all auth styles! you pick!") but
then give each customer control of which style they specifically
accept. This is bogus behavior on their part, but the oauth2 package's
global caching per URL isn't helping. (It's also bad to have a
package-global cache that can never be GC'ed)

So, this change moves the cache to hang off the oauth *Configs
instead. Unfortunately, it does so with some backwards compatiblity
compromises (an atomic.Value hack), lest people are using old versions
of Go still or copying a Config by value, both of which this package
previously accidentally supported, even though they weren't tested.

This change also means that anybody that's repeatedly making ephemeral
oauth.Configs without an explicit auth style will be losing &
reinitializing their cache on any auth style failures + fallbacks to
the other style. I think that should be pretty rare. People seem to
make an oauth2.Config once earlier and stash it away somewhere (often
deep in a token fetcher or HTTP client/transport).

Change-Id: I91f107368ab3c3d77bc425eeef65372a589feb7b
Signed-off-by: Brad Fitzpatrick <bradfitz@golang.org>
Reviewed-on: https://go-review.googlesource.com/c/oauth2/+/515675
TryBot-Result: Gopher Robot <gobot@golang.org>
Reviewed-by: Roland Shoemaker <roland@golang.org>
Reviewed-by: Adrian Dewhurst <adrian@tailscale.com>
Reviewed-by: Michael Knyszek <mknyszek@google.com>

---
## [TheGeekOnSkates/mobile-mainframe](https://github.com/TheGeekOnSkates/mobile-mainframe)@[90fdf0c19b...](https://github.com/TheGeekOnSkates/mobile-mainframe/commit/90fdf0c19bbbfb53854534e402d84dd42a5b56e2)
#### Wednesday 2023-09-13 13:29:05 by The Geek on Skates

Started reworking the tutorial into a micro-library (see commit notes)

Yes, I'm basically redoing some work I did at work.  And this is a total rewrite, not using any of the code I had in the version I wrote at work.  This is for two reasons:

1. Missed opportunities.  I can do some things here to make the API cleaner and easier to use than that little R&D project at work.
2. Software freedom.  Now I can honestly say, there is not a single BYTE of anything that ever was company code in this project.  And that's rad.  I'll delete the 2.0 branch when all this is done.

Still on my to-do list:

* Support multiple connections.  I want to do something like my old work version with socket_select; maybe like a WS_ForEach and you pass it a function or something like that.
* Wrap socket_read/write.  Make it simpler, like $input = WS_Read($client); and WS_Write("some data");
* Better error handling.  If it fails to send to a socket, for a reason other than the client disconnecting, then quit trying to talk to that client. :-)
* When it's all said and done, make this a separate GitHub repo.  It's light, doesn't require any ridiculous hoops to install it, and it works.  Write docs, do stuff with it, etc.
* Write that chat program and move on! :-)

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[fb4587b336...](https://github.com/Jolly-66/tgstation/commit/fb4587b3368ebb55e0cc10f8c650abcc26afa5d4)
#### Wednesday 2023-09-13 14:10:26 by san7890

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
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d034711fbc...](https://github.com/TaleStation/TaleStation/commit/d034711fbc29e9a28cc4af9c84f7597e2042c41a)
#### Wednesday 2023-09-13 14:32:36 by TaleStationBot

[MIRROR] [MDB IGNORE] Desouls Hivelord (#7690)

Original PR: https://github.com/tgstation/tgstation/pull/78213
-----
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

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[5a52df5219...](https://github.com/TaleStation/TaleStation/commit/5a52df5219cf78cefdac75fe6ac6d40921e74dc8)
#### Wednesday 2023-09-13 14:32:36 by TaleStationBot

[MIRROR] [MDB IGNORE] John Splintercell: a gun that is only good for shooting out lights (#7712)

Original PR: https://github.com/tgstation/tgstation/pull/78128
-----
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

Co-authored-by: Hatterhat <31829017+Hatterhat@users.noreply.github.com>
Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[98321c94d5...](https://github.com/TaleStation/TaleStation/commit/98321c94d543d39341d79cff114ca12b8bb5fb3d)
#### Wednesday 2023-09-13 14:32:36 by TaleStationBot

[MIRROR] [MDB IGNORE] SPESSMEN 2.0: le cargo resprite (no mining) ((i hate mining)) (#7459)

Original PR: https://github.com/tgstation/tgstation/pull/77456
-----
## About The Pull Request


![image](https://github.com/tgstation/tgstation/assets/86872535/3f43680a-36f0-4008-8e0f-3a1c4cee5427)

googoogagaga. hey guys, it's me! le crates guy!

cargo's resprite was about a year ago now, and i, and the spritetainers
who's approval I got, believe that it's time for a refresh. so uh. here
it is. yeah.

this PR adds a new piece of outerwear for cargo players to wear, a
gorka! some soviet eastern european larp-er jacket. looks cool tho.

and, as well, the quatermaster is now distinct compared to his
underlings- decked out with a spiffy overcoat and dress shirt.

now, you may be wondering about the fact that the cargo tech is now
wearing jeans? this is the new look for the cargo tech, but! before you
start soul posting, you can still infact, get shorts if you want.

really, I wanted it to be randomised, a coin-flip, but uh- that's not
possible lol.

random misc changes: changed PDA colours, qm wears laceups, cargo cap
was repainted

i got approval from both Wallemations and Imaginos16 for this PR and the
changes associated with it.
## Why It's Good For The Game

shruggers idk, i think it looks good. cargo is now much more visually
distinct, and has a better vision to it. quatermaster receiving a new
look that makes him stand out is a good thing too, imo.
## Changelog
:cl: axietheaxolot / viro
imageadd: brand new cargo sprites!
/:cl:

---------

Co-authored-by: axietheaxolotl <86872535+axietheaxolotl@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Lancej/PathOfBuilding](https://github.com/Lancej/PathOfBuilding)@[fb66ee7051...](https://github.com/Lancej/PathOfBuilding/commit/fb66ee70516cdb416b6f9c7799307c5757e199b2)
#### Wednesday 2023-09-13 14:55:31 by LocalIdentity

Fix accuracy of skill Mana/Life cost calculations (#6220)

* Rough code to male it work

* Recommit changes

* Fix breakdowns

* Correct values for Divine Blessing

* Fix breakdown when using Lifetap or Blood Magic

* Fix display of skills with innate Life Cost

---------

Co-authored-by: LocalIdentity <localidentity2@gmail.com>

---
## [codecov/codecov-api](https://github.com/codecov/codecov-api)@[e2c6b1c425...](https://github.com/codecov/codecov-api/commit/e2c6b1c425cac66f0d422bd5692c7aae4cc46b61)
#### Wednesday 2023-09-13 15:00:55 by Giovanni M Guidini

fix: lru_cache issues + meta info missing  (#72)

Context: https://github.com/codecov/engineering-team/issues/119

So the real issue with the meta info is fixed in codecov/shared#22.
spoiler: reusing the report details cached values and _changing_ them is not a good idea.

However in the process of debuging that @matt-codecov pointed out that we were not using lru_cache correctly.
Check this very well made video: https://www.youtube.com/watch?v=sVjtp6tGo0g

So the present changes upgrade shared so we fix the meta info stuff AND address the cache issue.
There are further complications with the caching situation, which explain why I decided to add the cached value in the
`obj` instead of `self`. The thing is that there's only 1 instance of `ArchiveField` shared among ALL instances of
the model class (for example, all `ReportDetail` instances). This kinda makes sense because we only create an instance
of `ArchiveField` in the declaration of the `ReportDetail` class.

Because of that if the cache is in the `self` of `ArchiveField` different instances of `ReportDetails` will have dirty cached value of other `ReportDetails` instances and we get wrong values. To fix that I envision 3 possibilities:
1. Putting the cached value in the `ReportDetails` instance directly (the `obj`), and checking for the presence of that value.
If it's there it's guaranteed that we put it there, and we can update it on writes, so that we can always use it. Because it is
for each `ReportDetails` instance we always get the correct value, and it's cleared when the instance is killed and garbage collected.

2. Storing an entire table of cached values in the `self` (`ArchiveField`) and using the appropriate cache value when possible. The problem here is that we need to manage the cache ourselves (which is not that hard, honestly) and probably set a max value. Then we will populate the cache and over time evict old values. The 2nd problem is that the values themselves might be too big to hold in memory (which can be fixed by setting a very small value in the cache size). There's a fine line there, but it's more work than option 1 anyway.

3. We move the getting and parsing of the value to outside `ArchiveField` (so it's a normal function) and use `lru_cache` in that function. Because the `rehydrate` function takes a reference to `obj` I don't think we should pass that, so the issue here is that we can't cache the rehydrated value, and would have to rehydrate every time (which currently is not expensive at all in any model)

This is an instance cache, so it shouldn't need to be cleaned for the duration of the instance's life
(because it is updates on the SET)

closes codecov/engineering-team#119

---
## [pippinbarr/v-r-5](https://github.com/pippinbarr/v-r-5)@[2f37a867d3...](https://github.com/pippinbarr/v-r-5/commit/2f37a867d302869708d5ff2b5380906489f305d0)
#### Wednesday 2023-09-13 15:01:28 by Pippin Barr

Got grid snapping working

- I actually did this yesterday but didn't get to writing this commit message until just now because life is the hottest of messes at the moment
- I had a breakthrough with ProBuilder (a stupid one but still) where I realized I was having trouble lining stuff up because when I was creating the initial cube I would extrude into the room I wasn't aligning it with the grid first, thus the first change would snap to the grid and thus make the whole thing off by some fraction of a unit. Once I placed the initial cube on the grid it all lines up like a dream. So now I can remake my rooms and I assume they won't have seams - well let's see.

---
## [OSZKAT/my_first_repo](https://github.com/OSZKAT/my_first_repo)@[a8635e98c2...](https://github.com/OSZKAT/my_first_repo/commit/a8635e98c2d8d7db51aa6f1ebfe5aef60daa1e73)
#### Wednesday 2023-09-13 15:10:20 by daanworks

i wanted to write a great commit message instead of fuck you

---
## [PeterMoroz/linux](https://github.com/PeterMoroz/linux)@[561d896a14...](https://github.com/PeterMoroz/linux/commit/561d896a14684eb648a138fd18f9084c51b2dd14)
#### Wednesday 2023-09-13 16:06:07 by Michal Vlasák

tools: labs: qemu: Add run-qemu.sh as alternative

TL;DR: In one window run `make -j$(ncproc) console` and `cd` to some
lab's subdirectory (`skels/...`). In second window `cd` to matching
`skels/...` subdirectory, edit source files and compile with something
like `kmake` (`alias kmake='make -C "$HOME/src/linux/" M="$(pwd)"'`) as
needed. The `skels` directory is shared between the host and the guest,
thus in the first window, so you can just `insmod` and `rmmod` the
compiled modules. You can kill the VM by `CTRL-a x` (if you made some
writes from the VM it might be a good idea to run `sync` first). Samba
and QEMU are required.

Full description:

To be honest I don't like the current QEMU setup. I am sure there are
things it does that I don't understand yet, because I have not yet
finished all the labs, but in any case I think that the setup can be
improved.

Some things in particular I don't like about the current setup:

 - "Huge" opaque `.ext4` images are used, even though the contents of
   the  root file system are not that large.
 - While running QEMU newly built modules can't be copied to the image.
 - Mounting and unmounting the `.ext4` image for copying the modules
   requires `sudo`.
 - The networking setup seems too complex, requires `sudo` and was
   broken (at least for me - IIRC I didn't get IP through DHCP), thus I
   also didn't get `ssh` to work. I also seem to be not the only one
   having issues with this:
   https://github.com/linux-kernel-labs/linux/pull/240#issuecomment-956219190
 - `dnsmasq` and `nttctp` mostly don't start correctly (they are not
   killed correctly by the previous run) - this isn't a problem on my
   end, as demonstrated by the output at
   https://linux-kernel-labs.github.io/refs/heads/master/info/vm.html,
   which shows the same issues.
 - Running `minicom` is required to access the serial port, thus at
   least two terminals are required for working with the VM (not a huge
   problem for me personally, since I use `tmux`, but I know some people
   complain about this). The setup also seems unnecessarily complex.
 - I remember a lot of the `.mon` `.pts` files being left uncleaned in
   some cases.
 - I recall warnigns about some of the entries added to `/etc/inittab`
   being ignored.
 - Even though root login requires no password I have to enter the
   `root` username.

In this commit I introdoce an alternative way of running QEMU through a
new `run-qemu.sh` script. The setup is laregely independent and its user
interface consists of `console` and `gui` targets. I tried to make the
script parameterizable through environment variables (inherited from
Make variables), though it may be argued that the default values should
be encoded in Makefile rather than in the script like they are now. I
have no strong opinions about that, it's' just that the current state
allows running the script in standalone fashion.

What the setup brings:

 - A rootfs is extracted from the official Yocto Project tarball and
   kept in a directory that is shared through  [Samba as network
   share](https://www.kernel.org/doc/html/latest/filesystems/cifs/cifsroot.html).
   The `skels` directory is shared as well. Thus the modules can be
   freely tweaked / compiled / ran from either the host or guest.
 - The QEMU stdio serial console setup is used (`ttyS0` on the kernel
   side). This means that running QEMU results in the serial console
   being mapped directly to standard input and output of the terminal -
   `minicom` is not needed. This is the console mode (`make console`).
 -  The setup allows also allows the virtual machine to be run in
    graphical mode (`make gui`).
 - Root is logged in automatically in `console` mode (though similar
   thing could be done for the `gui` mode).
 - Although Samba (`smbd`) is required, `sudo` or root access is not.
 - Networking through QEMU's default [SLIRP backend](https://wiki.qemu.org/Documentation/Networking#User_Networking_.28SLIRP.29).
   DHCP is handled by the kernel, which overcomes some problems I had
   with the System V init system in the Yocto images.
 - The compilation can largely be done with something like this `kmake`
   alias: `alias kmake='make -C "$HOME/src/linux/" M="$(pwd)"'`
   (customize as needed). Though this is not enough for some labs (I no
   longer remember the details, but I think it was some of the earlier
   labs which had dependencies between modules, I think I used the
   classic `make build` for that.

Known issues:

 - SSH support is currently missing. This both requires more featureful
   Yocto images and is IMO unnecessary, since it wouldn't bring much
   benefit over the console mode. Though it can be easily achieved by
   using QEMU option like `-nic user,hostfwd=tcp::2222-:22`, which would
   allow SSH'ing into the guest by something like `ssh -p 2222
   root@localhost`.
 - I used a slightly less advanced setup while doing the labs, so the
   lab workflow with this particular setup is largely untested. There
   may be problems with file permissions due to the samba share.
 - The guest seems to fail to shutdown correctly in a timely manner. I
   just took the habbit of killing qemu with `CTRL-a` followed by `x`,
   potentially running `sync` first to ensure my work is saved (though
   rarely did I actually modify anything on the guest side).

[The former setup](https://github.com/vlasakm/linux/commit/720bd6444a036c2ae6a3e76b7f6aac72f562053a)
I used contains some details of the SSH setup if anyone is interested in
that. It was the basis for this PR, so some ideas can be seen there
(Samba share for `skels`), but I didn't take particular care with [the
kernel config](https://github.com/vlasakm/linux/commit/0290919905e7f4fe3562a46d3274f8d41ad02c55)
and the automounting didn't really work (the `init` would try to mount
the filesystem before networking was up).

What I evaluated and didn't use in the end:

 - At first I tried to extend my former setup by just automounting the
   Samba share. I didn't manage to do this - the (non)workings of init
   scripts seem to be beyond me. If anyone is interested here are a few
   pointers:
   [[1]](https://unix.stackexchange.com/questions/169697/how-does-netdev-mount-option-in-etc-fstab-work),
   `/etc/inittab`, `/etc/init.d/mountall.sh`, `/etc/init.d/mountnfs.sh`.
 - I tried using `9p` [[2]](https://wiki.qemu.org/Documentation/9p),
   [[3]](https://wiki.qemu.org/Documentation/9psetup)
   [[4]](https://wiki.qemu.org/Documentation/9p_root_fs) which is built
   into QEMU and can be compiled into the kernel. With `mapped-xattr`
   security model it would be too cumbersome to create the rootfs, and
   `passthrough` would require root privileges. It is also very slow.
   There are also some problems with trying to use it as rootfs, maybe
   specific to `linux-kernel-labs` kernel version or config. Ask me if
   interested.
   [[5]](https://lists.gnu.org/archive/html/qemu-devel/2016-09/msg07184.html)
   [[6]](https://lore.kernel.org/linux-fsdevel/20210608153524.GB504497@redhat.com/)
   [[7]](https://lore.kernel.org/all/YL1eM+mzjuggDvqp@codewreck.org/T/)
 - QEMU has an option to setup the Samba share on its own, though I
   found a custom config (based on the QEMU one) to be easier - allows
   customization like multiple shares, unix extensions, different port,
   etc.

Signed-off-by: Michal Vlasák <lahcim8@gmail.com>
Signed-off-by: Daniel Baluta <daniel.baluta@nxp.com>

---
## [Rabiulislam30/Sentiment-Analysis](https://github.com/Rabiulislam30/Sentiment-Analysis)@[31ede9ff73...](https://github.com/Rabiulislam30/Sentiment-Analysis/commit/31ede9ff732e4b97427759b4f1b1267d92311a7d)
#### Wednesday 2023-09-13 16:39:35 by RABIUL ISLAM

Add files via upload

Project Title: Sentiment Analysis for Text Data

Description:

Welcome to the Sentiment Analysis for Text Data project! 📊📝

This project is all about understanding and analyzing the emotions, attitudes, and sentiments expressed in text data. Whether you're interested in tracking customer feedback, monitoring social media sentiments, or gaining insights from user reviews, sentiment analysis can be a powerful tool.

Key Features:

🔍 Text Preprocessing: The project includes robust text preprocessing techniques to clean and prepare your data for sentiment analysis. This step ensures that your analysis is accurate and meaningful.

📈 Sentiment Scoring: We utilize the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool to score text data for sentiment. VADER is a reliable and well-established tool for this task.

📊 Visualization: Dive into the results with informative visualizations! We provide charts and graphs to help you understand the sentiment trends in your data.

👩‍💻 Code: All the code used in this project is open-source and available on GitHub. You can easily access and adapt it to your specific needs.

📄 Documentation: We've included comprehensive documentation to guide you through the project setup, usage, and customization. It's a helpful resource to get started quickly.

Why Sentiment Analysis?:

Sentiment analysis has numerous applications across various industries:

Customer Feedback: Understand how your customers feel about your products or services.
Social Media Monitoring: Keep an eye on the sentiment surrounding your brand on social media platforms.
Market Research: Analyze market trends and consumer sentiment.
Product Reviews: Evaluate product reviews to make data-driven decisions.
Getting Started:

Clone or download the project repository from GitHub.
Follow the setup instructions in the documentation to get the project up and running.
Import your own text data or use the provided sample data for analysis.
Run the sentiment analysis and explore the results.
Contributions:

We welcome contributions from the open-source community! Feel free to submit bug reports, feature requests, or even pull requests to improve this sentiment analysis project.

Let's gain valuable insights from text data and understand the sentiments expressed within it. Happy sentiment analyzing! 🚀📊

---
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[6c34d93be7...](https://github.com/Zergspower/tgstation/commit/6c34d93be715012943626d0f812e99f730a536ef)
#### Wednesday 2023-09-13 16:57:35 by necromanceranne

Nukies Update 7: Hats (Also massive uplink standardization, weapon kits and ammo changes) (#77330)

## About The Pull Request

Massively overhauls and standardizes the nuclear operative uplink. 

### Weapon Kits

Essentially, all the main weapons of the uplink have been changed to
instead come as 'weapon kits', which are essentially cases containing a
weapon loadout to enable operatives to easily start operating on only
just one item purchase, without the fuss of worrying whether or not
operatives are getting spare ammo, or getting relevant equipment for
success. Consider this a pseudo-loadout, though without necessarily
restricting the purchasing of more weapon kits.

All kits come in three categories: Low Cost (8 TC), Medium Cost (14 TC)
and High Cost (18 TC). This is also matched by categorized ammo costs;
Basic Ammo (2 TC), Hollow Point and Armour Penetrating (4 TC),
Incendiary (3 TC) and Special (or anything that does not easily fit
these categories and does something real extra) (5 TC). Weapons that
lacked these ammos have gained these ammo types to fill the gaps.

<details>
There is may one exception to this in disruptor ammo, which is priced as
basic ammo if only because it isn't _quite_ good enough to justify
pricing at 5 tc and I can see an op wanting to use it as a basic ammo
type instead of normal .50 BMG against, say, a silicon/mech heavy
opposition. Since it cannot kill organics on its own, I'll consider this
mostly basic-adjacent
</details>
The kits have also been labelled based on potential difficulty. This
reflects possible difficulties in using the item, how conducive it is to
success for how much game knowledge needed to actually use it, and how
likely an op is to succeed using it. I don't expect ops to win using
nothing but a rocket launcher, but I think ops should get a fair shake
at trying, yeah?

The kits are as below:
#### **Low-Cost**
_Bulldog (Moderate):_ Shotgun and three magazines of standard ammo.
_Ansem (Easy/Spare):_ Pistol and three spare magazines of standard ammo.
#### **Medium Cost**
_C-20r (Easy):_ SMG and three spare magazines of standard ammo.
_Energy Sword and Shield (Very Hard):_ Energy sword and shield. (Also a
special hat)
_Revolver (Moderate):_ Revolver and three speedloaders of standard ammo.
_Rocket Launcher (Hard):_ Rocket launcher with three spare rockets.
#### **High Cost**
_L6 SAW (Moderate):_ LMG, and that's it. No spare ammo.
_M-90gl (Hard):_ Rifle, two spare magazines of standard ammo and a box
of rubber grenades.
_Sniper (Hard):_ Sniper rifle, two spare magazine of standard ammo, and
one magazine of disruptor ammo. Also suit and tie.
_CQC (Very Hard):_ Comes with a stealth implant and a bandana.
_Double-Energy Sword (Very Hard):_ Double-energy sword, syndicate soap,
antislip module, meth injector and a prisoner jumpsuit.
_**NEW** Grenadier's Kit (Hard):_ Grenadier's belt and grenade launcher
(the one that launchers chem grenades). (I replaced the shit acid
grenade with another flashbang in the belt)

Surplus SMG (Flukie difficulty) has been unchanged. It just now comes
with two rations.

Includes two new revolver ammo types: Phasic, which goes through walls
and armor, but has significantly less damage as a result (I've equalized
the revolver damage and the rifle version's damage to 30 for both). And
Heartseeker, which has homing bullets. Both are Special ammo, and are
priced at 5 TC a speedloader.

### Other Gear

The other items in the uplink have also been consolidated and
standardized in various ways.

#### Grenades

Most now cost 15 TC for three grenades of any given type (including the
full fungal tuberculous). This is pretty much identical to the previous
price, just more consistent overall and front-loaded in cost.

#### Reinforcements

All the various reinforcements now cost 35 TC and all refundable,
equalizing cost to the average across the reinforcements. This is
primarily because I feel like all these options should be weighed
equally, and not one of these options are necessarily worse or better
than the other in their current balance. They're largely inaccessible
for normal ops regardless, and typically come out when there is a
discount or war ops. I took the average value and went with it. Not much
more to say.

#### Mechs

They're just cheaper. These things still suck and they need help.
They've always needed help. A slightly less excessive value for the
mechs may help see people willing to spend the TC on them. I doubt it. I
seriously suggest not buying these still. I keep them in primarily
because they are big stompy mechs and are kind of iconic 'war ops' gear.

#### Bundles

Since I've implemented weapon kits, gun bundles are rather redundant. So
the bulldog weapon and ammo bundle, the c20-r weapon and ammo bundle and
technically the sniper bundle were removed. The sniper bundle is now the
weapon kit, obviously.

Nothing else here really. Except for one....

#### Implants

Not much changed here. I standardized the implant prices to 8 TC a pop.
This is in accordance with traitor implants, which ops also get. So
everything in this category bar a few exceptions (like macro/microbombs)
are around 8 TC. Makes sense to me, really.

Importantly, I made the Implant bundle 25 TC, and I unrandomized the
contents. Who in the right fucking mind would spend 40 TC just to get
five reviver implants is beyond me. But instead, you get one of each of
the cybernetic implants except thermal eyes (you can just buy thermals
and get the benefit of both vision types; x-ray and thermal vision, if
you want to use smokescreens a lot).

#### Base Keys

They're all now 15 TC, except the fridge which is 5 TC. It's weird
they're valued differently when they are taken mostly to do gimmicks
like xenobio and toxins in a hurry before hitting the station. So we've
standardized it.

## Hat Crate

**YES, GOOD SIR, YOU TOO CAN ORDER A HAT CRATE FROM THE SYNDICATE STORE
FOR ONLY 5 TC!**

**NO NEED FOR A KEY, JUST BUY IT AND PULL IT OPEN WITH YOUR STANDARD
ISSUE CROWBAR!**

**ENJOY YOUR NEW CRATE! ENJOY YOUR NEW HAT!**

**PUT IT ON USING THE FREE HAT STABILIZERS WE INCLUDED WITH THE HATS!**

~~**NO REFUNDS IF YOU GET BLOOD ON YOUR HAT!**~~

<details>
There is a 1% chance to instagib people with direct hits from a rocket.
This does the crit effect.
</details>

## Why It's Good For The Game

The uplink needed more spring cleaning and standardization.

With this, I've partially implemented my older idea for ammo consistency
and initial allowance for nukies. Ammo is kind of over-priced and often
where a good chunk of TC goes towards without really pushing nukies
towards meaningful success. And it is often what is tripping up new
players who didn't think to get any. Now, when they get a gun, they get
ammo in their case. On top of this, the weapon kit category is both at
the top of the uplink AND has a little label to say 'Recommend', so that
these new players will hopefully know they should be looking there
first.

In addition, it is the gateway towards a concept that is currently being
worked on. Nuclear operatives having some degree of predefined loadouts
for players to select if they aren't sure what they want, or don't know
what to get. Nukies is very confusing for many players. So giving them a
fighting chance with some premade setups can help ease them into the
role without needing too much player knowledge in how to apply the
items. This is only one step towards that, so that players can identify
what gear they need to help succeed based on their skill.

I wanted to implement a difficulty warning so that players can choose
gear loadouts that are actually conducive to their skill and knowledge.
I based it on how much players would need to know to engage in combat
with it, and how much fiddling is required to get something to work
properly (overly involved reloading is a consideration, for example, as
well as precise button presses). In addition, how much of a force
multiplier some weapons can be for their ease of use.

Most people recognize the c20-r as the most new player friendly weapon,
as an example. So it would be good to steer players towards taking that
gun because of how easy it is to use, understand and succeed with it.

And most importantly of all; Having standards within the uplink is
important. Most of the values in the uplink are just completely random.
Nobody has a good grasp of what is too much or too little. Even just a
hint of consistency, and people will stick to it (see implants for what
I mean). And there is still some work to be done even there. A good
start is weapons. Price for power can be meaningful when decided whether
we want some weapons to come out more often than others. Players do
enjoy making informed decisions and choices, and having affordability be
a draw to some otherwise less powerful weapons (looking at you, Bulldog)
can actually be a worthwhile and meaningful difference.

~~I thought it would tick off the gun nerds to change the calibers on
the guns.~~

~~I also thought adding hats would be funny given the release of TF2's
most recent update.~~

## Changelog
:cl:
balance: Standardizes some of the nuclear operative entries to have more
consistent pricing within their respective categories.
add: Adds some new categories so that players have an easier time
navigating the nuclear operative uplink.
balance: Many items have had prices reduced or adjusted to make them
more desirable or more consistent within their category.
add: Weapon kits have replaced almost all the individual weapons in the
uplink. You now buy these instead of the individual weapon. These often
come with spare ammo or relevant gear for success.
add: Most ammo types have been standardized in price.
refactor; Removes a lot of redundant item entry code and tidies up the
actual code part of the nuclear uplink so that it is much easier to find
things within it.
add: Added 40 new cosmetic items to the Syndicate Store. Buy them now
from the Hat Crate, only 5 TC!
code: Updated the nuclear operative uplink files.
/:cl:

---
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[95ec0e6545...](https://github.com/Zergspower/tgstation/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Wednesday 2023-09-13 16:57:35 by necromanceranne

Dissection experiments are handled by autopsy surgery. Removes redundant dissection surgery. You can repeat an autopsy on someone who has come back to life. (#77386)

## About The Pull Request

TRAIT_DISSECTED has had the surgical speed boost moved over to
TRAIT_SURGICALLY_ANALYZED.

TRAIT_DISSECTED now tracks if we can do an autopsy on the same body
again, and blocks further autopsies if it is on the mob. A mob that
comes back to life loses TRAIT_DISSECTED. This allows for mobs to be
autopsied once again.

Since it is completely redundant now (and was the whole time TBH),
dissections have been removed in favour of just having the experiment
track autopsies.

Fixes https://github.com/tgstation/tgstation/issues/76775

## Why It's Good For The Game

Today I showed up to a round where someone autopsied all the bodies in
the morgue, not realizing they were using the wrong surgery. Since I
couldn't _redo_ the surgery, this rendered all these bodies useless.
This was not out of maliciousness, they just didn't know better. There
are two autopsies in the surgery list, but only one is valid for the
experiment and doing the wrong one blocks _both surgeries_. Dissection
is completely useless outside of experiments. This same issue also
prevents additional autopsies on the same person, even if they had come
back to life and died again after you had done the initial autopsy.
Surely you would want to do more than one autopsy, right? That's two
separate deaths!

This resolves that by giving you a method of redoing any screwups on the
same corpse if necessary. It only matters if the experiment is available
anyway, so there isn't much reason to punish players unduly just because
they weren't aware science hadn't hit a button on their side (especially
since it isn't communicated to the coroner in any way to begin with). It
also removes a completely useless surgery and ties in the experiment to
what the coroner is already going to be doing. They can dissect their
corpses to their hearts content without worrying about retribution from
science for doing so.

In addition, someone repeatedly dying can continue to have autopsies
done on them over the course of the round. The surgery bonus only
applies once, so the only reason to do autopsies after the first is to
discover what might have killed someone. No reason this should block
further surgeries, just block surgeries when the person remains a
corpse.

## Changelog
:cl:
fix: You can do autopsies on people who were revived and died again
after they had already been dissected.
qol: Autopsies have become the surgery needed to complete the dissection
experiments. As a result, the dissection surgery has been removed as it
is now redundant.
qol: A coroner knows whether someone has been autopsied and recently
dissected (and thus hasn't been revived) by examining them.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [McRamon/Paradise](https://github.com/McRamon/Paradise)@[acb7352265...](https://github.com/McRamon/Paradise/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Wednesday 2023-09-13 17:07:34 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[9dbf819e8a...](https://github.com/cmss13-devs/cmss13/commit/9dbf819e8a0512809c54ae8aae43749265a939bf)
#### Wednesday 2023-09-13 17:48:31 by forest2001

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
## [TasnimOy/EmotionRecognition](https://github.com/TasnimOy/EmotionRecognition)@[29536e6d1e...](https://github.com/TasnimOy/EmotionRecognition/commit/29536e6d1ec15ee53bc2332de13779327f31c35c)
#### Wednesday 2023-09-13 17:49:20 by Marzan Tasnim Oyshi

Add files via upload

This repository contains the code for extracting audio features and predicting emotions from audio files using deep learning techniques.

Table of Contents

Overview
File Structure
Getting Started
Datasets Used for Training
References
1. Overview

The provided code is structured in the following manner:

Feature Extraction: Extract various audio features such as ZCR, Chroma_stft, MFCC, RMS, MelSpectogram, Spectral Contrast, Spectral Entropy, and Pitch from .wav audio files.
Model Definition: Define a Conv1D deep learning model to classify emotions based on extracted features.
Model Training: Train the model on preprocessed data.
Model Evaluation: Evaluate the trained model's performance on test data and visualize results.
Prediction on New Data: Predict emotions on new audio files using the pre-trained model and evaluate the distribution of predicted emotions.
2. File Structure

The main files include:

feature_extraction.py: Contains the code for extracting audio features.
model_definition_training.py: Contains the code for defining, training, and evaluating the model.
predict_on_new_data.py: Contains the code for predicting emotions on new audio files.
3. Getting Started

Make sure you have the required libraries installed. This includes:
librosa
numpy
pandas
parselmouth
os
tensorflow
scikit-learn
joblib
matplotlib
Set the appropriate paths for DATA_DIR and OUTPUT_CSV in the feature_extraction.py file to specify where your audio files are stored and where the extracted features should be saved, respectively.
Run the feature extraction code to generate the .csv file with extracted features.
In model_definition_training.py, set the dataset_path variable to the path of the generated .csv file.
Train the model and evaluate its performance.
For predicting emotions on new data, update the paths in predict_on_new_data.py and run it.
4. Datasets Used for Training

RAVDESS: The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS) encompasses audio and video data from professional actors expressing a range of emotions. The dataset covers eight distinct emotions and each emotion is captured in two intensity levels. The dataset offers both audio and video recordings, with an equal representation of male and female actors. [1]

TESS: The Toronto Emotional Speech Set (TESS) is designed specifically with the older demographic in mind. TESS consists of emotional speech samples from older adult female actors. It covers seven emotions through 200 lexically matched statements. [2]

IEMOCAP: The Interactive Emotional Dyadic Motion Capture (IEMOCAP) dataset contains approximately 12 hours of audio-visual data, including video, speech, motion capture of facial movements, and text transcriptions. This dataset captures a wide range of emotions in various contexts from ten actors in dyadic sessions. For this project, the emotions 'frustrated' and 'excited' were utilized. [3]

5. References

Livingstone, S. R., & Russo, F. A. (2018). The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS): A dynamic, multimodal set of facial and vocal expressions in North American English. PloS one, 13(5), e0196391.
Pichora-Fuller, M. K., et al. (2020). Toronto Emotional Speech Set (TESS).
Busso, C., et al. (2008). IEMOCAP: Interactive emotional dyadic motion capture database. Language resources and evaluation, 42(4), 335.

---
## [Khan/jenkins-jobs](https://github.com/Khan/jenkins-jobs)@[073d8c550f...](https://github.com/Khan/jenkins-jobs/commit/073d8c550f42fe091dd5b6cafe4c6b17a6caa738)
#### Wednesday 2023-09-13 18:05:45 by Craig Silverstein

Make the paths set in onWorker and onMaster match .profile. (#134)

## Summary:
Sadly, jenkins doesn't exec `.profile` or `.bashrc` when running
jenkins jobs, it just uses the same path the jenkins binary uses.

On the workers, the jenkins binary (actually the `jar slave.jar`
process) runs via ssh, which *does* exec `.profile`, so all jenkins
jobs on workers run with the path that's in `.profile`.

But on the main jenkins server, the jenkins binary (`jar jenkins.jar`)
runs via systemd, which uses its own default path.  In particular,
systemd runs as root (and later does a proces-chown to the jenkins
user), so it does not use jenkins's .profile.

There might be some way to change this in systemd, but that's pretty
black magic.  Instead, we just set the path we want in our
onWorker.groovy and onMaster.groovy scripts, which run at the
"outside" of all our jenkins jobs.

Unfortunately, the paths set in those scripts had gotten out of date
with the path set in the .profile file.  I get them back in sync, and
add a breadcrumb in .profile so hopefully if the path changes again,
we'll update it everywhere we need to.

This lets me remove the explicit path-adding in
update-devserver-static-images.groovy, which was always an awkward
hack.

Issue: none

## Test plan:
Fingers crossed.  In theory this shouldn't affect any jobs, but we'll
have to land it and see..

Author: csilvers

Reviewers: dbraley, csilvers, #infra-platform

Required Reviewers:

Approved By: dbraley

Checks:

Pull Request URL: https://github.com/Khan/jenkins-jobs/pull/134

---
## [cakexensen/russ-station](https://github.com/cakexensen/russ-station)@[297f7f88e8...](https://github.com/cakexensen/russ-station/commit/297f7f88e866d4a17b27cb15c0b8ee606742bbf6)
#### Wednesday 2023-09-13 18:15:21 by Sealed101

Fixes things about goliaths: wallhacks/range hacks(no, really) and tentacles not spawning in mineral turfs; also fixes `find_potential_targets` wallhacks (#77393)

## About The Pull Request

Goliath's sand digging behaviour could potentially target a turf that's
actually unreachable by the goliath, e.g.
```
G#
#T
```
where G - goliath # - wall T - target turf. fixed that, but i think
there could be something easier here, maybe instead grabbing turfs in
goliath's `view()`? unsure

The component goliaths use to telegraph their attacks
(`basic_mob_attack_telegraph`) casts a `do_after()` to perform the
attack, but it was not actually checking for the target staying in melee
range, as it was using the source goliath as both `user` and `target`,
so it didn't actually care at all for the target. Implemented an
`extra_checks` to `Adjacent()` since that's the closest we get for melee
range shenanigans I suppose
This still allows the source basicmob to attack the target if the target
moves around the source basicmob.

`!`Goliaths were also able to summon tentacles on a target that moved
into cover and still stayed in the `find_potential_targets` target
range. Which meant more wallhacks. This was a thing for the base
`find_potential_targets`, meaning that every basic mob using it was a
dirty haxxor (or very vengeful). Fixed that by making
`find_potential_targets` also check for `can_see()` before proceeding
further down `find_potential_targets/perform()`. `!` The only exception
to this check currently are bileworms.

`!`Goliath tentacles were not spawning in mineral turfs as their
`Initialize()` checked for closed turfs before handling mineral turf
mining. Fixed that as well.

## Why It's Good For The Game

![Dr__Hax_by_Didgeridoo_Dealer](https://github.com/tgstation/tgstation/assets/75863639/fbcbfc1b-f489-435e-bb01-677f55398787)

## Changelog

:cl:
fix: fixed goliaths digging sand that they can't actually reach (behind
windows or inbetween closed turfs)
fix: fixed goliaths melee attacking their target despite the target
running away from goliath melee range
fix: fixed goliath tentacles not spawning in mineral turfs
fix: fixed goliaths summoning tentacles on targets that moved behind
cover but stayed in their targeting range. this applies for most basic
mobs, really, so if any basic mob was targeting you despite you hauling
ass behind cover, they shouldn't anymore
/:cl:

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[b033e1ed6a...](https://github.com/MarkSuckerberg/Shiptest/commit/b033e1ed6a1e7f87edc73a75a96bcf6536e39aba)
#### Wednesday 2023-09-13 18:21:46 by Sun-Soaked

Update_Appearance Port (#2170)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
[(original pr)](https://github.com/tgstation/tgstation/pull/55468)
After nine years in development we hope it was worth the wait

I ported this specifically for the signals I'll need for world icons.
However, it had a lot of other useful stuff, so I ended up just grabbing
(almost) the entire pr.
I tried to grab as few of the superfluous code rewrites as possible to
make reviewing a bit easier, but I couldn't help grab stuff like the APC
icon code rewrite(the original code was a war crime).

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

- ports the wrapper proc `update_appearance` for icons, descs, and
names, adds `update_desc` and `update_name` subprocs to handle those.
Things. without just stuffing them into update_icons like some kind of
psychopath

- ports a bunch of signal hooks useful for changing names, descriptions,
and icons. I needed these for world_icons which is where this wild ride
all started

- ports some `base_icon_state` implementation. Stuff like spear code
makes slightly less duplicates(and more sense) now which is nice.
We could definitely implement it more I think but that's a future me
problem

- 500 files of immersive vsc-mass-editing action to implement
`update_appearance()`(sorry in advance, but not as sorry as I was when
manually copy-pasting the custom ones for like 3 straight days)

-"consig" and "comisg" have been taken out behind the codebase and shot.
Not 'technically' a bug it just made my head hurt

-My first pr with 0 player facing changes (confetti)
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: TemporalOroboros, Memed Hams
code: ports update_appearance, update_name, and update_desc from tg, as
well as associated signals
code: a bit of base_icon_state implementation. Can you believe it's been
sitting in our code almost unused for like 3 years
code: cleans up some code formatting, mainly around custom icons and
overlays
code: fixes the typos in COMSIG_STORAGE_EXITED and
COMSIG_STORAGE_ENTERED
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [StarStation13/Save-Our-Ship-test](https://github.com/StarStation13/Save-Our-Ship-test)@[ee4021c507...](https://github.com/StarStation13/Save-Our-Ship-test/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Wednesday 2023-09-13 19:32:42 by Imaginos16

Destroying Sprite Cruft Part One: Cruft Sucks (#2220)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Title


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/1cedcdb1-01b5-4f28-a759-65428c2dcd0a)

In total, the:

- IV Drip
- All-In-One Grinder
- Book Binder
- Book Scanner
- Water Cooler
- Tank Dispenser

Have all been successfully uncrufted. No more cruft. Just clean sprites
now :D

Oh and dressers have directionals now at the request of @Bjarl 

Credit goes to the original authors in the changelog.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
begone cruft I fucking hate cruft
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy, Maxymax13, Wallemations, Kryson,
Viro/Axietheaxolotl, MeyHaZah
imageadd: Books, IV drips, tank dispensers, all-in-one grinders, water
coolers, book binders and book scanners have been resprited!
imageadd: Dressers now have directionals!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [andrewyernau/StardewValley](https://github.com/andrewyernau/StardewValley)@[dcbbbaa175...](https://github.com/andrewyernau/StardewValley/commit/dcbbbaa175e502259cb55174c497c3e3796dfbc8)
#### Wednesday 2023-09-13 21:31:44 by StreakerOne

delete files so i can fucking review stuff, fuck you, github

---
## [MaskRay/llvm-project](https://github.com/MaskRay/llvm-project)@[2b7373cbf7...](https://github.com/MaskRay/llvm-project/commit/2b7373cbf7ee8abbfaec33bea5a7673f31afea7f)
#### Wednesday 2023-09-13 22:14:57 by Fangrui Song

[ELF] Align the end of PT_GNU_RELRO associated PT_LOAD to a common-page-size boundary

Close #57618: currently we align the end of PT_GNU_RELRO to a common-page-size
boundary, but do not align the end of the associated PT_LOAD. This is benign
when runtime_page_size >= common-page-size.

However, when runtime_page_size < common-page-size, it is possible that
`alignUp(end(PT_LOAD), page_size) < alignDown(end(PT_GNU_RELRO), page_size)`.
In this case, rtld's mprotect call for PT_GNU_RELRO will apply to unmapped
regions and lead to an error, e.g.

```
error while loading shared libraries: cannot apply additional memory protection after relocation: Cannot allocate memory
```

To fix the issue, apply two changes:

* in the presence of SECTIONS: change DATA_SEGMENT_RELRO_END (see also https://reviews.llvm.org/D124656) to use max-page-size instead of common-page-size
* in the absence of PHDRS/SECTIONS: ensure the end of the PT_LOAD program loader associated with the PT_GNU_RELRO segment is aligned to a common-page-size boundary.

To prevent strip from corrupting PT_LOAD program headers, add a padding section
.relro_padding like mold.

In the presence of PHDRS/SECTIONS commands, we don't add .relro_padding or align
the end of PT_GNU_RELRO. This is different from the previous behavior where we
unconditionally aligned the end of PT_GNU_RELRO to a common-page-size. I think
this change is acceptable. Most SECTIONS users don't use RELRO anyway.

---

Close #65002: GNU ld from 2.39 onwards aligns the end of PT_GNU_RELRO to a
max-page-size boundary (https://sourceware.org/PR28824) so that the last page is
protected even if system-page-size > common-page-size.

In my opinion, losing protection for the last page when the system page size is
larger than common-page-size is not really an issue. Double mapping a page of up
to max-common-page for the protection could cause undesired VM waste. Internally
we had users complaining about 2MiB max-page-size applying to shared objects.

Our two RW PT_LOAD design gives more flexibility.
I believe we should keep common-page-size as the RELRO alignment boundary,
otherwise the setting is just useless. Users who are really anxious can set
common-page-size to match their system page size.

---

17 tests need updating as there are lots of change detectors.

* avoid-empty-program-headers.s: test that if the only RELRO section is .tbss, we don't need .relro_padding
* ppc64-toc-addis-nop.s: that that when PHDRS is used, we should not need .relro_padding

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[06e7270008...](https://github.com/jlsnow301/tgstation/commit/06e7270008d4b49a7e73fd088135822a9ec76891)
#### Wednesday 2023-09-13 22:44:05 by GuillaumePrata

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[2a3b489eaf...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/2a3b489eaf176cfd9c9b85cc87c42927b7aa26e6)
#### Wednesday 2023-09-13 22:44:41 by SkyratBot

[MIRROR] Conveyor Belts are now easier to extend and have screentips [MDB IGNORE] (#23679)

* Conveyor Belts are now easier to extend and have screentips (#78278)

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

* Conveyor Belts are now easier to extend and have screentips

---------

Co-authored-by: ArcaneMusic <41715314+ArcaneMusic@users.noreply.github.com>

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[7d600bf36a...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/7d600bf36a691d4be27e852eed0106a1564d7aee)
#### Wednesday 2023-09-13 23:07:17 by TheObserver-sys

More plants, new chems, new carpet generation techniques, plantcell buff, and the drills now have a GPS signal! (#5912)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![image](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/assets/58029438/4d3a51f1-7d2b-4d56-9971-7f33d76610f1)

![image](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/assets/58029438/608ba481-2499-4bf0-a25c-cc503655bf7d)

New! Exciting! Things! YEEHAW!

Okay, hype aside, this adds two plants from Main -- the third, and most
powerful sister of the ambrosia family, and the better grass, carpet!

Ambrosia Gaia: A difficult plant to keep alive, being very vulnerable to
weeds, pests, and any amount of toxins in the tray, as well as voracious
when it comes to nutrients and water. In exchange, the plant produces a
very, very powerful healing agent: Earthsblood.

For the cost of your brain, your ability to gauge how injured you are,
and when it works again, the ability to see clearly, your body will be
repaired in miraculous ways! (4/4 Brute Burn, 4 tox, 10 oxy, 2 clone).
The current damage is set to 1 brain damage, which means you'd need to
use a fair amount to die -- but not treating it will debilitate you.
Overdoses at over 15u.
In the future, it will also be a usable plant chem -- but let's not
worry about that until after I scream at the entirety of botany.

Carpet: Grass mutation, pull it free, get free carpet tile. OR! Mix with
the items in the image to create New! and Exciting! colors. Mix 2 parts
liquefied carpet, with 1 part plasticide, and you too can redecorate
like the best of them*

*some colors still have to be bought from cargo.
*someone help me make it a sprayable so we don't need solidification
please....

This also buffs a certain aspect of xenobotany -- plant cells.
For reasons only known to god.. and I think he left baycode a long time
ago, plant cells could only ever reach a maximum rating of 2000. As a
large cell. So you can't stuff it in a gun. This is dogshit --
especially for the challenge of reaching 200 potency on a plant, a feat
that is nearly impossible. The math has been buffed, so if you even
manage to get to 100, you at least have a Rating 20000 cell, something
you can run a department off of if straits are dire.

The final, and more QoL thing than straight buff or new thing: GPS
Drills
Drills now have a GPS signal. Never lose a pesky drill again!*
*you did remember your GPS device, yeah?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Give a xenobotanist something worth working to in normal gameplay, and
they'll endeavour to do so while waiting for the fun plants to come back
to station. Don't, and watch them just kinda wilt waist deep in glow
berries, gold apples, and ice chilis. Also, it's easier than you think
to lose a giant drill when you've stepped away from the planet for a
long while. only to come back later. Putting GPSes in them just means
you can continue the work again.

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
add: Two new plants, Ambrosia Gaia, and Carpet
add: New chems! Earthsblood, trading the mind for the body, and Carpet
and it's many mixtures, capable of being solidified later!
qol: Mining Drills now have an integral GPS. It took strength of a
million men to not make the tag DRILLD0 as a terrible joke.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: TheObserver-sys <Gizmomaster777@gmail.com>
Co-authored-by: Captain277 <agentraven16@gmail.com>

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[784efe9b51...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/784efe9b514256072f90ffbae9acebe38b2f5b4f)
#### Wednesday 2023-09-13 23:07:17 by CharlesWedge

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

