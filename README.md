## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-08](docs/good-messages/2023/2023-02-08.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,359,089 were push events containing 3,607,691 commit messages that amount to 276,624,311 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 58 messages:


## [Floofies/Skyrat-tg](https://github.com/Floofies/Skyrat-tg)@[30530f2c96...](https://github.com/Floofies/Skyrat-tg/commit/30530f2c96c02b1a188ee870a7aff18f65ab3bd5)
#### Wednesday 2023-02-08 00:09:01 by SkyratBot

[MIRROR] AI actions won't unassign each other's movement targets & Mice stop being scared of people if fed cheese  [MDB IGNORE] (#18268)

AI actions won't unassign each other's movement targets & Mice stop being scared of people if fed cheese  (#72130)

## About The Pull Request

Fixes #72116 
I've had a persistent issue with basic mob actions reporting this error
and think I finally cracked it
When replanning with `AI_BEHAVIOR_CAN_PLAN_DURING_EXECUTION` it can run
`Setup` on one action leading to the plan changing, meaning that it runs
`finishCommand` to cancel all other existing commands
If you triggered a replan by setting up a movement action in the middle
of another movement action, cancelling the existing action would remove
the target already set by the current one.
We want actions to be able to remove _their own_ movement target but not
if it has been changed by something else in the intervening time.

I fixed this by passing a source every time you set a movement target
and adding a proc which only clears it if you are the source... but this
feels kind of ugly. I couldn't think of anything but if you have a
better idea let me know.

Also while I was doing this I turned it into a feature because I'm
crazy.
If you feed a mouse cheese by hand it will stop being scared of humans
and so will any other mice it attracts from eating more cheese. This is
mostly because I think industrial mouse farming to pass cargo bounties
is funny.
Mice controlled by a Regal Rat lose this behaviour and forget any past
loyalties they may have had.


https://user-images.githubusercontent.com/7483112/208779368-3bd1da0f-4191-4405-86e5-b55a58c2cd00.mp4

Oh also I removed a block about cancelling if you have another target
from the "hunt" behaviour, everywhere using this already achieves that
simply by ordering the actions in expected priority order and it was
messing with how I expected mice to work.
Now if they happen to stop by some cheese they will correctly stop
fleeing in order to eat it before continuing to run away.

## Why It's Good For The Game

Fixes a bug I kept running into.
Makes it possible to set up a mouse farm without them screaming
constantly.
Lets people more easily domesticate mice to support Ratatouille
gameplay.

## Changelog

:cl:
add: Mice who are fed cheese by hand will accept humans as friends, at
least until reminded otherwise by their rightful lord.
fix: Fixed a runtime preventing mice from acting correctly when trying
to flee and also eat cheese at the same time.
/:cl:

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[5f78464e25...](https://github.com/harryob/cmss13/commit/5f78464e255b89ada7ca58f5114561be7b32f055)
#### Wednesday 2023-02-08 00:16:55 by NewyearnewmeUwu

Removes skull balaclava and skull facepaint from loadout, places them hidden on the Almayer. (#2526)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This removes the skull balaclavas and the facepaints from the loadout
menu and instead places them in 2 places hidden around the Almayer. The
reason I have done this is that they are almost exclusively used by
people who who are referencing a character- usually Ghost from MW2
(either version) or the characters from COD Ghosts. See below for more
details.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is an OOC meme item that doesn't fit the tone of CM, particularly
because we _already_ have an item with a skull on it in case you want to
use it: Armor! They wrote things on armor in the movie, including a
skull!

![image](https://user-images.githubusercontent.com/70115628/215395714-4aa1c9a2-7621-4f82-8e4b-6d7ed4905f89.png)

Instead, we have these types of people, running a skull 'clava in every
round even as command or medical characters. This is a modern 'operator'
look, not a Space 'Nam-esque look and not an Aliens look. If you want
something that'd remind you of Space 'nam, just look at the classic
'born to kill' helmet. Now, look at these CALL OF DUTY CHARACTERS THAT
THIS ITEM REFERENCES!


![image](https://user-images.githubusercontent.com/70115628/215396029-290063ae-cd96-4929-b6f0-ae2f1c517887.png)

![image](https://user-images.githubusercontent.com/70115628/215396040-0eb9e31f-71ed-408a-8248-152916427bdd.png)

![image](https://user-images.githubusercontent.com/70115628/215396561-f4493f24-2405-4b8d-8034-02a96ea6919f.png)

This is goofy as hell and kind of an outlier among the customization
options since it is _very clearly_ a reference to COD. Look at its
description:

"The face of your nightmares. Heed the call of duty as the ghost in the
night with this metal 'clava. Additionally protects against the cold.
Now in black!"

You'd get laughed off a real marine base for wearing this, let alone
wearing one on an op. We don't need more people running this every
round, and this gives them something to fight over between eachother- if
_you_ want to larp as Simon 'Ghost' Riley from hit video game COD MW2
(either version) then you'll have to hunt it down.
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
del: Removed skull balaclavas and skull facepaint from the loadout
options
maptweak: adds a single skull facepaint and balaclava, each hidden in
their own locations on the Almayer.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [MichaelDeBoey/next.js](https://github.com/MichaelDeBoey/next.js)@[268dd6e80b...](https://github.com/MichaelDeBoey/next.js/commit/268dd6e80bb4e17096c0e75da94cf4de0b809697)
#### Wednesday 2023-02-08 00:23:28 by José Fernando Höwer Barbosa

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
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[83275d8cdf...](https://github.com/pytorch/pytorch/commit/83275d8cdf7721285c4e1b921c28295dc215ba7c)
#### Wednesday 2023-02-08 01:48:38 by Brian Hirsh

add torch.autograd._set_view_replay_enabled, use in aot autograd (#92588)

tldr; this should fix some minor perf regressions that were caused by adding more as_strided() calls in aot autograd.

This PR adds a new context manager, `torch.autograd._set_view_replay_enabled()`.

Context: AOT Autograd has special handling for "outputs that alias graph intermediates". E.g. given this function:

```
def f(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    return out
```

AOT Autograd will do the following:

```
def fn_to_compile(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    # return the graph intermediate
    return y, out

compiled_fn = compile(fn_to_compile)

def wrapper(x):
    y, out = compiled_fn(x)
    # regenerate the alias of the graph intermediate
    return out._view_func(y)
```

What's annoying is that `out._view_func()` will result in a `.as_strided` call, because `out` is an ordinary runtime tensor. This (likely?) caused a perf regression, because when running the backward, out `as_strided_backward()` is slower than our `view_backward()`.

In this PR, I added some TLS for instructing autograd to do view replay instead of as_strided, even when given a normal tensor. I'm definitely interested in thoughts from autograd folks (cc @albanD @soulitzer). A few points that I want to bring up:

(1) One reason that this API seems generally useful to me is because of the case where you `torch.compile()` a function, and you pass in two inputs that alias each other, and mutate one of the inputs. Autograd is forced to add a bunch of as_strided() calls into the graph when this happens, but this would give users an escape hatch for better compiled perf in this situation

(2) To be fair, AOT Autograd probably won't need this TLS in the long term. There's a better (more complicated) solution, where AOT Autograd manually precomputes the view chain off of graph intermediates during tracing, and re-applies them at runtime. This is kind of complicated though and feels lower priority to implement immediately.

(3) Given all of that I made the API private, but lmk what you all think.

This is a followup of https://github.com/pytorch/pytorch/pull/92255.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/92588
Approved by: https://github.com/ezyang, https://github.com/albanD

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[91f06a97d3...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Wednesday 2023-02-08 01:51:06 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [FRC-Team3484/X23_RobotCode](https://github.com/FRC-Team3484/X23_RobotCode)@[aa04f17b7e...](https://github.com/FRC-Team3484/X23_RobotCode/commit/aa04f17b7e062ad432c7e734a988f5974d27d9cf)
#### Wednesday 2023-02-08 01:51:12 by Programmer1

I said a funny joke about ripping a body part off and got banned. We made the second PID Loop, and Bortnite became the favorite mentor of the day. We are now scared of the cv->?->Output thingy but once we suceed we will rule all of FRC. If we fail then arson would be kinda funny but a bad idea.

---
## [smxi/inxi](https://github.com/smxi/inxi)@[464cac2f1e...](https://github.com/smxi/inxi/commit/464cac2f1ef6c25ae173ce1c8d151c8e210ab84b)
#### Wednesday 2023-02-08 02:00:13 by Harald Hope

A small point release, various smaller items, ongoing updates to matching table
features, bug fixes, but nothing major.

--------------------------------------------------------------------------------
SPECIAL THANKS:

1. Thanks Umio-Yasuno in github issue #281 for actually being proactive and
finding some Intel/AMD gpu device id lists. I wish more issues would be like
that.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. DEBUG: --debug-arg and --debug-arg-use must use the full format:
--debug-arg="-GS", or else the command line eats the args, even if in quotes.
The error handlers will then complain about no data supplied, and it will exit.

--------------------------------------------------------------------------------
BUGS:

1. GRAPHICS: An accidental 'and' instead of 'or' test (see Code 1) led to
systems without gpu or dri graphics drivers not showing their xorg driver even
when present. This was due to a mistake, and also due to how Perl handles || and
&& in sequence, which made this bug not show up until I tested on a system with
xorg graphics driver, but without dri or gpu drivers. Virtually no modern
hardware or operating systems would trip this condition, but older hardware and
operating systems, which may not have gpu or dri drivers, might. And did, in my
case. This is by the way why I try to test on old hardware at least now and
then.

--------------------------------------------------------------------------------
FIXES:

1. CODE: A poorly done attempt at optimization would have broken case
insensitive pre-compiled regex with $pattern = qr/../ because you can't add
/$pattern/i to precompiled pattern, but qr/.../i support only added perl 5.014.
This should impact almost nobody, but it is/was a glitch. Basically qr/../ can
only be used when no /i type modifier is required if supporting Perl less than
5.014.

See inxi-perl/docs/optimization.txt section REGEX for more on this.

Note that Perl already compares the values in the variable each iteration via a
simple equality test, so the only real gain from using qr// is not having to do
that equality test each iteration of a loop.

2. OUTPUT: Fixed a few small inner key name failures to use '-' instead of ' '
to separate key terms:

3. REPOS: Called urpm urpmq, which is the query tool, not the actual type.

4. GRAPHICS: Fixed some gpu_id.pl matching rules. Thanks Umio-Yasuno in github
issue #281 for noticing that some of the matching rules were either wrong or not
loose enough.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1a. OPTIONS: Long time oversight, no option to test or do one time change of key:
value separator string ':'. This goes along with existing config option
SEP2_CONSOLE. Added --separator/--sep {character}.

1b. OPTIONS: Added synonym for --output: --export, and for --output-file:
--export-file.

2a. GRAPHICS: New Intel gpu data source, from intel, finally. This let us add a
lot more gpu ids. Thanks Umio-Yasuno in github issue #281 for finding these.

2b. GRAPHICS: New AMD data source, from github. This let me fill in some more,
albeit not as accurately as previous sources, but added more so fine. Thanks
Umio-Yasuno in github issue #281 for finding these.

3. CONFIG: In a first, took a feature from acxi, --config, and imported it into
inxi! This shows active current configuration, by file.

4. CPU: updated, fine tuned amd cpu microarch ids.

5. DISKS: More disk vendors added. Not as many as usual, I think the high tech
sanctions against China may be slowing the rate of new Chinese SSD/USB vendors.
But still some new ones, as always. Not many new IDs for existing ones though,
that is noteworthy. A few new data sources to help pinpoint vendor names found
too, though those won't in general impact users, but can be used to determine if
a string is in fact a company name.

--------------------------------------------------------------------------------
CHANGES:

1. OUTPUT: Fix 2, -t 'started by:' key name changed to: started-by:
-G 'direct render:' changed to 'direct-render:'.

--------------------------------------------------------------------------------
DOCUMENTATION:

1a. MAN: there were a few <...> instead of [...] for required option arguments.
Fixed those.

1b. MAN: also added --debug-id [string] since that is in general useful info.

1c. MAN: Added qualifiers about when xwayland: and compositor: items appear for
default -Ga output.

1d. MAN: Typo in config path in man page, .conf/ should be .config/.

1e. MAN: for --output json/xml, added pointer to doc page on smxi.org, people
being unable to grasp the output is getting tiresome.

1f. MAN: Added synonym for --output, --export.

2a. SMXI.ORG DOCS: added --output json/xml documentation page:
https://smxi.org/docs/inxi-json-xml-output.htm - this is also linked to from the
github wiki page, though of course nobody is going to read it, as well as from
a few pages in smxi.org.

2b. Updated inxi-man,options,changelog.htm files.

3. CHANGELOG: Changed to use same format as acxi.changelog, leading topic id's
in upper case, makes it easier to scan read and organize.

4a. DOCS: docs/inxi-cpu.txt - cleaned up, re-arranged a bit, added cpuid data
explanation, and updated header on inxi-perl/data/cpu/microarch to better
explain the way amd does ext fam / ext model, which are not the same,
bizarrrely, very confusing.

4b. DOCS: New: docs/inxi-disks.txt. Split out from inxi-resources.txt, part of
the ongoing to documentation modularization, slowly splitting out sub topics
from inxi-data.txt and inxi-resources.txt. Note this is in general only done
when I'm working on that specific feature. But slowly, surely.

--------------------------------------------------------------------------------
CODE:

1. GRAPHICS: Test when no gpu drivers and no dri drivers but x drivers never
showed x driver. Was supposed to be all || for tests:

if (@$gpu_drivers || $graphics{'dri-drivers'} && @$x_drivers){

https://perldoc.perl.org/perlop. I believe this led to test 1 being false, test
2 being false, and since that left tests 2 and 3 needing to be true for the &&
logical and to be true. Since only one of the two was true, the last bit was
seen as false.

2. GRAPHICS: Connected with 1, noticed that for some weird reason, I'd decided
to assign the array ref for drivers like this:

@$x_drivers = (a, b, c);
when it was supposed to be:
$x_drivers = [a,b,c];

This did not cause any issues, since they mean the same thing, but it was silly
to write it that way.

3a. DEBUG: Added --debug-arg-use which allows testers to run a specific argument
combination that may be causing issues.

3b. DEBUG: Also added more validation, to make sure arg for --debug-arg /
--debug-arg-use start with - or -- followed by a letter.

4. START: Removed this code block from set_konvi_data. I had left this in place
for a release or two to make sure no need for it was found, but it will never be
used since it never worked in the first place.
	# my $config_cmd = '';
	# there's no current kde 5 konvi config tool that we're aware of. Correct if changes.
	# This part may never have worked, but I don't have legacy data to determine.
	# The idea was to get inxi.conf files from konvi data stores, but that was never right.
	# if (main::check_program('kde4-config')){
	#	$config_cmd = 'kde4-config --path data';
	# }
	# kde5-coinfig never existed, was replaced by $XDG_DATA_HOME in KDE
	# elsif (main::check_program('kde-config')){
	# 	$config_cmd = 'kde-config --path data';
	# }
	# elsif (main::check_program('qtpaths')){
	# 	$config_cmd = 'qtpaths --paths GenericDataLocation';
	# }
	# The section below is on request of Argonel from the Konversation developer team:
	# it sources config files like $HOME/.kde/share/apps/konversation/scripts/inxi.conf
	#  if ($config_cmd){
	#	  my @data = main::grabber("$config_cmd 2>/dev/null",':');
	# 	Configs::set(\@data) if @data;
	#	 main::log_data('dump',"kde config \@data",\@data) if $b_log;
	# }

5. OPTIONS: in OptionsHandler::post_process(), reorganized the various run and
exit triggers, help, configs, recommends, version, etc. All on top now.

---
## [min-jean-cho/pytorch](https://github.com/min-jean-cho/pytorch)@[5c6f5439b7...](https://github.com/min-jean-cho/pytorch/commit/5c6f5439b7e6a5e63a68b36b4cf093a00d46e8be)
#### Wednesday 2023-02-08 02:30:53 by Edward Z. Yang

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
## [junepark678/palera1n-c](https://github.com/junepark678/palera1n-c)@[731e1cba30...](https://github.com/junepark678/palera1n-c/commit/731e1cba30b200577d17ab1fd8598622f3e9df3d)
#### Wednesday 2023-02-08 03:22:34 by junepark678

finalize build.yml v20
fuck you macos build times
FUCK AMFI

---
## [RanTranslations/packages_apps_Settings-yaap](https://github.com/RanTranslations/packages_apps_Settings-yaap)@[3c433521a6...](https://github.com/RanTranslations/packages_apps_Settings-yaap/commit/3c433521a66e2a0eaa7ac7b8f714472784e52505)
#### Wednesday 2023-02-08 03:47:45 by Ido Ben-Hur

Settings: Refactor and clean connectivity check preference

wow this was just horrible...

Made this preference way more maintainable and runtime effective:
* Declare the preference in xml instead of hardcoding - this makes it searchable, more maintainable and is also better runtime wise
* Use arrays instead of manually naming each URL
* Use an ArrayList to handle index <-> setting relationship more easily
* Use static imports instead of literal calls
* Actually handle cases of non availability
* There is absolutely no reason to handle OnResume here
* Get rid of useless functions
* Get rid of useless imports
* Move resources to the proper custom files so we don't confuse translators
* More, too lazy. Don't write shit code please. Thank you.

---
## [junepark678/palera1n-c](https://github.com/junepark678/palera1n-c)@[eb9268083c...](https://github.com/junepark678/palera1n-c/commit/eb9268083c0cf3e0b2a3053b44a13a91d679e682)
#### Wednesday 2023-02-08 03:55:20 by junepark678

finalize build.yml v21
fuck you macos build times
FUCK AMFI

fix so that it downloads build time not configure time

---
## [kkellogg378/sudokuSolver](https://github.com/kkellogg378/sudokuSolver)@[b317f688b4...](https://github.com/kkellogg378/sudokuSolver/commit/b317f688b4ed1464a10f6dea5ca9005eb4600dd0)
#### Wednesday 2023-02-08 05:14:50 by jesusFreak1

Update sudokumain.c

Renamed "nosolution" to "no_solution"
Added several probably unnecessary checks in a failed attempt at debugging the code 
Added a section to reset the grid to a Zero Matrix if no solution is found, however the code still hangs before reaching that point
Gave use to the pointer "*p". Guess I forgot to do that when originally tackling this code.
Rebuilt the Message Loop. Not sure why, that part I did a while ago and I don't remember the purpose

Notes to self: Hardcoding the "valid" int to 0 or 1 produces the "No Solution" and "Success" results, respectively. However, setting that to the isValid function makes the program commit suicide still when there is no solution. I've provided blocks to prevent the isValid from trying to process array elements that aren't on the array, but that doesn't fix it

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3f61c4c2cd...](https://github.com/tgstation/tgstation/commit/3f61c4c2cdaba5de603e4ee32e9655f111cbc86d)
#### Wednesday 2023-02-08 05:59:51 by jimmyl

Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

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

---
## [iefnaf/guava](https://github.com/iefnaf/guava)@[8a676ade61...](https://github.com/iefnaf/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Wednesday 2023-02-08 06:12:57 by cpovirk

Make the build work under more JDK versions.

(Guava is already _usable_ under plenty of verions. This change affects only people who build it themselves.)

And run CI under JDK17. Maybe this will make CI painfully slow, but we'll see what happens. If we want to drop something, we should consider whether to revert 17 or to drop 11 instead (so as to maintain coverage at the endpoints of \[8, 17\]).

## Notes on some of the versions

### JDK9

I expected Error Prone to work, but I saw `invalid flag: -Xep:NullArgumentForNonNullParameter:OFF`, even though that flag is [already](https://github.com/google/guava/blob/166d8c0d8733d40914fb24f368cb587a92bddfe0/pom.xml#L515) part of [the same `<arg>`](https://github.com/google/error-prone/issues/1086#issuecomment-411544589), which works fine for other JDK versions. So I disabled Error Prone for that version.

Then I had a Javadoc problem with the `--no-module-directories` configuration from cl/413934851 (the fix for https://github.com/google/guava/issues/5457). After reading [JDK-8215582](https://bugs.openjdk.org/browse/JDK-8215582) more carefully, I get the impression that that flag might not have been added until 11: "addressed in JDK 11, along with an option to revert to the old layout in case of need." So I disabled it for 9-10.

Then I ran into a problem similar to https://github.com/bazelbuild/bazel/issues/6173 / [JDK-8184940](https://bugs.openjdk.java.net/browse/JDK-8184940). I'm not sure exactly what tool produced a file with a month of 0, but it happened only when building `guava-tests`. At that point, I gave up, though I left the 2 above workarounds in place.

### JDK10

This fails with some kind of problem finding a Guice dependency inside Maven. I didn't investigate.

### JDK15 and JDK16

These fail with [the `TreeMap` bug](https://bugs.openjdk.org/browse/JDK-8259622) that [our collection testers had detected](https://github.com/google/guava/issues/5801#issue-1068748849) but we never got around to reporting. Thankfully, it got reported and [fixed](https://github.com/openjdk/jdk/commit/2c8e337dff4c84fb435cafac8b571f94e161f074) for JDK17. We could consider suppressing the tests under that version.

### JDK18, JDK19, and JDK20-early-access

These fail with [`SecurityManager` trouble](https://github.com/google/guava/issues/5801#issuecomment-1293817701).

## Notes on the other actual changes

### `maven-javadoc-plugin`

I set up `maven-javadoc-plugin` to use `-source ${java.specification.version}`. Otherwise, it would [take the version from `maven-compiler-plugin`](https://github.com/google/guava/issues/5801#issuecomment-1314291284). That's typically fine: Guava's source code targets Java 8, so `-source 8` "ought" to work. But it doesn't actually work because we also pass Javadoc the _JDK_ sources (so that `{@inheritDoc}` works better), which naturally can target whichever version of the JDK we're building with.

### Error Prone

While Error Prone is mostly usable [on JDK11+](https://errorprone.info/docs/installation), some of its checks have [problems under some versions](https://github.com/google/error-prone/issues/3540), at least when they're reporting warnings.

This stems from its use of part of the Checker Framework, which [doesn't support JDKs in the gap between 11 and 17](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/framework/src/main/java/org/checkerframework/framework/source/SourceChecker.java#L553-L554). And specifically,  it looks like the Checker Framework is [trying to look up `BindingPatternTree` under any JDK12+](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/javacutil/src/main/java/org/checkerframework/javacutil/TreeUtils.java#L131-L144). But `BindingPatternTree` (besides not being present at all [until JDK14](https://github.com/openjdk/jdk/commit/229e0d16313b10932b9ce7506d84096696983699#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R41)) didn't declare that method [until JDK16](https://github.com/openjdk/jdk/commit/18bc95ba51b6864150c28985e65b6f784ea8ee2c#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R39).

Anyway, the problem we saw was [a `NoSuchMethodException` during the `AbstractReferenceEquality` call to `NullnessAnalysis.getNullness`](https://oss-fuzz-build-logs.storage.googleapis.com/log-a9d04aa2-8b5a-47ca-8066-7e6b38548064.txt), which uses Checker Framework dataflow.

To address that, I disabled Error Prone for the versions under which I'd expect the `BindingPatternTree` code to be a problem.

(I also disabled it for JDK10: As noted above, Error Prone [supports JDK11+](https://errorprone.info/docs/installation). And as noted further above, Maven doesn't get far enough with JDK10 to even start running Error Prone.)

Fixes https://github.com/google/guava/issues/5801

RELNOTES=n/a
PiperOrigin-RevId: 488902996

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[d95ca04819...](https://github.com/Lamella-0587/Skyrat-tg/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Wednesday 2023-02-08 06:17:18 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [dgp1130/rules_prerender](https://github.com/dgp1130/rules_prerender)@[c2cdea3682...](https://github.com/dgp1130/rules_prerender/commit/c2cdea36827d85037b6d11b188f990d8bd23e028)
#### Wednesday 2023-02-08 06:37:00 by Doug Parker

Enables strictest reasonable TypeScript settings and fixes failures.

Specific options and their reasoning include:

* Enabled `allowUnusedLabels` as labels are generally an antipattern and usually an attempt to make an object literal.
* Enabled `noImplicitReturns` as forgetting to return is a very easy mistake to make and good to correct.
* Enabled `noFallthroughCaseInSwitch` as switch fallthroughs are a terrible idea that should never have been allowed in the first place.
* Enabled `noImplicitOverride` as overriding a method should be an explicit action and clearly not accidental.
* Enabled `noPropertyAccessFromIndexSignature` as I want to be explicit about statically known properties vs dynamically retrieved properties. In kind of on the fence about this one TBH, but my experience with Closure compiler makes me comfortable with this dichotomy, so it doesn't bother me.
* Enabled `noUncheckedIndexAccess` to require checking for `undefined` where necessary. I'm also not entirely sold on this one, and it can be annoying to deal with, especially with arrays. However it is generally good practice and (mostly) avoidable if you're comfortable with the language.

---
## [alaviss/nimskull](https://github.com/alaviss/nimskull)@[f35b5bf2d4...](https://github.com/alaviss/nimskull/commit/f35b5bf2d447c10b6a104ef0649115a266e8dea6)
#### Wednesday 2023-02-08 06:54:00 by haxscramper

Make compiler report structured

Full rework of the compiler message handling pipeline. Remove old-style message generation that was
based purely on strings that were formatted in-place, and instead implement structured logging where
main compiler code only instantiates objects with required information.

Explanation of changes for this commit will be split into several sections, matching number of edit
iterations I had to make in order for this to work properly.

* File reorganization

In addition to the architectural changes this PR requires some type definition movements.

- PNode, PSym and PType definitions (and all associated types and enums) were moved to the
  ast_types.nim file which is then reexported in the ast.nim
- Enum defininitions for the nilability checking were moved to nilcheck_enums.nim and then
  reexported
- Enum definitions for the VM were moved to to vm_enums.nim

* New files

- Main definition of the report types is provided in the reports.nim file, together with minor
  helper procedures and definition of the ReportList type. This file is imported by options, msgs
  and other parts of the compiler.
- Implementation of the default error reporting is provided in the cli_reporter.nim - all
  disguisting hardcoded string hacks were moved to this single file. Now you can really witness the
  "error messages are good enough for me" thinking that prevailed in the compiler UX since it's
  inception.

* Changed files

Most of the changes follow very simple pattern - old-style hardcoded hacks are replaced with
structural report that is constructed in-place and then converted to string /when necessary/. I'm
pretty sure this change already puts me close to getting CS PHD - it was *unimaginably hard* to
figure out that hardcoding text formatting in place is not the best architecture. Damn, I can
probably apply to the nobel prize right now after I figure that out.

** Changes in message reporting pipeline

Old error messages where reportined via random combinations of the following:

- Direct calls to `msgs.liMessage` proc - it was mostly used in the helper templates like
  `lintReport`
- `message`
- `rawMessage`
- `fatal`
- `globalError` - template for reporting global errors. Misused to the point where name completely
  lost it's meaning and documentation does not make any sense whatsoever. [fn:global-err]
- `localError` - template for reporting necessary error location, wrapper around `liMessage`
- `warningDeprecated` - used two times in the whole compiler in order to print out error message
  about deprecated command switches.

Full pipeline of the error processing was:

- Message was generated in-place, without any colored formatting (was added in `liMessage`)
  - There were several ways message could be generated - all of them were used interchangeably,
    without any clear system.
    1. Some file had a collection of constant strings, such as `errCannotInferStaticParam = "cannot
       infer the value of the static param '$1'"` that were used in the `localReport` message
       formatting immediately. Some constants were used pretty often, some were used only once.
    2. Warning and hint messages were categorized to some extent, so and the enum was used to
       provide message formatting via `array[TMsgKind, string]` where `string` was a `std/strutils`
       formatting string.
    3. In a lot of cases error message was generated using hardcoded (and repeatedly copy-pasted)
       string
- It was passed down to the `liMessage` (removed now) procedure, that dispatched based on the global
  configuration state (whether `ignoreMsgBecauseOfIdeTools` holds for example)
- Then message, together with necessary bits of formatting (such as `Hint` prefix with coloring) was
  passed down to the `styledMsgWriteln(args: varargs[typed])` template, whcih did the final dispatch
  into
- One of the two different /macros/ for writing text out - `callStyledWriteLineStderr` and
  `callIgnoringStyle`.
  - Dispatch could happen into stdout/stderr or message writer hook if it was non-nil
- When message was written out it went into `writeLnHook` callback (misused for
  `{.explain.}` [fn:writeln-explain]) (hacked for `compiles()` [fn:writeln-compiles]) and was
  written out to the stdout/stderr.

It is now replaced with:

- `Report` object is instantiated at some point of a compilation process (it might be an immediate
  report via `localError` or delayed via `nkError` and written out later)
- `structuredReportHook` converts it to string internally. All decitions for formatting, coloring
  etc. happen inside of the structured report hook. Where to write message, which format and so on.
- `writeLnHook` /can/ be used by the `structuredReportHook` if needed - right now it is turned into
  simple convenience callback. In future this could even be replaced with simple helper proc, for
  now I left it as it is now because I'm not 100% sure that I can safely remove this.

** Changes in the warning and hint filtering

Report filtering is done in the particular *implementation* of the error hook -
`options.isEnabled()` provides a default predicate to check whether specific report can be written
out, but it must still be called manually. This allows to still see all the reports if needed. For
example, `cli_reporter.reportHook()` uses additional checks to force write some reports (such as
debug trace in `compiles()` context).

Most of the hint and warning were already categorized, altough some reports had to be split into
several (such as `--hint=Performance` that actually controlled reports for `CopiesToSink` and
`CannotMakeSink`, `--hint=Name` that controlled three reports).

None of the errors were categorized (reports from the `nkError` progress was incorporated, but in
I'm mostly describing changes wrt. to old reporting system) and all were generated in-place

** Minor related changes

- List of allowed reports is now stored in the `noteSets: array[ConfNoteSet, ReportKinds]` field of
  the `ConfigRef`, instead of *seven* separate feilds. Access is now done via getter/setter procs,
  which allows to track changes in the current configuration state.
- Renamed list of local options to `localOptions` - added accessors to track changes in the state.
- Move all default report filter configuration to `lineinfos.computeNotesVerbosity()` - previously
  it was scattered in two different places: `NotesVerbosity` for `--verbosity:N` was calculated in
  `lineinfos`, foreignPackageNotesDefault was constructed in `options`
- Changed formatting of the `internalAssert` and `internalError` messages
- Removed lots of string formatting procs from the various `sem*` modules - ideally they should
  *all* be moved to the `cli_reporter` and related.

-------

Additional notes

[fn:global-err] As I said earlier, `globalError` was misused - it is still not possible to fully get
rid of this sickening hack, since it is used for /control flow/ (you read this correct - it is an
error reporting template, and it is used for control flow. Wonderful design right?).

So, in short - `globalError` can raise `ERecoverableError` that can be caught in some other layer
(for example `sem.tryConstExpr` abuses that in order to bail out (pretty sure it was done as an
'optimization' of some sort, just like 'compiles') when expression fails to evaluate at
compile-time [fn:except])

[fn:except] https://github.com/nim-works/nimskull/pull/94#issuecomment-1006927599

[fn:writeln-explain] Of course you can't have a proper error reporting in the nim compiler, so this
hook was also misused to the point of complete nonsense. Most notable clusterfuck where you could
spot this little shit is implementation of `{.explain.}` pragma for concepts. It was implemented via
really 'smart' (aka welcome to hell) solution in

https://github.com/nim-works/nimskull/commit/74a80988d9289e8147a791c4b0939d4287baaff3 (sigmatch
~704) and then further "improved" in
https://github.com/nim-lang/Nim/commit/fe48dd1cbec500298f7edeb75f1d6fef8490346c by slicing out parts
of the error message with `let msg = s.replace("Error:", errorPrefix)`

For now I had to reuse similar hack - I *do* override error reporting hook in order to collect all
the missing report information. In the future it would be unnecessary - when concept is matched it's
body will be evaluated to `nkError` with reports that are written out later.

[fn:writeln-compiles] when `compiles()` check is executed, all error output is temporarily disabled
(both stderr and stdout) via setting allowed output flags to `{}` (by default it is set to

---
## [Penghisbungholius/tgstation](https://github.com/Penghisbungholius/tgstation)@[bf73344399...](https://github.com/Penghisbungholius/tgstation/commit/bf73344399f4b372c13d367cbbd8a40bec23916b)
#### Wednesday 2023-02-08 07:01:26 by Time-Green

[READY] DRAMATIC SHUTTLES!! You can now fly around the shuttle (#71906)

You can move around shuttles during transport now! Instead of them
teleporting you instantly into deepspace, you can move around somewhat
depending on your space-mobility and grip-strength.


![image](https://user-images.githubusercontent.com/7501474/206866132-3fae024c-a8a2-4f4a-b4b8-37c96a254498.png)

**Please watch the demonstration aswell, it should answer most
questions:**
https://www.youtube.com/watch?v=Os77qDOVSXE

Interactions:
- Being within armsreach of a wall or solid object means you 'cling',
where the shuttle pull is very weak and you can basically run around the
shutt;e (but dont fuck up or you're gone)
- Being in range of nothing gives you a very heavy pull, you can barely
resist if you have a decent jetpack
- Objects are instantly power-yeeted
- Being pulled or riding something excempts you from hyperspace pull
- Touching a space tile while being on hyperspace dumps you in
deepspace, you either go back to the shuttle or enjoy deepspace
- On shuttle hyperspace tiles are a lot less dangerous, and will instead
launch and freeze you instead of teleporting you into deepspace
- In-case it wasn't obvious, you can rest outside the shuttle as long as
something is blocking your path. I think it's funny but I might nerf it

:cl:
add: You can now fly around the shuttle during transit! Woohoo! You can
either cling to the side or grab a jetpack and try and keep up with the
shuttle! Carps can move around freely in hyperspace
qol: Increased shuttle hyperspace size from 8 tiles to 16
/:cl:

- [x] Find a way to detect when a shuttle arrives and do something with
the shit left in hyperspace

Things I will do in another PR: 
- Engines spit fire and hurt (almost finished but I want to keep this
small)
- Random shuttle events. You might run into dust meteors or migrating
carps OR A CHANGELING INFILTRATOR
- Hyperspace turfs on the shuttle pull you under the shuttle

### Why it's good for the game
It's so much more immersive than being instantly teleported into
deepspace. It gives you a chance to recover if you get spaced or for
daredevils to look cool

It's also just very cool idk

---
## [Penghisbungholius/tgstation](https://github.com/Penghisbungholius/tgstation)@[acb96fee1d...](https://github.com/Penghisbungholius/tgstation/commit/acb96fee1d0f6605992280d751a7b9930e3a7211)
#### Wednesday 2023-02-08 07:01:26 by MrMelbert

Refactors memories to be less painful to add and apply, moves memory detail / text to memory subtypes. Adds some new memories to demonstrate.  (#72110)

## About The Pull Request

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

## Why It's Good For The Game

Makes it way simpler to add new memories. Maybe we'll get some more fun
ones now?

## Changelog

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

---
## [PA-GK/android_frameworks_base](https://github.com/PA-GK/android_frameworks_base)@[13f877ef8d...](https://github.com/PA-GK/android_frameworks_base/commit/13f877ef8db753516070ffbc7f80ea3b3bd1f9f1)
#### Wednesday 2023-02-08 07:19:28 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [1582130940/android_kernel_xiaomi_sdm660](https://github.com/1582130940/android_kernel_xiaomi_sdm660)@[501c7e54dc...](https://github.com/1582130940/android_kernel_xiaomi_sdm660/commit/501c7e54dcefa482637de1e397371a60ae2aff68)
#### Wednesday 2023-02-08 08:18:34 by Angelo G. Del Regno

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
## [BeatAroundTheBuscher/ROSIGMA](https://github.com/BeatAroundTheBuscher/ROSIGMA)@[d28fef844a...](https://github.com/BeatAroundTheBuscher/ROSIGMA/commit/d28fef844af8c4ed02960f3434982f4b34bdb0ca)
#### Wednesday 2023-02-08 10:36:02 by Surrealaser

Khorne Update

1. Added the stat gain on melee hit/kill 'Rampage' mechanics to more Khorne units; Juggernauts, Khorne Warptalons.

2. Standardized traits among Khorne units like Fear and Pain Immunity.

3. Added the Intimidation ability/weapon. This is primarily used for Khorne units that lack ranged weapons for reaction fire like Bloodletters, Juggernauts and Warptalons; drains TUs and Morale in a small AoE via paralytic terror.

---
## [yssource/awesome-hacking](https://github.com/yssource/awesome-hacking)@[c93ff660eb...](https://github.com/yssource/awesome-hacking/commit/c93ff660eb0b0233cb1d76d4e61b2596c2fe08a8)
#### Wednesday 2023-02-08 11:24:10 by Hack like a Pornstar

Update books.md

There are so many books one can find on infosec, from Hacking Exposed to the Web Application Handbook. However, the books that I suggest in this pull request are of a different kind. They portray real life hacking scenarios where the reader shadows a hacker trying to break into a company. They get to experience the frustraiton, joy and excitment of a real hacking engagement.
Furthermore, the techniques and tips focus on common systems and network configurations: Windows, Mainframes, Active Directory, Linux, etc.
Cheers,

---
## [SoDebug/kernel_xiaomi_raphael](https://github.com/SoDebug/kernel_xiaomi_raphael)@[3b068dd51a...](https://github.com/SoDebug/kernel_xiaomi_raphael/commit/3b068dd51aeb4fc5b5cc5b2934d595cb48b25fba)
#### Wednesday 2023-02-08 11:41:15 by kondors1995

raphael_defconfig: Revert FBEv2 defconfig changes

To maiteiners who still use FBEv1 Fuck you in particular

https://www.youtube.com/watch?v=Ok3xVYz8Ibs

---
## [aruna17256/java](https://github.com/aruna17256/java)@[6c2f5ffffa...](https://github.com/aruna17256/java/commit/6c2f5ffffafe732718f303028d0f78db56468a9d)
#### Wednesday 2023-02-08 11:51:32 by aruna17256

Three Idiots

Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a program to find the midpoint of the line.

---
## [DawfukFR/kernel_oneplus_sm8250](https://github.com/DawfukFR/kernel_oneplus_sm8250)@[521d0ac13d...](https://github.com/DawfukFR/kernel_oneplus_sm8250/commit/521d0ac13df592bcbbe3e06168edb75f79233626)
#### Wednesday 2023-02-08 11:52:49 by Wang Han

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
Signed-off-by: Blaster4385 <venkateshchaturvedi12@gmail.com>

---
## [newstools/2023-iol](https://github.com/newstools/2023-iol)@[55b944157f...](https://github.com/newstools/2023-iol/commit/55b944157fd25c87c6d8d692d8033ffacc9ed586)
#### Wednesday 2023-02-08 12:10:57 by Billy Einkamerer

Created Text For URL [www.iol.co.za/news/news/crime-and-courts/double-life-sentence-for-kzn-man-who-killed-his-ex-girlfriend-and-her-new-boyfriend-while-they-were-asleep-649ef8dc-e892-40d4-991a-49d3c87752d0]

---
## [LeDrascol/SPLOTCH-Station-13](https://github.com/LeDrascol/SPLOTCH-Station-13)@[bfe52432b8...](https://github.com/LeDrascol/SPLOTCH-Station-13/commit/bfe52432b81c443578e1e1776be7c4c410c28d9b)
#### Wednesday 2023-02-08 13:15:36 by Darius

Initial implementation of Divine Prayer Altar

This commit add a prayer system for Blessed Blood quirk users to request blessings.

The following changes are made:
- Added the Divine Prayer Altar
- Added CSS class blessedphrase
- Added CSS animation blessedcolor
- Added span define span_blessedphrase
- Added admin topic for blessed requests
- Removed Blessed Blood rewards for holy points of 3+

---
## [AshfordGraye/ProjectRPG](https://github.com/AshfordGraye/ProjectRPG)@[9fc7ba666e...](https://github.com/AshfordGraye/ProjectRPG/commit/9fc7ba666ea976d6e6a86edc2120ac65a11e55bb)
#### Wednesday 2023-02-08 13:41:08 by Ash

A learning experience I'm sure all programmers go through...

After a machine restore and cloning the repo back from GitHub it became apparent that all local files previously present but assigned to .gitignore had been lost - including the OriginalAppBuild folder which included the original application from which this unfinished one was built. 

Well, obviously - I told it to ignore them didn't I...

The absolute kicker? I deleted the backup while cleaning up my documents folder on autopilot before restoring my machine...

A classic example of being reminded the hard way that computers do EXACTLY what you tell them to and that having backups are only good if you keep them somewhere you wont touch them by mistake.

The only upshots here are that my written work was in a totally separate location, and the actual code itself is of course exactly how I Ieft it - Praise the Omnissiah.

This commit recreates a documents folder and adds the base files for some documents I can recreate easily like the .drawio files. Added the assignment brief and some files for code snips and pseudocode writing for the assignment itself. The OriginalAppBuild is completely gone - there's no way I can reverse engineer what the code has now turned into back into what it was. Be like turning an omelette back into eggs.

---
## [Signal-K/client](https://github.com/Signal-K/client)@[69497a1500...](https://github.com/Signal-K/client/commit/69497a1500e3ec2237555d07581ab4cd40880de2)
#### Wednesday 2023-02-08 13:41:48 by Liam Arbuckle

🪁🥎 ↝ #8 Add file upload feature & auth handler

1. Completed authentication header for web client. To the end user it is 100% offchain, with user profiles being stored on a postgresql database. However, I've taken a dive into the Magic sdk to create wallet addresses for each user, as well as a Flask-based authentication handler for future metamask/wallet interaction. I've made this decision for a few reasons (like simplicity), but the main reason is for the client to seem like a regular journal platform and not be confusing, as well as follow the 'web3-agnostic' design language I favour for projects like this due to confusion and/or distrust of web3 products/teams. However, since each user will have a wallet address, they'll be able to interact with smart contracts and IPFS just fine. Further discussion will need to take place to discuss long-term suitability of this model, including things like gas fees (currently everything regarding transactions is occurring on Goerli [testnet] and gas fees will be processed by a "superuser" so that there's no restrictions or huge expenses) and how we go about getting users to trust the web3 nature (which I've got a lot of experience with). However, I don't fully know the exact demographics we'll be targeting & also I understand that that's quite a while away, so I'll raise it now but won't spend any time thinking about it until the time comes
          2. I've continued with the contracts for proposals/publications & updating the metadata standards. I favour a lazy minting approach with data processing being handled by a Flask blueprint (which is a formula my team have developed on signal-k/sytizen). Right now I'm using Thirdweb & Moralis for the contract interactions and I have also, with much difficulty, succeeded in getting Moralis to self-host on my Postgres server. Finally, I've begun the process of optimising the base layer contracts so that the gas fees (which are already reduced post-merge) are essentially negligible at this time.
          3. File upload for posts/articles feature on the web client is complete, and the smart contracts now receive all file upload metadata from this.
          4. Begun a new flask blueprint (forked from point #2) to generate dataset previews based on which modules (e.g. lightkurve) are used and to add interactive nature to the 'sandbox' feature discussed earlier
          5. Reluctantly continued some documentation

(above message from the Desci discord, see https://github.com/signal-k/sytizen/issues/16 for more info)

---
## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[fedf2f3a26...](https://github.com/ArtemisStation/artemis-tg/commit/fedf2f3a26869848f5fc8f41381d1aff944ed9f6)
#### Wednesday 2023-02-08 13:43:30 by Sol N

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[8f24aba86f...](https://github.com/odoo-dev/odoo/commit/8f24aba86faf2639109b56887781b0daaf60be98)
#### Wednesday 2023-02-08 13:54:35 by Romain Derie

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

closes odoo/odoo#111400

X-original-commit: 639cfc76ba259eea8f38284192017024809173b3
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>
Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [Abinash12abhi/java-basics](https://github.com/Abinash12abhi/java-basics)@[10f8cc1e4a...](https://github.com/Abinash12abhi/java-basics/commit/10f8cc1e4a8b9e9fc1bebe1099c633e83470bc17)
#### Wednesday 2023-02-08 14:29:42 by Abinash12abhi

 Flash

A young man named Diffny leaves home to travel to California, to join the Team Flash. Although Diffny is not able to join this elite team immediately, he befriends the three most formidable members of the age: Joe, Ramsey and vixon and gets involved in affairs of the state and court.At that time, the Villan was planning to dethrone the king and to take the kingdom and to remove the Team Flash of the guard. Since the Villan has spies mixed with the local public , Diffny decides to send a message of his whereabouts to the team Flash in unique way.He gave a note to a boy which has the following message. I am at the midpoint of the line joining the farmhouse next to the palace and the light house. The Team Flash were puzzled. Can you help them find out the location of Diffny?Given the coordinates of the 2 places (x1,y1) and (x2,y2), write a program to find the location of Diffny.

Input & Output Format:

Input consists of 4 integers.

First value consists of x1.

Second value consists of y1.

Third value consists of x2.

Fourth value consists of y2.

Output consists of two float values.

Sample Input
2

4

10

15

Sample Output

6.0
9.5

---
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[a57b142c1a...](https://github.com/Jolly-66/dragon-station/commit/a57b142c1a4949ded1dcde1157ccf789fb21aabd)
#### Wednesday 2023-02-08 15:04:52 by SkyratBot

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
## [RizeKishimaro/Tracebook](https://github.com/RizeKishimaro/Tracebook)@[045e9dfd30...](https://github.com/RizeKishimaro/Tracebook/commit/045e9dfd30af4c6c52784708fb9a7dbeeb975d25)
#### Wednesday 2023-02-08 15:36:44 by Linus Walker

Merge pull request #34 from RizeKishimaro/login-rs

I hate myself, Fuck

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[55a9da130e...](https://github.com/odoo-dev/odoo/commit/55a9da130e0309cb95904e53ae0c16fec81f094e)
#### Wednesday 2023-02-08 16:12:45 by Arnold Moyaux

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

---
## [rgwood/nushell](https://github.com/rgwood/nushell)@[3d65fd7cc4...](https://github.com/rgwood/nushell/commit/3d65fd7cc4f6e0db0c1c31b895feabf2be66cb0a)
#### Wednesday 2023-02-08 16:43:05 by Doru

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
## [ctm/Bataan-Memorial-Death-March](https://github.com/ctm/Bataan-Memorial-Death-March)@[5ab8a8dc6e...](https://github.com/ctm/Bataan-Memorial-Death-March/commit/5ab8a8dc6e10efad8018814604d9844061d57508)
#### Wednesday 2023-02-08 16:57:50 by Clifford T. Matthews

includes today's "speed: run and removes an interval pack run

Today went poorly.  In retrospect, I should not have worn my ruck for
the nature hike I did with Marcia and Jeff on the 2nd. I also
shouldn't have done the second AA loop I did yesterday.  I probably
should have also done my interval training without my ruck on Monday.
Oh, and I shouldn't have worn my ski boots for a few hours the other
day, either.

At this point it looks like I actually have a blister where my hot spot is.
That *may* be a good sign, because a blister is much more likely to resolve
relatively quickly than a morton's neuroma.  OTOH, it was quite uncomfortable
today and that was with 400mg ibuprofen and 500mg acetaminophen, although
the discomfort lessened toward the end.

In addition to being slowed down by my right foot, I also got off to a late
start which caused me to have to come to a complete stop for a while twice
at the intersection for the main entrance to Albuquerque Academy.  It's
hard for me to tell just looking at my Strava information, and I have too
many other things to do than to write some software to tease out the data,
but it looks like I lost about thirty seconds at each stop, *but* by giving
my foot a rest I may have allowed myself to run faster later, so I can't
just take 6 seconds off my average pace to make up for the lost time.

In light of my foot discomfort, I'm going to make some changes.  I'm
going to run less running (perhaps none) tomorrow and Friday. I'm not
going to do pack intervals Monday.  Instead, I'll probably drive to
the library, do unweighted intervals and drive back.  Sadly, Tough
Ruck is looking unlikely this year, and I probably won't decide on
Cocodona 250 until after Bataan Memorial.

---
## [mjg/git](https://github.com/mjg/git)@[69bbbe484b...](https://github.com/mjg/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Wednesday 2023-02-08 17:01:55 by Jeff King

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
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[8500d62b79...](https://github.com/Paxilmaniac/Skyrat-tg/commit/8500d62b798a45812832be0c686f532f877f1e3a)
#### Wednesday 2023-02-08 17:50:06 by SkyratBot

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
## [linuxlizard/pymake](https://github.com/linuxlizard/pymake)@[6e27d8db27...](https://github.com/linuxlizard/pymake/commit/6e27d8db27a5ab05ff66553a454e72788795b87c)
#### Wednesday 2023-02-08 17:58:22 by David Poole

huge update, many fixes

- refactor the LHS tokenizer to handle possibilty of both Targets,
  Assignment, or plain Expression.  The LHS tokenizer will now store the
  whitespace as individual Literals. When the statement has been
  tokenized far enough to determine Rule, Assignment, or Expression,
  then we'll deal with the whitespace.
  - whitespace is discarded in Targets
  - whitespace is preserved until the parse phase
     - if the statement is a directive, the first whitespace after the
       directive is discarded
     otherwise, all whitespace is preserved.

- the LHS tokenize now returns a raw token_list for the LHS. The calling
  tokenizer/parser will create the Target or Assignment or Expression

- I successfully removed two of the most ugly methods from vline: rstrip
  and truncate. I originally used those methods to truncate a Rule line
  with a dangling Recipe. Now, with a more updated Recipe tokenizer, I
  can pass the remaining vchars to the recipe tokenizer directly, no
  more need to do horrible ugly hacks directly into the VCharString.

- added a temporary _view() fn for interactive debugging. At the pdb
  prompt, use print(_view(array-of-vchar)) to see the array-of-vchar as
  a string.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[d35a9220f5...](https://github.com/git-for-windows/git/commit/d35a9220f56d9e22db44496659226ef5f6e936cb)
#### Wednesday 2023-02-08 18:18:07 by Johannes Schindelin

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
## [jozuenoon/rust-clippy](https://github.com/jozuenoon/rust-clippy)@[9e8f53d09a...](https://github.com/jozuenoon/rust-clippy/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Wednesday 2023-02-08 18:25:41 by bors

Auto merge of #101986 - WaffleLapkin:move_lint_note_to_the_bottom, r=estebank

Move lint level source explanation to the bottom

So, uhhhhh

r? `@estebank`

## User-facing change

"note: `#[warn(...)]` on by default" and such are moved to the bottom of the diagnostic:
```diff
-   = note: `#[warn(unsupported_calling_conventions)]` on by default
   = warning: this was previously accepted by the compiler but is being phased out; it will become a hard error in a future release!
   = note: for more information, see issue #87678 <https://github.com/rust-lang/rust/issues/87678>
+   = note: `#[warn(unsupported_calling_conventions)]` on by default
```

Why warning is enabled is the least important thing, so it shouldn't be the first note the user reads, IMO.

## Developer-facing change

`struct_span_lint` and similar methods have a different signature.

Before: `..., impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>)`
After: `..., impl Into<DiagnosticMessage>, impl for<'a, 'b> FnOnce(&'b mut DiagnosticBuilder<'a, ()>) -> &'b mut DiagnosticBuilder<'a, ()>`

The reason for this is that `struct_span_lint` needs to edit the diagnostic _after_ `decorate` closure is called. This also makes lint code a little bit nicer in my opinion.

Another option is to use `impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>) -> DiagnosticBuilder<'a, ()>` altough I don't _really_ see reasons to do `let lint = lint.build(message)` everywhere.

## Subtle problem

By moving the message outside of the closure (that may not be called if the lint is disabled) `format!(...)` is executed earlier, possibly formatting `Ty` which may call a query that trims paths that crashes the compiler if there were no warnings...

I don't think it's that big of a deal, considering that we move from `format!(...)` to `fluent` (which is lazy by-default) anyway, however this required adding a workaround which is unfortunate.

## P.S.

I'm sorry, I do not how to make this PR smaller/easier to review. Changes to the lint API affect SO MUCH 😢

---
## [dbutenhof/pbench](https://github.com/dbutenhof/pbench)@[9e0769e141...](https://github.com/dbutenhof/pbench/commit/9e0769e14120662d96ec9706c8d47e38260a082f)
#### Wednesday 2023-02-08 18:25:43 by David Butenhof

Fix operation synchronization

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
`state` and `message` columns. The `state` can be advanced through `READY`, `WORKING`, `OK`, and `FAILED`, and a message can be associated with each
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

---
## [isabee07/task-manager](https://github.com/isabee07/task-manager)@[83d15f1acf...](https://github.com/isabee07/task-manager/commit/83d15f1acf08265234195a57e41c750f11c2196d)
#### Wednesday 2023-02-08 18:39:20 by MIA ISABELLA ISABELLA

shit got fucked up i literally hate this thing so much

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d4db75283b...](https://github.com/mrakgr/The-Spiral-Language/commit/d4db75283b7b313848b5bf8eac4f29c5f3145113)
#### Wednesday 2023-02-08 18:57:20 by Marko Grdinić

"1:35pm. I do not know whether it is the experience in concurrent programming, or the focus of having the goal of learning webdev directly, or if the docs are simply better now, but I am making huge progress right now. I am soaking up the knowledge like a spoonge.

Breakfast time.

2:35pm. Done with breakfast. I want to chill a bit longer and then I will resume.

3:05pm. Let me resume.

Now that I think about it, I have no idea how how the data transfer between the server and client works. By that I mean, the number of requests and such. Now that I understand middleware, I understand that the app just replies to requests. But surely it does not transfer the web page in its entirety all at once. They should be back and forth talk as html, images and JS are transfered separately, right?

I am going to have to come to an understanding of those basics at some point.

3:10pm. Focus me, let turn off Youtube music.

https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-7.0#service-registration-methods

Focus on reading this article and then the other. After that I might want to watch sometihng about the basics of how server client communication works.

> For more information, see Write custom ASP.NET Core middleware.

I need to remember this link.

```cs
public class Operation : IOperationTransient, IOperationScoped, IOperationSingleton
{
    public Operation()
    {
        OperationId = Guid.NewGuid().ToString()[^4..];
    }

    public string OperationId { get; }
}
```

I did not know that it was possible to get the last 4 elems of an array in C# like this.

3:20pm. Focus me, stop reading /g/. Get into it.

```cs
public class IndexModel : PageModel
{
    private readonly ILogger _logger;
    private readonly IOperationTransient _transientOperation;
    private readonly IOperationSingleton _singletonOperation;
    private readonly IOperationScoped _scopedOperation;

    public IndexModel(ILogger<IndexModel> logger,
                      IOperationTransient transientOperation,
                      IOperationScoped scopedOperation,
                      IOperationSingleton singletonOperation)
    {
        _logger = logger;
        _transientOperation = transientOperation;
        _scopedOperation    = scopedOperation;
        _singletonOperation = singletonOperation;
    }

    public void  OnGet()
    {
        _logger.LogInformation("Transient: " + _transientOperation.OperationId);
        _logger.LogInformation("Scoped: "    + _scopedOperation.OperationId);
        _logger.LogInformation("Singleton: " + _singletonOperation.OperationId);
    }
}
```

I have to admit this is really informative, because I'd never think of a shitty design pattern like this one myself.

3:35pm. I need to get used to DI. It is creating objects based on their runtime types.

https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-7.0#framework-provided-services

Sigh, spare me. It really has a ton of these. But I get it. I really get it now.

I think last time I didn't really for some reason. But DI is a pervasive pattern in OO programming.

3:45pm. https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-7.0&tabs=windows#middleware

Now comes middleware.

> The request handling pipeline is composed as a series of middleware components. Each component performs operations on an HttpContext and either invokes the next middleware in the pipeline or terminates the request.

///

The WebApplicationBuilder.Build method configures a host with a set of default options, such as:

Use Kestrel as the web server and enable IIS integration.
Load configuration from appsettings.json, environment variables, command line arguments, and other configuration sources.
Send logging output to the console and debug providers.

///

So it is loading from `appsettings.json` in this step? I've been wondering about this for a long time.

https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-7.0&tabs=windows#non-web-scenarios

https://www.iis.net/

It keeps talking about IIS.

> Kestrel is often run in a reverse proxy configuration using IIS.

What is a reverse proxy configuration? Does this mean I do not have to use it with IIS?

> A reverse proxy server is a type of proxy server that typically sits behind the firewall in a private network and directs client requests to the appropriate backend server. A reverse proxy provides an additional level of abstraction and control to ensure the smooth flow of network traffic between clients and servers.

https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-7.0&tabs=windows#content-root

> During development, the content root defaults to the project's root directory. This directory is also the base path for both the app's content files and the Web root. Specify a different content root by setting its path when building the host. For more information, see Content root.

It really answers all my answers here.

https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api?source=recommendations&view=aspnetcore-7.0&tabs=visual-studio
Tutorial: Create a minimal API with ASP.NET Core

I'll go over this, but first let me just take a peek at the 3.1 documentation.

https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-3.1

Yeah, it is a bit worse, but all the aspects are still there. I was simply retarded. And in this tutorial, remember the JS no-batteries servers that I looked into. Yeah, it is the same thing.

4:10pm. https://github.com/DapperLib/Dapper

I guess Dapper and EF are the most popular database libraries in the .NET world. This one has nearly 16k stars. 3.6k forks, now that is something.

4:15pm. https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api?source=recommendations&view=aspnetcore-7.0&tabs=visual-studio#add-the-api-code

Yeah, I've been foolish. I should started my ASP.NET journey here. And then either looked into Blazor or functional frameworks, skipping over the controllers. Although to be honest, I am embarassed that I can't understand MVC properly.

https://learn.microsoft.com/en-us/aspnet/core/web-api/?view=aspnetcore-7.0

Wait, this isn't MVC.

4:20pm. Forget this. I hate programming with attributes. DI is just barely palatable to me, but this I don't like. I think functional programming will have a better response than attributes.

...Now...

Let me think.

4:25pm. I'll figure out how to run F# projects in different configurations.

https://stackoverflow.com/questions/63103106/how-to-debug-a-net-core-console-app-when-using-dotnet-run

https://learn.microsoft.com/en-us/dotnet/core/tutorials/debugging-with-visual-studio-code?pivots=dotnet-7-0

I forgot how running stuff in VS Code works. Forget that for now.

You really add a lot of complications when you get away from the IDE.

4:30pm. I think I have the basics of ASP.NET down now. Let me just take a look at the Middleware page for 7.0.

https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-7.0

Ok, I am going to make an assumpting. For a particular page, just the HTML is sent back. And then the browser has the option of getting the multimedia files separately.

https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-7.0

> The Routing middleware in the preceding diagram is shown following Static Files. This is the order that the project templates implement by explicitly calling app.UseRouting. If you don't call app.UseRouting, the Routing middleware runs at the beginning of the pipeline by default. For more information, see Routing.

4:40pm. I a bit confused as I read this:

```cs
app.UseResponseCaching();
app.UseResponseCompression();
app.UseStaticFiles();
```

I think this would in fact cause the response to be written to multiple times. How does that work?

4:50pm. https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-7.0#built-in-middleware

I do not get most of these middleware.

4:55pm. But that doesn't matter. Let me take a break here. I get the gist of what the framework is about now. It is pretty modular with DI and middleware. But middleware itself is nothing special. This is how all the JS frameworks that I've seen work. I forgot what the name of those servers were, but they had custom routing. In the minimal example, it was shown how to do exactly that.

5pm. Now that I have all this fundamental knowledge, it isn't such a mystery as to how ASP.NET would interact with...or rather it isn't a mystery of how functional and other kinds of frameworks could be built on top of it.

5:05pm. I can build a server with this no problem.

I just need some kind of remoting solution for the client and I am set. And I've already seen an example of that in the SAFE Dojo.

I'll also be using that in the future when I make something in Python and want to communicate to the .NET land.

Now...I wanted to say, that I need more knowledge of the existing DI services that ASP.NET library offers. I also need more knowledge of existing middleware. Right now I barely know anything about them. I certainly can't claim that I know how to build a significant website - something on the level of Mangadex yet.

But that is just a matter of learning as I go along.

It would be pointless to just dive in and read up each and every service as if I were memorizing an encyclopedia.

5:05pm. Right now I am in great shape.

What I should do here is go back to studying the SAFE stack. Apart from more of the samples, the Elmish library is the next in line. I'll just study the examples for a few days until my curiosity is stated and then start work on my own project.

5:10pm. Let me take a break here. I do not feel like starting right away.

https://manonepunch.com/manga/one-punch-man-chapter-173/

I am a bit behind on OPM so let read this for a bit. Then I'll get started on the Elmish samples.

5:25pm. https://chapmanganato.com/manga-wd951838/chapter-174

Just this chapter and I'll leave the rest for later.

5:35pm. Enough of that. Let me check out the Elmist examples.

https://elmish.github.io/elmish/

https://elmish.github.io/elmish/docs/basics.html

`#r "Fable.Elmish.dll"`

Ugh, what do I do about this?

Let me sidetrack a bit. What are the new features of F#. The ones I've been using are quite old.

https://devblogs.microsoft.com/dotnet/whats-new-in-fsharp-6/

```fs
let readFilesTask (path1, path2) =
   task {
        let! bytes1 = File.ReadAllBytesAsync(path1)
        let! bytes2 = File.ReadAllBytesAsync(path2)
        return Array.append bytes1 bytes2
   }
```

Interesting.

> Up to and including F# 5.0, F# has used expr.[idx] as indexing syntax. This syntax was based on a similar notation used in OCaml for string indexed lookup. Allowing the use of expr[idx] is based on repeated feedback from those learning F# or seeing F# for the first time that the use of dot-notation indexing comes across as an unnecessary divergence from standard industry practice. There is no need for F# to diverge here.

Ok.

```fs
> [<return: Struct>]
let (|Int|_|) str =
   match System.Int32.TryParse(str) with
   | true, int -> ValueSome(int)
   | _ -> ValueNone
```

Struct active patterns. This is great.

```fs
type Pair = Pair of int * int

let analyzeObject (input: obj) =
    match input with
    | :? (int * int) as (x, y) -> printfn $"A tuple: {x}, {y}"
    | :? Pair as Pair (x, y) -> printfn $"A DU: {x}, {y}"
    | _ -> printfn "Nope"

let input = box (1, 2)
```

> In F# 6, we’ve added a new declarative feature that allows code to optionally indicate that lambda arguments should be inlined at callsites.

This is one of the tricks from Spiral.

```fs
let inline iterateTwice ([<InlineIfLambda>] action) (array: 'T[]) =
    for j = 0 to array.Length-1 do
        action array[j]
    for j = 0 to array.Length-1 do
        action array[j]
```

> Unlike previous versions of F#, this optimization applies regardless of the size of the lambda expression involved. This feature can also be used to implement loop unrolling and similar transformations reliably.

Why did I even make Spiral?

> In F# 6, the compiled form of generative list and array expressions is now up to 4x faster (see the relevant pull request). Generative list and array expressions also have greatly improved debugging. For example:

> NOTE: High-performance modern tensor implementations are available through TorchSharp and TensorFlow.NET.

Has somebody done PyTorch wrappers for .NET?

> One of the most anticipated features in the F# 6 toolchain is the addition of “Pipeline debugging”. Now, the F# compiler emits debug stepping points for each position in an F# pipeline involving |>, ||> and |||> operators. At each step, the input or intermediate stage of the pipeline can be inspected in a typical debugger.

Interesting.

5:50pm.

```
PS C:\Users\Marko> dotnet fsi

Microsoft (R) F# Interactive version 12.4.0.0 for F# 7.0
Copyright (c) Microsoft Corporation. All Rights Reserved.

For help type #help;;

>
```

Oh, I can enter the F# FSI like this. Had no idea.

I loads quite fast too.

6:20pm. Had to leave for lunch. At any rate, F# 6 has a ton of improvements.

https://learn.microsoft.com/en-us/dotnet/fsharp/whats-new/fsharp-50

What did I miss in F# 5?

I guess this is how I will be ending my day today.

`#r "nuget: Newtonsoft.Json"`

In that example, I'll try to load Elmish like this.

`#r "Fable.Elmish.dll"`

What am I going to do with this? Nothing.

https://learn.microsoft.com/en-us/dotnet/fsharp/whats-new/fsharp-50#string-interpolation

Oh wasn't this here in the earlier versions?

What version am I using for Spiral anyway? 5.0. I must have upgraded to it along the way. I think I started with 3.

```fs
let name = "Phillip"
let age = 29

printfn $"Name: %s{name}, Age: %d{age}"

// Error: type mismatch
printfn $"Name: %s{age}, Age: %d{name}"
```

I am going to switch to using this. There is zero reason to sprintf apart from maybe requiring to print {}.

```fs
let str =
    $"""The result of squaring each odd item in {[1..10]} is:
{
    let square x = x * x
    let isOdd x = x % 2 <> 0
    let oddSquares xs =
        xs
        |> List.filter isOdd
        |> List.map square
    oddSquares [1..10]
}
"""
```

Sweet.

> F# 5 also adds support for a nameof pattern that can be used in match expressions:

```fs
[<Struct; IsByRefLike>]
type RecordedEvent = { EventType: string; Data: ReadOnlySpan<byte> }

type MyEvent =
    | AData of int
    | BData of string

let deserialize (e: RecordedEvent) : MyEvent =
    match e.EventType with
    | nameof AData -> AData (JsonSerializer.Deserialize<int> e.Data)
    | nameof BData -> BData (JsonSerializer.Deserialize<string> e.Data)
    | t -> failwithf "Invalid EventType: %s" t
```

What is this? Is it looking for "MyEvent" in the patttern?

```fs
open type System.Math

let x = Min(1.0, 2.0)

module M =
    type DU = A | B | C

    let someOtherFunction x = x + 1

// Open only the type inside the module
open type M.DU

printfn $"{A}"
```

This is new.

```fs
// First, create a 3D array to slice

let dim = 2
let m = Array3D.zeroCreate<int> dim dim dim

let mutable count = 0

for z in 0..dim-1 do
    for y in 0..dim-1 do
        for x in 0..dim-1 do
            m[x,y,z] <- count
            count <- count + 1

// Now let's get the [4;5] slice!
m[*, 0, 1]
```

It is getting more Pythonic by the day.

https://learn.microsoft.com/en-us/dotnet/fsharp/whats-new/fsharp-50#applicative-computation-expressions

Once more, this is new.

https://learn.microsoft.com/en-us/dotnet/fsharp/whats-new/fsharp-50#interfaces-can-be-implemented-at-different-generic-instantiations

Didn't know this wasn't possible.

https://learn.microsoft.com/en-us/dotnet/fsharp/whats-new/fsharp-50#preview-reverse-indexes

```fs
let xs = [1..10]

// Get element 1 from the end:
xs[^1]

// From the end slices

let lastTwoOldStyle = xs[(xs.Length-2)..]

let lastTwoNewStyle = xs[^1..]

lastTwoOldStyle = lastTwoNewStyle // true
```

Here are reverse indexes. This is better than what Python does.

```fs
open System

type InputKind =
    | Text of placeholder:string option
    | Password of placeholder: string option

type InputOptions =
  { Label: string option
    Kind : InputKind
    Validators : (string -> bool) array }

type InputBuilder() =
    member t.Yield(_) =
      { Label = None
        Kind = Text None
        Validators = [||] }

    [<CustomOperation("text")>]
    member this.Text(io, ?placeholder) =
        { io with Kind = Text placeholder }

    [<CustomOperation("password")>]
    member this.Password(io, ?placeholder) =
        { io with Kind = Password placeholder }

    [<CustomOperation("label")>]
    member this.Label(io, label) =
        { io with Label = Some label }

    [<CustomOperation("with_validators")>]
    member this.Validators(io, [<ParamArray>] validators) =
        { io with Validators = validators }

let input = InputBuilder()

let name =
    input {
    label "Name"
    text
    with_validators
        (String.IsNullOrWhiteSpace >> not)
    }

let email =
    input {
    label "Email"
    text "Your email"
    with_validators
        (String.IsNullOrWhiteSpace >> not)
        (fun s -> s.Contains "@")
    }

let password =
    input {
    label "Password"
    password "Must contains at least 6 characters, one number and one uppercase"
    with_validators
        (String.exists Char.IsUpper)
        (String.exists Char.IsDigit)
        (fun s -> s.Length >= 6)
    }
```

I saw this kind of code being used in the SAFE Dojo and it surprised me.

https://learn.microsoft.com/en-us/dotnet/fsharp/whats-new/fsharp-47

https://learn.microsoft.com/en-us/dotnet/fsharp/whats-new/fsharp-45

```fs
> $"{m}";;
val it: string = "System.Int32[,,]"

> m[0,*,*];;
val it: int array2d = [[0; 4]
                       [2; 6]]

> m[1,*,*];;
val it: int array2d = [[1; 5]
                       [3; 7]]
```

I pasted the example in fsi, and I see the text got it wrong. Nevermind.

What is new in F# 7?

https://devblogs.microsoft.com/dotnet/announcing-fsharp-7/

> We are adding a way of declaring, calling and implementing interfaces with static abstract methods, described in F# RFC 1124. This is a new feature in .NET 7, matching the corresponding C# feature. One notable application is generic math.

What is this? Something like typeclasses?

https://devblogs.microsoft.com/dotnet/announcing-fsharp-7/#making-working-with-srtps-easier

These are nice.

```fs
type AverageOps<'T when 'T: (static member (+): 'T * 'T -> 'T)
                   and  'T: (static member DivideByInt : 'T*int -> 'T)
                   and  'T: (static member Zero : 'T)> = 'T
```

This is really nice.

```fs
let inline average<'T when AverageOps<'T>>(xs: 'T array) =
    let mutable sum = 'T.Zero
    for x in xs do
        sum <- sum + x
    'T.DivideByInt(sum, xs.Length)
```

The previous syntax was shit.

https://devblogs.microsoft.com/dotnet/announcing-fsharp-7/#init-scope-and-init-only-properties

I honestly didn't know that init properties even existed.

7:10pm. How annoying. It is super annoying. I should be working in regular VS instead of messing with the command line. When I am playing around like this it just takes time to set up the project and I get nothing in return.

7:25pm. https://www.nuget.org/packages/Elmish

Ok, VS Code has Nuget and paket extensions that makes working with them a lot easier than from the command line.

Let me unistall the global paket.

Then the plugin complains to install paket instead of doing it automatically. Lame.

```
PS E:\Webdev\Fable\qwe> dotnet add package elmish
```

Anyway, it is easy to add packages just like this. Just why am I messing around with Paket? I can always convert to it later if I do not need it.

7:35pm. With that out of the way, let me close here. I've caught up with the F# innovations. I've covered the ASP.NET fundamentals. I've familiarized myself with F# package management version nuovo.

7:40pm. I understand all the basics of webdev right now. Tomorrow, what I will focus on is covering the Elimish examples. Then I will take a look at the SAFE stack examples.

After that I will start work on my own things. That CFR Leduc webapp will be my first target. I want something I can put on my portfolio as well as make programming related Youtube vids. After that I'll look at Ionide. I simply need some practical experience first. Ionide can wait for later.

The main goal is to attain a level of webdev skills where I can realistically bluff as being an experience developer in that. My main goal is to get a job so I can start making money. OSS work would be a priority if it could get me that, but it is not.

I need a couple of projects in this field to get me familiarized with all aspects of it.

Once I grasp that, I will be able to grasp anything. I think at this point I am probably too late to win the race for the Singularity, but that is no reason to stop living today. I might have made too many bad choices, but making the right decision in that past is always easy with today's skill. So I should just keep going forward.

In the future, I should be able to get some interesting paid work, and enjoy life a bit."

---
## [Limych/ha-temperature-feels-like](https://github.com/Limych/ha-temperature-feels-like)@[c09d0357c9...](https://github.com/Limych/ha-temperature-feels-like/commit/c09d0357c9f3035e19d4de8ecb579854cc0a9e09)
#### Wednesday 2023-02-08 20:22:33 by Vincent Le Bourlot

Update is_metric for HA 2023.1+ (close #107) (#108)

* Update units conversion for HA 2022.10+ (close #93)
<!--
  You are amazing! Thanks for contributing to our project!
  Please, DO NOT DELETE ANY TEXT from this template! (unless instructed).
-->
## Breaking change
<!--
  If your PR contains a breaking change for existing users, it is important
  to tell them what breaks, how to make it work again and why we did this.
  This piece of text is published with the release notes, so it helps if you
  write it towards our users, not us.
  Note: Remove this section if this PR is NOT a breaking change.
-->

## Proposed change
<!--
  Describe the big picture of your changes here to communicate to the
  maintainers why we should accept this pull request. If it fixes a bug
  or resolves a feature request, be sure to link to that issue in the
  additional information section.
-->

## Type of change
<!--
  What type of change does your PR introduce to Home Assistant?
  NOTE: Please, check only 1! box!
  If your PR requires multiple boxes to be checked, you'll most likely need to
  split it into multiple PRs. This makes things easier and faster to code review.
-->

- [ ] Dependency upgrade
- [ ] Bugfix (non-breaking change which fixes an issue)
- [ ] New feature (which adds functionality to an this integration)
- [ ] Breaking change (fix/feature causing existing functionality to break)
- [ ] Code quality improvements to existing code or addition of tests

## Example entry for `configuration.yaml`:
<!--
  Supplying a configuration snippet, makes it easier for a maintainer to test
  your PR. Furthermore, for new integrations, it gives an impression of how
  the configuration would look like.
  Note: Remove this section if this PR does not have an example entry.
-->

```yaml
# Example configuration.yaml

```

## Additional information
<!--
  Details are important, and help maintainers processing your PR.
  Please be sure to fill out additional details, if applicable.
-->

- This PR fixes or closes issue: fixes #
- This PR is related to issue:

## Checklist
<!--
  Put an `x` in the boxes that apply. You can also fill these out after
  creating the PR. If you're unsure about any of them, don't hesitate to ask.
  We're here to help! This is simply a reminder of what we are going to look
  for before merging your code.
-->

- [ ] The code change is tested and works locally.
- [ ] There is no commented out code in this PR.
- [ ] The code has been formatted using Black (`black --fast custom_components`)

If user exposed functionality or configuration variables are added/changed:

- [ ] Documentation added/updated to README.md

<!--
  Thank you for contributing <3
-->

* Delete .gitpod.yml

---
## [discord/discord-api-docs](https://github.com/discord/discord-api-docs)@[dd3f05a170...](https://github.com/discord/discord-api-docs/commit/dd3f05a1709add398bac3a68af3cc27287f67038)
#### Wednesday 2023-02-08 20:48:29 by Jerry Jiang

Document Silent Messages. (#5910)

Hey folks!

This is actually my 2022 hackweek project which I got to finish to
completion. :)

During a message send request, if you include the new
`SUPPRESS_NOTIFICATIONS` flag it will not broadcast any push/desktop
notifications but will still increment the relevant mention counters.

The intention is that you can get someone's attention but not feel like
you could be distracting them. Like when you DM someone at 5am. I'm sure some
bots can leverage this as well to avoid noise or something.

Also this should work for the webhook send request as well.

[Add a picture of the UI here]

If you're looking to leverage this as a non-bot, you can write `@silent`
as the _very first_ thing in a message. Make sure your client is
up-to-date btw. Autocomplete a-la `@everyone` is not planned. Eventually we may
put this in an "actual UI", for now this is where it lives. :)

Also sorry to all the users on Discord named silent who may have some
textual conflict now. Forgive me!

---
## [Abyss-Services/abyss-browser-OLD](https://github.com/Abyss-Services/abyss-browser-OLD)@[9fa00e07fd...](https://github.com/Abyss-Services/abyss-browser-OLD/commit/9fa00e07fd2633bc16776653987abcc05673910f)
#### Wednesday 2023-02-08 20:52:34 by pxstaa

ur ugly as fuck go away bitchhhh

yeahhh uhhh anyway go die

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[ae08395328...](https://github.com/IndieanaJones/tgstation/commit/ae08395328672ee40c5abb7f2bd1452bb932d6d4)
#### Wednesday 2023-02-08 21:02:42 by san7890

Syndicate Bomb Core Payloads Can Only Be Triggered via the Bomb (#72986)

## About The Pull Request

Basically, you can't extract the bomb core, slap a 10-second c4 on it/on
the shell/and run off having triggered an incredibly powerful explosion.
This is accomplished by having the syndicate bomb override ex_act (it
will be deleted if the explosion goes off), as well as the payload
itself being subtyped into something resistant to bombs and burning.

In-universe, this is described as the shell being quite resistant to
forms of external explosive force- but if any explosive force comes from
within the bomb's shell: kabloom. The bombcore itself has been
redesigned (in a rare moment of non-ineptude) by Donk Co., who has
redesigned the bomb core payload from the ground up- meaning that it can
only be detonated electronically by an impulse from the bomb machinery.
Cutting the wrong wire and attempting to get rid of the bomb by hitting
it with an axe or something will still cause it to blow up, but you know
how those things can be.
## Why It's Good For The Game

I feel like the point of the syndicate bomb is to be a threat for the
crew to match up against. I want a clown in bomb squad gear to head out
to the site and sweat trying to figure out which wire it is, until....
KA-BLHONK: red mist. Or, I want some "helpful" assistant to interrupt
someone's session by going "I KNOW WHAT WIRE IT IS", and having those
odds of either blowing everyone around them up or actually saving the
day.

Being able to detonate something that was balanced and designed to have
_at least_ one minute and a half in **10 SECONDS** is just so injurious
to the game. You can buy a shitload of these bombs, extract the cores,
slap c4 on it and go around the station doling out some serious
explosions. You can run into medbay, wrench it down, slap a c4 on it AND
NO ONE CAN DO ANYTHING ABOUT IT! They can't cut wires, they can't figure
it out to save the day, all they can do is run. Running from danger is
fine and acceptable, but it's just completely stacked against the crew
in a way that I feel needs to be rectified somehow.

I like the idea of purposefully fucking with the wires on the spot so
you sacrificially kill everyone, that feels quite fair to me. I just
simply don't like the fact that you can waltz around the station
punching huge gaps in the hull (remember, putting c4 on the bomb core
itself would cause it to go kabloom) with nearly nothing as far as risk.
It's way too rewarding for something very easy to accomplish (there's a
reason why it's 90 seconds- it's not meant to be easy to accomplish).

This doesn't affect base bombcore behavior, just the explodey ones that
come standard in syndicate bombs.
## Changelog
:cl:
balance: After an unfortunate event occuring when some nuclear
operatives took the ship to a Fireworks Store, the Syndicate have
re-engineered their bomb cores to only explode when electronically
triggered by the bomb shell itself. The payload inside a standard
syndicate bomb can not be exploded with another explosion, you must keep
it in the bomb machinery for it to actually do some explodey stuff.
/:cl:

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[406b6870bd...](https://github.com/Zergspower/Skyrat-tg/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Wednesday 2023-02-08 21:54:47 by SkyratBot

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
## [OpenAngelArena/oaa](https://github.com/OpenAngelArena/oaa)@[5ab0cf7824...](https://github.com/OpenAngelArena/oaa/commit/5ab0cf78244f7b7d29ea7d65b1535c247a7ae882)
#### Wednesday 2023-02-08 22:03:19 by Darko V

Hero item build guides (#3460)

Updated item build guides for:
Abaddon
Anti-Mage
Arc Warden
Axe
Batrider
Bloodseeker
Bristleback
Broodmother
Centaur Warrunner
Chatterjee
Chen
Crystal Maiden
Dark Seer
Dark Willow
Dawnbreaker
Drow Ranger
Ember Spirit
Faceless Void
Grimstroke
Gyrocopter
Hoodwink
Io
Jakiro
Juggernaut
Kunkka
Lone Druid
Luna
Lycan
Marci
Medusa
Mirana
Naga Siren
Necrophos
Ogre Magi
Oracle
Pangolier
Phantom Assassin
Phantom Lancer
Primal Beast
Puck
Pudge
Pugna
Razor
Riki
Sand King
Shadow Shaman
Silencer
Skywrath Mage
Snapfire
Sniper
Sohei
Spectre
Storm Spirit
Sven
Techies
Terrorblade
Tinkerer
Tiny
Troll Warlord
Tusk
Undying
Ursa
Venomancer
Viper
Visage
Void Spirit
Warlock
Weaver
Windranger
Winter Wyvern
Witch Doctor
Wraith King
Zeus

---
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[1c27d16e6e...](https://github.com/david-rowley/postgres/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Wednesday 2023-02-08 22:38:06 by Tom Lane

Revise tree-walk APIs to improve spec compliance & silence warnings.

expression_tree_walker and allied functions have traditionally
declared their callback functions as, say, "bool (*walker) ()"
to allow for variation in the declared types of the callback
functions' context argument.  This is apparently going to be
forbidden by the next version of the C standard, and the latest
version of clang warns about that.  In any case it's always
been pretty poor for error-detection purposes, so fixing it is
a good thing to do.

What we want to do is change the callback argument declarations to
be like "bool (*walker) (Node *node, void *context)", which is
correct so far as expression_tree_walker and friends are concerned,
but not change the actual callback functions.  Strict compliance with
the C standard would require changing them to declare their arguments
as "void *context" and then cast to the appropriate context struct
type internally.  That'd be very invasive and it would also introduce
a bunch of opportunities for future bugs, since we'd no longer have
any check that the correct sort of context object is passed by outside
callers or internal recursion cases.  Therefore, we're just going
to ignore the standard's position that "void *" isn't necessarily
compatible with struct pointers.  No machine built in the last forty
or so years actually behaves that way, so it's not worth introducing
bug hazards for compatibility with long-dead hardware.

Therefore, to silence these compiler warnings, introduce a layer of
macro wrappers that cast the supplied function name to the official
argument type.  Thanks to our use of -Wcast-function-type, this will
still produce a warning if the supplied function is seriously
incompatible with the required signature, without going as far as
the official spec restriction does.

This method fixes the problem without any need for source code changes
outside nodeFuncs.h/.c.  However, it is an ABI break because the
physically called functions now have names ending in "_impl".  Hence
we can only fix it this way in HEAD.  In the back branches, we'll have
to settle for disabling -Wdeprecated-non-prototype.

Discussion: https://postgr.es/m/CA+hUKGKpHPDTv67Y+s6yiC8KH5OXeDg6a-twWo_xznKTcG0kSA@mail.gmail.com

---
## [jonpryor/java.interop](https://github.com/jonpryor/java.interop)@[7ab120940a...](https://github.com/jonpryor/java.interop/commit/7ab120940ad38f1d70f31a38dc23f9688e180c5c)
#### Wednesday 2023-02-08 22:46:36 by Jonathan Pryor

[Java.Interop.Tools.Expressions] Add Java.Interop.Tools.Expressions

Fixes: https://github.com/xamarin/java.interop/issues/616

Context: https://github.com/xamarin/java.interop/issues/14
Context: ff4053cb1e966ebec1c16f97211b9ded936f2707
Context: da5d1b8103bb90f156b93ebac9caa16cfc85764e
Context: 4787e0179b349ab5ee0d0dd03d08b694acea4971
Context: 41ba34856ab119ea6e22ab103320180143fdf03d

Remember `jnimarshalmethod-gen` (176240d2)?  And it's crazy idea to
use the `System.Linq.Expressions`-based custom marshaling
infrastructure (ff4053cb, da5d1b81) to generate JNI marshal methods
at build/packaging time.  And how we had to back burner it because
it depended upon `System.Reflection.Emit` being able to write
assemblies to disk, which is a feature that never made it to
.NET Core, and is still lacking as of .NET 7?

Add `src/Java.Interop.Tools.Expressions`, which contains code which
uses Mono.Cecil to compile `Expression<T>` expressions to IL.

Then update `jnimarshalmethod-gen` to use it!

~~ Usage ~~

	% dotnet bin/Debug-net7.0/jnimarshalmethod-gen.dll \
	  bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  -v -v --keeptemp \
	  --jvm /Library/Java/JavaVirtualMachines/microsoft-11.jdk/Contents/Home/lib/jli/libjli.dylib \
	  -o _x \
	  -L bin/TestDebug-net7.0 \
	  -L /usr/local/share/dotnet/shared/Microsoft.NETCore.App/7.0.0

First param is assembly to process; `Java.Interop.Export-Tests.dll`
is handy because that's what the `run-test-jnimarshal` target in
`Makefile` processed.

  * `-v -v` is *really* verbose output

  * `--keeptemp` is keep temporary files, in this case
    `_x/Java.Interop.Export-Tests.dll.cecil`.

  * `--jvm PATH` is the path to the JVM library to load+use.

  * `-o DIR` is where to place output files; this will create
    `_x/Java.Interop.Export-Tests.dll`.

  * `-L DIR` adds `DIR` to library resolution paths; this adds
    `bin/TestDebug/net7.0` (dependencies of
    `Java.Interop.Export-Tests.dll`) and
    `Microsoft.NETCore.App/7.0.0-rc.1.22422.12` (net7 libs).

By default the directories containing input assemblies and the
directory containing `System.Private.CoreLib.dll` are part of the
default `-L` list.

When running in-tree, e.g. AzDO pipeline execution, `--jvm PATH`
will attempt to read the path in `bin/Build*/JdkInfo.props`
a'la `TestJVM` (002dea4a).  This allows an in-place update in
`core-tests.yaml` which does:

	dotnet bin/Debug-net7.0/jnimarshalmethod-gen.dll \
	  bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  -v -v --keeptemp -o bin/TestDebug-net7.0

~~ Using `jnimarshalmethod-gen` output ~~

What does `jnimarshalmethod-gen` *do*?

	% ikdasm bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll > beg.il
	% ikdasm _x/Java.Interop.Export-Tests.dll > end.il
	% git diff --no-index beg.il end.il
	# https://gist.github.com/jonpryor/b8233444f2e51043732bea922f6afc81

is a ~1KB diff which shows, paraphrasing greatly:

	public partial class ExportTest {
	    partial class '__<$>_jni_marshal_methods' {
	        static IntPtr funcIJavaObject (IntPtr jnienv, IntPtr this) => …
	        // …
	        [JniAddNativeMethodRegistration]
	        static void __RegisterNativeMembers (JniNativeMethodRegistrationArguments args) => …
	    }
	}
	internal delegate long _JniMarshal_PP_L (IntPtr jnienv, IntPtr self);
	// …

wherein `ExportTest._<$>_jni_marshal_methods` and the `_JniMarshal*`
delegate types are added to the assembly.

This also unblocks the desire stated in 4787e017:

> For `Java.Base`, @jonpryor wants to support the custom marshaling
> infrastructure introduced in 77a6bf86.  This would allow types to
> participate in JNI marshal method ("connector method") generation
> *at runtime*, allowing specialization based on the current set of
> types and assemblies.

What can we do with this `jnimarshalmethod-gen` output?  Use it!

First, make sure the tests work:

	% dotnet test --logger "console;verbosity=detailed" bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll
	…
	Passed!  - Failed:     0, Passed:    17, Skipped:     0, Total:    17, Duration: 103 ms - Java.Interop.Export-Tests.dll (net7.0)

Then update/replace the unit test assembly with
`jnimarshalmethod-gen` output:

	% \cp _x/Java.Interop.Export-Tests.dll bin/TestDebug-net7.0
	% dotnet test --logger "console;verbosity=detailed" bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll
	…
	Total tests: 17
	     Passed: 17

`core-tests.yaml` has been updated to do this.

~~ One-Off Tests ~~

One-off tests: ensure that the generated assembly can be decompiled:

	% ikdasm  bin/TestDebug-net7.0/Java.Interop.Tools.Expressions-Tests-ExpressionAssemblyBuilderTests.dll
	% monodis bin/TestDebug-net7.0/Java.Interop.Tools.Expressions-Tests-ExpressionAssemblyBuilderTests.dll

	% ikdasm  _x/Java.Interop.Export-Tests.dll
	% monodis _x/Java.Interop.Export-Tests.dll
	# which currently fails :-()

Re-enable most of `Java.Interop.Export-Tests.dll` for .NET 7;
see 41ba3485, which disabled those tests.

To verify the generated IL, use the [dotnet-ilverify][0] tool:

	dotnet tool install --global dotnet-ilverify

Usage of which is "weird":

	$HOME/.dotnet/tools/ilverify _x/Java.Interop.Export-Tests.dll \
	  --tokens --system-module System.Private.CoreLib \
	  -r 'bin/TestDebug-net7.0/*.dll' \
	  -r '/usr/local/share/dotnet/shared/Microsoft.NETCore.App/7.0.0/*.dll'
	All Classes and Methods in /Volumes/Xamarin-Work/src/xamarin/Java.Interop/_x/Java.Interop.Export-Tests.dll Verified.
	# no errors!

where:

  * `--tokens`: Include metadata tokens in error messages.
  * `--system-module NAME`: set the "System module name".  Defaults
    to `mscorlib`, which is wrong for .NET 5+, so this must be set to
    `System.Private.CoreLib` (no `.dll` suffix!).
  * `-r FILE-GLOB`: Where to resolve assembly references for the
    input assembly.  Fortunately file globs are supported…

~~ Removing `System.Private.CoreLib` ~~

`System.Private.CoreLib.dll` is *private*; it's not part of the
public assembly surface area, so you can't use
`csc -r:System.Private.CoreLib …` and expect it to work.  This makes
things interesting because *at runtime* everything "important" is in
`System.Private.CoreLib.dll`, like `System.Object`.

Specifically, if we do the "obvious" thing and do:

	newTypeDefinition.BaseType = assemblyDefinition.MainModule
	    .ImportReference (typeof (object));

you're gonna have a bad type, because the resulting IL for
`newTypeDefinition` will have a base class of
`[System.Private.CoreLib]System.Object`, which isn't usable.

Fix this by:

 1. Writing the assembly to a `Stream`.
 2. Reading the `Stream` from (1)
 3. Fixing all member references and assembly references so that
    `System.Private.CoreLib` is not referenced.

If `jnimarshalmethod-gen.dll --keeptemp` is used, then a `.cecil`
file is created with the contents of (1).

Additionally, and unexpectedly -- [jbevain/cecil#895][1] -- Mono.Cecil
adds a reference to the assembly being modified.  Remove the declaring
assembly from `AssemblyReferences`.

[0]: https://www.nuget.org/packages/dotnet-ilverify
[1]: https://github.com/jbevain/cecil/issues/895

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[97f567fdc7...](https://github.com/tgstation/tgstation/commit/97f567fdc745230b1594c305680dce683512d032)
#### Wednesday 2023-02-08 22:58:35 by MMMiracles

Tramstation: Growing Pains (#72331)

## About The Pull Request


![image](https://user-images.githubusercontent.com/9276171/209841644-3e8be93c-7903-4eb4-85bf-cc582248a9fa.png)

## Why It's Good For The Game

Lots of QoL and structural changes in attempt to make the cool map even
cooler.

## Changelog
:cl: MMMiracles
add: Tramstation has received a substantial overhaul! Please consult
your local tour guide and station maps for changes.
/:cl:

**Changes (as of so far)**
- The Tramstation tunnels have been extended 6 tiles each way, making
that trek across the central rail a little more dangerous.
- No more mid-way safety net on the transit rails. You're either making
it or you're jumping to the bottom floor to avoid the tram.
- The central rail apparently had a negative slowdown, meaning you
actually WERE faster to just run the gauntlet because it literally made
you faster. This has been reverted because I want you to get hit by a
train.
- The side routes are now a bit more dangerous since you can get pushed
off into the lower floor
- Fauna overhaul! Several locations including the transit tunnels have
gotten some greenery to help liven up transit between sectors. Please do
not rip up the AstroTurf it is very expensive in space.
- Handicap-accessible departments! Every major wing and departments with
multiple floors has been given a 2x3 elevator segment for those among
the crew who have been hit by the tram a few too many times. Handicap
inaccessible staircases may or may not come after this (i hate the
handicapped)
- Expanded Security wing! You know that lame hallway between
interrogation and the courtroom access? Now its a whole holding wing fit
with essentials to keep your inmates content while waiting for their due
process (never ever).
- Reworked Bridge! Front row seats to the western tram dock as well as a
furnished meeting room with various corporate memorabilia!
- The HoP's office has been moved to function more as an arrival gate
for late joining crew! Scenic queue lines and an option to block off the
lower dorm access if you really want to enforce the 'Papers, Please'
roleplay you've always wanted out of your HoP experience.
- Combined the teleporter/gateway/eva access into one special external
operations room. All you off-station needs in one convenient place!
- More multi-z integration! Several segments (mainly maintenance level
transfers) have been given overhangs and better methods to move between
levels. This is still being expanded upon as of current PR posting.
- The power/pipe access shafts have been changed to be more
public-facing and now also act as another inbetween for
maintenance-dwelling crew to shift between floors.
- Multi-z solars! Both solar wings have been extensively overhauled to
include multi-z structuring and easily doubled the amount of roundstart
panels on the map.
- Escape pod bay! [Casually borrowing from a certain ship
map](https://tgstation13.org/phpBB/viewtopic.php?t=32834), there is now
a centralized location for all station escape pods on the floor below
Arrivals. Honestly makes more sense thematically instead of having a
bunch of scattered bays.
- MULEBOT integration! Each major department now has delivery drop-off
points along with Cargo getting a minor restructuring to fit 4 MULEBOTs.
Seedy side-tunnels and drop points have been added for departments that
aren't normally accessible from upper maintenance so they can still
properly deliver cargo if sent this way. I can't guarantee this won't
end in MULEBOTs getting ran over by a tram because they're fickle
beasts.
- Complete rework of the disposals/piping/wirenet! I literally ripped
everything up and rebuilt it with (hopefully) better stability in mind.
Disposals is now also set up in that it'll try to avoid going through
departments unnecessarily if your package isn't marked for it.
- Cargo's mail room and trash room has been overhauled to be more easily
accessed for cargo techs and for routing mail.
- The chef has access to the morgue's back door via the front
maintenance hatch while Robotics can now access the same back door via
their maintenance shaft.
- The chem lab's starting area has been expanded so chemists don't have
to worry as much about digging if they don't have large projects.

![2023 02 02-18 15
45](https://user-images.githubusercontent.com/9276171/216472805-77074a12-d653-41c4-b730-f26f93c27d3b.png)
![2023 02 02-18 15
38](https://user-images.githubusercontent.com/9276171/216472852-555e6ca9-e967-4915-9555-e29cfc99393d.png)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[27c35bfa0b...](https://github.com/tgstation/tgstation/commit/27c35bfa0b11a7248314cc057b70c6a0729794bf)
#### Wednesday 2023-02-08 23:07:03 by MrMelbert

Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line: 
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy. 

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[c7a33d5ff9...](https://github.com/cmss13-devs/cmss13/commit/c7a33d5ff9f4f7563145e82dd6cd0cd00f6b53c5)
#### Wednesday 2023-02-08 23:11:23 by riot

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
## [shlomenu/program_synthesizing_networks](https://github.com/shlomenu/program_synthesizing_networks)@[d19f44df3a...](https://github.com/shlomenu/program_synthesizing_networks/commit/d19f44df3a2574c65053d8f4e0d45fc3055ec030)
#### Wednesday 2023-02-08 23:23:12 by Eli Whitehouse

rigorously measure baseline

I have rigorously measured the baseline and had some results that
I think are promising with the PSN.  I have further modified the
design so that it is not a residual unit, but one in which all
backpropagation must occur via the GNN.

In trying to run my model 10 times, I observed that the performance
was dramatically slowing because the codebook was becoming so large
(2000+ vectors in one case).  I realized that of course this isbad
from a performance perspective, but it's terrible for the theory of
how/why the PSN is supposed to work.  If there's so many discrete
representations that you could assign one to each training data
point multiple times over, then you're hardly instituting a bottleneck
at all.  Particularly bad: the test data could be quantizing to
representations that there isn't even enough training data to vet.
The entire purpose is that in performing inference at test time,
you are simply binning data into bins that have already proven
to be more general through experience with the training data.  I
believe that for this to occur, the number of representations has
to be less than the number of training data points.  Of course,
it must also be larger than the number of possible class labels.
In general usage, those two numbers might be very difficult to
precisely state; one would just have to play around with them.
Nonetheless, a more robust approach should be taken than simply
retaining every representation ever discovered.  Unless we are
more selective than this, there is no way to make sure we are
creating a bottleneck, much less one whose discrete structure is
constantly evolving in challenging ways.  I believe that even as
the programs get more sophisticated in the current regime, because
all programs are retained, this doesn't really create greater
challenge for the network; just a bit more temporary busywork.

In order to make room for new representations to still be introduced
as new representations are discovered, we need to cull the representations
of some percent of its least frequently selected members.  What remains
will be the frontier, which will then be refilled with whatever number
of new representations can be discovered within a certain time limit
and do not exceed the given maximum size.  The changes saved with
this commit include:

 - correction of unequal parameters between `raven_baseline` and
   `raven_psn`
 - addition of vqvae-style baseline testing the influence of
   quantization alone.
 - modification of semantics of `beta` parameter; it now shrinks the
   prequantizer loss by a factor of beta if beta is a fraction less
   than one, and shrinks the codebook loss by a factor of 1 / beta
   if beta is greater than one.
 - implementation of a modification of the `Quantizer` class so that
   it is no longer a residual unit; all backpropagation occurs via
   the GNN.

---

