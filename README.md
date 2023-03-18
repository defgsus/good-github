## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-17](docs/good-messages/2023/2023-03-17.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,224,141 were push events containing 3,318,370 commit messages that amount to 243,957,127 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [jntrnr/nushell](https://github.com/jntrnr/nushell)@[2e01bf9cba...](https://github.com/jntrnr/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Friday 2023-03-17 00:30:17 by Bob Hyman

add `dirs` command to std lib (#8368)

# Description

Prototype replacement for `enter`, `n`, `p`, `exit` built-ins
implemented as scripts in standard library.
MVP-level capabilities (rough hack), for feedback please. Not intended
to merge and ship as is.

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes
New command in standard library

```nushell
〉use ~/src/rust/nushell/crates/nu-utils/standard_library/dirs.nu
---------------------------------------------- /home/bobhy ----------------------------------------------
〉help dirs
module dirs.nu -- maintain list of remembered directories + navigate them

todo:
* expand relative to absolute paths (or relative to some prefix?)
* what if user does `cd` by hand?

Module: dirs

Exported commands:
  add (dirs add), drop, next (dirs next), prev (dirs prev), show (dirs show)

This module exports environment.
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs add ~/src/rust/nushell /etc ~/.cargo
-------------------------------------- /home/bobhy/src/rust/nushell --------------------------------------
〉dirs next 2
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │         │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
│ 3 │ ==>     │ ~/.cargo           │
╰───┴─────────┴────────────────────╯
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs drop
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │ ==>     │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
╰───┴─────────┴────────────────────╯
---------------------------------------------- /home/bobhy ----------------------------------------------
〉
```
# Tests + Formatting

Haven't even looked at stdlib `tests.nu` yet.

Other todos:
* address module todos.
* integrate into std lib, rather than as standalone module. Somehow
arrange for `use .../standard_library/std.nu` to load this module
without having to put all the source in `std.nu`?
*  Maybe command should be `std dirs ...`?   
* what else do `enter` and `exit` do that this should do? Then deprecate
those commands.

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
## [vittorioromeo/corrade](https://github.com/vittorioromeo/corrade)@[9d03dde6d3...](https://github.com/vittorioromeo/corrade/commit/9d03dde6d3bc453ee58b7901f2a9aa8d0574bd1e)
#### Friday 2023-03-17 01:13:50 by Vladimír Vondruš

Containers: don't use a bool in Triple NoInit test.

It's just too fucking painful with GCC 12 optimizations. Like, I
regularly got an XPASS for this code:

    Triple<float, int, bool> aTrivial{35.0f, 3, true};
    new(&aTrivial) Triple<float, int, bool>{Corrade::NoInit};

    CORRADE_EXPECT_FAIL_IF(!aTrivial.third(), "...");
    CORRADE_COMPARE(aTrivial.third(), true);

HOW ON EARTH can the boolean value fail on check, saying it's false, but
then in another check be true?! And of course no amount of trying to
change it to !(aTrivial.third() == true), or CORRADE_VERIFY(), etc.,
fixed it. The boolean always read as two different values on the two
lines. Amazing compilers, or UB, or I don't know what.

---
## [UandWhatArmy/WaveGeneration](https://github.com/UandWhatArmy/WaveGeneration)@[83e052dc04...](https://github.com/UandWhatArmy/WaveGeneration/commit/83e052dc04e0e6c104a80037d8844bc3d02c04f0)
#### Friday 2023-03-17 01:21:11 by UandWhatArmy

holy shit I want to shoot myself, fixed all memory leaks though

---
## [Allen050329/pytorch-uvm](https://github.com/Allen050329/pytorch-uvm)@[a269469982...](https://github.com/Allen050329/pytorch-uvm/commit/a2694699821be04e6a74760ba754911e714a5486)
#### Friday 2023-03-17 01:41:09 by Brian Hirsh

aot autograd refactor: make all synthetic base logic layered in a single location (#96235)

This  refactor doesn't significantly change LoC in aot autograd, but I think this nets out to making it clearer (interested in peoples' thoughts).

The idea is that I tried to re-write the part of aot autograd that deals with synthetic bases in a layered way, similar to how Ed wrote the logic for dedup'ing inputs: it happens in one place, and all of the downstream transformation in aot autograd don't have to worry about it.

Specifically, I added a new function `aot_wrapper_synthetic_base`, similar to the existing `aot_wrapper_dedupe`.

The benefit: none of the other code in aot autograd needs to think about synthetic bases (previously, synthetic base code was intertwined in several places).

The downsides: there are two.

(1) `aot_wrapper_synthetic_base()` needs to have its own epilogue. There is one particularly hairy case, where factoring the synthetic base logic to a single location was painful: If you have two inputs that alias each other, where one gets a data mutation, and the other gets a metadata mutation.

Ordinarily, metadata mutations are handled by the runtime epilogue, in `create_runtime_wrapper`. However, now that things are factored this way, the runtime wrapper operates only on synthetic bases instead of operating on the original inputs. For data mutations, it is fine to apply the data mutation to the synthetic base instead of the original input alias. But for metadata mutations, we **need** to apply the metadata mutation directly to the original inputs.

The way that I handled this was by tracking which inputs slot into this specific case (part of a synthetic base, and get metadata mutations), and updateing the flat_fn() that we pass downstream to return these updated inputs as extra outputs. From the perspective of downstream logic, these are real user outputs, that it can treat like any other user outputs. `aot_wrapper_synthetic_base` will know to grab these extra outputs and use them to apply the metadata mutations.

This was pretty annoying, but has the benefit that all of that logic is encapsulated entirely in `aot_wrapper_synthetic_base()`.

(2) input mutations are now performed on the synthetic base instead of the individual aliases.

You can see the original code comment [here](https://github.com/pytorch/pytorch/blob/b0b5f3c6c681896febbd9ff7ad7649b13def345d/torch/_functorch/aot_autograd.py#L1131) for details. We used to do the optimized thing in this case, and now we do the less optimized thing (copying the entire synthetic base, instead of the potentially smaller alias).

To be fair, we had no data showing that this optimization was showing improvements on any models in practice. I also think that the main reason anyone would ever run across this problem is because of a graph break - so if you care about perf, you probably want to avoid the extra graph breaks to begin with. I haven't added any warnings for this, but we probably could depending on what people think.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/96235
Approved by: https://github.com/ezyang

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[7cc6934eff...](https://github.com/DesmontTiney/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Friday 2023-03-17 01:46:47 by LemonInTheDark

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
## [tuurep/dotfiles](https://github.com/tuurep/dotfiles)@[c9d0113cd8...](https://github.com/tuurep/dotfiles/commit/c9d0113cd8ad2448516da0c242d1556af0e8f71e)
#### Friday 2023-03-17 01:52:30 by Tuure

Improve usage of :substitute

:substitute is so close to being incredibly useful, but it's so damn
tedious to write by hand...

Absolutely set gdefault, there isn't a single time i've ever used it
without the g flag... and if needed, adding g will toggle it off.

Though ignorecase+smartcase are very comfortable for search (/), they
are counterproductive for substitutes: preserving capitalization of
words that case-insensitively match the pattern is now impossible.

This plugin could be looked at to remedy the problem:
https://github.com/tpope/vim-abolish
+ the {} addition to substitutes (subversions) is really neat.

All I want from that plugin is the :%S , it actually kinda contains too
much stuff - consider forking and isolating the :%S

Question: does vim-abolish work with :set gdefault? From the nvim help
under gdefault:

DEPRECATED:
        Setting this option may break plugins that are not aware
	of this option.  Also, many users get confused that adding the /g flag
	has the opposite effect of that it normally does.

Bruh why you deprecating my favorite setting?

Overall this commit is a good starting point to make substitute really
comfortable to use, although it comes with the drawback of having to use
case-sensitive searches.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[42dd487728...](https://github.com/Paxilmaniac/Skyrat-tg/commit/42dd4877288a8476a2cd0f6ef9d936071b207d3d)
#### Friday 2023-03-17 01:55:34 by SkyratBot

[MIRROR] Station Trait: Spider Infestation [MDB IGNORE] (#19813)

* Station Trait: Spider Infestation (#73893)

## About The Pull Request

Hate having your cables eaten by mice? Nanotrasen have heard your
complaints and settled on a natural, _organic_, and eco-friendly
solution.

When this station trait is active, roundstart and event mouse spawns
have a chance to instead be replaced with duct spiders (both will exist,
it doesn't remove mice).
Duct spiders are largely harmless to humans, actively hunt other
maintenance creatures (such as mice), and have only one _tiny_ downside.

![image](https://user-images.githubusercontent.com/7483112/224345781-2627be98-67f2-4cab-ac40-c6c9b35ea909.png)

These mobs can also sometimes be spawned by a minor scrubber clog event.

As a side note, all spider basic mobs with AI (except Araneus) will now
try to automatically fill a small area around them with webs.

Also I made it so that mobs will ignore their random_walking behaviour
if they're engaged in a `do_after`, just in case.

## Why It's Good For The Game

Adds a little bit of variety to things which can slightly annoy you in
maintenance.
Spiders will automatically make places they live in look like spiders
live there.

## Changelog

:cl:
add: A station trait which sometimes populates maintenance with small
spiders. You can wear them as a hat if you wanted to have a spider on
your head for some reason.
add: Spider mobs will automatically start webbing up their environment.
/:cl:

* Station Trait: Spider Infestation

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Mr0maks/space-station-14](https://github.com/Mr0maks/space-station-14)@[581e8a0d12...](https://github.com/Mr0maks/space-station-14/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Friday 2023-03-17 01:57:54 by eclips_e

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
## [illuminatiorg/how-do-i-join-the-illuminati](https://github.com/illuminatiorg/how-do-i-join-the-illuminati)@[1412b95330...](https://github.com/illuminatiorg/how-do-i-join-the-illuminati/commit/1412b95330ef18bdbb44891bf6743f03cad9a3c4)
#### Friday 2023-03-17 02:19:33 by illuminatiorg

how I joined the Illuminati

HOW I FINALLY JOIN THE BAVARIAN MEDIEVAL  ILLUMINATI THROUGH THIS EMAIL ADDRESS illuminati.am@aol.com  AFTER BEEN SCAMMED NINE TIMES I got to give Testimony On How I Join The Illuminati; contact no whatsapp for membership . For privacy reasons I would not introduce myself here. Those of you that have been scammed severally on the process of joining Illuminati, I write onto you today, that I myself have been scammed severally and even duped on my quest to join Illuminati for 7 years but I never give up because I was a young scholar and I know the Illuminati do exist that I just have not meant the right link and believe I i'll have a huge benefit as a member of the Illuminati; that was sure, but each time I tried to join I keep getting scammed over and over. Due to the several scams people (even myself) went through in order to join the Illuminati many gave up, I pleaded with a professor in Harvard University and even brought to his notice the stress countless people are going through in order to join the Illuminati he saw my seriousness and he directed me to visit certain people in Freemason and I did,they directed me a top member of the Bavarian Illuminati Brotherhood, Prof Wormtail ,he called me on Telegram video call and gave me satisfying pieces of information that actually convinced me to proceed, he redirected me to the above email address and told me no membership on whatsapp and also told me never to contact any whatsapp for membership; at first i came to the knowledge that there are two portals to joining the Illuminati, and I have be an Online member throughout the 7 years but no benefit while the Bavarian Illuminati was still unknown to me until I met Prof Wormtail; he told me no membership on whatsapp that he will only redirect me after giving me the information I need know before applying, he redirected me to this email address >> ILLUMINATI.AM@AOL.COM << ( I have never seen this email before for 7 years that I have been searching) I quickly send a request to  the email to join the Illuminati and suddenly I got an instant reply and was take to a different chat platform where I did and me with the Bavarian recruitment master and after much dialogues I went through all the procedures. In 24hr two official black Mercedes cars came to my house according to my address on the membership application form, they picked me up, I was taken into a secret interview which I passed. I also signed a multi-billion Dollar contract form .The Rite was performed in the lodge in my country at 00:00 AM. A lot happened after the initiation ceremony; I visited many countries and was introduced to a lot of members; men and women, even teenagers in the Illuminati brotherhood. Am happy to tell you that I am a full member today through Prof Hunter, his whatsapp number above and as a member of Illuminati, I give this testimony in my honor to help those truly searching for the right part. ( contact the email above for a direct request to join the Bavarian Illuminati ) I shall show appreciation by continuously giving testimony to help those in the Light who want to go deeper into the Illuminati Brotherhood...NEVER GIVE UP JOINING THE ILLUMINATI ORGANISATION, JUST QUIT THE ONLINE MEMBERSHIP PORTAL AND AVOID CONTACTING WHATSAPP FOR MEMBERSHIP; IN GENERAL THE ILLUMINATI HAS NO COMMUNICATION WITH WHATSAPP>>> THE ILLUMINATI 2023 MEMBERSHIP FORM IS OUT. AS AN EDUCATED PERSON IT IS A WAY TO LEADERSHIP. EMAIL>>  illuminati.am@aol.com  << this is an instant reply official email address of the THE BAVARIAN MEDIEVAL ILLUMINATI PORTAL >>FOR DIRECT MEMBERSHIP REQUEST ,THE GERMANY INFORMATION AGENCY FOR MEMBERSHIP DIRECTIVES AND ENLIGHTENMENT. There are two ways to join the Illuminati organisation, the online membership is simply online and does not attract any benefit except the secret Bavarian Illuminati connection<<<< THE BAVARIAN MEDIEVAL ILLUMINATI MEMBERSHIP FORM IS OUT. A NEW AGE IS UPON US. Examples of Illuminati members: Serena Williams Prince Nicki Minaj Chrissy Teigen Jay-Z Nicolas Cage Rihanna Paris Hilton Taylor Swift Miley Cyrus, Selena Gomez Lindsay Loha. ARE YOU A BUSINESSMAN and WOMAN,POLITICIAN,ARTIST OR, ACTRESS,STUDENT,TRADER,WORKER,WHOSOEVER YOU MAY BE and your desire for WEALTH,INFLUENCE,FAME,POWER, PROTECTION AND CONNECTION.A FEW OF THE UNCOUNTABLE MEMBERSHIP BENEFITS ARE MENTIONED BELOW:
A Cash Reward of USD $5,000,000,.00, USD and above.
A New Sleek Dream CAR valued at USD $300,000 USD
A Dream House bought in the country of your own choice
One Month holiday (fully paid) to your dream tourist destination.
One year Golf Membership package
A V.I.P treatment in all Airports in the World
A total Lifestyle change
Access to Bohemian Grove
Monthly payment of $1million USD into your bank account every month as a member
One Month booked Appointment with Top 5 world Leaders and Top 5 Celebrities in the World. darken under the fall of the long night.
#illuminati #money #wealth #brotherhood #love #illuminati #tiktok #dubai #tiktok #usa #gucci #louisvuitton #ferarri #satan #japan #kesfet #t #humour #duet #jungkook #sad #asmr #jimin #bk #pov #we #iusedtobebeautiful #hiking #xyzbca #vhyfamily #akım #you #kesfet #work #featureme #keyk #vikin  #illuminati #money #wealth #brotherhood #love #illuminati #tiktok #dubai #tiktok #usa #gucci #louisvuitton #ferarri #satan #japan #kesfet #t #humour #duet #jungkook #sad #asmr #jimin #bk #pov #we #iusedtobebeautiful #hiking #xyzbca #vhyfamily

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[28f0050497...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/28f005049793e5ce558a24e3220cd90421920291)
#### Friday 2023-03-17 02:44:18 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [chtfc/Terminal](https://github.com/chtfc/Terminal)@[f7b0f7444a...](https://github.com/chtfc/Terminal/commit/f7b0f7444a101420665de1cf5400d02408226666)
#### Friday 2023-03-17 02:44:22 by Mike Griese

Spec for Elevation QOL improvements (#8455)

### ⇒ [doc link](https://github.com/microsoft/terminal/blob/dev/migrie/s/1032-elevation-qol/doc/specs/%235000%20-%20Process%20Model%202.0/%231032%20-%20Elevation%20Quality%20of%20Life%20Improvements.md) ⇐


## Summary of the Pull Request

Despite my best efforts to mix elevation levels in a single Terminal window, it seems that there's no way to do that safely. With the dream of mixed elevation dead, this spec outlines a number of quality-of-life improvements we can make to the Terminal today. These should make using the terminal in elevated scenarios better, since we can't have M/E.

### Abstract

> For a long time, we've been researching adding support to the Windows Terminal
> for running both unelevated and elevated (admin) tabs side-by-side, in the same
> window. However, after much research, we've determined that there isn't a safe
> way to do this without opening the Terminal up as a potential
> escalation-of-privilege vector.
> 
> Instead, we'll be adding a number of features to the Terminal to improve the
> user experience of working in elevated scenarios. These improvements include:
> 
> * A visible indicator that the Terminal window is elevated ([#1939])
> * Configuring the Terminal to always run elevated ([#632])
> * Configuring a specific profile to always open elevated ([#632])
> * Allowing new tabs, panes to be opened elevated directly from an unelevated
>   window
> * Dynamic profile appearance that changes depending on if the Terminal is
>   elevated or not. ([#1939], [#8311])


## PR Checklist
* [x] Specs: #1032, #632
* [x] References: #5000, #4472, #2227, #7240, #8135, #8311
* [x] I work here

## Detailed Description of the Pull Request / Additional comments
_\*<sup>\*</sup><sub>\*</sub> read the spec  <sub>\*</sub><sup>\*</sup>\*_

### Why are these two separate documents?

I felt that the spec that is currently in review in #7240 and this doc should remain separate, yet closely related documents. #7240 is more about showing how this large set of problems discussed in #5000 can all be solved technically, and how those solutions can be used together. It establishes that none of the proposed solutions for components of #5000 will preclude the possibility of other components being solved. What it does _not_ do however is drill too deeply on the user experience that will be built on top of those architectural changes. 

This doc on the other hand focuses more closely on a pair of scenarios, and establishes how those scenarios will work technically, and how they'll be exposed to the user.

---
## [khevy/tgstation](https://github.com/khevy/tgstation)@[e47c47a081...](https://github.com/khevy/tgstation/commit/e47c47a081f5919eea2b43453be7ac011ee2a492)
#### Friday 2023-03-17 03:11:57 by MrMelbert

You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed (#73983)

## About The Pull Request

If you are restrained, and placed into an unlocked labor camp
teleporter, you cannot instantly resist out of it. However the resist
timer is cut in half while unlocked.

## Why It's Good For The Game

Getting someone into the gulag teleporter is an incredibly un-necessary
pain in the rear because simply *spamming resist* turns it into a game
where you have to shove them in, then really quick go over to the
computer and slam the lock button. This is... kinda lame. A lot of new
player security officers get got by this, and I think it's sad. Inb4
"Skill issue"

## Changelog

:cl: Melbert
balance: If you are handcuffed, you can't instantly resist out of an
unlocked labor camp teleporter (however, resist time is halved).
/:cl:

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[9c8abee554...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/9c8abee5540f17951b1947a212b80521f1b36300)
#### Friday 2023-03-17 03:49:31 by IrkallaEpsilon

Matterforge Recipe expansion (#5168)

## About The Pull Request

This PR adds a few more matterforge recipes, some of stupidly high
difficulty and pointless rewards if miners are doing their job (looking
at you steel to gold), some of more usefulness (gold to plat, plat to
osmium). All require different temperature and energy ranges so they
cannot be rushed thoroughly. Not much thought was put into realism but
eh who cares, the matterforge is a cool thing ingame and its fun to use.
Some temperatures ranges (Steel to gold) are very narrow hence the use
of a gyrotron would be needed to get the most out of it. Or precise
heating (temperature can be raised to exorbitant amounts to prevent
heater cheese). This also would allow for Research to collab with cargo
for exports specially if dynamic prices ever come. In particular looking
at the gold to plat transmutation here. Plat can be exported by cargo in
which cargo can order more shit from.

I aint a good coder else I would add specific atmospheric conditions
needed, not just temperature (e.g. N2O must be present).
Reminded me a bit of TGs gas reactions but less gamy. 

## Why It's Good For The Game

More Matterforge recipes. Most relatively pointless and niche, some
allow science to give cargo something to sell, others can help with
theres an overabundance of Plat due to new miners. Mostly just giving
some extra uses for the forge. Oh and an alternative way to get plasteel
while sacrificing phoron sheets. Also bragging rights of effectively
turning iron (and carbon) into gold at specific temperatures and energy
levels on the particle focus.

A proper coder should check if these recipes are fine. Its 2:30 AM and I
thought this would just be neat.

## Changelog

:cl:
add: Various matterforge recipes
/:cl:

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[d261466765...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/d2614667654c0e35b2c906971ca94ece9e7b8629)
#### Friday 2023-03-17 03:49:31 by IrkallaEpsilon

Scattershot nerfs (#5175)

Sniper laser was tame.

## About The Pull Request

This is bullshit. Splurting out 180 damage with high AP with no delay is
not okay. Its as bullshit as most FCU we had. Mainly removed scatter on
high powered lasers and bloody stuns so the scatter lense may stay for
the mining tool (as there is no way to increase firerate on a
projectile.

## Why It's Good For The Game

Ever got hit at close range by the particle defender on main? Yeah that
is not fun.

## Changelog
:cl:
balance: Scattershot on high powered weapons nerfed. Heavy laser and
laser cannon beam and electrode now wont create submunitions. Stun beam
submunition count lowered.
/:cl:

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[b3a43f2b85...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/b3a43f2b8522c03ca976a1f7e72aa9deea97b350)
#### Friday 2023-03-17 03:49:31 by IrkallaEpsilon

Buffs Excav Laser Module (#5174)

## About The Pull Request

Buffs Excav laser module. Inconsisten with the one hit of rocks.
Hopefully this ammends it specially since scatterlenses are getting
removed (although nobody used them in combat yet.)

## Why It's Good For The Game

Scatter lense gone, legitimate mining tool needs a buff. The other
options (Phoron Bore) are a sick joke with how slow clunky they are to
use.


## Changelog
:cl:
balance: Meatier sound on excav laser. Higher excav power to
consistently one shot rocks.
/:cl:

---
## [gheskett/HackerSM64](https://github.com/gheskett/HackerSM64)@[ef38abb1c0...](https://github.com/gheskett/HackerSM64/commit/ef38abb1c0c2b39536e2a1a04003bc10556f5cb1)
#### Friday 2023-03-17 05:22:44 by Fazana

Frustratio funny fix 2 (#593)

* Update game_init.c

* fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[065a44bb43...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/065a44bb436047745e9ce003441d2edbe5fa2b88)
#### Friday 2023-03-17 05:55:47 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- Faster stdenv rebuilds: the third compilation of gcc
  (i.e. stageCompare) is no longer a `drvInput` of the final stdenv.
  This allows Nix to build stageCompare in parallel with the rest of
  nixpkgs instead of in series.
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more Frankenstein compiler: the final gcc and the libraries it
  links against (mpfr, mpc, isl, glibc) are all built by the same
  compiler (xgcc) instead of a mixture of the bootstrapFiles'
  compiler and xgcc.
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- Many other small `stdenv` hacks eliminated
- `gcc` and `clang` share the same codepath for more of `cc-wrapper`.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- This should allow each of the libraries that ship with `gcc`
  (lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`, much like https://github.com/NixOS/nixpkgs/pull/132343

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909
- https://github.com/NixOS/nixpkgs/pull/216136
- https://github.com/NixOS/nixpkgs/pull/216237
- https://github.com/NixOS/nixpkgs/pull/210019
- https://github.com/NixOS/nixpkgs/pull/216232
- https://github.com/NixOS/nixpkgs/pull/216016
- https://github.com/NixOS/nixpkgs/pull/217977
- https://github.com/NixOS/nixpkgs/pull/217995

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [JonnycatMeow/Unix-Static-Libs](https://github.com/JonnycatMeow/Unix-Static-Libs)@[36cc4126bb...](https://github.com/JonnycatMeow/Unix-Static-Libs/commit/36cc4126bb5976e1ec545e318793b24de8c2c935)
#### Friday 2023-03-17 06:43:12 by Jonathan Gomez

fuck you  .ds_store

https://stackoverflow.com/questions/107701/how-can-i-remove-ds-store-files-from-a-git-repository

thank you sooo much

---
## [j12bates/Rolling](https://github.com/j12bates/Rolling)@[6890a6a763...](https://github.com/j12bates/Rolling/commit/6890a6a7636ef40c97390f17c25880a1a219d0fd)
#### Friday 2023-03-17 07:32:46 by Jacob Bates

This Program Should Work

Yep! It should just work now! I've put in the exhaustive test, and I've
tested it on a couple known ranges, nothing special as I want to wait to
make this discovery with my friend tomorrow morning. Gosh, I can't wait!
But yeah, the only other things I need to do for this version 1 is
polish up the documentation, and maybe tweak the way the program outputs
stuff...

---
## [Pradeepsaman/project1](https://github.com/Pradeepsaman/project1)@[f12d884529...](https://github.com/Pradeepsaman/project1/commit/f12d884529e64d7b48eb70feca7e44ad9d40d158)
#### Friday 2023-03-17 08:35:49 by Pradeepsaman

Add files via upload

Business case:To predict whether patient has heart disease or not
as its a Binary Classification
Domain Analysis
• There are 14 columns in the dataset, where the patient_id column is a unique and random identifier. The remaining 13 features are described in the section below.

• heart_disease_present: 0-No, 1-yes

• slope_of_peak_exercise_st_segment (type: int): the slope of the peak exercise ST segment, an electrocardiography read out indicating quality of blood flow to the heart

• thal (type: categorical): results of thallium stress test measuring blood flow to the heart, with possible values normal, fixed_defect, reversible_defect

• resting_blood_pressure (type: int): resting blood pressure

• chest_pain_type (type: int): chest pain type (4 values)

• num_major_vessels (type: int): number of major vessels (0-3) colored by flourosopy

• fasting_blood_sugar_gt_120_mg_per_dl (type: binary): fasting blood sugar > 120 mg/dl

• resting_ekg_results (type: int): resting electrocardiographic results (values 0,1,2)

• serum_cholesterol_mg_per_dl (type: int): serum cholestoral in mg/dl

• oldpeak_eq_st_depression (type: float): oldpeak = ST depression induced by exercise relative to rest, a measure of abnormality in electrocardiograms

• sex (type: binary): 0: female, 1: male

• age (type: int): age in years

• max_heart_rate_achieved (type: int): maximum heart rate achieved (beats per minute)

• exercise_induced_angina (type: binary): exercise-induced chest pain (0: False, 1: True)

---
## [eduardojabes/screeps](https://github.com/eduardojabes/screeps)@[ebddeb670a...](https://github.com/eduardojabes/screeps/commit/ebddeb670a265504eac8e46d928f926503877dbe)
#### Friday 2023-03-17 11:35:57 by Tobias Wilken

End of an epoch, friendly TooAngel NPC died (#712)

It is a sad day in the screeps multiverse. The friendly TooAngel NPC from the neighborhood died.
Since the official release of the game it was spending joy, some action via quests and helped improving defenses, while it was just trying to survive somehow for years.
Rest in peace friendly TooAngel NPC.

Some cleanup as condolences:
- Improve code quality
- Extract pixel generation
- Improve on reservations
- Reenable boost config
- Fix issues on mineral handling
- Split up quests in host and player
- Include attacked creeps in the reputation
- Start with autorespawner

---
## [dbutenhof/pbench](https://github.com/dbutenhof/pbench)@[36cbbd1c8f...](https://github.com/dbutenhof/pbench/commit/36cbbd1c8f98ddd4c46ccd7405fbca6263245753)
#### Friday 2023-03-17 11:53:07 by David Butenhof

Fix operation synchronization (#3232)

* Fix operation synchronization

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
`state` and `message` columns. The `state` can be advanced through `READY`,
`WORKING`, `OK`, and `FAILED`, and a message can be associated with each
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

NOTE: Alembic schema changes for Operation table

After working with Pete get get alembic to successfully generate a revision
file for my changes, we realized what a pain it would be to migrate (and
test) an actual live database. We need to have a functional test framework to
stand up an "old" functional DB, upgrade it to the latest revision, and then
validate the correctness.

---
## [rd-stuffs/android_frameworks_base](https://github.com/rd-stuffs/android_frameworks_base)@[3301776659...](https://github.com/rd-stuffs/android_frameworks_base/commit/3301776659e1d1078333c3624c8fbef5ab75f3cc)
#### Friday 2023-03-17 12:26:17 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [insertnamehere123/cmss13](https://github.com/insertnamehere123/cmss13)@[e5ab42dba0...](https://github.com/insertnamehere123/cmss13/commit/e5ab42dba06e537df5c146169971dd8418f2ce55)
#### Friday 2023-03-17 12:37:08 by boskoramen

Consolidates some XSS under hivecore (#2738)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Spawn pool and evo pods are removed and their functionality is
umbrella'd under the hive core. Sprites still exist though.

# Explain why it's good for the game

"Roleplay" has become an increasingly more popular and touchy subject
within the community as of recently. I, wholeheartedly agree, that
roleplay is an important aspect of the game, and there are ways to
improve it. One of these ways is through immersion. In this MR, it is
intended to increase player immersion.

One of the most memorable and haunting scenes in Aliens was when they
reached the hive and they found the bodies. This very unique and
cinematic scene was often able to be replicated in CM, with the marines
busting open the hive and finding all the chestbursted bodies of their
comrades. Roleplaying this out was commonplace. "Dear God... what did
they do to you..." or acting out in disgust are just a few of the many
ways having bodies in the hive positively impacted the game.

XSS was a failed attempt at spicing up the xenomorph gameplay loop at
the expense of immersion and should be at least somewhat reverted while
keeping balance in mind. A brief discussion with many prominent
xenomorph players, including those most experienced in queen, have not
particularly expressed favor to XSS either.

To start, let us remember why XSS (xeno special structures - hive core,
evo pods, morpher, pool, etc) was added.

https://docs.google.com/document/d/19_zDUmLdxpUzxj-GuWu7F4bSj4zBYzmZ39s_N5X7kQ0/edit
- This is the original development document for XSS.
Let us examine the major points:
1.Introduce a way for Xenomorph players to recycle - This idea was never
reached.

2.Reduce Xenomorph attrition - Grand objective was unsuccessful. Very
little changed.

3. Offer new avenues of play "by reducing the punishment of xenos dying"
- This never happened. Dying was still just as punishing, especially
with facehug nerfs.

The spawn pool - The idea of the spawn pool was successful and has
remained unchanged since. I would argue, however, it is not immersive.
Xenomorphs do not have bright, glowing, acidic pools in their hives.
(Yes I know there was a comic with a pool, and this is not how it was
used)

Egg Morpher - These used to be TURRETS. They are no longer turrets, and
their sprites have been broken for almost 4 years (the bodies put inside
of them used to show their face in the little purple part) They are
currently defunct facehugger reservoirs. I am in favor of removing them,
but I would argue that is a balance issue (number of huggers in play)

Evolution Pod - It was intended for these to be able to be eaten in
order to evolve. They haven't done this for years. Why do we still have
them? They take up 18 spaces of precious hive weeds, provide light,
(xenomorphs HATE light) and wherever a hive core is built, these are
also built. We can just merge them with the hive core because there is
no reason to have them anymore.

This PR currently completely removes the spawn pool and evolution pod
from gameplay, while reimagining their functions for current balance.
This PR is not intended to change balance in any way.

All functionality from the spawn pool in regards to "pooled" larva has
been given to the hive core, and they are now called "burrowed" larva.
Chestbursts now give two larva, this is to be kept with current balance
of two xenos per capture.

Evopod functionality and evolution speed boost was merged with the hive
core.


# Testing Photographs and Procedure
n/a


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

:cl: TheDonkified
del: Evo pods and spawn pool are removed.
add: Hive core directly affects evolution speed and is where burrowed
larva spawn from now on.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [GeraldR63/AstroNavi](https://github.com/GeraldR63/AstroNavi)@[a4e0138759...](https://github.com/GeraldR63/AstroNavi/commit/a4e01387591af982073eb0520e0846ad5c5dd2b5)
#### Friday 2023-03-17 12:53:41 by DO4ZWO

Well, Shaka, when the walls fell.

Holy Moly. I have it. Now the calculation of GHA, SHA, DECLINATION for a given Date and Time corresponds to the Nautical Almanac. Shaka! Added calculation mode for DIP and Refraction. You can take the figures from Nautical Almanac or those calculated by this software. Both works. Hot fix for a fatal error came with some changes to the hard wired CB data. Added tooltips to all of the inputfields and checkboxes. Fixed TZ issue. My recommendation is: User a watch at TZ 0 and set System Time of your Android to GMT. I made one huge mistake because the emulator run at GMT and I tried to  get correct figures for local time. Shit happened. Seem to work now.

---
## [phorgeit/phorge](https://github.com/phorgeit/phorge)@[b33e373503...](https://github.com/phorgeit/phorge/commit/b33e373503c6f64118ec77bb34dc8224d54da4e3)
#### Friday 2023-03-17 12:56:28 by Valerio Bozzolan

Drag & Drop: set a link as external

Summary:
Rest assured: external links remain evil, by default.

Don't adopt them randomly by induction.

Whether you believe it or not, this specific external
link merited some deep thoughts on Phorge:

- https://we.phorge.it/T15172

So, whenever you use a mouse, a finger, or whenever we have
a confirmation dialog or not to prevent onblur disasters,
this change is probably consistent with common expectations.

Having said, external links remain evil - by default.

Closes T15172

Test Plan:
- Drag & Drop a File on a Remarkup text
- click on the link inside the popup
- it opens in a new tab (without risk of form loss)

Reviewers: O1 Blessed Committers, avivey

Reviewed By: O1 Blessed Committers, avivey

Subscribers: speck, tobiaswiese, Matthew, Cigaryno

Maniphest Tasks: T15172

Differential Revision: https://we.phorge.it/D25077

---
## [kdmukai/seedsigner](https://github.com/kdmukai/seedsigner)@[d2a657f2d4...](https://github.com/kdmukai/seedsigner/commit/d2a657f2d43c6e77e9c48cb1f859e8f4984a5f00)
#### Friday 2023-03-17 13:23:29 by Marc G

Various edits B4 upstream submission

After a long hiatus, I have finally completed my proposed changes to the software verification section of our readme.

The verification focuses on keybase.io now storing and verifying the 3 online properties (seedsigner.com, twitter.com/seedsigner and github.com/seedsigner)

This makes the key more secure, easier to import and generally less hassle. its also revokable.  

There is more detail about how/why in the expand blocks, but It was suggested to me to keep the instructions straightforward (ie do this and now do that) , so I have reduced focus much on the why. 
However, some basic "why & how" has also been placed in new collapsible sections, at the end of each step. 

Later on, I want to add color to the collapse sections so that they show a natural boundary, but so far that markdown code is elusive to me. ;) 
Done is better than perfect....
The same for getting my external links to open in a new tab/window. sigh. Markdown is ... well....tricky. 

I can make the screenshots smaller. please comment on their size.


The Verification is done in 3 steps:
1. import the public key
2. Verify its the correct key by verying it and then comparing the Key ID to Keybase.io/seedsigner. If it matches, then its the real seedsigner project person that signed.
this is arguablly the most critical step of verifying and hence we ask the user to check for themselves that the key ID from verify is the same as on keybase.io. Hence the Key ID's are blurred in the screenshots. We dont want the user to compare the screenshots to each other. we want them to compare their result to their browser. 

3. Verify that the other files (at this stage just the .zip file) are also not altered. This does a comparision of the various files actual and expected hashes.

If all is well here, then tell the user about their success :). 
Explain the warnings, which ones are benign, and what to do if verification fails.


Lastly, "Write the software to the MicroSD' section - 
I have got draft text for this, but havent published it yet. 
The verify PR is big enough !!

Please review for my PR flow and clarity, I do still want to improve the formatting,  but wanted to get everyone's thoughts before messing with the detailed formatting and line breaks, which are especially painful!

FYI - I have done my screenshots using layers, so it easy to edit in the future. I think they

---
## [AdobeDocs/workfront.en](https://github.com/AdobeDocs/workfront.en)@[6da7a06774...](https://github.com/AdobeDocs/workfront.en/commit/6da7a06774862afedd1a9b9f2383fd12eeaa31f4)
#### Friday 2023-03-17 15:26:16 by Courtney Christensen

Merge pull request #1208 from AdobeDocs/i-hate-my-life

merge me

---
## [Tsunamico/Tsunamico-cmss13](https://github.com/Tsunamico/Tsunamico-cmss13)@[639765b0c6...](https://github.com/Tsunamico/Tsunamico-cmss13/commit/639765b0c69faddeec405080ab4fde79503fcf5d)
#### Friday 2023-03-17 15:40:02 by Skegal

Loadout - Sniper facepaint (#2015)

# About the pull request

This PR is here to add the sniper facepaint into the loadout for 4
points like the skull facepaint.
 
 I tested it and it worked well as expected.
 
I saw a lot of marines asking the sniper for their bodypaint recently,
and i thought, that since it doesnt change anything game-wise we could
give it on the loadout, as the sniper isnt always here and sometime even
throw it to the trash...also people wont annoy the sniper for his paint
too.

((sorry for the webedit i ran into some problem doing the PR with visual
code studio))

# Explain why it's good for the game

I think its good because it add more customisation to characters with
one more good looking facepaint and like i said earlier, i saw some
marines asking the sniper for it (talked about it on discord and people
seemed to be ok with it)


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

i posted the pic here
https://discord.com/channels/150315577943130112/1054515157923020842 (if
in the pic you see the facepaint above the other paint its normal, i
tested it with the code above the other but it should appear under the
skull paint in the pr)

</details>


# Changelog

:cl: Skegal
add: Added Full Body Paint to Loadout
/:cl:

---
## [googelreviews/s3fs-fuse](https://github.com/googelreviews/s3fs-fuse)@[5358606aa5...](https://github.com/googelreviews/s3fs-fuse/commit/5358606aa56d26cce5e26412e73417eec1146856)
#### Friday 2023-03-17 15:52:26 by buy google reviews

buy google reviews

                                  BUY GOOGLE REVIEWS
 
 
 
 

Who doesn’t want to Buy Google Reviews? And if you are looking for this then be relaxed, you are at the right place. If you are new in the business then you will have to face a lot of difficulties. As we all know, creating credibility in online businesses is much more difficult. No matter what niche you are working with we’ll help all types of business houses to get google reviews. No matter what they are verified, positive, cheap, negative, or a 5-star. Our every single review is safe and organic. In today’s world millions of people are buying google reviews for their GMB page. So that they can boost their sale. It’s proven that online reviews especially google reviews help to increase online sales.
  
                     	How Google Reviews Help To Grow Your Business


             	




If you are a newbie and didn’t spend a dime on marketing then google reviews will be the best choice to give your sales a high fly. By buying google reviews for your business page you can easily get the first-page rank on local SEO. Not only that by using google reviews you will also create a balanced playing field for your brand, make it popular and help your mom-and-pop operations.
Telling the stories of your customer’s google reviews allows your products to be good. Without downloading any app people can share their thoughts just like that. One undoubtedly should buy google reviews rather than spend bucks on marketing campaigns.
Apart from this google reviews create social proof about your products far better than any other costly marketing ads. And that’s how online reviews help to grow an online business. 
 
      	                               Why You Should Choose Us..?


 
                                         	  


Google reviews are the most trustworthy and that’s too even without spending lots of money you don’t need to know slick marketing to buy google reviews because there are hundreds of dedicated sellers to help you purchase google reviews at an affordable price.
Simply you can take your customer’s review by sending them a link from your Google My Business online review page. But when you have no customers yet. And that’s high time when you are in bad need to buy a google review for your GMB. These are the only online testimonials that will help customers to take any decision to buy any products from you. And that’s how google reviews create online awareness among buyers and boost your sales at the very early stage of your business and help to increase your business online.
 
                                               
 
How Do We Work:
The main benefit to buy google reviews is it can boost the local ranking of your business. And the local searches or rankings help reach your products to your local customers in real-time.
Verified reviews: You purchase google reviews for your GMB and you want your every review would be verified and permanent because verified reviews can impact your business positively by increasing new customers.
5-star positive reviews: Before buying a product, people want to know about the satisfaction level of their customers experience. When they see lots of positive 5-star reviews on your google profile saying good things about your products, they will be more interested to buy your products.
Local reviewer profile: We help you buy google reviews in USA or UK along with ensuring the reviewer's local profile meaning if your business is located in USA or UK then we give you google my business online reviews from the same profile.
No bots, permanent reviews: We have thousands of real profile located various locations in the world. We don’t use any bots or software. We manually do human process to buy google reviews verified, 5-star reviews, positive, cheap, or negative.
 






                      	





















Ranking your business locally is the one of best benefits of buying google reviews. It also helps to reach your products to the customers in real time.
Varified review: When you purchase google reviews for your GMB and you want 100% verified reviews it helps your sales to touch the sky.
5-star positive reviews: Everyone who shops online want to know customer satisfaction by using google reviews you will get a lot of 5-star reviews which will attract the attention of the customers and make them buy your products.
Local Reviewer Profile: when we help you to buy google reviews in countries like the USA or Canada that assures that you will get authentic reviews from the profiles of the USA or Canada
No Bots, Permanent Review: We have millions of profiles throughout the world to get you 100% original reviews. No bots, no fake we assure only permanent review.

---
## [Moonshanks/cmss13](https://github.com/Moonshanks/cmss13)@[d40fdb9101...](https://github.com/Moonshanks/cmss13/commit/d40fdb91011bb0aa4053a9386311ed131e0ae6ac)
#### Friday 2023-03-17 15:58:01 by NewyearnewmeUwu

nukes the last default ss13 door on big red (#2830)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
i thought i fixed this?
didn't i guess
removed the weirdass ss13 door in the OR theater's observer area yeah
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
it's ugly
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
maptweak: removed yet another default ss13 door from big red
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [nm-pbl/SB-PBL-GP--6724-1677996344](https://github.com/nm-pbl/SB-PBL-GP--6724-1677996344)@[2984edcbd3...](https://github.com/nm-pbl/SB-PBL-GP--6724-1677996344/commit/2984edcbd3f89a2b3897fe54a534829acd66c32c)
#### Friday 2023-03-17 16:17:08 by PURUSOTH1703

Add files via upload

An empathy map is a tool used to understand the perspectives and experiences of a particular user or customer. In the case of vehicle management, an empathy map can help you understand the emotions, thoughts, and behaviours of someone who is responsible for the rental vehicle.

---
## [Kubic70/BlueMoon-Station-13](https://github.com/Kubic70/BlueMoon-Station-13)@[bc48a6eafc...](https://github.com/Kubic70/BlueMoon-Station-13/commit/bc48a6eafcf9afedfc419afaa982dd15339a94aa)
#### Friday 2023-03-17 16:51:01 by Darius

Add vampire ability permission check

Adds a new mob proc that allows checking if vampiric abilities should function. Allows easily checking anti-magic, trait holy, garlic necklace, garlic blood, and staked status.

Bloodfledge actions and coffin healing will now use this check. Flight potions will warn bloodfledge quirk users before allowing consumption.

---
## [IBM/openapi-validator](https://github.com/IBM/openapi-validator)@[947c9ceb04...](https://github.com/IBM/openapi-validator/commit/947c9ceb04d7af15c6655285bfdf32e5a18192be)
#### Friday 2023-03-17 17:22:04 by Dustin Popp

chore: update prettier version and adjust code (#570)

Even though it's a perfectly compatible change, I thought the new version would be a good
opportunity to update our linting rules which is something I've wanted to do for a while.

This commit bumps our `prettier` version to 2.x, which includes some beneficial defaults;
primarily, enforcing trailing commas. I realize trailing commas may not be viewed as
"beneficial" by all :) but I think they are valuable and the AirBnb JS style guide (which
we try to use as our source of truth, not that we're following it perfectly) requires
them. Happy to debate the change but thought I'd propose it because the lack of trailing
commas has bugged me for a while haha.

Signed-off-by: Dustin Popp <dpopp07@gmail.com>

---
## [Gnucash/gnucash](https://github.com/Gnucash/gnucash)@[b4b8431984...](https://github.com/Gnucash/gnucash/commit/b4b843198421aef9332ad1cae348a4acacfa5586)
#### Friday 2023-03-17 17:42:34 by John Ralls

Bug 798778 - GnuCashquits abruptly when attempting to edit options…

for certain reports.

Those reports being ones using complex options, apparently because
the callbacks weren't protected from Guile's garbage collector.

So replace the anyway ugly hack of a void* with a std::any wrapping
a class holding a std::unique_ptr with a custom deleter. The
constructor calls scm_gc_protect_object on the SCM containing the
callback and the custom deleter calls scm_gc_unprotect_object. The
copy constructor, required for std::any, makes a new std::unique_ptr
and calls scm_gc_protect_object again ensuring that the protect and
unprotect calls are symmetrical.

Meanwhile std::any hides the Guile dependency from all the classes
that don't need to know about it. The only ugliness is that there's
no good place to put a common implementation of SCNCallbackWrapper so it's
repeated in gnc-optiondb.i and dialog-options.cpp.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[916360eee8...](https://github.com/mrakgr/The-Spiral-Language/commit/916360eee86e9509228ada4cf9d79549ea417b9b)
#### Friday 2023-03-17 18:26:12 by Marko Grdinić

"8:50am.

///

Hi Marko,

Thank you for your interest in our .NET Developer vacancy.

The first step in our hiring proces is for you to take an online skill assessment.

Completing this assessment will help you demonstrate the skills required for this role, so that we can focus on your abilities rather than on comparing CVs. This removes potential bias from the process, giving all candidates an equal opportunity to shine.

You can start the assessment by clicking here: [sic]

About us:
We are a software house with a 15-year history, a rich portfolio and projects all over the world. We build our brand on professionalism and flexibility in delivering software solutions. We are not afraid of unconventional ideas and value innovation and imaginative change.

Our offer:
○ An attractive salary
○ Large freedom and real influence
○ No unhealthy competition, team approach to meeting challenges
○ Remote or hybrid work model
○ Company apartments in cool cities across Europe: work and enjoy a memorable getaway

///

Got a reply on AngelList. Finally, fuck. Let me chill a bit and then I'll do the assesment later. This company offers 50-90k pounds salary.

Fail or win, these are the kinds of 'exercises' that I should be doing right now. I should be innundated in them.

Forget that for now. Let me read Fran's new chapter.

9:30am. Ok, let me finish the Mimicry Girls latest raw and then I'll start the assessment. After that I'll move on to getting the CFR algorithm to work.

https://support.testgorilla.com/hc/en-us/articles/9027758023579

Is this going to be some kind of a quiz?

Hmmm, maybe instead of my resume being good, they just send these out to everybody? If so, that's fine too.

...Wait, it seems I'll be expected to make recordings. That is new.

Let me turn on the webcam and mic.

10:05am. This test is pretty nasty. It tests me on difficult, but dumb trivia of the .NET ecosystem. I already feel like skipping this compnay, but let me just keep going.

https://www.tutorialsteacher.com/csharp/csharp-hashtable
> Elements are stored as DictionaryEntry objects.

Whops I got this wrong, amongst many others...

The ASP.NET questions I was just guessing blindly. No way am I getting a job here, they aren't looking for a person like me. They are looking for some monkey who memorized the .NET API.

10:30am. I didn't think it would be like this. If I get a reject here, I'll go the other way if I encounter tests like these instead of wasting my time on them. At least the Green Hills one from over a year ago was interesting to do the first time even if it was ultimately futile, but this one tests me on things that would be better left to the IDE.

10:35am. Ok, I'll learn from this. The reason why I got a response so quickly is because the company has this kind of weeder test and not much else. A lot of the choices had errors in them, like they were written by a bored engineer in an hour or two.

These companies really do treat candidates like trash.

10:40am. Let me take a short break and then I will do some actual programming. I need to take what I have an turn it into a player.

https://m.mangatown.com/manga/tower_of_god/c551/

Tower Of God is resuming so let me read it.

10:50am. Ok, in the future, unless accept starts with an interview, or some kind of a project that I could do properly, I am definitely going to be a avoiding companies like these.

11:20am. Let me resume.

Ugh, my heart is not really into doing my portfolio project. What I really want is to get some acceptance.

I hate thise waiting period before these compos ignore me.

But focus me. I'll get into it once I start.

11:35am. I am pissed at being quized like this. It makes me look like I barely have a clue how to program.

The embarassing thing is that I made a mistake on one of the English proficiency questions (out of 20). This will go into my dark history.

11:45am. You know what, forget this. I want to apply to companies. I want them to suck my cock through interview invites.

Right now I am applying to Otta and it is breaking my balls.

The stupid thing offered to import my LinkedIn profile, but didn't take in the data correctly. Now I have to waste time doing it by hand.

https://app.otta.com/jobs/REhZMTky

I am just applying at random here, but the application is asking me:

> What experience do you have that aligns with what we're looking for in this role? *

It is only now that I've bothered actually looking at the description and see that it is a language related role.

12:25pm. Let me apply on LinkedIn next.

> What is your expected base salary? (Please specify currency and pay frequency)*

I've started to adapt to this question and started putting 1$/year everywhere.

My god, applying at this site takes a long time. WTF.

https://www.kaseya.com/careers/jobs/id/4776161004/?gh_jid=4776161004#application-form

Maybe I should be tailoring my resume to these companies.

1:05pm. It is not really worth it. If the resume is good, then the portfolio and everything else does not matter. I should be getting invites purely based on experience.

My real job right now is to apply to companies and get that kind of experience, not make Youtube video or redo the CFR algo for the 100th time.

1:10pm. Let me just apply to Barclays as well and then I'll go have breakfast.

https://apply.jobs.barclays/careersection/careersection/candidateacquisition/flow.jsf

This is the worst web page ever. Like hell will I spend time filling in the shit from my CV here again.

1:20pm. https://apply.jobs.barclays/careersection/careersection/candidateacquisition/flow.jsf

This site is fucking with me to an extreme degree. It is so slow and unresponsive on top of not accepting my data when I try to save. Fuck it.

https://www.linkedin.com/jobs/search/?currentJobId=3480126268&geoId=91000000&keywords=f%23&start=25

Credit Suisse might go under so let me avoid it.

https://www.linkedin.com/jobs/search/?currentJobId=3497477128&geoId=91000000&keywords=f%23&start=50
> Do you want to improve Danish businesses with your tech skills? Are you passionate about tackling business challenges and turning solutions into software? Then you might be the next colleague we are looking for. If, furthermore, you are enthusiastic about being a trusted advisor, about architecting IT solutions on a whiteboard, about high quality C# and about writing parser combinations in F#, you will feel right at home in Copenhagen Software.

Parser combinators.

1:40pm. I am way overdue for breakfast.

I've realized something. There is an endless supply of .NET jobs out there so I can just shotgun the resumes to them and get a sense of how effective it is.

1:45pm. I am putting in too much effort into trying to fit in at those dinky startups. To get an F# job, it is like looking for some hidden treasure.

Instead I should be doing this more rapidly. LinkedIn should be my first choice for everything.

2:10pm.

///

Pronouns:
He/him
She/her
They/them
Xe/xem
Ze/hir
Ey/em
Hir/hir
Fae/faer
Hu/hu
Use name only

Custom
Let the employer know what pronouns you use so that they can address you correctly.

///

Lmao. This is the first time I've encountered this. Is this a joke?

2:30pm. https://www.linkedin.com/jobs/search/?currentJobId=3473491164&f_WT=2&geoId=103644278&keywords=.net&location=United%20States&refresh=true&sortBy=R

Oh, Athropic is hiring, and this is remote.

> $270,000 - $445,000 a year

Holy shit.

3:45pm. Done with applying. There are many duplicates, but I must have applied to over 30 different places, not counting the AngelList applications. This should give me some feedback on my resume at the very least.

What I can do now is give up. If it won't go through, it won't go through. I'll just have to look in the local area, and through my relatives if I want to get something.

Let's give it a few months. I'll finish my portfolio project by that time, and maybe give A Team or interviewing.io a try.

Now, let me do it professionally. I've noticed that Angular is required in a lot of places, so when I am done I should study that. For now, let me just focus on my portfolio.

4:30pm. > We have recently been receiving an overwhelming response to our adverts and we will do our best to let you know the outcome of your application, however if you have not heard from us within 14 days of your submission, then please assume that you have not been shortlisted on this particular occasion.

Got this email.

Damn it, just why is this happening? My decision that I had to get a job had absolutely nothing to do with the wider economy, I just got the sense it was time, but I could not have picked a worse timing.

Nevermind this, nevermind this. Maybe in the future AI will be able to replace HR departments. It seems more likely that it would programmers.

My plan if I get an interview invitation is to ask ChatGPT for advice.

This particular round today is just so I can get a sense of where my resume stands. Do I have to increase the amount of bullshit on it or not?

4:35pm. Let me program.

...I wish there was a way to get ahead in this world with just my own power.

4:45pm.

```fs
type PathProb = float * float
// type IChance<'card> =
//     abstract member chance : choices: 'card [] * cont: ('card -> float) -> float
type IAction<'model,'action> =
    abstract member action : model: 'model * actions: 'action [] * path_prob: PathProb * cont: ('action * PathProb -> float) -> float
// type ITerminal =
//     abstract member terminal : float -> float
```

Let me leave this like so for now.

Right now, I am off my game.

4:50pm. It is all the fault of that stupid quiz for gouging my insecurities.

5pm. Got a reject from TheoremOne. Fastest time that has ever happened. What a downer. Well, they are probably looking for US guys, and I just missed that requirement or something like that. Or maybe they already hired somebody.

I need to keep going. I must keep going.

5:40pm. My heart is not into it, so I am not making making progress.

6:15pm. Done with lunch. My heart feels heavy so I can't muster any energy to move forward.

This is ridiculous. Just is why is finding work so hard in this day and age? That is how it feels.

It is all that quiz's fault that I feel like this.

6:50pm. If I think about it, this is like the second time this has happened. With Branimir, he also heckled me about the details on the app he was working on. For some reason he never got into my background even a little and we were just circling the drain about validating some schema or some nonsense like that.

I am going to make a rule about not answering any of the tedious API details in the future during the initial round. I just feel so lost during these interviews. What is right, and what is wrong, I have no idea.

But there is a pattern that whoever has contacted me to 'help' me, or like this particualr company today who sent me an accept, or the people who recommended me their own places, they have all been busts. When Branimir contacted me, I was expecting he would be sending me some actual work, imagine my disapointment when he just wanted to act as a middleman.

I need some actual work, not these jokers.

it has been in the past that people have contacted, giving me shitty advice and whatnot. Think about the UPMEM guy for example. That was a waste of time. And there were people before him.

I need some actual contacts who are worth keeping. Who can send me jobs that pay, instead of advice and opportunities.

7pm. There is no way around it. I am going to simply have to keep going until I see a pattern that I can take advantage in these job applications.

///

>>92147265
Today I applied to some .NET startup on AngelList and got an accept right away, and got a sent a link to some quiz. I was thinking it would be some HackerRank tier question which would have been easy enough to work out from first principles, but it was much worse. The stupid quiz was full of API trivia - multiple choice questions where some library function was renamed, and I was asked to spot the right one. Or I was asked to pick the code segment that does what it says in the description, out of very similar choices.

Fuck!

These questions I could do very easily with access to the docs and an IDE, but I had 10m to do 16 of them and I actually times out on the last 6.

Just who the fuck is going to remember the trivial details of the .NET standard library? Hell the last time I read a text file from disk must have been years ago! I never even used the non-generic Hashtable in my life, I always use the Dictionary! I really wish that AI could replace the HR departments at these companies.

///

https://boards.4channel.org/g/thread/92147265/twg-tech-workers-general#p92148614

///

>>92149118 (You)
Welcome to every contractor-style interview ever.

///

Shit, am I going to have to deal with this if I join A Team? I hadn't realized this was a contractor-style interview.

7:20pm. Let me close here.

> Completing this assessment will help you demonstrate the skills required for this role, so that we can focus on your abilities rather than on comparing CVs. This removes potential bias from the process, giving all candidates an equal opportunity to shine.

I'll forgive this company for messing with me like this. Focusing on my abilities is it? Going by the results, you'd think I don't know how to read a file from disk."

---
## [QuacksQ/TESTING](https://github.com/QuacksQ/TESTING)@[a3451b7fe4...](https://github.com/QuacksQ/TESTING/commit/a3451b7fe4ff60e0cb6cc4f2bd6d20543f455940)
#### Friday 2023-03-17 18:37:01 by san7890

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
## [QuacksQ/TESTING](https://github.com/QuacksQ/TESTING)@[db7534d6da...](https://github.com/QuacksQ/TESTING/commit/db7534d6dabf0127c87b291eae4063b6f77d36e4)
#### Friday 2023-03-17 18:37:01 by LemonInTheDark

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
## [ShadowOpsCross/ThatsIT](https://github.com/ShadowOpsCross/ThatsIT)@[685ba9064f...](https://github.com/ShadowOpsCross/ThatsIT/commit/685ba9064f44b7d2b25eec243b237d27cfd0a3f7)
#### Friday 2023-03-17 18:37:23 by Arsenii

Merge pull request #2 from ShadowOpsCross/workflows

Fuck you 1

---
## [eorus/dwm](https://github.com/eorus/dwm)@[67d76bdc68...](https://github.com/eorus/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Friday 2023-03-17 18:49:02 by Chris Down

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
## [prodirus/TaleStation](https://github.com/prodirus/TaleStation)@[d972612ad8...](https://github.com/prodirus/TaleStation/commit/d972612ad8dd951c1802a118b424ff029223505b)
#### Friday 2023-03-17 18:56:10 by TaleStationBot

[MIRROR] [MDB IGNORE] It Came From Outer Spess: Adds midround changelings, delivered by an absolutely disgusting changeling meteor (#4412)

Original PR: https://github.com/tgstation/tgstation/pull/73018
-----
## About The Pull Request

Adds a new dynamic midround opportunity and random event - Space
Changeling.


https://user-images.githubusercontent.com/28870487/215284465-f5c5c1b1-b83d-471a-89be-1b65a4d2f2d4.mp4

If you are fortunate enough to recieve this role, you will be stuffed
into a changeling meteor and hurled at the side of the station. With no
crew identities, no access, and no equipment, you'll have to rely on
your **free** organic space suit and armblade to infiltrate the station
and get settled.

With no disguises to fall back on, the midround changeling experience
may lead to some very unfavorable situations. It's not unlikely that
you'll be spotted making your way inside, or that someone will see the
impact site and cause a panic. This role is not easy, but keep in mind
that you also have nothing to lose in the event that you use Lesser
Form/Headslug.

Aside from the starting circumstances, you have the same objectives and
capabilities as a roundstart changeling. Getting inside of the station
will be the hard part, but from there you can do what changelings do
best and blend in.

<details>
<summary>A brief note on the free stuff you get:</summary>
<br>
You get the organic space suit and armblade for free. The space suit is
absolutely vital, but I decided that the armblade should be given for
free as well. It's necessary for breaking open windows or airlocks and
getting access to the station, since otherwise your options are limited
to arrivals/departures. Having to pay a 2 point tax to avoid walking
naked into the main hallways of the station and getting gibbed is lame,
and with the added difficulty of the role I think it's fair.
</details>

Also, this is my 100th PR here! :)

## Why It's Good For The Game

Adds midround changelings in a WAY COOLER way than just making a random
crew/new arrival a changeling.

Lets people experience Hardmode Changeling, and test the adaptability
and flexibility of the most versatile antagonist even harder than
before. Losing the option to bypass the whole shape-shifter thing by
disguising as your crew identity presents a welcome change to the
formula.

Adds a teensy bit more midround variety, so we stop getting Nightmare At
The Thirty Minute Mark every round.
## Changelog
:cl: Rhials
add: Midround changeling spawn event.
add: Changeling meteor. It has a present for you.
/:cl:

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[8b4676e25b...](https://github.com/git-for-windows/git/commit/8b4676e25b5fac285214b43e032406f53cc712bf)
#### Friday 2023-03-17 18:59:18 by Johannes Schindelin

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
## [Maetrim/DDOBuilder](https://github.com/Maetrim/DDOBuilder)@[f3dd083b9f...](https://github.com/Maetrim/DDOBuilder/commit/f3dd083b9f136255e3a69f3d029058a65fd6e5dd)
#### Friday 2023-03-17 19:12:05 by Maetrim

Build 1.0.0.184

Fix: Feat "Wild Shape: Blighted Wolf" now has its description
Fix: Missing Blight Caster feat "Thorn Imbue" automatically assigned at level 4
Fix: Natures Warrior enhancement options "Dead Nerves", "Play Dead" and "Bad Wolf" now correctly require enhancement "Blight Caster: The Cycle of Decays" to be trained
Fix: "IoD: Weapon: Claw Slot" options for ability increases now have their correct names rather than all being "Meltclaw" (Reported by GillianGroks)
Fix: The following IoD augments will now have different values when slotted in a Minor Artifact (Reported by GillianGroks)
---Scale - False Life +58
---Fang - Accuracy +23
---Fang - Deadly +12
---Fang - Deception +12/+18
---Fang - Seeker +15
---Fang - Healing Amplification +61
---Fang - Negative Healing Amplification +61
---Fang - Repair Amplification +61
---Claw - PRR +38
---Claw - MRR +38
---Claw - Spell Penetration +10
---Claw - Trip cannot be modelled at +17 with Improved Trip in this version of the builder
---Claw - Sunder cannot be modelled at +17 with Improved Sunder in this version of the builder
---Claw - Assassinate +17
---Horn - Armor Piercing +23
---All Dinosaur Bone Artifact Item slots updated to match new augments
---Note that due to some augment renaming here, some existing builds will have to re-select their augments again, as all augment names need to be unique
Fix: Enhancement "Dark Hunter: Underdark Defenses" is no longer erronesously shown as a clickie type enhancement
New: New option in forum export to show level and feat selection without skills (Requested by Bolo_Grubb)
Fix: "Season's Herald: Time and Tide" is no longer erroneously dependant on "Wax and Wane" (Reported by EShadowbringer)
Fix: Past Life: Mixer of Magics now has the correct icon
Fix: The Ranger Dark Hunter tree now has the correct class icon
Fix: Drow Imbue I/II enhancements now have the correct icom
Fix: "Drow Venomed Blades" enhancement now has the correct text and is no longer restricted by Assassins Venomed Blade
Fix: "Assassin: Venomed Blades" text updated

---
## [LiquidFirefly/VOREStation](https://github.com/LiquidFirefly/VOREStation)@[8f3509b45c...](https://github.com/LiquidFirefly/VOREStation/commit/8f3509b45cec56962eabc7463256e4f144985867)
#### Friday 2023-03-17 20:57:16 by Mr. Gazer 'Toxic Player' Gazer

Diamonds aren't |my| best friend...... .. . .. fucked up of 'em honestly.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[55c39d4573...](https://github.com/wrye-bash/wrye-bash/commit/55c39d45734a59dc3fb734adbbe36f7995648af2)
#### Friday 2023-03-17 21:07:06 by Infernio

Fix the whole 'auto-wrapping text' mess

I've finally figured it out. Took literally hours of fiddling around
with AutoWrapStaticText to work around a really weird bug, then more
hours to figure out how to get the settings dialog to wrap nicely when
it's opened, but it's done. It's wonderful. I never want to touch it
again.

Utumno:
We must link to the commit here - just a fixup (kept separate in case
there is a shorter url - certainly needs to wrap better :P)

I am really curious to learn what the 'really weird bug" was - I
remember wrapping being a pain so I'd like to know what made the
difference finally - is it just the `dc = wx.ClientDC(self)` (?)

You mean wx.AutoWrapStaticText and it _is_ wonderful

Edit: added a wx (Pep8) suffix to wx functions/overrides - makes it
much easier to figure out on first read (plus if we ever want to swap
gui libs this would be done by a metaclass reading off the correctly
suffixed method)

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[7bd6c179f3...](https://github.com/Koi-3088/ForkBot.NET/commit/7bd6c179f38232b06cb3c60c285d6ca5fc98d644)
#### Friday 2023-03-17 22:02:48 by Koi

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
## [git/git](https://github.com/git/git)@[eaa0fd6584...](https://github.com/git/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Friday 2023-03-17 22:17:05 by Jeff King

git_connect(): fix corner cases in downgrading v2 to v0

There's code in git_connect() that checks whether we are doing a push
with protocol_v2, and if so, drops us to protocol_v0 (since we know
how to do v2 only for fetches). But it misses some corner cases:

  1. it checks the "prog" variable, which is actually the path to
     receive-pack on the remote side. By default this is just
     "git-receive-pack", but it could be an arbitrary string (like
     "/path/to/git receive-pack", etc). We'd accidentally stay in v2
     mode in this case.

  2. besides "receive-pack" and "upload-pack", there's one other value
     we'd expect: "upload-archive" for handling "git archive --remote".
     Like receive-pack, this doesn't understand v2, and should use the
     v0 protocol.

In practice, neither of these causes bugs in the real world so far. We
do send a "we understand v2" probe to the server, but since no server
implements v2 for anything but upload-pack, it's simply ignored. But
this would eventually become a problem if we do implement v2 for those
endpoints, as older clients would falsely claim to understand it,
leading to a server response they can't parse.

We can fix (1) by passing in both the program path and the "name" of the
operation. I treat the name as a string here, because that's the pattern
set in transport_connect(), which is one of our callers (we were simply
throwing away the "name" value there before).

We can fix (2) by allowing only known-v2 protocols ("upload-pack"),
rather than blocking unknown ones ("receive-pack" and "upload-archive").
That will mean whoever eventually implements v2 push will have to adjust
this list, but that's reasonable. We'll do the safe, conservative thing
(sticking to v0) by default, and anybody working on v2 will quickly
realize this spot needs to be updated.

The new tests cover the receive-pack and upload-archive cases above, and
re-confirm that we allow v2 with an arbitrary "--upload-pack" path (that
already worked before this patch, of course, but it would be an easy
thing to break if we flipped the allow/block logic without also handling
"name" separately).

Here are a few miscellaneous implementation notes, since I had to do a
little head-scratching to understand who calls what:

  - transport_connect() is called only for git-upload-archive. For
    non-http git remotes, that resolves to the virtual connect_git()
    function (which then calls git_connect(); confused yet?). So
    plumbing through "name" in connect_git() covers that.

  - for regular fetches and pushes, callers use higher-level functions
    like transport_fetch_refs(). For non-http git remotes, that means
    calling git_connect() under the hood via connect_setup(). And that
    uses the "for_push" flag to decide which name to use.

  - likewise, plumbing like fetch-pack and send-pack may call
    git_connect() directly; they each know which name to use.

  - for remote helpers (including http), we already have separate
    parameters for "name" and "exec" (another name for "prog"). In
    process_connect_service(), we feed the "name" to the helper via
    "connect" or "stateless-connect" directives.

    There's also a "servpath" option, which can be used to tell the
    helper about the "exec" path. But no helpers we implement support
    it! For http it would be useless anyway (no reasonable server
    implementation will allow you to send a shell command to run the
    server). In theory it would be useful for more obscure helpers like
    remote-ext, but even there it is not implemented.

    It's tempting to get rid of it simply to reduce confusion, but we
    have publicly documented it since it was added in fa8c097cc9
    (Support remote helpers implementing smart transports, 2009-12-09),
    so it's possible some helper in the wild is using it.

  - So for v2, helpers (again, including http) are mainly used via
    stateless-connect, driven by the main program. But they do still
    need to decide whether to do a v2 probe. And so there's similar
    logic in remote-curl.c's discover_refs() that looks for
    "git-receive-pack". But it's not buggy in the same way. Since it
    doesn't support servpath, it is always dealing with a "service"
    string like "git-receive-pack". And since it doesn't support
    straight "connect", it can't be used for "upload-archive".

    So we could leave that spot alone. But I've updated it here to match
    the logic we're changing in connect_git(). That seems like the least
    confusing thing for somebody who has to touch both of these spots
    later (say, to add v2 push support). I didn't add a new test to make
    sure this doesn't break anything; we already have several tests (in
    t5551 and elsewhere) that make sure we are using v2 over http.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [TheDuckCow/MCprep](https://github.com/TheDuckCow/MCprep)@[a34b01aa69...](https://github.com/TheDuckCow/MCprep/commit/a34b01aa69f7e215a0cd6ec46665e1c15a0a78ca)
#### Friday 2023-03-17 23:45:17 by mahid

Added type annotations and use of Path
Replaced some instances of os.path with the Path object from pathlib for
readability. Also added type annotations to MCprepEnv as we're moving
towards that. This also means MCprep will not work at all in Blender
2.7x due to the use of new syntax.

This will be the first in a long process of modernizing MCprep's code
with 2.8 style code. Blender 2.7x users may not be happy, but it's for
the better. If anything, 6 years worth of 2.7x support was a mistake (in
my opinion), as it limited what we could do and opened MCprep to even
more bugs (like in Blender 2.93 with make_annotations, which ironically
now is deprecated).

---

