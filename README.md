## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-22](docs/good-messages/2022/2022-06-22.md)


1,610,568 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,610,568 were push events containing 2,462,668 commit messages that amount to 187,695,300 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [newstools/2022-vanguard-nigeria](https://github.com/newstools/2022-vanguard-nigeria)@[c2fce6c0dc...](https://github.com/newstools/2022-vanguard-nigeria/commit/c2fce6c0dca34adb4acc39ba7da6cf06419477a6)
#### Wednesday 2022-06-22 00:08:03 by Billy Einkamerer

Created Text For URL [www.vanguardngr.com/2022/06/youre-still-all-ive-ever-known-bbnaijas-angel-remembers-late-boyfriend-3years-after/]

---
## [karmaisblackandbluepilled/Merchant-Station-13](https://github.com/karmaisblackandbluepilled/Merchant-Station-13)@[2a3b63c243...](https://github.com/karmaisblackandbluepilled/Merchant-Station-13/commit/2a3b63c2434fec55f7dd1f232455d1594c21809f)
#### Wednesday 2022-06-22 00:12:22 by BettonnCZ

Adds a new sprite for the stacker (#196)

fuck you

---
## [Dragonkiller93/Paradise](https://github.com/Dragonkiller93/Paradise)@[6082c95eb3...](https://github.com/Dragonkiller93/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Wednesday 2022-06-22 00:34:20 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [GForceTF/tgstation](https://github.com/GForceTF/tgstation)@[9428d97a4f...](https://github.com/GForceTF/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Wednesday 2022-06-22 01:12:50 by Imaginos16

[MDB IGNORE] The Tilening V2 - Damaged Tile Overlays Edition (#67761)


About The Pull Request

Hello once more! As we near summer, I continued to reminisce on several PRs done throughout last year! One of them was the controversial, but rather positive Tilening V1, as done by me and Twaticus a while back (#58932), and felt I could've done a better job with how it was presented.

And thus, thanks to @Fikou encouraging me with a very interesting find of a previous tile resprite attempt, I've successfully done it!

Ladies and Gentlemen, I present to you all, Tilening Version Two!
image

Now this isn't your run of the mill tile resprite. While I did improve the appearance of several tiles I haven't touched last time (including the showroom/freezer tiles now), I decided to do something special that most mappers shall appreciate!

Don't you hate it when of all damaged states, there's only ones for grey tiles when we have white, black, terracotta and a bunch of other materials? Don't you wish they were overlays instead?

Well golly gee do I have good news for you!
image
image

After painstakingly spending at least several hours trying to learn enough code to pull it off, I have successfully made it so most tiles display transparent versions of damage overlays over them! This means mappers can express their creativity that much better! And thanks to how the code is written, its super easy to snowflake certain tile types to make them use unique damaged states (looking at you wooden tiles), so fret not in that aspect.

Credits to:
@WJohn For actually making those damaged overlays! Wouldn't've done the PR if it wasn't for you.
@dragomagol, @RigglePrime and @LemonInTheDark for helping me out in a VC at 10 PM to 12 AM troubleshooting the code to make this improvement work!
Why It's Good For The Game

The shading is done better as compared to last time, making them feel more cubical and less like a pancake when seen from above! This PR also makes it so that we never ever have to touch damaged tiles ever again potentially, saving up some RSC regarding icons.

However, due to how damaged tiles are currently mapped in, rather than overlayed as I envision in the future, it'll require a PR by San to be merged later that should make it safe to remove these icons.
Changelog

cl PositiveEntropy, WJohnston, Dragomagol, LemonInTheDark, Riggle
imageadd: Resprites most variety of tiles into a better shaded version!
code: Damaged floors are now damaged overlays, meaning that most tiles should properly display a damaged state!
/cl

---
## [Skb111/-My15days-coding-challenge](https://github.com/Skb111/-My15days-coding-challenge)@[f4dfb626ec...](https://github.com/Skb111/-My15days-coding-challenge/commit/f4dfb626ec26f56ffee96caf74351bb3ee7afe06)
#### Wednesday 2022-06-22 01:31:16 by skb

yeah tonight task made/makes it day8 of my challenge,there was slow down on things for days now thank GOD i scale through

---
## [sailfishos-mirror/procps](https://github.com/sailfishos-mirror/procps)@[8c336e07c6...](https://github.com/sailfishos-mirror/procps/commit/8c336e07c6dd6129f0f6fbec645790f8f24be061)
#### Wednesday 2022-06-22 01:44:08 by Jim Warner

top: avoid library shame with refactored 'Ctrl' window <=== port of newlib bc4b499e

       [ sorry, but under this master branch ]
       [ the whole next narrative is frankly ]
       [ mostly pure unadulterated bullshit. ]

______________________________ original newlib message

Well darn it, whoever wrote that new library caught me
with my pants down (again?). Shoot, they were not just
down but somehow missing altogether. Here's the story.

Any item from that library supported by dynamic memory
can only be represented in user's stacks exactly once.

Should any string based enumerator be duplicated among
the items array, for any instance beyond the first the
library will return '[ duplicate ENUM ]' for a result.

That's where I lost my pants. While command lines were
given special handling (and never duplicated) I failed
to turn on CGROUPS, SUPGRPS & ENVIRON when testing the
Ctrl-G, Ctrl-U & Ctrl-N keys. If any of those 3 are on
that's when a Ctrl window sees a 'duplicate' notation.

[ and who runs top with such fields displayed anyway ]

In responding to this oops, the internals were changed
quite dramatically & vastly simplified in the process.

More importantly, the 'duplicate' results are no more.

Signed-off-by: Jim Warner <james.warner@comcast.net>

---
## [Bungalow-13/Bungalow-13](https://github.com/Bungalow-13/Bungalow-13)@[8a977645a0...](https://github.com/Bungalow-13/Bungalow-13/commit/8a977645a0f4c6e1560405bc0acaa317f643a7e0)
#### Wednesday 2022-06-22 01:52:15 by projectkepler-RU

Blue helmets resprites (#777)

* gsdkfsldka

* blue helmet babey

* more reskin

* aaa

* blue helmete

* blue beret too :)

* the blue helmets :3

* I hate how hard my fucking life is

* now you have both :)

---
## [SeeminglyTypicalUsername/RockStar](https://github.com/SeeminglyTypicalUsername/RockStar)@[45e28cafc6...](https://github.com/SeeminglyTypicalUsername/RockStar/commit/45e28cafc6bd1b4b3f940e32b82a184fd01cff93)
#### Wednesday 2022-06-22 02:12:19 by SeeminglyTypicalUsername

Mercenary fix

holy fuck this was broken so bad. it was using the Den Hitman loadout and the suit was broken for another loadout. Horrible.

---
## [LandSandBoat/server](https://github.com/LandSandBoat/server)@[ccf500070d...](https://github.com/LandSandBoat/server/commit/ccf500070d4448d1e2acbdb711190d5b4e21c4e6)
#### Wednesday 2022-06-22 02:18:18 by neuromancerxi

Add scripts and adjust plumbing for many temp items (#670)

* Add scripts and adjust plumbing for many temp items

Adds Scripts for items.
Adds Effect scripts for X_BOOST_II
Updates Effect scripts for the following:

ACCURACY_BOOST
ATTACK_BOOST
INTENSION
MAGIC_SHIELD
MULTI_STRIKES
MULTI_SHOTS
PAX
PHYSICAL_SHIELD
POTENCY
RAMPART

Adjusts item_usable use times to 1s.

Notes on effects:

Ascetics Tonic/Gambir - +25/+50 MATT/MACC
A big Thank You to Nyu for confirming the Intension effect for MACC.
https://www.bg-wiki.com/bg/Ascetic's_Tonic
https://www.bg-wiki.com/bg/Ascetic's_Gambir

Bravers Drink - +15 to All Stats
https://www.bg-wiki.com/bg/Braver's%20Drink
Reference to Icons/Effects - https://youtu.be/JYT5a_pTA3o?t=20

Champions Tonic - +15 Haste / +3 Crit rate
Champions Drink/Gambir - +18 Haste / +5% Crit rate
Expected Haste effect to be Magic pool based on BG comment (18 and 15)
Critical Hit rate, no data available from community sources, conservative value of 5 (Drink/Gambir) 3 (Tonic)
Both BG and 'clopedia sources confirm Critical Hit Rate (as does the effect description), however, only BG has a reference to Haste value.
https://www.bg-wiki.com/bg/Champion's_Tonic

Gnostics Drink - Enmity -10
No community resources confirm this value, using SCH Animus Minuo as an reference.
https://www.bg-wiki.com/bg/Gnostic's%20Drink
https://www.bg-wiki.com/bg/Animus_Minuo

Monarchs Drink - Regain +3 (30/1000 per tick) for 3 minutes.
https://www.bg-wiki.com/bg/Monarch's_Drink

Stalwart's Tonic/Gambir - ACC/RACC 50/100 ATTP/RATTP 25/50
A big Thank You to Nyu for confirming the effects apply ACC/RACC and ATTP/RATTP across two effects.
https://www.bg-wiki.com/bg/Stalwart's_Tonic
https://www.bg-wiki.com/bg/Stalwart's_Gambir

Berserker's Tonic/Drink - DA 50/100
Thanks to Nyu for confirming the MULTI_STRIKES effect and 1m duration.
https://ffxiclopedia.fandom.com/wiki/Berserker%27s_Drink
No full data on DA rate, minus 'clopedia which has verification tags. Working on the expectation that this follows a good portion of the other items and follows the half potency values for the lesser item.

Swiftshot Tonic/Drink - Double Shot 50/100
https://www.ffxiah.com/forum/topic/28603/fools-tonic-broken#1749569

Dusty Scroll of Reraise - Reraise III, 10m duration.
https://www.bg-wiki.com/bg/Dusty_Reraise

Spiritual Incense/Fools Drink/Tonic/Powder: See effects/magic_shield
Carnal Incense/Fanatics Drink/Tonic/Powder: See effects/physical_shield

* Removed copypasta subp and trailing whitespace.

* Item script clean-up and move effect functions to item_utils.

* Resolve Conflicts

Convert namespace in scripts from item_utils to xi.item_utils
PHYS_ABSORB to Percent from 10000 Scale

---
## [Rebirth-of-the-Night/Rebirth-Of-The-Night](https://github.com/Rebirth-of-the-Night/Rebirth-Of-The-Night)@[52caa606ac...](https://github.com/Rebirth-of-the-Night/Rebirth-Of-The-Night/commit/52caa606ac67d67e1f6ebda880e612e7c0d20d00)
#### Wednesday 2022-06-22 03:14:36 by Foreck1

Bunch o'stuff

Added Tapestry blocks: red, green, cyan, and purple. One-way craft with wool.
Swapped Zanite with Gravitite
Gravitite is now mostly equivalent to silver in stats
Gravitite ore is now sturdy level
Zanite is now part of the gem tier in stats
Zanite ore is now refined level
Zanite now has an ingot form for all equipment
Zanite now counts towards gem advancements
Nerfed Ptera health to half
Tweaked rain droplets on screen effect
Doubled resolution of water drop and fire particles
Added new painting to go along cyan tapestry
Textures tweaked/added for diamond ingot, exorite ingot, ruby ingot, sapphire ingot, zanite ingot
Fixed missing texture particles for giant clovers
Moved Bloodied demon eye recipe from crafting table to runic table to make it more obvious
Nerfed extra drops from clay in rivers to be twice as rare

---
## [Robbbert/hbmame](https://github.com/Robbbert/hbmame)@[ba63081d10...](https://github.com/Robbbert/hbmame/commit/ba63081d109c904902958c6324b013cb10b42732)
#### Wednesday 2022-06-22 03:33:08 by 0kmg

gameboy.xml: Added 21 more prototypes. (#9962)

* gameboy.xml: Added 21 more prototypes.

New working software list additions
-----------------------------------
Astérix (earlier prototype) [VGHF, Hidden Palace]
Astérix (early prototype) [VGHF, Hidden Palace]
Asteroids (prototype) [VGHF, Hidden Palace]
Barbie - Game Girl (prototype) [VGHF, Hidden Palace]
Battle Ships (Spain, prototype) [VGHF, Hidden Palace]
Blaster Master Boy (USA, prototype) [VGHF, Hidden Palace]
Bomb Jack (earlier prototype) [VGHF, Hidden Palace]
Bomb Jack (later prototype) [VGHF, Hidden Palace]
Bonk's Adventure (USA, prototype) [VGHF, Hidden Palace]
Bubble Ghost (prototype) [VGHF, Hidden Palace]
Catrap (prototype) [Forest of Illusion, Swanhubstream]
Cosmo Tank (USA, prototype) [VGHF, Hidden Palace]
Dropzone (prototype, alt) [VGHF, Hidden Palace]
Gauntlet II (prototype) [Forest of Illusion, Rezrospect]
Ghostbusters II (prototype) [VGHF, Hidden Palace]
Kung-Fu Master (prototype) [Forest of Illusion, FNeogeo]
Mysterium (prototype) [Forest of Illusion, Rezrospect]
Obélix (Europe, French / German, prototype) [Forest of Illusion]
Prince of Persia (prototype) [Forest of Illusion, FNeogeo]
The Blues Brothers (prototype) [Forest of Illusion, FNeogeo]
Triumph (prototype) [Gaming Alexandria]

---
## [ryancabanas/LearnReact](https://github.com/ryancabanas/LearnReact)@[a4edd5d474...](https://github.com/ryancabanas/LearnReact/commit/a4edd5d4747a786587a613107dde9afad193e036)
#### Wednesday 2022-06-22 03:34:35 by Ryan Cabanas

69. Demo App: Adding a Chart
70. Adding Dynamic Styles

- This is a HUGE commit.  In this commit we're adding a chart with vertical
  month bars that are the sum of the expense values by month for the given year.

- You can see that many new components were created:

  - `ChartBar.js`: Displays the individual vertical bars of the overall chart.
  - `Chart.js`: Displays the vertical bars together in a single chart.
  - `ExpensesChart.js`: This is an additional layer that allows us to customize
    how we will use the `Chart.js` component.  This is a really cool design
    because the `Chart.js` component was built with a generic approach in mind
    so that it could be reused for whatever data points we want/need to use with
    it.  By adding the extra `ExpenseChart.js` component layer, it allows us to
    decide how we wish to use the generic `Chart.js` component ***this*** time.

    Along with the specific `ExpenseChart.js` component, we modify the `Expenses.js`
    component, which passes expenses-specific data to the expenses-specific
    `ExpensesChart.js` component and then from there we pass the data to the
    `Chart.js` component in a generic manner.

- The CSS files really make this chart work and I don't know anything about CSS,
  obviously, by looking at what the instructor was able to do with it in this
  chart, which, I think, was amazing.

- The instructor began by creating the `Chart.js` component first.  In there, he
  built it out as if the `ChartBar.js` component already existed.  This allowed
  him to flexibly declare whatever he wanted the `ChartBar.js` component to
  expect.  ***Then*** he built the `ChartBar.js` component around that.

  In the `Chart.js` component, he also added some logic to calculate the max
  value across all vertical bar values and then passed that to the `ChartBar.js`
  component.

- In the `ChartBar.js` component, he used a lot of `div` elements with CSS
  classes.  Each layer adding something to the overall chart design.  Again, I
  don't know enough about CSS to appreciate this, but it's good to try and
  remember this approach for later.

  Oh.  Also, here in this component, he dynamically modified the CSS/styling by
  calculating a value here in the component and then setting the dynamic value
  of the `div` element with `style={{height: barFillHeight}}`, where the outer
  curly braces are for the expression, but the inner curly braces are really
  for an object, just like CSS uses.  So you really are dynamically setting the
  CSS styling here in the `div` element.  He also said that if you happen to be
  working with a CSS property that uses a hyphen in it's name, then you can either
  wrap the property name in quotes, of you can use camel case and React will
  interpret that into the hyphened name for you.

- In the `ExpensesChart.js` component, we do a lot of expense-specific chart
  prep work.  We built out the array with months and then set the sum value for
  the objects (months) within that array.

  Then the info generated here in `ExpensesChart.js` is passed to the `Chart.js`
  component.

- Lastly we have changes to the `Expenses.js` component, which just displays the
  `ExpensesChart.js` component and passes the filtered expenses data to the
  `ExpensesChart.js` component.

---
## [mroccyen/redis](https://github.com/mroccyen/redis)@[0e5b813ef9...](https://github.com/mroccyen/redis/commit/0e5b813ef94b373f82bc75efcf3405f2c81af3dc)
#### Wednesday 2022-06-22 03:36:11 by yoav-steinberg

Multiparam config set (#9748)

We can now do: `config set maxmemory 10m repl-backlog-size 5m`

## Basic algorithm to support "transaction like" config sets:

1. Backup all relevant current values (via get).
2. Run "verify" and "set" on everything, if we fail run "restore".
3. Run "apply" on everything (optional optimization: skip functions already run). If we fail run "restore".
4. Return success.

### restore
1. Run set on everything in backup. If we fail log it and continue (this puts us in an undefined
   state but we decided it's better than the alternative of panicking). This indicates either a bug
   or some unsupported external state.
2. Run apply on everything in backup (optimization: skip functions already run). If we fail log
   it (see comment above).
3. Return error.

## Implementation/design changes:
* Apply function are idempotent (have no effect if they are run more than once for the same config).
* No indication in set functions if we're reading the config or running from the `CONFIG SET` command
   (removed `update` argument).
* Set function should set some config variable and assume an (optional) apply function will use that
   later to apply. If we know this setting can be safely applied immediately and can always be reverted
   and doesn't depend on any other configuration we can apply immediately from within the set function
   (and not store the setting anywhere). This is the case of this `dir` config, for example, which has no
   apply function. No apply function is need also in the case that setting the variable in the `server` struct
   is all that needs to be done to make the configuration take effect. Note that the original concept of `update_fn`,
   which received the old and new values was removed and replaced by the optional apply function.
* Apply functions use settings written to the `server` struct and don't receive any inputs.
* I take care that for the generic (non-special) configs if there's no change I avoid calling the setter (possible
   optimization: avoid calling the apply function as well).
* Passing the same config parameter more than once to `config set` will fail. You can't do `config set my-setting
   value1 my-setting value2`.

Note that getting `save` in the context of the conf file parsing to work here as before was a pain.
The conf file supports an aggregate `save` definition, where each `save` line is added to the server's
save params. This is unlike any other line in the config file where each line overwrites any previous
configuration. Since we now support passing multiple save params in a single line (see top comments
about `save` in https://github.com/redis/redis/pull/9644) we should deprecate the aggregate nature of
this config line and perhaps reduce this ugly code in the future.

---
## [rayankoliai/finalprojectibm](https://github.com/rayankoliai/finalprojectibm)@[4272638f35...](https://github.com/rayankoliai/finalprojectibm/commit/4272638f355ae83036119f62803358166d531bcc)
#### Wednesday 2022-06-22 04:00:16 by rayankoliai

CONTRIBUTING.md

Contributing
When contributing a major change to this repository, please first discuss the change you wish to make via an issue or via Slack in the #racial-justice-legit-info channel in the Call for Code Slack workspace. Minor issues can simply be addressed by sending by a pull request.

All pull requests will require you to ensure the change is certified via the Developer Certificate of Origin (DCO). The DCO is a lightweight way for contributors to certify that they wrote or otherwise have the right to submit the code they are contributing to the project.

Please note we have a Code of Conduct, please follow it in all your interactions with the project and its community.

Coding Standards
This project adheres to the PEP 8 Python Coding Style Guidelines, Django naming conventions, and other standards. See STYLE.md for details.

Programming Languages
Scripts are written for "bash" shell. Python code is written at the Python 3.6 level.

Managing Dependencies
Install or uninstall all dependencies using these commands while you are in the pipenv shell:

(cfc) $ pipenv install <program>"
(cfc) $ pipenv lock -r > requirements.txt"
The pipfile, pipfile.lock and requirements.txt will be part of the git commit/pull-request to be reviewed.

Pull Request Process
Fork the repository.
Commit your changes to your fork.
Submit a pull request. Don't forget to add yourself in the Authors file!
Handle any feedback before the request is merged.
Accept our sincere Thank You!
Code of Conduct
Our Pledge
In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

Our Standards
Examples of behavior that contributes to creating a positive environment include:

Using welcoming and inclusive language
Being respectful of differing viewpoints and experiences
Gracefully accepting constructive criticism
Focusing on what is best for the community
Showing empathy towards other community members
Examples of unacceptable behavior by participants include:

The use of sexualized language or imagery and unwelcome sexual attention or advances
Trolling, insulting/derogatory comments, and personal or political attacks
Public or private harassment
Publishing others' private information, such as a physical or electronic address, without explicit permission
Other conduct which could reasonably be considered inappropriate in a professional setting
Our Responsibilities
Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

Scope
This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team on Slack in the #racial-justice-legit-info channel.

All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident.Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

Attribution
This Code of Conduct is adapted from the Contributor Covenant, version 1.4, available at http://contributor-covenant.org/version/1/4

---
## [newstools/2022-herald-live](https://github.com/newstools/2022-herald-live)@[3a5a22666b...](https://github.com/newstools/2022-herald-live/commit/3a5a22666b1ecbceca68e49698bd7e32491f6c99)
#### Wednesday 2022-06-22 04:16:40 by Billy Einkamerer

Created Text For URL [www.heraldlive.co.za/news/2022-06-22-life-imprisonment-for-man-who-killed-his-legal-practitioner-girlfriend/]

---
## [ini23/android_kernel_xiaomi_sdm660_southwest](https://github.com/ini23/android_kernel_xiaomi_sdm660_southwest)@[9e360b90ea...](https://github.com/ini23/android_kernel_xiaomi_sdm660_southwest/commit/9e360b90ea0e5a9c298537995330da947a7ac7a6)
#### Wednesday 2022-06-22 06:04:15 by Angelo G. Del Regno

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
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Kneba <abenkenary3@gmail.com>
Signed-off-by: Tiktodz <kuplemarkeple@gmail.com>

---
## [Skarlso/cluster-api-provider-aws](https://github.com/Skarlso/cluster-api-provider-aws)@[867afc7ac7...](https://github.com/Skarlso/cluster-api-provider-aws/commit/867afc7ac718621a11e00fc2b05589ac2548d4d5)
#### Wednesday 2022-06-22 06:14:43 by Claudia Beresford

Fail apidiff make target when git fails

This is a fairly simple fix to ensure that when `git diff` fails on the
`make apidiff` target, the exit code is actually picked up by make.
Previously the exit code from `diff` was "swallowed" by the `if`.

eg:
```
$ cat Makefile
thing:
        if (exit 1); then \
		echo foo; \
        fi
        echo "still here"

$ make thing
still here
$ echo $?
0
```

What we want:
- exit 1 when `git diff` fails
- exit 0 when `grep` fails
- call `go-apidiff` when `git diff` and `grep` succeeds
- exit 1 when `go-apidiff` fails

This is honestly a complete pain to do in a Makefile.

I tried capturing output, moving everything to a script, calling from
one thing to another. But really this is just tricky to do the way we
want in Make.

So, if we can live with a little repetition, we can do the following:
- Check the `git diff` can run, exit 1 if not
- Run the `git diff` again, this time piping the successful command to
  `grep`
- If `grep` fails, then no worries, the target will roll on and exit 0
  like it always has.
- If `grep` succeeds then the `go-apidiff` tool is called and the target
  runs as intended.

------

In the case of `$(APIDIFF_OLD_COMMIT)`, there is some annoying `make`
magic going on here. Which I can't simply make fail since it will cause any
job which uses something in this Makefile to fail out of proximity.
The `shell` is expanded when the file is loaded meaning even targets
which do not care about the value will end up erroring (but not exiting)
when it fails. These are not errors which impact the target's run, but
they look annoying in CI.

Since this var is only used by `apidiff`, we can move it into that
target so it is only evaluated when specifically called.

---
## [alphagov/govuk-prototype-kit](https://github.com/alphagov/govuk-prototype-kit)@[92625aac97...](https://github.com/alphagov/govuk-prototype-kit/commit/92625aac9758543882ad535aa0d5067abe12a15e)
#### Wednesday 2022-06-22 07:55:15 by Laurence de Bruxelles

Change tests to generate a release archive only once

Use a lockfile to make sure that if the test helper `mkReleaseArchive()`
is called more than once, it won't create more than one
`create-release-archive` process. The behaviour we want is that it all
calls will block until the initial process has finished.

The way I figured to do that was that all calls try and acquire a
lockfile (atomically), if that lockfile is already held that means
another call is already creating the release archive. When the lockfile
is released, the process should have successfully created a release
archive, so no extra work is needed.

Unfortunately, in Node.js it seems there is no way to block waiting for
a lockfile to be released, so we have to rewrite the test utils and all
relevant tests to be asynchronous. To be fair they should have been
asynchronous in the first place, but it was still a very painful
process.

Note that I haven't rewritten the scripts in `cypress/scripts` to use
async functions; without the use of top-level await it was a bit more
effort than I was prepared to do, compounded with the fact that
there doesn't seem to be an easy way to await `child_process.spawn()`
(`util.promisify` doesn't work), and async `child_process.exec()` and
`child_process.execFile()` don't do `stdio: 'inherit'`. Maybe the only
way around it is to use the `execa` library (: Anyway I couldn't be
dealing with that, so now we have to deal with duplication in
`__tests__/util`. There are ...ways... to reduce the duplication
(proper-lockfile does this with its `lib/adapter` module) but they are a
bit magic, and plus it means writing our code using callbacks, which is
just... woof. No.

Anyway as you can tell this is has been a great learning opporunity :')
Just use async the first time and save myself the pain later!!

---
## [32th-System/deltarune_repainted](https://github.com/32th-System/deltarune_repainted)@[b714ae750b...](https://github.com/32th-System/deltarune_repainted/commit/b714ae750b475d6108f8e9686d64446a7225cf75)
#### Wednesday 2022-06-22 08:19:01 by Fatfuck22

Hello Reddit, I have a problem. My dad has begun had identity issues ever since I introduced him to Team Fortress 2.

So I decided to introduce my not so gaming father to Team Fortress 2 in order to strengthen our bond a little, I’m not quite sure if it worked. He started off by testing random characters such as the Scout, Soldier, Engineer, Demoman, however, there was only one class he played for over 2 minutes, the Heavy Weapons Guy. At first I guess I was glad that he was enjoying the game, and didn’t care for much, but I started getting worried when he wouldn’t come down for dinner, and when he finally did come down, he had put on this terrible fake Russian accent. He didn’t say too much of the Heavy quotes, but he started calling my mom by the name of medic, I thought it would be over by the next day. I woke up early and found my dad in the kitchen, he looked like an absolute mess, but still put on a smile, I genuinely thought everything was like normal again, he just had trouble sleeping, until he told me, again in a stupid fake Russian accent, he told me that he had been up all night playing Team Fortress 2. Not only that but he wasn’t eating his normal breakfast, he was making the iconic sandwich, only now did I understand how serious of an issue this was, before leaving to work with the sandwich in his mouth while saying “I AM FULL OF SANDWICH! AND I AM GOING TO WORK!” I was left speechless, I stood still for about 10 minutes thinking of the monster I’ve created. I was greeted by my mother with a worried expression and I could only imagine how it must be to see the love of your life change personality in less than 15 hours! I was hoping he’d realize by the time he got home from work that he can’t be doing this and maintain his job or friends. When I came home from school I found him slouched on the couch with, once again, a sandwich in his hand, he noticed me and called to me, “Scout! Get over here!” I quickly yelled at him, “DAD! I AM NOT THE SCOUT!” only to see him shake his head, “Scout, I am not your father, I am the Heavy Weapons Guy, and THIS, is my weapon!” only to show off his newly bought gaming mouse. I quickly ran upstairs only to start writing this, what do I do Reddit? He has yet not found out about the whole pootis meme and I’m scared of what will happen once he does, if this keeps up my parents are sure to get a divorce! Help me Reddit!

---
## [teo8192/dwm](https://github.com/teo8192/dwm)@[67d76bdc68...](https://github.com/teo8192/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-06-22 08:22:10 by Chris Down

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
## [peff/git](https://github.com/peff/git)@[f727008556...](https://github.com/peff/git/commit/f72700855650ec21c123078df0a36ad9cdf16b6c)
#### Wednesday 2022-06-22 08:32:18 by Jeff King

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
## [peff/git](https://github.com/peff/git)@[d9467050fd...](https://github.com/peff/git/commit/d9467050fd14e2008e6533d59e94dfc8cb92c410)
#### Wednesday 2022-06-22 08:32:24 by Jeff King

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
## [rubyzee/android_kernel_xiaomi_mt6768](https://github.com/rubyzee/android_kernel_xiaomi_mt6768)@[110b809c37...](https://github.com/rubyzee/android_kernel_xiaomi_mt6768/commit/110b809c37a1c5cbdfcfcc3b29341ff7bb449f9c)
#### Wednesday 2022-06-22 09:09:10 by Peter Zijlstra

sched/core: Fix ttwu() race

Paul reported rcutorture occasionally hitting a NULL deref:

  sched_ttwu_pending()
    ttwu_do_wakeup()
      check_preempt_curr() := check_preempt_wakeup()
        find_matching_se()
          is_same_group()
            if (se->cfs_rq == pse->cfs_rq) <-- *BOOM*

Debugging showed that this only appears to happen when we take the new
code-path from commit:

  2ebb17717550 ("sched/core: Offload wakee task activation if it the wakee is descheduling")

and only when @cpu == smp_processor_id(). Something which should not
be possible, because p->on_cpu can only be true for remote tasks.
Similarly, without the new code-path from commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

this would've unconditionally hit:

  smp_cond_load_acquire(&p->on_cpu, !VAL);

and if: 'cpu == smp_processor_id() && p->on_cpu' is possible, this
would result in an instant live-lock (with IRQs disabled), something
that hasn't been reported.

The NULL deref can be explained however if the task_cpu(p) load at the
beginning of try_to_wake_up() returns an old value, and this old value
happens to be smp_processor_id(). Further assume that the p->on_cpu
load accurately returns 1, it really is still running, just not here.

Then, when we enqueue the task locally, we can crash in exactly the
observed manner because p->se.cfs_rq != rq->cfs_rq, because p's cfs_rq
is from the wrong CPU, therefore we'll iterate into the non-existant
parents and NULL deref.

The closest semi-plausible scenario I've managed to contrive is
somewhat elaborate (then again, actual reproduction takes many CPU
hours of rcutorture, so it can't be anything obvious):

					X->cpu = 1
					rq(1)->curr = X

	CPU0				CPU1				CPU2

					// switch away from X
					LOCK rq(1)->lock
					smp_mb__after_spinlock
					dequeue_task(X)
					  X->on_rq = 9
					switch_to(Z)
					  X->on_cpu = 0
					UNLOCK rq(1)->lock

									// migrate X to cpu 0
									LOCK rq(1)->lock
									dequeue_task(X)
									set_task_cpu(X, 0)
									  X->cpu = 0
									UNLOCK rq(1)->lock

									LOCK rq(0)->lock
									enqueue_task(X)
									  X->on_rq = 1
									UNLOCK rq(0)->lock

	// switch to X
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	switch_to(X)
	  X->on_cpu = 1
	UNLOCK rq(0)->lock

	// X goes sleep
	X->state = TASK_UNINTERRUPTIBLE
	smp_mb();			// wake X
					ttwu()
					  LOCK X->pi_lock
					  smp_mb__after_spinlock

					  if (p->state)

					  cpu = X->cpu; // =? 1

					  smp_rmb()

	// X calls schedule()
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	dequeue_task(X)
	  X->on_rq = 0

					  if (p->on_rq)

					  smp_rmb();

					  if (p->on_cpu && ttwu_queue_wakelist(..)) [*]

					  smp_cond_load_acquire(&p->on_cpu, !VAL)

					  cpu = select_task_rq(X, X->wake_cpu, ...)
					  if (X->cpu != cpu)
	switch_to(Y)
	  X->on_cpu = 0
	UNLOCK rq(0)->lock

However I'm having trouble convincing myself that's actually possible
on x86_64 -- after all, every LOCK implies an smp_mb() there, so if ttwu
observes ->state != RUNNING, it must also observe ->cpu != 1.

(Most of the previous ttwu() races were found on very large PowerPC)

Nevertheless, this fully explains the observed failure case.

Fix it by ordering the task_cpu(p) load after the p->on_cpu load,
which is easy since nothing actually uses @cpu before this.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Paul E. McKenney <paulmck@kernel.org>
Tested-by: Paul E. McKenney <paulmck@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Link: https://lkml.kernel.org/r/20200622125649.GC576871@hirez.programming.kicks-ass.net
Signed-off-by: Egii <regidesoftian@gmail.com>

---
## [AngelicosPhosphoros/rust](https://github.com/AngelicosPhosphoros/rust)@[07f586fe74...](https://github.com/AngelicosPhosphoros/rust/commit/07f586fe746a362fdebfc1cec0016dd024780dce)
#### Wednesday 2022-06-22 10:43:35 by Dylan DPC

Rollup merge of #96642 - thomcc:thinbox-zst-ugh, r=yaahc

Avoid zero-sized allocs in ThinBox if T and H are both ZSTs.

This was surprisingly tricky, and took longer to get right than expected. `ThinBox` is a surprisingly subtle piece of code. That said, in the end, a lot of this was due to overthinking[^overthink] -- ultimately the fix ended up fairly clean and simple.

[^overthink]: Honestly, for a while I was convinced this couldn't be done without allocations or runtime branches in these cases, but that's obviously untrue.

Anyway, as a result of spending all that time debugging, I've extended the tests quite a bit, and also added more debug assertions. Many of these helped for subtle bugs I made in the middle (for example, the alloc/drop tracking is because I ended up double-dropping the value in the case where both were ZSTs), they're arguably a bit of overkill at this point, although I imagine they could help in the future too.

Anyway, these tests cover a wide range of size/align cases, nd fully pass under miri[^1]. They also do some smoke-check asserting that the value has the correct alignment, although in practice it's totally within the compiler's rights to delete these assertions since we'd have already done UB if they get hit. They have more boilerplate than they really need, but it's not *too* bad on a per-test basis.

A notable absence from testing is atypical header types, but at the moment it's impossible to manually implement `Pointee`. It would be really nice to have testing here, since it's not 100% obvious to me that the aligned read/write we use for `H` are correct in the face of arbitrary combinations of `size_of::<H>()`, `align_of::<H>()`, and `align_of::<T>()`. (That said, I spent a while thinking through it and am *pretty* sure it's fine -- I'd just feel... better if we could test some cases for non-ZST headers which have unequal and align).

[^1]: Or at least, they pass under miri if I copy the code and tests into a new crate and run miri on it (after making it less stdlibified).

Fixes #96485.

I'd request review ``@yaahc,`` but I believe you're taking some time away from reviews, so I'll request from the previous PR's reviewer (I think that the context helps, even if the actual change didn't end up being bad here).

r? ``@joshtriplett``

---
## [jcs-PR/melpa](https://github.com/jcs-PR/melpa)@[570bde6b4b...](https://github.com/jcs-PR/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Wednesday 2022-06-22 12:38:00 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [planetscale/vitess](https://github.com/planetscale/vitess)@[dbfb9a49f7...](https://github.com/planetscale/vitess/commit/dbfb9a49f7c3b067221d0aae0d3c0285e6baf098)
#### Wednesday 2022-06-22 12:55:48 by Andrew Mason

[vtadmin] Add infrastructure for generating authz tests for vtadmin (#10397)

* Add infrastructure for generating authz tests for vtadmin

The lack of verifying authz checks are where they should be is one of the
most glaring issues in vtadmin (in my opinion; it's also my "fault" things
are this way). At the same time, writing all the code by hand to verify
every single endpoint would be a giant pain (which is the main reason
things are this way). So, let's codegen all the bits we don't care about!
The bonus here is that the config.json now can serve as authoritative on
what permissions are required for what endpoints.

The goal here is to have the config primarily specify the rules needed for
each endpoint, with as minimal "overhead" (currently specifying test cases
and mock data) as possible.

I want to separate the introduction of this setup from its complete
adoption, so I will submit a follow-up change that adds the rest of the
endpoint tests.

Signed-off-by: Andrew Mason <andrew@planetscale.com>

* add missing license headers

Signed-off-by: Andrew Mason <andrew@planetscale.com>

* Add make target and CI check

Signed-off-by: Andrew Mason <andrew@planetscale.com>

---
## [ProgrammerParty/.github](https://github.com/ProgrammerParty/.github)@[f815cc5334...](https://github.com/ProgrammerParty/.github/commit/f815cc5334024d78ede4e416a52a65d68c9b65e4)
#### Wednesday 2022-06-22 13:57:25 by DMGHa

Merge pull request #1 from ProgrammerParty/pls

fuck you

---
## [isaacphysics/isaac-react-app](https://github.com/isaacphysics/isaac-react-app)@[7a8df37c78...](https://github.com/isaacphysics/isaac-react-app/commit/7a8df37c78e257c987f9db6fb8acb3dac2aeb2c0)
#### Wednesday 2022-06-22 14:17:02 by Chris Purdy

Evil hack to get keyboard working on cloze questions

This takes `useKeyboardSensor` from `react-beautiful-dnd`, and adds some extra (nasty) stuff so that it behaves as expected with cloze questions. Since you can only interact with one cloze question at a time, this should work fine in theory, and is certainly better than the non-functioning keyboard interaction we had already.
It might break if the question rerenders underneath it, but it should break nicely and just cancel any drag in progress.

---
## [ImBroke40/HELP-ME-PLEASE](https://github.com/ImBroke40/HELP-ME-PLEASE)@[c19f2b99bb...](https://github.com/ImBroke40/HELP-ME-PLEASE/commit/c19f2b99bbe59abc82bc2f0b7ff130e39bb9eeb5)
#### Wednesday 2022-06-22 14:32:55 by ImBroke40

Update first.py

So the issue is whenever you answer No to the question - print("Uhm- Uh, hello? Is this the uh- Suicide Prevention Hotline or-?")
    
    Q1A = input("Type Yes or No to continue ") - it skips all the code where it says - if Q1A == "No" or Q1A == "no":
        print("Oh... Sorry I'll try a different num- you know what, nevermind, it's easier to finish it this way. *Hangs up*")
        time.sleep(2)
        print("The next day you sit down on your leather couch, turn on the tv, and are greeted with the famaliar sound of the news coverage, it goes on for what seems like forever, but then, the screen turns pure black, \n not the shitty dark blue it turns to when it's turned off, but pure black, you get up to check on the router to see if the wifi is down, but as soon as you do, the tv switches to a breaking news channel.") 
        time.sleep(4)
        print(" TV REPORTER: [Late this evening in North Jester, 34 year old Jessica McCaine has had an unholy ending to her 17 year careeer as an actress.]")
        time.sleep(2)
        print("{SUBTITLES: THESE NEXT FEW PICTURES CONTAIN GRAPHIC AND MATURE CONTENT, VIEWER DISCRETION IS ADVISED.} \n The first picture on the screen, showing her hanging from a rope that is tied to the bars on her balcony. \n Her head and eyes rolled back, staring right at the sky. Her mouth, hastily sewn shut, small streaks of blood leaking from the holes on her lips.") - and just exits any help is appreciated, thx!

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[763a10d1cc...](https://github.com/jlsnow301/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Wednesday 2022-06-22 15:23:18 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)@[5a37518e42...](https://github.com/RocketChat/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Wednesday 2022-06-22 16:29:44 by Ben Wiederhake

[FIX] Client-generated sort parameters in channel directory  (#25768)

## Proposed changes (including videos or screenshots)
- In the web-client, sorting the channel directory by "Last Message" raises the error "Invalid sort parameter provided".

I don't think a screenshot is necessary, but if you'd like one anyway, here it is:

![Bildschirmfoto_2022-06-06_12-54-34](https://user-images.githubusercontent.com/2690845/172147996-e9942daf-6819-4eee-afa4-b1c6bce7a650.png)


## Issue(s)
Closes #25695

## Steps to test or reproduce

- Open the web client, i.e. navigate your browser to `https://rocketchat.$DOMAIN/home`
- Click the "Directory" button in the top left, (or just navigate directly to `https://rocketchat.$DOMAIN/directory/channels`)
- In the table header, click on "Last message" once
- In the table header, click on "Last message" again

Expected behavior: Clicking "Last message" turns on and then toggles sorting by the date of the last message, either first ascending and then descending, or the other way around.

Actual behavior: The first click sorts the messages in ascending order (good!), the second click shows a red warning box "FIXME", the table content disappears, and is replaced by throbbing grey placeholders.

### "Good" request (ascending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A1%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":1}
count | 25
```

Response:
```
{"result":[{"_id":"AAAAAAAAAAAAAAAAA","name":"foobar","fname":"foobar","t":"c","usersCount":10,"ts":"2019-01-01T00:00:00.000Z","default":false,"lastMessage":{"_id":"AAAAAAAAAAAAAAAAA","rid":"AAAAAAAAAAAAAAAAA","msg":"Hello, World!","ts":"2019-01-01T00:00:00.000Z","u":{"_id":"AAAAAAAAAAAAAAAAA","username":"normaluser","name":"normaluser"},"unread":true,"_updatedAt":"2019-01-01T00:00:00.000Z","urls":[],"mentions":[],"channels":[]},"description":"Obviously, this JSON response is heavily censored."}],"count":25,"offset":0,"total":52,"success":true}
```

(Obviously, this JSON response is heavily censored, but you get the gist: It was successful.)

### "Bad" request (descending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A0%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":0}
count | 25
```

Response:
```
{"success":false,"error":"Invalid sort parameter provided: \"{\"lastMessage\":0}\" [error-invalid-sort]","errorType":"error-invalid-sort","details":{"helperMethod":"parseJsonQuery"}}
```

## Further comments

Version on the server where I noticed this: `https://rocketchat.$DOMAIN/api/info` returns `{"version":"4.8","success":true}`. According to the "Releases" page, this version appeared 5 days ago, so I believe this is up to date.

### The journey to here

For some reason, the descending order uses the wrong magic number "0", and the server can't interpret that. However, this *used* to work, so I'm not very sure about this.

The error message appears in the source code of the entire organization exactly once: https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L42
So I'll guess that this is the line of code that generated this particular message.

A few lines above we see that the server only knows 1 and -1 as magic numbers for the sorting:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L35
This matches the observed bug: The browser sends 1 (which works) and 0 (which doesn't work).

Generally, it seems that the web client actually uses the strings "asc" and "desc" internally, which are hard to mix up. So I assume that it's the conversion of that is broken somehow.

Exactly this seems to be the case here:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/client/views/directory/hooks.js#L11

The code around it produces exactly the kind of query seen in the network log, and can also produce the buggy parameter `sort: 0`. This either fixes bug #25695, or a different bug of the same kind.

I am not sure how to add tests for this, can someone do this for me or show me where to start? I'm actually just an end-user and "accidentally" found the fix for the bug while writing the bug report ^^'

EDIT: Rebased for convenience, and to re-check CI.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[10d1039ef8...](https://github.com/mrakgr/The-Spiral-Language/commit/10d1039ef8f31a7de3ea60ace89ca7dfffd6f126)
#### Wednesday 2022-06-22 18:08:58 by Marko Grdinić

"10:25am. Let me chill a bit and then I will post the review. After that it will be time to start.

10:55am. Let me start. First thing's first - I'll post the review on the Simulacrum blog.

...Actually, let me read Frieren first.

Done. Let me adjust the review a bit. I'll also put some links I've found in the meantime.

///

Half the year is over and I've spent six month cultivating my [art skills](https://twitter.com/Ghostlike). Right now I am recovering from a failed attempt and illustrating the flying golden city, so it is the ideal time to do the halfly review. It is an interesting thing. In programming, if you want to save time, the first choice is always to find a library that does what you want and make use of it. Languages, and all other considerations are secondary to that. Though pro programmers are generally weak and start to panic whenever it is time to learn something new, switching languages is not a big deal.

In art, switching 3d software, generally is a big deal. So far, I've used many different 3d software: Blender, Moi, Clarisse, Zbrush, Substance Painter, Houdini, and just today I gave 3ds Max a try. All of these software have different navigation. It is like trying to drive several different types of cars if every one of them had different ways of steering and their pedals had their positions swapped. I have no idea why they do this, but it makes context switching between them quite hard and it constantly disrupts my muscle memory. A few days ago I tried Clarisse after not using it for a few months and if there was a camera in my room it would show me practicing the super saiyan transformation.

I had the idea of trying out kitbashing. This is not something I could ever imagine failing at. Kitbashing is just getting existing models from a library and putting them around the scene instead of taking the longer way, which is modeling the assets yourself. The [kitbashed models](https://kitbash3d.com/products/manhattan?_pos=1&_psq=manh&_ss=e&_v=1.0) are done by pros and look great. The particular kit I linked to has 12.5m polys, and the .blend file is 2.6gb. When I try to open it, Blender lags a lot, and even displaying the models as bounding boxes in the viewport does not help much. I tried making use of them in Clarisse, but realistically, I am at my limit here. I do not have room in my head for much more than Blender and Moi. The models are simply too high poly, and are unusable without significant hardware upgrades to my rig. Maybe if I got the 64-core Threadripper and 128gb I could upgrade my style so it incorporates kitbashing, but right now I'll just make do with what I have.

Me trying to make use of procedural city generation and kitbashing is more a matter of principle than actual need. Modeling things by yourself can be quite fast depending on the amount of detail you are going for. And I definitely don't need much.

It is just frustrating to fail in such a manner, to do what should be the right thing, only for the wrong thing to end up being right. Unlike images which you can downscale very easily, 3d models aren't so straightforward, and I am better modeling on my own. This is a good lesson for me, 2d artists just get their references and draw. From here on out, I'll get my refs and model. After I am done with the flying city scene, I'll move on to character modeling and finally bring Euclid along with the rest of the NPCs into light. After that I'll move on to music.

I've finally had some success with making use of ML as well. While my reinforcement learning attempts were a complete disaster, I got lucky this time and found something good almost right off the bat. It started with me playing with the [Deep Dream Generator](https://deepdreamgenerator.com/) and finding the results interesting, and then looking for something I could run on my own rig. I found [CAST](https://github.com/zyxElsa/CAST_pytorch) and managed to adapt it so it can do style transfer even on my weak rig. You can see examples of it in action on my Twitter profile. My plan so far is to do some low-mid poly modeling, render it using Cycles/Luxcore and then do style transfer to get rid of the plastic 3d look. For charas, I will spend some time sculpting them myself in 3d, style transferring and then painting over the image by hand until I am satisfied. Last week the plan was to get a char modeling program, but given how poorly the urban procedural generation experiment went, I am very skeptical of taking any more shortcuts.

Right now my skills are just about good enough to be an apprentice illustrator, but definitely not something like a mangaka. I know my limits which is why I am aiming for a VN, rather than a manga. If I went for a manga, all my time would be consumed by drawing even if I were good at it. I am lazy and want to give myself breathing room. I'll make a resolution: 1 scene or 1 character a week, over time that kind of effort will pile up and my skills will grow from their current low 3/5 rank. I admire steadiness and consistency rather than artfulness, so that is what I will aspire to reach. I have a lot of breadth, and in the next six months I'll aim to exchange that for depth in a particular style.

In case you are wondering, 5/5 is the pinnacle of human achievement, and I'd put people like Kim Jung Gi and Murata Yusuke at such a level. I am not even going to try beating them, getting to peak 3/5 would be enough for me. Though 5/5 is the limit of humans, it is not the limit in any absolute sense. And it has actually been exceeded at the start of the year by [diffusion models](https://www.youtube.com/results?search_query=dalle+2). Honestly, when OpenAI said that GPT-3 was too dangerous to release, I thought that deep learning had jumped the shark. AlphaGo was an exciting moment, but the rest of the RL achievements since 2016 are huge circus acts, more like ambushes than legitimate achievements. The same goes for pro beating poker bots.

But what they've done here I find admirable. If I could run something like DALLE 2 on my home rig, or even rent it cheaply, it would completely change the way I did art and I probably would not have bothered investing so much into 3d skills. I'd put it at low rank 6. At peak rank 6 you'd have a proper memory system that you could tell it - 'This is a sketch of Euclid, remember him, and make it anime.' And 'Generate him from the sides and the back in several different versions, I'll tell you which ones are suitable to be his actual form.' To be peak rank 6 the system should be capable of targeted memory formation much like humans. Today's transformers have only short term memory, and would forget what they know in a couple of conversations. The static weights of a NN are long term memories, but the way they are formed using SGD is not principled, and as a consequence the further you get from training on static datasets the more issues show up.

Though not as huge as GPT-3 which had almost 200b, DALLE 2 does have 5b parameters, so absolutely no home rig could ever run it. 5b params would require 20gb just to store the weights. It would probably require a cluster just for a forward pass on a decently sized image. AI chips are supposedly here, but I haven't felt them making any impact, so who knows when we are going to get enough computing power to play with non-toy models. The style transfer net that I got was a fortuitous encounter, and I am not likely to get another.

It is an arms race, and it does not feel like I've made a single step forward with my own efforts. I look at OpenAI and Deepmind which I see as competitors, and it feels like they are far ahead. Sure they have big brains and pockets, but none of the fundamental concerns that I've had with deep learning methods have changed.

Deepmind might have made AlphaGo, and I still couldn't run it today. In contrast, 8 years after the Deep Blue and Kasparov match, you could get something as good at it on your home computer.

You get new training methods and architectures, you have advances in generative modeling, you have proof of how great matrix multiplication truly is, but none of those advances will change that deep learning is not capable of continuous and long term learning. There are a lot of brains doing research, but there were no sparks of genius produced. When it happens the Singularity will ignite.

It is going to happen. GPUs won't stay dominant forever and the hardware necessary to properly cultivate ML skills will arrive. With strong enough hardware, there will be ways of having it itself tell us how to optimally use it. Right now we are good at making use of GPUs, but at the same time restricted to what they are good at. I feel the timeline is a bit wonky, the memristor breakthroughs failed to properly manifest, if they had we could have had terabyte non-volatile memory devices suitable for all sorts of tasks, and especially AI.

If you look at the current GPU development, it is struggling. NVidia is silently ramping up the power consumption to get the performance increases inline with predictions and that way of getting improvements is shallow, it won't last for long. In fact, what you'd want to see is power consumption going in the other direction.

The main low hanging fruit to be plucked in ML is sparsity, GPUs aren't suited for it, but AI chips are so that is where the river will flow. They will also pave the way for true multi-core processing. 7 years ago when I got my rig, I opted for a 4 core CPU, if I got one now for the same price it would be 8 cores. If Moore's Law was alive a 64 core CPU would be mid end instead of very high end. AI chips will bridge the gap instead. Being able to use them will bring a change in mindset. It is a lot easier to learn something if the circumstances force you to do it, so having to do async programming should be beneficial for research into asynchronous learning algorithms. Getting rid of layerwise hierarchy is similar to getting rid of temporal hierarchy, so following that path should give insights into the true nature of long term and continuous learning. It is a complete mystery how the brain does its long term memory formation. I couldn't figure it out, and I do not not even understand why other people cannot figure it out. It is even a mystery whether once that is figured out, it would be possible to derive an algorithm that could be run on the GPUs.

For me, style transfer is the most convenient route of getting back into ML. If I can make some money through Heaven's Key I could reinvest that into better hardware, and ML development. The CAST net given by the author is only 7m params, using a bigger net, and trying out different training methods that I have in mind should lead to improvements. I wanted to do this through RL. As I said, it is a race, and I sure was pissed to not be allowed to even run out of the gate while everyone else seemingly raced off. In my desperation I thought of getting a job, but it does not make sense for me to become a programmer only to set the money on fire trying to make RL work. Deepmind and OpenAI sure aren't spending their own money on their experiments. The way I want to win at ML is to establish a base, and then enlarge it by reinvesting the profits. A relationship where I am the only one putting in effort and getting nothing in return would quickly turn sour. So if I became a programmer, I'd be forced down the doomed path of the normie. Making money only to become a NPC is not worth it.

The Singularity is everything to me. It is a war. If you look at the world today, it is split into anti and pro technology factions. These aren't formal factions, but in general you have people who use technology do so begrudgingly, and see it only as fashion. They live the same they would have a thousand years ago, except they have fancy clothes, are fat, and have smartphones. They aren't consumed by technology and look down on those who have.

The pro technology faction agents believe in it. Even if they don't understand its potential, they trust it, more so than they do other people. They've given their souls to the future.

In the next few decades this long war will reach its conclusion and a decisive victor will emerge. I know which side I will be on.

I am frustrated with my own failures and the way the timeline is progressing, but I am not 60 years old, but 35, so in all likelihood I'll be able to afford the time needed to play the game properly and live through to the end of the era of man. The long term is scary when you are human. Tomorrow, I'll be fine, but who knows what will happen to me 20 years down the road. Long term, I'll only be able to feel safe with the power of the machines at my disposal.

I need resources to develop my ML skills further.

Becoming an artist in this situation seems absurd, but take a look at the latest diffusion models and consider what they could be capable of with a few more upgrades. So a hybrid artist/ML class does not seem at all ridiculous to develop in the current day. On the 3d side, we will get neural based renderers and content producing analogues of DALLE. It does not seem absurd that in the future NNs will be capable of making animations. It should be obvious that to reach rank 6 in art, one has to retire his own pen and rely on machines as much as possible.

I want a path that sustains me on its own. I'd rather make 1k as an artist than 10k as a programmer so I will do whatever I can to make this work in the most direct way possible. Art will give me an opportunity to slowly increase my following and hence income, while making use of ML. Programming itself will be the last field of all to succumb to ML, so ironically it will not give me opportunities to make use of it. Rather I expect to be able to make use of those skills along the way in art.

When it is time to start Heaven's Key, I'll announce it on Twitter. I'll probably post the story on Royal Road or ScribbleHub instead of here in order to garner readers.

I'll aim to begin by the end of the year. Right now what I want to internalize is proper self reliance in my 3d modeling by doing more scenes and chara modeling. When I have a finely polished technique in this area, I will move to music studies. No doubt music itself will take me at least 3 months to grasp. I am really looking forward to finding out what kind of NN work has been done there.

One thing I also look forward to is a bear market in BTC. The big run-up, the blow off top, the months-long consolidation and failed rally, followed by the break in the last two months greatly resemble what happened in late 2000 to tech stocks. It was a fun party for those in BTC, but after it gets crushed the GPU prices will be able to feel some relief, meaning in the future I'll actually be able to afford a decent upgrade. If you are in it now, it is not worth praying for a recovery like in late 2018 when it got crushed to below 4k. An asset like BTC you only get into when it breaks out to new highs and don't hold it for long. There will be a bull market in something else, so it is better to find and hold that. The only thing waiting for the BTC crowd is years of bear market action from here on out, that is one party you'd want to miss.

---

Here are some extra links that I've found since I've written the above.

https://semianalysis.substack.com/p/tenstorrent-blackhole-grendel-and

Semi Analysis has some interesting stuff in the AI chip space. I've been hyped for AI chips for a long time, but the efforts of these companies are really lame. You'd expect AI chips to beat the pants off GPUs, but both Graphcore and TensTorrent are struggling to exceed the performance of years old Nvidia GPUs. I expected there to be a ton of companies who would be interested in the Spiral language, but out of 50 startups I've looked at only TensTorrent, Groq and Graphcore are in my eyesight, and maybe they are doing me a favor by ignoring me.

https://semianalysis.substack.com/p/why-america-will-lose-semiconductors
https://semianalysis.substack.com/p/nvidia-hacked-a-national-security

China getting their hands on American technology and speeding up their hardware development can only be good for consumers like me. Based Lapsus$ helping to break Nvidia's monopoly. I've been ignorant of just how much China is developing their own semiconductor industry until I read the first article. At some point this has to have an impact on AI.

https://www.lesswrong.com/posts/xwBuoE9p8GE7RAuhd/brain-efficiency-much-more-than-you-wanted-to-know

I liked this article. It is a good reminder that we are in the mid-2022, and GPUs and CPUs do not have much room to develop anymore, which will pave the way to different kinds of chips. A cluster of GPUs might have power to emulate the brain even today, but as singular devices the main thing they lack are the huge memory stores that the brain has which might be on the order of 1,0000 terabytes. It is hard to be a Singularity fan at this point in time. Forget AGI escaping from the labs, I'd rather memristors do that instead.

///

Let me go with this.

12:15pm. Let me finally post it.

Oh yeah, let me check the journal for how to switch Wordpress to markdown.

///

3pm. Ah, the markdown block is just what I needed! Was it this easy all along? It was such a hassle to keep switching the editor to classic mode just to get this functionality.

It is possible to open it by typing /markdown.

Ok, let me post it.

///

Ok. I found this excerpt in the journal.

12:35pm. Done. I've posted it. As usual the exact place this is posted will be a secret.

It is time for breakfast.

https://semianalysis.substack.com/p/as-moores-law-slows-apple-is-forced
https://semianalysis.substack.com/p/nvidia-ada-lovelace-leaked-specifications
https://semianalysis.substack.com/p/amd-to-infinity-and-beyond

Right now I am reading the articles here. After I am done I will open up Blender and resume modeling. Yesterday I stopped at watching the Scatter 5 tutorial. It will be time to get that done.

https://semianalysis.substack.com/archive?sort=search&search=groq

They don't have anything on Groq.

https://semianalysis.substack.com/p/moores-law-is-dead-for-dram-and-that
https://semianalysis.substack.com/p/samsung-electronics-cultural-issues
https://semianalysis.substack.com/p/tesla-dojo-unique-packaging-and-chip

I haven't read anything about Tesla's chip up to now. Let me get breakfast while I read.

https://semianalysis.substack.com/p/samsung-electronics-cultural-issues
> Density gains have been so tepid, that the DRAM manufactures have turned to using letters as the suffix rather than numbers like they did in the pre-20nm generation.

https://semianalysis.substack.com/p/moores-law-is-dead-for-dram-and-that
> Moore’s law has been the driver of semiconductor capabilities and cost for decades. This phenomenon is still being pushed by the likes of TSMC, Intel, and Samsung in logic, but in DRAM, it is dead. DRAM scaling slowed significantly nearly a decade ago and it is moving at a snail’s pace now.

This is a problem as huge memory stores are necessary for AGI.

1:50pm. Let me resume. Legendary Mechanic has been taking a lot out of me. It is not high art like Reverend Insanity. I wish the MC didn't have the ability to mine players for infinite XP. It feels so cheap. Also unlike gu cultivation, he is just using a RPG system and leveling up. The only time that was good was with Kumo.

But it is fun regardless.

Doing art is really difficult for me. Unlike programming which I can scheme and then fire away and be done, art is really labor intensive. So far, my plans to automate things that I wanted to have failed. If I only had to do writing I'd have a lot easier time. Who knows if I will make it, but I'll try my best. Either way, let me cultivate it for a few more months and then I'll do music. If I really feel like I can't do it after the next six months, I'll get a programming job and just do some writing on the side during my free time.

...Yeah, that is the problem. These kinds of thoughts might be an indication of my approaching failure. A person who really wanted to win would not have outs. It will cause me to struggle against my laziness.

And struggle I shall. Let me finally do some art. First I need to master scatter. It actually uses geo nodes to do scattering, and the tree is humongous.

https://youtu.be/HYkMd6FX8jM
Architectural Visualization in Blender - Part1/2

It is time for this. I should just focus on mastering Scatter.

https://youtu.be/HYkMd6FX8jM?t=397

Does he ever get around to actually making part 2?

https://youtu.be/HYkMd6FX8jM?t=559

Hmmmm...this might be how he added it to the asset browser. Do I have this blend file?

https://youtu.be/HYkMd6FX8jM?t=558

I am confused. Does it automatically unpack the scatter library there.

C:\Users\Marko\AppData\Roaming\Blender Foundation\Blender\data\scatter library\_biomes_

Yeah, for me it does it here. Actually instead of just biomes, let me go up a folder.

Yeah, I think biomes are everything here. Ok.

2:30pm. This is nice. Now I have access to some greenery assets. This will be useful. It is making me wonder - maybe it would be a good idea to try putting in Manhattan as an asset. It might be an easier way of putting things together. I'll consider it after I set up the shot. For now let me get back to the tutorial.

https://youtu.be/HYkMd6FX8jM?t=656

I don't know, for some reason Scatter preset is giving me a Python exception when I try to use it. I might want to downgrade to 3.1. I'll see how it goes.

For now, let me watch the tutorial for a bit longer and then I'll try it.

https://youtu.be/HYkMd6FX8jM?t=687

Yeah, let me try it.

2:50pm. No, it is not working for me for some reason either in 3.1 or 3.2.

3pm. Ohhh, I got it!

It ended up working in 3.2 rather than 3.1. What I did was erase all the systems in the System List and only then used the scatter preset. It works. It seems those systems I got rid of in the outliner manually were causing issues.

3pm. I suppose an issue I have now is that it does not work for 3.1, but who cares.

3:05pm. This was a gain. Let me return to the tutorial.

3:15pm. https://youtu.be/HYkMd6FX8jM?t=803

Let me take a short break here. I am following along well enough. Let me resume.

https://youtu.be/HYkMd6FX8jM?t=807

Push along?

Interesting. Even though Blender is less capable at large poly geomtry than Clarisse, Scatter 5's capabilities exceed it a lot in terms of ergonomics.

3:35pm. https://youtu.be/HYkMd6FX8jM?t=977

Hrmmm. For some reason pressing alt to enable the camera optimization for all the systems does not work. Why?

I am not sure. I guess I'll have to leave that asside for the time being.

https://youtu.be/HYkMd6FX8jM?t=1030

Ah, they need to all be selected.

https://youtu.be/HYkMd6FX8jM?t=1043

This is nice, it would be a lot harder to do in Clarisse.

https://youtu.be/HYkMd6FX8jM?t=1149

Closed Bezier area.

https://youtu.be/HYkMd6FX8jM?t=1159

It this a special mode? I wonder how he is doing the fence.

https://youtu.be/HYkMd6FX8jM?t=1167
> Scatter5 manual mode was born out of a simple idea: we wanted to create an alternative distribution workflow for artists who do not necessarily need a fully procedural solution, but would rather want a more direct "physical" approach.
> The main goal of this mode is emulating a painting workflow, graphic tablet support was a matter of course.

https://youtu.be/HYkMd6FX8jM?t=1169

This stuff here could be useful for setting houses manually.

https://youtu.be/HYkMd6FX8jM?t=1175

The really went all out with this. Blender addons really make it hard to move to Clarisse. For all I know, maybe I'll even manage to make Manhattan work through the asset browser. I'd have to take to turn all the parented models into properly offsetted collections, but after that I'd be gold.

4:10pm. Previously I had assumed that multiple systems had to be selected for alt to work, but I was wrong. I can't get it to work for some reason. I don't know why.

4:20pm. Had to take a short break. Let me see if I can figure out how to make batch operations with Alt work. Why aren't they working already?

https://blenderartists.org/t/scatter-5-2-brand-new-release/1177672/3088?u=marko_grdinic

///

I've have two problems:

1) The Alt key for batch changes does not work for me. I've made sure to select multiple systems, but holding Alt and pressing Display As for example only modifies the actively selected system. I don't know what to do about this. Any ideas?

2) Selecting collections as opposed to objects in the asset browser does not work. Are collections not supported? I can get around this by copying them to viewport and selecting them from there.

///

Nevermind this. I've asked the author so I should get a reply in this thread.

Let me see if I can figure out how to visualize vertex colors. It works easily enough, but it does not seem I can edit it. Nevermind that. How did he edit the mask?

https://youtu.be/HYkMd6FX8jM?t=998

He turned on the vertex group. Let me try that.

4:50pm. It works quite nicely. Ok.

4:50pm. I am done with playing around with Scatter. I'll wait for the replies from the author in order to figure ou the two issues.

Now I'll get started on doing my own thing. Let me just reload the musquito repelant. Every summer it's the same thing.

The apex predators that are humans are food for tiny insects.

5pm. Now focus me.

5:05pm. No really, let me just do it. I'll pick a simple structure and just implement it. Big buildings in the middle, and progressively smaller ones as the center recedes.

...Oh, scattering from collections worked now. It might have had something with me messing in the outliner.

5:35pm. RIght now I am just playing with it. As fun as this is, what I should be focusing is the manual mode. It seems to have been made for me. Let me take a look at the stuff in the manual.

5:40pm. https://sites.google.com/view/scatter5docs/example-files
> When distributing your assets, you might want to dynamically assign the objects based on their physical scale value. This is where the instancing by scale method comes in handy, it's an essential tool to have if you're after a realistic scatter. In this demo, paint the group driving the shrink feature and the instances will dynamically change. The terrain shader is derived from this scale mask.

5:50pm.

///

Asteroid Belt
In this scene we are creating an animated asteroid belt using Scatter5 new volume distribution method. The asteroids are animated using the noise offset feature. We could also animate the rotation with keyframes. The CCBY asteroid models are made by Spacehead and hdri by PixeledAsteroid.

///

It has volume distribution.

https://sites.google.com/view/scatter5docs/manual/manual-mode

Anyway, for now, this is what I need.

Let me open a fresh instance of Blender and I will try the Alt thing again.

It seems it works now.

6:10pm. Found a bug in the relax brush. It seems when objects have been erased, it runs into an array out of bounds error.

...No, nevermind, it is just broken.

6:35pm. I have no idea what rotate settings and scale settings are supposed to be doing. I tried rotating and scaling and used these brushes hoping it would reset the instances, but nothing happened. Let me ask in the thread.

https://sites.google.com/view/scatter5docs/manual/extra

///

Export to Objects
If you'd like to export your instances to other softwares, you will first need to convert your selected scatter-system to blender instances object, to do so, use the "Selected to Instances" operator.

Pro Tip: If you need to link a scatter system in your pipeline, do not use the scatter_obj  in your outliner,  the best practice is to non-destructively use this export operator, and link the resulting collection! ( Linking/Appending an empty geometry node object is not currently supported in blender 3.0.)

Export to Json
It is possible to encode all scattered points location, rotation, scale to a .json format with the export to Json operator.

///

So I could do my thing here, and export it as alembic and into Clarisse should I want to.

7:30pm. Let me have lunch here.

7:35pm. I think I'll close for the day here. I've been in the zone just playing with Scatter 5 itself. Minus the bugs, I am happy with manual mode. It is what I should be using to make a city. Their functionality is so good. I never even thought that the addon would have something like this.

8:05pm. Done with lunch. Let me close. Tomorrow I'll actually put those buildings down."

---
## [lakshmipathyarjun6/geometry-central](https://github.com/lakshmipathyarjun6/geometry-central)@[3b2abde959...](https://github.com/lakshmipathyarjun6/geometry-central/commit/3b2abde959079aa93fa4da8d73416a88a4ea5dfa)
#### Wednesday 2022-06-22 18:28:36 by Arjun S. Lakshmipathy

Merge pull request #31 from lakshmipathyarjun6/ss

Stupid ass visual studio forced renaming shit

---
## [Ojjie/knowledge](https://github.com/Ojjie/knowledge)@[1a8afcccc6...](https://github.com/Ojjie/knowledge/commit/1a8afcccc6124b9505282abfb9b0f2c28cf7946d)
#### Wednesday 2022-06-22 20:24:50 by Nikita Voloboev

SUMMARY animals books startups ngrok cloud-computing gcp aws-lambda cloudflare-workers serverless-computing build-systems computer-graphics computer-vision image-processing compression formal-verification kafka arweave blockchain cardano ethereum near solana databases postgresql redis design-inspiration design figma-plugins logos user-experience devops temporal terraform distributed-systems drugs investing learning environment rules front-end minecraft arduino recipes knowledge-graphs latex happiness life success xcode macOS datasets ml-libraries pytorch machine-learning ml-models reinforcement-learning calculus fractals satisfiability-modulo-theories math statistics acting music-production decentralization graphql http iot microservices networking nginx tcp tls nlp containers docker kubernetes emulators ios linux operating-systems wiki-workflow nix quantum-computing privacy c-libraries clojure-libraries clojure qt crystal flutter elixir-libraries elm fsharp go-libraries go idris java-libraries js-libraries nextjs react-components vue julia-libraries kotlin-libraries lisp ocaml-libraries ocaml php programming-languages django python-libraries python ruby rust-libraries rust scala swift-libraries typescript-libraries typescript zig constraint-programming embedded-systems jupyter-notebooks git psychology solving-problems robots cryptography security social-networks emacs elasticsearch tools netherlands russia cinematography video virtual-reality browsers deno nestjs nodejs web-accessibility web consultancies interviews remote-work

---
## [jbardin/go-cty](https://github.com/jbardin/go-cty)@[97bafac0de...](https://github.com/jbardin/go-cty/commit/97bafac0dea33a3f74db88ab54dea2937b9e8aef)
#### Wednesday 2022-06-22 22:06:30 by Martin Atkins

Remove all of the encoding/gob support code

I originally introduced all of this here as a concession to trying to
HashiCorp trying to get cty values to round-trip through the various
very magical gob-based wire interfaces in Terraform v0.11 and earlier,
back when they thought cty and what became "HCL 2" would just be a drop-in
replacement for HCL 1 and the various different competing representations
of dynamic values.

However, in practice none of that ever actually worked out and instead
Terraform now natively uses cty JSON/msgpack and other such mechanisms for
its wire protocols, making this gob handling code redundant.

This stuff caused various maintenance headaches and panic bugs which make
them a burden to retain. Although this is technically a breaking change
to the public cty API, in practice this stuff was only here to allow
Terraform to use it _indirectly_ as a side-effect of passing values into
the encoding/gob package, and so I'm treating it as if it had been an
internal implementation detail even though in principle it could've been
depended on externally. If anyone was doing that, I'm sorry; I suggest
copying the relevant support code into your own package instead if you
wish to continue using cty with gob.

---
## [isabelgk/surge](https://github.com/isabelgk/surge)@[e6f4ffaef9...](https://github.com/isabelgk/surge/commit/e6f4ffaef9d6f3222749fcf0d86a37063130a36e)
#### Wednesday 2022-06-22 22:58:24 by Paul

Doubleclick Renamed Modulators without annoying bug (#6024)

Doubleclick renames a modulator. Cool

But this kinda sucks if you click into a modulator and then click to arm
quickly and misfire a double click

So if you have *just* selected a modulator the double click doesn't work.

Only after that

Closes #5774

---

