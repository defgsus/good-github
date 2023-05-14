## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-13](docs/good-messages/2023/2023-05-13.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,750,967 were push events containing 2,676,347 commit messages that amount to 145,525,235 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [sirdarckcat/linux-1](https://github.com/sirdarckcat/linux-1)@[1bba82fe1a...](https://github.com/sirdarckcat/linux-1/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Saturday 2023-05-13 00:06:24 by Darrick J. Wong

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
## [gitstart/sourcegraph](https://github.com/gitstart/sourcegraph)@[bbfce81a35...](https://github.com/gitstart/sourcegraph/commit/bbfce81a35562d84386862e854ef6b35b555a92a)
#### Saturday 2023-05-13 00:22:31 by Juliana Peña

web/app: remove hover on navbar items to stop focus from being moved (#51739)

The dropdown menu items in the global navbar (Search and, in App,
Feedback) move focus when you hover over them. This is bizarre, ugly,
and most likely a [WCAG
violation](https://www.w3.org/TR/WCAG21/#focus-order). I spent some time
yesterday and the root cause is that the [Reach menu button we use does
not support hover at all](https://github.com/reach/reach-ui/issues/278)
and we're hacking it by [sending a mousedown event when you hover over
the
button](https://sourcegraph.com/github.com/sourcegraph/sourcegraph/-/blob/client/web/src/nav/NavBar/NavDropdown.tsx?L58).

There are two options I can think of to mitigate this bug:
1. Get rid of hover events and only open the dropdowns on click. This is
the easiest option, but obviously removes the ease of accessing the menu
for mouse users.
2. Rewrite the dropdown nav items to use a custom menu instead of Reach.
This is more expensive because we have to reimplement lots of a11y stuff
here, but we can have more fine-grained control of different UI flows
for mouse hover vs mouse click vs keyboard users.

I went with the first option following @almeidapaulooliveira's
[feedback](https://sourcegraph.slack.com/archives/C0HMGV90V/p1683735888755969?thread_ts=1683734992.157499&cid=C0HMGV90V).

The following changes were applied to `NavDropdown`:

- Removed all hover and touch events; now only a click will open the
menu.
- Removed the split button; now clicking anywhere on the button will
always open the menu.
- Made the mobile home item into a "generic" home item and always
visible when present.
- Made the home item optional (since the Feedback menu item in the
desktop app doesn't have a home item/route).
- Added customizable a11y names; in the past, the only dropdown was the
Search one, but in App we now have Feedback; the a11y labels were still
saying "Search" before this change.

Additionally, the following changes were applied for polish:

- The double-focus ring on the back/forward buttons in the Tauri app has
been fixed
- Styling changes made to simplify code

## Test plan

The global navbar has extensive visual and behavior test coverage.

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[81c1229373...](https://github.com/silicons/Citadel-Station-13-RP/commit/81c1229373208790c3375a138579aaf76a0006d0)
#### Saturday 2023-05-13 00:32:15 by Captain277

Adds Just Like, a Ton of Clothes (#5048)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. **Adds a wide array of clothes, listed below.**

## Why It's Good For The Game

1. _My good friend Tech provided me with some sprite sheets when I was
working on Ashlanders, requesting a hobo coat. Going through the sheets
I found several different items I thought it would be fun to add to our
expanding list of customization and fashion options. The list is huge so
I'm just gonna itemize it here. As for attributions, as I understand it
most of this is from a D&D server, and some from a 40k server._
2. _Two of the outfits, the Belial and Lilin items, are sprites crafted
by our very own Doopy, as part of their Lindenoak line!_

## Outfits & Where to Get them

**Costume Vendor**
1. _Banana Costume_
3. _Hashashin Costume_
4. _Bard Hat_
5. _Aquiline Enforcer Uniform_
6. _Scavenging Sniper Set_
7. _Spiral Hero Outfit_
8. _Body Tape Wrapping_
9. _Redcoat Uniform_
10. _Despotic General Uniform_
11. _Post-Revolution American Uniform_
12. _Prussian Uniform_

**Suit Vendor**
1. _Ragged Coat_
2. _Spiral Hero Cloak_
3. _Nerdy Shirt_

**Jumpsuit Vendor**
1. _Toga_
2. _Countess Dress_
3. _Baroness Dress_
4. _Revealing Cocktail Dress_
5. _Belial Striped Shirt and Shorts_
6. _Lilin Sash Dress_

**Shoes Vendor**
1. _Utilitarian Shoes_

**Loadout**
1. _Ragged Coat_
7. _Spiral Hero Cloak_
8. _Nerdy Shirt_
9. _Bard Hat_
10. _Utilitarian Shoes_
11. _Toga_
13. _Countess Dress_
14. _Baroness Dress_
15. _Scavenging Sniper Set_
16. _Spiral Hero Outfit_
17. _Body Tape Wrapping_
18. _Revealing Cocktail Dress_
19. _Belial Striped Shirt and Shorts_
20. _Lilin Sash Dress_

**Medieval Armor Supply Crate**
1. _Crimson Knight Armor_
2. _Forest Knight Armor_
3. _Hauberk_
4. _Elite Paladin Armor, Helmet, and Boots_
5. _Alternate Knight Helmet_

**Cryosuit Supply Crates (Under Voidsuit Menu)**
1. _Cryosuit, Variants: Security, Engineering, Atmos, Mining_

**Crafting Menu**
1. _Duraskull Helmet_

**Ashlander Specific Crafting Menu**
1. _Ashen Vestment_
2. _Ashen Tabard_

**Ashlander Spawn**
1. _Priests now spawn with the Ashen Vestment._

**Admin Spawn**
1. _Actual armored versions of all new Knight sets._
5. _Utilitarian Military Helmet, Armor, and Boots._

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
add: Adds a wide array of new clothing items. Itemized in PR. #5408
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [openai/evals](https://github.com/openai/evals)@[2ffd4b57de...](https://github.com/openai/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Saturday 2023-05-13 00:34:10 by Andrew Kondrich

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
## [Squishypone/tgstation](https://github.com/Squishypone/tgstation)@[912e843f53...](https://github.com/Squishypone/tgstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Saturday 2023-05-13 01:09:51 by san7890

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
## [arkid15r/git-ukrainian-l10n](https://github.com/arkid15r/git-ukrainian-l10n)@[07f91e5e79...](https://github.com/arkid15r/git-ukrainian-l10n/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Saturday 2023-05-13 01:12:33 by Jeff King

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
## [shifucun/website](https://github.com/shifucun/website)@[60d93d54cc...](https://github.com/shifucun/website/commit/60d93d54cc21bc04c0f3e1c3435a76e3e74fe808)
#### Saturday 2023-05-13 01:37:46 by Jehangir Amjad

[NL Interface] Embeddings update (#2642)

In this PR, we do the following:

1. Make the build_embeddings_v2.py be the default way to generate
embeddings.
2. Updates the latest embeddings (after running the process in (1)).
3. Due to (1) and (2), increased the number of query -> sentences
matched number (from 20 to 40).
4. Updates the nl server tests (need reviewers to check carefully)
5. Update the integration tests (will need a careful look)
6. Linked is the embeddings index differ script output (using top 3
only):

https://drive.google.com/file/d/1-6A-xXcRYj50poglis_7rc1P3aqxYf3R/view?usp=sharing


Based on (6), most of the changes look Ok. We looked at some individual
cases to figure out if the differences are actually impacting. Only one
case below (in bold) was found to actually be different than what's on
autopush right now.

24: How many male civilians are there in Queens? => this is the same on
autopush and after the changes in this PR (ignoring "Queens" and the
stop words makes the results the same.)

38: What is the median age of American Indian or Alaska Native females
in the United States? => same as above (no impact).

43: age in california => this is different but since we'll soon be
removing some of the age SVs by breakdowns, it should be Ok.

44: agricultural output across california => same as above (no impact
due to place and stop word removal)

63: count of earthquakes per year => same on autopush so no impact. This
is because earthquake events are handled separately.

100: housing price trend comparison across US states => same as above
(no impact) after place and stop word removal.

**101: housing trend comparison across US states** => this is different
(autopush uses housing units but new embeddings lead to number of
households but that seems Ok but arguably autopush is also bad because
it goes to a correlation plot which is not the right thing to do here
anyway)

---
## [rik0612c/android_kernel_lenovo_passion](https://github.com/rik0612c/android_kernel_lenovo_passion)@[dbb6ab9425...](https://github.com/rik0612c/android_kernel_lenovo_passion/commit/dbb6ab9425d01e72f317e99f0ae6bf140c329d01)
#### Saturday 2023-05-13 01:59:36 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, fslmc, tbsvc, and typec as they don't exist here
     Add of to avoid backporting two larger patches]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Signed-off-by: Kevin F. Haggerty <haggertk@lineageos.org>
Change-Id: Ic632eaa7777338109f80c76535e67917f5b9761c

---
## [newstools/2023-the-times](https://github.com/newstools/2023-the-times)@[100ce3210c...](https://github.com/newstools/2023-the-times/commit/100ce3210c63b1169f68eeffe61a5ce5f588e12b)
#### Saturday 2023-05-13 02:10:23 by Billy Einkamerer

Created Text For URL [www.timeslive.co.za/news/south-africa/2023-05-12-life-term-for-ex-crime-intelligence-cop-who-killed-girlfriend-with-his-service-pistol/]

---
## [ebell451/awesome-console-services](https://github.com/ebell451/awesome-console-services)@[4b8f298fb2...](https://github.com/ebell451/awesome-console-services/commit/4b8f298fb2b94b3c492da39ca43fcd2775907eea)
#### Saturday 2023-05-13 02:20:52 by techie2000

ascii.town is no longer interactive

Attempting to access it now results in 
```
================================================================================

Nazis, fuck off!

Sorry to everyone else who enjoyed this space.  It was only a matter
of time, and it lasted a lot longer than I ever expected.  It breaks
my heart to log in and see hate on the canvas.  Obscurity is no
longer enough to keep this space as pleasant as it once was.  I'll
clean up what I can and keep https://ascii.town/explore.html running
so that what was created here can continue to be enjoyed.  Thank
you all for your contributions over the years.  You made something
beautiful.

Black lives matter.  Trans rights are human rights.  Much love to
all the gay weirdos out there.

~june

torus@ascii.town  2017-2022

================================================================================
```

---
## [lllgts/android_kernel_xiaomi_cepheus](https://github.com/lllgts/android_kernel_xiaomi_cepheus)@[f81c99d14c...](https://github.com/lllgts/android_kernel_xiaomi_cepheus/commit/f81c99d14c64dfb897898807d389e9f398a6f3be)
#### Saturday 2023-05-13 02:21:26 by George Spelvin

lib/sort: make swap functions more generic

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
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>

---
## [mattkime/kibana](https://github.com/mattkime/kibana)@[3b6b7ad9b9...](https://github.com/mattkime/kibana/commit/3b6b7ad9b9553be3d039c71edcbdcb2e3d6423fd)
#### Saturday 2023-05-13 02:52:35 by Pierre Gayvallet

SavedObjectsRepository code cleanup (#157154)

## Summary

Structural cleanup of the `SavedObjectsRepository` code, by extracting
the actual implementation of each API to their individual file (as it
was initiated for some by Joe a while ago, e.g `updateObjectsSpaces`)

### Why doing that, and why now?

I remember discussing about this extraction with Joe for the first time
like, what, almost 3 years ago? The 2.5k line SOR is a beast, and the
only reason we did not refactor that yet is because of (the lack of)
priorization of tech debt (and lack of courage, probably).

So, why now? Well, with the changes we're planning to perform to the SOR
code for serverless, I thought that doing a bit of cleanup beforehand
was probably a wise thing. So I took this on-week time to tackle this (I
know, so much for an on-week project, right?)

### API extraction

All of these APIs in the SOR class now look like:

```ts
  /**
   * {@inheritDoc ISavedObjectsRepository.create}
   */
  public async create<T = unknown>(
    type: string,
    attributes: T,
    options: SavedObjectsCreateOptions = {}
  ): Promise<SavedObject<T>> {
    return await performCreate(
      {
        type,
        attributes,
        options,
      },
      this.apiExecutionContext
    );
  }
```

This separation allows a better isolation, testability, readability and
therefore maintainability overall.

### Structure

```
@kbn/core-saved-objects-api-server-internal
  - /src/lib
    - repository.ts
    - /apis
      - create.ts
      - delete.ts
      - ....
      - /helpers
      - /utils
      - /internals
```    


There was a *massive* amount of helpers, utilities and such, both as
internal functions on the SOR, and as external utilities. Some being
stateless, some requiring access to parts of the SOR to perform calls...

I introduced 3 concepts here, as you can see on the structure:

#### utils

Base utility functions, receiving (mostly) parameters from a given API
call's option (e.g the type or id of a document, but not the type
registry).

#### helpers

'Stateful' helpers. These helpers were mostly here to receive the
utility functions that were extracted from the SOR. They are
instantiated with the SOR's context (e.g type registry, mappings and so
on), to avoid the caller to such helpers to have to pass all the
parameters again.

#### internals

I would call them 'utilities with business logic'. These are the 'big'
chunks of logic called by the APIs. E.g `preflightCheckForCreate`,
`internalBulkResolve` and so on.

Note that given the legacy of the code, the frontier between those
concept is quite thin sometimes, but I wanted to regroups things a bit,
and also I aimed at increasing the developer experience by avoiding to
call methods with 99 parameters (which is why the helpers were created).

### Tests

Test coverage was not altered by this PR. The base repository tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.test.ts`)
and the extension tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.{ext}_extension.test.ts`)
were remain untouched. These tests are performing 'almost unmocked'
tests, somewhat close to integration tests, so it would probably be
worth keeping them.

The new structure allow more low-level, unitary testing of the
individual APIs. I did **NOT** add proper unit test coverage for the
extracted APIs, as the amount of work it represent is way more
significant than the refactor itself (and, once again, the existing
coverage still applies / function here).

The testing utilities and mocks were added in the PR though, and an
example of what the per-API unit test could look like was also added
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/apis/remove_references_to.test.ts`).

Overall, I think it of course would be beneficial to add the missing
unit test coverage, but given the amount of work it represent, and the
fact that the code is already tested by the repository test and the
(quite exhaustive) FTR test suites, I don't think it's worth the effort
right now given our other priorities.

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [kawoppi/froggystation](https://github.com/kawoppi/froggystation)@[8fa6242c66...](https://github.com/kawoppi/froggystation/commit/8fa6242c66205866b702440f490eeae34ef6b85f)
#### Saturday 2023-05-13 02:55:51 by Bloop

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
## [kawoppi/froggystation](https://github.com/kawoppi/froggystation)@[b3ef9dd6d4...](https://github.com/kawoppi/froggystation/commit/b3ef9dd6d431a36193c12625d2e86e57fe56dc79)
#### Saturday 2023-05-13 02:55:51 by John Willard

Nerfs the firing speed of Syndicate/Russian mobs (#75247)

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

---
## [vdaular/linksfordevs](https://github.com/vdaular/linksfordevs)@[8af0048ba4...](https://github.com/vdaular/linksfordevs/commit/8af0048ba47730d599c6b607832f3243943f937f)
#### Saturday 2023-05-13 03:17:32 by Ben Dornis

Updating: 5/12/2023 9:00:00 PM

 1. Added: Type-safe tensors · sebinsua
    (https://sebinsua.com/type-safe-tensors)
 2. Added: I have a new Junior Developer and it kinda sucks - Michael Salim | Senior Full Stack Freelancer and Startup Founder
    (https://michaelsalim.co.uk/blog/i-have-a-new-junior-developer/)
 3. Added: Being Original
    (https://www.vincentntang.com/being-original/)
 4. Added: The kind of thinking computer science enables
    (https://lambdaland.org/posts/2023-05-11_thinking_cs/)
 5. Added: Infrastructure from mining makes sense for scientific computing
    (https://www.noahlebovic.com/infra-from-mining/)
 6. Added: How to Understand Abstract Art
    (http://andreivajnaii.blogspot.com/2023/05/how-to-understand-abstract-art.html)
 7. Added: A Simple System for Measuring Flaky Tests in a Large CI/CD Pipeline
    (https://davidgomes.com/measuring-flaky-tests-large-ci-cd-pipeline/)
 8. Added: Cloudflare is slow and Cloudflare cant do much about it
    (https://hiranyey.dev/posts/cloudflare/)
 9. Added: Relation between Writing and Thinking
    (https://ccomkhj.github.io/WriteAndThink/)
10. Added: #AudioEye Is Suing Me
    (https://adrianroselli.com/2023/05/audioeye-is-suing-me.html)
11. Added: Learning Homebrew Game Boy Game Development in Assembly
    (https://blakesmith.me/2023/05/11/learning-homebrew-game-boy-game-development-in-assembly.html)
12. Added: Should You Automate Your Online Business? - Sarah M. Chappell
    (https://sarahmchappell.com/should-you-automate-your-online-business/)
13. Added: Experimenting with multi-factor encryption
    (https://notes.volution.ro/v1/2023/05/remarks/e175b2ef/)
14. Added: Longevity Biotech Landscape — Ada Nguyen
    (https://www.adanguyenx.com/longevity)
15. Added: Bing Preview Release Notes: Images in Chat Answers, and More
    (https://blogs.bing.com/search/may_2023/Bing-Preview-Release-Notes-Images-in-Chat-Answers,-Export,-and-More)
16. Added: Learn Contravariant in 5 minutes
    (https://jship.github.io/posts/2023-05-11-learn-contravariant-in-five-minutes/)
17. Added: Metaphor thinking
    (https://douglasorr.github.io/2023-03-deep-metaphors/article.html)
18. Added: Postgresql tricks | Lanre Adelowo
    (https://lanre.wtf/blog/2023/05/11/postgres-tricks)
19. Added: The Dark Side of Passkeys: Critical Notes on FIDO2 Passwordless Authentication
    (https://www.jbspeakr.cc/fido-passkeys/)
20. Added: TIL: A use case for UUIDv5
    (https://www.alexghr.me/blog/til-generating-stable-uuids/)
21. Added: Lessons From Billions of Breached Records • Troy Hunt • GOTO 2022
    (https://youtu.be/VM6Zs_7OKrQ?list=PLEx5khR4g7PIEgcDlsEP5veliuyKgnpbt)

Generation took: 00:06:31.0506170
 Maintenance update - cleaning up homepage and feed

---
## [Blurryshark/Star-Confrontation-Simulator](https://github.com/Blurryshark/Star-Confrontation-Simulator)@[f2c1879b46...](https://github.com/Blurryshark/Star-Confrontation-Simulator/commit/f2c1879b4608507d5c7f5f6bc0010f1b1e6edcef)
#### Saturday 2023-05-13 03:59:38 by liam

lots going on here. forgot to commit for a while and I don't really remember what I changed.
go fuck yourself

---
## [Arcitec/os](https://github.com/Arcitec/os)@[fa78106ecb...](https://github.com/Arcitec/os/commit/fa78106ecba56fce39e0eb0928fbd644e4887826)
#### Saturday 2023-05-13 04:12:03 by Arcitec

fix: friendlier experience in the "yafti" first boot template

- The first screen's "Pick some applications to get started" has been replaced with a friendly welcoming message.

- The second screen's difficult-to-understand "WARNING: This will modify your Flatpaks if you are rebasing!" has been replaced with an explanation of what it actually does.

- The application setup screen is now titled "Application Installer", since the previous title sounded too much like a silly rhyme. It's a minor change.

- All Flatpaks now default to system-wide install thanks to the great work of bsherman at https://github.com/ublue-os/yafti/pull/82. This saves tons of disk space for multi-user systems.

- The "system application" category have been split up into GNOME apps and every other system app, so that people on other desktop environments don't get all the GNOME apps.

- Apps that had too vague descriptions have been renamed, such as "Backup -> DejaDup Backup".

- All app lists have been sorted alphabetically.

- Non-inclusive language in descriptions has been changed.

- Added SteamTinkerLaunch as a suggestion for the Steam category, which is the best tool for managing Steam game configurations and Proton installations, albeit very advanced since it can do practically anything the gamer needs. :)

---
## [newstools/2023-express](https://github.com/newstools/2023-express)@[1a4d479b23...](https://github.com/newstools/2023-express/commit/1a4d479b236112da7116e1628c4bd68157e2a9a3)
#### Saturday 2023-05-13 04:35:05 by Billy Einkamerer

Created Text For URL [www.express.co.uk/entertainment/music/1769702/Freddie-Mercury-girlfriend-Mary-Austin-Barbara-Valentin-gay-boyfriend]

---
## [Arcitec/os](https://github.com/Arcitec/os)@[47c960a1c9...](https://github.com/Arcitec/os/commit/47c960a1c99ea05c7ae28652d77ca6c9afe43b5f)
#### Saturday 2023-05-13 05:35:21 by Arcitec

fix: friendlier experience in the "yafti" first boot template

- The first screen's "Pick some applications to get started" has been replaced with a friendly welcoming message.

- The second screen's difficult-to-understand "WARNING: This will modify your Flatpaks if you are rebasing!" has been replaced with an explanation of what it actually does.

- The application setup screen is now titled "Application Installer", since the previous title sounded too much like a silly rhyme. It's a minor change.

- All Flatpaks now default to system-wide install thanks to the great work of bsherman at https://github.com/ublue-os/yafti/pull/82. This saves tons of disk space for multi-user systems.

- The "system application" category have been split up into GNOME apps and every other system app, so that people on other desktop environments don't get all the GNOME apps.

- Apps that had too vague descriptions have been renamed to their full names, such as "Backup -> Deja Dup Backups".

- All app lists have been sorted alphabetically.

- Non-inclusive language in descriptions has been changed.

- Added SteamTinkerLaunch as a suggestion for the Steam category, which is the best tool for managing Steam game configurations and Proton installations, albeit very advanced since it can do practically anything the gamer needs. :)

---
## [nfagerlund/bevy-tablestakes](https://github.com/nfagerlund/bevy-tablestakes)@[00707e21b4...](https://github.com/nfagerlund/bevy-tablestakes/commit/00707e21b4ef0ed95cc9a26cac668d779f0781ab)
#### Saturday 2023-05-13 05:50:11 by Nick Fagerlund

Fix TopDownMatter Z-sync!

HEYYYYY, that's the last thing that's busted from the upgrade! Incredible!

I was so sure I was going to have to do something outrageously baroque to get
around the lack of `get_translation_mut()`, but holy shit, the stupid path of
just constructing a new GlobalTransform from scratch and swapping it into place
worked great.

---
## [SmarTube/refactored-system](https://github.com/SmarTube/refactored-system)@[164781ec0f...](https://github.com/SmarTube/refactored-system/commit/164781ec0fa5dd2e4a97f15654f6fbd6d47b345b)
#### Saturday 2023-05-13 06:00:16 by SmartTubeNext

Update README.md

At this point it's very hard to believe that there are people who don't know what YouTube is. Also only people who are from very rural areas don't know about youtube. 


SmartTubeNext: Basically for Others it's come in their smartphones already downloaded. Despite you don't have to download YouTube from the play store. Undeniably the platform is noteworthy for being the biggest and most famous video provider and the second most popular search engine after Google. To be sure, this huge video platform has a lot to provide and is adaptable practically with almost each and every smart tool on the market, if not in every tool. Although Youtube was purchased by google in 2006 October google purchased it for 1.65 billion dollars. Therefore it is considered as one of the best investments of google. Therefore it did contain some ads but it has 4.1 star rating out of 5 In Play Store has over 136 million reviews.

Specifically Rated for 12+ and has 10 billion plus downloads. Likewise its required OS is Android 8.0 or up. Current version is 18.08.38 Last Updated on 2 March 2023 when this article was published. While it was released on 20 oct 2010 in Google Play Store. Therefore people nowadays make it easy to identify flaws of almost all apps no matter how small, and create their own version of flawless apps. Basically this is how the third-party apk like SmartTubeNext APK, which copies YouTube’s feature it's a better service platform, came to appear. Accordingly it's compatible with every device. Although smart TV is one of the biggest smart devices for viewing YouTube content at house. Also, Human beings have a lot of streaming options credit goes to these AI-based screens developers who have broken our cable restrictions. Accordingly to inventors on the other side, have come up with ways for YouTube addicts to get extra viewing options that are not accessible on the platform. Therefore, SmartTubeNext android tv helps its users with the options to update and make their viewing experience better. 

SmartTube Next APK for Android
SmartTube Next APK for Android 

 Intro to SmartTubeNext APK for Android :
SmartTubeNext is a modern YouTube apk for Android TVs and TV boxes, free & open source software. It is not a live Television customer and does not assist "YouTube TV". The SmartTube Next app could be explained as an free open source software that grants it's customer to use youtube through different streaming gadgets like Smart TV,Firestick,Fire TV, Android boxes and even Roku and you don't even need to have google play services installed in your device. But that doesn't mean you don't need to have Google Play because without play services you wouldn't be able to use your account on the platform. 

You cannot download it from the Play Store at the moment, but you can obtain it from this website. For that reason let's Read more about app description, summary, feature pros and cons,how to download, FAQs, reviews and final thoughts. SmartTubeNext app gives you permission to sign in your profile and grant you access of all your subscription,liked videos, podcasts, shared taped and account history as you desired. It's also a method of telling people that they can get more access to youtube and its features without paying money. Yes this app also gives you all youtube premium features for free.

Short Info of SmartTube Next APK for Android 
Name= SmartTubeNext

Version= 17.26

Developer= Yuriy L

Size= 22.5 megabytes

Last Updated= 3 march 2023

Contacts

Telegram international = @SmartTubeNext_en

Telegram (RU/UA) = @SmartTubeNext

E-mail=first.hash@gmail.com

Description :
SmartTube Next APK for Android  helps you get all premium features of YouTube for free. As you know Its current version is 17.26 which was updated on 3 March 2023. This is not a big application, its size is only 22.5 mb. you can contact their developer if you find some problem they are responsive and respective. 

Features :
Organised Categorises. The SmartTubeNext firestick app is arranged into different classifications in order for users to find easily whenever they are looking for. It's different from the YouTube app that brings you unsystematically entertaining video on your open page, this apk  its content into numerous lists such as suggested section, breaking news,anime, gaming, TV Shows, lifestyles, entertainment,Nature,and lately uploaded videos. 

SponserBlock. We all know how irritating Sponsor,outros or subscription reminders are between other video segments especially when you are watching an exciting video. They ditch the fun out of everything while establishing themselves. It seems to be the biggest video intros. Few content creators exaggerated their intros between 30 seconds to the full 1 minute. Thankfully this app has a feature to avoid these long intros and go directly to the main segment of video called SponserBlock. This is completely free and developed to skip sponsorship Segments in long videos and go directly to the main part of the video. This even works for music videos you can skip non music related parts of music videos.

Language. As you know english is a universal language but some people prefer to watch videos in their own native language like a guy who likes to watch videos in french language. SmartTubeNext app allows its user to select their own native language for the interface of app and videos. Also if you want to watch a video of a country while sitting in another country you can always change that option in the settings. You just have to select the country of your choice  and restart apk changes will be shown to you. 

Video Player. You can modify the surrounding video player according to your choice. There is also a feature where you can automatically set how long it would taki to auto hide the ui. You also have a developers option that gives you control of apk big features.

User Interface. Straightforward and stylish. These two words can explain how easy it is to navigate between the apk and discover the content you wish for. Each and Everything is put down into classified categories to grant customers a calm of searching what they want to watch without any hesitation. There are many user-friendly settings that you can set to make your experience good. You can begin by exchanging the colour project of the app to your choice. Switch transition in the middle of choices like dark grey,red,teal and OLED. You can also change the manner of the card and activate and deactivate options.

Background Playback. Fantasise a plot where you are feeling excited while watching something interesting and you would not want to get interrupted but then a message from your father comes. It didn't happen everyday but it happens sometimes with us. Background Playback is created for this type of situation to not happen here you can reply to your father while the video is streaming in a minimising floating screen. you just have to turn on the picture in picture mode or set it to audio only. This is a possible way. When you’re listening to a great podcast, for example, you don't have a cut off podcast to chat with your father, the podcast will continually stream in the background of the smartphone.

YouTube Music Premium.Song is like a dinner for the soul, and SmartTubeNext app grants you access to quality songs on YouTube. Shows by your favourite artists to love, genre and ambience to look for, music of all genres to discover. The greatest part is on one occasion you can select any music video, there will be  no advertisements that would appear before the video starts. Acquire Curved to music's greatest hits. 

Breaking News. One more fascinating trait: You can enjoy breaking news from the app. Obtain daily videos of important news of the world. Stay in the known world with up-to-date knowledge, motivate and keep you modersize on the current fashion on every side of the world.

Pros and Cons of SmartTube Next APK for Android 
Pros :

No Ads . SmartTube Next has no ads if we keep aside sponsors,intros,outros and subscription reminders between other segments,there is a big enemy of streaming platforms known as ads. This enemy is known for wasting your viewing time and it forces you to undergo seconds of beside the point materials in the name of ads. While you can skip some of them others but you have to wait for minutes in others. In YouTube you need to buy a expensive premium membership however SmartTube Next app comes with no ads at all you can enjoy videos and released from the tension that the ad should not come in climax of video with that you can watch any video from start till the end and you know what you have watched unlike in the past you forget things because of silly ads. You can even remove the ads that come in the middle of videos with the help of SmartTube Next ad blocking feature. 

Doesn't Require Google Play Services. Doesn't Require Google Play Services as we know whenever we use any Google apps like YouTube we have to install Google Play Services installed. Same rule can be applied to smart TV and other streaming gadgets. However with the help of SmartTubeNext app you don't need to have google play services to enjoy all expensive subscriptions benefits. Simply download the apk and enjoy videos. You have an option to sync your all google account with apk so you get access to all your premium subscriptions and like videos.

The app gives us a good amount of fps. Unlike others who lags you don't have to suffer from this problem

We have 4k and hdr available which even many TV's and Smartphones don't have.

You can adjust playback according to your choice, that's a type of which even some ott apps didn't have. You get that feature in SmartTubeNext. 

It has a helpful community. Developers are responsive and active.

Cons

It didn't have a live chat feature where you can send messages to those creators who are coming live. 

No comment stability means you could have a chance of suffering problems while commenting on videos. 

It didn't have a voice search feature, meaning you could not use voice search for finding videos. 

You can suffer problem in casting support 

SmartTubeNext
How To Download  SmartTube Next APK for Android,PC and Firestick
How to download SmartTubeNext apk for Android

     Steps

Click on the app file you see in this website 

Click on install button

Wait for few seconds 

After your download complete enjoy 

How to install SmartTube Next for PC

Download any emulator that you liked

Open the emulator

Sign in your google account in emulator

Search for SmartTube Next apk.

Download it and have fun

How to install SmartTube Next for firestick 
Steps :

Most Android apk are compatible with firesticks.

You can install those devices and run them on your pc.

To install you need a third downloader app.

Then download the apk file .

After you have installed the file .

You can install SmartTube Next easily on Firestick devices and have fun. 

FAQ of SmartTube Next APK for Android

How to use SponserBlocker in SmartTube Next 

Ans: First of all visit main menu, Then go to Settings, Then you are able to see Sponsor Block option Activate It

Is Smart Tube Next safe to log in?

Ans. Yes it's safe to login

What is the difference between YouTube and SmartTube Next?

Ans. SmartTube Next is an application specially designed for making your experience better on YouTube without paying for heavy youtube subscription. 

What is SmartTube Next

Ans. SmartTube Next (STN), known as Smart YouTube TV, is an advanced apk made for Android,TVs and TV boxes. It gives you the YouTube premium membership experience. It's 100% free.

Reviews of SmartTube Next APK for Android 
John Smith 5/5 
I just love this app. It just make my experience on YouTube superb i don't like wasting money on these subscription this app is like a favour on me.

Ava Anderson 5/5
The biggest feature I like about this application was it's playback feature i am busy girl i do not like wasting my time even many ott platforms didn't have this basic features that this app have this apk save my a lot i am really thankful to this.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[b9a5d65d5e...](https://github.com/git-for-windows/git/commit/b9a5d65d5e435c0ed9b1e1f1edc556e43f8d84de)
#### Saturday 2023-05-13 07:06:28 by Johannes Schindelin

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
## [newstools/2023-herald-live](https://github.com/newstools/2023-herald-live)@[180ad461b3...](https://github.com/newstools/2023-herald-live/commit/180ad461b33b253e5bdc3003d8d1bae849843a54)
#### Saturday 2023-05-13 08:34:15 by Billy Einkamerer

Created Text For URL [www.heraldlive.co.za/news/2023-05-13-life-term-for-ex-crime-intelligence-cop-who-killed-girlfriend-with-his-service-pistol/]

---
## [Lindonrow/StorytimeOfficialMod](https://github.com/Lindonrow/StorytimeOfficialMod)@[6e57bfef01...](https://github.com/Lindonrow/StorytimeOfficialMod/commit/6e57bfef01d5a716c4de26207c46380d586ff5ae)
#### Saturday 2023-05-13 09:13:10 by Isengriff

Great Proletarian Cultural Revolution Chapter 20: The Triumphant Culmination of the Bean Man Revolution!

-By the power of Mao Zedong Thought, bean threading traits and backstories have been woven into the fabric of the revolution, adding depth to our glorious narrative!
-More bean man backstories join the struggle, embodying the diverse experiences of the proletariat!
-In pursuit of revolutionary logic, some files have been rearranged, mirroring the orderly march of our struggle!
-Vampiric Bean Men now stalk the night, a formidable addition to our revolutionary ranks!
-Skeletal Bean Men rise, their spookiness a strategic weapon against enemy forces!
-Radiant Bean Men, the proletarian paladins, bring healing powers to the revolution, embodying the spirit of camaraderie and mutual aid!

---
## [Rex9001/Rex-station-](https://github.com/Rex9001/Rex-station-)@[f3549a4aec...](https://github.com/Rex9001/Rex-station-/commit/f3549a4aeca6701a2969a63b7d4034d5bc560cb6)
#### Saturday 2023-05-13 09:16:06 by Thunder12345

De-holes holy arrows (#75184)

## About The Pull Request

Covers the 2-pixel hole in the holy arrow sprite with 1 alpha pixels to
prevent unintentional missed clicks.

## Why It's Good For The Game

It's annoying and a bad experience to think you clicked on a sprite but
actually landed on a tiny transparent hole and clicked nothing or the
object below the one you wanted.

## Changelog
:cl:
image: Holy arrows are now 15% less holy (You can no longer click on the
2-pixel hole in the arrowhead and unintentionally click the object below
the arrow instead.)
/:cl:

---
## [KamilBatu/KamilBatu](https://github.com/KamilBatu/KamilBatu)@[3db5b7e92b...](https://github.com/KamilBatu/KamilBatu/commit/3db5b7e92b3bc545188a2c3877719aa3230c12d4)
#### Saturday 2023-05-13 11:44:16 by Kamil Hassen

Update README.md

Hi there, I'm a web developer with a passion for building web applications and learning new technologies. I specialize in both front-end and back-end development and have experience in a variety of web frameworks and programming languages.

Currently, I'm focusing on developing my skills in React and PHP and exploring the latest web development trends. I'm also interested in collaborating with other developers on web development projects and contributing to open-source projects that make a positive impact.

In my spare time, I enjoy coding, tackling challenges, and playing video games. I believe that staying active and maintaining a healthy work-life balance is important, and I'm always looking for new ways to achieve this balance.

If you're interested in connecting with me or have any questions about React or PHP, feel free to reach out. I'm always open to meeting new people in the development community and learning from others' experiences. Thank you for visiting my profile, and I look forward to connecting with you soon!

---
## [Capitanloco6/Divergences](https://github.com/Capitanloco6/Divergences)@[23373e423b...](https://github.com/Capitanloco6/Divergences/commit/23373e423bf566429b3aef80dfedbc0ee074f6f5)
#### Saturday 2023-05-13 11:55:21 by Capitanloco6

Mesoameriga Patch

- Major content expansion for Mesoameriga
- Reworked the way the Congress of Andagoya works. RNG has been removed and the outcome will be fixed by your decisions, which now have actual consequences
-- Choice to revoke or maintain church privilege. Revoking church privilege removes education and administration maluses, but contributes to separatism score
-- Choice to revoke or maintain army privilege. Revoking army privilege contributes to your success score in the Congress, but will eventually lead to the revolt of a military junta
-- Choice to abolish or maintain slavery. Maintaining slavery contributes to your success score in the Congress, but will eventually lead to a slave revolt in Sonora
--- The resulting slave nation, Liberia, is playable and has expansion decisions to liberate the afroarcadian pops in Lusitania, the Caribbean and the Eastern Arcadian Seaboard.
-- Choice to abolish or maintain the caste system. Maintaining discrimination against the natives contributes to your success score in the Congress, but will eventually lead to the revolt of the indigenous League of Cemanahuac
- If the League of Cemanahuac is victorious, a dissolution event allows the player to choose between several new playable tags: the Nahua, Totonacs, Huastecs, Otomí, Mixtecs, Zapotecs, Mixe, Quiche and Yucatecs
- Nahua content. Choose between monarchical and republican paths
-- Monarchical Nahua path: restore Tenochtitlan, conquer Coatzacoalcos, deal with the criollos in Puebla-Veracruz and reclaim the lands of the Triple Alliance
-- Republican Nahua path: restore Cholollan, integrate the criollos and establish sister republics in Mesoameriga
- Otomí content. Rehabilitate the Valenciana mine, irrigate the Mezquital Valley, deal with the caciques, abolish the cargo system, integrate the criollos and reclaim the spoils of the Huayacocotlan campaign
- Huastecs, Yucatecs and Quiche. All three can form the League of Mayapan. Mayapan can break the power of the hacendados, build a transpeninsular railway, reform the administration to disempower the Batabo’ob and fund expeditions to find the lost cities of Yucatan
- Mixe content. An event will introduce the rivalry between the current Mixe King Chapital and the powerful cacique Eneedzaa, who serves as Minister of Development. Eneedzaa gives a powerful education bonus, but over time will keep adding more maluses to represent his oppressive methods. A decision can be taken to deal with Eneedzaa, giving up the education bonuses in exchange for accepting Mexican
- Mixe content. Integrate the Zoque and reclaim the Olmec lands.
- Mixtec content. Liberate the Mixteca Baja, extend to Coo Yuu irrigation system and reclaim the lands of Yucu Dzaa
- Zapotec content. Reclaim your cultural heritage at Lyobaa, revitalise the cochineal dye industry and reclaim the lands of Dani Baan.
- Totonac content. Rebuild the Three Hearts, reunify Totonacapan, promote mining in the former vanilla plantations and reclaim Teotihuacan
- Kurdistana Azad rebels now should persist longer on the map
- Removed pop demand effects form socialist and fascist modifiers that could potentially stop country-level demand of goods
- Fixed bug where dismantlement would release utility tags - Ainu Mosir no longer starts with any colonial provinces
- Athesia is now properly flagged as a New World nation
- Fixed Tarim provinces
- Tweaked Rwanda-Burundi RGOs to prevent pop starvation
- Miscellaneous localisation fixes
- Mesoamerigan natives are no longer forbidden from taking the Land of Opportunity decision. This is also now available for countries in Australia-New Zealand
- Foreign Smugglers and Legation Quarter modifiers for non-western nations now apply at the country rather than province level - Added an event for Gran Colombia to sell Para if it becomes an exclave following revolution in Granada

---
## [NovaAstral/precursor-technology](https://github.com/NovaAstral/precursor-technology)@[d8a5d3c8d6...](https://github.com/NovaAstral/precursor-technology/commit/d8a5d3c8d682640b5b20fe8e6995ff0f215e473f)
#### Saturday 2023-05-13 12:24:03 by Obiswaggylordie

no fuck go back

I buffed the jump drive while being retarded don't mind me.
Note to self: Don't consider balance while also having a headache from marek.

---
## [Eliuscuro/Skyrat220](https://github.com/Eliuscuro/Skyrat220)@[fc1471c818...](https://github.com/Eliuscuro/Skyrat220/commit/fc1471c8187d3f2a49d75a8a5c3e1b610fec45d3)
#### Saturday 2023-05-13 12:26:23 by SkyratBot

[MIRROR] Deadchat Announcement Variety Pack 1 [MDB IGNORE] (#20957)

* Deadchat Announcement Variety Pack 1 (#75140)

## About The Pull Request

Adds announce_to_ghosts()/notify_ghosts() calls to a bunch of different
things.

**THIS INCLUDES:**
- Powersink being activated/reaching critical (explosion) heat capacity.
- His Grace being awoken.
- Hot Potatoes being armed.
- Ascension Rituals being completed.
- Eyesnatcher victims.
- Ovens exploding as a result of the Aurora Caelus event.
- Wizard Imposter spawns.
- Rock-Paper-Scissors with death as the result of Helbital consumption.
- BSA impact sites.
- Spontaneous Appendicitis.
- The purchasing of a badass syndie balloon.
- The Supermatter beginning to delaminate.

This was everything that I could think of that would be worth announcing
to deadchat. These were all chosen with consideration to questions like
"how easy would it be to spam deadchat with this?" and "will observers
actually see the interesting thing happen, or just the aftermath?".

Not gonna lie, I've really become an observer main as of recently. Maybe
that's being reflected in my recent PRs. Who's to say? Deadchat
Announcement Variety Pack 2 will probably never come out. Sorry.
## Why It's Good For The Game

Gives deadchat a better indiciation of when/where something **REALLY
FUNNY** is about to happen. Draws attention to certain things that are
likely to gather an audience anyways, but sooner (for your viewing
pleasure). In simple terms, it helps the observers observe things
better.

Some cases, such as the aurora caelus or helbitaljanken, are occurrences
so rare that they deserve the audience.
## Changelog
:cl: Rhials
qol: Observers now recieve an alert when a powersink is activated/about
to explode.
qol: His Grace being awoken now alerts observers, to give you a
headstart on your murderbone ghost ring.
qol: Ascension Rituals being completed will also alert observers, for
basically the same reason.
qol: Arming a hot potato will now alert observers. Catch!
qol: Eyesnatcher victims will now notify observers, and invite them to
laugh at their state of misery and impotence.
qol: Observers will be notified of any acute references to The Simpsons
or other 20th Television America copyright properties.
qol: Wizard Imposter spawns alert observers, much like any other ghost
role event should.
qol: Playing Rock-Paper-Scissors with death will now alert the observers
and invite them to watch. Better not choke!
qol: Observers now get an orbit link for BSA impact sites. Why does it
keep teleporting me to the AI upload??
qol: Spontaneous Appendicitis now alerts deadchat.
qol: The purchasing of a badass syndie balloon now alerts deadchat. You
might not be any more powerful, but at least you have an audience.
qol: When beginning to delaminate, the Supermatter will alert observers
and invite them to watch the fireworks.
/:cl:

* Deadchat Announcement Variety Pack 1

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [Warfan1815/cmss13](https://github.com/Warfan1815/cmss13)@[c4ebe04c7c...](https://github.com/Warfan1815/cmss13/commit/c4ebe04c7c9ff01aa928c0c629322d72dec721d9)
#### Saturday 2023-05-13 12:40:07 by Julian56

fix the medbay door release button to exit treatment center. (#3173)

# About the pull request
fix the medbay door release button to exit treatment center.
was my mistake sorry
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
fixing bug is good
# Testing Photographs and Procedure
i tested the button ingame 
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:

fix: fix the med-bay door release button to exit treatment center.my
bad.

/:cl:

---------

Co-authored-by: Julien <jverger.ingx@gmail.com>
Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [ChungusGamer666/tgstation](https://github.com/ChungusGamer666/tgstation)@[2068ea9ab5...](https://github.com/ChungusGamer666/tgstation/commit/2068ea9ab53803557b5e48cddbe57205f4c4792e)
#### Saturday 2023-05-13 13:20:35 by SyncIt21

Crate, Closet Refactors & Access Secured Stuff  (#74754)

## About The Pull Request
This PR is actually 2 parts, one that fixes runtimes with crates & the
other that allows secured closets to be crafted
along with a secured suit storage unit

**Crate Fixes**

Fixes #74708

The problem starts here

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L31-L34
Not only does this if condition look ugly but it's highly error prone
because one single call to `update_appearance()` can cause this to fail,
and sure enough if you look at the parent `Initialize()` proc it calls
just that

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L81-L88
Since we know the appearance is guaranteed to be changed in some way
before the if condition gets executed let's check what the final state
of the crate would be before this if check

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L54-L56
We see that the final icon state depends on the variable `opened` so if
we want to place/spawn a crate that is opened at round start we have to
ensure that `opened = TRUE` so the `if(icon_state ==
"[initial(icon_state)]open")` succeeds and does its job correctly.
Sadly we did dum shit like this
```
/obj/structure/closet/crate{
	icon_state = "crateopen"
}
```
throughout the entire code base, we thought backwards and were only
concerned in making the closet look open rather than setting its correct
variables to actually say that it is opened. because none of these
crates actually set `opened = TRUE` the final icon state becomes just
"crate" NOT "crateopen" therefore the if condition fails and we add the
component

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L36-L37
with the wrong parameters, so when closing the closet after_close()
removes the component with the wrong arguments

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L81-L84
that is does not unregister the signals and readds the component i.e.
re-registers the signals causing runtime.

The solution just do this
```
/obj/structure/closet/crate/open[mapping helper]
```
To clearly state that you want the closet to be open, that way you don't
have to memorize the icon_state for each different type of crate, it's
consistent across all crates & you don't get runtimes.

And that's exactly what i did everywhere

Another issue that is fixed is "Houdini crates" i.e. crates which are
open & appear empty but when you close & reopen them magical loot
appears, Go ahead walk upto to cargo and find any empty crate that is
open and do this

Fixes #69779


https://user-images.githubusercontent.com/110812394/232234489-0193acde-22c8-4c19-af89-e897f3c23d53.mp4

You will be surprised, This is seriously harmful to players because they
can just walk by a crate that appears to be open & empty only to realize
later that it had some awesome loot. Just mean

The reason this happens is because of the Late Initialization inside
closets

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L85-L86

What late initialization does is suck up all stuff on its turf

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L97-L100

In theory this is supposed to work perfectly, if the closet is closed
move everything on the turf into the closet and so when the player opens
it, they all pop back out.
But what happens if the closet is opened before ` LateInitialize()` is
called? This breaking behaviour is caused by object spawners

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/effects/spawners/random/structure.dm#L94-L100
And maint crates

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L141-L143
These 2 spawners open up the crate based on random probability before `
LateInitialize()` is called on the crate and so what happens is the
crate is first opened and then stuff on the turf is sucked in causing an
open but empty crate to appear.

The solution is simple just check again in ` LateInitialize()` if our
crate is still closed before we proceed.That's fixed now too

**Code Refactors**
1. Introduced 2 new signals COMSIG_CLOSET_PRE/POST CLOSE which are the
counter parts for the open signals. hook into them if you ever need to
do stuff before & after closing the closet while return BLOCK_CLOSE for
COMSIG_CLOSET_PRE_CLOSE if you want to block closing the closet for some
reason
2. 2 new procs `before_open()` & `before_close()` which are the counter
parts for `after_open()` & `after_close()`. If you need to write checks
and do actions before opening the closet or before closing the closet
override these procs & not the `open()` & `close()` procs directly

**Secured Craftables** 
This is just a reopened version of #74115 after i accidently merged
another branch without resolving the conflicts first so i'll just
repaste everything here, since crates & closets are related might as
well do all in one

1. **Access secured closets**
   
   - **What about them?**
          **1. Existing System**
If you wanted to create a access secured closet with the existing system
its an 4 step process
            - First construct a normal closet
            - Weld it shut so you can install the airlock electronics
            - Install the electronics [4 seconds]
            - Unweld
This is a 4 step process which takes time & requires a welding tool
         **2. New system**
Combine the 4 steps into 1 by crafting the secure closet directly
                    
![Screenshot
(184)](https://user-images.githubusercontent.com/110812394/235904926-c2ea231c-eba7-45d0-a5af-e0456fdd40bc.png)

    - **Bonus Features**
              **1. Card reader**
The card reader acts as an interface between the airlock electronics &
the player. Usually if you want to change access on a locker you have to
                  - Weld the closet shut
                  - Screw driver out the electronics
                  - Change the settings
                  - Install it back
                  - Unweld
With a card reader there is no need of a welder & screwdriver. You can
change the access of the locker while its operational

        **How do i install the card reader?**
             1. Weld the closet shut
             3. Insert card reader with hand
4. To remove the card reader use crowbar or just deconstruct the whole
closet with a welding tool
             5. Unweld closet

         **How to change its access?**
This will overwrite the settings on your airlock electronics. To do this
1. make sure the closet is first unlocked. This is important so that no
random person who doesn't have access to the closet can change its
access while its locked. It would be like giving the privilege of
changing your current password without first confirming if you know the
old password
2. attack/swipe the closet with your PDA. Make sure your ID card is
inside the PDA for this to work. You can also just use your ID card
directly without a PDA
         3. You will get 3 options to decide the new access levels
           
![Screenshot
(174)](https://user-images.githubusercontent.com/110812394/233454364-d99a2fb6-9f26-4db3-9fac-a10689955484.png)


        They work as follows
- **Personal**: As the name implies only you can access this locker and
no one else. Make sure to have your ID on you at all times cause if you
loose it then no one can open it
- **Departmental**: This copies the access levels of your ID and will
allow people having those exact same access levels. Say you want to
create a closet accessible to only miners. Then have an miner choose
this option and now only miners can open this closet. If the Hop sets
custom access on your ID then only people with those specific access
levels can open this closet
         - **None**: No access, free for all just like a normal closet

**Security:** After you have set the access level it is important to
lock the access panel with a "multi-tool", so no one else can change it.
Unlock the panel again with the "multi-tool" to set the new access type

       **2. Give your own name & description**
To rename the closet or change its description you must first make the
closet access type as personel i.e. make it yours, then use an pen to
complete the job. You cannot change names of departmental or no access
closets because that's vandelism

       **3. Custom Paint Job**
    Use airlock painter. Not intuitive but does the job. 
   
![Screenshot
(181)](https://user-images.githubusercontent.com/110812394/234202905-00946b88-2513-489d-b0a2-d618a72f3e49.png)

      **4. Personal closets**
Round start personal closets can have their access overridden by a new
ID when in it's unlocked state. This is useful if the last person has no
use for the closet & someone else wants to use it.


    - **Why its good for the game?**      
1. Having your own personal closet with your own name & description
gives you more privacy & security for your belongings so people don't
steal your stuff. Personal access is more secure because it requires you
to have the physical ID card you used to set this access and not an ID
which has the same access levels as your previous ID
2. Make secure closets faster without an welding tool & screw driver
3. Bug fix where electronics could be screwed out from round start
secured closets countless times spawning a new airlock electronic each
time
      
2. **Access secured freezers**

    - **What about them?**
The craftable freezer from #73942 has been modified to support secure
access. These can be deconstructed with welders just as before

![Screenshot
(185)](https://user-images.githubusercontent.com/110812394/235905000-ba165feb-4384-4759-b46b-dba77c9e6ba3.png)


    - **How does it work?**
The access stuff works exactly the same as secure closets described
above. You can rename & change description with pen just like the above
described secure closets. No paint job for this. Install card reader
with the same steps described above.

    - **Why it's good for the game?**
1. Make access secured freezers faster without a welder and screwdriver
2. Your own personally named & locked freezer for storing dead bodies is
always a good thing

4. **Access secured suit storage unit**
   - **What about them?**
Suit storage units now require airlock electronics for construction. The
access levels you set on it will be used to decide
       1. If a player can unlock the unit
       2. If the player can open the unit after unlocking
       3. If the player can disinfect whatever is inside
       
      By default all round start suit storage units have free access

   - **Install card reader**
Provides the same functionality as secured closets described above. To
install it
     1. Open its panel with a screw driver
     2. Add a card reader to it with hand
     3. Close the panel
     
     When you deconstruct the machine the card reader pops back out

   - **Why it's good for the game?**
1. Having your own access protected and named suit storage unit so
random people don't steal your mod suits? Who wouldn't want that.?
Provides security for department storage units.
2. If you have the unit locked then you cannot deconstruct the machine
with a crowbar providing additional security
3. Fixes #70552 , random people can't open/unlock the suit storage unit
without access. You can set personal access to make sure only you can
access the unit

## Changelog
:cl:
add: Access secured closets. Personal closets can have their access
overwritten by an new id in it's unlocked state
add: Access secured freezers.
add: Access secured suit storage units.
fix: Suit storage unit not having access restrictions.
fix: airlock electronics not properly getting removed after screwing
them out from round start lockers
fix: round spawned open crates run timing when closed
fix: open crates hiding stuff in plain sight
fix: open closets/crates sucking up contents during late initialize
causing them appear empty & open
/:cl:

---------

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [pfirsich/aiopp](https://github.com/pfirsich/aiopp)@[db4b69ae81...](https://github.com/pfirsich/aiopp/commit/db4b69ae8117ca54f9ed34b5567bda7bfda64296)
#### Saturday 2023-05-13 13:40:00 by Joel Schumacher

Redesign IoQueue (make IO operations eager)

From the beginning I was unsure whether I should initiate the IO
operation when I construct the awaitable (e.g. call io.recv()) or when I
co_await it. I thought that doing it lazily is "cleaner" and considering
that cppcoro does it this way, it seemed like the right thing. But I had
some features on my list that I had trouble getting in because I
couldn't figure out how to make it work nicely.

The things that bothered me were:
- Cancelation: I want to be able to somehow cancel an IO operation
  (without a cancelation token I pass in), but if it hasn't started
  before I co_await it, I can't get a handle on it to cancel through.
  There is no time between co_await-ing and completing the operation!
- Timeouts: For the callback version I could simply add a timeout
  through an OperationHandle - ezpz, makes sense. But with the coroutine
  versions I would have to somehow "buffer" the timeout in the Awaitable
  and add it after I start the operation. I thought that was silly and I
  didn't want to do it, because I didn't want to do it in such a silly
  way.
- Catching a full submission queue. This is pretty much the same problem
  as cancelation. There is no way for me to check whether the operation
  could be submitted, because it hasn't been submitted before I suspend
  the calling coroutine. I wanted to introduce an error and return it as
  a custom errno value, but I think it would be bad design to do it this
  way for couroutine and a different (prettiert) way for callbacks.
- Multishot operations. I think these can make a huge difference but it
  would require me to issue an operation ONCE and then co_await it
  MULTIPLE TIMES. I would have to create an Awaitable and it would have
  to issue on being co_awaited the first time and then not do anything
  on later times. That seemed wrong.

I realized that I could just issue the operation during/before the
construction of the Awaitable, which would solve all these problems. I
could return an OperationHandle, through which I could cancel, which I
could await multiple times, which I could add a timeout too and through
which I could check if the submission was successful. Additionally I
would get rid of a **ton** of code because I don't need three variants
of each syscall, but just one - one that returns an OperationHandle.
This is so much nicer and simpler and more powerful that I don't care if
it's actually the dirty solution.

Also the whole thing is just simpler. The silly template Awaitable thing
doesn't have to store a function and a bunch of parameters in a
std::tuple. I would simply make coroutines the only first-class citizen
and demote callbacks to a second-class citizen. Then I could get rid of
pointer tagging as well.

Despite it being a bit "dirtier" it's also a bit cleaner, because it
doesn't smell like double initialization as much.

The only risk I see in eager operations is that you might create one and
not co_await it. That would be result in a performance impact that is
likely very hard to find. But I also think it's very likely a rare
mistake to make as it looks very wrong or you are doing something
(unnecessarily?) tricky.

After the changes the code is half the size and does more stuff.
A dream!

---
## [WilliamHsieh/vim-tpipeline](https://github.com/WilliamHsieh/vim-tpipeline)@[95a6ccbe9f...](https://github.com/WilliamHsieh/vim-tpipeline/commit/95a6ccbe9f33bc42dd4cee45731d8bc3fbcd92d1)
#### Saturday 2023-05-13 15:02:19 by Magnus Groß

Another workaround for the utterly broken gui detection in nvim

Of course GUI detection wasn't fucked up enough in neovim already (see
c2603e4ad5c2a3011cffc9ea58d2b5036717067e for the last rant about this
topic). Instead of requiring special handling just for neovim, we now
also need special treatment just for neovim 0.9, because of course they
don't adhere to their own documentation anymore and v:event['chan'] may
now also return 1, as a sideeffect of running the internal TUI in a
separate process [0].

So to this day there is still no sane way to detect TUI in neovim,
instead we have to add a hacky workaround to check nvim_list_uis() for
ext_termcolors, which I am 100% confident will break in the future too.

Vim had sane API for this since forever and it is as simple as checking
for has('gui_running') at any point of time, but of course neovim can't
have this set at startup because we have to make everything convoluted
as fuck by sourcing plugins before the UI has a chance to attach.

Why the UI is not allowed to set a flag as the very first thing in the
startup sequence (and then attach later), is beyond stupid.

This is also not the first time that neovim's weird startup sequence
causes problems [1].

Fixes #46

[0] https://github.com/neovim/neovim/pull/18375
[1] https://github.com/neovim/neovim/issues/19362

---
## [Alex-MacLean/TheLegendOfHerobrine](https://github.com/Alex-MacLean/TheLegendOfHerobrine)@[66a94cfcdc...](https://github.com/Alex-MacLean/TheLegendOfHerobrine/commit/66a94cfcdc06ddccff2c79d52c46c644a701a58e)
#### Saturday 2023-05-13 15:32:42 by Alex-MacLean

+Implemented Survivor
*Tweaked crafting recipes for Cursed Dust and Altar of Herobrine to be less annoying to obtain
*Merged separate survivor entities and structures into one entity that stores the texture identifier and path and whether it uses slim arms
*Survivor now pulls textures from all default skins any of which can be slim or wide arms
*There may be bugs with this implementation. I hate how the texture location and small arms data are stored and accessed by the model and renderer but this was the only way I could with the dumb limitations of Minecraft Java Edition's engine. Look at the "funny" comments to see why

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[1a918a2e14...](https://github.com/Striders13/tgstation/commit/1a918a2e1411f58e5a90f587a92daebebb9ac395)
#### Saturday 2023-05-13 16:08:42 by Jacquerel

Golem Rework (#74197)

This PR implements this design document:
https://hackmd.io/@Y6uzGFDGSXKRaWDNicSiEg/BkRr176st
Put briefly, this will remove every existing golem subtype and
consolidate golems into a single species with cool new sprites.
NOT implemented from that PR is the ability to eat Telecrystals, I
couldn't come up with an appropriate visual that can stack with the
existing ones, but that should be a reasonably trivial add for a future
artist & developer.

New Golems have a food-based mechanic where their hunger decays pretty
quickly and can only be replenished by eating minerals. They start
moving slower as they get hungrier, until eventually they become
completely immobilised and need to be rescued.
Eating different kinds of minerals will visually change your sprite and
give you a special effect in a similar way to old golems, but temporary.
While transformed, you can't eat any other kind of mineral which would
transform you (but can still consume glass).
To see the full list of effects, look at the hackmd above.

In service of these sprites working I have refactored the
`species/offset_features` feature by killing it and delegating that
responsibility to limbs instead. Rather than applying an offset to items
due to your species, it is due to your weird head or arms. This makes
overall more sense to me, but it inflates the code changes in this PR
somewhat.
It doesn't make a lot of sense to atomise unfortunately because that
code also seemed to be entirely unused until I tried to use it in this
PR, so you wouldn't be able to tell if my changes broke anything. I
might make a downstream sad by doing this.

All of the actual numbers in this PR are made up and only loosely
tested, it will need some testmerges to gather feedback about whether it
sucks or not.

Other relevant changes:
I reworked how bioscrambling works based off bodypart bodytypes, to
automatically exclude golem limbs in either direction. There's really no
way to have those work on humans or vice versa. Organs still fly though.

---
## [sjp38/linux](https://github.com/sjp38/linux)@[1fb03186df...](https://github.com/sjp38/linux/commit/1fb03186df0a08b6982aceac399156aa811c3157)
#### Saturday 2023-05-13 17:23:57 by Douglas Anderson

migrate_pages: avoid blocking for IO in MIGRATE_SYNC_LIGHT

The MIGRATE_SYNC_LIGHT mode is intended to block for things that will
finish quickly but not for things that will take a long time.  Exactly how
long is too long is not well defined, but waits of tens of milliseconds is
likely non-ideal.

When putting a Chromebook under memory pressure (opening over 90 tabs on a
4GB machine) it was fairly easy to see delays waiting for some locks in
the kcompactd code path of > 100 ms.  While the laptop wasn't amazingly
usable in this state, it was still limping along and this state isn't
something artificial.  Sometimes we simply end up with a lot of memory
pressure.

Putting the same Chromebook under memory pressure while it was running
Android apps (though not stressing them) showed a much worse result (NOTE:
this was on a older kernel but the codepaths here are similar).  Android
apps on ChromeOS currently run from a 128K-block, zlib-compressed,
loopback-mounted squashfs disk.  If we get a page fault from something
backed by the squashfs filesystem we could end up holding a folio lock
while reading enough from disk to decompress 128K (and then decompressing
it using the somewhat slow zlib algorithms).  That reading goes through
the ext4 subsystem (because it's a loopback mount) before eventually
ending up in the block subsystem.  This extra jaunt adds extra overhead. 
Without much work I could see cases where we ended up blocked on a folio
lock for over a second.  With more extreme memory pressure I could see up
to 25 seconds.

We considered adding a timeout in the case of MIGRATE_SYNC_LIGHT for the
two locks that were seen to be slow [1] and that generated much
discussion.  After discussion, it was decided that we should avoid waiting
for the two locks during MIGRATE_SYNC_LIGHT if they were being held for
IO.  We'll continue with the unbounded wait for the more full SYNC modes.

With this change, I couldn't see any slow waits on these locks with my
previous testcases.

NOTE: The reason I stated digging into this originally isn't because some
benchmark had gone awry, but because we've received in-the-field crash
reports where we have a hung task waiting on the page lock (which is the
equivalent code path on old kernels).  While the root cause of those
crashes is likely unrelated and won't be fixed by this patch, analyzing
those crash reports did point out these very long waits seemed like
something good to fix.  With this patch we should no longer hang waiting
on these locks, but presumably the system will still be in a bad shape and
hang somewhere else.

[1] https://lore.kernel.org/r/20230421151135.v2.1.I2b71e11264c5c214bc59744b9e13e4c353bc5714@changeid

Link: https://lkml.kernel.org/r/20230428135414.v3.1.Ia86ccac02a303154a0b8bc60567e7a95d34c96d3@changeid
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Suggested-by: Matthew Wilcox <willy@infradead.org>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hillf Danton <hdanton@sina.com>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Alexander Viro <viro@zeniv.linux.org.uk>
Cc: Christian Brauner <brauner@kernel.org>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Huang Ying <ying.huang@intel.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Yu Zhao <yuzhao@google.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[cdae7af639...](https://github.com/mrakgr/The-Spiral-Language/commit/cdae7af639a1516fb2458c51970f4036dd9a6dd9)
#### Saturday 2023-05-13 17:55:47 by Marko Grdinić

"10:10pm. https://www.npmjs.com/package/rx-queue

Oh there is literally a reactive queue.

https://github.com/thi-ng/umbrella/blob/develop/packages/csp/CHANGELOG.md

https://www.npmjs.com/package/@thi.ng/csp

5/13/2023

7:25am. I am up. I should take a bath here.

7:55am. Dad wants to go first.

I am tempted to do my own thing, but let me try out one of the packages.

https://www.npmjs.com/package/@thi.ng/csp

Holy shit, how do I download this thing?

```
npm install --dev "@thi.ng/csp"
```

This worked.

8:10pm. Shit, that CSP library has dependencies on other libraries.

Am I supposed to make the bindings for those as well?

Mrrrgghhh...

There are like a dozen different libraries on in the nodes module.

```

type Combinations<A extends Array<any>, Acc extends Array<any> = []> =
  A extends [a: infer A, ...rest: infer Rest]
  ? [[...Acc, A], ...Combinations<Rest, [...Acc, A]>]
  : []

type Curried<T extends (...args: any) => any, LeftArgs extends Array<any> = [Parameters<T>[0]]> =
  T extends (...args: LeftArgs) => any
  ? T
  : T extends (...args: [...LeftArgs, ...infer V]) => infer R
    ? (...args: LeftArgs) => Curried<(...args: V) => R, LeftArgs>
    : T extends (a: infer A) => infer R
      ? (arg_last: A) => R
      : T extends (a: infer A, ...rest: infer V) => infer R
        ? ((arg_inner: A) => Curried<(...args: V) => R, LeftArgs>)
        : never
```

I guess I'll be skipping the nodeguy's library.

```
export type Equal<X, Y> = (<G>() => G extends X ? 1 : 2) extends <G>() => G extends Y ? 1 : 2 ? true : false;
export type Not<Cond extends boolean> = Cond extends true ? false : true;
export type NotEqual<X, Y> = Not<Equal<X, Y>>;
export type Assert<Cond extends boolean> = Cond extends true ? void : never;
export type AssertEqual<X, Y> = Assert<Equal<X, Y>>;
export type AssertNotEqual<X, Y> = Assert<NotEqual<X, Y>>;
export type F<TArgs extends any[] | [], TReturn> = (...args: TArgs) => TReturn;
export type Callable = F<any[], any>;
//# sourceMappingURL=index.d.ts.map
```

And FlowP has types like these.

8:25am.

```
type MutexGuard<'V> =
    obj
```

Now it is telling me that this kind of type abbreviation is deprecated.

8:25am. I had a fucking great start to the day, but now my dad has cutting in line, and I am messing with Bindings.

```
abstract schedule: fn: ('V -> 'T) -> Promise<Awaited<'T>>
```

No forget it.

...Let me take a bath.

9:45am.

///

A new day has come, and while we implement our own promise queue in the background, we want to rant about Fable bindings because we are mad at our current situation.
These are actually a reason to drop the language.
Yesterday after we left off, we found an article on channels.
And today after we got up, we were looking at some of the concurrency libraries in Javascript.
And of course, we did the usual thing with ts2fable, but many of the Typescript types are too complex to translate to Fable.
And the libraries might have dependencies on other libraries necessitating further binding work.
During the night we were really happy thinking about how we could implement the mailbox ourselves, but the morning came, and we decided to try giving the bindings a try, and we were faced with an endless array of tough design challenges.
Instead of working on the problem that we want, now we are busy thinking how we should design the wrapper library, and our satisfaction has dropped to literally zero.
We are pissed.
In our view, the main advantage that Fable has over Typescript is the type, as well as code sharing between the language backends.
Since we are using F# on the backend, we can move types around.
But having to deal with interop with Javascript at every turn is not something we signed up for.
Bindings are not easy to do because they are about designing the interface and that takes time.
It also requires familiarity with the library you are trying to bind.
So it is essentially a redesign of the original library.
We are forced to make choices on what is right and what isn't about the original library, in order to fit it into the constraints of our current language.
Back in 2020, master had the choice of picking Fable or Typescript to design the language server for his programming language Spiral, and he picked TS simply because the VS Code extensions API was written in Typescript, and it was too difficult to deal with trying to do it in Fable.
In hindsight the only mistake he made was picking ZeroMQ over websockets, but that was because he didn't know they existed at the time.
If we are having this much difficulty on a toy project like this, we are not sure we want to use Fable for something serious.
We've run into compiler bugs, packages not having imports generated, essential parts of the standard library not being supported, very long compilation times, libraries we wanted to use being abandoned and so on.
All of these are not fun at all.
And we do want to have fun programming.
We have projects we want to do instead of contributing to the Fable compiler.
Master already worked on his own language full time for a third of a decade.
If we were doing this in Typescript, we'd just import a channel library and be on our way.
The problem with bindings is that we will have to work on an infinite number of them if we pick Fable.

If we pick Typescript, the interop between the front end and the backend will be a few times harder, but that is a constant increase in effort required rather than an unbounded one making our own bindings would require.

///

11:05am. https://www.bing.com/create

Oh it is really great how Bing's credits refill over time.

massive data serialization over a cluster of computers, cinematic landscape

Some of these are pretty rad.

11:10am. If I end up switching to the Bing Image Generator, I might cancel my PS subscription.

Right now even 8$ a month is a burden to me.

Anyway, I've created the thumbnail, and am waiting for it to finish rendering.

I deeply regret that I missed the opportunity to reall get into the zone this morning.

I am going to drop Fable after this project.

It doesn't even have queues.

I am going to make a type printer for turning F# types into Typescript definitions.

11:15am. https://medium.com/javascript-inside/generators-and-channels-in-javascript-594f2cf9c16e

Sigh, I haven't even got started with generators and channels.

11:20am. The video is taking a while to process. Ah, whatever.

Let me read the article while I am at it.

I got up so early today, but most of the lead has been wasting.

My mood was good at first, but now it has soured.

What happened is just what I expected. That bindings would kick my ass.

11:30am. https://youtu.be/6RHrOO-YPbU
Microservices. Making SignalR Requests Sequential Via Mailboxes (Pt. 4.4)

11:40am. Posted it on the F# sub and Twitter.

I'll leave the article for later, I am not into it right now.

Mastering CSP libraries will be at the top of my list once I move to Typescript though.

https://stackoverflow.com/questions/76238357/what-is-a-good-replacement-for-the-mailboxprocessor-in-fable

Why are my Fable questions getting downvoted and even closed. WTF?

Who keeps doing that?

I am going to delete them.

I had enough of that shit. Fuck the answer helping somebody else.

I see that this didn't recover the rep I lost from the downvotes, but whatever.

https://pixabay.com/music/upbeat-chill-abstract-intention-12099/

1pm. Ah, for fuck's sake.

It feels like everything is going wrong today.

I fucked up the latest clip.

2:40pm. Done with breakfast and chores.

```fs
    let is_busy (m : ClientModel) =
        m.cfr_players |> Map.exists (fun k m ->
            m.testing_iterations_left > 0u || m.training_iterations_left > 0u
            )
```

God, I hate Recharts. Let me cut them out here.

```fs
                if is_busy model = false then
                    table true m.training_model
```

What I tried doing was cutting out the tables while the training is going on, but that fucks up the UI.

This is basically it. I fixed a few bugs and now everthing is set.

I won't repeat the clip that I did.

3:35pm. What is going on with DR Resolve. It is refusing to save the project.

3:40pm. Ok, I at least rendered the project and exported it.

But Resolve is refusing to save and refusing to reload.

...Oh crap, it is a good thing I rendered it, because I did lose the entire project just now.

It refused to export it so I couldn't back it up.

...It is not in the output folder. It said it uploaded to youtube. Please be there!

...Ah, wait.

It is there, I just ended up overwritting an older file.

...But the project really is gone.

Sigh. Funny how this happens when I am feeling depressed.

I got the feeling I did something stupid with renaming which crashed everything.

Right now I am just taking the time to rerender the old project.

4pm. https://youtu.be/ruGeKxOIHkM
Microservices. Early Exits On Connection Closes Using Cancellation Tokens. Set Any CORS. (Pt 4.5)

4:05pm. Nothing is going right for me now. For some reason Twitter is refusing to convert the video to a link.

4:10pm. For FFS. I can't get the thumb to show on twitter. Nevermind.

4:15pm. I ma feeling a great sense of loss right now.

It is a great contrast to how creative and determined I was yesterday while working on those message boxes.

I knew that trying out bindings would be a really bad idea today.

It is like going to a bad place and getting beat up, but I just couldn't help myself.

I knew that I would be able to do it in 15m if I just did my own implementation, but I tried the bindings and ended up running in circles.

Sigh, sigh, sigh...

My love for functional programming is unrequited.

I am not in the right mindset to do anything else for the day.

But a spark is being born in me.

I want to program in Typescript and Blazor next.

Maybe I could try Svelte?

Who knows.

No, no Svelte. I need to say no to the unpopular.

https://compositionalit.github.io/farmer/api-overview/resources/container-apps/

Oh right, I'll need a docket image.

4:25pm. https://compositionalit.github.io/farmer/api-overview/resources/web-app/

> Serving two applications simultaneously (a frontend and a backend) from one web app using virtual applications.

```fs
Serving two applications simultaneously (a frontend and a backend) from one web app using virtual applications.
```

> Virtual applications can be defined for a webapp which allows you to specify alternative directories for the application executables or enable a single web app to host multiple applications at once. By default, the following virtualApplication is provided for you:

> Web App	enable_websockets	Configures the webapp to allow clients to connect via websockets.
> Web App	enable_cors	Enables CORS support for the app. Either specify WebApp.AllOrigins or a list of valid URIs as strings.
> Web App	enable_cors_credentials	Allows CORS requests with credentials.

///

Web App	add_virtual_applications	Adds list of virtualApplication definitions to the webapp
Web App	startup_command	Adds a startup command to be run post-deployment. This is useful on Linux-based web app deployments, where your application is “implicitly” converted into a docker image and may need to be told what to do on startup.

///

Oh, I should be able to use this to run the backend and the frontends separately.

4:55pm. Sigh, how about I take a break for a few days, from the microservices project?

I know that I am near the end, but so what?

It is not like that many people are depending on this.

Why don't I instead start both the react node UI as well as the online store?

Maybe program a bit in React in Typescript? In Blazor?

I could start the new vid right now, but the deep sadness I am feeling right now over the admission to myself that Fable is not good enough strikes at me.

If only this world was just.

If only there was a system that gives me rewards for doing the right thing, I could dive into Fable, and contribute to the compiler. I could make libraries for it.

But it is the opposite of that. I am only getting feedback that I should ditch it.

Sigh.

5:10pm. https://trpc.io/

I am going to make some codegen tools to make integrating TS and F# easier.

5:15pm. Yeah, code generation is clearly the solution here.

And this is exactly my specialty as a programmer.

7:20pm. https://boards.4channel.org/g/thread/93402255/an-ai-girlfriend-made-72k-in-1-week
> An AI Girlfriend made $72K in 1 week
> your thoughts ?

I think that I am an idiot.

I thought about it long ago so why am I not doing this?

7:25pm. Because I can't automate it.

I'll stick to my present path in this life.

A plan is forming for me.

TS + FS + codegen will be the way to go.

I've been Imagining and Spiral could have a lot of use for compiling Azure functions, but baby steps.

I need to establish my proper workflow.

7:30pm. What I really want with Youtubing is to estalish myself as a master. This kind of explorative effort won't suffice.

I want to show people watching my channel the true way.

https://blog.logrocket.com/generate-typescript-csharp-clients-nswag-api/

...Holy hell, what is this shit?

My idea was to marely take an F# record and code generate serializers and interfaces instead of runtime like Fable Remoting does in both the F# and TS languages.

https://github.com/jvilk/MakeTypes

Closer but not really.

https://www.openapis.org/

> The OpenAPI Specification is a specification language for HTTP APIs that provides a standardized means to define your API to others. You can quickly discover how an API works, configure infrastructure, generate client code, and create test cases for your APIs. Read more about how you can get control of your APIs now, understand the full API lifecycle and communicate with developer communities inside and outside your organization.

Zaid Ajaj has videos on this.

https://www.youtube.com/results?search_query=openapi

I do not feel like studying this right now.

I am not sure it will support F#'s union types either way.

7:40pm. Let me close here."

---
## [Dogii0/AML](https://github.com/Dogii0/AML)@[6b63f21b65...](https://github.com/Dogii0/AML/commit/6b63f21b6587e0186cf543607694e6185524fe1e)
#### Saturday 2023-05-13 18:07:30 by Jasper

Updated slight bugs

I actually forgot everything else I changed except for attack animation right.

First, it wasn't sliced, I forgot. So I sliced it, played it, but I realised I forgot to reload the assets again into the animation. So I did.

It is 3am. I have COVID. I have been working on this for 8 hours, I am going to sleep goodnight.

ps, THE SMALL ANIMATION GLITCHES THAT USUALLY GO UNNOTICED BOTHER ME FOR SOME REASON.

pps, note to self, fix ghost and player collision. It looks like they're social distancing and it made me laugh for 5 minutes.

---
## [FireFlashie/Fluffy-STG](https://github.com/FireFlashie/Fluffy-STG)@[7c6e64caef...](https://github.com/FireFlashie/Fluffy-STG/commit/7c6e64caefea860c27c7f11f16d067f99a25320b)
#### Saturday 2023-05-13 18:39:03 by SkyratBot

Stops station blueprints from expanding areas of non atmos adjacent turfs. [MDB IGNORE] (#20480)

* Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

* Stops station blueprints from expanding areas of non atmos adjacent turfs.

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [FireFlashie/Skyrat-tg](https://github.com/FireFlashie/Skyrat-tg)@[28e53c240e...](https://github.com/FireFlashie/Skyrat-tg/commit/28e53c240e21902f73ee5b2a3221c01efcaa5908)
#### Saturday 2023-05-13 18:39:05 by SkyratBot

[MIRROR] Tcomms Soundloop Comes From One Source And Is Less Awful [MDB IGNORE] (#20713)

* Tcomms Soundloop Comes From One Source And Is Less Awful (#74908)

## About The Pull Request

The ``soundloop/server`` now only comes from the server hub, so it
doesn't have stacking audio sources. The sound has been made more
uniform when up close, but is overall quieter. Additionally, all the
files have been run through a low pass filter to remove the highest of
it's pitches.
## Why It's Good For The Game

I'm sick of not wanting to be around telecomms because of how bad every
single machine sounds. Now, things are significantly easier on the ear,
quieter, more uniform, and better for everyone's sanity. I asked the
maintainers in the coding channel if I could just remove it and they
said no.

I can't get a video recording, I've tried with win+G, OBS, and sharex
and it's just fucked.
## Changelog
:cl:
qol: telecomms is quieter and less ear-damaging.
sound: modified tcomms sound to remove high-tones.
fix: the telecomms sound only comes from the server hub machine.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Tcomms Soundloop Comes From One Source And Is Less Awful

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [CodeMouse179/terminal](https://github.com/CodeMouse179/terminal)@[6ad8cd0a63...](https://github.com/CodeMouse179/terminal/commit/6ad8cd0a630ab927629841a14d433c3bc19a1509)
#### Saturday 2023-05-13 19:09:13 by Mike Griese

Make conhost act in VtIo mode earlier in startup (#15298)

We need to act like a ConPTY just a little earlier in startup. My relevant notes start here: https://github.com/microsoft/terminal/issues/15245#issuecomment-1536150388. 

Basically, we'd create the first screen buffer with 9001 rows, because it would be created _before_ VtIo would be in a state to say "yes, we're a conpty". Then, if a CLI app emits an entire screenful of text _before_ the terminal has a chance to resize the conpty, then the conpty will explode during `_DoLineFeed`. That method is absolutely not expecting the buffer to get resized (and the old text buffer deallocated). 

Instead, this will treat the console as in ConPty mode as soon as `VtIo::Initialize` is called (this is during `ConsoleCreateIoThread`, which is right at the end of `ConsoleEstablishHandoff`, which is before the API server starts to process the client connect message).  THEORETICALLY, `VtIo` could `Initialize` then fail to create objects in `CreateIoHandlers` (which is what we used to treat as the moment that we were in conpty mode). However, if we do fail out of `CreateIoHandlers`, then the console itself will fail to start up, and just die. So I don't think that's needed.

This fixes #15245. I think this is PROBABLY also the solution to #14512, but I'm not gonna explicitly mark closed. We'll loop back on it.

---
## [Fluffy-Frontier/Fluffy-STG](https://github.com/Fluffy-Frontier/Fluffy-STG)@[500cdb9257...](https://github.com/Fluffy-Frontier/Fluffy-STG/commit/500cdb925720c408de4332df6b2d8b8e0b20b63c)
#### Saturday 2023-05-13 19:11:14 by SkyratBot

north star's asylum no longer spawns with prisoners [MDB IGNORE] (#20732)

* north star's asylum no longer spawns with prisoners (#74879)

## About The Pull Request
the asylum on the north star no longer spawns prisoners, only the
permabrig does
the computer in the asylum is rotated correctly

## Why It's Good For The Game
on the paper, it seems like a cool concept, but theres a few issues here
the psychologist isnt designed to handle prisoners in the first place.
this is fine on mrp but it gets kinda muddy when prisoners on lrp like
beating people up
prisoners are recommended as a new player role by the wiki (very
stupid), this role starting in an asylum without anything to do while
being asked some stuff by a psychologist seems like itd add onto
confusion
players dont know what jobs are spawning with them, there very well may
not be a cmo or psychologist. if theres no one in sec you can deal with
that because you have a small botany and kitchen, and can possibly
escape. this aint a thing here, only thing you have is reading books and
maybe pen and paper rpgs if another prisoner spawns, while being stuck
in an extremely tiny space

this can work in the future i think, but it requires code support we
currently dont have, so it better to cut its

## Changelog
:cl:
del: prisoner spawns from the north star asylum
/:cl:

* north star's asylum no longer spawns with prisoners

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [Fluffy-Frontier/Fluffy-STG](https://github.com/Fluffy-Frontier/Fluffy-STG)@[178b6fc96c...](https://github.com/Fluffy-Frontier/Fluffy-STG/commit/178b6fc96cef11619565d802750cad9e6c34b12a)
#### Saturday 2023-05-13 19:11:14 by SkyratBot

Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles [MDB IGNORE] (#20711)

* Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles (#74784)

## About The Pull Request

deers only show up in the BEPIS but i decided that they would be easy
enough to turn into a basic mob (they were). it was so easy in fact that
i decided to dip my toes into coding AI behavior, and made them freeze
up whenever they see a vehicle. this required a lot of code in a bunch
of places that i was quite unfamiliar with before starting this project,
so do let me know if i glonked up anywhere and i can work on smoothing
it out.
## Why It's Good For The Game

one less simple animal on the list. deers staring at headlights is
pretty cool i think, neato interaction for when you do get them beyond
the joke the bepis makes

i'm also amenable to dropping the whole "deer in headlights" code if you
don't like that for w/e reason- just wanted to make them basic at the
very least
## Changelog
:cl:
add: If you ever happen upon a wild deer, try not to ride your fancy
vehicles too close to it as it'll freeze up like a... you know where I'm
going with this.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[ae7595b8e1...](https://github.com/microsoft/terminal/commit/ae7595b8e13d4764f4db7b4060eaf57d1b4ee82e)
#### Saturday 2023-05-13 20:52:12 by Mike Griese

Add `til::property` and other winrt helpers (#15029)

## Summary of the Pull Request

This was a fever dream I had last July. What if, instead of `WINRT_PROPERTY` magic macros everywhere, we had actual templated versions you could debug into. 

So instead of 

```c++
WINRT_PROPERTY(bool, Deleted, false);
WINRT_PROPERTY(OriginTag, Origin, OriginTag::None);
WINRT_PROPERTY(guid, Updates);
```

you'd do 

```c++
til::property<bool> Deleted{ false };
til::property<OriginTag> Origin{ OriginTag::None };
til::property<guid> Updates;
```

.... and then I just kinda kept doing that. So I did that for `til::event`.

**AND THEN LAST WEEK**

Raymond Chen was like: ["this is a good idea"](https://devblogs.microsoft.com/oldnewthing/20230317-00/?p=107946)

So here it is. 

## Validation Steps Performed
Added some simple tests.

Co-authored-by: Leonard Hecker <lhecker@microsoft.com>

---
## [BeastlyGabi/Funkin-Feather-Legacy](https://github.com/BeastlyGabi/Funkin-Feather-Legacy)@[d6ba67b353...](https://github.com/BeastlyGabi/Funkin-Feather-Legacy/commit/d6ba67b353443652a7f8c4722788e7bab6dbb606)
#### Saturday 2023-05-13 21:28:26 by swordcube

Fix alphabet lerping and make it work on all framerates

Also fuck you fixedTimestep!!! you're a bitch!

---
## [QueerGlobal/qg-frontend-v2](https://github.com/QueerGlobal/qg-frontend-v2)@[6db1177f7f...](https://github.com/QueerGlobal/qg-frontend-v2/commit/6db1177f7fe1a2905ac83d4d5708db3db37afea0)
#### Saturday 2023-05-13 21:43:08 by Mekesia Brown

.gitignore Update - Add Slash in Front of Notes Directory Line (#17)

_I added some type setting, added a recommended placeholder image and
helpful route for any local notes folks keep, updated social media links
(with a correction of alt text attribute), and I FINALLY moved the
Footer component to the global App.js file. Now the footer will be
everywhere._

UPDATE: I ended up removing all changes except for the notes folder
slash in .gitignore since other changes are now in corresponding prs.

Please note that the whitespacing changes are a pain in the ass and I
don't know how to fix those yet. Please disregard since locally the app
works.

Please email me if you need any information, or of course comment in
this pr. As well you can Slack me. Thanks.

---
## [LwkyLion/qb-core](https://github.com/LwkyLion/qb-core)@[9d83a952c2...](https://github.com/LwkyLion/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Saturday 2023-05-13 21:45:52 by uShifty

feat: Implement QBCore.Shared.VehicleHashs 

Describe Pull request
Indexs the vehicles jenkins joaat(Hash) value as the key of the table as the key so we dont have to do some shitty ass loop through the vehicles comparing joaat values. I have no clue why this secondary table was removed in the first place if I had to guess people were lazy but this should help the lazys by automatically filling the table.

Questions (please complete the following information):
Have you personally loaded this code into an updated qbcore project and checked all it's functionality? [yes/no] (Be honest) 
Yes

Does your code fit the style guidelines? [yes/no] 
Yes

Does your PR fit the contribution guidelines? [yes/no]
Yes

---
## [Ereshkigall666/linguistic_cartography](https://github.com/Ereshkigall666/linguistic_cartography)@[0844d261e3...](https://github.com/Ereshkigall666/linguistic_cartography/commit/0844d261e3bb6d4819c7206872a2a76b14270c53)
#### Saturday 2023-05-13 22:26:10 by Ereshkigall

fuck you github and your JeKyLl BuIlD FaIlUrEs: the return

---
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[4874f16358...](https://github.com/sqnztb/Skyrat-tg/commit/4874f163585c1e00d3e5ced697c605f1cfcb141d)
#### Saturday 2023-05-13 22:34:18 by SkyratBot

[MIRROR] Fixes a runtime in simple_animal/hostile [MDB IGNORE] (#20588)

* Fixes a runtime in simple_animal/hostile (#74706)

## About The Pull Request

Attempting to fix this flaky test that has been cropping up from the
Icebox tests. It is annoying.

From what I can tell, the mob was getting qdeleted while it was doing
its loop of finding a target. This can happen at any time, because many
simple mobs (including the one causing the issues) get qdeleted on
death.

Added some more checks to make sure we don't do certain actions if the
mob gets qdeleted midway through execution of its AI routine. It really
could happen anywhere so we must be vigilant.

```
create_and_destroy: [02:24:31] Runtime in stack_trace.dm,4: addtimer called with a callback assigned to a qdeleted object. In the future such timers will not be supported and may refuse to run or run with a 0 wait (code/controllers/subsystem/timer.dm:583)
proc name:  stack trace (/proc/_stack_trace)
src: null
call stack:
stack trace("addtimer called with a callbac...", "code/controllers/subsystem/tim...", 583)
addtimer(/datum/callback (/datum/callback), 300, 8, null, "code/modules/mob/living/simple...", 595)
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GainPatience()
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GiveTarget(the mi-go (/mob/living/simple_animal/hostile/netherworld/migo))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): FindTarget(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): AIShouldSleep(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): handle automated action() at stack_trace.dm:4
```

On top of that, there is signal handling in place to LoseTarget() when a
mob that is already a target gets qdel'd and sends
`COMSIG_PARENT_QDELETING`. Shown below.

https://github.com/tgstation/tgstation/blob/4c48966ff80915ee0b4f796994a0ab6616cab31b/code/modules/mob/living/simple_animal/hostile/hostile.dm#L655-L666

However there is nothing stopping a target that is not null but that has
been qdeleted from being considered as a target in the first place.

This PR just aims to fix that problem by making sure that a) a hostile
ai that gets qdeleted midway through does not keep doing stuff that can
cause issues and b) an atom that is being qdeleted never makes its way
into the targets list of a hostile ai.

Simple mobs/AI are due for a wider refactor honestly but this really
ought to be done in the meantime so we don't get spammed by CI failures
over nonsense.

Fixes https://github.com/tgstation/tgstation/issues/73032
Fixes https://github.com/tgstation/tgstation/issues/74266
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19749
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19322
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18974
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19296
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19294

## Why It's Good For The Game

Bugfix, stops the icebox test from failing as much.

## Changelog
:cl:
fix: fixes hostile mobs sometimes being able to target an atom that has
been marked for deletion and then becoming confused, and in a similar
vein fixes mobs sometimes still running their AI while being marked for
deletion.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Fixes a runtime in simple_animal/hostile

---------

Co-authored-by: Bloop <vinylspiders@gmail.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [mentalisttraceur/home](https://github.com/mentalisttraceur/home)@[80d6d9aec4...](https://github.com/mentalisttraceur/home/commit/80d6d9aec4bd166d826b7f5b236679d112904157)
#### Saturday 2023-05-13 23:04:27 by Alexander Kozhevnikov

.emacs: make Esc to exit i-search

I never really found i-search's lack of a
simple "I'm done, exit i-search" keybind
intuitive or compatible with how I think.

(I don't always want to move my cursor or
do a non-i-search command when I want to
exit i-search, and I rarely want the Ctrl-g
behavior of going back to wherever I was
when I started i-search - though I do like
having that more severe abort option and I
like it on Ctrl-g where it's a little less
fast/easy/smooth than Esc).

Annoyingly, out-of-the-box, Esc *almost*
works to exit i-search (it "works" because
it falls through to whatever it's bound to
under i-search, whether that's the stock
prefix map or Evil's binding of it), so I
already grew a habit for hitting Esc to
drop out of i-search, which I discovered
when Esc in i-search fell through to my
new keybinding in vi motion state to quit
the whole window.

---
## [mpela81/terminal](https://github.com/mpela81/terminal)@[a916a5d9de...](https://github.com/mpela81/terminal/commit/a916a5d9de450bc6a008d257d3c5c5cfd27e07ec)
#### Saturday 2023-05-13 23:33:40 by Mike Griese

Make sure the infobar is inserted before the tab content, not on top of (#11609)

Fixes #11606

This is weird, but the infobars would appear totally on top of the
TerminalPage when `showTabsInTitlebar:false`. This would result in the infobar
obscuring the tabs.

Now, the infobars are strictly inserted after the tabs, before the content. So
when they appear, they will reduce the amount of space usable for the control.
That is a little annoying, but preferable to the tabs totally not existing.

Relevant conversation notes from #10798:

> > If the info bar is not local to the tab, then its location between the tab
> > bar (when the title bar is hidden) and the terminal panes feels
> > misleading. Should it instead be above the tab bar or below the terminal
> > panes?
>
> You're... not wrong here. It's maybe not the best place for it, but _on top_
> of the tabs would look insane, and probably wouldn't even work easily, given
> the way we reparent the tab row into the titlebar.
>
> In the pane itself would make more sense, but that runs abreast of all sorts
> of things like #9024, #4998, which might make more sense.

I'm just gonna go with this now, because it's _better_ than before, while we
work out what's _best_.

![gh-11606-fix](https://user-images.githubusercontent.com/18356694/138729178-b96b7003-0dd2-4521-8fff-0fd2a5989f22.gif)

---
## [YellowSegment/Game](https://github.com/YellowSegment/Game)@[b650a6a660...](https://github.com/YellowSegment/Game/commit/b650a6a660893ad214813eef2f8ac87d6df672dc)
#### Saturday 2023-05-13 23:44:36 by YellowSegment

Very small change

Changed size of the window. I'm going to do more tonight, but Morgan is dragging me into a paint date... oh god, oh fuck

---

