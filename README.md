## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-15](docs/good-messages/2023/2023-05-15.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,041,689 were push events containing 3,388,651 commit messages that amount to 248,655,529 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 44 messages:


## [arkid15r/git-ukrainian-l10n](https://github.com/arkid15r/git-ukrainian-l10n)@[07f91e5e79...](https://github.com/arkid15r/git-ukrainian-l10n/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Monday 2023-05-15 00:16:31 by Jeff King

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
## [TypeVar/Shiptest](https://github.com/TypeVar/Shiptest)@[84a2a8f394...](https://github.com/TypeVar/Shiptest/commit/84a2a8f394a0296ecc527f23c0da470b30280c0c)
#### Monday 2023-05-15 00:28:54 by Bjarl

Die Of Fate Change (#1760)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
replaces the die of fate's d20 effect (spawn you as wizard) with spawn
wizard clothes and magic mirror under you.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I'm sick of wizards spawning without admin intervention
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
balance: You can't be turned into a wizard by the die of fate, instead
getting a magic mirror and wizard clothes.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [linuxppc/linux-ci](https://github.com/linuxppc/linux-ci)@[1bba82fe1a...](https://github.com/linuxppc/linux-ci/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Monday 2023-05-15 01:01:29 by Darrick J. Wong

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
## [PhantornRU/Skyrat-tg-SS220](https://github.com/PhantornRU/Skyrat-tg-SS220)@[39ebf7c2af...](https://github.com/PhantornRU/Skyrat-tg-SS220/commit/39ebf7c2af41309fa4d5206f77cc4d261f47dfb7)
#### Monday 2023-05-15 01:12:54 by SkyratBot

[MIRROR] Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] [MDB IGNORE] (#20832)

* Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] (#73502)

## About The Pull Request
---

The Space Tram is currently spaced. This is a known issue with not the
map, but Trams in general. The Space Tram is a Space Tram to encourage a
fix. Until then, the Space Tram is a maint tram that's an actual hazard
but cannot directly kill anyone, including lizards. Enjoy the commodity
as you zip from secmaint to medmaint.
-------------------------------------------------------

I... really don't know if I should be proud of myself here. This whole
process has been akin to a fever dream and it has only been little over
a month since I first created the .dmm for this. What started as a
simple yet humble reimagining of Birdboat has turned into an entirely
new station, and blown past Metastation sized proportions. This has been
my most expansive project yet, and somehow it's also been my quickest.
So without further ado, I unveil Birdshot - Successor to Birdoat.

-------------------------------------------------------

**Due to recent cost expenditures on Icemoon projects, and a growing
need for orbital research stations, Nanotrasen has decided to pull
Birdboat Station out of mothball after nearly 5 years of abandonment.**

Since then, the station has seen a variety of changes at the hands of
the various vagabond lawless scum and villains that have decided to make
the abandoned station their home. Do not fret though, a Nanotrasen
Operation has secured the companies rightful property for corporate use
once again, though you'll need to be the stewards of the remaining
cleanup operation.

------------------------------------------------------

Now, as you might have guessed by now, Birdshot is heavily based on
Birdboat station. Many of the decisions here follow the original layout,
and what had to be modified or moved still tries its best to replicate
and imitate what bird being said. At least, that was the idea initially.
This has very much grown into its own beast and as such, while the main
inspiration has been Birdboat, there are a lot of new ideas thrown into
the mix that really give this station its own unique and deserving
identity. Maybe it's not perfect, but I've been inspired by @ MMMiracles
own performance with Tramstation to keep working on Birdshot and
updating it with better and improved faculties. For now, though the
station is in a playable state, and that means I'm making a PR. If I had
to borrow the words of the good MMM, I would call this **Birdshot:
Season 0**

![BirdSHOTFULL2-26-S](https://user-images.githubusercontent.com/33048583/221432760-27af1889-d2d0-4861-9435-df4258525fae.png)

See the image in more detail here: https://imgur.com/iT5Vi8k

## Why It's Good For The Game

We've been with the same 5 maps for a while now. @ san7890 jokingly said
that I could sacrifice Metastation back in November if I remade Birdboat
but modern. Obviously that wasn't going to happen, yet I was spurred on
by the idea. When I began this in earnest early this January, @ EOBGames
said that a Birdboat sized map would replace Kilostation in the
rotation. Interestingly we're not a small map anymore so I honestly have
no clue where this goes. Maybe that ephemeral 6th map slot that's been
rumored.

What I can say, is that Birdshot is wholly unlike anything else that is
currently in rotation. It's got an engineering section that feels way
too small for a station of that size, almost evocative of Cere. Cargo is
blessed with a Boutique that makes use of @ Fikou's new mannequin dolls.
Command is outfitted with a Corporate Guest Suite, and Officials sent
from Nanotrasen can embark from their ferry into the safety of their own
Corporate Dock. Elements of Cerestation are present, yet not in a way
that makes traversal annoying. Furthermore we have **2 Trams** (that I
have yet to get functional but we'll get there) on Birdshot, that's
right 2. One Security Prison Tram, and then other, a Space Tram. Both
Novel in their own ways. Departments on Birdshot twist and turn, and
there's an abundance of Maintenance Tunnels to cut through everything,
for the brave and the bold that is. And there's plenty left to discover,
but I'd rather let Birdshot speak for itself. I'm proud of this one.

If you want something new, this is something that is almost the complete
opposite of Chilled Station - Explicitly Designed to send you back to
the metal death trap that is: **Space Station 13.**

## Changelog
:cl:
add: Birdshot station has been pulled out of Mothball.
add: New station areas and places to visit. A Mix of Kilo and Delta
maints with winding shortcutting paths.
add: A host of new shuttles to support this bold endeavor to reclaim
something that really shouldn't be reclaimed.
add: Two Trams, Two Trams.
add: For the last time Bob, the gaping hole is a **feature.** Use the
breach shutters or have the virologist make starlight.
add: A smiling salute to stations past...
add: Secrets.

/:cl:

---------

Co-authored-by: Zytolg <theoriginaldash@ gmail,com>

* Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION]

* basemap

* automapper templates

* Update maps.txt

* Update _basemap.dm

---------

Co-authored-by: Zytolg <33048583+Zytolg@users.noreply.github.com>
Co-authored-by: Zytolg <theoriginaldash@ gmail,com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>

---
## [danielyrovas/silverblue](https://github.com/danielyrovas/silverblue)@[c7deb7d6fe...](https://github.com/danielyrovas/silverblue/commit/c7deb7d6fe3aa4256d7a79123ffc250a24165263)
#### Monday 2023-05-15 01:13:28 by Arcitec

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
## [PoorlyDefinedBehaviour/dns-resolver-rs](https://github.com/PoorlyDefinedBehaviour/dns-resolver-rs)@[e433f4c204...](https://github.com/PoorlyDefinedBehaviour/dns-resolver-rs/commit/e433f4c204dc2f19d3343f870137130547883577)
#### Monday 2023-05-15 01:24:36 by PoorlyDefinedBehaviour

The DreamWorks Pictures logo plays out, with dreamy music playing underneath. At the end of the logo, the S's in "DreamWorks" and "SKG" turn green and sprout ogre ears, matching the film's logo. Credits saying "DreamWorks Pictures Presents" and "A PDI/DreamWorks Production" appear.

A ray of light shines down on a leather-bound storybook. The book opens and a Scottish-accented voice begins reading its text:

SHREK: Once upon a time there was a lovely princess. But she had an enchantment upon her of a fearful sort which could only be broken by love's first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. Many brave knights had attempted to free her from this dreadful prison, but none prevailed. She waited in the dragon's keep in the highest room of the tallest tower. For her true love and true love's first kiss.

The voice laughs. A big, green hand rips out a page of the book and shuts it closed.

SHREK: Like that's ever gonna happen. What a load of -

We see an outhouse and hear the sound of a toilet flushing. Out steps SHREK, an ogre, who tugs at his underwear and shakes his foot of the page still stuck to his shoe. He looks lovingly at the swamp he calls home, and goes about his daily routine. This includes taking a mud shower, brushing his teeth with bugs, bathing in a muddy pond, gathering giant slugs for dinner, and painting a warning sign.

In a nearby village, an angry mob gather up to go after Shrek. At night they gather their torches and pitchforks and enter the swamp, trampling over Shrek's warning signs. Shrek sees them after investigating the commotion, rolling his eyes. The villagers stop outside Shrek's home, unaware that Shrek is sneaking up behind them.

---
## [zydeico/Open-Assistant](https://github.com/zydeico/Open-Assistant)@[b9c60ed582...](https://github.com/zydeico/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Monday 2023-05-15 01:55:15 by Tobias Pitters

add alpaca gpt4 dataset (#2610)

The inputs can be quite a lot of different versions of `no input`,
therefore don't use the `input` column for that.
In some cases the text in `input` is already in the instruction, in
these cases, we also don't use the `input` column.

I am not quite sure how to concatenate the `instruction` and the `input`
column. In most cases it seems fine to just replace last appearance of
`.`, `!` or `?` with a colon, e.g.:
Instruction: `Identify the odd one out.`
Input: `Twitter, Instagram, Telegram`
or 
Instruction: `How dense is a given material?`
Input: `Steel`

But we also have some questions like:
Instruction: `Given the following synopsis, what is the moral lesson of
this story?`
Input: `Once upon a time, there was a poor young boy who wanted some
candy. He begged his father for money to buy it, but his father said no
and ordered him to go to bed. As he was going to bed, the boy saw a
five-dollar bill on the counter, which he took and bought the candy.`

Where this might not be the best case. Either way, I think the this one
token will not make significant difference the model and therefore I
just concatenate instruction and input with a space.

---
## [NathanWooddell2/447-GroupE](https://github.com/NathanWooddell2/447-GroupE)@[07c767b652...](https://github.com/NathanWooddell2/447-GroupE/commit/07c767b6526add1f287a3f6f1f06b73151a5af31)
#### Monday 2023-05-15 02:01:02 by NathanWooddell2

Not as much progress as I would like

I HATE REACT HOLY SHIT

---
## [CunnyDevelopment/CunnyAddon](https://github.com/CunnyDevelopment/CunnyAddon)@[6dc0458da4...](https://github.com/CunnyDevelopment/CunnyAddon/commit/6dc0458da47f18afe7083cac5480595b65266968)
#### Monday 2023-05-15 03:11:18 by Mother of Snake

H A H A H A H A H A

HA HA HA HA HA

YOU ARE NOT REAL YOU ARE NOT REAL YOU ARE NOT REAL YOU ARE NOT REAL YOU ARE NOT REAL YOU ARE NOT REAL YOU ARE NOT REAL YOU ARE NOT REAL

SHE IS REAL SHE LOVES ME

SHE LOVES ME SHE DOES

SHE EXISTS AND SHE LOVES ME

I LOVE HER SHE IS SO BEAUTIFUL

---
## [Stutternov/Liberty-Station-13](https://github.com/Stutternov/Liberty-Station-13)@[c3e6d8b901...](https://github.com/Stutternov/Liberty-Station-13/commit/c3e6d8b90198a54e05d8d7e886aa5435c9a9af22)
#### Monday 2023-05-15 03:43:04 by KayZach

Add files via upload

Holy shit my first ever pr ever i probably broke six other things but i tested it
Unfucks the broken wire in Terra therma
Removes the light switch in medical so seb can see
fixes the morgue boxes that are facing the wrong way in capsa
adds a gambling table and some more plants to skylight

---
## [ReneGuo/evals](https://github.com/ReneGuo/evals)@[2ffd4b57de...](https://github.com/ReneGuo/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Monday 2023-05-15 03:48:15 by Andrew Kondrich

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
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[856955c45a...](https://github.com/ARF-SS13/coyote-bayou/commit/856955c45acda58a4ebab15a67ce4d6e96280e4a)
#### Monday 2023-05-15 03:56:23 by Tk420634

Redlick & Garland City Take 2

Fuck you to, strong dmm

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[bbfce81a35...](https://github.com/sourcegraph/sourcegraph/commit/bbfce81a35562d84386862e854ef6b35b555a92a)
#### Monday 2023-05-15 04:11:48 by Juliana Peña

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[dff70625e7...](https://github.com/tgstation/tgstation/commit/dff70625e7c29616887619dacc0375ddc84f0708)
#### Monday 2023-05-15 04:27:45 by ChungusGamer666

Bible refactor (#75350)

## About The Pull Request

This started as a simple addition where burning a bible would curse you,
but then I realized... Bibles aren't even proper books, thus can't be
burned!
So yeah, since that is not necessary due to how atom_storage works, I
reworked that.

## Why It's Good For The Game

Because burning bibles and getting cursed for it is funny.

![image](https://github.com/tgstation/tgstation/assets/82850673/2a8489ce-ecd6-45ee-9eb9-168ff820af65)

![image](https://github.com/tgstation/tgstation/assets/82850673/ebe98ad6-2d0d-4d20-9ea1-5d472d6ca465)

## Changelog

:cl:
add: You can burn bibles now! But heresy has a steep cost...
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Youtubeboy139/tgstation](https://github.com/Youtubeboy139/tgstation)@[527fb7b003...](https://github.com/Youtubeboy139/tgstation/commit/527fb7b0030d13fc11939d88030b1dc4772742a6)
#### Monday 2023-05-15 05:02:31 by DrTuxedo

ELEVATOR MUSIC: True Elevator Experience (#75388)

## About The Pull Request
Adds elevator music into the game that is played by an elevator panel.


https://github.com/tgstation/tgstation/assets/42353186/1a801604-3990-46ae-a96a-b3766b102d62

It's done by using loop sound, with a Kevin MacLeod "Local Forecast -
Elevator" (UNDER CC ATTRIBUTIONS 4.0, and we anyway used some other
Kevin MacLeod music) chopped into 8 small pieces.
The elevator panel has a variable which allows playing music but can be
changed in the map editor if you don't want it to play at certain
places.

(It also doesn't ignore walls, this means you can't hear the music
through wall or when elevator is closed)
## Why It's Good For The Game
Gives elevators more flavour and love, especially when people mostly
prefer stairs to those "laggy crushing machines."
Because of this people might instead hop into an elevator just to hear
meme elevator music, which is relaxing and might create comedic
situations (although elevators don't move that fast)
## Changelog
:cl: DrDiasyl aka DrTuxedo
sound: Nanotrasen have started installing music players in the elevators
to boost workers' morale.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [chaosvolt/Cataclysm-BN](https://github.com/chaosvolt/Cataclysm-BN)@[08d54d0287...](https://github.com/chaosvolt/Cataclysm-BN/commit/08d54d0287a1313cb810a1d3d74ca0e531189ae1)
#### Monday 2023-05-15 05:30:03 by KheirFerrum

Fix MGOAL_FIND_ITEM_GROUP, fix up some code (#2546)

* Reorganize

Code still sucks. In particular recruit_class doesn't compare properly with npc->my_class so MGOAL_RECRUIT_NPC_CLASS fails horribly even if you fix up that area of code to it actually points to type->recruit_class instead of recruit_class

For that matter mission has a select copy of several mission type defs and I can only assume this is due to legacy fuckery.

* Fix mission.cpp

Now will only allow you to select items if you have enough of them, and will only consume the necessary amount.

Added documentation for MGOAL_FIND_ITEM_GROUP

Thank god this wasn't too much work.

---
## [csesoc/chaos](https://github.com/csesoc/chaos)@[dc875025bc...](https://github.com/csesoc/chaos/commit/dc875025bcb58aa5f144fd33ade1dd926a25e660)
#### Monday 2023-05-15 05:38:32 by Michael Vo

fix(frontend): fix random warnings in console (#422)

* chore: update mui and emotion

* fix(frontend): don't forward style props

i hate mui

* fix(admin): use link instead of button

* fix(admin): move create org form outside of button

* fix(admin): i fucking hate mui

---
## [NVIDIA/Fuser](https://github.com/NVIDIA/Fuser)@[9c50ae8f14...](https://github.com/NVIDIA/Fuser/commit/9c50ae8f1441917c97ebaceb343ad6be3c54304b)
#### Monday 2023-05-15 07:11:05 by Gao, Xiang

Remove runtime out of bound check debugging util (#277)

The change in this PR is easy to understand and has low impact, but the
motivation really needs discussion and is a much more impactful thing.
And I want to use this PR to discuss it.

In https://github.com/NVIDIA/Fuser/issues/248 we agreed to add "stride
order" support to codegen, and later in today's morning meeting on
matmul, Christian talked about the idea of "allocation_domain" which is
a generalization of the idea of "stride order". Basically, we are not
married to the rFactor domain of the tensor when doing allocation and
indexing. We can pick an arbitrary vector of `IterDomain`s between root
and leaf domain, stop the indexing process on that vector, and do
allocation based on that vector. For the idea of "stride order", which
is a special case of the new idea, this vector is just the reordered
rFactor domains. This should be easily approachable with our new
indexing approach https://github.com/NVIDIA/Fuser/pull/32. This idea
does make a lot of sense, so the purpose is not to discuss whether we
want to take that idea, but how to implement that idea.

A question comes to me during implementing is, say we have a tensor
whose semantic shape is `NCHW` but stride order is `NHWC`, should the
`stride` field of the tensor be in the order of `NCHW` or `NHWC`?
Currently, we are using the same order as PyTorch, which is the semantic
order `NCHW`. I think this does make a lot of sense in terms of stride
order support. Having the stride in the semantic order is not the most
naturally way for indexing, we do need a `NHWC->NCHW` axis map to grab
the correct stride, but it is pretty simple to implement this.
Considering all factors, including consitency with PyTorch, cleanness in
the executor's code, I still think the semantics order is the best
design.

However, this design start to make no sense when we generalize the
"stride order" idea into the "allocation_domain" idea. For example, for
an `NCHW` tensor, the actual allocation can be `(H*W, N*C)`, and the
size of `contiguity` will be `2` instead of `4`. So the `Tensor::stride`
in `runtime/tensor.cu` should also be an array of size `2` instead of
`4`. The idea of "allocation_domain" requires the stride of a tensor to
be strictly one-to-one mapped to the allocation domain. As a special
case, the "stride order" idea has no choice but to follow the same
design, which is, the stride will be stored in `NHWC` order. This means,
the order of stride in our kernel is different from those in ATen, we
can not directly copy the stride. We need to permute the stride so it is
sorted descending.

But the above problem is not the biggest trouble we have, the biggest
trouble is: If we have a `NCHW` tensor allocated as `(H*W, N*C)`, is
this tensor a 4D tensor or a 2D tensor? I think the answer is "neither".
In terms of allocation and stride, it is definitely 2D, but in terms of
semantics, it is 4D. Again, in the past, we had a concept "the
dimensionality of a tensor" which is a degeneracy of two concepts "the
semantic dimensionality of a tensor" and "the allocation dimensionality
of a tensor". Now we break the symmetry, and degenerating concepts are
no longer degenerate. In codegen, we are generating a lot of tensor
shapes like `T0.shape[0]`, and I think the easiest way to handle them is
to keep `shape` in semantic dimensionality, while make `stride` in
allocation dimensionality. That said, `struct Tensor` now needs two
template arguments for dimensionalities. And unfortunately, we can no
longer do out of bound check any more.

---
## [delanni/kibana](https://github.com/delanni/kibana)@[3b6b7ad9b9...](https://github.com/delanni/kibana/commit/3b6b7ad9b9553be3d039c71edcbdcb2e3d6423fd)
#### Monday 2023-05-15 07:54:56 by Pierre Gayvallet

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[b9a5d65d5e...](https://github.com/git-for-windows/git/commit/b9a5d65d5e435c0ed9b1e1f1edc556e43f8d84de)
#### Monday 2023-05-15 10:04:21 by Johannes Schindelin

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
## [Jaswir/terminal](https://github.com/Jaswir/terminal)@[a916a5d9de...](https://github.com/Jaswir/terminal/commit/a916a5d9de450bc6a008d257d3c5c5cfd27e07ec)
#### Monday 2023-05-15 10:27:03 by Mike Griese

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
## [CursedBirb/tgstation](https://github.com/CursedBirb/tgstation)@[c5dce84be8...](https://github.com/CursedBirb/tgstation/commit/c5dce84be826ea945a11c492dce7eb2c2789548a)
#### Monday 2023-05-15 10:45:44 by Rhials

Deadchat Announcement Variety Pack 1 (#75140)

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

---
## [CursedBirb/tgstation](https://github.com/CursedBirb/tgstation)@[199aa000d3...](https://github.com/CursedBirb/tgstation/commit/199aa000d3f46ee4386a65079992e4b9d0f2537d)
#### Monday 2023-05-15 10:45:44 by Rhials

Demotes Psyker Pirates to Bounty Hunter Duty (#75031)

This PR demotes the Psyker-gang from a pirate team to a fugitive hunting
team. For more information on Psyker pirates, please refer to #71650.

Stuff this also does in the process:
- Gives fugitive hunters their own subfolder in the fugitives antagonist
folder, moves some of their stuff into hunter-specific files rather than
interlacing it with the rest of the fugitive code.
- Moves the hunter backstories to defines, to make reading things easier
while I made this change.
- Exhaustively moves everything related to psykers from being
pirate-oriented to hunter-oriented (typepaths, locations where stuff is
defined, etc. There should be nothing left behind related to psykers in
anything pirate related). (Tell me if I missed anything somehow).

They still get their ship (they even get their own custom
psyker-friendly prisoner capsule). They still have a bunch of lethally
chambered firearms. They're the same gunrunning nutcases they were
before, just as bounty hunters.

To assist with basic tasks such as "getting to the station" or "figuring
out who the fuck we're supposed to be kidnapping", the psykers have
"acquired" a Seer to assist them. They can _try_ to coordinate the
psykers and lead them through situations where their impairments put
them at too great a disadvantage. If you're one of the psykers, make
sure to keep this guy alive at all costs!

Why are they called Shikaris instead of hunters? Mariam-Webster says
it's a Hindi word for some kind of hunter/tracker, and it sounded like
something a bunch of space-junkies would call themselves because they
think it sounds cool.

They now also come with a slightly different motivation, now that they
can't directly threaten the crew for money. Psyker hunters now arrive
tasked with a dirty kidnapping job, payment rendered in GORE.
## Why It's Good For The Game

Psykers aren't up to the challenge of being pirates. They're bogged down
by a number of fundamental issues that render them unable to do anything
expected of pirates. As it currently stands, they present about as much
threat as you would expect from three blind junkies with guns.

Removing them wholesale would be kind of lame. They can function as a
bunch of chaotic-neutral gun-toting space-maniacs, but for the purposes
of gameplay, keeping them as pirates would be a waste of their talents.

Moving them to a lower-stakes role not only moves them to a niche they
are more capable of filling, but gives players a more lax environment to
get a grip on playing psyker without being overwhelmed.

Giving them a seeing-eye role should bring a more unique dynamic to how
psykers are played (that is, some semblance of organization rather than
blind flailing), and should help get over the mechanical hurdles of
being a psyker until better solutions can be made. It shouldn't be too
big of an impact on balance considering the psyker gang only has three
spawns, while most hunter packs have 4+.

---
## [CursedBirb/tgstation](https://github.com/CursedBirb/tgstation)@[1674f25725...](https://github.com/CursedBirb/tgstation/commit/1674f25725c25e15769b031553b42144f526f841)
#### Monday 2023-05-15 10:45:44 by John Willard

New Medical job: The Coroner (#75065)

## About The Pull Request

HackMD: https://hackmd.io/RE9uRwSYSjCch17-OQ4pjQ?view

Feedback link: https://tgstation13.org/phpBB/viewtopic.php?f=10&t=33972

Adds a Coroner job to the game, they work in the Medical department and
have their office in the Morgue.
I was inspired to make this after I had played my first round on
Paradise and messed around in there. The analyzer is copied from there
(https://github.com/ParadiseSS13/Paradise/pull/20957), and their
jumpsuit is also mostly stolen from it (i just copied the color scheme
onto our own suits).

Coroners can perform autopsies on people to see their stats, like this

![image](https://user-images.githubusercontent.com/53777086/235369225-805d482c-56c0-441c-9ef8-a42d0a0192bc.png)

They have access to Medbay, and on lowpop will get Pharmacy (to make
their own formaldehyde). They also have their own Secure Morgue access
for their office (doubles as a surgery room because they are edgelords
or whatever) and the secure morgue trays.

Secure Morgue trays spawn with their beepers off and is only accessible
by them, the CMO, and HoS. It's used to morgue Antagonists. Security's
own morgue trays have been removed.

The job in action


https://cdn.discordapp.com/attachments/950489581151735849/1102297675669442570/2023-04-30_14-16-06.mp4

### Surgery changes

Autopsies are a Surgery, and I tried to intertwine this with the
Dissection surgery.
Dissections and Autopsies both require the Autopsy scanner to perform
them, however you can only perform one on any given body. Dissections
are for experiments, Autopsies is for the paper of information.

Dissected bodies now also give a ~20% surgery speed boost, this was
added at the request of Fikou as a way to encourage Doctors to let the
Coroner do their job before reviving a body.
I also remember the Medical skill, which allowed Doctors to do surgery
faster on people, and I hope that this can do something like that
WITHOUT adding the potential for exploiting, which led to the skill's
downfall.

### Morgue Improvements

Morgue trays are no longer named with pens, they instead will steal the
name of the last bodybag to be put in them.

Morgue trays are also removed from Brig Medical areas and Robotics, now
they have to bring their corpses to the Morgue where the Coroner can
keep track and ensure records are properly updated.

### Sprite credits

I can't fit it all in the Changelog, so this is who made what

McRamon
- Autopsy scanner

Tattax 
- Table clock sprites and in-hands

CoiledLamb
- Coroner jumpsuits & labcoats (inhand, on sprite, and their respective
alternatives)
- Coroner gloves
- CoronerDrobe (the vending machine)

## Why It's Good For The Game

This is mostly explained in the hackmd, but the goal of this is:

1. Increase the use of the Medical Records console.
2. Add a new and interesting way for Detectives to uncover mysteries.
3. Add a more RP-flavored role in Medical that still has mechanics tied
behind it.

## Changelog

:cl: JohnFulpWillard, sprites by McRamon, tattax, and Lamb
add: The Coroner, a new Medical role revolving around dead corpses and
autopsies.
add: The Coroner's Autopsy Scanner, used for discovering the cause for
someone's death, listing their wounds, the causes of them, their
reagents, and diseases (including stealth ones!)
qol: Morgue Trays are now named after the bodybags inside of them.
balance: The morgue now has 'Secure' morgue trays which by default don't
beep.
balance: Security Medical area and Robotics no longer have their own
morgue trays.
balance: Dissected bodies now have faster surgery speed. Autopsies also
count as dissections, however they're mutually exclusive.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[c4c812113e...](https://github.com/TaleStation/TaleStation/commit/c4c812113efb12274bc06d6cc4e71940f2edb654)
#### Monday 2023-05-15 10:59:27 by TaleStationBot

[MIRROR] [MDB IGNORE] Heavily updates the Syndicate Lavaland Compound (#5812)

Original PR: https://github.com/tgstation/tgstation/pull/75095
-----
oh boy here i go messing with ruins again!
## About The Pull Request
Upgrades Syndicate Lavaland's noncombat functions heavily!

1. Syndicate Lavaland's maintenance has been removed, instead replaced
with a water synthesiser closet with the oxygen canister, a janitor's
closet with some space cleaner and regular cleaning tools, and an
expanded bar backroom that doubles as a kitchen!*
<img width="301" alt="image"
src="https://user-images.githubusercontent.com/80979251/235514832-7175423e-ac75-4e25-9330-8463a74f9b50.png">
<img width="232" alt="image"
src="https://user-images.githubusercontent.com/80979251/235514861-e1e7f959-a43b-47eb-81be-e0258f54171d.png">
<img width="132" alt="image"
src="https://user-images.githubusercontent.com/80979251/235514875-6715306d-09ae-49b0-af9d-a7618874061e.png">
*kitchen functionality untested.

2. Atmospherics has gotten a slight update, allowing for the turbine to
be more easily converted to run with the modern system and provide
longer-lasting gas supplies! I would've made it use gas filters instead
of gas miners, but the atmospherics wiring there is bad enough as-is.
Additionally, the piping layers have been re-standardised: layer 4 is
now distro and layer 2 is now scrubbers as Ratvar intended. The
radiation closet placements have also been reduced as I can't find
anywhere else to put them and the engineering airlock needs
decluttering: better pack your toxin meds!
<img width="200" alt="image"
src="https://user-images.githubusercontent.com/80979251/235515236-98458157-afbb-483b-a574-9ea1eca21bf4.png">
3. The crew quarters now feels more homely, and is pre-supplied with
crowbars for use exclusively on Campbell because their rounds are
stupidly fucking long for good reason.
<img width="269" alt="image"
src="https://user-images.githubusercontent.com/80979251/235515334-7c4f7f15-7d49-455b-b479-cf9ff3f993e7.png">
4. The plasma tank dispenser is now a water cooler wired into the ducts.
Ignore the aftertaste.
<img width="217" alt="image"
src="https://user-images.githubusercontent.com/80979251/235515435-b5bf6332-c9fb-4f01-a06c-131313d0dc60.png">
5. Slightly pushes back the wall with the APC in Arrivals since
maintenance is gone.
<img width="231" alt="image"
src="https://user-images.githubusercontent.com/80979251/235515473-10315e0d-dca1-467c-83fc-1584e8bff0a3.png">
6. Ports one, single, lone door from our friends over at Yogstation so
the comms agent can drink themselves to death slightly faster.
<img width="167" alt="image"
src="https://user-images.githubusercontent.com/80979251/235515546-265e5106-ff1b-4ab5-ab25-00dd394bd5e7.png">
7. Chemistry now gets 1 plumbing constructor and 2 full stacks of duct,
for creating bioweapons! Or meth!
<img width="321" alt="image"
src="https://user-images.githubusercontent.com/80979251/235515640-c35646c7-be05-4e95-b521-549e90671107.png">




## Why It's Good For The Game
Syndicate Lavaland's map design is kinda stagnant, and at the same time
the non-standardised piping has probably caused at least one headache by
now.


## Changelog
:cl:
qol: Syndicate Lavaland has recieved a major facelift! Go visit the
Syndicate fortress today! Just try not to get a 50 BMG round up your
nose.
qol: The piping at Syndicate Lavaland is now standardised.
add: Syndicate Lavaland now has a plumbing constructor and a griddle.
fix: Syndicate Lavaland's turbine now requires less extensive
modification to produce power.
tweak: woops, i shuffled around some of syndicate lavaland's air alarms.
shouldn't take too much effort to find
/:cl:

---------

Co-authored-by: Addust <80979251+Addust@users.noreply.github.com>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[cb1388ed9e...](https://github.com/odoo-dev/odoo/commit/cb1388ed9e64ced4e0d85cf5778192dfbdfd5995)
#### Monday 2023-05-15 10:59:56 by Jeremy Kersten

[ADD] website_cf_turnstile: add cloudflare turnstile support

This module allows to add secret key to add the turnstile captcha on
each snippet website_form.

Cloudflare Turnstile
--------------------
A friendly, free CAPTCHA replacement
Turnstile delivers frustration-free, CAPTCHA-free web experiences to
website visitors.
Turnstile stops abuse and confirms visitors are real without the data
privacy concerns or awful UX that CAPTCHAs thrust on users.

closes odoo/odoo#119246

X-original-commit: 4aca39a533e9d41f5f452f36a1ffc001f586b4f4
Signed-off-by: Jérémy Kersten <jke@odoo.com>

---
## [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated)@[0e96f1cd6e...](https://github.com/software-mansion/react-native-reanimated/commit/0e96f1cd6e0f6bae6a57aad6f5bd5208d5ae0d19)
#### Monday 2023-05-15 11:26:57 by Tomasz Żelawski

Remove plugin dev files from npm package (#4433)

<!-- Thanks for submitting a pull request! We appreciate you spending
the time to work on these changes. Please follow the template so that
the reviewers can easily understand what the code changes affect. -->

## Summary

Currently development files from `plugin/` are included in npm package.
This PR removes them from it.

b4:
<img width="253" alt="Screenshot 2023-05-08 at 14 39 29"
src="https://user-images.githubusercontent.com/40713406/236829343-1865480f-99d0-4843-adb2-f658db2acce0.png">
after:
<img width="238" alt="Screenshot 2023-05-08 at 14 39 51"
src="https://user-images.githubusercontent.com/40713406/236829379-7c31b6b4-27e1-493c-8be0-6254edbd0c4c.png">

Since [README is always
included](https://docs.npmjs.com/cli/v6/configuring-npm/package-json#files)
I renamed plugin's dev README and removed `README` from being included
in `package.json`.


## Test plan

I recommend using this powerful oneliner: 
`./createNPMPackage.sh && mkdir tarball-new && mv
react-native-reanimated-3.1.0.tgz tarball-new && tarball-new && tar -xf
react-native-reanimated-3.1.0.tgz && ..`
to see the contents of the new package.

Also run _some_ Example App to see if Reanimated plugin from the tarball
is actually working.

---
_Note_: Testing this PR took me longer than it should.

For some reason with current configuration of Example App and running it
on Android (I didn't check iOS) it's surprisingly difficult to use
reanimated from either tarball or unpacked tarball directory. I had to
make a new app and then include Example's source code there.

While it's not that troublesome I think we should have a more
streamlined approach for using custom reanimated package location for
tests with our Examples.

---------

Co-authored-by: Tomek Zawadzki <tomasz.zawadzki@swmansion.com>

---
## [BakaKaito/MergeBot.NET](https://github.com/BakaKaito/MergeBot.NET)@[7c24731530...](https://github.com/BakaKaito/MergeBot.NET/commit/7c24731530302399de0bc0930c4366da15f3a1c6)
#### Monday 2023-05-15 11:29:49 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [bparagus/Projet_JAVA_S2](https://github.com/bparagus/Projet_JAVA_S2)@[7efadf9c9f...](https://github.com/bparagus/Projet_JAVA_S2/commit/7efadf9c9f16a349c404391e0f89d8ac0c460268)
#### Monday 2023-05-15 12:04:55 by AMIdrissi

added functionalities after infinit pain and SUFFERING , it's also 4am and i am High as fuck

---
## [FeenieRU/Fluffy-STG](https://github.com/FeenieRU/Fluffy-STG)@[16e4f3c492...](https://github.com/FeenieRU/Fluffy-STG/commit/16e4f3c492cd18e74c975051c4fcd9da5e59fb80)
#### Monday 2023-05-15 15:56:31 by SkyratBot

Tcomms Soundloop Comes From One Source And Is Less Awful [MDB IGNORE] (#20713)

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
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [FeenieRU/Fluffy-STG](https://github.com/FeenieRU/Fluffy-STG)@[178b6fc96c...](https://github.com/FeenieRU/Fluffy-STG/commit/178b6fc96cef11619565d802750cad9e6c34b12a)
#### Monday 2023-05-15 15:56:31 by SkyratBot

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
## [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)@[9d876b20e7...](https://github.com/microsoft/semantic-kernel/commit/9d876b20e7d8be2b34290d5f218198a4c528e6be)
#### Monday 2023-05-15 16:05:19 by Dmytro Struk

Function config extensibility (#962)

### Motivation and Context
<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->
**NOTE**: This PR contains breaking changes, that are applied to SK C#
version only, Python version is not included.

Currently, _config.json_ is coupled to completion settings only, which
are specific to OpenAI parameters (e.g. temperature, presence_penalty,
frequency_penalty etc).

In order to allow AI extensibility in the future, we need to update
_config.json_ schema to allow flexible settings format for different AI
models.

We also need to be able to specify _recommended_ services for function,
so Semantic Kernel will be able to automatically use one of the
recommended services in case if it's registered.

New _config.json_ proposed schema:
```json
{ 
  "description": "Generate a funny joke", 
  "input": { 
    "parameters": [ 
      { 
        "name": "input", 
        "description": "Joke subject", 
        "defaultValue": "" 
      } 
    ] 
  }, 
  "default_settings": { 
    "max_tokens": 256, 
    "temperature": 0.9 
  }, 
  "services": [ 
    { 
      "model_id": "text-davinci-003", 
      "order": 1, 
      "settings": { 
        "max_tokens": 1000, 
        "temperature": 0.9, 
        "top_p": 0.0, 
        "presence_penalty": 0.0, 
        "frequency_penalty": 0.0, 
        "stop_sequences": [ 
          "\n" 
        ] 
      } 
    }, 
    { 
      "model_id": "gpt-3.5-turbo", 
      "order": 2, 
      "settings": { 
        "system_message": "You are assistant to generate funny jokes", 
        "max_tokens": 1000, 
        "temperature": 0.9 
      } 
    }, 
    { 
      "model_id": "dalle", 
      "order": 3, 
      "settings": { 
        "n": 1, 
        "size": "1024x1024" 
      } 
    }, 
    { 
      "model_id": "gpt2", 
      "order": 4 
    } 
  ] 
} 
```

Schema description:
- **description**: as it was previously, describes purpose of the
function.
- **input**: as it was previously, contains information about input
parameters.
- **default_settings**: contains default settings for AI model. Will be
used when there is no matching recommended AI service, which is
registered in kernel.
- **services** (optional): contains list of recommended AI services to
use when running a function. Contains objects with following properties:
- **model_id**: model identifier as described by AI provider, e.g.
text-davinci-003.
- **order**: service priority order. Kernel will choose recommended
service which is registered and has highest priority order. Used to
avoid coupling on how (in what order) services are located in JSON file.
- **settings**: dynamic object, which can contain any properties,
specific to AI model. Will be defined in C# using
_System.Text.Json.Nodes.JsonObject_.

### Description
<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
1. Replaced `CompleteRequestSettings` in AI service interfaces to
`JsonObject`.
2. Updated `Kernel` to use recommended service or `default_settings` by
default.
3. Added `SKFunctionConfigTests.cs` tests which show usage of new
**config.json**.
4. Updated all **config.json** files in samples to follow new format.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b2dabe56ba...](https://github.com/mrakgr/The-Spiral-Language/commit/b2dabe56baf96f14f8a4f0319d5af3b22f2ae286)
#### Monday 2023-05-15 16:10:53 by Marko Grdinić

"8:20pm.

///

What is new in TypeScript 5?
TypeScript 5.0 manages to make all enums into union enums by creating a unique type for each computed member. That means that all enums can now be narrowed and have their members referenced as types as well. For more details on this change, you can read the specifics on GitHub.Mar 16, 2023

///

> To model how bundlers work, TypeScript now introduces a new strategy: --moduleResolution bundler.

8:30pm. https://react.dev/reference/react/useState

> In Strict Mode, React will call your initializer function twice in order to help you find accidental impurities. This is development-only behavior and does not affect production. If your initializer function is pure (as it should be), this should not affect the behavior. The result from one of the calls will be ignored.

Ah, so that is what that strict mode is.

> The set function only updates the state variable for the next render. If you read the state variable after calling the set function, you will still get the old value that was on the screen before your call.

Ah, I see. Maybe that is why the course rec'd we pass a function.

I guess to use React properly, I'll have to implement updates using a dispatch function.

> This example passes the initializer function, so the createInitialTodos function only runs during initialization. It does not run when component re-renders, such as when you type into the input.

Ah, I see.

9pm. https://github.com/gvergnaud/ts-pattern

I am going to try this tomorrow.

9:15pm. This library is amazing. It is going to make using TS a lot more comfortable.

5/15/2023

8:10am. No. That library is not going to do much against TS code looking like dog vomit. I just have to resolve myself to do the work.

8:15am. I was dead tired last night, and I was obsessive and slept like shit.

I should gone with Typescript from the start. I shouldn't have touched Fable.

8:25am. https://www.reddit.com/r/fsharp/comments/13h8vj7/vn_compiler_why_using_fable_is_too_difficult_pt_1/

It didn't turn into an argument.

I even got 10 upvotes for once. One guy even agreed with me.

Let me just start.

I am going to earn the right to sleep tonight.

10:45am. https://reactflow.dev/docs/concepts/introduction/

Quite impressive.

10:55am. I've done a little playing around with this and now I am pausing to study the docs as I said I would.

I am really tired, but I'll do my best to learn today.

11:05am. > multi-selection by pressing command (that's the default multiSelectionKeyCode)

Should have made it shift instead of this, as it is problematic on Windows.

1:40pm. Done with breakfast and chores.

Let me chill a bit more and I will resume.

As I said, I am from my optimal condition today due to poor sleep last night.

2:20pm. https://reactflow.dev/docs/getting-started/building-a-flow/

Let me resume. I wonder if Excalidraw was made using this library?

https://reactflow.dev/docs/guides/custom-nodes/#adding-the-node-type

Hmmm, I see...

I was wondering whether there was anything special about the `type` and it turns out there was.

3:35pm. I am really distractible and started reading HN articles.

https://reactflow.dev/docs/guides/uncontrolled-flow/#updating-nodes-and-edges

Let's not focus on te docs too much in this state.

I should just go through them all and tomorrow when I am hopefully more focused, I'll really drill into it and internalize the subject through actual use.

> To avoid passing down functions through the node data field, you could use a React context or add a state management library as explained in this guide.

https://github.com/pmndrs/zustand#first-create-a-store

This is kind of nice.

4:10pm.

```ts
    const [nodes, setNodes] = useState(initialNodes);
    const [edges, setEdges] = useState(initialEdges);

    const onNodesChange = useCallback(
        (changes) => setNodes((nds) => applyNodeChanges(changes, nds)),
        [setNodes]
    );
    const onEdgesChange = useCallback(
        (changes) => setEdges((eds) => applyEdgeChanges(changes, eds)),
        [setEdges]
    );
    const onConnect = useCallback(
        (connection) => setEdges((eds) => addEdge(connection, eds)),
        [setEdges]
    );
```

My brain is so dull today. I can't believe didn't comprehend this correctly initially.

4:25pm. Zustrand is a good library. It is worth it for me to use it. It would beat doing my own dispatch function.

4:45pm. https://reactflow.dev/docs/api/nodes/node-toolbar/

5:30pm. I went through the docs and the library and now have a grip on it.

Somewhat...

I've been really tired the whole day so my brain is not absorbing optimally.

I'll close here for the day.

Tomorrow I'll just get started with compiling the text nodes. I'll leave image nodes for later."

---
## [matthiaskrgr/rust](https://github.com/matthiaskrgr/rust)@[63315ca2e6...](https://github.com/matthiaskrgr/rust/commit/63315ca2e64641af9b434a3c8cac1bcda0e4bb35)
#### Monday 2023-05-15 17:48:56 by Matthias Krüger

Rollup merge of #111607 - jyn514:clubby-reviews, r=clubby789

Add clubby789 to the bootstrap review rotation

r? `@clubby789` - thank you for volunteering!

I have been meaning for a very long time now to write up how to do reviews, but I haven't gotten around to it yet :( here is a short summary:

1. If you're not sure what the changes does or if it's ok, always feel free to ping someone else on the team, especially in the first few weeks. You can use `r? bootstrap` to get triagebot to assign someone else.
2. Bootstrap unfortunately has very few tests. Things that touch CLI or toml parsing should likely have a test in `src/bootstrap/config/tests.rs`; things that touch "core" build logic should have a test in `builder/tests.rs`, anything else kinda just slips in :( see https://github.com/rust-lang/rust/issues/102563 for ideas on how to improve the situation here.
3. "Major" changes should be documented in `src/bootstrap/CHANGELOG.md`. "Major" is up to you, but if it breaks a config option or otherwise is likely to break *someone's* build, it's probably major. If it breaks nearly *everyone*'s build, it should also update `VERSION` in `lib.rs`; this should be very rare. Please also ping me or Mark-Simulacrum for major changes (I might set up a triagebot ping for this so you don't have to remember).
4. Once you've approved the PR, tell bors it's ok - you've been contributing for a while so you know how bors works, but here's a cheatsheet just in case: https://bors.rust-lang.org

Documentation about how to use bootstrap lives at https://rustc-dev-guide.rust-lang.org/building/bootstrapping.html; internal docs live in `src/bootstrap/README.md`. The latter unfortunately is not very complete.

---
## [enso-org/enso](https://github.com/enso-org/enso)@[4b7afbfd36...](https://github.com/enso-org/enso/commit/4b7afbfd3619c22b6b31f2840fa807f0af41fb57)
#### Monday 2023-05-15 18:16:00 by Ilya Bogdanov

Fix blank input port (#6614)

Fixes #6485

Conflicting requirements for the widget tree caused the issue:
1. The span tree node had a connection, and the text of the `number1` label was changed to white (as per the `Connected` color state)
2. The node configuration did not consider it a valid port because the span tree kind was `Operation`, which is not a port usually. So the port shape was not displayed, making the label blend with the node background.

I fixed the issue by considering the existence of the current connection for `Operation` nodes. Remember that it does not turn the node into a port, so after removing the connection, it's not possible to connect it back. That makes sense, in my opinion, as the resulting AST is invalid anyway. But at least we can see the label on the invalid node.


https://github.com/enso-org/enso/assets/6566674/23934966-8f72-4675-abe3-78a3f0c0cda4

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[d4e2137e45...](https://github.com/treckstar/yolo-octo-hipster/commit/d4e2137e45410bd072e10f8b95927742f6d59442)
#### Monday 2023-05-15 19:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [CleverRaven/Cataclysm-DDA](https://github.com/CleverRaven/Cataclysm-DDA)@[59c577e9f9...](https://github.com/CleverRaven/Cataclysm-DDA/commit/59c577e9f92bd3349312e254fa29d2bfcc84392f)
#### Monday 2023-05-15 19:46:22 by Karol1223

A bunch of random item reworks: 3 (#65532)

* boltcutters & chopsticks

* tin snips

* knitting needles

* silly notes

* hairbrush

* flags oh god the flags

* evil commas

* density list removal

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[77ae1b635a...](https://github.com/pytorch/pytorch/commit/77ae1b635a1dc18165775a1c682e5331416f2cf1)
#### Monday 2023-05-15 20:21:07 by Joel Schlosser

Update base for Update on "(WIP; DO NOT REVIEW) Use python tensor subclass version of NT for PT2"


I'm out next week so I'm dumping some stuff here for whoever is interested. Added some notes inline. Other things:
* Main idea: convert real NT -> fake / meta instance of `NestedTensor` python tensor subclass during tracing and use that throughout the rest of the PT2 stack
* Python tensor subclass only supports contiguous for now
    * Only need `sizes` because of this, and `sizes` is a dim-length list containing int / List[int] items (for ragged dims) OR SymInts for dynamic shapes (will probably only support this case anyway)
* Inference-only for now; ignore Autograd
* Skip functionalization on NTs for now (there's no in-place op support anyway, although we should ideally handle NT <-> T views within functionalization)

Example script:
```python
import torch
from torch.nested import nested_tensor
from torch.nested._nested_tensor import NestedTensor
from torch._inductor import debug

torch._inductor.config.debug = True
torch._dynamo.config.traceable_tensor_subclasses.add(NestedTensor)

device = 'cuda'

def make_tensor(*shape, device=device, dtype=torch.float32):
    return torch.randn(*shape, device=device, dtype=dtype)

torch.manual_seed(1)

def fn(x, x_offsets):
    x_nt = torch._nested_view_from_jagged(x, x_offsets)
    x_nt = x_nt + 69
    x_nt = x_nt * 42
    return x_nt

torch._dynamo.disallow_in_graph(torch.diff)

compiled_fn = torch.compile(fn)

# shape (sum(*), D)
# component shapes: (3, 5), (4, 5), (6, 5)
x = make_tensor(13, 5)
x_offsets = torch.tensor([0, 3, 7, 13], dtype=torch.int64, device=device)

# helps create dynamic graph right away
torch._dynamo.mark_dynamic(x, 0)
torch._dynamo.mark_dynamic(x_offsets, 0)

output = compiled_fn(x, x_offsets)

# shape (sum(*), D)
# component shapes: (2, 5), (6, 5), (4, 5), (5, 5)
y = make_tensor(17, 5)
y_offsets = torch.tensor([0, 2, 8, 12, 17], dtype=torch.int64, device=device)

output2 = compiled_fn(y, y_offsets)

print(output)
print(output2)
```

WARNING: AWFUL HACKS AHEAD. DO NOT REVIEW YET.

cc soumith voznesenskym penguinwu anijain2305 EikanWang jgong5 Guobing-Chen XiaobingSuper zhuhaozhe blzheng Xia-Weiwen wenzhe-nrv jiayisunx peterbell10 desertfire

[ghstack-poisoned]

---
## [yuiseki/evals](https://github.com/yuiseki/evals)@[170dfd886c...](https://github.com/yuiseki/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Monday 2023-05-15 21:09:25 by Robert Bateman

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
## [kwazedilla/Ion](https://github.com/kwazedilla/Ion)@[def6328a38...](https://github.com/kwazedilla/Ion/commit/def6328a3840de08ec4b1bdd22ce8d482210e205)
#### Monday 2023-05-15 21:45:48 by Astralchroma

Whoever decided to not set a default value for this, fuck you

---
## [shifucun/website](https://github.com/shifucun/website)@[60d93d54cc...](https://github.com/shifucun/website/commit/60d93d54cc21bc04c0f3e1c3435a76e3e74fe808)
#### Monday 2023-05-15 21:47:14 by Jehangir Amjad

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
## [Ademx1/ConsoleAppProject](https://github.com/Ademx1/ConsoleAppProject)@[1af6148f1e...](https://github.com/Ademx1/ConsoleAppProject/commit/1af6148f1e32bed23490424cb891e7b71021324c)
#### Monday 2023-05-15 21:55:46 by Adem Novruzlu

Deleted Implementations  

and I literally hate my life at this point ):

---
## [sjp38/linux](https://github.com/sjp38/linux)@[1f25f4701d...](https://github.com/sjp38/linux/commit/1f25f4701dad5099ef89db6d4206b4b912dc0d5a)
#### Monday 2023-05-15 23:22:06 by Douglas Anderson

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
## [JayGgit/JayGgit.github.io](https://github.com/JayGgit/JayGgit.github.io)@[145940547c...](https://github.com/JayGgit/JayGgit.github.io/commit/145940547c77e8ce6ca449e00ffffd8a9e7fccaa)
#### Monday 2023-05-15 23:31:00 by JayG

I didn't like that I did previous commit. Especially since I wrong a whole entire paragraph on the last commit's title. Anyways, I shouldn't do that on this commit. Wait, anyways... WAIT. I need to use another 30 seconds of GitHub actions :(. I'm now sad. Well, anyways, if you missed the title on the last commit, it was "Made the "I'm JayG" part not, you know... On on a second page on mobile. Why do people even visit my website??? Especially on mobile??? Huh... I will never know. Ughhhh. I need to use like 30 seconds on GitHub actions too. FOR ONE LINE OF CODE. :(((((( Anyways Happy Birthday Discord... Except I kinda want my perfered username, other then the fact that Discord CHANGED THE USERNAME SYSTEM. Wait, this is getting too long. For a GitHub commit too. Way too long title. Anyways, GitHub should really add a max character limit... Anyways, again. Goodbye :(". Yeah, very long. Super long

---

