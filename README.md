## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-22](docs/good-messages/2023/2023-07-22.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,870,377 were push events containing 2,657,897 commit messages that amount to 163,839,162 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 50 messages:


## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[171b1478f9...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Saturday 2023-07-22 00:02:22 by vampirebat74

Limbus Company E.G.O dump (#1062)

* Adds roseate desire

roseate sfx

datums

weapons

add aedd

sprite adjustments

unfucks suits

new sfx

name fix

aaaa

adds capote

adds sloshing

farmwatch

farmwatch suit

stuff

farmwatch stuff

capote inhands

red sheet finished

sloshing gift

linters

Stuff

stuff

fixes shit

stuff

weapon code cleanup

spicebush finished

removes the heal

code fix

stuff

removes reference

farmwatch hat

new vfx

requested changes

* block duration

---------

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[8d669c5514...](https://github.com/git-for-windows/git/commit/8d669c5514e853f9f00517bfda13ff5225b2052f)
#### Saturday 2023-07-22 00:05:33 by Johannes Schindelin

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
## [MemedHams/Shiptest](https://github.com/MemedHams/Shiptest)@[f07cb3bd3b...](https://github.com/MemedHams/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Saturday 2023-07-22 00:52:03 by Bjarl

Overmap 4.7: Gas Giants, More Storms, 8 hours of work (#1997)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds some content based on sprites I saw sitting around in the overmap
file, mainly carp storms and dust storms.
Carp storms throw space carp at you. Dust storms throw dust.

Also adds gas giants, a place to harvest gasses if you're low, and don't
want to stop at a planet. They *should* be persistent. Your average gas
giant mix is very cold, very high pressure, and absolutely not something
you want to breathe. Plasma giants are cold and allow harvesting of
plasma.

Electrical storms have been rebalanced to not Explode Your Ship. Minor
and Moderate ones will now only shock and damage objects and mobs, major
ones will still explode you, so remain careful.



![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/84257435-32de-45a5-8a8d-d9aa30021f90)
Example overmap with some carp migrations.


https://github.com/shiptest-ss13/Shiptest/assets/94164348/5c30fa9a-c7e4-453a-99a6-5c3564946b26
flying through a minor electrical storm


https://github.com/shiptest-ss13/Shiptest/assets/94164348/db7fcdf0-3f7a-4830-821e-a4a7106632ba
gas giant


https://github.com/shiptest-ss13/Shiptest/assets/94164348/0a5f0575-b7d9-4e3f-9e13-942a8fdf8617

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/6bb5ddc2-373a-4dd9-9a63-0f6f0bdd26a9)

plasma giant

https://github.com/shiptest-ss13/Shiptest/assets/94164348/9268c293-39f3-4306-889e-f8c19067cec1

A particularly dusty solar system

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/5b27e2a8-1cc1-47bb-95b8-e9d5c3ba8e71)


I might try and fix ion storms but I don't see what might be breaking
them.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More content for the overmap / balancing out some old systems
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Planets now can (and will) play a sound when you land on them
add: Gas / Plasma giants, cold, dockable worlds with absolutely no
livable surfaces. As a matter of fact it's all chasm. All highly
pressurized, gas rich, chasm.
add: Dust storms and carp storms now grace the sector. 
add: physical storms (dust, carp, asteroid), will now only trigger if
you go through them too fast. Take it easy and you might get through
unscathed.
add: planets will now have a name on the overmap
add: overmap hazards now have a description
tweak: Space carp can now survive in hyperspace, their natural habitat
balance: minor and moderate electrical storms will no longer Explode you
balance: asteroid storm lists have been trimmed of Extremely Deadly ones
fix: restores planet naming behavior, I believe this was unintentionally
removed at some point
fix: Ion storms work again. Fuck you whoever touched them last.
soundadd: planet_landing_1 and planet_landing_2, (tech_notification and
sos_morse_code from CM respectively. I don't know how to attribute
properly please tell me how if you have issue with this attribution
because I did not make these sounds they're from Colonial Marines)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[08c90f2116...](https://github.com/Sonic121x/Skyrat-tg/commit/08c90f211652f33a431ee9d7cdc317fb71e981b7)
#### Saturday 2023-07-22 01:14:40 by SkyratBot

[MIRROR] [MDB IGNORE] Angled Lights & Lighting Prototyping Tool  [MDB IGNORE] (#22582)

* [MDB IGNORE] Angled Lights & Lighting Prototyping Tool  (#74365)

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

Co-authored-by: MMMiracles <lolaccount1@ hotmail.com>

* [MDB IGNORE] Angled Lights & Lighting Prototyping Tool

* Update north_star.dmm

* Revert "Update north_star.dmm"

This reverts commit bb5b8b5a549f7edc3e23a369a147ed96bab41991.

* Updatepaths

* Update nukie_base.dmm

* Newer version of northstar with the penguins

* Update northstar_cryo.dmm

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: MMMiracles <lolaccount1@ hotmail.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [fw-ai-external/evals](https://github.com/fw-ai-external/evals)@[640a032362...](https://github.com/fw-ai-external/evals/commit/640a032362e8d5264bd773790ad6dc9bfe371a9b)
#### Saturday 2023-07-22 01:32:05 by oscar

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
## [fw-ai-external/evals](https://github.com/fw-ai-external/evals)@[fb73e86b97...](https://github.com/fw-ai-external/evals/commit/fb73e86b97ff4748b9b489cdb2ae665745f22ecf)
#### Saturday 2023-07-22 01:32:05 by Juyeon Yoon

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
## [fw-ai-external/evals](https://github.com/fw-ai-external/evals)@[1f67052669...](https://github.com/fw-ai-external/evals/commit/1f670526696fc31cb89dc43a9fd1321c5d068b4b)
#### Saturday 2023-07-22 01:32:05 by Chen Zhao

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
## [fw-ai-external/evals](https://github.com/fw-ai-external/evals)@[f48dc50cd7...](https://github.com/fw-ai-external/evals/commit/f48dc50cd776bdc182cf7cb65f7020fcd9e4b9df)
#### Saturday 2023-07-22 01:32:05 by robin luo

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
## [fw-ai-external/evals](https://github.com/fw-ai-external/evals)@[427f7c0623...](https://github.com/fw-ai-external/evals/commit/427f7c06239369f648876d8d7296e35d03a3bc09)
#### Saturday 2023-07-22 01:32:05 by jjyuhub

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
## [fw-ai-external/evals](https://github.com/fw-ai-external/evals)@[33d5c86eea...](https://github.com/fw-ai-external/evals/commit/33d5c86eea0320fda79075b1a7430bc9c22d234c)
#### Saturday 2023-07-22 01:32:05 by Syed Rishad

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
## [fw-ai-external/evals](https://github.com/fw-ai-external/evals)@[7a4d72edc3...](https://github.com/fw-ai-external/evals/commit/7a4d72edc394e0bdc77a89e481ea4be1c643b820)
#### Saturday 2023-07-22 01:32:05 by Lorenzo

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
## [fw-ai-external/evals](https://github.com/fw-ai-external/evals)@[5211455d65...](https://github.com/fw-ai-external/evals/commit/5211455d659624ae3e1fa3bdeab5123f53ee2294)
#### Saturday 2023-07-22 01:32:05 by Sean Bird

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
## [A-Noid33/mame](https://github.com/A-Noid33/mame)@[2bdde3e05c...](https://github.com/A-Noid33/mame/commit/2bdde3e05c73b25593defb29d5ee021d139428ef)
#### Saturday 2023-07-22 01:33:18 by Bob Schultz

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
## [uCZMG/Web-Environment-Integrity](https://github.com/uCZMG/Web-Environment-Integrity)@[48f40de76f...](https://github.com/uCZMG/Web-Environment-Integrity/commit/48f40de76f76a72236293fce12f9d1331a2eeb88)
#### Saturday 2023-07-22 01:34:25 by CZMG

improve spec

My name is Walter Hartwell White. I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If you're watching this tape, I'm probably dead, murdered by my brother-in-law Hank Schrader. Hank has been building a meth empire for over a year now and using me as his chemist. Shortly after my 50th birthday, Hank came to me with a rather, shocking proposition. He asked that I use my chemistry knowledge to cook methamphetamine, which he would then sell using his connections in the drug world. Connections that he made through his career with the DEA. I was... astounded, I... I always thought that Hank was a very moral man and I was... thrown, confused, but I was also particularly vulnerable at the time, something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me on a ride along, and showed me just how much money even a small meth operation could make. And I was weak. I didn't want my family to go into financial ruin so I agreed. Every day, I think back at that moment with regret. I quickly realized that I was in way over my head, and Hank had a partner, a man named Gustavo Fring, a businessman. Hank essentially sold me into servitude to this man, and when I tried to quit, Fring threatened my family. I didn't know where to turn. Eventually, Hank and Fring had a falling out. From what I can gather, Hank was always pushing for a greater share of the business, to which Fring flatly refused to give him, and things escalated. Fring was able to arrange, uh I guess I guess you call it a "hit" on my brother-in-law, and failed, but Hank was seriously injured, and I wound up paying his medical bills which amounted to a little over $177,000. Upon recovery, Hank was bent on revenge, working with a man named Hector Salamanca, he plotted to kill Fring, and did so. In fact, the bomb that he used was built by me, and he gave me no option in it. I have often contemplated suicide, but I'm a coward. I wanted to go to the police, but I was frightened. Hank had risen in the ranks to become the head of the Albuquerque DEA, and about that time, to keep me in line, he took my children from me. For 3 months he kept them. My wife, who up until that point, had no idea of my criminal activities, was horrified to learn what I had done, why Hank had taken our children. We were scared. I was in Hell, I hated myself for what I had brought upon my family. Recently, I tried once again to quit, to end this nightmare, and in response, he gave me this. I can't take this anymore. I live in fear every day that Hank will kill me, or worse, hurt my family. I... All I could think to do was to make this video in hope that the world will finally see this man, for what he really is.

---
## [N3D6/YogstationIfItWasntMid](https://github.com/N3D6/YogstationIfItWasntMid)@[38b3114cd7...](https://github.com/N3D6/YogstationIfItWasntMid/commit/38b3114cd7fb5d1212ca64049cf34165611f8c76)
#### Saturday 2023-07-22 01:55:59 by N3D6

Merge remote-tracking branch 'upstream/master' into asteroid-decals-fuck-you-edition

---
## [2Pako/CustomerFeedbackDataset](https://github.com/2Pako/CustomerFeedbackDataset)@[5b70e7ba75...](https://github.com/2Pako/CustomerFeedbackDataset/commit/5b70e7ba754031a8db3d6f69ec0a0273f0a10ad4)
#### Saturday 2023-07-22 02:12:36 by Francisco

Customer Feedback Dataset
This dataset contains customer sentiments expressed in various sources such as social media, review platforms, testimonials, and more. The dataset includes text, sentiment (positive or negative), source of the sentiment, date/time of the sentiment, user ID, location, and confidence score. The sentiments reflect customers' opinions and experiences with products, services, movies, music, books, restaurants, websites, customer support, and more.

Will be using this dataset to practice cleaning data

First Step is to import the needed libraries.
import pandas as pd # data processing
import numpy as np # linear algebra
​
​
Second step is to read the data
data = pd.read_csv("sentiment-analysis.csv")
data.head(20)
Text, Sentiment, Source, Date/Time, User ID, Location, Confidence Score
0	"I love this product!", Positive, Twitter, 202...
1	"The service was terrible.", Negative, Yelp Re...
2	"This movie is amazing!", Positive, IMDb, 2023...
3	"I'm so disappointed with their customer suppo...
4	"Just had the best meal of my life!", Positive...
5	"The quality of this product is subpar.", Nega...
6	"I can't stop listening to this song. It's inc...
7	"Their website is so user-friendly. Love it!",...
8	"I loved the movie! It was fantastic!", Positi...
9	"The customer service was terrible.", Negative...
10	"This book made me feel inspired. Highly recom...
11	"I'm extremely disappointed with their product...
12	"Just had the most amazing vacation! I can't w...
13	"The food at this restaurant was awful. Never ...
14	"I can't stop listening to this song. It's my ...
15	"Their website is so confusing and poorly desi...
16	"I had an incredible experience at the theme p...
17	"The product arrived damaged. Very disappointe...
18	"The concert was absolutely breathtaking. Best...
19	"I had a terrible experience with their custom...
We Can start to Clean this Data
First we should see the dimensions of the data and if we have any null values.

data.info
<bound method DataFrame.info of    Text, Sentiment, Source, Date/Time, User ID, Location, Confidence Score
0   "I love this product!", Positive, Twitter, 202...
1   "The service was terrible.", Negative, Yelp Re...
2   "This movie is amazing!", Positive, IMDb, 2023...
3   "I'm so disappointed with their customer suppo...
4   "Just had the best meal of my life!", Positive...
..                                                ...
93  "I can't stop listening to this song. It's my ...
94  "Their website is so confusing and poorly desi...
95  "I had an incredible experience at the theme p...
96                                                NaN
97                                                NaN

[98 rows x 1 columns]>
dataN = data.dropna()
dataN.info
<bound method DataFrame.info of    Text, Sentiment, Source, Date/Time, User ID, Location, Confidence Score
0   "I love this product!", Positive, Twitter, 202...
1   "The service was terrible.", Negative, Yelp Re...
2   "This movie is amazing!", Positive, IMDb, 2023...
3   "I'm so disappointed with their customer suppo...
4   "Just had the best meal of my life!", Positive...
..                                                ...
91  "Just had the most amazing vacation! I can't w...
92  "The food at this restaurant was awful. Never ...
93  "I can't stop listening to this song. It's my ...
94  "Their website is so confusing and poorly desi...
95  "I had an incredible experience at the theme p...

[96 rows x 1 columns]>
A total of 2 values were NAN or null. The .dropna() function removed these. As a reminder, do not alter the raw data

Unravel the Data
Now that the null values have been dropped we can separate into columns

The columns are separated by ",". Will have to separate these as such.

NewData = pd.DataFrame(columns = ["Text", "Sentiment", "Source", "Date/Time", "User ID", "Location", "Confidence Score"])
for i in dataN.index:
    aux = dataN.iloc[i, 0].split(",")
    NewData.loc[len(NewData)] = aux
NewData.head(5)
Text	Sentiment	Source	Date/Time	User ID	Location	Confidence Score
0	"I love this product!"	Positive	Twitter	2023-06-15 09:23:14	@user123	New York	0.85
1	"The service was terrible."	Negative	Yelp Reviews	2023-06-15 11:45:32	user456	Los Angeles	0.65
2	"This movie is amazing!"	Positive	IMDb	2023-06-15 14:10:22	moviefan789	London	0.92
3	"I'm so disappointed with their customer suppo...	Negative	Online Forum	2023-06-15 17:35:11	forumuser1	Toronto	0.78
4	"Just had the best meal of my life!"	Positive	TripAdvisor	2023-06-16 08:50:59	foodie22	Paris	0.88
This is now separated. Will need to ensure we have no null values.

NANDATA= NewData.notnull()
NANDATA.info
<bound method DataFrame.info of     Text  Sentiment  Source  Date/Time  User ID  Location  Confidence Score
0   True       True    True       True     True      True              True
1   True       True    True       True     True      True              True
2   True       True    True       True     True      True              True
3   True       True    True       True     True      True              True
4   True       True    True       True     True      True              True
..   ...        ...     ...        ...      ...       ...               ...
91  True       True    True       True     True      True              True
92  True       True    True       True     True      True              True
93  True       True    True       True     True      True              True
94  True       True    True       True     True      True              True
95  True       True    True       True     True      True              True

[96 rows x 7 columns]>
This concludes the Data Clean up for Python. While more can be done, this was not the goal for this project. Will Continue in Tableau.
NewData.to_csv('CFD_Clean_Data.csv')
​

---
## [Bri-ishMan/mystation](https://github.com/Bri-ishMan/mystation)@[988a6dcc21...](https://github.com/Bri-ishMan/mystation/commit/988a6dcc2142b4ef3244a18ad4e1781671fb7320)
#### Saturday 2023-07-22 03:17:05 by YehnBeep

Removes suicide check from positronic brains (#76081)

# About The Pull Request

This removes the suicide check from positronic brains.

# Why It's Good For The Game

There seems to be 2 arguments for why suicide should forbid ghost roles:
1. "If they suicided they didn't want to play"
2. "antag rolling"

So let's look at each.

And an addendum on scope: This is meant only to apply to ghost roles
(and new characters from said roles); I do not wish to change that
people are not allowed back onto the same character they suicided on.

## "Suiciders left the round of their own choice and shouldn't be
allowed back in"

There are many, many ways in this game to end up with a character in a
state that's nearly/effectively unplayable, even if the controlling
player doesn't truly wish to completely leave. Some things can be
resolved with competent medical or science staff, but competent staff
are not always available in a round or might be beleaguered by round
events.

Then there are a number of conditions/states which the game provides no
path to resolve (save drastic measures like abandoning the
character/body, of course).

Or one might have simply become stuck in a place where rescue is
unlikely.

## Antag rolling

The problem here is this code does not particularly target antag
rollers. It paints such a broad brush that it simply catches everyone
whom might not know "No no, you have to **ghost** here, not suicide".
Even if an antag roller is stopped once, they'll easily bypass it next
time through the many, many means open to them - and if 'ghost' is made
effectively the same as 'suicide', it simply punishes people who got
stuck or similar even more.

Because of the wide range of means to kill oneself on a normal
character, to effectively stop antag rolling requires discerning intent
through context and patterns of one's actions. This might not be
possible in code until General Intelligence is a solved problem, and if
it is possible, this doesn't do it. It's a shotgun that kills everyone
in the room and if there happened to be an antag roller there, well,
even a stopped clock is right twice a day.

And then, of course, that the code was broken for so long would seem to
indicate it's not done that much.

## Practical Impact and Design Philosophy

Just from my personal observations, even wanting into a posibrain is a
niche thing usually only taken by a small number of the same players
round-to-round. In practice, whether this PR is merged or not likely
won't have a great impact on the game. But that could change if the
philosophy behind this check is applied to a wider number of things.

If someone wants to die, it's not hard. Walk out an airlock. Into the
supermatter. Blob, Xenos, or some other hazard present? Walk towards
them. Step in front of a shuttle. Turn on internals and wait a bit.
Countless other ways. Except, perhaps, if a character is disabled or
crippled or stuck, in which case use of a verb may be necessary.

In other games with much narrower sets of mechanics, it may be possible
to close certain paths on the assumption it would mostly be used for bad
faith reasons. In SS13, the sheer number of ways in which a good faith
character be "screwed" but not quite killed off, and which a bad faith
actor can find to kill themselves while bypassing restrictions placed on
verbs, means that I think this code's design philosophy is harmful to
the game and its good faith players.

# Changelog

:cl:
del: Positronic brains no longer check for suicide verb use.
/:cl:

---
## [Bri-ishMan/mystation](https://github.com/Bri-ishMan/mystation)@[803658dc30...](https://github.com/Bri-ishMan/mystation/commit/803658dc30b4445e81592daa1823a98719246269)
#### Saturday 2023-07-22 03:17:05 by Rhials

Deadchat Announcement Variety Pack 2 and also some fixes to other popups (#76053)

## About The Pull Request

This adds ghost orbit popups for the following: 
- Macrobombs (or stacked microbombs) being triggered.
- HFR Meltdowns.
- Living players about to be gored by an emagged organ harvester.
- Nuclear devices being armed.
- Doomsday devices.
- Blob hosts bursting.

This also modifies the following ghost orbit popups:
- Toy hot potatoes will no longer cause a popup when armed.
- Normal spider eggs will not flash the byond window, only special egg
types.
## Why It's Good For The Game

Gives more gathering spots/information to deadchat. Let no entertaining
moment in this game go unobserved.

Spider eggs flashing your window for every single egg produced makes
alt-tabbing suck. I saw some guy on the forums complaining about it and
thought "huh yeah I guess he's got a point that pisses me off too" so
here we are.
## Changelog
:cl: Rhials
qol: Basic spider eggs no longer flash the byond window when ready to
hatch.
qol: Toy hot potatoes no longer give a ghost notification.
qol: Deadchat will be notified in the event of an imminent macrobomb
detonation, HFR meltdown, organ harvesting,
qol: Deadchat will be notified when a nuclear/doomsday device is
activated, as well as when a blob-infection bursts.
/:cl:

---
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[e9eccf3b0b...](https://github.com/ss220club/Skyrat-tg/commit/e9eccf3b0bc57137a03ee319b0e081e78a8b06ed)
#### Saturday 2023-07-22 03:18:10 by SkyratBot

[MIRROR] Removes the word "chemical" from "chemical patch" [MDB IGNORE] (#22610)

* Removes the word "chemical" from "chemical patch" (#76966)

## About The Pull Request
In #76011, I bitched and moaned about how the ChemMaster gives patches a
huge ass name. I've talked to other Medical Doctor mains and I also
heard bitching about the word "chemical", which is just a pain in the
ass. It seems many of us just end up removing it because it's so
repetitive and makes the patch's name long fnr. I don't think the word
"chemical" is really needed in there since you can clearly tell it's a
chemical patch just by looking at the word "patch" and the sprite.

I don't think this should affect anything else in the game in a negative
way. In that same issue, it was suggested that the cap for names was
increased instead, but this also solves the issue of the word "chemical"
taking up so much space in the patch's name without touching unknown
lands.
## Why It's Good For The Game
Less words, more healing!
## Changelog
:cl:
qol: The word "chemical" has been removed from "chemical patch" when
printing patches
/:cl:

* Removes the word "chemical" from "chemical patch"

---------

Co-authored-by: Justice <42555530+Justice12354@users.noreply.github.com>

---
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[606f0009a1...](https://github.com/ss220club/Skyrat-tg/commit/606f0009a1b61472a534b3dbc7e618680b292f55)
#### Saturday 2023-07-22 03:18:10 by SkyratBot

[MIRROR] Removes two redundant components [MDB IGNORE] (#22613)

* Removes two redundant components (#76866)

## About The Pull Request

We're starting to get to have enough components that people don't
realise that what they want already exists but doesn't have the name
they expect 🙃

I recently added `track_hierarchical_movement` which is similar enough
to `connect_containers` that it shouldn't independently exist, even if I
like sending a new signal more than the ugly setup pattern for
`connect_loc`.

`trait_loc` is actually older than `give_turf_traits` but
`give_turf_traits` covers more edge cases than `turf_loc` so seems like
the better one to maintain.
HOWEVER `give_turf_traits` held a list of references to atoms in it,
which isn't great in an element. I couldn't think of a way to completely
eliminate the list, but it isn't a list of references any more so it
shouldn't cause any hard deletions.

## Why It's Good For The Game

Having two components which do the same thing but marginally differently
is confusing and going to cause us trouble down the line.

## Changelog

Not player facing

* Removes two redundant components

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[16cecf864d...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Saturday 2023-07-22 03:18:20 by Jacquerel

Goliath basic mob (#76754)

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

---
## [Rexicon226/SpaceWarp](https://github.com/Rexicon226/SpaceWarp)@[0bf9fdaa8c...](https://github.com/Rexicon226/SpaceWarp/commit/0bf9fdaa8c63352e5279a7d27a1d2ac997d46b8d)
#### Saturday 2023-07-22 06:14:17 by David

Fix the spacing issue in the modlist

Yeah, I think this is the correct solution. To be honest the manager code is fucking dark magic. Please comment if there is anything dumb about this. It works though, at least as far as I can tell!

---
## [Rexicon226/SpaceWarp](https://github.com/Rexicon226/SpaceWarp)@[c554bd8b4e...](https://github.com/Rexicon226/SpaceWarp/commit/c554bd8b4e8d4f3c16ee58d2f5b31120b4c5d6e5)
#### Saturday 2023-07-22 06:14:17 by David

a much better builder :3

Dear fellow developers and collaborators, I humbly come before you with a sincere plea for forgiveness for the quality of my recent code. I fully acknowledge and deeply regret the shortcomings and mistakes in my implementation. I understand that my code may have caused inconveniences and difficulties, and I am truly sorry for any frustration it may have caused. I assure you that I am committed to improving my skills and knowledge, and I am eager to learn from your expertise and guidance. Please grant me the opportunity to make amends and contribute positively to our shared goals. Thank you for your understanding and kindness in this matter.

---
## [Clownsw/rust-analyzer](https://github.com/Clownsw/rust-analyzer)@[994f4f6e2e...](https://github.com/Clownsw/rust-analyzer/commit/994f4f6e2e45bef4bebeeabee4e3d67b87727b91)
#### Saturday 2023-07-22 07:24:17 by bors

Auto merge of #15290 - igorskyflyer:igorskyflyer-dx-install-extension, r=lnicola

editor/code: [DX] Use notification command links for debugger installation

This PR improves DX (developer experience) when installing the VS Code extension for the first time. When doing so and trying to debug a Rust file, we get an error notification that either CodeLLDB or C++ extension/debugger should be installed (see image below).

<div align="center">
	<img src="https://github.com/rust-lang/rust-analyzer/assets/20957750/e8ebeb1e-85f4-44e2-b79f-c48cf52e5f36" alt="Rust, prompt to install debug extension">
</div>

The PR enhances the links in the given notification and upon clicking instead of opening the Web page of the extension it installs the extension immediately, without the need to leave the editor.

Note: the feature needs to be refined, maybe an "install in progress" message or something similar, I left that for you guys to decide and implement. I think it also possible to first open the sidebar, open the Extensions tab, then run the extension installation command which would make it more user-friendly.

P.S. it is also possible to open the extension's details in VS Code directly via the same links and then the user would have to manually click on the Install button - if installation is not the desired behavior.

Happy coding! 🎉

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[4aec91cc06...](https://github.com/AnywayFarus/Skyrat-tg/commit/4aec91cc069b1beb1ec6593522dc5f65f7c5c7aa)
#### Saturday 2023-07-22 07:44:49 by GoldenAlpharex

[MANUAL MIRROR] Fixes carbon bodytypes not always being synchronized with bodyparts + Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused [MDB IGNORE] (#22519)

* Fixes carbon bodytypes not always being synchronized with bodyparts (#76522)

Fixes https://github.com/tgstation/tgstation/issues/76481
TLDR /mob/living/carbon/human/species subtypes were NOT updating their
bodytypes on spawn due to absurd and wacky carbon bodypart creation code
that meant try_attach_limb() never got called (What the FUCK?)

* Fixes CI too

* [NO GBP] Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused (#76500)

## About The Pull Request

TRAIT_LIVERLESS_METABOLISM should do what it implies, and make you
always metabolize as if you were liverless.
This was a stupid mistake on my part because I wasn't aware
TRAIT_STABLELIVER was a thing.

## Why It's Good For The Game

TRAIT_LIVERLESS_METABOLISM and TRAIT_STABLELIVER should not behave the
exact same.

## Changelog

Not quite player facing.

* I fucking swear I fixed this before

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [janvee-singh/Google-GirlHackathon-Ideathon-Finale-Round](https://github.com/janvee-singh/Google-GirlHackathon-Ideathon-Finale-Round)@[4d1ba37458...](https://github.com/janvee-singh/Google-GirlHackathon-Ideathon-Finale-Round/commit/4d1ba37458344477b943d1acd455a796f7e25c0a)
#### Saturday 2023-07-22 08:10:54 by Janvee Singh

Add files via upload

I am incredibly grateful for this remarkable achievement as I was one of the finalist in Google Girl Hackathon 2023. This year the Hackathon comprised 3 learning cohorts, and I had the privilege of being part of the networking and troubleshooting cohort.

During the Ideathon Finale round, I had the opportunity to present my idea on designing a highly secure, reliable, and scalable fintech application. Throughout the process, I gained invaluable knowledge and skills that have expanded my horizons. This describes my journey so far.

---
## [Anujaraktate/Data_Analysis_on_Electric_Vehicle](https://github.com/Anujaraktate/Data_Analysis_on_Electric_Vehicle)@[cbece4223c...](https://github.com/Anujaraktate/Data_Analysis_on_Electric_Vehicle/commit/cbece4223ca99b19e5b39ab27d9ce390f2c5b7e8)
#### Saturday 2023-07-22 08:17:32 by Anuja Raktate

Add files via upload

During this hackathon, I had the opportunity to work on an engaging Data Analysis project focusing on Electric Vehicles (EVs). 🚗💨 Exploring a comprehensive dataset of EVs, I leveraged Python's Plotly library to conduct extensive Exploratory Data Analysis (EDA). 📊📈 The goal was to gain valuable insights into the trends and patterns in EVs' adoption and characteristics.

The analysis involved univariate and bivariate visualizations, showcasing the distribution of Electric Vehicle Types, Electric Range, Base MSRP, and more. 📍 Additionally, I crafted an interactive Choropleth map to visualize the geographic distribution of EV vehicles based on location, highlighting EV adoption across different cities and states. 🗺️

One of the most exciting aspects of this project was creating a captivating Racing Bar Plot! 🏎️📊 This animated visualization showcased the evolution of EV Makes and their counts over the years, providing a dynamic look at the fast-paced development of the EV industry. 🚀

It was an enriching experience to delve into the world of data-driven insights and apply Python programming skills to bring the data to life. 🐍💡 I'm grateful to Innomatics Research Labs for organizing this hackathon and providing an excellent platform to sharpen our data analysis and visualization abilities.

---
## [Fluffy-Frontier/FluffySTG](https://github.com/Fluffy-Frontier/FluffySTG)@[54ce0ae44a...](https://github.com/Fluffy-Frontier/FluffySTG/commit/54ce0ae44ae9c1534fe4e4917a7be0e83a69d589)
#### Saturday 2023-07-22 08:39:25 by SkyratBot

There is no longer a 50% chance of catching a heretic out when examining them drawing influences [MDB IGNORE] (#22532)

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[1d28964d37...](https://github.com/cmss13-devs/cmss13/commit/1d28964d37f9b95773580cca3471a2a4f5c03eb0)
#### Saturday 2023-07-22 08:40:44 by naut

New blood bags (#3961)

# About the pull request

Since we're putting so much emphasis on blood bags lately, I figured I
might as well do my part as spriter and add actual _labels_ to the
things so you can tell what they are at a glance. Also overhauled the
system to use overlays and underlays instead of the cursed
`full/half/empty` thing that it had going beforehand.

# Explain why it's good for the game

You now no longer have to manually inspect blood bags to tell what type
they are! Rejoice.

# Testing Photographs and Procedure
<img width="251" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/55491249/c4424ec3-bfe6-4d58-8915-595b468a7606">

_Blood bags in action. Sort of. Yes, they actually change color now._

<img width="571" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/55491249/3b478c65-54b9-4321-bf02-dcfacaf1ad23">

_Icon states! Also sprinkled in some yet-unused labels for future
use(TM). AB types are here, too, because I forgot they weren't in the
game._
# Changelog

:cl: nauticall
imageadd: Resprited blood bags to look nicer and use proper a proper
overlay/underlay system. Their types are also now distinguishable at a
glance.
code: Reworked the way blood bag sprites work behind the scenes to use
the overlay/underlay system.
/:cl:

---
## [mearaj/gio](https://github.com/mearaj/gio)@[6ea4119a3c...](https://github.com/mearaj/gio/commit/6ea4119a3ceb36f009af1486e41b47f08c2239bd)
#### Saturday 2023-07-22 09:58:27 by Chris Waldon

text,widget: [API] implement consistent, controllable line height

This commit ensures that any given paragraph of text shaped by Gio will use a single
internal line height. This line height is determined (by default) by the text size,
rather than the fonts involved. This is a breaking change, as previously we would
blindly use the largest line height of any font in a line for that line, leading to
lines within the same paragraph with extremely uneven spacing. This commit also
updates some test expectations in package widget.

I thought pretty hard about how to implement line spacing, and consulted a few sources:

[0] https://www.figma.com/blog/line-height-changes/
[1] https://practicaltypography.com/line-spacing.html
[2] https://developer.mozilla.org/en-US/docs/Web/CSS/line-height

There is no single, universal way to think about line spacing. Fonts internally specify
a line height as the sum of their ascent, descent, and gap, but the line height of two
fonts at the same pixel size (say 20 Sp) can vary wildy (especially across writing systems).
There are two strategies we could pursue to establish the line height of a paragraph of text:

- derive the line height from the fonts involved (our old behavior, and the behavior of
  many word processors)
- derive the line height from the requested text size provided by the user (the behavior of the
  web).

The challenge with the first option is that for a given piece of text in the UI, there can
be a silly number of fonts involved. If a label dispays user-generated content, the user can
put an emoji in it, and emoji fonts have different line heights from latin ones. This can cause
unexpected and nasty layout shift. Gio would previously do exactly this, on a line-by-line basis,
resulting in unevenly spaced lines within a paragraph depending on which fonts were used on
which lines. Choosing one of the fonts and enforcing its line height would make things consistent,
but it isn't clear how to choose that canonical font. There is no 1:1 mapping between the input
text.Font provided in the shaping parameters and a single font.Face. Instead, that mapping depends
upon the runes being shaped.

I think the only sane way to implement the first option would be to synthesize some text in the
provided system.Locale (mapping the language to a script and then generating a rune from that
script), shape that single rune, and then enforce the line height of the resulting face on the
entire paragraph. This would require doing a fair bit more work per paragraph than Gio does today,
so I've opted not to do it.

Instead, the second option allows us to choose a line height based on the size of the text that
the user wants to display. While this can potentially interact poorly with unusually tall fonts,
it means that text will always have a consistent line height.

I've provided two knobs to control line height:

- text.Parameters.LineHeight lets you set a specific height in pixels with a default value of
  text.Parameters.PxPerEm.
- text.Parameters.LineHeightScale applies a scaling factor to the LineHeight, allowing you to
  easily space out text without hard-coding a specific pixel size. The default value here
  (drawn from the recommendations of [1]) is 1.2, which looks pretty good across many fonts.

I've chosen this two-value API because many users will want to set one or the other value. I
considered instead a single value field and a "mode" that would specify how it was used, but
that felt uglier. Also, you *can* set both of these two fields and get predictable results.

I'd like to revisit using the line height of the chosen fonts in the future, but it seems a
little too complex to be worthwhile right now. An interesting option would be making the
select-a-face-using-locale strategy described above an opt-in feature, though some users
might instead want to just use the tallest line height among fonts in use. Something like
this Android API might be appropriate:

[3] https://learn.microsoft.com/en-us/dotnet/api/android.widget.textview.fallbacklinespacing?view=xamarin-android-sdk-13

I'd like to thank Dominik Honnef for some good discussion around this feature, and for pointing
me to some good sources on the subject.

Signed-off-by: Chris Waldon <christopher.waldon.dev@gmail.com>

---
## [hasanozye/FrameWorkAdvance2](https://github.com/hasanozye/FrameWorkAdvance2)@[e408133a36...](https://github.com/hasanozye/FrameWorkAdvance2/commit/e408133a36d0c78b5dac301bc4ef4041ea51c652)
#### Saturday 2023-07-22 10:16:38 by Hasan Özyer

"📖 Page turn: Welcome to the magical world of HomePage! 🏰✨ Navigate through the wonders of web testing with our captivating methods! 🚀✨ Whether you're searching for your favorite products or exploring the enchanting menus, we've got you covered! 💻🌈 Let the WebDriver dance to the rhythm of your commands as you embark on exciting testing adventures! 🪄🧙‍♂️ Experience the power of Hasan's HomePage and unleash the true potential of your web tests! 🌟🔥"

---
## [Chetansm684/Coffee-House](https://github.com/Chetansm684/Coffee-House)@[3d9cddd8f0...](https://github.com/Chetansm684/Coffee-House/commit/3d9cddd8f0e9ea9d8c47b44ec7fd53c4eae73f74)
#### Saturday 2023-07-22 10:21:06 by Chetan Meshram

Add files via upload

Welcome to my captivating online portfolio and personal website! 🌟 Immerse yourself in a world of creativity and innovation as you explore my diverse projects and endeavors. From stunning web designs to engaging software projects, my portfolio showcases my passion for technology and design.

Through my website, I aim to inspire and share my journey as a lifelong learner and creator. Delve into the captivating visuals, seamless user experiences, and impressive functionality that reflect my dedication to excellence in every project.

Join me on this exciting digital journey, where every pixel and line of code tells a unique story. Discover the power of imagination and see how it comes to life in my creations. From front-end enchantment to back-end wizardry, my website is a testament to my commitment to pushing the boundaries of what's possible.

Feel free to connect with me, whether you're interested in collaborating, exploring new opportunities, or just sharing your thoughts. Let's embark on an exciting adventure together and make the web a more beautiful and meaningful place.

Explore, enjoy, and let's create something extraordinary together! 🚀✨

---
## [HWSensum/Fluffy-Frontier-Sensum](https://github.com/HWSensum/Fluffy-Frontier-Sensum)@[9e523715ac...](https://github.com/HWSensum/Fluffy-Frontier-Sensum/commit/9e523715acd373ce1a74bdc8f9c2fe422c2ad61e)
#### Saturday 2023-07-22 10:36:21 by SkyratBot

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
## [Hardaeborla/zechub](https://github.com/Hardaeborla/zechub)@[59162474a9...](https://github.com/Hardaeborla/zechub/commit/59162474a951093b37a9c8fa6a908f9daabf2f5a)
#### Saturday 2023-07-22 10:40:18 by Hardaeborla

zecweekly52.md

# ZecWeekly #52
ZecHub Announces the Launch of ZecHub Extras, UK court Grants Craig Wright's Bitcoin Appeal, DOJ to Boost Crypto Investigations by Team Merging 






Curated by "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

---

### Welcome to ZecWeekly
Hello Zcashers!! It's another exciting part of the week when we share recent update happening in the Crypto Space and Zcash Ecosystem. We will be delving into the launch of the first ever NFT marketplace by ZecHub known as ZecHub Extras. We'll also be looking at the Trailing Finality Layer as proposed by ECC. Plus, get ready to discover valuable Zcash tips and more! Stay tuned.

You can also be a contributor on ZecHub by helping us create our weekly Newsletter and get rewarded for your contribution. Learn more by clicking the link below 👇👇
[Create ZecWeekly Newsletter](https://wiki.zechub.xyz/ZecWeekly-newsletter) 

---

## This Week's Education Piece 
We will be learning more about an Interchain privacy protocol which utilizes Layer - 1 Proof-of-Stake protocol to provide interchain asset-agnostic privacy for users. This is Web3 project is known as Namada Protocol. This wiki covers all important things you need to know about Namada Protocol and most importantly, it's Strategic alliance with Zcash. Learn more about Namada Protocol by reading through the link below 👇👇
[Namada Protocol] (https://wiki.zechub.xyz/namada-protocol) 




## Zcash Updates


#### ECC & ZF Updates

[ECC Trailing Finality Layer Proposal](https://twitter.com/ElectricCoinCo/status/1681675480594800641?t=TV4H2fqP-DEM2F3GHGaF8A&s=19) 

[Zcon4 Registration Deadline](https://twitter.com/ZcashFoundation/status/1682425238510772224?t=7N-NNVIoiSDmh7Bu_OqGPg&s=19) 

[Trailing Finality Layer consensus protocol design-Zcon4](https://twitter.com/ZcashFoundation/status/1682148567337533441?t=OWzt0SjtevIDZ2ijR0atkg&s=19)

[Roadmap For LookUp Tables - Zcon4](https://twitter.com/ZcashFoundation/status/1682122103309385728?t=R6QKBZmHQp1OwwKKvhMCFg&s=19) 

[Growing the Zcash Community-Zcon4](https://twitter.com/ZcashFoundation/status/1680969337903915009?t=ADDqmmjY7MMXaARaFmnS-Q&s=19) 

[Ambassador Lightning Talks - Zcon4](https://twitter.com/ZcashFoundation/status/1682055885550411778?t=PC_nPohhxBps1ORuoC2VJQ&s=19) 

[Zcash Unfi Library - Zcon4](https://twitter.com/ZcashFoundation/status/1681780396344721408?t=QaU_LQsC75Z2NKmHOw8RbQ&s=19) 

[Future Developments on the ZSA protocol including atomic swaps - Zcon4] (https://twitter.com/ZcashFoundation/status/1681742420667514885?t=Zz0BgF_zVAImQMzJQgpSDw&s=19) 

[Learn and Understand the Ziggurat Process on Zcash(https://twitter.com/ZcashFoundation/status/1681381864584380427?t=4p1GZkq58aJKWfL2B1wgVw&s=19) 

[Zcash Engineering Security - Zcon4](https://twitter.com/ZcashFoundation/status/1681688881534517249?t=Zn-78Sb43S45VGxgIW0DSw&s=19) 


[Explore the depths of ZKP technology -ZkWeek](https://twitter.com/ZcashFoundation/status/1681417741159284736?t=e7Twxtr-LNayOLQSAUUm6g&s=19) 

[Interact with the Community and Ambassadors Here](https://twitter.com/ZcashFoundation/status/1680969340194021376?t=KLO0EAVY6DcrmGIffJFDQA&s=19) 







#### Zcash Community Grants Updates

[Zcash Ecosystem Grant Funding](https://twitter.com/ZcashFoundation/status/1682425236073881615?t=TrT1q9LyiySOBlsdeium1w&s=19) 

[The Future of Zcash Funding and Decentralization](https://twitter.com/ZcashFoundation/status/1682479746007826432?t=UiLUIKecGAq65xOj1VCLNg&s=19)

[Zcash Sustainability and Resilience](https://twitter.com/ZcashFoundation/status/1681417737766092802?t=UJbT3hhHaWxR8jLob7If6g&s=19) 

[Key Insights and Advice for Grant Recipients and Applicants](https://twitter.com/ZcashFoundation/status/1681337820323954689?t=VPV5wiuIusTWSaPINxc86g&s=19) 

[Suggest Questions For The Panel Here](https://forum.zcashcommunity.com/t/suggest-questions-for-the-zcon4-town-halls/45137) 




#### Community Projects

[The launch of ZecHub Extras, NFT and Store](https://twitter.com/ZecHub/status/1682411383093067776?t=GzCGkptfcyXXzy1n5KdTxw&s=19) 


[Zcash Explorers Celebrate 2 years of serving ZEC Transactions](https://twitter.com/ZcashExplorer/status/1681832545065771008?t=U-ruCf_l_0hVKAJNSUIeuw&s=19) 

[ZecHub DAO to migrate from Ethereum to a platform called "DaoDao" on Cosmos](https://twitter.com/zooko/status/1681197513695711233?t=jrn7kYpmlQEfa3YaZcB-cA&s=19) 


[Experience Cryptography with @CryptoLoungeExp](https://twitter.com/CryptoLoungeExp/status/1681234516264865792?t=SfUI0Z-SEJBFe4kD5W9ecw&s=19)



[Zcash Crusader - Rise of ZEC (Chapter 1)](https://twitter.com/zcashesp/status/1682560856440045569?t=UNbhuFJPGYsFe03LwgmGtg&s=19) 

[Zcash Brazil - Sign Up to watch Zcon4 online](https://twitter.com/zcashbrazil/status/1682179897265909760?t=5tujuYJUCLwEynvMjqw6jw&s=19) 


[Community of Artists Coming Soon on Free2z](https://twitter.com/zcashesp/status/1682559603542749185?t=JuS7PkEjGNZUyfkf6d1VFA&s=19) 

[The State of Zcash Governance](https://twitter.com/nate_zec/status/1682569263201280000?t=PEfjYmEhtISqSWYVZCBt0A&s=19) 

[Ender Arrieta Shares Initial Experience on Free2z](https://twitter.com/zcashesp/status/1682557886654816257?t=VipreXDhHjKtw68dYKyyrw&s=19) 

[ZavaX Oracle - Build a bridge between Avalanche and Zcash](https://twitter.com/reddevinc/status/1681038207821938691?t=WLFic-6i6aQIJrx0dDoEpw&s=19) 

[You are in control with Zcash - Zcash Brazil] (https://twitter.com/zcashbrazil/status/1681767022256959488?t=GwqNp5QHaceN0RxVnutlgQ&s=19) 

[What Zingo Offers](https://twitter.com/ZingoLabs/status/1681678601597472768?t=g4J6AKeFczJ1rUNyryaIRg&s=19) 

[Zcast Episode 5](https://twitter.com/ZcastEsp/status/1682493918389084161?t=M4HqLI9w37f_waESCk1Thw&s=19) 

[Zcash Brazil Phone Donation](https://twitter.com/ezecZshield/status/1682451052283547653?t=4hiHi5ieQN9nfkyc46tbZA&s=19) 

[Club Calender for Zcon4 by ZFAV](https://twitter.com/ZFAVClub/status/1680180190742183936?t=NCfga18J1NQyUrxyBcfktw&s=19) 

[Zecmarts - Online Store for Zcash] (https://twitter.com/zcash/status/1682182877906186240?t=_IsywpS-LfgAwvZYzlBmAA&s=19) 




 




#### News & Media

[UK court grants appeal from Craig Wright in Bitcoin rights lawsuit-Cointelegraph](https://cointelegraph.com/news/uk-courts-grants-appeal-craig-wright-bitcoin-rights-lawsuit) 

[DOJ looks to increase crypto investigations with move to merge teams-The Block](https://www.theblock.co/post/240967/doj-looks-to-increase-crypto-investigations-with-move-to-merge-teams) 

[Nigerian social payments app shuts down crypto exchange services](https://cointelegraph.com/news/nigerian-social-payments-app-shuts-down-crypto-exchange-services) 

[SEC hints at potential appeal to XRP ruling from Ripple Labs lawsuit-Cointelegraph](https://cointelegraph.com/news/sec-hints-at-potential-appeal-to-xrp-ruling-from-ripple-labs-lawsuit) 


[Celsius Network reaches settlements that could clear path to return customer funds: WSJ-The Block](https://www.theblock.co/post/241028/celsius-network-reaches-settlements-wsj) 


## Some Zcash Tweets

[Zcash Español -Lesson of the night](https://twitter.com/zcashesp/status/1682565063763275776?t=PBp7LvAWQH666A3TlgPEOQ&s=19) 

[I Love Zcash Community Consistency - Gary Weinstein](https://twitter.com/Gary_Weinstein_/status/1682445177661673487?t=QYXCizVSB2eTWzgih5wBdg&s=19) 


[I was buying my daily coffee with Zcash - Zooko](https://twitter.com/zooko/status/1682506385374994432?t=umGSQrC4F6ctPhAJ7ySKBA&s=19) 

[Preparing for Zcon4 with ZFAV](https://twitter.com/ZFAVClub/status/1681571837392613376?t=luC8cIRI_so3x6H5z9qP1g&s=19) 

[Visualizing the Zcash Network](https://twitter.com/dismad8/status/1681419103553359872?t=K1211kDTLScXmKv715pbaA&s=19) 

[Zcash Bugs in a Chart - Taylor Hornby](https://twitter.com/DefuseSec/status/1680740997330788354?t=abq4Cf0KLN9GMZJFhwcO4w&s=19) 

[Roosevelt ranked 4th on  Zcon4 Leaderboard Event](https://twitter.com/gordonesroo/status/1682527369804800003?t=QCqgOEl6y6REUIgLkbe47g&s=19) 

[Dash Community Commends Zcash](https://twitter.com/Dash_Community/status/1682444884077170693?t=lENQNcev6HmoR9P3jzJSQg&s=19) 

[Breaking the Silence](https://twitter.com/michae2xl/status/1682234408290377729?t=SeNHGQbNhvrf97RJ3lInnA&s=19) 

[Solicit For Donations on Free2z](https://twitter.com/gordonesroo/status/1682571508328148992?t=uiyQcttVS_zC11t9JXy9Fg&s=19)

[Beautiful Zcash Shirt on a beautiful Zcasher 😍](https://twitter.com/SheEmprende_/status/1682574050974105601?t=hexJADl9ey2ZMe0g91rTLw&s=19) 



 









## Zeme of the Week
[https://twitter.com/doloresampaio/status/1682528086540034048?t=-VLEzCpRaBdBXmYLqmEV2g&s=19](https://twitter.com/doloresampaio/status/1682528086540034048?t=-VLEzCpRaBdBXmYLqmEV2g&s=19) 

## Jobs in the Ecosystem

- [Director of Security, ECC](https://apply.workable.com/electric-coin-company/j/E68A4C20E2/)

---
## [Moonshanks/cmss13](https://github.com/Moonshanks/cmss13)@[d26452bb9a...](https://github.com/Moonshanks/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Saturday 2023-07-22 11:04:49 by Unknownity

Burrower burrow changes and fixes (#3818)

# About the pull request

The PR contains mostly fixes for the Burrower that have been around,
that being that other xenos could slash them while they were burrowed,
that they could resist (and get rid of fire) while burrowed, that they
still took shrapnel and direct flame damage while burrowed, that SG
autofire and sentries were shooting at a burrowed burrower, wasting ammo
in the process.

Two other notable changes are that the unburrow stun now also works on
other non-friendly xenomorphs (and it works on all of them, skill issue
if you manage to get stunned from that as a T3/Queen) and that burrowing
and unburrowing now has sounds (a change many people were positive about
when it was initially included in the Impaler PR) which may find
tracking and noticing the presence of burrowers easier.

burrowing sound: https://voca.ro/1dQ0pvBMidsr
unburrowing sound: https://vocaroo.com/1zzEz3NQ2Kx5

# Explain why it's good for the game

Bugfixes and a counter to one of the most annoying abilities (that
people consider) in the game.


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Unknownity
fix: Fixed burrowed mobs being able to be targeted by sentries, mines
and SG autofire.
fix: Fixed burrowed mobs being able to grab mobs on the surface.
fix: Fixed burrowed mobs being able to resist while burrowed.
fix: Fixed burrowers taking damage from direct flame and shrapnel from
explosions.
fix: Fixed burrowers being able to get slashed from enemy Xenos on the
surface.
fix: Fixed burrowers unburrow stun to now properly target and stun enemy
Xenos.
soundadd: Added sounds for the Burrower when they are burrowing and
unburrowing.
/:cl:

Co-authored-by: Unknownity <a>

---
## [Moonshanks/cmss13](https://github.com/Moonshanks/cmss13)@[5f5fcd2b27...](https://github.com/Moonshanks/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Saturday 2023-07-22 11:04:49 by Drathek

Fix marines not getting first dibs if they ghost (#3802)

# About the pull request

This PR fixes an issue where hugged marines that burst were not getting
first dibs on the larva if they ghosted. Previously the mind maybe
wasn't cleared out to find the ghost mob, but it currently is.

NOTE: The existing check requiring the marine to be nested is still in
place to get first dibs. I'm honestly not sure if this check should
still exist. On one hand I can agree it might be hard for the marine
trying to get help to suddenly become the larva and switch gears - they
are still going to be in the mindset of a marine that the larva should
die. But its also sort of weird to only get the first dibs if nested. If
xenos are unnesting hugged marines just before they pop, thats already a
mechanic abuse that should be ahelped; but ideally there wouldn't be
anything to be abused. Also, some may consider this kind of larva
undesirable anyways so maybe they'd prefer the marine to have it... So
let me know if I should just remove the nested check on line 151.

# Explain why it's good for the game

Fixes an unintended consequence of ghosting when hugged that would
prevent that marine from getting their first dibs on the larva.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>


![dibs](https://github.com/cmss13-devs/cmss13/assets/76988376/84e44345-2b83-473f-9997-f7865bcef1dd)

</details>


# Changelog
:cl: Drathek
fix: Fix ghosting preventing first dibs on the larva in a hugged marine
/:cl:

---
## [Javeriach/Web-Development-Projects](https://github.com/Javeriach/Web-Development-Projects)@[bbd0b357b6...](https://github.com/Javeriach/Web-Development-Projects/commit/bbd0b357b6ad038807ba3145cce65bcccd7b8da3)
#### Saturday 2023-07-22 13:06:46 by Javeriach

Create Weather App

Welcome to our Weather App repository on GitHub! 🌤️🌧️🌪️

Our Weather App is built with HTML, CSS, Bootstrap framework, and JavaScript, offering a range of key features to keep you informed about the weather conditions:

- 🌡️ Current Temperature: Get real-time temperature updates for the selected city.
- ⏰ Current Time: Stay synced with the local time of the chosen city.
- 📅 Current Date and Weekday: Always know the current date and day of the week.
- 🏳️ City's Country Name: Displaying the country associated with the chosen city.
- ☁️ Weather Conditions: Detailed information on the current weather.
- 🌡️ Feels Like: Find out how the weather feels like in real-time.
- 💧 Humidity: Get the humidity percentage for better planning.
- ⛈️ Pressure: Know the atmospheric pressure in the selected location.
- 🌡️ Temperature Max and Min: Get the maximum and minimum temperatures.
- 🌈 Weather-Related Icons: Intuitive icons for better visualization.
- ❌ Error Handling: Providing a smooth experience by handling errors gracefully.
- 📱 Responsiveness: Enjoy a seamless user experience across devices.
- 🌒 Dark Mode: Toggle to dark mode for a pleasant viewing experience at night.

Join us in exploring the world of weather through our interactive and feature-rich Weather App! Stay prepared and informed no matter what the weather brings. Happy coding! 🚀🌐

---
## [TeshariEnjoer/FluffySTG](https://github.com/TeshariEnjoer/FluffySTG)@[f17bfbcbad...](https://github.com/TeshariEnjoer/FluffySTG/commit/f17bfbcbad67d5c2d6d66d1aa61d4893f64acb09)
#### Saturday 2023-07-22 13:23:24 by GoldenAlpharex

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags [MDB IGNORE] (#22516)

* SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

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

Bugs are bad they make you mad

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

* Fixed a compile error (whoops)

* Whoops fixed that wrong

* Okay now I compiled and made sure it was fixed for real, I swear!

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [Aakodal/nixos](https://github.com/Aakodal/nixos)@[a200158149...](https://github.com/Aakodal/nixos/commit/a2001581498d97aee805bd6f447502795c3f9988)
#### Saturday 2023-07-22 13:37:47 by Aakodal

damn i suck at this thing

hyprland: update config to use literals and proper nix syntax
neovim: fuck this
theming: help me
overlays: prepare for custom packages (100% useless for now)
chore: remove dead code (again)

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[efbe50f2b2...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/efbe50f2b269e6552b68360aafa0b8c476394584)
#### Saturday 2023-07-22 13:39:28 by SkyratBot

[MIRROR] Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection [MDB IGNORE] (#22495)

* Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection (#76852)

## About The Pull Request

Refactors arcane barrage (the wizard spell) and blood barrage (the weird
version of the same spell that cultists get) into the magic subtype. No
longer are they rifles...for some reason. Also they have sprites once
again! Yay. Fixes https://github.com/tgstation/tgstation/issues/76561

So as to not replicate a really crappy system used to get the hand
swapping working, I've just opted to take this opportunity to make
arcane barrage an automatic fire weapon. Yes, this is kind of a feature,
but it's...it's appropriate, don't you think? And I don't think
meaningfully changes its fire rate?

Blood Barrage no longer harms cultists/constructs shot by it and now
properly just heals them/injects them with unholy water. Why all this
was shoved into the Bump() proc is beyond me, but it works now. Fixes
https://github.com/tgstation/tgstation/issues/76560

I've improved the variables for some of the cult spells, and I've also
fixed what I think is one the most pesky parts of how drawing blood
works. So, rather than using range(), it uses view(), which seems to
cause the spell to be a bit funky with lighting? So if you're in
darkness (gosh cultists in dim light, how unheard of), this spell
struggles to gather up blood. Not anymore it doesn't!

Lastly, it only worked on blood pools or droplets, not blood trails. So,
you could bleed a character out by dragging them around, but not sap up
the blood they're dropping from doing so. Only the intermittent blood
splatters or your own bloody footprints count.

Here is the funny thing with that. It still cleans up the blood trail.
You just couldn't activate the blood draw from the trail or treat it as
blood. Now you can. Blood trails now give you +5 charges, and you can
activate the blood draw using blood trails.

## Why It's Good For The Game

Arcane Barrage/Blood Barrage:

This was some really old code and I'm still not sure why they were made
as a separate spell to the madoka reference, which at this stage is
still better than this spell. But at least it is using a sensible
subtype with a reasonable, more modern component to facilitate the
'rapid firing barrage of magical bullet' image this spell is meant to
invoke. As a result of all this nonsense, this spell had its sprites
broken because it kept being attached to stuff in the rifles folder.
Let's put a stop to that here and now and break it independently
instead.

Oh also cultists getting shot by healing bullets that still killed them
is both funny and dumb and the way it worked was bonkers.

Blood Draw:
A cultist trying to determine, on the fly, what blood is a valid for the
blood draw is nearly impossible from visual alone. You'd be convinced
this part of the spell is broken just because having a splatter and a
trail on the same tile massively obfuscates whether you're looking at
valid sources of blood. I've struggled to understand as a player what
was going on and why it was so selective about what was acceptable. Now
I see that the problem was one of visual accuracy, bad type checking,
and really, really outdated code that should have been improved with
better procs.

Blood trails are also actually made from dragging out a creature's
bloody corpse. For humans, the most common source of blood trails, this
does actually mean they're losing blood to produce these trails. It
stands to reason this should be a valid source (bloody footprints are,
after all). I gave them a...somewhat minor amount of charge contribution
just to keep it moderately sane for how much blood it generates.

## Changelog
:cl:
refactor: Arcane Barrage and Blood Barrage are magic gun subtypes and
not rifle subtypes. Also they have sprites again.
qol: The barrage spells now use the automatic component to do its thing.
fix: Blood Barrage once again heals cultists and constructs without
hurting them.
code: Cleans up how Blood Rites finds blood to draw in. You can now just
click turfs as well as blood, and it should now be much more accurate
about it.
qol: Blood trails contribute to charges gained using Blood Rites. You
can also activate Blood Rite's blood draw using blood trails.
/:cl:

* Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [RainbowTaro2022/yuzu](https://github.com/RainbowTaro2022/yuzu)@[8e703e08df...](https://github.com/RainbowTaro2022/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Saturday 2023-07-22 15:09:13 by comex

Implement SSL service

This implements some missing network APIs including a large chunk of the SSL
service, enough for Mario Maker (with an appropriate mod applied) to connect to
the fan server [Open Course World](https://opencourse.world/).

Connecting to first-party servers is out of scope of this PR and is a
minefield I'd rather not step into.

 ## TLS

TLS is implemented with multiple backends depending on the system's 'native'
TLS library.  Currently there are two backends: Schannel for Windows, and
OpenSSL for Linux.  (In reality Linux is a bit of a free-for-all where there's
no one 'native' library, but OpenSSL is the closest it gets.)  On macOS the
'native' library is SecureTransport but that isn't implemented in this PR.
(Instead, all non-Windows OSes will use OpenSSL unless disabled with
`-DENABLE_OPENSSL=OFF`.)

Why have multiple backends instead of just using a single library, especially
given that Yuzu already embeds mbedtls for cryptographic algorithms?  Well, I
tried implementing this on mbedtls first, but the problem is TLS policies -
mainly trusted certificate policies, and to a lesser extent trusted algorithms,
SSL versions, etc.

...In practice, the chance that someone is going to conduct a man-in-the-middle
attack on a third-party game server is pretty low, but I'm a security nerd so I
like to do the right security things.

My base assumption is that we want to use the host system's TLS policies.  An
alternative would be to more closely emulate the Switch's TLS implementation
(which is based on NSS).  But for one thing, I don't feel like reverse
engineering it.  And I'd argue that for third-party servers such as Open Course
World, it's theoretically preferable to use the system's policies rather than
the Switch's, for two reasons

1. Someday the Switch will stop being updated, and the trusted cert list,
   algorithms, etc. will start to go stale, but users will still want to
   connect to third-party servers, and there's no reason they shouldn't have
   up-to-date security when doing so.  At that point, homebrew users on actual
   hardware may patch the TLS implementation, but for emulators it's simpler to
   just use the host's stack.

2. Also, it's good to respect any custom certificate policies the user may have
   added systemwide.  For example, they may have added custom trusted CAs in
   order to use TLS debugging tools or pass through corporate MitM middleboxes.
   Or they may have removed some CAs that are normally trusted out of paranoia.

Note that this policy wouldn't work as-is for connecting to first-party
servers, because some of them serve certificates based on Nintendo's own CA
rather than a publicly trusted one.  However, this could probably be solved
easily by using appropriate APIs to adding Nintendo's CA as an alternate
trusted cert for Yuzu's connections.  That is not implemented in this PR
because, again, first-party servers are out of scope.

(If anything I'd rather have an option to _block_ connections to Nintendo
servers, but that's not implemented here.)

To use the host's TLS policies, there are three theoretical options:

a) Import the host's trusted certificate list into a cross-platform TLS
   library (presumably mbedtls).

b) Use the native TLS library to verify certificates but use a cross-platform
   TLS library for everything else.

c) Use the native TLS library for everything.

Two problems with option a).  First, importing the trusted certificate list at
minimum requires a bunch of platform-specific code, which mbedtls does not have
built in.  Interestingly, OpenSSL recently gained the ability to import the
Windows certificate trust store... but that leads to the second problem, which
is that a list of trusted certificates is [not expressive
enough](https://bugs.archlinux.org/task/41909) to express a modern certificate
trust policy.  For example, Windows has the concept of [explicitly distrusted
certificates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265983(v=ws.11)),
and macOS requires Certificate Transparency validation for some certificates
with complex rules for when it's required.

Option b) (using native library just to verify certs) is probably feasible, but
it would miss aspects of TLS policy other than trusted certs (like allowed
algorithms), and in any case it might well require writing more code, not less,
compared to using the native library for everything.

So I ended up at option c), using the native library for everything.

What I'd *really* prefer would be to use a third-party library that does option
c) for me.  Rust has a good library for this,
[native-tls](https://docs.rs/native-tls/latest/native_tls/).  I did search, but
I couldn't find a good option in the C or C++ ecosystem, at least not any that
wasn't part of some much larger framework.  I was surprised - isn't this a
pretty common use case?  Well, many applications only need TLS for HTTPS, and they can
use libcurl, which has a TLS abstraction layer internally but doesn't expose
it.  Other applications only support a single TLS library, or use one of the
aforementioned larger frameworks, or are platform-specific to begin with, or of
course are written in a non-C/C++ language, most of which have some canonical
choice for TLS.  But there are also many applications that have a set of TLS
backends just like this; it's just that nobody has gone ahead and abstracted
the pattern into a library, at least not a widespread one.

Amusingly, there is one TLS abstraction layer that Yuzu already bundles: the
one in ffmpeg.  But it is missing some features that would be needed to use it
here (like reusing an existing socket rather than managing the socket itself).
Though, that does mean that the wiki's build instructions for Linux (and macOS
for some reason?) already recommend installing OpenSSL, so no need to update
those.

 ## Other APIs implemented

- Sockets:
    - GetSockOpt(`SO_ERROR`)
    - SetSockOpt(`SO_NOSIGPIPE`) (stub, I have no idea what this does on Switch)
    - `DuplicateSocket` (because the SSL sysmodule calls it internally)
    - More `PollEvents` values

- NSD:
    - `Resolve` and `ResolveEx` (stub, good enough for Open Course World and
      probably most third-party servers, but not first-party)

- SFDNSRES:
    - `GetHostByNameRequest` and `GetHostByNameRequestWithOptions`
    - `ResolverSetOptionRequest` (stub)

 ## Fixes

- Parts of the socket code were previously allocating a `sockaddr` object on
  the stack when calling functions that take a `sockaddr*` (e.g. `accept`).
  This might seem like the right thing to do to avoid illegal aliasing, but in
  fact `sockaddr` is not guaranteed to be large enough to hold any particular
  type of address, only the header.  This worked in practice because in
  practice `sockaddr` is the same size as `sockaddr_in`, but it's not how the
  API is meant to be used.  I changed this to allocate an `sockaddr_in` on the
  stack and `reinterpret_cast` it.  I could try to do something cleverer with
  `aligned_storage`, but casting is the idiomatic way to use these particular
  APIs, so it's really the system's responsibility to avoid any aliasing
  issues.

- I rewrote most of the `GetAddrInfoRequest[WithOptions]` implementation.  The
  old implementation invoked the host's getaddrinfo directly from sfdnsres.cpp,
  and directly passed through the host's socket type, protocol, etc. values
  rather than looking up the corresponding constants on the Switch.  To be
  fair, these constants don't tend to actually vary across systems, but
  still... I added a wrapper for `getaddrinfo` in
  `internal_network/network.cpp` similar to the ones for other socket APIs, and
  changed the `GetAddrInfoRequest` implementation to use it.  While I was at
  it, I rewrote the serialization to use the same approach I used to implement
  `GetHostByNameRequest`, because it reduces the number of size calculations.
  While doing so I removed `AF_INET6` support because the Switch doesn't
  support IPv6; it might be nice to support IPv6 anyway, but that would have to
  apply to all of the socket APIs.

  I also corrected the IPC wrappers for `GetAddrInfoRequest` and
  `GetAddrInfoRequestWithOptions` based on reverse engineering and hardware
  testing.  Every call to `GetAddrInfoRequestWithOptions` returns *four*
  different error codes (IPC status, getaddrinfo error code, netdb error code,
  and errno), and `GetAddrInfoRequest` returns three of those but in a
  different order, and it doesn't really matter but the existing implementation
  was a bit off, as I discovered while testing `GetHostByNameRequest`.

  - The new serialization code is based on two simple helper functions:

    ```cpp
    template <typename T> static void Append(std::vector<u8>& vec, T t);
    void AppendNulTerminated(std::vector<u8>& vec, std::string_view str);
    ```

    I was thinking there must be existing functions somewhere that assist with
    serialization/deserialization of binary data, but all I could find was the
    helper methods in `IOFile` and `HLERequestContext`, not anything that could
    be used with a generic byte buffer.  If I'm not missing something, then
    maybe I should move the above functions to a new header in `common`...
    right now they're just sitting in `sfdnsres.cpp` where they're used.

- Not a fix, but `SocketBase::Recv`/`Send` is changed to use `std::span<u8>`
  rather than `std::vector<u8>&` to avoid needing to copy the data to/from a
  vector when those methods are called from the TLS implementation.

---
## [czarchasm00/morehud-cz](https://github.com/czarchasm00/morehud-cz)@[0c1f7eed0b...](https://github.com/czarchasm00/morehud-cz/commit/0c1f7eed0bfa97c3cddac033bb51ec358a8891eb)
#### Saturday 2023-07-22 17:30:07 by czarchasm00

???????????????

i fucking hate github
somehow it never got these changes
this fucking program is so fucking stupid
these are MINMODE CHANGES
i did this as my FIRST COMMIT
YESTERDAY
?????????????????????????

---
## [EOBGames/tgstation](https://github.com/EOBGames/tgstation)@[daa33d89fe...](https://github.com/EOBGames/tgstation/commit/daa33d89fef10650f89f7db160f110141ab99e5d)
#### Saturday 2023-07-22 17:54:05 by IndieanaJones

Xenomorph/Alien Rework 2023: Part 1 (#75286)

## About The Pull Request

Alternative to #75277

Kept you waiting, huh?

This PR is the first part of a Xenomorph rework which seeks to make the
big lugs more balanced and up to date with /tg/'s current design. This
mainly involves curtailing xenomorph's infamous hardstuns into more
interactive forms of combat, while also giving some buffs to the
xenomorph's more unique abilities in order to keep them threatening.

Part 1 will focus on simple number changes and some simple mechanic
changes. In the future, changes will be made to endgame involving
xenomorphs, along with changes to other facets of Xenomorphs.

Highly based off of #55937.

Changes:

- Xenomorph disarm has been completely reworked. While a disarm will
attempt to, well, disarm, a human opponent should they be holding
something, it will no longer immediately hardstun targets when they
aren't. Instead, the xenomorph will shove the target several tiles back
and inflict 35 stamina damage. If the target slams into a wall, this
will also come with the added effect of knocking them down. If a human
is incapacitated, however, right click will slam them into the ground,
which paralyzes them for a lengthy 5 seconds (which is ultimately half
the time xenos could stun you for before), allowing for safe transport
back to the nest as long as you keep them close.

- Humans can now shove xenomorphs. Due to being the superior predator,
however, you can't knock down xenomorphs from shoving. You can slow them
for a little bit akin to humans though.

- Neurotoxin no longer is a hardstun. Instead, it deals 50 stamina
damage on contact. It is still resisted by BIO armor.

**HUNTER:**
- Speed reduced from -1 to -0.3.
- Pounce speed is twice as fast as before (1 to 2)
- Hardstun time on pounce reduced from 10 seconds to 5 seconds.

Hunters being insanely fast has been a major balance-ruining factor of
xenomorphs for many years now. These buggers could practically ambush
anyone, hardstun them immediately, and then leave before anyone could do
anything. Now, with their speed nerfed and in combination with the xeno
shove changes, hunters will need to spend more time to down a target.
Their pounce was practically useless, so its been sped up in order to
make it more practical to use.

**SENTINEL**
- Speed reduced from 0 to 0.2
- Cloak alpha reduced from 0.75 to 0.25 (you're more hidden now)

Sentinels receive a large nerf in regards to their spit, but their
before useless cloaking ability has been greatly improved upon as
compensation. They now serve better as defenders and ranged ambushers.

**XENOMORPH DRONE**
- No changes

As in the original PR, drones are perfeclty balanced in my eyes, so no
changes were required.

**XENOMORPH PRAETORIAN**
- Speed increased from 1 to 0.5
- No changes

Praetorians get affected by the nerfs of the other xeno abilities, but
now they're a bit faster in order to close the gap to use their
abilities.

**XENOMORPH QUEEN**
- Speed increased from 3 to 2
- Health increased from 400 to 500
- Damage increased from 20 to 50

Xenomorph queens have been sped up and made more tanky and lethal in
close-range combat. Fighting this beast up-close should be a death
sentence to almost anything else in the game. Speed increases will help
her re-position and close the gap on potential prey.

**OTHER CHANGES**
- Fixed a bug where simplemobs didn't actually use xenomorph's damage
values when they were attacked by them.

## Why It's Good For The Game

Xenomorphs are old, and haven't been updated for quite a long time. This
has left them as sources of a bunch of hardstuns which made counterplay
from a modern spaceman extremely difficult. With these changes, fighting
xenomorphs is more interactive and should end up being more enjoyable
for both crew and xenos. Buffs were also given out to incentivize usage
of xenomorph's unique abilities as opposed to the standard disarm spam
which was most effective for them until now.

## Changelog
:cl:
balance: Xenos have been rebalanced, removing their hardstuns on their
disarm and neurotoxin, along with a slew of other changes. Xenos have
received buffs to their more unique abilities in return.
fix: Fixed simplemobs ignoring xenomorph's melee damage values when
being attacked by them.
/:cl:

---
## [sipacid/psg](https://github.com/sipacid/psg)@[4424a602e5...](https://github.com/sipacid/psg/commit/4424a602e5bcab8e4567e1ed1832c202f1254f37)
#### Saturday 2023-07-22 18:04:03 by Eve

enough sports poor study joking do I have to doh rocket science cracks me up theft IMHO I can't believe it really bastard experts ghetto play frown one more time how about those yankees stuff au revoir bring it on sloth awesome happy happy joy joy I be like what part of God do you not understand hello bring it on holy grail dude such a scoffer

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[4e91d057d7...](https://github.com/tgstation/tgstation/commit/4e91d057d7d627bd8c356a2251195eb579106707)
#### Saturday 2023-07-22 18:05:24 by MrMelbert

Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

## About The Pull Request

This PR adds a new wizard ritual (the kind that require 100 threat on
dynamic)

This ritual allows the wizard to select one spellbook entry (item or
spell), to which everyone on the station will be given or taught said
spell or item. If the spell requires a robe, the spell becomes robeless,
and if the item requires wizard to use, it makes it usable. Mostly.

- Want an epic sword fight? Give everyone a high-frequency blade

- One mindswap not enough shenanigans for you? Give out mindswap

- Fourth of July? Fireball would be pretty hilarious...

The wizard ritual costs 3 points plus the cost of whatever entry you are
giving out. So giving everyone fireball is 5 points.

It can only be cast once by a wizard, because I didn't want to go
through the effort to allow multiple in existence


## Why It's Good For The Game

Someone gave me the idea and I thought it sounded pretty funny as an
alternative to Summon Magic

Maybe I make this a Grand Finale ritual instead / in tandem? That's also
an idea.

## Changelog

:cl: Melbert
add: Wizards have a new Right and Wrong: Mass Teaching, allowing them to
grant everyone on the station one spell or relic of their choice!
/:cl:

---
## [MEHDIDELNAVAZI/Fetchdata_API_React](https://github.com/MEHDIDELNAVAZI/Fetchdata_API_React)@[8871aa28f0...](https://github.com/MEHDIDELNAVAZI/Fetchdata_API_React/commit/8871aa28f09f300f4050069e5e8ab51826a30b7c)
#### Saturday 2023-07-22 19:27:27 by mehdi

In this latest update, we're taking our project to the next level with some awesome features and improvements!

📥 Fetching Data:
Now, our application is even more dynamic as we've successfully implemented data fetching from the website. This allows us to display real-time data to our users, enhancing their overall experience and making the app much more engaging.

💀 Skeleton Loading Component:
We understand the importance of a smooth user experience, and that's why we've introduced a sleek and seamless skeleton loading component. Users will now see visually appealing loading placeholders while the data is being fetched, eliminating any potential frustration caused by blank screens or delays.

🔜 What's Next?
We're not stopping here! In the next commit, we'll be focusing on two major tasks:

🗑️ Delete and Update Functionality:
We're gearing up to implement the delete and update functionalities, which are crucial for providing users with the ability to manage their data effortlessly. This will empower our users and make our application more interactive and user-friendly.

➕ Creating New User Feature:
The excitement doesn't end there! We have an exciting surprise for our users in the next update. We'll be introducing a brand-new feature that enables users to create a new account seamlessly. This will expand the capabilities of our app and attract even more users to join our community.

Stay tuned for more updates as we continue to enhance and refine our React project. Your feedback and support are invaluable to us, and we can't wait to share these fantastic additions with you all.

Let's build something amazing together! 🎉

#ReactProject #DataFetching #SkeletonLoading #DeleteUpdateFunctionality #NewUserFeature #OpenSource #GitHubCommit

---
## [Offroaders123/Game-Loop](https://github.com/Offroaders123/Game-Loop)@[581f52efe0...](https://github.com/Offroaders123/Game-Loop/commit/581f52efe0949101a075c7a3a4a0052cba20022f)
#### Saturday 2023-07-22 19:32:30 by Offroaders123

Server Worker Module

Vite makes this super nice :)
https://stephendoddtech.com/blog/game-design/javascript-web-worker-set-interval-game-loop (Haven't read this yet, it was in my tab bar though)
https://vitejs.dev/guide/features.html#import-with-query-suffixes (sick!!! this helps out so much with the compilation step!)

I think I'm going to make myself allow myself (yes?) to rely on Vite in this case here. Getting the development of this set up is more important this time, than building it all from scratch. Of course, I still want to understand how it works under the hood though, I don't like magic code (I want to start using Svelte, but it isn't clicking for me how a lot of it works yet. At least, how it manages to do what it does. I know why it works, but I want to know how it works [is that the same thing? idk])

Tried setting up Svelte here, but it just isn't too easy to embed directly into the existing project. At least I don't know the best way to do that yet.

Just found this, not sure if it's what I'd like, but it kind of sounds like it.
https://github.com/DirtyHairy/worker-rpc

---
## [DanielJin21/bevy](https://github.com/DanielJin21/bevy)@[fb4c21e3e6...](https://github.com/DanielJin21/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Saturday 2023-07-22 19:33:34 by Ida "Iyes

bevy_audio: ECS-based API redesign (#8424)

# Objective

Improve the `bevy_audio` API to make it more user-friendly and
ECS-idiomatic. This PR is a first-pass at addressing some of the most
obvious (to me) problems. In the interest of keeping the scope small,
further improvements can be done in future PRs.

The current `bevy_audio` API is very clunky to work with, due to how it
(ab)uses bevy assets to represent audio sinks.

The user needs to write a lot of boilerplate (accessing
`Res<Assets<AudioSink>>`) and deal with a lot of cognitive overhead
(worry about strong vs. weak handles, etc.) in order to control audio
playback.

Audio playback is initiated via a centralized `Audio` resource, which
makes it difficult to keep track of many different sounds playing in a
typical game.

Further, everything carries a generic type parameter for the sound
source type, making it difficult to mix custom sound sources (such as
procedurally generated audio or unofficial formats) with regular audio
assets.

Let's fix these issues.

## Solution

Refactor `bevy_audio` to a more idiomatic ECS API. Remove the `Audio`
resource. Do everything via entities and components instead.

Audio playback data is now stored in components:
- `PlaybackSettings`, `SpatialSettings`, `Handle<AudioSource>` are now
components. The user inserts them to tell Bevy to play a sound and
configure the initial playback parameters.
- `AudioSink`, `SpatialAudioSink` are now components instead of special
magical "asset" types. They are inserted by Bevy when it actually begins
playing the sound, and can be queried for by the user in order to
control the sound during playback.

Bundles: `AudioBundle` and `SpatialAudioBundle` are available to make it
easy for users to play sounds. Spawn an entity with one of these bundles
(or insert them to a complex entity alongside other stuff) to play a
sound.

Each entity represents a sound to be played.

There is also a new "auto-despawn" feature (activated using
`PlaybackSettings`), which, if enabled, tells Bevy to despawn entities
when the sink playback finishes. This allows for "fire-and-forget" sound
playback. Users can simply
spawn entities whenever they want to play sounds and not have to worry
about leaking memory.

## Unsolved Questions

I think the current design is *fine*. I'd be happy for it to be merged.
It has some possibly-surprising usability pitfalls, but I think it is
still much better than the old `bevy_audio`. Here are some discussion
questions for things that we could further improve. I'm undecided on
these questions, which is why I didn't implement them. We should decide
which of these should be addressed in this PR, and what should be left
for future PRs. Or if they should be addressed at all.

### What happens when sounds start playing?

Currently, the audio sink components are inserted and the bundle
components are kept. Should Bevy remove the bundle components? Something
else?

The current design allows an entity to be reused for playing the same
sound with the same parameters repeatedly. This is a niche use case I'd
like to be supported, but if we have to give it up for a simpler design,
I'd be fine with that.

### What happens if users remove any of the components themselves?

As described above, currently, entities can be reused. Removing the
audio sink causes it to be "detached" (I kept the old `Drop` impl), so
the sound keeps playing. However, if the audio bundle components are not
removed, Bevy will detect this entity as a "queued" sound entity again
(has the bundle compoenents, without a sink component), just like before
playing the sound the first time, and start playing the sound again.

This behavior might be surprising? Should we do something different?

### Should mutations to `PlaybackSettings` be applied to the audio sink?

We currently do not do that. `PlaybackSettings` is just for the initial
settings when the sound starts playing. This is clearly documented.

Do we want to keep this behavior, or do we want to allow users to use
`PlaybackSettings` instead of `AudioSink`/`SpatialAudioSink` to control
sounds during playback too?

I think I prefer for them to be kept separate. It is not a bad mental
model once you understand it, and it is documented.

### Should `AudioSink` and `SpatialAudioSink` be unified into a single
component type?

They provide a similar API (via the `AudioSinkPlayback` trait) and it
might be annoying for users to have to deal with both of them. The
unification could be done using an enum that is matched on internally by
the methods. Spatial audio has extra features, so this might make it
harder to access. I think we shouldn't.

### Automatic synchronization of spatial sound properties from
Transforms?

Should Bevy automatically apply changes to Transforms to spatial audio
entities? How do we distinguish between listener and emitter? Which one
does the transform represent? Where should the other one come from?

Alternatively, leave this problem for now, and address it in a future
PR. Or do nothing, and let users deal with it, as shown in the
`spatial_audio_2d` and `spatial_audio_3d` examples.

---

## Changelog

Added:
- `AudioBundle`/`SpatialAudioBundle`, add them to entities to play
sounds.

Removed:
 - The `Audio` resource.
 - `AudioOutput` is no longer `pub`.

Changed:
 - `AudioSink`, `SpatialAudioSink` are now components instead of assets.

## Migration Guide

// TODO: write a more detailed migration guide, after the "unsolved
questions" are answered and this PR is finalized.

Before:

```rust

/// Need to store handles somewhere
#[derive(Resource)]
struct MyMusic {
    sink: Handle<AudioSink>,
}

fn play_music(
    asset_server: Res<AssetServer>,
    audio: Res<Audio>,
    audio_sinks: Res<Assets<AudioSink>>,
    mut commands: Commands,
) {
    let weak_handle = audio.play_with_settings(
        asset_server.load("music.ogg"),
        PlaybackSettings::LOOP.with_volume(0.5),
    );
    // upgrade to strong handle and store it
    commands.insert_resource(MyMusic {
        sink: audio_sinks.get_handle(weak_handle),
    });
}

fn toggle_pause_music(
    audio_sinks: Res<Assets<AudioSink>>,
    mymusic: Option<Res<MyMusic>>,
) {
    if let Some(mymusic) = &mymusic {
        if let Some(sink) = audio_sinks.get(&mymusic.sink) {
            sink.toggle();
        }
    }
}
```

Now:

```rust
/// Marker component for our music entity
#[derive(Component)]
struct MyMusic;

fn play_music(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    commands.spawn((
        AudioBundle::from_audio_source(asset_server.load("music.ogg"))
            .with_settings(PlaybackSettings::LOOP.with_volume(0.5)),
        MyMusic,
    ));
}

fn toggle_pause_music(
    // `AudioSink` will be inserted by Bevy when the audio starts playing
    query_music: Query<&AudioSink, With<MyMusic>>,
) {
    if let Ok(sink) = query.get_single() {
        sink.toggle();
    }
}
```

---
## [SARDONYX-forks/git](https://github.com/SARDONYX-forks/git)@[07f91e5e79...](https://github.com/SARDONYX-forks/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Saturday 2023-07-22 21:16:47 by Jeff King

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
## [Naya-James-Mbabila/Arduino-Codes-for-an-Echolocation-device-with-the-use-of-HC-SR04](https://github.com/Naya-James-Mbabila/Arduino-Codes-for-an-Echolocation-device-with-the-use-of-HC-SR04)@[8ab270530f...](https://github.com/Naya-James-Mbabila/Arduino-Codes-for-an-Echolocation-device-with-the-use-of-HC-SR04/commit/8ab270530f9ec52ac007388b57232a43981fcf8d)
#### Saturday 2023-07-22 22:30:00 by Naya James Mbabila

Create README.md

Human echolocation
Abstract
The concept of human echolocation was formally studied in science and engineering in the 1950s (Lore Thaler and Melvyn A. Goodale, 2016). The term echolocation was coined by zoologist Donald Griffin in 1944, however, the concept of visually impaired humans being able to echolocate dates back to 1749. There has been a lot of research and inventions in the field of echolocation worldwide. Inasmuch as echolocation technologies do exist, they are not available in developing countries due to their high cost. Considering Ghana as the locality for this research, there is the need to produce less expensive and highly effective echolocation devices to assist visually impaired people on a large scale. A brief on-campus interaction with visually impaired students showed that the white cane is the only technology they know and have access to.  
This write-up presents and seeks ideas worth considering in making echolocation and movement of the visually impaired easier and affordable. 


Introduction
Echolocation, or sonar, is the use of sound waves, mostly ultrasonic waves, to determine the location of objects. This ability is prevalent in microchiropteran bats, odontocetes (dolphins and toothed whales), rats, and other animals that depend on sound for either food or safety. In sighted humans, this is quite rare but common among visually impaired people. Blind people are generally more sensitive to echoes than sighted people since it is conceptualized that blindness has a high relation to high hearing and echolocation ability (Andrew et al, 2017). This concept relates to the use and disuse of body parts theory. In genetics: Preformation and natural selection, Jean-Baptist Lamarck enunciated the law of use and disuse, which states “that when certain organs become specially developed as a result of some environmental need, then that state of development is hereditary and can be passed on to progeny”. With respect to this, the superior colliculus is expected to be more efficient in the blind. Deeper layers of the superior colliculus are known to be involved in the processing of visual information, thus in the visual cortex. As stated earlier, there has been researched into the concept of human echolocation, but there have not been any verified ways to stimulate the superior colliculus or the visual cortex to enable humans to echolocate with high precision just like other animals. , animals specialized for echolocation typically use much higher sound frequencies for their echolocation, and have specialized capabilities to detect time delays in sound, which regular humans do not (Jascha et al, 2015). The separating line is that many blind people are good at hearing sounds, majority of blind people are not good echolocators (Lore Thaler and Melvyn A. Goodale, 2016). 
To curb this, it will be very helpful to make echolocation devices that combine the abilities of echolocating, taking pictures and interpreting them to a visually impaired listener, and directing blind people around during movement. Amphenol, a high-tech company in Mexico, has started working on similar models, but the concern is the ability to produce similar-purpose devices for local use. To get the best out of this, there was an interaction with four visually impaired students on campus. Undeniably, results from four interviewees are not enough to make solid conclusions, but the results are in line with known literature. 



Interaction with the blind
On July 9, there was an informal interaction with 4 visually impaired students at the University of Ghana, 3 females, and a male, named A, B, C, and D. The reasons for these interactions were to find out things related to the concept of echolocation and other concerns. These were; 
(1) Their awareness of echolocation devices. 
(2)  The usefulness of sound in their life and how well they use sound in their daily activities. 
(3) Their mental visualization of objects, specifically whether they visualize things in color, black and white, or black.
 (4)Their concerns about movement and things that can be done to improve their life on campus, with respect to echolocation. 
Some of the interviewees were not familiar with the name of the concept, but they were with the explanation. According to interviewee A, the white cane is the only echolocation device she knows. This was similar to B and C, however, D said he has heard of wristwatches and other technologies that can help visually impaired people to echolocate. On the whole, the knowledge of echolocation technologies in Ghana is minimal, hence, they are not readily available
Another concern was with ‘sound refinery’. According to C, there is always a lot of noise in the environment, and thinks that sound should be refinable or filterable to help visually impaired people easily find their way to their destinations. 
•	Sound Imaging
The common forms of imaging are photography, radiography, and sonography. The concern in this context is to use sound to take real-life pictures. If light can be used to take regular pictures, what will be the need for using sound to take pictures? 
•	Sound refining
The concern is whether or not sound from a particular sound can one separated from that of another source.
Echolocation devices are not new worldwide, but they are not prominent in Ghana. This makes it worth adventuring into. 



•	Sound for security
Aside from the usage of sound for human echolocation, sound can be used for security purposes. The rationale is that though security cameras are good at giving information about the immediate environment and threats, they are not so efficient. In the sense that, people can always outsmart the cameras by using routes that cannot be detected by the camera. Light is not good at diffraction as sound is. In that, if sound is used for security, intruders will be detected no matter what route they take. With this, sound will be used to detect moving obstacles, new stationary obstacles, and so on.  
 
Functions of Arduino Codes
The code defines three pins: trigPin, echoPin, and buzzerPin. The trigPin and echoPin are used to measure the distance to the nearest object using an ultrasonic sensor. The buzzerPin is used to control a buzzer.
The setup() function initializes the pins and starts the serial communication.
The loop() function measures the distance to the nearest object and turns on the buzzer accordingly. If the object is very close, the buzzer will be turned on for the entire time. If the object is within range, the buzzer will be turned on for a short period of time. If the object is getting close, the buzzer will be turned on for a longer period of time. If the object is far away, the buzzer will not be turned on.
The measureDistance() function measures the distance to the nearest object using the ultrasonic sensor. The function first clears the trigPin, then waits for 2 microseconds, then sets the trigPin on HIGH state for 10 micro seconds, then waits for 10 microseconds, then clears the trigPin again. The function then reads the echoPin, which returns the sound wave travel time in microseconds. The function then calculates the distance and returns it.
This code can be used to create a device that measures the distance to objects and turns on a buzzer accordingly. The device could be used for a variety of purposes, such as security, obstacle avoidance, or proximity detection.


References 
1.	A summary of research investigating echolocation abilities of blind and sighted humans Kolarik AJ, Cirstea S, Pardhan S, Moore BC. A summary of research investigating echolocation abilities of blind and sighted humans. Hear Res. 2014 Apr;310:60-8. doi: 10.1016/j.heares.2014.01.010. Epub 2014 Feb 10. PMID: 24524865.
2.	Approximate diffraction modeling for real-time sound propagation simulation. Pisha L, Atre S, Burnett J, Yadegari S. Approximate diffraction modeling for real-time sound propagation simulation. J Acoust Soc Am. 2020 Oct;148(4):1922. doi: 10.1121/10.0002115. PMID: 33138484.

3.	Bat-inspired signal design for target discrimination in human echolocation. Sumiya M, Ashihara K, Yoshino K, Gogami M, Nagatani Y, Kobayasi KI, Watanabe Y, Hiryu S. Bat-inspired signal design for target discrimination in human echolocation. J Acoust Soc Am. 2019 Apr;145(4):2221. doi: 10.1121/1.5097166. PMID: 31046316.

4.	Echolocation in humans: an overview. WIREs Cogn Sci 2016, 7:382–393. doi: 10.1002/wcs.140. Lore Thaler and Melvyn A. Goodale

5.	Blindness enhances auditory obstacle circumvention: Assessing echolocation, sensory substitution, and visual-based navigation. Kolarik AJ, Scarfe AC, Moore BC, Pardhan S. Blindness enhances auditory obstacle circumvention: Assessing echolocation, sensory substitution, and visual-based navigation. PLoS One. 2017. Apr 13;12(4):e0175750. doi: 10.1371/journal.pone.0175750. PMID: 28407000; PMCID: PMC5391114.


6.	Human click-based echolocation: Effects of blindness and age, and real-life implications in a 10-week training program. Liam J. Norman, Caitlin Dodsworth, Denise Foresteire, Lore Thaler PLoS One. 2021; 16(6): e0252330. Published online 2021 Jun 2. doi: 10.1371/journal.pone.0252330 PMCID:PMC8171922

7.	Navigation aid for blind persons by visual-to-auditory sensory substitution: A pilot study. Alexander Neugebauer, Katharina Rifai, Mathias Getzlaff, Siegfried Wahl. PLoS One. 2020; 15(8): e0237344. Published online 2020 Aug 20. doi: 10.1371/journal.pone.0237344. PMCID: PMC7446825

---

