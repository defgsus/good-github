## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-07](docs/good-messages/2022/2022-10-07.md)


2,092,125 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,092,125 were push events containing 3,110,204 commit messages that amount to 243,399,448 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [est31/rust-clippy](https://github.com/est31/rust-clippy)@[9e8f53d09a...](https://github.com/est31/rust-clippy/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Friday 2022-10-07 00:13:55 by bors

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
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[74586e2091...](https://github.com/Paxilmaniac/Skyrat-tg/commit/74586e2091b0793b4eca713eff890a76afbd3c89)
#### Friday 2022-10-07 00:31:14 by SkyratBot

[MIRROR] Upgrades the Modsuit Adapter Shell [MDB IGNORE] (#16669)

* Upgrades the Modsuit Adapter Shell (#70286)

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

* Upgrades the Modsuit Adapter Shell

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [Twaticus/tgstation](https://github.com/Twaticus/tgstation)@[23bfdec8f4...](https://github.com/Twaticus/tgstation/commit/23bfdec8f43046f7b54906509e38ed1ad91f5096)
#### Friday 2022-10-07 01:04:59 by LemonInTheDark

Multiz Rework: Human Suffering Edition (Contains PLANE CUBE) (#69115)


About The Pull Request

I've reworked multiz. This was done because our current implementation of multiz flattens planes down into just the openspace plane. This breaks any effects we attach to plane masters (including lighting), but it also totally kills the SIDE_MAP map format, which we NEED for wallening (A major 3/4ths resprite of all wall and wall adjacent things, making them more then one tile high. Without sidemap we would be unable to display things both in from of and behind objects on map. Stupid.)

This required MASSIVE changes. Both to all uses of the plane var for reasons I'll discuss later, and to a ton of different systems that interact with rendering.

I'll do my best to keep this compact, but there's only so much I can do. Sorry brother.
Core idea

OK: first thing.
vis_contents as it works now squishes the planes of everything inside it down into the plane of the vis_loc.
This is bad. But how to do better?

It's trivially easy to make copies of our existing plane masters but offset, and relay them to the bottom of the plane above. Not a problem. The issue is how to get the actual atoms on the map to "land" on them properly.

We could use FLOAT_PLANE to offset planes based off how they're being seen, in theory this would allow us to create lens for how objects are viewed.
But that's not a stable thing to do, because properly "landing" a plane on a desired plane master would require taking into account every bit of how it's being seen, would inherently break this effect.

Ok so we need to manually edit planes based off "z layer" (IE: what layer of a z stack are you on).

That's the key conceit of this pr. Implementing the plane cube, and ensuring planes are always offset properly.
Everything else is just gravy.
About the Plane Cube

Each plane master (except ones that opt out) is copied down by some constant value equal to the max absolute change between the first and the last plane.
We do this based off the max z stack size detected by SSmapping. This is also where updates come from, and where all our updating logic will live.

As mentioned, plane masters can choose to opt out of being mirrored down. In this case, anything that interacts with them assuming that they'll be offset will instead just get back the valid plane value. This works for render targets too, since I had to work them into the system as well.

Plane masters can also be temporarily hidden from the client's screen. This is done as an attempt at optimization, and applies to anything used in niche cases, or planes only used if there's a z layer below you.
About Plane Master Groups

BYOND supports having different "maps" on screen at once (IE: groups of items/turfs/etc)
Plane masters cannot cover 2 maps at once, since their location is determined by their screen_loc.
So we need to maintain a mirror of each plane for every map we have open.

This was quite messy, so I've refactored it (and maps too) to be a bit more modular.

Rather then storing a list of plane masters, we store a list of plane master group datums.
Each datum is in charge of the plane masters for its particular map, both creating them, and managing them.

Like I mentioned, I also refactored map views. Adding a new mapview is now as simple as newing a /atom/movable/screen/map_view, calling generate_view with the appropriate map id, setting things you want to display in its vis_contents, and then calling display_to on it, passing in the mob to show ourselves to.

Much better then the hardcoded pattern we used to use. So much duplicated code man.

Oh and plane master controllers, that system we have that allows for applying filters to sets of plane masters? I've made it use lookups on plane master groups now, rather then hanging references to all impacted planes. This makes logic easier, and prevents the need to manage references and update the controllers.

image

In addition, I've added a debug ui for plane masters.
It allows you to view all of your own plane masters and short descriptions of what they do, alongside tools for editing them and their relays.

It ALSO supports editing someone elses plane masters, AND it supports (in a very fragile and incomplete manner) viewing literally through someone else's eyes, including their plane masters. This is very useful, because it means you can debug "hey my X is yorked" issues yourself, on live.

In order to accomplish this I have needed to add setters for an ungodly amount of visual impacting vars. Sight flags, eye, see_invis, see_in_dark, etc.

It also comes with an info dump about the ui, and plane masters/relays in general.

Sort of on that note. I've documented everything I know that's niche/useful about our visual effects and rendering system. My hope is this will serve to bring people up to speed on what can be done more quickly, alongside making my sin here less horrible.
See https://github.com/LemonInTheDark/tgstation/blob/multiz-hell/.github/guides/VISUALS.md.
"Landing" planes

Ok so I've explained the backend, but how do we actually land planes properly?
Most of the time this is really simple. When a plane var is set, we need to provide some spokesperson for the appearance's z level. We can use this to derive their z layer, and thus what offset to use.

This is just a lot of gruntwork, but it's occasionally more complex.
Sometimes we need to cache a list of z layer -> effect, and then use that.
Also a LOT of updating on z move. So much z move shit.

Oh. and in order to make byond darkness work properly, I needed to add SEE_BLACKNESS to all sight flags.
This draws darkness to plane 0, which means I'm able to relay it around and draw it on different z layers as is possible. fun darkness ripple effects incoming someday

I also need to update mob overlays on move.
I do this by realiizing their appearances, mutating their plane, and then readding the overlay in the correct order.

The cost of this is currently 3N. I'm convinced this could be improved, but I've not got to it yet.
It can also occasionally cause overlays to corrupt. This is fixed by laying a protective ward of overlays.Copy in the sand, but that spell makes the compiler confused, so I'll have to bully lummy about fixing it at some point.
Behavior changes

We've had to give up on the already broken gateway "see through" effect. Won't work without managing gateway plane masters or something stupid. Not worth it.
So instead we display the other side as a ui element. It's worse, but not that bad.

Because vis_contents no longer flattens planes (most of the time), some uses of it now have interesting behavior.
The main thing that comes to mind is alert popups that display mobs. They can impact the lighting plane.
I don't really care, but it should be fixable, I think, given elbow grease.

Ah and I've cleaned up layers and plane defines to make them a bit easier to read/reason about, at least I think.
Why It's Good For The Game
<visual candy>

Fixes #65800
Fixes #68461
Changelog

cl
refactor: Refactored... well a lot really. Map views, anything to do with planes, multiz, a shit ton of rendering stuff. Basically if you see anything off visually report it
admin: VV a mob, and hit View/Edit Planes in the dropdown to steal their view, and modify it as you like. You can do the same to yourself using the Edit/Debug Planes verb
/cl

---
## [Twaticus/tgstation](https://github.com/Twaticus/tgstation)@[e5a2b0f16e...](https://github.com/Twaticus/tgstation/commit/e5a2b0f16e2bb47b0ed60e487e3c6b2dd32f81dc)
#### Friday 2022-10-07 01:04:59 by LemonInTheDark

Micros the lighting subsystem (Saves a second of init) (#69838)


About The Pull Request

Micros lighting objects, and their creation

We save a good bit of time by not walking space turfs adjacent to new objects.
We also save some time with micros in the actual underlay update logic.

I swear dude we spend like 0.8 seconds of init applying the underlay. I want threaded maptick already

Micros lighting sources, and corner creation

A: Corners were being passed just A turf, and then expected to generatecorners based on that. This is pointless.
It is better to instead pass in the coords of the bottom left turf, and then build in a circle. This saves like 0.3 seconds

B: We use so many damn datum vars in corner application that we just do not need to.
This resolves that, since it pissed me off. It's pointless. Lets cache em instead

There's some misc datum var caching going on here too. Lemme see...
Oh and a bit of shortcutting for a for loop, since it was a tad expensive on its own.

Also I removed the turfs list, because it does fucking nothing. Why is this still here.

All my little optimizations save about 1 second of init I think
Not great, but not bad, and plus actual lighting work is faster now too
Why It's Good For The Game

Speed

---
## [Twaticus/tgstation](https://github.com/Twaticus/tgstation)@[cee07f804c...](https://github.com/Twaticus/tgstation/commit/cee07f804cc1df6d9cb0ff783ad4504458cf2c8b)
#### Friday 2022-10-07 01:04:59 by LemonInTheDark

Airlock open delay audit (#69905)


About The Pull Request

A: Mineral doors no longer take 6 SECONDS to open if you bump anything beforehand. Holy shit why would you do this.
B: Airlocks no longer require you to have not bumped anything in a second, lowered to 0.3 seconds. This is safe because I've moved shock immunity to its own logic. This should make opening doors feel less horrible
Why It's Good For The Game

Feels better.
Changelog

cl
balance: Airlocks will open on bump in series much faster now. As a tradeoff, you're immune to shocks from them for a second after you last got shocked by one.
fix: Mineral doors will no longer take 6 WHOLE SECONDS to open if you've bumped something else recently
/cl

---
## [Twaticus/tgstation](https://github.com/Twaticus/tgstation)@[d45e244401...](https://github.com/Twaticus/tgstation/commit/d45e244401425d34edc38e3dd2f3c2bbdbcec7ce)
#### Friday 2022-10-07 01:10:02 by san7890

Crab-17 No Longer Breaks Economy If You Swipe Too Fast (#70094)

Hey there,

Remember swiping credit cards, before everything was chipped? You know how sometimes if you went too slow, the transaction might fail, the cashier had to plonk in some digits on their machine, and you had to go again? That kinda sucked.

If you're too young to get that reference, just imagine the card swiping task in AMONG US. Doesn't that minigame suck? You know exactly what that is. Same principle.

Anyways, that's pretty much what was going on here. The reason why SS.Economy would break so god damn hard if you swiped an ID before the machine's "boot up" slowflake animation was complete is probably due to the line where it starts fast processing. I added an early return to check for if the animation was complete by leveraging a var we already set at the end of the process, because I am lazy.

There's probably a few other ways you can tackle this issue, but this feels right to me in a thematic sense. I'm willing to change it if needed though.

---
## [eziochiu/mame_ios](https://github.com/eziochiu/mame_ios)@[ba63081d10...](https://github.com/eziochiu/mame_ios/commit/ba63081d109c904902958c6324b013cb10b42732)
#### Friday 2022-10-07 01:59:30 by 0kmg

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
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[1af2c12e05...](https://github.com/TaleStation/TaleStation/commit/1af2c12e0501c2cf5eb5946738360564fd78cea4)
#### Friday 2022-10-07 02:03:09 by TaleStationBot

[MIRROR] [MDB IGNORE] canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#2676)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

* fix

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [dynamitegus/y124.github.io](https://github.com/dynamitegus/y124.github.io)@[d54b6835fd...](https://github.com/dynamitegus/y124.github.io/commit/d54b6835fdf08638a1fe7eb6e7acff3f4591c766)
#### Friday 2022-10-07 02:51:25 by y124

Merge pull request #2 from dynamitegus/master

fuck your stupid tab key

---
## [miukimiu/eui](https://github.com/miukimiu/eui)@[2a8747414a...](https://github.com/miukimiu/eui/commit/2a8747414a1345623d99b025611ff6c78ae1aa82)
#### Friday 2022-10-07 03:24:06 by Constance Chen

Clean up styles further

- went down a bit of a rabbit hole with this, sorry - especially w/ refactoring `mathWithUnits` to accept multiple args (been on my radar for some time)

- the major bug that this work fixes is that we *can't* use a dynamic `paddingSize` based on isFullScreen because the fullscreen code block and non-fullscreen code block need separate and non-connected padding sizes

- in the end i'm still not 100% convinced the code is less 'ugly' with the new `generatePaddingCss` util but our Emotion styles are now more static at least :/ which, considering perf is already a little questionable with the tokens mixin, I thought was worth the tradeoff

---
## [facebook/hhvm](https://github.com/facebook/hhvm)@[cbeeb6fc89...](https://github.com/facebook/hhvm/commit/cbeeb6fc896d862aff10cd75bc42ee79beb962a9)
#### Friday 2022-10-07 03:39:08 by Lucian Wischik

I believe we never use changes_since_baseline

Summary:
Naming_sqlite stores a table that only ever has a single row: NAMING_LOCAL_CHANGES, whose row contains (1) an ocaml blob of local changes, (2) the revision for this saved-state.

The ocaml blob of local changes had been used for fast incremental naming table generation, as an ugly hack that was faster than generating the entire new naming-table from scratch i.e. writing 6M rows. In D31413518 (https://github.com/facebook/hhvm/commit/8f9e9d2f1568b084660bda8fe87b8725d61674d1) (Oct 2021) bobrenjc93 changed it to a much better technique, namely, inserting/removing only the delta rows. But it left behind the ocaml-blob of local changes. I wrote at the time "We should get rid of it: either in this diff or the next, delete the entire LocalChanges module." What gives us surety that it's okay to delete the ocaml-blob is that I had added telemetry D28839883 (https://github.com/facebook/hhvm/commit/330e97ccd08b144117c21a3ebefa248061d3d5ed) (June 2021) on the code-paths which read the ocaml-blob, and the telemetry shows that we only ever read an empty ocaml-blob.

But what about the second item, "(2) revision for this saved-state"? Do we ever use that? Reading the code shows that the only place "revision-for-saved-state" is ever consumed is by Hulk.v1 in a codepath that appears not to exist any longer, inside Naming_table.choose_local_changes. I think that Hulk.v1 used to provide a naming-table-delta along with the revision that the delta is with respect to, and it used to compare that revision against the naming-table-sqlite that it got from disk, and fail if they were different. This check had been introduced in D18723777 (https://github.com/facebook/hhvm/commit/7c671def9ee84762cf38e16d761c140a4bf01eca) (Nov 2019) for hulk remote workers. My hunch is that we're not using it any longer.

Therefore, this diff adds telemetry on the only codepath that uses "revision-for-saved-state" from the NAMING_LOCAL_CHANGES row. If this telemetry proves that we don't use it, and we already have telemetry which proves that ocaml-blob is always empty, then we'll be confident in deleting NAMING_LOCAL_CHANGES.

Reviewed By: bobrenjc93

Differential Revision: D40118751

fbshipit-source-id: 0b8e2eac4cfe8513cc5d0155184b7d15efd99dc8

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[4b246ab0fc...](https://github.com/san7890/bruhstation/commit/4b246ab0fc35b535c40af96fa6ec03d1ce5e7840)
#### Friday 2022-10-07 03:49:00 by san7890

i knew it fucking didn't work correclty fuck you vsc

GRR

---
## [rd-stuffs/msm-4.14](https://github.com/rd-stuffs/msm-4.14)@[3827e165e3...](https://github.com/rd-stuffs/msm-4.14/commit/3827e165e371975e53511e05a3e9143a8812752e)
#### Friday 2022-10-07 04:37:16 by Wang Han

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
Signed-off-by: Richard Raya <rdxzv.dev@gmail.com>

---
## [rajat7377/animepedia](https://github.com/rajat7377/animepedia)@[d93637aa2f...](https://github.com/rajat7377/animepedia/commit/d93637aa2f7457316f06b0f78126ade3cf2fecfc)
#### Friday 2022-10-07 06:43:01 by Rajat Dixit

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
## [qtqqtq/Skyrat-tg](https://github.com/qtqqtq/Skyrat-tg)@[e1839f0e37...](https://github.com/qtqqtq/Skyrat-tg/commit/e1839f0e375a2169c8d80d942376dddb8be1958d)
#### Friday 2022-10-07 06:44:03 by SkyratBot

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
## [AnywayFarus/tgstation](https://github.com/AnywayFarus/tgstation)@[99b8d6b494...](https://github.com/AnywayFarus/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Friday 2022-10-07 08:42:35 by vincentiusvin

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
## [moulin-louis/minishell-42](https://github.com/moulin-louis/minishell-42)@[fe834b76ad...](https://github.com/moulin-louis/minishell-42/commit/fe834b76ad27fbc71594f07a8d676ad478ae0407)
#### Friday 2022-10-07 08:59:45 by Bertrand SCHOEFFLER

working on export, sick fuck, added ut_strcmp (because we need it like hell) and other stuff

---
## [pri0818/falcon_kernel_realme_sm7125](https://github.com/pri0818/falcon_kernel_realme_sm7125)@[67abd89085...](https://github.com/pri0818/falcon_kernel_realme_sm7125/commit/67abd89085e39530e8941a67c0b472956c9d362a)
#### Friday 2022-10-07 09:06:06 by Peter Zijlstra

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
Signed-off-by: pri0818 <priyanshusinghal0818@gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[c0a9f52f45...](https://github.com/treckstar/yolo-octo-hipster/commit/c0a9f52f45be447da3f57d4e8c364580158e0e58)
#### Friday 2022-10-07 09:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [kyedodev/pdenv](https://github.com/kyedodev/pdenv)@[5f3fd24a3b...](https://github.com/kyedodev/pdenv/commit/5f3fd24a3b7301927da2375abcdb3badbffff793)
#### Friday 2022-10-07 10:35:56 by kyedodev

holy shit, things kinda work
don't have arrays yet, some things need polishing, ALMOST DONE!!

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[405e3f1479...](https://github.com/yogstation13/Yogstation/commit/405e3f1479b22535c9ed26eb944abfdde4b8e1eb)
#### Friday 2022-10-07 11:45:34 by Kylerace

Fixes Massive Radio Overtime, Implements a Spatial Grid System for Faster Searching Over Areas (#61422)

a month or two ago i realized that on master the reason why get_hearers_in_view() overtimes so much (ie one of our highest overtiming procs at highpop) is because when you transmit a radio signal over the common channel, it can take ~20 MILLISECONDS, which isnt good when 1. player verbs and commands usually execute after SendMaps processes for that tick, meaning they can execute AFTER the tick was supposed to start if master is overloaded and theres a lot of maptick 2. each of our server ticks are only 50 ms, so i started on optimizing this.

the main optimization was SSspatial_grid which allows searching through 15x15 spatial_grid_cell datums (one set for each z level) far faster than iterating over movables in view() to look for what you want. now all hearing sensitive movables in the 5x5 areas associated with each spatial_grid_cell datum are stored in the datum (so are client mobs). when you search for one of the stored "types" (hearable or client mob) in a radius around a center, it just needs to

    iterate over the cell datums in range
    add the content type you want from the datums to a list
    subtract contents that arent in range, then contents not in line of sight
    return the list

from benchmarks, this makes short range searches like what is used with radio code (it goes over every radio connected to a radio channel that can hear the signal then calls get_hearers_in_view() to search in the radios canhear_range which is at most 3) about 3-10 times faster depending on workload. the line of sight algorithm scales well with range but not very well if it has to check LOS to > 100 objects, which seems incredibly rare for this workload, the largest range any radio in the game searches through is only 3 tiles

the second optimization is to enforce complex setter vars for radios that removes them from the global radio list if they couldnt actually receive any radio transmissions from a given frequency in the first place.

the third optimization i did was massively reduce the number of hearables on the station by making hologram projectors not hear if dont have an active call/anything that would make them need hearing. so one of hte most common non player hearables that require view iteration to find is crossed out.

also implements a variation of an idea oranges had on how to speed up get_hearers_in_view() now that ive realized that view() cant be replicated by a raycasting algorithm. it distributes pregenerated abstract /mob/oranges_ear instances to all hearables in range such that theres at max one per turf and then iterates through only those mobs to take advantage of type-specific view() optimizations and just adds up the references in each one to create the list of hearing atoms, then puts the oranges_ear mobs back into nullspace. this is about 2x as fast as the get_hearers_in_view() on master

holy FUCK its fast. like really fucking fast. the only costly part of the radio transmission pipeline i dont touch is mob/living/Hear() which takes ~100 microseconds on live but searching through every radio in the world with get_hearers_in_radio_ranges() -> get_hearers_in_view() is much faster, as well as the filtering radios step

the spatial grid searching proc is about 36 microseconds/call at 10 range and 16 microseconds at 3 range in the captains office (relatively many hearables in view), the new get_hearers_in_view() was 4.16 times faster than get_hearers_in_view_old() at 10 range and 4.59 times faster at 3 range

SSspatial_grid could be used for a lot more things other than just radio and say code, i just didnt implement it. for example since the cells are datums you could get all cells in a radius then register for new objects entering them then activate when a player enters your radius. this is something that would require either very expensive view() calls or iterating over every player in the global list and calling get_dist() on them which isnt that expensive but is still worse than it needs to be

on normal get_hearers_in_view cost the new version that uses /mob/oranges_ear instances is about 2x faster than the old version, especially since the number of hearing sensitive movables has been brought down dramatically.

with get_hearers_in_view_oranges_ear() being the benchmark proc that implements this system and get_hearers_in_view() being a slightly optimized version of the version we have on master, get_hearers_in_view_as() being a more optimized version of the one we have on master, and get_hearers_in_LOS() being the raycasting version currently only used for radios because it cant replicate view()'s behavior perfectly.

---
## [acroreiser/android_kernel_lenovo_a6010](https://github.com/acroreiser/android_kernel_lenovo_a6010)@[408f6e1b7a...](https://github.com/acroreiser/android_kernel_lenovo_a6010/commit/408f6e1b7af12e051b1c234faf0b217a22efaef5)
#### Friday 2022-10-07 12:10:59 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

@acroreiser: backported to 3.10 using can_lookup() helper copied from fs/namei.c instead of d_is_dir()

---
## [ScriptGiver69/IWannaSeeYouJiggleForSure](https://github.com/ScriptGiver69/IWannaSeeYouJiggleForSure)@[a68619c1b8...](https://github.com/ScriptGiver69/IWannaSeeYouJiggleForSure/commit/a68619c1b813adb8ea37159e9f756f5442f8cc8a)
#### Friday 2022-10-07 12:30:24 by ScriptGiver69

NPCFuckerOfficial

Connection terminated. I'm sorry to interrupt you, Elizabeth, if you still even remember that name, But I'm afraid you've been misinformed. You are not here to receive a gift, nor have you been called here by the individual you assume, although, you have indeed been called. You have all been called here, into a labyrinth of sounds and smells, misdirection and misfortune. A labyrinth with no exit, a maze with no prize. You don't even realize that you are trapped. Your lust for blood has driven you in endless circles, chasing the cries of children in some unseen chamber, always seeming so near, yet somehow out of reach, but you will never find them. None of you will. This is where your story ends. And to you, my brave volunteer, who somehow found this job listing not intended for you, although there was a way out planned for you, I have a feeling that's not what you want. I have a feeling that you are right where you want to be. I am remaining as well. I am nearby. This place will not be remembered, and the memory of everything that started this can finally begin to fade away. As the agony of every tragedy should. And to you monsters trapped in the corridors, be still and give up your spirits. They don't belong to you. For most of you, I believe there is peace and perhaps more waiting for you after the smoke clears. Although, for one of you, the darkest pit of Hell has opened to swallow you whole, so don't keep the devil waiting, old friend. My daughter, if you can hear me, I knew you would return as well. It's in your nature to protect the innocent. I'm sorry that on that day, the day you were shut out and left to die, no one was there to lift you up into their arms the way you lifted others into yours, and then, what became of you. I should have known you wouldn't be content to disappear, not my daughter. I couldn't save you then, so let me save you now. It's time to rest - for you, and for those you have carried in your arms. This ends for all of us. End communication.

---
## [SaurabhGuptaGoldy/100daysofCodingChallengeofVITBhopal](https://github.com/SaurabhGuptaGoldy/100daysofCodingChallengeofVITBhopal)@[f05ed48613...](https://github.com/SaurabhGuptaGoldy/100daysofCodingChallengeofVITBhopal/commit/f05ed48613338f7a555f5a34f92b3bd06676b44c)
#### Friday 2022-10-07 12:34:33 by SAURABH GUPTA

Add files via upload

Hello my friends! 
                      Today, i introduce to 2 new person of my new journey. VIT Bhopal i.e. Vellore Institute of Technology Bhopal is my new college and VIT Bhopal has one of the great person 1st person is Shriram R Sir & 2nd person is Dr. Kanchan Lata Kashyap Ma'am. Shriram R Sir is VIT Bhopal' Placement Director and Dr. Kanchan Lata Kashyap Ma'am is Program Chair of MCA Branch Of VIT Bhopal. Both person have helping and supporting nature.

Shriram R Sir says to us that 
"Be a good driver, if you're starting then don't go for 50th step, go step by step, every step is important for next all steps"

#100daysofcodingchallenge #day_3
#vitbhopal
#Starting_Java
#objectorientedprogramming
#oracle
#HackerRank
#geeksforgeeks 
#leetcode 
#hackathon 
#hackerearth 
#C
#C++
#C#
#Python

Today is my 3rd day of #100daysofcodingchallenge and I'm practicing on Java Programming Language. Java is an object oriented programming language. Java is used for Android Development, Web development, App Development etc. Java is similar to C++ and C# or vice versa.
                   Thank you so much to Shriram R Sir and Dr. Kanchan Lata Kashyap  Ma'am.
                And special thanks to my Mom, love you mom❣️
        I'll try to giving my bestest best work of my life, thanks to my classmates for supporting to me.
              Sorry to me for late starting, but i know that 'every day is available for beginning'.

Java Bassic Topic name- Print "Hello World"

---
## [hakmad/daisy](https://github.com/hakmad/daisy)@[9d65d40b5e...](https://github.com/hakmad/daisy/commit/9d65d40b5e7d90aae78f8d04a02cb83ecca16ba6)
#### Friday 2022-10-07 14:27:26 by hakmad

Added -e postprocessing argument

I actually changed quite a bit. Here's a brief summary:
- I changed `do_postprocessing` to `run_commands`. It now takes a single
  argument which tells `subprocess` what to actually run.
- I replaced the `-c` option because I changed my mind on having a
  subparser, it seemed too complicated for what I wanted to do.
- I added a new argument: `-e`/`--execute`, which takes commands to
  execute as an argument to itself.
- I changed the help information for `-p`/`--postprocessing` slightly.

Overall, I think I'm happier with this choice. Initially I was going for
something like:
- `daisy ... -p` would run postprocessing from `config.json`.
- `daisy ... -p [commands]` would run postprocessing using `[commands]`.

The downside of that is that if you wanted to do *both*...well you
can't. The current setup is as follows:
- `daisy ... -p` will run postprocessing from `config.json` as usual.
- `daisy ... -e [commands]` will run postprocessing from `[commands]`.

Note that these aren't mutually exclusive, so if you wanted to you could
use both.

I think, in terms of things left to do:
- Add options to modify command line output (`-q`: quiet, `-v`:
  verbose). I'll probably just add one or the other, not both.
- Start breaking up the main file into seperate parts. This is a bit
  iffy given how much of the code depends on the `CONFIG` global
  variable (damnit, they were right!) and to be honest, maybe it's not
  even necessary (the entire program is under 500 SLOC including
  comments and docstrings).
- Testing. Oh god I'm not looking forward to this because I have no clue
  how to test **any of this!** How *are* you supposed to test a CLI
  application? None of the functions return anything!
- Actually release this on PyPI or something so people don't follow my
  crappy instructions of `git clone lol`.
- Maybe change how templating works, so I can give this to someone else
  and they can configure it to do something else rather than just, you
  know, blog posts and the index/about pages. Maybe a seperate projects
  page/area/thing? This is probably the most difficult and something I
  won't do until I need it, so yeah.

Other than that, this program is pretty much complete! I really don't
want to add more than what I have simply because there's no reason to.
Some of the things I have already are a bit unnecessary (I definitely
won't be using `-e` or `-c`) and I've already feature crept a *lot* so I
want to avoid any more of that. Overall, it's been a fun journey, I feel
like I learnt a lot. :)

---
## [newstools/2022-independent-nigeria](https://github.com/newstools/2022-independent-nigeria)@[f4a72fb20d...](https://github.com/newstools/2022-independent-nigeria/commit/f4a72fb20d629d8dfc2b1cedd987e033bf964eef)
#### Friday 2022-10-07 15:05:35 by Billy Einkamerer

Created Text For URL [independent.ng/nkechi-blessing-flaunts-young-lover-after-messy-break-up-with-ex-boyfriend-opeyemi/]

---
## [PistachioPiper/genshin-buddy](https://github.com/PistachioPiper/genshin-buddy)@[e32366e4c2...](https://github.com/PistachioPiper/genshin-buddy/commit/e32366e4c2601127306d3e6b846cca6fc76a6574)
#### Friday 2022-10-07 15:06:48 by Piper

thank you discord go suck a fat nut why won't you let me get a channel's name you stupid idiot i actually hate you fuck off

---
## [BryantD/itch-rpg-jams](https://github.com/BryantD/itch-rpg-jams)@[bcb591fefc...](https://github.com/BryantD/itch-rpg-jams/commit/bcb591fefc2450432b92b5749051adc9b3dc5ee4)
#### Friday 2022-10-07 15:36:34 by BryantD

Initial commit!

Status:

- crawling works
- basic listing (by gametype) works
        - but needs to be tweaked because I mishandled defaults
- I shouldn't forget that I'm half-assing dates and durations right now

Notes:

I used a lot of new tools here. I like some of them and I don't like some of them.

The combo of Click and cloup for CLI options is fun. I think I prefer this to argparse, since it's easier to read on the whole.

Dataclasses are cool. I think I'm misusing them since my ItchJam class has a lot of functionality beyond just being a dataclass, but it's fine. Saved me some typing, what more could I want?

dataset is a dead end for me. I like not having to write schema but it doesn't handle enums gracefully so I had too much extra work writing little translation hooks all over the place.

"So isn't the problem actually enums?"

"No. Shut up."

(It actually isn't; I think it's reasonable to expect a good SQL library to auto-translate between normal python types. What I really need is the moral equivalent of a NoSQL sqlite. Which is sqlite but the little efficient libraries don't tend to support SQLite's JSON support. Pickle isn't safe for this use case. Etc.)

---
## [fatimzehraa/minishell](https://github.com/fatimzehraa/minishell)@[21bbd2877a...](https://github.com/fatimzehraa/minishell/commit/21bbd2877a118c30c94014120b6b70d5ec29a3a7)
#### Friday 2022-10-07 15:45:42 by fatima-zahra

fixing what merge ruined`:	DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

Copyright (c) 2022 Author. All rights reserved.

Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

	DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
	0. You just DO WHAT THE FUCK YOU WANT TO.`

---
## [aras-p/oiio](https://github.com/aras-p/oiio)@[4ee35351f1...](https://github.com/aras-p/oiio/commit/4ee35351f100c79738c77892fb8ccca8ddc004c9)
#### Friday 2022-10-07 19:57:08 by Aras Pranckevičius

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
## [Opentrons/opentrons-python-packages](https://github.com/Opentrons/opentrons-python-packages)@[6554cce5c2...](https://github.com/Opentrons/opentrons-python-packages/commit/6554cce5c250f86f633f07f4f816a804096c6f11)
#### Friday 2022-10-07 20:33:17 by Seth Foster

feat(build): build wheels (#3)

Add the code harnessing to properly build wheels for the OT-2.

This code is a little annoying and complicated. There are three main
parts:
1. Walking the package directory and orchestrating builds (lives in
`builder.build.orchestrate)
2. Dealing with downloading and unzipping sources (lives in
`builder.build.download`)
3. Building the wheels (lives in `builder.build.build_wheel`) and the
attendant shellcall infrastructure (lives in
`builder.build.shell_environment`)

## Walking package directories and orchestrating builds

This isn't really that bad; it's a lot of path manipulation. Options
about builds are bundled up and passed around in dataclasses. The intent
is that you can add new stuff in the packages directory and it'll find
it if you put a `build.py` in there. The `build.py` is eval'd and calls
into `builder.build` with a nice interface to specify how to build the
package.

## Downloading and unzipping sources
This is a little more of the same - give us a url, we'll download it,
we'll unpack it (while trying to avoid trivial tarfile path manipulation
attacks). This stuff goes in build/.

## Building the package and handling shells
It's really annoying to deal with the shellcalls. The previous PR's test
file approached it by running the sdk environment prep once, capturing
all the stuff it did, and passing that to calls. This is weird and prone
to failure because passing environment variables to popen for some
reason is super inconsistent.

The slightly more nuclear option, which this PR does instead, is to have
a single long running interactive shell process that you send stuff to
with stdin. now, you can set up the buildroot environment in the
subshell and just send over commands. Works actually pretty well, and
also has some bonuses like "handles aliases correctly" and "you can add
a venv".

In terms of building, we need to handle build-time dependencies, which
we do via a little venv; and we need to set a whole bunch of other magic
environment flags and options that the sdk doesn't do.

Once we do all that, we can build a wheel!


Closes RCORE-209
Closes RCORE-210
Closes RCORE-215

---
## [ShizCalev/tgstation](https://github.com/ShizCalev/tgstation)@[422accbe4e...](https://github.com/ShizCalev/tgstation/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Friday 2022-10-07 20:59:48 by John Willard

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
## [rjbs/Synergy](https://github.com/rjbs/Synergy)@[0f62e29320...](https://github.com/rjbs/Synergy/commit/0f62e2932082f92df04e902810f629e029d741ae)
#### Friday 2022-10-07 23:25:12 by Ricardo Signes

WIP: a new rototron engine

This is not perfect, or probably even 10 years perfect, but I think it's
a big improvement, and should be pretty easy to finish delivering.

The old rototron worked like this:

    every week has a Weeks Since Epoch number, WSE

    every rotor has a list of workers

    for each rotor:
      candidate-list = all workers for rotor, deterministically sorted

      for each day in the week being scheduled:
        CANDIDATE: until scheduled or worker list exhausted:
          candidate = delete candidate-list[ WSE % candidate-list.size ]

          if candidate is unavailable or on leave
            next CANDIDATE

GOOD:  Because the WSE number is stable within a week, the first choice
for any day in the week is the same, as is the second.  That means a
week will favor being one person.  If that person is not available for 2
days, the same person is likely to be fallback.

BAD:  Not too much prevents week 1's first choice from being week 2's
second choice, meaning the odds of getting two weeks in a row, when
somebody is out for a week, are poorly defined.  (Insert link to number
theory about coprimality here.)

BAD:  Rotors are entirely unaware of each other, so nothing much
prevents someone being assigned three rotations in a week.

The new rototron (not fully implemented yet) works like this:

    every week has a Weeks Since Epoch number, WSE

    every rotor has a map of workers to fixed preference¹

    every rotor-worker has a level of rotor-fatigue²

    ROTOR: for each rotor:
      for every worker in worker map:
        if worker has any other rotor assignment in this date range:
          mark worker as one level less preferable

      for every level of preferability:
        select set of workers available on the most days³

        for each worker in this set:
          select set of workers with the lowest rotor-fatigue

          candidate = set[ WSE % set.size ]

          schedule candidate for all available dates in range

          redo ROTOR with unscheduled days

1: Preference is a number.  The lower the preference number, the more
   likely someone is to be scheduled.  Thing of preference:1 as being
   "first string".  For most rotors, the usual plumbers will all have
   preference 1, and I (rjbs) might have preference 3.  For escalation,
   a full-time escalation handler would have preference 1, and most
   everyone else preference 2.

2: I bet we'll want to adjust how rotor fatigue works, but right now
   your level of rotor fatigue is the number of days you were on
   rotation in the last 90 days.  This builds up every time you're on
   duty, and fades off over time.

3: If everybody is available all week, the set is everybody.  If two
   people are out one day, it's everybody but those two.  If everybody
   is out exactly one day, it's everybody again.

Rotor fatigue probably has two problems.  First, if a rotation is done
by one person for 90d and then a second person is added to rotation with
the same preference, they'd be on rotation 45d before getting a break.
be on rotation for 45d straight.  Second, it's per-rotor, which may or
may not be noticeable over time.  Still, it should be easy to adjust its
behavior over time, and this was easy to implement.

The next likely steps are:

1.  Replace the availability checker callback with something acting kind
    of or exactly like the AvailabilityChecker class in Rototron1.

2.  Treat the rototron's own schedule (persisted in SQLite or something)
    as canonical, with the JMAP duty roster calendar treated as a
    published copy.

---
## [FWest98/OS-Windows_Terminal](https://github.com/FWest98/OS-Windows_Terminal)@[b4b6636b49...](https://github.com/FWest98/OS-Windows_Terminal/commit/b4b6636b4952ac8ff6a9864f641973bb49d91ce4)
#### Friday 2022-10-07 23:39:47 by Mårten Rånge

Relax shader strictness in RELEASE mode (#13998)

Disables strictness and warnings as errors for custom pixel shaders in
RELEASE. Windows terminal is not telling the user why the shader won't
compile which makes it very frustrating for the shader hacker.

After trying the recent preview none of my shaders loaded anymore in
Windows Terminal Preview which made me very sad. I had no idea what was
wrong with them. After cloning the git repo, building it, fighting an
issue that prevent DEBUG SDK from being used I finally was able to
identify some issues that were blocking my shaders.

> error X3556: integer modulus may be much slower, try using uints if possible.
> error X4000: use of potentially uninitialized variable (rayCylinder)

While the first one is a good warning I don't think it is an error and
the tools I use didn't flag it so was hard to know.

The second one I was staring at the code and was unable to identify what
exactly was causing the issues, I fumbled with the code a few times and
just felt the fun drain away.

IMHO: I want it to be fun to develop shaders for windows terminal.
Fighting invisible errors are not fun. I am not after building
production shaders for Windows Terminal, I want some cool effects. So
while I am as a .NET developer always runs with Warning as errors I
don't think it's the right option here. Especially since Windows
Terminal doesn't tell what is the problem.

However, I understand if the shaders you ship with Windows Terminal
should be free of errors and silly mistakes, so I kept the stricter
setting in DEBUG mode.

## Validation Steps Performed

Loaded Windows Terminal in RELEASE and DEBUG mode and validated that
RELEASE mode had reduced strictness but DEBUG retained the previous more
restrictive mode.

---
## [tyrant/50ftclit](https://github.com/tyrant/50ftclit)@[aca06d22e2...](https://github.com/tyrant/50ftclit/commit/aca06d22e2bbf9f8238a3072a39c74e2022d0495)
#### Friday 2022-10-07 23:41:46 by Mikey Clarke

Reduced Ruby version again, 3.0.2->2.7.4

Dear god. I attempted to install 3.0.2 on Prod ... but this time hit a 'gcc: internal compiler error: Killed (program cc1)', which monstrous amounts of googling tells me is Prod genuinely literally running out of memory. Aah. Yes I could fall to Devops and start Rackspace-ly configuring Prod and getting this shit sorted out properly (including bumping up its Ubuntu Server LTS to the latest LTS and not whatever the hell I'd most recently set it as, decades back) but that'll take all day. Fuckit. Let's just use Prod's latest already-existing Ruby, 2.7.4.

---

