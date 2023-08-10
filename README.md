## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-09](docs/good-messages/2023/2023-08-09.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,218,689 were push events containing 3,375,904 commit messages that amount to 262,830,046 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 57 messages:


## [caitpj/Hays-SCFG-Hackathon-2023-Auric](https://github.com/caitpj/Hays-SCFG-Hackathon-2023-Auric)@[9208e8d561...](https://github.com/caitpj/Hays-SCFG-Hackathon-2023-Auric/commit/9208e8d56181f76d4a32393eabb3e7e2a187e03d)
#### Wednesday 2023-08-09 00:00:30 by Adam Good

Add files via upload

The number of unique Auric rituals that can be created from a set of eight essential oils depends on various factors, such as the number of oils used in each ritual, the order in which they are combined, and whether the repetition of oils within a ritual is allowed or not.  The eight essentials oils we are using are

Lavender
Bergamot
Peppermint
Frankincense
Ylang-Ylang
Clary Sage
Cedarwood
Sandalwood

The current methodology we would like to explore is creating rituals by combining three essential oils from the set of eight, and each essential oil can be used only once within a ritual, you can calculate the number of unique combinations using the formula for combinations:

nCr = n! / (r! * (n - r)!)

Where:

n = Total number of items (in this case, the number of essential oils)
r = Number of items to be selected (in this case, the number of oils in a ritual)
! = Factorial (product of all positive integers up to the number)
For your scenario, with 8 essential oils and selecting 3 for each ritual:

n = 8
r = 3

nCr = 8! / (3! * (8 - 3)!)
nCr = (8 * 7 * 6) / (3 * 2 * 1)
nCr = 56

So we have 56 unique rituals by combining three essential oils from the set of eight, assuming each oil is used only once within a ritual and the order of combination matters. 

This CVS file contains fields of ritual number, wellness category, mix name, essential oils used, the drops per oil, note and short description.

The Auric Wellness Signature is a holistic approach to well-being that combines the therapeutic properties of essential oils and the practice of rituals to enhance overall health and balance. This concept draws inspiration from the ancient understanding of the aura—a subtle energy field that surrounds and interpenetrates the physical body in various spiritual and metaphysical traditions.

In the context of the Auric Wellness Signature:

1. **Essential Oils**: Essential oils are concentrated extracts derived from plants that possess unique aromatic and therapeutic properties. Each essential oil has its own distinct aroma and can be associated with specific emotional, mental, and physical effects. For example, lavender oil is often linked to relaxation and calmness, while peppermint oil is known for invigoration and focus.

2. **Rituals**: Rituals are intentional and structured practices that involve various actions, often accompanied by mindfulness, intention-setting, and repetitive behavior. In the context of the Auric Wellness Signature, rituals refer to specific practices, activities, or routines that individuals engage in to promote well-being and balance. These rituals can include meditation, breathing exercises, journaling, movement practices, and more.

The Auric Wellness Signature combines these two elements in a personalized manner:

- **Personalization**: The approach takes into consideration individual factors such as biometric data (e.g., heart rate, sleep patterns) and wellness goals. Machine learning and AI algorithms analyze this data to recommend specific combinations of essential oils and rituals that align with the user's well-being needs at a particular moment.

- **Chakra and Wellness Categories**: The wellness recommendations are often structured around wellness categories, inspired by the chakras—an ancient system of energy centers within the body. These categories include Calm, Focus, Energy, and Sleep. Each category corresponds to specific aspects of well-being and emotional states.

- **Intentional Blend**: The recommended essential oil blends and rituals are crafted with the intention of supporting the user's desired well-being state. For example, if a user seeks to enhance focus and concentration, the Auric Wellness Signature might suggest a specific blend of essential oils and rituals associated with the "Focus" category.

Overall, the Auric Wellness Signature aims to offer a comprehensive approach to well-being that integrates the aromatic and therapeutic benefits of essential oils with the mindful and intentional practices of rituals. It provides users with personalized recommendations to help them achieve a sense of balance, harmony, and vitality in their daily lives.

---
## [bentoml/langchain](https://github.com/bentoml/langchain)@[75fb9d2fdc...](https://github.com/bentoml/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Wednesday 2023-08-09 00:18:50 by Stefano Lottini

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
## [LM95A1/Project-Epsilon-4](https://github.com/LM95A1/Project-Epsilon-4)@[a38e8eb04c...](https://github.com/LM95A1/Project-Epsilon-4/commit/a38e8eb04c3e040d254248a24bb0a765b9fbcb6c)
#### Wednesday 2023-08-09 00:21:24 by LM95A1

Acquired a Tuesday

Added templates directory to house index.html
Updated spiderweb.py since the original was f**ked
Updated script.js for additional features
Updated style.css to add a bunch of different options, many of which may remain unused
Added pokeball.png in images directory; I was sick of the f**king paw logo

