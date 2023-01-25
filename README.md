## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-24](docs/good-messages/2023/2023-01-24.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,336,183 were push events containing 3,491,543 commit messages that amount to 263,000,627 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [CERT-Polska/mquery](https://github.com/CERT-Polska/mquery)@[e832f51fb3...](https://github.com/CERT-Polska/mquery/commit/e832f51fb3e9475ef959d92e7c0944ecf1598451)
#### Tuesday 2023-01-24 00:06:06 by msm-code

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[67bf270e36...](https://github.com/git-for-windows/git/commit/67bf270e361e5bb54e0e60064fed299f91fb8b5a)
#### Tuesday 2023-01-24 00:17:02 by Johannes Schindelin

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
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[0fbe798920...](https://github.com/willior/Action_RPG_1/commit/0fbe7989203a17fd319d2510372853044cb595e6)
#### Tuesday 2023-01-24 00:20:49 by willior

layer interaction issue

we can program logic so that Player interaction ignores interacting with objects that aren't on the same layer. however, this doesn't work for objects that are supposed to be interactable from 2 different layers, such as ladders. a conundrum.
right now, what we do is check area.get_parent().layer != layer; aka, compare the area's body's layer with our own.
an extreeemely hacky way of fixing this would be to give the TopInteractZone & BottomInteractZones of the Ladder different parents who each have their own layer property. but that's stupid...
another way of fixing this would be to add all the layers from which an object should be interactable to an array, and then iterate through them. this would allow for expanded functionality, too, since theoretically we could make a ladder/transition from layer 1 to layer 3 (right now, ladders are hard-coded to transition between 1 level at a time, aka go from layer to layer+1). the issue with that is the z-index/ysorting. if an object is on layer 0, it will draw behind objects on layer 2. there isn't an elegant way of drawing the player in front of a ladder on layer 0 that's also supposed to draw in front of a TileMap on layer 2, UNLESS the ladder was composed of TWO sprites - one for each half - in which case, we could set the z_index individually for each half of the ladder. but i'm not going to do that.
for now, let's revert the complexity and try to get 1 layer ladder transitions and interactions working in a simple & elegant manner.
there is another possibility, which is instead of checking/comparing layers, we could check a "ignore_interaction_layer" flag, and if it's true, it supercedes ignoring InteractObjects on different layers. man i just don't know.
so what we've done is add 2 variables to the ladder: to_layer, and to_layer_override.
to_layer = layer+1, and to_layer_override is an exported integer.
if to_layer_override > 0, then we set to_layer to to_layer_override; otherwise, to_layer remains layer+1. this allows skipping layer 1. place the ladder on the layer you want the bottom exit to go, and then input a "to_layer_override" in the exported variable, eg., 2. theoretically you can also have ladders that don't change the player's layer. simply set to_layer_override to the layer the ladder is already on, and it should work. and it does, like a makeshift bridge of sorts.
one issue is that ladders that aren't currently being climbed still process and scan for bodies in their ExitAreas. so if two ladders' ExitAreas overlap, it will run the exit code for one of the ladders, regardless of which one you try to climb. in other words, if a ladder's upper exit exists in the same location as another ladder's lower exit, the game can process climbing onto the upper ladder as EXITING the lower ladder thus cancelling the climb state.
i'm trying to think of the best solution to this. one way to do it would be to simply disable the ladders' _process() function if nobody's on them. another would be to disable the collisionshapes. i'm concerned for multiplayer, though, because if one player is on a lower ladder, say, and player2 is on an upper ladder, and their exits meet, then the lower ladder would process player2 as exiting it, making the upper ladder unclimbable for player2 if the lower ladder had player1 climbing it.
probably the best way to handle this - but it'd be slightly complex - would be for the ladders themselves to actually keep track of player(s) climbing them, and have their exits process only bodies that they've determined to be climbing them, and not bodies on other ladders. fuck.
also fixed an issue involving examining InteractObjects, which include Ladders & IngredientPickups. the examine dialog box was no longer popping up. this was confusing and still is. for InteractObjects, we declare multiple variables having to do with dialog. they include:

examine_script
object_name
examine_file

the logic of IngredientPickups is as follows:

it has its object_name set, eg. "Water".
we then check the IngredientDatabase for "Water", and return the ingredient when found.
we then set examine_script = ingredient.description.

then, when examine() is called on the IngredientPickup, we call:

Global.create_dialog_box(examine_script, examine_file, examine_index)

first, we check if external_file != null, and set dialogBox.external_file to external_file if it is not null. otherwise, we set dialogBox.dialog_script to [dialog_script]. then we add the DialogBox.
dialogBox.external_file is initialized as an empty String (''). on dialogBox._ready(), we check if external_file != '', and load the file if it isn't, and set it to dialog_script.
then we check if dialog_script == null. this is where the issue was occurring; the dialogBox was always interpreting dialog_script to be null, even when the IngredientPickup had its examine_script set properly.
it turns out this was because we were initializing InteractObject.examine_file to ''.  the Global.create_dialog_box() function doesn't interpret '' as null, and so it assigned '' to dialogBox.external_file INSTEAD of assigning dialogBox.dialog_script properly. then, the dialogBox can't find the file, so dialog_script gets set to null, making it delete itself before anything happens.
this is extremely messy. there is a better way to do this. this was particularly dangerous because there are no errors in the code; it was simply due to poor logic.
one thing i don't understand, though... let's see if we can step through the logic....

InteractObject.examine() is called, which calls Global.create_dialog_box(examine_script, examine_file, examine_index).
examine_script is set properly;
examine_file = '';
examine_index = 0.

in the function, we check if external_file != null, which it wasn't; it was ''. and so we assigned dialogBox.external_file to ''.
then, on dialogBox._ready(), we check if external_file != ''... but it was. oh, i see now. the Global function executed its code properly, because it interpreted a non-null examine_script (''), which overrode assigning the dialogBox's dialog_script variable. then, on dialogBox._ready(), neither the external_file check nor the dialog_script check pass (because external_file == '' && dialog_script == null). because of this, the dialogBox got deleted instantly. dangerous code here.
christ. anyways, interaction is now prevented between layers. fantastic. on player._on_InteractHitbox_area_entered(area), we check:

if area.get_parent().layer != layer and area.get_parent().get("to_layer") != layer:

this returns out of the function if there is both a layer mismatch between area.get_parent() layer & player.layer, AND if the area's parent has a "to_layer" property that ALSO doesn't match player.layer (if area.get_parent().get("to_layer") returns null, ie. the interactable body doesn't have a to_layer property, it also counts as a mismatch).
fuck.

---
## [trunk-io/plugins](https://github.com/trunk-io/plugins)@[1a0b7ffe7f...](https://github.com/trunk-io/plugins/commit/1a0b7ffe7f5a1b34b5af6f6cf368041ae349ed94)
#### Tuesday 2023-01-24 00:25:26 by Tyler Jang

Improve TaskFailure debug experience (#96)

The failure `detailPath` was formerly omitted, but passing in asymmetric
wrappers to `toMatchSpecificSnapshot` provides an alternative that
prints much more detailed failure information.

### Background
Improves CI and local experience of debugging when failures occur. This
has been a long time coming. Previous [failure
runs](https://github.com/trunk-io/plugins/actions/runs/3977200383/jobs/6818150578)
were painfully difficult to debug, particularly if they couldn't be
reproduced locally, and would often involve `cd`-ing into autodeleted
directories. Now, failure detail information is printed directly through
the use of asymmetric property matchers (see screenshot below).

![Screenshot 2023-01-21 at 11 39 16
PM](https://user-images.githubusercontent.com/42743566/213905613-a7f8e441-9017-4d81-b4eb-5a874c52d37d.png)

### Alternatives (that I considered and attempted)
1. Using custom serializers.
[jest-specific-snapshot](https://github.com/igor-dv/jest-specific-snapshot)
supports this, and there are decent
[documentation](https://jestjs.io/docs/expect#expectaddsnapshotserializerserializer)
and
[guides](https://medium.com/@luisvieira_gmr/jest-snapshot-serializers-6a96f5c362a1)
about how to approach this. However, whatever serialized output is
created is written to the snapshot file itself. This means that we would
have to save all of the detailPath contents (which presents numerous
problems, including nondeterministic paths), or none at all.
2. Ditching snapshots completely and using a stricter JSON approach.
This would be closer to the original approach, but it flies in the face
of recent work, including numerous QoL improvements, so I did not
thoroughly consider this option.
3. Using a custom asymmetric property matcher. There is also decent
documentation on [property
matchers](https://jestjs.io/docs/snapshot-testing#property-matchers) and
[guides](https://redd.one/blog/practical-guide-to-custom-jest-matchers).
There are a couple key problems, however. It is difficult or impossible
to write the actual contents of errors to snapshot files--they are
instead replaced with matcher names (see screenshot below). They are
also somewhat inflexible, particularly when used with
`jest-specific-snapshot`.
4. Wrapping expect in a try and rethrow. This
[suggestion](https://stackoverflow.com/a/55097584) was made, and it
would be a bit more general for the purposes of providing debug
information, but it would require significant custom code in order to
determine what the desired message to print would be. TaskFailures are
the primary focus here.
5. Using built-in asymmetric property matchers. The final approach that
I took is similar to option 3, but adds a bit more custom hacky code in
order to ensure that as much useful information is written to the
snapshot as possible. I use property matchers mapped to each individual
taskFailure, and I apply them conditionally based on the test state and
whether or not I have computed that failure to be present in the
snapshot (see comments in `tests/utils/index.ts`). The only operational
downside is that replacing existing snapshots with failure content
becomes a bit more difficult, but not significantly.

### Follow-up Work
- I may consider also including debug information such as the
trunkVersion and the linterVersion. If necessary, these wrappers can
also be expanded to include other useful information through additional
asymmetric matchers (custom or built-in).
- I may also integrate
[retries](https://www.npmjs.com/package/jest-retries) if flaky failures
are determined to be due to network issues after this PR brings out new
insights.

Alternative 3
![Screenshot 2023-01-21 at 11 45 52
PM](https://user-images.githubusercontent.com/42743566/213905770-d8737589-cb6b-4700-89de-7d112574b5c1.png)

Co-authored-by: Chris Clearwater <chris@trunk.io>

---
## [Teabone3/GameGuruRepo](https://github.com/Teabone3/GameGuruRepo)@[27d7493c1c...](https://github.com/Teabone3/GameGuruRepo/commit/27d7493c1cab486fb078210f1207ff347e6d5169)
#### Tuesday 2023-01-24 00:28:12 by Teabone

Fixes Dying Effects (Heartbeat + Red Screen)

Multiple Fixes and Changes to Player's Dying Effect trigger:

Fixes issue causing dying effect when the player was barely hurt:

Previously if the player was ever hurt, even by 1 point of damage, the player would act as if he was dying. The screen would go red and a heart-beat sound would play repeatedly until the player finds a health item or regenerates health. This used to occur instantly because the player's main script was set to cause this effect whenever the player's health was lower than 100. So for example if your health was 99, your game would assume the player is dying and cause a heart beat sound to play and flash the screen red. This change sets to check if player's health is less than 50% of its set maximum in the editor. Meaning less than 50/100 or less than 150/300 etc for examples.

Fixes 100 points being assumed as the maximum health for all games:

The original player script was set to assume the player's maximum health would always be 100 points. It was not using a percentage system either. So even if you set the players health to 1000 (for example) if you get injured the dying effect would only play if the players health was 99 out of 1000. This changes the solid "100" value to "g_gameloop_StartHealth".

In short, the "annoying" heartbeat and red-screen flashes will only ever occur if the player's health is drastically lower than its maximum meaning you will hear it only when you are actually dying or majorly hurt. A highly requested change in the community over the years.

We could in the future perhaps add an user option in the start marker to change what percentage the health must be lower than, to play the dying effects. For example replacing the 2 with a variable that can be controlled in the start marker in editor. So you can control how much to divide the maximum health by to determine percentage.

 g_PlayerHealth >= (g_gameloop_StartHealth/2) )

* Please note this change does not remove the player blood decals on screen, that occur when the player is hurt. It only changes when to run the dying/near death effects (heart-beat and red transparency on the overall screen).

---
## [13190-2022-23/13190PowerPlay](https://github.com/13190-2022-23/13190PowerPlay)@[c59e5c1fc3...](https://github.com/13190-2022-23/13190PowerPlay/commit/c59e5c1fc3a26c9c28921ed7ae05db3ec9b1603d)
#### Tuesday 2023-01-24 00:28:32 by RichardkimAXel

started work on 1+0 auto to add to the FinalParkAuto
THE ONE PIEEEEECEEEE!!!!!!!!
THE ONE PIECE IS REALLLL!!!!!!!!!!!

Can we get much higher? So high
Oh, oh, oh
Oh, oh, oh, oh
Oh, oh
Yeah, yeah, yeah, yeah
I fantasized 'bout this back in Chicago
Mercy, mercy me, that Murcielago
That's me, the first year that I blow
How you say broke in Spanish? Me, no hablo
Me drown sorrow in that Diablo
Me found bravery in my bravado
DJs need to listen to the models
"You ain't got no fuckin' Yeezy in your Serato?"
Stupid, but what the hell do I know?
I'm just a Chi-town nigga with a Nas flow
And my chick in that new Phoebe Philo
So much head, I woke up to Sleepy Hollow
Can we get much higher?
Oh, oh, oh
Oh, oh, oh, oh
Oh, oh
Look like a fat booty Céline Dion
Sex is on fire, I'm the King of Leon-a Lewis
Beyond the truest, hey, teacher, teacher
Tell me, how do you respond to students?
And refresh the page and restart the memory?
Respark the soul and rebuild the energy?
We stopped the ignorance, we killed the enemies
Sorry for the night demons still visit me
The plan was to drink until the pain over
But what's worse, the pain or the hangover?
Fresh air, rollin' down the window
Too many Urkels on your team, that's why your wins low
Don't make me pull the toys out, huh
Don't make me pull the toys
And fire up the engines, huh
And then they make noise
Can we get much higher? So high
Oh, oh, oh
Oh, oh, oh, oh
Oh, oh
At the mall, there was a séance
Just kids, no parents
Then the sky filled with herons
(I saw the devil) in a Chrysler LeBaron
And the hell, it wouldn't spare us
And the fires did declare us
But after that, took pills, kissed an heiress
And woke up back in Paris

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[2327e445d2...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/2327e445d26e20ab410a5f97109d2088c00681ce)
#### Tuesday 2023-01-24 00:29:06 by SkyratBot

[MIRROR] Gatfruit will no longer drop from ice portals. [MDB IGNORE] (#18202)

* Gatfruit will no longer drop from ice portals. (#72048)

## About The Pull Request

For some god-forsaken reason, somebody decided that ice portals should
be able to drop one of the most disruptive items in the game. This PR
amends this by removing it from the drop pool.

## Why It's Good For The Game

In 2013 gatfruit was introduced in the following PR #2000 . This was
almost a decade ago at this point, repeatedly through the PR the creator
states his belief that this item should only ever be obtainable through
admin intervention due to its ridiculous capabilities. At the time
everyone in the PR agreed it was a reasonable item to add **as it was
unobtainable without admin intervention**. Over the years, it has crept
its way to become more prevalent and openly obtainable, the most
offensive of these options is the ice moon portal. As is, there is a 1
in 28 chance of obtaining the seeds, this sounds pretty inoffensive
right? That's just 3.44% probability. Now, let us search the instances
of the portal that spawns this.

![image](https://user-images.githubusercontent.com/16896032/208220173-bbefe604-0885-44a5-9add-b5f0c62067cc.png)

That is a big number, a lot of chances to get that seed packet and other
gamer looters. Now, let's take a look at the probability of being able
to get these seeds, assuming you wipe out all of the portals.

![image](https://user-images.githubusercontent.com/16896032/208220460-3f59a2ac-d936-4f3a-aa14-9c637af6a9d7.png)

92.8% chance to be able to get these seeds each shift if you focus
entirely on gaming the portals. That's a pretty insane probability of
being able to obtain the gatfruit seeds.

While I dislike people who sprint to the seed vault, there is at least
the possibility of a pod person telling them to fuck off when they
demand their _free_ gamer seed. There is also the fact that the ruin
isn't a guaranteed spawn every shift.

## Changelog

:cl:
balance: Gatfruit seeds will no longer drop from ice portals.
/:cl:

* Gatfruit will no longer drop from ice portals.

Co-authored-by: carshalash <carshalash@gmail.com>

---
## [sailfishos-mirror/git](https://github.com/sailfishos-mirror/git)@[69bbbe484b...](https://github.com/sailfishos-mirror/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Tuesday 2023-01-24 01:04:04 by Jeff King

hash-object: use fsck for object checks

Since c879daa237 (Make hash-object more robust against malformed
objects, 2011-02-05), we've done some rudimentary checks against objects
we're about to write by running them through our usual parsers for
trees, commits, and tags.

These parsers catch some problems, but they are not nearly as careful as
the fsck functions (which make sense; the parsers are designed to be
fast and forgiving, bailing only when the input is unintelligible). We
are better off doing the more thorough fsck checks when writing objects.
Doing so at write time is much better than writing garbage only to find
out later (after building more history atop it!) that fsck complains
about it, or hosts with transfer.fsckObjects reject it.

This is obviously going to be a user-visible behavior change, and the
test changes earlier in this series show the scope of the impact. But
I'd argue that this is OK:

  - the documentation for hash-object is already vague about which
    checks we might do, saying that --literally will allow "any
    garbage[...] which might not otherwise pass standard object parsing
    or git-fsck checks". So we are already covered under the documented
    behavior.

  - users don't generally run hash-object anyway. There are a lot of
    spots in the tests that needed to be updated because creating
    garbage objects is something that Git's tests disproportionately do.

  - it's hard to imagine anyone thinking the new behavior is worse. Any
    object we reject would be a potential problem down the road for the
    user. And if they really want to create garbage, --literally is
    already the escape hatch they need.

Note that the change here is actually in index_mem(), which handles the
HASH_FORMAT_CHECK flag passed by hash-object. That flag is also used by
"git-replace --edit" to sanity-check the result. Covering that with more
thorough checks likewise seems like a good thing.

Besides being more thorough, there are a few other bonuses:

  - we get rid of some questionable stack allocations of object structs.
    These don't seem to currently cause any problems in practice, but
    they subtly violate some of the assumptions made by the rest of the
    code (e.g., the "struct commit" we put on the stack and
    zero-initialize will not have a proper index from
    alloc_comit_index().

  - likewise, those parsed object structs are the source of some small
    memory leaks

  - the resulting messages are much better. For example:

      [before]
      $ echo 'tree 123' | git hash-object -t commit --stdin
      error: bogus commit object 0000000000000000000000000000000000000000
      fatal: corrupt commit

      [after]
      $ echo 'tree 123' | git.compile hash-object -t commit --stdin
      error: object fails fsck: badTreeSha1: invalid 'tree' line format - bad sha1
      fatal: refusing to create malformed object

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Bobthe28th/tgstation](https://github.com/Bobthe28th/tgstation)@[c3a1f21c1a...](https://github.com/Bobthe28th/tgstation/commit/c3a1f21c1afc10bd5515114e0c6117ac73c87f62)
#### Tuesday 2023-01-24 01:19:18 by MrMelbert

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
## [ozzono/scripts](https://github.com/ozzono/scripts)@[ee5fcbc52a...](https://github.com/ozzono/scripts/commit/ee5fcbc52add9c9b23cd7de5671bb531fbd112b0)
#### Tuesday 2023-01-24 02:06:09 by Hugo Virgílio

Fortune Commit: I sat laughing snidely into my notebook until they showed me a PC running
Linux. And oh! It was as though the heavens opened and God handed down a
client-side OS so beautiful, so graceful, and so elegant that a million
Microsoft developers couldn't have invented it even if they had a hundred
years and a thousand crates of Jolt cola.
		-- LAN Times

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[5c6f5439b7...](https://github.com/pytorch/pytorch/commit/5c6f5439b7e6a5e63a68b36b4cf093a00d46e8be)
#### Tuesday 2023-01-24 02:14:03 by Edward Z. Yang

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
## [team3130/Swerve_2022](https://github.com/team3130/Swerve_2022)@[7810a8a4b2...](https://github.com/team3130/Swerve_2022/commit/7810a8a4b237682379a21db209a07eb2ce851d31)
#### Tuesday 2023-01-24 02:21:03 by caleb

Fixed errors see commit desc

I added math for converting encoder readings to real life values. I also added some network table entry's for reading encoder values. Lastly I found the problem from tonight, we had outdated dependency's (god I hate gradle)

---
## [azerothcore/azerothcore-wotlk](https://github.com/azerothcore/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/azerothcore/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Tuesday 2023-01-24 02:43:11 by ICXCNIKA

fix(DB/Locale): deDE fix request items texts #02 (#14615)

Process of translation: only original sources of deDE texts by
researching multiple sources, reverse translation by searching for
related quest items/NPCs and using these names to reconstruct a proper
translation.

This fixes the terms

Coldtooth-Mine (Eisbeißermine), Doomhammer (Schicksalshammer), Fizzle
(Zischel), Fizzledowser (Rutenwünschels), Fizzlebub (Zischelbub),
Burning Blade (Brennende Klinge), Ashenvale (Eschental),
Bloodscalp/s/stamm (Blutskalpe, Blutskalpstamm),
Darkspeartrolle/Darkspears/Darkspearstamm (Dunkelspeere,
Dunkelspeertrolle, -stamm), Moonglade (Mondlichtung), Starblaze
(Sternenschauer), Shadowglen (Laubschattental), Darrowshire (Darroheim),
Booty Bay (Beutebucht), Ratchet (Ratschet), Dizzywig (Flunkerblick),
Hearthglen (Herdweiler), Chillwindspitze (Zugwindspitze), Stormrage
(Sturmgrimm), Stormpike (Sturmlanze/n), Ironforge (Eisenschmiede),
Thunderhorn (Donnerhörner), Steamboil (Kesseldampf), Twilight-Hammer,
-klan (Schattenhammer/Schattenhammerklan), Fathom-Kern (Tiefenkern),
Blackfathom Deeps (Tiefschwarze Grotte), Blackrock-* (Schwarzfels-*),
Hawkwind (Falkenwind), Feathermoon (Mondfeder), Moonrage (Mondzorn),
Firemane (Feuermähne), Searingblade (Sengende Klinge), Ragefireabgrund
(Flammenschlund), Ironbands Areal (Eisenbands Lager), Zandalar
(Zandalari), Southshore (Süderstade)

for quest progress/request text entries for the deDE localisation with
proper casus/declension (these are not proper translated names of
locations/NPCs that have been left over by Blizzard since their language
localisations in TBC in 2006 and onward).

Added missing progress/request text entries for 308, 311, 417, 1644,
1787, 5059, 5060, 5721, 6004, 6023, 6025, 6187, 8042, 8043, 8044, 8046,
8047, 8048, 8050-8079, 8102, 8107, 8108, 8111, 8112, 8113, 8117, 8118,
8142, 8143, 8147, 8183-8195, 8238, 8239, 8240, 8243, 8246, 8860, 9594,
9692, 9707, 10414, 10415, 10919, 11451. (A lot of them are
Zandalari/Zul'Gurub related quests.)

Replaced post-Cataclysm progress/request text entries for 933, 935,
6387, 7383.

Fixed a wrong $R with plain text at progress/request text for 9147.

Added missing female gender equivalent to 6391.

(There are probably more changes in the file that aren't further
explained here as it was hard to keep track of everything. If you think
I made a mistake or have questions please contact me directly.)

<!-- First of all, THANK YOU for your contribution. -->

## Changes Proposed:
-  Fixing a lot in the quest_request_items_locale table.

## Issues Addressed:
<!-- If your fix has a relating issue, link it below -->
- Fixing some of the tasks in
https://github.com/azerothcore/azerothcore-wotlk/issues/14244
Referring to my other two bug reports from CC Github:
- https://github.com/chromiecraft/chromiecraft/issues/4697
- https://github.com/chromiecraft/chromiecraft/issues/4745

## SOURCE:
<!-- If you can, include a source that can strengthen your claim -->
- Read the text on top.

## Tests Performed:
<!-- Does it build without errors? Did you test in-game? What did you
test? On which OS did you test? Describe any other tests performed -->
- Not tested.


## How to Test the Changes:
<!-- Describe in a detailed step-by-step order how to test the changes
-->
All of the changes are to reward texts of quests, can be tested by
completing quests or simply reviewing the changed file.

## Known Issues and TODO List:
<!-- Is there anything else left to do after this PR? -->

- [ ]
- [ ]

<!-- If you intend to contribute repeatedly to our project, it is a good
idea to join our discord channel. We set ranks for our contributors and
give them access to special resources or knowledge:
https://discord.com/invite/DasJqPba)
Do not remove the instructions below about testing, they will help users
to test your PR -->
## How to Test AzerothCore PRs
 
When a PR is ready to be tested, it will be marked as **[WAITING TO BE
TESTED]**.

You can help by testing PRs and writing your feedback here on the PR's
page on GitHub. Follow the instructions here:

http://www.azerothcore.org/wiki/How-to-test-a-PR

**REMEMBER**: when testing a PR that changes something **generic** (i.e.
a part of code that handles more than one specific thing), the tester
should not only check that the PR does its job (e.g. fixing spell XXX)
but **especially** check that the PR does not cause any regression (i.e.
introducing new bugs).

**For example**: if a PR fixes spell X by changing a part of code that
handles spells X, Y, and Z, we should not only test X, but **we should
test Y and Z as well**.

---
## [TheHackerManXD/git_test](https://github.com/TheHackerManXD/git_test)@[731da66654...](https://github.com/TheHackerManXD/git_test/commit/731da666542111e76e471c63e1205387027db652)
#### Tuesday 2023-01-24 03:26:37 by Le Hacker Man

test message
>> -paragraph 1
>> -paragraph 2
>>
>> test. this is a test paragraph. I need to kinda know if I would be able to write a fully fledged paragraph. Will this break the line? Will it start off on a new line? Im just gonna say something gibberish from here on out. afsgiknsgiaoshgnsighs oh oh shit it did. Wonder if
>>
>> test paragraph 2. test test this
>> new line
>> is part
>> of the same
>> paragraph
>> .
>>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[85cf32d496...](https://github.com/treckstar/yolo-octo-hipster/commit/85cf32d4961265423dede9b42095eeecd437602e)
#### Tuesday 2023-01-24 04:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [mpaglia0/ansel](https://github.com/mpaglia0/ansel)@[8502f413b8...](https://github.com/mpaglia0/ansel/commit/8502f413b885010a4fdf3d8a6222ffc2bbf2ce44)
#### Tuesday 2023-01-24 07:05:12 by Aurélien PIERRE

Remove histogram color profile

Aside from being coded with the ass (entirely copy-pasted), the histogram color profile is useless since the histogram is grabbed in display RGB. If we want to display the histogram in pipe RGB, then we can convert display to pipe RGB but if RGB got clipped in display, then we convert clipped signal.

The whole thing is misleading and was used in overexposed module, which completely voids its purpose. Say you display histogram in Rec 2020 (super large), but your display is sRGB (super small), then you clip in sRGB at 100%, but converting back to Rec 2020, your 100% becomes 90 % or something, and the scope shows no overexposure at all.

That's bullshit coded by idiots. Not sure why it took me 4 years to spot it.

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[873da57fc9...](https://github.com/clintjedwards/gofer/commit/873da57fc9fde80ee9dd647df75e4793010b32da)
#### Tuesday 2023-01-24 07:28:40 by Clint J Edwards

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
## [PixelExperience-Devices/device_samsung_sm7125-common](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common)@[68610492a9...](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common/commit/68610492a9eddaf866210b7aa7c9dff99379479b)
#### Tuesday 2023-01-24 07:40:59 by Ruchit

sm7125: (note to self) dont pick this ye dumb idiot its only for wip branch so you can test shit better k bye

---
## [zeeb92/tgstation](https://github.com/zeeb92/tgstation)@[75439c71f2...](https://github.com/zeeb92/tgstation/commit/75439c71f2282a3ae72b4ea35c80e27ca8556aaf)
#### Tuesday 2023-01-24 09:57:38 by Mothblocks

Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins (#71989)

This one is fun.

On every /turf/Initialize and /atom/Initialize, we try to set
`smoothing_groups` and `canSmoothWith` to a cached list of bitfields. At
the type level, these are specified as lists of IDs, which are then
`Join`ed in Initialize, and retrieved from the cache (or built from
there).

The problem is that the cache only misses about 60 times, but the cache
hits more than a hundred thousand times. This means we eat the cost of
`Join` (which is very very slow, because strings + BYOND), as well as
the preliminary `length` checks, for every single atom.

Furthermore, as you might remember, if you have any list variable set on
a type, it'll create a hidden `(init)` proc to create the list. On
turfs, that costs us about 60ms.

This PR does a cool trick where we can completely eliminate the `Join`
*and* the lists at the cost of a little more work when building the
cache.

The trick is that we replace the current type definitions with this:

```patch
- smoothing_groups = list(SMOOTH_GROUP_TURF_OPEN, SMOOTH_GROUP_FLOOR_ASH)
- canSmoothWith = list(SMOOTH_GROUP_FLOOR_ASH, SMOOTH_GROUP_CLOSED_TURFS)
+ smoothing_groups = SMOOTH_GROUP_TURF_OPEN + SMOOTH_GROUP_FLOOR_ASH
+ canSmoothWith = SMOOTH_GROUP_FLOOR_ASH + SMOOTH_GROUP_CLOSED_TURFS
```

These defines, instead of being numbers, are now segments of a string,
delimited by commas.

For instance, if ASH used to be 13, and CLOSED_TURFS used to be 37, this
used to equal `list(13, 37)`. Now, it equals `"13,37,"`.

Then, when the cache misses, we take that string, and treat it as part
of a JSON list, and decode it from there. Meaning:

```java
// Starting value
"13,37,"

// We have a trailing comma, so add a dummy value
"13,37,0"

// Make it an array
"[13,37,0]"

// Decode
list(13, 37, 0)

// Chop off the dummy value
list(13, 37) // Done!
```

This on its own eliminates 265ms *without space ruins*, with the
combined savings of turf/Initialize, atom/Initialize, and the hidden
(init) procs that no longer exist.

Furthermore, there's some other fun stuff we gain from this approach
emergently.

We previously had a difference between `S_TURF` and `S_OBJ`. The idea is
that if you have any smoothing groups with `S_OBJ`, then you will gain
the `SMOOTH_OBJ` bitflag (though note to self, I need to check that the
cost of adding this is actually worth it). This is achieved by the fact
that `S_OBJ` simply takes the last turf, and adds onto that, meaning
that if the biggest value in the sorting groups is greater than that,
then we know we're going to be smoothing to objects.

This new method provides a limitation here. BYOND has no way of
converting a number to a string at compile time, meaning that we can't
evaluate `MAX_S_TURF + offset` into a string. Instead, in order to
preserve the nice UX, `S_OBJ` now instead opts to make the numbers
negative. This means that what used to be something like:

```dm
smoothing_groups = list(SMOOTH_GROUP_ALIEN_RESIN, SMOOTH_GROUP_ALIEN_WEEDS)
```

...which may have been represented as

```dm
smoothing_groups = list(15, MAX_S_TURF + 3)
```

...will now become, at compile time:

```dm
smoothing_groups = "15,-3,"
```

Except! Because we guarantee smoothing groups are sorted through unit
testing, this is actually going to look like:

```dm
smoothing_groups = "-3,15,"
```

Meaning that we can now check if we're smoothing with objects just by
checking if `smoothing_groups[1] == "-"`, as that's the only way that is
possible. Neat!

Furthermore, though much simpler, what used to be `if
(length(smoothing_groups))` (and canSmoothWith) on every single
atom/Initialize and turf/Initialize can now be `if (smoothing_groups)`,
since empty strings are falsy. `length` is about 15% slower than doing
nothing, so in procs as hot as this, this gives some nice gains just on
its own.

For developers, very little changes. Instead of using `list`, you now
use `+`. The order might change, as `S_OBJ` now needs to come first, but
unit tests will catch you if you mess up. Also, you will notice that all
`S_OBJ` have been increased by one. This is because we used to have
`S_TURF(0)` and `S_OBJ(0)`, but with this new trick, -0 == 0, and so
they conflicted and needed to be changed.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5d3717c4d4...](https://github.com/mrakgr/The-Spiral-Language/commit/5d3717c4d43b8cf180ceb25e07d606223d7186a1)
#### Tuesday 2023-01-24 11:18:01 by Marko Grdinić

"https://rentry.org/hiresfixjan23
> Upscaler = Latent or your GAN of choice, denoising = ~0.65 or ~0.30 respectively

Maybe should try 0.65 instead of just 0.6 or 0.7

10:55pm. https://news.ycombinator.com/item?id=34492437

///

I asked ChatGPT to write a poem based on this post. Here's what it wrote:

---

Two hearts, two minds, working side by side
In pursuit of a mission to make AI safe and wide
Microsoft’s investment allows us to stay true
To our capped-profit company, our mission, and you
From cloud computing to real-world use
We collaborate to ensure our systems are not abused
OpenAI API, Azure’s OpenAI Service, and Designer too
We’re working side by side to make our visions come true
Together we review, together we synthesize
Together we build, together we realize
The potential of advanced AI that’s powerful and safe
Ensuring its benefits can be shared far and wide

///

Way better poet than me.

1/24/2023

9:50am. Any mail? Nothing except some Paperspace spam.

10am. I see on the application page that I got a few rejects, but the rest are pending. I just applied to a small startup for game engine programming.

10:10am. https://angel.co/jobs?job_listing_id=2511252
> RESPECTED, CONNECTED & GLOBALLY REGARDED INDIVIDUAL MOVING IN CIRCLES OF INFLUENCE AND WEALTH.

Look at this job. 1m a year. Now that is something.

10:20am. I've applied to a few places. I guess I won't have much to do yet.

10:25am. Let me chill a bit and then I'll slowly get started.

10:55am. Let me do some more application. Forget AngelList. Since I am .NET focused, it would make sense to get jobs in that area, but even Rust is more popular than .NET on AngelList. The only .NET jobs as far as I could see are some Unity ones.

Let me ask HN.

https://news.ycombinator.com/item?id=31812098
Show HN: Remote .NET Job Board

https://dotnetdevs.co/

Let's give this a try.

> Describe yourself as a dev in a few words
> Expert functional programmer who wants to make his PL the dominant language for programming AI chips

Let me go with this.

> Share a few paragraphs on your past experiences and what makes you special. This is your chance to stand out amongst the crowd. Don't be shy!

>  Personally identifiable information will be removed.

Huh, why?

///

I used to be good at competitive programming back in school to the point of being a national champion on Croatia at one point. Then I drifted away before the deep learning revolution drew me back. I started work on ML library for F# that later became a language. In the next decade, there will be a paradigm shift in programming as AI accelerators and PIM devices become mainstream, and I believe the design of my PL is the most suitable to support all those devices.

The many years of full time work on my language and the ML library gave me a deep familiarity in functional programming, PL development, deep learning and concurrency.

///

Let me just go with this.

https://dotnetdevs.co/jobs

Yeah, I should be applying here. The job board being more out of the way is not that bad, that means the companies will be less swamped by resumes.

> Working together in a team is very important for us at Power Diary. Please briefly outline the type of team you like to work in.*

Uh, what kinds of teams are there.

> Work well in a small team with a clear mission

Sounds good to me.

> A small team with a clear mission.

Posted this.

I am looking at DraftKings job boards, and it says Github. I wonder if Github has a job board?

https://www.remotely.jobs/

Found this in a thread.

https://github.com/tramcar/awesome-job-boards

https://functionaljobs.dev/

Oh this has some functional jobs.

https://www.functionaljobs.com/

This is one is defunct. The latest job is from 2021.

https://functional.works-hub.com/

This might be interesting.

11:35am. Maybe I should really start studying Rust.

https://www.reddit.com/r/fsharp/comments/10k2sou/where_do_i_find_f_remote_jobs/

Posted this on the F# sub. This is how serious I am this time.

https://gist.github.com/swlaschin/6459789afd1b5e7a2c9f6a531c37b1ec

> The F# slack has a #jobs channel. If you've not already joined, you can join using the guide here https://fsharp.org/guides/slack/

I might want to check this out.

https://foundation.fsharp.org/join

Ah, I need to join the F# foundation before I can access their Slack.

12:10m. > Once you are a member, you will automatically be queued to receive an invite to the Foundation’s Slack team.

I joined the free tier as a member. I guess at some point I'll get an invite to the F# slack. Anyway, if finding an F# remote job turns out to be too difficult, I might have to pick up something like Rust, as well as start picking up those database, cloud and whatever technologies. In the worst, I'll do some freelancing for peenies in order to motivate myself to pick up new technologies. I am far too out of sync with what the market demands right now, and that would serve to calibrate me.

It is only the second day I started applying. I'll see how it goes. It is good to be proactive like this.

Let's give it a few days. I'll probably get some replies to that F# thread and see how it goes from there.

Right now, it is time for chores and breakfast. For the rest of the day after that, I'll do some writing. Let's see if I can do 2k words today."

---
## [totalspectrum/spin2cpp](https://github.com/totalspectrum/spin2cpp)@[231cd01d28...](https://github.com/totalspectrum/spin2cpp/commit/231cd01d28c3481e70929507ac927f73176d847c)
#### Tuesday 2023-01-24 12:35:46 by Eric R. Smith

Merge pull request #352 from Wuerfel21/W21-fix-stupid-fucking-bullshit

Fix funny bug and add optimizer debug code

---
## [newstools/2023-iol-pretoria-news](https://github.com/newstools/2023-iol-pretoria-news)@[b9c8bb1159...](https://github.com/newstools/2023-iol-pretoria-news/commit/b9c8bb11595c989d6cf9885a87297e472da96a9d)
#### Tuesday 2023-01-24 12:52:38 by Billy Einkamerer

Created Text For URL [www.iol.co.za/pretoria-news/news/pretoria-news/news/head-girl-and-head-boy-terms-discriminate-against-pupils-who-do-not-identify-as-male-or-female-says-foundation-f60c5c29-c0bd-4791-8854-49af45a32b71]

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[00e7d5d746...](https://github.com/Jacquerel/orbstation/commit/00e7d5d7465211ccf0e3d604e566e2c08775cd20)
#### Tuesday 2023-01-24 13:04:05 by GoldenAlpharex

*hand, or That /One/ Emote You Always Felt Was Missing (#71600)

## About The Pull Request
It's happened to me _repeatedly_ that I'd see someone down on the floor,
and wanted to just, give them a hand, so they could take it and get up
that way, without just, directly clicking on them, since that's a little
bland. I've also wanted to just, offer my hand to someone so they could
grab it, so that I could pull them alongside me, rather than just
targeting one of their arms and ctrl-clicking them.

I've had this idea for a _long_ time, and only just decided to do this
today.

Now, I know what you might say. "Golden, that's a lot of code for
something this simple!" You're not wrong. _However_. I decided to go
along and to give some more love to the `/datum/status_effect/offering`
status effect and the offering-related alerts, to make them a lot more
versatile and a lot less hardcoded. Hence the whole "refactoring" part
of this.

Of course, when I add something, I don't do it half-way. So, the way the
emote works is much like the `*slap` emote, except that:

- When you click on someone, it does the exact same as if you were
offering the item to them, except that it's targeted (much like
ctrl-shift-click).
- If there's nobody directly adjacent to you, it won't do anything.
- If there's at least one person lying down around you, you will offer
them your help to get up. Should they take your hand and let you help
them up, you will both receive a simple memory about being helped up (or
helping up), as well as a 45-seconds-long small mood buff, because it
feels nice to be on either end of such a friendly gesture. If they get
up, they automatically get disqualified from being offered some help
standing up, and likewise, if you lie down, that offer goes away as
well.
- If there's at least one person around you, you will instead extend
your hand in their direction, for them to grab onto it. Should they do
so, you will then grab them by their arms and pull them.

I reworked the offering status effect to no longer have a hardcoded
`can_hold_items()` check, so that kisses and the hand offering would no
longer need you to have free hands to complete. The logic here is that
you can still pull someone even with both hands filled, so I figured I'd
leave it this way.

Note: If anyone would like to give the item a better sprite, by all
means, go ahead, that'd be amazing. I'm just not really a great spriter
and couldn't be bothered to waste hours making a very _meh_ hand.

## Why It's Good For The Game
It's fluff, and nice fluff at that. It makes it easier for people to be
nice to one-another without having to necessarily spend so long writing
up an emote that the person on the floor will already have gotten back
up. I'm sure the MRP folks will like it, and I'm certain the HRP
downstreams will love it too ;)

## Changelog

:cl:
add: Added the *hand emote, which you can offer to someone standing up
in order to give them the possibility to grab onto your hand and let you
drag them away, or to someone lying down to help them back up, which
always makes everyone involved a little happier!
refactor: De-hardcoded and genericized a lot of the offering status
effect and alert code, to make it require a lot less copy-paste to
handle new cases.
fix: Offering a kiss no longer requires the receiver to have free hands
to accept said kiss!
/:cl:

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[6c065f72b8...](https://github.com/git-for-windows/git/commit/6c065f72b8d581eee53ab82e82da049ee492bf11)
#### Tuesday 2023-01-24 13:19:23 by Jeff King

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

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[8e5251ea60...](https://github.com/Stalkeros2/Skyrat-tg/commit/8e5251ea6090a67d0b16c6799f1071884f7c7188)
#### Tuesday 2023-01-24 13:44:27 by SkyratBot

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
## [xlloss/buildroot](https://github.com/xlloss/buildroot)@[dcd36d47d2...](https://github.com/xlloss/buildroot/commit/dcd36d47d2416e1c713849a8b95fa5e6e8530b51)
#### Tuesday 2023-01-24 14:01:29 by Thomas Petazzoni

toolchain-external: fix potential entire root filesystem removal

This reverts commit a0aa7e0e1750f6ace2879ea8adb1425a41431b79 and reworks
the code to fix a major and potentially catastrophic bug when the
following conditions are met:

 - The user has selected a "known toolchain profile", such as a Linaro
   toolchain, a Sourcery CodeBench toolchain etc. People using "custom
   toolchain profile" are not affected.

 - The user has enabled BR2_TOOLCHAIN_EXTERNAL_PREINSTALLED=y to
   indicate that the toolchain is already locally available (as
   opposed to having Buildroot download and extract the toolchain)

 - The user has left BR2_TOOLCHAIN_EXTERNAL_PATH empty, because his
   toolchain is directly available through the PATH environment
   variable. When BR2_TOOLCHAIN_EXTERNAL_PATH is non-empty, Buildroot
   will do something silly (remove the toolchain contents), but that
   are limited to the toolchain itself.

When such conditions are met, Buildroot will run "rm -rf /*" due to
TOOLCHAIN_EXTERNAL_INSTALL_DIR being empty.

This bug does not exist in 2016.05, and appeared in 2016.08 due to
commit a0aa7e0e1750f6ace2879ea8adb1425a41431b79.

Commit a0aa7e0e1750f6ace2879ea8adb1425a41431b79 removed the assignment
of TOOLCHAIN_EXTERNAL_SOURCE and TOOLCHAIN_EXTERNAL_SITE to empty, as
part of a global cleanup to remove such assignments that supposedly
had become unneeded following a fix of the package infrastructure
(75630eba22b20d6140a5b58a6d1e35598fb3c0d3: core: do not attempt
downloads with no _VERSION set).

However, this causes TOOLCHAIN_EXTERNAL_SOURCE to be non-empty even
for BR2_TOOLCHAIN_EXTERNAL_PREINSTALLED=y configuration, with the
following consequences:

 - Buildroot downloads the toolchain tarball (while we're saying the
   toolchain is already available). Not dramatic, but clearly buggy.

 - Buildroot registers a post-extract hook that moves the toolchain
   from its extract directory (output/build/toolchain-external-.../ to
   its final location in host/opt/ext-toolchain/). Before doing this,
   it removes everything in TOOLCHAIN_EXTERNAL_INSTALL_DIR (which
   should normally be host/opt/ext-toolchain/).

Another mistake that caused the bug is commit
b731dc7bfb9c8ce7be502711f0b44ccab5515f1d ("toolchain-external: make
extraction idempotent"), which introduce the dangerous call "rm -rf
$(var)/*", which can be catastrophic if by mistake $(var) is
empty. Instead, this commit should have just used rm -rf $(var) to
remove the directory instead: it would have failed without consequences
if $(var) is empty, and the directory was anyway already re-created
right after with a mkdir.

To address this problem, we:

 - Revert commit a0aa7e0e1750f6ace2879ea8adb1425a41431b79, so that
   _SOURCE and _SITE are empty in the pre-installed toolchain case.

 - Rework the code to ensure that similar problems will no happen in the
   future, by:

   - Registering the TOOLCHAIN_EXTERNAL_MOVE hook only when
     BR2_TOOLCHAIN_EXTERNAL_DOWNLOAD=y, since moving the toolchain is
     only needed when Buildroot downloaded the toolchain.

   - Introduce a variable TOOLCHAIN_EXTERNAL_DOWNLOAD_INSTALL_DIR which
     is the path in which Buildroot installs external toolchains when it
     is in charge of downloading/extracting them. Then, the
     TOOLCHAIN_EXTERNAL_MOVE hook is changed to use this variable, which
     is guaranteed to be non-empty.

   - Replace the removal of the directory contents $(var)/* by removing
     the directory itself $(var). The directory was anyway already
     re-created if needed afterwards. Thanks to doing this, if $(var)
     ever becomes empty, we will do "rm -rf" which will fail and abort
     the build, and not the catastrophic "rm -rf /*".

Reported-by: Mason <slash.tmp@free.fr>
Cc: Mason <slash.tmp@free.fr>
Signed-off-by: Thomas Petazzoni <thomas.petazzoni@free-electrons.com>
Signed-off-by: Peter Korsgaard <peter@korsgaard.com>
(cherry picked from commit b171466c445dbdd39d5084dd4e4c138a7051d99a)

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[4305ca8faa...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/4305ca8faa2f25dc9c5bd7ff653492e0e8c5dc0f)
#### Tuesday 2023-01-24 14:01:55 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>
Signed-off-by: pix106 <sbordenave@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [rust-bitcoin/rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin)@[f6d983b2ef...](https://github.com/rust-bitcoin/rust-bitcoin/commit/f6d983b2ef4dfacd53499fd9f1d77058c0f396ff)
#### Tuesday 2023-01-24 14:18:33 by Andrew Poelstra

Merge rust-bitcoin/rust-bitcoin#1532: Improve Psbt error handling

e7bbfd391353fd03d60550c768364e9de5d3e8c5 Improve Psbt error handling (DanGould)

Pull request description:

  ## Separate `encode::Error` and `psbt::Error` recursive dependency

  This initial work attempts to fix #837's first 2 points

  > - The current psbt::serialize::Deserialize has an error type of consensus::encode::Error. I think we should cleanly separate consensus encoding errors from application-level encoding errors like psbt.
  > - There is a recursive dependence between encode::Error and psbt::Error which would need to be cleanly dissected and separated so that there is no dependence or only one-way dependence.

  ## Better `ParseError(String)` types

  arturomf94 how compatible do your #1310 changes look to address #837's third point with this design?

  > - There are a lot ParseError(String) messages that could use a better type to downflow the information.

  I think your prior art would completely address this issue now.

  ## On handling `io::Error` with an associated error

  `encode::Error` has an `Io` variant. now that `Psbt::deserialize` returns `psbt::Error` and produces an `io::Error`, we need an `Io` variant on `psbt::Error`. Except that doing so breaks  `#[derive(Eq)]` and lots of tests for `psbt::Error`.

  Kixunil, I'm trying to understand your feedback regarding a solution to this problem.

  > I believe that the best error untangling would be to make decodable error associated.

  > I meant having associated `Error` type at `Decodable` trait. Encoding should only fail if the writer fails so we should have `io::Error` there (at least until we have something like `genio`).
  >
  > > [it] is a problem to instantiate consensus::encode::Error in [the psbt] module for `io::Error`?
  >
  > It certainly does look strange. Maybe we should have this shared type:
  >
  > ```rust
  > /// Error used when reading or decoding fails.
  > pub enum ReadError<Io, Decode> {
  >     /// Reading failed
  >     Io(Io),
  >     /// Decoding failed
  >     Decode(Decode), // consensus and PSBT error here
  > }
  > ```
  >
  > However this one will be annoying to use with `?` :( We could have `ResultExt` to provide `decode()` and `io()` methods to make it easier.
  >
  > If that's not acceptable then I think deduplicated IO error is better.

  Kixunil didn't we just get rid of Psbt as `Decodable`? Would this make more sense to have as an error associated with `Deserialize`? Or did we do the opposite of what we should have by making Psbt only `Serialize`/`Deserialize` because of #934, where only consensus objects are allowed to be `Decodable`? I wonder if we prioritized that strict categorization and are stuck with worth machinery because of it. My goal with #988 was to get to a point where we could address #837 and ultimately implement PSBTv2.

ACKs for top commit:
  tcharding:
    ACK e7bbfd391353fd03d60550c768364e9de5d3e8c5
  apoelstra:
    ACK e7bbfd391353fd03d60550c768364e9de5d3e8c5

Tree-SHA512: 32975594fde42727ea9030f46570a1403ae1a108570ab115519ebeddc28938f141e2134b04d6b29ce94817ed776c13815dea5647c463e4a13b47ba55f4e7858a

---
## [A-Hilaly/ack-test-infra](https://github.com/A-Hilaly/ack-test-infra)@[ad886bafa8...](https://github.com/A-Hilaly/ack-test-infra/commit/ad886bafa81a73e1548b7057cf9b76e3fb4b1741)
#### Tuesday 2023-01-24 15:07:08 by Amine Hilaly

Move Go binaries to `/usr/local/bin`

Yesterday, i embarked on a wild 7 hour journey to fix a bug that had
been causing prow jobs to fail with the error message "Kind not found".
The bug was introduced after a recent update that bumped the Go compiler
to `1.19`. I found the investigation to this bug to be both interesting
and frustrating, so i wanted to share some key takeways with the
community:

The patch that introduced Go `1.19` also modified a `go get` command
into a `go install` command (because of this deprecation notice:
https://go.dev/doc/go-get-install-deprecation), which technically should
not have caused any issues. I tried restarting the e2e jobs in various
repositories to figure out whether the error was only related to one
controller or code-generator only, but all the repositories that execute
e2e tests were affected.

First, i started suspecting that thee `go install` command was not
working properly or had not been used correctly. I experiemented with it
locally, using various combinations of `GOPATH` and `GOBIN`, however, i
learned that the Go compiler is sophisticated enough to always put
downloaded binaries under `GOBIN` or `GOPATH/bin`. I then wondered if
the `PATH` variable didn't include the `GOBIN` path, which i ssupposed
to contain the `kind` and `controller-gen` binaries. I spent some time
reading the Dockerfiles and testing scripts, but they all set `GOPATH`
and always included a `GOBIN` in the `PATH` variable.

I also suspected that the issue may be related to the containers, but
experimentations with "Go containers" and environement variables
manipulation did not yield any results. I also tried building minimal
DOckerfiles to try to reproduce the issue, but that also did not give
any clues.

At this point, I suspected the container image it self. I build an image
locally and ran a shell inside it, but everythin g looked fine. THe
`kind` and `controller-gen` binaries were present and the `PATH` and
`GOPATH` variables were properly set. I then suspect that we may have a
corrupted published image in ECR, but pulling the image and running the
same commands revealed that the image was fine.

I then took a break from experimenting with Go/Docker/Envvars and tried
to spin some prowjobs with `v0.0.10` and `v0.0.9` (the last two versions
that were still using Go 1.17) of the integration tests image. This
confirmed that the issue was only with `v0.0.11`.

So, I decided to investigate further and logged in the Prow production
cluster. My first attempt was to restart a job and try to "exec bash" in
it, but the jobs failed to quickly for that to be possible. I then ran
a custom prow job (with `v0.0.11` integration image tag) but with a
`sleep 10000` command. When looking inside, there were no `kind` or
`controller-gen` binaries, i searched the entire file system, they were
nowhere to be found, grep, find, name it all.. nada. I then execute a
`go install sigs.k8s.io/kind@v0.17.0"`, and bam, it worked, the binary
was here again. The same thing happened with controller-gen. So for now
we know that we ship images with all the necessary binaries and when a
prow job starts, they disapear...

To isolate the problem further, i created a `ProwJob` resource and
copied the `Pod` (spawned by Prow) spec and metadata into a different
file. Running the same commands used previously proved that indeed
something is wrong with the pod spec, causing the binaries to disapear.
And when a file disppears it reminds me of my college years, where i
epically failed to use symbolic links, which is a bit similar (at least
from a UX point) to volume mounts in the Docker world.

So, i decided to check the volume mounts, and to my not-surprise, I
found this:

```yaml
    - mountPath: /home/prow/go
      name: code
```

Yes... Prow is mounting the test-infra source code into `GOPATH`
(`/home/prow/go` in prow jobs) ! Which is the parent directory of
`GOBIN` where we install the binaries. And it all makes sense now.
Mounting code into this directory overrides the existing volume and
deletes everything existing in `GOPATH` including the binaries we
installed before.

The Dockerfile was missing the `mv` commands that puts `kind` and
`controller-gen` in `/usr/bin`. To fix this issue, I added the missing
`mv` command to the docker file and published and new `integration`
image `v0.0.12`.

---

Anyways, investigating the source of the volume mount led me to the Prow
presets configurations. Presets are a set of configurations (volume
mounts, environement variables, etc...) that are used for jobs with
specific labels in their metadata. I tried to play with this in our Prow
cluster, but quickly stoped when it was a bit risky and could break
other components too. While digging into `test-infra` pod-util package i
learned that the code volume is not coming from our defined presets and
is a default preset coming from Prow it self - the `/home/prow/go` value
is harded-coded in `prow/pod-utils/decorate/podspec.go#L54`. I'm not
sure whether we can override this value.

Anyways, for now, i'm just gonna implement a quick fix which moves the
binaries to `/usr/bin` instead of leaving them inside `GOBIN`. Ideally
we should either choose a new directory go `GOPATH` that is different
from `$HOME/go` or find a solution that will let the code and our
binaries coexist in the same place. Either of them requires a lot of
changes and can agressively break some our prow components/scripts.

@jljaco is currently workng on creating a staging cluster, which will
provide us a safe environementto test and experiment with new
configurations. This will allow us to try out new changes without having
to woryy about potentially impacting the production environement.

Signed-off-by: Amine Hilaly <hilalyamine@gmail.com>

---
## [CDCgov/prime-reportstream](https://github.com/CDCgov/prime-reportstream)@[479d860427...](https://github.com/CDCgov/prime-reportstream/commit/479d86042794baa6f0b095572c2fee5e0b480d95)
#### Tuesday 2023-01-24 15:15:26 by Stephen Kao

Experience-7891: Disable organization-specific fetches as admin

This changeset disables a few Organization-specific requests to mitigate the number of 404s we're getting as admins try to fetch Organization resources:
- Organization settings
- Deliveries
- Submissions

There's not a one-size-fits-all solution here given the different fetch mechanisms we already have and how the data is rendered, so I tried to add minimal changes to prevent disrupting anything down the line.  I think going forward, we can make a generic `useOrganizationQuery` hook that'll automatically be disabled if the user is logged in as an admin without impersonating an Organization.  There are a lot of layers with our fetching that in my opinion should be untangled, but that's out of the scope of this pull request.

---
## [sammmhodge/AlienPowerWash](https://github.com/sammmhodge/AlienPowerWash)@[5919dcf543...](https://github.com/sammmhodge/AlienPowerWash/commit/5919dcf5432330de6644fe9e97331c962e03e231)
#### Tuesday 2023-01-24 16:01:56 by sammmhodge

The game now calculates a percentage cleaned

Adult Tim: Survival of the fittest. It's the law of the jungle. There's always someone trying to take what's yours. How do I know? It almost happened to me.

Tim Templeton... quit monkeying around. Hot dogs are getting cold. Hot dogs? At least, this is how I remember it. All right, buddy, let's eat. You see, I was seven years old... and back then, you relied on your imagination. When I wasn't exploring the Congo... I was a deep sea diver. Tim! Our hero! Don't worry, Mom and Dad. I got this! Grab on! Some days, I rescued my parents. That way! Other days, they rescued me. - I'm losing control. - Tim, look out! Tree! You're breaking up! Slow down, Tim! - Turn, Tim. - Turn! - Are you hurt? - I'm okay. Show Mommy your teeth. It was just the three of us. The Templetons. And three is the perfect number. Interesting fact... did you know that the triangle is the strongest shape found in nature? I was the luckiest kid ever. My parents even had cool jobs. They worked for the biggest pet company

in the world... Puppy Co. - Yes, Mr. Francis? - Puppy Co needs you. It's go time. They worked in a department called "Marketing..." where they got to launch new products. Even though my parents worked really hard... they still made just enough time for me. Three stories, five hugs, and my special song, right? You got it! Blackbird singing in the dead of night Take these broken wings and learn to fly All your life You were only waiting For this moment to arise Hey, Tim. How would you like to have a baby brother? No, thanks. I'm enough.

Adult Tim: Life was good. Life was perfect. But as I drifted off to sleep... something my parents said got me thinking. Where do babies come from? The day I got a little brother started like any other day... but little did I know... my life would never be the same.

Wake up, little halflings! It's 7:00 a.m. Wake up, little halflings! Morning, Wizzie! What great adventure lies in wait for you today? Oh, yeah! My parents always said that I had an overactive imagination. But I clearly remember... the baby was delivered in a taxi. What the... Hey! Tim, look who's here. Meet your new baby brother. Baby what? Brother.

Adult Tim: I had a million questions. Who is this guy? Why is he here? What's with that outfit? Why's he so fat? Why's he staring at me? Does he know karate? What's going on?

That way? - Okay. - Okay.

Adult Tim: Right from the start, he was yelling at people... ordering everyone around.

Oh, you want this?

Adult Tim: One thing was clear. He was the boss. He set up his office, right smack dab in the middle of the house. He conducted meetings.

- You called? - Do you need Seor Squeaky?

Adult Tim: Lots and lots of meetings. Even in the middle of the night.

I'm up! I'm up! - We're coming! - We'll be right there!

Adult Tim: If things weren't done to his immediate satisfaction... he had a fit.

Where's the bottle? - He has to have his bottle!

Adult Tim: He had everyone wrapped around his chubby little finger. Everyone except for me.

Diaper! - Bottle! Dad! I can't sleep. I know, bud. Me neither. The baby needs a lot of attention right now. Okay, good talk! - But... - It's okay. Daddy's here. Daddy's here. What about me? The year: 2057. Ensign T-Rex and I are investigating a hostile alien invasion. It's so much worse than we thought. Mom, he's naked! I'm naked!

Say "naked." No! Who's Mommy's little cutie? Are you Mommy's little cutie? No, he's Daddy's little tough guy, right? You know one of us has to go with Mr. Francis to the pet convention. In Vegas. - You know what? You should go. - No, no. You should go. Well, you need a break. - I'll stay with the baby, and you... - Maybe the baby should decide. Who do you want to stay with you? Daddy or Mommy? Or Daddy? He wants his mommy. Okay, we need to talk! In private. - Sure. - About what, bud? About the b-a-b-e-e. "Y," Tim. Why? Because he came out of nowhere! We don't even know him. How can we trust him? Come on, he's just a baby. Seriously? I'm the only one that thinks there's something weird about this guy? - Oopsie! I got it. - Five-second rule. Tim? Look at him! He wears a suit! I know. Isn't it cute? He's like a little man. He carries a briefcase. Does no else think that's... I don't know, a little freaky? Well, you carried Lam-Lam around until you were like... This is not about Lam-Lam. All babies are different, Tim. And each one is special. He's taking over the whole house! Are you taking over the house? Yes, you are. Yes, you are.

Trust me, one day you're gonna get to know this little guy... and you are gonna love him with all of your heart. Just like we do. All of your heart? Never. Hello! It's time for my three stories, five hugs, and special song! How about one story... three hugs, and my special song? Just my special song? Mom? Dad? Hey. What happened to bedtime? We'll have it on Monday, Mr. Francis. Don't cry! Don't cry. Hello? Hello? No, ma'am, not yet. No, I'm not making excuses. Yes, ma'am, I know I've been here a long time. Believe me, it feels like my whole life. I'm making great progress with the parents already. The usual procedure, sleep deprivation, hunger strikes. They're very disoriented. I've got them eating out of the palm of my hand. They do everything for me. It's hilarious. But I think the kid might be on to me. No, I can handle him. I know how important this mission is to the company. Mission? Well, trust me, ma'am. You got the right baby for this job. Hands up, devil baby! Fart! Poop! Doodie! I've gotta deal with the k-i-d. You can talk! Uh, goo-goo Ga-ga.

No, you can really talk. I heard you! Fine. I can talk. Now, let's see if you can listen. Get me a double espresso... and see if there's someplace around here with decent sushi. I'd kill for a spicy tuna roll right about now. Get yourself a little something. Who are you? Let's just say I'm the boss. The boss? You're a baby! You wear a diaper. You know who else wears diapers? Astronauts and NASCAR drivers, that's who. It's called efficiency, Templeton. The average toddler spends, what? 45 hours a year on the potty? I'm the boss. I don't have that kind of spare time. Well, you're not the boss of me. - I am the boss of you. - No, you're not. - Am, too. - Are not. - Am, too! - Are not! - Am, too. - Are not! - Am, too. - Are not! Am, too. Am, too. I was here first. Just wait until Mom and Dad find out about this. Oh, yeah? You think they'd pick you over me? With your track record? You don't know anything about me. So that's how you wanna play it, huh? Let's see. Templeton, Timothy. Middle name.... I'm sorry. Leslie! - Mostly C's... - How do you know all that? Can't ride a bike without training wheels? Even bears can ride a bike

without training wheels, Leslie. DOB says you're seven. Seven and a half. Power nap! You were saying? I'm seven and a half. Exactly! You're old. It's time to make way for the next generation. It's the way of the world. You would never ask your parents for an old toy. Lam-Lam? Everyone wants the hot, new thing. Destroy. Destroy. - Lam-Lam! - I've got fresh batteries. Boom! Mom and Dad don't even know you. They love me! Oh, yeah? Do the math, kid. There's only so much love to go around. It's like these beads. You used to have all your parents' love. All their time. All their attention. You had all the beads. But then I came along. Babies take up a lot of time. They need a lot of attention. They get all the love. We could share. You obviously didn't go to business school. Look, Templeton, the numbers just don't add up. There's not enough love for the two of us. Not enough beads to go around. And then, all of a sudden, there's no place for Tim. Tim doesn't fit anymore. Oh, no! What about Tim? So keep quiet. Stay out of my way. Or there's gonna be cutbacks. You can't be fired from your own family. Can you? Wake up, little halflings! It's 7:00 a.m. Wake up, little half... What's the use?

Arise for a nutritious breakfast! It's 7:00 a.m. What's wrong, Timothy? Has that little dwarf made you blue? Mm-hmm. Then I shall cast upon him a great curse! He shall not pass! It's no use, Wizzie. He's got Mom and Dad completely fooled. If they knew what I knew, they'd never let him stay. Perhaps your parents need to be enlightened. With a great curse! They shall not pass! Yeah. I need to enlighten them... with proof! That's what I need, proof! Expose his dark magic! Testing, testing. Testing, testing. Maybe they can return him to the store... and get their money back! We could buy a bouncy house! Godspeed, Tim! It's 8:45 a.m. Ninja. Ninja. Ninja. Ninja. Babies everywhere! They're spreading. Mom! Dad! What's going on? It's an invasion! It's a play date! That's a keeper. It's a meeting, and you won't be attending. We'll see about that. Thank you all for coming here on such short notice. Now, before we begin... Yes, sir! - Sure is! - Affirmative! Jimbo, run some interference. Hey! - We babies are having a crisis! - Oh, no! - That's awful!

- Horrible! What is it? It's simpler if I just show you. Teddy, if you please. Let's put on a show. Here we go! Jimbo, hit the lights. You see, babies aren't getting as much love as we used to. Why? Have we been bad? No, Staci. But I'll tell you who is. Behold our mortal enemy. Puppies! No! That's exactly the problem. Puppies? What's the deal with puppies? Throughout history... people have loved babies more than anything in the world. We've always been a must-have item... number one on every wish list. Puppies were merely accessories. But all that changed when the puppies began coming out... with new designer models. Each one more adorable than the last. Remember the Labradoodle? The Peekapoo? The Chiweenie? Try to say "Chiweenie" without smiling. Not possible. Don't waste your time. We all laughed at the Shar Pei. And now it's number one in China. - Oh, no. - That's terrible! - Horrible! - Yes. And it gets even worse. Francis Francis, the CEO of Puppy Co, made this announcement. Teddy, roll the clip. And we are on schedule... to release the most adorable puppy ever. We're gonna launch it at the pet convention in Las Vegas! Watch out, world! It's gonna crush the competition!

- Yay! - No, Jimbo. No "Yay"! We are the competition! This is war. Puppies are winning, and babies are losing. Thank you, Teddy. And if this new puppy is as cute as we fear... it could put the baby business out of business, baby. That's awful! Bad news, baby! What are we going to do? My job is to find out exactly what that new puppy is... so that Baby Corp can stop it. And you're going to help me. - Genius! - Home run! You still got it, boss! Yay! Yay. Now, your parents all work for Puppy Co. So have you learned anything from them? - Yes, sir! - Sure did! Fantastic. Triplets, go! - A. - B. - C. - D. No, what have you learned about the new puppy? Yay, puppy! No, Jimbo! Puppies are evil. Staci, read back the notes. I can't read. What's it say? This is my team? A muscle-head, a bunch of yes men, and a doodler? - Exactly! - Affirmative! Good call. - Oh, yeah! - Nice one, BB! Gotcha!

Put that cookie down. Cookies are for closers. - Let's have another show! - No, Teddy! - How about a hug? - No more shows! Boss? - There's plenty of love to go around. - Go to sleep! Nighty-night. - Boss! - Boss! - What? - Parents! It's like they're having their own little meeting. - Isn't that adorable? - Who wants dessert? God, this is so humiliating. God, this is so humiliating. Wait until Mom and Dad hear this. Hey, Templeton, what you got there? Nothing. Hand over the tape. Never! Mom! Dad! Over here! - Hi, Timmy! - Hi! Anyway... Flower power! You can't get away from Johnny Law, simpleton. Fasten your seat belt. Let's go! Run, run, run. What? Hey! Uh-oh. Run, run, run. Catch, catch, catch. Yes! Oh, yeah! Let go, you little... Oh, look! The kids are finally getting along. That's nice. Sayonara! You wanna play? Let's play. No!

Save Boss! Save Boss! - Get him! - I got him! - I got him! - I got him! You're toast, baby man! Upsies, I need upsies! Who wants... Cheese sticks! Mom, Dad! I've got proof! Someone can't go down the stairs? Nothing can stop me! Mom! Dad! Where are you guys? Hello? Where did everyone go? Mom, Dad! The baby can talk! Oh, can he now? Wait, how did you... Hand over the tape, Timmy. Or Lam-Lam gets it, see? No! What's that, Lam-Lam? You want a nose ring? It's really not my scene, but who am I to judge? And an eyebrow ring? Seems like a little too much, Lam-Lam. How's that gonna look in a job interview? Stop it! The tape, Timmy! Or I'm gonna rip, rip, rip. No! Let go! - You let go! - You let go! - Give me the tape! - Give me Lam-Lam! Whoops! Too far. Templeton! Templeton, let's be reasonable. We can be reasonable, right? What are you doing? You've been asking for this since you got here! We can talk about this over a juice box! Time for juice boxes is over. No, Templeton. You wouldn't. Say bye-bye, baby! You're fired! What are you doing? Nothing.

My proof! Tim! Explain yourself! Yes, explain yourself. It wasn't me! It was the baby's fault. The baby's fault? It's true! He can talk. They all can talk. They were having a meeting. There's something about puppies. It's one big baby con-spy-racy! Timothy Leslie Templeton! We are very disappointed in you. - No, we're mad at you! - Exactly, we're mad at you. - Mad? - You need a time-out! - You're grounded! - Yes, grounded! - For two... - Three! - Three days? - Weeks! Weeks! Three weeks! For three... evers! Grounded? You're gonna stay in this house with your baby brother... until you learn to get along. Great.

Adult Tim: It was my first time behind bars. The big house. The lock-up. Grounded for life. The minutes turned into hours, the hours into days. Every man has his breaking point. This was mine.

Blackbird singing in the dead of night - Take these broken wings and learn to fly - Hey, that's my song. All your life You were only waiting For this moment to arise It's okay, little halfling. Perhaps I can be of some assistance. Blackbird singing in the dead of night!

Pray, take these broken wings and learn to fly! Fly, you fools! Thanks, Wizzie. But it's not the same. If only I could reach my magical shank. I could break us out of this big house. Templeton! Templeton, we have to talk. Go away. Blackbird singing in the dead of night Stop it! That's my song, not yours. My parents wrote it just for me. Really? Your parents are Lennon and McCartney? No, Ted and Janice. You don't even know their names! You're just trying to steal them from me. You stole everything! You're the one who should be in jail! Look, it's time we put our differences aside. Have you been... No! Where's HR when you need them? Take it. I don't want your filthy money. Look, I told you to stay out of my way. I can't! You're in my house. I don't wanna be here... any more than you want me to be here. Then why are you torturing me? The truth is I'm no ordinary baby. Well, no kidding. I'm on a mission from above. Are you the Baby Jesus? Yes. I'm the Baby Jesus. No! You see, I'm more middle management for the company. The company? What company? Here. Take this. It'll explain everything. What do you want me to do with that? - I want you to suck it. - You suck it!

No, it's for you to suck. I'm not sucking that! - Suck it. - I don't know where it's been! It's not where it's been. It's where it will take you. Don't you wanna know... where babies really come from? Binky. Papish. Nuk-Nuk. Boo-Boo. Bo-Bo. Bah-Bah. Chupie. Hushie-Baby. Tootsie. It goes by many names. But through its power, you will know the truth. Come on, faster! Mommy! Where are we? Welcome to Baby Corp! No way. - Thank you. - What? Relax. They can't see us or hear us. - We're, like, virtual and stuff? - Yep. - You mean they won't feel this? - Nope. - Or this? - Nada. Karate! Don't embarrass yourself, Templeton. I can still see you. So this is where babies come from? Where'd you think, the cabbage patch? Magic fairies? No, my parents told me that... What? No. That's disgusting. Yeah, it didn't sound right to me, either. I can't believe my parents didn't tell me about this. If people knew where babies really came from, they'd never have one. Same thing with hot dogs, by the way. Going upsies! So how come I don't remember this place? You did.

But after normal babies get their pacifiers taken away... you forget all about Baby Corp. How come you're not normal? A few of us, the best of the best... are selected for the... For the ultimate honor. Upper management. This, Templeton, is where all the action is. Nap time in Sector G. So this whole place is run by babies? Yep. My Dad says, "Those who can, do." "And those who can't, supervise." Your father is a hippy. What happens when you grow up? We don't. We drink a super-secret baby formula that keeps us babies forever. Back to work! Formula break is over! We're in a crisis here! Don't you know we're in a crisis here? Who is that? That is my boss. Big Boss Baby. What is she screaming about? Well, see this pie chart? Wow, it looks like a giant pie. It represents all the love there is in the world. - I love pie. - Who doesn't? - Apple. - Fine. - No, cherry! - Perfect! - Not pumpkin. - Okay. That's a vegetable. Point is, the puppies' slice is getting bigger and bigger. They're stealing all our love! Just like you did to me. Exactly. And if this keeps up... there might not be enough pie left for babies.

No pie? No pie. So, my mission is to find out what this new puppy is. So you're, like, on a spy mission? Cool! Yes! Cool! And if... When I succeed... I'll become a Baby Corp legend. Like Super Big Boss Baby, Mega Boss Baby... Seriously Big Boss Baby... and him. Now that's a big, fat baby. No, that's Big Fat Boss Baby. This is Super Colossal Big Fat Boss Baby. He was the youngest Chief Executive Infant in the history of the company. Was? What happened to him? Retired, years ago. But I still try and live up to his legend. In every situation, I ask myself... "W-W-S-C-B-F-B-B-D? "What Would Super Colossal Big Fat Boss Baby Do?" So that's all you get? Your picture on the wall? Come here! I'll get a promotion. The corner office... with my own private potty. Wow. So when you're done, you're coming back here? A-S-A-P, T-i-m. I'm not a family man. I belong behind a desk. - That's awesome! - I know, right? - Pew pew. - What? So help me, I will nail his diaper to the wall! Have we heard anything from that little Boss Baby... that we sent down to the Templetons? - I don't know. - You're fired! Oh, no. You're all fired! The pet convention is in two days.

If he doesn't come up with answers... he is fired, retired! - Gone! - Tour's over. What was Big Bossy Baby Lady screaming about? She's demanding actual results. The pet convention is in two days, and I've got nothing! That's her! Don't answer it! Stress nap! If I don't find out what that new puppy is and fast... not only will I not get that promotion... I could get fired! Hey, relax. I'm sure there's other cool jobs for babies, right? Meanwhile, two days goes by like that. You better start packing. What? You don't get it, Templeton. If I'm fired, they'll take away my formula. I will turn into a normal baby... and live here forever with you. - No! - Yes! And I promise you this... Every morning you wake up... I'll be there. Every night, at dinner... I'll be there. Every birthday party... I'll be there. Every Christmas! I'll be there Year after year after year. We will grow old together. You and I... will be brothers. Always. - No. No, this is terrible! - I know. - This can't be happening. - But it is! - You can't stay here! - I can't!

- Don't panic! - But it feels right! I know, but we have to fix this. We have to make sure you don't get fired. We? We. I will help you... but just to get rid of you. Deal? Deal. Here's to never seeing you again. Back at ya, baby. Now let's get to work. Come on, come on, come on. Slice! No, no. There's nothing here about a new puppy. Aren't you gonna do any work? I'm very busy delegating. He drains it! So once we find the file on the new puppy... what do we do then? Send in the baby ninjas? Even better. I'm going to write the perfect memo. - Boom! - Boom! Wait. What's a memo? A memo is something you write to give people information. That's your plan? You're gonna write a book report? That's so boring. No, Templeton. Memos are for important things. A memo can bring people together. A memo can be a call to arms... a manifesto, a poem. A memo can change the world. Wow! When you explain it like that... it still sounds boring. You'll learn, kid. You'll learn. Wait a second. This is it! What? What is it? Check this out. Take Your Kid to Work Day.

People take children to a place of business? Why? Because it's awesome! It's disgusting. Don't you see? We can get inside Puppy Co... and find out what the new puppy is! What's the point? You're grounded. Your parents aren't going to take us anywhere. You're right. They think we hate each other. Hate is a strong word. It's the right word, but still. We have to convince them that we're actual brothers. Right. That we... Loathe? No. Like! No. That we... La, la, la... Le, Le, Le... No. No way. No. You don't mean... Love each other. I just threw up a noodle and swallowed it. - Here comes the choo-choo train! - No. - Choo, choo, chugga, chugga. - No choo-choo! Hold the train! No! It looks like it's already been eaten! Who's there? I got a racket! What's going on in here? I'm just feeding the baby. They're watching. Choo-choo. Okay. Choo-choo on that. I don't wear nautical. It's not even Friday! Come on, you're putting this thing on! You gonna make me? You can't make me, punk. - What have you done to me? - Stop! - Get back here!

- No! No way. Come on! Tim, what are you doing in here? Oh, no. Hey, what's all the racket? Isn't he adorable? I've got one for you, too! Ahoy, matey! What? Bummer. Smile! Smile for the camera. It makes me feel weak. - Who's ticklish? - It doesn't work on me. - Here? - I'm dead down there. Come on, everyone has a tickle spot. "'I don't think I'll fit,' said Gretel." Come here, look at this. "'I could get in myself.' "And then, Hansel and Gretel... "pushed the wicked old woman into the oven. "And the godless witch was miserably burnt to death." Let me get this straight. The story is about cannibalism and burning people alive. Yeah. No wonder kids are so messed up! Getting along is exhausting. Back at ya, Tim. You should have seen your face in that picture. You were all... I'm not used to being tickled. Once at a corporate retreat. But those things always get weird. What? You've never been tickled? What about your parents? I'm sorry. I forgot. You didn't have parents, did you? Tim, I may look like a baby... but I was born all grown up. I can't even imagine not being a kid. You missed out on your whole childhood?

You never had someone to love you? You can't miss what you never had. Wake up, little halflings! Hey, Tim. Wake up, buddy. - What? - Rise and shine! Is something wrong? Am I fired? No, you're late for work. What? It's Take Your Kid to Work Day! And you're the kid. You're officially un-grounded. - Really? - Really. Can the baby come, too? I don't see why not. Yes! Yes, yes, yes! Yeah! I wish I was that excited for work. Look, it's my spatula. Yeah, baby. All right, gentlemen. Welcome to Puppy Co. Wow! This is awesome! And Tim, look! They have a puppy pool and everything! Isn't that sanitary? Hey, bud, you wanna get a picture with Puppy Co Pete? No, thanks. It's probably too scary for the baby. Nice call. Your dad and I have some work to do. You wanna come up to the office and hang out with us? We'll stick your brother in the Puppy Zone... while we have a little Tim time. Tim time? Dad and I know we haven't been able to do as much with you as we used to. So, what do you say? No, thanks. I'd rather spend time with the baby. - So cute. - That's so sweet. Way to keep your eyes on the prize, Templeton.

We find out what the new puppy is, and I go home. You guys stay in the Puppy Zone, okay? Okay, bye! That's where we'll find the secret file on the new puppy. We'll never get through that door. No, not that door. The doggy door. But how do we get past the guard? No, no, no. No way. No! Itchy, plushy, puppy pants! What a cute, little pup... Ow! Yay! Kids. Get down. All the way down. I've never been so humiliated in all my life. Arf! Hey! Fetch! What am I doing? Oh, no! Yes! What a good boy. No. No biting. Timothy Templeton, office ninja. - Over here. - What is it? It's gotta be in here. It's begging us to go in. Wow. That's a lot of paperwork. I thought puppies shredded everything. This is getting creepy. I've come for your soul. Cut it out! Wait! That's it! The file! See! I was right. No. I've seen this before somewhere. We've gotta find something to replace it with.

You're right. Like another file. Yes! A file with the same weight. So it can be placed in the exact same position. - With the exact same weight. - You already said that. I know I said it. Hey, you hit me twice. Make it a third time. Wait! I think I've seen one here. Smead manila, pressboard edges. About 50 ounces. No, 49. Try this one. Wait! Now it's perfect. Yes! I feel like we should run. I know, but it's just so mesmerizing. I kind of wanna see how it ends. Yeah, me too. Well, that didn't end well. What? What the...? Thanks for dropping in, kids. Francis Francis? I see you've met my big brother, Eugene. A man of few words. None, in fact. Can you put your head back on, please? What is all this? Surprise! A Baby Corp binky? Where did you get that? You don't recognize me? Perhaps from my youth! Super Colossal Big Fat Boss Baby? He is him? And him is you? Except older and wrinklier. That's not right. No. You were my hero! How did you end up here? You know what I do to little kids who ask lots of questions about me? Eugene! I read them my story. And, I baked cookies! Eugene, my chair. Now, it all started at Baby Corp...

a long, long time ago. I was a hotshot executive... headed straight to the top. Everyone loved me. They gave me a promotion, the corner office... my very own... Personal potty? I had it all. But then one day... I made a terrible discovery. I was getting old. The formula wasn't working anymore. It turns out I was lactose intolerant. - No! - Yes! I got called in to see the board of directors. Who are the boring directors? The biggest baby bosses of them all. I thought they loved me. But they replaced me with someone new. Someone younger. That's horrible. All of a sudden, she got all the love... all the attention. You know how that feels, don't you, Tim? It hurts, doesn't it? Yeah. It does. And then what happened? Well... They fired me! And took away my special formula. Then they sent me down to live with a... - family! - Oh, Francis, no! Baby Corp betrayed me! And I'm finally going to get revenge... with the Forever Puppy. - Huh? - That's it? No, no. Imagine a puppy that never grows up. A puppy that stays a puppy forever. Once I launch my Forever Puppies to every corner of the world...

they'll be so adorable... How cute! ...no one will ever want a baby ever, ever again. The end of Baby Corp! Please. A puppy that never grows up? That's impossible! Isn't it? It was, until you brought me the key ingredient. My secret formula. It's mine! It's mine! It's all mine. No! You brought me the very thing I needed to destroy Baby Corp. - No! - Yes! You walked right into my trap! - You'll never get away with this! - Yeah, not if we... What? Tell? Who are you gonna tell, Tim? Your parents? Where are the boys? I told them to stay in the Puppy Zone. I'm taking them both with me to Las Vegas. So stay out of my way. I'd hate for them to get terminated. They'd never leave us alone. Oh, really? Wait until they meet Puppy Co's certified... in-house childcare expert. Oh, no. - Don't be nervous, buddy. - It's only overnight. We'll be back before you know it. Besides, you boys are in great hands. That's right! Eugenia is practically perfect in every way. No. Please don't go with him. Francis Francis is trying to... Believe me... Eugenia won't take her eyes off your children.

Not for one second. That's very reassuring. Now you see them. And now, you don't. Too-da-loo! To the airport! It's over. I'm through. What do we do, Templeton? What do we do? We have to get to the airport and stop Francis Francis... before the plane takes off! Yes! But how do we get past Scary Poppins down there? Okay. There must be something we can do. Hey, it's not that bad. Are you okay? What's the matter with you? Don't look at me! Oh, no! Without that formula, I turn into a normal baby. You know, goo-goo, Ga-ga. The whole bit! Oh, no! Gross! I'm a ticking baby time bomb! I'm going to turn into a puking, pooping, helpless baby! Wait a second. That gives me an idea. What? What is it? I've been through a lot of babysitters... and they all fear one thing. Now, ladies, the secret to deep fried butter... is a healthy dab of margarine. Hey, Mr. Lady Man! The baby. I think he's sick! You gotta do something! Oh, the horror! - Templeton! - Delicious! Gross! It got in your mouth! It got in my mouth, too! I think I'm gonna be sick! Swirly! There's only an hour

before the plane takes off. Let's take the bike. The bike? I don't know. Let's move! - Okay, but wait right here! - What? Where are you going? Templeton! Always wear a helmet. Too-da-loo, toilet head! You'll never catch us! Staci! Staci, come in! Oh, Staci! - Is that you, boss? - Code red! I'm being chased by a killer babysitter! Gather the team! On it, boss. - Hello! - Hello! - Hello! - Code red. Got it! We got a code red. Repeat... We got a code red! What are you doing, Templeton? Go, go! But that's jaywalking! Here, I'll pay your ticket. Go! I think we lost him! Oh, no, we didn't! Flower power! Pow, pow, pow! That's my boy! Poppy! Run, run, run. Uh-oh. Run, run, run. Tim, you've gotta go faster! I can't do it! You can. You've got it in you, Templeton. Now, eyes ahead. I said eyes ahead, son! Buttocks up! Now pedal like you mean it!

Either you run the day, or the day runs you. Good! Uh-oh! My training wheels! I can't ride without training wheels! Whether you think you can or you think you can't, you're right! What are you talking about? The path to success is not a straight line, Templeton... but rather a wild ride... like a ship at sea. And you're a sea captain... taming a turbulent ocean! I'm a sea captain, taming the ocean! Good! Tree! I'm gonna hit it! Aim for failure, and you'll always succeed. - What? - Aim away from failure! I'm doing it. I'm doing it! Once success is a habit... then it's all downhill. Look! There they are! Mom, Dad! - Train! - Choo-choo! Stop! What are you doing? - We're gonna make it. - But I don't have a quote for this! You did it! No! We did it. And all without your training wheels. Coming through! Baby on board! Hang on to your diaper! Duck and cover! Hold it, buddy! I'm gonna need a strip search on two. There they are! Mom, Dad! Hey, not so fast! Oh, no. Templeton! - Hey! - Sorry!

Hey, where'd you go? Oh, no! Not again! Not now! What the...? No, no, no! Come on! I think I ate $1.75. Excuse me, coming through! Mom, Dad! Hurry now! Move! We don't wanna miss our flight! - No! - I warned you! Wait! - No! - No. Mom, Dad! Stop! No! No, no, no. They're gone. I failed. I would've gotten to my parents if I didn't have to go back for you! What? We would have been here in plenty of time... if you knew how to ride a bike like a normal kid! We're never going to stop the launch on time. Who cares? My parents are in danger. I care! Baby Corp is going to go out of business. That's all you ever talk about. You don't even know what it's like to be part of a family. And you don't know what it's like to have a job! You don't know anything about hugs, or bedtime stories, or special songs! Oh, please! Stop acting like a baby. You're a baby! You take that back. My life was perfect until you showed up! Believe me, kid, the feeling is mutual. I wish I'd never met you! I wish you'd never been born! Where are you going?

Fine! Blackbird singing in the dead of night Take these broken wings and learn to fly All your life You were only waiting For this moment to arise Would Timothy Templeton please pick up the white courtesy phone? Timothy Leslie Templeton, please pick up the white courtesy phone. Leslie. Hello? It's me. Don't hang up, Tim! Tim, I wasn't born. I was hired. What do you mean? Baby Corp is the only home I've ever known. So you're right. I don't know what it's like... to be part of a family. But I do care. You do? Yeah. And the only way to save both is to stop Francis Francis. Yeah. I can't do this without you, Tim. I need you. - I guess we do make a pretty good team. - No. Literally, I can't reach the door knobs. Oh, right. Don't worry, Tim. We're gonna save your parents. And your company. But how do we get to Vegas now? We're gonna need a miracle. Follow that Elvis! Why? Where there's Elvis, there's Vegas! There's another one! And another one! Elvises everywhere! Tim, there's our flight! And there goes our ticket! Hey! Don't be cruel! Sorry!

- Well, thank you! - Oh, baby! Well, thank you very much. Hello. Hi. Ticket please. One moment. It's been stolen! Impersonating an Elvis impersonator? Get him! Humina, humina, humina. Stop! The ghost of Elvis! We gotta find seats! Come on, this way! What is this place? This, Templeton, is first class. Why is it empty? No one can afford it. That's what makes it so wonderful. Hello! This is Captain Ross. Ladies and gentlemen, and those in coach... please fasten your seat belts. We're about to take off. What's the matter, Templeton? My parents always hold my hand during takeoff. Boy, the stocks are crazy today. Ladies and gentlemen, Captain Ross again. As you can see, I've switched off the seat belt sign. What are you two boys doing up here? We're Captain Ross's kids. He told us to sit here. Well, can I get you special guys anything? Anything? Anything. Aye! All right, Francis Francis. This will teach you to kidnap the parents of One-Eyed Tim. Oh, please. If only it were that easy. What's your plan? You're not gonna write a memo, are you? No. Come on. You said you never really had a childhood, right?

Why don't you give it a try? - No, I can't. - It's fun! Here, let's get you into character. I don't know. I feel silly! Go on! Say something mean to him. All right, all right, all right. So, you went to a community college, is it? I don't know. Keep going! And you have the guts to ask me for a bonus, now? See! Now you're getting into it. Huh? Well, blow me down. Your exit interview is over! That was pretty good. Who was that guy anyway? - The captain! - What? En garde! Heave! Ho! Thar she blows! Watch your stern! - Aye! - Dodge, parry, and thrust! Sounds like a heck of a law firm! Nice try! Heads up! You're fired! And here's your severance package. Ha! Wait. You're not supposed to end with "Ha!" You're not? You're supposed to end with "Argh!" Got it! Argh! That's great! Thanks! I just went with the flow. Ladies and gentlemen, and those in coach... on the left side of the plane... you can see we're approaching fabulous Las Vegas. Land ho! Ahoy, matey. Bye, Dad! Thanks for the lift! - Okay. What?

- Let's move. - Going to the Heartbreak Hotel? - I'm going to the Heartbreak Hotel. - Me, too! - Me, too! Me, too! We've gotta get to the convention center. Should we get a taxi? Darn! I spent all my per Diem. That's more our speed. Right. Excuse me, ladies. Can we get a ride home? Jimmy's been sick, and he needs his expensive medicine. Where do you live, sweetie? The convention center. Bye, sweetie! Have a fun lady party! Chicks dig babies. The people of Long Island do not know how to make an iced tea. Oh, no! How are we gonna find my parents in here? Tim! Over there. Okay, now where's Puppy Co? Puppy Co, Puppy Co, Puppy Co... Aha! Here it is. Found it! But how did you...? Hey! Where'd you go? Not again! Come on! I need you! I'm back! I'm back. What's going on? That's right. We're gonna launch a brand new puppy in every continent. In every country! We're going to take over the world, one heart at a time. - Tim, there they are! - Mom, Dad! Imagine a puppy that never grows up... never gets old. A puppy that stays a puppy forever.

I give you the only thing you'll ever love... the Forever Puppy! Mommy? Avert your eyes, Templeton! Hey! What are you doing here? Mom, Dad! What are they doing here? What are Tim and the baby doing here? What are any of us doing here, really? What is going on here? He's got my parents! We're really here to get them. Get them! Get the Forever Puppy! We've got to get backstage. In there! Run! Go, go, go! Left, right! Left, right! Left, right! Yes! Fart. Poop. Doodie. Look at all that formula. Now that's how you launch a product. Oh, no! He's putting them under the rocket! Elvis has left the building! Mom, Dad... I'm coming! Atta boy! Go, Tim! Go, go! Launch initiated. I'm launching my Forever Puppies, and there's nothing you can do about it! No! Baby Corp stole all the love from me... and now I'm going to take it back from them. You should understand what I'm talking about. You got replaced just like me! No! I'm nothing like you! Bratty kid! Let our parents go! His parents. The parents. Yeah! You could have had your parents' love all to yourself again! But no! You blew it! You let that baby boss you around.

He doesn't work for me. We're partners! I'm not ticklish. Hey! Where's the baby? Everyone has a tickle spot! My ears! Stop it! Little brats! Nothing is going to get in the way of my vengeance. Not you, not anybody! Baby Corp is through. I win! Ha! Wrong! You're not supposed to end with "Ha!" - That's right! - What? You're supposed to end with... Argh! En garde! You're fired! And here's your severance package! Take that, you scurvy scallywag! Argh! One minute and counting. - Help! - Anybody! Tim! What are you doing? No! Mom, Dad, I'm coming! Is that you? Don't worry, Mom and Dad. I got this! - Are you okay? - Is the baby all right? Yes, the baby's fine. Who was that? That was me! The baby's fine. It won't budge! What's happening? Wait a second! Hey. I know a way to move my parents. - How? - We can use the puppies! Upsies.

I need upsies. But what if you "go baby" again? It'll be fine. Fine, fine. Fine! It'll be fine. Hang on to your diaper! We're moving! Why are we moving? All right, Mom and Dad, hang on! T-minus 30 seconds. Oh, no! Wait! Hold on! Go, Tim! Get your parents... out of here. You've gotta jump! Come on, it's a piece of cake! No! No patty cake! Get down! Don't cry. I'm sorry. Please don't cry! 20 seconds. 15 seconds. Blackbird singing in the dead of night Take these broken wings and learn to fly All your life You were only waiting For this moment to arise - Three... - Gotcha! ...two, one. Blast off! Yeah! Hey, are you still in there? Aha! What happened? Did we win? - We won! - We won? - We won, we won, we won! - We won! Yes! Victory nap! You ruined everything! It's not fair! It's not fair! That's not right. Now you're really going to pay! Oh, yeah? It's time you pick on someone your own size! What? Eugene! You put me down!

You hear me? I am the boss of you! This time, we'll raise him right. I'm sure that's gonna turn out fine. Tim, what's happening? Mom, Dad, hold on! Yes! - Tim? - Tim! Tim! Are you okay? I'm fine. We're fine. You saved us. You're our hero. And a great big brother. We love you both so much. Both of us? With all our heart. Let's go home. How do I look? You look great. Well, team, good job. Staci, this letter should get you into the school of your choice. - Kindergarten? - That's right. And if there's anything else... How about a raise? Staci, you don't get paid. - One million ziggity-five! - Eight! - A tricycle! - Skates! - Candy corn? - Lollipop! Deal. Best boss ever. And you guys don't always have to toe the company line, you know? It's okay to think for yourself. - No, sir! - No way! That's a terrible idea! That's the attitude. - You're so right! - You've got it, sir! - You're the man! - Absolutely!

Here you go, big guy. You've earned it. You wanna hug me, don't you? I'll miss you too, buddy. Okay. - There, there. - It'll be okay, big guy. So... you did it. No. We did it. By the way, congratulations on your promotion. The corner office, the private potty. All that stuff. But, hey! How about you? You have your parents all to yourself. So what am I gonna tell Mom and Dad after you leave? Don't worry. Baby Corp has a procedure for situations like this. It'll be like I was never born. I almost forgot! No way! Lam-Lam! - You fixed her. - Yep. She's as good as new. She's a tough one. Well, I guess we both got what we wanted. It's a win-win. Probably should... Yeah. So, stay in school. I don't really have a choice. Yeah, right. - Goodbye, Tim. - Bye. Yeah, right. He left as suddenly as he arrived. Bye. Finally, my life was perfect again. Forget about the baby. Oopsies! Pardon me, big fella. Surprise! Hooray! Forget about the baby? No, thanks. I'm good.

Okie-dokie.

Tim: [voice over] Dear Boss Baby... I don't usually write very much... but now I know that memos are very important things. Even though I never went to business school... I did learn to share in kindergarten. And if there isn't enough love for the two of us... then I wanna give you all of mine. I would like to offer you a job. It will be hard work... and there will be no pay. But the good news is that you can never be fired. And I promise you this. Every morning when you wake up, I will be there. Every night at dinner, I will be there. Every birthday party, every Christmas morning... I will be there. Year after year after year. We will grow old together. And you and I will always... ...be brothers. Always.

Wake up, little halflings! It's 7:00 a.m. What's the point, Wizzie? Because it's 7:00 a.m. I have one job to do, and you make it so difficult. It's okay, little halfling. Sometimes, I get confused too. Especially during daylight savings time. Spring forward, fall back. We don't even have calendars in the wizard's realm! There is no spring, only darkness and winter! I'm not confused at all, Wizzie. I just miss him. Tim, look who's here! It's your new baby...

Tim: Brother! You're here! You're really here!

Gentle, gentle. You came back! Say hello to Theodore Lindsey Templeton. Lindsey? Who's ticklish? Who's ticklish? Here you go.

Adult Tim: So, that's my story. Our story. Luckily for me and my little brother, it had a happy ending.

Is that a true story, Daddy? Well, sweetie, that's how I remember it. - But you know what I found out? - What? There's plenty of love for everyone. Even me? Especially you. Just ask your Uncle Ted. Hey, kid, I hear you're gonna have a baby sister. I wanted a horse. Here you go, kid. Go get yourself a horse. You know, I'm proud of you, Leslie. Back at ya, Lindsey. Hi there, baby sister. All right, guys. Time for bed. Come on, Mom. Just a little longer. Okay.

Wizzie: Wake up, little halflings! It's time to leave. Go and live your peasant lives. Be gone with you!

---
## [owi92/tobira](https://github.com/owi92/tobira)@[2a9add1e61...](https://github.com/owi92/tobira/commit/2a9add1e615f0c545f7aa1a6e2aea0b0820d9de6)
#### Tuesday 2023-01-24 17:56:12 by Lukas Kalbertodt

Add framework for authentication (authkit) and use it for local dev setup & test deployments (#645)

Closes #550 

See the referenced issue for motivation. Can be reviewed commit by
commit, but reviewing all in one isn't bad either.

As you can see from the changes, our framework does more than the
previous `login-handler.py`: it sends the `POST /~session` request to
Tobira itself. That means no `X-Accel-Redirect` magic is needed, making
the nginx simpler.

The main part is done, but this is still a draft for a number of
reasons:
- [x] Decide on name and scope for the NPM package. ->
`@opencast/tobira-authkit`
- [x] We want to potentially also implement `auth.mode =
"opencast-users"`. In that mode, Tobira would handle `POST /~login`
requests itself by just asking Opencast if the login data is correct.
That should be fairly easy to do. And I think it's very useful: it's
_the_ obvious auth system Tobira should support and I assume quite a few
institutions want to use it. Further, even if an institution wants a
different auth system in the long run, just using Opencast users is a
very simple way to get everything running. Without auth system, you only
see an empty Tobira which is quite underwhelming. So this would
drastically improve the "first setup" experience IMO.
- [x] ~~I also noticed that we might want to simplify login handlers
even more by adding yet another mode. In that mode, Tobira would forward
`POST /~login` requests to a configured HTTP service which would send
back appropriate auth headers. This is little work in Tobira and that
way, the nginx config could be a lot smaller still, again making it
easier to set up Tobira.~~ -> I still think it's useful, but we won't do
it now.
- [x] Once all the previous points are decided: update docs
appropriately. -> Done with NPM package name `@tobira/authkit` for now.

So yeah, I'd like to talk about the two additional auth modes and
whether we want them. Of course they could be implemented in a separate
PR. But it would also be nice to only needing to rewrite the docs once.

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[50e2eb7195...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/50e2eb7195ce633aa42c10e86efc652ea436304e)
#### Tuesday 2023-01-24 18:27:24 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[5e80257423...](https://github.com/tgstation/tgstation/commit/5e802574231c9c6fe835c40b55f2c8aa9f1c68b4)
#### Tuesday 2023-01-24 18:34:30 by Jeremiah

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
## [Rapandrasmus/HeavenStudio](https://github.com/Rapandrasmus/HeavenStudio)@[54c4899f9d...](https://github.com/Rapandrasmus/HeavenStudio/commit/54c4899f9d31999a946e006c6c9b8235bdc1c778)
#### Tuesday 2023-01-24 18:42:08 by AstrlJelly

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
## [AnoymTDS/HTML5-CLASSES](https://github.com/AnoymTDS/HTML5-CLASSES)@[69beee3103...](https://github.com/AnoymTDS/HTML5-CLASSES/commit/69beee3103c62e354f424e310f6b64ad3897656e)
#### Tuesday 2023-01-24 19:09:59 by AnoymTDS

Rename Brain Teaser4 to Brain Teaser4.html

A malicious user who works in the dark web uses a certain method to trick unsuspecting victims. He started by using 3 different tags by default. The first tags makes reference to the uniformity of linkswhere we have multiple links rangung from 0-9 sent to one email address. The other tags are focused on phone numbers and a text file  is this "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life"

---
## [sexy90gxebattlefactoryplayer/pokemon-showdown](https://github.com/sexy90gxebattlefactoryplayer/pokemon-showdown)@[d19c762ffc...](https://github.com/sexy90gxebattlefactoryplayer/pokemon-showdown/commit/d19c762ffc8757af8ef227570f82dd6b4f0378ef)
#### Tuesday 2023-01-24 20:11:16 by sexy90gxebattlefactoryplayer

Gen 8 Battle Factory: Remove Band set from Ubers Darmanitan-Galar 

Credentials: https://cdn.discordapp.com/attachments/1042959218208157696/1067534457160089731/image.png (i am "lost wind's elegy")

Darm-G's firepower is just fine with scarf; there aren't many (if any?) relevant 1hkos or 2hkos you miss out on compared to band. The only one I can think of is missing out on the OHKO vs Sp. Def Necrozma Dusk Mane, and nobody's leaving their NDM in anyway + you probably have like 12 other things to deal with it.

Without scarf, however, you miss out on really good source of offensive checking and revenge killing potential. Scarf outspeeds huge threats like non scarf Yveltal, Eternatus, Calyrex-Shadow, etc. 

What sparks had to say about band darm in proper SS Ubers:
sparks — Today at 1:53 PM
not really but with band building needs to be more focused cos the speed over the 90s and etern etc is insane with scarf

sparks — Today at 1:54 PM
while with band you're very much focused on "how to take out ndm and capitalize while not being weak to ho"

As a secondary factor, it would make Ubers in BF a lot better. Currently you have to not only win the coinflip of what move Darm clicks but also the coinflip of what item it is. Both of these are more or less up to random chance.

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[979b26d52e...](https://github.com/Thunder12345/tgstation/commit/979b26d52e09dcaa7ad00ce07c1e16760dbd7cb2)
#### Tuesday 2023-01-24 21:47:06 by tralezab

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
## [zerbina/nimskull](https://github.com/zerbina/nimskull)@[d30cba58c0...](https://github.com/zerbina/nimskull/commit/d30cba58c0c2c8bc353f51240f84eadaf19ebdc5)
#### Tuesday 2023-01-24 23:15:47 by Saem Ghani

Extract nkError diagnostics data

`nkError` has a `reportId` which unfortunately opens any possible
"report" crawling its way in there. This commit introduces a new
design where `nkError` owns it's diagnostic data, as well as,
`ast_types` where `nkError` and friends are defined, owns the data
types. `Report` and all the associated cruft now is there simply to do
rendering.

`Report` still handles, routing and final consolidation, but in future
developments that will likely evolved further.

Overall Change:
- AST/Sem drop `ReportId` and associated memory leak
- AST/Sem now define a diagnostic type and are primary data owners
- `Report` is now used in legacy situations and rendering, the former
    is to be addressed in future commits

What didn't change/major caveats:
- `structuredReportHook` still uses `Report`, this consequences...
- `concept` and `{.explain.}` related erros have regressed, their tests
    marked with known issue, as this isn't a full conversion
- diagnostics involving magics, have inconsistent rendering, a pre-
    existing issue, sorting this out is future work

Lessons and Takeaways
=====================

Each module should own/define the data types that it's fundamentally in
charge of. Modules which are effectively components, like `lexer`,
`parser`, `vm`, etc, should produce diagnostics, events, telemetry,
whatever and their caller should handle output/rendering of these. The
key part about that last point is that the renderer and its format must
not be pushed into these modules, rather the renderer should consume
what they produce (directly or via an intermediary/translation).

For those wondering about why a value type was use inside the `nkError`
instead of the current `ref object`. I ran 3 bootstrap runs with each
version of `nkError`, and with the `TAstDiag` (value type) was
consistently ~10% slower during the bootstrap process.

|run|type|real|user|sys|
|:----|:----|:----|:----|:----|
|1|pastdiag|28.675|27.056|2.527|
|2|pastdiag|28.184|26.663|1.372|
|3|pastdiag|28.276|26.682|1.446|
|1|tastdiag|31.562|29.245|3.236|
|2|tastdiag|30.453|28.413|1.871|
|3|tastdiag|30.368|28.311|1.896|

|type|real|user|sys|summary|
|:----|:----|:----|:----|:----|
|pastdiag|28.38|26.80|1.78|avg|
|tastdiag|30.79|28.66|2.33|avg|
|pastdiag| 0.20| 0.17|0.50|avg dev|
|tastdiag| 0.51| 0.39|0.60|avg dev|

The report data types are rather bloated, eg: using `Int128` for
enum `high`/`low` values.

For diagnostics, it's best to capture very little data, and then query
within the rendering layer. Temper this where querying is reproducing
complex analysis, reconstituting heavy context, or keeping data large
data sets alive just so it can be queried later.

It's very possible we don't clean-up the symbol table of abandoned
analyses. This likely results in space leaks, or rather an overhead
while processing each module.

This style of conditional `0 < foo` is forbidden, it's just not
accessible code and prone to reasoning and ultimatley logic errors.

When doing inline error state representation in a data type, such as
`TLineInfo`, where the invalid state is
`TLineInfo(line: 0, col: -1, fileIndex: InvalidFileIdx)`, the default
initiatlization of objects is not our friend. This became a minor issue
during `nkError` construction. Where the line info on the provided
`wrongNode: PNode` parameter might be invalid. Hard to say, as the
default initialization is technically a valid location. A heuristic was
put into place to work around it and I think it'll hold until we fix it
properly. I see this as a language design problem, now one could argue
that a better selection of invalid state is required, but when working
in a retroactive case such as this, it's a non-starter. Furthermore, the
ergonomics of `{.requiresInit.}` leave much to be desired. I'm not sure
what exactly the answer is, but I think this is the difference between
something very primitive like a `struct` vs an actual `object`.

A number of node consts sets in `ast_query` and related modules are not
defined as compositions of each other. This can easily lead to changes
that only impact partial parts of the compiler and introducing yet more
bugs. This might be worth of a compiler style guide remark.

Just like a large amount of imports is likely a source of issues, so are
broad exports, avoid these like the plague. Removing these from
`reports` and related modules resulted in a number of significant and
hard to debug errors -- first encountered within CI, via a `bors try`.
They manifested as a doc gen build failure, which was seen as an
undefined symbol error. All because `reports` and friends were
exporting large swaths of other modules, eg: `ast_types`. After much
debugging and fixing error diagnostics to provide recursive dependency
detection as part of those unindentifier errors, it was fixed. It wasted
an entire day. Exports just create massive public surfaces, don't do it.

Details
=======

Finally, this commit impacts a very wide swath of the compiler, lots of
code had to be updated, along with many stylistic fixes. What follows is
a list of more detailed changes, in no particular order:

`ast_types`/`nkError` higlights:
- defines all its own diagnostic data types for `nkError`
- design-wise, `nkError` nodes are now much more likely to contain the
  immediate ast they're taking the place of, like a true wrapper. This
  should allow for easy recovery by simply getting `n.diag.wrongNode`.
- call mismatch related types (`SemCallMismatch` and `SemDiagnostics`)
  moved to `ast_types`
- moved `NodeId` into `ast_types from `packed_ast`, so it can be used
  more broadly, such as in `PAstDiag` as mentioned above.
- Removed `ReportID`, instead `PAstDiag` uses the `NodeId` of the first
  error node they're embedded in` as their `diagId`. This is an easy way
  to have a monotonic sequence, while also some correlation between diag
  and error node. Due to copies, the `diagId` and `PNode` `id` can
  diverge, but that's useful information in and of itself.

`ast` procs like `newNode` no longer have to care about `sons` on
`nkError` nodes, this also stops accidental traverls.

`ast_query` literal node kind `const` as sets
  Now, various const set ranges relating to literals were defined
independently, now only the smallest sets are, while bigger sets are
defined based on the smaller sets. Going forward, this should ensure
adding new node kinds updates all broader ranges.
  means: `nkLiterals* = nkIntLiterals + nkFloatLiterals + nkStrLiterals`
  Extracting a style guide remark out of the commit message would be a
good idea.

`msgs` now bridges translating `PAstDiag` to legacy `Report` for routing
and rendering. Although, routing should probably not be part of `Report`
stuff.

Moved illformed ast message creation routines earlier in `msgs` to
reuse them when generating legacy report message strings. String
generation should move to a rendering layer in the future.

More consistent VM/Gen event to AST diag mapping, mostly within
`compilerbridge` which now has simplified/fewer pathways.

Removed `traceReason` from VM stacktrace events
  This includes legacy reports, the primary motivation is that it was
being captured and not used. Additionally, not all stacktraces can be
related back to a meaningful vm event.
  Also, the fixing up of data types also resulted in some code
simplification in vmgen and sem.

Clean-up identifier errors and fix vm err location
- cleaned up various expected identifier messages
- vm errors now capture instantiation info correctly
- errors don't set location data on diagnostics if already present, to
  honour overrides

Diag mapping in `vm` and `vmgen` was updated.
Mapping `vm` and `vmgen` events to `PAstDiag` are presently in their
respective modules as they both directly depend upon `ast_types`. Not an
ideal situation, but a lot more refactoring is required until `vm` is
free of AST knowledge/dependencies.

`options` module now manages `ReportSet` as a simple collection of
`NodeId`s of diagnostics that have been reported.

Removed `ConfigRef` param from `types.typeMismatch`, it wasn't being
used

Report Output and Generation Details
====================================

Better error for `is` with wrong number of args:
- previously: `wrong number of arguments`
- now: `'is' operator takes 2 arguments'
- fixed `tests/errmsgs/tmisc` test to match wording

Undeclared identifier errors now output any recursive modules imports
that were detected as those can be a cause of such errors.

Recursive dependency tracking from the importer is cheaper, as it now
only stores FileIndex pairs. Unfortunately, we don't have a clearing
mechanism, so new minor space leak. :/

removed some eager diag message data querying

Fixed doc gen error report rendering, which weren't outputing the full
text, making it impossible to find where errors/hints/warnings were
occurring. Without this fix, it meant an unclosed backtick in a doc
block was breaking CI... cool.

Legacy Report Related Change Details
====================================

Removed some bounds tracking in reports
  A number of `Report`s are tracking, but never using a pair of `Int128`
in order to know out of bound issues for arrays, ranges, ordinals, etc.
  The data is rarely if ever output in messages and that's a lot of
bytes in most cases. Disabled whereever this was inconvenient, it can be
restored for error messages we wish to improve as future work.
  Created `rsemBigOrdsEnergy` to not overload `mismatchCount` tuple with
`Int128` bloat, and moved the following reports there:
- `rsemSetTooBig`
- `rsemArrayExpectsPositiveRange`
- `rsemInvalidOrderInEnum`
(partial list)
  No longer capture `countMismatch` data for these as it's unreported:
- `rsemExpectedLow0Discriminant`
- `rsemExpectedHighCappedDiscriminant`
(partial list)

The `errorKind` property now returns a `TAstDiagKind`

Errors related to positions in calls where identifiers are expected have
been updated to provide a bit more context:
- dot calls, callable fields access, etc errors wording update,
    indicating the problematic identifier and then the call expression
    within which it was found. See:
    `rsemExpectedIdentifierWithExprContext` handling in `cli_reporter`
- updated `astrepr` to handle new `diag` field of `nkError` variant
Resulting in the following test changes:
- `nimsuggest` test `tchk1` updated for messages with "found" wording
    instead of "got"

`countMismatch` in reports are now `int`s, instead of `Int128`,
seiously, how many were we expecting?

The string value of `mSizeOf` as `"sizeOf"` was taken from VM tests, but
doesn't jive with other tests that serialize the same magic. Need to
figure out which convention to go by.

Regression/Caveat Details
=========================

`concept` and `{.explain.}` error msg regression
  The compiler presently doesn't emit useful diagnostics for these,
simply a count of number of diagnostics failed. The implementation is
tied up with `structuredReportHook`, which in turn uses `Report`, and
there isn't a reasonable way to turn this into `PAstDiag` for
consumption. The following tests are disabled `knownIssue`:
- tests/lang_experimental/concepts/t3330
- tests/lang_experimental/concepts/texplain
- tests/lang_experimental/concepts/twrapconcept

Misc
====

Noted issues with the `reports` module and friends, hopefully it wards
off any further profileration and people can help with incremental
rework.

`types.semReportTypeMismatch` no longer takes a `ConfigRef` parameter.
This turned out to be unnecessary/unused after all the diag changes.

`sigmatch` has fewer dependencies on `reports_sem`

`getReport` moved to `msgs`, dropped `conf` param

Creating a new use qualifier diagnostic via
`semstmts.newSymChoiceUseQualifierDiag` will assert that there are at
least two choices to avoid spurious errors.

Removed a number of compile warnings by removing unused imports.

updated `astrepr` to use ast diagnostics from `nkError` nodes.

Reduce broad exports by `Report` related modules:
- `reports` was leaking `ast_types` _everywhere_
- `reports_base` had overlapping exports

Formatting/Style clean-ups in these modules

Random Report Changes:
- remove `rsemUserRaw`, it's never used
- renamed `rrsemCompilesError` to `rsemComplesHasEffects`

Special thanks to zerbina for all the code reviews and suggestions!

Co-authored-by: zerbina <100542850+zerbina@users.noreply.github.com>

---

