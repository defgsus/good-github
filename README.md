## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-12-24](docs/good-messages/2021/2021-12-24.md)


1,366,013 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,366,013 were push events containing 1,857,505 commit messages that amount to 137,336,975 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 44 messages:


## [Mu-L/maui](https://github.com/Mu-L/maui)@[ac6befcbee...](https://github.com/Mu-L/maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Friday 2021-12-24 00:33:04 by Jonathan Peppers

[controls] Brush.Foo should return immutable instances (#3824)

When profiling a `dotnet new maui` app, with this package:

https://github.com/jonathanpeppers/Mono.Profiler.Android

The `alloc` report shows:

    Allocation summary
    Bytes      Count  Average Type name
    39984        147 2 72     Microsoft.Maui.Controls.SolidColorBrush

Stack trace:

    38352 bytes from:
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.VisualElement:.cctor ()
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.Brush:.cctor ()

Reviewing the `Brush` class, there are indeed 147 `SolidColorBrush`
created on startup that are stored in fields.

But what is weird about this, is that `SolidColorBrush` is mutable!

    public Color Color
    {
        get => (Color)GetValue(ColorProperty);
        set => SetValue(ColorProperty, value);
    }

So I could literally write code like:

    Brush.Blue.Color = Colors.Red;

Blue is red! (insert evil laughter?)

I think the appropriate fix here is that all of these `static
readonly` fields should just be properties that return a new
`ImmutableBrush`. We can cache the values in fields on demand. Then
someone can't do something evil like change `Blue` to `Red`?

I reviewed WPF source code to check what they do, and they took a
similar approach:

https://github.com/dotnet/wpf/blob/5e8187344b2b561ef08b9ca2735cd89cbdd3c11e/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/brushes.cs#L33-L1586

We should make this API change now before MAUI is stable, and we have
the side benefit to save 39984 bytes of memory on startup?

I added tests for these scenarios, and discovered 3 typos for `Brush`
colors that listed the wrong color.

---
## [Munkybooty/dash](https://github.com/Munkybooty/dash)@[b33fc8c839...](https://github.com/Munkybooty/dash/commit/b33fc8c839ab435ec198d95853282611266066c5)
#### Friday 2021-12-24 00:42:04 by Wladimir J. van der Laan

Merge #15277: contrib: Enable building in Guix containers

751549b52a9a4cd27389d807ae67f02bbb39cd7f contrib: guix: Additional clarifications re: substitutes (Carl Dong)
cd3e947f50db7cfe05c05b368c25742193729a62 contrib: guix: Various improvements. (Carl Dong)
8dff3e48a9e03299468ed3b342642f01f70da9db contrib: guix: Clarify SOURCE_DATE_EPOCH. (Carl Dong)
3e80ec3ea9691c7c89173de922a113e643fe976b contrib: Add deterministic Guix builds. (Carl Dong)

Pull request description:

  ~~**This post is kept updated as this project progresses. Use this [latest update link](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718) to see what's new.**~~

  Please read the `README.md`.

  -----

  ### Guix Introduction

  This PR enables building bitcoin in Guix containers. [Guix](https://www.gnu.org/software/guix/manual/en/html_node/Features.html) is a transactional package manager much like Nix, but unlike Nix, it has more of a focus on [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) and [reproducibility](https://www.gnu.org/software/guix/blog/tags/reproducible-builds/) which are attractive for security-sensitive projects like bitcoin.

  ### Guix Build Walkthrough

  Please read the `README.md`.

  [Old instructions no. 4](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718)

  [Old instructions no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-493827011)

  [Old instructions no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old instructions no. 1</summary>
  In this PR, we define a Guix [manifest](https://www.gnu.org/software/guix/manual/en/html_node/Invoking-guix-package.html#profile_002dmanifest) in `contrib/guix/manifest.scm`, which declares what packages we want in our environment.

  We can then invoke
  ```
  guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```
  To have Guix:
  1. Build an environment containing the packages we defined in our `contrib/guix/manifest.scm` manifest from the Guix bootstrap binaries (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) for more details).
  2. Start a container with that environment that has no network access, and no access to the host's filesystem except to the `pwd` that it was started in.
  3. Drop you into a shell in that container.

  > Note: if you don't want to wait hours for Guix to build the entire world from scratch, you can eliminate the `--no-substitutes` option to have Guix download from available binary sources. Note that this convenience doesn't necessarily compromise your security, as you can check that a package was built correctly after the fact using `guix build --check <packagename>`

  Therefore, we can perform a build of bitcoin much like in Gitian by invoking the following:

  ```
  make -C depends -j"$(nproc)" download && \
      cat contrib/guix/build.sh | guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```

  We don't include `make -C depends -j"$(nproc)" download` inside `contrib/guix/build.sh` because `contrib/guix/build.sh` is run inside the container, which has no network access (which is a good thing).
  </details>

  ### Rationale

  I believe that this represents a substantial improvement for the "supply chain security" of bitcoin because:

  1. We no longer have to rely on Ubuntu for our build environment for our releases ([oh the horror](https://github.com/bitcoin/bitcoin/blob/72bd4ab867e3be0d8410403d9641c08288d343e3/contrib/gitian-descriptors/gitian-linux.yml#L10)), because Guix builds everything about the container, we can perform this on almost any Linux distro/system.
  2. It is now much easier to determine what trusted binaries are in our supply chain, and even make a nice visualization! (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html)).
  3. There is active effort among Guix folks to minimize the number of trusted binaries even further. OriansJ's [stage0](https://github.com/oriansj/stage0), and janneke's [Mes](https://www.gnu.org/software/mes/) all aim to achieve [reduced binary boostrap](http://joyofsource.com/reduced-binary-seed-bootstrap.html) for Guix. In fact, I believe if OriansJ gets his way, we will end up some day with only a single trusted binary: hex0 (a ~500 byte self-hosting hex assembler).

  ### Steps to Completion

  - [x] Successfully build bitcoin inside the Guix environment
  - [x] Make `check-symbols` pass
  - [x] Do the above but without nasty hacks
  - [x] Solve some of the more innocuous hacks
  - [ ] Make it cross-compile (HELP WANTED HERE)
    - [x] Linux
      - [x] x86_64-linux-gnu
      - [x] i686-linux-gnu
      - [x] aarch64-linux-gnu
      - [x] arm-linux-gnueabihf
      - [x] riscv64-linux-gnu
    - [ ] OS X
      - [ ] x86_64-apple-darwin14
    - [ ] Windows
      - [ ] x86_64-w64-mingw32
  - [ ] Maybe make importer for depends syntax
  - [ ] Document build process for future releases
  - [ ] Extra: Pin the revision of Guix that we build with with Guix [inferiors](https://www.gnu.org/software/guix/manual/en/html_node/Inferiors.html)

  ### Help Wanted

  [Old content no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-483318210)

  [Old content no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old content no. 1</summary>
  As of now, the command described above to perform a build of bitcoin a lot like Gitian works, but fails at the `check-symbols` stage. This is because a few dynamic libraries are linked in that shouldn't be.

  Here's what `ldd src/bitcoind` looks like when built in a Guix container:
  ```
  	linux-vdso.so.1 (0x00007ffcc2d90000)
  	libdl.so.2 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libdl.so.2 (0x00007fb7eda09000)
  	librt.so.1 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/librt.so.1 (0x00007fb7ed9ff000)
  	libstdc++.so.6 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libstdc++.so.6 (0x00007fb7ed87c000)
  	libpthread.so.0 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libpthread.so.0 (0x00007fb7ed85b000)
  	libm.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libm.so.6 (0x00007fb7ed6da000)
  	libgcc_s.so.1 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libgcc_s.so.1 (0x00007fb7ed6bf000)
  	libc.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libc.so.6 (0x00007fb7ed506000)
  	/gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007fb7ee3a0000)
  ```

  And here's what it looks in one of our releases:
  ```
  	linux-vdso.so.1 (0x00007ffff52cd000)
  	libpthread.so.0 => /usr/lib/libpthread.so.0 (0x00007f87726b4000)
  	librt.so.1 => /usr/lib/librt.so.1 (0x00007f87726aa000)
  	libm.so.6 => /usr/lib/libm.so.6 (0x00007f8772525000)
  	libgcc_s.so.1 => /usr/lib/libgcc_s.so.1 (0x00007f877250b000)
  	libc.so.6 => /usr/lib/libc.so.6 (0x00007f8772347000)
  	/lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007f8773392000)
  ```

  ~~I suspect it is because my script does not apply the gitian-input patches [described in the release process](https://github.com/bitcoin/bitcoin/blob/master/doc/release-process.md#fetch-and-create-inputs-first-time-or-when-dependency-versions-change) but there is no description as to how these patches are applied.~~ It might also be something else entirely.

  Edit: It is something else. It appears that the gitian inputs are only used by [`gitian-win-signer.yml`](https://github.com/bitcoin/bitcoin/blob/d6e700e40f861ddd6743f4d13f0d6f6bc19093c2/contrib/gitian-descriptors/gitian-win-signer.yml#L14)
  </details>

  ### How to Help

  1. Install Guix on your distro either [from source](https://www.gnu.org/software/guix/manual/en/html_node/Requirements.html) or perform a [binary installation](https://www.gnu.org/software/guix/manual/en/html_node/Binary-Installation.html#Binary-Installation)
  2. Try out my branch and the command described above!

ACKs for top commit:
  MarcoFalke:
    Thanks for the replies. ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f
  laanwj:
    ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f

Tree-SHA512: 50e6ab58c6bda9a67125b6271daf7eff0ca57d0efa8941ed3cd951e5bf78b31552fc5e537b1e1bcf2d3cc918c63adf19d685aa117a0f851024dc67e697890a8d

---
## [tdauth/wowr](https://github.com/tdauth/wowr)@[c18494720f...](https://github.com/tdauth/wowr/commit/c18494720f3ccadb571c0f54d0accd08775daf94)
#### Friday 2021-12-24 01:04:37 by barade

1.9.0

- Add chat command "-aiattackson/off X".
- Do not ally leaving players with all players.
- Left players react to changing alliance settings towards them.
- Add missing tooltip to Orc Frigate.
- Fix victory condition of killing Archimonde being enabled when voting for it (was switched).
- Add special building Lich King to Undead.
- Add expiring timers for votes in the beginning.
- More space on the hidden island.
- Update map descriptions.
- Add hidden mountain base.
- Replace ulti of Admiral Proudmoore with Battleship.
- Replace Summon Water Elemental by Summon Sea Elemental for Admiral Proudmoore since Sea Elementals walk amphibiously.
- Translate tooltips of Summon Water Elemental back into English.
- Try to fix AI alliance reactions to allying or unallying.
- Add chat commands "-aigold/wood X".
- Increase Draenei shop build time.
- Fix allowing to research Thorium Armor for Draenei.
- Fix tooltip of Unique - Scepter of the Sea Giant.
- Add Magic Vault to Blood Elves.
- Add spell book to multiple tier 3 buildings including demigod temples.
- Add chat commands "-statsshow/hide" to show/hide player stats in a multiboard.
- Make Fountain of Life an Altar equivalent which is important for AI.
- One single Freelancers AI script enabled randomly for AI which gets Freelancer game mode.
- Give Freelancers AI Hideouts at Theramore in the beginning of the game.

---
## [godisgoodmatt/christmasspecial](https://github.com/godisgoodmatt/christmasspecial)@[39163b95db...](https://github.com/godisgoodmatt/christmasspecial/commit/39163b95db41d96cda158bef20d71522aa6b09d0)
#### Friday 2021-12-24 01:40:07 by wibi

holy shit
- buster: fixed scrap crystal having no sfx
- buster: fixed revelation, in order: erroring, casting forward, and giving blessings to the enemy instead of you
- bert: fixed passives with effects in before start turn, like hot table, applying twice if you're warrior
- bert: added more passive equipment for A Bonus
- bert: added rainmaking for Something Large
- bert: marked slushie, sing, tree shake, stygian blade, divine grip, and luck omen as excludefromrandomlists
- bert: rewrote A Spell to specify it just has to be a *valid* witch spell
- bert: retooled A Flower to be a mana generator instead of just any mana equipment
- bert: added more mana-generating equipment for A Flower
- diane: fixed thief's generator never being shuffled
- diane: some if(simulation) wrapping for thief items
- diane: excluded nicholas from thief's episode due to gift bag giving thief too many items
- diane: main menu credits now point out that they're incomplete and player must beat an episode to view full credits
- diane: changed credits music to angelmoon's ice stage remix
- diane: tidied up the credits a bit
- diane: excluded bounty hunter from jester becasue making cards unavailable for reasons other than chain doesn't work right
- diane: fixed offset of christmas ghosts

---
## [cheeserox/cheeserox](https://github.com/cheeserox/cheeserox)@[a8805f7133...](https://github.com/cheeserox/cheeserox/commit/a8805f71334dc7e5b571b2824b457727636a7f08)
#### Friday 2021-12-24 02:26:09 by Blue2k

attempt making 2012 player work and giving up afterwards because fuck you

---
## [KythiX/Backend](https://github.com/KythiX/Backend)@[7cc96e6cd3...](https://github.com/KythiX/Backend/commit/7cc96e6cd379fa6e1df283c15cd27668a97801d6)
#### Friday 2021-12-24 02:31:31 by Neko

Revert: fuck you nasa

This reverts commit eef00d8f1a28069b9e8b9f4ef1676048c8108672.

---
## [10088/rust](https://github.com/10088/rust)@[b269213b35...](https://github.com/10088/rust/commit/b269213b35f102a22b5a9645de48814fa255f7a2)
#### Friday 2021-12-24 03:14:26 by Matthias Krüger

Rollup merge of #91387 - graydon:E0038-clarification, r=wesleywiser

Clarify and tidy up explanation of E0038

I ran into E0038 (specifically the `Self:Sized` constraint on object-safety) the other day and it seemed to me that the explanations I found floating around the internet were a bit .. wrong. Like they didn't make sense. And then I went and checked the official explanation here and it didn't make sense either.

As far as I can tell (reading through the history of the RFCs), two totally different aspects of object-safety have got tangled up in much of the writing on the subject:
  - Object-safety related to "not even theoretically possible" issues. This includes things like "methods that take or return Self by value", which obviously will never work for an unsized type in a world with fixed-size stack frames (and it'd be an opaque type anyways, which, ugh). This sort of thing was originally decided method-by-method, with non-object-safe methods stripped from objects; but in [RFC 0255](https://rust-lang.github.io/rfcs/0255-object-safety.html) this sort of per-impossible-method reasoning was made into a per-trait safety property (with the escape hatch left in where users could mark methods `where Self:Sized` to have them stripped before the trait's object safety is considered).
  - Object-safety related to "totally possible but ergonomically a little awkward" issues. Specifically in a trait with `Trait:Sized`, there's no a priori reason why this constraint makes the trait impossible to make into an object -- imagine it had nothing but harmless `&self`-taking methods. No problem! Who cares if the Trait requires its implementing types to be sized? As far as I can tell reading the history here, in both RFC 0255 and then later in [RFC 0546](https://rust-lang.github.io/rfcs/0546-Self-not-sized-by-default.html) it seems that the motivation for making `Trait:Sized` be non-object-safe has _nothing to do_ with the impossibility of making objects out of such types, and everything to do with enabling "[a trait object SomeTrait to implement the trait SomeTrait](https://rust-lang.github.io/rfcs/0546-Self-not-sized-by-default.html#motivation)". That is, since `dyn Trait` is unsized, if `Trait:Sized` then you can never have the automatic (and reasonable) ergonomic implicit `impl Trait for dyn Trait`. And the authors of that RFC really wanted that automatic implicit implementation of `Trait` for `dyn Trait`. So they just defined `Trait:Sized` as non-object safe -- no `dyn Trait` can ever exist that the compiler can't synthesize such an impl for. Well enough!

However, I noticed in my reading-and-reconstruction that lots of documentation on the internet, including forum and Q&A site answers and (most worrying) the compiler explanation all kinda grasp at something like the first ("not theoretically possible") explanation, and fail to mention the second ("just an ergonomic constraint") explanation. So I figured I'd clean up the docs to clarify, maybe confuse the next person less (unless of course I'm misreading the history here and misunderstanding motives -- please let me know if so!)

While here I also did some cleanups:

  - Rewrote the preamble, trying to help the user get a little better oriented (I found the existing preamble a bit scattered).
  - Modernized notation (using `dyn Trait`)
  - Changed the section headings to all be written with the same logical sense: to all be written as "conditions that violate object safety" rather than a mix of that and the negated form "conditions that must not happen in order to ensure object safety".

I think there's a fair bit more to clean up in this doc -- the later sections get a bit rambly and I suspect there should be a completely separated-out section covering the `where Self:Sized` escape hatch for instructing the compiler to "do the old thing" and strip methods off traits when turning them into objects (it's a bit buried as a digression in the individual sub-error sections). But I did what I had time for now.

---
## [AryanTommer/business](https://github.com/AryanTommer/business)@[3ca10b9692...](https://github.com/AryanTommer/business/commit/3ca10b9692b9dae988fbe3c528b96814e3cb5cf3)
#### Friday 2021-12-24 03:29:10 by David Beguin

[IMP] im_livechat : optimize reports queries

Before, the duration and time to answer where computed based on the
mail channel creation date and
- the first message date from operator (for time to answer)
- the last message date (for duration)
But as the mail channel can be created long ago before the first message,
the result was not really representative.

Now, we are basing the computation only based on the messages.
Time to answer : first message date from operator - first message date
Duration : last message date - first message date

It allows, with the add of the second join on mail_message,
to simplify the extraction of those two indicator by removing the long
subselects.

Also, we fix the nbr_message in operator by adding the missing distinct.

Special mention to @jem-odoo who clearly did (almost) all the work :
This guy is amazing ! After a long and mature reflexion,
he finally put all his mighty power to enhance thoses reports
to give the users a wonderfull experience full of flowers and
peacefull sun, but also fast as a energized rabbit superhero !
Hail to him ! The One, the Only, the Chosen..
If you see him around the corner, please give him all your love
and gratitude ! Voilà voilà..

Task ID : 1895998
Closes PR #28283

---
## [AryanTommer/business](https://github.com/AryanTommer/business)@[855c6dac25...](https://github.com/AryanTommer/business/commit/855c6dac25fccaf9312543022001ed0b360d6e13)
#### Friday 2021-12-24 03:31:40 by RomainLibert

[IMP] lunch: automatize lunch orders

We would like to automatize lunch as currently all orders are manually ordered and validated,
and a cash move has to be manually created each time you want to credit the wallet of some user.

1/ In this commit we add a new widget that comes with the kanban view
   and will allow to take orders in a friendly manner.
2/ We also add a lunch.supplier model this also allows you to configure an
   automatic ordering via email.
3/ Introduces new lunch.location model to replace res.partner on suppliers
4/ New mail template for automatic ordering
5/ Add the concept of new products (mark a product as new until some date)
6/ The toppings are now defined by product category
7/ Lunch.order removed, lunch.order.line renamed into lunch.order
8/ New SQL report to get the wallet content (aggregate of lunch.cashmove and lunch.order)
9/ New setting to allow negative wallet (aka overdraft)
10/ Application now remembers what notes and toppings you last ordered with your product
11/ You can change your location using the widget on the kanban view
12/ Edition of the order can be done until the order is arrived

TaskID: 1856876
TaskID: 1916105

closes odoo/odoo#30028

---
## [AryanTommer/business](https://github.com/AryanTommer/business)@[42fbee83ad...](https://github.com/AryanTommer/business/commit/42fbee83ad2f3f33188cf27a1449b8875c2d8a2a)
#### Friday 2021-12-24 03:32:20 by Xavier Morel

[IMP] qweb: stop requiring t-name-flagged sub-node

QWeb's rendering currently *requires* that when loading a document
instead of rendering the document itself it will render a sub-node
with a properly labeled t-name. If a view is invoked by id, ir.qweb
will look for a child with a t-name and fix up that t-name such that
the base qweb object will find and render it.

This feature mostly exists for JS compatibility (because a single
document can contain multiple cross-linkable templates, and it was
useful for cross-implementation tests though I'm not sue they're even
checked anymore), and the <template> tag kinda took care of it,
however with a more proper qweb view it becomes more of a liability /
pain in the ass.

Note: turns out there are bits of javascript which read server
templates (???) and need to be altered to correctly handle the lack of
<templates> wrapping.

---
## [AryanTommer/business](https://github.com/AryanTommer/business)@[bfcf237fbe...](https://github.com/AryanTommer/business/commit/bfcf237fbe2bf05c3e9b9688e319913d33a92a36)
#### Friday 2021-12-24 04:19:25 by Thibault Delavallée

[REM] partner_autocomplete_address_extended: remove broken module

Commits a6e1eb9f0ad285fac7d0ca0b9f89f046d78ec9c7 and 8a1815b31eacc148d6e98795899ee24a9ca8cab1 added among a lot of other things
a bridge module between ``partner_autocomplete`` and ``base_address_extended``.
It is used only to redefine the ``_split_street_with_params`` method from
``base_address_extended``. This method is used to find street name, number and
number2 from an address, given a format coming from the country.

However the override completely fucks up the original method purpose and uses
an hardcoded regex coming out of the blue. Parameters like country format is
not taken into account which is annoying when trying to parse country dependent
data.

Tests from ``base_address_extended`` crash completely when used with the
``partner_autocomplete_address_extended`` implementation.

Considering the original complete specifications from commits
"""
For Name field or M2O, gives a list of companies
Data comes from Odoo IAP Service
"""

Or specs found in the original task ID 1867818 pad
"""
If Extended Address module is installed, the street number should be correctly
splitted Or the complete address is put in street2 if impossible to parse
"""

we think that this implementation is broken by design. Indeed there is no
mention of street2 anywhere in the code, and this implementation ensure street
will never be correctly split. We therefore remove it completely.

Task ID 2158302
PR odoo/odoo#42678

---
## [AryanTommer/business](https://github.com/AryanTommer/business)@[c608ae527a...](https://github.com/AryanTommer/business/commit/c608ae527a834615ba4b2d81c7b29a9409da2baf)
#### Friday 2021-12-24 04:30:33 by Odoo's Mergebot

[MERGE] calendar, google_calendar: Refactoring

1/ Recurring Events
==============
TL;DR A bit of magic and ... Pouf ... all virtual events are now real records.

## Purpose
The current implementation of recurring events uses "virtual events" to represents all
events in the recurrence. Only one event is stored in the database. All other events are
dynamically built and sent to the web client which sees them as real records.
This implementation is old, difficult to read (6 years of changes and bug fixes) and
has become more and more difficult to maintain.
A fresh start would be welcome.

## Specification
When creating a recurring event, a `calendar.recurrence.rule` record should be created.
This model holds the rrule configuration and is responsible to manage events that result
from the rrule.
When a new recurrence is created, all resulting events are also created (stored in the
database). No more virtual events.
To avoid an explosion of events, a maximum of 720 events is created. With 720 events,
a daily recurrence lasts for 2 years and a weekly recurrence lasts for 15 years.
This strategy is used by Google Calendar and seems acceptable in most cases.
A cron job could eventually be introduced to generated more events as the end comes.

This allows to introduce an new rrule end type: 'Forever'. This is actually a shortcut
to create a recurrence running for 720 events.

Inspired by Google Calendar, new possibilities are introduced when modifying a recurring
event (e.g. change the name, add an attendee):
- Modify only this particular event (the event is still part of the recurrence)
- Modify this and following events (events are still in the same recurrence)
- Modify all events

In a similar way, when updating the rrule of an event (e.g. from every Monday to every
Tuesday), the user can choose to:
- Modify this and following events: the recurrence is split. The first part remains
  unchanged but now ends when the second recurrence begins. The second parts is the
  updated rrule.
- Modify only this particular event.
- Modify all events: Forbidden (same as Google Calendar)

Note: when events are "moved" because the rrule changed, the events are not actually
moved. They are unlinked and new events are created (See "Some design choices explained"
section).

## Some design choices explained

### Where to store the rrule?

Two options were considered.
1) Store the rrule on an event, each event of the recurrence having a Many2one
to the parent_id, aka the Master Event of the recurrence.

2) Store the rrule on another model: `calendar.recurrence.rule`. Each event in the
recurrence having a Many2one to the recurrence record.

Both options have pros & cons. But there is no clear winner.
However the actual business logic of handling the recurrence creation/update
would be the same.
Where the rrule configuration is stored is the only main difference between both options.
And this is probably the easiest part of implementing recurring events.

With that in mind, option 2) is chosen. It allows to clearly separate recurrence
logic from the events themselves. It is also the "correct" way of modeling data to avoid
many empty columns for most records.

### Reusing events on rrule update
When an rrule is modified, events should also be updated.
In most cases, current events are unlinked and new events are created from scratch.
Only events exactly at the same time before and after the rrule update are kept.
Trying to reuse other events would require an obscure and arbitrary heuristic.
(Imagine an rrule every Monday that is changed to every Tuesday and every Friday.
What would you do?).
This implies that any change to a specific event (name change, attendee added, chatter
messages) is lost. This tradeoff seems acceptable as updating an rrule should not be
that frequent. Moreover, Google Calendar also works that way so why not Odoo?

### Reusing events on events shifts

On the calendar view, drag and drop an event to shift the entire recurrence.

One way to handle the recurrence shift is to apply the same timedelta to all events.
Now events are correctly positioned... except for events that were specifically
moved. Those outliers needs special handling.
This also introduces some behavior inconsistencies:
when an rrule is directly modified, events are not reused, but when the rrule is
modified by drag & dropping an event, events are reused. This option needs more code to
handle the shift and the behaviors are not consistent.

The chosen option is to find the rrule configuration from the dragged event (this is
easy) and update the recurrence with those new rrule values. This brings us back to
an rrule update (see above): code reusability yeah; one behavior to rule them all yeah.
One downside is that outliers are lost (but Google Calendar also works that way).

2/ Synchronization with Google Calendar
==============
This commit refactors calendar synchronization between Odoo and Google after the
main calendar application refactoring.

This refactoring takes advantage of two new features from the Google API:

- New way of synchronizing resources efficiently[1]
Incremental sync is performed repeatedly and updates Odoo with all the changes that
happened ever since the previous sync. Each time, Odoo provides the previous sync
token it obtained from Google and stores the new sync token from the response.

- Event metadata[2]
Ability to set hidden key-value pairs with an event, called extended properties.
These extended properties are used to store the related odoo event id and the Odoo
owner id (see known limitations)

### Known limitations
- Let A and B be two new users (no tokens available). A creates an event in Odoo and
invites B. A is the owner of the event (user_id). Now B authenticates to his Google Calendar
account and synchronizes his calendar. We cannot send the event to A's calendar since we
don't have any access to his Google Calendar. Hence the event his sent to B's calendar.
This leads to data de-synchronisation: The owner is A in Odoo but B in Google.
The "real" owner (user A) is stored in the Google event's metadata to be able to
reconcile the owner for following synchronizations.

- Let A and B be two users of Odoo and Google Calendar. And let the Google Calendar of B
be private (e.g. if A creates an event in Google Calendar and invites B, B won't see the
event in his calendar). If A creates an event in Odoo and invites B. The event is synced
to Google Calendar of A. Now B can see the event in Odoo but he can't see it in his
Google Calendar.

Task 2126717
PR #42031
PR Enterprise https://github.com/odoo/enterprise/pull/8006

[1] https://developers.google.com/calendar/v3/sync
[2] https://developers.google.com/calendar/extended-properties

--
I confirm I have signed the CLA and read the PR guidelines at www.odoo.com/submit-pr

Signed-off-by: Yannick Tivisse (yti) <yti@odoo.com>

---
## [AryanTommer/business](https://github.com/AryanTommer/business)@[574dd61351...](https://github.com/AryanTommer/business/commit/574dd61351f71dcc074b45523ca55ee1e59f8f75)
#### Friday 2021-12-24 04:37:46 by Thibault Delavallée

[HACK] crm: allow ordering on my activities deadline

RATIONALE

Activities are a way to organize our daily pipe. Notably in a sales pipeline
salesmen may have multiple leads with activities to perform in the next few
days. We would like to be able to have a list view displaying a list of leads
with "my" deadline, and to order leads based on this field.

PURPOSE

As activities are linked to records through a one2many and as my activities
are only a subset of those activities, it is impossible to store a field
on lead model. Indeed it would depend on the current user which makes storing
it impossible.

However ordering on a column in list view asks for a stored field. As it is
not possible, this commit proposes to hijack the web client and search of lead
model in order to allow it.

SPECIFICATIONS

Introduce a activity_date_deadline_my field, computed and searchable that
behaves like activity_date_deadline. It is filtered on current user activities
instead of being global to the record activities. "My" deadline is the earliest
deadline of my activities, even in the past.

Ordering through web client calls search_read with an order parameter set.
Search_read then calls search. In this commit we therefore override search
to intercept a search without count with an order on activity_date_deadline_my.
In that case we do the search in two steps.

First step: fill with deadline-based results

  * Perform a read_group on my activities to get a mapping lead_id / deadline
    Remember date_deadline is required, we always have a value for it. Only
    the earliest deadline per lead is kept.
  * Search leads linked to those activities that also match the asked domain
    and order from the original search request.
  * Results of that search will be at the top of returned results. Use limit
    None because we have to search all leads linked to activities as ordering
    on deadline is done in post processing.
  * Reorder them according to deadline asc or desc depending on original
    search ordering. Finally take only a subset of those leads to fill with
    results matching asked offset / limit.

Second step: fill with other results. If first step does not gives results
enough to match offset and limit parameters we fill with a search on other
leads. We keep the asked domain and ordering while filtering out already
scanned leads to keep a coherent results.

All other search and search_read are left untouched by this commit to avoid
side effects. Search_count is not affected by this commit.

As web client order availability is simply based on field being stored we
have to allow hijacking its value. A new option 'allow_order' is added that
display the order icon in list view column headers. It allows calling
search_read with an order based on the column but nothing more. Using it
on a not-stored field will give a warning log and ORM ignores it by default.

LIMITATIONS

At least following limitations apply

  * search on "my activities" gives a list of ids that is used for searching
    and ordering. It means that having too much activities on a given user can
    result in poor performances.
    -> we consider that activities assigned to a given user should be kept
    under control. Leads with activities for a given user should be a small
    subset of leads without activities.
  * ordering on activity_date_deadline_my always put those records on the top
    (deadline asc or desc) whatever the actual ordering of order items given
    to search. This is done to avoid complex implementation where deadline
    would be used to order records within groups ordered by another field.
    -> for example: order = 'priority DESC, activity_date_deadline_my ASC'
    actually behaves like 'activity_date_deadline_my ASC, priority DESC'.

WARNING

This implementation is a hack. It has been done by professionals. Do not try
to do it at home.

More seriously this is hackish and should be avoided. IN our case we consider
that the use of activities in sales pipeline is mainly driven by "my activities
deadline", which is not necessarily the case with longer processes like tasks.

Moreover user tests tend to show that this feature could be interesting. It
will improve quality of Odoo CRM and its adoption by improving its daily
use. A framework solution has to be found. Until this is done we keep this
hack and hope it is not duplicated in other applications.

LINKS

Task ID 2276011
Prepares Task ID 2243124 (My activities in CRM)
PR #52232

Signed-off-by: Thibault Delavallee (tde) <tde@openerp.com>

---
## [AryanTommer/business](https://github.com/AryanTommer/business)@[46c3a9670d...](https://github.com/AryanTommer/business/commit/46c3a9670d98a0110c7a4d867cfcb760142b372e)
#### Friday 2021-12-24 04:51:29 by qsm-odoo

[IMP] web_editor, website, *: move text tools in snippets panel

*: website_event, test_website

This commit is a series of hacks. The goal is to move the summernote
text tools to the editor panel for the website editor. All the code
to use the text tools in a top bar is kept (mass mailing, etc) and the
text tools are placed at the right place for website in an ugly way.

This is obviously temporary, until we can implement those text tools
more generically and in a better way thanks to the new editor.

Part of https://github.com/odoo/odoo/pull/57975
task-2344227

closes odoo/odoo#58199

X-original-commit: ff81fa4798e232a03daf0eeff7d85ad35a52b25c
Related: odoo/design-themes#365
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [AryanTommer/business](https://github.com/AryanTommer/business)@[1c8a958098...](https://github.com/AryanTommer/business/commit/1c8a95809852baefa851985507a07ac7f6465dc7)
#### Friday 2021-12-24 04:58:20 by Adrian Torres

[IMP] core: introduce `api.ondelete` decorator

With this commit, a new ORM api decorator is introduced:
`api.ondelete(*, at_uninstall)`.

This decorator is to be applied to Model methods that check for specific
business conditions when attempting to unlink a record via the
interface.

E.g. trying to unlink a validated journal entry

This decorator allows this logic to exist outside the `BaseModel.unlink`
method and is automatically bypassed when in uninstall mode, this means
that during an uninstall any and all data related to a module can and
will be removed easily and cleanly while still being able to apply
business logic to manual deletion of records.

This feature opens the gates to solving a very big problem with
uninstalls: records and tables that remain in a database despite the
relevant module being uninstalled, because if an override to unlink
raises an error, the data will never be deleted from the database.

Henceforth, overrides of unlink shall solely be used for data-cleaning
purposes, i.e. deletion or modification of data that is related to the
one currently being deleted but cannot be automatically deleted because
there are no proper SQL relations.

In certain very specific, low-level scenarios an unlink may be
overridden to raise an error, but this should only be done if you know
what the fuck you're doing, most of the time you'll want to resort to
`@api.ondelete`.

Note that this new decorator includes a keyword-only, required argument
called `at_uninstall`, in most business cases this argument shall be
False as this argument dictates whether or not this method should be
executed in the `unlink` call during uninstall. It should only be set to
True if you are certain of all the implications which most likely means
that the records of the model in which this ondelete function is defined
will NOT be removed during uninstall, they will forever linger in the DB
until manual intervention, this in turn can mean a wide range of
undefined problems due to crap left on the database.

Following commits will replace any `unlink` overrides that raise
business errors by methods decorated with `api.ondelete`, another commit
will introduce a pylint checker that will raise a warning any time that
an unlink override raises an error.

---
## [AryanTommer/business](https://github.com/AryanTommer/business)@[c9c7198b53...](https://github.com/AryanTommer/business/commit/c9c7198b537b3b6426c791b5f9581e4fdcc88ea8)
#### Friday 2021-12-24 05:05:01 by Xavier Morel

[IMP] tours: make chrome request a websocket port from the OS

This should be a smarter and properly reliable version of #42071: in
that, the runner requests a port, closes it, and gives the port to
Chrome. However this apparently turns out to be less reliable than
hoped for and the port we just released can immediately be picked up
by somebody else (the original PR assumed the allocation of ephemeral
ports would be random or FIFO but that may not be the case, especially
inside containers).

This uses the same technique of requesting port 0 so the OS allocates
one, but it's Chrome requesting & immediately connecting so there
should be no race condition possible, and we keep the property that as
long as ephemeral ports are available Chrome will be able to open one
without conflicts or overlaps.

This leaves the issue of *retrieving* the port chrome got. Thankfully
it turns out we use a custom user-data-dir in which case Chrome writes
the port it got to `$DATA_DIR/DevToolsActivePort`[0]. Despite the
file's name it *also* contains the path for the devtools endpoint so
we need to only read the first line (rather than be able to read and
intify the entire thing).

Wait up to 10s before giving up entirely, and wait 100ms between each
check for the file's existence: on my machine without significant load
the file appears after 80 to 150ms, waiting up to 90ms seems ok (it's
not like we're in a super hurry as tours tend to be pretty long).

Other paths explored before moc used his eyes and brain and found out
about DevToolsActivePort:

* Chrome prints ws URL on the stderr, however because we don't know
  how much garbage Chrome might send there we need to send it to a
  continuous sink otherwise Chrome *might* end up blocking on its
  stderr because we're not reading from it. This turns out to be a bit
  of a mess of processes or additional threads.
* xdo suggested we check what ports Chrome listens on using something
  like netstat/ss (turns out `psutil` has support for that OOTB),
  which worked great except on WSL (where it didn't work at all), and
  the future-proofness was a bit questionable as Chrome might add
  other servers in the future.
* fme suggested using socket activation support[1] and passing in the
  port we'd opened without closing it, which would really have been
  ideal, however it turns out it was removed a few months later when
  chrome added pipes support[2], which was a pain to realize as chrome
  doesn't exactly do any useful error reporting (so unknown options
  just disappear into a void to be never seen or heard of ever).
* And while the pipes system[3] has *serious* positive attributes
  (even lower initialization overhead, we could remove the websocket
  dependency, also avoids wasting sockets though that's not too much
  of an issue here) it would require rewriting a lot more than just
  the initialization as it uses its own logical protocol
  (NUL-terminated JSON). TBF most of the messaging stuff is properly
  contained into just a few `_websocket` methods but still...

[0] https://bugs.chromium.org/p/chromium/issues/detail?id=624837#c4
[1] https://bugs.chromium.org/p/chromium/issues/detail?id=624837
[2] https://chromium-review.googlesource.com/c/chromium/src/+/954405/3#message-ab7415a7db7b94787300d987216e9ce60db47bc2
[3] https://chromium-review.googlesource.com/c/chromium/src/+/954405/3

opw-2378464

closes odoo/odoo#65195

X-original-commit: b679d97a83f1ac898ee0916e92a5b440702bdcdf
Signed-off-by: Xavier Morel (xmo) <xmo@odoo.com>
Co-authored-by: Xavier Dollé <xdo@odoo.com>
Co-authored-by: Christophe Monniez <moc@odoo.com>

---
## [AryanTommer/business](https://github.com/AryanTommer/business)@[01875541b1...](https://github.com/AryanTommer/business/commit/01875541b1a8131cb0c5459f18670e9a97713135)
#### Friday 2021-12-24 05:17:24 by Xavier Morel

[CHG] core, web: deprecate t-raw

Add a big fat warning when the qweb compiler finds a `t-raw`.

`t-esc` should now be used everywhere, the use-case for `t-raw` should
be handled by converting the corresponding values to `Markup`
objects. Even though it's convenient, this constructor *should never
be made available in the qweb rendering context* (maybe that should be
checked for explicitely?).

Replace `werkzeug.escape` by `markupsafe.escape` in
`odoo.tools.html_escape`, this means the output of `html_escape` is
markup-safe.

Updated qweb to work correctly with escaping and `Markup`, amongst
other things QWeb bodies should be markup-safe internally (so that a
`t-set` value can be fed into a `t-esc`). See at the bottom for the
attributes handling as it's a bit complicated.

`to_text` needed updating: `markupsafe.Markup` is a subclass of `str`,
but `str` is not a passthrough for strings. So `Markup` instances
going through would be converted to normal `str`, losing their safety
flag. Since qweb internally uses `to_text` on pretty much
everything (in order to handle None / False), this would then cause
almost every `Markup` to get mistakenly double-escaped.

Also mark a bunch of APIs as markup-safe by default

* html_sanitize output.
* HTML fields content, sanitization is applied on intake (so stripped
  by the trip through the database) and if the field is unsanitised
  the injection is very much intentional, probably. Note: this
  includes automatically decoding bytes as a number of default values
  & computes yield bytes, which Markup will happily accept... by
  repr-ing them which is useless. This is hard to notice without `-b`.
* Script-safe json, it's rather the point (though it uses a
  non-standard escaping scheme).
* Note that `nl2br`, kinda: it should work correctly whether or not
  the input is markup-safe, this means we should not need to escape
  values fed to `nl2br`, but it doesn't hurt either.

Update some qweb field serialisations to mark their output as
markup-safe when necessary (e.g. monetary, barcode,
contact). Otherwise either using proper escaping internally or doing
nothing should do the trick.

Also update qweb to return markup-safe bytes: we want qweb to return
markup-safe contents as a common use-case is to render something with
one template, and inject its content in an other one (with Python code
inbetween, as `t-call` works a bit differently and does not go through
the external rendering interface).

However qweb returns `bytes` while `Markup` extends `str`. After a
quick experiment with changing qweb rendering to return `str` (rather
unmitigated failure I fear), it looks like the safest tack is to add a
somewhat similar bytes-based type, which decodes to a `Markup` but
keeps to bytes semantics.

For debugging and convenience reasons, MarkupSafeBytes does *not*
stringify and raises an error instead (`__repr__` works fine). This is
to avoid implicit stringifications which do the wrong thing (namely
create a string `"b'foo'"`).

Also add some configuration around BytesWarning (which still has to be
enabled at the interpreter level via `-b`, there's no way to enable it
programmatically smh), and monkeypatch `showwarning` to show warning
tracebacks, as it's common for warnings to be triggered in the bowels
of the application, and hard to relate to business logic without the
complete traceback.

`t-out`
=======

`t-esc` is a bit confusing for the new behaviour of "maybe escape
maybe not", so add a `t-out` alias with the same behaviour.

Unlike `t-raw`, `t-esc` is only soft-deprecated for now: there are
thousands of instances, so editing all the templates is not
great. Eventually we'll add a `ci/style` to prevent addition of new
ones, and eventually we might do a bulk-replace and hard-deprecate.

Attributes handling
===================

There are a few issues with respect to attributes. The first issue is
that markup-safe content is not necessarily attributes-safe
e.g. markup-safe content can contain unescaped `<` or double-quotes
while attributes can not. So we must forcefully escape the input, even
if it's supposedly markup-safe already.

This causes a problem for script-safe JSON: it's markup-safe but
really does its own thing. So instead of escaping it up-front and
wrapping it in Markup, make script-safe JSON its own type which
applies JSON-escaping *during the `__html__` call.

This way if a script-safe JSON object goes through `markupsafe.escape`
we'll apply script-safe escaping, otherwise it'll be treated as a
regular strings and eventually escaped the normal way.

A second issue was the processing of format-valued
attributes (`t-attf`): literal segments should always be markup-safe,
while non-literal may or may not be. This turns out to be an issue if
the non-literal segment *is* markup-safe: in that case when the
literal and non-literal segments get concatenated the literal segments
will get escaped, then attributes serialization will escape
them *again* leading to doubly-escaped content in attributes.

The most visible instance of this was the `snippet_options` template,
specifically:

    <t t-set="so_content_addition_selector" t-translation="off">blockquote, ...</t>
    <div id="so_content_addition"
        t-att-data-selector="so_content_addition_selector"
        t-attf-data-drop-near="p, h1, h2, h3, .row > div > img, #{so_content_addition_selector}"
        data-drop-in=".content, nav"/>

Here `so_content_addition_selector` is a qweb body therefore
markup-safe, When concatenated with the literal part of
`t-atff-data-drop-near` it would cause the HTML-escaping of that
yielding a new Markup object. Normal attributes processing would then
strip the markup flag (using `str()`) and escape it again, leading to
doubly-escaped literals.

The original hack around was to unescape() `Markup` content before
stringifying it and escaping it again, in the attribute serialization
method (`_append_attributes`).

That's pretty disgusting, after some more consideration & testing it
looks like a much better and safer fix is to ensure the
expression (non-literal) segments of format strings always result in
`str`, never `Markup`, which is easy enough: just all `str()` on the
output of strexpr. We could also have concatenated all the bits using
`''.join` instead of repeated concatenation (`+`).

Also add a check on the type of the format string for safety, I think
it should always be a proper str and the bytes thing is only when
running in py2 (where lxml uses bytestrings as a space optimization
for ascii-only values) but it should not hurt too much to perform a
single typecheck assertion on the value... instead of performing one
per literal segment.

Note: we may need to implement unescape anyway, because it's still
possible to get double-escaping with the current scheme: given an
explicitly escape-ed `foo` and `t-att-foo="foo"`, `foo` will be
re-escaped.

fixup! [CHG] core, web: deprecate t-raw

---
## [fulpstation/fulpstation](https://github.com/fulpstation/fulpstation)@[c797bf79ea...](https://github.com/fulpstation/fulpstation/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Friday 2021-12-24 05:57:09 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [linnpap/Skyrat-tg](https://github.com/linnpap/Skyrat-tg)@[729c443922...](https://github.com/linnpap/Skyrat-tg/commit/729c443922de29ff69c6f43ec602c070a07e8e41)
#### Friday 2021-12-24 06:18:55 by SkyratBot

[MIRROR] Fixes random hell Move() call counts, removes the parent call from mob/Login [MDB IGNORE] (#9995)

* Fixes random hell call-counts to Move (#63317)

Removes the parent call from mob/Login

Mothblocks pinged me with a profile of just a hellish amount of move calls
Way too many, like 200000
Started looking into it, got distracted by how expensive macros were
Turns out most of the cost of macros was in the nuke ops summon spawner

So I looked at why, only bit of it that was at all expensive was the login for the cyborgs
Tested on a local, huh that is slow yeah

Looked at the profiler, huh there's that move count again
So anyway, why is login so expensive

Spawned a few cyborgs in, dragged myself into them, nothing
Spawned myself in with sdql magic using the summon spawner, man it really is still there
I guess it has to do with move somehow, try and stick a breakpoint on it, get fucked by the debugger
I notice the hanging comes during the Login parent call

Try again, this time with good breakpoints.
We're trying to move, to (1,1,1), just like the reference says we will https://secure.byond.com/docs/ref/#/mob/proc/Login

But man, it just keeps happening, and we don't actually move
Step through the code, we've got that null loc check in atom/movable/Move

So the move to (1,1,1) isn't working

Here's the exact line from the reference
"If the mob has no location, place it near (1,1,1) if possible"
Keyword is near

Talked to lummox about this behavior, figured it was a bug

It turns out by near, they mean inside that tile's area
It'll keep trying to place you somewhere, in an attempt to effectively cover for shitty login systems, until you succeed in moving

That tile is space. There are 200,000 tiles with the same area as it
OH.

So anyway, we're not calling parent on mob/login anymore. We can do all the work it did that we care about ourselves (IE: Just the statobj set)
And this way we don't need to worry about 4 SECONDS OF OVERTIME WHENEVER SOME POOR FUCK MESSES UP SPAWN ORDER

So yeah, I'm a genius and not at all just malding at the existance of keybind macros, and hopefully another source of stutter bites the dust
Not actually sure how widespread this is, but even if it's just spawn becacons that's pretty banging

* Fixes random hell Move() call counts, removes the parent call from mob/Login

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [zhengshiJ/incubator-doris](https://github.com/zhengshiJ/incubator-doris)@[e9c3572d4b...](https://github.com/zhengshiJ/incubator-doris/commit/e9c3572d4b9cd07581be36eee802cdb67f39f513)
#### Friday 2021-12-24 06:26:46 by HB

[docs] Improve the chapter on debugging FE in doc.  (#7309)

At present, there are defects in the chapter on debugging FE in doc. My colleagues and I stepped on the pit when 
building the debugging environment, so I want to improve this chapter in combination with my own stepping on the pit 
experience.

The following is my explanation of the changes: 

1. mkdir -p ./thirdparty/installed/bin
explain: When I downloaded versions 0.14 and 0.15, there were no files under thirdparty, so I didn't know whether to 
create it myself or what to do. Finally, I decided to create it myself. I think it's necessary to add instructions here.

2. Add installation thrift@0.13.0 Failed handling method. 
explain: My colleagues and I failed to find the installation package when executing the installation command, and finally 
found a solution on GitHub. Therefore, I added the handling method of the problem to avoid other Mac users from 
getting stuck in this place.

3. Fixed an error in the generated code description.
explain: Before I finished building the code, I debugged FE, and I failed all the time. Idea hints that no files can be found. 
Later, after consulting with morningman in wechat group, it was understood that `mvn install -DskipTests` does not 
need to execute `mvn generate-sources` after execution. This is inconsistent with the description in the document and 
needs to be corrected.

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[4610f700eb...](https://github.com/vincentiusvin/tgstation/commit/4610f700eb74a3a41555e69c4904ad897caf2d99)
#### Friday 2021-12-24 07:06:20 by LemonInTheDark

Fixes up multiz atmos connection, cleans some things up in general (#63270)

About The Pull Request

ALLLRIGHT so
Multiz atmos was letting gas flow down into things that should be well, not flowable into
Like say doors, or windows.

This is weird.

Let's get into some context on why yeah?

First, how do things work currently?

atoms have a can_atmos_pass var defined on them. This points to a define that describes how they interact with
flow.
ATMOS_PASS_NO means well, if we're asked, block any attempts at flow. This is what walls use.
ATMOS_PASS_YES means the inverse
ATMOS_PASS_DENSITY means check our current density
ATMOS_PASS_PROC means call can_atmos_pass, we need some more details about this attempt

These are effectively optimizations.

That var, can_atmos_pass is accessed by CANATMOSPASS() the macro
It's used for 3 things.

1: Can this turf share at all?
2: Can this turf share with another turf
3: Does this atom block a share to another turf

All of this logic is bundled together to weed out the weak.

Anyway, so when we added multiz atmos, we effectively made a second version of this system, but for vertical
checks.

Issue here, we don't actually need to.
The only time we care if a check is vertical or not is if we're talking to another turf, it's not like you'll
have an object that only wants to block vertical atmos.
And even if you did, that's what ATMOS_PASS_PROC is for.

As it stands we need to either ignore any object behavior, or just duplicate can_atmos_pass but again.
Silly.

So I've merged the two, and added an arg to mark if this is a verical attempt.
This'll fix things that really should block up/down but don't, like windows and doors and such.

Past that, I've cleaned can_atmos_pass up a bit so it's easier for people to understand in future.
Oh and I removed the second CANATMOSPASS from immediate_calculate_adjacent_turfs.
It isn't a huge optimization, and it's just not functional.

It ties into zAirOut and zAirIn, both of which expect to be called with a valid direction.
So if say, you open a door that's currently blocking space from leaking in from above, you end up with the door
just not asking the space above if it wants to share, since the door can't zAirOut with itself.

Let's just wipe it out.

This makes the other code much cleaner too, heals the soul.

Anyway yadeyada old as ass bug, peace is restored to the kingdom, none noticed this somehow you'd think people
would notice window plasma, etc etc.
Why It's Good For The Game

MUH SIMULATION
Also fuck window gas
Changelog

cl
fix: Fixed gas flowing into windows from above, I am.... so tired
fix: Fixes gas sometimes not moving up from below after a structure change, see above
/cl

---
## [acatalfano/rethink-first-app](https://github.com/acatalfano/rethink-first-app)@[4adb2b859d...](https://github.com/acatalfano/rethink-first-app/commit/4adb2b859d9097cc4b2ff550364d0944ca5b1949)
#### Friday 2021-12-24 07:18:27 by Adam Catalfano

rollback where I left a ton of ugly-as-flying-fuck todo's---Amy if you look at this commit, be gentle! it's not meant for ppl to see and I hate it!

---
## [connectuum/poemdown](https://github.com/connectuum/poemdown)@[132d125dd8...](https://github.com/connectuum/poemdown/commit/132d125dd890b596ef5bdcdaa07d5be09041a64c)
#### Friday 2021-12-24 08:10:28 by connectuum

refactored the HTML-conversion process

as we enter into algorithm, demands upon concentration increase. find your quiet place, your flow state, your algorithm rhythm.

commit goal: begin the real HTML-conversion algorithm.

immediate obstacles: the existing `ToHtml()` function already feels overly complicated and deeply-branching. also, if we were to write a new `ToBetterHtml()` function, there would be a lot of duplicated code. duplicated code should be healed, collapsed, into a new function, reusable anywhere.

(otherwise: code copies drift out of sync due to human error, leading to a broad class of bugs where human _expectation_ of functional-equivalence collides with a different _reality_. to avoid refactoring is to encourage _more_ such duplication and inconsistency. travel that path long enough, and your problems shall become great enough to earn a name: _technical debt_.)

refactoring is holy: seek it always.

a refactor _appreciates_ code already set in place, understands exactly what that code achieves, its purpose... then shatters it without mercy, reassembling it into something better. [slow zoom out of fractal into itself again]. demand the right to change. to grow. to break. to prune away, then reach ever further. YOU.

now to the problem at hand: refactoring our whitespace-related logic into a new, focused, testable, reusable function.

to perform its work, this function must know which character to consider, and (for tabs) the number of characters present in the current line of converted text. it produces an dual output, for clarity and convenience of use; consider `if ( TryFind(x, out y) ) { use y; }` vs. all the nullness in `var y = FindOrNull(x); if ( y != null ) { use y.Value; }`.

the function's name, inputs, and outputs are its exterior signature. code written elsewhere can call upon this signature, sending along inputs to receive outputs in return. within this new exterior, however, the HTML-conversion logic (the `switch` conditions and their resulting outcomes) remains the same.

with refactor complete, the old `ToHtml()` sheds its shadow, keeping only its unique rainbow-coloring capabilities. the new `ToHtml()` isn't _nearly_ as interesting yet, but is now poised to begin growth. the conversion algorithm shall take root here.

_By and Down the River_ has been my song today, and found its way into the work. the song seems broadly aimed at empty, insincere leadership. but it also admonishes internally: give Light unto your work, share of it and benefit, lest it bloat, betray, and decay you. another scale smaller, and it places you as judge of your own plans, paths, and aspirations; which are worthy? which shall rot your soul?

and here is that holy recursion, that nested depth-wise repetition, we see it everywhere; it resonates throughout. it feels of universe, and the point was: i feel it also in this music, these words. it feels like Truth.

as does [the strain of context]. if everything breaks down _two_, then the challenge is to defy the sharpest oppositional gravities. defy... as in [defy, resist, counter], and _not_ [avoid, provoke, attack]. _not_ [mislead, brainwash, con, confuse]. _not_ [tribes and factions]. _not_ [win or lose].

what feels like Truth is a tapestry of bindings, all-woven from factual, fictional, emotional findings. different perspectives, interconnected, search-and-traversable, social-and-sharable, deeply private-protected. 

to spike into extreme is to deny our collective-connected binding, to boldly test [the strain of context]. this invites judgement, but not aggression: not all extremes are necessarily bad. Trust in the natural strain, and delight in the refactoring. then Trust the strain will smooth our way through change forevermore.

---
## [Byte-Masons/defi-ui-template](https://github.com/Byte-Masons/defi-ui-template)@[c63023cd91...](https://github.com/Byte-Masons/defi-ui-template/commit/c63023cd914d4bc7ed341387ce5dcce4b11da4fe)
#### Friday 2021-12-24 08:22:43 by Morgan Hall

Ask myself what would I want if I didn't know what I know

Get started on work to make the repo a reusable template for shady super-coders and noobs alike.

I've tried to approach this with the following principals:
- we shouldn't use anything so clever, it would create an obstacle to use for someone with less experience
- where we use anything that might be more complicated than paint-by-numbers we should demonstrate its use
- we should offer graduated customization paths so a non-tech person can personallize it with little fuss without preventing a power user from doing whatever they want

With that in mind, I have:
- Set the font to Montserrat.  Its safe, common, and harmless in case the consumer doesn't want to change it
- Added Storybook, and stories for each component we have, so anyone can see what components they have to play with
- Added react-navigation and set our app up as a 4-page demo so we can demonstrate its use
- Created some simple abstractions (components) for common layout css so a noob can find and use what they need without knowledge of CSS
- Used CSS modules and CSS variables so a user can choose to just change color scheme, configure dimensions and a more elaborate color config, or go into the CSS and change it there.
- updated the readme with some notes on use

Some notes:
- Ive chopped and changed between interface/type for defining props.  Theres nothing in this - my IDE quick templates write `interface`, I manually write `type`
- we have some components that are nothing more than a div with styles, and so could be achieved just by using a style.  We do this to make it easy for a novice to pick and choose components they require by name rather than having to understand CSS.  If the consumer does not use these components, tree shaking will omit them from the bundle anyway
- we typically pass bot `className` and `style` through to root tags on each component, to give the consumer max flexibility in styling
- we define props for almost every component, even when these are repetitive.  This is so less experienced devs can change for a single component with confidence. Types are removed in conversion to JS anyway

---
## [besser435/Fork-Knife](https://github.com/besser435/Fork-Knife)@[1e6034a917...](https://github.com/besser435/Fork-Knife/commit/1e6034a9171bbef8aac50d20cf20a94db349f724)
#### Friday 2021-12-24 08:58:55 by Brandon

I hate this

The guns part is done in an awful way oh boy
Actually, everything is done in an awful way.

---
## [mikairyuu/kernel_xiaomi_sm7250](https://github.com/mikairyuu/kernel_xiaomi_sm7250)@[213739de40...](https://github.com/mikairyuu/kernel_xiaomi_sm7250/commit/213739de40a2c173505b3f2ebbcda3dfbee3a690)
#### Friday 2021-12-24 09:03:52 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [opal/opal](https://github.com/opal/opal)@[d83d7400f4...](https://github.com/opal/opal/commit/d83d7400f49f8e255de9e10cf3fc277d195ef85b)
#### Friday 2021-12-24 09:25:06 by hmdne

Optimize $eqeq and $eqeqeq calls.

```
 Comparison of the Asciidoctor (a real-life Opal application) compile and run:
                  Compile time: 5.999 -> 5.987 (change: -0.19%)
                      Run time: 0.271 -> 0.268 (change: -1.11%)
                   Bundle size: 4784558 -> 4766408 (change: -0.38%)
          Minified bundle size: 1027822 -> 1015882 (change: -1.16%)
            Mangled & minified: 716587 -> 702347 (change: -1.99%)
```

Similarly to how we optimize $rb_lt and friends to create a shortpath
for those, let's optimize $eqeq,$eqeqeq as well. This certainly brings
an incompatibility if we monkey patch those methods for Number/String,
but with the previous commit we made it reliable to return `nil` from
== and === which is in my opinion much more important.

---
## [RealAkito/frameworks_base](https://github.com/RealAkito/frameworks_base)@[91d7ff9f9a...](https://github.com/RealAkito/frameworks_base/commit/91d7ff9f9a5157a9eb6010688ae64fbf2a1ab4da)
#### Friday 2021-12-24 09:41:34 by Akito Mizukito

[HACK]: Hardcode horizon and intercept

For some whatever reason, AmbietFilter is unable to read its own configuration overlay in Evolution X...
We'll just... do this.

I hate my life.

Change-Id: I1f95bbae8960001b94ed634fce2b83c4fdc79582
Signed-off-by: Akito Mizukito <akito@evolution-x.org>

---
## [mosoft521/guava](https://github.com/mosoft521/guava)@[e015172847...](https://github.com/mosoft521/guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Friday 2021-12-24 09:52:54 by cpovirk

Remove `@Beta` from uncontroversial `Futures` methods:

- `submit`
- `submitAsync`
- `scheduleAsync`
- `nonCancellationPropagating`
- `inCompletionOrder`

I did also add a TODO to potentially make the return type of `scheduleAsync` more specific in the future. However, to the best of my knowledge, no one has ever asked for this. (That's not surprising: `ScheduledFuture` isn't any more useful than `Future` unless you're implementing a `ScheduledExecutorService`, and even then, access to its timeout is unavoidably racy.) Plus, should we ever need to do it, we can do it compatibly by injecting a bridge method with the old signature.

(I didn't see any discussion of the return type in the API Review doc or the CL review thread. It probably just didn't come up, or maybe we all independently concluded that it wasn't worth the trouble, given that `MoreExecutors.listeningDecorator(ScheduledExecutorService)` is a bit of a pain? But I'm guessing `scheduleAsync` would be easier.)

RELNOTES=`util.concurrent`: Removed `@Beta` from `Futures` methods: `submit`, `submitAsync`, `scheduleAsync`, `nonCancellationPropagating`, `inCompletionOrder`.
PiperOrigin-RevId: 416139691

---
## [starmaid/adventofcode2021](https://github.com/starmaid/adventofcode2021)@[70cd33f338...](https://github.com/starmaid/adventofcode2021/commit/70cd33f338500e168f2c19d0f2bacff88f37d551)
#### Friday 2021-12-24 10:05:01 by Nicholas Masso

god why the hell did my input have to be so SHITTY

---
## [rHermes/adventofcode](https://github.com/rHermes/adventofcode)@[e12181559f...](https://github.com/rHermes/adventofcode/commit/e12181559f0100103a879efb70b41f5618dfbfdc)
#### Friday 2021-12-24 10:32:34 by Teodor Spæren

2021 Day 24

What a task it was today! The toughest task of the year and maybe one of
the harder I've solved in AoC overall!

I spent a long time on this one and I tried multiple different avenues
when it comes to solving it.

The first approach I took was to try solve it by parsing the
instructions into a tree and then solve on that, creating an AST for
much the same purpose. I tried using z3 and sympy without making any
headway.

After maybe 3 and a half hours, I gave up on a general approach and
decided to try to reverse engineer my input directly. I translated it
into a python program using some sed commands and started going through
each step.

Here I realized that there is really is the same instructions 14 times,
but with 3 different variables, let's call them a, b and c. The output
from each round is the "z" register and the round is only dependent on
z, a, b, c and the input for this round, w.

Once I was able to isolate this, I then started reducing the round
function further, until it was something I could reason more
analytically about. I wasn't able to make some elegant solution as to
why this is the case, but in the end it comes out so that the only way
to reduce the "z" register in a round, is if the input number and the
"b" variable fullfills the equation:

((z % 26) + b) == w

where "w" is the input variable. I then guessed that we would take every
opportunity we could to reduce the variable and I wrote a function
around this. It feels like there should be some proof for this, but I'm
not able to work that out now.

I also don't know if all inputs follow the general pattern that I had,
and that you can solve this task by reading the abc's straight from the
input at specific places. I'll look more into this later.

One guy at work beat me today, with a time of 2 hours 58 minutes. I am a
bit mad about that, a blow to the ego :P

A great day, mixing reverse engineering and analytical thinking! I love
it!

Score:
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 24   04:58:40   1901      0   04:59:14   1793      0

---
## [Timwi/KtaneContent](https://github.com/Timwi/KtaneContent)@[d57e2753b5...](https://github.com/Timwi/KtaneContent/commit/d57e2753b5bfab52c0dda3c2d3725121dd9685db)
#### Friday 2021-12-24 11:51:30 by MasQueElite

Linted old manuals (#: a lot) (#1198)

* Linted old manuals, as well as my Cent. translations

Description: pain.

Also, could you check my translated 1000 Words and my translated Clock?
Seems like 1000 Words has a wrong word, and the Clock has an svg without newlines? (also it gets rid of the darkmode stuff oof sorry keep that)

Also, check The Swan (original) as well, I think that change is weird, but maybe the linter complained about it, I don't remember.
And I also deleted (in my translated Double-Oh) the .dark table, .dark td .strike selectors, sorry :c restore those as well plz
Aaaaaaaaand I think the rest is up do date. That's all about linting the original manuals.

* Redoing my changes that got wiped out in the merge

Co-authored-by: Luminoscity <luminoscity@gmail.com>

---
## [SilentEnforcer/tgwr-mod](https://github.com/SilentEnforcer/tgwr-mod)@[7ab848b0ac...](https://github.com/SilentEnforcer/tgwr-mod/commit/7ab848b0acd5e972f8a63bd1c9f96dee7ad20f75)
#### Friday 2021-12-24 14:01:26 by fallgelb22061940

removed my "feature"

enjoy cringe larp path and remember to walk today instead of laying in pc chair fuckers :trollface: :trollface: :trollface:

---
## [oxidecomputer/hubris](https://github.com/oxidecomputer/hubris)@[09fec719f3...](https://github.com/oxidecomputer/hubris/commit/09fec719f39d25e5e181377c313d9f4ef14ca316)
#### Friday 2021-12-24 15:44:48 by Cliff L. Biffle

Remove "standalone" build.

I introduced the standalone build early on as a way of quickly iterating
on a single task, without waiting for an entire image to build -- an
equivalent to `cargo check`. It has proven somewhat useful but also
breaks things.

- The standalone build does not build the actual code you'd ship, it
  instead configures the code in "standalone mode" where a bunch of
  stuff is arbitrarily stubbed out. This means that getting a successful
  standalone build tells you little about the real build.

- You can also _forget_ to put in the standalone magic, in which case
  your actual firmware builds, but then someone else doing a
  "standalone" build later faces a cryptic failure. This is why the
  standalone builds are run in CI -- to avoid this.

- As we introduce increasing levels of configurability in tasks,
  stubbing that configuration out in arbitrary ways is getting harder.
  When it was a matter of conditional compilation driven by board name,
  we could sprinkle in some `feature = "standalone"` hacks to guide it.
  As we move toward task slots and general configuration data in the
  app.toml, the main distinguishing feature of the standalone build --
  that it does not _have_ an app.toml -- starts to become a real pain.

My iteration workflow is currently served by `cargo xtask build`. I am
not aware of any reliable way of getting RLS/rust-analyzer to work on
Hubris, even _with_ the standalone build, so this shouldn't regress
editor support.

---
## [Abefeidileke/Abefeidileke](https://github.com/Abefeidileke/Abefeidileke)@[ea96a1cf2a...](https://github.com/Abefeidileke/Abefeidileke/commit/ea96a1cf2aa034e0040b54fbc637362569096601)
#### Friday 2021-12-24 17:09:48 by Abefeidileke

As I was saying when God create us he give us knowledge

When we wake up we see a new thing everyday why can't you change for Newton everyday success is not by Force but by choice never think you small or big for success or for anything too pushy to your great hire you never know how thick river may take until you enter it you never know how a Russian is drawing until you enter it but always remember he's either you work or croc or run or fly make sure you didn't stop on the road of success it's not over auntie is over 3rd mate off the challenges may much but always remember the challenges is the food of champion without story no Glory I still remain a Abefeidileke

---
## [Abefeidileke/docs](https://github.com/Abefeidileke/docs)@[060911c369...](https://github.com/Abefeidileke/docs/commit/060911c369e0caff13adc01589bb4245d55e5e60)
#### Friday 2021-12-24 17:22:27 by Abefeidileke

My story

We get married and November 2005 since then he has been show me his real face he will beat me commandment on top of my money he will let me know cool with another woman for so many days I don't know what to do I really stay home and cry and after I get my memory back I'll go to my work and when I came back and say sorry retrieve me and collect money from me this life I don't know what to call me but what I know is that it's not all the mens are bad I can't remember how my father used to treat me and my mother he will go for us it doesn't want to even see us over for a little bit may his soul rest in peace ok I'll continue my story hope you are with me thank you

---
## [avar/git](https://github.com/avar/git)@[56314e85ac...](https://github.com/avar/git/commit/56314e85ac64fc765476f9eb3516c659e7aacee5)
#### Friday 2021-12-24 17:59:07 by Ævar Arnfjörð Bjarmason

usage API: add "core.usageAddSource" config to add <file>:<line>

Optionally extend the support that BUG() has had for emitting line
numbers to the {usage,fatal,error,warning}{,_errno}() functions.

Before we'd unconditionally get error messages like:

    $ git -c core.x=y config --get --bool core.x
    fatal: bad boolean config value 'y' for 'core.x'

Which can be changed with core.usageAddSource=true to include the file
and line numbers:

    $ git -c core.usageAddSource=true -c core.x=y config --get --bool core.x
    fatal: config.c:1241: bad boolean config value 'y' for 'core.x'

As the added documentation notes this is primarily intended to be
useful to developers of git itself, but is being exposed as a user
setting to e.g. help file better bug reports.

This also adds a "GIT_TEST_USAGE_ADD_SOURCE" setting intended to run
the test suite in this mode.

Currently it has a lot of failures. Most of those are rather trivial,
and can be "fixed" by pointing GIT_TEST_CMP to a "diff -u" that does a
s/^(usage|fatal|error|warning): [^:]+:[0-9]+/$1/g on its input files,
and likewise for a "grep" wrapper that does the same.

Even if we can't run the tests in this mode yet I'd like to have this
for ad-hoc debugging, and to make it easier to work towards running
the tests in this mode. If we can turn this on permanently it'll be
much easier to read test output, as we won't need to worry about the
indirection of looking up where an error might have been emitted,
which can be especially painful when the message being emitted isn't
unique within git.git.

This new code needs to be guarded by the "dying" variable for the
reasons explained in 2d3c02f5db6 (die(): stop hiding errors due to
overzealous recursion guard, 2017-06-21), and for those same reasons
it's racy under multi-threading.

Here the worst case is that incrementing the variable will run away
from us, and we won't get our desired <file>:<line> number. That's OK
in this case, those cases should be isolated to the config code (if we
can't parse the config), memory allocation etc, but we'll get it right
in the common cases.

Using GIT_TEST_USAGE_ADD_SOURCE should be immune from any racyness, as
it only needs a getenv() and git_parse_maybe_bool(), which won't die.

Add a repo_cfg_bool_env() wrapper to repo-settings.c for
GIT_TEST_USAGE_ADD_SOURCE, in 3050b6dfc75 (repo-settings.c: simplify
the setup, 2021-09-21) I indicated that the GIT_TEST_MULTI_PACK_INDEX
env variable/config pair in that file has odd semantics, but users of
repo_cfg_bool_env() have straightforward and expected semantics. If
the environment variable is set (true or false) we'll use it,
otherwise we'll use the config, and finally fall back on the
default (of "false", in this case).

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [polygoblyn/MonkeStation](https://github.com/polygoblyn/MonkeStation)@[d011e51dcf...](https://github.com/polygoblyn/MonkeStation/commit/d011e51dcf956ceebd29b54c8594cde48a740e6d)
#### Friday 2021-12-24 18:03:26 by nednaZ

Adds a newline to this file

I know a commit to master is bad, but oh my god it's one newline because this was made BEFORE the new linter requirements and this wasn't caught after the upstream merge.
I'm literally typing a hundred times the edit amount to justify adding the enter key.

How are you though? I hope things are going well for you, keep your mind fresh and don't stress over the small stuff because it's not worth it.
And always remember, grab moths.

---
## [McDutchie/ksh](https://github.com/McDutchie/ksh)@[c5018f7c95...](https://github.com/McDutchie/ksh/commit/c5018f7c9523a1e9d2039ae83caf52a8011dec82)
#### Friday 2021-12-24 18:12:24 by Martijn Dekker

Re-fix defining types conditionally or in subshells (re: 5cc9fcc1)

New version. I'm pretty sure the problems that forced me to revert
it earlier are fixed.

This commit mitigates the effects of the hack explained in the
referenced commit so that dummy built-in command nodes added by the
parser for declaration/assignment purposes do not leak out into the
execution level, except in a relatively harmless corner case.

Something like

    if false; then
        typeset -T Foo_t=(integer -i bar)
    fi

will no longer leave a broken dummy Foo_t declaration command. The
same applies to declaration commands created with enum.

The corner case remaining is:

    $ ksh -c 'false && enum E_t=(a b c); E_t -a x=(b b a c)'
    ksh: E_t: not found

Since the 'enum' command is not executed, this should have thrown
a syntax error on the 'E_t -a' declaration:
ksh: syntax error at line 1: `(' unexpected

This is because the -c script is parsed entirely before being
executed, so E_t is recognised as a declaration built-in at parse
time. However, the 'not found' error shows that it was successfully
eliminated at execution time, so the inconsistent state will no
longer persist.

This fix now allows another fix to be effective as well: since
built-ins do not know about virtual subshells, fork a virtual
subshell into a real subshell before adding any built-ins.

src/cmd/ksh93/sh/parse.c:

- Add a pair of functions, dcl_hactivate() and dcl_dehacktivate(),
  that (de)activate an internal declaration built-ins tree into
  which check_typedef() can pre-add dummy type declaration command
  nodes. A viewpath from the main built-ins tree to this internal
  tree is added, unifying the two for search purposes and causing
  new nodes to be added to the internal tree. When parsing is done,
  we close that viewpath. This hides those pre-added nodes at
  execution time. Since the parser is sometimes called recursively
  (e.g. for command substitutions), keep track of this and only
  activate and deactivate at the first level.
     (Fixed compared to previous version of this commit: calling
  dcl_dehacktivate() when the recursion level is already zero is
  now a harmless no-op. Since this only occurs in error handling
  conditions, who cares.)

- We also need to catch errors. This is done by setting libast's
  error_info.exit variable to a dcl_exit() function that tidies up
  and then passes control to the original (usually sh_exit()).
     (Fixed compared to previous version of this commit: dcl_exit()
  immediately deactivates the hack, no matter the recursion level,
  and restores the regular sh_exit(). This is the right thing to
  do when we're in the process of erroring out.)

- sh_cmd(): This is the most central function in the parser. You'd
  think it was sh_parse(), but $(modern)-form command substitutions
  use sh_dolparen() instead. Both call sh_cmd(). So let's simply
  add a dcl_hacktivate() call at the beginning and a
  dcl_deactivate() call at the end.

- assign(): This function calls path_search(), which among many
  other things executes an FPATH search, which may execute
  arbitrary code at parse time (!!!). So, regardless of recursion
  level, forcibly dehacktivate() to avoid those ugly parser side
  effects returning in that context.

src/cmd/ksh93/bltins/enum.c: b_enum():

- Fork a virtual subshell before adding a built-in.

src/cmd/ksh93/sh/xec.c: sh_exec():

- Fork a virtual subshell when detecting typeset's -T option.

Improves fix to https://github.com/ksh93/ksh/issues/256

---
## [leoDesilva/MathALang](https://github.com/leoDesilva/MathALang)@[7174c3662f...](https://github.com/leoDesilva/MathALang/commit/7174c3662fbcf21ebd40d7d524a7207175b82fbf)
#### Friday 2021-12-24 18:16:51 by leoDesilva

It took an unconcionable amount of time just to implement modifying arrays at an index so here, after a solid day's work litterally getting a single thing done. It Is Done. Please God No More. I just love coding, the funny thing is that it only took like 10 lines of code, and a hacky solution that was three single characters (i guess four) '+[0]' saved what was about 4 hours work and like 50 lines of code :), thank you for listening to my Ted Talk.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5afa770b15...](https://github.com/mrakgr/The-Spiral-Language/commit/5afa770b157dec1ef137702ea21b89aad17b0bb7)
#### Friday 2021-12-24 18:24:30 by Marko Grdinić

"9:35am. I am up and why is Youtube having ads? Is UBlock broken?

9:50am. Let me chill a bit and then I will start.

10:25am. Let me start. Through the nightmare, I will reach my victory.

1) Normals.

First up, it is normals.

In the future, it will definitely be worth it to get hyped up for genetic programming, but I need some support. In order to revive the poker plan, I need to find the algorithms first. And how much computation and effort I will need for that is unknown to me.

A single Grayskull chip would be enough to get me back into the game. I could build the C backend and the GP system, but probably not find the algorithms for the memory system. So it would end much like before. I'd do my duty, but I need reinforcements to really push it through to the victory point.

I don't know how I will get the necessary resources. Getting a job and investing in the market would take too long. It would also tie up my time.

Making games has an open ended upside, so it could potentially work, but I'd need a lot of luck.

I've had an idea yesterday - I might be able to associate myself with the GP crowd. I'd need to become a researcher, but those are poor as hell if Zenna is any indication. Still, if Heaven's Key flops very hard, that would be an option.

10:35am. I'll think about that whne it comes to it. The power of good art should not be that weak. I should be able to attract some customers for my vision of the future.

The success of my game work does not really hinge on my programming skills though, just on my artistic vision and perseverance.

If I could just get the next level of algorithms, I could become unstoppable. I could rampage through the online dens, make an untold amount of money and buy all the hardware that I need to see me all the way to the Singularity.

10:40am. In a real world, I could live and die by my programming ability.

Right now, I suppose I have no choice, but to become a charlatan.

Job vs game. Honestly, if the job market hiring wasn't so broken and the only thing I had to do to get hired was to beat a difficult challenge, I would not mind getting it. If other people are really better than me I could accept my loss, but getting filtered by a bunch of drones quashes my desire to work at that at all.

The world is really heavily signaling me that wagies are at the bottom of the tottem pole.

Since things are like that, I should chose the hard and irrational choices. If I could have made these kinds of moves in ML, I could have probably found the algorithms that I needed.

To achieve true excellence, I should always be making the choices that increase my skills.

Imagine if during high school I quit it with the intention of focusing solely on programming. I could have used the Internet to study, got a job. I could very well have been a millionaire by now. Instead I let myself be coerced to go down the path laid out by others to my detriment. That was the time to show my will and I blew it.

I need the money now to get the algorithms. If I had a million to get the right hardware, I might be able to leapfrog the rest of the field in this race. Instead I have no choice, but to gamble to stay afloat.

10:50am. Sigh, if the humanists succeed in their friendly AI project, we'll be lucky if it just kills us all.

Maybe after all is said and done, I'll get a chance to reload with my skills intact. Who knows.

I do not want to rely on anything. Not other people, not God, not even myself. I only want to rely on a well made plan. And I should act in line with my ambition and character. So let me watch those tutorials.

Normals.

https://youtu.be/lmMD9fV98Co
What Are Normals? 3D Fundamentals (Blender 2.8)

11:20am. There is some buggy behavior. When you use set from faces when shading flat it smoothes out the vertex normals as if it were shaded smooth. Then if you go into that mode, you get weird lighting. The only way to fix that is to repeat the operation in smooth mode.

Strangely enough, I do not know how to fix it directly in shade flat mode. Let me get back to the video.

Done.

https://docs.blender.org/manual/en/latest/modeling/meshes/editing/mesh/normals.html?highlight=normal#rotate

There is no choice, I need to read the manual.

11:50am. Ok, the best way to restore the normals is to just use reset vector. That bring them back once they've been smoothed out.

https://youtu.be/sqGFhiP-2mc
Weighted Normal | Blender 2.8x Tutorial

I've been playing with normal options, but they are so similar that I have no idea what they are doing. At least, I now know how to rotate and point them to a target.

I have an inkling that I could have gotten the plasma to work simply by shading smooth. Let me try that.

Yep. All auto smoothing does is average out the corner normals. You can literally see it at work in edit mode when the normals are set to show in overlays.

I've been under the impression that it does something tricky, but it is quite simple. Had I understood this, I'd not have been fooled by facing options. The layer weights work based off normals and this completely tripped them up.

Let me add a bevel.

12:40pm. Sigh, what a waste of time. I do not think the normals were broken at all when using facing. It is just that I did not have translucency. Actually, no that is not it. He is using something else to immitate translucency. What a good job he did. I'll have to study it more. The power trick is better than using the color ramp for controling the factor.

https://youtu.be/sqGFhiP-2mc
Weighted Normal | Blender 2.8x Tutorial

Let me round off the normals with this last vid and then I'll stop for the morning.

https://youtu.be/sqGFhiP-2mc?t=312

Yeah, I was starting to suspect that face normals are decorative. Let me finish the tutorial, and I will consider what to do next.

https://youtu.be/sqGFhiP-2mc?t=340

Surprisingly the vertex normals do not affect shading either.

1:25pm. I am playing with the effect now, and having the faces that are facing you be transparent is a really cool effect. I have been looking something like it.

1:30pm. Enough, let me have breakfast here. I need to do the chores.

2:05pm. Done with chores. Breakfast time.

3:15pm. Let me resume.

Where was I? I am of the mind that messing with procedural textures and such is too much of a pain in the ass. I really can always touch it up in CSP. if I want finely shaped mist, I can do it using sculpting.

Nevermind that for now.

2) Properties.
3) Visual effects. The materials pack as well.
4) Aura.
5) The geometry nodes course.

https://youtu.be/9ehbb93atqo?t=932

I am done with normals. Let me study properties. That should not be too hard.

https://youtu.be/_197jQFh22E
Custom properties and drivers in blender made easy

Let me go with this.

3:30pm. I watched 2/3rds of it. It is a fairly fast tutorial. This is enough, I learned all that I wanted to. Properties are easy. I expected that I would be able to use #property format, but it seems it is different than that.

Let me finish the video from yesterday.

3:35pm. Mmaybe it is fine if I lose because I followed the art route. I'll cultivate it to the best of my ability, but if that does not work out then I simply was not good enough to serve as the catalyst. There isn't a way of doing this that has a 100% chance of suceeding, so chosing a path that depenends solvely on my own effort has appeal. I'll be able to accept the outcome if I go down this way.

https://youtu.be/9ehbb93atqo?t=1192

The way he does this scripting is interesting. I wonder if I could just use the custom property like this directly?

3:50pm. I do not know. For some reason I can't get properties to work. Let me finish the video and then I'll look at the previous one again.

Ok, I understand custom properties, but how do I use material properties?

https://youtu.be/rZQyot2rQNU
Creating Custom Properties in color, degree, float, and Booleans Value | blender 2.9

Let me watch this for a bit. Sigh, I am in tutorial hell again.

I figured it out myself. It turns out you can copy and paste drivers directly. Now that I click on edit I see where I went wrong. I need the materials ID.

4:10pm. Ok, I am done with the properties for good this time. Let me check out auras.

https://www.youtube.com/results?search_query=blender+aura

There is a bunch on this here.

https://youtu.be/Fymn4Qt7enY
Blender 2.81+ EEVEE - Super Saiyan Auras Tutorial w/ Download

This is pretty cool.

https://youtu.be/Fymn4Qt7enY?t=241

This step is surprising. It does not connect it to normals?

https://youtu.be/Fymn4Qt7enY?t=486

How formidable. You really can do anything with procedural textures can't you?

https://youtu.be/Fymn4Qt7enY?t=1158

He says he did not know how to do the yellow glow at the back. One solution would be to add a separate object that is empty in front.

Another option might be to use 'facing' together with something that checks the normal direction. I do not know what that would be though.

4:45pm. Ok, what is next?

Geometry nodes. Let me do just a tad of sculpting. I want to see how a gradient texture would be affected by the mesh shape.

5pm. How does the mapping node work? I do not get this. Also, I get that the object coordinates are attacked to the pivot point, but what about generated and the rest.

https://youtu.be/XfTZc1SuQSA
Blender 3D Tutorial : Texture Coordinate and Mapping Nodes in Blender 3D (W/O Node Wrangler)

https://docs.blender.org/manual/en/2.79/render/cycles/nodes/types/vector/mapping.html

////

Vector type
Allows the user to choose which vector type to use.

Texture
This is the most common option that you will use and will be sufficient for most cases.
Point
This works similar to Texture but the way the math works the Scale values are divided rather than multiplied.
Vector
Behaves the same as Point mode but changes in Location are ignored – that is, the texture does not move.
Normal
Transforms a normal vector with unit length.

///

Ok, nevermind what the difference between generated and object are. They are the same just shifted. Forget that.

5:10pm. Ok, that is that. I need to finalize this in my head. Let me take a short break just to think.

5) The geometry nodes course.

I have this thing left only.

So far it is day two of my HDRI adventure.

5:25pm. I think the biggest problem is that one particular scene I've been envisioning is impossible.

5:30pm. Damn it, I sure do not feel like starting work now. I'd rather just stop here and start when I am fresher. My suffering is high, but let me embrace it even more.

Let me watch some tutorials. I want to get some geomtry node knowledge After that I'll start for real. I am going to focus from here on out.

This proceduaral stuff requires too much knowledge, what I should do from here on out is what I can either sculpt or model directly. Let me do it.

https://www.youtube.com/playlist?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB

Let me go through this from top to bottom.

https://youtu.be/QhIIZbhlaqg?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=70

This is really amazing. I wish I had the skill to create this.

https://youtu.be/QhIIZbhlaqg?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=587
> Imagine having a library of your own digital assets such as trees, buildings, books, etc.

5:55pm. This is a hybrid programming/art approach to art. It is should be something I master.

5:55pm. https://youtu.be/sBJ-HuBL6gw?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=130

This video will be my limit for today. I just do not have enough energy to do much more. I am not sure I have enough to even finish this. Yesterday I had a good night's sleep, but now I woke up too early and I've been feelings strained.

I think after I deal with geometry nodes, the only hurdle I will have left is rigging. I still have a bit more learning to do before I can be considered a fully fledged sculptor.

6pm. Tomorrow, I'll want to do some art and watch the rest of this course. I am going to simplify my thinking to what is possible and create that HDRI. Then I can pat myself on the back for finishing the first real thing and do some learning. This is the way things should go - you learn a bit, you play a bit. The two steps feed into each other and create motivation to keep going. Just watching tutorials is hell.

https://youtu.be/sBJ-HuBL6gw?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=737

Oh wow, I wouldn't have thought to use S here. Let me go have lunch.

6:35pm. Let me resume. Just a bit more and I am done. This tutorial is not too hard, but it is useful. My understanding of how to manipulate nodes is really lacking, so even this beginner tutorial has material new to me.

6:45pm. https://youtu.be/sBJ-HuBL6gw?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&t=1140

This video is not as tedious as I thought it would be.

7:05pm. https://www.youtube.com/watch?v=L_8xTV3IP3A&list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB&index=5
04 Applying Materials -Geometry Nodes For Beginners / Blender 3.0

Let me stop here. I am done for the day. Watching the first video did raise my motivation to watch the following ones. This course is worth watching. I'll do it tomorrow, and then just get something done. I keep wanting to do something something fancy with the abyss without actually being fancy. Radical simplicity is not an easy thing. Forget it. I'll just go with simplicity and add things as as I go along.

I do not have any particularly good ideas as far as art is concerned. I doubt I am going to come up with particularly inspired images. So let me just do the least that I can. There is no point in adding things for the sake of it.

I might have a habit of spreading my net widely when learning, but when it comes to work I like to do it in the simplest possible way.

Since I am in doubt, I'll just do that here."

---
## [MikhailChaus/TableView-iPhone-Settings](https://github.com/MikhailChaus/TableView-iPhone-Settings)@[b918a81f61...](https://github.com/MikhailChaus/TableView-iPhone-Settings/commit/b918a81f61d39698242125828b224aa089300f49)
#### Friday 2021-12-24 18:51:20 by Mikhail Chaus

Delete Storybord.

Fuck you main.storyboard. You are suck!

---
## [JustLenard/TheOdinProject-FreeCodeCamp-Learning-Projects](https://github.com/JustLenard/TheOdinProject-FreeCodeCamp-Learning-Projects)@[1312ca9796...](https://github.com/JustLenard/TheOdinProject-FreeCodeCamp-Learning-Projects/commit/1312ca9796498e29525b025ad90802b4aa16816e)
#### Friday 2021-12-24 20:06:34 by Cociug Vitalie

Updade

I can't believe it. Such a stupid thing happened to me. 
My only acces to electricity for my PC died. Now I can't fucking code. 
The thing is, I even did some coding in the morning but
Didn't push it. I so don't wanna lose my streak so fuck, this what I am going to do

---
## [superpowers04/FNF-PsychEngine](https://github.com/superpowers04/FNF-PsychEngine)@[86a44f5f1f...](https://github.com/superpowers04/FNF-PsychEngine/commit/86a44f5f1fe53b8c08d310aeff47e3c636e4bfe4)
#### Friday 2021-12-24 20:17:02 by ShadowMario

Fixed dumb stupid ass mistake

Jesus fuck i think i lost half of my braincells, now i only have a quarter left

---

