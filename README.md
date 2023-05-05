## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-04](docs/good-messages/2023/2023-05-04.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,220,458 were push events containing 3,707,068 commit messages that amount to 251,725,264 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 57 messages:


## [matts1/rules_rust](https://github.com/matts1/rules_rust)@[80f0eb488a...](https://github.com/matts1/rules_rust/commit/80f0eb488ab9cabc4920ac446478cbf2feedc3f3)
#### Thursday 2023-05-04 00:00:06 by scentini

Support for `no_std` mode (#1934)

Initial support for `no_std` mode.
This allows us to
1. Don't pass the whole standard library to compile actions that specify `no_std`
2. Conditionally select `crate_features` and `deps` based on whether `no_std` mode is used.
Currently the only supported modes are `off` and `alloc`, with a possibility to expand in the future.

The `no_std` support comes with the following caveats:
1. Targets in `exec` mode are still built with `std`; the logic here being that if a device has enough space to run bazel and rustc, std's presence would not be a problem. This also saves some additional transitions on `proc_macro`s (they need `std`), as they are built in `exec` mode.
2. Tests are still built with `std`, as `libtest` depends on `libstd`

There is quite an ugly hack to make us be able to `select` on the `no_std` flavor taking `exec` into account; I'm looking forward to the day where Bazel will expose better ways to inspect the cfg.

There is also one part I didn't manage to make work - having a `rust_test` that tests the `rust_shared_library` in `cc_common.link` mode; I got a link error for missing `__rg_alloc` & co. symbols, which should be present as we pass `--@rules_rust//rust/settings:experimental_use_global_allocator=True`. Unfortunately I could only spot this error on CI, and could not reproduce locally. I removed the test because the `rust_shared_library` is already tested via a `cc_test`. I will however give another shot at inspecting how my local setup differs from CI.

The `rust_binary` source code in `main.rs` was borrowed from https://github.com/jfarrell468/no_std_examples, big thanks to @jfarrell468 for letting me use it.

Co-authored-by: Krasimir Georgiev <krasimir@google.com>
Co-authored-by: UebelAndre <github@uebelandre.com>

---
## [mattmanj17-forks/terminal](https://github.com/mattmanj17-forks/terminal)@[ae7595b8e1...](https://github.com/mattmanj17-forks/terminal/commit/ae7595b8e13d4764f4db7b4060eaf57d1b4ee82e)
#### Thursday 2023-05-04 00:08:20 by Mike Griese

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
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[3ecc9f859d...](https://github.com/lessthnthree/Skyrat-tg/commit/3ecc9f859dfc0f870500d717e382d52662667996)
#### Thursday 2023-05-04 00:16:23 by SkyratBot

[MIRROR] Allows Export of your Preferences JSON File [MDB IGNORE] (#20894)

* Allows Export of your Preferences JSON File (#75014)

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

* Allows Export of your Preferences JSON File

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[96676cc94e...](https://github.com/lessthnthree/Skyrat-tg/commit/96676cc94e9ab363e8350644a58449af11b614a7)
#### Thursday 2023-05-04 00:16:23 by SkyratBot

[MIRROR] Gunpoints now take half a second to activate, make gasp sounds, and briefly immobilize the shooter and target, other small balance changes [MDB IGNORE] (#20882)

* Gunpoints now take half a second to activate, make gasp sounds, and briefly immobilize the shooter and target, other small balance changes (#74036)

## About The Pull Request
This PR messes around with gunpoints a bit, with the purpose of making
them more viable in certain scenarios without making them obnoxious. The
biggest change is that gunpoints now require a 0.5 second do_after()
where neither the shooter nor the target moves, and immobilizes both of
them for 0.75 seconds if point blank, or half that if you're 2 tiles
away. Originally you were supposed to only be able to initiate a
gunpoint from point-blank, but #56601 seems to have removed that
requirement, so we'll run with it and just leave it as advantageous to
gunpoint closer up. The do_after() reinforces that it should be used as
an ambush tactic, and so you can't use it on someone who's actively
fleeing or fighting you.

Getting held up will now make you emit a shocked gasp sound, a la Metal
Gear Solid, which combined with the short immobilize will hopefully make
it more noticeable that someone's pointing a gun at you.

Holdups will now immediately give a 25% bonus to damage and wounds,
instead of having to wait 2.5 seconds to hit the double damage stage.

Finally, right clicking someone that you're holding up will no longer
shoot them. That just feels like good consistency.

## Why It's Good For The Game
Hopefully makes gunpoints a little more viable for when you want to
stick someone who's not expecting it up without them immediately jetting
off. In the future I'd like to ape Baycode and let the gunman have an
action that toggles whether the victim is allowed to move, so you can
order them to move to a second location without instantly shooting them,
but that'll come later.
## Changelog
:cl: Ryll/Shaps
balance: Holding someone at gunpoint now requires both the shooter and
the victim to hold still for half a second before activating, so you
can't hold-up people fleeing or fighting you. After that, it will
briefly immobilize the both of you, 0.75 seconds if adjacent, or half
that if you're two tiles away. Nuke ops are immune to the
immobilization, since they're ready to die anyways.
balance: Holding someone up will immediately apply a 1.25x damage and
wound multiplier, rather than waiting 2.5 seconds to hit 2x.
soundadd: Being held up will now make the victim play a sharp gasp
sound, a la Metal Gear Solid.
qol: Trying to hold someone up that you're already holding up will no
longer shoot them.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Gunpoints now take half a second to activate, make gasp sounds, and briefly immobilize the shooter and target, other small balance changes

---------

Co-authored-by: Ryll Ryll <3589655+Ryll-Ryll@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[1b5c0489a4...](https://github.com/norsvenska/tgstation/commit/1b5c0489a4088dca925ab061a389d95005c95820)
#### Thursday 2023-05-04 00:21:38 by san7890

`ex_act()` will work on basic mobs again (lol) + Unit Test (#74953)

basically ex_act's implementation on basic mobs would call parent and
then react to it's value, this is presumably to do the first check about
space vine mutations and whatever. the problem is that the `/mob/living`
implementation would itself also call parent, and that would always
return null because `/atom/proc/ex_act` doesn't have a set return value.
So, this simply would _always_ early return, with ex_act presumably
*never* working on basic mobs for at least four months now.

I decided to then change up the return values for pretty much all
implementations of `ex_act()` since there was no rhyme or reason to
returning null/FALSE/TRUE, and documenting why it's like that.

Just to make sure I wasn't breaking anything doing this (at least on
base implementations), I wrote a unit test for all of the three major
physical types in game (objs, mobs, turfs) because i am a paranoid
fuckar. we should be good to go now though.
## Why It's Good For The Game

i noticed this because placing c4's on sargeant araneus wouldn't
actually damage it whatsoever. now it actually does the stated 30
damage, but araneus has like 250 health so it doesn't actually matter in
the long run. whatever at least it does the damn 30 now.

also adds a unit test for this specific case as well as a range of other
cases to ensure this stuff doesn't silently break in this way anymore

---
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[9c0900bc9f...](https://github.com/norsvenska/tgstation/commit/9c0900bc9f53d4de402df5528c181bee757d03cb)
#### Thursday 2023-05-04 00:21:38 by Wallem

Adds the Death Sandwich to the game (#75013)

## About The Pull Request
Adds the Death Sandwich to the game, the ultimate form of
bread-conveyed-meat-based consumables.

![deathsandwich](https://user-images.githubusercontent.com/66052067/235041733-287be1fd-1eed-4d6d-840b-96f95494f093.png)


And remember;
Eat it right, or you die!
## Why It's Good For The Game
I'm genuinely surprised we don't already have a meatball sub in the game
also I love humor food, and I doubt my edition of the Eggcellent
Challenge would ever be merged if I tried to do so, so this is the next
best thing.
## Changelog
:cl: Wallem
add: The ancient recipe for the Death Sandwich has been rediscovered
buried in the deepest depths of an erupting volcano.
/:cl:

---
## [TOBKA4/cmss13](https://github.com/TOBKA4/cmss13)@[b451aba2d4...](https://github.com/TOBKA4/cmss13/commit/b451aba2d4fd87a3b5cceaaba6955b8b783f84b2)
#### Thursday 2023-05-04 00:26:30 by Hopekz

Fix a start now error and add the ability of queuing the start of the game (#3090)

This PR does two things.

Fixes this error when trying to start early

![dreamseeker_lIUnkd0lFZ](https://user-images.githubusercontent.com/24533979/232609965-5cf94825-0671-420b-8625-16f505f26d63.png)


And adds queuing meaning that if an admin wants to start a game early
during loading; it will now tell them that the game will launch as soon
as it is available then waits for the game to be ready before starting.

Before this PR it just tells you that the game isn't ready then you have
to wait for it to load and launch the "start now" command again.

Does not bypass the "are you sure?" check because it has been moved to
the front.

Honestly made this PR because I hate waiting for the start I just want
to do it once when I see the game window then step away for like a
minute instead of having to wait for it.


:cl: Hopek
add: Adds the support for queuing the round start meaning that if an
admin pressed "start now" it will actually wait until the game is loaded
then immediately start the game as expected versus telling you to try
later.
fix: fixed the "start now" verb displaying that the game has already
started when it is loading because it didn't understand how to read the
game state properly.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [pulsar-edit/pulsar](https://github.com/pulsar-edit/pulsar)@[71d4ad1d07...](https://github.com/pulsar-edit/pulsar/commit/71d4ad1d076f097a5a53a107209ccc3f332954e7)
#### Thursday 2023-05-04 00:33:09 by Andrew Dupont

Restore `core.useTreeSitterParsers` setting…

…along with a temporary `core.useExperimentalModernTreeSitter` setting.

If we truly planned to keep three different language modes around indefinitely,
changing `core.useTreeSitterParsers` to an enum would make sense. But we don't,
so it'd actually just be a gigantic pain in the ass to migrate one setting to
another of a different type.

When we ship modern-tree-sitter experimentally, we'll make it opt-in via the
temporary setting. When we make it the official tree-sitter implementation and
remove the legacy node-tree-sitter version, we'll remove the temporary setting
and just change the semantics around `core.useTreeSitterParsers`.

Reverting the addition of the `core.languageParser` setting is a chore, but it
prevents a _gigantic_ future headache.

---
## [saltwaterterrapin/EvilHack](https://github.com/saltwaterterrapin/EvilHack)@[56b756dbb5...](https://github.com/saltwaterterrapin/EvilHack/commit/56b756dbb5f7da4ea91f799b9971f78995f5eeb7)
#### Thursday 2023-05-04 00:33:49 by k21971

More Drow abilities, strengths and weaknesses.

This commit basically revolves around how the Drow race operates in the
dark, or in the absence of it (light). I've also added a new trinsic
ability. Details are as follows:

* Drow take a flat -3 to-hit penalty when fighting in a lit area. But if
shrouded in darkness, they get a bonus to-hit: (u.ulevel / 3) + 2. This
equates to a +2 to-hit bonus at experience level one, and scales all the
way up to around a +15 to-hit bonus at experience level 30 (same scale
that Monks enjoy if fighting bare-handed using martial arts skill).
* Drow will heal more slowly while in a lit area. If shrouded in
darkness, the natural heal rate goes back to normal
* (Not Drow specific) some tweaks to thievery skill were made, and being
in darkness now gives the Rogue some actual benefit (moreso if that
Rogue is Drow).
* Ultravision - infravision allows the player to see a monster in the
dark, but only if that monster is infravisible. Ultravision allows
monsters to be seen in the dark no matter what. Drow inherently have
this ability, as do any drow-analogue monsters. I may confer this
ability to other monsters, need to go through my old ad&d monster
manuals and see what's appropriate
* Drow are not infravisible (that carried over from the elf template I
used in an earlier commit)

Drow race is starting to come together. Still a lot to do, but we're
getting there.

---
## [GribbaG/Nautical-Voyage-3](https://github.com/GribbaG/Nautical-Voyage-3)@[ec577988c0...](https://github.com/GribbaG/Nautical-Voyage-3/commit/ec577988c077c80f35d9c70b8447deb141669b9a)
#### Thursday 2023-05-04 01:13:26 by GribbaG

fuck you kyle

added some stuff like up and down and something else idk. fuck u tho kyle

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[3012809701...](https://github.com/diphons/D8G_Kernel_oxygen/commit/301280970134ca7d2724b366cf2b95b1894a4b1b)
#### Thursday 2023-05-04 02:20:54 by Wang Han

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

---
## [filiphsps/Metro-Compose](https://github.com/filiphsps/Metro-Compose)@[2f8de6fd4e...](https://github.com/filiphsps/Metro-Compose/commit/2f8de6fd4e752d9288992fcc855f69b09d26a30b)
#### Thursday 2023-05-04 02:43:33 by Filiph Sandström

Metro: Refactor `forceTapAnimation` into `TiltIndication`

Fixes #192.

This was a real PITA to reverse engineer and figure out thanks to the
lackluster `Indication` and `Interaction` documentation.

The API is also missing some expected features like proper rotation
so instead we have to use `android.graphics.Camera` for the actual
tilting effect.

Hopefully my pain reverse engineering `rememberRipple`& co and then
subsequent sharing of a real-world reimplementation will prevent
future generations from having to suffer the same way I have.

Y'all have been forewarned, if you choose to tread where I've tread
you'll only experience madness.

---
## [NanoCats/Monkestation2.0](https://github.com/NanoCats/Monkestation2.0)@[79e07c00db...](https://github.com/NanoCats/Monkestation2.0/commit/79e07c00db8607513347f8e7e6f2a8520e563680)
#### Thursday 2023-05-04 03:33:23 by Aeri

fucking wacky ass goddamn cargo order console locations fixed

---
## [YuXiaoDou/Open-Assistant](https://github.com/YuXiaoDou/Open-Assistant)@[b9c60ed582...](https://github.com/YuXiaoDou/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Thursday 2023-05-04 03:53:56 by Tobias Pitters

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
## [Youssefchahboune/GameProjectWinter2023](https://github.com/Youssefchahboune/GameProjectWinter2023)@[96847318f7...](https://github.com/Youssefchahboune/GameProjectWinter2023/commit/96847318f77d351be17c70c16b2c33c2eef555c8)
#### Thursday 2023-05-04 04:42:33 by ctsaki25

fixed buttons

what a pain in the ass jesus christ im sorry but holy crap man

---
## [whiteinge/dotfiles](https://github.com/whiteinge/dotfiles)@[07baa587e4...](https://github.com/whiteinge/dotfiles/commit/07baa587e44387d4f931ea575f7a2fe88e68e3b2)
#### Thursday 2023-05-04 04:55:36 by Seth House

Add lr and xe repos to my default clone

I try to stick to POSIX compatibility for my shell scripts, however
there are a few insufficiencies that aren't easy/possible to work
around. The big two are find and xargs. I rely on non-POSIX flags pretty
heavily (-0, -P, -r, -print0, -printf) and that usually means installing
the GNU suite (Busybox did copy a few of those flags but not all). But
it's kind of a crapshoot writing feature-detection all over is way too
verbose for simple scripts.

Why POSIX? For portability? For simplicity? Because ideologically I like
the Suckless philosophy? Maybe I just like doing it because it's harder
:-P. If I choose a custom userspace then I break portability. But
I write my dotfiles for ml; anything intended for an audience should be
broken out into a dedicated repo. (Note to self: do that for a few of
the scripts in bin.)

There's the question if I choose to install an extra util on top of
POSIX, then why not just install the GNU suite and be done with it?
I think it really is just a philosophical desire to avoid bloated tools
where possible. The bloat doesn't really affect me in any practical way,
but there's something appealing about a 2k SLOC find/ls replacement with
better ergonomics, or a 600 SLOC replacement for xargs. If the
apocalypse comes and we have to rebuild society, government, industry,
and POSIX (^_^), we need to retain the principles and fundamentals. All
the feature-creep will happen later (whether we want it to or not).

Jokes aside, I'd like to experiment more with running a minimal
userspace. Something like busybox with a few hand-picked extras.

---
## [smantriplw/ppdb-laravel](https://github.com/smantriplw/ppdb-laravel)@[778a055053...](https://github.com/smantriplw/ppdb-laravel/commit/778a055053a62c5562d465db9e4fae54bc35c6bc)
#### Thursday 2023-05-04 05:04:53 by Hanif Dwy Putra S

feat: add fucking, shit, and bitch thing in the school

Signed-off-by: Hanif Dwy Putra S <hanifdwyputrasembiring@gmail.com>

---
## [alexhenrie/git](https://github.com/alexhenrie/git)@[07f91e5e79...](https://github.com/alexhenrie/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Thursday 2023-05-04 05:34:40 by Jeff King

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
## [PinkSwitch/Archipelago](https://github.com/PinkSwitch/Archipelago)@[6d13dc4944...](https://github.com/PinkSwitch/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Thursday 2023-05-04 06:04:26 by el-u

lufia2ac: new features, bug fixes, and more (#1549)

### New features

- ***Architect mode***
  Usually the cave is randomized by the game, meaning that each attempt will produce a different dungeon. However, with this new feature the player can, between runs, opt into keeping the same cave. If activated, they will then encounter the same floor layouts, same enemy spawns, and same red chest contents as on their previous attempt.   

- ***Custom item pool***
  Previously, the multiworld item pool consisted entirely of random blue chest items because, well, the permanent checks are blue chests and that's what one would normally get from these. While blue chest items often greatly increase your odds against regular enemies, being able to defeat the Master can be contingent on having an appropriate equipment setup of red chest items (such as Dekar blade) or even enemy drops (such as Hidora rock), most of which cannot normally be obtained from blue chests.
  With the custom item pool option, players now have the freedom to place any cave item into the multiworld itempool for their world.

- ***Enemy floor number, enemy sprite, and enemy movement pattern randomization***
  Experienced players can deduce a lot of information about the opposition they will be facing, for example: Given the current floor number, one can know in advance which of the enemy types will have a chance to spawn on that floor. And when seeing a particular enemy sprite, one can already know which enemy types one might have to face in battle if one were to come in contact with it, and also how that enemy group will move through the dungeon.
  Three new randomization options are added for players who want to spice up their game: one can shuffle which enemy types appear on which floor, one can shuffle which sprite is used by which enemy type, and one can shuffle which movement pattern is used by which sprite.

- ***EXP modifier***
  Just a simple multiplier option to allow people to level up faster. (For technical reasons, the maximum amount of EXP that can be awarded for a single enemy is limited to 65535, but even with the maximum allowed modifier of 500% there are only 6 enemy types in the cave that can reach this cap.)


### Balance change

- ***proportionally adjust chest type distribution to accommodate increased blue chest chance***
  One of the main problems that became apparent in the current version has to do with the distribution of chest contents. The game considers 6 categories, namely: consumable (mostly non-restorative), consumable (restorative), blue chest item, spell, gear, and weapon. Since only blue chests count as multiworld locations, we want to have a mechanism to customize the blue chest chance.
  Given how the chest types are detetermined in game, a naive implementation of an increased blue chest chance causes only the consumable chance to be decreased in return. In practice, this has resulted in some players of worlds with a high blue chest chance struggling (more than usual) to keep their party alive because they were always low on comsumables that restore HP and MP.
  The new algorithm tries to avoid this one-sided effect by having an increase in blue chest chance resulting in a decrease of all other types, calculated in such a way that the relative distribution of the other 5 categories stays (approximately) the same.


### Bug fixes

- ***prevent using party member items if character is already in party***
  This should have been changed at the same time that 6eb00621e39c930f5746f5f3c69a6bc19cd0e84a was made, but oh well... 

- ***fix glitched sprite when opening a chest immediately after receiving an item***
  When opening a chest right after receiving a multiworld item (such that there were two item get animations in the exact same iteration of the game main loop), the item from the chest would display an incorrect sprite in the wrong place. Fixed by cleaning up some relevant memory addresses after getting the multiworld item.

- ***fix death link***
  There was a condition in `deathlink_kill_player` that looked kinda smart (it checked the time against `last_death_link`), but actually wasn't smart at all because `deathlink_kill_player` is executed as an async task and the main thread will update `last_death_link` after creating the task, meaning that whether or not the incoming death link would actually be passed to the game seems to have been up to a race condition. Fixed by simply removing that check.


### Other

- ***add Lufia II Ancient Cave (and SMW) to the network diagram***
  These two games were missing from the SNES sector.

- ***implement get_filler_item_name***
  Place a restorative consumable instead of a completely random item. (Now the only known problem with item links in lufia2ac is... that noone has ever tested item links. But this should be an improvement at least. Anyway, now #1172 can come ;)
  And btw., if you think that the implementation of random selection in this method looks weird, that's because it is indeed weird. (It tries to recreate the algorithm that the game itself uses when it generates a replacement item for a chest that would contain a spell that the party already knows.)

- ***store all options in a dataclass***
  This is basically like using #993 (but without actual support from core). It makes the lufia2ac world code much nicer to maintain because one doesn't have to change 5 different places anymore when adding or renaming an option.

- ***remove master_hp.scale***
  I have to admit: `scale` was a mistake. Never have I seen a single option value cause so many user misconceptions. Some people assume it affects enemies other than the Master; some people assume it affects stats other than HP; and many people will just assume it is a magic option that will somehow counterbalance whatever settings combination they are currently trying to shoot themselves in the foot with.
  On top of that, the `scale` mechanism probably doesn't provide a good user experience even when used for its intended purpose (since having reached floor XY in general doesn't mean you will have the power to deplete XY% of the Masters usual HP; especially given that, due to the randomness of loot, you are never guaranteed to be able to defeat the vanilla Master even when you have cleared 100% of the floors).
  The intended target audience of the `master_hp` option are people who want to fight the Master (and know how to fight it), but also want to lessen (to a degree of their choosing) the harsh dependence on the specific equipment setups that are usually required to win this fight even when having done all 99 floors. They can achieve this by setting the `master_hp` option to a numeric value appropriate for the level of challenge they are seeking. Therefore, nothing of value should be lost by removing the special `scale` value from the `master_hp` option, while at the same time a major source of user confusion will be eliminated.

- ***typing***
  This (combined with the switch to the option dataclass) greatly reduces the typing problems in the lufia2ac world. The remaining typing errors mostly fall into 4 categories:
  1. Lambdas with defaults (which seem to be incorrectly reported as an error due to a mypy bug)
  1. Classmethods that return instances (which could probably be improved using PEP 673 "Self" types, but that would require Python 3.11 as the minimum supported version)
  1. Everything that inherits from TextChoice (which is a typing mess in core)
  1. Everything related to asar.py (which does not have proper typing and lies outside of this project)

## How was this tested?

https://discord.com/channels/731205301247803413/1080852357442707476 and others

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[c2232ab14b...](https://github.com/treckstar/yolo-octo-hipster/commit/c2232ab14bdbb2ef83d0cb7ece6396d3cf44038a)
#### Thursday 2023-05-04 07:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [UserSniper/PizzaTowerFamicom](https://github.com/UserSniper/PizzaTowerFamicom)@[a7d2f5afde...](https://github.com/UserSniper/PizzaTowerFamicom/commit/a7d2f5afdeb66a34ee0dd505d66bd05f9e20c20b)
#### Thursday 2023-05-04 07:36:29 by ADM228

Revert "Merge pull request #3 from UserSniper/revert-2-main"

This reverts commit 82979faf5bdbb6ed3bd5c57cae07065c33a1c13f, reversing
changes made to 5b97b0e963ba4f9692ccb7cd36e57672c9c98fe5.

HOLY SHIT WHY CAN'T I USE GIT PROPERLY
>tries to update fs-driver branch
>accidentally merges fs-driver changes into main
>tries to revert it
>13 more fucking commits

kill my brain

---
## [Harvendois/PersonalPortfolioWebsite](https://github.com/Harvendois/PersonalPortfolioWebsite)@[5e126dab19...](https://github.com/Harvendois/PersonalPortfolioWebsite/commit/5e126dab1907f8821ba2b0c58400a77073435acb)
#### Thursday 2023-05-04 07:37:20 by Jungha Cho

May 4th Update - Contact and Hero Section

Today I really worked on making the website look better. That was the primary idea. 
- Contact Section gets a shape boost with bootstrap. Name, Email, Message, and Submit button all gets cool shape. They also do a validity check on their own :) pretty nice. The main problem is that the submit button somehow fails to send the values that are stored. I will have to fix that, but for now, the shapes are looking good! 
- Other sections also got minor revisions :) don't worry. 
- Hero Section gets a black background, a JS animation using setTimeOut. I think I can do so much more with setTimeOut and time manipulation skills, but this really requires me to understand more about how JavaScript works with setTimeOut and asynchronous executions. GPT mentioned using Promise and such, so those are some study materials too. 
- New ideas popping up! It would be nice to have a custom made button (that is V shaped) on the bottom of each section, which will scroll down to the next section automatically when clicked. onclick functions shouldn't be too hard right?
- New idea: the about section's text area gotta have this carousel-like-navbar that can move from slide to slide with different text information. I can keep academic life, my history, and main description text all within this. 
- New idea: the experience section better keep 
- New content: Activities (RA, WSP, Tutoring, Ambassador, and others) and clubs, all in timeline.

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[410979bb6a...](https://github.com/Stalkeros2/Skyrat-tg/commit/410979bb6af8b1ccfb840dee0461867724714912)
#### Thursday 2023-05-04 07:42:02 by SkyratBot

[MIRROR] Microing var/static times (~0.015 seconds of init) [MDB IGNORE] (#20688)

* Microing var/static times (~0.015 seconds of init) (#74769)

## About The Pull Request

Moth and I came up with an affront to god and man, and used it to track
the time spent creating /static (and in theory /global) variables (this
happens right at the start of init)
They cost as a sum about 0.05 seconds btw, at least currently.

```
/datum/timer
    var/key

/datum/timer/New(file, line)
    src.key = "[file]:[line]"

/datum/timer/proc/operator*(x)
    rustg_time_reset(key)
    return x

/datum/timer/proc/operator+(x)
    var/time = rustg_time_microseconds(key)
    world.log << "TIMER: [key]: [time]"
    return x

Regex:
var/static/([\w/]+) =
-> var/static/$1 = (new /datum/timer(__FILE__, __LINE__)) * (new /datum/timer(__FILE__, __LINE__)) +
```

Output on moth's pc looks like this, time in microseconds

[output_sorted.csv](https://github.com/tgstation/tgstation/files/11241900/output_sorted.csv)

Most of this is either icon_states() memes (which appears to be cached
btw, that's interesting), or a variation on typecacheof()
There is one get_asset_datum call, but that is ALREADY cached and so is
just redundant. That's a good 0.01 seconds saved.

The rest of the time here is slightly more interesting.

The majority of typecacheof() is iterating the output of typesof(), a
byond internal proc that returns a list of types that either are or are
the child of the passed in type.
A decent chunk of time here (0.005 seconds, or 10% of the proc) can be
saved by unrolling the arguments to the proc.
It takes an arbitrary amount of typepaths as input, but we can't like
use arglist() here (cause this is an internal "proc"), so instead we try
a window of args, passing in null if we start to try and take in too
much.
Window size matters, zebra fits better into 4 then 5, especially because
of how grouping needs to work to make this effect happen.
We save about 0.001 for zebra btw, which is around about 7%. It's lower
cause we need to group the paths beforehand I think.

The speedup is minor, but it DOES exist. Plus it's fun.

## Why It's Good For The Game

Microing is a hell of a drug

* Microing var/static times (~0.015 seconds of init)

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [i386sh/discpywal](https://github.com/i386sh/discpywal)@[bd2910ece9...](https://github.com/i386sh/discpywal/commit/bd2910ece94de84e0f4dd9ec3658013aea22a868)
#### Thursday 2023-05-04 07:44:25 by notzer0

Main bot code

fuck you it's the code for it i'll put the config scheme up in a second

---
## [IAD3D/OrbsVR](https://github.com/IAD3D/OrbsVR)@[eeb2bf2647...](https://github.com/IAD3D/OrbsVR/commit/eeb2bf26474da44d3237d66a4a2bd97963d5a684)
#### Thursday 2023-05-04 07:54:10 by QuentinFKS

[concept] Ajout FX Variant Zone + des fix

Ruler of everything en boucle dans mes oreilles depuis 4 jours:

Juno was mad, he knew he'd been had
So he shot at the sun with a gun
Shot at the sun with a gun
Shot at his wily one only friend
In the gallows or the ghetto
In the town or the meadow
In the billows even over the sun
Every end of the time is another begun
You understand mechanical hands
Are the ruler of everything (ah)
Ruler of everything (ah)
I'm the ruler of everything in the end
♪
Do you like how I dance? I've got zirconium pants
Consequential enough to slip you into a trance
Do you like how I walk? Do you like how I talk?
Do you like how my face disintegrates into chalk?
I have a wonderful wife, I have a powerful job
She criticizes me for being egocentric
You practice your mannerisms into the wall
If this mirror were clearer, I'd be standing so tall
I saw you slobber over clovers on the side of the hill
I was observing the birds (circle in for the kill)
I've been you, I know you, your facade is a scam
You know you're making me cry, this is the way that I am
I've been living a lie, a metamorphical scheme
Detective undercover, brotherhood, objective, obscene
Oh, no, no, oh yeah
♪
Do you hear the flibbity jibbity jibber jabber
With an, "Oh my God, I've got to get out of here or I'll have another
Word to sell, another story to tell
Another time piece ringing the bell"
Do you hear the clock stop when you reach the end?
No, you know it must be never ending, comprehend if you can
But when you try to pretend to understand
You resemble a fool, although you're only a man
So give it up and smile
♪
Do you hear the flibbity jibbity jibber jabber
With an, "Oh my God, I've got to get out of here or I'll have another
Word to sell, another story to tell
Another time piece ringing the bell"
Do you hear the clock stop when you reach the end?
No, you know it must be never ending, comprehend if you can
But when you try to pretend to understand
You resemble a fool although you're only a man
So give it up and smile
♪
You understand mechanical hands
Are the ruler of everything (ah)
Ruler of everything (ah)
I'm the ruler of everything
In the end
♪
Without looking down, gliding around
Like a bumbling dragon, I fly
Scraping my face on the sky
Oh, no, no, oh, yeah

---
## [mizushudesuyo/kernel_xiaomi_lavender](https://github.com/mizushudesuyo/kernel_xiaomi_lavender)@[cfaf637a55...](https://github.com/mizushudesuyo/kernel_xiaomi_lavender/commit/cfaf637a559ed23dc973674a7af1c1b7515c6f1e)
#### Thursday 2023-05-04 08:24:33 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: ImPrashantt <prashant33968@gmail.com>

---
## [newstools/2023-business-daily-kenya](https://github.com/newstools/2023-business-daily-kenya)@[153383052a...](https://github.com/newstools/2023-business-daily-kenya/commit/153383052a99124e81450bf011e92b09970f860b)
#### Thursday 2023-05-04 09:46:57 by Billy Einkamerer

Created Text For URL [www.businessdailyafrica.com/bd/lifestyle/weekend-with-the-ceo/faith-nkatha-her-boys-and-god-s-place-in-corporate-meetings--4221870]

---
## [ioccc-src/temp-test-ioccc](https://github.com/ioccc-src/temp-test-ioccc)@[bb7c81e4f6...](https://github.com/ioccc-src/temp-test-ioccc/commit/bb7c81e4f67e124a29d3d71da8df42eae0a064d5)
#### Thursday 2023-05-04 09:51:09 by Cody Boone Ferguson

Add entry to faq.md about terminal sanity

In other words after running a curses program (ANSI escape codes can
also cause problems) the terminal can be quite insane; echo might be
disabled as a simpler example but many worse more annoying problems can
occur.

The simplest way is to run reset. This will restore everything though
it'll clear the screen (clear command will not fix any problems but just
clear the screen). For echo disabled stty echo should work. Sometimes
you can get away with doing stty sane.

Now these are in the faq.md. I wrote more about this in 2020/ferguson1
but that doesn't really matter other than it was the inspiration for
this entry (which I think is a good idea to include).

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[dd7d24e9ff...](https://github.com/EaW-Team/equestria_dev/commit/dd7d24e9ffb1751567b805532e8c6e383bafc7f3)
#### Thursday 2023-05-04 10:01:20 by Mustafa Alperen Seki

Add ideology independent names for countries.

In basegame this is only used for Collab Government names, so so far only Olenia had this defined in EaW, as we don't use that puppet type anythwhere else. I was thinking of adding them regardless, my bored ass decided to finally do it.

Also grouped CHN puppet names together like SOL, NLR, and TEM ones had.

And moved PCB to basegame and EWI to griffonia file.

---
## [MassMeta/tgstation](https://github.com/MassMeta/tgstation)@[2b2cb3dff6...](https://github.com/MassMeta/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Thursday 2023-05-04 10:02:38 by LemonInTheDark

Hologram Touchup (Init savings edition) (#74793)

## About The Pull Request

### Polishes and Reworks Holograms

Hologram generation currently involves a bunch of icon operations, which
are slow.
Not to mention a series of get flats for the human models, which is even
worse.

We lose 0.05 seconds of init to em off just the 2 RCD holograms. it
hurts man.

So instead, let's use filters and render steps to achive the same
effect.

While I'm here I'll dim the holo light and make it blue, make the
hologram and its beam emissive (so they glow), and do some fenangling
with move_hologram() (it doesn't clear the hologram off failure anymore,
instead relying on callers to do that) to ensure holocalls can't be
accidentially ended by moving out of the area.

Ah and I added RESET_ALPHA to the emissive appearance flags, cause the
alpha does override and fuck with color rendering, which ends up looking
dumb. If we're gonna support this stuff it should be first class not
accidential.

### Makes Static Not Shit

While I'm here (since holograms see static) lets ensure the static plane
is always visible if you're seeing through an ai eye.

The old solution was limited to applying it to JUST ais, which isn't
satisfactory for this sort of thing and missed a LOT of cases (I didn't
really get how ai eyes worked before I'ma be honest)

I'm adding a signal off the hud for it detecting a change in its eye
here.
This is semi redundant, but avoids unneeded dupe work, so I'm ok with
it.

The pipeline here is less sane then I'd like, but it works and that's
enough

## Why It's Good For The Game


![dreamseeker_zMiLXzlZ2X](https://user-images.githubusercontent.com/58055496/232470136-add945da-5f76-469e-ba1a-6ed3159b6f5b.png)
More pretty, better ux, **static works**

## Changelog
:cl:
add: Holograms glow now, pokes at the lighting for holocalls in general
a bit to make em nicer.
qol: You can no longer accidentally end a holocall (as a non ai) by
leaving the area. Felt like garbage
fix: Fixes static rendering improperly if viewed by a non ai
/:cl:

---
## [TheBestPessimist/dippidy-derp](https://github.com/TheBestPessimist/dippidy-derp)@[cf98e42f46...](https://github.com/TheBestPessimist/dippidy-derp/commit/cf98e42f46c36a00a7104bc7ccfa8d66c61fdc1a)
#### Thursday 2023-05-04 11:56:24 by TheBestPessimist

Disable Modern Standby

It's a piece of shit. Fuck this fucking shit. Whenever my screen turns off, laptop goes to sleep. This if fucking retarded

---
## [OpenVisionE2/enigma2-openvision](https://github.com/OpenVisionE2/enigma2-openvision)@[fdfef7ebaf...](https://github.com/OpenVisionE2/enigma2-openvision/commit/fdfef7ebaf60b0044b05c7e8d6f2576a28ef4030)
#### Thursday 2023-05-04 12:10:47 by persianpros

Add shitty dmamlogic code

Part of the code is based on https://github.com/OpenVisionE2/enigma2-openvision/commit/9847be82208877f0a9a12b1e3f3dc98f81b8dda2 and https://github.com/OpenVisionE2/enigma2-openvision/commit/ac85a2a4365fd3fff538d64ccf94728162b14e36

The rest is based on https://github.com/openatv/enigma2/commit/c00d421fddda4d84f0a40f5e723c064965423692 which I did split it in a general commit (https://github.com/OpenVisionE2/enigma2-openvision/commit/ad455e4dd64c6b9d21aa64124eb27b485834e01e) and this one which is dreambox specific

We don't provide e2 images for dmamlogic but for compatibility with ATV and future cherry-picks I add this code so we could move on but we can consider dmamlogic code as garbage because the audio won't work and the final image is not usable thanks to all the stupid people behind dmamlogic audio patch

---
## [spartanbobby/cmss13](https://github.com/spartanbobby/cmss13)@[d728da3e02...](https://github.com/spartanbobby/cmss13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Thursday 2023-05-04 12:28:48 by Puckaboo2

Healer Balance Changes (#2896)

# About the pull request
This pull request addresses the boring and low-risk gameplay of the
Healer drone, who spends half the round sitting next to recovery nodes
and recovering her health so she may use it again, rinse and repeat
until a rine notices said drone has purple on it and booms her.

First, by changing her health from 600 to 500, Healer can spend more
time healing her sisters than sitting through another 100 health to heal
herself. Though this makes her less tanky than before, healing classes
are not known to be tanks. To ensure Healer can still heal five times
without depleting too much of her health whilst still giving her sisters
a decent amount of heals, I made her ability cost 75 health instead of
100, and also made her ability cost 200 plasma. Since Healer replenishes
plasma much more quickly than her health, she can still put herself into
crit if she heals too frequently. Due to this buff, her heals had a
slight nerf, being 10 damage a second for ten seconds instead of 12
damage per second for ten seconds for a total of 20 less damage healed
per application overall.

In addition to these changes, I'm giving Healer a better plasma transfer
for when she has nobody else to heal/nowhere else to weed and she has an
opportunity to assist her sisters. While a normal drone transfers 50
plasma with a delay of 20, Healer transfers 100 with a delay of 15,
which is nowhere near Hivelord's gargantuan 200 plasma with a delay of
5, but it still is better than a normal drone.

Finally, to give the huggers and larva some love, Healer will
specifically heal little ones 1.5 health per second for 10 seconds for
15 of her own health and 30 plasma.

# Explain why it's good for the game
Healer drone isn't fun. You run around and heal a bunch of T3s, then sit
out for half the battle trying to heal that massive 600 heath while you
wonder why you take so long to heal even though you have Strong
pheromones. You cry to mom for help, but she doesn't have time to heal a
drone who can't build walls and has no need to weed at the moment. You
think, 'screw it, I'm going to make a recovery node and camp here until
I heal', but by the time you finish healing, several T3s and a silly
rouny just suicided into a wall of talls and destroyed your recovery
node, so you run off and make another one. But oh, someone noticed you
have purple on your carapace and decide your location is precisely where
a shell should land, right as you're building one.

No more. These changes allow Healer to move around at her leisure and
makes Healer more engaging by allowing her to be a more front-line
participant and actively run around and heal her sisters without having
to incur such a harsh penalty.

Let this be a testmerge, please.

# Changelog

:cl: Puckaboo2
balance: Healer Drone's health was reduced to 500 from 600.
balance: Healer's damage has been increased to 17 from 12 and the tackle
damage debuff has been halved.
balance: Healer Drone's Apply Salve ability now costs 75 health and 200
plasma, down from 120 health and up from 0 plasma.
balance: Healer Drone's Apply Salve ability now heals 10 damage per
second for 10 seconds, down from 12 damage per second for ten seconds.
balance: To prevent spam healing between Healers, Apply Salve costs 100
health instead of 75 health when Healer heals another Healer. Much
healing.
balance: Healer has an improved Transfer Plasma that gives 100 plasma
instead of 50, with a 25% shorter delay.
balance: Healer will heal huggers and larva for 1.5 health a second for
10 seconds, costing 15 health and 30 plasma.
tweak: Healer will now face the xeno she is healing if she was not
facing their direction before.
spellcheck: All instances of VERYSMALL and VERYLARGE have been renamed
to VERY_SMALL and VERY_LARGE.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[8f24aba86f...](https://github.com/odoo-dev/odoo/commit/8f24aba86faf2639109b56887781b0daaf60be98)
#### Thursday 2023-05-04 12:28:56 by Romain Derie

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
## [StrangerStrings/digitool](https://github.com/StrangerStrings/digitool)@[9bc2fd99a8...](https://github.com/StrangerStrings/digitool/commit/9bc2fd99a817eb585b4f0809688713f7fc67acfa)
#### Thursday 2023-05-04 13:28:11 by =

 I don't know the shortcut emojis oh thank you monkey. The thing is it used to be FN but I seem to have changed so fuck off control commands hello it's regarding an I don't know how to stop desk Taiwan yeah go on then

---
## [AndrewKhassapov/character-soup](https://github.com/AndrewKhassapov/character-soup)@[ec06f0e37c...](https://github.com/AndrewKhassapov/character-soup/commit/ec06f0e37cb594e5be7fbba860e259e715da6f13)
#### Thursday 2023-05-04 13:34:19 by AndrewKhassapov

Update README.md

+ It is almost Friday, 5 May, here in Melbourne. And alas, we bid adieu to World Password Day.
May you have a lifetime of no breaches.
May any phishing attempts be funny and poorly spelled.
And may your stockings be filled with hard-to-open foods, such as pineapples and hard-shelled crab, after CorrectHorseBatteryStaple fails to visit your home at night, because it's locked up.

---
## [umut-er/pool-for-physicists-only](https://github.com/umut-er/pool-for-physicists-only)@[42c03f6a75...](https://github.com/umut-er/pool-for-physicists-only/commit/42c03f6a75d001c33d4dc62656189a8c26b20af2)
#### Thursday 2023-05-04 13:49:37 by Umut Utku ERŞAHİNCE

fix: now implementing the complicated ball-cushion formula.
Several hours of work (mostly debugging) done, several more to go! Proceed with caution if you want to change these stuff!
There is an issue where we can't detect some collisions. This is in my opinion not a bug in the implementation. Our approach needs to change to fix this. Don't know how commonly this happens or whether it will affect regular user experience. Playtesting is required after pockets are implemented and game is operational.

---
## [ma44/tgstation](https://github.com/ma44/tgstation)@[fa0225b05c...](https://github.com/ma44/tgstation/commit/fa0225b05c5411c46187f67816f8363e7dd91f30)
#### Thursday 2023-05-04 14:18:58 by san7890

Converts Spiderlings from Structures to Basic Mobs (#75001)

If I could've made this more atomic, I would have in a heartbeat, trust
me.

## About The Pull Request

Hey there. People were mocking us for having spiderlings still be a
subtype of `/obj/structure`. I decided to take a lot of time to fix
that. A lot of behavior it was implementing was just pseudo-mob stuff,
so it was actually easier than it looked for the raw conversion. A lot
of the footwork on spider stuff in the basic framework was already done
previously by Jacquerel, so that was pretty nice.

However, there are two new things that weren't introduced in the code
that had to be put in.

A) A component to handle growth and differentiation into a mob. This may
have already existed, no clue. If it does (and it's NOT
evolutionary_leap), let me know.
B) AI Behavior to handle seeking out a vent, entering a vent, and then
exiting out of a different vent. I may have gone a bit wacky on the
code, but it certainly works as expected (spiderling goes in one vent,
exits the other). Let me know if you can think of a way it can be better
optimized, but it was deliberately written to be very failsafey in case
shit goes yonkers.

One fundamental difference between structure spiderlings and basic mob
spiderlings (beyond the AI and not just a random prob() check for
movement) is the fact that they had vent movement coded in... but we
_really_ don't need stuff like that for our intents and purposes. If the
range turns out to be too OP in the current framework, we can always
change it up a bit, but also there's a _lot_ of vents we can end up in
the station (my testing had one spiderling end up in the AI sat to get
obliterated).
## Why It's Good For The Game

Spiderlings aren't structures! They behave like a mob should! Players
can possess spiderlings! They work seamlessly with differentiating into
a giant spider! Better AI! More room for people to add into this very
under-utilized buggers!
## Changelog
:cl:
refactor: Spiderlings are now basic mobs, report any complete
weirdness/deviation from known behavior. They should be a lot more
intelligent now though.
add: AI Spiderlings are super fragile, but they're also super fast,
especially when they get into a vent. Once they're in circulation, they
could end up everywhere! Maybe in the armory, maybe in a locked closet
in maintenance. Be sure to be vigilant and splat them whenever you can
to save the station from a whole lotta heartache!
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Quacks-and-Kepteyn/Skyrat-tg](https://github.com/Quacks-and-Kepteyn/Skyrat-tg)@[39ebf7c2af...](https://github.com/Quacks-and-Kepteyn/Skyrat-tg/commit/39ebf7c2af41309fa4d5206f77cc4d261f47dfb7)
#### Thursday 2023-05-04 14:37:27 by SkyratBot

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
## [blackcrystall/cmi](https://github.com/blackcrystall/cmi)@[4cf0651670...](https://github.com/blackcrystall/cmi/commit/4cf06516705b3e0f4a6f446cd36eaa15b554a561)
#### Thursday 2023-05-04 14:44:08 by BlackCrystalic

Fixes queen stat bug (#3168)

# About the pull request

Good morning VIETNAM!
That again happened! We found some mistake!

# Explain why it's good for the game

That not good for game, because I fixend so usual staff, like timer for
queen, he can abuse that to make engage on last second and marines -
bruh, young queen, FIGHT! and BANG! Screech on ALL marines... Stupid
folks.

(devs trying to find and fix bugs)
https://www.youtube.com/watch?v=ryNSpF9I3rE

# Changelog

:cl:
fix: Stat proc replaced with get_status_tab_items, fixed issue with
QUEEN additional status
/:cl:

Co-authored-by: BlackCrystalic <blackcrystalic@inbox.ru>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[152729ffda...](https://github.com/TaleStation/TaleStation/commit/152729ffda8aa428047b51fc648ac221cc3a4ca4)
#### Thursday 2023-05-04 15:05:14 by TaleStationBot

[MIRROR] [MDB IGNORE] Minerals have been refactored so costs and minerals in items are now in terms of mineral defines. (#5615)

Original PR: https://github.com/tgstation/tgstation/pull/75052
-----
## About The Pull Request

Ladies, Gentlemen, Gamers. You're probably wondering why I've called you
all here (through the automatic reviewer request system). So, mineral
balance! Mineral balance is less a balance and more of a nervous white
dude juggling spinning plates on a high-wire on his first day. The fact
it hasn't failed after going on this long is a miracle in and of itself.

This PR does not change mineral balance. What this does is moves over
every individual cost, both in crafting recipes attached to an object
over to a define based system. We have 3 defines:

`sheet_material_amount=2000` . Stock standard mineral sheet. This being
our central mineral unit, this is used for all costs 2000+.
`half_sheet_material_amount=1000` . Same as above, but using iron rods
as our inbetween for costs of 1000-1999.
`small_material_amount=100` . This hits 1-999. This covers... a
startlingly large amount of the codebase. It's feast or famine out here
in terms of mineral costs as a result, items are either sheets upon
sheets, or some fraction of small mats.

Shout out to riot darts for being the worst material cost in the game. I
will not elaborate.

Regardless, this has no functional change, but it sets the groundwork
for making future changes to material costs much, MUCH easier, and moves
over to a single, standardized set of units to help enforce coding
standards on new items, and will bring up lots of uncomfortable balance
questions down the line.

For now though, this serves as some rough boundaries on how items costs
are related, and will make adjusting these values easier going forward.

Except for foam darts.

I did round up foam darts.

## Why It's Good For The Game

Adjusting mineral balance on the macro scale will be as simple as
changing the aforementioned mineral defines, where the alternative is a
rats nest of magic number defines. ~~No seriously, 11.25 iron for a foam
dart are you kidding me what is the POINT WHY NOT JUST MAKE IT 11~~

Items individual numbers have not been adjusted yet, but we can
standardize how the conversation can be held and actually GET SOMEWHERE
on material balance as opposed to throwing our hands up or ignoring it
for another 10 years.

## Changelog
:cl:
refactor: Mineral costs have been reformatted to be scaled by the number
of sheets, darts, and small fractions they make up.
qol: Foam darts no longer hold a fraction of a unit of iron within
themselves.
/:cl:

---------

Co-authored-by: ArcaneMusic <41715314+ArcaneMusic@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [MensonRbx/RobloxModules](https://github.com/MensonRbx/RobloxModules)@[61209ed61a...](https://github.com/MensonRbx/RobloxModules/commit/61209ed61acaf7b0eb6f14bdf19ee2a964fbd8b3)
#### Thursday 2023-05-04 15:45:27 by MensonRbx

Stupid idea, but whatever

I might just continue trying to create weird abstractions like this for the hell of it, I quite enjoy it

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[590bad4061...](https://github.com/Huffie56/cmss13/commit/590bad4061627b75b638c0f7c1fbd3cca84e43c1)
#### Thursday 2023-05-04 15:48:14 by sleepynecrons

updates for landing zone sign sprites (#3180)

# About the pull request

Cleans up the palettes on the landing zone sign sprites and gives them a
fresh coat of paint (or blood). Not something most people will notice I
think but it's something I've been wanting to do.


# Explain why it's good for the game

gradients ugly


# Before and After
<details>
<summary>Click to see sprites</summary>


![osudodajs2](https://user-images.githubusercontent.com/106241650/235265980-e622b7da-8f79-4920-ba27-97d704c65550.gif)


![beforenafter](https://user-images.githubusercontent.com/106241650/235266004-0e46a574-9262-445f-98d9-4b19aa53a8fb.png)

</details>


# Changelog

:cl:
imageadd: new sprites for landing zone signs
imagedel: deleted old landing zone signs
/:cl:

---
## [gjcolombo/omicron](https://github.com/gjcolombo/omicron)@[ccc28fe4c8...](https://github.com/gjcolombo/omicron/commit/ccc28fe4c857c08599f5d9d6eff6ecfcaa298eb6)
#### Thursday 2023-05-04 16:15:57 by Sean Klein

[sled-agent] Refactor service management out of `StorageManager` (#2946)

## History

The Sled Agent has historically had two different "managers" responsible
for Zones:

1. `ServiceManager`, which resided over zones that do not operate on
Datasets
2. `StorageManager`, which manages disks, but also manages zones which
operate on those disks

This separation is even reflected in the sled agent API exposed to Nexus
- the Sled Agent exposes:

- `PUT /services`
- `PUT /filesystem`

For "add a service (within a zone) to this sled" vs "add a dataset (and
corresponding zone) to this sled within a particular zpool".

This has been kinda handy for Nexus, since "provision CRDB on this
dataset" and "start the CRDB service on that dataset" don't need to be
separate operations. Within the Sled Agent, however, it has been a
pain-in-the-butt from a perspective of diverging implementations. The
`StorageManager` and `ServiceManager` have evolved their own mechanisms
for storing configs, identifying filesystems on which to place zpools,
etc, even though their responsibilities (managing running zones) overlap
quite a lot.

## This PR

This PR migrates the responsibility for "service management" entirely
into the `ServiceManager`, leaving the `StorageManager` responsible for
monitoring disks.

In detail, this means:

- The responsibility for launching Clickhouse, CRDB, and Crucible zones
has moved from `storage_manager.rs` into `services.rs`
- Unfortunately, this also means we're taking a somewhat hacky approach
to formatting CRDB. This is fixed in
https://github.com/oxidecomputer/omicron/pull/2954.
- The `StorageManager` no longer requires an Etherstub device during
construction
- The `ServiceZoneRequest` can operate on an optional `dataset` argument
- The "config management" for datastore-based zones is now much more
aligned with non-dataset zones. Each sled stores
`/var/oxide/services.toml` and `/var/oxide/storage-services.toml` for
each group.
- These still need to be fixed with
https://github.com/oxidecomputer/omicron/issues/2888 , but it should be
simpler now.
- `filesystem_ensure` - which previously asked the `StorageManager` to
format a dataset and also launch a zone - now asks the `StorageManager`
to format a dataset, and separately asks the `ServiceManager` to launch
a zone.
- In the future, this may become vectorized ("ensure the sled has *all*
the datasets we want...") to have parity with the service management,
but this would require a more invasive change in Nexus.

---
## [Moltovz/Shiptest](https://github.com/Moltovz/Shiptest)@[b5dc4835a6...](https://github.com/Moltovz/Shiptest/commit/b5dc4835a6af4fc2ee07e2d26e86382b3d0fb1ab)
#### Thursday 2023-05-04 16:51:28 by Bjarl

New Ruin: Singularity Research Lab (#1612)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds the Singularity Research Lab, formerly a cutting edge science
station, now overrun with kudzu, it is a space ruin.
<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->
![2022 11 25-10 46
03](https://user-images.githubusercontent.com/94164348/204041197-027d9a73-8707-4a00-ad5c-1afcfeff13e0.png)
![2022 11 25-10 46
14](https://user-images.githubusercontent.com/94164348/204041200-98d1a2ac-112c-4c4f-b1ff-d0c1e5a59e81.png)
![2022 11 25-10 46
06](https://user-images.githubusercontent.com/94164348/204041203-4e84a947-8ec9-476d-ae8e-aa9bc17c101a.png)

The two areas of note are the singularity reactor, which is assembled,
and would just need a hand if someone were to want to start it, and the
research lab. The Research lab contains the fruits of the now deceased
science staff's labors, assorted energy weapons. Unfortunately, it also
contains the deceased science staff.

![dreamseeker_HFLqhdKLV5](https://user-images.githubusercontent.com/94164348/204038725-1dd396cd-4961-40e1-bd7a-b60b69a33eaf.png)
Other areas of the base were not so lucky, and are thoroughly infested

![image](https://user-images.githubusercontent.com/94164348/204039090-c85eb551-af84-4000-b1d9-14b15c987680.png)
The engineering team attempted to hold back the vines, and quickly
discovered that fire was not sufficient.

![dreamseeker_IrJikGDXKw](https://user-images.githubusercontent.com/94164348/204039133-273f0a19-c9b7-467e-a06a-05e0a951e4e6.png)
And what used to be the recreation area is completely gone

Notably, the hangar is empty. I plan on making a patch to put a
subshuttle inside it once that rolls around.

Notable loot includes:
3 energy SMGs
3 Flamethrowers
The Ion Projector, a self charging Ion weapon.
An Antique Laser
2 Energy PDWs
2 Accelerator Laser Cannons
4 engineering hardsuits
An engineering lathe and circuit imprinter
A particle accelerator
A singularity generator
6 emitters
1 energy shotgun
Kudzu Seeds
Basically Everything You'd Need For an R&D Set Up
A sense of pride and accomplishment



I feel like this has some rough spots but I've got no idea where to
start, so into the review -> testing -> feedback process it goes

- [x] The ruin spawns when the spawn ruin verb doesn't runtime.
## Why It's Good For The Game
More ruin variety. This one spawns in space and does a few things that I
haven't seen yet. Mainly a singularity, cool semi-hidden asteroid base
that could in theory, be turned into a player lair.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An abandoned Nanotrasen Asteroid Facility has been spotted in the
area. Salvage teams are advised to steer clear, or at least bring a
knife.
add: kudzu zombie subtype. 
fix: vent iconstates.
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
Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [Moltovz/Shiptest](https://github.com/Moltovz/Shiptest)@[7df4885117...](https://github.com/Moltovz/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Thursday 2023-05-04 16:51:28 by Mark Suckerberg

[Needs TM] The Accelerataning (#1781)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Gone are the days of spam clicking buttons to move faster in a
direction, with this PR, ships now accelerate constantly (as long as you
have fuel and don't touch the throttle) in a direction you set, leading
to a much smoother flight experience. I imagine it's going to be a bit
tougher to thread gaps, but flying a spaceship *is* quite literally
rocket science. So.

![](https://user-images.githubusercontent.com/29362068/220281305-12f6b796-9d8a-41ce-84a6-236bb03274da.gif)

Also actually makes the minimum and maximum speed work, and adjusts them
to a more tolerable level.

## Why It's Good For The Game
Eliminates the ability to cheese high speeds by spamming the accelerate
button, and also makes the flight experience much more pleasant as you
don't have to spam click to move a decent speed.

## Changelog

:cl:
add: A new system for ship flight, where you only point a direction and
set the throttle to change your speed, reducing the need for
spam-clicking.
fix: There's now a maximum and minimum speed, 600spm and 0.01spm,
respectively. The limits have been broken all this time.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [gnachman/iTerm2](https://github.com/gnachman/iTerm2)@[ed5edcadad...](https://github.com/gnachman/iTerm2/commit/ed5edcadad01f5feeb63ea66548c167ffa456221)
#### Thursday 2023-05-04 17:27:46 by George Nachman

Fix an incorrect assumption that OSC 7 precedes the prompt, when in fact it comes after. Also fix a performance issue with PromptStateMachine - in Swift getting the length of a string is an O(N) operation, it seems. This caused performance problems when the state machine was confused (e.g., start in tcsh with shell integration then run zsh which sends OSC 7 and it gets stuck in the 'accruing' state). My dream is that some day I can enjoy the quality of life I had in Turbo Pascal where counting the length of a string could be done in constant time.

---
## [Blosuhm/MSF](https://github.com/Blosuhm/MSF)@[371fd7a375...](https://github.com/Blosuhm/MSF/commit/371fd7a375e2d436058ac8094e58e1a3dfd232fd)
#### Thursday 2023-05-04 17:39:02 by Blosuhm

Good afternoon, my name is zakarias dropping here a fat W

This is the best python you'll ever see (don't look to closely).

And this is a test to see if I can push to the main branch.
But I don't think I can.
Help me.
I am in pain.
I am suffering.

Goodbye cruel world.
This is the end.
I am going to die.

- Zakarias

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[8f5ad18cc7...](https://github.com/newstools/2023-new-york-post/commit/8f5ad18cc7bb485e7f1021b97f5d7f61bb09b3db)
#### Thursday 2023-05-04 17:50:16 by Billy Einkamerer

Created Text For URL [nypost.com/2023/05/04/colorado-man-tyler-griffen-told-cops-he-remembers-punching-girlfriend-dezirae-andersen-before-she-jumped-from-times-square-hotel/]

---
## [NVIDIA/Fuser](https://github.com/NVIDIA/Fuser)@[9c50ae8f14...](https://github.com/NVIDIA/Fuser/commit/9c50ae8f1441917c97ebaceb343ad6be3c54304b)
#### Thursday 2023-05-04 18:26:51 by Gao, Xiang

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
## [BrendanHar/CSCI442](https://github.com/BrendanHar/CSCI442)@[d015e4e5aa...](https://github.com/BrendanHar/CSCI442/commit/d015e4e5aa9f357081fff7c904d134b88daa7b64)
#### Thursday 2023-05-04 18:38:39 by Brendan

My name is Walter Hartwell White. I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If you're watching this tape, I'm probably dead– murdered by my brother-in-law, Hank Schrader. Hank has been building a meth empire for over a year now, and using me as his chemist. Shortly after my 50th birthday, he asked that I use my chemistry knowledge to cook methamphetamine, which he would then sell using connections that he made through his career with the DEA. I was... astounded. I... I always thought Hank was a very moral man, and I was particularly vulnerable at the time – something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me in on a ride-along and showed me just how much money even a small meth operation could make. And I was weak. I didn't want my family to go into financial ruin, so I agreed. Hank had a partner, a businessman named Gustavo Fring. Hank sold me into servitude to this man. And when I tried to quit, Fring threatened my family. I didn't know where to turn. Eventually, Hank and Fring had a falling-out. Things escalated. Fring was able to arrange – uh, I guess... I guess you call it a

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7c6d8e2372...](https://github.com/mrakgr/The-Spiral-Language/commit/7c6d8e23728706b5f048a47742b0fae910c5c677)
#### Thursday 2023-05-04 19:31:46 by Marko Grdinić

"8:40am. Almost done chilling. Let me just finish Hagure Idol and then I will resume where I was yesterday.

9am. Let me start. I'll leave leasure for later? Any mail?

I opened some issues yesterday.

Nope, nevermind that. I'll just cover the bugs and be done with it.

10:25am. https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90
https://news.ycombinator.com/item?id=35811741

I'll read this later.

https://creativecow.net/forums/thread/weird-timeline-playback-audio-fade-in-issue/

Damn it, now DR bugs are wasting my time.

While I was going through the video I noticed that I accidentally had a clip frame frozen when I fixed it, the audio started fading weirdly.

This happened to me once previously, and I had trouble dealing with it.

11:55am. Damn it, why is the audio getting quiet in places.

...Oh, I am checking it out in the fairlight page, and there are these weird crossfades that span the entire clip!

WTF?

Cutting and reinserting on the fairlight page seems to get rid of that.

Ok, at least now I have a better way of fixing it than before.

///

No, it doesn't seem like we have much in the way of choices.
There is something here about notifying the client when the connection is closed, but we can't see a way to get the level of control that we desire.
We'll have to go with the more flexible appproach and check out those Fable SignalR packages.

///

12:50pm. https://shmew.github.io/Fable.SignalR/#/signalr-client/connecting

Let me stop here. This library was an excellent find!

I am looking forward to trying it out.

https://github.com/Shmew/Fable.SignalR/issues/

Opened issue 41 here.

https://github.com/Shmew/Fable.SignalR/search?q=Fable.FastCheck

```
---------------------------------------------------------------------
Build Time Report
---------------------------------------------------------------------
Target         Duration
------         --------
CleanDocs      00:00:00.0301179
ConfigDebug    00:00:00.0001886
Clean          00:00:00.0794757
CopyDocFiles   00:00:00.0017037
Restore        00:00:54.4596244   (Unsupported log file format. Latest supported version is 14, the log file has version 15.)
PackageJson    00:00:00           (skipped)
YarnInstall    00:00:00           (skipped)
Lint           00:00:00           (skipped)
Build          00:00:00           (skipped)
RebuildSass    00:00:00           (skipped)
RunTests       00:00:00           (skipped)
All            00:00:00           (skipped)
PrepDocs       00:00:00           (skipped)
Start          00:00:00           (skipped)
Dev            00:00:00           (skipped)
Total:         00:00:54.6751661
Status:        Failure
```

Predicatably the project doesn't build.

4:55pm. I've yet to get a `build.fsx` file to build successfully even a single time in my life.

5:15pm. https://www.reddit.com/r/fsharp/comments/137pm7u/what_should_be_done_with_abandonware_libraries/

Ok, what I will do is try a step by step rebuild.

```
<?xml version="1.0" encoding="utf-8"?>
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Library</OutputType>
    <TargetFramework>netstandard2.0</TargetFramework>
  </PropertyGroup>
  <ItemGroup>
    <Compile Include="Shared.fs" />
    <Compile Include="Types.fs" />
    <Compile Include="HttpClient.fs" />
    <Compile Include="HubConnection.fs" />
    <Compile Include="Protocols.fs" />
    <Compile Include="SignalR.fs" />
    <None Include="paket.references" />
    <None Include="paket.template" />
  </ItemGroup>
  <PropertyGroup>
    <NpmDependencies>
      <NpmPackage Name="@microsoft/signalr" Version="gte 3.1.5 lt 6" ResolutionStrategy="max" />
    </NpmDependencies>
  </PropertyGroup>
  <Import Project="..\..\.paket\Paket.Restore.targets" />
</Project>
```

Oh, I didn't know that npm packages could be included in the .fsproj file.

Let's just do it.

I'll go ever the projects one by one, adding the files into them.

6:20pm. https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.hubendpointconventionbuilder?view=aspnetcore-8.0

I am so confused. Why is this class not where it should be?

https://www.nuget.org/packages?q=signalr

What the dick. The regular SignalR is really old!

```
Microsoft.AspNetCore.App.Ref v7.0.5
```

Wait, here it says the exact package. I forgot to paste in the framework reference, damn.

6:55pm. I'll stop here for the day.

https://www.semianalysis.com/p/google-we-have-no-moat-and-neither

This blog always has interesting stuff on it.

At the rate I am going I should be able to finish the rebuild of the SignalR library tomorrow."

---
## [sleepynecrons/cmss13](https://github.com/sleepynecrons/cmss13)@[c4ebe04c7c...](https://github.com/sleepynecrons/cmss13/commit/c4ebe04c7c9ff01aa928c0c629322d72dec721d9)
#### Thursday 2023-05-04 19:47:05 by Julian56

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
## [andrguardia/final_assignment](https://github.com/andrguardia/final_assignment)@[4ee7eea896...](https://github.com/andrguardia/final_assignment/commit/4ee7eea8966596c83232956126ce5185481ec5bb)
#### Thursday 2023-05-04 22:27:01 by Andre Guardia

Im going insane trying to set up a plot in this god forsaken programming language. I saved all path results as arrays of the form [(xPoint:Double, yPoint:Double)]. Unfortunately I am either too hungry, too tired or too much of a noob to figure this one out tonight. Great progress for today though. the hardest part of this project is behind me: setting up and solving the hamiltonian. i am pumped abt that. I might need to revise the constants to ensure the results are actually accurate, but at this point we are 2/3 of the way there. Just need to get Prof Terry's help doing all this plot stuff. I CANNOT FIGURE THIS OUT FOR THE LIFE OF ME UGHGHDHFHV.

Plotting this would've taken me literally 1 minute if THIS WERE PYTHON......to that point, there might be a matplotlib wrapper for Swift. Will look into it hehehe

---
## [atosti/tgstation](https://github.com/atosti/tgstation)@[c8c977989a...](https://github.com/atosti/tgstation/commit/c8c977989a793cfe1e24eb6aa4350e14335025e5)
#### Thursday 2023-05-04 22:35:44 by John Willard

Mimes can no longer write without breaking their vow. (#74674)

## About The Pull Request

I feel this is gonna be unpopular with the lazy mime players.

Also, this is an idea I had in my backlog for a while now

![image](https://user-images.githubusercontent.com/53777086/231355622-2c5d5d5a-813d-420c-ae42-c1bdc657f3ba.png)

This removes the Mime's ability to write on paper while they're on their
vow of silence.
This can be compared to hand language, which doesn't let you speak
despite not being considered "talking", and PDA messaging, which does
the same.

Mimes can still write with their pen, which is a nice invisible white
color. I thought I would keep it in as I find that interaction funny to
have a Mime give someone just a blank paper, unknowing that there's text
on it.
Spraycans/Telekinesis/Circuits are also left unaffected because they
require actual effort to obtain (doing genetics, doing circuits, or
printing spraycans which take a lot of inventory space and is limited),
compared to paper which you can carry hundreds of papers around and is
bountiful across the station.

I thought this was attempted at least once, but I can't find any PR that
mentions it, so I'm shooting my shot to see if this is something we'd
want.

## Why It's Good For The Game

Mimes using paper is a lazy way to bypass their one job gimmick: Emoting
over talking.

If they get a job change, they can simply break their vow to access
paper writing abilities, so this doesn't affect that really. It more-so
hits the Mimes who uses the job for the free spells/healing
abilities/etc, and bypasses the downsides (im aware its harder to get
people to read paper than it is to talk to them, but you can literally
get the mute quirk and itll have the same effect without being the whole
job).

The point is, you don't get invisible walls for free; it comes at a cost
of not being able to talk to people. If you want to talk, then break
your vow, lose access to your Mime abilities, and remake it later when
the cooldown is over. You're not meant to do both.

## Changelog

:cl:
balance: Mimes can no longer write on paper without breaking their vow.
/:cl:

---
## [GribbaG/Nautical-Voyage-3](https://github.com/GribbaG/Nautical-Voyage-3)@[e112ae81ea...](https://github.com/GribbaG/Nautical-Voyage-3/commit/e112ae81ea49d4a9e1faa6de5797f7a6c611503a)
#### Thursday 2023-05-04 22:51:21 by GribbaG

Revert "fuck you kyle"

This reverts commit ec577988c077c80f35d9c70b8447deb141669b9a.

---
## [davimedio01/natural-computing-algorithms](https://github.com/davimedio01/natural-computing-algorithms)@[1a17599420...](https://github.com/davimedio01/natural-computing-algorithms/commit/1a17599420dcbcc29f5dea6d0dda17ca9f64d626)
#### Thursday 2023-05-04 23:12:08 by Davi Neves

Fuck up Luis, Luiz and Giovani for this shit.

I CAN'T FUCKING COMPETE! I JUST CAN'T FUCKING COMPETE! FOR YOU THREE: GET OUT FROM MY WORK . GET. FUCKING. OUT!

---