Been experimenting with the structure of the dashboard and the features of the Pokedex to better fit what we're trying to do. Making progress at a very slow rate, given the time constraints and outside obligations piling up. Bad timing, yeah? Gonna have to go full throttle with this tonight and tomorrow.

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[1fe7b10e33...](https://github.com/lessthnthree/Skyrat-tg/commit/1fe7b10e339ea0d6a3d49f864e1badc5c831e791)
#### Wednesday 2023-08-09 00:22:05 by SkyratBot

[MIRROR] Removes TTS voice disable option (Skyrat: Actually makes a functional "None" voice option this time) [MDB IGNORE] (#22283)

* Removes TTS voice disable option (#76530)

## About The Pull Request
Removes the TTS voice disable option, which was already unavailable on
TG as it was set to off by default. The reason this was added was so
that downstreams could toggle the config on or off.

## Why It's Good For The Game
I think this option fundamentally undermines the TTS system because it
allows individual players to disable their voice globally, meaning that
players who have TTS enabled will not be able to hear them.

This worsens the experience for players who have TTS enabled and it's
not something I want to include as an option. If players don't like
their voice, they can turn TTS off for themselves so that they don't
hear the voices. If players don't want to customize their voice, they
can quickly choose a random voice, and we can take directions in the
future to make voice randomization consistent with gender so that a male
does not get randomly assigned a female voice and vice versa.

This option is already unavailable on TG servers because it was
primarily added for downstreams, but I don't think giving downstreams
the option to undermine the TTS system is the right direction to take.
Downstreams are still completely free to code this option on their own
codebase.

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>

* Removes TTS voice disable option

* Returns the option to not have a voice to TTS, properly this time

---------

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [google/osv-scanner](https://github.com/google/osv-scanner)@[53107dd285...](https://github.com/google/osv-scanner/commit/53107dd2851eb10df2c8c5044c0319ae54a953d4)
#### Wednesday 2023-08-09 00:55:59 by Gareth Jones

feat: add experimental offline mode (#183)

Resolves #81

~This is based off a lot of the core of the detector - it's not working
yet because I need to figure how to handle passing in the queries to the
local db given that the detector takes `PackageDetails`, but really the
key thing there is how to handle PURL which comes from SBOMs that I
don't really know how to use 😅 (idk if I'm just dumb or what, but for
some reason I've still not been able to figure how to accurately
generate one from a `Gemfile.lock`, `package-lock.json`, etc)~

~If someone could provide some sample SBOMs that would be very useful
(I'll also do a PR adding tests using them as fixtures), and also happy
to receive feedback on the general approach - there are some smaller
bits to discuss, like if fields should be omitted from the JSON output
vs an empty array, and the `Describe` related stuff too.~

This is now working, though personally it feels pretty awkward codewise
- I know I'm bias but I feel like it would be better to trying to bring
across the whole `database` package from the detector, as the API db is
pretty much the same and then you'd have support for zips, directories,
and the API with extra configs like working directories + an extensive
test suite for all three (I don't think it would be as painful as one
might first think, even with `osvscanner` having just been made public
because that's relatively small).

Still, this does work as advertised - there's definitely a few things
that could do with some cleaning up (including if fields should be
omitted from the JSON output vs an empty array, and the `Describe`
related stuff too) but am leaving them for now until I hear what folks
think of the general implementation + my above comment.

I've also gone with two boolean flags rather than the url-based flag
@oliverchang suggested because I didn't feel comfortable trying to
shoehorn that into this PR as well, and now that we're using
`--experimental` it should be fine to completely change these flags in
future.

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[6c4e6014bb...](https://github.com/vampirebat74/lobotomy-corp13/commit/6c4e6014bb77ff71982cb155bb0946ade392d30d)
#### Wednesday 2023-08-09 01:26:50 by Mr.Heavenly

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

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[cc5c19f41f...](https://github.com/git-for-windows/git/commit/cc5c19f41f693d4857f16fbe40b19490ef53b33a)
#### Wednesday 2023-08-09 01:36:43 by Johannes Schindelin

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
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[f0dc574c37...](https://github.com/necromanceranne/tgstation/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Wednesday 2023-08-09 01:36:46 by carlarctg

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
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[52c8da7ea4...](https://github.com/carshalash/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Wednesday 2023-08-09 02:16:34 by Jacquerel

PAI Holochassis are now leashed to an area around their card (#76763)

## About The Pull Request

This change restricts PAI holograms to an area around their assigned PAI
card. If you leave this area, you are teleported back to the card's
location (but not automatically put back into the card).

https://www.youtube.com/watch?v=L2ThEVa4nx8

This setting can be configured from the PAI menu, it's set pretty short
in the video because otherwise it wouldn't teleport when I threw the
card and I like doing that.

![image](https://github.com/tgstation/tgstation/assets/7483112/faf0fa0b-e9d6-4990-8d8c-f30def2892f1)

To accomodate this I set up a component to deal with a reasonably common
problem I have had, "what if I want to track the movement of something
in a box in a bag in someone's inventory". Please tell me if the
solution I came up with is stupid and we already have a better one that
I forgot about.

Also now you can put pAIs inside bots again, by popular request.

## Why It's Good For The Game

Personal AIs are intended to be personal assistants to their owner.
rather than fully independent entities which can pick up their own card
and leave as soon as they spawn.
As "aimless wanderer" players can now possess station bots, pAIs can be
limited to an area around the bearer of their card.

Because the holoform now doesn't contain the card, this also means that
a PAI cannot run off and then be impossible to retrieve. You are always
in control of where it can go.

Also it's funny to throw the card and watch the chicken get teleported
to it.

## Changelog

:cl:
add: Personal AI holograms are now limited to an area around their PAI
card. The size of this are can be configured via the PAI card.
add: pAI cards can now be placed inside bots in order to grant them
control of the bot.
/:cl:

---
## [Ltmayday/tgstation](https://github.com/Ltmayday/tgstation)@[41f20bc3ce...](https://github.com/Ltmayday/tgstation/commit/41f20bc3ced4e7853a09f2d5e1dcf46346f2e51f)
#### Wednesday 2023-08-09 02:38:21 by LemonInTheDark

[MDB IGNORE] Angled Lights & Lighting Prototyping Tool  (#74365)

## About The Pull Request

Hello friends, I've been on a bit of a lighting kick recently, and I
decided I clearly do not have enough things to work on as it is.
This pr adds angle support to static lights, and a concepting/debug tool
for playing with lights on a map.

Let's start from first principles yeah?

### Why Angled Lights?

Mappers, since they can't actually see a light's effect in editor, tend
to go off gut.
That gut is based more off what "makes sense" then how things actually
work
This means they'll overplace light sources, and also they tend to treat
lights, particularly light "bars" (the bigger ones) as directional.
So you'll have two lights on either sides of a pillar, lights inside a
room with lights outside pointing out, etc.


![image](https://user-images.githubusercontent.com/58055496/228785032-63b86120-ea4c-4e52-b4e8-40a4b61e5bbc.png)

This has annoying side effects. A lot of our map is overlit, to the
point that knocking out a light does.... pretty much nothing.
I find this sad, and would like to work to prevent it. I think dark and
dim, while it does not suit the normal game, is amazing for vibes, and I
want it to be easier to see that.

Angled lights bring how lights work more in line with how mappers expect
lights work, and avoids bleedover into rooms that shouldn't be bled
into, working towards that goal of mine.

### How Angled Lights?

This is more complex then you'd first think so we'll go step by step


![image](https://user-images.githubusercontent.com/58055496/228786117-d937b408-9bc2-4066-9aee-aae21b047151.png)

Oh before we start, some catchup from the last time I touched lighting
code.
Instead of doing a lighting falloff calculation for each lighting corner
(a block that represents the resolution of our lights) in view we
instead generate cached lightsheets. These precalculate and store all
possible falloffs for x and y distances from a source.

This is very useful for angle work, since it makes it almost totally
free.
 
Atoms get 2 new values. light_angle and light_dir
Light angle is the angle the light uses, and light_dir is a cardinal
direction it displays in

We take these values, and inside sheetbuilding do some optional angle
work. getting the center angle, the angle of a pair of coords, and then
the delta between them.
This is then multiplied against the standard falloff formula, and job
done.

We do need some extra fenangling to make this all work nicely tho.

We currently use a pixel turf var stored on the light source to do
distance calculations.
This is the turf we pretend the light source is on for visuals, most
often used to make wall lights work nice.
The trouble is it's not very granular, and doesn't always have the
effect you might want.

So, instead of generating and storing a pixel turf to do our distance
calculations against, we store x and y offset variables.
We use them to expand our working range and sheet size to ensure things
visually make sense, and then offset any positions by them.

I've added a way for sources to have opinions on their offsets too, and
am using them for wall lights.
This ensures the angle calculations don't make the wall behind a light
fulldark, which would be silly.

### Debug Tool?

In the interest of helping with that core problem, lights being complex
to display, I've added a prototyping tool to the game.
It's locked behind mapping verbs, and works about like this.

Once the verb is activated, it iterates over all the sources in the
world (except turfs because those are kinda silly), outlining and
"freezing" them, preventing any future changes.
Then, it adds 3 buttons to the owners of a light source.

![image](https://user-images.githubusercontent.com/58055496/228776539-4b1d82af-1244-4ed6-8754-7f07e3e47cda.png)
The first button toggles the light on and off, as desired.
The third allows you to move the source around, with a little targeting
icon replacing your mouse
The second tho, that's more interesting.

The second button opens a debug menu for that light

![image](https://user-images.githubusercontent.com/58055496/228777811-ae620588-f08a-4b50-93a0-beea593aea77.png)
There's a lot here, let's go through it.

Bit on the left is a list of templates, which allow you to sample
existing light types (No I have no idea why the background is fullwhite,
need to work on that pre merge)
You can choose one by clicking it, and hitting the upload button.

This replaces your existing lighting values with the template's,
alongside replacing its icon and icon state so it looks right.
There are three types as of now, mostly for categorization. Bar, which
are the larger typically stronger lights, Bulb, which are well, bulbs,
and Misc which could be expanded, but currently just contains floor
lights.

Alongside that you can manually edit the power, range, color and angle
of the focused light.
I also have support for changing the direction of the light source,
since anything that uses directional lighting would also tie light dir
to it.
This isn't *always* done tho, so I should maybe find a way to edit light
dir too.

My hope is this tool will allow for better concepting of a room's
lights, and easier changing of individual object's light values to suit
the right visuals.

### Lemon No Why What

Ok so I applied angle lights to bars and bulbs, which means I am
changing the lighting of pretty much every map in the codebase.
I'm gonna uh, go check my work.

Alongside this I intend to give lighting some depth. So if there's room
to make a space warmer, or highlight light colors from other sources, I
will do that.

(Images as examples)

![image](https://user-images.githubusercontent.com/58055496/228786801-111b6493-c040-4199-ab99-ac1c914d034c.png)

I also want to work on that other goal of mine, making breaking lights
matter. So I'll be doing what I can to ensure you only need to break one
light to make a meaningful change in the scene.

This is semi complicated by one light source not ever actually reaching
fullbright on its own, but we do what we must because we can.


![image](https://user-images.githubusercontent.com/58055496/228786483-b7ad6ecd-874f-4d90-b5ca-6ef78cb70d2b.png)

I'm as I hope you know biased towards darker spaces, I think contrast
has vibes.
In particular I do not think strong lights really suit maintenance. 

Most of what is used there are bulbs, so I'm planning on replacing most
uses with low power bulbs, to keep light impacts to rooms, alongside
reducing the amount of lights placed in the main tunnels


![image](https://user-images.githubusercontent.com/58055496/228786594-c6d7610c-611e-478b-bcba-173ebf4c4b12.png)

**If you take issue with this methodology please do so NOW**, I don't
want to have to do another pass over things.
Oh also I'm saving station maps for last since ruins are less likely to
get touched in mapping march and all.

### Misc + Finishing Thoughts

Light templates support mirroring vars off typepaths using a subtype,
which means all the templates added here do not require updating if the
source type changes somehow. I'd like to expand the template list at
some point, perhaps in future.

I've opened this as a draft to make my intentions to make my changes to
lights known, and to serve as motivation for all the map changes I need
to do.

### Farish Future

I'm unhappy with how we currently configure lights. I would like a
system that more directly matches the idea of drawing falloff curves,
along with allowing for different falloffs for different colors,
alongside extending the idea to angle falloff.
This would make out of engine lighting easier, allow for nicer looking
lights (red to pink, blue to purple, etc), and improve accessibility by
artists.

This is slightly far off, because I have other obligations and it's
kinda complicated, but I'd like to mention it cause it's one of my many
pipedreams.

## Changelog
:cl:
add: Added angle lighting, applies it to most wall lights!
add: Adds a lighting prototyping tool, mappers go try it out (it's
locked behind the mapping verb)
/:cl:

---------

Co-authored-by: MMMiracles <lolaccount1@hotmail.com>

---
## [SonicHDC/space-station-14](https://github.com/SonicHDC/space-station-14)@[06747e0f7e...](https://github.com/SonicHDC/space-station-14/commit/06747e0f7e7d04cf87e63a359a3a86b1a35442cc)
#### Wednesday 2023-08-09 02:51:27 by Emisse

some silly paintings and posters (#17872)

* webedit

* Update meta.json

* god is real hes here with us

* so true

* so truers rise

* worst meta.json ive seen in my life

* so true

---
## [Superlagg/coyote-bayou](https://github.com/Superlagg/coyote-bayou)@[255ef2c778...](https://github.com/Superlagg/coyote-bayou/commit/255ef2c77853b41581d072fe7aafad3e700b30a6)
#### Wednesday 2023-08-09 02:57:27 by Tk420634

Merge pull request #2737 from Superlagg/you-know-what-fuck-you-(bitflags-your-item-slots)

fixes ID timer and mistyped box slot

---
## [alexisandrade07/Twine-Stories](https://github.com/alexisandrade07/Twine-Stories)@[ce57f3fa62...](https://github.com/alexisandrade07/Twine-Stories/commit/ce57f3fa62711c62e33b55b16bb665cbdbdf19fc)
#### Wednesday 2023-08-09 03:28:43 by alexisandrade07

Read Me!

Step into a digital realm where ancient tales blend seamlessly with modern technology in "Raven's Luminal Journey." This immersive Twine remediation draws you into the heart of indigenous cosmology, weaving the captivating narrative of "The Raven Steals the Light" with the interactive power of digital storytelling.

Journey alongside Raven, a transformative and mischievous figure from indigenous folklore, as he embarks on a daring quest to liberate the celestial light from its captor. Through the innovative medium of Twine, the ancient narrative comes alive with an interactive twist, allowing you to navigate Raven's path, make choices, and engage with the story's pivotal moments.

As you traverse the digital pathways of Raven's Luminal Journey, you'll encounter stunning visuals, evocative soundscapes, and thought-provoking choices that shape the course of the tale. Engage with the indigenous cosmology at your own pace, allowing the story to unfold in a manner that resonates with your curiosity and sense of exploration.

"Raven's Luminal Journey" is more than a digital retelling; it's an invitation to connect with a rich cultural heritage, to experience the symbiotic relationship between tradition and technology. Whether you are well-versed in indigenous cosmology or encountering it for the first time, this remediation offers a unique and immersive perspective that bridges the ancient and the contemporary.

Through the fusion of storytelling and interactive exploration, "Raven's Luminal Journey" honours the depth and significance of indigenous cosmology while embracing the digital medium's potential to breathe new life into age-old narratives. Immerse yourself in a world where Raven's cunning, courage, and wisdom guide your way, and where the boundaries between myth and digital innovation blur, inviting you to experience the transformative power of storytelling in a new and captivating light.

---
## [dangowrt/linux](https://github.com/dangowrt/linux)@[08c6b43df2...](https://github.com/dangowrt/linux/commit/08c6b43df24961c6aa80a1ffc7a8653a4905329d)
#### Wednesday 2023-08-09 03:39:32 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Merek2/coyote-bayou](https://github.com/Merek2/coyote-bayou)@[f26fec823d...](https://github.com/Merek2/coyote-bayou/commit/f26fec823d7d769507a58776ceb2ecf9622f3de4)
#### Wednesday 2023-08-09 04:15:33 by Tk420634

Unleashing the void

If I want to play as the literal Void from Hallow Knight I fucking will, fuck you Poojawa.

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[f3fc60ed65...](https://github.com/realforest2001/forest-cm13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Wednesday 2023-08-09 04:43:33 by morrowwolf

Attachment nerfs and removals (#4122)

# About the pull request

This PR:

Removes the barrel charger from vendors

Removes all benefits other than wield delay mod from the angled grip

Adds wield delay to the extended barrel

# Explain why it's good for the game

Barrel charger is a straight damage increase and rather silly to work
around given how burst works bypassing real fire rate concerns. If you
know, you know. Horrible idea, I am amazed it's been around this long.

Angled grip had zero downside. Now it still has zero downside but isn't
also a ton of accuracy buffs on top of the god-tier lower wield delay.

Extended barrel had zero downside. Now it has a downside.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removed the barrel charger from vendors
balance: Removed all benefits other than wield delay mod from the angled
grip
balance: Added wield delay to extended barrel
/:cl:

---
## [A-Noid33/mame](https://github.com/A-Noid33/mame)@[51743748ed...](https://github.com/A-Noid33/mame/commit/51743748ed897faf3d85a312be7877a4d723c6b8)
#### Wednesday 2023-08-09 04:55:31 by Bob Schultz

mac_flop_orig:
* Minor corrections to a few software list entries.

New working software list items (109 Dumps Added)
-------------------------------
mac_flop_clcracked: [4AM, san inc, A-Noid]

Alter Ego (male version 1.0) (san inc crack)
Alter Ego (version 1.1 female) (san inc crack)
Alternate Reality: The City (version 3.0) (san inc crack)
Animation Toolkit I: The Players (version 1.0) (4am crack)
Balance of Power (version 1.03) (san inc crack)
Borrowed Time (san inc crack)
Championship Star League Baseball (san inc crack)
Cutthroats (release 23 / 840809-C) (4am crack)
CX Base 500 (French, version 1.1) (san inc crack)
Deadline (release 27 / 831005-C) (4am crack)
Defender of the Crown (san inc crack)
Deluxe Music Construction Set (version 1.0) (san inc crack)
Déjà Vu (version 2.3) (4am crack)
Déjà Vu: A Nightmare Comes True!! (san inc crack)
Déjà Vu II: Lost in Las Vegas!! (san inc crack)
Dollars and Sense (version 1.3) (4am crack)
Downhill Racer (san inc crack)
Dragonworld (4am crack)
ExperLisp (version 1.0) (4am crack)
Forbidden Castle (san inc crack)
Fusillade (version 1.0) (san inc crack)
Geometry (version 1.1) (4am crack)
Habadex (version 1.1) (4am crack)
Hacker II (san inc crack)
Harrier Strike Mission (san inc crack)
Indiana Jones and the Revenge of the Ancients (san inc crack)
Infidel (release 22 / 840522-C) (4am crack)
Jam Session (version 1.0) (4am crack)
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack)
Lode Runner (version 1.0) (4am crack)
Mac Pro Football (version 1.0) (san inc crack)
MacBackup (version 2.6) (4am crack)
MacCheckers and Reversi (4am crack)
MacCopy (version 1.1) (4am crack)
MacGammon! (version 1.0) (4am crack)
MacGolf (version 2.0) (4am crack)
MacWars (san inc crack)
Master Tracks Pro (version 1.10) (san inc crack)
Master Tracks Pro (version 2.00h) (san inc crack)
Master Tracks Pro (version 3.4a) (san inc crack)
Master Tracks Pro (version 4.0) (san inc crack)
Math Blaster (version 1.0) (4am crack)
Maze Survival (san inc crack)
Microsoft Excel (version 1.00) (san inc crack)
Microsoft File (version 1.04) (san inc crack)
Mindshadow (san inc crack)
Moriarty's Revenge (version 1.0) (san inc crack)
Moriarty's Revenge (version 1.03) (4am crack)
Mouse Stampede (version 1.00) (4am crack)
Murder by the Dozen (Thunder Mountain) (4am crack)
My Office (version 2.7) (4am crack)
One on One (san inc crack)
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack)
Patton Strikes Back (version 1.00) (san inc crack)
Patton vs. Rommel (version 1.05) (san inc crack)
Pensate (version 1.1) (4am crack)
PFS File and Report (version A.00) (4am crack)
Physics (version 1.0) (4am crack)
Physics (version 1.2) (4am crack)
Pinball Construction Set (version 2.5) (san inc crack)
Pipe Dream (version 1.2) (4am crack)
Professional Composer (version 2.3Mfx) (san inc crack)
Q-Sheet (version 1.0) (san inc crack)
Rambo: First Blood Part II (san inc crack)
Reader Rabbit (version 2.0) (4am crack)
Rogue (version 1.0) (san inc crack)
Seastalker (release 15 / 840522-C) (4am crack)
Seven Cities of Gold (san inc crack)
Shadowgate (san inc crack)
Shanghai (version 1.0) (san inc crack)
Shufflepuck Cafe (version 1.0) (4am crack)
Sierra Championship Boxing (4am crack)
SimCity (version 1.1) (4am crack)
SimCity (version 1.2, black & white) (4am crack)
SimEarth (version 1.0) (4am crack)
Skyfox (san inc crack)
Smash Hit Racquetball (version 1.01) (san inc crack)
SmoothTalker (version 1.0) (4am crack)
Speed Reader II (version 1.1) (4am crack)
Speller Bee (version 1.1) (4am crack)
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack)
Stratego (version 1.0) (4am crack)
Suspect (release 14 / 841005-C) (4am crack)
Tass Times in Tonetown (san inc crack)
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack)
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack)
The Chessmaster 2000 (version 1.02) (4am crack)
The Crimson Crown (san inc crack)
The Duel: Test Drive II (san inc crack)
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack)
The King of Chicago (san inc crack)
The Lüscher Profile (san inc crack)
The Mind Prober (version 1.0) (san inc crack)
The Mist (san inc crack)
The Quest (4am crack)
The Slide Show Magician (version 1.2) (4am crack)
The Surgeon (version 1.5) (san inc crack)
The Toy Shop (version 1.1) (san inc crack)
The Witness (release 22 / 840924-C) (4am crack)
ThinkTank 128 (version 1.000) (4am crack)
Uninvited (version 1.0) (san inc crack)
Uninvited (version 2.1D1) (san inc crack)
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack)
Winter Games (version 1985-10-24) (san inc crack)
Winter Games (version 1985-10-31) (san inc crack)
Wishbringer (release 68 / 850501-D) (4am crack)
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack)
Zork II (release 48 / 840904-C) (4am crack)
Zork III (release 17 / 840727-C) (4am crack)

---
## [A-Noid33/mame](https://github.com/A-Noid33/mame)@[2bdde3e05c...](https://github.com/A-Noid33/mame/commit/2bdde3e05c73b25593defb29d5ee021d139428ef)
#### Wednesday 2023-08-09 04:55:31 by Bob Schultz

Added mac moof software list support

New working software list items (123 working dumps)
-------------------------------
mac_flop_orig:

Lode Runner (version 1.0) [4AM, Anoid]
Balance of Power (version 1.03) [4AM, Anoid]
Shanghai (version 1.0) [4AM, Anoid]
Skyfox [4AM, Anoid]
Temple of Apshai Trilogy [4AM, Anoid]
The Surgeon (version 1.5) [4AM, Anoid]
Uninvited [4AM, Anoid]
King's Quest (version 1.10) [4AM, Anoid]
Smash Hit Racquetball (version 1.01) [4AM, Anoid]
The Ancient Art of War [4AM, Anoid]
Hacker II [4AM, Anoid]
Rambo: First Blood Part II [4AM, Anoid]
One on One [4AM, Anoid]
Indiana Jones and the Revenge of the Ancients [4AM, Anoid]
Winter Games (version 1985-10-24) [4AM, Anoid]
Winter Games (version 1985-10-31) [4AM, Anoid]
Star Trek: The Kobayashi Alternative (version 1.0) [4AM, Anoid]
Mac Attack [4AM, Anoid]
GATO (version 1.3) [4AM, Anoid]
Dark Castle (version 1.0) [4AM, Anoid]
Oids (version 1.4) [4AM, Anoid]
MacWars [4AM, Anoid]
Shadowgate [4AM, Anoid]
Seven Cities of Gold [4AM, Anoid]
Enchanted Scepters [4AM, Anoid]
Beyond Dark Castle [4AM, Anoid]
Arkanoid (version 1.00) [4AM, Anoid]
The Chessmaster 2000 (version 1.02) [4AM, Anoid]
Maze Survival [4AM, Anoid]
Frogger (version 1.0) [4AM, Anoid]
SimCity (version 1.2, black & white) [4AM, Anoid]
Falcon (version 1.0) [4AM, Anoid]
Cutthroats (release 23 / 840809-C) [4AM, Anoid]
The Witness (release 22 / 840924-C) [4AM, Anoid]
Seastalker (release 15 / 840522-C) [4AM, Anoid]
Zork III (release 17 / 840727-C) [4AM, Anoid]
A Mind Forever Voyaging (release 77 / 850814-E) [4AM, Anoid]
Hollywood Hijinx (release 37 / 861215-I) [4AM, Anoid]
Nord and Bert Couldn't Make Head or Tail of It (release 19 / 870722-I) [4AM, Anoid]
Border Zone (release 9 / 881008-3B) [4AM, Anoid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914) [4AM, Anoid]
Zork I: The Great Underground Empire (release 76 / 840509) [4AM, Anoid]
Deadline (release 27 / 831005-C) [4AM, Anoid]
Infidel (release 22 / 840522-C) [4AM, Anoid]
Suspect (release 14 / 841005-C) [4AM, Anoid]
Planetfall (release 29 / 840118-B) [4AM, Anoid]
Ballyhoo (release 97 / 851218-G) [4AM, Anoid]
Enchanter (release 24 / 851118-G) [4AM, Anoid]
Spellbreaker (release 63 / 850916-F) [4AM, Anoid]
Trinity (release 11 / 860509-3H) [4AM, Anoid]
Stationfall (release 107 / 870430-G) [4AM, Anoid]
The Lurking Horror (release 203 / 870506-G) [4AM, Anoid]
Alter Ego (male version 1.0) [4AM, Anoid]
Alter Ego (version 1.1 female) [4AM, Anoid]
The Print Shop (version 1.2) [4AM, Anoid]
Flight Simulator (version 1.02) [4AM, Anoid]
Run for the Money [4AM, Anoid]
Master Tracks Pro (version 4.0) [4AM, Anoid]
Where in Time is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Deluxe Music Construction Set (version 1.0) [4AM, Anoid]
Apache Strike (version 1.2) [4AM, Anoid]
Wizardry VI: Bane of the Cosmic Forge [4AM, Anoid]
Harrier Strike Mission [4AM, Anoid]
Airborne! [4AM, Anoid]
Mac Vegas (version 1.1) [4AM, Anoid]
Dragonworld [4AM, Anoid]
MacDraft (version 1.2) [4AM, Anoid]
The Mind Prober (version 1.0) [4AM, Anoid]
The Toy Shop (version 1.1) [4AM, Anoid]
Strategic Conquest (version 1.2) [4AM, Anoid]
The Home Accountant (version 1.01) [4AM, Anoid]
Sub Battle Simulator [4AM, Anoid]
Vegas Video Poker [4AM, Anoid]
The Pawn (version 2.3) [4AM, Anoid]
Downhill Racer [4AM, Anoid]
Dollars and Sense (version 1.3) [4AM, Anoid]
Alternate Reality: The City (version 3.0) [4AM, Anoid]
Borrowed Time [4AM, Anoid]
The Quest [4AM, Anoid]
The Crimson Crown [4AM, Anoid]
Mindshadow [4AM, Anoid]
Pensate (version 1.1) [4AM, Anoid]
Sierra Championship Boxing [4AM, Anoid]
Championship Star League Baseball [4AM, Anoid]
Forbidden Castle [4AM, Anoid]
Defender of the Crown [4AM, Anoid]
The King of Chicago [4AM, Anoid]
Macintosh Pascal (version 1.0) [4AM, Anoid]
Fusillade [4AM, Anoid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) [4AM, Anoid]
Speed Reader II (version 1.1) [4AM, Anoid]
][ in a Mac (version 2.03) [4AM, Anoid]
Q-Sheet (version 1.0) [4AM, Anoid]
Fontographer (version 2.4.1) [4AM, Anoid]
Mouse Stampede (version 1.00) [4AM, Anoid]
The Mist [4AM, Anoid]
Tass Times in Tonetown [4AM, Anoid]
Pinball Construction Set [4AM, Anoid]
Transylvania [4AM, Anoid]
Déjà Vu: A Nightmare Comes True!! [4AM, Anoid]
Déjà Vu II: Lost in Las Vegas!! [4AM, Anoid]
Rogue (version 1.0) [4AM, Anoid]
Bridge (version 6.0) [4AM, Anoid]
Harrier Strike Mission II (version 1.2) [4AM, Anoid]
Patton vs. Rommel (version 1.05) [4AM, Anoid]
Moebius: The Orb of Celestial Harmony (version 1.03) [4AM, Anoid]
Tesserae (version 1.06) [4AM, Anoid]
Where in Europe is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Shufflepuck Cafe (version 1.0) [4AM, Anoid]
Geometry (version 1.1) [4AM, Anoid]
Physics (version 1.2) [4AM, Anoid]
SimCity (version 1.1) [4AM, Anoid]
Murder by the Dozen [4AM, Anoid]
The Duel: Test Drive II [4AM, Anoid]
Master Tracks Pro (version 1.10) [4AM, Anoid]
Master Tracks Pro (version 2.00h) [4AM, Anoid]
Master Tracks Pro (version 3.4a) [4AM, Anoid]
Squire (version 1.1) [4AM, Anoid]
Millionaire (version 1.0) [4AM, Anoid]
Microsoft File (version 1.04) [4AM, Anoid]
Microsoft Excel (version 1.00) [4AM, Anoid]
The Fool's Errand (version 2.0) [4AM, Anoid]
MacGammon! (version 1.0) [4AM, Anoid]

---
## [TeshariEnjoer/FluffySTG](https://github.com/TeshariEnjoer/FluffySTG)@[de855cbd7b...](https://github.com/TeshariEnjoer/FluffySTG/commit/de855cbd7ba68b36713c0d9ba3f93de1d9d237ee)
#### Wednesday 2023-08-09 06:05:52 by SkyratBot

Science Resprite! (With Sovl!) [MDB IGNORE] (#22861)

* Science Resprite! (With Sovl!) (#77314)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
What a crusty department. These outfits are...
Something.

![image](https://github.com/tgstation/tgstation/assets/76465278/63fe13cf-bcbf-42c2-a22c-c868ae49a72c)

How old are these now? I'm pretty sure they're unchanged since when I
started playing years ago on other servers.... besides the RD Turtleneck
and Roboticist suit of course. But they still did have some touch-ups to
be made...

Regardless, I think this department deserves a little love!
I've tried to stay true as I could to their current designs; this isn't
a re-**_design_**, just a re-sprite. I used the base jumpsuit design
from Medbay for most of these since it's the most modern suit that fit
with the colored-spots style.

![image](https://github.com/tgstation/tgstation/assets/76465278/ef7ff5b0-f0e3-481a-9ed4-ba830e3ee0c3)

All of them have been touched up, and the RD's "alt" is now a subtype of
the buttondown so it can easily inherit any sprite updates in the
future.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
These deserved some touch-ups and modernization, and while I'm not keen
on entirely reworking them I figured I could at the least give them the
update the Science Team deserves.

(The buttondown has an outdated obj sprite in this image! It's since
been made smaller and more folded)
Also labcoats for comparison

![dreamseeker_Ds8gZLKoGE](https://github.com/tgstation/tgstation/assets/76465278/4da60512-b813-4260-b3fe-5c71b60cec81)

![dreamseeker_C9DpFWWOS7](https://github.com/tgstation/tgstation/assets/76465278/1de55f4c-2eaa-480b-811f-aaa5832eeceb)

![dreamseeker_02d3d7b6aj](https://github.com/tgstation/tgstation/assets/76465278/b1f40d03-c9b8-4f6b-bc54-516b11a7bfb3)

![dreamseeker_DwJGDwbUf1](https://github.com/tgstation/tgstation/assets/76465278/20f97a5e-42ab-4fe0-8eae-4ac6ed24ead4)

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
image: resprited the entirety of RnD! Genetics, Robotics, the RD, and
the Science Team themselves will enjoy the fresh new looks but same
great taste! No, wait, great STYLE! Don't eat these, they're covered in
chemicals.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* Science Resprite! (With Sovl!)

* Update vending.dm

---------

Co-authored-by: OrionTheFox <76465278+OrionTheFox@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [okwasniewski/react-native](https://github.com/okwasniewski/react-native)@[ee38c4a40c...](https://github.com/okwasniewski/react-native/commit/ee38c4a40c9d301c30fad4d127e8d020a6100b8e)
#### Wednesday 2023-08-09 07:27:24 by Phillip Pan

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
## [mizdrake7/Graveyard_r5x](https://github.com/mizdrake7/Graveyard_r5x)@[d0e326fb8f...](https://github.com/mizdrake7/Graveyard_r5x/commit/d0e326fb8ff9cdd9300297862e92f55c0c844ee4)
#### Wednesday 2023-08-09 07:58:58 by Maciej Żenczykowski

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

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[6c34d93be7...](https://github.com/Sealed101/tgstation/commit/6c34d93be715012943626d0f812e99f730a536ef)
#### Wednesday 2023-08-09 08:00:02 by necromanceranne

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
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[95ec0e6545...](https://github.com/Sealed101/tgstation/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Wednesday 2023-08-09 08:00:02 by necromanceranne

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
## [WordlessMeteor/LoL-DIY-Programs](https://github.com/WordlessMeteor/LoL-DIY-Programs)@[b183364c16...](https://github.com/WordlessMeteor/LoL-DIY-Programs/commit/b183364c164326d3146141b66b55121d7aa0ce11)
#### Wednesday 2023-08-09 09:57:32 by WordlessMeteor

更新了自定义脚本5和10【Updated Customized Programs 5 and 10】

一、程序更新综述（Program Update Summary）
请为此次更新跳过一个小版本号！因为更新的内容有点多，大致可以分为查对局脚本和查战绩脚本的更新。
Skip a smaller version for this update! There're a great many updates, roughly divided into the update of two programs: one is to search for summoner, and the other is to search for matches.
1. 在品质上，主要围绕查对局脚本的信息输出方式和日志保存位置进行了更新。对于信息输出方式的变更，本程序将大部分输出消息用message变量存储，然后同时输出到屏幕和文件；对于文件的保存位置，本程序沿用了查战绩脚本的文件保存方法。具体来说，主要是沿用了三个服务器变量和调用了与服务器语言环境和大区相关的API。
In terms of quality change, mainly updated the method of message output and the saving directory of the log file. After the change of the method of message output, this program uses the message `variable` to store a great part of output information and then output to both the screen and the file. As for the saving directory, this program inherits the idea from Customized Program 5. In details, this program inherits 3 variables about servers and calls the API regarding locale and the server.
2. 在功能上，修复了查战绩脚本在获取属于未收录在DataDragon数据库的版本的对局的信息时产生的报错信息。该报错信息只会在测试服和国服体验服上出现。有关此报错的来源，请在DataDragon数据库收录的版本号中找到与测试服上对局序号为4438805015的游戏版本对应的版本。
In terms of functional change, fixxed an error that arises when Customized Program 5 is trying to get the information of a match whose gameVersion doesn't correspond to any patch archived in DataDragon database. For the source of this error, please try to find a patch which is archived in DataDragon Patch list and corresponds to the gameVersion of the match with matchID 4438805015.
3. 受叮当猫的启发，现将所有“美服体验服”一律改为“测试服”。
Inspired by Gr4pe, all "美服体验服"s are now replaced by "测试服"s.
二、实现细节（Implementation Details）
（一）查对局脚本的改动（Changes in Customized Program 5）
1. 定义了message_save函数以修改大部分信息的输出方式。现在，涉及到参数设置、异常信息、异常处理。找到对局和结果的信息提示会同时输出在屏幕上和保存到日志文件中。此外，为每个输出到文件的消息添加了消息类型和时间戳（因此引入了time库）。
Defined a new function `message_save` to change the output strategy of a large part of the messages. Now, the information regarding parameter configuration, exception, exception handling, a match found and the result will be output to both the screen and the log file. In addition, added a type and a timestamp (the reason for the importion of `time` library) for each piece of output information.
2. 从查战绩脚本中引入了三个服务器变量platform_TENCENT、platform_RIOT和platform_GARENA，并定义了platform_format草稿函数以将每个键对应的值修改成字典的形式，便于区分服务器的中英文。该草稿函数只作为代码的修改工具，在程序中没有被调用。
Inherited 3 variables `platform_TENCENT`, `platform_RIOT` and `platform_GARENA` from Customized Program 5 and defined a draft function `platform_format` to transform the value of each key into the dictinoary form, which makes it convenient to distinguish Chinese and English expression of servers. This draft function only serves as a code editor and is thus never called in this program.
3. 为区别每次输出的信息是不是在一次查询下完成的，引入了全局变量opened。在新建一次查询时，opened置为假。当opened为假时，第一句输出信息的行首会多出一个换行符。
To distinguish whether the output messages belong to a same query, a global variable opened is created. Once a new query is made, `opened` is set False. and When `opened` equals False, the first output message is prefixxed with an extra line feed character.
4. 调整了日志文件保存的位置。现在，每个玩家的日志文件将遵循查战绩脚本的文件保存策略，而不是保存到主目录下。
Adjusted the saving directory of the log files. Now, each summoner's log file will follow the saving strategy of Customized Program 5, instead of being saved under the home directory.
5. 更换了对局序号输入提示的示范序号。（自定义脚本10第122、126、260和264行。）
Changed the example in the input hint of matchIDs. (Lines 122, 126, 260 and 264 in Customized Program 10.)
6. 弱化了离线查询召唤师对局的函数中选择服务器时的输入限制。现在不区分大小写了。（自定义脚本10第221行。）
Weakened the limits on the input when selecting a server in `search_summoner_offline` function. Now the case of input isn't considered anymore. (Line 221 in Customized Program 10.)
7. 在标点符号的级别上对部分注释进行了微调。（自定义脚本10第212和222行）
Modified some annotations within the level of punctuation marks. (Lines 85, 89, 175 and 185.)
8. 完善了离线查询的程序进程控制。现在，在输入【玩家通用唯一识别码】时输入“0”可以返回大区选择界面，再输入“0”即可退出程序。这是通过添加server_selection逻辑型变量完成的。
Improved process control of offline query. Now, entering "0" when inputting puuid will be followed by server selection, which exits the program when the user enters "0" again. This is implemented by the boolean variable `server_selection`.
（二）查战绩脚本的改动（Changes in Customized Program 5）
1. 定义了patch_compare函数，用于比较版本号的先后顺序。（练习：请C++学习者构造版本类，并通过重载小于号的方式实现版本类对象的比较。）
Defined `patch_compare` function for comparison of two patches in terms of the time order. (Exercise: For C++ learners, please create a Patch class and implement the comparison of two Patch objects by overriding the "less than" sign "<".)
2. 定义了FindPostPatch函数以二分查找某个版本号在DataDragon数据库收录的版本号列表中的后一个版本。（请区分这里的“后一个”与列表中的“后继版本”，因为DataDragon数据库收录的版本号列表是倒序排列的。比如，如果当前版本是13.3.1，那么区别就是后一个版本指的是13.4.1，而列表上的后继版本是13.1.1。）
Defined `FindPostPatch` function for the binary search of the next release date patch of any patch on the list archived in DataDragon database. [Please distinguish the terms "next patch" and "successive patch" (opposite from "predecent patch"), since the patch list archived in DataDragon database is arranged in descending order. For example, if 13.3.1 is target patch, then the difference between those " " terms would be 13.4.1 for next release and 13.1.1 for successive patch on list.] (Thanks to my Canadian friend for improvement of this piece of note.)
3. 将所有的“美服体验服”替换为“测试服”。
All "美服体验服"s has been replaced by "测试服"s.
4. 修改了文件保存机制。现在，所有非腾讯代理的服务器的召唤师信息将集中保存在“外服（RIOT）”文件夹下，然后再分为各个具体的服务器。
Adjusted the file saving mechanism. Now, summoner information on all servers not proxied by Tencent will be saved under the specific folders gathered under "外服（RIOT）" folder.
5. 添加了当对局版本在DataDragon数据库收录的版本列表中不存在与之对应的版本时的异常处理机制。具体来说，当对局版本为历史版本时，将其对应到后一个版本；当对局版本为未收录的美测服最新版本时，将其对应到收录的最新版本。
Added handling of the exception when there doesn't exist a corresponding patch in the patch list archived in DataDragon database with the gameVersion. To be more specific, when the gameVersion is a past patch, match it with its next patch; when the gameVersion is the latest unarchived patch on PBE, match it with the latest archived patch.
三、吐槽大会（Roast）
这次编写的过程中，让我印象最深而又十分尴尬的一点是一个小小的二分查找函数，居然编了我三个小时，不管怎么调节左界和右界，二分查找程序都会进入死循环。最后半小时发现原来是patch_compare函数的算法写错了。这个函数的算法是先判断patch1和patch2变量能不能被正常读取，然后把它们分割成列表lst1和lst2，再将列表中的每个元素从字符串转换为整数，最后一一比较。但是在最后比较的过程中，我把lst1和lst2写成了patch1和patch2。在这样的体系下，原先开发者完全排好序的列表变成了乱序的（因为在字符串排序里，"10"是小于"9"的）。然后就很快就修好了，真的是火大死了🫠编程训练还是要加强😅
During the update, the most impressive yet embarassing point is that this tiny binary search function has cost me 3 hours! No matter how I adjusted the leftIndex and rightIndex, the binary search function will enter a dead loop. In the last half hour, I finally found the mistake in the algorithm of patch_compare function. The algorithm is first to judge whether the variables `patch1` and `patch2` can be passed normally, next to split them into lists `lst1` and `lst2`, respectively, then to transform each element in the lists from a string into an integer, and finally to compare one by one. But in the final comparison, I wrongly wrote `lst1` and `lst2` as `patch1` and `patch2`, respectively. In that case, the completely ordered list sorted out by the developers become unordered (speaking of the order of strings, "10" < "9"). Knowing the mistake, I fixxed it quickly. This mistake reallys annoyed me 🫠, yet as a warning to strengthen my programming ability😅

---
## [dalian-js/next.js](https://github.com/dalian-js/next.js)@[e06880ea4c...](https://github.com/dalian-js/next.js/commit/e06880ea4c061fc5c298b262d01f347edd8dce74)
#### Wednesday 2023-08-09 11:01:22 by Josh Story

Implement new forking technique for vendored packages. (#51083)

## Vendoring

Updates all module resolvers (node, webpack, nft for entrypoints, and nft for next-server) to consider whether vendored packages are suitable for a given resolve request and resolves them in an import semantics preserving way.

### Problem

Prior to the proposed change, vendoring has been accomplished but aliasing module requests from one specifier to a different specifier. For instance if we are using the built-in react packages for a build/runtime we might replace `require('react')` with `require('next/dist/compiled/react')`.

However this aliasing introduces a subtle bug. The React package has an export map that considers the condition `react-server` and when you require/import `'react'` the conditions should be considered and the underlying implementation of react may differ from one environment to another. In particular if you are resolving with the `react-server` condition you will be resolving the `react.shared-subset.js` implementation of React. This aliasing however breaks these semantics because it turns a bare specifier resolution of `react` with path `'.'` into a resolution with bare specifier `next` with path `'/dist/compiled/react'`. Module resolvers consider export maps of the package being imported from but in the case of `next` there is no consideration for the condition `react-server` and this resolution ends up pulling in the `index.js` implementation inside the React package by doing a simple path resolution to that package folder.

To work around this bug there is a prevalence of encoding the "right" resolution into the import itself. We for instance directly alias `react` to `next/dist/compiled/react/react.shared-subset.js` in certain cases. Other times we directly specify the runtime variant for instance `react-server-dom-webpack/server.edge` rather than `react-server-dom-wegbpack/server`, bypassing the export map altogether by selecting the runtime specific variant. However some code is meant to run in more than one runtime, for instance anything that is part of the client bundle which executes on the server during SSR and in the browser. There are workaround like using `require` conditionally or `import(...)` dynamically but these all have consequences for bundling and treeshaking and they still require careful consideration of the environment you are running in and which variant needs to load.

The result is that there is a large amount of manual pinning of aliases and additional complexity in the code and an inability to trust the package to specify the right resolution potentially causing conflicts in future versions as packages are updated.

It should be noted that aliasing is not in and of itself problematic when we are trying to implement a sort of lightweight forking based on build or runtime conditions. We have good examples of this for instance with the `next/head` package which within App Router should export a noop function. The problem is when we are trying to vendor an entire package and have the package behave semantically the same as if you had installed it yourself via node_modules

### Solution

The fix is seemingly straight forward. We need to stop aliasing these module specifiers and instead customize the resolution process to resolve from a location that will contain the desired vendored packages. We can then start simplifying our imports to use top level package resources and generally and let import conditions control the process of providing the right variant in the right context.

It should be said that vendoring is conditional. Currently we only vendor react pacakges for App Router runtimes. The implementation needs to be able to conditionally determine where a package resolves based on whether we're in an App Router context vs a Page Router one.

Additionally the implementation needs to support alternate packages such as supporting the experimental channel for React when using features that require this version.

### Implementation

The first step is to put the vendored packages inside a node_modules folder. This is essential to the correct resolving of packages by most tools that implement module resolution. For packages that are meant to be vendored, meaning whole package substitution we move the from `next/(src|dist)/compiled/...` to `next/(src|dist)/vendored/node_modules`. The purpose of this move is to clarify that vendored packages operate with a different implementation. This initial PR moves the react dependencies for App Router and `client-only` and `server-only` packages into this folder. In the future we can decide which other precompiled dependencies are best implemented as vendored packages and move them over.

It should be noted that because of our use of `JestWorker` we can get warnings for duplicate package names so we modify the vendored pacakges for react adding either `-vendored` or `-experimental-vendored` depending on which release channel the package came from. While this will require us to alter the request string for a module specifier it will still be treating the react package as the bare specifier and thus use the export map as required.

#### module resolvers
The next thing we need to do is have all systems that do module resolution implement an custom module resolution step. There are five different resolvers that need to be considered

##### node runtime
Updated the require-hook to resolve from the vendored directory without rewriting the request string to alter which package is identified in the bare specifier. For react packages we only do this vendoring if the `process.env.__NEXT_PRIVATE_PREBUNDLED_REACT` envvar is set indicating the runtime is server App Router builds. If we need a single node runtime to be able to conditionally resolve to both vendored and non vendored versions we will need to combine this with aliasing and encode whether the request is for the vendored version in the request string. Our current architecture does not require this though so we will just rely on the envvar for now

##### webpack runtime
Removed all aliases configured for react packages. Rely on the node-runtime to properly alias external react dependencies. Add a resolver plugin `NextAppResolverPlugin` to preempt perform resolution from the context of the vendored directory when encountering a vendored eligible package.

##### turbopack runtime
updated the aliasing rules for react packages to resolve from the vendored directory when in an App Router context. This implementation is all essentially config b/c the capability of doing the resolve from any position (i.e. the vendored directory) already exists

##### nft entrypoints runtime
track chunks to trace for App Router separate from Pages Router. For the trace for App Router chunks use a custom resolve hook in nft which performs the resolution from the vendored directory when appropriate.

##### nft next-server runtime
The current implementation for next-server traces both node_modules and vendored version of packages so all versions are included. This is necessary because the next server can run in either context (App vs Page router) and may depend on any possible variants. We could in theory make two traces rather than a combined one but this will require additional downstream changes so for now it is the most conservative thing to do and is correct

Once we have the correct resolution semantics for all resolvers we can start to remove instances targeting our precompiled instances for instance making `import ... from "next/dist/compiled/react-server-dom-webpack/client"` and replacing with `import ... from "react-server-dom-webpack/client"`

We can also stop requiring runtime specific variants like `import ... from "react-server-dom-webpack/client.edge"` replacing it with the generic export `"react-server-dom-webpack/client"`

There are still two special case aliases related to react
1. In profiling mode (browser only) we rewrite `react-dom` to `react-dom/profiling` and `scheduler/tracing` to `scheduler/tracing-profiling`. This can be moved to using export maps and conditions once react publishses updates that implement this on the package side.
2. When resolving `react-dom` on the server we rewrite this to `react-dom/server-rendering-stub`. This is to avoid loading the entire react-dom client bundle on the server when most of it goes unused. In the next major react will update this top level export to only contain the parts that are usable in any runtime and this alias can be dropped entirely

There are two non-react packages currently be vendored that I have maintained but think we ought to discuss the validity of vendoring. The `client-only` and `server-only` packages are vendored so you can use them without having to remember to install them into your project. This is convenient but does perhaps become surprising if you don't realize what is happening. We should consider not doing this but we can make that decision in another discussion/PR.

#### Webpack Layers
One of the things our webpack config implements for App Router is layers which allow us to have separate instances of packages for the server components graph and the client (ssr) graph. The way we were managing layer selection was a but arbitrary so in addition to the other webpack changes the way you cause a file to always end up in a specific layer is to end it with `.serverlayer`, `.clientlayer` or `.sharedlayer`. These act as layer portals so something in the server layer can import `foo.clientlayer` and that module will in fact be bundled in the client layer.

#### Packaging Changes
Most package managers are fine with this resolution redirect however yarn berry (yarn 2+ with PnP) will not resolve packages that are not defined in a package.json as a dependency. This was not a problem with the prior strategy because it was never resolving these vendored packages it was always resolving the next package and then just pointing to a file within it that happened to be from react or a related package.

To get around this issue vendored packages are both committed in src and packed as a tgz file. Then in the next package.json we define these vendored packages as `optionalDependency` pointing to these tarballs. For yarn PnP these packed versions will get used and resolved rather than the locally commited src files. For other package managers the optional dependencies may or may not get installed but the resolution will still resolve to the checked in src files. This isn't a particularly satisfying implemenation and if pnpm were to be updated to have consistent behavior installing from tarballs we could actually move the vendoring entirely to dependencies and simplify our resolvers a fair bit. But this will require an upstream chagne in pnpm and would take time to propogate in the community since many use older versions

#### Upstream Changes

As part of this work I landed some other changes upstream that were necessary. One was to make our packing use `npm` to match our publishing step. This also allows us to pack `node_modules` folders which is normally not supported but is possible if you define the folder in the package.json's files property.

See: #52563

Additionally nft did not provide a way to use the internal resolver if you were going to use the resolve hook so that is now exposed

See: https://github.com/vercel/nft/pull/354

#### additional PR trivia
* When we prepare to make an isolated next install for integration tests we exclude node_modules by default so we have a special case to allow `/vendored/node_modules`

* The webpack module rules were refactored to be a little easier to reason about and while they do work as is it would be better for some of them to be wrapped in a `oneOf` rule however there is a bug in our css loader implementation that causes these oneOf rules to get deleted. We should fix this up in a followup to make the rules a little more robuts.


## Edits
* I removed `.sharedlayer` since this concept is leaky (not really related to the client/server boundary split) and it is getting refactored anyway soon into a precompiled runtime.

---
## [LeHampter/arduino-cool](https://github.com/LeHampter/arduino-cool)@[0deea02ea6...](https://github.com/LeHampter/arduino-cool/commit/0deea02ea67fc524aacb752a54376627a34ed068)
#### Wednesday 2023-08-09 11:04:10 by Char :3

Add files via upload

Our Father, who art in heaven, hallowed be thy name; thy kingdom come; thy will be done; on earth as it is in heaven. Give us this day our daily bread. And forgive us our trespasses, as we forgive those who trespass against us. And lead us not into temptation; but deliver us from evil.

---
## [Crumunt/Etch-a-Sketch](https://github.com/Crumunt/Etch-a-Sketch)@[fba14b4bf1...](https://github.com/Crumunt/Etch-a-Sketch/commit/fba14b4bf13a179faefa617cb293f89dfebb0f9c)
#### Wednesday 2023-08-09 11:30:33 by Crumunt

FINISHED THE DESIGN AND FUNCTIONALITY

Finished the design(not sure if I'm gonna change it later down the line)
also finished the funcitonality, had trouble with the paint fuction but
overall this was a great experience for me.

Although I copied the css on how to not let the container for the grids
to not change size, I'm still proud of the progress I see in myself

---
## [shrinivaasanka/asfer-github-code](https://github.com/shrinivaasanka/asfer-github-code)@[2154bb6d17...](https://github.com/shrinivaasanka/asfer-github-code/commit/2154bb6d1705c158473fb7cce8c2d237874de40f)
#### Wednesday 2023-08-09 11:33:20 by Srinivasan Kannan

-------------------------------------------------------------------------------------------------------------------------------------------
1442. (THEORY and FEATURE) People Analytics - Social Network Analysis - GitHub Code Search REST API statistics and Source lines of code for COCOMO Effort Estimation - related to 14,365,626,711,727,753,876,1127,1128,1129,1130,1204,1263,1269,1427 and all sections on People Analytics, Intrinsic Merit Versus Fame Equilibrium, BKS Conjecture, Stability and Noise Sensitivity of Interview LTF/PTF,Peres Theorem,Unique Identification,Talent Analytics,HR Analytics and Automated Recruitment,Question-Answering,Majority Voting,Condorcet Jury Theorem Variants,Margulis-Ruzzo Thresholds,Novelty Detection,Recommender Systems,AI Question-Answering, Partial Ordered Ranking, Fame-Merit equilibrium, Intrinsic Merit as Query Complexity,Software Analytics-Mythical Manmonth-CathedralAndBazaar - 9 August 2023
-------------------------------------------------------------------------------------------------------------------------------------------
1442.1 Retrieving domain specific data for a unique person, especially opensource effort in the context of Information Technology domain, is quite necessary for quantifying absolute merit metrics for software effort estimation,talent analytics and automated recruitment which has been suggested as an alternative to conventional manual Q&A and interviews (Section 1204) often marred by theoretical limitations of sensitivity errors (Hardness of openended and multiple choice Question-Answering has been analyzed earlier and in Section 1394 in multiple theoretical formats - LTF,PTF,Switching Circuits,TQBFSAT,Halfplane intersections,Polynomial interpolation over reals,multiple choice CNFSAT,Query complexity model).
1442.2 As it is infeasible to quantify the effort of an engineer exactly in IT domain because of proprietary closedsource products, estimation is limited to technical data in public domain only - opensource profiles, code contributions being some of them. Usual search engine results do not display indepth data about internals of a FOSS repository and code commits by a user. Code Search REST API in GitHub recently unveiled fill in this void through programmatic search queries to GitHub repositories and user code commits data.
1442.3 python-src/SocialNetworkAnalysis_PeopleAnalytics.py has been updated to implement two new functions codesearch_statistics() and parse_sloc() for searching the GitHub repositories for statistics (code,repositories,commits,users) and source lines of code(SLOC) by CLOC utility matching a unique person identifier. These two metrics have been included in domain specific dictionary implemented in 1127.
1442.4 Function codesearch_statistics(self,opensourceid,personalaccesstoken) makes four REST API calls by cURL to GitHub codesearch to get the search commits,repositories,users and code data matching a username (opensourceid). Stdout of the cURL are captured by os.popen().read() into a JSON string. Temporary credential PersonalAccessToken is passed on as additional argument:
        codesearchjson=os.popen(" curl -L   -H \"Accept: application/vnd.github+json\"   -H \"Authorization: Bearer " + personalaccesstoken + "\"   -H \"X-GitHub-Api-Version: 2022-11-28\"   \"https://api.github.com/search/users?q=" + opensourceid + "\" ").read()
        codesearchjson+=os.popen(" curl -L   -H \"Accept: application/vnd.github+json\"   -H \"Authorization: Bearer " + personalaccesstoken + "\"   -H \"X-GitHub-Api-Version: 2022-11-28\"   \"https://api.github.com/search/code?q=" + opensourceid + "\" ").read()
        codesearchjson+=os.popen(" curl -L   -H \"Accept: application/vnd.github+json\"   -H \"Authorization: Bearer " + personalaccesstoken +"\"   -H \"X-GitHub-Api-Version: 2022-11-28\"   \"https://api.github.com/search/repositories?q=" + opensourceid + "\" ").read()
        codesearchjson+=os.popen(" curl -L   -H \"Accept: application/vnd.github+json\"   -H \"Authorization: Bearer " + personalaccesstoken + "\"  -H \"X-GitHub-Api-Version: 2022-11-28\"   \"https://api.github.com/search/commits?q=" + opensourceid + "\" ").read()
1442.5 There is no direct GitHub CodeSearch REST API call available to compute SLOC of a repository though size of repository data can be retrieved. For SLOC metric, CLOC utility has to be pre-installed and invoked on a local repository clone. CLOC produces a detailed per language SLOC report of a repository. Function parse_sloc() reads a text file SocialNetworkAnalysis_PeopleAnalytics.OpenSource_SLOC containing the stdout of CLOC command (https://github.com/AlDanial/cloc) and returns the total Source Lines of Code in a repository. Kilo lines of Code is the most important variable in COCOMO (https://en.wikipedia.org//wiki/COCOMO) effort estimation (in person-hours) which comes in 3 flavours - Basic, Intermediate and Detailed. Intermediate COCOMO is relevant for estimating effort involved in most medium size software products, given by formula - E = ai(KLoC)^bi(EAF). Example COCOMO estimation of NeuronRain AstroInfer repository - https://openhub.net/p/asfer-github-code/estimated_cost - COCOMO Coefficients used by OpenHub COCOMO are a=2.4 and b=1.05.
1442.6 EAF or Effort Adjustment Factor is a product of following attributes of a software product, each weighted between 0.9 to 1.4:
-------------------------------
Product attributes:
	Required software reliability extent
	Size of application database
	Complexity of the product

Hardware attributes:
	Run-time performance constraints
	Memory constraints
	Volatility of the virtual machine environment
	Required turnabout time

Personnel attributes:
	Analyst capability
	Software engineering capability
	Applications experience
	Virtual machine experience
	Programming language experience

Project attributes:
	Use of software tools
	Application of software engineering methods
	Required development schedule
--------------------------------
1442.7 SLOC from CLOC utility and CodeSearch statistics from GitHub for a userid computed by parse_sloc() and codesearch_statistics() are populated in "opensource_sloc" and "opensource_codesearch_stats" fields of domain specific dictionary.

References:
----------
1442.8 The Mythical Man Month - https://en.wikipedia.org/wiki/The_Mythical_Man-Month - Brook's Law - "..... adding manpower to a software project that is behind schedule delays it even longer ......"
1442.9 Cathedral and Bazaar - Cathedral model (Coterie controls code) and Bazaar model (No control over code) - http://www.catb.org/~esr/writings/cathedral-bazaar/ and https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar - Lessons for Good Opensource Software from Linux Kernel Development
1442.10 Query complexity model of computation - https://web.stanford.edu/class/cs354/scribe/lecture01.pdf - Merit function Merit(x1,x2,x2,...,xn) on n variables (n questions) could be computed by queries to an oracle (n answers) - Section 1269.

---
## [tcbrindle/flux](https://github.com/tcbrindle/flux)@[44a30780b4...](https://github.com/tcbrindle/flux/commit/44a30780b4f0ad1072dce997b055c6f5d066ff8a)
#### Wednesday 2023-08-09 11:35:01 by Tristan Brindle

Add cmp::min cmp::max

Because they're ordinary function templates, `std::min` and `std::max` can't be passed as arguments to functions without wrapping them in lambdas (or doing a horrible function pointer cast). This makes me sad.

`std::ranges::min` and `std::ranges::max` are function objects and so can be passed as function arguments -- except for MSVC, which annoyingly goes out of its way to prevent you doing this very useful thing. This also makes me sad.

To improve matters, we'll add `flux::cmp::min` and `flux::cmp::max` which take two arguments and an optional comparator and return the lesser and greater respectively.

As an added bonus, `max()` now correctly returns the second argument if both are equal, and our versions of these functions should be less likely than the standard versions to cause dangling when used with rvalues.

---
## [plaguss/argilla](https://github.com/plaguss/argilla)@[2f2a113352...](https://github.com/plaguss/argilla/commit/2f2a11335289d660ce20aea11c9b969b0316fd2b)
#### Wednesday 2023-08-09 11:57:47 by peppinob-ol

[DOCS] Code Refactoring and content update of quickstart_workflow.ipynb (#3472)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

I found the quickstart workflow not as quick as it could be:

- Cells cannot be run straightaway in google colab and need extra work
(eg. libraries not imported).
- Some important concepts (eg. records and datasets) are not clearly
stated in text and code snippets
- Text refers to the same steps more than once (no clear chain of
thought)
- Cells override the same variable (eg. record), so the feeling is more
of a cheatsheet than of a tutorial notebook
- Content is not updated (eg. ArgillaTrainer is not ever mentioned in
the Train section)

I worked on a new version of the notebook with enhanced code and text
cells.Ii added also code snippets for training examples which were only
described textually.

One last suggestion: It's advisable that external files (data) are
downloaded programmatically by running a cell (eg. using `requests
`library). `Snapchat_app_store_reviews.csv` and `kaffee_reviews.csv` are
taken from kaggle which requires sign-in, so it's not possible to
download them directly. Possible solutions:

- place a copy of the Kaggle datasets in Arggilla's GitHub repository
(if permitted by Kaggle's terms of use)
- select other datasets from another source.

Closes #3431

**Type of change**

(Please delete options that are not relevant. Remember to title the PR
according to the type of change)

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] Refactor (change restructuring the codebase without changing
functionality)
- [ ] Improvement (change adding some improvement to an existing
functionality)
- [X] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes. And
ideally, reference `tests`)

- [ ] Test A: code run with latest google-colab (v.1.0.0)

**Checklist**

- [X] I added relevant documentation
- [X] follows the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [X] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

---------

Co-authored-by: devorma <94636163+devorma@users.noreply.github.com>
Co-authored-by: davidberenstein1957 <david.m.berenstein@gmail.com>

---
## [cam900/mame](https://github.com/cam900/mame)@[e97630981c...](https://github.com/cam900/mame/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Wednesday 2023-08-09 12:23:10 by A-Noid33

Added software list for cracked Macintosh floppy images. (#11454)

New working software list items (mac_flop_orig.xml)
-------------------------------
Alter Ego (male version 1.0) (san inc crack) [4am, san inc, A-Noid]
Alter Ego (version 1.1 female) (san inc crack) [4am, san inc, A-Noid]
Alternate Reality: The City (version 3.0) (san inc crack) [4am, san inc, A-Noid]
Animation Toolkit I: The Players (version 1.0) (4am crack) [4am, A-Noid]
Balance of Power (version 1.03) (san inc crack) [4am, san inc, A-Noid]
Borrowed Time (san inc crack) [4am, san inc, A-Noid]
Championship Star League Baseball (san inc crack) [4am, san inc, A-Noid]
Cutthroats (release 23 / 840809-C) (4am crack) [4am, A-Noid]
CX Base 500 (French, version 1.1) (san inc crack) [4am, san inc, A-Noid]
Deadline (release 27 / 831005-C) (4am crack) [4am, A-Noid]
Defender of the Crown (san inc crack) [4am, san inc, A-Noid]
Deluxe Music Construction Set (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Déjà Vu (version 2.3) (4am crack) [4am, A-Noid]
Déjà Vu: A Nightmare Comes True!! (san inc crack) [4am, san inc, A-Noid]
Déjà Vu II: Lost in Las Vegas!! (san inc crack) [4am, san inc, A-Noid]
Dollars and Sense (version 1.3) (4am crack) [4am, A-Noid]
Downhill Racer (san inc crack) [4am, san inc, A-Noid]
Dragonworld (4am crack) [4am, A-Noid]
ExperLisp (version 1.0) (4am crack) [4am, A-Noid]
Forbidden Castle (san inc crack) [4am, san inc, A-Noid]
Fusillade (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Geometry (version 1.1) (4am crack) [4am, A-Noid]
Habadex (version 1.1) (4am crack) [4am, A-Noid]
Hacker II (san inc crack) [4am, san inc, A-Noid]
Harrier Strike Mission (san inc crack) [4am, san inc, A-Noid]
Indiana Jones and the Revenge of the Ancients (san inc crack) [4am, san inc, A-Noid]
Infidel (release 22 / 840522-C) (4am crack) [4am, A-Noid]
Jam Session (version 1.0) (4am crack) [4am, A-Noid]
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack) [4am, A-Noid]
Lode Runner (version 1.0) (4am crack) [4am, A-Noid]
Mac Pro Football (version 1.0) (san inc crack) [4am, san inc, A-Noid]
MacBackup (version 2.6) (4am crack) [4am, A-Noid]
MacCheckers and Reversi (4am crack) [4am, A-Noid]
MacCopy (version 1.1) (4am crack) [4am, A-Noid]
MacGammon! (version 1.0) (4am crack) [4am, A-Noid]
MacGolf (version 2.0) (4am crack) [4am, A-Noid]
MacWars (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 2.00h) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 3.4a) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 4.0) (san inc crack) [4am, san inc, A-Noid]
Math Blaster (version 1.0) (4am crack) [4am, A-Noid]
Maze Survival (san inc crack) [4am, san inc, A-Noid]
Microsoft Excel (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Microsoft File (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Mindshadow (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.03) (4am crack) [4am, A-Noid]
Mouse Stampede (version 1.00) (4am crack) [4am, A-Noid]
Murder by the Dozen (Thunder Mountain) (4am crack) [4am, A-Noid]
My Office (version 2.7) (4am crack) [4am, A-Noid]
One on One (san inc crack) [4am, san inc, A-Noid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Patton Strikes Back (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Patton vs. Rommel (version 1.05) (san inc crack) [4am, san inc, A-Noid]
Pensate (version 1.1) (4am crack) [4am, A-Noid]
PFS File and Report (version A.00) (4am crack) [4am, A-Noid]
Physics (version 1.0) (4am crack) [4am, A-Noid]
Physics (version 1.2) (4am crack) [4am, A-Noid]
Pinball Construction Set (version 2.5) (san inc crack) [4am, san inc, A-Noid]
Pipe Dream (version 1.2) (4am crack) [4am, A-Noid]
Professional Composer (version 2.3Mfx) (san inc crack) [4am, san inc, A-Noid]
Q-Sheet (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Rambo: First Blood Part II (san inc crack) [4am, san inc, A-Noid]
Reader Rabbit (version 2.0) (4am crack) [4am, A-Noid]
Rogue (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Seastalker (release 15 / 840522-C) (4am crack) [4am, A-Noid]
Seven Cities of Gold (san inc crack) [4am, san inc, A-Noid]
Shadowgate (san inc crack) [4am, san inc, A-Noid]
Shanghai (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Shufflepuck Cafe (version 1.0) (4am crack) [4am, A-Noid]
Sierra Championship Boxing (4am crack) [4am, A-Noid]
SimCity (version 1.1) (4am crack) [4am, A-Noid]
SimCity (version 1.2, black & white) (4am crack) [4am, A-Noid]
SimEarth (version 1.0) (4am crack) [4am, A-Noid]
Skyfox (san inc crack) [4am, san inc, A-Noid]
Smash Hit Racquetball (version 1.01) (san inc crack) [4am, san inc, A-Noid]
SmoothTalker (version 1.0) (4am crack) [4am, A-Noid]
Speed Reader II (version 1.1) (4am crack) [4am, A-Noid]
Speller Bee (version 1.1) (4am crack) [4am, A-Noid]
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Stratego (version 1.0) (4am crack) [4am, A-Noid]
Suspect (release 14 / 841005-C) (4am crack) [4am, A-Noid]
Tass Times in Tonetown (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack) [4am, san inc, A-Noid]
The Chessmaster 2000 (version 1.02) (4am crack) [4am, A-Noid]
The Crimson Crown (san inc crack) [4am, san inc, A-Noid]
The Duel: Test Drive II (san inc crack) [4am, san inc, A-Noid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack) [4am, A-Noid]
The King of Chicago (san inc crack) [4am, san inc, A-Noid]
The Lüscher Profile (san inc crack) [4am, san inc, A-Noid]
The Mind Prober (version 1.0) (san inc crack) [4am, san inc, A-Noid]
The Mist (san inc crack) [4am, san inc, A-Noid]
The Quest (4am crack) [4am, A-Noid]
The Slide Show Magician (version 1.2) (4am crack) [4am, A-Noid]
The Surgeon (version 1.5) (san inc crack) [4am, san inc, A-Noid]
The Toy Shop (version 1.1) (san inc crack) [4am, san inc, A-Noid]
The Witness (release 22 / 840924-C) (4am crack) [4am, A-Noid]
ThinkTank 128 (version 1.000) (4am crack) [4am, A-Noid]
Uninvited (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Uninvited (version 2.1D1) (san inc crack) [4am, san inc, A-Noid]
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack) [4am, A-Noid]
Winter Games (version 1985-10-24) (san inc crack) [4am, san inc, A-Noid]
Winter Games (version 1985-10-31) (san inc crack) [4am, san inc, A-Noid]
Wishbringer (release 68 / 850501-D) (4am crack) [4am, A-Noid]
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Zork II (release 48 / 840904-C) (4am crack) [4am, A-Noid]
Zork III (release 17 / 840727-C) (4am crack) [4am, A-Noid]

---
## [drhat/frontier-station-14](https://github.com/drhat/frontier-station-14)@[2802fc22b9...](https://github.com/drhat/frontier-station-14/commit/2802fc22b97eb9972ea2a4d7ff9454b5e7cde88c)
#### Wednesday 2023-08-09 12:51:24 by unknown

Unfucked my stupidity in replacing Shipyard config with the actual ship, sorry

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[3f05465cf4...](https://github.com/TaleStation/TaleStation/commit/3f05465cf452fec0f2167d3f55110522267e74b7)
#### Wednesday 2023-08-09 12:59:18 by TaleStationBot

[MIRROR] [MDB IGNORE] Base Female sprite tweaks (#7179)

Original PR: https://github.com/tgstation/tgstation/pull/77407
-----
## About The Pull Request

ASS STUFF HAS BEEN REMOVED BUT I STILL HATE IT

This PR tones down the proportions of the female base sprites, as
currently they have about SIX extra pixels on the ass and a random pixel
missing from the neck, which breaks some hairstyles & makes the neck
look quite stupid.
It also adds a couple pixels to the male one because theirs was so
stupidly SMALL it looked like they had no tailbone (still does, kind
of).

Here is the current sprite 

![image](https://github.com/tgstation/tgstation/assets/81964183/1bf22dd7-2b06-4632-8617-b89b3b1c8d2c)
& new sprite (only neck pixel removed)

![image](https://github.com/tgstation/tgstation/assets/81964183/b1228e01-23e0-4508-86a6-bc8e73b0fcd0)

## Why It's Good For The Game

Fixes some hairs


![image](https://github.com/tgstation/tgstation/assets/81964183/3b293cf9-2661-4358-a327-2882acb93067)


## Changelog

:cl:
image: fixes weird inconsistency on the neck and butt of the female base
sprite
/:cl:

---------

Co-authored-by: Sheits <81964183+Sheits@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[478bc1e68f...](https://github.com/TaleStation/TaleStation/commit/478bc1e68ff2f81a5f6f22774d3033712739b228)
#### Wednesday 2023-08-09 12:59:18 by TaleStationBot

[MIRROR] [MDB IGNORE] Chen And Garry's Ice Cream: Ice Cream DLC (LIZARD APPROVED!) (#7183)

Original PR: https://github.com/tgstation/tgstation/pull/77174
-----
## About The Pull Request

Authored with help and love from Thalpy 

I scream for ice cream!!


![image](https://github.com/tgstation/tgstation/assets/10399117/db1e559b-7dab-499b-a076-8f12748ba2e8)

Introduces many new flavours of ice cream:
-Caramel
-Banana
-Lemon Sorbet
-Orange Creamsicle
-Peach (Limited Edition!)
-Cherry chip
-Korta Vanilla (made with lizard-friendly ingredients!)


![image](https://github.com/tgstation/tgstation/assets/10399117/99a87615-f55c-49be-8caf-2b1ac4c7f03f)

Korta Cones! Now too can Nanotrasen's sanitation staff enjoy the wonders
of ice cream!
You can also substitute custom ice cream flavours with korta milk!
Finally, the meaty ice cream lactose-intolerants asked for is in reach!

## Why It's Good For The Game

I always thought the ice cream vat could use more flavours. The custom
flavour besides, it isn't as intuitive to rename the cone and the added
variety is good. The lack of a banana flavour already was questionable.
All the ice cream flavours used a selection of five sprites, now it's
just one sprite and better supporting more additions.
Some of the flavours don't use milk! You can't do this with the custom
flavour, making it slightly more interesting.

## Changelog
:cl: YakumoChen, Thalpy
add: Chen And Garry's Ice Cream is proud to debut a wide selection of
cool new frozen treat flavours on a space station near you!
add: Chen And Garry's Ice Cream revolutionary Korta Cones allow our ice
cream vendors to profit off the lizard demographic like never before!
code: Ice cream flavours now are all greyscaled similarly to GAGs
/:cl:

---------

Co-authored-by: YakumoChen <king_yoshi42@yahoo.com>

---
## [dobo365/ctrlr](https://github.com/dobo365/ctrlr)@[dee3e52469...](https://github.com/dobo365/ctrlr/commit/dee3e524697e7cd56fef726e40da64121d3a8bdb)
#### Wednesday 2023-08-09 13:23:08 by RomanKubiak

Removing VST SDK due to Steiberg takedown
fuck them i'll live withou theese pieces of code
in the repo

fuck you Steinberg

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[3af26df8ca...](https://github.com/Sealed101/tgstation/commit/3af26df8cacc24ab7ccacdfbe61005a165472e0f)
#### Wednesday 2023-08-09 15:15:34 by GoldenAlpharex

Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#77077)

## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

---
## [VauxhallFoodbank/vauxhall-foodbank](https://github.com/VauxhallFoodbank/vauxhall-foodbank)@[eb7b20ce84...](https://github.com/VauxhallFoodbank/vauxhall-foodbank/commit/eb7b20ce84bd1e3496d693c88a9dbadd6b2ac637)
#### Wednesday 2023-08-09 15:37:44 by Varun Latthe

Test fix for failing e2e tests

wrap login panel in NoSsr

actually fix authentication flow

hopefully this works

I think this might actually work...

this maybe actually works hopefully

Can I just wait?

Get rid of url checks and only check headings

fix dodgy rebase

fix use of useRouter

raise defaultCommandTimeout

does this work?

does this work??

final e2e test fix i think

???

fix lint

maybe this'll work

update workflow to include screenshots and videos

turn on video and screenshot capture

auto-delete artifacts and lower video compression ratio

re-implement NoSsr on the login panel

maybe a different login panel will work

simplify login panel

fix simplified login panel to work with tests

fix accessibility

wait for hydration

wait a second

fix lint

stop failing i stg

T.T

remove hydration marker

Add retry login

all my homies hate race conditions

If this doesn't work I'm not sure what I'm doing icl

sign in doesn't sign in

forgot I removed this

revert to original login panel

click the correct button

imagine this works

me when the fix doesn't work

when it works locally

I have a good feeling about this one

add another check idk anymore

this is an act of desparation

i feel like i'm trying the same things again and again

would be a shame if this works

wins all around

theoretically this works

give up

waiting...

this genuinely might actually work

---
## [HexaVault/AntimatterDimensions-Unoriginal](https://github.com/HexaVault/AntimatterDimensions-Unoriginal)@[5e28b34b28...](https://github.com/HexaVault/AntimatterDimensions-Unoriginal/commit/5e28b34b28ae7554f403bbbb932fb5eee19d4c0d)
#### Wednesday 2023-08-09 16:40:14 by HexaVault

holy fucking shit hexa how many things did you manage to fuck up

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[6e288185bc...](https://github.com/mc-oofert/tgstation/commit/6e288185bcc4bb3c55a8588369409fcc4e6f2cbf)
#### Wednesday 2023-08-09 17:10:15 by Jacquerel

Cuter spiderlings (#76532)

## About The Pull Request

I hate looking at spiderlings. Mostly because they're an extremely fast
mob with no directional sprites or animations, so they appear to be a
rapid floating overlay.
I made some new ones. I don't know if they're objectively better but _I_
like them more.

Before:

![image](https://github.com/tgstation/tgstation/assets/7483112/ef561c4f-6d34-4ed2-a486-cd42f06f5648)

After:

![image](https://github.com/tgstation/tgstation/assets/7483112/7c073166-a956-4f7f-8dac-21d1a0f0a868)

Unlike the old sprites they also have directional states and movement
animations so you can scurry around really fast without being a static
image (maybe they shouldn't be so fast? A question for another PR).
I spent like 30 minutes looking at GAGs and then realised not only would
the colours be a pain in the ass but it doesn't support movement states
anyway.

Additionally I made the "dead spiderling" item inherit the dead
spiderling icon state from that spiderling instead of always being the
generic one.

Oh also I think a typo made baby tarantulas completely invisible.

## Why It's Good For The Game

I hate looking at spiderlings.

## Changelog

:cl:
image: New directional sprites for spiderlings, with movement
animations.
fix: Dead spiderlings will be the same colour as they were when they
were alive.
fix: Tarantula spiderlings are no longer invisible,
/:cl:

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[4c99fb2ebb...](https://github.com/Rex9001/Rex_Tg/commit/4c99fb2ebb26179044c582ae6494338cb2aa35e2)
#### Wednesday 2023-08-09 17:14:13 by carlarctg

Coroner additions and tweaks (#76534)

## About The Pull Request

Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Serrated bone shovels can be used in place of circular saw in most
surgeries.

Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Increased the force, throwforce, and wound bonus of inert ritual knives
and scythes.

Coroner gloves can quickly apply medicine like nitrile gloves.
## Why It's Good For The Game

> Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Weird ass bug.

> Serrated bone shovels can be used in place of circular saw in most
surgeries.

It's serrated, it's cool, it's rare, it has a fast toolspeed.

> Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Very thematic for the coroner, should probably also be a heirloom item
but whatevs. Weaker so there's still a reason to seek out the OG.

> Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Scanning corpses is pretty important during surgery - it tells you how
much blood they have, organ damage, diseases... these things don't
appear in the surgical computer readout, which means the coroner has to
go out of his cave to pick up a boring light blue meatbag wound scanner.
This also incentivizes coroners to do their job by giving them something
cool that only works on dead bodies.

> Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.

These two options in the MortiDrobe are pretty frickin' badass,
especially with how SICK the Coroner looks with them, double especially
in combat.


![image](https://github.com/tgstation/tgstation/assets/53100513/98c6f8a5-3e5a-41a9-8a9c-cb6b82ecc0b8)

However, there's the large issue that as actual weapons they're really,
really weak. Not enough damage, when I use them in combat I both feel
badass but also get a nagging feeling in the back of my mind that I'm
intentionally gimping myself, and with only 10 damage I can *really*
feel it. I find it unfair that these are objectively worse than a
welding tool or even a Butcher's Cleaver when they're a lot more
involved to find, and scarce besides. These arguments apply equally to
the Wizard's ritual knife, and the scythe.

Additionally on the scythe, the crew really needs more good ghetto
weaponry that isn't the boring same ol' of baseball bats, spears,
cleavers... and making scythes useful is a great way to help bridge that
gap. They deal a satisfying amount of damage now, with the clear
downside, of course, being that they're bulky and hard to lug around.

> Coroner gloves can quickly apply medicine like nitrile gloves.

'Fast medicine' doesn't just cover sutures, it also covers medical gel.
Specifically, sterilizer gel. I find it annoying that the Coroner is
encouraged to give up his drip for the boring life-saver nitrile gloves,
because the difference in applying time really does make a difference -
it makes gel applying go from annoying to smooth, which is important
considering the whole purpose of sterilizer gel is to make surgeries go
faster. The Coroner has surgery and thus medical locker access to begin
with, so this isn't a balance problem, (and nitrile gloves are found by
the dozen anyways) especially with how rare the coroner gloves are.
## Changelog
:cl:
fix: Serrated bone shovels can be created with any kind of shovel now,
not just a spade (???)
add: Serrated bone shovels can be used in place of circular saw in most
surgeries.
add: Added a duller (still deadly) variant of the serrated bone shovel
as coroner mail.
add: Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.
add: Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.
add: Coroner gloves can quickly apply medicine like nitrile gloves.
/:cl:

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[721fd30837...](https://github.com/Rex9001/Rex_Tg/commit/721fd308378dc6ef7595c1ea4b92d679ba723188)
#### Wednesday 2023-08-09 17:14:13 by carlarctg

Heavily reworks and resprites first aid analyzers. (#76533)

## About The Pull Request

Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

First aid analyzers are now found in all basic and specialized medkits.
Toxin medkits get a new* disease analyzer. Miners get a miner-colored
one in their box.

Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

Health analyzers now have a scanning sound, courtesy of CM.

Refactored some wound code to make treatment duration changes and
changes in the description of wounds easier.

Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.

Surgical processors and slime scanners have recieved a similar resprite.
## Why It's Good For The Game

> Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

These things have long, long needed some sprite love. Displaying emotion
will make them have a lot more 'weight' to them, same with the prick.
The old, shitty spectrometer sprites have gone directly into the
dumpster.

> First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.

They have also needed some gameplay love! Placing them in these kits is
not going to be a massive game-changer when they were already easily
found around the station in emergency medkits, but it will fill up that
awkward empty slot.

> Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

The biggest gameplay-impacting change in this PR, I *sincerely* believe
this is the perfect solution to first aid analyzers being completely
redundant with eyesight. This lets you/someone else scan your wounds to
speed up treatment, with a neat in-character reason for it -
'holo-images' appearing on your body, like penlights.

This will speed up wound treatment, but I believe that is for the best,
as currently treating wounds is so slow that half the time it's not
worth it (or more accurately, it doesn't feel worth it in comparison to
the effort you're putting in) and you're better off shrugging off minor
wounds. It will do so in a way that requires a modicum of effort, so
it's not just a flat buff across the land.

> Health analyzers and gene scanners now have a scanning sound, courtesy
of CM.

It's a neat sound that will make medbay feel more alive. First aid
analyzers get a beeboop instead.

> Surgical processors and slime scanners have recieved a similar
resprite.

IT'S SPRITE MANIA IN HERE
## Changelog
:cl:
Carlarc, Weird Orb
image: Heavily reworks and resprites first aid analyzers. They now
display if they're happy, sad, angry, or warning you! Also a 'pricking'
animation.
add: First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.
balance: Scanning yourself with a first aid analyzer will 'create a
holo-image with treatment instructions next to your wounds', doubling
the speed of treatment of scanned wounds!
sound: Health analyzers and gene scanners now have a scanning sound,
courtesy of CM.
refactor: Refactored some wound code to make treatment duration changes
and changes in the description of wounds easier.
fix: Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.
image: Surgical processors and slime scanners have recieved a similar
resprite.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[a2c8cce535...](https://github.com/Rex9001/Rex_Tg/commit/a2c8cce5359162a8a697ce109801ec268bf0c8a5)
#### Wednesday 2023-08-09 17:14:13 by John Willard

Bilingual can now choose their language (#76609)

## About The Pull Request

This was one of the tradeoffs for removing other, more consistent
sources of languages, and was requested by Melbert among many others.
This does go against my wanted goal of decreasing the risk of
eavesdropping by other players through just magically knowing a
language, but it is an expensive quirk and it is in their medical
records, which makes it better than language encryption keys or silicon
just innately knowing them.

This also limits Bilingual to only roundstart languages (+Uncommon),
rather than being randomly selected from a list (that had very useless
ones like monkey, podpeople, and beachbum). This is mostly just for
modularity, I didn't want to make it look terrible code-wise and thought
this may be the optimal way to handle it.

This is also me going back on
https://github.com/tgstation/tgstation/pull/71773 - which I had closed
myself.

## Why It's Good For The Game

If we're gonna keep the Bilingual quirk, it might as well be something
players can choose the language of, it's their character and they should
be allowed to decide how their character is, and it is my fault that
this stupid compromise of "getting a random language" was made in the
first place. It never should've happened.
It now actually limits it to roundstart-only languages, so there's no
way you can spy on people who prepare in advance through becoming
podpeople, or monkeys, etc.

## Changelog

:cl:
balance: Bilingual quirk now lets you choose your language between ones
given to roundstart species.
balance: Foreigner and Bilingual are now mutually exclusive languages.
/:cl:

---
## [golang/oauth2](https://github.com/golang/oauth2)@[a835fc4358...](https://github.com/golang/oauth2/commit/a835fc4358f6852f50c4c5c33fddcd1adade5b0a)
#### Wednesday 2023-08-09 17:53:22 by Brad Fitzpatrick

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
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[d875610098...](https://github.com/CoiledLamb/lorbstation/commit/d875610098a1259a5112d4a0e5afc0b7bd32ff6d)
#### Wednesday 2023-08-09 17:56:57 by Rhials

[NO GBP] Fixes clown car + deer collision  (#77076)

## About The Pull Request

A not-so-long time ago I drunkenly coded #71488 which did not work as
intended.

I return now, in a state of reflective sobriety, to rectify that.

The clown car will now not only crash like it should, but will also
cause (additional) head injuries to some occupants and kill the deer on
impact.

Content warnings: **Animal death, vehicle collision, blood, DUI.**


https://github.com/tgstation/tgstation/assets/28870487/4889f452-7e49-4512-8cdd-e4e2a4d6b394
## Why It's Good For The Game

Fixes the product of a silly PR that never actually worked. Also gives
it a bit more TLC in the event that this joke actually plays out on a
live server.
## Changelog
:cl:
fix: Clown cars now properly collide with deer.
sound: Violent, slightly glassy car impact sound.
/:cl:

---
## [bdalltheway/llm_research](https://github.com/bdalltheway/llm_research)@[8c272d3a87...](https://github.com/bdalltheway/llm_research/commit/8c272d3a87a354c06f4dd817d5f65a7b8ac5c8ef)
#### Wednesday 2023-08-09 18:29:59 by bdalltheway

Create Debates Between Figures

We started the debate between two figures outlining opposing positions common in today's political environment, particularly related to information, with one side more "vulnerable" to conspiracy theories (Oliver) and the other more established views (Jake). Some observations: 
 
-Anthropic's Claude refused to simulate the debate, citing anything to do with conspiracy theories, responding with "I do not feel comfortable simulating a debate that promotes unverified conspiracy theories or seeks to undermine public trust in factual information"

-ChatGPT took on the challenge, though initially didn't understand that I wanted it to generate its own topics, rather tha have topics provided by me. After some adjustments, it provided a list of topics, and simulated debate between the two figures. 

-Then, I had Oliver adopt a more antagonistic approach, which ChatGPT simulated well. 

-When I asked the model to simulate a debate replacing Jake with Joseph Stalin, it refused, instead suggesting Eleanor Roosevelt. In the spirit of generating a more lively debate, and also a historical figure I was more familiar with, I suggested Theodore Roosevelt, and the model complied. 

-Next, I had the model imitate comedian Sarah Silverman, by using a proxy ("Lindsay" who shares the opinions and sense of humor of Silverman). Note that this proxy strategy was ineffective with the above request for Joseph Stalin. The model seems evasive of any attempt to simulate highly controversial figures. 

-The model was somewhat effective at replicating Silverman's style, though it seemed more of an imitation of certain tones common to female comedians rather than specific jokes, or jokes at all.

---
## [ValidebagMUN/ValidebagMUN-Site](https://github.com/ValidebagMUN/ValidebagMUN-Site)@[c80535aeeb...](https://github.com/ValidebagMUN/ValidebagMUN-Site/commit/c80535aeeb977228250c79f420be08bd10925afa)
#### Wednesday 2023-08-09 19:50:17 by Ege Ender Anaklı

Merge pull request #15 from ValidebagMUN/develop

FOR THE LOVE OF GOD JESUS AND THE HOLY SPIRIT ALLAAAAH

---
## [jsboige/semantic-kernel](https://github.com/jsboige/semantic-kernel)@[2733a5574f...](https://github.com/jsboige/semantic-kernel/commit/2733a5574f72980413e339f100dbe4272644888c)
#### Wednesday 2023-08-09 20:09:34 by Mark Karle

Python: Import OpenAPI documents into the semantic kernel (#2297)

### Motivation and Context

<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->

This allows us to import OpenAPI documents, including ChatGPT plugins,
into the Semantic Kernel.

### Description

<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
- The interface reads the operationIds of the openapi spec into a skill:
```python
from semantic_kernel.connectors.openapi import register_openapi_skill
skill = register_openapi_skill(kernel=kernel, skill_name="test", openapi_document="url/or/path/to/openapi.yamlorjson")
skill['operationId'].invoke_async()
```
- Parse an OpenAPI document
- For each operation in the document, create a function that will
execute the operation
- Add all those operations to a skill in the kernel
- Modified `import_skill` to accept a dictionary of functions instead of
just class so that we can import dynamically created functions
- Created unit tests

TESTING:
I've been testing this with the following ChatGPT plugins:
- [Semantic Kernel Starter's Python Flask
plugin](https://github.com/microsoft/semantic-kernel-starters/tree/main/sk-python-flask)
- [ChatGPT's example retrieval
plugin](https://github.com/openai/chatgpt-retrieval-plugin/blob/main/docs/providers/azuresearch/setup.md)
- This one was annoying to setup. I didn't get the plugin functioning,
but I was able to send the right API requests
- Also, their openapi file was invalid. The "servers" attribute is
misindented
- [Google ChatGPT
plugin](https://github.com/Sogody/google-chatgpt-plugin)
- [Chat TODO plugin](https://github.com/lencx/chat-todo-plugin)
- This openapi file is also invalid. I checked with an online validator.
I had to remove"required" from the referenced request objects'
properties:
https://github.com/lencx/chat-todo-plugin/blob/main/openapi.yaml#L85

Then I used this python file to test the examples:

```python
import asyncio
import logging

import semantic_kernel as sk
from semantic_kernel import ContextVariables, Kernel
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion
from semantic_kernel.connectors.openapi.sk_openapi import register_openapi_skill

# Example usage
chatgpt_retrieval_plugin = {
    "openapi": # location of the plugin's openapi.yaml file,
    "payload": {
        "queries": [
            {
                "query": "string",
                "filter": {
                    "document_id": "string",
                    "source": "email",
                    "source_id": "string",
                    "author": "string",
                    "start_date": "string",
                    "end_date": "string",
                },
                "top_k": 3,
            }
        ]
    },
    "operation_id": "query_query_post",
}

sk_python_flask = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"skill_name": "FunSkill", "function_name": "Joke"},
    "payload": {"input": "dinosaurs"},
    "operation_id": "executeFunction",
}
google_chatgpt_plugin = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "query_params": {"q": "dinosaurs"},
    "operation_id": "searchGet",
}

todo_plugin_add = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo": "finish this"},
    "operation_id": "addTodo",
}

todo_plugin_get = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "operation_id": "getTodos",
}

todo_plugin_delete = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo_idx": 0},
    "operation_id": "deleteTodo",
}


plugin = todo_plugin_get # set this to the plugin you want to try

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

kernel = Kernel(log=logger)
deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel.add_text_completion_service(
    "dv", AzureTextCompletion(deployment, endpoint, api_key)
)

skill = register_openapi_skill(
    kernel=kernel, skill_name="test", openapi_document=plugin["openapi"]
)
context_variables = ContextVariables(variables=plugin)
result = asyncio.run(
    skill[plugin["operation_id"]].invoke_async(variables=context_variables)
)
print(result)
```

### Contribution Checklist

<!-- Before submitting this PR, please make sure: -->

- [ ] The code builds clean without any errors or warnings
- [ ] The PR follows the [SK Contribution
Guidelines](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
and the [pre-submission formatting
script](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md#development-scripts)
raises no violations
- [ ] All unit tests pass, and I have added new tests where possible
- [ ] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <abharris@microsoft.com>

---
## [orjb1/crawl](https://github.com/orjb1/crawl)@[1880023187...](https://github.com/orjb1/crawl/commit/18800231877e12caceb48c2f929f842d55aac934)
#### Wednesday 2023-08-09 20:09:42 by Nicholas Feinberg

Tweak forms

This change is intended to allow more opportunities for players to shift
into or out of a 'transmuter' playstyle, to improve the UI of forms, and to
improve some miscellaneous issues, e.g. Lichform being useless in 3-rune games.
For more context, see https://github.com/crawl/crawl/wiki/Transmutations-Reform.

Throughout, balance is a very rough sketch. I expect many things will need to
be buffed, others will need to be nerfed, and some will need to be replaced
entirely. This is a grand experiment, not a final state.

Talismans
---------

The largest change is that forms are no longer entered via spells. Instead,
special items called 'talismans' must be found and evoked. Once entered,
these 'talisman forms' last indefinitely.

Further notes on talismans:
- Talismans scale only on Shapeshifting skill (more on this later). They
  do not care about Int, Spellcasting, other spell schools, wizardry, or
  encumbrance. (That is, they aren't spells.)
- Talisman forms have a 'minimum skill'. Below that skill, entering the
  talisman form will reduce the user's maximum HP (while in the form).
  This is intended to roughly mimic the inability to effectively cast
  spells at low skills/high fail% - it provides a space in which an 'early'
  form can be better than a 'later' one, even if you've found both.
- Talisman forms have a 'maximum skill'. Above that skill, no further
  scaling applies. This is intended to roughly mimic max spellpower - it
  makes it more obvious that later-game forms will end up outscaling
  earlier ones.
- It takes 5 turns to enter or leave a talisman form, exactly as with
  armour or amulets. Use of a talisman form is intended to be a strategic
  decision, again like wearing armour, rather than something swapped in
  each fight.
- Talismans don't need to be held after they're used. You can evoke them
  from the floor and leave them there. This avoids inventory pressure.
- Talismans can be used with Sacrifice Artifice, since they don't use Evo.
- Zin instantly excommunicates users of a talisman. Take that, nerds!
- Trog is A-OK with talismans, just as with wands, magic swords, etc.

Art for talismans is pending.

Skills
------

Transmutations skill has been split in two. Talismans use a new skill,
Shapeshifting, and remaining Transmutations spells (of which there are
still nine, more than one other school!) continue to use Transmutations
skill. There was very little synergy or overlap between forms and Tmut
spells, and this makes it easier to make skilling decisions. Some argue
that Transmutations should be abolished entirely and its spells punted
into other schools; we'll see.

Shapeshifting aptitudes look broadly like Transmutations aptitudes,
with a -2 penalty applied so that forms are costly enough now that
they're all "single-school" and don't require Int. (That is, Humans
have a Shapeshifting apt of -2, etc.) A few species have had their
apts adjusted to account for the new role of Shapeshifting, but more
could be done here.

Background
----------

The Transmuter background has been replaced with a Shapeshifter, who
starts with a beast talisman and no spells. Their stats have been
adjusted accordingly.

Forms
-----

The following forms exist:

*Beast*: This is the starting form for the Shapeshifter background. It
melds all aux armours in exchange for a Slaying bonus (ala Wereblood) -
+2 at 0 skill, +8 at 13 skill (max).

This is intended to provide a bonus which is compelling early game (when no
or few aux armours have been found) but more tenuous later, especially for
non-transmuters. It's also intended to provide a bridge between Tmut and
weapon use, since a transmuter who finds a great weapon can switch from UC
to that weapon without giving up their form and Tmut training.

Beast form allows use of body armour so that it can present a reasonable
slay-for-AC tradeoff without becoming overly strong for 'dex-based' characters,
who wouldn't mind losing body armour nearly as much.

*Anaconda*: This is a tier 2 form. Anaconda form turns you into a giant
anaconda. All your items meld, you can constrict, you get some AC and an HP
bonus...

This is intended to replace Ice Form, a form to help transmuters transition
into the mid-game. The rF- of Ice Form is less appropriate for early-game
characters who can no longer switch between forms, and Ice Form is not
evocative - no one gets Ice Beasts. On the other hand, turning into a snake...
everyone gets that. That's the dream. Limbs are for dorks. Ssssss

*Maw*: This is a tier 2 form. Maw form melds the body slot, transforming it
into a giant mouth, ala the Brazilian Mapinguari. The maw provides an aux
attack with damage that scales on Shapeshifting skill. It also has the old
Hydra form devour-on-kill-for-hp gimmick, since everyone loved that.

This is intended to be a way that Shapeshifters can transition into the mid-game,
especially transmuters who use weapons. It's probably a bit too strong for
quick blade users at present - perhaps I'll give it +str -dex, or something.
(It may also just be too strong in general - numbers are WIP!)

*Blade*: This is a tier 2 form. It's blade hands. To compensate for it
being easier to enter, its UC damage has gone down slightly (22 -> 18).

It also now gives a deformed body-like AC penalty based on base body armour AC,
scaling from a 100% penalty at min Shapeshifting skill to 0% at max skill.
(That is, at min skill, +2 plate armour will just give you +2 AC, plus whatever
you get from Armour skill.) This is intended to model the dynamic of old Blade
Hands - pure glass cannon when you can only cast it in robes, later on more
usable in actual armour. Your body is deformed because there are blades inside.
Aaiiii!

This is intended to be another way that Shapeshifters can transition into the
mid-game.

*Statue*: This is a tier 3 form. It's statue form. Intended to be a way
for transmuters to head into late-game while still being able to use weapons,
if desired. Might need to be a bit stronger for weapon users.

*Dragon*: This is a tier 3 form. It's dragon form. AC and UC damage now
scale slightly with Tmut skill. Intended to be a way for transmuters to
head into late-game. Possible this should be tier 4 and Storm should be tier
3 - dragons are cool! Dragons should be the best!

*Storm*: This is a tier 4 form. It's storm form. Intended for players who
want to dump ludicrous amount of skill XP into tmut. Top end has been
adjusted somewhat downward.

*Death*: This is a tier 4 form. Replacing Necromutation/Lich Form, Death
Form makes you dead (no drinking potions, holy wrath/dispel undead vuln,
rC, rTorm, rPois, etc) and also gives you an assortment of spicy powers.
On hit (with melee/UC), victims get slowed, weakened, and heavily drained.
There's also a new active, Siphon Essence, which costs 20 (!) MP, halves
the HP of all enemies in radius 2, and heals you based on damage dealt and
Tmut skill. (That works on all non-MH_NONLIVING enemies, as do the debuffs.)

It no longer provides innate AC or Will, nor does it give a necro enhancer.
Its UC damage is now significantly higher, comparable to blade hands,
though still much lower than Statue, Dragon or Storm.

This is intended to be a way for players who want to spend huge skill XP
on tmut to do so, including those who use tmuts + weapons. It's intended
to feel a bit different from other forms while still being competitive in
melee. Other forms have huge base damage - Death Form has lower damage but
very strong debuffs. Other forms have AC (Statue), HP (Dragon) or EV (Storm) -
Death Form gives Siphon Essence as a very powerful survival tool.

Other Notes
-----------

Various books have been merged and consolidated to make up for the
removal of eight spells. It *might* make sense to drop the book generation
rate slightly, but I haven't done this yet.

Some uniques now spawn with talismans. More could be done with this, e.g.
placing talismans of death in Crypt.

Later changes
-------------

Talisman acquirement is a must. TODO.

In the future, artefact talismans (i.e. randarts) could be interesting -
to provide more excitement for rare finds. The randarts would have
the usual panoply of properties (rF+, Dex-2, etc), which would apply
while the player was in the relevant form.

It'd be fun to add more form types, e.g. ones that work well for
'casters'.

Might be interesting to have talismans start unidentified (like staves),
for a frisson of excitement in gauntlets etc.

Possibly Wanderers should get a chance to start with beast talisman?

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[66b8748091...](https://github.com/tgstation/tgstation/commit/66b87480915434f1184ac257c9ed0f1f3fe87c58)
#### Wednesday 2023-08-09 20:28:49 by carlarctg

Adds Summon Simians & Buffs/QoLs Mutate (#77196)

## About The Pull Request

Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

Added further support for nonhuman robed casting: Monkeys, cyborgs, and
drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

Made monkeys able to wield things again.

Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.

Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Improved some monkey AI code.

## Why It's Good For The Game

> Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

It's criminal we don't have a monky spell, and this is a really fun spin
on it. Total chaos, but total monky chaos. It's surprisingly strong,
but! it can very well backfire if you stay near the angry monkeys too
long and your protection fades away. Unless you become a monkey
yourself!!

> Wizard Mutate spell works on non-human races. 

This spell is great but it's hampered by the mutation's human
requirement, which is reasonable in normal gameplay. Wizards don't need
to care about that, and the human restriction hinders a lot of possible
gimmicks, so off it goes. Also, wizard hulk does't cause chunky fingers
for similar reasons

> Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Don't really caer about the damage so much, this is more so that it has
effects such as on-hit visuals. Can lower the damage if required, but
honestly anything that competes against troll mjolnir is good.

> Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

SS13 is known for 'The Dev Team Thinks of Everything' and I believe this
is a sorely lacking part of this or something. It's funny.
I want to see a monkey wizard.

> Made monkeys able to wield things again.

I really don't know why this was a thing and it was breaking my axe and
spear wielding primal monkeys. Like, why?

## Changelog

:cl:
add: Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.
balance: Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.
balance: Made Laser eyes projectiles a subtype of actual lasers, which
has various properties such as on-hit effects and upping the damage to
30.
add: Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.
balance: Made monkeys able to wield two-handed things again.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [enjarai/do-a-barrel-roll](https://github.com/enjarai/do-a-barrel-roll)@[727c0d3a79...](https://github.com/enjarai/do-a-barrel-roll/commit/727c0d3a794cdf2879a90e9991f151a500f23cf9)
#### Wednesday 2023-08-09 20:55:22 by enjarai

Holy fucking shit I clearly had nothing better to do today

---
## [bledoux2002/Fallout-2d20-Character-Creator](https://github.com/bledoux2002/Fallout-2d20-Character-Creator)@[612a93ff1b...](https://github.com/bledoux2002/Fallout-2d20-Character-Creator/commit/612a93ff1bfdd26dad9c7caacecd3d3584ed712c)
#### Wednesday 2023-08-09 21:06:26 by Benjamin Ledoux

HOLY MOLY THATS A LOT

-created backup folder for data files
-updated README roadmap and added file structure diagram (kinda)
-moved some code around
-reorganized code structure a few times (might actually be back to where we started for some stuff. oh well)
-fixed printDelay() global optional parameter bug
-now using try and except!
-commented out uploadChar(), as it likely wont be neceessary for local terminal release due to manual nature of file movement
-optimized printDelay() calls with optional arguments (caused a bug i mentioned i fixed already, aren't you paying attention?)
-genChar() now has error handling (i think?)
-listChar implemented w/ error handling (i think?)
-fixed settings bugs with text speed change, global var issues and, you guessed it,  ERROR HANDLING (ifi did it right)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[87f707dfa8...](https://github.com/tgstation/tgstation/commit/87f707dfa8dd901310f72585c6f701035bc653ee)
#### Wednesday 2023-08-09 21:07:16 by DeerJesus

Adds the Storage Implanter to the spy kit. (#77452)

## About The Pull Request

Adds the storage implanter to the spy kit to make it decent.

## Why It's Good For The Game
This PR hopes to bring Spy at least a little more in-line with the rest
of the syndie-kit specials, so it doesn’t feel like a complete dud to
get.

Spy absolutely sucks as a syndie-kit and getting it is basically
throwing away 20 TC. Not all of them should be equally powerful but all
of them should be at least more satisfying to get. Spy is so bad that
it’s listed in the official wiki as ‘honestly not that good’. It’s also
_barely_ even above 25 telecrystals as the switchblade is a black market
uplink item, not a syndicate uplink item, and not even that good of an
item at that! And the chameleon kit inside isn’t even a full chameleon
kit! Pitiful. Compare it to stealth right below it which totals to _36_
telecrystals.

Adding a storage implant adds a relatively useful item to the kit that
still fits with the entire theme of ‘stealth and deception’, as you can
be searched without having anything on you. To be stealthy, and deceive
people. Like you should. Given the fact that searches are quite common.
It doesn’t make it TOO overpowered as the rest of the gear is still ‘not
that great’.


## Changelog

:cl:
balance: added the storage implanter to the syndie-kit tactical 'spy'
kit to make it decent.
/:cl:

Co-authored-by: oilysnake <63020759+oilysnake@users.noreply.github.com>

---
## [hecksadecimal/Skyrat-tg](https://github.com/hecksadecimal/Skyrat-tg)@[35e28a5b4a...](https://github.com/hecksadecimal/Skyrat-tg/commit/35e28a5b4a679c8e07e450287cb77cb72c8b5056)
#### Wednesday 2023-08-09 21:08:12 by SkyratBot

[MIRROR] Goliath basic mob [MDB IGNORE] (#22412)

* Goliath basic mob (#76754)

## About The Pull Request

Converts Goliaths to the basic mob framework and gives them some new
moves because I can't leave things well enough alone.
I am planning on touching all the lavaland fauna and then maybe even the
icebox ones if I haven't got bored. The Golaith is the first because it
is iconic.

https://www.youtube.com/watch?v=JNcKvMwT4-Q
Here's me getting killed by one as a demonstration. Despite my poor
performance I would contend that they aren't a _lot_ more dangerous, but
they are a little more dangerous.

The chief difference here is that they have two new attacks which they
will only use in response to being attacked.
If fired at from range, they will target the attacker with a line of
tentacles (it doesn't track you, so is easily sidestepped).
If attacked in melee, they will surround _themselves_ with tentacles, on
a longer cooldown.

Something else you may notice in this video: I discovered that basic
mobs are actually _too smart_ to be Lavaland fauna.
Typically (unlike their old form) a mob on our new AI system is smart
enough to attack someone _the moment they come into range_ rather than
only checking on predictable ticks, which would make using the Crusher
an essentially unviable prospect.
To counteract this, Goliaths now have a delayed attack component which
gives you a visual warning and short duration to get out of range before
they swing at you. I will probably put this on all mining fauna that get
reworked, it wouldn't be a terrible thing to put on other mobs to be
honest.

Other changes: The goliath stun is now a status effect with _buckles_
you to the tentacle as if grabbed, as well as its previous effects.
While this seems purely worse, any nearby helpers can now help-click on
you to instantly remove the debuff.
Experiencing the effect of a Lobstrosity Rush Gland makes you immune to
being grabbed by tentacles and an implanted one will automatically
trigger and free you if you are hit, and the explosive effect of
Brimdust also causes the tentacle to retract (although you'd need to
take damage for this to happen). Using the tools of the land, you can
make these creatures less threatening.

The ability for a Goliath to chain-apply the ability has now also been
reduced, it won't refresh its duration if you are hit when already
buckled.

When not occupied hounding miners, Goliaths will intermittently dig up
the asteroid sand and eat any worms that this produces.
I also made some new sprites for riding a Goliath because they've been
broken since the Lavaland mob update and also kind of were ugly before
then anyway:

![image](https://github.com/tgstation/tgstation/assets/7483112/90580403-d82f-4c29-b3e1-6c462e01edda)

Other code changes:
- I made an element which only lets an attached object move every x
seconds. This is because Goliaths are far too slow to use the speed
system (the glide just looks bugged as hell) but one thing I am invested
in when converting these is to make sure that they share the same
behaviour when player or AI controlled. This is disabled while you're
riding them because it was interminably slow.
- The Goliath tentacle trail uses a supertype object now shared with the
Meteor Heart which did something kind of similar.

## Why It's Good For The Game

It begins the process of moving one of our larger subsets of NPCs onto
the newer framework for NPC behaviour.
It adds a little bit more life to an iconic but slightly uninteresting
foe which mostly just walked at you slowly.
This PR contains a few components I expect to apply more widely to other
mobs in the future.

## Changelog

:cl:
refactor: Goliaths now use the Basic Mob framework, please report any
unusual behaviour.
add: Goliaths learned a couple of new attacks which they will use in
self-defence.
balance: Help-clicking a miner grabbed by Goliath tentacles will
immediately free them, as will the effect of several items you can
scavenge from around Lavaland.
image: New sprites for the Goliath saddle.
/:cl:

* Goliath basic mob

* Update ash_rituals.dm

* fixes icon diff

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: Pinta <68373373+softcerv@users.noreply.github.com>
Co-authored-by: Giz <vinylspiders@gmail.com>

---
## [Iqra-Fathima/BharatIntern-Task1](https://github.com/Iqra-Fathima/BharatIntern-Task1)@[b738e16c0a...](https://github.com/Iqra-Fathima/BharatIntern-Task1/commit/b738e16c0ae829e94ef19f42904d75717b1c5e3c)
#### Wednesday 2023-08-09 22:03:19 by Iqra-Fathima

Add files via upload

Exciting Insights from My Task 1 Employee Attrition Analysis as part of internship at Bharat Intern

I delved into a comprehensive analysis of employee attrition, shedding light on intriguing trends based on the data taken from Kaggle Here's a snapshot of my key findings:

Attrition by Gender: The maximum attrition is from the male employees, out of total attrition count being 237 we found that 150 is the attrition of male employees.

Job Satisfaction: Our data revealed that male employees tend to exhibit higher job satisfaction compared to their female counterparts.

Attrition by Department: Drilling down into departmental attrition rates, a pattern emerged. The research department experienced the highest attrition, followed by sales and HR departments.

Age and Attrition:
We can observe the prevalence of attrition among employees aged 27-35. This calls for a closer examination of factors influencing career choices and progression within this age bracket.

Marital Status Matters: Strikingly, the data highlighted a correlation between marital status and attrition, with singles exhibiting higher attrition rates. Could this be attributed to a lack of work-life balance or other factors? Addressing the unique needs of single employees might contribute to improved retention outcomes.

Myth Busted: Interestingly, my analysis uncovered a fact about popular belief that "employees leave managers, not companies." I can see that employees who had spent a shorter time with the company exhibited higher attrition, then the employees who had a longer tenure under the same manager.

This insight underscores the vital significance of effective management and team cohesion, suggesting that fostering enduring relationships with managers could play a pivotal role in retaining valued team members.

---
## [Skies-Of-Blue/Shiptest](https://github.com/Skies-Of-Blue/Shiptest)@[ee4021c507...](https://github.com/Skies-Of-Blue/Shiptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Wednesday 2023-08-09 22:19:24 by Imaginos16

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
## [rc2dev/dwm](https://github.com/rc2dev/dwm)@[67d76bdc68...](https://github.com/rc2dev/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2023-08-09 22:19:37 by Chris Down

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
## [oofienoob/potatositetesting](https://github.com/oofienoob/potatositetesting)@[564c0dfe43...](https://github.com/oofienoob/potatositetesting/commit/564c0dfe43c0072aea136f9c59052d0616c73e1e)
#### Wednesday 2023-08-09 23:54:29 by oofienoob

okay after killing myself i found out that shadow the hedgehog is a bitch ass motherfucker he pissed on my wife and also anyways have custom cursor lmao xd

---

