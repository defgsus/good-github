## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-08](docs/good-messages/2022/2022-10-08.md)


1,699,543 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,699,543 were push events containing 2,421,515 commit messages that amount to 165,000,435 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[59658c7e5f...](https://github.com/Buildstarted/linksfordevs/commit/59658c7e5ffebe0b20a63eb5e4a36cf973eca1fa)
#### Saturday 2022-10-08 01:06:12 by Ben Dornis

Updating: 10/8/2022 1:00:00 AM

 1. Added: Lessons Learned From Three Years of Open Source Contributions
    (https://navendu.me/posts/open-source-lessons/)
 2. Added: My Favourite Computer, An Old Mac
    (http://muezza.ca/thoughts/favourite_computer/)
 3. Added: Why remote work might end
    (https://manassaloi.com/2022/10/01/remote-office.html)
 4. Added: Setting up my new computer, vim, and listening to Spotify in the terminal
    (https://johnwhiles.com/posts/the-new-dots)
 5. Added: A Letter to Myself
    (https://calder-ty.com/posts/a-letter-to-myself/)
 6. Added: Learnings as a Tech Lead
    (https://linghao.io/posts/tl-learnings-2022)
 7. Added: Red Meat Friday: Is The FSF Fighting The Previous War?
    (https://irreal.org/blog/?p=10864)
 8. Added: Privacy As A Moral Buffer — Simon Berens
    (https://simonberens.me/blog/privacy-as-a-moral-buffer)
 9. Added: Effortless Language Servers
    (https://stefan-marr.de/2022/10/effortless-language-servers/)
10. Added: When Life Gives You an Integer
    (https://blog.charliemeyer.co/when-life-gives-you-an-integer/)
11. Added: Thomas Tanay | How government expenditures finance themselves
    (https://thomas-tanay.github.io/posts/2022-SFCmodel)
12. Added: Small correlations can drive large increases in teen depression · Chris Said
    (https://chris-said.io/2022/05/10/social-media-and-teen-depression/)
13. Added: Overzealous Destructuring | Aleksandr Hovhannisyan
    (https://www.aleksandrhovhannisyan.com/blog/overzealous-destructuring/)
14. Added: POV: You are trying to pet a dog in RPG games
    (https://youtube.com/watch?v=CnBaVC_7JmE)

Generation took: 00:06:02.4804582
 Maintenance update - cleaning up homepage and feed

---
## [BinAlexme/free-programming-books](https://github.com/BinAlexme/free-programming-books)@[5fd70502a0...](https://github.com/BinAlexme/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Saturday 2022-10-08 01:07:02 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [ebobrow/rust-clippy](https://github.com/ebobrow/rust-clippy)@[9e8f53d09a...](https://github.com/ebobrow/rust-clippy/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Saturday 2022-10-08 01:10:08 by bors

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
## [smxi/inxi](https://github.com/smxi/inxi)@[b6ac6026f2...](https://github.com/smxi/inxi/commit/b6ac6026f2d563039211f290ac3bc61a18789274)
#### Saturday 2022-10-08 02:43:32 by Harald Hope

Another big one, with a long time to-do item done! /sys based sensors data is
now used as a fallback, with fully revised error messages to handle this new
sensor data variant. Due to potential bugs this might create, this was left off
of the 3.3.21 release, which needed to go out on a schedule, but there is plenty
of time for 3.3.22 to be debugged.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. inxi can't currently handle raw in[0-9] voltage sensor data from
/sys/class/hwmon, that may get corrected, but I've honestly never seen a system
that shows raw in[0-9] values as field names, so it's probably not very
pressing, but it can happen. Similar that is to how default fanx and tempx field
names are processed.

2. Currently only checking -Gx, -Nx device temp for bus IDs ending in .0, which
is the primary PCI device. I think that's the only one that will have a temp,
.1, which is a second device on the same hardware, doesn't have that data in
tests. Saves some requests since it's a big glob of /sys.

3. Spiral Linux has no obvious way to determine that it is Spiral and not Debian
11 as base distro. No /etc/ files for distro ID contain anything for spiral, so
leaving that one alone.

4. Can't get 100% reliable cpu level > v2 due to it not being a pure cpu flag
based test, which is kind of sadly typical for the originators of this idea, but
since the choice was dump the feature, or just use the note: check for > v2,
opted for note: check. One wants to ask questions here, but honestly I already
know the answer so why bother asking the question... The docs for this are
awful, inadequate, incomplete.

My strong suspicion is that this is NOT intended to be a distro-wide feature
beyond v2 support minimum, but rather is for specific compile options for a
package or daemon or server or whatever that can benefit from this type of
fine-tuning. One thinks of Gentoo for example back when such fine-tunings could
actually deliver noticeable differences in performance. A per system type
feature that is, not a distro-wide feature. At least that's my initial feeling,
but this is probably about all the  time I will spend on it since inxi can't get
it more accurate anyway.

--------------------------------------------------------------------------------
BUGS:

1. Bug in monitor position logic, the horizontal/vertical sorts were being done
alphanumerically, leading to absurd results where 800 > 2560 or whatever.
Basically all x / y positions less than 1000 would have forced the smaller
number to be considered as the greatest value. Another corner case find by
mrmazda. Thanks mrmazda!

--------------------------------------------------------------------------------
FIXES:

1. Added i350bb sensor to network sensor type.

2. Small glitch with some scenarios with missing fan1 in sensors, showed fan1 0
rpm, but then showed fan 3: empty. That was a slight error in how undefined vs
'' empty was treated.

3. Added fix for defective fan speeds, skip fan item if > 15000, which is a bug
in the fan speed report, making it useless. Seen 65535 reported RPM. Could
probably make it 10000 upper limit but suspect that is a simple bug that creates
an absurd value, 2^16 so won't be anything high unless bug active. This fix runs
for ipmi, linux, and sysctl fan data.

4. Trying for fix for dynamic gpu voltage, assumed always mV, but might be V.

5. Inadequate or obscure or non-existent redhat/suse documentation led to some
fixes for cpu v levels. Note that level v3/v4 can't be fully determined by cpu
flag tests, but who cares? Certainly not me. Added 'note: check' for v3/v4.

6. Nvidia device arch id was too loose, false id for non existing lovelace arch.
Note that due to array reverse, the newest ids will always run first, which
leads to possible false positives with first string match tests when no product
IDs are available yet.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. Elbrus CPU arch, process, year, arch data made more complete using new data
resource. Thanks Elbrus guys!

2. Finally, raw, basic /sys/class/hwmon temp data. Linux kernel docs note
supports temp, fan, volts, amps, energy. But have only seen temps so far. Can
force /sys use with --force sensors-sys / --sensors-sys, though there's no point
to doing that except to test.

Also changed --recommends to note lm-sensors not required for sensor data now.

3. Adding device temp for -Gx, -Nx. Will only work for Linux and when found, and
only for free drivers (I think).

4. Added xdriinfo based dri drivers (with fallback to Xorg.0.log as data source,
not as accurate), that will show if and only if that driver is not the same name
as a detected X or gpu driver.

5. Another big upgrade to cp_cpu_arch, added and corrected many AMD/Intel
matches.

6. A few more gpu product ids, Intel, added.

7. More disk vendors, ids, the list, as we are now well aware, is endless,
reflecting perhaps the futility of pursuing the infinite using finite means.

--------------------------------------------------------------------------------
CHANGES:

1. Slight changes in how inxi supplies no sensor data messages, and in the
fallback cases and handling. More accurate and precise, and more robust overall.

2. Due to complexity of understanding level: and the fact not all cpu flags are
exposed that are required, moved -Cxx level: to -Ca.

3. Changing slightly inaccurate Sound Server for ALSA/OSS to Sound API, which is
the closest I can come to explaining clearly what it is. Note that you can only
load one API type audio subsystem/driver, so you will be running one or the
other, never both, from what I understand.

Since OpenBSD sndio includes sndiod, calling that a sound server is basically
fine, since it's both the server and the interface, if I understand it right,
and there won't be a second sound server listed, actually won't be for any BSD
that I know of, it's going to be sndio or OSS or nothing, unless something has
changed.

--------------------------------------------------------------------------------
DOCUMENTATION:

1. Man page, updates for /sys/class/hwmon based sensor data.

2. Small update for cpu level v3/v4, added note: check explanation, though it's
too hard to really explain this stuff since the docs are... not wonderful, when
they even exist and don't contradict each other.

--------------------------------------------------------------------------------
CODE:

1. Refined significantly sensors missing data and error messages to be much more
accurate and granular. Also enables more sensors tools, though hopefully they
won't appear since those are a real pain to implement, but it's more open to
being sensor tool agnostic now due to these refinements than before.

2. Added xdpiinfo to debugger.

3. Switched x_drivers to return ref of array of refs, use join for output only,
that lets us use the drivers to test dri stuff also (if we want or need to), and
keeps it consistent with how most of inxi does that type of data
handling/testing. If undef, it means no array ref exists, which makes testing
easy.

Not truly understanding hash/array refs when inxi rewrite to Perl started is
probably one of the bigger causes of glitches and ongoing optimizations.
Basically, in all but very small array cases, it's almost always better to start
with a ref from the start as soon as the hash/array moves between functions,
with one exception, when it's a globally stored data item. Then it depends. But
this requires a consistent testing for null data as well, which is harder if you
did it in different ways from the start. But slowly and surely chipping away at
these.

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[e1839f0e37...](https://github.com/lessthnthree/Skyrat-tg/commit/e1839f0e375a2169c8d80d942376dddb8be1958d)
#### Saturday 2022-10-08 03:01:46 by SkyratBot

[MIRROR] Spider Rebalance PR: Burn Baby Burn Edition [MDB IGNORE] (#15997)

* Spider Rebalance PR: Burn Baby Burn Edition (#68971)

This is a remake of #66106, with more thought put into the underlying balance. The main goal of this PR is to make fighting spiders more accessible and interesting for the majority of the crew while nerfing the extremely strong and boring option of simply using freezing temps to kill spiders. Also fixes #67765. The changes are as follows:

NEW SPIDER COUNTERS

    Fly swatters now deal 25 damage to spiders on hit, increased from 1
    Pesticide now deals massive stamina damage to spiders and a little bit of physical damage as well (the damage portion not added by this PR)
    Spiders can now be caught on fire through any traditional mean of catching something on fire. Spiders will automatically put themselves out after a time. This was done instead of an active action because AI spiders are also subject to this change as well, and I don't feel like bloating the simple mob AI with putting themselves out

SPIDER CHANGES

NERFS

    Toxin injection has been removed from all spiders except for the hunter, flesh spiders and the viper
    Hunter toxin (used by hunters and flesh spiders) now only brings the afflicted down to 40 health, and will stop taking effect once the afflicted reaches that threshold. Should the afflicted still have the toxin in their system and get healed, the toxin will begin dealing damage again until the afflicted is at 40 health or below again
    Viper toxin now only brings the afflicted down to 10 health, but also has the hallucination effects of Mindbreaker toxin. This hallucination effect is applied regardless of target health. It also no longer generates other harmful chemicals into the afflicted's system, but is much more potent at base
    Flesh spiders cannot regenerate while on fire

BUFFS

    Time it takes for spiders to normalize their temperature cut by half. While they will react faster when in cold or hot environments, when they leave said environments it will take less time to return to normal temperature
    Unsuitable temperature damage reduced to 4 from 8
    You can no longer push spiders by running into them
    Webbing heat damage threshold increased from 300 to 350 (same temp where spiders also take damage)
    Broodmother egg laying time reduced to 12 seconds from 15
    Broodmother web laying time multiplier reduced to 0.5 from 1
    Broodmother health increased to 60 from 40
    Broodmother damage increased to 10 - 15 from 5 -10

BEHIND THE SCENES CHANGES

    You can now make any simple mob able to be caught on fire by setting flammable to true
    How fast a simplemob stops burning is controlled by fire_stack_removal_speed
    Can now now control how fast simplemobs regulate their temperature using temperature_normalization_speed. Before this PR, this value was hard-coded at 10, I have set the default to 5 as 10 was too long in almost any case. This will notably affect slimes, who could easily die to being cold long after being removed from the cold area. I see this as purely beneficial
    Toxins now have a health_required value. The afflicted has to be above this health value in order to take damage from the toxin. Only used in the spider toxins currently
    When I was setting up simplemobs to be flammable, I noticed basic mobs can be glitchily set on fire, so I fixed it to where they can't be set on fire.

Why It's Good For The Game

    Spacing something is very easy, but not very fun or interesting compared to starting and controlling a fire. Swapping spiders' temperature weakness from spacing to fire is beneficial to the fun of fighting them and playing as them, allowing more creativity and resourcefulness on both sides. Ideally, this should allow for atmosians and chemists to use their skills in a fun way.
    Currently, ignoring spacing them, the only people who can reasonably take on spiders is security, since they have lasers which do burn and stuns to slow the spiders down. However, this small subset of players cannot normally destroy a spider infestation without spacing them, so letting fly swatters and pesticide be used to combat spiders allows other crewmembers to fight back, letting them actually enjoy facing spiders as a threat and allowing the crew to defend themselves.
    Being killed by spider toxin after fighting off a horde isn't fun. The changes still make it a threat you have to be aware of, but not one which detracts as much from the combat loop. This also forces spiders to secure the kill themselves, which is more fun than having the toxin do it for you.
    Broodmothers in their current state are incredibly weak by themselves, which is intentional by design. However, the new changes hope to make playing as a broodmother easier and hopefully allow more broodmothers to get the spider infestation started properly. After all, Dynamic is their common source now, and they should be consistently worth the threat cost to spawn them.
    Previously, spider structures would seemingly vanish for no reason if the room was heated to be greater than 300 but less than 350, as the spiders would not be able to tell that it was too hot. Now, if the structures are taking damage, spiders will also be taking damage, so understanding what's going on should be easier now.
    Pushing spiders into a corner by running into them was not a fun tactic to deal with as a spider and didn't make much sense seeing how big the spiders are.

Changelog

cl
add: Spiders can now be caught on fire
add: Spiders take significant damage from fly swatters and stamina damage from pesticide
balance: Spiders have been re-balanced. Their toxins can no longer kill but they are not as susceptible to freezing
balance: General stats of spider broodmothers have been buffed with more health, damage, and faster web and egg placement
balance: Flesh spiders cannot regenerate whilst on fire
balance: Simplemobs change their internal temperature twice as fast
fix: Basic mobs no longer glitchily catch on fire.
/cl

* Spider Rebalance PR: Burn Baby Burn Edition

Co-authored-by: IndieanaJones <47086570+IndieanaJones@users.noreply.github.com>

---
## [nblockchain/geewallet](https://github.com/nblockchain/geewallet)@[cae07411f7...](https://github.com/nblockchain/geewallet/commit/cae07411f70ff28e132a424a3f6b3e554af15e78)
#### Saturday 2022-10-08 03:14:19 by Andres G. Aragoneses

GitHubCI(Linux+GTK): retry 'make' 3 times (flakey nuget)

Previous commit fixed indeed the 'sanitycheck' of some builds
affecting Linux+GTK, however, one of the builds failed at the
'make' step. By looking at the log, you can see the compiler
error hints at the Xamarin.Forms dependency not being present,
so this means that nuget restore didn't work properly.

If a nuget restore operation doesn't work, it should fail in
that process and stop; not sure why it didn't fail this way.
But it's not worth to investigate because:

1) In the past, I implemented[1] a solution to have the nuget
restore operation be part of the normal build, kind of like
a PreBuild step via MSBuild. The code that allowed this is
kinda horrible and don't want to debug at the moment, because...

2) We're going to move to .NET6 soon anyway, which means not
using nuget anymore (in favour of the "dotnet restore" command).

Given the above, I'm using here temporarily a very hacky solution:
retry the 'make' step 3 times. And I also doing it in a very ugly
way because I'm very wary of using random people's githubActions,
such as what is the existing/recommended solution for this in
the GitHubActions marketplace [2].

[1] 9804b653a63266c8560c7e8143f9ec644f05a334
[2] https://github.com/marketplace/actions/retry-step

---
## [firedreamer/Firedreamer-Hugo](https://github.com/firedreamer/Firedreamer-Hugo)@[f33dea30e6...](https://github.com/firedreamer/Firedreamer-Hugo/commit/f33dea30e6599abae1a21471e4fc3b28afef6277)
#### Saturday 2022-10-08 04:00:15 by Ashe O'Hawkes

Initial commit

Add files via upload

Docs and mainpage

doridoridoridori

Neco Arc is all that I think of. Neco Arc is the best thing that I ever saw. It all started on Discord, on a videogame music server. I started seeing those gifs of a cute small catgirl dancing the gangnam style dance. It was very funny, but I continued with my life. Then, I saw it again. This time she was riding a car. The next one was the thing that made me realize how perfect this character is. Her little voice saying "dori dori dori dori" made me realize I just found the meaning of life. Neco Arc became my entire life after that. I will do anything to meet this perfect being. I want to hug her tightly while she purrs feeling comfortable in my arms. I will find a way to meet Neco Arc. I do not care what I have to do. I don't care anymore. I will do anything to meet Neco Arc. I want her to say "Gurenyuu" as she walks around, showing everyone what the perfect life is. Neco Arc will show us how to become better. Neco Arc is the new symbol of peace. Dori dori dori dori.

remove doridori

Neco Arc is nothing that I think of. Neco Arc is the worst thing that I ever saw. It all started on Discord, on a videogame music server. I started seeing those gifs of a cute small catgirl dancing the gangnam style dance. It was very unfunny, but I continued with my life. Then, I saw it again. This time she was riding a car. The next one was the thing that made me realize how broken this character is. Her little voice saying "dori dori dori dori" made me realize I just lost the meaning of life, if I ever found it. Neco Arc became only a tiny footnote in my life after that. I will do anything to kill this wretched being. I want to strangle her tightly while she screams in my arms. I will find a way to destroy Neco Arc. I do not care what I have to do. I don't care anymore. I will do anything to destroy Neco Arc. I want her to say absolutely nothing as she walks around, showing everyone how fucking pointless life is. Neco Arc will show us how to become worse. Neco Arc is the new symbol of hatered. Dori dori dori dori.

---
## [montchr/dotfield](https://github.com/montchr/dotfield)@[30f66d7415...](https://github.com/montchr/dotfield/commit/30f66d7415c9b9811d3386e37d02061b234a6c66)
#### Saturday 2022-10-08 04:47:14 by Chris Montgomery

chore: remove `lando-cli` to maintain our No Star Wars Fanboys policy

i can abide a star wars reference here and there but the length to
which this project goes to keep up the CUTE and RANDOM and COOL
references really puts me off. yes, i could go on about why i think
proclaiming your love of Star Wars all over the place serves as a
very straightforward and uncreative substitute for having a nuanced
appreciation for sci-fi and storytelling... but at a very basic level,
i see the layers of inside jokes littered throughout that project as
a significant red flag and deterrent to taking it seriously. like, i
really really do not want to think about Han Solo every time i run
`docker-compose` or whatever, please fucking spare me.

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[91f02f2a6b...](https://github.com/Wallemations/heavenstation/commit/91f02f2a6b99c6eb5ae56fc3f7cfb903e703bc08)
#### Saturday 2022-10-08 04:53:26 by John Willard

canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

---
## [Pranjal-0402/animepedia](https://github.com/Pranjal-0402/animepedia)@[d93637aa2f...](https://github.com/Pranjal-0402/animepedia/commit/d93637aa2f7457316f06b0f78126ade3cf2fecfc)
#### Saturday 2022-10-08 05:06:34 by Rajat Dixit

Added Astro Boy

            <div class="card mb-3 card-bg my-4" style="max-width: 100%;">
                <div class="row no-gutters">
                    <div class="col-md-4">
                    <!-- Replace image_name_here by the complete name (with extension) of the image you uploaded -->
                        <img src="./images/Astro Boy.jpg" alt="Astro Boy" height="390px" width="300px">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h2 class="card-title">Astro Boy</h2>
                            <p class="card-text">
                              One of the oldest anime characters in existence, Astro Boy first appeared on television screens in 1963, helping to usher in the phenomenon now known 
                               worldwide as anime.
                            </p>
                            <p>
                             Astro, a boy who was both more than human and less than human, guided kids through complex morality tales where the characters had complicated 
                             motivations, social problems didn't always have easy solutions, and people had the capacity to perform both great acts of kindness and of evil.
                           </p>
                            <hr>
                            <p>Contributed by- Rajat Dixit</p>
                        </div>
                    </div>
                </div>
            </div>
            <!--Sample [Character Name] card end-->
            <!--Add your card below this line -->

---
## [MrKleiner/source_tricks](https://github.com/MrKleiner/source_tricks)@[46fb9b42d1...](https://github.com/MrKleiner/source_tricks/commit/46fb9b42d155e92da4af8b9d6dab38faa05be17d)
#### Saturday 2022-10-08 05:21:44 by baton

I hate myself

fuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuck

---
## [dawsonkeyes/master-skyrat](https://github.com/dawsonkeyes/master-skyrat)@[bd76bd7398...](https://github.com/dawsonkeyes/master-skyrat/commit/bd76bd73981505b30d2897ce0405790667b1f633)
#### Saturday 2022-10-08 06:49:31 by dawsonkeyes

i fucking hate single letter vars, eat shit. also adds the boots i guess

---
## [Wad67/ArxLibertatisFTLConverter](https://github.com/Wad67/ArxLibertatisFTLConverter)@[3475055ba6...](https://github.com/Wad67/ArxLibertatisFTLConverter/commit/3475055ba615aea74069ce8863ee9e2c5844c38d)
#### Saturday 2022-10-08 06:53:55 by Wayde

Fix orientation, UV's

Model is now right way up, UV's still kinda fucky but that's for texture layering / transparency to handle

I hate quaternions

---
## [hugok79/subsurface.github.io](https://github.com/hugok79/subsurface.github.io)@[ad4b82193b...](https://github.com/hugok79/subsurface.github.io/commit/ad4b82193be920f3b90c6a31a757368dcc202c54)
#### Saturday 2022-10-08 09:35:03 by Dirk Hohndel

small updates to deal with horizontal lines

I wonder if the magic that creates them isn't more trouble than it's worth.
Maybe it would be better to make them explicit? This seems hacky...

This commit also has a couple of tiny edits to the things Jason brought
over from the old FAQ.

Signed-off-by: Dirk Hohndel <dirk@hohndel.org>

---
## [Norikiru/bloxflip-autocrash](https://github.com/Norikiru/bloxflip-autocrash)@[fce80dd446...](https://github.com/Norikiru/bloxflip-autocrash/commit/fce80dd446096f354774d68f52958cf3cfc3bf84)
#### Saturday 2022-10-08 09:48:05 by Norikiru

Revert "fetch: go back to browser fetch from libcurl"

This reverts commit fedc2b05ddeee6bc6165b820aaf01600975d6e51.

fetch: revert to curl (fuck you git)

---
## [fightant1w1ll/react](https://github.com/fightant1w1ll/react)@[b6978bc38f...](https://github.com/fightant1w1ll/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Saturday 2022-10-08 09:51:26 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [troyandy1023/111-1HW2](https://github.com/troyandy1023/111-1HW2)@[872ee7ebd3...](https://github.com/troyandy1023/111-1HW2/commit/872ee7ebd327e15b164c8296494a377dcd442b26)
#### Saturday 2022-10-08 11:48:11 by troyandy1023

(手可以借給我嗎)
YA
I &$"&@ the same 都好像沒有變
你來 changed 還是討厭下雨天
還是不愛認錯 脾氣是硬了點
這我都清楚 但我沒有辦法改變
我後悔高中裝£¥{*&/#%的排氣管
想努力賺錢養妳 卻養成了壞習慣
我還想帶到妳 到處含 到處帶你玩
without you it feels like
情人節沒有愛人 耶
像台相機沒有快門 耶
像上出所沒有檯燈 耶
without you it feels like
呃 \%¥ we刀no嘿嘿
It be like youtube without no 呸踢斯
Or 呃 Chen without no pages
without you it fish
(合唱嗎)
凹you
I 東往那 be alone欸
想念妳的每個角度
如果我們還能夠重來 Oh
You dont know how I feel inside 手
I don't wanna live 凹 you
我沒有辦法!
再拼 too that
重蹈覆轍 I can too that
沒得負責 oh damn too bad
I的揪rua 味U味
先把我的面子放兩邊
榨乾我就像搶劫
Goddamn I got 內不內
然後進去 拖馬燙 呦
救救窩 I call my friends
訴苦 說了好幾遍
他們叫我振作點
I know 勉 fuckin care
幫我刪了instagram
pose i don't wanna 席
讓你神通 with me
我乾掉哼 李行
just wanna noise
我們之間太多的我捨不得放手耶
失去妳就像失去我的麥克風
我不要我的fans
不要IG的followers呃 顆
(尖叫聲)
I don't wanna live we凹you
I don't wanna be alone and
想念妳的每個角度
如果我們還能夠重來 Oh
You don't know how I feel inside
手
(借給我)
凹 you
我沒有辦法
I don't wanna 李we凹 you
I don't wanna be alone 欸
想念妳的每個角度
如果我們還能夠重來 Oh
You don't know how I feel inside
So
I don't wanna 李we凹 you
我沒有辦法
(謝謝)

---
## [MJZ1977/Stockfish](https://github.com/MJZ1977/Stockfish)@[cb9c2594fc...](https://github.com/MJZ1977/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Saturday 2022-10-08 12:04:08 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [sthagen/OpenImageIO-oiio](https://github.com/sthagen/OpenImageIO-oiio)@[4ee35351f1...](https://github.com/sthagen/OpenImageIO-oiio/commit/4ee35351f100c79738c77892fb8ccca8ddc004c9)
#### Saturday 2022-10-08 12:11:54 by Aras Pranckevičius

DDS: alpha/luminance format fixes, add & enable more tests (#3581)

* DDS: fixes for A8, L8, A8L8 formats

While developing #3573 at one time I had them working properly, but then
while fixing the address sanitizer failure for 3-channel formats I
botched them again. Note to self: never again do a "yeah I'll add tests
later", since if I had all of them running all the time this would
not have happened. :facepalm:

* DDS: extend test coverage for more formats & channel size cases

With more test images recently added (https://github.com/OpenImageIO/oiio/pull/3459),
start using them for DDS tests. This covers now:
- Alpha, Luminance and Alpha+Luminance formats,
- RGB formats with rarer channel sizes (rgb10 a2, r3g3b2),
- Several "broken" DDS file cases
- Removed usage of sample-DXT1 since it is well covered by others.

---
## [anki-geo/ultimate-geography](https://github.com/anki-geo/ultimate-geography)@[90e1e3dfff...](https://github.com/anki-geo/ultimate-geography/commit/90e1e3dfff699da113346e4ae1522ff0c8f5479e)
#### Saturday 2022-10-08 12:40:59 by aplaice

Expand SADR country info mentioning alternative names (#570)

Fix #561.

As discussed in #561, saying that "Sahara Zachodnia" (Western Sahara)
is also known as SADR (in the Polish version), is ambiguous and
potentially misleading, since Western Sahara is both the name of the
geographic area (ignoring political associations) and one of the names
used for the partially recognised state.  However, AFAICT, we have the
exact same situation for Artsakh, in Polish, (Górski
Karabach (Nagorno-Karabakh) also known as Artsakh, where
Nagorno-Karabakh can refer both to the country and the geographical
area.).  Also, since we're generally dealing with countries, here, it
should be clear that we mean Western Sahara (the country) rather than
WS (the area), so I think my initial worry was overblown.

I'm not 100% sure if I have the correct gender for conosciuto in
Italian (should it agree with Repubblica.. or with stato?).

The same question holds for Czech — should známý agree with
..republika or with stát?

I've gone with agreement with stát for Czech (male) and with
republic (female) for Italian, because in the former the second clause
is separated only with a comma, while in the latter it's separated by
a semicolon.  The choice of separator was based on precedence in other
cases (Faroe islands and Taiwan).

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[d45e244401...](https://github.com/Time-Green/tgstation/commit/d45e244401425d34edc38e3dd2f3c2bbdbcec7ce)
#### Saturday 2022-10-08 12:43:58 by san7890

Crab-17 No Longer Breaks Economy If You Swipe Too Fast (#70094)

Hey there,

Remember swiping credit cards, before everything was chipped? You know how sometimes if you went too slow, the transaction might fail, the cashier had to plonk in some digits on their machine, and you had to go again? That kinda sucked.

If you're too young to get that reference, just imagine the card swiping task in AMONG US. Doesn't that minigame suck? You know exactly what that is. Same principle.

Anyways, that's pretty much what was going on here. The reason why SS.Economy would break so god damn hard if you swiped an ID before the machine's "boot up" slowflake animation was complete is probably due to the line where it starts fast processing. I added an early return to check for if the animation was complete by leveraging a var we already set at the end of the process, because I am lazy.

There's probably a few other ways you can tackle this issue, but this feels right to me in a thematic sense. I'm willing to change it if needed though.

---
## [mayebejames/WebDesigns](https://github.com/mayebejames/WebDesigns)@[f16558bbf4...](https://github.com/mayebejames/WebDesigns/commit/f16558bbf4e7b706a2fedcccafb2f069a75e5267)
#### Saturday 2022-10-08 13:12:55 by mayebejames

Colour & line height/length tweaks

Colour for default text (including headings) changed to off-black #333 in order to slightly reduce the feeling of body text density and darkness. Changing the font weight to 300 is an alternative option but I think is a more stark change. 

Line height has been very slightly increased to 1.45 from 1.4 for exactly the same reason as above. I note that Life in the Fast Lane and Gwern both use line heights of ~1.65. Andy Matuschak's notes in contrast use 1.4. I do think that 1.65 looks fine but again am cutting a more conservative line. I may revisit 1.65 if using for shorter note-like sentences such as LITFL. Similarly, line height has been increased and bottom margin added to list items in order to allow lists to be more spaced out. In medicine lists are usually extremely content-dense, so spacing them out allows the different ideas and points to breathe. 

Now that I have moved away from more complex (and hacky) sidebar and margin notes designs, the previous max-width felt too small on larger screens. I've increased from ~750px to 950px so that the page looks slightly less like a river of text.

---
## [UwUMacaroniTime/tgstation](https://github.com/UwUMacaroniTime/tgstation)@[32c2e4ccd3...](https://github.com/UwUMacaroniTime/tgstation/commit/32c2e4ccd3ee10b62a8f5d8e7ad3dbd1e33213ea)
#### Saturday 2022-10-08 15:15:20 by Fikou

gives medical ert a health analyzer (#70244)

* gives medical ert a health analyzer

* fuck you *upgrades your analyzer*

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[fc7c186957...](https://github.com/tgstation/tgstation/commit/fc7c186957088b6ffd0605f814bea754670c0212)
#### Saturday 2022-10-08 15:30:28 by RikuTheKiller

Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[14c96d05b8...](https://github.com/GoblinBackwards/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Saturday 2022-10-08 17:50:11 by scriptis

TGUI for Techfabs II: The Great Recategorizing (AND ICONS) (AND MECHFABS) (AND AUTOLATHES) (#69990)

    I recategorized EVERY /datum/design/ IN THE GAME to be more UX friendly and I HATE MYSELF FOR IT
    I refactored techfab UI to WORK ANYWHERE for ANY MACHINE THAT USES /datum/design as a SET OF MODULAR COMPONENTS
    I moved a lot of DESIGNS EXCLUSIVE TO THE AUTOLATHE to also work IN PROTOLATHES
    I made MATERIAL ICONS animate between ICON STATES for STACKS
    I PUT ICONS IN ALL OF YOUR FABRICATORS
    I SOMEHOW DID ALL OF THIS WITHOUT LOSING ANY PERFORMANCE
    ALSO SUPPORTS COMPONENT PRINTERS AND MODULE DUPLICATORS

Other garbage:

    Fixed numerous spelling and consistency issues in designs
    Removed Machine Design (<x>) and Computer Design (<x>) from all relevant designs
    All designs are now in title case
    Numerous designs that were formerly autolathe exclusives can now also be printed at a protolathe (but not all); this is mostly just service equipment like drinking glasses and plates and silverware
    Circuits components can no longer be printed at a circuit imprinter (fixes 

    Integrated circuit components printed in the component printer/module printer cost twice as much than from an un upgraded circuit printer #67758)
    Designs that are not sensible for a department to have are no longer accessible to that department (read: medbay printing turbine parts)

Why It's Good For The Game

Improved UX for techfabs, but also for mechfabs and autolathes, and oh look it's pretty!

also I spent like eight hours doing nothing but categorizing /datum/designs and I'll cry if some version of this doesn't get merged eventually
Changelog

cl
refactor: mechfabs, autolathes, component printers, and module duplicators now use techfab tgui components
refactor: every single design is now categorized and subcategorized
refactor: mechfabs and autolathes are now in typescript
qol: techfabs now have icons for what you're about to print
qol: techfab material icons are now animated
qol: techfab material icons now fade when no materials are available
qol: techfab searching no longer lags like hell
qol: techfab searching now searches all recipes instead of just the current category
qol: techfabs now have subcategorization (stock part users rejoice)
qol: techfabs now announce when new recipes are available
qol: numerous other techfab ui tweaks
balance: some designs that were formerly autolathe exclusive can now be printed at some departmental techfabs

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[99b8d6b494...](https://github.com/GoblinBackwards/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Saturday 2022-10-08 17:50:11 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[a2577296e6...](https://github.com/lizardqueenlexi/orbstation/commit/a2577296e62a0f3c335648169a335fe7d3de4bdc)
#### Saturday 2022-10-08 18:00:54 by RikuTheKiller

Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[422accbe4e...](https://github.com/lizardqueenlexi/orbstation/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Saturday 2022-10-08 18:00:54 by John Willard

[MDB IGNORE] Shuttle engines part 2: Engines are now machines (#69793)

* Makes engines machines instead of structures

* Updates the maps

* Fixes boards and anchoring

* Removes 2 unused engine types

Router was actually used a total of once, so I just replaced it with propulsion.
I think cutting down on these useless engine types that make no difference in-game would be a nice first step to adding more functionalities to them.

* Don't use power (since shuttles dont have)

Shuttles don't have APCs, instead they just have infinite power, so I'm removing their power usage for now. I'm hoping this can be removed when unique mechanics are added to engines, because I would like them to make use of power like other machines.

* re-organizes vars

* deletes deleted dm file

* Slightly improves cargo selling code

* Renames the updatepaths

* Removes in_wall engines

I hate this stupid engine it sucks it's useless it's used solely for the tram it provides nothing of benefit to the server
replaces them with regular engines

---
## [nalind/buildah-1](https://github.com/nalind/buildah-1)@[2adbe2a58a...](https://github.com/nalind/buildah-1/commit/2adbe2a58a77b014be59c68abf58b682ad5e5c20)
#### Saturday 2022-10-08 18:11:07 by Ed Santiago

System test cleanup: document, clarify, fix

Primary purpose: fix "preconfigured TARGETARCH/etc" test so
it will work under podman and on multiarch.

Root cause of it not working: I mistakenly advised @flouthoc,
in #4310, to write a containerfile in $TEST_SCRATCH_DIR. I
thought it was an empty directory. Big, big mistake. (Sorry,
Aditya). Document this near the variable definition, and
fix the test once again.

@nalind pointed out that the containerfile doesn't need to
be generated on-the-fly, so, use a static one. In the spirit
of DIE, read the TARGETxxx vars from it. Not that we're
expecting more variables, but, it's just cleaner.

Also, as long as I'm here: in run_buildah, when logging the
command being run, use #/$ prompt for root/rootless. I was
getting too confused looking at logs of root runs.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [qxb3/qxb3.tk](https://github.com/qxb3/qxb3.tk)@[1e44b6cd39...](https://github.com/qxb3/qxb3.tk/commit/1e44b6cd3959411b602e670fbf055532371daf2f)
#### Saturday 2022-10-08 18:16:50 by qxb3

client: adding sass to finally cutomize bulma instead of having just plain css to change stuff and feeling a headache, pain, existential crisis, i want to die pls help me

---
## [smklein/diesel](https://github.com/smklein/diesel)@[448df6b615...](https://github.com/smklein/diesel/commit/448df6b61566dbd419554fc82abd018357848846)
#### Saturday 2022-10-08 18:44:23 by Georg Semmler

Address #3173

This is a tricky one. It seems like the behaviour described in that
issue should work out of the box, but it doesn't. I've spend some time
to investigate various solutions to make this work, but I came to the
conclusion that the current behaviour is the correct one.

The underlying issue here is that such an query promotes the inner
`Nullable<_>` of the field onto the outer `Queryable` wrapper. Without
`Selectable` that would require a select clause like
`.select((table::column.assume_not_null(),).nullable())`. This is
technically a safe pattern, but requires the usage of the "advanced"
`assume_not_null()` method to forcibly convert types to their not null representation.

Possible solutions tried to make the enable constructs shown in that
issue:

* I've tried to make the `impl Selectable for Option<T>` return the
following `SelectExpression`:
`dsl::Nullable<dsl::AssumeNotNull<T::SelectExpression>>`
where `AssumeNotNull` converts each tuple element to the corresponding
not nullable expression, while `Nullable` wraps the tuple itself into a
nullable type wrapper.
* I've tried to apply a similar approach like that one above, but only
for derived impls by manipulating the generated code for a optional
field with `#[diesel(embed)]`

Both solutions require changes to our sql type system, as for example
allowing to load a non nullable value into a `Option<T>` to enable their
usage in a more general scope as the presented example case.
(See the added test cases for this). That by itself would be fine in my
opinion, as this is always a safe operation. Unfortunately the
`AssumeNotNull` transformation would be applied recursively for all
sub-tuples, which in turn would cause trouble with nested joins (again
see the examples). We would be able to workaround this issue by allowing
the `FromSql<ST, DB> for Option<T>` impl for non-nullable types to catch
null values, which in turn really feels like a bad hack. (You would like
to get an error there instead, but nested nullable information are
gone.)
All in all this lead me to the conclusion that the current behaviour is
correct.

This PR adds a few additional tests (an adjusted version of the test
from the bug report + more tests around nested joins) and does move
around some code bits that I noticed while working on this.

I think the official answer for the bug report would be: Either wrap the
inner type also in an `Option` or provide a manual `Selectable` impl
that does the "right" thing there.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[d28b3ab06b...](https://github.com/treckstar/yolo-octo-hipster/commit/d28b3ab06bf8bde00474f8685bbd9ebf41815d13)
#### Saturday 2022-10-08 19:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Brakau-TD/Course_Management_GUI](https://github.com/Brakau-TD/Course_Management_GUI)@[830e5b5e47...](https://github.com/Brakau-TD/Course_Management_GUI/commit/830e5b5e47d26d941d0de261e954b7becc9c1a46)
#### Saturday 2022-10-08 19:37:57 by Brakau-TD

Holy Shit!!!

Ich sollte vorsichtiger sein, bevor ich irgendwie viele tolle neuerungen einbaue
auch wenn ich glaube, dass die "nur" kosmetisch sind. Das sind sie nicht

Das holen der einträge aus den Listboxen ist komplex
dort müssen richtige listen abgelegt werden, erstmal egan, wie hübsch die sind

ich hab jetzt eine (halb-okaye) Version von Samstag abend 19:45 hergestellt. Hier muss ich mal deutlich schauen, was da geht.

VORSICHTIGGGGGG!!!!!!

Die Speicher-Buttons müssen erfrischt werden. Ich bin müde und muss heute aufhören

---
## [VictorGamer072YT/BackToTheFutureV](https://github.com/VictorGamer072YT/BackToTheFutureV)@[b10eba0182...](https://github.com/VictorGamer072YT/BackToTheFutureV/commit/b10eba0182f586a32f5d16c5b67317be2c1c5ac5)
#### Saturday 2022-10-08 19:43:42 by Victor

Strip the cheat menu, and unlock the spawn/photo menu

Because apparently, someone had the utterly brilliant idea to add stupid cheats to this. It's pointless, annoying, and besides, we don't even have missions or anything to justify a shitty non sandbox experience.

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[296f94d64a...](https://github.com/ammarfaizi2/linux-fork/commit/296f94d64aebe673142dd4ec5c063c7e08525648)
#### Saturday 2022-10-08 20:23:12 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Luziferium/randomizer-csgo](https://github.com/Luziferium/randomizer-csgo)@[1eb759caa8...](https://github.com/Luziferium/randomizer-csgo/commit/1eb759caa87ba2d507f5027dd1aa8dfed396dda5)
#### Saturday 2022-10-08 20:41:27 by Luziferium

yeah settings impl haha ok cool temporary. "i hate my live" ~ busted

---
## [NattyNarwhal/Submariner](https://github.com/NattyNarwhal/Submariner)@[9f01f515e4...](https://github.com/NattyNarwhal/Submariner/commit/9f01f515e4d6a26cd4888b36a0a1eb3905d9438d)
#### Saturday 2022-10-08 21:35:56 by Calvin Buckley

Wrapper class for system metadata functions

Uses AVAsset and AudioToolbox as the two strategies. Kinda ugly, but
I'm no Swift expert.

Annoyingly, the system APIs have some limitations we can't cover with
using both of them. But hey, we can always have TagLib (or keep SFBAE)
later.

---
## [ZhenjaMax/BetterBalancedGame](https://github.com/ZhenjaMax/BetterBalancedGame)@[518c3da67b...](https://github.com/ZhenjaMax/BetterBalancedGame/commit/518c3da67b9517c0554322a5f642c9ed98e34a04)
#### Saturday 2022-10-08 23:26:24 by ZhenjaMax

English lang 5.1

New lines for 5.1 patch:
Ottoman UU (naval) - can enter Ocean tiles regardless of researched Technologies;
Ottoman Ibrahim unique governor R2 promotion - +1 movement within 10 tiles of city instead of useless griveances ability;

- Goddess of the Hunt pantheon - +2 gold instead of +1 food;

- Railroad - cost increased to 2 iron & 1 coal per tile;
- Intelligence Agency - +50% production to Spies, +2 capacity (instead of +1).
- Statue of Zeus World Wonder - +35% instead of +50% to anti-cavalry;

- Agoge policy - recon (Classical and earlier);
- Feudal Contract policy - recon (Renaissance and earlier);
- Grande Armee policy - recon (Industrial and earlier);
- Military First policy - recon (all);

Edited lines for 5.1 patch:
Eleanor leader ability - works grant +1 instead of +2;
Ethiopia UU - +1 movement if starts in Hills instead of ignoring them;

Deleted lines for 5.1 patch:
Ethiopia UI - reverted to base-game (faith from adjacent mountains);
Rome UD - reverted to base-game (no culture per adjacent districts);

New other lines:
- Base ranged naval units - Range of these units (1, 2, 3, 4);
- Warrior Monk R2 Promotion - 250 Religious pressure within 6 tiles clarification;
- Victor T3 promotion - anti-air icon;
- Pingala L1 promotion - clarification what affect +100% GPP;
- Orszaghaz World Wonder (English fix) - clarification of Diplomatic favor, +1 is equal +100%;

Medina quarter policy - district icon;
Liberalism policy - district icon;
New deal policy - district icon;
Serfdom policy - charge icon;
Public Works policy - charge icon;
Logistics policy - movement icon;
Integrated Attack Logistics policy - movement icon;
Public Transport (English fix) - yields clarification;
Gothic Architecture policy (English fix) - toward Renaissance and earlier;
Wisselbanken policy (English fix) - +0.25 points (not .25), re-wrote sentence;
Machiavellianism policy - turn icon;
Containment policy - government icon;
Hallyu policy - promotion icon;
Non-stated Actors policy - promotion icon;
Press Gangs policy (English fix) - forgotten "+" character.

Edited other lines:
- Australia leader ability - turn icon;
- France civilization ability (English fix) - moved number and tourism icon near each other;
- Macedon leader ability - turn icon;
- Ottoman UB - first constructed UB grants free Governor Title; it is old artifact from v4 that nobody wrote before;
- Scotland UI - grants +1 appeal to adjacent tiles; edited sentence;
- Spain UI - 8 tiles from current capital; added Science icon;

- Divine Spark pantheon - Great People icons;
- City Patron pantheon - district icons;
- God of War and Plunder pantheon - Great People icons;

- Warlord Throne - production for all cities;
- Foreign Ministry (English fix) - moved items between sentences;

- Trench Warfare policy - for "all" (forgotten word);
- Insulae policy - district icon;

---

