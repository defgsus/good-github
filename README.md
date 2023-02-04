## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-03](docs/good-messages/2023/2023-02-03.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,145,555 were push events containing 3,303,018 commit messages that amount to 258,330,356 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[4ce115a2a2...](https://github.com/realforest2001/forest-cm13/commit/4ce115a2a26f8b6664a230bdaff483a1889f17c4)
#### Friday 2023-02-03 00:06:29 by carlarctg

Adds Ludicrously In-Depth Black Market to Recquisitions. (#2014)

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

VASTLY enhances the Black Market. Black market items are obtainable by
deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.

Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...

Various valuable, rare, or otherwise interesting items now have a 'black
market value' that allows them to be sent down the ASRS elevator in
exchange for black market points to order various things with. Anything
that's 'rare' is probably worth something. Added a scanner to the black
market to let them detect said points.

Added DIALOGUE to the black market.

FIxed some construction wirecutter steps needing a screwdriver for some
reason.

Changed up Req's mapping to add a hidden storage room.

slightly changed human remains' description

Added the maintenance jack, can be found in the black market for now.

Improved supply shuttle code somewhat.

# Explain why it's good for the game

> VASTLY enhances the Black Market. Black market items are obtainable by
deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.

Black Market is comically underused, by comically enhancing it like this
it will freshen shipside roleplay and create new and interesting
scenarios for MPs, req, and bystanders to interact with.

> Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...

The contraband needs to be actually meaningful to the players for it to
have any impact. The list of loot has been curated so that players will
be intrigued, but will not be able to abuse it for
too-stronger-than-usual gear without blatant drawbacks.

> Various valuable, rare, or otherwise interesting items now have a
'black market value' that allows them to be sent down the ASRS elevator
in exchange for black market points to order various things with. Added
a scanner to the black market to let them detect said points.

This means CTs could go on scavenger hunts through the ship, evading
curious MPs to sift through maintenance and various hidey holes scanning
everything.

> Added DIALOGUE to the black market.

Finally, we have dialogue in CM! The very first human NPC. We're
ignoring WO because nobody likes WO.

> FIxed some construction wirecutter steps needing a screwdriver for
some reason.

Necessary in this PR to avoid stupid confusion when deconstructing the
computers.

> Changed up Req's mapping to add a hidden storage room.

To let CTs hide their goodies so they won't be in open sight. NOT DONE
YET!

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
add: VASTLY enhances the Black Market. Black market items are obtainable
by deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.
add: Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...
add: Various valuable, rare, or otherwise interesting items now have a
'black market value' that allows them to be sent down the ASRS elevator
in exchange for black market points to order various things with.
Anything that's 'rare' is probably worth something. Added a scanner to
the black market to let them detect said points.
add: Added DIALOGUE to the black market.
fix: FIxed some construction wirecutter steps needing a screwdriver for
some reason.
spellcheck: slightly changed human remains' description
add: Added the maintenance jack, can be found in the black market for
now.
code: Improved supply shuttle code somewhat.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>
Co-authored-by: XSlayer300 <35091844+XSlayer300@users.noreply.github.com>
Co-authored-by: Segrain <Segrain@users.noreply.github.com>
Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>

---
## [jinjieSpring/odoo-16](https://github.com/jinjieSpring/odoo-16)@[f05491105f...](https://github.com/jinjieSpring/odoo-16/commit/f05491105f93939490cbeb078cb7653c38685644)
#### Friday 2023-02-03 00:14:07 by Romain Derie

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

closes odoo/odoo#111531

X-original-commit: 8f24aba86faf2639109b56887781b0daaf60be98
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [Dantesousa/Nebula13-Reborn](https://github.com/Dantesousa/Nebula13-Reborn)@[ffac8f0df0...](https://github.com/Dantesousa/Nebula13-Reborn/commit/ffac8f0df07c8473e26420a8fe3c1acf6bd20dbf)
#### Friday 2023-02-03 00:16:37 by SkyratBot

[MIRROR] Fixes critical plane masters improperly not being readded in show_to [MDB IGNORE] (#19060)

Fixes critical plane masters improperly not being readded in show_to (#72604)

## About The Pull Request

[Adds support for pulling z offset context from an atom's
plane](https://github.com/tgstation/tgstation/commit/9f215c5316e5cfdbedf6a23ff97dfee0e523354b)

This is needed to fix paper bins, since the object we plane set there
isn't actually on a z level.
Useful elsewhere too!

[Fixes compiler errors that came from asserting that plane spokesmen had
a plane
var](https://github.com/tgstation/tgstation/commit/b830002443f2fbe230e9ff00236d7a46a9f2eec7)

[Ensures lighting backdrops ALWAYS exist for each lighting
plane.](https://github.com/tgstation/tgstation/commit/0e931169f7c5336333bc6f41353c82f603fc1170)

They can't float becuase we can see more then one plane at once yaknow?

[Fixes parallax going to shit if a mob moved zs without having a
client](https://github.com/tgstation/tgstation/commit/244b2b25baecfc644505a3ea1e348e0cb97a04e0)

Issue lies with how is_outside_bounds just blocked any plane readding
It's possible for a client to not be connected during z moves, so we
need to account for them rejoining in show_to, instead of just blocking
any of our edge cases.

Fixing this involved having parallax override blocks for show_plane and
anything with the right critical flags ensuring mobs have JUST the right
PMs and relays.
It's duped logic but I'm unsure of how else to handle it and frankly
this stuff is just kinda depressing.
Might refactor later

[show_to can be called twice successfully with no hide_from
call.](https://github.com/tgstation/tgstation/commit/092581a5c06f7f884f48d41c96fa9300327ef214)

Ensures no runtimes off the registers from this

## Why It's Good For The Game

Fixes #72543
Fixes lighting looking batshit on multiz. None reported this I cry into
the night.

## Changelog
:cl:
fix: Fixes parallax showing up ABOVE the game if you moved z levels
while disconnected
/:cl:

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Time-Green <timkoster1@hotmail.com>

---
## [dagster-io/dagster](https://github.com/dagster-io/dagster)@[84c7e77a81...](https://github.com/dagster-io/dagster/commit/84c7e77a8170aa11b53ef10fda93bc4b33134b1e)
#### Friday 2023-02-03 01:08:15 by Ben Gotow

[dagit] Add ErrorBoundary to Dagit to reduce severity of React errors (#11824)

### Summary & Motivation

Corresponding Internal PR:
https://github.com/dagster-io/internal/pull/4659

Hey folks, this PR wraps key components of Dagit in React "error
boundaries", which give us the opportunity to present errors more
gracefully and let users recover / continue to use other parts of the
app. So far I've added them to:

- The top component that renders page content (everything below the
toolbar)
- The details section of the asset partitions and events pages (which
was a production issue yesterday)
- The asset graph and asset graph sidebar
- The op graph and op graph sidebar
- The run logs container and the run gannt chart
- The instance run timeline
- The `<Dialog />` component (errors in a dialog should never take down
the rest of the page)

Anywhere else we should add these?

### Resetting after errors

The component I added takes a `resetErrorOnChange` prop which acts a bit
like a useMemo dependency list -- if any of the values change and it's
in an error state, it resets the error and tries to render it's subtree
again. We need this for cases where the error boundary is not unmounted
/ remounted but it's content could meaningfully change. (eg: you click
another asset or tab). I think this is better than putting a `key={}` on
the Error Boundary because that would force a re-render on the whole
subtree in the happy case.

### Cloud

In cloud dagit, we need to implement a top level context exposed by the
new Error Boundary class in order to send errors (which are now caught)
to DataDog. I think we also want to change the text to let users know
that their errors are automatically submitted to us, so I made that text
configurable. We can also disable the display of the error stack trace
in cloud if we want to.

### How I Tested These Changes

I tested these changes by adding `throw new Error()` to various React
render methods and verifying that Dagit fails more gracefully. I also
verified that this can catch the infinite recursion bug, which is a bit
of an interesting one, by reverting to last night's code and running
without the GraphQL patch.


![image](https://user-images.githubusercontent.com/1037212/213761842-9c01de3e-aa19-40e8-8ea5-2db143684ea6.png)


![image](https://user-images.githubusercontent.com/1037212/213762126-e94f2f8e-1a82-4d71-b624-525533c34d28.png)

Edit: Updated styling

<img width="727" alt="image"
src="https://user-images.githubusercontent.com/1037212/213804637-46343cb0-34de-4154-bd5e-1f61d0a30e92.png">

Co-authored-by: bengotow <bgotow@elementl.com>

---
## [stevessr/git](https://github.com/stevessr/git)@[f1c903debd...](https://github.com/stevessr/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Friday 2023-02-03 01:44:13 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[36f72a88a7...](https://github.com/KenAdeniji/WordEngineering/commit/36f72a88a7c1f0009bcea49e5f1838b9370cc46b)
#### Friday 2023-02-03 01:59:44 by Ken Adeniji

2023-02-02T17:47:00 ... 2023-02-02T17:48:00
https://github.com/KenAdeniji/WordEngineering/blob/main/IIS/WordEngineering/Alameda%20County%20Health%20Agency%20Care%20Services%20Tri-City%20Community%20Support%20Center%20Behavioral%20Health%20Care%20Services/2022-02-02T1746DennisO'Brien_Abi_Abibat_5107952434.txt

Doctor Dennis O'Brien
mailto:Dennis.O'Brien@acgov.org
(510) 795-2474

Abi Abibat
(510) 795-2434

Alameda County Health Agency Care Services Tri-City Community Support Center Behavioral Health Care Services
39155 Liberty Street Suite G 710
Fremont, California (CA) 94538
United States of America (USA)
Telephone: (510) 795-2434
Fax: (510) 793-3972
webmaster@acbhcs.org

Kehinde Adewumi Adeniji
4762 Canvasback Common
Fremont, California (CA) 94555
(510) 796-8121
mailto:KenAdeniji@hotmail.com
http://KenAdeniji.WordPress.com

Abi Abibat called me earlier today.
I called Abi back and she did not receive my telephone call nor did she call me back.

Thank you and God blesses.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[74144f2bc9...](https://github.com/timothymtorres/tgstation/commit/74144f2bc9e69c9829339a1bd7ffa962e37c0cd0)
#### Friday 2023-02-03 02:13:00 by LemonInTheDark

Fixes some runtime spam from lazyloading/map templates (#73037)

## About The Pull Request

Ensures we don't try and rebuild loading turfs midload

Turf refs persist through destroy, so when we changeturf earlier to get
our turf reservation, we insert our space turfs into the rebuild queue,
and then end up here where we can be rebuilt randomly, midload, with
uninit'd turfs

Avoids starting atmos machine processing until init

This avoids some runtimes with null gasmixtures

There's still trouble with atmos and template loading, pipes start
processing before their pipelines exist, so we just kinda get fucked.
Need to look into this more deeply, it involves pulling this stuff off
`on_construct` and `setup_template_machinery` and throwing it in maybe
late init, which I don't really relish but will just have to do
eventually.

## Why It's Good For The Game

Reduces runtime spam

---
## [shlomenu/program_synthesizing_networks](https://github.com/shlomenu/program_synthesizing_networks)@[d4471c69d1...](https://github.com/shlomenu/program_synthesizing_networks/commit/d4471c69d19a41f61256fd6ff05cc09ee028cf4f)
#### Friday 2023-02-03 02:45:32 by Eli Whitehouse

minor bug fixes

So far, the removal of fine-grained quantization via `out_codebook` does
not seem to have changed the plateauing accuracies I have experienced up
to this point.

In my previous draft of the paper to accompany this code, I was very
focused on the fact that in choosing between courser and finer-grained
nearest-neighbor quantization, one was essentially choosing between more
flexible discrete structure and more flexible continuous structure in
the representation.  I think my underlying intuition was that neural
networks were probably not making much use of the discrete structure
that was created by nearest-neighbor quantization.  Indeed, the
dimensionalities typically used for VQ-VAE-descended architectures
suggest that the goal is generally to be so fine that the discrete
information available is too subtle and voluminous to be of much use.

I believed that if one initially used a courser quantization, then
mapped this choice onto a more complex discrete representation from
which the original continuous information must be discerned with
increased greater precision, I would force the neural network to reckon
with the role of discrete structure of in the more finely quantized
representation.  This has occurred when the prequantizer and GNN have
independently learned to predict the same thing on a different basis.
The out-codebook vectors are gradually made to resemble prequantizer
outputs, and therefore the training data, and the GNN is encouraged
to closely reconstruct these vectors purely from the discrete structure
corresponding to in-codebook vectors.  Consequently, the entire model
should succeed when there is a profitable alignment between training
data and discrete representations that allows out-codebook
representations and discrete representations to coincide.  When this
occurs, the resulting model should generalize more quickly and easily,
as there are fewer "bins" with which to identify new data according
to the course quantization, even if its representation subsequently
becomes more finely differentiated.

This theory presents a compelling case: by constraining the realizable
outputs of the model, course quantization makes it easier to generalize
at test time but harder to learn.  We can ameliorate this by making the
categorical choices of representation the network faces more structured,
informative, and distinct.  However, I don't think the mechanism it
lays out accomplishes this.  As described, the PSN architecture simply
institutes a requirement that the model be able to map the discrete
information captured by a categorical choice of in-codebook vector
(a graph representing its index) to an approximation of the continuous
information captured therein.  In an autoencoding task where training
where there is a clear incentive to map each training data point to a
distinct output, there is no risk of codebook collapse, and training
data outnumber discrete representations, this constraint would force
the model to consider the discrete structure of each of its (limited)
choices.  However in any less perfect condition, such as an autoencoding
task with limited training data or a more typical classification task,
there is little reason to think that the categorical choices faced by
the network are made more meaningfully distinct by this mechanism; it
seems more likely that the potentially large approximation in copied
gradients only encourages them to be less so at convergence.

A better mechanism would ensure that the representation resulting from
the categorical choice of in-codebook vector is always enhanced with
discrete structure through a novel join representation.  Without the
need to enforce equivalence between two separate representations there
is no need to isolate the GNN, and consequently no need for two-stage
quantization.  Thus we may backpropagate through the network in a much
more ordinary way, only using stopgradients for the single course
quantization, as in the VQ-VAE.

In particular, we may design a kind of residual unit where the coursely
quantization of the prequantizer output is packed into the node
representation, and the output of the GNN is transformed such that it
can be added back to the original quantized output before processing
by the postquantizer.  This residual unit with single-stage quantization
still functions as a generic neural network component, but arguably
in a more compelling way.  Furthermore, because the GNN has some context
for how to interpret a particular graph, and is also graded according
to its success at the actual downstream prediction task, we have every
reason to think that the feedback given to the prequantizer bears on
the relevance of the singular codebook's continuous and discrete structure.
Consequently, the prequantizer's choice of codebook index should also
be more informative in guiding distributional program search.

It is worth noting that this scheme is similar in spirit to noisy
generalization.  However, rather than imposing a very simple,
"one dimensional" kind of adjacency between neighboring codebook
vectors, these adjacencies are instead defined by more general
relational structure.

I am hoping that this altered design of a Program Synthesizing Residual
Unit will achieve better than the plateauing accuracies I have continued
to experience with the PSN

In anticipation of the aforementioned changes, a number of bug fixes are
being committed so as to checkpoint the most recent PSN design.  These
include:

 - fix various broken calls from API changes
 - enforce that by passing an empty frontier to `GraphQuantizer.explore`
   you are specifically requesting uniform distributional search
   (i.e. breadth-first search)
 - the mechanism for selecting 2d positional embeddings was not functioning
   properly, as it appears the previous attempt at multidimensional indexing
   was not working as expected; this was fixed by using calls to `torch.gather`.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[6de1258bd3...](https://github.com/tgstation/tgstation/commit/6de1258bd3fb5919bb45f3dac3ae801d4b3bc8d6)
#### Friday 2023-02-03 03:59:43 by Jacquerel

Admins can now choose where fish go (#73109)

## About The Pull Request

I've pigeonholed myself as the fish guy now. It seems like someone made
events easier to add admin controls for so I thought I'd add some to the
event I most recently touched.

Instead of letting the RNG choose admins can now direct a circle of carp
to converge upon a specific location, or even a trail of specific
locations if they want the carp to just sort of swim in a circle around
the space station (although the ones on the far side of the station from
the starting point will travel all the way through it to get there).
This also works with magicarp.
They don't really move fast enough for you to use this to punish a
specific person but you can use it to annoy a specific location full of
people.

Plausibly there's no reason the code _wouldn't_ work for a specified
atom instead of a turf (as long as it sticks to one z level) but I
couldn't think of an elegant way of selecting that whereas "use my
current ghost location" is very intuitive, so I didn't add one.

## Why It's Good For The Game

Plausibly this permits admins do more fun things.

## Changelog

:cl:
admin: Admins can direct where carp (or magicarp) are interested in
going when manually triggering the event
/:cl:

---
## [em-go/emgo.space.web](https://github.com/em-go/emgo.space.web)@[208b92049a...](https://github.com/em-go/emgo.space.web/commit/208b92049adfbd547d76267295e266fe8b1f39de)
#### Friday 2023-02-03 04:12:34 by em

Create LICENSE.md

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

---
## [NotAKidOnSteam/MenuScalePatch](https://github.com/NotAKidOnSteam/MenuScalePatch)@[4a5527d7de...](https://github.com/NotAKidOnSteam/MenuScalePatch/commit/4a5527d7de0e7c59defcd910c3827487b19e3668)
#### Friday 2023-02-03 04:27:35 by NotAKidoS

i hate all

holy shit this fucking bug took me two hours to fix
why was the solution so simple... fuck

---
## [Korywon/tgstation](https://github.com/Korywon/tgstation)@[eb6c0eb37c...](https://github.com/Korywon/tgstation/commit/eb6c0eb37c095c188074c7cec98bf5bf36a2cf04)
#### Friday 2023-02-03 04:48:07 by Jacquerel

Dogs use the Pet Command system (#72045)


About The Pull Request

Chiefly this refactors dogs to use the newer component/datum system for "pet which follows instructions". It also refactors it a little bit because I had better ideas while working on this than I had last week. Specifically, instead of passing around keys we just stick a weakref to our currently active behaviour in the blackboard. Basically the same but skipping an unecessary step.

Additionally it adds a component for the previous "befriending a mob by clicking it repeatedly" behaviour which hopefully we won't use too much because it's not very exciting (I am planning on replacing it for dogs some time after Christmas).
The biggest effort in here was making the Fetch command more generic, which includes multiple behaviours (which might be used on their own?) and another component (for holding an item without hands).

Additionally I noticed that dogs would keep following my instructions after they died.
This seems unideal, and would be unideal for virtually any AI controller, so I added it as an AI_flag just in case there's some circumstance where you do want to process AI on a dead mob.

Finally this should replicate all behaviour Ian already had plus "follow" (from rats) and a new bonus easter egg reaction, however I noticed that the fetch command is supposed to have Ian eat any food that you try to get him to fetch.
This has been broken for some time and I will be away from my desk for a couple weeks pretty soon, so I wrote the behaviour for this but left it unused. I will come back to this in the future, once I figure out a way to implement it which does not require adding the "you can hit this" flag to every edible item.

Also I had to refit the recent addition of dogs barking at felinids to fit into this, with a side effect that now dogs won't get mad at a Felinid they are friends with. This... feels like intended behaviour anyway?
Why It's Good For The Game

It's good for these to work the same way instead of reimplementing the same behaviour in multiple files.
Being able to have Ian (or other dogs) follow you around the station is both fun and cute, and also makes him significantly more vulnerable to being murdered.
Changelog

cl
add: Ian has learned some new tricks, tell him what a good boy he is!
add: Ian will come on a walk with you, if you are his friend.
refactor: Ian's tricks work the same way as some other mobs' tricks and should be extendable to future mobs.
fix: Dogs no longer run at the maximum possible speed for a mob at all times.
add: When Ian gets old, he also slows down. Poor little guy.
add: Dogs will no longer dislike the presence of Felinids who have taken the time to befriend them.
/cl

---
## [FoxLisk/NMG-League-Bot](https://github.com/FoxLisk/NMG-League-Bot)@[dc0d2018a6...](https://github.com/FoxLisk/NMG-League-Bot/commit/dc0d2018a6292cc5ca914efff2a2dc942bd5f605)
#### Friday 2023-02-03 05:11:09 by Alexander

Merge pull request #63 from FoxLisk/qualifier-submissions-and-holy-shit-github-desktop-sucks

Qualifier submissions and holy shit GitHub desktop sucks

---
## [WagicProject/wagic](https://github.com/WagicProject/wagic)@[c757c2c2fc...](https://github.com/WagicProject/wagic/commit/c757c2c2fca42a1a2b07ccaf095fa21ae3fec992)
#### Friday 2023-02-03 05:41:31 by Eduardo MG

Macros for Ward and for play top of library from exile, bug fixes

Batterbone
Ormos, Archive Keeper crashes the game while drawing if you have less than 5 cards in library
Primal Command crashed the game
Austere Command not really supported
Shivan Wumpus crashed the game
Go-Shintai of Life's Origin
Diregraf Horde
Unblinking Observer
Cairn Wanderer
Old Man of the Sea
Grow from the Ashes
Scourge of Nel Toth
Faceless Butcher
Portal to Phyrexia
Avenging Druid
Teysa, Envoy of Ghosts
Siege Veteran
Sparring Regimen
Skinwing
Stampede
Collector Ouphe
Terror of Mount Velus
Vizier of the True
Demonic Vigor

---
## [tomara-x/moths](https://github.com/tomara-x/moths)@[c0aa2281d4...](https://github.com/tomara-x/moths/commit/c0aa2281d4089d2df8b58692c4b3ad352e9352b2)
#### Friday 2023-02-03 05:51:22 by tomara_x

holy shit!

i don't know what it is, but holy fucking shit! oversampling does some
stuff!

---
## [Nanu308/cmss13](https://github.com/Nanu308/cmss13)@[558717e6f6...](https://github.com/Nanu308/cmss13/commit/558717e6f627bf2bdc8e00c620db04c0a55cede0)
#### Friday 2023-02-03 06:56:21 by zeroisthebiggay

(hopefully) webedits a grammatical correction into headbite's kill message (#2537)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

when someone dies to headbite it displays as
`Urr Mot'herr has died to executed by headbite at the Containers from
Elder Lurker (GIT-222)`
hopefully with this simple one line webedit it should instead be
`Urr Mot'herr has died to headbite execution at the Containers from
Elder Lurker (GIT-222)`
god fucking knows if this is the right line

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

uhm
it reads better

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

github

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
spellcheck: 'executed by headbite' to 'headbite execution' when listing
someone dying to a headbite in deadchat
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Roadhog360/Et-Futurum-Requiem](https://github.com/Roadhog360/Et-Futurum-Requiem)@[8f90447043...](https://github.com/Roadhog360/Et-Futurum-Requiem/commit/8f9044704355203f71c84f4763ad40f82f26c2db)
#### Friday 2023-02-03 07:29:32 by Roadhog360

Fix build failure because IntelliJ apparently has trouble showing build errors...

And just like that, I went from thinking this IDE was 10/10, to 0/10 because apparently IntelliJ thinks it's a good idea to WAIT UNTIL YOU OPEN A FILE TO SHOW YOU A FUCKING COMPILE ERROR. And the sane behavior is FUCKING DEFAULT TO OFF!?

but if I go back to Eclipse I gotta deal with slow BS, no mod dev plugin and files randomly not saving. Why does no fucking functioning IDE exist?

---
## [linwenbo/gpdb](https://github.com/linwenbo/gpdb)@[1f5ef5ae08...](https://github.com/linwenbo/gpdb/commit/1f5ef5ae0806cb75bb0297e46e41765ffa426252)
#### Friday 2023-02-03 07:52:03 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [GuillaumeWaignier/fibaro](https://github.com/GuillaumeWaignier/fibaro)@[c97e7af345...](https://github.com/GuillaumeWaignier/fibaro/commit/c97e7af3459cb3ff088b22dea4201e5f14bab973)
#### Friday 2023-02-03 07:59:42 by PeterV989

Updating the setpoints wasn't working as expected

I installed your update and played around with it. The first glaring problem was that the setpoint for the unchanged setpoint does not need to be converted to °C. The value you are using is already in Celsius. I simply removed the call to getDegreesCelsius for that setpoint.

This next problem is very subtle. I tried to track down a way to fix it but can't quite do that yet. The problem is that when I change both setpoints in the device screen, only the last change is sent to the thermostat. What I mean by that is that since the heating setpoint is updated first, the value doesn't get updated in the traits area or properties area. Then the cooling setpoint is changed but the old heating setpoint is still in the body['traits']['sdm.devices.traits.ThermostatTemperatureSetpoint'] (perhaps because while the value may have been sent to the thermostat, the thermostat has not been read back into the body yet?). My thoughts were to have an setAutoThermostatSetpoint() method and use it when the device is in Auto mode. But, for the life of me, I can't see where those methods are connected to the event system. That may not make sense within the context of the Fibaro system but IMHO the documentation is very sparse and your ability to have hunted down the mechanisms for all of this is astounding. (Maybe when I grow up I can be just like you [weird American humor]).

And finally, this won't be a problem for me but a final check should prevent the cooling setpoint to be less than the heating setpoint. I notice in the Nest app when I bump one value up or down towards the other value it automatically adjusts the value to keep them 2° or 3° different. Not at all sure of a clean way to do that other than to pick one and adjust it when that condition is met.

If I can help further with my setup just let me know. I'm happy to oblige.

Peter

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[128bbe6516...](https://github.com/TaleStation/TaleStation/commit/128bbe6516b3ddccdbc23784c578d41fd6a05c00)
#### Friday 2023-02-03 09:32:02 by TaleStationBot

[MIRROR] [MDB IGNORE] Cleans Up (a few) Single-Lines Over 300 Characters (#4389)

Original PR: https://github.com/tgstation/tgstation/pull/73124
-----
## About The Pull Request

These were just super long picks with multiple strings/file
references/whatever, let's convert it into a list of picks, maybe do
some cool proc stuff, just make it look NICER.

I found it by doing `rg '.{300,}' code > output.txt` from the root of my
repository (used ripgrep because that's what i had at the time), and you
can see a copy of the results I got here:
https://github.com/tgstation/tgstation/files/10553651/output.txt in case
you wanna take a stab at it. I didn't filter by .dm code file, so
there's a few bulky JSONs and MD sections, but maybe those are good
candidates for splitting up the wording or otherwise prettifying the
JSON? Unsure.
## Why It's Good For The Game

It really fucking sucks to have to scroll horizontally for three years
in order to fix a typo or something.
## Changelog
Nothing that concerns players.

I also did the mi-go stuff, but I'm going to split that into it's own PR
so it's easier to deal with impending conflicts. Besides, that one is a
bit soulful, and I'd rather my changes be discussed in a different PR
entirely.

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[406b6870bd...](https://github.com/Sonic121x/Skyrat-tg/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Friday 2023-02-03 11:22:58 by SkyratBot

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
## [avar/git](https://github.com/avar/git)@[69bbbe484b...](https://github.com/avar/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Friday 2023-02-03 12:24:47 by Jeff King

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
## [prembala1710/CliqInformerProject](https://github.com/prembala1710/CliqInformerProject)@[90696d449d...](https://github.com/prembala1710/CliqInformerProject/commit/90696d449d4c738be92e6d3dcf5619cf6476c252)
#### Friday 2023-02-03 15:28:00 by prem-pt6970

An informant (also called an informer or, as a slang term, a “snitch”)[1] is a person who provides privileged information about a person or organization to an agency. The term is usually used within the law-enforcement world, where informants are officially known as confidential human sources (CHS), or criminal informants (CI). It can also refer pejoratively to someone who supplies information without the consent of the involved parties.[2] The term is commonly used in politics, industry, entertainment, and academia.[3][4] In the United States, a confidential informant or "CI" is "any individual who provides useful and credible information to a law enforcement agency regarding felonious criminal activities and from whom the agency expects or intends to obtain additional useful and credible information regarding such activities in the future".[5] Criminal informants Informants are extremely common in every-day police work, including homicide and narcotics investigations. Any citizen who provides crime related information to law enforcement by definition is an informant.[6] Law enforcement and intelligence agencies may face criticism regarding their conduct towards informants. Informants may be shown leniency for their own crimes in exchange for information, or simply turn out to be dishonest in their information, resulting in the time and money spent acquiring them being wasted. Informants are often regarded as traitors by their former criminal associates. Whatever the nature of a group, it is likely to feel strong hostility toward any known informers, regard them as threats and inflict punishments ranging from social ostracism through physical abuse and/or death. Informers are therefore generally protected, either by being segregated while in prison or, if they are not incarcerated, relocated under a new identity. Informant motivation FBI Anchorage aid for assessing confidential human sources Informants, and especially criminal informants, can be motivated by many reasons. Many informants are not themselves aware of all of their reasons for providing information, but nonetheless do so. Many informants provide information while under stress, duress, emotion and other life factors that can affect the accuracy or veracity of information provided. Law enforcement officers, prosecutors, defense lawyers, judges and others should be aware of possible motivations so that they can properly approach, assess and verify informants information. Generally, informants motivations can be broken down into self-interest, self-preservation and conscience. A list of possible motivations includes: Self-Interest: Financial reward[7] Pre-trial release from custody Withdrawal or dismissal of criminal charges Reduction of sentence Choice of location to serve sentence Elimination of rivals or unwanted criminal associates. Elimination of competitors engaged in criminal activities. Diversion of suspicion from their own criminal activities. Revenge[7] Self-Preservation: Fear of harm from others. Threat of arrest or charges. Threat of incarceration. Desire for witness protection program. Conscience: Desire to leave criminal past Guilty conscience Genuine desire to assist law enforcement and society.[8] Labor and social movements Corporations and the detective agencies that sometimes represent them have historically hired labor spies to monitor or control labor organizations and their activities.[9] Such individuals may be professionals or recruits from the workforce. They may be willing accomplices, or may be tricked into informing on their co-workers unionization efforts.[10] Paid informants have often been used by authorities within politically and socially oriented movements to weaken, destabilize and ultimately break them.[11] Politics A redacted version of the FBI policy manual concerning the use of informants Informers alert authorities regarding government officials that are corrupt. Officials may be taking bribes or be participants in a money loop also called a kickback. Informers in some countries receive a percentage of all monies recovered byt

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[cb2175245a...](https://github.com/pytorch/pytorch/commit/cb2175245a5959fd4598866ae9c75e6000441b29)
#### Friday 2023-02-03 16:01:19 by Brian Hirsh

Update base for Update on "add torch.autograd._set_view_replay_enabled, use in aot autograd"

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

In this PR, I added some TLS for instructing autograd to do view replay instead of as_strided, even when given a normal tensor. I'm definitely interested in thoughts from autograd folks (cc albanD soulitzer). A few points that I want to bring up:

(1) One reason that this API seems generally useful to me is because of the case where you `torch.compile()` a function, and you pass in two inputs that alias each other, and mutate one of the inputs. Autograd is forced to add a bunch of as_strided() calls into the graph when this happens, but this would give users an escape hatch for better compiled perf in this situation

(2) To be fair, AOT Autograd probably won't need this TLS in the long term. There's a better (more complicated) solution, where AOT Autograd manually precomputes the view chain off of graph intermediates during tracing, and re-applies them at runtime. This is kind of complicated though and feels lower priority to implement immediately.

(3) Given all of that I made the API private, but lmk what you all think.

This is a followup of https://github.com/pytorch/pytorch/pull/92255.




[ghstack-poisoned]

---
## [Floofies/tgstation](https://github.com/Floofies/tgstation)@[a47afd9051...](https://github.com/Floofies/tgstation/commit/a47afd905156bcc9a070db015cec7b1d1a07c578)
#### Friday 2023-02-03 17:07:18 by Sol N

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
## [vizionsin/yugioh](https://github.com/vizionsin/yugioh)@[333371f6b7...](https://github.com/vizionsin/yugioh/commit/333371f6b7fa533b433fc36eed20a2da28416532)
#### Friday 2023-02-03 17:17:58 by miguel

bro

Don't care for other ppl think bout you. if ppl like you, they like you, and if they don't they don't. get over it dude cuz that's just how life works and if ur sorry ass can't accept that, you do you, sis. I rest my case.

---
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[ba57c05af4...](https://github.com/KenAdeniji/WordEngineering/commit/ba57c05af493551a4dfa9c1819abdfc1aa2c5f0d)
#### Friday 2023-02-03 18:19:45 by Ken Adeniji

2023-02-02T17:47:00 ... 2023-02-02T17:59:00
https://github.com/KenAdeniji/WordEngineering/blob/main/IIS/WordEngineering/Alameda%20County%20Health%20Agency%20Care%20Services%20Tri-City%20Community%20Support%20Center%20Behavioral%20Health%20Care%20Services/2022-02-02T1746DennisO'Brien_Abi_Abibat_5107952434.txt

Maureen	Orphanos
Behavioral Health Clinical Manager
Alameda County Health Agency Care Services Tri-City Community Support Center Behavioral Health Care Services
mailto:Maureen.Orphanos@acgov.org
(510) 795-2478
(925) 560-5888

Doctor Dennis O'Brien
mailto:Dennis.O'Brien@acgov.org
(510) 795-2474
(510) 600-0617

Abi Abajiboye
(510) 795-2434

Alameda County Health Agency Care Services Tri-City Community Support Center Behavioral Health Care Services
39155 Liberty Street Suite G 710
Fremont, California (CA) 94538
United States of America (USA)
Telephone: (510) 795-2434
Fax: (510) 793-3972
webmaster@acbhcs.org

Kehinde Adewumi Adeniji
4762 Canvasback Common
Fremont, California (CA) 94555
(510) 796-8121
mailto:KenAdeniji@hotmail.com
http://KenAdeniji.WordPress.com

Abi Abibat called me earlier today.
I called Abi back and she did not receive my telephone call nor did she call me back.

Thank you and God blesses.

2023-02-02T20:37:00 I called and I left a voice mail for doctor Dennis O'Brien on (510) 600-0617.
	Sustenance of the truth.

2023-02-03T09:59:00 Doctor Dennis O'Brien said, I am probably not be coming back to work.
2023-02-03T10:03:00 I called Abi back and she did not receive my telephone call nor did she call me back.

---
## [BBBBAface/Voidcrew-LRP](https://github.com/BBBBAface/Voidcrew-LRP)@[a05d69d10a...](https://github.com/BBBBAface/Voidcrew-LRP/commit/a05d69d10a26b502d8ef6fe86b023fd95025ca0f)
#### Friday 2023-02-03 18:30:13 by Addust

oh my fucking god I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JS…

---
## [jarrodjeffi/origin-story](https://github.com/jarrodjeffi/origin-story)@[ef949f9ff0...](https://github.com/jarrodjeffi/origin-story/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Friday 2023-02-03 20:23:59 by ICXCNIKA

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
## [Gnuxie/Draupnir](https://github.com/Gnuxie/Draupnir)@[72f554ef2e...](https://github.com/Gnuxie/Draupnir/commit/72f554ef2e1f9354949fb9258e4f556ea03dae97)
#### Friday 2023-02-03 20:32:21 by gnuxie

Improve HTTP Error handling.

So as a history lesson.
The Matrix Bot SDK uses the npm library "requests".
When there was a http error, matrix-bot-sdk
would literally throw the response object.
This would be a horrible 1000+line long thing to accidentally
be logged to the console via node's inspect.
Though it was inevitable since you can't be sure every catch
was handling the error correctly. Irregardless, the solution
developed at Element was to create an error object
that had concise details.
This was great, however, within the matrix-bot-sdk there is
[this](https://github.com/Half-Shot/matrix-bot-sdk/blob/f58d7ea6e24d1db8b9b8009dea4cd97cbff54d0c/src/http.ts#L66)
awful line of code which logs every http error as error using the
matrix-bot-sdk logger.
This wastes so much log space and causes alarm fatigue,
rather than muting the module, the action instead taken
was to redact stack traces from http errors.
This was not a good idea.
Eventually matrix-bot-sdk was updated to have a MatrixError type
when a request was performed via the client-server api that had an
error.
matrix-appservice-bridge depends upon this and so Mjolnir now needs
to be updated to throw MatrixError's.
We have gone a step further in this commit and also muted
the matrix-bot-sdk http module, to stop the alarm fatigue problem
https://github.com/turt2live/matrix-bot-sdk/pull/158

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[25f4961156...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/25f4961156121121aa9b545cfc9f6014b89c2362)
#### Friday 2023-02-03 20:53:19 by SkyratBot

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
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[e9c87c0acb...](https://github.com/Helg2/tgstation/commit/e9c87c0acb15439c8f577bba35c45f51bf03d1aa)
#### Friday 2023-02-03 21:26:27 by LemonInTheDark

Starlight Polish (Space is blue!) (#72886)

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

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[fc12508d01...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/fc12508d01830198416938d9fe0766d2b83101ad)
#### Friday 2023-02-03 21:59:48 by SkyratBot

[MIRROR] STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows [MDB IGNORE] (#18775)

* STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows (#72282)

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

* STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [mikestef9/ack-test-infra](https://github.com/mikestef9/ack-test-infra)@[95e4857b28...](https://github.com/mikestef9/ack-test-infra/commit/95e4857b28122c6c5f8a30260be3dcac94e0e466)
#### Friday 2023-02-03 22:11:33 by Amine

Move Go binaries to `/usr/bin` (#287)

Issue https://github.com/aws-controllers-k8s/community/issues/1640

TL;DR: Prow was mounting `test-infra` code volume into `$GOPATH`
causing the deletion of `kind` and `controller-gen` binaries that are
installed in `$GOPATH/bin`


Yesterday, i embarked on a wild 7 hour journey to fix a bug that had
been causing prow jobs to fail with the error message "Kind not found".
The bug was introduced after a recent update that bumped the Go compiler
to `1.19`. I found the investigation to this bug to be both interesting
and frustrating, so i wanted to share some key takeways with the
community:

[The patch](https://github.com/aws-controllers-k8s/test-infra/commit/14dda81ce8ea430b51c9ce738483bea3744a5450) that introduced Go `1.19` also modified a `go get` command
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
the `PATH` variable didn't include the `GOBIN` path, which is supposed
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

Anyways, for now, i'm just gonna implement a quick fix that moves the
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

By submitting this pull request, I confirm that my contribution is made under the terms of the Apache 2.0 license.

---
## [alynch-ni/ni-linux](https://github.com/alynch-ni/ni-linux)@[2f722caecd...](https://github.com/alynch-ni/ni-linux/commit/2f722caecd547353ec47758cc9186567a61b125a)
#### Friday 2023-02-03 22:37:25 by Karthik Manamcheri

8250: Do not create ttyS* nodes for nonexistant devices

This commit is a merge of two upstream-unfriendly commits:
   commit ba93f2d13b34 ("8250: Make SERIAL_8250_RUNTIME_UARTS work correctly")
   commit 0d1ed2d7adc1 ("Revert "serial: 8250: Do nothing if nr_uarts=0"")

This was an attempt to resolve an architectural oddity in the 8250 core
code, which was that, by design, it will create a static (build- or
cmdline-specified) number of ttyS* devices, which is at odds with how
most other Linux kernel drivers work. The original commit messages did
not accurately describe the problem, so this is a merge-and-replace in
order to get a better commit description. So, without further ado:

The current state of affairs is as follows:

There exists two build-time constants.
   - CONFIG_SERIAL_8250_NR_UARTS: the build-time max number of 8250 UARTs.
   - CONFIG_SERIAL_8250_RUNTIME_UARTS: the boot-time number of 8250 UARTs.
        (confusingly, this is also the default setting of 8250.nr_uarts)

The way that the 8250 driver handles creation of ttyS* device is that, at
initialize time, we create min(8250.nr_uarts, NR_UARTS) ttyS* devices
up-front, and when a UART is registered, serial8250_find_match_or_unused
will either merge it in under an existing ttyS* or find an unused one.

There also exists code in the 8250 driver to automatically enumerate the
UARTs specified in the SERIAL_PORT_DFNS table; these are the "well-known"
ports at 0x3F8/0x2F8/0x3E8/0x2E8 from the IBM PC platform, and they are
added this way because they predate the use of ACPI tables for enumeration.

(Oh, and also you can point the ttyS* devices to completely different
addresses from userspace via TIOCSSERIAL.)

This has two ramifications for NI devices:

1) There is a limit on number of UARTs with 8250_core; this is a noteworthy
   problem when you are also a vendor of multiport serial cards, such as
   the PXIe-8430/16. However, the user experience of increasing the limit
   with a generic platform kernel is also bad; if, as a distro, we release
   a kernel with a default limit of 128, then users that have PXI systems
   that don't have any multiport serial cards will still be presented with
   devices named ttyS0 through ttyS127, even though most of them are just
   "empty" slots that are not backed by real devices.

2) ttyS0 through ttyS3 will always be given the addresses for the "legacy"
   serial ports, even if on-board controller ports are at different
   addresses. This is the case on several NI controllers; for example, on
   some sbRIO products [1] the UARTs are at 0x3F8, 0x350, 0x360, etc.
   However, because the legacy ports get first-dibs, those ports will be
   ttyS0, ttyS4, ttyS5, ... because the legacy 0x2f8/0x3E8/0x2E8 get S1-S3.

Our initial attempt at resolving this was to redefine 8250.nr_uarts to mean
"the number of automatically-created UART entries" and define it to be 0
(because we neither want the legacy ports nor the extra "empty" ports). On
NI platforms, all serial ports are described in the ACPI table, so legacy
enumeration is neither necessary nor desirable. However, this approach got
soundly rejected upstream because it "caused existing kernel configurations
to act differently from before" [2].

We're not alone in finding the upstream behavior to be counterintuitive;
I have found at least two other attempts [3, 4] to resolve it with similar
pushback of the form "this breaks existing users".

A "proper" upstreamable solution probably needs two parts, with the default
settings such that the current behavior is retained but can be opted-out
(via Kconfig and/or kernel cmdline).
- a config token for "don't create a bunch of empty devices" (1)
- a config token for "don't add legacy ports, let ACPI handle it" (2)

Until that arrives, we're stuck keeping this around, because we're _also_
stuck with not wanting to renumber ttyS* devices from the way we've shipped
them.

[1] https://github.com/ni/meta-nilrt/blob/8106f31da6980ee4ee94fa0e03b991479d9aa43e/recipes-kernel/kernel-tests/kernel-tests-files/test_kernel_serial_devices.sh#L127
[2] https://lore.kernel.org/lkml/20130603213754.GA15479@kroah.com/
[3] https://lore.kernel.org/linux-serial/1420513785-23660-1-git-send-email-peter@hurleysoftware.com/
[4] https://lore.kernel.org/linux-serial/20221025073944.102437-1-martin@geanix.com/

[SBOs from initial patches]
Natinst-CAR-ID: 634278
Signed-off-by: Karthik Manamcheri <karthik.manamcheri@ni.com>
Signed-off-by: Richard Tollerton <rich.tollerton@ni.com>
Signed-off-by: Brad Mouring <brad.mouring@ni.com>
Natinst-ReviewBoard-ID: 183619

Upstream-Status: Denied [rejected upstream]
Natinst-AzDO-ID: 2133864
Signed-off-by: Brenda Streiff <brenda.streiff@ni.com>

---
## [goober3/hi-github-portside](https://github.com/goober3/hi-github-portside)@[f1adf3f2d0...](https://github.com/goober3/hi-github-portside/commit/f1adf3f2d0a1b7690b3ffc5b81d6ace7b376490b)
#### Friday 2023-02-03 23:52:10 by goober3

fuck you! the megacarp is no longer called geroge.

---

