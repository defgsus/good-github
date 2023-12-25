## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-24](docs/good-messages/2023/2023-12-24.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,175,024 were push events containing 2,731,839 commit messages that amount to 132,470,484 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 56 messages:


## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[2201bf6bfa...](https://github.com/TaleStation/TaleStation/commit/2201bf6bfa814e509d2810b645ac267f7eac4426)
#### Sunday 2023-12-24 00:43:24 by TaleStationBot

[MIRROR] [MDB IGNORE] Deviant Crew antag panel category, Obsessed crew now shown in orbit menu, Paradox Clone orbit tab is now white (#9157)

Original PR: https://github.com/tgstation/tgstation/pull/80450
-----

## About The Pull Request

This rounds up the "Other" (Brainwashed, Hypnotised, Wizard Revenge, and
Obsession) antagonist category into the new "Deviant Crew" category.
This tab is white!

Obsessed crew are now displayed in the orbit panel (no other antagonists
in this group are though).

The Spacetime Aberrations (Paradox Clone) group has also been changed to
be white.

Here's how that looks:


![image](https://github.com/tgstation/tgstation/assets/28870487/415b8cbb-7ac3-4e24-9f74-466480c2aab0)
## Why It's Good For The Game

As was the case with paradox clones, observers can already discern when
a player is obsessed. It shouldn't be a pain to observe these guys,
especially when they're a more RP oriented antag that are (usually)
deserving of the audience.

I made paradox clones and obsessed the same color because they're both
in the broader spectrum of "fucked up crew".

Also converts common text entries to a single define. That is good
coding practice I think.
## Changelog
:cl: Rhials
qol: Obsessed crewmembers are now displayed in the orbit panel.
qol: The Paradox Clone orbit menu tab is now white. Neat!
/:cl:

---------

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>

---
## [kittysmooch/Skyrat-tg](https://github.com/kittysmooch/Skyrat-tg)@[2805c86c81...](https://github.com/kittysmooch/Skyrat-tg/commit/2805c86c811fde2450a054a25c7a665b77df47e5)
#### Sunday 2023-12-24 00:59:26 by Nerevar

[THE HALF-MODULAR PRINCE] Snalance (Snail Balance) and Snissues (Snail Issues) Adjustment (#25439)

* initial d

* holy shit i forgot

* i got so much cheese in my pocket, they thought I was a fucking calzone

* opp was sneak-dissing on the 'gram, turned his city into pompeii

* Just fixing some diffs (line breaks should match tg)

* Fixes these edit comments

---------

Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [oooAHOYooo/oooAHOYooo.github.io](https://github.com/oooAHOYooo/oooAHOYooo.github.io)@[f5016a70a1...](https://github.com/oooAHOYooo/oooAHOYooo.github.io/commit/f5016a70a121bd9c904e14bb4ae31841b0045de0)
#### Sunday 2023-12-24 01:01:24 by agBabbbyCakes (ApeWorX, LTD)

got wild - goodnight - going to go paint - God bless and Merry Christmas to all

---
## [sxjeru/Hbm-s-Nuclear-Tech-CI](https://github.com/sxjeru/Hbm-s-Nuclear-Tech-CI)@[be2c17f102...](https://github.com/sxjeru/Hbm-s-Nuclear-Tech-CI/commit/be2c17f1028c6129e97620c7d9ecad79b7b06579)
#### Sunday 2023-12-24 01:01:24 by Bob

can't wait for the silly people on discord bug me 24/7 about this fuckin

g commit i swear to god this is why we can't have nice things

---
## [AshtonFox/Skyrat-tg](https://github.com/AshtonFox/Skyrat-tg)@[48b5a35dea...](https://github.com/AshtonFox/Skyrat-tg/commit/48b5a35deadc1cdeb19d117ee50702c76df0d275)
#### Sunday 2023-12-24 01:03:41 by Bloop

[MISSED MIRRORS] Linters, part two (#25138)

* Split Run Linters step into multiple steps (#78265)

Splits the big "Run Linters" step into multiple steps. Also since all of
these steps are independent of eachother, I've made them all run
regardless of if the job is currently failing.

<details>
<summary>Proof of testing:</summary>

Fail in install tools, all linting steps are skipped:
https://github.com/distributivgesetz/tgstation/actions/runs/6151628214/job/16692089726
Fail in Run DreamChecker, other steps continue to run:
https://github.com/distributivgesetz/tgstation/actions/runs/6151664705/job/16692203569?pr=2
</details>

<details>
<summary>Pictured: me breaking CI for a day</summary>

https://github.com/tgstation/tgstation/assets/47710522/ea12ad30-2b69-4aa3-9642-7d0818eab2d1

</details>

Going through the Run Linters step has always been a slog. Finding an
error is like finding a needle in a haystack. Seeing what command
exactly went wrong is going to go a long way in helping people find out
which linters have failed.

nothing playerfacing

* Fixes TFE being useless after #78265 (#78433)

I thought `set +e` would still make the shell exit with an error if any
command failed, I didn't think that it would just use the exit code of
the last command. I am dumb, I'm an idiot and I want to cry.

* Update ci_suite.yml

* Fix some odd vscode highlighting errors in workflow files  (#78274)

few errors which were odd and annoying

stealing PRs from san7890, they wanted to do this
nothing playerfacing

* Only cancel concurrent CI in the same PR (#73398)

More merge queue bullshit. Cancels are counted as failures, and even
though on my test branch it worked completely fine, when trying on two
real PRs, it did not.

This makes it so merges into master might mess with CI clogging again,
but also merge queue is going to do that on its own, and the gain is
worth it.


![image](https://user-images.githubusercontent.com/35135081/218340666-6f937611-c47e-4122-b4b8-b84e8edcc1e9.png)

* Remove cache purge key that has never worked and has meant that our cache has never worked (#71529)

ci_suite.yml runs on your fork. This means you do not have access to
secrets. Every user has had the purge key of blank.

WE have it set to something. Which means the master cache that every PR
pulls from has been unable to match.

This means our cache has been at the max limit all this time, constantly
clearing out old caches, and never reusing any.

* Caches Node and Python Bootstrap for GH Actions (#78307)

## About The Pull Request

I was planning on doing this a lot earlier but ran into some weird
roadblocks, but this time I finally did the research and it's done
properly.

We do a lot of useless work on every single CI run, and in the interest
of saving the world's energy (by a matter of at least 10 seconds per my
testing), lets stop doing so much extra work by caching both the work we
do on the python bootstrap installation (we literally call it `cache`
for a reason) and the Node installation by sharing it between github
actions runners.

Here's a random CI run on master where you can see that the `Install
Tools` portion takes about 19 seconds -
https://github.com/tgstation/tgstation/actions/runs/6167104927/job/16737570519

Here's the CI run I was testing with where you can see we slim it down
to about 6 seconds for the `Install Tools` step, but with a second-or-so
taken to restore the cache since the runner needs to download+unzip the
cache. it tends to be shorter or longer by a second at times but i'm
certain this is just noise -
https://github.com/san7890/bruhstation/actions/runs/6167245722/job/16737919874

On average, we save about **10 seconds** a run on Run Linters, which is
meant to be the fastest CI step. Future improvements would lie in making
either maplint or the tgui test suite faster, but that would be a much
more complicated and code-intensive task. cache go weeeee

## Changelog

Nothing that concerns players.

* Conditionally run TGS tests (#73704)

Also add test merge support for pull requests

---------

Co-authored-by: distributivgesetz <distributivgesetz93@gmail.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jordan Dominion <Cyberboss@users.noreply.github.com>

---
## [AshtonFox/Skyrat-tg](https://github.com/AshtonFox/Skyrat-tg)@[17cba0dccf...](https://github.com/AshtonFox/Skyrat-tg/commit/17cba0dccfb57eb492fcfade92abc0065a07b356)
#### Sunday 2023-12-24 01:03:41 by Bloop

[MISSED MIRROR] Puts all traits in the globalvars file + CI Testing (#79642) (#25131)

* Puts all traits in the globalvars file + CI Testing (#79642)

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-

![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).

* Update tgstation.dme

* Update _traits.dm

* Comment these out for now

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [AshtonFox/Skyrat-tg](https://github.com/AshtonFox/Skyrat-tg)@[67ddf1507c...](https://github.com/AshtonFox/Skyrat-tg/commit/67ddf1507c8663c4b8f006ed8c763ca372e5fc29)
#### Sunday 2023-12-24 01:03:41 by SkyratBot

[MIRROR] Make sign language unaffected by the Social Anxiety quirk's direct speech effects [MDB IGNORE] (#25140)

* Make sign language unaffected by the Social Anxiety quirk's direct speech effects (#79809)

## About The Pull Request

Alternative title: "Make going non-verbal make you less anxious."

This is a two line change to `social_anxiety.dm` to quit out its
`handle_speech` method when user has the `TRAIT_SIGN_LANG` trait.
This stops the Social Anxiety quirk from applying its
stutters/fillers/blockers for as long as the speaker is using sign
language.
This does nothing to any of social anxiety's non-verbal effects, those
are still active regardless and entirely unaffected.
## Why It's Good For The Game

Primarily: I think giving people the choice between using anxious talk
or sign language, and thus the different hurdles inherent to both, makes
for a more interesting gameplay interaction than simply blanket-applying
the quirk's speech effects to both.

Secondarily: Social Anxiety's non-verbal penalties are entirely
unaffected. One will still get the penalties from making eye contact and
occasionally make eye contact with objects. Notably this includes the
stuttering making eye contact could get you, which still makes your
signing shaky. You're still anxious, after all.
On top of this, it still costs more to pick up Signer than Social
Anxiety allows for, and thus the change doesn't simply make the
combination free points.

Tertiarily: when one has trouble speaking verbally, non-verbal
communication can be helpful in overcoming that hurdle. This is
especially so when the trigger for said anxiety is speaking verbally in
the first place. This is part of why I was so enamoured by the
combination before a broader and, mind you, fairly needed fix to sign
language made these interact differently.
## Changelog
:cl:
balance: signers no longer suffer from social anxiety's speech changes
when they go non-verbal. Other effects are maintained.
/:cl:

* Make sign language unaffected by the Social Anxiety quirk's direct speech effects

---------

Co-authored-by: _0Steven <42909981+00-Steven@users.noreply.github.com>

---
## [AshtonFox/Skyrat-tg](https://github.com/AshtonFox/Skyrat-tg)@[fcbbb6e0e0...](https://github.com/AshtonFox/Skyrat-tg/commit/fcbbb6e0e0f9c0132fbc962bb03464bdcd1b20c4)
#### Sunday 2023-12-24 01:03:41 by SkyratBot

[MIRROR] Fixes body collision causing a stun, despite a successful block. [MDB IGNORE] (#25146)

* Fixes body collision causing a stun, despite a successful block. (#79824)

## About The Pull Request

Puts a block check into the ``throw_impact()`` of carbon mobs.

## Why It's Good For The Game

I'm touching on a lot of 'get around shields' stuns, and this has been a
big one for the better part of a few years and potentially not even
intentional. I would say it gained its largest popularity when it became
weaponized with fireman carrying.

Despite seemingly rolling to block, blocking a body hitting you doesn't
actually do anything at all. This reminds me a bit of energy bolas. So I
fixed it? I think, there might be a better fix, I'm just replicating
code present in xenomorph tackles. This shit sucks, please recommend a
better fix if you know it.

## Changelog
:cl:
fix: When you successfully block a body collision, it does something
rather than nothing at all.
/:cl:

* Fixes body collision causing a stun, despite a successful block.

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [tesselslate/advent](https://github.com/tesselslate/advent)@[cd10cb75cd...](https://github.com/tesselslate/advent/commit/cd10cb75cdfb9f62e62f926df8a1a6ce24c0f9ed)
#### Sunday 2023-12-24 01:36:27 by tesselslate

2020: day 22

~6m/~20m | main issue on part 1 was getting the order in which cards got
put back on the deck wrong. main issue on part 2 was parsing this god
awful description of the problem. like just spell the requirements out
clearly god damn this is why i skipped day 21 i literally couldnt
understand what it was asking

although i did lose like 4 minutes to my own fault because i did > for
the length check instead of >=

---
## [Gabevicarv/neurottic](https://github.com/Gabevicarv/neurottic)@[f412c63d28...](https://github.com/Gabevicarv/neurottic/commit/f412c63d281ec5847ef8b120d335b17579589a33)
#### Sunday 2023-12-24 01:59:16 by Gabevicarv

A webpage for my girlfriend, she is a begginer 3D designer on second life.

---
## [RikuTheKiller/tgstation](https://github.com/RikuTheKiller/tgstation)@[33e10634ba...](https://github.com/RikuTheKiller/tgstation/commit/33e10634ba89c28c1ca3518068e916ec0a10b33e)
#### Sunday 2023-12-24 02:46:20 by Iamgoofball

Fixes Holy Water performing water metabolization twice, giving more blood and making you less drunk (#80440)

## About The Pull Request

~~Fixes Holy Water taking double the time it's supposed to take to
deconvert, and fixes it metabolizing out at twice the normal speed.~~

Fixes Holy Water performing water metabolization twice, giving more
blood and making you less drunk

## Why It's Good For The Game

lmfao ~~this is why deconversion for cult sucked~~ so bad

## Changelog

:cl:
fix: Fixes Holy Water giving you more blood and making you less drunk
than water normally does.
/:cl:

---
## [lifehackerhansol/Kurisu](https://github.com/lifehackerhansol/Kurisu)@[9e35541d41...](https://github.com/lifehackerhansol/Kurisu/commit/9e35541d41ded2e07a938ef8acfc9b70916c1090)
#### Sunday 2023-12-24 02:51:40 by eip

github said i added this but i didnt mean to so i removed it

and then it turned out it needed it anyway
fuck you github

---
## [crawl/crawl](https://github.com/crawl/crawl)@[7102d64fe6...](https://github.com/crawl/crawl/commit/7102d64fe61c79f22477f8d731bca40e15f233c7)
#### Sunday 2023-12-24 03:07:33 by regret-index

Make Boris make you sad

Boris is a very sad unique. He's lost his dagger (acddeb6). He's been
seperated from his cat (8eed16d) for ages. He's become nearly identical to
plain liches aside from trading Haste for Iron Shot (6612197). He's lost a
decently large chunk of his placement range, diluting his gimmick (f5560fb,
1b62a5d, 67d208b). He also just doesn't actually kill many people- while
it's obviously awkward to assess the killrate statistics of somebody that
comes back, his killrate over the past three versions is a very sad ~0.45%.

It could bring one to tears, really. He's got an almost tangibly
miserable lot, one could say.

Boris now loses Invisibility for an upgraded version of the weeping skull
misery cloud spell (c.f. d47e5fa) - a cloud line that lasts 8-12 turns that
doesn't skip over the vulnerable, and which forms a mephitic-cloud style
1-radius burst of 2-5 turn clouds. (Most of the Invisibility weight wasn't
entirely put into this new March of Sorrows, and was distributed into other
conjurations.) This should be an interestingly nasty combination with his
Orb of Destruction, as it will eat away at players trying to sidestep the
orbs. It also cutely makes every single one of his spells conjurations,
which I'm sure he'd prefer, and gives him a spell distinct from both liches
and other uniques. Wear rN+.

Boris also now places in Depths:1-2, Vaults:1, and Elf:$, so his
resurrection mechanic has more chances to actually be seen. This might make
him a bit absurd on the orb run, but he's only gotten 5 kills then in the
last nearly three years since 3208aba, so it should be fine.

(Also, some more Boris lines and text. Hooray for melodramatics.)

---
## [Frostleaft07/android_kernel_realme_mt6765](https://github.com/Frostleaft07/android_kernel_realme_mt6765)@[8bddce881a...](https://github.com/Frostleaft07/android_kernel_realme_mt6765/commit/8bddce881ac1ab6dd3da2e1504601eeb2e84b170)
#### Sunday 2023-12-24 03:27:23 by Douglas Anderson

serial: core: Allow processing sysrq at port unlock time

[ Upstream commit d6e1935819db0c91ce4a5af82466f3ab50d17346 ]

Right now serial drivers process sysrq keys deep in their character
receiving code.  This means that they've already grabbed their
port->lock spinlock.  This can end up getting in the way if we've go
to do serial stuff (especially kgdb) in response to the sysrq.

Serial drivers have various hacks in them to handle this.  Looking at
'8250_port.c' you can see that the console_write() skips locking if
we're in the sysrq handler.  Looking at 'msm_serial.c' you can see
that the port lock is dropped around uart_handle_sysrq_char().

It turns out that these hacks aren't exactly perfect.  If you have
lockdep turned on and use something like the 8250_port hack you'll get
a splat that looks like:

  WARNING: possible circular locking dependency detected
  [...] is trying to acquire lock:
  ... (console_owner){-.-.}, at: console_unlock+0x2e0/0x5e4

  but task is already holding lock:
  ... (&port_lock_key){-.-.}, at: serial8250_handle_irq+0x30/0xe4

  which lock already depends on the new lock.

  the existing dependency chain (in reverse order) is:

  -> #1 (&port_lock_key){-.-.}:
         _raw_spin_lock_irqsave+0x58/0x70
         serial8250_console_write+0xa8/0x250
         univ8250_console_write+0x40/0x4c
         console_unlock+0x528/0x5e4
         register_console+0x2c4/0x3b0
         uart_add_one_port+0x350/0x478
         serial8250_register_8250_port+0x350/0x3a8
         dw8250_probe+0x67c/0x754
         platform_drv_probe+0x58/0xa4
         really_probe+0x150/0x294
         driver_probe_device+0xac/0xe8
         __driver_attach+0x98/0xd0
         bus_for_each_dev+0x84/0xc8
         driver_attach+0x2c/0x34
         bus_add_driver+0xf0/0x1ec
         driver_register+0xb4/0x100
         __platform_driver_register+0x60/0x6c
         dw8250_platform_driver_init+0x20/0x28
	 ...

  -> #0 (console_owner){-.-.}:
         lock_acquire+0x1e8/0x214
         console_unlock+0x35c/0x5e4
         vprintk_emit+0x230/0x274
         vprintk_default+0x7c/0x84
         vprintk_func+0x190/0x1bc
         printk+0x80/0xa0
         __handle_sysrq+0x104/0x21c
         handle_sysrq+0x30/0x3c
         serial8250_read_char+0x15c/0x18c
         serial8250_rx_chars+0x34/0x74
         serial8250_handle_irq+0x9c/0xe4
         dw8250_handle_irq+0x98/0xcc
         serial8250_interrupt+0x50/0xe8
         ...

  other info that might help us debug this:

   Possible unsafe locking scenario:

         CPU0                    CPU1
         ----                    ----
    lock(&port_lock_key);
                                 lock(console_owner);
                                 lock(&port_lock_key);
    lock(console_owner);

   *** DEADLOCK ***

The hack used in 'msm_serial.c' doesn't cause the above splats but it
seems a bit ugly to unlock / lock our spinlock deep in our irq
handler.

It seems like we could defer processing the sysrq until the end of the
interrupt handler right after we've unlocked the port.  With this
scheme if a whole batch of sysrq characters comes in one irq then we
won't handle them all, but that seems like it should be a fine
compromise.

Signed-off-by: Douglas Anderson <dianders@chromium.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [standby24x7/langchain](https://github.com/standby24x7/langchain)@[d4f45b1421...](https://github.com/standby24x7/langchain/commit/d4f45b1421ec8b56fe6aeed84f81ca1b3f91383f)
#### Sunday 2023-12-24 05:42:21 by Sypherd

core(minor): Allow explicit types for ChatMessageHistory adds (#14967)

<!-- Thank you for contributing to LangChain!

Replace this entire comment with:
  - **Description:** a description of the change, 
  - **Issue:** the issue # it fixes (if applicable),
  - **Dependencies:** any dependencies required for this change,
- **Tag maintainer:** for a quicker response, tag the relevant
maintainer (see below),
- **Twitter handle:** we announce bigger features on Twitter. If your PR
gets announced, and you'd like a mention, we'll gladly shout you out!

Please make sure your PR is passing linting and testing before
submitting. Run `make format`, `make lint` and `make test` to check this
locally.

See contribution guidelines for more information on how to write/run
tests, lint, etc:
https://python.langchain.com/docs/contributing/

If you're adding a new integration, please include:
1. a test for the integration, preferably unit tests that do not rely on
network access,
2. an example notebook showing its use. It lives in `docs/extras`
directory.

If no one reviews your PR within a few days, please @-mention one of
@baskaryan, @eyurtsev, @hwchase17.
 -->
## Description
Changes the behavior of `add_user_message` and `add_ai_message` to allow
for messages of those types to be passed in. Currently, if you want to
use the `add_user_message` or `add_ai_message` methods, you have to pass
in a string. For `add_message` on `ChatMessageHistory`, however, you
have to pass a `BaseMessage`. This behavior seems a bit inconsistent.
Personally, I'd love to be able to be explicit that I want to
`add_user_message` and pass in a `HumanMessage` without having to grab
the `content` attribute. This PR allows `add_user_message` to accept
`HumanMessage`s or `str`s and `add_ai_message` to accept `AIMessage`s or
`str`s to add that functionality and ensure backwards compatibility.

## Issue
* None

## Dependencies
* None

## Tag maintainer
@hinthornw
@baskaryan 

## Note
`make test` results in `make: *** No rule to make target 'test'.  Stop.`

---
## [dwrrehman/programming_language](https://github.com/dwrrehman/programming_language)@[93dee0ec73...](https://github.com/dwrrehman/programming_language/commit/93dee0ec73f602a772191979e42540a9a5f48c41)
#### Sunday 2023-12-24 06:39:12 by Daniel Rehman

make registers spelt differently without any r, and in hex instead of decimal. also figured out how to make compiletime function calls work only using the branch machinery that we had. also got passing arguments to those compiletime function calls working too yayyyyy. pretty amazing it all works really well, and theres literally no user defined names in the entire language, which is pretty crazy lol. i am quite happy with it so far. i want to use it alot more now.

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[baf2778142...](https://github.com/morgoth1145/advent-of-code/commit/baf27781420b5920c8cccf3b610791eaa44aa77f)
#### Sunday 2023-12-24 06:57:08 by Patrick Hogg

2023 Day 24 Part 2

This also threw me for a loop, and it really shouldn't have thrown me for as much of a loop!

Fundamentally we have (for each hailstone) these 3 equations:
x + t * xv = p.x + t * v.x
y + t * yv = p.y + t * v.y
z + t * zv = p.z + t * v.z
Where x, y, and z is the initial positions of the stone, t is the time of collision, and xv, yv, and zv is the velocity of the stone.

Initially I tried sending those equations for *all* the hailstones at z3. It could do it for the input but it choked on my real input, sadly. I left that running in the background and tried some other things.
1) I misread the example and thought that it implied that at t=1 and t=2 there will always be a collision, so I tried iterating through pairs of hailstones to extrapolate the stone's position and velocity, but this never worked for the example. (The first two intersections are t=1 and t=3!)
2) I tried to solve the systems of equations for 3 hailstones and the stone by hand. This gets super messy...
3) I started to code up a 3-deep nested loop to have z3 try to solve the system of equations for 3 hailstones for me.

However, while working on #3 I realized that we're guaranteed that *any* three hailstones are hit and are solvable. As such, the nested loop is dumb! Given this, I tried setting up z3 to just solve the system of equations for the first 3 hailstones, but it choked on that too. Thankfully I remembered about sympy and after verifying its API, I gave it a shot. It pretty much immediately gave me the answer, finally!

I clearly don't do this sort of work enough, this was way more painful than it should have been.

Rank 502. Oof, wish I'd have thought of sympy sooner...

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[62bec47f2e...](https://github.com/morgoth1145/advent-of-code/commit/62bec47f2e8213735eea1413293feed1bf400624)
#### Sunday 2023-12-24 07:04:09 by Patrick Hogg

2023 Day 24 Part 2

This also threw me for a loop, and it really shouldn't have thrown me for as much of a loop!

Fundamentally we have (for each hailstone) these 3 equations:
x + t * xv = p.x + t * v.x
y + t * yv = p.y + t * v.y
z + t * zv = p.z + t * v.z
Where x, y, and z is the initial positions of the stone, t is the time of collision, and xv, yv, and zv is the velocity of the stone.

Initially I tried sending those equations for *all* the hailstones at z3. It could do it for the example but it choked on my real input, sadly. I left that running in the background and tried some other things.
1) I misread the example and thought that it implied that at t=1 and t=2 there will always be a collision, so I tried iterating through pairs of hailstones to extrapolate the stone's position and velocity, but this never worked for the example. (The first two intersections are t=1 and t=3!)
2) I tried to solve the systems of equations for 3 hailstones and the stone by hand. This gets super messy...
3) I started to code up a 3-deep nested loop to have z3 try to solve the system of equations for 3 hailstones for me.

However, while working on #3 I realized that we're guaranteed that *any* three hailstones are hit and are solvable. As such, the nested loop is dumb! Given this, I tried setting up z3 to just solve the system of equations for the first 3 hailstones, but it choked on that too. Thankfully I remembered about sympy and after verifying its API, I gave it a shot. It pretty much immediately gave me the answer, finally!

I clearly don't do this sort of work enough, this was way more painful than it should have been.

Rank 502. Oof, wish I'd have thought of sympy sooner...

---
## [SizableShrimp/AdventOfCode2023](https://github.com/SizableShrimp/AdventOfCode2023)@[f19b3973c0...](https://github.com/SizableShrimp/AdventOfCode2023/commit/f19b3973c0089cc78a0ce5ad7cb7213be0782001)
#### Sunday 2023-12-24 07:19:53 by SizableShrimp

Implement Day 24 in Kotlin

I didn't place today, but I was tantalizingly close. #823 on Part 1, and #124 on Part 2. Today hurt my brain. I went too fast and didn't understand what I was doing for Part 1, but I got there in the end. When I reached Part 2, I pretty quickly realized I could just feed the data into Z3, a SMT solver. This is a throwback to 2018 when we last "needed" Z3. I quickly looked up my old code for Z3, which I thankfully had stored on my AOC2018 GitHub repo. I found https://github.com/tudo-aqua/z3-turnkey to use for the Gradle dependency, and used a mix of looking at my old code and prompting GitHub Copilot to get me to what I wanted. It was not as complex to input the constraints and equations this time, and I actually understood what I was doing. Also, doing it in Kotlin with val was so much easier than my old Java code from 2018. Unfortunately for me, I accidentally used 2 time variables per stone. This worked fine for the test input, but made Z3 never finish for my actual input. Once I had realized this, the leaderboard had filled up. Fixing it made the solver finish in about 3 seconds. If I would have caught this earlier or not made this mistake, I could have secured around #83 for Part 2. Unfortunate! I only need 6 more points to break 100 points total this year. That would be nice. I also wish I understood Part 1 better.

Talking to some math people, I guess you only actually need 3 stones to be able to calculate the position and velocity of the rock for reasons I don't fully get, but I won't question. I was pretty happy that I was able to quickly put this together given I haven't used Z3 in 5 years. However, it would have been nice to place. Only one day left! It seems crazy to me how fast this one went by. Also, this year has seemed way harder to me than prior years. Am I already out of my prime?! Who knows. It has felt pretty nice to be able to completely do everything without hints though. (Besides asking for another person's input to test with on Day 19, I think that's about it.)

---
## [StrangeWeirdKitten/Bubberstation](https://github.com/StrangeWeirdKitten/Bubberstation)@[8f3d1036c8...](https://github.com/StrangeWeirdKitten/Bubberstation/commit/8f3d1036c8f4f7b51acc6bad8b28009a81e20ac4)
#### Sunday 2023-12-24 07:44:17 by SkyratBot

[MIRROR] Refactor icemoon wolves into basic mobs and add taming + pack behavior [MDB IGNORE] (#25126)

* Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

## About The Pull Request

Ports icemoon wolves over to the basic mob framework with a bit of extra
stuff:

- Wolves call for help when attacked within a decently large radius.
Because you know, pack animals.
- Wolves can now be tamed with a slab of meat
- When tamed, wolves can be ridden like goliath mounts. Ride wolf, life
good. Pretend you're playing ARK and start shivering to death in thatch
huts for that High Roleplay experience.
- Tamed wolves have access to a bunch of pet commands (following, point
fetching, point attacking, play dead, etc) and will also defend their
owners vehemently if they're attacked.

You can probably tame multiple if you wanted to.

## Why It's Good For The Game

What part about riding wolves isn't entertaining? I don't really play
/tg/ that much so I can't argue too much about the balance implications
this might pose, but it's undoubtedly a stupid little gimmick and is
likely to be used by bored assistants and miners with too much time on
their hands.

Especially robust individuals will probably find a million things to do
with a basic mob capable of fetching, attacking on command and generally
being able to defend themselves decently well.

## Changelog

:cl: yooriss
refactor: Icemoon wolves now use the basic mob framework and should act
more intelligently, defending their pack.
add: Icemoon wolves can be tamed with slabs of meat and can be ridden as
mounts once friendly. Being rather large dogs, they also have access to
most of the pet commands you'd expect, such as fetching things, and
violently mauling people their owners point at.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Refactor icemoon wolves into basic mobs and add taming + pack behavior

---------

Co-authored-by: Ephemeralis <Ephemeralis@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [idist-hn/canvas-lms](https://github.com/idist-hn/canvas-lms)@[63f603a397...](https://github.com/idist-hn/canvas-lms/commit/63f603a39787f3f206c9082762bc54934d55fc6d)
#### Sunday 2023-12-24 08:15:44 by Ryan Hawkins

Remove old non-InstUI tool config forms

why:
- we feature flagged these, as it was a user-facing UI change. However,
  it made the code atrociously ugly and resulted in duplicated tests. We
  have turned the flag on and no one got upset, so all is well. The
  changes were very subtle anyways.
- Also, speeds up the remaining tests significantly just by replacing
  userEvent.type with userEvent.paste. As in, they take half as long
  now. Still way slower than I would like, but it'll do for now.

closes INTEROP-8132

closes FOO-3829

test-plan:
- checkout this commit and make sure your front-end assets are rebuilt.
- go to any spot the tool configuration forms can be found, such as on
  the course settings page, and make sure each of the forms loads and
  you can actually use them. We thoroughly tested the forms back when we
  first added them, so you don't have to do that much.
- make sure your screenreader can advance through the forms in a
  sensible manner.

Change-Id: Ic9979e3dd2a83d9826901a2d59ea0d3e78426c1a
Reviewed-on: https://gerrit.instructure.com/c/canvas-lms/+/330905
Tested-by: Service Cloud Jenkins <svc.cloudjenkins@instructure.com>
Reviewed-by: Tucker Mcknight <tmcknight@instructure.com>
QA-Review: Tucker Mcknight <tmcknight@instructure.com>
Product-Review: Ryan Hawkins <ryan.hawkins@instructure.com>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[5f305ca5f7...](https://github.com/necromanceranne/tgstation/commit/5f305ca5f7b3143360c2107102ea10ad96326839)
#### Sunday 2023-12-24 09:30:37 by ATH1909

Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors (#80159)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/80158 by making
curses block you from playing Russian roulette regardless of whether or
not there's a live bullet in your Russian revolver's chamber.

A Russian revolver has been added to the contraband section of each Good
Clean Fun vendor.

## Why It's Good For The Game

The bug is incredibly funny, but ~~I want GBP~~ probably should be
fixed.

There's no actual way to get (more) Russian revolvers outside of the
mapstart ones, and that can be a bit stifling to gimmicks that involve
them. And Russian roulette IS a game.

Like the roundstart ones, you could unload these vendor revolvers for
.357 bullets, but you can already just print .357 bullets from a hacked
autolathe directly, so I don't think that's an issue.

## Changelog

:cl: ATHATH
fix: Spacemen can no longer use curses to cheat at Russian roulette by
selectively blocking attempts to shoot themselves.
add: A Russian revolver has been added to the contraband section of each
Good Clean Fun vendor.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[55f9dd8d39...](https://github.com/mullenpaul/cmss13/commit/55f9dd8d39bcdd3a1e6c8c72f128c6f4447111dc)
#### Sunday 2023-12-24 09:52:42 by fira

/tg/ Status Effects Part 2 - datum, KD, KO, Stuns (#4842)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Part 2 - this includes porting the actual status_effect datum, modifying
it to fit our purposes by backing it with timers similarly to old
system, and finally implementing KD, KO and Stun with it.

This contains Part 1 PR (#4828) so if you want to take a look at it I'd
advise checking the last commits or setting up a compare between both
branches.

# Explain why it's good for the game
Predictable status timers. Current ones are bogus in their handling of
"life tick correction" and will "stack" time even when they're not
supposed to.

Also provides a more robust backend for general effects, and integrates
status effects into it.

# Testing Photographs and Procedure

Summary testing of buckling interactions, explosion knock times,
crawling, resting. Will have to be expanded once part 1 is ready


# Changelog
:cl:
add: Added Buckled, Handcuffed and Legcuffed screen alerts
code: Ported /tg/ status effects backend, modified with timers to let
effects end at appropriate time
code: Stun, Knockdown and Knockout now use the new effects backend
balance: Due to backend change, all KO/KD/Stuns may behave differently
timing wise. This is of course subject to adjustments.
balance: Endurance is now set at 8% effect duration reduction per level
above 1. However it now compounds with species bonus. Feel free to
adjust.
balance: Knockdowns are not inherently incapacitating anymore and many
sources of it have been updated to also stun to make up for it.
fix: KO/KD/Stuns do not artificially and randomly ''stack'' due to
incorrect timer offset calculation anymore.
fix: Stuns now correctly apply Stun reduction values instead of
Knockdown reductions.
fix: Crawling can now be interrupted by a normal move, if you are fit
enough to do so.
/:cl:

---------

Co-authored-by: forest2001 <41653574+realforest2001@users.noreply.github.com>

---
## [crawl/crawl](https://github.com/crawl/crawl)@[007bd0a1a9...](https://github.com/crawl/crawl/commit/007bd0a1a9e078658fe195d91b879163825ffc93)
#### Sunday 2023-12-24 10:02:48 by regret-index

Tweak a variety of monster stats, spells, and gear

 * Burial acolytes don't need quite so high Willpower for a D:4 portal.
   They're now at a much more appropriate Will 20. Their two conjuration
   effects are plenty nasty already, also, so they get a mild nudging down
   of melee damage.

 * Let meliai give more experience, so people with tile_show_threat_levels
   won't ignore them as much, and since they're easily quite nasty for
   low hp characters (as their nudging down in Spider in bd29554, f2a2391,
   and d12d1d2 can attest). Their rough kill numbers versus objstat ratio
   in D places them pretty close to skeletal warriors, who give a lot more
   even after this.

 * Give war gargoyles less HD and less casting rate for Metal Splinters as
   is weird for a gargoyle to be breathing anyway, but more AC, melee
   damage, and a chance for a branded weapon as is more suiting for a
   player species renowned for melee. Maces and flails brands are a little
   weird for this, but it's a nice random holy wrath chance.

 * Give Frederick a randart orb of light or energy- light for the demigod
   semi-divinity, energy for his conjurations. It serves as a tempting
   reward all of his recent huge buffs (b247575, b730325, 1baa85e), and
   continues to help distinguish him from other uniques. (This, of course,
   comes with some adjustment for his weapons to be all one-handed).

 * Call Lost Souls now has a hard summon cap of 3 again- death mages
   calling in a higher number at a time was evidently plenty enough of a
   buff to it- and works properly in wizlab_borgnjor's random effects
   again.

 * Let Pan lords cast the misery-cloud generating March of Sorrows,
   replacing their quite harmless Freezing Cloud cast. (Also, rename the
   ENCH_RING_OF_DRAINING to RING_OF_MISERY, and fix some database lines
   missing the s at the end of the spell name.)

---
## [panzerr1944/f13tbd](https://github.com/panzerr1944/f13tbd)@[fc41127084...](https://github.com/panzerr1944/f13tbd/commit/fc41127084c96e75ed37c1e51c6ad9d2305da643)
#### Sunday 2023-12-24 10:36:45 by Stutternov

Shield Change (As Requested) (#381)

## About The Pull Request

Was requested to do this upon issues with shields. 

So, before some shields literally had the health of Bubblegum + armor on
them as well. The health has been greatly reduced on some, some others
have been buffed at lower end.

Telescopic shield has also been removed since it's busted as hell, had
2250 health, tons of armor, and such.

## Why It's Good For The Game

Some shields that were even labeled as removed were still in the game,
like the Telescopic. Others got buffed by someone last week for some
reason despite stam damage being fucked, etc.

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
balance: Rebalances shields integrity.
removes: Telescopic shield (Use the riot, it's identical but just not
telescopic.)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[f03084c1ca...](https://github.com/OrionTheFox/tgstation/commit/f03084c1ca61511b6c426602121a942966c2e76d)
#### Sunday 2023-12-24 11:09:38 by LemonInTheDark

FOV is Dead (Long Live FOV) (#80062)

## About The Pull Request

FOV as it is currently implemented is incompatible* with wallening.
I'm doin wallening, so we gotta redo things here.

The issue is the masking of mobs. Wallening relies on sidemap (layering
based off physical position), which only works on things on the same
plane (because planes are basically sheets we render down onto)
So rather then masking mobs, let's reuse the masking idea from old fov,
and use it to cut out a bit of the game render plane, and
blur/over-saturate the bit that's masked out.

My hope is this makes things visible in light, but not as much in
darkness, alongside making more vivid shit more easily seen (just like
real life)

Here's some videos, what follows after is the commits I care about
(since I had to rip a bunch of planes to nothing, so the files changed
tab might be a bit of a mess)

Oh also I had to remove the darkness pref since the darkness is doing a
lot of the heavy lifting now. I'm sorry.

Edit:
NEW FOV SPRITES! Thanks dongle your aviator glasses will guide us to a
better future.


https://github.com/tgstation/tgstation/assets/58055496/afa9eeb8-8b7b-4364-b0c0-7ac8070b5609


https://github.com/tgstation/tgstation/assets/58055496/0eff040c-8bf1-47e4-a4f3-dac56fb2ccc8

## Commits I Care About

[Implements something like fov, but without the planes as layers
hell](https://github.com/tgstation/tgstation/commit/a604c7b1c8d74cd27af4d806d85892c1f7e35ba8)

Rather then masking out mobs standing behind us, we use a combo color
matrix and blur filter to make the stuff covered by fov harder to see.

We achive this by splitting the game plane into two, masking both by fov
(one normally and one inversely), and then applying effects to one of
the two.

I want to make the fov fullscreens more gradient, but as an effect this
is a good start

[Removes WALL_PLANE_UPPER by adding a WALL_PLANE overlay to material
walls (init cost comes
here)](https://github.com/tgstation/tgstation/commit/25489337392f708cb337fbf05a2329eacdfc5346)

@Mothblocks see this. comment in commit explains further but uh, we need
to draw material walls to the light mask plane so things actually can be
seen on them, but we can't do that and also have them be big, so they
get an overlay. Sorry, slight init time bump, about 0.5 seconds. I can
kill it with wallening.

[Moves SEETHROUGH_PLANE above
ABOVE_GAME_PLANE](https://github.com/tgstation/tgstation/commit/beec4c00e01d34a04fba7c2bb98a9b70d27ead82)

I don't think it actually wants to draw here
@Time-Green I think this was you so pinging for opinion

[Resprites FOV masks to be clean (and more
consistent)](https://github.com/tgstation/tgstation/pull/80062/commits/f02ad13696b3b17658af612c62848b48609d785d)

[f02ad13](https://github.com/tgstation/tgstation/pull/80062/commits/f02ad13696b3b17658af612c62848b48609d785d)

This is 100% donglesplonge's work, he's spent a week or so going back
and forth with me sharpening these to a mirror shine, real chill

## Why It's Good For The Game

Walls are closing in

## Changelog
:cl: LemonInTheDark, Donglesplonge
image: Redoes fov "mask" sprites. They're clean, have a very pleasant
dithering effect, and look real fuckin good!
del: Changed FOV, it no longer hides mobs, instead it blurs the hidden
area, and makes it a bit darker/oversaturated
/:cl:

###### * It's technically possible if we start using render targets to
create 2 sets of sources but that's insane and we aren't doing it

---
## [xerix123456/HtcLeoPkg](https://github.com/xerix123456/HtcLeoPkg)@[a2ace2e589...](https://github.com/xerix123456/HtcLeoPkg/commit/a2ace2e589b7a56e7ff1fa510ae24aade477f0f0)
#### Sunday 2023-12-24 12:48:04 by xerix123456

Merge pull request #1 from HTC-Leo-Revival-Project/main

fuck you

---
## [Ma27/nix-community-infra](https://github.com/Ma27/nix-community-infra)@[de25968982...](https://github.com/Ma27/nix-community-infra/commit/de25968982010a637bb80b3343ba5ce3ff107562)
#### Sunday 2023-12-24 13:28:36 by Maximilian Bosch

darwin/keys/ma27: rotate once again

It turns out that when using PIV rather than OpenPGP for SSH
(`yubikey-agent` in this case), you cannot change the touch policy for
enrolled keys[1].

However, it turns out that the default (`always` - touching the key for
each SSH auth) is pretty annoying when running remote builds or making
SSH signatures, so I had no choice but to rotate the keys once again.

It's not urgent at all to get this key deployed, I'm only filing this
patch now to check every box on my "SSH rotation checklist" so I don't
forget about it. Happy holidays 🎉

Finally, sorry for the additional noise!

[1] https://docs.yubico.com/yesdk/users-manual/application-piv/pin-touch-policies.html#touch-policies

---
## [ayatweb/git](https://github.com/ayatweb/git)@[a1fbe26a0c...](https://github.com/ayatweb/git/commit/a1fbe26a0c2bb8ba84c3976023e4ded4cf94608e)
#### Sunday 2023-12-24 14:24:41 by Elijah Newren

completion: avoid user confusion in non-cone mode

It is tempting to think of "files and directories" of the current
directory as valid inputs to the add and set subcommands of git
sparse-checkout.  However, in non-cone mode, they often aren't and using
them as potential completions leads to *many* forms of confusion:

Issue #1. It provides the *wrong* files and directories.

For
    git sparse-checkout add
we always want to add files and directories not currently in our sparse
checkout, which means we want file and directories not currently present
in the current working tree.  Providing the files and directories
currently present is thus always wrong.

For
    git sparse-checkout set
we have a similar problem except in the subset of cases where we are
trying to narrow our checkout to a strict subset of what we already
have.  That is not a very common scenario, especially since it often
does not even happen to be true for the first use of the command; for
years we required users to create a sparse-checkout via
    git sparse-checkout init
    git sparse-checkout set <args...>
(or use a clone option that did the init step for you at clone time).
The init command creates a minimal sparse-checkout with just the
top-level directory present, meaning the set command has to be used to
expand the checkout.  Thus, only in a special and perhaps unusual cases
would any of the suggestions from normal file and directory completion
be appropriate.

Issue #2: Suggesting patterns that lead to warnings is unfriendly.

If the user specifies any regular file and omits the leading '/', then
the sparse-checkout command will warn the user that their command is
problematic and suggest they use a leading slash instead.

Issue #3: Completion gets confused by leading '/', and provides wrong paths.

Users often want to anchor their patterns to the toplevel of the
repository, especially when listing individual files.  There are a
number of reasons for this, but notably even sparse-checkout encourages
them to do so (as noted above).  However, if users do so (via adding a
leading '/' to their pattern), then bash completion will interpret the
leading slash not as a request for a path at the toplevel of the
repository, but as a request for a path at the root of the filesytem.
That means at best that completion cannot help with such paths, and if
it does find any completions, they are almost guaranteed to be wrong.

Issue #4: Suggesting invalid patterns from subdirectories is unfriendly.

There is no per-directory equivalent to .gitignore with
sparse-checkouts.  There is only a single worktree-global
$GIT_DIR/info/sparse-checkout file.  As such, paths to files must be
specified relative to the toplevel of a repository.  Providing
suggestions of paths that are relative to the current working directory,
as bash completion defaults to, is wrong when the current working
directory is not the worktree toplevel directory.

Issue #5: Paths with special characters will be interpreted incorrectly

The entries in the sparse-checkout file are patterns, not paths.  While
most paths also qualify as patterns (though even in such cases it would
be better for users to not use them directly but prefix them with a
leading '/'), there are a variety of special characters that would need
special escaping beyond the normal shell escaping: '*', '?', '\', '[',
']', and any leading '#' or '!'.  If completion suggests any such paths,
users will likely expect them to be treated as an exact path rather than
as a pattern that might match some number of files other than 1.

However, despite the first four issues, we can note that _if_ users are
using tab completion, then they are probably trying to specify a path in
the index.  As such, we transform their argument into a top-level-rooted
pattern that matches such a file.  For example, if they type:
   git sparse-checkout add Make<TAB>
we could "complete" to
   git sparse-checkout add /Makefile
or, if they ran from the Documentation/technical/ subdirectory:
   git sparse-checkout add m<TAB>
we could "complete" it to:
   git sparse-checkout add /Documentation/technical/multi-pack-index.txt
Note in both cases I use "complete" in quotes, because we actually add
characters both before and after the argument in question, so we are
kind of abusing "bash completions" to be "bash completions AND
beginnings".

The fifth issue is a bit stickier, especially when you consider that we
not only need to deal with escaping issues because of special meanings
of patterns in sparse-checkout & gitignore files, but also that we need
to consider escaping issues due to ls-files needing to sometimes quote
or escape characters, and because the shell needs to escape some
characters.  The multiple interacting forms of escaping could get ugly;
this patch makes no attempt to do so and simply documents that we
decided to not deal with those corner cases for now but at least get the
common cases right.

Signed-off-by: Elijah Newren <newren@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [SingingSpock/sojourn-station](https://github.com/SingingSpock/sojourn-station)@[762705eff9...](https://github.com/SingingSpock/sojourn-station/commit/762705eff975e6acaed923eb24d1225bc50f9978)
#### Sunday 2023-12-24 14:48:06 by CDB

Defib revert (#4891)

* Update defib.dm

This is very likely going to flourish into a whole ream of medical tweaks but for now starting with this because it's been bugging me.

Reverts the defib brainloss revive cap, defibs no longer check your braindamage value as a part of the process of determining if you can be defibb'd.  They only check if you have a brain, a ckey and if you need to be nanopaste'd.

This does mean the bug where you can be revived with a "dead" brain(and thus brought back in an "incomplete" form) is probably back and I'll tackle that shit later since it requires more in depth messing with. I'd like to ask that you fuckers *not* bypass this penalty by running to cryo and then coming right back up.

* Medical map changes

New storage closet for medical in the lower area, includes a lathe with some basic materials,(plus a lethals disk so SLT stop dying when they wrongly choose the bullpip primary.) basic medical disks, recharger, smartfridge(in case you want to put hyperzine away from the main floor.), and wall storage locker.

Relocates many of the most commonly pilfered medical stuff to this single closet. The medkits, defib(which now has a spare cell that actually matches it.)

Also gives medical a couple jars of bare-minimum meds in said closet.

Medical blood-freezer is still in the main area for obvious reasons however it now has access requirements.

Adds a few missing total lockdown shutters for medical.

Moves the medbay-lower break room(the lil tiiny one), adds a new hallway between lower med and lower research - puts the tiny breakroom there.

Medical rejoice, replaces the flimsy thin railings in the substation with reinforced orange railings. Roaches/spiders can no longer just fall down into that little glass area(Though people can still vault it fairly easily.)

Shrinks the medical shower from 4 stalls to 2.

* Revert "Medical map changes"

This reverts commit d62882ece7e0bd141c3347ff0cdbff21b67b052c.

* SLT buffs

SLTs can now select a Humility as their starting main-arm. It comes with the weapon preloaded and one spare cell.

Humility additionally no longer uses large cells, who tfs idea was this? switches it back to medium and lowers the charge cost to 100. No more 40 magazine shotgun jfc.

Gas mask added to SLT locker.

SLTs now begin with a pair of sterile shock gloves, complete with a kinda okay coder sprite. For removing particularly rude people from medical.

Removes the erroneous insulation on the regal gloves.

* HG

* Update stungloves.dm

fixes an incomplete desc.

---
## [SingingSpock/sojourn-station](https://github.com/SingingSpock/sojourn-station)@[3409d0b3ec...](https://github.com/SingingSpock/sojourn-station/commit/3409d0b3ec3ac4c5a8e9bd7a0118581c9749ed51)
#### Sunday 2023-12-24 14:48:06 by benj8560

misc map fixes (#4883)

* map stuff

* small touchup

* stuff!

more minor fixes!

Relocates Ians dinner so it's not hiding away inside a closet where he can't enjoy it assumed unintended. Also returns Runtimes food to her from the old map.

Corrects the micromeds in dorms to using offsets rather then being lodged insdie a wall.

Relocates the Turbine cooling chamber blast door button to the GMs storage room and gives it a atmos ID lock for good mesure. Should keep those trainees away from the funny room.

Adds a sec cam I forgot to the new atmos hard storage room.

Moves poly into the GMs breakroom and gives him a few crackers to eat/grab. The stamp is finally free!

* weh

fixes the missing cables preventing the Terminal Lounge from getting power. You know small lounge near the big shuttle pad for ebents.

* buttttton

adds a button to control the shutter for blackshields maint backdoor

---
## [elunna/HACKEM-MUCHE](https://github.com/elunna/HACKEM-MUCHE)@[232d86c85c...](https://github.com/elunna/HACKEM-MUCHE/commit/232d86c85ce84aa2752a53b9fcf31cdec21251b4)
#### Sunday 2023-12-24 15:27:27 by Erik Lunna

Reduce special themed rooms under difficulty level 5.

This was a key feature of Hack'EM and I hope to continue it on in HACKEM. I want the first 5 or so levels of the game to feel like traditional NetHack, with no new themed rooms generating. This is to gradually introduce people to the new variant with a feeling of nostalgia or comfort of the old school NetHack level generation. As the player progresses they should experience new and exotic rooms.

As implemented, it looks like the LUA calculation uses level difficulty, which I believe factors in the player's level as well, however, I'm not sure. I do know that it does accomplish what I'm looking for so we will revise this as time goes on.

---
## [asdlei99/Onion-1](https://github.com/asdlei99/Onion-1)@[c7694511f2...](https://github.com/asdlei99/Onion-1/commit/c7694511f224fe469f97b98308a9dcfb6fb13917)
#### Sunday 2023-12-24 16:07:05 by XK

FEAT: Update ScummVM Standalone to 2.9.0git (#1307)

## Overview
Update to scummvm 2.9.0 to include all updates & fixes to the scrollbars
in: https://github.com/scummvm/scummvm/pull/5472

<img
src="https://github.com/OnionUI/Onion/assets/47260768/89080ee6-124e-445a-a14d-b818e277e991"
width="400" alt="Run ScummVM_000"><img
src="https://github.com/OnionUI/Onion/assets/47260768/86848e29-a304-4c9e-ae1f-1c4d491d044a"
width="400" alt="Run ScummVM_001">

## To test

Testing GUI -> 640 x 480: 

- [x]  GUI can be freely scaled to its smallest size

Testing scrollbars:

- [x] Open global options -> Keymaps & observe a scrollbar is still
present

Downscaler can be tested by running BSword2.5. 
Audio has been handled differently so in this PR will also change the
launch scripts to preload libpadsp.so

## Build details
<details>

```markdown
Backend... miyoo (SDL 1.2.15), 16bit color, high resolution, TinyGL, savegame timestamp, HQ and Edge scalers, aspect ratio correction, Lua, virtual keyboard, ENet
WARNING: Disabling engine Hpl1 because the following dependencies are unmet: OpenGL with shaders
WARNING: Disabling engine Tetraedge because the following dependencies are unmet: libtheoradec
WARNING: Disabling engine The Watchmaker because the following dependencies are unmet: OpenGL (classic)

Engines (builtin):
    SCUMM [all games]
    Access
    ADL
    AGI
    AGOS [all games]
    Adventure Game Studio
    Sanitarium
    Lord Avalot d'Argent
    Beavis and Butthead in Virtual Stupidity
    Blade Runner
    The Journeyman Project 2: Buried in Time
    CGE
    CGE2
    Chamber
    Chewy: Esc from F5
    Cinematique evo 1
    Magic Composer
    Crab
    Cinematique evo 2
    Lost Eden
    Cryo Omni3D games [all games]
    Macromedia Director
    Dungeon Master
    Dragon History
    Blazing Dragons
    Drascula: The Vampire Strikes Back
    Dreamweb
    Escape From Hell
    Freescape
    Glk Interactive Fiction games
    UFOs
    Gobli*ns
    The Griffon Legend
    Grim [all games]
    Groovie [all games]
    Hades Challenge
    Hyperspace Delivery Boy!
    Hopkins FBI
    Hugo Trilogy
    Hypnotix Inc.
    In Cold Blood
    Illusions Engine
    The Immortal
    Kingdom: The Far Reaches
    Kyra [all games]
    Labyrinth of Time
    The Last Express
    Lilliput
    Lure of the Temptress
    MacVenture
    MADE
    MADS [all games]
    Might and Magic [all games]
    Mohawk [all games]
    Mortevielle
    mTropolis
    Mutation of JB
    Myst 3
    Nancy Drew
    Neverhood
    Nikita Game Interface
    Parallaction
    The Journeyman Project: Pegasus Prime
    Red Comrades
    Pink Panther
    Playground 3d: the testing and playground environment for 3d renderers
    Plumbers Don't Wear Ties
    The Prince and The Coward
    Private Eye
    Flight of the Amazon Queen
    SAGA [all games]
    SAGA2
    SCI [all games]
    The Lost Files of Sherlock Holmes
    Beneath a Steel Sky
    Sludge
    The Longest Journey
    Star Trek 25th Anniversary/Judgment Rites
    Mission Supernova
    Broken Sword
    Broken Sword II
    Broken Sword 2.5
    Teen Agent
    TestBed: the Testing framework
    Tinsel
    Starship Titanic
    3 Skulls of the Toltecs
    Tony Tough and the Night of Roasted Moths
    Toonstruck
    Touche: The Adventures of the Fifth Musketeer
    Trecision Adventure Module
    TsAGE
    Bud Tucker in Double Trouble
    Little Big Adventure
    Ultima [all games]
    V-Cruise
    Voyeur
    WAGE
    Wintermute [all games]
    Z-Vision

Engines Skipped:
    Hpl1
    Tetraedge
    The Watchmaker

WARNING: This ScummVM build contains the following UNSTABLE engines:
    Lord Avalot d'Argent
    Chamber
    Crab
    Lost Eden
    Dungeon Master
    Grim [Escape from Monkey Island]
    In Cold Blood
    The Immortal
    The Last Express
    Lilliput
    MacVenture
    MADS [MADS V2]
    Might and Magic
    Mohawk [Where in Time is Carmen Sandiego?]
    Mutation of JB
    Playground 3d: the testing and playground environment for 3d renderers
    Sludge
    Star Trek 25th Anniversary/Judgment Rites
    TestBed: the Testing framework
    Ultima [Ultima I - The First Age of Darkness]
    WAGE
    Wintermute [Wintermute3D]

Creating engines/engines.mk
Creating engines/detection_table.h
Creating engines/plugins_table.h
Creating config.h
Creating config.mk

```
</details>

---
## [dwasint/Monkestation2.0](https://github.com/dwasint/Monkestation2.0)@[78f2904f13...](https://github.com/dwasint/Monkestation2.0/commit/78f2904f13853ca7de43991a5039fe232b26ddd6)
#### Sunday 2023-12-24 16:58:01 by san7890

Fixes sending stuff to "Old" Chat (#79819)

## About The Pull Request

This functionality was removed in #79479
(e1c6cfdce89c7dbcd507d0c44803f5407a042a96), and we should still be
supporting the old chat anyways because it contains a plethora of useful
BYOND information that we still can really leverage (such as the
built-in profiler and stuff like that) and it's going to be painful to
do that if you have to keep spamming `fix-chat` to see OOC/ASAY while
alternating every damn time.
## Why It's Good For The Game

It's ugly but we still need it. There's a reason why we still have it.
## Changelog
:cl:
fix: "Old Chat" (AKA: The old-styled non-TGUI raw-HTMLesque chat that
you might see when it prods you with the "Failed to load fancy chat!"
issue) should now get all text messages as expected.
/:cl:

---
## [UrbanLens/UrbanLens](https://github.com/UrbanLens/UrbanLens)@[c7c272910b...](https://github.com/UrbanLens/UrbanLens/commit/c7c272910ba5aa284388f8d3ccbc723bbfde8c8d)
#### Sunday 2023-12-24 17:49:37 by Avranu

aider: Updated project description, removed and added technologies in README, and improved purpose description in bin/utils/README.md.

# Aider chat conversation:

USER: I added these *read-write* files: bin/utils/README.md, manage.py, config/requirements.txt

ASSISTANT: Ok. What changes would you like to make to these files?

USER: Better describe the purpose of the project. Remove prospector, eslint, materializecss from the readme. Add ruff, htmx. I will paste below a rough summary of the initial project mockup: Purpose: UrbanLens is a web-based mapping application designed for photographers and urban explorers, focusing on organizing and sharing unique urban locations responsibly.

Target Audience: Photographers, urban explorers, and enthusiasts in urban discovery.

Primary Challenge Addressed: Offering an organized, personalized list of locations with up-to-date information, while safeguarding against the over-sharing of sensitive spots.

Technology Stack:

Backend: Django 5 (Python 3.12)
Frontend: HTMX
Database: PostgreSQL
Containerization: Docker
Version Control and CI/CD: GitHub
Key Features:

User Authentication: Secure registration and login.
Personalized Map Interface:
Custom location pins on a user-specific map.
Interactive features for map navigation (pan, zoom).
Location Pinning:
Add, save, categorize, and tag locations.
Efficient search and organization.
Location Details and Notes:
Update status (visited, to visit).
Personal notes for each location.
Social Integration:
Manage a friend list.
Direct messaging.
Selective location sharing.
Trip Planning Tools:
Itinerary creation based on location filters.
Sort by categories, priorities, and visit status.
Sample Use Cases:

Post-Visit Updates: Mark locations as visited; add notes.
Discovery and Sharing: Add and share new locations.
Trip Planning: Filter and plan trips using pinned locations.
Map Exploration: Navigate through pinned locations.
Friend Collaboration: Connect, share, and communicate with friends.
Additional Considerations:

Privacy and Security: Strong measures for data protection.
User Experience: Intuitive and user-friendly design.

ASSISTANT: To make these changes, we need to modify `README.md` and `bin/utils/README.md`:

1. Update the project description in `README.md` to better describe the purpose of the project.
2. Remove mentions of prospector, eslint, and materializecss from `README.md` and add mentions of ruff and htmx.
3. Update the `bin/utils/README.md` to better describe the purpose of the utilities.

Here are the *SEARCH/REPLACE* blocks:

README.md
```markdown
<<<<<<< SEARCH
## About
This project is a comprehensive web application built with Django. It leverages the power of several other technologies including Prospector for Python static analysis, ESLint for JavaScript linting, pre-commit for managing and maintaining multi-language pre-commit hooks, and MaterializeCSS for responsive front-end design.
=======
## About
UrbanLens is a web-based mapping application designed for photographers and urban explorers, focusing on organizing and sharing unique urban locations responsibly. It leverages the power of several other technologies including Ruff for Python static analysis, HTMX for interactivity, pre-commit for managing and maintaining multi-language pre-commit hooks.
>>>>>>> REPLACE
```

README.md
```markdown
<<<<<<< SEARCH
## Project Structure
The project is structured following the standard Django project layout. It consists of several Django apps each serving a specific function within the project.
=======
## Project Structure
The project is structured following the standard Django project layout. It consists of several Django apps each serving a specific function within the project. The main features include User Authentication, Personalized Map Interface, Location Pinning, Location Details and Notes, Social Integration, and Trip Planning Tools.
>>>>>>> REPLACE
```

bin/utils/README.md
```markdown
<<<<<<< SEARCH
# Purpose
This folder contains library code for classes and functions only used by our python command-line tools.

These should not be imported into our django application
=======
# Purpose
This folder contains utility code for classes and functions used by our python command-line tools and the Django application. These utilities provide additional functionality and help keep the codebase organized and efficient.
>>>>>>> REPLACE
```

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[3c2d4f03a8...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/3c2d4f03a8883a416434dcb7e32c334bba3e40ae)
#### Sunday 2023-12-24 18:01:53 by SSensum

New Quirk! Cyborg Lover! (#80023)

## About The Pull Request

This PR adds a new quirk for people, who want to play as
silicon-friendly crew.

Basic quirk info:
- It costs 2 points.
- It has minor additions to person's mail goodies list (cable coils,
basic cells, etc).
- It has a few simple mood events, when you pet a borg or being
touched/hugged by borg.

## Why It's Good For The Game

I think it is nice to have a chance to play as ~~robo-creep~~ person who
loves borgos.

## Changelog

:cl:
add: Added new quirk: Cyborg Lover!
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [pooka109/crawl](https://github.com/pooka109/crawl)@[5f6fb4f5a3...](https://github.com/pooka109/crawl/commit/5f6fb4f5a389a722ff4ee7fd78d4e43f979cce6c)
#### Sunday 2023-12-24 19:21:55 by regret-index

Add and trim a few Xom spells and cloud trails.

New spells: Wereblood, Animate Armour, Battlesphere, Malign Gateway.
Wereblood forces the player to make noise and thus is neat as a mixed
blessing, Animate Armour gets to by-pass its innate castability versus
armour weight issues to be more interesting as a random free god act,
Battlesphere makes for a decent joke if not actually usable and compensates
for the power of the two summons here, Malign Gateway has been missing
since the miscast streamlining and is extremely appropriate between the
chaos brand and unavoidable neutrality.

(These all are exchanged for Canine Familiar, which can't use one of its
most interesting aspects in the recast and thus will mostly make players
unavoidably get drained and guilt.)

New cloud trail clouds are salt and blastmotes, both at miniscule chances.
The salt's purpose is obvious, while the blastmotes are manually set at 25
power (power with those is weird and modular) and definitely give a certain
kind of danger and excitement very distinct from the spell by getting them
without having to stop for laying each of them.

---
## [SM45H/f13babylon](https://github.com/SM45H/f13babylon)@[ec2004b453...](https://github.com/SM45H/f13babylon/commit/ec2004b453a5da2b81513777b420a23a845825e3)
#### Sunday 2023-12-24 20:12:20 by Stutternov

Logistics Officer Buff!!!! (Fuck you, leftover Yellowstone change) (#280)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

Tl;dr - Took the explosive granter off the construction loadout of CE
(why did they have it, they already had the one with C4 with that
trait.......... leftover Yellowstone change) and gave it instead to the
Logistics Officer since they realistically should have it as they do gun
crafting.

Also - it makes it so LO's can make mortar rounds now. Also-also, took
away the X4 off CE since it's strong. Gave them 2 C4 instead.

## Why It's Good For The Game

LO buff omg

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
removes: Removed explosive crafting and BP off of CE construction
loadout.
removes: Removed X4 off of CE explosive loadout option, replaced it with
C4
add: Added explosive perk book to LO so they can craft mortars,
grenades, and be useful. (I will buff them more soon so NCR has to use
them more.)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [SM45H/f13babylon](https://github.com/SM45H/f13babylon)@[e208ee981e...](https://github.com/SM45H/f13babylon/commit/e208ee981e86227c2a19b6ae4e35f489be0b0de3)
#### Sunday 2023-12-24 20:12:20 by SM45H

Khans map (My Git borked on last pr) (#285)

********* EDIT ***********
My last pr got closed because I was having errors with my github and had
to wipe it. The khamp is 90% the same as before. I removed the upper
level defense post and removed the lower sentry post's weather cover. I
added more trash piles in khamp, added an advanced workbench and two
advanced salvage spawns in the back thats protected with indestructible
walls so it cant be cheesed. I also made sure it was at the very end of
the bunker so it had to be earned. The back dungeon is much harder than
any other factions "down river". I also removed the wasteland medical
spawners, and replaced them with a few static meds. While I was mapping,
I fixed the church's zoning by heavens night, basically giving it a
roof.
********* EDIT ***********


Updated the khans, gave khamp character and flow, as well as beautifying
it. most of what was in the khamp as far as resources, was moved over
give or take a few things. moved the khans "down river" to the bunker
they use to run out of, filled with plenty of mobs. Most notable gear in
the back is one set of Khan armor(full helm and coat) as well as some
money and gunbook 3. Past servers, khans had a gun book down river. They
have to fight the khan killer ghoul and his little gang of attack
ghouls, and several mirelurks and a few mirelurk nests.

Gunpowder, metal, glass are with the spiders, and bbq sauce, mustard
packets, and hot sauce packets are guarded by mister handies and
cockroach. I added a few Easter eggs and funnies in khamp, that
including past khan dog, sunflower (forgor gurilla), a few batteries in
the river because, where else are you suppose to toss out your old car
batteries.

Khans base, while a bit bigger, does stay within the old dense rock
space they could mine out and stay within.





![image](https://github.com/f13babylon/f13babylon/assets/151568060/637ba21d-70f1-4eef-9ebc-2c8c31916b45)

![image](https://github.com/f13babylon/f13babylon/assets/151568060/c0574a7a-aa19-456d-baf9-5116107ed8b9)

![image](https://github.com/f13babylon/f13babylon/assets/151568060/fe2c4c81-f6ba-487a-a7c8-287bc8397ff1)

---
## [SM45H/f13babylon](https://github.com/SM45H/f13babylon)@[893e0e151c...](https://github.com/SM45H/f13babylon/commit/893e0e151c05648fd712f75e24520fc77354ed39)
#### Sunday 2023-12-24 20:12:20 by lolman360

robot update/rework (#204)

## About The Pull Request

does a lot of changes to robots
all changes TBD

robots are now much faster (0.3 slowdown instead of 1).
they are also somewhat tankier across the board to compensate for their
lack of armor (0 armor btw)

robot modules have been revisited:
medical assaultron was rolled into medical borg and is now an altskin.
mining borg now has a shovel, and its emag module is a rocketsledge that
mines better and has 12 less damage.
engiborg's emag module is also a rocketsledge (uncreative)
assaultron was rolled into secborg and is now an altskin.
vtec has been nerfed significantly from -1 slowdown to -0.25

gutsy flamethrower nerfed significantly: 1s firedelay, 33% lower
projectile count, actual energy cost

all robots now have the wastebot faction, since all selectable sprites
are fo13 robots anyways. this also makes slugs do 90 damage to them,
which is extremely funny and something i might remove. again, tbd



## Why It's Good For The Game

as long as they're pickable they should be functional

## Pre-Merge Checklist
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.


## Changelog

:cl:
add: new stuff to robots
del: old stuff from robots
tweak: robots can now patch nests
balance: robots are overall buffed (holy shit their slowdown was
dogshit)
/:cl:

---
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[247a4e02ea...](https://github.com/FalloutFalcon/Shiptest/commit/247a4e02eab24ccfa191ea0447e587aeaf4c1235)
#### Sunday 2023-12-24 20:35:38 by BluBerry016

{Icemoon, Ruin} The Crashed Holemaker (#2413)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a brand-new - well, [new to
shiptest](https://cohost.org/bluwu016/post/885120-a-compilation-of-my) -
ruin to the Icemoon roster, focused on the service department.

It's flavored around being an *incredibly* old NT Spaceworks vessel
that's been carved in half and crashed - what's present only being the
fore of the ship. Being mainly service-focused, it's loot is pretty dry
~~as is it's sole threat.~~
If more current-day mappers/balance-heads have any words about how to
fluff out either of those pools a bit more with the screenshots below,
lemme know. I'll listen well.

(Notarized loot summary removed as updating it was a pain in the ass,
lmao.)

It strikes me as leaning on the underwhelming side from looking at the
other ruins present here but we'll. See? I suppose? It's good practice
for me in the whole, "making something I have memorized and that looks
good normally look sicker ruined".

<details><summary>Pictures (All but SDMM Outdated)</summary>
<p>

Ignore that there's no rust, the firelocks are open here, and some
stuff's knocked around, I was testing it prior to me tacking the rust on
and took pics after running around it in-person.


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/51a3cc54-1727-4241-9592-639f892621bf)


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/580e39fe-bbf9-481f-aff8-cc25f860638d)

StrongDMM View:

![2023-11-09 15 02
20](https://github.com/shiptest-ss13/Shiptest/assets/50649185/5b94af63-d2d8-42bd-a823-0d300d66191f)

</p>
</details> 
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This isn't what I intended to do when I was like, "oh yeah, I have a
goofy ahh downstream out of boredom, ya'll want some of our better
ships" but w/e here it is anyways. Ya'll need ruins. I made (another)
ruin.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A new icemoon ruin has been added, should you be in need of service
department goodies.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: BluBerry016 <50649185+unit0016@users.noreply.github.com>

---
## [ac-frg/littlefs](https://github.com/ac-frg/littlefs)@[eb6c361dfa...](https://github.com/ac-frg/littlefs/commit/eb6c361dfa6ee2179679c8cf9098fb6dc74c930d)
#### Sunday 2023-12-24 20:38:44 by Christopher Haster

Adopted lazy orphaned mdir drops

This ended up being much less of a simplification than I hoped it would.

It's still easier/more efficient to revert to a relocation in most cases
when dropping in an mdir split, and the small gain from simplifying how
drops/commits interact is overshadowed by the code duplication necessary
to separate lfsr_mdir_drop out from lfsr_mdir_commit:

            code          stack
  before:  30952           2528
  after:   31280 (+1.1%)   2648 (+4.7%)

Still, this does at least simplify the logical corner cases (we don't
need to abort commits when droppable anymore), and lfsr_mdir_drop is
ultimately necessary for supporting lazy file creation.

Also having a fix-orphans step during mount allows other littlefs
implementations the option to create orphanned mdirs without compat
issues. So this ends up the more flexible approach.

It _might_ be worth having both eager mdir drops and an explicit
lfsr_mdir_drop for lazy file creation in the future, but I doubt this
will end up worth the code duplication...

---

Oh right, I forgot to actually describe this change.

This trades eager mdir drops:

1. Drop mdirs from the mtree immediately as soon as their weight goes
   to zero.

For lazy mdir drops:

1. Drop mdirs from the mtree in a second commit.
2. Scan and drop orphaned mdirs on the first write after mount.

This sounds very similar to the previous "deorphan" scan, which risked
an extreme performance cost during mount, but it should be noted this
orphan scan only needs to touch every mdir once. This makes it no worse
than the overhead of actually mounting the filesystem.

We can also keep an eye out for orphaned mdirs when we mount, so no
extra scan is needed unless there was an unlucky powerloss.

Eager mdir dropping sounds simpler, but thanks to deferred commits
introduces some subtle complexity around aborting commits that would
drop an mdir to zero. Remember commits are viewable on-disk as soon as a
commit completes.

In _theory_, lazy mdir drops simplify the logic around committing to
mdirs.

Though the real kicker is that lazy mdir drops are required for lazy file
creation.

The current idea for lazy file creation involves tracking mid-less
opened-but-not-yet-created files. These files can have bshrubs, so they
need space on an mdir somewhere. But they aren't actually created yet,
so they don't have an mid.

This is fine (though it's probably going to be tricky) as long as we
allocate an mid on file sync, but there is always a risk of losing power
with mdirs that contain only RAM-backed files. Fortunately, no-mids
means no orphaned files, but it does mean orphaned mdirs with no synced
contents.

Long story short, lazy mdir drops are currently a necessary evil, and
logical simplification, that unfortunately comes with some cost.

---
## [eilandert/inspect-http-requests](https://github.com/eilandert/inspect-http-requests)@[f5793369ec...](https://github.com/eilandert/inspect-http-requests/commit/f5793369ec3b4272c8db2f16b8ba508f34e41897)
#### Sunday 2023-12-24 20:42:09 by Thijs Eilander

Pr create ignore list (#16)

* change get_config to get_option

* sigh

* I hate myself & I want to die.

---
## [J-128/sodoff-j](https://github.com/J-128/sodoff-j)@[3272360259...](https://github.com/J-128/sodoff-j/commit/32723602599be7fc55de1c02587933b647c22da7)
#### Sunday 2023-12-24 20:43:30 by J-128

missiontext: correct "Skrill" to "Skrills"
context: Dagur: "We were out searching for Skrills to join the Berserkers when we came across her. We think she was trying to become friends with a Skrill at Glacier Island, but the Skrill was having none of it. No fault of our mystery dragon; Skrills just are very territorial!"

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e8cf56dcb2...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e8cf56dcb2553c842abd7adf60a99b33d65ecfbe)
#### Sunday 2023-12-24 21:06:28 by SkyratBot

[MIRROR] Roundstart AIs are positronic [MDB IGNORE] (#25679)

* Roundstart AIs are positronic (#80355)

## About The Pull Request

If you disassemble an AI which was in the round from the start it will
produce a Positronic Cube rather than an MMI with the brain of that
player's usual human character in it.

Also I made changes to a couple of feedback balloon alerts which would
always trigger a runtime when constructing or deconstructing an AI, this
was because balloon alerts have a small time delay before executing and
we deleted the AI mob or structure after trying to show a balloon alert
on them, so they'd never appear.

## Why It's Good For The Game

Honestly this is _mostly_ about vibes, it has annoyed me since AI
deconstruction was added that Nanotrasen AIs tend to actually be brains
in jars rather than AIs. Now they're artifical.
It does also mean that you can't deconstruct the AI and then put its
brain into a human body, which is similarly mostly bad because of vibes:
If you sign up as an AI I think you should be an AI or a cyborg even
after deconstruction.

It also universally looks really stupid when you deconstruct an AI and
it says it has the brain of Penelope Dreadful in there, like should I
expect them to start RPing as their normal character instead of the AI
they have been playing all round now?

## Changelog

:cl:
balance: Roundstart AIs are now made of positronic cubes, rather than
brains inside MMIs
/:cl:

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@ users.noreply.github.com>

* Roundstart AIs are positronic

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: John Willard <53777086+JohnFulpWillard@ users.noreply.github.com>

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[741558c9b2...](https://github.com/wrye-bash/wrye-bash/commit/741558c9b260e18509afad2f193dcaf3389ea2bb)
#### Sunday 2023-12-24 21:33:25 by MrD

312 Nightly:

Refix file duplicate for screens: RRR EEE try_rename for ModList

This was fixed again recently IIRC RRR - the problem (apart from regexes)
is we want to rename. This aligns the signatures of all except the
installers try_rename and fixes related pycharm warnings. Still WIP, due
to the weird screens rename logic - see old todos in there.

Move common logic to base:

 - we could eliminate all but IList overrides using unique_key?

Mopy/bash/bosh/__init__.py: The actual fix:

Traceback (most recent call last):
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\balt.py", line 1636, in __Execute
    menu.Append(menuItem)
    ^^^^^^^^^^^^^^
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\balt.py", line 515, in _conversation_wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\basher\files_links.py", line 144, in Execute
    self.window.RefreshUI(redraw=dests, detail_item=dests[-1])
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\balt.py", line 786, in RefreshUI
    self.PopulateItem(item=upd)
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\balt.py", line 730, in PopulateItem
    self.labels[col](self, item))
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\basher\__init__.py", line 3589, in <lambda>
    hitItem = self._getItemClicked(lb_dex_and_flags)
                                            ^^^^^^^^^
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\bolt.py", line 1632, in __getitem__
    return self._data[key]
           ~~~~~~~~~~^^^^^
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\bolt.py", line 679, in __getitem__
    return super().__getitem__(FName(k))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyError: FName('rt4 Copy')
python-BaseException

Interlude - WIP unify set_item_format for masters/mods list:

Where all the usual load order methods / modInfos fields appear in a
cameo - as promised in 8338cb9bebf91737e5d4bc9f08a201a16914b0bb.
Mouse texts will be rearranged a bit - should be a dict[str, int]
for priority - done later in this commit.

_set_color

I commented on the couple checks we don't need for masters - it's worth the
copy/paste removal

item_format.back_key

has_master_size_mismatch

- added `'Deactivate' in fileBashTags` for masters also

more unification

MasterInfo.getDirtyMessage:

- added also getDirtyMessage check for masters

So finally set_item_format moved to base - more work needed to display
more messages (those elif are evil) and convert messages to prioritized
dict but this will do for now - the goal was to reduce occurrences of
load order operations and modInfos info set accesses

_ListItemFormat.back_key property:

This should result in printing all the applicable mouse texts but setting
the highest priority background

ListItemFormat.text_key prop

336 - renames in the Inis hierarchies

AIniFile was really AIniInfo - the 'file' part is added in IniFileInfo
renamed also. I moved ADefaultIniInfo just below AIniInfo for easier
comparison.

Nit in _mergeability:

Remove the repeating verbose noise to make easier to follow (I am trying
to understand what load order info is needed for mergeability checks) at
the expense of *one* loacalized strings lookup before _exit() on
first failure (and short circuits). Made also some micro
optimizations/nit, in particular I  re-made plugin_inis to a dict to
save the dict creation in _mergeability and inlined now shorter
_is_mergeable_no_load

Passed the modInfos in to make the dependency explicit - we could attach
the ini to the modInfo - better solution but more tricky to implement

TTT Maybe fix incorrect directory move?

This makes OMOD extraction work on Linux, but I don't know if getting
rid of the .head there is actually correct or if it'll just break
something else. And while we're at it, does this need a _retry too?

Work around icon size crash RRR

Still no fix in sight for this - it seems to have worked for a while,
but now it's broken again. Work around this once and for all by
requesting a restart instead.

Ut:

It was easier to fix than to explain all the subtle ways this would
go wrong (if user unhides a button that was hidden in previous session
and button is created with updated icon size) - fixes status bar being
redrawed with updated (wrong) icon size if user chooses to not restart
after changing icon size. The assumption that icon sizes could be hot
switched was hardwired in the code so I had to hardwire the opposite.
Note BashStatusBar was in scope at least. This was a showstopper as
(not) discussed - thanks :)

This triggered some (final) refactoring of the status bar - turns out
we were performing a lot more refreshes than needed and in particular
we shouldn't bind the EVT_SIZE - maybe this was causing the crash?

Under RRR (there was an issue I think)

TTT does not seem removing this call entirely to cause problems on Windows?

Mopy/bash/basher/app_buttons.py: Guess this is the intended behavior?

Cleanup status bar text apis: TTT

We had:

- BashFrame.set_status_count used once in
- SashUIListPanel.SetStatusCount used twice - is the if needed in
ShowPanel too? TTT
- BashStatusBar.set_sb_text the real one (wraps _native), but why did it
call self.refresh_status_bar()? -> turns out we needed this on show_panel
- BashFrame.set_status_info, the API

This cures the flickering of the status bar buttons while not ellipsizing
the third sb field (item counts). The flickering was due to SetStatusWidths
that was only needed when the panel was shown. Not sure if we ever bypass
the ShowPanel call TTT - onSize was not needed here.

FFF statusBar.set_sb_text -> set_status_info

Stop binding the size event on the StatusBar: TTT

Turns out we don't need to reposition the buttons on a size event - wx is
doing this for us. Was this maybe the root cause of the crash on resizing
the buttons?

Hide TES4View/TES4Trans launchers when EXE missing

I don't have a TES4View.exe/TES4Trans.exe in my game folder, yet the
launchers were still shown since they bypass app_button_factory (and so
also bypass find_launcher). Could have tried making this work with
app_button_factory instead, but the comment seems to indicate that's not
an option?

Ut: this finally calls init for all app buttons via app_button_factory.
Now that the logic is spelled out clearly - does TES4Edit launched with
-translate/-view arguments start TES4Trans/TES4View? The API is not
expressive enough for this (joins with app_launcher) but can be extended -
or better wait till we obsolete app_key so the code becomes simpler
(we should use the uid for the images, should be unique :p, and rename
those again, duh - then simplify find_launcher by constructing the
paths in constants). Did not add keys to the ini as this is on its way
out. Also - do all the menu items apply to TES4View/Trans?Lod? TTT

If you find this method long you need to have a look at its first
iteration:

https://github.com/wrye-bash/wrye-bash/blob/2f0ace775218125e3c977b1b35258cb8810f1bcd/Mopy/bash/basher/links.py#L43-L584

:P

Co-authored-by: MrD <the.ubik@gmail.com>

Properly support high DPI images RRR

Turns out the high DPI image support introduced in # 557 <--- RRR had
some significant issues - most notably, it was rendering crisp high-res
images, but wx then decided to upscale them *again* if your DPI scaling
was set to 200%.

To fix this, we need to move to wx.BitmapBundle. This is intended to be
used by bundling multiple versions of the asset and sticking them all
into a bundle, then having wx choose the most appropriate resolution. Or
use an SVG, statically render a bunch of sizes and stick them all in a
bundle. We don't do that and instead dynamically create them, sticking
only a base resolution asset and the actual version we need in. That way
wx will use the higher-resolution version without applying its own
scaling. This does of course look ugly with checkboxes and such, but
those are temporary anyway - # 511 <--- RRR will replace them with SVGs.

Note that we now pass in iconSize for (nearly?) everything, so maybe we
should just make it a required parameter.

Under # 511, # 557 <--- RRR

SSS Small addition for SSE update support

The nextObject default needs to change as well, of course.

SSS Fix edge case when shortcut has custom icon

Would fail when calling exists() on it afterwards since it was a
string, not a Path.

Note also that shortcuts still have messed up icon sizes (at least on my
high DPI monitor), but that's purely cosmetic and so can wait until 313.

FO3: Fix Sort: Armor/Clothes regression

Broke in b866822b54497914190faf0c5aad9c9442053809.

FO3: Add handling of 4-byte QUST\DATA subrecord

Apparently only the float can be cut off as well, as seen in the
Updated Unofficial Fallout 3 Patch, v3.3.3.

SSS Fix slight cosmetic regression

Would show the 'Another plugin has the same timestamp' text twice.

Another cosmetic regression

Invalid packages would no longer get the grey invalid text color.

FNV: Update condition_function_data

Couple new functions. Fixes the BP failing on Ammo Script Fixes.

Mark CELL\DATA subrecord as required

It's required in xEdit. DynDOLOD removes it, however, so we have to add
it back or risk getting slapped with

  AttributeError: 'NoneType' object has no attribute 'isInterior'

Note that my inf-480-525-fo4-records-pt11 branch has a lot of work on
required subrecords, but work on it won't resume until 313 development
begins, for obvious reasons.

Disable expanded ESL range for Enderal SE & TES5VR RRR

Follow-up to bb3df381d95061e036cfb7f554bc60bdf90e3743. We will want to
undo these changes once we tackle # 673 <--- RRR.

Move 'run' code to env; make get_file_version work on Linux

    Moves run_exe to env wrappers and makes it return a Popen reference
we can access from within app_buttons or wherever else a subprocess is called.

    Reimplements get_file_version to use native binary reading utilities on Linux. It Just Works!

    Refines Java detection a bit.

fix @set_cwd discarding function return value

    @set_cwd would cause the annotated function to discard its return
value. Keep whatever the original function returns as a local variable
and return that after os.chdir().

    Removed non-functional get_file_version method.

    Added some type hints and comments.

SSS Some minor followup fixes for Linux

- Prefer JAVA_HOME if set
- Skip 0.0.0.0 and 1.0.0.0 versions to match the Windows version
- Fix reading of xSE versions (uses commas and spaces instead of dots)
- Get rid of u'' prefixes and use f-strings

Add some quick partial form hacks

xEdit has added some support for them and DynDOLOD is already using
them. Just skip them from consideration in the BP entirely for now,
since most of these are going to be 100% empty anyways and only used to
add/override children. We will eventually have to go back and implement
them properly, since they *can* override some data, but this will do for
312.

Left PARTIAL_FORM_HACK comments so we can easily track these hacks down.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[84cb3caf94...](https://github.com/wrye-bash/wrye-bash/commit/84cb3caf943c053dd85166af184cc56b71ebe1cb)
#### Sunday 2023-12-24 21:33:25 by MrD

Squashed version of ut-353-pt1-578:

Refactoring in load order:

Move  the logic of _filter_active in callers - they were doing the checks
anyways - then inline - we certainly want to thin LoGame API, _games_lo
is complex enough and flat is better (and shorter) than nested here.

_CleanPlugins(LoGame):

Clean/create logic is very hard to follow - let's confine it to games that
need it. We then need to clarify what happens with cached parameters vs
creating the plugins txt - AsteriskGame._fetch_load_order logic is still
hard to follow see todos added there.

EAFP for parsing mod file

Then I realized that since 96394dda9179188825cc184ea84d689bda667824
actually for Textfile games we only need to remove the master_path,
so _active_entries_to_remove is only needed in AsteriskGame - then
_clean_actives, which for Asterisk necessarily cleans
the whole plugins.txt, is inlined taking down tricky logic and lots
of comments trying to explain what goes on.

Oh lord_func:

I. Use the return value:

This necessitated returning from _update_cache -> refresh_lo (single
use). For now I return the cached_lord - this is temporary, we will
eventually confine cached_lord to load_order.py, but we need to forge
a ring for that - that's part II.

quiet WIP:

get_load_order had quiet=False effectively - added this as default to
fix_load/active and then in set_load_order quiet=True and set it only
in load_order.save_lo

Became clear that warn_missing_lo_act was only updated when quiet was
False which was when lo_deprint was called. This simplified the bolts
of _game_lo at the expense of a local modInfos import - nice.

The timestamp game _fix_load_order override was tricky to get - if fix_lo
was None, which only happened in _restore_lo (quiet=True and
set_load_order validation) and in refresh_lo (for validation of a saved
load order), it would not reorder the added plugins but add them to the
end - I kept that but dropped the debug message as anyway the lo_added
will be printed. What we should do when a plugin is added needs
standardizing - makes sense to add them at the end so saves show blue.

Mopy/bash/basher/__init__.py: nit, better reset a dialog trigger before
showing the dialog lest one falleth into an infinite loop.

Expose more LoadOrder attributes:

The index dicts contain all the info of load order/active changes - as
a bonus a couple one-line, one-use methods were removed. load_order.py
is the balt of load order handling and although (because of saved load
order handling) it does have a well defined role it still needs to be
kept at a minimum - more on this later.

Simplify/optimize _refresh_mod_inis:

No need to clean up since we overwrite at the end - pruned also the OD.

Only the values of _plugin_inis was used - this will re-become a dict
but for now simplify and make easier to track by exposing it and
removing essentially nothing-new ini_files (not the ini_files.py
module).

WIP refactor BP activations handling:

count would decide on refreshing saves - probably if any mods got
activated we should DO. Moved the info handling higher up, I need to do
activations in parent.

Reduce occurrences of lo_activate (2)/cached_lo_save_active (1) - these
must be further confined. Note the decoupling from load_order (and Link)
in patcher_dialog.py

_modTimesChange -> unlock_lo - mod redates fix:

Was unlocking in all except one case - in those cases unlocking made
only sense if the game was a timestamp game - I am glad I kept
_modTimesChange and gladder I dropped it

Needs some testing as there are subtle changes in the logic - note that:

mod_links.py: we wouldn't unlock. That was actually a bug (if lock load
order was on) as the redates would silently be reverted in refresh_lo
(with no change shown in the UI) and then a dialog would be displayed on
*next time* we would tab in to Bash (still no change in the UI).
That was probably not the intention :P

Mopy/bash/basher/app_buttons.py: while we did unlock always we did not
forceRefresh - well it's a couple stats() added, won't harm

The rest is fine - just one more use of using_txt_file, inside the same
(DoSave) scope - good sign.

Mopy/bash/basher/installers_links.py: the (not so) long term goal is to
absorb this into refresh - need to refactor base signature for this.

WIP setGhost return status change: RRR TTT drop notify bain?

This gets us rid of a few uglyStuff including a Path method (# RRR 368), and
one bare except - we might as well deprint out (and maybe tighten the
remaining except).

As seen in _refresh_from_data_dir we chop off the ghost extension so we
should not notify BAIN TTT cause data_sizeCrcDate is difficult to track,
hence WIP see next commit

Under # RRR 219

isGhost -> is_ghost:

Now that autoGhost is (will) be gone

Some nit - in particular no need to create these (None, None, None) tuples

Drop _reset_info_sets: TTT EEE Mopy/bash/basher/files_links.py

Finally, this set up was a smell. This makes some calls like new_info
more expensive but no worries

TTT new_info: the _in_refresh param is obviously a temp hack :P

WIP decide what we need to refresh in restore backup:

This is partial (new_info is the hardest to absorb in refresh from the
refresh satellites). No need to further dig in there - refresh will see
an overhaul soon.

Sort by master status once in _fix_load_order: EEE drop allow_deactivate_master?

Trying to make complex less complicated here - comments included. This
permitted inlining _index_of_first_esp - IIUC we just needed to calculate
once and then increment. So one function and 2 uses of in_master_block
down - neat.

More undead pruning: RRR

Including one more modInfos local import - typing is badly needed here

Mopy/bash/gui/popups.py: user_ok was essentially unused, was checked in
show_modal - while quietly doing RRR

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[2d89babc8a...](https://github.com/lessthnthree/effigy-se/commit/2d89babc8a5e3de936e16aacd6804c29bb08d61f)
#### Sunday 2023-12-24 21:36:28 by distributivgesetz

Delamination variants are now locked in after the countdown is reached (#80324)

## About The Pull Request

Does what it says on the tin.
## Why It's Good For The Game

This effectively changes one and only one thing: 

The "All Within Theoretical Limits" achievement is easier/fairer to get
with this. Previously, if you edged a crystal with the gas composition
method to get a resonance cascade, you had to make sure that your gas
composition stayed until it left the explosion point, which made the
achievement extremely finnicky and unfun to get this way. Regular
delaminations won't really be affected, because yeah. It's at the
explosion point. What are you going to do about it?

This makes the achievement easier to cheese, but honestly, in my opinion
as person who added the achievement, meh. If people feel like this isn't
good for the achievement, say something in the comments.

Closes #79528

## Changelog
:cl:
balance: Delamination variants no longer change once the explosion point
has been reached.
/:cl:

---
## [Blad3sy/Advent-of-Code](https://github.com/Blad3sy/Advent-of-Code)@[e9913e4314...](https://github.com/Blad3sy/Advent-of-Code/commit/e9913e43141736ac701ba693df76e1172e29f069)
#### Sunday 2023-12-24 22:12:12 by Blad3sy

Completed Day 24

I don't feel... even remotely good about this one.

Part 1 was easy simultaneous equation maths, but I forgot about time and input about 4 wrong answers before remembering to check if the collision occurred before the start point!

Part 2 was essentially cheating using a library called z3, but you can read about my opinions on that in the actual file.

Here's to hoping Day 25 is less of a shitshow, and actually satisfying and fun to complete.

---
## [Grifthegnome/OutlawMod](https://github.com/Grifthegnome/OutlawMod)@[beaa0abf86...](https://github.com/Grifthegnome/OutlawMod/commit/beaa0abf8639412a8921d39650ff57f4621c73da)
#### Sunday 2023-12-24 22:26:22 by Grifthegnome

Added AiTaskReactToProjectiles, Fixed Morale Bug, Changed AiTaskStayCloseToHerd to take combat into account, AI LKP improvements. ManagedEntityArray Class.

AiTaskReactToProjectiles
1. AI With this task will aggro to an entity that shot a projectile when that projectile passes near them. This makes them look smarter and more responsive when they ecounter near misses.
2. I had to write an entity manager system to track all projectiles, as WalkInteractveEntities no longer tracks EntityProjectiles or EntityItems.
3. Currently this tracks all protiles in one pool, but we should really distinguish between projectiles in flight and ones that have landed.

Fixed Morale Bug
1. Fixed a bug where an if statement was checking AI Awareness incorrectly.

AITaskStayCloseToHeard Now Accounts For Combat
1.When an AI looks for a new herd master, it will prioritize herd members that are in combat.

Improved Lask Known Position
1. Added "attackEntity" notification that is caught by AiTaskShootProjectileAtEntity and AiTaskPersueAndEngageEntity. This sets the last known positon for these behaviors based on events the AI percieve, such as a passing arrow or an friendly who gets killed, this allows the AI to react much more dynamically as a group and seek out the source of an attack.
2. The result is that the AI push players much more agressively.

ManagedEntityArray Class
1. This is a self compacting array class that does not allow sparse entries.
2. Any time its contents are gotten or counted it removes all null entires.
3. This is an ideal structure for tracking Entities that frequently become invalid at runtime.

---
## [RypoFalem/crawl](https://github.com/RypoFalem/crawl)@[dffb6e3712...](https://github.com/RypoFalem/crawl/commit/dffb6e3712f7bc9ff45b6ae244928f1d806afe75)
#### Sunday 2023-12-24 22:46:02 by regret-index

Brain Feed -> Brain Bite (minor damage + mp drain, no int drain)

Brain Feed is an extremely weird monster spell in most games. With so
little stat drain around by default in a three-rune game, individual hits
against a stat approach 0 extremely rarely unless a player has next to
none, which is influenced heavily by character start combo and very little
by normal character growth. The relatively minor hit of intelligence also
does very little for its use on higher Int characters aside from slightly
worsening spell success rates, which works weirdly against the flavour of
various brain-eating monsters not actually caring about the quality of
brain so much as just killing those with incidentally little of it.

It's kind of difficult to tell what this spell should do. It'd be entirely
possible to make it drain a lot more intelligence or percentage-based +
flat intelligence to make actually effect more characters, but while
strategic damage of a restorable sort would be more mechanical diversity,
screwing with spell success chances and non-tangible damage rolls aren't
mechanics we've kept to the present day (c.f. skilldrain, old sap magic).
So, I'm sidestepping the original effect of the spell entirely, while
focusing still on its theme.

Brain Feed is now revised into Brain Bite, a mildly-experimental mix of half
a Smite plus a percentile version of Draining Gaze- 4-8 irresistable direct
damage doubled if you have no mp, then draining 20% of one's max mp (rounded
down). (This now also works on monsters, dealing damage checking on antimagic
and then applying antimagic.) The percentage part lets it scale across the
game (compared to Draining Gaze rapidly heavily draining most player mp), and
irresistable but restrained damage sources are currently pretty reserved
designs (Smiting, Damnation, usually Torment) that could be iterated further
upon.

(It'd be good to think over what the point of statdrain even is outside
of Hell, Tomb, and klown pies. Possibly a variant of flaying but only
for stats would be interesting, possibly making an even shorter para but
with brief stat-zero would be an interesting revision of current para.
This is kind of out of this particular commit's scope, though- getting
to stat zero via Brain Feed didn't really happen for a very large number
of character combinations, so concerns over that are minimal.)

Tile update uses the old mimic teeth tile by coolio, modified by jpeg,
on top of the current Brain Feed icon by snw-0.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[0a097184f4...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/0a097184f4770600ed32ce4cc3646075bbfc2492)
#### Sunday 2023-12-24 22:50:21 by John Willard

PDA update (Messenger works while dead, Microwave works, etc). (#80069)

This is an update that touches many more things all at once (compared to
my other PRs) meant to make PDAs in general feel more consistent and not
take away from one of the experiences we want to encourage: interaction
between players.

1. Replaced all checks of a 'pda' with a 'modular pc'. This means
technically (though not done in-game currently) other modpcs can hold an
uplink, and microwaves can charge laptops.
2. Speaking of microwave, they now don't break and require
deconstruction if the cell is removed mid-charge.
3. When a Mod PC is out of power, it will now allow the Messenger to
work (which now also doesn't consume any additional power), if the app
exists on the PC. Here's a video demonstration

https://github.com/tgstation/tgstation/assets/53777086/7ae12f81-a271-49b8-95fa-2ba54d2e2d1f

4. Flashlights can't be turned on while the cell is dead
5. I replaced a bunch of program vars with ``program_flags`` and renamed
``usage_flags`` to ``can_run_on_flags``.
6. Added a debug modPC that has every app installed by default. Mafia
had some issues in the past that were unknown because Mafia wasn't
preinstalled with any tablet so was never in create & destroy nor in any
other unit test. This was just an easy solution I had, but PDAs should
get more in-depth unit tests in the future for running apps n stuff- I
just wanted to make sure no other apps were broken/harddeling.

Currently when a PDA dies, its only use is to reply to PDA messages sent
to you, since you can still reply to them. Instead of just fixing it and
telling players to cope, I thought it would be nice to allow PDA
Messenger to still work, as it is a vital app.
You can call it some emergency power mode or whatever, I don't really
mind the reason behind why it is this way.

When I made cells used more on PDAs, my main goal was to encourage
upgrading your PDA and/or limiting how many apps you use at once, I did
not want this to hit on players who use it as a form of interaction.
This is the best of both worlds, I think.

The rest of the changes is just for modularity, if some downstream wants
to add tablets, phone computers, or whatever the hell else, they can
still get just as far as PDAs should be able to get to, hopefully.

:cl:
add: PDAs with a dead power cell are now limited to using their
Messenger app.
fix: Microwaves now stop charging PDAs if the cell was removed
mid-charge.
fix: Microwaves can now charge laptops.
fix: PDA Flashlights can't be turned on while the PDA is dead.
fix: You can now hold a laptop up to a camera (if it has a notekeeper
app installed) like PDAs already could.
/:cl:

---------

Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [elunna/HACKEM-MUCHE](https://github.com/elunna/HACKEM-MUCHE)@[6e9ccd66d7...](https://github.com/elunna/HACKEM-MUCHE/commit/6e9ccd66d7fd3498f3d4f4787c109c4625a394db)
#### Sunday 2023-12-24 23:05:10 by Erik Lunna

Ported forges and lava demons from EvilHack.

Currently the implementation mirrors that of EvilHack except for the #forge command. I am leaving that out because I want the simplest version of this feature as possible. Forges let the player repair metallic armor, bless items, dispose of zombies or organic items, dispose of the iron ball and chain, and summon lava demons and fire elementals. The actual forging mechanics complicate matters more than I want and introduce a new command. I'm also not sure how to balance out the forging recipes, what to allow, what quantities make sense, and etc etc etc - so I'm just going to bypass it. The core features of the forge are fantastic and I think we can actually add a couple more subtle ones to really make them shine.

---
## [K9100ii/android_hardware_samsung_slsi-linaro_exynos5](https://github.com/K9100ii/android_hardware_samsung_slsi-linaro_exynos5)@[9086120d26...](https://github.com/K9100ii/android_hardware_samsung_slsi-linaro_exynos5/commit/9086120d26bc3d161d365122b9c0dfd36e9c8503)
#### Sunday 2023-12-24 23:19:59 by K9100ii

exynos5: Switch to a new versioned path and BSP variant setting

Copy-paste explanation:

There are two sets of BSP sources - These new ones intended for Android
13, and older ones originally intended for Android 10. The older ones
have support for some legacy things like HWC1 for older devices, and
the newer ones have support for newer things like gralloc4.

To keep support for older devices going, I want to keep the older
sources alongside the newer ones. But they can't co-exist as-is. Some
changes are needed:
 - a change of paths to the BSP sources, which are referenced directly
   within them
 - a new BSP variant setting ('TARGET_SLSI_VARIANT' flag)
 - and finally, some soong namespacing.

The BSP variant setting and paths are the biggest challenge. For the
existing BSP sources, there's absolutely no versioning. It's the same
old generic "linaro"/"samsung_slsi-linaro" for both sets of BSP sources.
Sadly, my expressions of concern for my life to not be made more hellish
were quite badly dismissed, all the while I'd think it would be best
practice to version things like this to not keep using the same old
generic identifiers and not run into issues (or for others to not do so)
later, so I'm on my own to figure out what to do here.

My solution that touches the least I can is as follows:

For Android 13 - The older Android 10 BSP sources are typically used,
and since I'd like to use 13 sources as I have a device that requires
gralloc4, I need to make changes within them.
To manage it, the naming is as follows:
  Directory for 10 sources - 'samsung_slsi-linaro'
  Directory for 13 sources - 'samsung_slsi-linaro_13-e850-96'
  Git branch name for 10 sources - '...'
  Git branch name for 13 sources - '..._13-e850-96'
  SLSI variant flag setting for 10 sources - 'linaro'
  SLSI variant flag setting for 13 sources - 'linaro_13-e850-96'
The only changes here are for 13 sources. Naming is left untouched for
10 sources so as to not break anything for trees using them currently.

For Android 14+ - I'd want to preserve support for older devices,
provided if, and hoping that, running newer Android versions doesn't
become an impossibility for them, so, while the newer Android 13 BSP
sources are typically used, I'd have to make changes to the 10 sources
to keep them alongside.
To manage it, the naming will be as follows:
  Directory for 10 sources - 'samsung_slsi-linaro_10-e850-96'
  Directory for 13 sources - 'samsung_slsi-linaro'
  Git branch name for 10 sources - '..._10-e850-96'
  Git branch name for 13 sources -  '...' / '..._13-e850-96'
  SLSI variant flag setting for 10 sources - 'linaro_10-e850-96'
  SLSI variant flag setting for 13 sources - 'linaro'
The directory and variant flag setting will be untouched for 13 sources,
so as to stay in line with everyone else, and changes would only need to
be made within 10 sources. However, for consistency, there will always
be versioned git branches in future, alongside non-versioned ones with
whichever sources are typically used, though this all remains less than
ideal in any case.

Lastly, soong namespacing is added specifically for the "exynos" and
"graphics" parts of the sources. Without, there are conflicts between
the two sets of sources. For all devices, BoardConfigCommon.mk in the
collection of BSP configs is included, and namespaces can be added
there, and also the SLSI variant flag setting can be changed, for a
clean result where no changes are required in device trees at all.

Change-Id: I07b1aaf4c3d378e77dec2a137acb79c82a336374

---
## [RobinTail/express-zod-api](https://github.com/RobinTail/express-zod-api)@[9e6743b836...](https://github.com/RobinTail/express-zod-api/commit/9e6743b83623915823be234e2617f19eb38573b7)
#### Sunday 2023-12-24 23:26:45 by Anna Bocharova

`v16` is for Nina (#1386)

# Dedication


![image](https://github.com/RobinTail/express-zod-api/assets/13189514/b2c99e20-2727-43a3-bf76-2f718562f94c)

In year 2019, Nina Surgutskaya was 25 years young, when she was killed,
dismembered, and partially cooked by her boyfriend Mikhail Tikhonov, who
was a doctor by the way, in Kursk, western Russia. He became angry upon
learning that she was assigned male at birth, which was his motivation
for the crime. He also flushed some of Nina's body parts down the
toilet, and put her limbs and head in a suitcase.


https://www.dailymail.co.uk/news/article-6949841/Russian-doctor-murders-dismembers-cooks-transgender-woman.html?ito=social-twitter_mailonline

Transgender women suffer too frequently from transphobic violence and
cruelty, being the less protected social group. I'd like to raise an
awareness of this problem. Humans should be creators — not killers. But
most importantly, I want every transgender girl to have an opportunity
to create applications quickly and, in general, learn to write code
easily in order to receive job offers and leave dangerously transphobic
territories for more favorable and civilized ones, and live happily
there. Protect transgender women.

# Description

Featuring OpenAPI 3.1 for better Documentation and formatted code of
frontend client produced by Integration (using `prettier` or user
defined function). Additional setting for generating types in
Integration.

- #1382 
  - partially reverted, class remains, method remains
- #1385 
  - partially reverted, class remains, dependency remains
- #1387 
- #1391 
- #1412 
- #1415 
- #1416

---
## [NonQueueingMatt/Aurora.3](https://github.com/NonQueueingMatt/Aurora.3)@[bc66a212d7...](https://github.com/NonQueueingMatt/Aurora.3/commit/bc66a212d771eef33ae88445ebe4462ee25bde17)
#### Sunday 2023-12-24 23:35:03 by RustingWithYou

Hephaestus Security Ship & Corporate Voidsuit Tweaks (#17962)

* hephaestus security ship

* fuck off

* welcome mesgaes

* lattice hell

* damn you kaizr

* cabinet

---

