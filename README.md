## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-08](docs/good-messages/2022/2022-05-08.md)


1,498,293 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,498,293 were push events containing 2,192,235 commit messages that amount to 109,368,823 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[0504c0a2b4...](https://github.com/tgstation/tgstation/commit/0504c0a2b466d617efd4dcc77b092fcdbdad24be)
#### Sunday 2022-05-08 00:02:35 by LemonInTheDark

Improper forced qdel cleanup,  some expanded del all verbs (#66595)

* Removes all supurfolus uses of QDEL_HINT_LETMELIVE

This define exists to allow abstract, sturucturally important things to
opt out of being qdeleted.
It does not exist to be a "Immune to everything" get out of jail free
card.
We have systems for this, and it's not appropriate here.

This change is inherently breaking, because things might be improperly
qdeling these things. Those issues will need to be resolved in future,
as they pop up

* Changes all needless uses of COMSIG_PARENT_PREQDELETED

It exists for things that want to block the qdel. If that's not you,
don't use it

* Adds force and hard del verbs, for chip and break glass cases
respectively

The harddel verb comes with two options before it's run, to let you
tailor it to your level of fucked

* Damn you nova

Adds proper parent returns instead of . = ..()

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

* Ensures immortality talismans cannot delete their human if something goes fuckey. Thanks ath/oro for pointing this out

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

---
## [KDr2/llvm-project](https://github.com/KDr2/llvm-project)@[c2c259224b...](https://github.com/KDr2/llvm-project/commit/c2c259224bb30b089206dd69dc44aefddffec2f4)
#### Sunday 2022-05-08 00:07:39 by Amaury Séchet

const char* for LLVMTargetMachineEmitToFile's argument

The `LLVMTargetMachineEmitToFile` takes a `char* Filename` right now, but it doesn't modify it.
This is annoying to use in the case where you want to pass a const string, because you either have to remove the const, or copy it somewhere else and pass that. Either way, it's not very nice.

I added a const and clang formatted it. This shouldn't break any ABI in my opinion.
I'm sorry but I didn't know whom to put as reviewer for this, so I chose someone with a lot of commits from the .cpp file.

Reviewed By: deadalnix

Differential Revision: https://reviews.llvm.org/D124453

---
## [luckyzyx/Grasscutter](https://github.com/luckyzyx/Grasscutter)@[fbaeaee4b5...](https://github.com/luckyzyx/Grasscutter/commit/fbaeaee4b5aa82fe10897b60ea642d4428e8abd8)
#### Sunday 2022-05-08 00:37:25 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [Vandora-41/psychonaut](https://github.com/Vandora-41/psychonaut)@[98f32035d8...](https://github.com/Vandora-41/psychonaut/commit/98f32035d8dbd6b925700e9934652d03739f024b)
#### Sunday 2022-05-08 00:40:12 by LemonInTheDark

Parallax but better: Smooth movement cleanup (#66567)

* Alright, so I'm optimizing parallax code so I can justify making it do a
bit more work

To that end, lets make the checks it does each process event based.
There's two. One is for a difference in view, which is an easy fix since
I added a view setter like a year back now.

The second is something planets do when you change your z level.
This gets more complicated, because we're "owned" by a client.
So the only real pattern we can use to hook into the client's mob's
movement is something like connect_loc_behalf.

So, I've made connect_mob_behalf. Fuck you.

This saves a proc call and some redundant logic

* Fixes random parallax stuttering

Ok so this is kinda a weird one but hear me out.

Parallax has this concept of "direction" that some areas use, mostly
the shuttle transit ones. Set when you move into a new area.
So of course it has a setter. If you pass it a direction that it doesn't
already have, it'll start up the movement animation, and disable normal
parallax for a bit to give it some time to get going.

This var is typically set to 0.

The problem is we were setting /area/space's direction to null in
shuttle movement code, because of a forgotten proc arg.

Null is of course different then 0, so this would trigger a halt in
parallax processing.

This causes a lot of strange stutters in parallax, mostly when you're
moving between nearspace and space. It looks really bad, and I'm a bit
suprised none noticed.

I've fixed it, and added a default arg to the setter to prevent this
class of issue in future. Things look a good bit nicer this way

* Adds animation back to parallax

Ok so like, I know this was removed and "none could tell" and whatever,
and in fairness this animation method is a bit crummy.

What we really want to do is eliminate "halts" and "jumps" in the
parallax moveemnt. So it should be smooth.

As it is on live now, this just isn't what happens, you get jumping
between offsets. Looks frankly, horrible. Especially on the station.

Just what I've done won't be enough however, because what we need to do
is match our parallax scroll speed with our current glide speed. I need
to figure out how to do this well, and I have a feeling it will involve
some system of managing glide sources.

Anyway for now the animation looks really nice for ghosts with default
(high) settings, since they share the same delay.

I've done some refactoring to how old animation code worked pre (4b04f9012d1763df625e9e4ae75e4cf4bd1f3771). Two major
changes tho.

First, instead of doing all the animate checks each time we loop over a
layer, we only do the layer dependant ones. This saves a good bit of
time.

Second, we animate movement on absolute layers too. They're staying in
the same position, but they still move on the screen, so we do the same
gental leaning. This has a very nice visual effect.

Oh and I cleaned up some of the code slightly.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[27946f516d...](https://github.com/timothymtorres/tgstation/commit/27946f516dd77faa071576499bb700c6fa22fbab)
#### Sunday 2022-05-08 01:02:57 by san7890

Update Comments and Adjusts Incorrect Variables for Map Defines and Map Config (#66540)

Hey there,

These comments were really showing their age, and they gave the false impression that nothing had changed (there was a fucking City of Cogs mention in this comment!). I rewrote a bit of that, and included a blurb about using the in-game verb for Z-Levels so people don't get the wrong impressions of this quick-reference comment (they always do).

I also snooped around map_config.dm and I found some irregularities and rewrote the comments there to be a bit more readable (in my opinion). Do tell me if I'm a cringe bastard for writing what I did.

Also, we were using the Box whiteship/emergency shuttle if we were missing the MetaStation JSON. Whoops, let's make sure that's fixed.

People won't have to wander in #coding-general/#mapping-general asking "WHAT Z-LEVEL IS X ON???". It's now here for quick reference, as well as a long-winded section on why you shouldn't trust said quick reference.

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[d411393e72...](https://github.com/Pickle-Coding/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Sunday 2022-05-08 01:14:15 by Zytolg

NukeOps Firebase Rework (#66149)

Attention Recruit: Welcome to Firebase Balthazord
Here you will lean how to:
-Kill corpo scum
-Kill corpo scum
-Kill corpo scu-

This has been on my docket for months. Ever since gave the Holding Facility a much needed facelift. I have been eyeballing the nukie base, waiting for that stroke of inspiration to hit me. It finally did. Gone are the aging walls of the old encampment. Nukies finally have what well-funded corpo-terrorists always dream of- a home.

It's more than a Home. This is a sweeping rework that is part of a series of reworks to revisit old locations and not only bring them up to date with our current asset roster, but to make them properly belong within the game world. The Nuke-Ops base may ultimately be a tiny chunk of the overall SS13 experience, but I'll be damned if it isn't a defining one. It's also a location that has the capacity to do one thing that I have always wanted to do. Purchase Property. You heard me right, you get to buy rooms now. The newly expanded Nuke-Ops base features, with @Mothblocks blessing, further expansions that you can purchase from your local Syndicate Uplink. Spend your TC, expand your capabilities, and utilize your expertise in order to create
the most mind-boggling disky heists there are.

Possible expansions to your terrorism suite include:
-Ordinance Lab
-Bio-Terrorism Lab
-Chemical Manufacturing Plant

Definite expansions to your Nuke-Ops Firebase include:
-Crew Bunks
-Lab Wing
-War Table
-Upgraded "Disembarkment" Bay"

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[4652d4bb63...](https://github.com/Pickle-Coding/tgstation/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Sunday 2022-05-08 01:14:15 by Jolly

Updates The Derelict to some modern standards, also some turf edits (#66045)

Brings The Derelict up to speed with some of our new mapping tools and stuff.
This also places nearstation turf in certain areas, as well as general turf clean up.
Also cleans up the absurdly placed black holes of light that were over space tiles.
Girder/Grill spawners were placed in certain locations (mostly on external girlls).
I also remapped the main AI chambers SMES power to not go through the fucking wall, as a trade off, its no longer wired round start, and the two pieces of cable that are automatically in the room have been swapped out for two (2) five cables each. Its not enough to reach the main area, but god fuck wires running through walls.

As an aside, some of plating on the outside, walls include, does look weird being full bright like this. I'm neutral for the most part. Theres a weird fine balance that needs to be maintained with some of the areas being open to space, I've opted to keep lattice as nearstation and any thing plating and above as turfed (excluding plating that is solely in space).

I'll be redoing the turfs of this later, sprite wise.

Images

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[b86cf89125...](https://github.com/Pickle-Coding/tgstation/commit/b86cf89125a425ad650abedf436bb02918c36dcd)
#### Sunday 2022-05-08 01:14:15 by Aleksej Komarov

tgui: API improvements + docs (#65943)


About The Pull Request

This pull request improves tgui API in many ways.

Using TGUI for custom HTML popups

This standardizes and simplifies the process of HTML popup creation and DM <-> JS communication.

Makes tgui window API a perfect alternative for old-style browser panels. It will be super useful for @Iamgoofball since he wanted to make a lightweight browser element that plays background music, and this will make his life a lot easier.

It is now possible to create tgui windows with fully inlined JS and CSS, which can be used to make unkillable tgui-based UIs (can't white/blue screen due to network errors). You can split files into JS and CSS, and still serve a single HTML file using this.

Moved sendMessage function to the Byond API object, where it rightfully belongs, and now supports a shorthand form: Byond.sendMessage(type, payload). This shortens and simplifies a lot of code.

Refactored window.update to no longer be public. Now to subscribe to incoming messages, you should use new public APIs: Byond.subscribe(fn) and Byond.subscribeTo(type, fn), and TGUI internally uses these functions as well, which reduces boilerplate in index.js.

Renamed window.__windowId__ to Byond.windowId (old variable is still available for backwards compatibility).

Byond API now supports null id, e.g. Byond.winget(null, 'url'), which makes things like this possible:

// Fetch URL of a currently connected server
Byond.winget(null, 'url').then((serverUrl) => {
  // Connect to this server (opens a new dreamseeker instance)
  Byond.call(serverUrl);
  // Close this client because new instance is connecting
  Byond.command('.quit');
});

Certain polyfills are now statically compiled (commited into git) and are baked into tgui.html. The downside is that HTML went 16 kB -> 50 kB. The upside is that you can now use a relatively modern level API with full support for IE8 when writing plain old html UIs using /datum/tgui_window directly. They are committed into git, because polyfills will never need to be updated (unless of course we randomly decide to get rid of ie8.js and html5shiv.js).
Breaking Changes

No breaking changes. This should be tested for regressions. Upgrading is simple if you're on a relatively up-to-date branch - copy paste all affected tgui files and you're good.

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[95db2c6bfc...](https://github.com/pariahstation/Pariah-Station/commit/95db2c6bfc84871f2fa51eeef253f681dc46a632)
#### Sunday 2022-05-08 01:52:11 by Kapu1178

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301) (#696)

About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [ponapalt/yaya-shiori](https://github.com/ponapalt/yaya-shiori)@[cfed02ec42...](https://github.com/ponapalt/yaya-shiori/commit/cfed02ec4204f2c944ae5896637a7cd4538aeb84)
#### Sunday 2022-05-08 02:30:40 by steve02081504

Revert about MoveFile

This reverts commit 45ac23ebe3f9e046b308be133c80c73487a13684 and fc4174d225256b6e2e186e26b039777e3980b643.

Consider adding this change to next release if you think it's appropriate, as in theory it doesn't have much of an impact
:a: Sorry for doing the stupid thing of writing code without thinking first

---
## [cdcline/demo-website](https://github.com/cdcline/demo-website)@[a454ad4a5f...](https://github.com/cdcline/demo-website/commit/a454ad4a5f999c811d5c51744754175a5d3f4cbb)
#### Sunday 2022-05-08 02:37:15 by Chris Cline

Cleanup footer and Page floating

The Page would grow to a max size, but was justified to the left.

This makes it awkward in large screens because it feels like a lot
of unused pixels they paid for.

So we'll float the page in the center of the background, which gives
a nice illusion of using more of the page than you actually are.

The Footer wasn't aligned correctly because the text was different
sizes and it's difficult to get a correct float with 3 items of
very different sizes.

So we hack in a right/left aligned style & do some fancy media
tags to handle the ugly layout at low widths

Definatly a hack for just this case but also looks good and this
is the demo so yeah, gonna go with it.

Also cleans up some bad spacing.

Also does minor cleanup
 * Fixes some invalid spacing

---
## [NOUIY/aws-cdk](https://github.com/NOUIY/aws-cdk)@[c071367def...](https://github.com/NOUIY/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Sunday 2022-05-08 03:59:50 by Kaizen Conroy

feat(glue): support partition index on tables (#17998)

This PR adds support for creating partition indexes on tables via custom resources.
It offers two different ways to create indexes:

```ts
// via table definition
const table = new glue.Table(this, 'Table', {
  database,
  bucket,
  tableName: 'table',
  columns,
  partitionKeys,
  partitionIndexes: [{
    indexName: 'my-index',
    keyNames: ['month'],
  }],
  dataFormat: glue.DataFormat.CSV,
});
```

```ts
// or as a function
table.AddPartitionIndex([{
  indexName: 'my-other-index',
  keyNames: ['month', 'year'],
});
```

I also refactored the format of some tests, which is what accounts for the large diff in `test.table.ts`. 

Motivation: 
Creating partition indexes on a table is something you can do via the console, but is not an exposed property in cloudformation. In this case, I think it makes sense to support this feature via custom resources as it will significantly reduce the customer pain of either provisioning a custom resource with correct permissions or manually going into the console after resource creation. Supporting this feature allows for synth-time checks and dependency chaining for multiple indexes (reason detailed in the FAQ) which removes a rather sharp edge for users provisioning custom resource indexes themselves.

FAQ:

Why do we need to chain dependencies between different Partition Index Custom Resources? 
  - Because Glue only allows 1 index to be created or deleted simultaneously per table. Without dependencies the resources will try to create partition indexes simultaneously and the second sdk call with be dropped.

Why is it called `partitionIndexes`? Is that really how you pluralize index?
  - [Yesish](https://www.nasdaq.com/articles/indexes-or-indices-whats-the-deal-2016-05-12). If you hate it it can be `partitionIndices`.

Why is `keyNames` of type `string[]` and not `Column[]`? `PartitionKey` is of type `Column[]` and partition indexes must be a subset of partition keys...
  - This could be a debate. But my argument is that the pattern I see for defining a Table is to define partition keys inline and not declare them each as variables. It would be pretty clunky from a UX perspective:
    ```ts
    const key1 = { name: 'mykey', type: glue.Schema.STRING };
    const key2 = { name: 'mykey2', type: glue.Schema.STRING };
    const key3 = { name: 'mykey3', type: glue.Schema.STRING };
    new glue.Table(this, 'table', {
      database,
      bucket,
      tableName: 'table',
      columns,
      partitionKeys: [key1, key2, key3],
      partitionIndexes: [key1, key2],
      dataFormat: glue.DataFormat.CSV,
    });
    ```

Why are there 2 different checks for having > 3 partition indexes?
  - It's possible someone decides to define 3 indexes in the definition and then try to add another with `table.addPartitionIndex()`. This would be a nasty deploy time error, its better if it is synth time. It's also possible someone decides to define 4 indexes in the definition. It's better to fast-fail here before we create 3 custom resources.

What if I deploy a table, manually add 3 partition indexes, and then try to call `table.addPartitionIndex()` and update the stack? Will that still be a synth time failure?
  - Sorry, no. 

Why do we need to generate names?
  - We don't. I just thought it would be helpful.

Why is `grantToUnderlyingResources` public?
  - I thought it would be helpful. Some permissions need to be added to the table, the database, and the catalog.

Closes #17589.

----

*By submitting this pull request, I confirm that my contribution is made under the terms of the Apache-2.0 license*

---
## [mvaisakh/oneplus7](https://github.com/mvaisakh/oneplus7)@[e267660b57...](https://github.com/mvaisakh/oneplus7/commit/e267660b57166ebf1758c28fb789a091ffa8b96f)
#### Sunday 2022-05-08 05:22:06 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [ametech-solutions/ametech-solutions.github.io](https://github.com/ametech-solutions/ametech-solutions.github.io)@[0b5d35fdee...](https://github.com/ametech-solutions/ametech-solutions.github.io/commit/0b5d35fdeebf489a094f07d5549e559cda69a405)
#### Sunday 2022-05-08 05:42:29 by Justin Russell

fuck you callout button  with :hover. i won, you are only making this take longer.

---
## [neirusalwa/GShade-Presets](https://github.com/neirusalwa/GShade-Presets)@[dcdb3bb7d2...](https://github.com/neirusalwa/GShade-Presets/commit/dcdb3bb7d29f1d2a27d5a64c853fe95f2f4d44df)
#### Sunday 2022-05-08 06:19:45 by ellie t

MagicBloom.fx flicker bug fix

In some extreme light conditions, mostly at night with a flickering light source nearby lighting up multiple differently colored moving surfaces ie. light reflections lighting up a character (mostly when close up but can happen from further away), the bloom adaptation from MagicBloom.fx will go haywire due to the other settings being pretty aggressive and it'll start making the screen flicker anywhere from "quite a lot" to "a LOT and violently" (pure white screen to very dark and so on).   

Restoring that value to a more sensible value like the default 0.100 instead of the current 1.000 completely fixes that issue for no visible difference since this only affects the speed at which it changes not the change itself.  

The whole preset being taxing already due to being made for screenshots mostly, I don't see a reason for it to require instantaneous transitions for its effects since your framerate will be heavily cut anyways on most systems.

---
## [fwilhe-containers/podman](https://github.com/fwilhe-containers/podman)@[e74717f348...](https://github.com/fwilhe-containers/podman/commit/e74717f348c2768b87cad7dd6997c42dc85fc50a)
#### Sunday 2022-05-08 07:16:34 by Ed Santiago

Treadmill script: revamp

Major revamp: instead of stacking a vendor commit on top of
the treadmill changes, do it the other way around: vendor,
then apply treadmill diffs.

Reason: the build-all-new-commits test. Sigh. It fails in the
common case where our treadmill changes include a new struct
element in cmd/podman/images/build.go

Why this is good: well, superficially, it's more intuitive.

Why this is horrible: omg the rebasing games are a nightmare.
When the vendor commit is on top (HEAD), it's ultra-trivial
to drop it, rebase the treadmill changes on main, then add
a new vendor-buildah commit on top. As you can see from the
diffs in this PR, treadmill-as-HEAD introduces all sorts
of complex dance steps in which things can go catastrophically
wrong and you can lose all your treadmill patches. I try very
hard to prevent this, and to offer hints if there's a problem,
and heck in the worst case it's still git so it's still possible
to find lost commits... but it's still much riskier than the
old way.

Alternative I considered: using sed magic to disable the
build-all-new-commits test. So tempting... but that would
also disable the bloat check.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [Atom-X-Devs/android_kernel_qcom_sdm660](https://github.com/Atom-X-Devs/android_kernel_qcom_sdm660)@[38b0bd0f25...](https://github.com/Atom-X-Devs/android_kernel_qcom_sdm660/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Sunday 2022-05-08 07:45:41 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [wanted2/wanted2.github.io](https://github.com/wanted2/wanted2.github.io)@[839f9f8769...](https://github.com/wanted2/wanted2.github.io/commit/839f9f876989576993ef98c6e60be14df0b5b496)
#### Sunday 2022-05-08 09:09:23 by wanted2

[1;36m"As you walk in God's divine wisdom, you will surely begin to see a greater measure of victory and good success in your life."[1;m
		[1;35m--Joseph Prince[1;m[0m

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7bac52fa68...](https://github.com/mrakgr/The-Spiral-Language/commit/7bac52fa68ad83ec8de0fb5dad4b19592dabf5f1)
#### Sunday 2022-05-08 11:17:35 by Marko Grdinić

"10am. Rough night. I went to bed at 2am and had trouble falling asleep. I became obessed with booleaning on curved surfaces. Let me do a bit more on that end.

Before than, let me watch the video by Josh again.

https://youtu.be/qB1eg3ef5vs
Why Your Shading Is Broken (and how to fix it!)

https://youtu.be/qB1eg3ef5vs?t=148

Ah, right. The boolean itself would not make it non-planar, but the bevel would!

10:20am. Focus me. Let me find my peace in booleaning curved surfaces.

11:55am. This is how long it took me to cut in a dozen and a half squares and circles into curved surfaces, clean them up and bevel them. Let me try it in Moi.

I'll just try cutting in a box into a sphere and observing what kind of output comes out.

1:05pm. I am getting filtered massively by 3d here. I spent all this time practicing boolean cleanups on curved surfaces.

This was the first time I tried out Moi 3d's exports. I imported a sphere that had a box cut into it, and to my surprise it has perfect shading!

Meanwhile my own thing is trash and it took 10-100x to create because of all the cleanup.

That other object I was practicing carving into and cleaning up. It is full of distortion when I put it through the striped matcap. It is absolute trash!

It is broken. I really made up my mind to use Hopscutter, but the method is so broken that unless the surface is perfectly flat, I have an enormous amount of cleanup work waiting for me. I even tried doing the subdiv style, but as expected, putting loops everywhere tends to distort the geometry. Working with subdiv is like walking a tightrope. Everything you do affects everything else.

Both the box modeling appoeach with booleans and bevel, and subdiv are just poor trickery.

1:05pm. Yes, I could put in the effort and do the rig using my current skills. If I applied myself, I could definitely do it within a day. But just what is the point in using such obviously broken methods to squeeze out a result? It is not like I am getting paid to make this prop in Blender. Finishing the project, but doing it poorly is no better than not finishing it at all!

1:10pm. I want to get a sense of freedom from art, I do not want to feel like I am doing janitorial work in C.

Blender is out of the running for me for modeling.

I am going to give Zbrush hard surface sculpting a serious try. If I really can't do it there, I'll hack everything out in Moi.

I did not think Moi would have such good shading results. It is really humbling.

1:15pm. Let me get breakfast and then I am going to dedicate myself to HS in Zbrush for a while."

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[228643cea9...](https://github.com/treckstar/yolo-octo-hipster/commit/228643cea929a7d6dbe82e0d11676449e3826ccf)
#### Sunday 2022-05-08 13:22:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [rluetzner/schafe-sind-bessere-rasenmaeher](https://github.com/rluetzner/schafe-sind-bessere-rasenmaeher)@[08fcd00e6a...](https://github.com/rluetzner/schafe-sind-bessere-rasenmaeher/commit/08fcd00e6a932f261922db3f5b1e6e973ca7648e)
#### Sunday 2022-05-08 14:33:00 by Robert Lützner

About: Update premise

I can't promise to write daily. It would be a great habit to have, but
in reality I find it very stressful to force myself to write.

Most often the free time I get ends up way late in the evening after a
hard day of work and only a semi-relaxing evening as a parent. A lot of
times I honestly just want to empty my brain with TV, reading or other
non-productive stuff. And that's totally fine.

Being creative takes time and I accept that right now I just can't find
the time to do so very often.

---
## [bustarhymes69/TourGuide](https://github.com/bustarhymes69/TourGuide)@[54adb80bd1...](https://github.com/bustarhymes69/TourGuide/commit/54adb80bd100c4da91d793641c1d9382d70cffb7)
#### Sunday 2022-05-08 14:36:03 by Aaron McGuire

Merge pull request #43 from Loathing-Associates-Scripting-Society/removeUsedOptions

okay i am pushing a new release (finally). i am pushing version to 2.0.0 because we've added a shitload of changes since the last version push. this version includes:

- fixes for several option availability glitches in grey you
- a tile for the unbreakable umbrella
- a new option that lets you be more facestabby w/ bowling ball

specifically, if you run `set tourGuideBowlingBallSupernag=true;` in the CLI, there will be an alert that floats on top of tourguide reminding you that your bowling ball is un-thrown until you throw it. it will not happen unless you set that option though, so most users will not see it.

happy speedrunning folks!

---
## [lord-denning/Huberman-Lab-Podcast-Transcripts](https://github.com/lord-denning/Huberman-Lab-Podcast-Transcripts)@[30259614a4...](https://github.com/lord-denning/Huberman-Lab-Podcast-Transcripts/commit/30259614a4170a521712eda0cf2c3b4b483f4897)
#### Sunday 2022-05-08 14:41:53 by lord-denning

Create 51. Science of Social Bonding in Family, Friendship & Romantic Love.md

---
## [SuperHerp/nBit_Calc](https://github.com/SuperHerp/nBit_Calc)@[adafedbb10...](https://github.com/SuperHerp/nBit_Calc/commit/adafedbb10cbd4da6a003df147699a9c371399b7)
#### Sunday 2022-05-08 15:28:07 by Simon K

fucking finally holy fucking shit division fucking  S U C K S  ASSSSSSSSSSSSSSSSSSSSSSSSSSSSS

---
## [dreamingskey/dreamingskey](https://github.com/dreamingskey/dreamingskey)@[b3c549b456...](https://github.com/dreamingskey/dreamingskey/commit/b3c549b456db8ae6f461f203b6a01e0071cde770)
#### Sunday 2022-05-08 16:42:52 by dreamingskey

Humanitys frames 

Spiritual growths lands history of so lands and ansestrys a app of the growth of meaning a simple man can be edgucated in farms crops agricultural the way of technologys 
Cultures bring to light media opssessions our possibilty in behavior that may not of been true but created by our weak will to exsept  worlds sin space between ourselves..in our selfritousness separates us in definitions. 
sciences energetic quests and mechanics ingineering to inhance lifes thrills and out constructed the other engineers an art of it's own part of the class of creativity the 
Animals gene pools medications medical mental breaks and conditions paths of our own negligence but the etempt to grab meaning in the acts of selfritrousness what it is mental and medical advances that are but ideas all is theory s but the contousness of god  keeps us  all in relation.  And nobody out of the Loop creativity and ideas of the wielding of patterns and thoughts of Heart keeps our kids with knowing dreams are a blessing and knowing Of right from wrong

---
## [itswhom/curriculum](https://github.com/itswhom/curriculum)@[9c740aacfa...](https://github.com/itswhom/curriculum/commit/9c740aacfa82b3abb39345c2f6fe042c271ca711)
#### Sunday 2022-05-08 17:15:37 by BMT-z

Add section for warnings about branch diversions

From personal experience and what I've seen in the git-help channel it seems like a few people are struggling with the issue of branch diversion, I'm still doing the html foundations and didn't realize making changes to my readme file via GitHub would cause the branch diversion issue, I think in git basics it should state that making any changes to your files via GitHub can cause issues and if you want to change even the readme file it's best to do it via a commit and push, I'm aware this is covered later on but i still believe making this a note in the git basics section would help a lot of users from running into this issue.

---
## [sjokkateer/laminas-di](https://github.com/sjokkateer/laminas-di)@[7345788344...](https://github.com/sjokkateer/laminas-di/commit/73457883443bce8d46ea259b50ae29a45b577ca5)
#### Sunday 2022-05-08 17:16:56 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[26b317a6e6...](https://github.com/mrakgr/The-Spiral-Language/commit/26b317a6e676330bd4b86ac095fc619fb8ef1af4)
#### Sunday 2022-05-08 17:35:36 by Marko Grdinić

"2pm. Done with breakfast. Let me chill a little. Shit like this just happens. It is in my nature to focus on a particular problem until I deal with it.

The subdiv and bevel styles are obviously wrong to me at this point. Moi might not be obviously right, but it is not obviously wrong.

Sculpting for hard surfaces is something I am going to have to just try.

2:45pm. Now I have a sphere and I am messing with filleting the edges of the cut in box. For the outer rim, masked it out, inverted it and then I can just use the polish deform to fillet it. But I am not really happy with the result. It ends up feeling bloated.

https://youtu.be/jkIf1nNzDKs?t=10
RETOPOLOGY tutorial for HARD SURFACE in Blender

Even more tutorials, let me watch them.

2:55pm. No, this is not the answer. Let me try the hPolish brush.

https://youtu.be/zxc8MvKTqus
Organic/Subd Hard Surface Modeling in Blender (A Brief Overview)

How did he manage this?

https://youtu.be/zxc8MvKTqus?t=548
> I actually didn't even use a bevel modifier. I used the bevel shader.

This is interesting. There is a bevel shader? Is that like the round edge shader for V-Ray?

It is not exactly a surprise that he is not using the bevel mod. It would break everything.

https://youtu.be/zxc8MvKTqus?t=558

Is that in Blender? Yep. Never saw it before.

3:25pm. There must be something wrong with me right now. Remember that course by Cane Towsend. How about I go through the initial part of it.

Right now I am in a state of complete perplexity. I do not even know how to bevel the edges for the cut out properly.

3:55pm. Now I am really focusing on following along what Cane is doing so far so good. Eventually I'll get to the edge work. The part where he explains the tools is not too hard. But I did not have the motivation to follow along last time and it all flew from memory. I only recall what I should be doing, but not how. I know he used the flatten brushes to get the edges.

That seems simple enough, but when I tried it on the circle I could not get it to work for some reason.

4:20pm. This is making me confused. Why is the mask pen brush not working all of a sudden. What did I do?

4:35pm. I don't know. What is happening that the mask is working in reverse mode. I need to switch to the eraser to get it to work normally. Maybe I toggled some setting by accident, but I do not know what.

https://youtu.be/vmCGZk7z0is
AskZBrush: “Why is my Mask Pen brush not masking fully opaque?”

Let me watch this.

4:45pm. Yeah, the pen is inverted. Forge tthis, let me move on. I set the last 2 parts of the course by some other guy to download.

5pm. Let me backtrack a little. How did he max out the mask intensity? By setting the focal shift to -100. Ok.

6pm. Had to take a break. I think I get how he does his thing now. The only thing I do not get exactly is how to do boolean slices without necessarily duplicating the mesh, and doing an intersection + a difference with the cutter.

https://www.reddit.com/r/ZBrush/comments/akgn6g/beginner_question_how_do_you_give_smooth_shading/

It turns Zbrush does not have smooth shading. It instead opts to get that using large poly quantity.

I tried using the Zremesher on the object that I've done, but just like last time it erodes the edges. Unless I want to carry around 100k poly objects even into Clarrise or Blender, I should do my work in Moi.

If the work involves cutting into curved surfaces even a little, I either have to do it in Moi or Zbrush. There is no way around it.

Now, the last part of that course I am downloading will be done in 15m.

Let me rant until then. What I am experiencing here is probably the same as when I did the compilers course in 2015. It took me as long as a week to muster the nerve to even begin work on the code generator for the Cool compiler.

Right now I am in that state. I know a lot of moves, but I am having trouble stepping up to the larger scale than I am used to. So far I've done onyl a simple primitive. The monitor was pretty simple.

Nobody would say that the rig I am attempting is complex, but it is a lot more complex than anything I've attempted previously.

6:05pm. Just a bit more. Just a bit more and I will work up the nerve to do it. If needed I will spend the time time in bed until I find the will.

Now...3m left. Let me just check out the HS techniques from this guy and maybe that will help me come to a conclussion.

6:10pm. Let me take a look at the course.

Udemy - Zbrush Hard Surface Sculpting for All Levels! by Sean Flower

This is the one I got.

> Please try to watch the same tutorial more than once.

Yeah, it is no wonder I've gone back to Cane's course.

6:25pm. Let me just dedicate myself to the Zbrush course. I want more knowledge so I can come to a correct conclussion which approach is best. I'll only feel inner peace once I know the basics properly. This urge to pursue knowledge will go away when I have enough. There is no need to force the matter.

Oh damn it is 10h. I thought it might be smaller since the other course was only 5 despite being twice as big in hard drive space.

This will take a while. I won't take it against me if I take a few days to cover it. I will keep persevering.

7:10pm. Left for lunch. Let me finish the video I am watching and I will call it a day.

This course will go into polygroups, while that radio course barely even touched upon them. It seems that unlike for Blender, Zbrush really needs some pirating in order to learn it. Courses like this one are indispensable.

7:15pm. He is really padding it with the hotkeys. Is the space bar that important? Maybe it is given that the brush stars in the corner instead of the center.

7:25pm. Yeah, the course is most likely 10h long just as it says on the tin. I'll have to speedwatch it before making a decision.

But what is there to decide. I already know that while I do need topology good enough for smooth shading, I do not need it to be sub-divisible. Moi gives me that as well as the ability to boolean on curved surfaces. That means I can just use Blender for blocking out organic shapes and move to Moi when I need to carve them.

Zbrush should not enter into the picture here. But I want it. I want to get just a bit better at this even if I turn my back on it. Maybe later I'll turn my back on 3d modeling as well. For all I know, I could spend the entirety of 2023 doing 2d drawing.

2022 is the time to learn 3d.

7:30pm. This is the way to live. I want to take the time to properly refine my technique. If I can do that, then doing art could be a fun hobby rather than a drudge work."

---
## [Fargowilta/FargowiltasSouls](https://github.com/Fargowilta/FargowiltasSouls)@[df7c27eb16...](https://github.com/Fargowilta/FargowiltasSouls/commit/df7c27eb16e2e5d05bcab70599aec5d1e99d2f06)
#### Sunday 2022-05-08 17:53:01 by terrynmuse

sibling pets are master drop now instead of emode nohit
devi pet talks because fuck you i can do that (has toggle)

---
## [RandomGamer123/tgstation](https://github.com/RandomGamer123/tgstation)@[a137c15a79...](https://github.com/RandomGamer123/tgstation/commit/a137c15a790bc8242a1ccd70bb6570d0278833c0)
#### Sunday 2022-05-08 18:21:01 by Vladin Heir

Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[351afe260b...](https://github.com/jlsnow301/tgstation/commit/351afe260b42764641a07385df5f7e24b840f631)
#### Sunday 2022-05-08 18:40:05 by san7890

Fixes Mapping Icons For Bodylimbs (Don't Get A Shock!) (#65899)

* Fixes Mapping Icons For Bodylimbs (Don't Get A Shock!)

Hey there,

I implore you look at this photograph right here:

Ugly stupid base broken dumb /obj instead of the actual sprite fucking garbage idiotic purple-white square damn it i hate it so much fuck fuck fuck fuck let's fix it before the fire under my seat gets worse argh

Anyways, I checked with Kapu and did a bit of testing, and I managed to figure out a way to get the best of both the mapping world and the in-game world. Don't believe me? Check these out:

* addressses review

things still work

* kills female moth chests

---
## [stonepillars/goon-flock](https://github.com/stonepillars/goon-flock)@[bdad398f9e...](https://github.com/stonepillars/goon-flock/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Sunday 2022-05-08 19:10:04 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [MichaelInsalaco/michaelinsalaco.github.io](https://github.com/MichaelInsalaco/michaelinsalaco.github.io)@[948acb3382...](https://github.com/MichaelInsalaco/michaelinsalaco.github.io/commit/948acb33827c9adeb13672cd68c102be89c5ff19)
#### Sunday 2022-05-08 23:27:18 by Bryan Guadagnini

Rev. 1

General things:

I actually like this font.  Let's keep it.

You're playing with mock-up to make less blocky is fine.  Let's keep it.

The drop shadows on the copy boxes are okay, but I don't like the white bands added.  Can we take those off?

Tighten the spacing (leading) between stacked lines of headlines. Then make consistent across all headlines.

I think the regular copy needs to be 1 point larger.  Also add a little more spacing (leading) between stacked lines of regular copy.  Then make consistent across all copy lines.

Adjust black copy boxes as needed to accommodate changes above.

Detail changes by section:

TOP NAV BAR:

I don't want the yellow strip at the top.  Just black.  But I would like to keep the little yellow arrow that indicates current section.  Can that just float in the black a little closer to the nav word?

Push my name a little further to right and have it stay a little larger when screen collapses.

Font size for nav items seems too small.  People who can afford me are older farts like myself ... who have trouble with tiny fonts.

HOME PAGE SECTION:

Recrop photo more pulled back like mock-up.

I like the image blurring you did in PS.

Lower the copy black copy box so it covers more road and less landscape, also competes with header content less.

SERVICES SECTION:

See General comments that apply.

Change the line of copy under "I do" headline to:  "Strategy, concepts, copywriting and direction for trade and consumer messaging."

PROCESS SECTION:

I'd like the black copy box to be higher and to the left ... and it could be wider and less tall if need be.  The goal is to not cover the sketch of my own website idea.  It's sorta like the artist making an appearance in his own painting ... while at the same time illustrating the point of how my ideas start on paper.

BRANDS SECTION:

Change the headline to: "A sampling of the brands I've worked with ... in no particular order:"

Change "Thiesen Dueker Group" to "Thiesen Dueker Financial Consulting Group"

Add "Universal Coatings"

Add "Panoche Creek"

DIRECT PITCH SECTION:

When the text gets bigger it might be okay floating over the table.  But I'm not loving the black drop shadow needed to lift the reverse text off the table ... and I could like that less when the text gets bigger.  So we can look, but I might want the black box to come back.

Indent the first example "When a Division 1 ...." as on mock-up.

The READ MORE button design is fine but feel unnecessarily small.  (Refer to old fart comment above.)

DIRECT PITCH FULL-STORE POP-UP:

Same text size and spacing revisions as rest of site.

Let's go with a darker shade of gray for the background and I think that'll be good enough.  No need for a texture.  Flat is where it's at.

Make the margins much larger so you're not reading long lines of type left to right.

Indent the examples copy (so only the headline, intro paragraph, and closing paragraph are flush left.)

CONTACT SECTION:

I think this photo would really benefit from the same blur treatment on the greenery in the background.

Keep the headline the same but change the text under that to a much more succinct:  "How can I help your business get the right message out there?"

Change the email to:  insalacomji@comcast.net

However, I think I would like to get me@MichaelJInsalaco.com and I'd dig your help doing that.  Then I have to figure out how to get it set up on my phone and laptop so I don't always have to go through the browser to get to it.  Easy for you.  Intimidating to me.

By the way, what happens when you click on the email address?  Does it open a new email pre-populated with my address?

MY CAREER SECTION:

Okay as is beside the text sizes.

MY CAREER POP-UP SECTION:

Same changes as the DIRECT PITCH pop-up section.

"Contact" needs to be a button to be seen.  What happens when you click that?  Does it jump back to the home page Contact section?

---
## [SiberianSpaceBat/sunset-wasteland](https://github.com/SiberianSpaceBat/sunset-wasteland)@[28d5794423...](https://github.com/SiberianSpaceBat/sunset-wasteland/commit/28d57944238656c75d3283c37c7a5453ce10e640)
#### Sunday 2022-05-08 23:56:27 by Shane Merrol

disables fermichem for synthtissue

Fuck fermichem, all my homies hate fermichem

Jokes aside, you need it for organ repair surgery, and it's a QoL change for FoA

---

