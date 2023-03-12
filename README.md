## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-11](docs/good-messages/2023/2023-03-11.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,917,132 were push events containing 2,610,269 commit messages that amount to 161,136,673 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 50 messages:


## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[6f1b1717a7...](https://github.com/morrowwolf/cmss13/commit/6f1b1717a7d6ef3c04ef58c294353fe0b98ca836)
#### Saturday 2023-03-11 00:52:07 by TotalEpicness

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
## [jhnc-oss/NetworkManager](https://github.com/jhnc-oss/NetworkManager)@[b77dc5e8db...](https://github.com/jhnc-oss/NetworkManager/commit/b77dc5e8db37669e248b68e64b552b8c36327b96)
#### Saturday 2023-03-11 01:05:23 by Thomas Haller

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
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[91f06a97d3...](https://github.com/Jolly-66/dragon-station/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Saturday 2023-03-11 01:37:13 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[d95ca04819...](https://github.com/Jolly-66/dragon-station/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Saturday 2023-03-11 01:37:13 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [PJB3005/space-station-14-content](https://github.com/PJB3005/space-station-14-content)@[581e8a0d12...](https://github.com/PJB3005/space-station-14-content/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Saturday 2023-03-11 03:08:34 by eclips_e

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
## [SrRapero720/LittleFrames-1.18.2](https://github.com/SrRapero720/LittleFrames-1.18.2)@[bd445909f3...](https://github.com/SrRapero720/LittleFrames-1.18.2/commit/bd445909f3547837122581eefe49822d718a5c9b)
#### Saturday 2023-03-11 03:33:42 by SrRapero720

Removed all LittleTiles dependency (fuck you CreativeMD)

---
## [lordkekz/ourMIPS](https://github.com/lordkekz/ourMIPS)@[5786aea2ab...](https://github.com/lordkekz/ourMIPS/commit/5786aea2ab9bbc38fbd59767331310e9699dd3cc)
#### Saturday 2023-03-11 04:01:51 by lordkekz

More weird folder shit and stuff, it's 4am and I've spent 6 hours banging my head against my keyboard because I couldn't figure out that Rider fails to debug the desktop avalonia app because of PublishSingleFile

Also I renamed folders again
i was stupid

---
## [ubinix-warun/seedsigner](https://github.com/ubinix-warun/seedsigner)@[d2a657f2d4...](https://github.com/ubinix-warun/seedsigner/commit/d2a657f2d43c6e77e9c48cb1f859e8f4984a5f00)
#### Saturday 2023-03-11 05:29:36 by Marc G

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
## [786aafreen/JennyK](https://github.com/786aafreen/JennyK)@[5d2cc758c3...](https://github.com/786aafreen/JennyK/commit/5d2cc758c39a3900c8a5146f311497c3e776bd0f)
#### Saturday 2023-03-11 05:43:01 by Aafreen Khan

Add files via upload

It is a dream of many of us to go to Hogwarts and learn magical spells just like Harry Potter and his friends. I always wanted to learn how I can be invisible. Harry had a cloak which could turn him invisible. That cloak was known as Cloak of Invisibility. 
Shukra Allahamdulillah ...Finally I did it so here the journey begins woahhhh...

---
## [mshurkaeu-public/i-care.by](https://github.com/mshurkaeu-public/i-care.by)@[c9013093fa...](https://github.com/mshurkaeu-public/i-care.by/commit/c9013093fa239ea41dae7dda80f1a1f60a896217)
#### Saturday 2023-03-11 05:45:28 by Mikalai Shurkaeu

The very first draft for #1

Developed during period 2023-02-15 - 2023-03-10.

Originally the idea in the issue was to create a mobile app with a name
like "who-is-he-how-is-she-meter".

When I started to work on the implementation I realized that it actually
would do the very basic and useful things to care about the most important
person in user's life. Thus I decided that the name of the app would be
something like "i-care.by <platform> app".

I chose Flutter to write code once and then compile it to different
target platforms.

"i-care.by web app" is available at
https://mshurkaeu-public.github.io/i-care.by-app/web/

In this first commit the following is implemented:
1. User preferences (name and preferred pronoun).
2. Display the list of the diary records on home page.
3. Editing today record (- want to do today, - emotions in that moment,
   - done today, - emotions in that moment)
4. Options to answer "who is the most important person in your life" are
   randomized on each run, so the user needs to focus and find the
   appropriate one.

Each day the application asks (trigerred by user)
1. Who is the most important person in your life?
2. What do you want to do for the person today?
3. What are your emotions and feelings in this moment?
--
then, presumably in the second part of the day,
4. What did you do for the person today?
5. What are you emotions and feelings in this moment?

The answers are recorded and stored in json format.
On web platform - in window.localStorage.
On other platforms - in application documents folder.
----

I want to say thank you to the following people, who helped me to create
this first draft (chronological order, most recent go first):

- my father, Nikolai Slon - provided valuable feedback about my texts.
  And that helped make the texts more clear.

- Olga Shramenok (Spasibyonok) and Arina Shramenok - provided valuable
  feedback about their vision of use cases for the application. That helped
  me better understand my own vision of the target audience and clarify
  messages, shown in the app.

- Maxim Khaletsky - provided valuable feedback about texts.
  Some of his ideas are not fully reviewed yet. But some of the issues, he
  found, are already fixed in this commit.

- Maksim Lakatkou - helped to find some typos and also push me in the
  direction to make texts more friendly. That led to the introduction of
  gender specific setting in the application and thus more friendly texts.

- Viachaslau Lyskouski - recommended me to use Flutter to achieve my goal
  "one code -> many target platforms". I han't knew about Flutter before that.

There were couple of more people, who helped and provided their feedback.
But I don't know if they are OK that their names are mentioned here. So,
thank you, Ch. D. and N. M., for your feedback.

---
## [Aidyn-A/pytorch](https://github.com/Aidyn-A/pytorch)@[11aab72dc9...](https://github.com/Aidyn-A/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Saturday 2023-03-11 06:22:05 by Driss Guessous

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
## [AtlasMediaGroup/TotalFreedomMod](https://github.com/AtlasMediaGroup/TotalFreedomMod)@[631b691518...](https://github.com/AtlasMediaGroup/TotalFreedomMod/commit/631b691518b13f1f92f3ed01285ae40e76f7a913)
#### Saturday 2023-03-11 06:53:37 by Video

General corrections
- Removes JDA as a dependency as we do not use that shit
- Fixes fuck-up on my end where I didn't think Paul used the libraries part of spigot.yml but he actually did

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[2cbb4fdb74...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/2cbb4fdb7402bf3c808da0ce5063a786fcf5ca09)
#### Saturday 2023-03-11 07:42:27 by Adam Joseph

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
## [DawfukFR/stellaris_kernel_oneplus_sm8250](https://github.com/DawfukFR/stellaris_kernel_oneplus_sm8250)@[b941f330d3...](https://github.com/DawfukFR/stellaris_kernel_oneplus_sm8250/commit/b941f330d388d2d159f6807531efad67b022e782)
#### Saturday 2023-03-11 08:55:10 by Wang Han

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
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[d240a2a0af...](https://github.com/Lamella-0587/Skyrat-tg/commit/d240a2a0afe11612fe14cbbcd29bb6744218308c)
#### Saturday 2023-03-11 08:58:33 by SkyratBot

[MIRROR] Brings the monkey back down (body horror edition/addition.) [MDB IGNORE] (#19572)

* Brings the monkey back down (body horror edition/addition.) (#73325)

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

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

* Brings the monkey back down (body horror edition/addition.)

* Update species.dm

* Delete infuser_entries.dm

---------

Co-authored-by: itseasytosee <55666666+itseasytosee@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[bd59288267...](https://github.com/Danielkaas94/DTAP/commit/bd592882674939c17bb996476132ca24c7637930)
#### Saturday 2023-03-11 09:03:44 by Danielkaas94

Sweet Disposition 💕
Sweet disposition, never too soon
Oh, reckless abandon
Like no one's watching you
A moment, a love, a dream aloud
A kiss, a cry, our rights, our wrongs
A moment, a love, a dream aloud
A moment, a love, a dream aloud

So stay there
Cause I'll be coming over
And while our blood's still young
It's so young, it runs
And won't stop till it's over
Won't stop to surrender

Songs of desperation
I played them for you
A moment, a love, a dream aloud
A kiss, a cry, our rights, our wrongs
A moment, a love, a dream aloud
A moment, a love, a dream aloud

So stay there
Cause I'll be coming over
And while our blood's still young
It's so young, it runs
And won't stop till it's over
Won't stop to surrender

Won't stop till it's over
Won't stop to surrender

---
## [NotLebedev/nushell](https://github.com/NotLebedev/nushell)@[378a3ae05f...](https://github.com/NotLebedev/nushell/commit/378a3ae05f5459a64f97af3781d4336c35652db4)
#### Saturday 2023-03-11 09:08:47 by Kovacsics Robert

Use `with-env` to avoid calling external command on invalid command (#8209)

# Description

My terminal emulator happens to be called `st`
(https://st.suckless.org/) which breaks these tests for me

_(Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.)_

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes

_(List of all changes that impact the user experience here. This helps
us keep track of breaking changes.)_

# Tests + Formatting

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
## [coryee/qemu](https://github.com/coryee/qemu)@[8d0efbcfa0...](https://github.com/coryee/qemu/commit/8d0efbcfa0656bef76e95d40933b6243feca58c9)
#### Saturday 2023-03-11 09:29:01 by Paolo Bonzini

docs: build-platforms: refine requirements on Python build dependencies

Historically, the critical dependency for both building and running
QEMU has been the distro packages.  Because QEMU is written in C and C's
package management has been tied to distros (at least if you do not want
to bundle libraries with the binary, otherwise I suppose you could use
something like conda or wrapdb), C dependencies of QEMU would target the
version that is shipped in relatively old but still commonly used distros.

For non-C libraries, however, the situation is different, as these
languages have their own package management tool (cpan, pip, gem, npm,
and so on).  For some of these languages, the amount of dependencies
for even a simple program can easily balloon to the point that many
distros have given up on packaging non-C code.  For this reason, it has
become increasingly normal for developers to download dependencies into
a self-contained local environment, instead of relying on distro packages.

Fortunately, this affects QEMU only at build time, as qemu.git does
not package non-C artifacts such as the qemu.qmp package; but still,
as we make more use of Python, we experience a clash between a support
policy that is written for the C world, and dependencies (both direct
and indirect) that increasingly do not care for the distro versions
and are quick at moving past Python runtime versions that are declared
end-of-life.

For example, Python 3.6 has been EOL'd since December 2021 and Meson 0.62
(released the following March) already dropped support for it.  Yet,
Python 3.6 is the default version of the Python runtime for RHEL/CentOS
8 and SLE 15, respectively the penultimate and the most recent version
of two distros that QEMU would like to support.  (It is also the version
used by Ubuntu 18.04, but QEMU stopped supporting it in April 2022).

There are good reasons to move forward with the deprecation of Python
3.6 in QEMU as well: completing the configure->meson switch (which
requires Meson 0.63), and making the QAPI generator fully typed (which
requires newer versions of not just mypy but also Python, due to PEP563).

Fortunately, these long-term support distros do include newer versions of
the Python runtime.  However, these more recent runtimes only come with
a very small subset of the Python packages that the distro includes.
Because most dependencies are optional tests (avocado, mypy, flake8)
and Meson is bundled with QEMU, the most noticeably missing package is
Sphinx (and the readthedocs theme).  There are four possibilities:

* we change the support policy and stop supporting CentOS 8 and SLE 15;
  not a good idea since CentOS 8 is not an unreasonable distro for us to
  want to continue to support

* we keep supporting Python 3.6 until CentOS 8 and SLE 15 stop being
  supported.  This is a possibility---but we may want to revise the support
  policy anyway because SLE 16 has not even been released, so this would
  mean delaying those desirable reasons for perhaps three years;

* we support Python 3.6 just for building documentation, i.e. we are
  careful not to use Python 3.7+ features in our Sphinx extensions but are
  free to use them elsewhere.  Besides being more complicated to understand
  for developers, this can be quite limiting; parts of the QAPI generator
  run at sphinx-build time, which would exclude one of the areas which
  would benefit from a newer version of the runtime;

* we only support Python 3.7+, which means CentOS 8 CI and users
  have to either install Sphinx from pip or disable documentation.

This proposed update to the support policy chooses the last of these
possibilities.  It does by modifying three aspects of the support
policy:

* it introduces different support periods for *native* vs. *non-native*
  dependencies.  Non-native dependencies are currently Python ones only,
  and for simplicity the policy only mentions Python; however, the concept
  generalizes to other languages with a well-known upstream package
  manager, that users of older distributions can fetch dependencies from;

* it opens up the possibility of taking non-native dependencies from their
  own package index instead of using the version in the distribution.  The
  wording right now is specific to dependencies that are only required at
  build time.  In the future we may have to refine it if, for example, parts
  of QEMU will be written in Rust; in that case, crates would be handled
  in a similar way to submodules and vendored in the release tarballs.

* it mentions specifically that optional build dependencies are excluded
  from the platform policy.  Tools such as mypy don't affect the ability
  to build QEMU and move fast enough that distros cannot standardize on
  a single version of them (for example RHEL9 does not package them at
  all, nor does it run them at rpmbuild time).  In other cases, such as
  cross compilers, we have alternatives.

Right now, non-native dependencies have to be download manually by
running "pip" before "configure".  In the future, it will be desirable
for configure to set up a virtual environment and download them in the
same way that it populates git submodules (but, in this case, without
vendoring them in the release tarballs).

Just like with submodules, this would make things easier for people
that can afford accessing the network in their build environment; the
option to populate the build environment manually would remain for
people whose build machines lack network access.  The change to the
support policy neither requires nor forbids this future change.

[Thanks to Daniel P. Berrangé, Peter Maydell and others for discussions
 that were copied or summarized in the above commit message]

Cc: Markus Armbruster <armbru@redhat.com>
Cc: Peter Maydell <peter.maydell@linaro.org>
Cc: John Snow <jsnow@redhat.com>
Cc: Kevin Wolf <kwolf@redhat.com>
Reviewed-by: Daniel P. Berrangé <berrange@redhat.com>
Reviewed-by: Alex Bennée <alex.bennee@linaro.org>
Signed-off-by: Paolo Bonzini <pbonzini@redhat.com>

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[f22a6af11c...](https://github.com/Danielkaas94/DTAP/commit/f22a6af11c259de6d84a63539407e9da0298a560)
#### Saturday 2023-03-11 09:34:54 by Danielkaas94

Here With Me ❣🏖❣
Watch the sun rise along the coast
As we're both getting old
I can't describe what I'm feeling
And all I know is we're going home
So please don't let me go
Don't let me go

And if it's right, I don't care how long it takes
As long as I'm with you I've got a smile on my face
Save your tears, it'll be okay
All I know is you're here with me

Watch the sun rise as we're getting old, oh oh
I can't describe oh, oh
I wish I could live through every memory of you
Just one more time before you float off in the wind
And all the time we spent
Waiting for the light to take us in
Have been the greatest moments of my life

I don't care how long it takes
As long as I'm with you I've got a smile on my face
Save your tears, it'll be okay
You're here with me

I can't describe

---
## [lordofpipes/prismlauncher.org](https://github.com/lordofpipes/prismlauncher.org)@[eda0200a36...](https://github.com/lordofpipes/prismlauncher.org/commit/eda0200a36453d4a0d65156bc80c4e05001b2104)
#### Saturday 2023-03-11 10:41:13 by lordpipe

improve java tutorial, instructions for aarch64

Hello! I am the author of the MinecraftHopper Java installation tutorial, here to help potentially rewrite most of this page for clarity.

Having this article in the first place is, of course, a stopgap measure until https://github.com/PrismLauncher/PrismLauncher/pull/285 is implemented and solves all these problems without the user having to do anything. But we should improve it anyways, as it has become a source of confusion.

CSS changes
===========

`<code>` blocks
---------------

Currently, light mode is a typographic disaster whenever `<code>` blocks are used. So I changed the background color from black to a light gray, so it displays similar to Github-flavored markdown. Might have just been a case where nobody tested light mode :D

Also, `border-radius` wasn't working because this is a CSS property that only accepts `px`, not `em`. It also had no padding to make it look non-janky.

Tables
------

Tables haven't been used on the wiki yet, so they had no borders. So I gave them a subtle border color.

Explanation of OpenJDK
======================

I've edited the article to include an explanation for why OpenJDK is preferred over Oracle.

Instructions for checking CPU architecture
==========================================

CPU architectures are becoming increasingly confusing as MacOS users don't know that M1 means aarch64, and Windows users are increasingly buying ARM tablets. This is especially a problem because on aarch64 platforms that emulate x86-64, downloading the wrong version can cause performance problems without any indication as to what the issue is. So we should provide detailed instruction on how to check.

Download Links
==============

It's almost impossible to choose between the numerous nearly identical Java distributions, but for various reasons we can't just recommend one single JDK, because the compatibility table is... complicated. Nevertheless, here is my rationale:

**Microsoft OpenJDK**

- It is the exact same binary shipped with the vanilla launcher, so in theory it should have slightly less issues than other distributions
- Microsoft OpenJDK is the only vendor that has explicitly promised permanent URLs for directly downloading the latest LTS. This means we can link directly to installers without the links going out of date.
    - A notable exception is they lack short URLs for macOS `.pkg` files. This may be coming in the future, though.
- "Microsoft" is particularly non-scary name for a game made by Microsoft. Some users have misplaced fear of malware when they hear unknown names like Azul or Temurin
- They have aarch64 builds for Windows and macOS
- **Con:** They don't have Java 8 or any builds for x86
- **Con:** It is open source, but it lacks the open source build infrastructure that Adoptium has. But it's not like the other distributions have reproducible builds anyways.

Therefore, this is the best link to use for downloading JDK 17 for Windows x64 and aarch64, and macOS x64 and aarch64.

**Temurin OpenJDK**

- They have 32 bit builds for all platforms
- They have a good landing page with architecture detection when you press the JDK 17 download button
- They have a Debian repository to replace the missing jdk8 in Debian 10+
- **Con:** They do not have aarch64 builds of Java 8 for macOS

Therefore, this is the best link for downloading JDK 17 for Windows x86, JDK 8 for Windows, JDK 8 for macOS aarch64, and JDK 8 for Debian.

**Azul OpenJDK**

- They provide JDK 8 for macOS aarch64. The only other vendor that has this is Coretto
- **Con:** They have an awful landing page that has you scrolling through 2 pages of Azul's products before reaching the downloads section

Therefore, this is the best link for downloading JDK 8 for macOS aarch64.

**❌ Amazon Coretto**

- I've heard they have the most complete debug symbols, which could in rare cases help with a native code crash
- Otherwise a good Java distribution, similar to Temurin, Azul, Microsoft
- **Con:** Most confusing download page, you have to scroll a box that doesn't have a scrollbar
- **Con:** Nobody likes Amazon (has nothing to do with the quality of the distribution, but maybe someone out there will think Alexa will eat their PC if they use it)

It's not necessary to provide a link to this

**❌ OpenJ9**

- **Con:** Breaks compatibility with mods

It's not necessary to provide a link to this

**❌ GraalVM**

- **Con:** Breaks compatibility with mods

It's not necessary to provide a link to this

**❌ Oracle Java**

- **Con:** Oracle likes to sue their users
- **Con:** Certain downloads are gated by account signup. This is so they can collect info on your employer so they can sue you

It's not necessary to provide a link to this, except for Intel graphics workarounds

Linux section
=============

I've changed the commands to download JDK instead of JRE, because some mods require a full JDK to be installed and this is what the vanilla launcher comes with.

More distributions are now named in the section titles. Added instructions for Alpine Linux, too.

Re-ordering of sections
=======================

For some reason "Using Java" was placed under "Special Cases", so I've moved it up

---
## [dcunited001/zettelkasten](https://github.com/dcunited001/zettelkasten)@[44c985f4a4...](https://github.com/dcunited001/zettelkasten/commit/44c985f4a48e02889223534c6ae303766509d419)
#### Saturday 2023-03-11 12:37:01 by David Conner

seems like a great time to mention: "FUCK YOU DEA"

---
## [Fateussy/FateTranslations](https://github.com/Fateussy/FateTranslations)@[d6cbeb45f5...](https://github.com/Fateussy/FateTranslations/commit/d6cbeb45f516020b472afbdedc572455884af304)
#### Saturday 2023-03-11 13:12:08 by Fateussy

Gewman twanswation

One thing I don't know why
It doesn't even matter how hard you try
Keep that in mind, I designed this rhyme
To explain in due time
All I know
Time is a valuable thing
Watch it fly by as the pendulum swings
Watch it count down to the end of the day
The clock ticks life away
It's so unreal
Didn't look out below
Watch the time go right out the window
Tryin' to hold on, did-didn't even know
I wasted it all just to watch you go
I kept everything inside and even though I tried
It all fell apart
What it meant to me will eventually
Be a memory of a time when I tried so hard
I tried so hard and got so far
But in the end it doesn't even matter
I had to fall to lose it all
But in the end it doesn't even matter
One thing, I don't know why
It doesn't even matter how hard you try
Keep that in mind, I designed this rhyme
To remind myself how I tried so hard
In spite of the way you were mockin' me
Acting like I was part of your property
Remembering all the times you fought with me
I'm surprised it got so far
Things aren't the way they were before
You wouldn't even recognize me anymore
Not that you knew me back then
But it all comes back to me in the end
You kept everything inside and even though I tried
It all fell apart
What it meant to me will eventually
Be a memory of a time when I tried so hard
I tried so hard and got so far
But in the end it doesn't even matter
I had to fall to lose it all
But in the end it doesn't even matter
I've put my trust in you
Pushed as far as I can go
For all this
There's only one thing you should know
I've put my trust in you
Pushed as far as I can go
For all this
There's only one thing you should know
I tried so hard and got so far
But in the end it doesn't even matter
I had to fall to lose it all
But in the end it doesn't even matter

---
## [Dhruv146/INFINEON_HACKATHON](https://github.com/Dhruv146/INFINEON_HACKATHON)@[aff7448e0e...](https://github.com/Dhruv146/INFINEON_HACKATHON/commit/aff7448e0ea8f7c3b1946e000c6956dca068fbdd)
#### Saturday 2023-03-11 13:31:17 by Dhruv146

Add files via upload

I had the opportunity to collaborate with my friends Krishil Rana, Aditya Pachchigar, and Bhargav Patel on exciting challenges and the development of innovative projects.

The problem statement was to create a GUI application for a chess board that would place pieces based on given data and find the closest safe position for the white piece. And we were supposed to optimize the data structure as well as the algorithm used for it.

One of the aspects of the hackathon that I appreciated the most was the opportunity to learn from industry experts who were on hand to provide guidance and support. I also valued the opportunity to interact with other people who shared my interests.

Everyone worked extremely hard and went above and beyond to create something truly exceptional, creating an electrifying atmosphere.
The level of ingenuity and creativity on display was astounding, and I left the event feeling energized and determined to continue pursuing my passion for technology.

Fortunately, my team and I won First Place in the Track "Smart Navigator" and received a Certificate of Achievement, a coffee mug, and a Rs. 20,000 Amazon Gift Card.

---
## [sthagen/facebook-pyre-check](https://github.com/sthagen/facebook-pyre-check)@[f3354a9fbc...](https://github.com/sthagen/facebook-pyre-check/commit/f3354a9fbc84f8521180c5948e53bc1b05a1fc2e)
#### Saturday 2023-03-11 13:43:18 by Steven Troxler

Avoid using an alias for AsyncContextManager

Summary:
For unknown reasons, Pyre is unhappy with the current implementation
of `typing.pyi`, which uses a generic type alias to `AbstractAsyncContextManager`
for `AsyncContextManager`.

Debugging this could be difficult - Pyre doesn't really provide us with any clue
about why a type is invalid, so we'll probably need to spend time doing a deep
dive: I filed T146882109 to investigate this in more detail but in my opinion we
really need to prioritize bumping typeshed

(Justification for why a patch and bump is better than filing a task
and claiming that it blocks typeshed upgrade:
- having a bunch of patches to maintain is tech debt, but it is very explicit;
  we can look at the patches and see exactly how many fixes are needed. And
  updating the patches, while annoying, is pretty easy (maybe 2-5 minutes per patch
  per update).
- sitting on an old typeshed, on the other hand, involves exactly the same bugs
  except they are accumulating invisibly, plus users aren't getting the benefit of new
  typeshed features; we've now been explicitly asked to bump at least twice

**How the vendored part of this diff was created**

```
# iterate on this until new patch applies cleanly
rm -rf ~/patched_typeshed
buck2 run //tools/pyre/scripts:download_typeshed -- -p ~/fbsource/fbcode/tools/pyre/scripts/typeshed-patches -o ~/patched_typeshed -u https://api.github.com/repos/python/typeshed/zipball/8aedbda4cdff81478b7414e46c400ad016342e02

# once patches look good, update the vendored code
rm -rf ~/fbsource/fbcode/tools/pyre/stubs/typeshed/typeshed
cp -R ~/patched_typeshed/typeshed ~/fbsource/fbcode/tools/pyre/stubs/typeshed/typeshed
```

(note that the `-u` flag is pinning to the URL discovered in the very first run when creating D43666059 - you want to omit it when starting a typeshed bump, but then pin it after that so that new commits to typeshed don't break all your patches).

Reviewed By: grievejia

Differential Revision: D43680647

fbshipit-source-id: 18e2d04b9b545f9e1a844b4eddad68066ee1f9a8

---
## [ShitijHalder/shitijhalder.github.io](https://github.com/ShitijHalder/shitijhalder.github.io)@[7fce589e31...](https://github.com/ShitijHalder/shitijhalder.github.io/commit/7fce589e3147836b2ecb941da3fdaab43e8d4749)
#### Saturday 2023-03-11 14:15:37 by SHITIJ

Files Update - New Blog Section added.

In this update, new Blog section is added and CSS files are also updated, making it more smoother and responsive. New icons are added with fresh codes of Java Script. New blocks are implemented in the blog section making the UI more beautiful. Daily Blog section will include 2 things mainly focused on (i) Blogging (ii) Personal Experiences. This section will show you my daily blogs and my personal experiences of my life.
If you find any bugs fell free to text me and report about it, I will fix it as soon as possible.

---
## [StonecoldLi/A-simple-CNN-to-classify-the-broken-or-unbroken-beam](https://github.com/StonecoldLi/A-simple-CNN-to-classify-the-broken-or-unbroken-beam)@[552eb7cb59...](https://github.com/StonecoldLi/A-simple-CNN-to-classify-the-broken-or-unbroken-beam/commit/552eb7cb59d80d7078d640844f41f0d8c0eb0cf8)
#### Saturday 2023-03-11 15:07:08 by StonecoldLi

Add files via upload

The training photos are over 100 pictures so I couldn't upload that, so sorry about that. Well, my method to create the training-photos-folders is to use AE (by editing the videos I provided here) and to get .jpeg files into the folders (which are directly named with 'broken' and 'unbroken'). Then you can use this shit-assed-like CNN to get a prediction of the new photo of the beam, however, the results showed0 pretty good, tks again!  There are totally 3 main steps in this project CREATE THE PICKLE FILE (loading_data_color.py), SET MODELS(set_models_flowers_color.py) and also I provide each type of beams for 2 test_pictures and you can use easy_gui_predcition.py to try for the prediction!

---
## [k2project/nt-mern](https://github.com/k2project/nt-mern)@[ea341e6b46...](https://github.com/k2project/nt-mern/commit/ea341e6b46cfaa8fff49731f54dbf06a2dd8c90b)
#### Saturday 2023-03-11 15:10:28 by Kris

Podcasts updates.

Please can you remove the BACP logo on the home page.
On the FAQ about working online, please can we change those circles to either the question mark or the numbers on the home page.
On FAQ please can we make WHAT IS PSYCHOTHERAPY? Bold.
On Blog can we change opinion piece to BLOG ARTICLE.
I like the question mark thing, can we try a small one to the left of Nujoji Calvocoressi Psychotherapy in the header?
Can you give me a bit more chin in my profile pic pls.
Is there a way that when you get to the bottom of the page it scrolls onto the next page?
Can we move the two new books to the top of the book section (Klein and Hirsch).
Let’s move down EMDR and ARE YOU LOST IN THE WORLD LIKE ME to the bottom videos and replace thumbnail with the rat attached.
Kirk Honda should be Dr Kirk Honda
Please can you replace the room image with ROOM 4 Geo.
Can we make the dummy a little darker like in the attached.
On the contact page can we hyperlink the addresses in the right box and change the map square on the left to a big question mark and hyperlink to https://en.wikipedia.org/wiki/Question_mark and maybe a small thumbnail photo of me in the corner, perhaps in black and white. This is a different image.
Do you think we should display an email address on the website if people don’t want to use the box?
Is something happening to Google Analytics? Is it closing down?
On the Inside Time article, when you expand, please can it show the Inside Time logo.
What do you think that on each page somewhere different on the squares section on the lines we have a small butterfly? I might be getting carried away but could look interesting. Maybe a little bigger than the ones on the chairs.
Do I need a pop-up cookie banner?
Can we try these background colours (attached) going dark – light in the order of the tabs, left – right.
On the home page – underneath bottom right-hand square in the white text box can we do a CTA to contact and remove the one from the top box.
On the blog page top right can we do a CTA to FAQ.
https://kijo.co.uk/blog/luxury-web-design-techniques-2021/ I like the custom curser.
Can we do some hidden animation on the navigation buttons? Make them jiggle or something.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[785120cb24...](https://github.com/treckstar/yolo-octo-hipster/commit/785120cb2458fa2fe904a8f55823809c4864c8a6)
#### Saturday 2023-03-11 16:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [V-Sekai/godot](https://github.com/V-Sekai/godot)@[6ef48bbf3f...](https://github.com/V-Sekai/godot/commit/6ef48bbf3f04e4499157cd1f3031b703d6ddbbc8)
#### Saturday 2023-03-11 16:29:55 by Rémi Verschelde

Bump version to 4.0-stable \o/

4 years of development.
12,000 merged pull requests.
7,000 fixed issues.
1,500 individual contributors across engine and docs.

The Godot 4.0 release is by all metrics our biggest release so far.
No stone has been left unturned, all parts of the engine have been
modernized, refactored, overhauled, rewritten, redesigned.

Our work is far from done. Many areas still have significant known issues,
and will require focused work from all willing contributors to fix blocking
bugs, implement missing features, optimize for performance or compatibility,
and improve the user experience.

But Godot 4.0 marks the start of the new, modern Godot Engine, and a solid
foundation for us all to build upon. Future 4.x releases will come with a
much faster cadence, enabling us to iterate quickly on new features and
improvements to what we already provide.

To all of you who were involved in making Godot 4.0 what it is today, however
big or small your contributions were:

THANK YOU!

This was a massive undertaking, and you all participated in unique and
wonderful ways to build a free and open source game engine for everyone to
use and enjoy. You are breathtaking! <3

---
## [Jacob-Jeffries/m12c](https://github.com/Jacob-Jeffries/m12c)@[ad6292fd91...](https://github.com/Jacob-Jeffries/m12c/commit/ad6292fd911a08ce4944c029c76c200ef28690bc)
#### Saturday 2023-03-11 16:41:00 by Jacob Jeffries

Fucked around and found out about inquier 9.x.x! Oh boy that was a pain in the ass - sticking to 8.2.4 for now!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4df6207389...](https://github.com/mrakgr/The-Spiral-Language/commit/4df62073898e417a7f069319b9819545f7f6e85f)
#### Saturday 2023-03-11 17:01:04 by Marko Grdinić

"8:10am. I am up. Let me chill a bit. I am starting to find my center.

I know how I am going to be explaining things.

9:40am. Done with the bath.

Anyway, I got two mail today. One is A Teamer wanting an interview, I told her later after I am done with my portfolio project.

The other is this.

///

Dear Marko,

Thanks for your interest in our Open Source Program!

Could you please provide more details about your OS project and its functionality? What tools are you interested in and how are you going to use them?

Thanks, I look forward to your response!

///

This is for the JetBrains Rider OS license.

///

I am interested in Rider. Despite what the language stats on the Github page say, Spiral is written 98% in F# so I want to use the IDE to program F# in it. I've been working on its for years in Visual Studio, but while I was watching some .NET tutorials on Youtube, I noticed Rider has a decompiler which caught my interest. I gave it a try and I like it, so I want to switch to it.

Currently, I am not really working on Spiral, but some open source portfolio projects and I will be making Youtube videos about them. See here: https://www.youtube.com/playlist?list=PL04PGV4cTuIX3bNEDDyi1L27Si0qpyAJ7

I do think Rider is the best compared to VS Code and VS, but as a hobbyist programmer looking to turn pro, I do not have the money to shell out for an IDE. Instead if you could give me an OS license for Rider, you could get some advertizing on Youtube in return.

As for the projects themselves:

* Spiral is a functional language that has features making it very efficient compared to ordinary functional languages (such as F# itself.) It is very similar to F# in syntax, and I've designed it so that when novel AI hardware comes out, I'll be able to program them in a functional style. I've verified its design on GPU programming, and now I am just waiting for companies like Tenstorrent to release their products. I'll be making backends for them in the future.

* The playlist I linked you is a mixed project that uses Fable + React on the JS side, F# on the .NET side, and in the future I'll bring in Python for ML, and possibly C# for databases. I am doing a little poker game, and I want to show how it can be designed so that it is easy to plug reinforcement learning algorithms into it. Since I am looking to become a full stack dev, I am making it a web application and will show how to manage the communication between the client and the server, as well as use the database, as well as how to do user logins and authorization.

///

Let me reply with this.

10am. Let me start making the next video. Though I am considering redoing the first one. At least just the screencast for it.

Let me do that. It is very boring to have a single static page.

10:20am. https://youtu.be/QJfCs9XEeJs
Intro To The Web Dev In F# Series

Here is the latest and greatest, now you can see me make the graphics. It is much better that I am doing something on the screen while I talk.

Now let me do that again.

I've had time to think what I want to do today during the night. What I want to do first is the prereqs video.

1:15pm. Let me take a break here. I have 6m done - yes took me all this time just to make that little bit.

One thing this video making is training is my focus. When writing and programming you can let your mind wander, but here, you need to be on the ball. I've had moments where I've found the recital to be much easier. I need to learn to tap into that feeling.

The fact that I often start feeling lethargic often when I recite really messed up my flow.

2:40pm. Done with breakfast. Let me chill a bit and then I will do the chores. After that I'll finish the Prereqs video.

After that comes the UI video. I had a lot of time to think of how to deal with it. Actually, it won't be the UI video. I'll skip tutorial1 and go straight to tutorial2.

2:45pm. Let me do the chores.

3:20pm. Done. Let me resume video making.

4:35pm. Finished and published it.

https://youtu.be/NARA4UXY5Q8
Prerequisites

Damn I do not feel like making another video right away. I'd much rather be doing programming.

4:45pm. Let me record a segment.

...But I really do not feel like it right now.

Yeah, forget it. I'll do it tomorrow. Right now, how about I do something else? I've been doing this all day already.

4:45pm. How I work on my resume for a bit?

5:15pm. https://resumake.io/

I've used this site to make a 0.5 page resume somehow. Having rails helped me keep on track.

Let me post in on LinkedIn so I can see if it makes any kind of difference.

5:30pm. I changed my resume on Indeed, LinkedIn and AngelList.

5:30pm. Now for some reason I lost my login on AngelList.

And when I try to sign in, it is creating a wholy new profile. What a timewaster!

5:40pm. I was trying to login from the wrong side.

Oh, Chrome found that one my passwords was compromised in a data breach. It is my Steam password. I didn't know it could do that.

5:45pm. Changed it. Ok, good. I've made a new resume, if this is not getting bites, I'll use ChatGPT later. For now I won't be applying anywhere.

Tomorrow, I am going to get the video on tutorial2 done. Then I will cover tutorial3.

I have an idea of what style I want to use for my presentations now. Excalidraw will be very helpful for this sort of purpose.

5:50pm. Oh, I finally figured out how to remove those deleted video from the playlist.

It turns out you first have to make them visible, and then remove them manually.

Now the thumbnail for the playlist itself is showing up properly.

Sheesh. Why is Youtube not doing this on its own?

5:55pm. Anyway, I'll close here.

It is time to slack once again. These videos really take a ton of effort, but I am oging to get my value's worth from the mic. It really is great, I just need to up my skills.

To be honest, my lack of focus when I am talking is really giving me concerns about how I am going to manage to get through the job interviews when I start applying later, but I'll take it one step at a time."

---
## [untamed-team/project-untamed](https://github.com/untamed-team/project-untamed)@[fed49efbe5...](https://github.com/untamed-team/project-untamed/commit/fed49efbe551b24303345aff88ee015e937ba859)
#### Saturday 2023-03-11 17:27:08 by ChespinCraft

porsite ow update

i hate this stupid fucking whale

---
## [MrSamu99/Shiptest](https://github.com/MrSamu99/Shiptest)@[7f8874df29...](https://github.com/MrSamu99/Shiptest/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Saturday 2023-03-11 17:32:15 by Zevotech

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
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[be9e96550f...](https://github.com/meemofcourse/Shiptest/commit/be9e96550f736f079942f6852862abf85b4c5d5e)
#### Saturday 2023-03-11 18:02:16 by meemofcourse

the Review is Stupid I Hate It When My Mistakes are Pointed Out

fixes piping, wiring, apcs, adds more decaling to things, adds boxes and mining gear to cargo, and whatever the fuck else i'm forgetting to put here

---
## [robertfwallis/The-Classic-Pack](https://github.com/robertfwallis/The-Classic-Pack)@[c283fcd626...](https://github.com/robertfwallis/The-Classic-Pack/commit/c283fcd62679788389658203a2acc22cf0974094)
#### Saturday 2023-03-11 18:05:08 by Robert Wallis

Remove Cog-tastrophe from SBFO OST

I've made the decision to remove Cog-tastrophe from the Sellbot Field Office OST for a few reasons.

1. Hearing Cog-tastrophe for up to 30 minutes straight can be incredibly irritating after a while. As much as it is one of my favourite Toontown Online songs, hearing it for a long period of time on loop will start to get annoying. It was acceptable in the VP and CFO as when done right those battles could literally last a mere 5 minutes, but you cannot rush The Boiler fight.

2. Whilst the VP, CFO and CJ shared Cog-tastrophe for their final rounds, the CEO did not. I feel as though future bosses under Disney's reign may not have featured Cog-tastrophe either, so it is fitting to remove it from The Boiler. To clear up confusion: Toontown Rewritten switched the final two CJ round musics as it was more fitting. In Toontown Online, Cog-tastrophe played during the final round, whereas it does not in Toontown Rewritten.

3. If you don't think Toontown Rewritten's music for The Boiler is fire, I don't know what to tell you. You're weird.

It also helps to save a little storage space. It's not a big loss.

---
## [FreeStylaLT/Citadel-Station-13-RP](https://github.com/FreeStylaLT/Citadel-Station-13-RP)@[b9313e344b...](https://github.com/FreeStylaLT/Citadel-Station-13-RP/commit/b9313e344b7b468f2e68d428e69c19503e3833b8)
#### Saturday 2023-03-11 18:18:03 by Keekenox

Fix Keek's Offset Sprites Finally (#5135)

Keekenox has fixed the pixel offsets for sprite assets, which is a
crucial improvement to the game. In the previous version, some sprites
appeared blurry and misaligned, making the game look unprofessional and
unpolished. With this commit, the sprites are correctly aligned,
improving the overall visual quality of the game. This is important
because it enhances the player experience and makes the game more
enjoyable.

Firstly, fixing the pixel offsets ensures that the sprites display
accurately across all devices and platforms. With the increasing
popularity of gaming on different devices, it is essential that the game
looks good and functions well across all of them. Inconsistent display
of assets can be frustrating for players and negatively impact their
experience. By addressing this issue, Keekenox has taken a step towards
creating a more accessible game, which can be played by a wider
audience.

Secondly, fixing the pixel offsets is important for the branding of the
game. The look and feel of the game are integral to creating a strong
brand image. The blurry and misaligned sprites make the game look less
polished and unprofessional. With the visual improvements from this
commit, the game now looks more visually appealing, and its brand image
is strengthened. This can lead to increased engagement, higher retention
rates, and better marketing opportunities.

Thirdly, by fixing the pixel offsets, Keekenox has made the game more
scalable. As the game grows and more assets are added, the risk of
misaligned and blurry sprites increases. By addressing this issue early
on, Keekenox has prevented potential headaches down the road, saving
time and resources in the long run. This demonstrates a commitment to
quality and attention to detail that players appreciate and respect.

Fourthly, fixing the pixel offsets is important for maintaining the
quality of the game. Players expect games to look and feel polished,
with attention given to even the smallest details. The misaligned and
blurry sprites detract from the overall quality of the game, leaving
players with a negative impression. By fixing this issue, Keekenox has
shown that they care about their players' experience and are committed
to delivering a high-quality game.

Lastly, fixing the pixel offsets has a direct impact on the player
experience. Games are meant to be enjoyable, and players want to immerse
themselves in a world that looks and feels great. Misaligned and blurry
sprites can be distracting and detract from the experience, making it
less enjoyable for the player. With the improvements made in this
commit, players can now enjoy the game without these distractions,
leading to increased satisfaction and potentially higher retention
rates.

In summary, fixing the pixel offsets for sprite assets is an important
improvement to the game. It ensures accurate display across all devices,
strengthens the brand image, improves scalability, maintains quality,
and enhances the player experience. Keekenox has demonstrated a
commitment to delivering a high-quality game, and players will
appreciate the attention to detail that went into this improvement.

---
## [Ekaterina-von-Russland/tgstation](https://github.com/Ekaterina-von-Russland/tgstation)@[2b76197397...](https://github.com/Ekaterina-von-Russland/tgstation/commit/2b76197397b4241957e93a9779fdd9dfbada2688)
#### Saturday 2023-03-11 18:29:26 by Jacquerel

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
## [DataSpieler12345/Python-Projects](https://github.com/DataSpieler12345/Python-Projects)@[805955a2af...](https://github.com/DataSpieler12345/Python-Projects/commit/805955a2afc708a9b985c3582405fb110e7aab68)
#### Saturday 2023-03-11 18:39:10 by BI - Data Analyst

My First Python Project! Yeah! :)

Amazing experience! ...there is still more to learn!

---
## [MuckerMayhem/Baystation12](https://github.com/MuckerMayhem/Baystation12)@[e6362376cb...](https://github.com/MuckerMayhem/Baystation12/commit/e6362376cb2bc6cf95004b921aa1f4bc5ff5ccb5)
#### Saturday 2023-03-11 18:50:16 by gy1ta23

rifles!!!1


fixes descs


lathemags


oops i forgot a mag


holy shit hitting / is not that hard


Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>
Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>
Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[83d3e312f8...](https://github.com/silicons/Citadel-Station-13-RP/commit/83d3e312f83d6cf3849ac3bf1baaf2c8f62ead0f)
#### Saturday 2023-03-11 18:51:33 by Zandario

fucky wucky (#5102)

I joked about having something silly to tell players we're fixing shit,
and while looking into bee's statpanel I noticed the image for this in
their HTML files so of course I had to add it.

Ported from: BeeStation/BeeStation-Hornet/pull/1574

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[6c978308c7...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/6c978308c71cbd5b24e3242aec42b227461f9aaa)
#### Saturday 2023-03-11 19:53:48 by SkyratBot

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[8500d62b79...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/8500d62b798a45812832be0c686f532f877f1e3a)
#### Saturday 2023-03-11 20:04:43 by SkyratBot

[MIRROR] Abductor scientist self-retrieve failure/runtime fix [MDB IGNORE] (#19179)

* Abductor scientist self-retrieve failure/runtime fix (#73172)

## About The Pull Request

Since the abductor outfit/implant would load before the abductor ship
(and it's teleport pad) when first generating a team, a runtime would
occur when trying to link the pad to the implant. Another would occur
every time you attempted to retrieve yourself (as the linked pad would
be null), preventing recall and completely neutering an abductor team's
most important maneuver.

Now, using the implant will perform the linking process again if no
linked pad is found, and provides the owner with a warning if (by some
great calamity) they genuinely have no pad to teleport back to. This
solves the issue of the implant sometimes not linking to a pad properly
on initialize, and makes them way less prone to breaking.

Apparently this has been broken for a while, presumably since the
abductor ship was made into a lazyloading template.
## Why It's Good For The Game

The funny silly grey men get to torture the poor hapless crew once
again.
## Changelog
:cl:
fix: abductor scientist's retrieval implants will now properly recall
the owner, and inform them upon recall failure.
/:cl:

* Abductor scientist self-retrieve failure/runtime fix

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [elee-p3/scsmush-evennia](https://github.com/elee-p3/scsmush-evennia)@[397108bca1...](https://github.com/elee-p3/scsmush-evennia/commit/397108bca1a3c3435dd333a95b1e624a43b774e6)
#### Saturday 2023-03-11 21:33:57 by dancerdevin

CmdLogmunch and CmdTeach implemented. logmuncher.py and log.txt versioned. My plan is to replace log.txt every time I want to munch a new log and iterate through all my old logs. Is that clunky? Fuck you!

---
## [8bit-coder/Charged-Up-2840](https://github.com/8bit-coder/Charged-Up-2840)@[dfe133bde2...](https://github.com/8bit-coder/Charged-Up-2840/commit/dfe133bde299ced59fd309acb519cd6dde361686)
#### Saturday 2023-03-11 21:37:35 by 8bit-coder

first refactor

theoretically this should all work, but i'm not entirely sure. we hnavent gotten any of the physical in bits in place for testing, but i'm assuming it should all work. let's pray for the bes.t

and since it feels like it, lets use this section as a personal diary entry.

right now, it's saturday. it's less than a week before competition, so we're very close to being done with robotics, forever. of course, i'll make sure to work on robotics in university. but asside from that, i feel weird. almost like a preemptive happiness for things to be over. i'm not sure what it is. i guess i'm also excited about my job; i really cant wait to start. i have this one math test on tuesday, but then i should be done with everything i have aside from that crappy english project. man, the timeline for that is gonna be ROUGH. i really dont want to work on it during tomorrow, but i guess i have to. anyways, gary just got back so i guess it's time to get back to work.. time will tell.....

---
## [robertxgray/crawl](https://github.com/robertxgray/crawl)@[c65c45c1d4...](https://github.com/robertxgray/crawl/commit/c65c45c1d4c4d4d01db8334bc56938436b0d3bc0)
#### Saturday 2023-03-11 21:54:50 by Nicholas Feinberg

Move the Vaults rune lock inside (hellmonk)

Long ago, Vaults got a 'rune lock' - the requirement that players find
at least one of the fabled Runes of Zot before entering. This was added
so that players would be encouraged to fight at least one of the final
challenges of the Lair branches (Snake, Spider etc) at a time when they
were still challenging. Before this lock was added, wise players fought
those challenges much later, after getting so much XP and loot from Vaults
etc that they were trivial.

This was a big improvement! But there was one downside - lunatic players
who wanted to get the silver or, god forbid, golden rune before getting
any other runes (or even entering the Lair, perhaps!) were blocked from
achieving their dreams. Tragic!

So, this commit lets them do that. You no longer need a rune to enter
the Vaults, but you do need a rune to leave. Wise play probably remains
unchanged,

There is a fairly strongly worded warning for players trying to enter
the Vaults without a rune, with a requirement to type 'yes' to enter
(ala stepping on a Zot trap, entering wizmode, etc). So I'm hoping this
doesn't affect the experience for newer players. If it does, I'll rethink
this!

---
## [nushell/nushell](https://github.com/nushell/nushell)@[2e01bf9cba...](https://github.com/nushell/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Saturday 2023-03-11 22:31:11 by Bob Hyman

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
## [gheskett/ultrasm64](https://github.com/gheskett/ultrasm64)@[eda46e5d64...](https://github.com/gheskett/ultrasm64/commit/eda46e5d6484dea72484a43305da3161b44f2d94)
#### Saturday 2023-03-11 22:42:51 by Gregory Heskett

Frustum Fix: Revert frustum ratio back to 2

Decomp team back in the stone ages set this to 1 for F3DEX2, assuming the default value (2) broke stuff.
This isn't actually the case, and it's a speed loss to use a value of 1, for a benefit that's completely intangible.

commit daa0c173b96c15d3483e784a9307267d6cf5aeac
Author: Fazana <52551480+FazanaJ@users.noreply.github.com>
Date:   Fri Mar 10 15:20:55 2023 +0000

    I think github are gonna give me badges for all these PR's (#597)

    * Update game_init.c

    * fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo

    * Update segment2.c

    * Update model.inc.c

commit 152df1daf3e23d5d9b51a68019cc3de0b8956bde
Author: Fazana <52551480+FazanaJ@users.noreply.github.com>
Date:   Fri Mar 10 15:04:01 2023 +0000

    Frustratio funny fix part 3 (#596)

    * Update game_init.c

    * fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo

    * Update segment2.c

commit e2e0bd4778ebc28cc1724ac5526de7b6c15108b5
Author: Fazana <52551480+FazanaJ@users.noreply.github.com>
Date:   Fri Mar 10 03:39:26 2023 +0000

    Frustratio funny fix 2 (#593)

    * Update game_init.c

    * fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo

commit 6d0d42f20205285a14eba65b8f64e235c7098784
Author: Gregory Heskett <gheskett@gmail.com>
Date:   Thu Mar 9 02:23:47 2023 -0500

    Revert frustum ratio back to 2

    Decomp team back in the stone ages set this to 1 for F3DEX2, assuming the default value (2) broke stuff. This isn't actually the case, and it's a speed loss to use a value of 1, for a benefit that's completely intangible.

---
## [ErickWDaniel/Check_For_WebSite_Dead_Link](https://github.com/ErickWDaniel/Check_For_WebSite_Dead_Link)@[21b082308c...](https://github.com/ErickWDaniel/Check_For_WebSite_Dead_Link/commit/21b082308c018ff64ca538d252283a7b91b66d1f)
#### Saturday 2023-03-11 23:01:59 by Erick W Daniel

Update README.md

## 😂 Here is a random joke that'll make you laugh!
![Jokes Card](https://readme-jokes.vercel.app/api)

---
## [Penghisbungholius/tgstation](https://github.com/Penghisbungholius/tgstation)@[97f567fdc7...](https://github.com/Penghisbungholius/tgstation/commit/97f567fdc745230b1594c305680dce683512d032)
#### Saturday 2023-03-11 23:39:58 by MMMiracles

Tramstation: Growing Pains (#72331)

## About The Pull Request


![image](https://user-images.githubusercontent.com/9276171/209841644-3e8be93c-7903-4eb4-85bf-cc582248a9fa.png)

## Why It's Good For The Game

Lots of QoL and structural changes in attempt to make the cool map even
cooler.

## Changelog
:cl: MMMiracles
add: Tramstation has received a substantial overhaul! Please consult
your local tour guide and station maps for changes.
/:cl:

**Changes (as of so far)**
- The Tramstation tunnels have been extended 6 tiles each way, making
that trek across the central rail a little more dangerous.
- No more mid-way safety net on the transit rails. You're either making
it or you're jumping to the bottom floor to avoid the tram.
- The central rail apparently had a negative slowdown, meaning you
actually WERE faster to just run the gauntlet because it literally made
you faster. This has been reverted because I want you to get hit by a
train.
- The side routes are now a bit more dangerous since you can get pushed
off into the lower floor
- Fauna overhaul! Several locations including the transit tunnels have
gotten some greenery to help liven up transit between sectors. Please do
not rip up the AstroTurf it is very expensive in space.
- Handicap-accessible departments! Every major wing and departments with
multiple floors has been given a 2x3 elevator segment for those among
the crew who have been hit by the tram a few too many times. Handicap
inaccessible staircases may or may not come after this (i hate the
handicapped)
- Expanded Security wing! You know that lame hallway between
interrogation and the courtroom access? Now its a whole holding wing fit
with essentials to keep your inmates content while waiting for their due
process (never ever).
- Reworked Bridge! Front row seats to the western tram dock as well as a
furnished meeting room with various corporate memorabilia!
- The HoP's office has been moved to function more as an arrival gate
for late joining crew! Scenic queue lines and an option to block off the
lower dorm access if you really want to enforce the 'Papers, Please'
roleplay you've always wanted out of your HoP experience.
- Combined the teleporter/gateway/eva access into one special external
operations room. All you off-station needs in one convenient place!
- More multi-z integration! Several segments (mainly maintenance level
transfers) have been given overhangs and better methods to move between
levels. This is still being expanded upon as of current PR posting.
- The power/pipe access shafts have been changed to be more
public-facing and now also act as another inbetween for
maintenance-dwelling crew to shift between floors.
- Multi-z solars! Both solar wings have been extensively overhauled to
include multi-z structuring and easily doubled the amount of roundstart
panels on the map.
- Escape pod bay! [Casually borrowing from a certain ship
map](https://tgstation13.org/phpBB/viewtopic.php?t=32834), there is now
a centralized location for all station escape pods on the floor below
Arrivals. Honestly makes more sense thematically instead of having a
bunch of scattered bays.
- MULEBOT integration! Each major department now has delivery drop-off
points along with Cargo getting a minor restructuring to fit 4 MULEBOTs.
Seedy side-tunnels and drop points have been added for departments that
aren't normally accessible from upper maintenance so they can still
properly deliver cargo if sent this way. I can't guarantee this won't
end in MULEBOTs getting ran over by a tram because they're fickle
beasts.
- Complete rework of the disposals/piping/wirenet! I literally ripped
everything up and rebuilt it with (hopefully) better stability in mind.
Disposals is now also set up in that it'll try to avoid going through
departments unnecessarily if your package isn't marked for it.
- Cargo's mail room and trash room has been overhauled to be more easily
accessed for cargo techs and for routing mail.
- The chef has access to the morgue's back door via the front
maintenance hatch while Robotics can now access the same back door via
their maintenance shaft.
- The chem lab's starting area has been expanded so chemists don't have
to worry as much about digging if they don't have large projects.

![2023 02 02-18 15
45](https://user-images.githubusercontent.com/9276171/216472805-77074a12-d653-41c4-b730-f26f93c27d3b.png)
![2023 02 02-18 15
38](https://user-images.githubusercontent.com/9276171/216472852-555e6ca9-e967-4915-9555-e29cfc99393d.png)

---
## [Penghisbungholius/tgstation](https://github.com/Penghisbungholius/tgstation)@[27c35bfa0b...](https://github.com/Penghisbungholius/tgstation/commit/27c35bfa0b11a7248314cc057b70c6a0729794bf)
#### Saturday 2023-03-11 23:39:58 by MrMelbert

Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line: 
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy. 

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

---

