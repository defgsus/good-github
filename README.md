## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-10](docs/good-messages/2023/2023-03-10.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,258,233 were push events containing 3,357,105 commit messages that amount to 253,169,228 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 62 messages:


## [linearcombination/DOC](https://github.com/linearcombination/DOC)@[3f23ada23b...](https://github.com/linearcombination/DOC/commit/3f23ada23b74fc17ce5af2fb1a12e8ea04f568c6)
#### Friday 2023-03-10 00:13:21 by linearcombination

Docx support and v1 UI candidate featuring basic and full uis (#91)

* Add initial proper docx support

Docx is the new preferred document output format as it is more easily
editable for translators.

This commit adds native docx support and an associated path for it in
the UI and backend as well as a test suite for it.

Supporting Docx meant adding a new code path that doesn't convert from
a finished HTML document to Docx in a wholesale fashion (in comparison
with conversion to PDF or ePub). Instead, the Docx is built up from
HTML snippets intermingled with required low-level Docx manipulations
to control one or two column layout and ultimately Docx template use
too. In turn this means that certain UI changes were necessary. The UI
changes include making the user choose either PDF, ePub, or Docx
rather than being able to choose all of them at once if desired. This
has the added benefit that a user can no longer choose to create three
different output formats in one go and thus the time for the request
to be fulfilled will be greatly reduced in such cases which will also
make the user feel the system is snappier (objectively, but more
importantly, subjectively).

Another UI change not directly related to Docx support is that we have
removed the drop down control to select chunking size. Instead, the UI
always sends chapter chunk size now and never verse chunking. Verse
chunking was decided to be of no value for translation purposes at
this time and verse interleaving is very costly in terms of
performance which makes for a bad UX. It can be resuscitated from git
history later if we want it back in the future though it is hard to
imagine now that happening.

Note too that Docx support does not include one of the layout options
available to HTML, PDF, and ePub: two column side by side languages.
This was never vetted as a needed requirement and has not been used or
requested for some time. It still exists as an option in HTML, PDF,
and ePub output formats as sort of a showcase for what can be done.
Also this layout would be much more difficult to implement in Docx.

This commit does not yet accommodate fonts for certain languages in
Docx format. To do so in Word will have to be the subject of a future
PR and appears to be of some complication. More research is needed.

There are also a few miscellaneous commits related to better naming,
a fix to configuration in docker-compose-override.yml, changing chunking
of several tests from the no longer used verse chunk size to chapter
chunk size instead, and remove commented out link in a Jinja HTML
template.

In a coming PR we will likely also want to ensure sources present no
linking in the generated doc. For now, for some sources, there are
some dead links in PDF, ePub, and Docx output formats. There is a
great deal of heterogeneity in links in the source. We successfully
handle tens of types, but there are apparently yet more that exist and
sometimes they are just malformed in the sources.

* Update non-docx assembly strategies interleaving order

Update the interleaving strategies for HTML, PDF, and ePub to follow
the order of interleaving that is implemented in the docx assembly
strategies which were designed to adhere to the product owner's latest
requirements updates as exemplified in a Word file that acts as
template. Specifically, book intro materials (TN and BC - BC wasn't
presented in the example, but intuition says it could follow TN book
intro) followed by USFM and footnotes, followed by chapter intro,
followed by verse-level translation notes, followed by other resource
assets (TQ, secondary USFM), and finally TW at language level. The old
order was book intros, chapter intro, USFM, verse-level TN notes, then
other remaining resource assets (with some variation).

* Update Makefile

* v1 UI candidate and full ui version both accessible and linked

- [x] basic version, i.e., v1, is available at #/v1/.

- [x] full version is available at #/

- [x] You can switch between them using a link in the About page of either

- [x] The Mast (the top area of the app where the logo and tab menu
  items live can be shown or hidden based on a bujild-time configuration
  setting in source at DOC/frontend/.env: VITE_SHOW_TOP_MATTER (which
  controls this for the full version) and
  VITE_SHOW_TOP_MATTER_IN_V1 (which controls this for the basic, v1,
  version). The usefulness of this comes into play if you want to, say,
  display the app without the Mast so as to integrate into an iframe
  within BIEL. If the app lives at its own link (with respect to
  navigation) then likely you would want the Mast kept in place.

- [x] Similarly, in the basic ui version, v1 candidate, there is a
  flag in the same .env file as above for showing or not showing
  resource types. We choose the approved USFM and TN types that are
  also listed in translations.json for the user. As such there is not
  a functional reason to show the resource types to the user. However, it
  likely a less surprising UX for the user if they are at
  least shown what resource types the system chose for them. The
  product owner will decide which option is best.

- [x] We didn’t yet actually have anything useful in the
  hamburger menu at the upper right in the Mast.  Thus, for now, I
  have disabled the ‘Hamburger ‘ menu in the top right of the Mast in
  both the basic and full UIs.

- [x] For now, the basic version, i.e., v1, defaults to PDF output.
  Why? Because many gateway languages use special fonts. As you
  likely recall from recent emails the handling of such fonts in
  Word document generation, especially for multi-language
  documents, is yet unsolved. I do have a lead on a couple
  approaches that may prove useful, but there is more work to be
  done there which will be the subject of a future PR or update to
  this PR if it has not yet been merged when I return to it.
  In the meantime, if you want to see the docx output for a gateway
  language simply switch to the full ui version (using the
  link in the About page or by manipulating the browser location URL
  to #/v1/) and request to generate Docx for said gateway language and
  view the result. For many gateway languages the result will be just
  fine, but for many which have special fonts you’ll get a document
  with fine structure (unless the underlying resource source assets
  are malformed or incomplete - this is true of many languages)
  but filled with unicode-font-missing boxes. Some backstory: Our PDF
  output comes from HTML that is rendered headless by webkit and the
  browser handles the fonts transparently (assuming they are installed
  into the environment the browser is running in), whereas with Docx
  generation things are more complicated.

    - [ ] What is likely going to be needed is a map of language to
      font needed for each language as well as the language’s
      identifying code (from
      Word’s perspective -probably an ANSI code or omething - see
      https://stackoverflow.com/questions/36967416/how-can-i-set-the-language-in-text-with-python-docx
      for example). For v1, we’ll only need that just for the gateway
      languages, but later for all languages. Hopefully there is a
      different less tedious way to solve this, but the link provided
      is the closest I have come so far as an approach that might work.
      With more time for researching it might turn out to be less
      onerous. Let's hope so.

- [ ] Other more minor items like font darkness/lightness, etc on
  various controls will get my attention before the deadline for
  launch.

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[6c978308c7...](https://github.com/lessthnthree/Skyrat-tg/commit/6c978308c71cbd5b24e3242aec42b227461f9aaa)
#### Friday 2023-03-10 00:13:23 by SkyratBot

[MIRROR] Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost [MDB IGNORE] (#19743)

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost (#73814)

## About The Pull Request

So we're like simultaneously moving two vague directions with research.
One being "experisci grants discounts for prohibitively expensive nodes
so you want to do the experiments to discount them" and the other being
"Let's give Heads of Staff a way to research anything they want without
any communication to the research department, including the very
expensive nodes that scientists may be working on"

You already see the issue, right? You can't have your cake and eat it
too.

It sucks for scientists to be working on a complex experiment like
weapons tech for that huge 90% discount only for the HoS to stumble onto
the bridge and research it anyways. Your time is wasted and RND is
slowed down massively.

We can do something to assuage that.

This PR makes it so completing an experiment which discounts already
completed nodes will refund a partial amount of the discount that
would've applied.

For example, researching industrial engineering without scanning the
iron toilets will refund ~5000 points.

This can only apply once per experiment, so if an experiment discounts
multiple technologies, they will only get a refund based on the first
technology researched.

## Why It's Good For The Game

This accomplishes the following:

- Expensive research nodes with difficult experiments remain expensive
without completing the experiments. If no one does the experiment, they
act the same as before.
- Expensive research nodes with very easy experiments (but time
consuming) no longer put RND on a time crunch to beat the itchy trigger
finger of the Heads of Staff. Stuff like scanning lathes allow the
scientists to work more at their own pace: they can talk to people or
maybe stop at the bar or kitchen between departments without feeling
pressure to get it done urgently.
- Scientists are able to complete experiments which previously were no
longer deemed relevant if they need a point injection. Experiments left
behind are no longer completely useless bricks. Maybe even gives
latejoin scientists something to do.
- Scientists mid experiment can still complete it to not feel like their
time is wasted.

Overall I think this has many benefits to the current science system
where many have complaints.

## Changelog

:cl: Melbert
qol: Completing an experiment which discounts a researched tech node
will give a partial refund of the discount lost. For example,
researching the industrial engineering research without scanning iron
toilets will refund ~5000 points if you complete it afterwards. This
only applies once per experiment, so experiments which discount multiple
nodes only refund the first researched.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [TheWolfbringer/tgstation](https://github.com/TheWolfbringer/tgstation)@[8ab74525c1...](https://github.com/TheWolfbringer/tgstation/commit/8ab74525c1c3c09a7605fead3ab013d29f24d07f)
#### Friday 2023-03-10 00:19:04 by itseasytosee

Brings the monkey back down (body horror edition/addition.) (#73325)

## About The Pull Request
Let me paint you a story.
A long time ago monkeys once rested their feet on the floor, this was a
time of bliss and peace. But sometime around the horrors of making
monkeys subtypes of humans did an atrocity occur.

![image](https://user-images.githubusercontent.com/55666666/217657059-5c960ab4-c3de-493c-ac12-28de99b43d7f.png)
**The monkeys were moved up.**
I thought this was bad, and alot of people on the forum tended to agree
with me

![image](https://user-images.githubusercontent.com/55666666/217657707-120354c7-b1a5-4d93-8813-8e10e142bd92.png)
This was do to some purpose of adjusting them so it could be easier to
fit item sprites onto them instead of preforming the hours of work
refractoring to make the heights of the items dynamic and adjustable. A
simple pixel shift may have sufficed, but you see, such a change would
NEVER allow the frankensteining of monkey and human features together.
This is that refractor.

In essence, the following is now true.
A top_offset can now be generated for a human based on a varible on
their chest and legs. By default, and as is true with human legs and
chests, this variable is ZERO by default. Monkey legs and chest have
NEGATIVE values proportionate and onto how much smaller their sprite is
compared to humans. Other bodyparts, as well as any other accociated
overlays, or clothing will automatically be offset to this axis. THIS
MEANS THAT MONKEYS ARE ON THE FLOOR. But is means something else too.
Something more freakish,


![image](https://user-images.githubusercontent.com/55666666/217659439-bc0b1a35-76c8-4490-b869-770180605822.png)
**What abominable monsters**, unreachable by players as long as we can't
stitch monkeys and humans together (oh but just wait until the feature
freeze ends)
Oh but you might be thinking, if legs can make a mob go down.
can it make a mob

**go**
**up??**

**OH NO**


![image](https://user-images.githubusercontent.com/55666666/217707042-0d53022f-d93a-4262-a5ce-ef15a99eb897.png)

![image](https://user-images.githubusercontent.com/55666666/217707060-779f5901-ab90-4a64-9ca7-0b147e24f099.png)

![image](https://user-images.githubusercontent.com/55666666/217707821-23d7457c-5881-40ae-8d9d-c9fbd645aba6.png)

These lads are stepping, and have been implemented solely for proof of
concept as a way to flex the system I have created and remain
inaccessible without admin intervention.

But really, when all is said and done, all this PR does in terms of
player facing changes is move the monkey back down.

![image](https://user-images.githubusercontent.com/55666666/217708365-b6922a6d-08d0-4267-8713-4f8dac29038e.png)
Oh and fixed monkey husked which have been broken for who knows how
long.

![image](https://user-images.githubusercontent.com/55666666/217708464-5a9b6f89-4223-4ae5-a21e-3a274a9f8db8.png)
## Why It's Good For The Game
The monkey is restored to its original position. Tools now exist to have
legs and torsos of varying heights. Monkey Husking is fixed.
## Changelog
:cl: itseasytosee
fix: Monkeys ues the proper husk sprites.
imageadd: The monkey has been moved back down to its lower, more
submissive position.
refactor: Your bodyparts are now dynamically rendered at a height
relevant to the length of your legs and torso, what does this mean for
you? Not much to be honest, but you might see a monkey pop up a bit if
you cut its legs off.
admin: The Tallboy is here
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [TheWolfbringer/tgstation](https://github.com/TheWolfbringer/tgstation)@[d55ce0f0bc...](https://github.com/TheWolfbringer/tgstation/commit/d55ce0f0bcb6c37113c9ec9f0e37facd99b69625)
#### Friday 2023-03-10 00:19:04 by Jacquerel

Don't create abandoned airlocks with walls underneath them. (#73656)

## About The Pull Request
Fixes #71504

#70237 attempted to remove this and did in some cases, however the case
where the abandoned airlock is able to find an adjacent wall turf to
copy the type of still fails to delete the airlock.
This fixes that.

Also in my testing, the times where it _failed_ to find a nearby wall
turf to copy and spawned a default wall would leave the mapping helper
visible in the round. Oops!

## Why It's Good For The Game

Mapping helpers should always delete themselves when finished.
The airlocks with walls under them are funny once and annoying the rest
of the time. As of that older PR, this continuing to happen is regarded
as a bug.
Also apparently it might be required anyway for Wallening.

## Changelog

:cl:
fix: Maintenance tunnels should no longer sometimes contain airlocks
with walls underneath them.
/:cl:

---
## [cceyda/argilla](https://github.com/cceyda/argilla)@[4c5f51377e...](https://github.com/cceyda/argilla/commit/4c5f51377e374fb30649bdc7b9a3291db21c5bb8)
#### Friday 2023-03-10 00:21:37 by Tom Aarsen

Use `rich` for logging, tracebacks, printing, progressbars (#2350)

Closes #1843

Hello!

## Pull Request overview
* Use [`rich`](https://github.com/Textualize/rich) for logging,
tracebacks, printing and progressbars.
* Add `rich` as a dependency.
* Remove `loguru` as a dependency and remove all mentions of it in the
codebase.
* Simplify logging configuration according to the logging documentation.
* Update logging tests.

## Before & After
[`rich`](https://github.com/Textualize/rich) is a large Python library
for very colorful formatting in the terminal. Most importantly (in my
opinion), it improves the readability of logs and tracebacks. Let's go
over some before-and-afters:
<details><summary>Printing, Logging & Progressbars</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219089678-e57906d3-568d-480e-88a4-9240397f5229.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219089826-646d57a6-7e5b-426f-9ab1-d6d6317ec885.png)

Note that for the logs, the repeated information on the left side is
removed. Beyond that, the file location from which the log originates is
moved to the right side. Beyond that, the progressbar has been updated,
ahd the URL in the printed output has been highlighted automatically.

</details>

<details><summary>Tracebacks</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219090868-42cfe128-fd98-47ec-9d38-6f6f52a21373.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219090903-86f1fe11-d509-440d-8a6a-2833c344707b.png)

---

### Before:

![image](https://user-images.githubusercontent.com/37621491/219091343-96bae874-a673-4281-80c5-caebb67e348e.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219091193-d4cb1f64-11a7-4783-a9b2-0aec1abb8eb7.png)

---

### Before

![image](https://user-images.githubusercontent.com/37621491/219091791-aa8969a1-e0c1-4708-a23d-38d22c2406f2.png)

### After

![image](https://user-images.githubusercontent.com/37621491/219091878-e24c1f6b-83fa-4fed-9705-ede522faee82.png)

</details>

## Notes
Note that there are some changes in the logging configuration. Most of
all, it has been simplified according to the note from
[here](https://docs.python.org/3/library/logging.html#logging.Logger.propagate).
In my changes, I only attach our handler to the root logger and let
propagation take care of the rest.

Beyond that, I've set `rich` to 13.0.1 as newer versions experience a
StopIteration error like discussed
[here](https://github.com/Textualize/rich/issues/2800#issuecomment-1428764064).

I've replaced `tqdm` with `rich` Progressbar when logging. However, I've
kept the `tqdm` progressbar for the [Weak
Labeling](https://github.com/argilla-io/argilla/blob/develop/src/argilla/labeling/text_classification/weak_labels.py)
for now.

One difference between the old situation and now is that all of the logs
are displayed during `pytest` under "live log call" (so, including
expected errors), while earlier only warnings were shown.

## What to review?
Please do the following when reviewing:
1. Ensuring that `rich` is correctly set to be installed whenever
someone installs `argilla`. I always set my dependencies explicitly in
setup.py like
[here](https://github.com/nltk/nltk/blob/develop/setup.py#L115) or
[here](https://github.com/huggingface/setfit/blob/78851287535305ef32f789c7a87004628172b5b6/setup.py#L47-L48),
but the one for `argilla` is
[empty](https://github.com/argilla-io/argilla/blob/develop/setup.py),
and `pyproject.toml` is used instead. I'd like for someone to look this
over.
2. Fetch this branch and run some arbitrary code. Load some data, log
some data, crash some programs, and get an idea of the changes.
Especially changes to loggers and tracebacks can be a bit personal, so
I'd like to get people on board with this. Otherwise we can scrap it or
find a compromise. After all, this is also a design PR.
3. Please have a look at my discussion points below.

## Discussion
`rich` is quite configurable, so there's some changes that we can make
still.
1. The `RichHandler` logging handler can be modified to e.g. include
rich tracebacks in their logs as discussed
[here](https://rich.readthedocs.io/en/latest/logging.html#handle-exceptions).
Are we interested in this?
2. The `rich` traceback handler can be set up to include local variables
in its traceback:
<details><summary>Click to see a rich traceback with local
variables</summary>


![image](https://user-images.githubusercontent.com/37621491/219096029-796b57ee-2f1b-485f-af35-c3effd44200b.png)
    </details>
Are we interested in this? I think this is a bit overkill in my opinion.
3. We can suppress frames from certain Python modules to exclude them
from the rich tracebacks. Are we interested in this?
4. The default rich traceback shows a maximum of 100 frames, which is a
*lot*. Are we interested in reducing this to only show the first and
last X?
5. The progress bar doesn't automatically stretch to fill the full
available width, while `tqdm` does. If we want, we can set `expand=True`
and it'll also expand to the entire width. Are we interested in this?
6. The progress "bar" does not need to be a bar, we can also use e.g. a
spinner animation. See some more info
[here](https://rich.readthedocs.io/en/latest/progress.html#columns). Are
we interested in this?

---

**Type of change**

- [x] Refactor (change restructuring the codebase without changing
functionality)

**How Has This Been Tested**

I've updated the tests according to my changes.

**Checklist**

- [x] I have merged the original branch into my forked branch
- [ ] I added relevant documentation
- [x] follows the style guidelines of this project
- [x] I did a self-review of my code
- [x] I added comments to my code
- [ ] I made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works

- Tom Aarsen

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[11aab72dc9...](https://github.com/pytorch/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Friday 2023-03-10 00:33:05 by Driss Guessous

[SDPA] Add an optional scale kwarg (#95259)

# Summary
This PR adds an optional kwarg to torch torch.nn.functional.scaled_dot_product_attention()
The new kwarg is a scaling factor that is applied after the q@k.T step of the computation. Made updates to the efficient kernel to support but flash and math were minimally updated to support as well.

Will reduce the complexity of: #94729 and has been asked for by a couple of users.

# Review Highlights
- As far as I know I did this the correct way and this both BC and FC compliant. However I always seem to break internal workloads so I would love if someone can advice I did this right?
- I named the optional arg 'scale'. This is probably dumb and I should name it 'scale_factor'. I will make this change but this is annoying and it will require someone thinking we should rename.
- 'scale' is interpreted as `Q@K.T * (scale)`

Pull Request resolved: https://github.com/pytorch/pytorch/pull/95259
Approved by: https://github.com/cpuhrsch

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[32c31b8fc0...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/32c31b8fc08aaec64dfc0583e02ed55b193ffa19)
#### Friday 2023-03-10 01:23:48 by SkyratBot

[MIRROR] Lighting source refactor (Tiny) [MDB IGNORE] (#19370)

* Lighting source refactor (Tiny) (#73284)

## About The Pull Request

I'm doing two things here. Let's get the boring bit out of the way.

Lighting source updates do three distinct things, and those things were
all in one proc.
I've split that one proc into three, with the first two feeding into the
third.

Second, more interesting thing.

An annoying aspect of our lighting system is the math we use for
calculating luminosity is hardcoded.
This means that we can't have subtypes that are angled, or that have
squared falloff, etc. All has to look the same.
This sucks, and it shows.

It has to be, goes the thinking, because we need very fast lookups that
OOP cannot provide.
We can't bog down the main equation with fluff, because the main
equation needs to be really speedy.

The thing about this equation is the only variants on a turf to turf
basis is exactly how far turfs are from the center.
So what if, instead of doing the math in our corner worker loop, we
build lookup tables to match our current source's state.
The tables, like a heatmap, could encode the lighting of any point along
the line.

This is actually faster then doing the math each time, because the list
generation can be cached.
It also means we've pulled the part we want to override out of hotcode.
It's cheap to override now, and a complex subtype, with angles and such
would have no impact on the typical usage.

So the code's faster, easier to read, and more extensible.
And we can do stuff like squared falloff for some lights in future
without breaking others.

Winning!

## Why It's Good For The Game

Winning

* Lighting source refactor (Tiny)

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[9e981753ca...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/9e981753ca16ea6f527f1ce26ee5cbc044ad80c7)
#### Friday 2023-03-10 01:23:48 by SkyratBot

[MIRROR] Reworked PDA menu & NtOS themes [MDB IGNORE] (#19390)

* Reworked PDA menu & NtOS themes (#73070)

## About The Pull Request

This is a port/rework of
https://github.com/yogstation13/Yogstation/pull/15735 - I changed a lot
of how it acted (some themes are locked behind maintenance apps).

The original author allowed this port to happen, and I really liked how
it looked there so I'd like to add it here.

### Applications

Removes the hardware configurator application, as all it did was show
you your space and battery now that all hardware was removed. These are
things your PC does by default, so it was just a waste of space.
Adds a Theme manager application instead, which allows you to change
your PDA's theme at will.
Adds a new Maintenance application that will give a new theme, however
it will also increase the size of the theme manager app itself as it's
bloatware.

### Menu

There's now a bar at the top of the menu showing 'special' tablet apps
which, for one reason or another, should stand out from the rest of the
apps. Currently this is PDA messenger and the Theme manager

Flashlight and Flashlight color is now only an icon, and is shown on the
same line as Updating you ID

https://cdn.discordapp.com/attachments/961874788706574386/1069621173693972551/2023-01-30_09-10-52.mov

![image](https://user-images.githubusercontent.com/53777086/215501361-5ea3086e-2ff5-4ab1-bde4-8a3d14014fce.png)

### Themes

Adds a lot of themes to choose from, although SOME are hidden behind
Maintenance applications, which will give you a random theme. These are
bloatware however, so they come with some extra cost to the app's
required space storage.

Themes are now supported on ALL APPLICATIONS! If you have a computer
theme, you will have that theme in EVERY app you enter, rather than just
a select few.
ALSO also, emagging the tablet will automatically set & unlock the
Syndicate theme, which makes your PDA obvious but you can disguise it if
you wish through just re-painting it to something else.

https://cdn.discordapp.com/attachments/828923843829432340/1069565383155122266/2023-01-30_05-29-53.mov

### Preferences

This also adds a pref for theme, reworking the ringtone code to work
with it as well. I also removed 2 entirely unused PDA prefs just 'cause.

Screenshot not up-to-date, they now have proper names.

![image](https://user-images.githubusercontent.com/53777086/215463669-0fe9951a-71f8-4b71-a97d-b79b5a2f945a.png)

### Other stuff

Made defines for device_themes
Added support for special app-side checks to download files
Fixed programs downloading themselves TWICE because defines all had the
same definition
Removes the Chemistry computer disk as it was empty due to chemistry
app's removal
Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
Moved over and added better documentation on data computer files, and
moved the ordnance ones to the same file as the others.

## Why It's Good For The Game

It makes PDAs a lot more customizable while adding more features to
maintenance applications. I think the themes look cool and it fits with
PDAs being "personal" anyways.

I also explained most of my other arguments in the about section, such
as the hardware configuration application.

## Changelog

:cl: Chubbygummibear & JohnFulpWillard
add: A ton of new NtOS themes, which are accessible by the new Themify
application that comes with all PCs.
add: Emagging a PC now defaults it to the Syndicate option (and adds it
to go back to it if you wish)
add: There's a new maintenance app that gives you rarer themes
qol: The NtOS Main menu was moved around, added "header" applications
that are shown where the Flashlight is, such as your Theme manager and
PDA messenger.
code: Made defines for device_themes
code: Added support for special app-side checks to download files
code: Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
fix: Programs no longer download twice.
del: Removes the Chemistry computer disk as it was empty due to
chemistry app's removal
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Reworked PDA menu & NtOS themes

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[26688597e3...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/26688597e317b30cdad644954c2f4654afec2b97)
#### Friday 2023-03-10 01:23:48 by Rimi Nosha

[MODULAR] [MDB IGNORE] Dim Lighting Some More, Removes Egregious Lighting Varedits in Interlink, Dynamically Calculate Night Shift Light Brightness and Color (#19039)

* Boom.

* Oop

* Fuck off single letter vars

* Fingers crossed.

* IT WORKS

* Adjust funny numbers

* Update a comment

---
## [DutKulang/LEAD](https://github.com/DutKulang/LEAD)@[cde04bc0a0...](https://github.com/DutKulang/LEAD/commit/cde04bc0a0ceab8521e5e419e1e3519abd4a44bb)
#### Friday 2023-03-10 01:29:26 by Dawa Edina Hillary

Proposed changed for Sida's profile

---
layout: profile
title:  "Sida Lillian"
image: "assets/images/profiles/Sida-Lillian/Sida-Lillian.jpg"
country: Uganda
region: West Nile
hub: CC4D
languages: "English (Fluent spoken and written), Bari/Kakwa (Fluent spoken and spoken), Arabic (good spoken only), Lugbara (fair spoken only)"
mail: sidalilian@proton.me
phone: "+256782739162"
whatsapp: 
website: 
telegram: "+256782739162"
github: github.com/sidalillian
linkedin: 
twitter: 
facebook: https://www.facebook.com/profile.php?id=100074066215635
instagram: 
mastodon: 
wikifab:
skills:
  - {name: Web & Software, number: 1, qualification: "using platforms, basic social media experiences, software download and installation \n \n
     * [Sida Lilian was trained on social media skills during the #ASKnet training in 2018](https://m.facebook.com/story.php?story_fbid=303135693607634&id=100017336164583) "}
  - {name: Community & Moderation, number: 2, qualification: "connecting people, trauma healing, event facilitation and meditation \n \n 
     * Certificate of participation in trauma healing& meditation training \n
     * She was trained and facilitated a post training on how to use Condoms under the #ASKnet project 2018"}
  - {name: Data Security & Research, number: 3, qualification: "data collection and protection of personal data \n \n 
     * Certificate in data collection"}

---

Sida Lilian is a female South Sudanese refugee in Uganda.

Expert in data collection, trauma healing, mediation, event facilitation of different types.

She was trained on how to collect both qualitative and quantitative data by REACH Uganda, Danish Refugee Council, Norwegian Refugee Council Uganda and GROUND TRUTH SOLUTIONS, she was also trained and worked as frontline worker on the *BOOST FOR THE YOUNGEST by Save The Children under Dubai Cara not only that she was also trained on Social Enterprise online by Makerere University - Canada in 2018, she was trained and worked as hygiene Promoter by CEFORD Uganda and was also trained and worked as Community Development Worker (CDW) by Danish Refugee Council.

She is confident, talented and determined to transform her community.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[6ebdfdc73f...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/6ebdfdc73f233d94bcc6c4a2f72d902af868583f)
#### Friday 2023-03-10 01:41:23 by SkyratBot

[MIRROR] Makes Shake() proc work [MDB IGNORE] (#19424)

* Makes Shake() proc work (#73480)

## About The Pull Request

Fixes #72321
Fixes #70388

The shake proc didn't work and hasn't for ages.
I remember it having worked at some point, but it was quite a long time
ago.
I cannot guarantee that the end result here is the same as it was, the
reason here being that I have no idea how this proc ever worked in the
first place. My limited understanding of the `animate` proc implies that
the previous implementation as written would never have acted as you
would expect it to, but clearly at some time in the past it did work. A
mystery.

As a result of the previous, possibly because the proc never _did_ work
as expected and just did something which looked vaguely correct most of
the time, both the default values and the values people were passing
into this proc were completely ridiculous.
Why would anyone ever want to pixel shift an object with a range of _15_
pixels in all directions? That's half a full tile! And why would you
want it to do this for 25 seconds?
So I also changed the values being passed in, because you really want
pretty small numbers passed into here most of the time.

Here's a video of everything that vibrates:
https://www.youtube.com/watch?v=Q0hoqmaXkKA

The exception is the v8 engine. I left this alone because it seems to
try and start shaking while in your hands, which doesn't work, and I
don't know how to fix that. This has potentially _also_ never worked.

## Why It's Good For The Game

Now you can see intended visual indicators for:
- Lobstrosities charging.
- Beepsky being EMPed.
- The Savannah Ivanov preparing to jump.
- The DNA infuser putting someone through the spin cycle.
- The mystery box admin item I had no previous idea even existed (fun
animations on this one).
- Anything else which wants to use this proc to create vibrating objects
in the future.

## Changelog

:cl:
fix: Lobstrosities and Tarantulas will once more vibrate to let you know
they're about to charge at you.
fix: The Savannah Ivanov will once more vibrate to let you know it's
about to jump into the air.
fix: The DNA infuser will now vibrate to let people know that it's busy
blending someone with a dead animal.
/:cl:

* Makes Shake() proc work

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [catapultam-habeo/pyrelight-server](https://github.com/catapultam-habeo/pyrelight-server)@[a3d9869f1c...](https://github.com/catapultam-habeo/pyrelight-server/commit/a3d9869f1c62ee3fc7ec1388e0934ec2a182a0c2)
#### Friday 2023-03-10 01:54:25 by catapultam-habeo

fix bank delete bug

finish cleaning up bank bag bug

lol kill me

sigh this is tiresome

fuck this

wtf is this

bah

bah

try this

bah

fuck this.

so angry

so tired ofthis shit

test

test?

---
## [Libertus-Lab/issrc](https://github.com/Libertus-Lab/issrc)@[118c151654...](https://github.com/Libertus-Lab/issrc/commit/118c15165401bb2acb62358f963777c44fb9c582)
#### Friday 2023-03-10 02:53:56 by Johannes Schindelin

Prevent `comctrl32.dll` from being inadvertently side-loaded

When running an installer from the Downloads folder, we do not trust any
file in that folder apart from the installer itself.

However, the way we need to mention `comctl32.dll` in the manifest
(because we want to use version 6, which cannot be simply loaded like
all the other `.dll` files because we would then end up with version 5)
unfortunately lets Windows look for a DLL side-load payload next to the
executable.

Now, it is relatively hard for a hacker to social-engineer their way to
a `<installer>.exe.Local` folder that contains the exact right subfolder
that then contains a usable (but maliciously-crafted) `comctl32.dll`.

However, we should prevent this if possible.

And it _is_ possible because we're copying the installer into a
temporary directory before spawning it there _anyway_, and before that
we do not need any visual styles, therefore we're plenty fine with using
`comctl32.dll` version 5 until that point.

So let's do this: modify the manifest of the installer (but not of its
compressed payload) so that it prevents DLL side-loading of
`comctl32.dll`.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [TurtleShroom/TSP_STORYTIME_RIDES_AGAIN](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN)@[f9cc7b6700...](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN/commit/f9cc7b670032700b71061303f8b07e52f8b47d24)
#### Friday 2023-03-10 03:07:56 by TURTLESHROOM

ANTI-HARRY POTTER ACTION

READ ANOTHER BOOK. (Ha ha. I hate "Harry Potter". I read the first book in the second grade and despised it.)

1. Reintroduced the Bean Roulette. It no longer has stupid HP references. I fixed the Spiked Butterscotch that way, too.
 (The only good references are Horcruxes and anything HP-related in "Grim Adventures of Billy and Mandy", such as Lord Moldy Butt.)

2. Isengriff doesn't know how to use Patches and MAYREQUIRE qualifiers, because he has the MOHAR Framework unlisted as a Dependency on his Mod's page. You no longer need that Mod to run the Storytime Mod, but the Bean Roulette doesn't work without it.

---
## [HackerN64/HackerSM64](https://github.com/HackerN64/HackerSM64)@[ef38abb1c0...](https://github.com/HackerN64/HackerSM64/commit/ef38abb1c0c2b39536e2a1a04003bc10556f5cb1)
#### Friday 2023-03-10 03:39:28 by Fazana

Frustratio funny fix 2 (#593)

* Update game_init.c

* fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo

---
## [BryceStevenWilley/docassemble-stubs](https://github.com/BryceStevenWilley/docassemble-stubs)@[0c9f7f9070...](https://github.com/BryceStevenWilley/docassemble-stubs/commit/0c9f7f9070675688d0d3453726af752d72b30431)
#### Friday 2023-03-10 04:12:02 by Bryce Willey

Got base stubtest working.

`stubtest --allowlist base_allowlist.txt docassembel.base`.

Also tried to get docassemble.webapp generated and working;
can successfully generated stubs for webapp, but can't do any stubtests
on it, making it a larger maintaince burden.

* everything eventually tries to call `docassemble.base.config.load()`,
  which calls `sys.exit(1)` if it can't load `/usr/share/docassemble/config.yml`,
  which is kinda ridiculous. With some hacking, we can skip it (consider contributing
  upstream to mypy, at least it shouldn't silently just shut down)
* watchdog.py loops forever without a `__main__` section, there's no avoiding that
  without updating docassemble upstream, something that Jonathan might be wary
  of, given this is mostly for type stuff, something he doesn't really want
  changes for.

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[ca1f89de03...](https://github.com/ARF-SS13/coyote-bayou/commit/ca1f89de03d088d262cef2bdbfffdeb29be909e1)
#### Friday 2023-03-10 04:13:36 by Tk420634

Mobn't

Removes some mobs to get us away from the ram limit some.

Fuck you ram limit, all my homies hate 32 bit software.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[7305d12d29...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/7305d12d29a89675b1fdee325e7b846576591624)
#### Friday 2023-03-10 04:17:24 by lessthanthree

[MANUAL MIRROR] Nightvision Rework (In the name of color) (#19608)

* Nightvision Rework (In the name of color) (#73094)

Relies on #72886 for some render relay expansion I use for light_mask
stuff.

Hello bestie! Night vision pissed me off, so I've come to burn this
place to the ground.
Two sections to discuss here. First we'll talk about see_in_dark and why
I hate it, second we'll discuss the lighting plane and how we brighten
it, plus introducing color to the party.

https://www.byond.com/docs/ref/#/mob/var/see_in_dark

See in dark lets us control how far away from us a turf can be before we
hide it/its contents if it's dark (not got luminosity set)
We currently set it semi inconsistently to provide nightvision to mobs.

The trouble is stuff that produces light != stuff that sets luminosity.
The worst case of this can be seen by walking out of escape on icebox,
where you'll see this

![image](https://user-images.githubusercontent.com/58055496/215683654-587fb00f-ebb8-4c83-962d-a1b2bf429c4a.png)

Snow draws above the lighting plane, so the snow will intermittently
draw, depending on see_in_dark and the luminosity from tracking lights.
This would in theory be solvable by modifying the area, but the same
problem applies across many things in the codebase.
As things currently stand, to be emissive you NEED to have a light on
your tile. People are bad at this, and honestly it's a bit much to
expect of them. An emissive overlay on a canister shouldn't need an
element or something and a list on turfs to manage it.
This gets worse when you factor in the patterns I'm using to avoid
drawing lights above nothing, which leads to lights that should show,
but are misoffset because their parent pixel offsets.

It's silly. We do it so we can have things like mesons without just
handing out night vision, but even there the effect of just hiding
objects and mobs looks baddddddd when moving. It's always bothered me.
I'll complain about mesons more later, but really just like, they're too
bright as it is.

I'm proposing here that rather then manually hiding stuff based off
distance from the player, we can instead show/hide using just the
lighting plane. This means things like mesons are gonna get dimmer, but
that's fine because they suck.

It does have some side effects, things like view() on mobs won't hide
stuff in darkness, but that's fine because none actually thinks about
view like that, I think.

Oh and I added a case to prevent examining stuff that's in darkness, and
not right next to you when you don't have enough nightvision, to match
the old behavior `see_in_dark` gave us.

Now I'd like to go on a mild tangent about color, please bare with me

You ever walk around with mesons on when there's a fire going, or an
ethereal or firelocks down.
You notice how there isn't really much color to our lights? Doesn't that
suck?

It's because the way we go about brighting lighting is by making
everything on the lighting plane transparent.
This is fine for brightening things, but it ends up looking kinda crummy
in the end and leads to really washed out colors that should be bright.
Playing engineer or miner gets fucking depressing.

The central idea of this pr, that everything else falls out of, is
instead of making the plane more transparent, we can use color matrixes
to make things AT LEAST x bright.

https://www.byond.com/docs/ref/#/{notes}/color-matrix

Brief recap for color matrixes, fully expanded they're a set of 20
different values in a list
Units generally scale 0-1 as multipliers, though since it's
multiplication in order to make an rgb(1,1,1) pixel fullbright you would
need to use 255s.

A "unit matrix" for color looks like this:
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0, 0, 0, 0
)
```

The first four rows are how much each r, g, b and a impact r, g, b and
well a.
So a first row of `(1, 0, 0, 0)` means 1 unit of r results in 1 unit of
r. and 0 units of green, blue and alpha, and so on.
A first row of `(0, 1, 0, 0)` would make 1 red component into 1 green
component, and leave red, blue and alpha alone, shifting any red of
whatever it's applied to a green.

Using these we can essentially color transform our world. It's a fun
tool. But there's more.

That last row there doesn't take a variable input like the others.
Instead, it ADDS some fraction of 255 to red, green, blue and alpha.

So a fifth row of `(1, 0, 0, 0)` would make every pixel as red as it
could possibly be.

This is what we're going to exploit here. You see all these values
accept negative multipliers, so we can lower colors down instead of
raising them up!
The key idea is using color matrix filters
https://www.byond.com/docs/ref/#/{notes}/filters/color to chain these
operations together.

Pulling alllll the way back, we want to brighten darkness without
affecting brighter colors.
Lower rgb values are darker, higher ones are brighter. This relationship
isn't really linear because of suffering reasons, but it's good enough
for this.
Let's try chaining some matrixes on the lighting plane, which is bright
where fullbright, and dark where dark.

Take a list like this

```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     -0.2, -0.2, -0.2, 0
)
```
That would darken the lighting a bit, but negative values will get
rounded to 0
A subsequent raising by the same amount
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.2, 0.2, 0.2, 0
)
```
Will essentially threshold our brightness at that value.
This ensures we aren't washing out colors when we make things brighter,
while leaving higher values unaffected since they basically just had a
constant subtracted and then readded.

You may have noticed, we gain access to individual color components
here.
This means not only can we darken and lighten by thresholds, we can
COLOR those thresholds.
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.1, 0.2, 0.1, 0
)
```
Something like the above, if applied with its inverse, would tint the
darkness green.
The delta between the different scalars will determine how vivid the
color is, and the actual value will impact the brightness.

Something that's always bothered me about nightvision is it's just
greyscale for the most part, there isn't any color to it.
There was an old idea of coloring the game plane to match their lenses,
but if you've ever played with the colorblind quirk you know that gets
headachey really fast.
So instead of that, lets color just the darkness that these glasses
produce.
It provides some reminder that you're wearing them, instead of just
being something you forget about while playing, and provides a reason to
use flashlights and such since they can give you a clearer, less tinted
view of things while retaining the ability to look around things.

I've so far applied this pattern to JUST headwear for humans (also those
mining wisps)
I'm planning on furthering it to mobs that use nightvision, but I wanted
to get this up cause I don't wanna pr it the day before the freeze.

Mesons are green, sec night vision is red, thermals orange, etc.

I think the effect this gives is really really nice.
I've tuned most things to work for the station, though mesons works for
lavaland for obvious reasons.

I've tuned things significantly darker then we have them set currently,
since I really hate flat lighting and this system suffers when
interacting with it.

My goal with these is to give you a rough idea of what's around you,
without a good eye for detail.
That's the difference between say, mesons, and night vision. One helps
you see outlines, the other gives you detail and prevents missing
someone in the darkness.

It's hard to balance this precisely because of different colored
backgrounds (looking at you icebox)
More can be done on this front in future but I'm quite happy with things
as of now

I have since expanded to all uses of nightvision, coloring most all of
them.

Along the way I turned some toggleable nightvision into just one level.
Fullbright sucks, and I'd rather just have one "good" value.

I've kept it for a few cases, mostly eyes you rip out of mobs.
Impacted mobs are nightmares, aliens, zombies, revenants, states and
sort of stands.

I've done a pass on all mobs and items that impact nightvision and added
what I thought was the right level of color to them. This includes stuff
like blobs and shuttle control consoles
As with glasses much of this was around reducing vision, though I kept
it stronger here, since many of these mobs rely on it for engaging with
the game

<details>
<summary>
Technical Changes
</summary>

filter transitions.
Found this when testing this pr, seemed silly.

This avoids dumbass overlay lighting lighting up wallmounts.
We switch modes if some turfflags are set, to accomplish the same thing
with more overhead, and support showing things through the darkness.

Also fixes a bug where you'd only get one fullscreen object per mob, so
opening and closing a submap would take it away

Also also fixes the lighting backdrop not actually spanning the screen.
It doesn't actually do anything anymore because of the fullscreen light
we have, but just in case that's unsued.
Needs cleanup in future.

color with a sprite

This is to support the above
We relay this plane to lighting mask so openspace can like, have
lighting

vision goggles and such
Side affect of removing see_in_dark. This logic is a bit weak atm, needs
some work.

It's a dupe of the nightvision action button, and newly redundant since
I've removed all uses of it

trasnparent won't render

These sucked
Also transparent stuff should never render, if it does you'll get white
blobs which suck

</details>

Videos! (Github doesn't like using a summary here I'm sorry)
<details>

Demonstration of ghost lighting, and color

https://user-images.githubusercontent.com/58055496/215693983-99e00f9e-7214-4cf4-a76a-6e669a8a1103.mp4

Engi-glass mesons and walking in maint (Potentially overtuned, yellow is
hard)

https://user-images.githubusercontent.com/58055496/215695978-26e7dc45-28aa-4285-ae95-62ea3d79860f.mp4

Diagnostic nightvision goggles and see_in_dark not hiding emissives

https://user-images.githubusercontent.com/58055496/215692233-115b4094-1099-4393-9e94-db2088d834f3.mp4

Sec nightvision (I just think it looks neat)

https://user-images.githubusercontent.com/58055496/215692269-bc08335e-0223-49c3-9faf-d2d7b22fe2d2.mp4

Medical nightvision goggles and other colors

https://user-images.githubusercontent.com/58055496/215692286-0ba3de6a-b1d5-4aed-a6eb-c32794ea45da.mp4

Miner mesons and mobs hiding in lavaland (This is basically the darkest
possible environment)

https://user-images.githubusercontent.com/58055496/215696327-26958b69-0e1c-4412-9298-4e9e68b3df68.mp4

Thermal goggles and coloring displayed mobs

https://user-images.githubusercontent.com/58055496/215692710-d2b101f3-7922-498c-918c-9b528d181430.mp4

</details>

I think it's pretty, and see_in_dark sucks butt.

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
add: The darkness that glasses and hud goggles that impact your
nightvision (think mesons, nightvision goggles, etc) lighten is now
tinted to match the glasses. S pretty IMO, and hopefully it helps with
forgetting you're wearing X.
balance: Nightvision is darker. I think bright looks bad, and things
like mesons do way too much
balance: Mesons (and mobs in general) no longer have a static distance
you can see stuff in the dark. If a tile is lit, you can now see it.
fix: Nightvision no longer dims colored lights, instead simply
thresholding off bits of darkness that are dimmer then some level.
/:cl:

* modular edits

* see_in_dark

* [MIRROR] Adds a unit test to detect double stacked lights [MDB IGNORE] (#19564)

* Adds a unit test to detect double stacked lights

* we really need to get that night vision pr done

* lints fixes

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Paxilmaniac <paxilmaniac@gmail.com>

* Update augments_eyes.dm

* Update augments_eyes.dm

* eeee

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: SkyratBot <59378654+SkyratBot@users.noreply.github.com>
Co-authored-by: Paxilmaniac <paxilmaniac@gmail.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[01dbd227c2...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/01dbd227c28f039ab5afd02e5e14589a3351a395)
#### Friday 2023-03-10 05:10:53 by Gandalf

[MIRROR] Grand Ritual: Alternate Wizard objective (Wizard Events II) (#72918) [MANUAL MIRROR] (#19751)

* Grand Ritual: Alternate Wizard objective (Wizard Events II) (#72918)

Adds an alternate greentext objective for Wizards known as the "Grand
Ritual". This was initially the gimmick of a different wizard-related
antagonist downstream. I didn't get permission to port it, so I'm
attaching it to regular Wizards instead.

Wizards will spawn in with a new Grand Ritual button next to their
antagonist info button. Pressing it will pinpoint them towards their
next Ritual Location (a randomly chosen region of the space station).
Once within that location, pressing it will summon a magic circle and
obliterate any dense objects which are in the way. This also puts the
ability on a two minute cooldown.
Clicking on the magic circle with an empty hand will begin a three-stage
invocation to gather magical power. You can interrupt this invocation at
any time and will resume from the last stage you completed (if you
finished two stages you only need to do one more).
Once you complete a ritual, a random event will be triggered based on
how many rituals you have performed so far. These tend to be ones which
annoy the crew in some manner, and Wizard Events are included in the
list. Additionally, something weird will usually happen to the room you
are in.
Then you are assigned a new location and can toddle off to do it again.

Once you have done this three times, you will be picked up by the
station's sensors every time you start a subsequent ritual and should
expect annoyed company to come investigate.
Once you have done this six times, you can finally spend all of that
accumulated power on the seventh Grand Finale ritual. Completing this
grants you victory at the end of the round and will have a larger,
flashier effect which you can pick from a list of options, think of it
like a wizard equivalent of a Traitor Final Objective or Heretic
Ascension.
After that you can still keep doing rituals if you want to pester the
crew further by summoning more random events, you've already "won" at
this point so now it's your job to make them want to go home.

I think it'd be more fun to just find out what the Finale ritual can do
by seeing it happen but maintainers will probably want a list of its
precise capabilities, so here it is:

Currently completing a ritual also has a chance to create Heretic
Reality Tears (of both varieties, available for Heretics to eat and
visible to crew) as a kind of cross-antagonist interaction which seemed
to make sense to me but if this seems thematically or mechanically
inappropriate it's easy to strip out.

* wew

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [GraeDevs/morecreeps-1.12.2](https://github.com/GraeDevs/morecreeps-1.12.2)@[39c86d8d69...](https://github.com/GraeDevs/morecreeps-1.12.2/commit/39c86d8d69ae0d36493e66d5656b45fa5ef68efe)
#### Friday 2023-03-10 06:08:58 by Renk

Shrink Ray Implemented: Issues found

- When using the grow ray, then the shrink ray, the hitbox tends to not want to shrink anymore. But if used without the use of the grow ray, works perfectly fine. But, done vice verse, makes the hitbox wonky as shit when using a grow ray after a shrink ray has been used.
Not really sure how to fix that one.

---
## [BeZaBel/NeonCat](https://github.com/BeZaBel/NeonCat)@[1b33c6c70e...](https://github.com/BeZaBel/NeonCat/commit/1b33c6c70ecb2a7791ee6a8ad9552b816842d7e9)
#### Friday 2023-03-10 06:09:01 by BeZaBel

too many changes, I know this is a shit commit but I can't remember what the hell did I change

---
## [retlaw34/Shiptest](https://github.com/retlaw34/Shiptest)@[84a2a8f394...](https://github.com/retlaw34/Shiptest/commit/84a2a8f394a0296ecc527f23c0da470b30280c0c)
#### Friday 2023-03-10 06:47:26 by Bjarl

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
## [Vincemeister/Favolist](https://github.com/Vincemeister/Favolist)@[459eab5650...](https://github.com/Vincemeister/Favolist/commit/459eab56503c975eda828eab1ede8e25c35c2d15)
#### Friday 2023-03-10 06:57:00 by Vincent Rehms

improved the products feed, added the profile box section to usr show, made some more seeds, created the menu bar. tried to tweak bootsrap variables but fucked up. so manually set font-weights which sucks ass. will need to do this later

---
## [LemonInTheDark/daedalusdock](https://github.com/LemonInTheDark/daedalusdock)@[ae08395328...](https://github.com/LemonInTheDark/daedalusdock/commit/ae08395328672ee40c5abb7f2bd1452bb932d6d4)
#### Friday 2023-03-10 07:36:29 by san7890

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
## [LynxSolstice/cmss13](https://github.com/LynxSolstice/cmss13)@[34daca112c...](https://github.com/LynxSolstice/cmss13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Friday 2023-03-10 08:04:01 by Segrain

Fix for varediting bitflags. (#2735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

I am honestly at a loss as to what is happening here. I do not speak
HTML all too well, and at cursory reading buttons _should_ be returning
their value, which is `1`, `2` and so on. But on debugging, they
actually return their text (`Save`, `Cancel`), which does not proceed to
work with the code receiving it. Changed that code accordingly, and then
edited the values for good measure in case somebody better versed in
HTML would get a heart attack from my folly.

Also, this looks ugly to me. Which button is which flag here?

![image](https://user-images.githubusercontent.com/4447185/221438285-cdb380c2-a871-4620-be04-0b3c5027501f.png)

This, in my humble opinion, is easier to read (would actually look
better outside of local server messing fancy windows as is its wont):

![image](https://user-images.githubusercontent.com/4447185/221438302-660c5976-d0e2-44fa-a18a-9f73a229f2c4.png)
In the process, I confess, my HTML illiteracy broke a little something
again. But we are not actually _using_ `slidecolor`, so hopefully it is
not actually important.

# Explain why it's good for the game

Is fix.


# Testing Photographs and Procedure
See above.

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
admin: Editing bitflag variables actually works now.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[582f5b38cb...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/582f5b38cb9ad5d051cbea48af501089ba3f0206)
#### Friday 2023-03-10 08:34:22 by Lance

Holy FUCK temporary commit

Mixed between previous abno based spawning and new subsystem

Cleanup Commit

Removes a lot of previous code and paves the way for the subsystem method.

Major Commit

Apocalypse Bird drops it's loot and only spawns once. It'll not try to happen if there aren't enough birds, and if two are breached before the third arrives it'll take the third breaching to start the event, until the others are suppressed. Birds do not target people and are immortal while moving to the portal. If unable to reach it after 3 minutes they'll be forced in manually.

Tweaked Proc

Redundant Code Removal

Remembered I didn't need this

Enhanced Code

Moved an if-statement to a better place to more adequately solve the issue.

Test Commit

Does this solution work?

Global Abnormality Mob List

Patrol Changes and Bird Grab changes

Gaming Test?

Temp Commit

Second Commit

Another Commit!

Fourth Commit

Subsystem changes. Dead abno cleansing. Lower speak cooldown. Debug text removal.

P-bird fix

Fixes P-bird able to die before reaching the portal

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[fc1e2e5e26...](https://github.com/carlarctg/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Friday 2023-03-10 08:39:59 by riot

L42A replacement with M4RA, less balance edition (#2674)

<!-- Write BELOW The Headers and ABOVE The comments else it may not be
viewable. -->

# IMPORTANT NOTES PLEASE READ
THIS DOES NOT CONTAIN THE NEW AMMO AND REBALANCED L42/M4RA THAT #1485
HAD
THIS DOES CONTAIN SOME BALANCE THINGS, BUT IT IS NOT ANYWHERE CLOSE TO
THE ABOVE

Also lore team wanted this, plz no gbp close maintainers 🙏 🙏 🧎‍♂️ 🕋 

# About the pull request

Replaces L42A in all marine available sources with the M4RA, the
canonical DMR of the USCM, you may notice this is currently the scout
rifle, well the scout rifle is now the M4RA Custom, a version that can
chamber the HV rounds that are spec ammo, but it can also chamber
standard m4ra rounds, albeit doing less damage with them than a normal
M4RA.

M4RA has current L42A stats fully, with the three exceptions being
having no stock to attach or remove(stock was not integrated it sucked),
being able to fit a/vgrip like scout m4RA, which may seem like a huge
thing but L42 stats were already insane, so it doesn't effect much.

M4RA Custom(scout gun), gets L42 stats as well, with the exception of
having less of a damage mult, meaning when not using the spec ammo, it
is out-preformed by the standard m4RA.

Adds new M4RA sprites, both standard and custom, by triiodine 

Adds sprites for all M4RA mag variants, by myself.

This was requested by lore team, previous PR of this with way more
balance stuff was #1485
Ok thats about all 🙂 

# Explain why it's good for the game

Lore accuracy is good, and this mostly doesn't effect the actual game
outside of the scout rifle changes.
Also scout rifle underpreformed if you weren't omega hell sliming with
inc-impact stunlocking while on fire, still will be omega hell slime
central but that isn't the thing being solved in this pr , it'll do fine
when NOT sliming at least now.


# Testing Photographs and Procedure
It works.


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
add: Adds the M4RA as the standard marine DMR, identical stats to L42
with the exception of fitting a v or agrip and no removable stock, stats
still the same as l42 without stock.
del: L42 from all marine accessible sources with the exception of black
market
balance: Scout M4RA is now the M4RA Custom, it can use standard M4RA
magazines but standard M4RA cannot use custom magazines.
balance: Scout M4RA now has L42/M4RA standard stats with the exception
of lower damage.
balance: Scout M4RA now can fit magnetic harness, laser sight, however
it can no longer fit recoil compensator
fix: R4T sling now has the correct color scheme on LV522
spellcheck: New desc for M4RA and L42 by misty
imageadd: New M4RA icons by triio, both scout and normal
/:cl:

---
## [BlackSilverUfa/data](https://github.com/BlackSilverUfa/data)@[749d645932...](https://github.com/BlackSilverUfa/data/commit/749d645932be3d5a732e7f8b822e7996cc379fff)
#### Friday 2023-03-10 08:48:15 by Дмитрий Карих

Запись стрима 1759103392

* Прохождения за один стрим — Подводный роман [100%]
* Прохождения за один стрим — Овощи [100%]
* Прохождения за один стрим — Парень, который мне нравится? [100%]
* Прохождения за один стрим — Jurassic Heart [100%]
* Первый взгляд 2023 — I Love You, Colonel Sanders! [100%]
* Первый взгляд 2023 — Hatoful Boyfriend [100%]

---
## [vpinball/pinmame](https://github.com/vpinball/pinmame)@[a37fbbe90f...](https://github.com/vpinball/pinmame/commit/a37fbbe90f79865b4d1f48228b9f2acc925a9be3)
#### Friday 2023-03-10 09:00:30 by toxie

address issue #102

cite from mjr:

The change to this file in commit 9ed410d, which is labeled as ported from MAME/MESS, adds a new bug, which affects DCS playback quality.

The changes are all to the implementation of the ABS (ABSOLUTE VALUE) instruction. The old version had an explicit CLR_S to clear the AS flag in ASTAT, whereas the new code deletes the CLR_S and substitutes CLR_FLAGS.

The addition of CLR_FLAGS is correct, since the instruction is documented as updating the AC-AN-AV-AZ flags. But the deletion of CLR_S is a bug, because the documentation also says that ABS must set or clear AS, according to the sign of the source operand. (See the ADSP 2100 User's Manual, 3rd edition, September 1995, section 15, ABSOLUTE VALUE (ABS) instruction: "AS: Set if the source operand is negative. Cleared otherwise.") CLR_FLAGS doesn't affect AS, so if AS was set going into the instruction, it'll still be set coming out, even if the operand was positive.

This isn't just a harmless bookkeeping detail - it actually breaks the DCS games in a subtle way! You can observe the effect of the bug on the DCS games by firing up ST-TNG LX7, going to the test menu, running the sound test, and letting track 1 ("1ST TUNE") run on auto-repeat. You'll hear a sort of flatulent distortion, which is occurring because that new ABS instruction bug is randomizing about 30% of the DCS frames decoded. It's actually affecting all of the tracks, but it seems to be more audible in tracks with lots of low bass frequencies, and just causes some annoying popping and crackling on most of the other tracks.

If anyone has been asking why the audio for all of the DCS games has been sucking lately, this is probably the answer.

Solution: Add back the CLR_S that was there before, right after the new CLR_FLAGS.

---
## [vesislavdimitrov/Car_Rental_System](https://github.com/vesislavdimitrov/Car_Rental_System)@[a352d68c0d...](https://github.com/vesislavdimitrov/Car_Rental_System/commit/a352d68c0d2207914c905dec56c6057ee1b272aa)
#### Friday 2023-03-10 09:54:47 by vesislavdimitrov

Oh Lord, you who are the refuge of the poor and needy,
we ask that you would save us
from the pestilence that stalks in the darkness
and the plague that destroys at midday.
Be our sun and shield.
Be our fortress.
Be our comfort this day.
May we not fear any evil
but rather trust in your might to save and your wisdom to guide,
so that we might rest  always in the shadow of the Almighty.
In the name of the One who heals our diseases. Amen.

---
## [minshin18/docs](https://github.com/minshin18/docs)@[460fc5f3c3...](https://github.com/minshin18/docs/commit/460fc5f3c36d94c1f75ef1e2de4da779697daa1d)
#### Friday 2023-03-10 10:08:28 by minshin18

minshin18.md

# GitHub Docs <!-- omit in toc -->

This repository contains the documentation website code and Markdown source files for [docs.github.com](https://docs.github.com).

GitHub's Docs team works on pre-production content in a private repo that regularly syncs with this public repo.

Use the table of contents icon <img src="/contributing/images/table-of-contents.png" width="25" height="25" /> on the top left corner of this document to get to a specific section of this guide quickly.

## Contributing

See [the contributing guide](CONTRIBUTING.md) for detailed instructions on how to get started with our project.

We accept different [types of contributions](https://github.com/github/docs/blob/main/contributing/types-of-contributions.md), including some that don't require you to write a single line of code.

On the GitHub Docs site, you can click the make a contribution button at the bottom of the page to open a pull request for quick fixes like typos, updates, or link fixes.

<img src="./contributing/images/contribution_cta.png" width="400">

For more complex contributions, you can open an issue using the most appropriate [issue template](https://github.com/github/docs/issues/new/choose) to describe the changes you'd like to see.

If you're looking for a way to contribute, you can scan through our [existing issues](https://github.com/github/docs/issues) for something to work on. When ready, check out [Getting Started with Contributing](/CONTRIBUTING.md) for detailed instructions.

### Join us in discussions

We use GitHub Discussions to talk about all sorts of topics related to documentation and this site. For example: if you'd like help troubleshooting a PR, have a great new idea, or want to share something amazing you've learned in our docs, join us in the [discussions](https://github.com/github/docs/discussions).

### And that's it!

If you're having trouble with your GitHub account, contact [Support](https://support.github.com/contact).

That's how you can easily become a member of the GitHub Documentation community. :sparkles:

## READMEs

In addition to the README you're reading right now, this repo includes other READMEs that describe the purpose of each subdirectory in more detail:

- [content/README.md](content/README.md)
- [content/graphql/README.md](content/graphql/README.md)
- [content/rest/README.md](content/rest/README.md)
- [contributing/README.md](contributing/README.md)
- [data/README.md](data/README.md)
- [data/reusables/README.md](data/reusables/README.md)
- [data/variables/README.md](data/variables/README.md)
- [components/README.md](components/README.md)
- [lib/liquid-tags/README.md](lib/liquid-tags/README.md)
- [middleware/README.md](middleware/README.md)
- [script/README.md](script/README.md)
- [stylesheets/README.md](stylesheets/README.md)
- [tests/README.md](tests/README.md)

## License

The GitHub product documentation in the assets, content, and data folders are licensed under a [CC-BY license](LICENSE).

All other code in this repository is licensed under the [MIT license](LICENSE-CODE).

When using the GitHub logos, be sure to follow the [GitHub logo guidelines](https://github.com/logos).

## Thanks :purple_heart:

Thanks for all your contributions and efforts towards improving the GitHub documentation. We thank you for being part of our :sparkles: community :sparkles:!

---
## [jcampoy/liferay-portal](https://github.com/jcampoy/liferay-portal)@[2581138019...](https://github.com/jcampoy/liferay-portal/commit/258113801997cd4333fa255e1ee207a999b6cfbe)
#### Friday 2023-03-10 10:10:35 by Greg Hurrell

LPS-129801 Port "render.es.js" to TS

Note this requires some horrible ugly casts for `Liferay`, because
globals are nasty and all that. Figuring out how to declare that as an
ambient type in some central location in the context of project
references is going to be complicated enough, based on my reading of:

    https://github.com/microsoft/TypeScript/issues/29002

that I am going to leave it for a separate commit.

There are a couple of `any` in here too, which I don't like (we've
mostly been able to get away without any `any` at all in
`frontend-js-react-web`) but I want to close up shop for the day so I am
going to commit this and push what I have.

---
## [juusujanar/matrix-docker-ansible-deploy](https://github.com/juusujanar/matrix-docker-ansible-deploy)@[adcc6d9723...](https://github.com/juusujanar/matrix-docker-ansible-deploy/commit/adcc6d9723086f65f1a7284a4d3eee03de56ac22)
#### Friday 2023-03-10 10:24:38 by Slavi Pantaleev

Relocate Traefik (to matrix-traefik.service && /matrix/traefik base path)

The migration is automatic. Existing users should experience a bit of
downtime until the playbook runs to completion, but don't need to do
anything manually.

This change is provoked by https://github.com/spantaleev/matrix-docker-ansible-deploy/pull/2535

While my statements there ("Traefik is a shared component among
sibling/related playbooks and should retain its global
non-matrix-prefixed name and path") do make sense, there's another point
of view as well.

With the addition of docker-socket-proxy support in bf2b54080789f7e,
we potentially introduced another non-`matrix-`-prefixed systemd service
and global path (`/devture-container-socket-proxy`). It would have
started to become messy.

Traefik always being called `devture-traefik.service` and using the `/devture-traefik` path
has the following downsides:

- different playbooks may write to the same place, unintentionally,
  before you disable the Traefik role in some of them.
  If each playbook manages its own installation, no such conflicts
  arise and you'll learn about the conflict when one of them starts its
  Traefik service and fails because the ports are already in use

- the data is scattered - backing up `/matrix` is no longer enough when
  some stuff lives in `/devture-traefik` or `/devture-container-socket-proxy` as well;
  similarly, deleting `/matrix` is no longer enough to clean up

For this reason, the Traefik instance managed by this playbook
will now be called `matrix-traefik` and live under `/matrix/traefik`.

This also makes it obvious to users running multiple playbooks, which
Traefik instance (powered by which playbook) is the active one.
Previously, you'd look at `devture-traefik.service` and wonder which
role was managing it.

---
## [LC4492/CM-Space-Station-13](https://github.com/LC4492/CM-Space-Station-13)@[6f1b1717a7...](https://github.com/LC4492/CM-Space-Station-13/commit/6f1b1717a7d6ef3c04ef58c294353fe0b98ca836)
#### Friday 2023-03-10 12:27:51 by TotalEpicness

Boiler rework Part 1: Globber base boiler (#965)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request


A total redesign of the base boiler reminiscent of the old premoba
boiler that would shoot projectile "Globs" with a modern CM take.

Base boiler as it is right now, is completely unfun, to play against and
to even play as. You'd be hard-pressed to find someone who enjoys
playing it past the first 10 minutes of doing so. It is this way not
because it's weak, but because it's unchallenging and 100% "safe"
gameplay. There are no combos, cool moves you can do, or even satisfying
effects, you just hit a button to spawn a telegraph which becomes a gas
cloud.

This PR, turns that right ontop of its head. Instead of "safe" gameplay,
globber's design philosophy is centered around being challenging, fun
and even adding new gameplay dynamics.

Globber will have higher HP, faster walkspeed, and faster firing bombard
compared to premoba.

However, globber will have their fellow xenos making plays to cover for
boiler, either directly through bodyblocking shots or making plays to
distract marines due to a minimal zoom range.

These both, in theory, will create a new gameplay dynamic where boilers
will still be able to block marine spearheads, but Globber needs to help
make a small counter push with their fellow brethren in order for
Globber to directly strike at marines and giving the Xenos the choice to
either capitalize on their advantage or heal up upon a successful glob.

Design doc
https://hackmd.io/@-h91mVK3RhaURcykLHRxJQ/S1W0FCZPj

### Details:
Globber will feature [TENTATIVE] higher HP and [TENTATIVE] faster walk
speed. It however will be slightly more vulnerable to fire as fire deals
[TENTATIVE]% more damage to it!


https://cdn.discordapp.com/attachments/458150341742166017/1013647188313776148/2022-08-28_17-10-53.mov

Globber Active 1 - Bombard: Spit a large acid glob that will, upon
impact, immediately spread a gas glob of your choice

- Cooldown: 30 seconds
- cost: 200 plasma
- Windup: 5 seconds

Globber Active 2 - Acid spray, instantly sprays a line of acid, May make
it a cone spray if it is too weak

- 8 second c/d
- No windup
- 40 plasma
- 6 tile range

Globber Active 3 - Shift spits: Switch between acid and neuro gas globs.
Acid deals more raw damage while neuro slows,blinds and eventually
knocks down marines. Neuro has a larger radius than acid

Globber Active 4 - Acid shroud: A quick windup action that dumps an acid
cloud over the boiler. Cooldowns other abilities similar to dump acid.

Globber Active 5 - Zoom: Short ranged zoom with short windup. Trades
awareness for zoom

Globber Passive: Brute armor, Globber features brute armor, however, it
does not protect against flames! Globber takes 1.5x damage to fire!

Acid glob: Pretty much the same as before. May adjust numbers.

Neuro smoke rework:
- Instead of insta blindness and deafness, these will now have a chance
of applying for every tick you are in the smoke. You still have
blurry/weldervision though
- Oxyloss toned down, it was 9 per tick, now two
- Knockdown chance lowered to 5% per tick. Stamina damage replaces RNG
knockdowns
+ Now deals stamina damage, and am making it stack fast, targeted
knockdown time is 2-3 seconds
+ Minor immediate slowdown applied. May remove as it stacks with stamina
damage slow
+ chance of dealing minor tox damage

### Boiler rework as a whole

The boiler rework is a total rework of the boiler strain and it's
strains.

I'm not gonna write the entire design doc here, but in short:

-Base boiler will be reworked (as shown here), named Globber
- trapper will be totally scrapped for 'Grenadier', a heavy siege strain
that lobs devastating nades that's counterable and challenging.
Grenadier will have the same zoom as Globber
- A long-range, general-purpose strain will be added, named "Striker
Boiler", which combines both the Railgun boiler and the mostly forgotten
"Acid Splatter" strains in the past, with a modern CM twist.

design docs( old as fuck and needs updating) _**REPLACE ME WITH NEW
ONE**_
https://github.com/cmss13-devs/cmss13-design-docs/pull/7
Striker design doc
https://github.com/cmss13-devs/cmss13-design-docs/pull/8


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
TL;DR base boiler is a literal NPC strain that no one likes to play as
or against. Attempt to make it more fun or die trying

if the design philosophy fails, then we can simply just tweak a few
values and have premoba boiler again.

Design doc is already made but its ancient as shit and I'm just gonna
make a new one so its WIP for now.

Design doc
https://hackmd.io/@-h91mVK3RhaURcykLHRxJQ/S1W0FCZPj

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: Totalepicness
add: Added "Globber Boiler", which is a total replacement of base
boiler, designed to kill the "safe" gameplay loops of current base
boiler in an attempt for a more challenging and fun caste to both play
as and against.
balance: Globber Active 1 - Bombard: Spit a large acid glob that will,
upon impact, immediately spread a gas glob of your choice
balance: Globber Active 2 - Spray acid: Instantly sprays a line of acid
balance: Globber Active 3 - Shift spits: Switch between acid and neuro
gas globs. Acid deals damage while neuro slows, blinds and eventually
knocks down marines. Neuro has a larger radius than acid
balance: Globber Active 4 - Acid shroud: A quick windup action that
dumps an acid cloud over the boiler. Cooldowns other abilities similar
to dump acid.
balance: Globber Active 5 - Zoom: Short-ranged zoom with no windup.
balance: Globber Passive: Globber features armor, but it is weaker
against flames! Stay away from fire!
refactor: Refractored some minor spit code and icons
balance: Neuro has been completely reworked to deal mainly stamina
damage, causes dizzyness and has a small chance to make you 'stumble' in
a random direction along with minor tox damage. Stay out of it!
add: Completly reworked neuro gas, it now uses a proper effect with
escalating effects the larger the dosage rather than RNG.
fix: Acid now deals damage to cades and now has a good chance of going
over instead of being airtight
fix:  Boiler globs no longer can target mobs and track them.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Epicness <coolguyethanw@gmail.com>
Co-authored-by: Geeves <ggrobler447@gmail.com>
Co-authored-by: Segrain <Segrain@users.noreply.github.com>
Co-authored-by: harryob <me@harryob.live>

---
## [dgmjr-io/VideoStickerBot](https://github.com/dgmjr-io/VideoStickerBot)@[22838d57eb...](https://github.com/dgmjr-io/VideoStickerBot/commit/22838d57ebd3cdb9b519a809b9f4c1d5e7929261)
#### Friday 2023-03-10 12:47:54 by David G. Moore, Jr

Initial check-in but the shit still deoesn't work

I FUCKING HATE PYTHON!!!

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[82763183d2...](https://github.com/odoo-dev/odoo/commit/82763183d2da5fe652d66dd482bbe7efedc2dbd9)
#### Friday 2023-03-10 13:06:46 by Romain Derie

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

closes odoo/odoo#111736

X-original-commit: f05491105f93939490cbeb078cb7653c38685644
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[c68a159884...](https://github.com/odoo-dev/odoo/commit/c68a15988432b201ae3786eb54bac3110c4242f4)
#### Friday 2023-03-10 13:19:58 by Arnold Moyaux

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

X-original-commit: 97f52bd40d97109a7983549d252476959ddceada
Part-of: odoo/odoo#112325

---
## [jamessimo/space-station-14](https://github.com/jamessimo/space-station-14)@[581e8a0d12...](https://github.com/jamessimo/space-station-14/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Friday 2023-03-10 13:39:46 by eclips_e

Give slimes their sex back (not the ERP one) (#14380)

<!-- Please read these guidelines before opening your PR: https://docs.spacestation14.io/en/getting-started/pr-guideline -->
<!-- The text between the arrows are comments - they will not be visible on your PR. -->

## About the PR
<!-- What does it change? What other things could this impact? -->

Gives back the ability for slimes to have a definitive sex. Cosmetic/visual things such as emotes/other stuff use the person's sex and not the gender and I feel like that the removal of slime's having sexes was just to show that the species refactor could handle unsexed species.

**Media**
<!-- 
PRs which make ingame changes (adding clothing, items, new features, etc) are required to have media attached that showcase the changes.
Small fixes/refactors are exempt.
Any media may be used in SS14 progress reports, with clear credit given.

If you're unsure whether your PR will require media, ask a maintainer.

Check the box below to confirm that you have in fact seen this (put an X in the brackets, like [X]):
-->

- [x] I have added screenshots/videos to this PR showcasing its changes ingame, **or** this PR does not require an ingame showcase

**Changelog**
<!--
Here you can fill out a changelog that will automatically be added to the game when your PR is merged.

Only put changes that are visible and important to the player on the changelog.

Don't consider the entry type suffix (e.g. add) to be "part" of the sentence:
bad: - add: a new tool for engineers
good: - add: added a new tool for engineers

Putting a name after the :cl: symbol will change the name that shows in the changelog (otherwise it takes your GitHub username)
Like so: :cl: PJB
-->

:cl: eclips_e
- fix: Male and female slimes now scream and laugh properly

---
## [hyperlane-xyz/hyperlane-monorepo](https://github.com/hyperlane-xyz/hyperlane-monorepo)@[59a90b1bb6...](https://github.com/hyperlane-xyz/hyperlane-monorepo/commit/59a90b1bb63106d9dd7fa640b17772096073dfb8)
#### Friday 2023-03-10 15:13:49 by Trevor Porter

Default to not allowing LocalStorage checkpoint syncers in relayer (#1900)

### Description

Open to better names

Adds a setting to the relayer, `allow_local_checkpoint_syncers`, which
determines whether local storage based checkpoint syncers will be
allowed by the metadata builder.

Originally, I wanted something a bit more clever, like being able to
specify `HYP_RELAYER_VALIDCHECKPOINTSYNCERS=LocalStorage,S3` or
something, where I'd like those variants to be matched to the variants
found in
https://github.com/hyperlane-xyz/hyperlane-monorepo/blob/main/rust/hyperlane-base/src/types/checkpoint_syncer.rs#L14.
But that enum requires values, so things get ugly. One option would be
to create a new enum like:
```
enum CheckpointSyncerTypes {
  LocalStorage,
  S3,
}
```
And another option is to use something like strum's
[EnumString](https://docs.rs/strum/latest/strum/derive.EnumString.html)
(shoutout to @mattiecnvr). But this still is a bit clunky, so for now
just making this a bool and we can figure out something more elegant
later if we ever get to a point where we're supporting multiple types of
checkpoint syncers

### Drive-by changes

none

### Related issues

- Fixes https://github.com/hyperlane-xyz/issues/issues/402

### Backward compatibility

_Are these changes backward compatible?_

Yes - although if you ever want to run a relayer that uses local storage
now, you'll need to set `HYP_RELAYER_ALLOWLOCALCHECKPOINTSYNCERS=true`

_Are there any infrastructure implications, e.g. changes that would
prohibit deploying older commits using this infra tooling?_

None - we always expect to not be reading from the local fs in deployed
relayers


### Testing

_What kind of testing have these changes undergone?_

Ran e2e tests

---
## [jamesthesnake/napari](https://github.com/jamesthesnake/napari)@[3ec4be1ae8...](https://github.com/jamesthesnake/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Friday 2023-03-10 15:38:33 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [MrSamu99/Shiptest](https://github.com/MrSamu99/Shiptest)@[7f8874df29...](https://github.com/MrSamu99/Shiptest/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Friday 2023-03-10 15:58:38 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[e9c87c0acb...](https://github.com/mc-oofert/tgstation/commit/e9c87c0acb15439c8f577bba35c45f51bf03d1aa)
#### Friday 2023-03-10 15:59:46 by LemonInTheDark

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
## [justsmth/aws-lc](https://github.com/justsmth/aws-lc)@[4263903bd1...](https://github.com/justsmth/aws-lc/commit/4263903bd1d15d56c47cbd6440bea657df2c142e)
#### Friday 2023-03-10 16:53:15 by David Benjamin

Maintain a frame pointer in aesni-gcm-x86_64.pl and add SEH unwind codes

Some profiling systems cannot unwind with CFI and benefit from having a
frame pointer. Since this code doesn't have enough register pressure to
actually need to use rbp as a general register, this change tweaks
things so that a frame pointer is preserved.

As this would invalidate the SEH handler, just replace it with proper
unwind codes, which are more profiler-friendly and supportable by our
unwind tests. Some notes on this:

- We don't currently support the automatic calling convention conversion
  with unwind codes, but this file already puts all arguments in
  registers, so I just renamed the arguments and put the last two
  arguments in RDI and RSI. Those I stashed into the parameter stack
  area because it's free storage.

- It is tedious to write the same directives in both CFI and SEH. We
  really could do with an abstraction. Although since most of our
  functions need a Windows variation anyway.

- I restored the original file's use of PUSH to save the registers.
  This matches what Clang likes to output anyway, and push is probably
  smaller than the corresponding move with offset. (And it reduces how
  much thinking about offsets I need to do.)

- Although it's an extra instruction, I restored the original file's
  separate fixed stack allocation and alloca for the sake of clarity.

- The epilog is constrained by Windows being extremely picky about
  epilogs. (Windows doesn't annotate epilogs and instead simulates
  forward.) I think other options are possible, but using LEA with an
  offset to realign the stack for the POPs both matches the examples in
  Windows and what Clang seems to like to output. The original file used
  MOV with offset, but it seems to be related to the funny SEH handler.

- The offsets in SEH directives may be surprising to someone used to CFI
  directives or a SysV RBP frame pointer. All three use slightly
  different baselines:

  CFI's canonical frame address (CFA) is RSP just before a CALL (so
  before the saved RIP in stack order). It is 16-byte aligned by ABI.

  A SysV RBP frame pointer is 16 bytes after that, after a saved RIP and
  saved RBP. It is also 16-byte aligned.

  Windows' baseline is the top of the fixed stack allocation, so
  potentially some bytes after that (all pushreg and allocstack
  directives). This too is required to be 16-byte aligned.

  Windows, however, doesn't require the frame register actually contain
  the fixed stack allocation. You can specify an offset from the value
  in the register to the actual top. But all the offsets in savereg,
  etc., directives use this baseline.

Performance difference is within measurement noise.

This does not create a stack frame for internal functions so
frame-pointer unwinding may miss a function or two, but the broad
attribution will be correct.

Change originally by Clemens Fruhwirth. Then reworked from Adam
Langley's https://boringssl-review.googlesource.com/c/boringssl/+/55945
by me to work on Windows and fix up some issues with the RBP setup.

Bug: b/33072965, 259
Change-Id: I52302635a8ad3d9272404feac125e2a4a4a5d14c
Reviewed-on: https://boringssl-review.googlesource.com/c/boringssl/+/56128
Reviewed-by: Adam Langley <agl@google.com>
Commit-Queue: David Benjamin <davidben@google.com>
(cherry picked from commit 0d5b6086143d19f86cc5d01b8944a1c13f99be24)

---
## [HaodongMo/ARC-9](https://github.com/HaodongMo/ARC-9)@[bab0e24906...](https://github.com/HaodongMo/ARC-9/commit/bab0e249064fc65adfedb5de4b21ab2f858952b6)
#### Friday 2023-03-10 17:05:02 by Darsu

consistent mp/server recoil with sp god i hate this fucking base and whoever made this visual recoil

---
## [readmeio/metrics-sdks](https://github.com/readmeio/metrics-sdks)@[1ce6c540e7...](https://github.com/readmeio/metrics-sdks/commit/1ce6c540e7ccee34b6b8d2b5c1326a5ff9157cb2)
#### Friday 2023-03-10 17:34:35 by Jon Ursenbach

fix(ruby): support rack@3.0.0 (#653)

* fix(ruby): compatibility issues with rack v3.0.0

* fix: typo

* fix: ruby gemfile issues

* chore(deps): updating all ruby deps to be compatible with rack@3.0

* fix: broken tests

* chore: wip work

* fix: rack 3.0.0 upgrade to do with rack.input not being rewindable

Opted to just use `@request.body.read` instead:
https://www.rubydoc.info/gems/rack/Rack/Request/Helpers#body-instance_method

* fix: remove `HAS_HTTP_QUIRKS` flag from integration tests

OK here's where this PR gets interesting... I spent a bunch of time debugging
the test failures here: https://github.com/readmeio/metrics-sdks/pull/653#pullrequestreview-1309362560

I eventually settled on some code that was working, committed here:
224e2ad54c9bef641db39e650bfdc464a55c929b

But that was causing a bunch of `EOFErrors` from Ruby when sending the
HTTP request out to the metrics server:

```
#<Thread:0x000000010c67e488 /Users/domh/Sites/readmeio/metrics-sdks/packages/ruby/lib/readme/request_queue.rb:30 run> terminated with exception (report_on_exception is true):
/opt/homebrew/lib/ruby/gems/3.1.0/gems/net-protocol-0.1.3/lib/net/protocol.rb:227:in `rbuf_fill': end of file reached (EOFError)
	from /opt/homebrew/lib/ruby/gems/3.1.0/gems/net-protocol-0.1.3/lib/net/protocol.rb:193:in `readuntil'
<long stack trace omitted>
```

It turns out that this wasn't a problem on the Ruby side, but in fact a
problem from the Node.js testing side, because when not in "quirks" mode
our fake metrics server happily accepted requests but just ignored them
and never responded to anything.

https://github.com/readmeio/metrics-sdks/blob/7728160f522847b9a59ce7a565eca35610c6e015/test/integration-metrics.test.js#L88-L113

Some languages are okay with this (node, PHP) and some are not okay with
this (python, and Ruby with rack@3.0.0 evidently).

Since it is kinda janky for us to create an HTTP server and just ignore
everything and not respond with anything, I've opted to make the quirks
behaviour the default with this PR! This seems to work for all languages
I've tested locally but lets see if it passes for all of them on CI 🤞

I also had to add another fix here where the body was being returned empty
to the test because the HTTP request from Ruby wasn't complete yet, so if
we hit this race condition, I've opted to just sleep for 300ms and try again.
Using this property:

https://nodejs.org/docs/latest/api/http.html#messagecomplete

Oh don't you just love HTTP.

* fix: rack body using `Rack::RewindableInput`

Creates a new `Rack::RewindableInput` on initialize, then in the body
method we read it in, then rewind it back and finally return it

---------

Co-authored-by: Dom Harrington <domharrington@users.noreply.github.com>
Co-authored-by: Dom Harrington <domharrington@protonmail.com>

---
## [mshurkaeu-public/i-care.by](https://github.com/mshurkaeu-public/i-care.by)@[ee0284b9ed...](https://github.com/mshurkaeu-public/i-care.by/commit/ee0284b9ed826e551a65e903233a5b31d6da1295)
#### Friday 2023-03-10 17:46:58 by Mikalai Shurkaeu

The very first draft for #1

Originally the idea in the issue was to create a mobile app
with a name like "who-is-he-how-is-she-meter".

When I started work on the implementation I realized that
it actually would do the very basic and useful things to
care about the most important person in user's life. Thus
I decided that the name of the app would be something like
"i-care.by <platform> app". I chose Flutter to write code
once and then compile it to different target platforms.

"i-care.by web app" is available at
https://mshurkaeu-public.github.io/i-care.by-app/web/

In this first commit the following is implemented:
1. User preferences (name and preferred pronoun).
2. Display the list of the diary records on home page.
3. Editing today record (- want to do today, - emotions in that
moment, - done today, - emotions in that moment)
4. Options to answer "who is the most important person
in your life" are randomized on each run, so the user needs
to focus and find the appropriate one.

Each day the application asks (trigerred by user)
1. Who is the most important person in your life?
2. What do you want to do for the person today?
3. What are your emotions and feelings in this moment?
--
then, presumably in the second part of the day,
4. What did you do for the person today?
5. What are you emotions and feelings in this moment?

The answers are recorded and stored in json format in
window.localStorage on web. And in application documents
folder on other platforms.
----

I want to say thank you to the following people, who helped
me create this first draft (chronological order, most recent
go first):

- my father, Nikolai Slon - provided valuable feedback about
  my texts. And that helped make the texts more clear.

- Olga Shramenok (Spasibyonok) and Arina Shramenok - provided
  valuable feedback about their vision of use cases for the
  application. That helped me better understand my own vision
  of the target audience and clarify messages, shown in the app.

- Maxim Khaletsky - provided valuable feedback about texts.
  Some of his ideas are not fully reviewed yet. But some of the
  issues, he found, are already fixed in this commit.

- Maksim Lakatkou - helped to find some typos and also push me
  in the direction to make texts more friendly. That led to the
  introduction of gender specific setting in the application and
  thus more friendly texts.

There were couple of more people, who helped and provided their
feedback. But I don't know if they are OK that their names are
mentioned here. So, thank you, Ch. D. and N. M., for your
feedback.

---
## [SlightlyCircuitous/Cockatrice](https://github.com/SlightlyCircuitous/Cockatrice)@[55a2f75d16...](https://github.com/SlightlyCircuitous/Cockatrice/commit/55a2f75d16511bad70e4689c9ac85af86ec797b2)
#### Friday 2023-03-10 17:49:03 by Basile Clement

Make cards rounded (#4765)

* Make cards rounded

Magic cards have rounded corners, and playing cards tend to have rounded
corners as well, but Cockatrice currently displays rectangular cards.

This can cause visual glitches when using image scans where the border
does not extend in the corner, and for this reason Cockatrice always
draws a (rectangular) border around the card to try and make it look a
bit better.

In this patch I take a different approach: rather than try to make
rounded pegs, er, cards, go into a square hole, the hole is now rounded.
More precisely, the AbstractCardItem now has a rounded rectangular shape
(with a corner of 5% of the width of the card, identical to that of
modern M:TG physical cards).

As a side effect, the card drawing gets a bit simplified by getting rid
of transformPainter() when drawing the card outline and using the
QPainter::drawPixmap overloads that takes a target QRectF instead.  This
means we no longer have to bother about card rotation when painting
since that's taken care of by the Graphics View framework (which
transformPainter() undoes).

* format

* Also give PileZone rounded corners

* Forgot untap status + bits of CardDragItem

* fix deckviewcard calculations

* Rounded CardInfoPicture

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[373fec086a...](https://github.com/mrakgr/The-Spiral-Language/commit/373fec086a5c69a3ebf5d4884a42c4b43c2cc364)
#### Friday 2023-03-10 17:57:24 by Marko Grdinić

"8:40am. I got Limbus Company yesterday and played until too late. Now I am groggy.

https://pluralistic.net/2023/03/09/autocomplete-worshippers/#the-real-ai-was-the-corporations-that-we-fought-along-the-way

///

But even if you add all of this up, double it, square it, and add a billion dollar confidence interval, it still doesn't add up to what Bank Of America analysts called "a defining moment — like the internet in the ’90s." For one thing, the most exciting part of the "internet in the '90s" was that it had incredibly low barriers to entry and wasn't dominated by large companies – indeed, it had them running scared.

The AI bubble, by contrast, is being inflated by massive incumbents, whose excitement boils down to "This will let the biggest companies get much, much bigger and the rest of you can go fuck yourselves." Some revolution.

///

This is such a great quote.

Let me read this and then I will get started...on that Reaper tutorial. I need to go through it.

9:25am. Let me get started.

Any mail?

Got an answer to the issue I opened yesterday.

https://javascript.plainenglish.io/javascript-finalizer-2859f0832f07

Oh, it seems JS has finalizers.

9:35am. Where was I?

///

> I was wondering if you've made sure to implement the finalizers so that they close out the side on the other machine? The connection being closed should also cause a disposal as well.

For this first part, the answer, for now, would be no. There is no treatment for that case. For that second part, I'm not sure. The implementation for the reply channel is very barebone, containing only one GUID identifying the value channel and another for the exception channel. It should be possible to save that identifier and reconstruct the channel so you can answer the front end even after disconnection.

Even though this scenario is plausible, it's not being supported at the moment. We could add an option to close all channels when the connection is dropped and add a way to restore broken channels, so both possibilities are supported.

> would that throw an exception in the async expression that is waiting on the reply channel?

I believe that should be the expected behavior, and honestly, I think that the exception serializer doesn't even work. Maybe we could also change it to expect a string that will turn into the exception Message while we are adding those features.

///

Let me watch the reapoer podcast. To be honest, I do not get why the mic has a port for the headphones, let me switch back to the regular port.

https://youtu.be/y-Tu14fG4C8?t=1774
How to Edit a Podcast | Reaper Tutorial

Let me resume this.

10:05pm. I really like Reaper. It is so snappy, Also, once I calculated the loudness it actually gave me the option to export the results as HTML and charted them!

https://youtu.be/y-Tu14fG4C8?t=2151

My own columns are different. I do not have the true peak, just the peak instead.

https://youtu.be/y-Tu14fG4C8?t=2259
> The default version of normalization is a different version which is mostly useless.

That is what I've been using.

https://youtu.be/y-Tu14fG4C8?t=2278

-19 if they are mono. Not -16?

https://youtu.be/y-Tu14fG4C8?t=2346

I thought decibels were base 2.

https://www.britannica.com/science/decibel

> Expressed as a formula, the intensity of a sound in decibels is 10 log10 (S1/S2), where S1 and S2 are the intensity of the two sounds; i.e., doubling the intensity of a sound means an increase of a little more than 3 dB.

Oh, they are log base 10.

I guess it makes sense then.

10:15am. https://youtu.be/y-Tu14fG4C8?t=2521

Let me just watch this. It is easy to understand, so I do not feel the urge to follow along right now.

https://www.pianoforproducers.com/loudness/#:~:text=True%20Peak%3A%20the%20maximum%20level,at%20a%20more%20detailed%20level.

> True Peak is just a more accurate version of peak. It essentially measures peak but at a more detailed level. I can get more into the technical difference, but it really doesn’t matter. They measure the same thing: the maximum level your signal reaches. Using either is fine, but if you have a choice technically True Peak is more accurate.

Ok.

> RMS: the average loudness level of your signal over a given time period using the average power of the signal.
> LUFS: the average loudness level of your signal over a given time period based on human perception of loudness.

Ok. Easy to understand.

> RMS: judges loudness based on the voltage of the signal.
> LUFS: judges loudness based on how humans perceive loudness.

https://youtu.be/y-Tu14fG4C8?t=2689

Is the limiter not clipping the values? How does that work?

https://youtu.be/y-Tu14fG4C8?t=3382

I already knew how to do denoising, but I've never heard about gates before.

https://youtu.be/y-Tu14fG4C8?t=3643

It is not nonsense, this is very easy to understand.

https://youtu.be/y-Tu14fG4C8?t=3943

This is super useful.

11am. Tried out the gate. I really don't need the noise subtraction thanks to it.

https://youtu.be/y-Tu14fG4C8?t=4369

I do not get it. What is the difference between this and a limiter?

https://youtu.be/y-Tu14fG4C8?t=4446

Ah, I get it. It just divides the audio above -7Db by 4.

https://youtu.be/y-Tu14fG4C8?t=5300

I can't tell at all what would be better and what would be worse.

11:50am. Let me take a short brea.

https://boards.4channel.org/a/thread/249895098/killing-bites#p249903640

It seems somebody started translating Vaian Maiden.

https://mangadex.org/title/0bfd9934-e738-44c0-adcf-dc7962f7d76c/vaia-n-maiden

11:55am. Ah, you know what. Let me stop here for breakfast.

https://youtu.be/y-Tu14fG4C8?t=6084

I have 35m of this left and I do not feel like rushing it.

12pm. Breakfast time.

https://mangadex.org/chapter/85f4c3c1-aabf-4c44-9661-87a5f03030d2/7

The art for this is actually quite good.

12:30pm. https://mangadex.org/chapter/552d8de6-70ca-49a8-9f13-53bb676857c5/13

Based.

///

Somebody posted the translated scripts for the two volumes on /a/ a couple months ago:
https://desuarchive.org/a/thread/247012151/#q247012151
https://desuarchive.org/a/thread/247091157/#q247091157

///

From the Dex forums. I'll check this out later. Now come the chores.

12:55pm. It is pouring outside so I'll leave them for later. Let me resume the Reaper editing course.

https://youtu.be/y-Tu14fG4C8?t=6484
> Some frequencies in music can interfere with speech intelligebility.

https://youtu.be/y-Tu14fG4C8?t=6940

This fade he is doing would have been really useful in Camtasia. It really might be worth trying out OBS + Da Vinci Resolve.

1:45pm. Done with that course.

Now, I am thinking. Whether I want to dumb Camtasia or not depends on how much I can do in OBS. Why couldn't I just export it raw into Da Vinci resolve for that matter? I had that idea plenty of times, but Camtasia seems to only favor lossy encodings.

Let me just take a look at an OBS tutorial.

https://youtu.be/ySENWFIkL7c
🔴 How to use OBS for Screen Recording or Streaming - Beginner Tutorial

https://youtu.be/ySENWFIkL7c?t=21
> I use it to record all of my videos on this channel.

https://youtu.be/ySENWFIkL7c?t=145

He says I could use a virtual camera to send video to Zoom or Google Meets. I've been wondering about that.

https://youtu.be/ySENWFIkL7c?t=440

I really wonder how those nested screens work? It boggles my mind a little.

2:15pm. I can't finish this. It is too boring. Enough.

Let me work on my own things.

Let me work on the nitro.

2:30pm. Let me do the script.

4:25pm. I admit, I am not getting much from Reaper. The gate effect is pretty great. I can set it to something like -26db, and it will cut out some of the noise sounds. It also allows me to normalize very precisely. But the equalizer, the compressor and the limiter...meh.

This mic does 98% the job on its own. I thought it would be sure to catch the soft humming of the radiator next to me like the webcam does, but it turns out that it doesn't. Which is great.

I thought I might need to sound proof my room, but it seems that this is not needed either. Maybe it is due to the placement or all the objects that are in the room, but there is zero reverb.

Even if I didn't touch the Gate and kept to Camtasia, I wouldn't have been particularly worse off.

Ok. Next time I'll just save the gate template and use Reaper to normalize the podcast and that is it.

4:35pm. https://youtu.be/_Z6-B8wEJC4
Intro To The Web Dev In F# Series

Here it is. Sometimes just having the right setup does all of the work for you.

4:40pm. I've spent too much time in a daze. Let me move on to the next video. I am way too slow.

Let me get started on the first tutorial.

5:25pm. I hate talking, I hate talking, I hate talking!

I hate talking!!!

Agh.

How about I skip tutorial 1?

Forget it. I need to scrap this project. It is shit.

5:40pm. I really need to think about the lesson plan. What I want to say, and so on. I find it very hard to come to it naturally.

6:15pm. Had to take off in order to do the chores.

I've been thinking. You know how with voice overs I write a paragraph and then recite it. From here on out, why don't I try adopting the same workflow except with screencasts. I can stitch together a video out of short screencasts. The surest way to get a mediocre result is to just try to do it all at once.

I am going to try it tomorrow. Somehow, the whole day went by and I've only produced a 3m video, but tomorrow I am going to do it in a more focused manner.

Tomorrow, what I am going to do is make a prerequisites video.

In the intro video I said what I am going to do. Before I can start I really need a video explaining to the various levels of the viewer what they should know before starting this playlist.

6:30pm. Lunch time.

6:50pm. Let me close here. I want to play Limbus Company.

Tomorrow, I am going to make a proper video, closer to being pro in quality.

I can beat myself up over my lack of skill, but before I conclude that making good vids is too much for me, how about I try putting in the proper effort?"

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[2b76197397...](https://github.com/GoldenAlpharex/tgstation/commit/2b76197397b4241957e93a9779fdd9dfbada2688)
#### Friday 2023-03-10 18:35:10 by Jacquerel

Makes Lesser Form into one ability & unit tests it (#73572)

## About The Pull Request

Fixes #73491
Every time I have used this ability lately it's been fucked. 
It would vanish from my actions at arbitrary moments, and also sometimes
transform me into a horrible monkey-man thing instead of a monkey. This
is a shame because being able to become a monkey can be pretty fun, even
if it makes you very vulnerable to being butchered.

Refactoring it into being one action instead of two actions which add
and remove each other fixes the part where the action just disappears.
It reliably sticks between transformations now, regardless of whether or
not they were voluntary.

I also noticed that when I was turning into a monkey it wasn't dropping
the changeling "fake clothes" outfit pieces I had on as a human, leading
to a really fucked up looking monkey. I fixed this by adding `force =
TRUE` in the drop to ground proc in the check for if the equipment you
have is still valid after your species changes. I don't _think_ this has
any side effects but I never do and then someone finds some.
For good measure I also made all of the changeling equipment abilities
which don't work if you are a monkey detect if you become a monkey and
retract themselves.

I also noticed that for a long time Last Resort has been trying and
failing to give you Lesser Form (well, Human Form rather) as a Headcrab,
so I fixed that and now you actually get the ability.

Finally I did a _little_ bit of housekeeping in general on the
changeling actions, mostly balloon alerts. I think these definitely need
more attention than I gave them though. I left a lot of the `to_chat`s
in place because many of them give information you want to be a little
sticky, or refer back to in order to double check what you just did.

I also added a unit test which flips back and forth a few times to
ensure the ability still works.
This required adding an "instant" flag to the monkeyize/humanize procs
to skip the timers, and idenitified a couple of weird issues.
First point: Humanising a monkey would remove the monkey mutation and
then call humanise again, which would not skip itself because it still
regarded you as being a monkey. I changed the order of operations here
slightly so that it will early return.
Second point: Calling `domutcheck` on `human/consistent` would runtime
because we skip the bit which sets up any mutations in their DNA. This
is a part of changeling transformation, so I just made it return
instantly.

## Why It's Good For The Game

You can use this ability again without getting stuck permanently as a
monkey, or it just deleting itself from your list of abilities for no
reason.
Turning into a monkey with fake outfit pieces on won't turn you into an
abomination.

## Changelog

:cl:
refactor: Changeling's Lesser Form is now one ability instead of two
which keep swapping, which should consistently turn you back and forth
without deleting itself from your action bar.
fix: Hatching from an egg left by a Last Resort headcrab should
correctly grant you Lesser Form in addition to your other abilities.
fix: Turning into a monkey while using the Changeling space suit won't
leave you as a monkey with a weird inflated head.
qol: Using lesser form as a monkey with only one stored DNA profile will
skip asking which profile you want and will simply transform you
immediately into the only option.
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Urban-Coalition/ArcCW_UR](https://github.com/Urban-Coalition/ArcCW_UR)@[7f3487f04f...](https://github.com/Urban-Coalition/ArcCW_UR/commit/7f3487f04f11366292ceb88ab246878d0c673043)
#### Friday 2023-03-10 18:42:57 by rzen1th

holy jesus god damn motherfucking christ how long was this like that

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[11ea0a44a6...](https://github.com/treckstar/yolo-octo-hipster/commit/11ea0a44a653fb54d05893e051acb8ac98610eb0)
#### Friday 2023-03-10 19:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[ff35822e36...](https://github.com/git-for-windows/git/commit/ff35822e36bc031f3c407fced092e9e24c29dd03)
#### Friday 2023-03-10 19:56:14 by Johannes Schindelin

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
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[ffac8f0df0...](https://github.com/Bubberstation/Bubberstation/commit/ffac8f0df07c8473e26420a8fe3c1acf6bd20dbf)
#### Friday 2023-03-10 20:33:56 by SkyratBot

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
## [NetworkManager/NetworkManager](https://github.com/NetworkManager/NetworkManager)@[b4346fb1f8...](https://github.com/NetworkManager/NetworkManager/commit/b4346fb1f8db486633b79ffbe267686605e5aaea)
#### Friday 2023-03-10 20:53:41 by Thomas Haller

platform: always reconfigure IP routes even if removed externally

NML3Cfg is stateful, that means it remembers which address/route it
configured earlier. That is important because the API users of NML3Cfg
only say what the want to configure now, and NML3Cfg needs to remove
addresses/routes that it configured earlier but are no longer to be
present. Also, NetworkManager wants to allow the user to add
addresses/routes externally with `ip addr|route add` and NetworkManager
not removing it. This is a common use case for dispatcher scripts, but
in general, we want to allow other components to add addresses/routes.

We try something similar with the removal of routes/addresses managed by
NetworkManager. When NetworkManager adds a route/address, which later
disappears, then we assume that the user intentionally removed the
address/route and take the hint to not re-add it.

However, it doesn't work. It is problematic for two reasons:

- kernel can automatically remove routes. For example, deleting an IPv4
  address that is the prefsrc of a route, will cause kernel to delete
  that route. Sure, we may be unable to re-configure the route at this
  moment, but we shouldn't remember indefinitely that the route is
  supposed to be absent. Rather, we should re-add it when possible.

- kernel is a pain with validating consistencies of routes. For example,
  when a route has a nexthop gateway, then the gateway must be onlink
  (directly reachable), or kernel refuses to add it with "Nexthop has
  invalid gateway". Of course, when removing the onlink route kernel is
  fine leaving the gateway route behind, which it would otherwise refuse
  to add.
  Anyway. Such interdependencies for when kernel rejects adding a route
  with "Nexthop has invalid gateway" are non-trivial. We try to work
  around that by always adding the necessary onlink routes. See
  nm_l3_config_data_add_dependent_onlink_routes(). But if the user
  externally removed the dependent onlink route, and NetworkManager
  remembers to not re-adding it, then the efforts from
  nm_l3_config_data_add_dependent_onlink_routes() are ignored. This
  causes ripple effects and NetworkManager will also be unable to add the
  nexthop route.

Trying to preserve absence of routes that NetworkManager would like to
configure is not tenable. Don't do it anymore. There was anyway no
guarantee that on the next update NetworkManager wouldn't try to re-add
the route in question. For example, if the route came from DHCP, and the
lease temporarily went away and came back, then NetworkManager probably
would have (correctly) forgotten that the user wished that the route be
absent. This did not work reliably and it just causes problems.

---
## [Wahab-rgb/Wahab-rgb](https://github.com/Wahab-rgb/Wahab-rgb)@[ea2b1974ea...](https://github.com/Wahab-rgb/Wahab-rgb/commit/ea2b1974ea40b12c9a54eb15774c8e9df5226d74)
#### Friday 2023-03-10 21:22:31 by Wahab-rgb

Add files via upload

Get ready to experience the classic game of Checkers like never before with our new 2D Checkers game, developed using Unity! We've combined the timeless gameplay of Checkers with modern graphics and animations to create an exciting and engaging experience for players of all ages.  In this game, players take turns moving their pieces diagonally across the board, with the goal of capturing their opponent's pieces by jumping over them. The game ends when one player has captured all of their opponent's pieces, or when one player has blocked all of their opponent's pieces from moving.  Our 2D Checkers game offers a variety of game modes to suit every player's preferences. In Single Player mode, players can test their skills against the computer, with difficulty settings ranging from easy to expert. With each game, the computer becomes more challenging, ensuring that players always have a new and exciting challenge to face.  For those who prefer to play with friends, our Multiplayer mode allows players to challenge each other to a game of Checkers. With a simple and intuitive interface, it's easy to invite friends to join a game and start playing right away.  In addition to the classic game of Checkers, our 2D Checkers game also offers several variations to keep things interesting. Players can choose to play the American version of Checkers, which allows pieces to move backwards, or the International version, which does not. They can also choose to play with different board sizes and piece colors, adding even more variety to the game.  To enhance the gameplay experience, we've included a variety of animations and sound effects to make every move feel satisfying. When a piece is captured, it's removed from the board in a dramatic and satisfying animation, and when a player wins the game, a triumphant sound effect plays to celebrate their victory.  Our 2D Checkers game is designed to be accessible and enjoyable for players of all ages and skill levels. With simple and intuitive controls, anyone can pick up the game and start playing right away.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[a3451b7fe4...](https://github.com/lessthnthree/tgstation/commit/a3451b7fe4ff60e0cb6cc4f2bd6d20543f455940)
#### Friday 2023-03-10 21:50:46 by san7890

Makes "forced" opening and closing of doors way more sane (#73699)

## About The Pull Request

The gist is that people thought that this was a boolean value, which was
fucked up. It's not a boolean value, it accepts anything between 0 and
2. So, let's re-arrange the checks and framework, give it some
descriptive defines, just so people know what the fuck "2" actually
does. `DOOR_DEFAULT_CHECKS` (0) does stuff normally,
`DOOR_FORCED_CHECKS` 1 typically just checking if we aren't emagged shut
or something (i suppose it could happen), and `DOOR_BYPASS_CHECKS` (2)
means that we just get the fucking door open if it isn't physically
sealed shut/open somehow.

I don't know if `forced` has ever _been_ a boolean, but for some reason
people thought it was.

I also enforced boolean returns instead of passing back null. This did
not matter for close() but i think it's silly to have a TRUE/null
dichotomy so that was also touched up.
## Why It's Good For The Game

Much better to read, less confusing, less stupid. It's been irritating
me for a while now, so let's just implement it now. Had to make a few
awkward concessions in order to fit this into the current code
framework, but it should be a lot nicer. I also shuffled the order of
some code around because certain placements didn't make any sense (early
returns not being in the right spot for an early return).
## Changelog
Nothing that should concern players.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[db7534d6da...](https://github.com/lessthnthree/tgstation/commit/db7534d6dabf0127c87b291eae4063b6f77d36e4)
#### Friday 2023-03-10 21:50:46 by LemonInTheDark

Lowers nightvision threshold to work for mesons, fixes not being able to examine stuff lit by overlay lights (#73712)

## About The Pull Request

Might be a bit low, but part of that is because it's kinda bad at
figuring color, rgb isn't really balanced in that respect

Fixes not being able to see stuff under the light of a lamp

Overlay lights don't set lumen, which leads to stupid when you try and
check with ONLY it
It worked before because the mob has THEIR luminosity set, which then
"glowed" out

That doesn't work here cause yaknow I removed our uses of byond lighting
(except for errant view() calls) so this is the best I've got

## Why It's Good For The Game

Closes #73548 

## Changelog
:cl:
fix: Examining in the dark is less wonk now, sorry bout that
/:cl:

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[7cc6934eff...](https://github.com/ZephyrTFA/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Friday 2023-03-10 21:58:17 by LemonInTheDark

Visual fixes (lighting, weird shit, old bugs from a parallax thing) (#73555)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Fixes a bug where anything fully dark on the floor plane would mask the
lighting
plane](https://github.com/tgstation/tgstation/commit/a1a03dc3393216098890b971b2271d56cb2c7463)

I fucked it up boys, needed to take alpha into account here

[Fixes pais getting parallax on icebox because their location was
nested](https://github.com/tgstation/tgstation/commit/81252e0f45c53918a14cc0148353ec440710f8e5)

God I hate this place (Note when I say get I mean they got the plane
master that controls it, not that they actually got it displayed. That
does appear to sometimes happen but I have no idea why)

[Fixes double flashlights not activating if enabled in
place](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

[efb8b64](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

cast_directional_light removes the lighting appearance, because it's
gonna modify it, but it turns out because appearances are static when
they're in like underlays/overlays, this could remove the WRONG UNDERLAY

This lead to double held flashlights just... not working until you
rotated. V stupid.

I've also had to move the flag set to make the overlay add in
cast_directional_light work. Depression

## Why It's Good For The Game

Closes #73535, closes #73517, closes #73518, and fixes part of #73471
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
fix: Fixes activating two flashlights without moving only turning on one
flashlight (until you move)
fix: Purely black things drawn on the floor (like carpets, those foam
dispensers, etc) will no longer cause things on top of them to be fully
masked in darkness
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[c914791ecb...](https://github.com/Buildstarted/linksfordevs/commit/c914791ecbc3283e5f00316e76935ba3f8ba1326)
#### Friday 2023-03-10 22:08:59 by Ben Dornis

Updating: 3/10/2023 10:00:00 PM

 1. Added: Finding Contentment in the Internet Age
    (https://josem.co/finding-contentment-in-the-internet-age/)
 2. Added: School, Home
    (https://notes.ekzhang.com/reflections/school-home)
 3. Added: Wrangling JSON Arrays: Zed vs SQL
    (https://www.brimdata.io/blog/wrangling-json-arrays-with-zed/)
 4. Added: The dogma of restful apis
    (https://bower.sh/dogma-of-restful-api)
 5. Added: Teaching is More than Dominoes
    (https://blog.charliemeyer.co/teaching-is-more-than-dominoes/)
 6. Added: OpenAI’s Massive Data Grab
    (https://katedowninglaw.com/2023/03/10/openais-massive-data-grab/)
 7. Added: Plotting constellations
    (https://www.johndcook.com/blog/2023/03/10/plotting-constellations/)
 8. Added: reb00ted | Meta's decentralized social plans confirmed. Is Embrace-Extend-Extinguish of the Fediverse next?
    (https://reb00ted.org/tech/20230310-meta-activitypub/)
 9. Added: On Feature Flags
    (https://truemped.github.io/posts/mgmt/on-feature-flags/)
10. Added: No heroes needed
    (https://rpadovani.com/no-heroes)
11. Added: Spotlight: Starlink, the truth is out there | SamKnows
    (https://www.samknows.com/blog/starlink)
12. Added: How I built and launched PropertyGuessr
    (https://www.fraserhamilton.dev/blog/how-i-built-propertyguessr)
13. Added: Unleash the Power of Self-Hosted Services with Cloudflare Tunnels
    (https://akashrajpurohit.com/blog/unleash-the-power-of-selfhosted-services-with-cloudflare-tunnels/)
14. Added: NYSED says you don't need to know CS to teach CS
    (https://cestlaz.github.io/post/soce/)
15. Added: Exploiting LCD refresh with Arduino
    (https://nwb.sh/exploiting_lcds/)
16. Added: QR Code Generator in Laravel 10 Tutorial
    (https://harrk.dev/qr-code-generator-in-laravel-10-tutorial/)
17. Added: Testing for POSIX compliance with Chimera Linux
    (https://snails.dev/posts/chimera-posix-testing.html)
18. Added: Taking Full Advantage of NoSideEffects, Or What's It Like To Be An Obsessional Researcher
    (https://www.typal.dev/blog-nosideeffects.html)
19. Added: A messy bedroom of thoughts
    (https://areamanm.github.io/2023/03/10/A-messy-bedroom-of-thoughts.html)
20. Added: The beauty of hurrying slowly
    (https://robert.bearblog.dev/the-beauty-of-hurrying-slowly/)
21. Added: Modern iOS Navigation Patterns · Frank Rausch
    (https://frankrausch.com/ios-navigation)
22. Added: From Metadata to Event block in nettrace format
    (https://chnasarre.medium.com/from-metadata-to-event-block-in-nettrace-format-90763a186dd5?sk=cdf7491e088a3f74d791ff7e132806c0)
23. Added: Introduction to the Community Toolkits for .NET and Windows
    (https://youtube.com/watch?v=wG67xSIlask)

Generation took: 00:08:47.9758640

---
## [DawfukFR/stellaris_kernel_oneplus_sm8250](https://github.com/DawfukFR/stellaris_kernel_oneplus_sm8250)@[5dc958bac8...](https://github.com/DawfukFR/stellaris_kernel_oneplus_sm8250/commit/5dc958bac819c036f199c923aaf4555e0465a5bb)
#### Friday 2023-03-10 22:14:14 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Co-authored-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[Tashar02: forwardport and adapt to 4.19 and xiaomi_sdm660's fp]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [RealOrko/revolut](https://github.com/RealOrko/revolut)@[80ebcc0835...](https://github.com/RealOrko/revolut/commit/80ebcc083560f453da5e64b29b32d789c8547215)
#### Friday 2023-03-10 22:22:01 by Gavin van der Merwe

Local development workflow complete

There are a couple of things I would like the reviewer to note whilst going through this:

 1. My choice of using dotnet 6 was probably a bad idea (after not doing it for 5/6 years this really hurt)

    It took me way longer to battle through the framework changes than I could remember to meet the requirements
    for the development of the API. This was by no means a 5 hour task. I also believe this would have been rather
    arduous using any statically typed language eg. Java Springboot.

    Also if I used a dynamically typed language like NodeJs, Python or Ruby I feel I would have been marked down
    from an SRE point of view as a potential candidate because the runtimes simply do not scale beyond the bounds
    of CSharp, Java, GoLang or Rust.

 2. This take home test requires a severe amount of unit testing already when it comes to dates alone and
    validating the API inputs/outputs visa vi models.

    Bringing a persistance store into the mix is perhaps too much? Especially when it comes to deployment concerns.
    Saying this should take 5 hours "including SRE concerns" is a bit unrealistic. How would I build all of the
    testing "goodness" based on the testing pyramid in 5 hours? Clocking 12 hours at the time of commit? If your
    conclusion is that I am "not good enough", then I probably do not want to work for your company. It tells me
    there is a serious lack of skills/maturity when it comes to hiring "best of breed" talent in your organisation.
    I have rebuilt infra teams without this development drama.

 3. Producing a system diagram for my "current build" should not be required. If in doubt there is always the
    AWS/Azure/OCI/IBM good or well architected guides. They always change as their products evolve.
    Reading my CV should be enough? I would obviously deploy this into an "enterprise grade" kubernetes cluster.
    No diagram would tell you that anyway?

 4. Deploying to the cloud? I think this is most upsetting part of this test. I have to waste my time and money to
    create a deployment that not only addresses development concerns but SRE concerns? Are you kidding me? 5 hours.

Summary

I am not happy I took on this test nor will I complete it. I resent the fact that I have to pay for my own compute
to test it, then try and read your mind as to how you will evaluate it. You probably wont even try to deploy it anyway.

---
## [abyteintime/stitchkit](https://github.com/abyteintime/stitchkit)@[fd62f3d1f3...](https://github.com/abyteintime/stitchkit/commit/fd62f3d1f3445bc826928762b6b6cc7236e670bb)
#### Friday 2023-03-10 22:40:03 by liquidev

some more dumb class specifiers

yeah epic why not invent a generic mechanism when you have that many for god's sake

---

