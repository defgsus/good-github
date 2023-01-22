## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-21](docs/good-messages/2023/2023-01-21.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,953,099 were push events containing 2,582,531 commit messages that amount to 155,377,736 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [gitster/git](https://github.com/gitster/git)@[6c065f72b8...](https://github.com/gitster/git/commit/6c065f72b8d581eee53ab82e82da049ee492bf11)
#### Saturday 2023-01-21 00:20:39 by Jeff King

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[19fa1ae808...](https://github.com/git-for-windows/git/commit/19fa1ae808fa94752302eb180ab5b2a76f022a5a)
#### Saturday 2023-01-21 00:22:46 by Johannes Schindelin

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
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[91a4590aa2...](https://github.com/clintjedwards/gofer/commit/91a4590aa27985263d9269109585275aefeb7421)
#### Saturday 2023-01-21 00:36:02 by Clint J Edwards

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
## [SteelMagnolias/PowerPlay2023](https://github.com/SteelMagnolias/PowerPlay2023)@[d2ceff589f...](https://github.com/SteelMagnolias/PowerPlay2023/commit/d2ceff589f856cece31dd1e6a9d63d4f5fa1adba)
#### Saturday 2023-01-21 00:50:39 by Abigail

separate manual and levels

Both manual and levels are working, but while the arm is moving, the manual controls cannot be used.  Pay attention to alreadyMoving variable which will tell you when the arm is moving during the finite state machine.  God sorry i messed this up the first time, my brain has literally been going in circles for like the last 12 hours.

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[9821251d81...](https://github.com/ARF-SS13/coyote-bayou/commit/9821251d8178f6ed89c4cadfec051d38beae4658)
#### Saturday 2023-01-21 01:07:40 by Superlagg

Merge pull request #1481 from ARF-SS13/Fuck-you-github

Map adjustments!

---
## [Saraistupid/HeavenStudio-Android](https://github.com/Saraistupid/HeavenStudio-Android)@[54c4899f9d...](https://github.com/Saraistupid/HeavenStudio-Android/commit/54c4899f9d31999a946e006c6c9b8235bdc1c778)
#### Saturday 2023-01-21 01:23:39 by AstrlJelly

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
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[5c6f5439b7...](https://github.com/pytorch/pytorch/commit/5c6f5439b7e6a5e63a68b36b4cf093a00d46e8be)
#### Saturday 2023-01-21 02:22:02 by Edward Z. Yang

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
## [kidgenius703/tgstation](https://github.com/kidgenius703/tgstation)@[a3e7c70f6d...](https://github.com/kidgenius703/tgstation/commit/a3e7c70f6da0fc7ea9929ddb39beddcf3113707f)
#### Saturday 2023-01-21 02:32:47 by necromanceranne

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
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[b7164095fd...](https://github.com/ARF-SS13/coyote-bayou/commit/b7164095fd1ad42d581cdce1b1861d180ec50323)
#### Saturday 2023-01-21 03:17:44 by Superlagg

Merge pull request #1482 from ARF-SS13/Fuck-you-github

Stinky nash gate buttons fixed

---
## [astropy/astropy.github.com](https://github.com/astropy/astropy.github.com)@[b2cbc0511e...](https://github.com/astropy/astropy.github.com/commit/b2cbc0511e1d624432d2751899ba4430f7673f6e)
#### Saturday 2023-01-21 03:22:57 by H. Moritz Günther

Remove Clara from Dev telecon organizer

Clara has indicated by email that she's currently too involved in teaching and getting her PhD done to fill this role. We'd love to have her back, but life happens and the purpose of the roles list is to record who does what right now and whom to contact for anything that comes up related to a specific role. Thus, this PR to remove her from the role, with the understanding that we are happy to add her back in as soon as she has time again.

---
## [angelaaan/FoodFrenzy](https://github.com/angelaaan/FoodFrenzy)@[2223af6988...](https://github.com/angelaaan/FoodFrenzy/commit/2223af69884d708fa7b6689b0bc71eee9cd2e297)
#### Saturday 2023-01-21 03:38:47 by angelaaan

verge of tears 10:38PM

bro i am trying to make the thing save BUT IT WONT FUCKING SAVE-

HELP
IT KEEPS DELETING THE DAMN FILE CONTENTS WHENEVER I RUN THE PROGRAM

---
## [agraef/purr-data](https://github.com/agraef/purr-data)@[597472e292...](https://github.com/agraef/purr-data/commit/597472e2927d8ca8ea0e826a260c642ba4b20e27)
#### Saturday 2023-01-21 04:01:48 by Albert Gräf

Windows packaging: GH-friendly OutputBaseFilename.

This makes my life less miserable when doing releases on the GH mirror,
because I don't have to manually edit the installer filenames before
uploading any more.

GitHub doesn't like blanks in upload file names, using dashes instead
makes uploading much easier and eliminates the need to zip the installer
before uploading. We also include a proper cpu architecture designation
(x86 or x86_64) in the output file name in lieu of the '(64 bit)' suffix
which causes trouble in GH uploads as well, because of the parentheses.

Note that this shouldn't affect the Gitlab CI since it looks for a
'Purr*.exe' build artifact, which will still match the package name.

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[979b26d52e...](https://github.com/JohnFulpWillard/tgstation/commit/979b26d52e09dcaa7ad00ce07c1e16760dbd7cb2)
#### Saturday 2023-01-21 04:09:43 by tralezab

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
## [peff/git](https://github.com/peff/git)@[ea0fc88e56...](https://github.com/peff/git/commit/ea0fc88e56b1f0a36337e3eb781aaa7b20c211d2)
#### Saturday 2023-01-21 05:14:24 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[bb01d6b1a5...](https://github.com/peff/git/commit/bb01d6b1a5aeaa4f265a531f62b24e9ae0a29f6d)
#### Saturday 2023-01-21 05:14:45 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[44013f8c24...](https://github.com/peff/git/commit/44013f8c244009e3be97ca757c3d9f79139dc4f8)
#### Saturday 2023-01-21 05:14:59 by Jeff King

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

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[25f4961156...](https://github.com/Paxilmaniac/Skyrat-tg/commit/25f4961156121121aa9b545cfc9f6014b89c2362)
#### Saturday 2023-01-21 05:18:02 by SkyratBot

[MIRROR] Refactors memories to be less painful to add and apply, moves memory detail / text to memory subtypes. Adds some new memories to demonstrate.  [MDB IGNORE] (#18487)

* Refactors memories to be less painful to add and apply, moves memory detail / text to memory subtypes. Adds some new memories to demonstrate.  (#72110)

So, a huge issue with memories and - what I personally believe is the
reason why not many have been added since their inception is - they're
very annoying to add!

Normally, adding subtypes of stuff like traumas or hallucinations are as
easy as doing just that, adding a subtype.

But memories used this factory argument passing method combined with
holding all their strings in a JSON file which made it just frustrating
to add, debug, or just mess with.

It also made it much harder to organize new memories keep it clean for
stuff like downstreams.

So I refactored it. Memories are now handled on a subtype by subtype
basis, instead of all memories being a `/datum/memory`.

Any variety of arguments can be passed into memories like addcomponent
(KWARGS) so each subtype can have their own `new` parameters.

This makes it much much easier to add a new memory. All you need to do
is make your subtype and add it somewhere. Don't need to mess with jsons
or defines or anything.

To demonstrate this, I added a few memories. Some existing memories had
their story values tweak to compensate.

Makes it way simpler to add new memories. Maybe we'll get some more fun
ones now?

:cl: Melbert
add: Roundstart captains will now memorize the code to the spare ID
safe.
add: Traitors will now memorize the location and code to their uplink.
add: Heads of staff winning a revolution will now get a memory of their
success.
add: Heads of staff and head revolutionaries who lose their respective
sides of the revolution also get a memory of their failure.
add: Completing a ritual of knowledge as a heretic grants you a quality
memory.
add: Successfully defusing a bomb now grants you a cool memory. Failing
it will also grant you a memory, though you will likely not be alive to
see it.
add: Planting bombs now increase their memory quality depending on how
cool the bomb is.
refactor: Memories have been refactored to be much easier to add.
/:cl:

* Modular!

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Funce <funce.973@gmail.com>

---
## [Kahsolt/stable-diffusion-webui-prompt-travel](https://github.com/Kahsolt/stable-diffusion-webui-prompt-travel)@[2bad452040...](https://github.com/Kahsolt/stable-diffusion-webui-prompt-travel/commit/2bad452040eb0df7e564c4b4449282db8b3c9029)
#### Saturday 2023-01-21 08:48:37 by Kahsolt

make batch scripts more friendly

remove all annoying %~dp0
seperate tunable parameters out
god blesses whose path contains space chars :(

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[db05d3f3ab...](https://github.com/treckstar/yolo-octo-hipster/commit/db05d3f3abb98d40e37d69f8140ef75ed0ebdd9a)
#### Saturday 2023-01-21 09:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [amylizzle/OpenDream](https://github.com/amylizzle/OpenDream)@[04e782a3fa...](https://github.com/amylizzle/OpenDream/commit/04e782a3fa9ba78f491dfff7d7be02c63ed0f0a0)
#### Saturday 2023-01-21 11:46:12 by Altoids1

Improves the grammar, functionality, and code quality of set declarations (#776)

* Makes Consume array overload return the tokentype it found

Plus adds some extra comments, in my crusade to comment more things.

EDIT: hate you Github Desktop

* Removes MultipleVarDec..., replaces with Aggregate generic

Removes DMASTProcStatementMultipleVarDeclarations,
replaces with DMASTAggregate<>.

DMASTAggregate now has the generic-ified responsibility of being a statement which is actually an aggregate of several statements, all of the same type.

The point of this is so that this aggregation behaviour can also be used for set declaration blocks (and maybe other stuff if we find other uses, I dunno)

* Adds some helpful ctors for DMASTProcBlockInner

There's a lot of repetitive empty or near-empty array inits at the caller side of some of these constructions, so I went ahead and moved those into the ctor. Also allows for a minor optimization (preferring using Array.Empty<> instead of constructing empty arrays).

* Improves SetStatement grammar, function & quality

(If any of you demand I insert the oxford comma into the commit header I am leaving 5ever :rage: )

This commit does several things in one fell swoop:
- Set statements now accept blocking, commas, bracing, all the good stuff that var declarations do
- Blocks now very consistently evaluate their SetStatements first and foremost, before anything else, in a way that makes sense
- Use of the 'in' keyword is now properly prohibited for all set use cases except 'src'
- 'src' now properly gives an unimplemented warning

Also in this commit is a bunch of random autodoc added to things that I looked at or touched over the course of writing this commit. :innocent:

* Implements cursed parity behaviour for non-const set statements

AFAIK, in BYOND, the previous set statement value is used to prop-up one that has a non-constant right-hand side. So I guess we have that behaviour available, now. :sweat_smile:

EDIT: Fixed behaviour in the didError case, minor formatting fixes

* Style fix, replaces several "\n{" with "{\n"

Most of these were my fault. Not all of them though. :^)

* Does the Wixoa reviews, adds EmptyBlock pragma error

As a byproduct of doing the reviews, I have accidentally added empty block detection for several (although perhaps not most) loops and blocks available in OD.

* Brace style fixes

* Does more Wixoa reviews, generalizes EmptyBlock emission

Note that we do not, as of yet, emit this warning for empty procs. This is because:
1. our own DMStandard has several empty procs (usually because they are unimplemented or useless, like the BYOND Hub interface procs)
2. Users may sometimes define an empty proc, intentionally, to act as an abstract virtual that child types can define in their own way.

We can revisit the problem later, I'm just trying to get my PR greenlit.

* Adds test for EmptyBlock pragma emission

Co-authored-by: wixoa <wixoag@gmail.com>

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[392ff5d5da...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/392ff5d5da8a6ad32dfcc7e6c064190d85ae0031)
#### Saturday 2023-01-21 12:07:36 by Angelo G. Del Regno

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
## [32th-System/deltarune_repainted](https://github.com/32th-System/deltarune_repainted)@[32e879e6f0...](https://github.com/32th-System/deltarune_repainted/commit/32e879e6f0d5b084fcc2adc6c38f1a7cc11db430)
#### Saturday 2023-01-21 12:50:02 by Fatfuck22

gustavo

Hello! And welcome to the Los Pollos Hermanos family. My name is Gustavo, but you can call me "Gus". I am thrilled that you'll be joining our team. Each and every day, we serve our customers exceptional food, with impecable service. We take pride in everything that we do. And after this 10 week online seminar, I'm sure you'll fit right in. I like to think I see things in people. To begin, I'd like to talk about the cornerstone of the Los Pollos Hermanos brand. Communication. As an employee of Los Pollos Hermanos, you set the tone for the entire dining experience. Be mindful of what your words, and behavior communicate to our guests. Always be aware of your posture, remember to stand up straight. Your customers and your back will thank you for it. Put effort into your appearance, all employees are required to dress appropriately. Keep your uniform clean, and pressed. If you want respect, you must look respectable. Speak in complete sentences, we never use one word greetings like "Hey" or "Yeah?" Always make eye contact, and finally, whenever you're with a customer or not, remain composed. Inside, you can be thinking about your homework, or friends, or your side business, but no one should ever know it. Because at Los Pollos Hermanos, someone... Is always watching. So dont forget to smile! Thats all for today, see you next time when we'll be discussing cleanliness.

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[e48a6edf5f...](https://github.com/re621/dnpcache/commit/e48a6edf5fad2fe59f9cfa99c2a2c2551651b4fc)
#### Saturday 2023-01-21 13:28:41 by bitWolfy

Remove 1017 artists from the DNP list.

Removed: lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, einin, freaks, angellsview3, arwenscoots, royalzbed, hellfurred, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, peshky, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, 100101, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, tren, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, jdlaclede, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [VastKilleroOm/TG220VAST](https://github.com/VastKilleroOm/TG220VAST)@[44008f485d...](https://github.com/VastKilleroOm/TG220VAST/commit/44008f485d6d72537935cfa8a3a5b6140eece744)
#### Saturday 2023-01-21 14:24:04 by Jacquerel

Fishing-themed Escape Shuttle (#71805)

## About The Pull Request

I can't do much coding until you review my other PRs so I'm making a
mapping PR instead.
I actually made this a while ago while I was trying out strongDMM. It
turns out: it's a good tool and easy to use.

![2022 12 09-10 51
26](https://user-images.githubusercontent.com/7483112/206686234-ae952ba3-2cb4-4093-80a0-d086fe95a3fc.png)

This mid-tier shuttle isn't enormous and is shaped like a fish. It
dedicates much of its internal space to an artificial fishing
environment, plus fishing equipment storage. Plus look at that lovely
wood panelling!
There's not a lot of seating or a large medbay, but there's five fishing
rods for people to wrestle each other over plus some aquariums to store
your catches in.

It contains a variety of fishing biomes (ocean, moisture trap, hole,
portal) but I couldn't fit "lava" in there even though I wanted to
because it's hardcoded to only have fish in it on the mining z-level.
If you're very lucky and nobody shoves you, the time between the shuttle
docking at the station and arriving at Centcomm might be enough time for
you to catch maybe four entire fish. Wow!

## Why It's Good For The Game

There are plenty of novelty shuttle options but I think this one is good
for a personal touch of "the Captain would rather be fishing than
hearing you complain about the nuclear operatives".

## Changelog

:cl:
add: Tell your crew how much you care by ordering a shuttle where half
of the seats have been removed so that you can get some angling done
before you clock out.
/:cl:

---
## [TheGameCreators/GameGuruRepo](https://github.com/TheGameCreators/GameGuruRepo)@[27d7493c1c...](https://github.com/TheGameCreators/GameGuruRepo/commit/27d7493c1cab486fb078210f1207ff347e6d5169)
#### Saturday 2023-01-21 15:00:33 by Teabone

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
## [martinpitt/cockpit](https://github.com/martinpitt/cockpit)@[e018be384b...](https://github.com/martinpitt/cockpit/commit/e018be384bc51a1f534f2b73a7212401e118d0e3)
#### Saturday 2023-01-21 15:22:12 by Martin Pitt

python: Add temporary ${libexecdir} expansion in manifests

This provides the moral equivalent of what commit 94394128e8b6 did for
the C bridge. However, we want to avoid parameterizing the py bridge
with ./configure arguments, to keep it buildable with pip. Detect the
path at runtime instead, there are only a few plausible options anyway.
This is a temporary hack until we eliminate all `${libexecdir}` from
manifests.

This fixes joining an IPA domain, as it now finds
cockpit-certificate-helper. TestIPA.testQualifiedUsers now gets much
further, unfortunately it still fails on the remote host part of the
test, as cockpit-ssh does not work yet.

It also fixes the cockpit-{ssh,pcp,askpass} paths in the manifests, but as we
don't do that routing yet, it does not fix any of the ssh/pcp tests yet.
But it is a necessary prerequisite for actually implementing these.

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[d2bc6caeeb...](https://github.com/NetBSD/pkgsrc/commit/d2bc6caeeb01ac9efee3d9bd1a5feb15299ee37a)
#### Saturday 2023-01-21 16:25:14 by bsiegert

Pullup ticket #6721 - requested by wiz
emulators/mame: bugfixes

Revisions pulled up:
- emulators/mame/Makefile                                       1.161
- emulators/mame/PLIST                                          1.73
- emulators/mame/distinfo                                       1.127

---
   Module Name:	pkgsrc
   Committed By:	wiz
   Date:		Sat Dec 31 11:12:58 UTC 2022

   Modified Files:
   	pkgsrc/emulators/mame: Makefile PLIST distinfo

   Log Message:
   mame: update to 0.251.

   It looks like MAME 0.251 has made it out the door just in time for
   the end of 2022! December felt like a long month in MAME development,
   because so much happened! Nebula, an elusive DECO Cassette game,
   is now emulated. With working steering controls, Magical Pumpkin:
   Puroland de Daibouken is now playable. Two members of the HP 9825
   family from the 1970s have been added, and issues with keyboard
   input on localised versions of the HP 86B have been fixed.

   One of the most interesting systems added this month is the so-called
   Ger?t 32620, make by the Institut f?r Kosmosforschung of the Deutsche
   Demokratische Republik. This device was used to read coded messages
   to be broadcast via shortwave radio numbers stations for reception
   by undercover agents. If a human were to read the numbers, they
   could inadvertently disclose knowledge about the nature of the
   messages or the coding scheme in their speech patterns. This device
   gives a small glimpse into the shadowy world of espionage.

   Konami fans have a lot to be excited about. Firstly, two more
   hand-held LCD games have been added: Skate or Die, and Bill Elliott?s
   NASCAR Racing. Secondly, Windy Fairy has been making steady progress
   on the PowerPC-based arcade systems, with gun controls now working
   in Teraburst. Finally, various refinements and fixes to the CPU
   core for Konami?s custom 6809 processor have fixed a subtle parallax
   scrolling effect in the classic Padodius DA!

   Several systems have been fleshed out noticeably this month,
   including the NEC PC-8801mkII SR family of Japanese computers, the
   3com Palm IIIc and Palm m100 PDAs, and the Yamaha DX100 synthesizer.
   Additionally, the NEC PC-88VA2 can now boot most software, and the
   work on the Palm systems has allowed the VTech IQ Unlimited to show
   signs of life.

   Quite a few systems have had pluggable controller support added
   this month, and support for some additional controllers has been
   added, including:

   * Pluggable controller support for consoles and computers from
     Sega, NEC and Sharp.

   * Sega Mega Drive mouse and 4-player adaptor support.

   * Support for an ATmega-based paddle controller that works with
     export versions of the Sega Master System.

   * NEC PC Engine mouse support.

   * Support for the Dempa Micom Soft XE-1AP, the first analog
     gamepad. Can be used with compatible software for the Sega Mega
     Drive, NEC PC Engine, Sharp X68000 and FM Towns families.

   Of course, there are lots of other fixes and emulation improvements.
   The Apple IIgs has better ADB and real-time clock emulation. Sega?s
   Turbo and Buck Rogers: Planet of Zoom have better controls, and
   the latter has had graphical priority issues fixed. The NES APU
   frame counter interrupt is now emulated, fixing issues with dozens
   of games. For developers, debugger command and expression history
   is now saved between sessions.

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[66b7310039...](https://github.com/Striders13/tgstation/commit/66b7310039297843b01c5b14a9b59180909ab52c)
#### Saturday 2023-01-21 17:30:45 by Rhials

STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows (#72282)

Adds the Terrify spell, and its associated status effect, Terrified.
This new spell is given to antagonist nightmares, as a part of their
brain. The spell only works in those surrounded by darkness, and will
apply the Terrified status effect if successful. Upon being Terrified,
victims will passively gain **Terror Buildup** if they remain in the
dark. As buildup increases, so do the negative effects, including tunnel
vision, panic attacks, dizziness, and more.

There are two primary methods for mitigating terror buildup. The first
is moving into the light, which will reverse the passive terror buildup
and eventually make it go away. The other method is by getting a hug
from a friendly hand, which will reduce buildup significantly.

Getting a hug from an UNfriendly hand (a nightmare, for instance) will
cause the victim to freak out and be briefly knocked down. This can be
spammed on targets who are caught alone in the dark, keeping them in an
unfavorable position (sideways) and adding to the victim's terror
buildup considerably. Escape into the light as soon as possible, or
you'll be pushed to MAXIMUM TERROR BUILDUP.

To what end? Heart failure. Past the soft terror cap (which limits how
much passively generated terror you can make) exists the hard terror
cap. Bypassing that threshold will cause a stress induced heart attack
and knock you unconscious (embarrassing!)

---
## [Floofies/Skyrat-tg](https://github.com/Floofies/Skyrat-tg)@[aa441a9633...](https://github.com/Floofies/Skyrat-tg/commit/aa441a96332829090664577d9b8a3cb5ddc1bcce)
#### Saturday 2023-01-21 17:56:04 by Zonespace

Mirror 72339 & 71284 (#18645)

* Renews a bunch of old roundend new reports that got lost. Plus, some roundend report QoL for cult and revs. (#71284)

A few roundend reports got lost from moving to dynamic and other prs.
This PRs re-allows them to occur. Namely: "Wizard Killed" (lost in
dynamic), "Blob nuked" (lost in dynamic), "Cult escaped" (lost in cult
rework), and "Nuke Ops Victory" (station destroyed via nuke) (lost from,
what I can see, an oversight / accidental swap of report values).

Additionally, small roundend report QOL for cult: Removes antag datums
from spirit realm ghosts after being dusted, so they do not show up on
the report. And in reverse, heads of staff who were dusted / destroyed
in revolution rounds are now also shown in roundend reports.

Some of these reports are dead, which is is a shame because I think
they're cool and fun.

:cl: Melbert
qol: Successfully fending off a blob now has a cross station news report
again. More pressing reports will take priority over it, though.
qol: Successfully killing a wizard (and all of their apprentices) now
has a cross station news report again.
qol: If more than half of a cultist team manages to escape on the
shuttle (rather than summoning Nar'sie), they will send a unique cross
station news report. This is still a loss, by the way. Summon Nar'sie!
qol: Nuclear Operatives successfully nuking the station now has its
unique cross station news report again, and no longer uses the generic
"The station was nuked" report.
qol: Nuking the station to stop a blob infection now has a unique cross
station news report again. Good luck convincing admins to allow this.
qol: Cult ghosts from "Spirit Realm" no longer persist on the cult's
team after being desummoned, meaning they will not show up on roundend
report.
qol: Heads of staff will now always show up on revolution roundend
report - even if their body was fully destroyed.
/:cl:

* Adds support for Rulesets having intrinsic template requirements (#72339)

Title

Ensures that we load templates for a ruleset before we attempt to place
or cache characters for that ruleset
Also makes wizard and abductor async load their template to improve
(apparent) loading times for them

This is the only thing left that I can think of that would cause antags
like nukies and abductors to spawn in wrong

This should not be player facing

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Floofies/Skyrat-tg](https://github.com/Floofies/Skyrat-tg)@[20d03b6483...](https://github.com/Floofies/Skyrat-tg/commit/20d03b64833c55b41011c01c665a09647f5badeb)
#### Saturday 2023-01-21 17:56:04 by SkyratBot

[MIRROR] Avoid creating string list of turf platings, rename some of the APIs, and improve focused test support - 160ms+ (more on prod) of init savings [MDB IGNORE] (#18357)

* Avoid creating string list of turf platings, rename some of the APIs, and improve focused test support - 160ms+ (more on prod) of init savings (#72056)

Looking at some stuff that uses `Join` right now as targets, this one's
pretty straight forward.

`/turf/open/floor/Initialize`, called 20,000 times without ruins,
creates a string list of the broken and burnt states. This carries the
fixed cost of `Join`, which is very expensive, as well as some (not
crazy, but not negligible) proc overhead.

These vars were used for effectively nothing, and have been replaced
with just using the list when necessary, which only adds an extra
millisecond of cost to update_overlays.

This was also used to automatically set `broken` and `burnt` at runtime.
However, this looks like it has gone completely unused. Adds a unit test
which adds it as a static field to the only type that cared about it,
which was abductor tiles, which is wrong anyway, but Whatever. I want to
support people making a subtype of floor tiles that are pre-broken
without it messing up stuff silently, so the test is there.

While I'm at it, renames `setup_broken_states` and `setup_burnt_states`
to remove `setup_`, since they don't really do that anymore (and never
did).

Also also, adds support for `PERFORM_ALL_TESTS` to work with multiple
focuses.

For reviewing, basically all of the changes are in floor.dm, aside from
test stuff, which is unit_test.dm.

* Avoid creating string list of turf platings, rename some of the APIs, and improve focused test support - 160ms+ (more on prod) of init savings

* a

* FUCK

* nope

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>
Co-authored-by: Tastyfish <crazychris32@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4de0ba43e7...](https://github.com/mrakgr/The-Spiral-Language/commit/4de0ba43e7f6bad5ddfb358af0ae77ef76249cbe)
#### Saturday 2023-01-21 18:03:30 by Marko Grdinić

"https://news.ycombinator.com/item?id=34455518
Ask HN: Has anyone successfully started their career over in their 30s?

> Well, what can you do, right? Big tech was (and probably still is) out of question, but I was happy to work with startups and just build the resume, going from random line programmer to lead developer within few years. At the end, nobody cares what you did 15 years ago, current experience is what matter.

Yeah, this is the route I should go. The higher the pay, the more selective the places will be regarding resumes.

https://news.ycombinator.com/item?id=34455934
Tell HN: Sometimes you don't realise how bad something is until you leave

> Just doing nothing sounds awesome. It's not. It's crap. Imagine having to sit at a workstation for months and years, having to be "present" with nothing to actually do but make some some BS stuff to appear busy. Even doing training courses and such becomes boring after a while. It was a kind of mental prison and my boss truly didn't give a flying you-know-what. Imagine having nothing in your week to justify the normal desire to do something useful. I even wrote scripts to make life better but my boss wouldn't consider them because I wrote them.

Yeah, I should just go to a fucking startup. I am torn between two desires, to slack off, and to be useful. Maybe I should take this story to heart and not slack off.

///

I am at the end of my career (already stopped working for someone else, just working on my own projects now) and as I look back at the various jobs I had; the ones that were engaging were also the most rewarding.
I had two short stints with government jobs (one working part-time while in college and once for a major defense contractor) and they were terrible. Strict rules prevented anyone from doing things that were fun and productive. At the end of the year, we once ran out of 'funded projects' and we were forced to work on trivial matters while tracking our time in 30 minute increments. It was painful to find a way to clean your desk for 2 hours. We would have a long meeting where nothing was really discussed just to have a few hours to charge to some check box item. This went on for several weeks.

The best jobs were the ones I had freedom to build what I though the customer wanted. I would sometimes work until 10pm not realizing that quitting time occurred hours earlier (I was still single at the time otherwise my wife would have interrupted).

Startups can be some of the best places to let your creative juices flow. They are not the most stable for guaranteed income, but they can be very rewarding in other ways.

///

HN is useful to me because of threads like these. I mean, what am I supposed to know about the difference between startups and corpos? These guys are telling me what to expect.

> My days at work where I'm actively engaged in a task and feel like I got something done fly by, whereas the days where I have nothing to do and I'm refreshing HN all day are not only boring but draining. Ironic that doing nothing makes you feel like you have no energy at the end of the day.

> It is funny though, the number of people I know who got there and then went back to work for "the man" again. Not for the money, but for having people they could hang out with and talk about things with. They sometimes find happiness working for a company where they have the freedom to be completely honest because "losing your job" isn't a threat that bothers them.

9:45am. https://www.efinancialcareers.com/news/2023/01/goldman-sachs-md-to-ai

If Z falls through, maybe I should apply to StabilityAI for the lulz. Anthropic didn't outright toss my resume away, Generally Intelligent did, who knows what SAI will do? It doesn't really matter.

The main thing I am missing is will. My failure in 2021 shattered my ego. I have to essentially repeat what I did from 2015. I'll take what I've accumulated so far, and start a whole new project to oppose nature.

The same thing that beat me in 2021 is what beat me in high school.

There is no need to take it laying down.

10:05pm. https://boards.4channel.org/g/thread/91013848#p91016046
These oni cyborg girls are amazing.

https://boards.4channel.org/g/thread/91013848#p91015631

Somebody is posting Hitler style art.

https://boards.4channel.org/g/thread/91013848#p91014097

I wonder which model is being used for this. They are talking about aom2.

https://boards.4channel.org/g/thread/91013848#p91014987
https://huggingface.co/WarriorMama777/OrangeMixs#abyssorangemix2-aom2
> It's the hard nsfw AOM2 model

10:40pm. Let me collect some of these images.

https://boards.4channel.org/g/thread/91013848#p91014097
https://boards.4channel.org/g/thread/91013848#p91014164
https://boards.4channel.org/g/thread/91013848#p91014190
https://boards.4channel.org/g/thread/91013848#p91014252
https://boards.4channel.org/g/thread/91013848#p91014287
https://boards.4channel.org/g/thread/91013848#p91014468

https://boards.4channel.org/g/thread/91013848#p91014578
This scenery image is wonderful.

https://boards.4channel.org/g/thread/91013848#p91014620
https://boards.4channel.org/g/thread/91013848#p91014704
https://boards.4channel.org/g/thread/91013848#p91015037

https://boards.4channel.org/g/thread/91013848#p91015868
Here is the oni girl

https://boards.4channel.org/g/thread/91013848#p91016111
Another

https://boards.4channel.org/g/thread/91013848#p91016145
Fem Astolfo

https://boards.4channel.org/g/thread/91013848#p91015968
Horror girl

https://boards.4channel.org/g/thread/91016223#p91016326
The next thread has more oni girls

Colorful. I'll have to remember this one.

https://boards.4channel.org/g/thread/91016223#p91016816

This landscape is really good.

https://boards.4channel.org/g/thread/91016223#p91017234

This one is great as well.

https://boards.4channel.org/g/thread/91016223#p91017349

I still haven't figured out how to get this level of coherency and detail. I'll have to busy myself with figuring it out at some point. Where is that original oni cyborg girl that really got me into them? I thought it was in this thread, but I can't find it.

These castles on top of mountains are so great. I really should figure out how they get the tiny details to fit so well. I should investigate photorealism. That will get me to the bottom of it.

1/21/2023

9:30am. Got a reply from that robotics startup guy. Nothing from Z yet. Incidentally, the current winter has been very warm, but now it finally turned cold. Brrrr.

I've decided one thing. I've been hamering the painterly styles far too much. I am going to go with more realistic ones in the future. I want to understand how crisp detailed images could be created.

Here is the email.

///

Hey Marko,

Thank you so much for this - love your ideas!

The idea of automating ML research and using genetic programming to find better algos is beautiful! Is your point that the main block to this is hardware? And is this just a qualitative issue (i.e. the things that GPUs can't do) or also quantitative (e.g. how long it would take / how much it would cost in current hardware)? And is Tenstorrent developing something along the lines of what you're looking for?

Could you go one level deeper and explain why this is bad - "No, that algorithm needs labels, it just feeds them along with the inputs."? Are you referring to the cost of annotating data or something else (perhaps a different / deeper flaw with this approach)?

And what is in your view the fundamental flaw with backprop?

Understanding intelligence is also one of my key motivators. The other one is that to achieve sustainability (environmental and economic) I think we need to figure out robotic manipulation - but that's a story for another day :)

All the best!

///

///

> The idea of automating ML research and using genetic programming to find better algos is beautiful! Is your point that the main block to this is hardware? And is this just a qualitative issue (i.e. the things that GPUs can't do) or also quantitative (e.g. how long it would take / how much it would cost in current hardware)?

GPUs (and CPUs) are Turing complete so you could do anything a different kind of computer could do on them, but trying to do the kind of research I want to do on them would be like setting money on fire. When you do regular (supervised) deep learning, you at least have an idea of what you are going to get in the end. But I have absolutely no idea what the kind of model that I want to get will be, how long it would take for a GP system to discover it or how much this would cost.

> Could you go one level deeper and explain why this is bad - "No, that algorithm needs labels, it just feeds them along with the inputs."? Are you referring to the cost of annotating data or something else (perhaps a different / deeper flaw with this approach)?

In supervised learning, this method would work worse than regular backprop. And in reinforcement learning, I don't see a way to make it work.

There are RL methods like inverse RL and decision transformers that can do RL without the need to do reward prediction, they are in fact passed in as input features, but much like regular RL, these are hacks. The only place where RL really works is in tabular form. Tabular RL and tabular CFR (CounterFactual Regret) work great. The superhuman poker agents like Pluribus work by putting tabular RL on top of a NN. My current best idea for how to use RL is to train a NN with evolution so it outputs a binary hash function, and then use tabular RL on top of that.

> And what is in your view the fundamental flaw with backprop?

Using the gradient barely makes sense as a credit assignment scheme. You can make a scalar multiplication chain, something like `a*b*c` and realize that the gradients get multiplied as they get propagated down the chain, instead of the more sensible thing which is divided. But even if you wanted to propagate the credit through inverses of a layer instead of the original (like in backprop) which has its own issues, that still leaves the question of how a net could form memories that last years and decades, or learn continuously.

Backprop simply does not have an answer to this. With backprop you can only try to propagate through impossibly long temporal chains. What Hinton is proposing doesn't answer how to do RL stably and efficiently, how to do long term credit assignment for the sake of long term memory formation, or how to learn continuously and adapt in real time.

Taking a step back, the biggest problem is that I can't reason about any of my ML ideas. I can only test them out. In the ML community nobody saw NNs making a resurgence in the 10s, they just started winning on benchmarks and that drew in the money and the attention. So they can't reason about it either, they can only come up with the ideas and test them. But that means that with that particular approach to research we are always held back by what we can imagine and we consider plausible rather than working towards making an intelligent system in a principled manner.

> And is Tenstorrent developing something along the lines of what you're looking for?

Going back to the first question, better hardware is what allowed ML researchers to see that backprop works really well for supervised learning in the 10s. I don't know for sure whether Tenstorrent will give me what I want, I've only watched the company videos, but better hardware is a catalyst for better research. Right now it might seem that the field is making progress, but it is only making progress on models that are suitable for GPUs. There might be models which aren't a good fit for them in the future.

Multicore computing devices with local only memory and PIM programming are where the future of programming is. It would make a huge difference for me to get a 1,000x increase in compute capacity compared to what I have now.

> All the best!

I am glad you find this interesting. I can keep going for as long as you like, if you have any more questions.

///

Good enough. Let me reply with this. I am supposed to be writing the author's note right now.

10:20am. Thunderbird is really nice. I love it. I have no idea why I haven't been using it all this while instead of logging into gmail every time.

10:40am. Had to take a break. Focus me. Let me get started on the Author's Note.

11:25am. Actually I decided to do the chores as the wood fuel stocks were running low.

Let me focus on the author's note now.

I spent a lot of time thinking about it during the night, but now that it has come to it, I am out of fuel. That reply must have taken it. But let me see if I can get some momentum going.

11:50am. Google Docs is going haywire on me.

12:25pm.

///

Author’s Note
1/21/2023

This chapter has 255 images, it has taken me quite a while to prompt them all. The model used in this chapter was Anything v3. Whereas in the previous chapters it was mostly SD 1.5 for the images that I prompted personally. In one of the comments on Royal Road, I said that they were slop when upscaled, and I still haven’t really figured out how to get the neat and crisp images that some of the anons in the /sdg/ thread do. For the next chapter I’ll try using Abyss Orange Mix 2 and go for a realistic style. I want to see whether that sort of thing would be enough to get the kind of vivid crisp detail in my images that I’d want. So far I've been producing them in the painterly style instead.

That 8$/month Paperspace subscription has really been working out for me. Overall, I think that instead of the tiled upscaling we are doing now, which is a hack, we need models that can produce images in 1-2k resolution natively. Plus models that do not struggle so much with anatomy. But I have confidence that these issues will be resolved before long.

Getting this chapter out was somewhat rocky. In late December, I posted a link to the PIM course on Reddit’s PL sub, got contacted by a dev from UPMEM, and I decided to do an UPMEM backend for Spiral. This took me 3 weeks and took up time that I would have otherwise used to write. It made me realize, 1.5 years after deep RL put its boot up my ass, that I am starting to get my taste for programming back. I did a bunch of improvements on the language along the way. And now, I’ve decided to start looking for a job. It is a pity this story has only a single patron at the time of writing; comparing myself to those popular authors who are making 30k/month is like being in hell. Even those making 500$/month seem uber successful.

What do they have that I don’t? Well, in Simulacrum’s case, its main message is that attaining superpowers in the real world requires you to die. This kind of story could never be popular to begin with. It would work a lot better as a game.

Which again brings me back to programming. I had to pretend to be a financial trader to get this info, but it seems Tenstorrent chips have an ETA of 6 months before they open source their SDK and allow consumers to program them. Presumably at that point I’ll be able to rent them on their dev cloud as well. If I just continue writing Heaven’s Key as I was doing up to now, I won’t have any funds to actually pay for the chips when they are released. Up to now I’ve been dedicating myself full time to Heaven’s Key, but €4/month is not going to cut it. And I am not sure if I put in more effort, that I’ll ever get another patron. So necessarily, Heaven’s Key is going to have to be sidelined, but I’ll continue writing it in my free time. Instead of just talking about evolutionary methods, now that I’ve made a language for myself, I should start work on a language for the machines. Spiral itself started as a deep learning library for F#, so it makes sense that Helix should start out as a genetic programming system. Once I get access to the next gen hardware I’ll be able to start work on that in earnest, but even now, I have the option of dipping my toes into evolutionary methods.

I’ll see how things go. I still feel like writing, but I also feel like programming, and I want to make some money for the future. I’ve been a hobbyist for over half a decade, and my skills are good enough to turn pro. Rather than rotting away as a writer, my true self is the one that pursues the Singularity earnestly. I’ve tried and I’ve failed, and in the end, having the machine tell me the way it should be used is the right path. I cannot do anything more, or anything less as a programmer.

///

This should be good enough. Now let me start proofreading. The size of the document is 54.3k words.

12:35pm. Let me have hbreakfast.

25/537. It will take me a while to go through all of this. I did the right thing by contacting Zenna last week. Hopefully, he has had time to think about my request. I should be done with proofreading tomorrow. After that I'll be able to start writing anew. I'll take some time to experiment with AOM2, and figure out how to do detailed scenery.

1:55pm. I've resumed. 54/537. The goal for today is to proofread.

2:05pm. Since I have some images in my unused folder, I should find a way to put some of them in. I just put a skull in there.

2:20pm. Had to take a break. I realized something just now. I should do a character sheet.

83/539. Let me pause here.

3pm. Did the char sheet. That pathos gain has been included. Now the size is 55.15k.

3:55pm. https://youtu.be/gSbE2hgCTLA
Demetori - 寂光寂滅 ～ The Truth of the Cessation of Dukkha [Full Album]

Oh, is this a new Demetori album? Nice!

4:05pm. Hmmm, looking at my old images, I realize that I've overdone the dreamlikeart, painting prompts in the later half.

> (TODO Image: Thought ignition.)

Whops, I forgot one.

4:45pm. I replaced them with a few sceneries I had lying around. I do not want to start up a PS instance just for this.

> Leaving so much unallocated space has a great benefit that I’ll be able to use it for synthesis programs; I do not want to keep running them on my own mind all the time

I didn't mean to say this.

4:55pm. 341/543.

5:20pm. > “Euclid! Euclid! Euclid!” A few more people came to the table, cheering him on and slapping him on the back. Whenever Euclid would throw, he would win, and whenever the others would, they’d lose. Was this table cursed?

Whops, the others were not supposed to be throwing.

Ah, crap, I didn't notice that the attendant had 5 regular fingers instead of a thumb. Maybe the readers won't either.

...No, it is fine. The thumb should be lower, but it a good hand nonetheless.

5:45pm. 362/485. I've zoomed out a bit due to the Docs going haywire, this is why the page count fell. At this rate, I am 3/4ths done with proofing. I'll to try to finish it either today or tomorrow. I'll want to reupload ch 14 to fix that typo I found by accident.

6:25pm. Done with lunch.

400/485. I am tempted to leave it for tomorrow, and I will, but let me do more.

7pm. 443/485. I am almost done, but I do not feel like going at it anymore. I'll finish this tomorrow and then post the chapter on my Patreon. At that point ch 16 will be complete. I'll be looking forward to starting 17."

---
## [shlomif/perl5](https://github.com/shlomif/perl5)@[fe5492d916...](https://github.com/shlomif/perl5/commit/fe5492d916201ce31a107839a36bcb1435fe7bf0)
#### Saturday 2023-01-21 18:29:32 by Yves Orton

regcomp.c etc - rework branch reset so it works properly

Branch reset was hacked in without much thought about how it might interact
with other features. Over time we added named capture and recursive patterns
with GOSUB, but I guess because branch reset is somewhat esoteric we didnt
notice the accumulating issues related to it.

The main problem was my original hack used a fairly simple device to give
multiple OPEN/CLOSE opcodes the same target buffer id. When it was introduced
this was fine. When GOSUB was added later however, we overlooked at that this
broke a key part of the book-keeping for GOSUB.

A GOSUB regop needs to know where to jump to, and which close paren to stop
at. However the structure of the regexp program can change from the time the
regop is created. This means we keep track of every OPEN/CLOSE regop we
encounter during parsing, and when something is inserted into the middle of
the program we make sure to move the offsets we store for the OPEN/CLOSE data.
This is essentially keyed and scaled to the number of parens we have seen.
When branch reset is used however the number of OPEN/CLOSE regops is more than
the number of logical buffers we have seen, and we only move one of the
OPEN/CLOSE buffers that is in the branch reset. Which of course breaks things.

Another issues with branch reset is that it creates weird artifacts like this:
/(?|(?<a>a)|(?<b>b))(?&a)(?&b)/ where the (?&b) actually maps to the (?<a>a)
capture buffer because they both have the same id. Another case is that you
cannot check if $+{b} matched and $+{a} did not, because conceptually they
were the same buffer under the hood.

These bugs are now fixed. The "aliasing" of capture buffers to each other is
now done virtually, and under the hood each capture buffer is distinct. We
introduce the concept of a "logical parno" which is the user visible capture
buffer id, and keep it distinct from the true capture buffer id. Most of the
internal logic uses the "true parno" for its business, so a bunch of problems
go away, and we keep maps from logical to physical parnos, and vice versa,
along with a map that gives use the "next physical parno with the same
logical parno". Thus we can quickly skip through the physical capture buffers
to find the one that matched. This means we also have to introduce a
logical_total_parens as well, to complement the already existing total_parens.
The latter refers to the true number of capture buffers. The former represents
the logical number visible to the user.

It is helpful to consider the following table:

  Logical:    $1      $2     $3       $2     $3     $4     $2     $5
  Physical:    1       2      3        4      5      6      7      8
  Next:        0       4      5        7      0      0      0      0
  Pattern:   /(pre)(?|(?<a>a)(?<b>b)|(?<c>c)(?<d>d)(?<e>e)|(?<f>))(post)/

The names are mapped to physical buffers. So $+{b} will show what is in
physical buffer 3. But $3 will show whichever of buffer 3 or 5 matched.
Similarly @{^CAPTURE} will contain 5 elements, not 8. But %+ will contain all
6 named buffers.

Since the need to map these values is rare, we only store these maps when they
are needed and branch reset has been used, when they are NULL it is assumed
that physical and logical buffers are identical.

Currently the way this change is implemented will likely break plug in regexp
engines because they will be missing the new logical_total_parens field at
the very least. Given that the perl internals code is somewhat poorly
abstracted from the regexp engine, with parts of the abstraction leaking out,
I think this is acceptable. If we want to make plug in regexp engines work
properly IMO we need to add some more hooks that they need to implement than
we currently do. For instance mg.c does more work than it should. Given there
are only a few plug in regexp engines and that it is specialized work, I
think this is acceptable. We can work with the authors to refine the API
properly later.

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[70042337db...](https://github.com/ARF-SS13/coyote-bayou/commit/70042337dbefb532ee9e1eb640edb00e9280c932)
#### Saturday 2023-01-21 21:18:03 by A Psycho

Merge pull request #1483 from ARF-SS13/Fuck-you-github

Small mapfixes

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[16715d9b34...](https://github.com/kleinerm/Psychtoolbox-3/commit/16715d9b34ece4a4be11e6a056f4558707de39fa)
#### Saturday 2023-01-21 21:23:06 by Mario Kleiner

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[a57b142c1a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/a57b142c1a4949ded1dcde1157ccf789fb21aabd)
#### Saturday 2023-01-21 21:38:58 by SkyratBot

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
## [zndrmn/rethinking-voxels](https://github.com/zndrmn/rethinking-voxels)@[90e76c20dc...](https://github.com/zndrmn/rethinking-voxels/commit/90e76c20dca459a71c8979834d8ba6daa46019d9)
#### Saturday 2023-01-21 21:47:01 by gri573

fix blocklight not working with advanced light propagation and no pixel perfect shadows

fuck you codium, I don't care if my commit messages are longer than 50 characters

---
## [1dot13/source](https://github.com/1dot13/source)@[57d2674f37...](https://github.com/1dot13/source/commit/57d2674f3779ea7881fd678c292a056278cd4569)
#### Saturday 2023-01-21 23:26:50 by majcosta

Use a modifiable user-preset sample for VS 2022/2019 (#97)

* Use a modifiable user-preset sample for VS 2022/2019

Customizing a repo-tracked preset file doesn't work:

Type in your gamedir for debugging, or toggle verbose mode for the build, or configure Chinese
UB MapEditor: you now have an unstaged `CMakePresets.json` change in your working directory.
very annoying.

Also, Visual Studio 2022's preset support has a bug: if you have a `CMakePresets.json` file,
no matter in which file (user or repo) the preset you have selected is defined, if you click
"Manage Configurations..." it will always open `CMakePresets.json` for editing, setting the
user up for failure and editing the commited-to-repository file.

Having just the `CMakeUserPresets.json` file also sidesteps another poor Visual Studio 2022
decision: hiding in Folder View files that are .gitignore'd (like `CMakeUserPresets.json`).

In the absence of a `CMakePresets.json` file, selecting "Manage Configurations..." will open
the right file for editing.

The workflow is then:

Copy `CMakeUserPresets.json.sample` into `CMakeUserPresets.json` _once_, then customize
that to your heart's content without git bothering you and accidentally adding an
unwanted change to a patch. Or make your own.

* Added auto-copy of profile template.

* declutter things a bit

move function out of root cmakelists.txt file
move user preset template to a presets directory

this is horrible and I hate it

Co-authored-by: CptMoore <39010654+CptMoore@users.noreply.github.com>

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[6200bc2360...](https://github.com/timothymtorres/tgstation/commit/6200bc23602dc058da7a552d8a0c2d2b67f29e60)
#### Saturday 2023-01-21 23:58:00 by Jacquerel

Basic Mob Carp IX: Carp Rifts & Migration (#72265)

## About The Pull Request

The almost-final part of the much larger PR I tried to make a month ago
(there's actually one more thing but I'm waiting on a dog PR to get
merged first).
This adds _new_ behaviour and abilities to carp.

Now when a Carp Migration occurs, all of the space carp who are spawned
are given a path through the station.
Specifically, each carp which shares a z level will try to path to a
specific station area, then back out into space.

https://www.youtube.com/watch?v=0KtTI4_7a0c
Here in this video we follow one carp and its friends as it attempts to
navigate "Kilo Station" in order to return to its ancestral spawning
grounds, via the dormitories.
Why are there walls underneath those windows? That's a question nature
has no answer for.

In order to ensure that they don't destroy Arrivals, Departures, and
anywhere else with windows in the process of trying to get inside they
have also gained a new "Lesser Carp Rift" ability.
This allows carp to teleport a short distance once per minute, leaving a
rift at their exit point. Any other mob can enter the rift to travel to
a similar location to the space carp (within the same 3x3 area).


https://user-images.githubusercontent.com/7483112/209584254-afb5839b-a1cd-4c5a-b701-dbb47a024272.mp4

Teleporting puts their attack on a one second cooldown so you won't be
_immediately_ bitten for 20 damage out of nowhere.

Their AI has been updated appropriately and they will use these
abilities:
- If they're trying to migrate through the station and encounter an
obstacle.
- If they're trying to atack something and encounter an obstacle.
- If they're trying to run away, as soon as possible.


https://user-images.githubusercontent.com/7483112/209584287-4402bf5b-3c41-4603-9205-5c4da8b4cd1c.mp4

That last point includes the HoS's pet Lia, who is an occasional target
of traitor objectives, which can either work in your favour (scaring her
to a less secure location) or against it (wait, where did she go?).

Also this fixes an embarassing bug where space carp weren't spaceproof
but I am going to pull that out into its own PR so it can be merged
without also needing to review this.

## Why It's Good For The Game

Carp are an iconic space animal but also quite boring, which this
hopefully remedies.

In the current game the Carp Migration event announces itself to the
crew and usually advertises to ghosts that a cool shark mob has spawned
and this changes essentially nothing about the round, the only people
Carp will usually attack are people who go out to set up the solars, and
the occasional wandering curator or lone operative.
This should make the announcement mean something, as suddenly it means a
belligerent animal might unexpectedly try to pass through your
workplace.

Non-magical space carp are weak enough that even an unarmed spaceman can
take on one or two at a time (and even being mildly armed with makeshift
weapons you have around makes them fairly non-threatening) but it can
give you a bit of excitement.

The ability for Carp to teleport allows them to do this without causing
_too much_ property damage or breaching the station, in my tests they
will _generally_ find a way in which doesn't involve them busting
windows open en masse. Also it just makes them a bit more interesting.
Traitors with dehydrated carp are not much able to make use of the Carp
Rift ability as there isn't any way to get them to do it on demand, but
you could spawn one which is not allied to you and then try to scare it
in an appropriate direction which I think is a fun use of the item.

This undoubtedly will make Space Dragon player-controlled carp more
dangerous in a way which is difficult to predict, but it also makes
playing as them more fun and might encourage some guerilla tactics and
cooperation which wasn't previously possible.

## Changelog

:cl:
add: Space Carp seem to have begun associating the station with food and
attempting to enter from the outside, rather than simply congregating
around solar panels. Employees are advised that these are wild animals,
and should not be fed.
add: Space Carp can intermittently teleport short distances, leaving a
short lived rift which other nearby carp will be attracted to follow
them through.
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---

